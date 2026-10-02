#!/usr/bin/env python3
"""Local-first web app for family and small-business finances.

Only Python's standard library is required. The HTTP server binds to loopback by
default; it deliberately has no accounts or remote access.
"""

import argparse
import calendar
from contextlib import closing
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from functools import partial
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
from pathlib import Path
import re
import sqlite3
from urllib.parse import parse_qs, urlsplit


DEFAULT_DB = Path.home() / ".morningstar" / "masroofi.sqlite3"
WEB_DIR = Path(__file__).resolve().parent / "web"
MAX_AMOUNT_CENTS = 999_999_999_999
VALID_CURRENCIES = {"USD", "EUR", "GBP", "CAD", "AUD", "MXN"}


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def connect_db(path):
    db = sqlite3.connect(path, timeout=5)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("PRAGMA busy_timeout = 5000")
    return db


def init_db(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(connect_db(path)) as db, db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS workspaces (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                kind TEXT NOT NULL CHECK (kind IN ('family', 'business')),
                currency TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS recurrences (
                id INTEGER PRIMARY KEY,
                workspace_id INTEGER NOT NULL REFERENCES workspaces(id),
                kind TEXT NOT NULL CHECK (kind IN ('expense', 'income')),
                category TEXT NOT NULL,
                amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
                party TEXT NOT NULL DEFAULT '',
                note TEXT NOT NULL DEFAULT '',
                day INTEGER NOT NULL CHECK (day BETWEEN 1 AND 31),
                start_month TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                workspace_id INTEGER NOT NULL REFERENCES workspaces(id),
                tx_date TEXT NOT NULL,
                kind TEXT NOT NULL CHECK (kind IN ('expense', 'income')),
                category TEXT NOT NULL,
                amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
                party TEXT NOT NULL DEFAULT '',
                note TEXT NOT NULL DEFAULT '',
                recurrence_id INTEGER REFERENCES recurrences(id) ON DELETE SET NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS transactions_by_month
                ON transactions(workspace_id, tx_date);
            CREATE TABLE IF NOT EXISTS occurrences (
                recurrence_id INTEGER NOT NULL REFERENCES recurrences(id) ON DELETE CASCADE,
                month TEXT NOT NULL,
                transaction_id INTEGER REFERENCES transactions(id) ON DELETE SET NULL,
                PRIMARY KEY (recurrence_id, month)
            );
            CREATE TABLE IF NOT EXISTS budgets (
                workspace_id INTEGER NOT NULL REFERENCES workspaces(id),
                month TEXT NOT NULL,
                category TEXT NOT NULL,
                amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
                PRIMARY KEY (workspace_id, month, category)
            );
        """)


def required_text(data, key, *, limit=100, allow_empty=False):
    value = data.get(key, "")
    if not isinstance(value, str):
        raise ApiError(400, f"{key} must be text")
    value = value.strip()
    if len(value) > limit or (not allow_empty and not value):
        raise ApiError(400, f"{key} must contain 1 to {limit} characters")
    return value


def valid_month(value):
    if (not isinstance(value, str) or
            not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", value) or
            value.startswith("0000")):
        raise ApiError(400, "month must be YYYY-MM")
    return value


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ApiError(400, "date must be YYYY-MM-DD")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ApiError(400, "date is invalid") from exc
    return value


def amount_cents(value, *, allow_zero=False):
    if not isinstance(value, (str, int, float)) or isinstance(value, bool):
        raise ApiError(400, "amount must be a number")
    try:
        number = Decimal(str(value))
        cents = number * 100
        if not number.is_finite() or cents != cents.to_integral_value():
            raise ApiError(400, "amount must have at most two decimal places")
        cents = int(cents)
    except (InvalidOperation, ValueError, OverflowError) as exc:
        raise ApiError(400, "amount is invalid") from exc
    if cents < 0 or (cents == 0 and not allow_zero) or cents > MAX_AMOUNT_CENTS:
        raise ApiError(400, "amount is outside the allowed range")
    return cents


def positive_id(value, label):
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise ApiError(400, f"{label} must be a positive integer") from exc
    if result < 1:
        raise ApiError(400, f"{label} must be a positive integer")
    return result


def workspace(db, workspace_id):
    row = db.execute("SELECT * FROM workspaces WHERE id = ?", (workspace_id,)).fetchone()
    if row is None:
        raise ApiError(404, "workspace not found")
    return dict(row)


def transaction_fields(data):
    kind = data.get("kind")
    if kind not in ("expense", "income"):
        raise ApiError(400, "kind must be expense or income")
    return {
        "tx_date": valid_date(data.get("date")),
        "kind": kind,
        "category": required_text(data, "category"),
        "amount_cents": amount_cents(data.get("amount")),
        "party": required_text(data, "party", allow_empty=True),
        "note": required_text(data, "note", limit=500, allow_empty=True),
    }


def month_transactions(db, workspace_id, month):
    return [dict(row) for row in db.execute("""
        SELECT id, tx_date AS date, kind, category, amount_cents, party, note,
               recurrence_id
        FROM transactions WHERE workspace_id = ? AND tx_date >= ? AND tx_date < ?
        ORDER BY tx_date DESC, id DESC
    """, (workspace_id, month + "-01", month + "-32"))]


def materialize_recurrences(db, workspace_id, month):
    today = date.today()
    if month > today.strftime("%Y-%m"):
        return
    year, number = map(int, month.split("-"))
    last_day = calendar.monthrange(year, number)[1]
    rules = db.execute("SELECT * FROM recurrences WHERE workspace_id = ? AND start_month <= ?",
                       (workspace_id, month)).fetchall()
    for rule in rules:
        due = date(year, number, min(rule["day"], last_day))
        if due > today:
            continue
        inserted = db.execute(
            "INSERT OR IGNORE INTO occurrences(recurrence_id, month) VALUES (?, ?)",
            (rule["id"], month),
        )
        if not inserted.rowcount:
            continue
        transaction = db.execute("""
            INSERT INTO transactions
                (workspace_id, tx_date, kind, category, amount_cents, party, note, recurrence_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (workspace_id, due.isoformat(), rule["kind"], rule["category"],
              rule["amount_cents"], rule["party"], rule["note"], rule["id"]))
        db.execute("""
            UPDATE occurrences SET transaction_id = ? WHERE recurrence_id = ? AND month = ?
        """, (transaction.lastrowid, rule["id"], month))


def dashboard(db, workspace_id, month):
    current_workspace = workspace(db, workspace_id)
    materialize_recurrences(db, workspace_id, month)
    transactions = month_transactions(db, workspace_id, month)
    budgets = [dict(row) for row in db.execute("""
        SELECT category, amount_cents FROM budgets
        WHERE workspace_id = ? AND month = ? ORDER BY category COLLATE NOCASE
    """, (workspace_id, month))]
    recurrences = [dict(row) for row in db.execute("""
        SELECT id, kind, category, amount_cents, party, note, day, start_month
        FROM recurrences WHERE workspace_id = ? ORDER BY id DESC
    """, (workspace_id,))]
    spent_by_category = {}
    income = expense = 0
    for row in transactions:
        if row["kind"] == "expense":
            expense += row["amount_cents"]
            category = row["category"]
            spent_by_category[category] = spent_by_category.get(category, 0) + row["amount_cents"]
        else:
            income += row["amount_cents"]
    for row in budgets:
        row["spent_cents"] = spent_by_category.get(row["category"], 0)
    return {
        "workspace": current_workspace,
        "month": month,
        "income_cents": income,
        "expense_cents": expense,
        "balance_cents": income - expense,
        "spent_by_category": spent_by_category,
        "transactions": transactions,
        "budgets": budgets,
        "recurrences": recurrences,
    }


def csv_safe(value):
    text = str(value)
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


class AppHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, db_path, **kwargs):
        self.db_path = db_path
        super().__init__(*args, **kwargs)

    def _send(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status, value):
        self._send(status, json.dumps(value, ensure_ascii=False).encode("utf-8"),
                   "application/json; charset=utf-8")

    def _committed_json(self, db, status, value):
        db.commit()
        self._json(status, value)

    def _payload(self):
        if not self.headers.get("Content-Type", "").startswith("application/json"):
            raise ApiError(415, "Content-Type must be application/json")
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError as exc:
            raise ApiError(400, "invalid Content-Length") from exc
        if not 0 < length <= 65_536:
            raise ApiError(413, "JSON body must be 1 to 65536 bytes")
        try:
            value = json.loads(self.rfile.read(length))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ApiError(400, "invalid JSON") from exc
        if not isinstance(value, dict):
            raise ApiError(400, "JSON body must be an object")
        return value

    def _query_id(self, query):
        return positive_id(query.get("workspace_id", [None])[0], "workspace_id")

    def _dispatch(self):
        host = self.headers.get("Host", "").split(":")[0].lower()
        if host not in ("127.0.0.1", "localhost"):
            raise ApiError(403, "only localhost access is allowed")
        parsed = urlsplit(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        if self.command == "GET" and path in ("/", "/index.html", "/app.js", "/style.css", "/favicon.svg"):
            file_name = "index.html" if path == "/" else path.lstrip("/")
            content_type = {
                "index.html": "text/html; charset=utf-8",
                "app.js": "text/javascript; charset=utf-8",
                "style.css": "text/css; charset=utf-8",
                "favicon.svg": "image/svg+xml",
            }[file_name]
            self._send(200, (WEB_DIR / file_name).read_bytes(), content_type)
            return
        if self.command == "GET" and path == "/api/health":
            self._json(200, {"status": "ok"})
            return
        with closing(connect_db(self.db_path)) as db, db:
            if self.command == "GET" and path == "/api/workspaces":
                rows = db.execute("SELECT id, name, kind, currency FROM workspaces ORDER BY id")
                self._json(200, {"workspaces": [dict(row) for row in rows]})
            elif self.command == "POST" and path == "/api/workspaces":
                data = self._payload()
                name = required_text(data, "name", limit=80)
                kind = data.get("kind")
                currency = data.get("currency")
                if kind not in ("family", "business"):
                    raise ApiError(400, "kind must be family or business")
                if currency not in VALID_CURRENCIES:
                    raise ApiError(400, "unsupported currency")
                cursor = db.execute("INSERT INTO workspaces(name, kind, currency) VALUES (?, ?, ?)",
                                    (name, kind, currency))
                self._committed_json(db, 201, workspace(db, cursor.lastrowid))
            elif self.command == "GET" and path == "/api/dashboard":
                workspace_id = self._query_id(query)
                month = valid_month(query.get("month", [date.today().strftime("%Y-%m")])[0])
                self._committed_json(db, 200, dashboard(db, workspace_id, month))
            elif self.command == "POST" and path == "/api/transactions":
                data = self._payload()
                workspace_id = positive_id(data.get("workspace_id"), "workspace_id")
                workspace(db, workspace_id)
                fields = transaction_fields(data)
                cursor = db.execute("""
                    INSERT INTO transactions
                        (workspace_id, tx_date, kind, category, amount_cents, party, note)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (workspace_id, *fields.values()))
                self._committed_json(db, 201, {"id": cursor.lastrowid})
            elif match := re.fullmatch(r"/api/transactions/(\d+)", path):
                transaction_id = positive_id(match.group(1), "transaction_id")
                if self.command == "PUT":
                    data = self._payload()
                    workspace_id = positive_id(data.get("workspace_id"), "workspace_id")
                    fields = transaction_fields(data)
                    cursor = db.execute("""
                        UPDATE transactions
                        SET tx_date = ?, kind = ?, category = ?, amount_cents = ?, party = ?, note = ?
                        WHERE id = ? AND workspace_id = ?
                    """, (*fields.values(), transaction_id, workspace_id))
                elif self.command == "DELETE":
                    workspace_id = self._query_id(query)
                    cursor = db.execute("DELETE FROM transactions WHERE id = ? AND workspace_id = ?",
                                        (transaction_id, workspace_id))
                else:
                    raise ApiError(405, "method not allowed")
                if not cursor.rowcount:
                    raise ApiError(404, "transaction not found")
                self._committed_json(db, 200, {"id": transaction_id})
            elif self.command == "PUT" and path == "/api/budgets":
                data = self._payload()
                workspace_id = positive_id(data.get("workspace_id"), "workspace_id")
                workspace(db, workspace_id)
                month = valid_month(data.get("month"))
                category = required_text(data, "category")
                cents = amount_cents(data.get("amount"), allow_zero=True)
                if cents:
                    db.execute("""
                        INSERT INTO budgets(workspace_id, month, category, amount_cents)
                        VALUES (?, ?, ?, ?)
                        ON CONFLICT(workspace_id, month, category)
                        DO UPDATE SET amount_cents = excluded.amount_cents
                    """, (workspace_id, month, category, cents))
                else:
                    db.execute("DELETE FROM budgets WHERE workspace_id = ? AND month = ? AND category = ?",
                               (workspace_id, month, category))
                self._committed_json(db, 200, {"category": category, "amount_cents": cents})
            elif self.command == "POST" and path == "/api/recurrences":
                data = self._payload()
                workspace_id = positive_id(data.get("workspace_id"), "workspace_id")
                workspace(db, workspace_id)
                fields = transaction_fields({**data, "date": date.today().isoformat()})
                day = positive_id(data.get("day"), "day")
                if day > 31:
                    raise ApiError(400, "day must be 1 to 31")
                start_month = valid_month(data.get("start_month"))
                cursor = db.execute("""
                    INSERT INTO recurrences
                        (workspace_id, kind, category, amount_cents, party, note, day, start_month)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (workspace_id, fields["kind"], fields["category"],
                      fields["amount_cents"], fields["party"], fields["note"], day, start_month))
                self._committed_json(db, 201, {"id": cursor.lastrowid})
            elif match := re.fullmatch(r"/api/recurrences/(\d+)", path):
                if self.command != "DELETE":
                    raise ApiError(405, "method not allowed")
                workspace_id = self._query_id(query)
                cursor = db.execute("DELETE FROM recurrences WHERE id = ? AND workspace_id = ?",
                                    (positive_id(match.group(1), "recurrence_id"), workspace_id))
                if not cursor.rowcount:
                    raise ApiError(404, "recurrence not found")
                self._committed_json(db, 200, {"deleted": True})
            elif self.command == "GET" and path == "/api/export":
                workspace_id = self._query_id(query)
                month = valid_month(query.get("month", [None])[0])
                current = dashboard(db, workspace_id, month)
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(["date", "type", "category", "amount", "currency", "person_or_vendor", "note"])
                for row in reversed(current["transactions"]):
                    writer.writerow([
                        row["date"], row["kind"], csv_safe(row["category"]),
                        f"{row['amount_cents'] / 100:.2f}", current["workspace"]["currency"],
                        csv_safe(row["party"]), csv_safe(row["note"]),
                    ])
                db.commit()
                self._send(200, ("\ufeff" + output.getvalue()).encode("utf-8"),
                           "text/csv; charset=utf-8")
            else:
                raise ApiError(404, "route not found")

    def do_GET(self):
        self._serve()

    def do_POST(self):
        self._serve()

    def do_PUT(self):
        self._serve()

    def do_DELETE(self):
        self._serve()

    def _serve(self):
        try:
            self._dispatch()
        except ApiError as exc:
            self._json(exc.status, {"error": exc.message})
        except (OSError, sqlite3.Error) as exc:
            self.log_error("internal error: %s", exc)
            self._json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "internal server error"})


def make_server(db_path, port=8765):
    init_db(db_path)
    return ThreadingHTTPServer(("127.0.0.1", port), partial(AppHandler, db_path=db_path))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Masroofi local web app")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite database path")
    parser.add_argument("--port", type=int, default=8765, help="local port (default: 8765)")
    args = parser.parse_args(argv)
    with make_server(args.db, args.port) as server:
        print(f"Masroofi is running at http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
