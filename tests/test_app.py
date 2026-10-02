from datetime import date
import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import ProxyHandler, Request, build_opener

from app import make_server


class WebAppTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.server = make_server(Path(self.directory.name) / "app.sqlite3", 0)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.stop_server)
        self.opener = build_opener(ProxyHandler({}))
        self.url = f"http://127.0.0.1:{self.server.server_port}"

    def stop_server(self):
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()

    def request(self, method, path, payload=None, expected=200):
        body = json.dumps(payload).encode() if payload is not None else None
        request = Request(self.url + path, data=body, method=method)
        if body is not None:
            request.add_header("Content-Type", "application/json")
        try:
            response = self.opener.open(request, timeout=5)
        except HTTPError as error:
            response = error
        with response:
            data = response.read()
            self.assertEqual(response.status, expected, data.decode())
            if response.headers.get_content_type() == "application/json":
                return json.loads(data)
            return data.decode("utf-8-sig")

    def workspace(self, name="Home", kind="family", currency="EUR"):
        return self.request("POST", "/api/workspaces", {
            "name": name, "kind": kind, "currency": currency,
        }, 201)["id"]

    def test_monthly_finances_budgets_export_and_workspace_isolation(self):
        self.assertEqual(self.request("GET", "/api/health"), {"status": "ok"})
        family = self.workspace()
        business = self.workspace("Studio", "business", "USD")
        expense = self.request("POST", "/api/transactions", {
            "workspace_id": family, "date": "2026-10-02", "kind": "expense",
            "category": "Groceries", "amount": "12.50", "party": "=shop", "note": "Milk",
        }, 201)["id"]
        self.request("POST", "/api/transactions", {
            "workspace_id": family, "date": "2026-10-03", "kind": "income",
            "category": "Salary", "amount": "100.00", "party": "Employer", "note": "",
        }, 201)
        self.request("PUT", "/api/budgets", {
            "workspace_id": family, "month": "2026-10", "category": "Groceries", "amount": "20.00",
        })
        dashboard = self.request("GET", f"/api/dashboard?workspace_id={family}&month=2026-10")
        self.assertEqual((dashboard["income_cents"], dashboard["expense_cents"], dashboard["balance_cents"]),
                         (10000, 1250, 8750))
        self.assertEqual(dashboard["budgets"][0]["spent_cents"], 1250)
        self.assertEqual(self.request("GET", f"/api/dashboard?workspace_id={business}&month=2026-10")["expense_cents"], 0)
        exported = self.request("GET", f"/api/export?workspace_id={family}&month=2026-10")
        self.assertIn("'=shop", exported)
        self.assertIn("Groceries", exported)

        self.request("PUT", f"/api/transactions/{expense}", {
            "workspace_id": family, "date": "2026-10-02", "kind": "expense",
            "category": "Groceries", "amount": "15", "party": "Shop", "note": "More milk",
        })
        self.assertEqual(self.request("GET", f"/api/dashboard?workspace_id={family}&month=2026-10")["expense_cents"], 1500)
        self.request("DELETE", f"/api/transactions/{expense}?workspace_id={business}", expected=404)
        self.request("DELETE", f"/api/transactions/{expense}?workspace_id={family}")
        self.assertEqual(self.request("GET", f"/api/dashboard?workspace_id={family}&month=2026-10")["expense_cents"], 0)

    def test_recurring_entries_are_idempotent_and_deletion_does_not_regenerate(self):
        work = self.workspace()
        month = date.today().strftime("%Y-%m")
        rule = self.request("POST", "/api/recurrences", {
            "workspace_id": work, "kind": "expense", "category": "Rent",
            "amount": "650.00", "party": "Landlord", "note": "", "day": 1,
            "start_month": month,
        }, 201)["id"]
        path = f"/api/dashboard?workspace_id={work}&month={month}"
        first = self.request("GET", path)
        self.assertEqual(first["expense_cents"], 65000)
        self.assertEqual(len(self.request("GET", path)["transactions"]), 1)
        transaction = first["transactions"][0]["id"]
        self.request("DELETE", f"/api/transactions/{transaction}?workspace_id={work}")
        self.assertEqual(len(self.request("GET", path)["transactions"]), 0)
        self.request("DELETE", f"/api/recurrences/{rule}?workspace_id={work}")
        self.assertEqual(len(self.request("GET", path)["recurrences"]), 0)

    def test_input_validation_and_static_ui(self):
        work = self.workspace()
        self.request("POST", "/api/transactions", {
            "workspace_id": work, "date": "2026-10-02", "kind": "expense",
            "category": "Food", "amount": "1.234", "party": "", "note": "",
        }, 400)
        self.request("GET", f"/api/dashboard?workspace_id={work}&month=2026-13", expected=400)
        self.request("GET", f"/api/dashboard?workspace_id={work}&month=0000-01", expected=400)
        self.request("PUT", "/api/budgets", {
            "workspace_id": work, "month": "2026-10", "category": "Food", "amount": "0",
        })
        self.assertIn("<html lang=\"en\">", self.request("GET", "/"))
        script = self.request("GET", "/app.js")
        self.assertIn("Français", self.request("GET", "/"))
        self.assertIn("'es-ES'", script)


if __name__ == "__main__":
    unittest.main()
