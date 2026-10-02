import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "expenses.py"


class ExpenseCliTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.data = self.root / "expenses.json"

    def run_cli(self, *arguments, expected_code=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--data", str(self.data), *arguments],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, expected_code, result.stderr)
        return result

    def test_add_summary_export_and_remove(self):
        self.run_cli("add", "12.50", "طعام", "--date", "2026-10-02", "--note", "غداء")
        self.run_cli("add", "4", "طعام", "--date", "2026-10-03")
        self.run_cli("add", "7.25", "نقل", "--date", "2026-09-30")
        self.assertEqual(len(json.loads(self.data.read_text(encoding="utf-8"))), 3)
        self.assertIn("الإجمالي: 16.50", self.run_cli("summary", "--month", "2026-10").stdout)
        self.assertIn("الإجمالي: 23.75", self.run_cli("summary").stdout)

        exported = self.root / "october.csv"
        self.run_cli("export", str(exported), "--month", "2026-10")
        with exported.open(encoding="utf-8-sig", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertEqual([row["amount"] for row in rows], ["12.50", "4.00"])

        self.run_cli("remove", "1")
        self.assertNotIn("غداء", self.run_cli("list").stdout)
        self.assertIn("الإجمالي: 4.00", self.run_cli("summary", "--month", "2026-10").stdout)

    def test_invalid_amount_does_not_create_data(self):
        self.run_cli("add", "1.234", "طعام", expected_code=2)
        self.run_cli("add", "-2", "طعام", expected_code=2)
        self.run_cli("add", "1e999", "طعام", expected_code=2)
        self.assertFalse(self.data.exists())

    def test_export_cannot_overwrite_data_file(self):
        self.run_cli("add", "3", "طعام", "--date", "2026-10-02")
        original = self.data.read_bytes()
        self.run_cli("export", str(self.data), expected_code=2)
        self.assertEqual(self.data.read_bytes(), original)

    def test_empty_file_and_invalid_month(self):
        self.assertIn("الإجمالي: 0.00", self.run_cli("summary").stdout)
        self.run_cli("list", "--month", "2026-13", expected_code=2)
        self.assertFalse(self.data.exists())


if __name__ == "__main__":
    unittest.main()
