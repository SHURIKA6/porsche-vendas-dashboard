from __future__ import annotations

import csv
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from prepare_data import OUTPUT_FIELDS, prepare_records


def sample_record(**overrides: str) -> dict[str, str]:
    record = {
        "SaleDateSanitized": "2024-03-14",
        "PorscheModelSanitized": "911 Turbo S",
        "ModelYearSanitized": "2024",
        "SalesPriceSanitized": "235000.00",
        "VehicleMileageSanitized": "1200",
        "PayMethodSanitized": "Credit Card",
        "CitySanitized": "Seattle",
        "StateSanitized": "WA",
        "DeliveryStatusSanitized": "Delivered",
    }
    record.update(overrides)
    return record


class PrepareDataTests(unittest.TestCase):
    def test_converts_types_and_invalid_date(self) -> None:
        rows, invalid_dates = prepare_records([sample_record(SaleDateSanitized="INVALID")])
        self.assertEqual(invalid_dates, 1)
        self.assertIsNone(rows[0]["data"])
        self.assertEqual(rows[0]["ano"], 2024)
        self.assertEqual(rows[0]["preco"], 235000.0)
        self.assertEqual(rows[0]["quilometragem"], 1200)
        self.assertEqual(rows[0]["estado"], "WA")
        self.assertEqual(list(rows[0]), OUTPUT_FIELDS)

    def test_rejects_missing_sanitized_field(self) -> None:
        record = sample_record()
        del record["SalesPriceSanitized"]
        with self.assertRaisesRegex(ValueError, "Campos sanitizados ausentes"):
            prepare_records([record])

    def test_rejects_invalid_year(self) -> None:
        with self.assertRaisesRegex(ValueError, "ano fora do intervalo"):
            prepare_records([sample_record(ModelYearSanitized="1899")])

    def test_rejects_negative_price(self) -> None:
        with self.assertRaisesRegex(ValueError, "não negativo"):
            prepare_records([sample_record(SalesPriceSanitized="-1")])

    def test_generated_outputs_match(self) -> None:
        json_path = ROOT / "data" / "vendas_sanitizadas.json"
        csv_path = ROOT / "data" / "vendas_sanitizadas.csv"
        if not json_path.exists() or not csv_path.exists():
            self.skipTest("Execute scripts/prepare_data.py antes dos testes.")
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["metadata"]["registros"], 100)
        self.assertEqual(payload["metadata"]["datas_invalidas"], 24)
        self.assertEqual(len(payload["rows"]), 100)
        self.assertEqual(set(payload["rows"][0]), set(OUTPUT_FIELDS))
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            csv_rows = list(csv.DictReader(handle))
        self.assertEqual(len(csv_rows), 100)
        self.assertEqual(list(csv_rows[0]), OUTPUT_FIELDS)


if __name__ == "__main__":
    unittest.main()
