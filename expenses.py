#!/usr/bin/env python3
"""A small, offline expense tracker with no third-party dependencies."""

import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import re
import tempfile


DEFAULT_DATA = Path.home() / ".morningstar" / "expenses.json"


def valid_amount(raw):
    try:
        amount = Decimal(raw)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("المبلغ يجب أن يكون رقمًا") from exc
    if not amount.is_finite() or amount <= 0:
        raise argparse.ArgumentTypeError("أدخل مبلغًا موجبًا بدقتين عشريتين كحد أقصى")
    try:
        if amount != amount.quantize(Decimal("0.01")):
            raise argparse.ArgumentTypeError("أدخل مبلغًا موجبًا بدقتين عشريتين كحد أقصى")
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("المبلغ كبير جدًا") from exc
    return f"{amount:.2f}"


def valid_date(raw):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        raise argparse.ArgumentTypeError("صيغة التاريخ المطلوبة: YYYY-MM-DD")
    try:
        date.fromisoformat(raw)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("تاريخ غير صالح") from exc
    return raw


def valid_month(raw):
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", raw):
        raise argparse.ArgumentTypeError("صيغة الشهر المطلوبة: YYYY-MM")
    return raw


def load_entries(path):
    if not path.exists():
        return []
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"تعذر قراءة ملف البيانات {path}: {exc}") from exc
    if not isinstance(entries, list):
        raise ValueError(f"ملف البيانات {path} لا يحتوي قائمة مصاريف")
    return entries


def save_entries(path, entries):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as output:
            temporary = Path(output.name)
            json.dump(entries, output, ensure_ascii=False, indent=2)
            output.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def selected_entries(entries, month):
    result = (entry for entry in entries if not month or entry["date"].startswith(month + "-"))
    return sorted(result, key=lambda entry: (entry["date"], entry["id"]))


def build_parser():
    parser = argparse.ArgumentParser(description="دفتر مصاريف بسيط يعمل دون اتصال")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="مسار ملف البيانات")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="إضافة مصروف")
    add.add_argument("amount", type=valid_amount, help="المبلغ")
    add.add_argument("category", help="التصنيف، مثل طعام")
    add.add_argument("--note", default="", help="ملاحظة اختيارية")
    add.add_argument("--date", type=valid_date, default=date.today().isoformat(), help="YYYY-MM-DD")

    listing = commands.add_parser("list", help="عرض المصاريف")
    listing.add_argument("--month", type=valid_month, help="YYYY-MM")

    summary = commands.add_parser("summary", help="إجمالي المصاريف حسب التصنيف")
    summary.add_argument("--month", type=valid_month, help="YYYY-MM")

    remove = commands.add_parser("remove", help="حذف مصروف برقم السجل")
    remove.add_argument("id", type=int, help="رقم السجل الظاهر في list")

    export = commands.add_parser("export", help="تصدير المصاريف إلى CSV")
    export.add_argument("file", type=Path, help="مسار ملف CSV")
    export.add_argument("--month", type=valid_month, help="YYYY-MM")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        entries = load_entries(args.data)
        if args.command == "add":
            category = args.category.strip()
            if not category:
                parser.error("التصنيف لا يمكن أن يكون فارغًا")
            next_id = max((entry["id"] for entry in entries), default=0) + 1
            entries.append({
                "id": next_id, "date": args.date, "category": category,
                "amount": args.amount, "note": args.note.strip(),
            })
            save_entries(args.data, entries)
            print(f"أُضيف المصروف رقم {next_id}")
        elif args.command == "remove":
            remaining = [entry for entry in entries if entry["id"] != args.id]
            if len(remaining) == len(entries):
                parser.error(f"لا يوجد مصروف برقم {args.id}")
            save_entries(args.data, remaining)
            print(f"حُذف المصروف رقم {args.id}")
        elif args.command == "list":
            rows = selected_entries(entries, args.month)
            if not rows:
                print("لا توجد مصاريف")
            for entry in rows:
                note = f" — {entry['note']}" if entry["note"] else ""
                print(f"{entry['id']} | {entry['date']} | {entry['category']} | {entry['amount']}{note}")
        elif args.command == "summary":
            totals = {}
            for entry in selected_entries(entries, args.month):
                category = entry["category"]
                totals[category] = totals.get(category, Decimal("0")) + Decimal(entry["amount"])
            for category in sorted(totals):
                print(f"{category}: {totals[category]:.2f}")
            print(f"الإجمالي: {sum(totals.values(), Decimal('0')):.2f}")
        elif args.command == "export":
            if args.file.resolve() == args.data.resolve():
                parser.error("مسار التصدير يجب أن يختلف عن ملف البيانات")
            rows = selected_entries(entries, args.month)
            args.file.parent.mkdir(parents=True, exist_ok=True)
            with args.file.open("w", encoding="utf-8-sig", newline="") as output:
                writer = csv.DictWriter(output, fieldnames=["id", "date", "category", "amount", "note"])
                writer.writeheader()
                writer.writerows(rows)
            print(f"صُدّر {len(rows)} مصروف إلى {args.file}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
