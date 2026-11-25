from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"

SOURCE_FIELDS = {
    "SaleDateSanitized": "data",
    "PorscheModelSanitized": "modelo",
    "ModelYearSanitized": "ano",
    "SalesPriceSanitized": "preco",
    "VehicleMileageSanitized": "quilometragem",
    "PayMethodSanitized": "pagamento",
    "CitySanitized": "cidade",
    "StateSanitized": "estado",
    "DeliveryStatusSanitized": "entrega",
}

OUTPUT_FIELDS = list(SOURCE_FIELDS.values())
INVALID_MARKERS = {"", "INVALID", "N/A", "NA", "NULL", "UNKNOWN", "INDISPONIVEL"}


def column_index(reference: str) -> int:
    match = re.match(r"([A-Za-z]+)", reference)
    if not match:
        raise ValueError(f"Referência de célula inválida: {reference!r}")
    index = 0
    for char in match.group(1).upper():
        index = index * 26 + ord(char) - ord("A") + 1
    return index - 1


def read_xlsx(path: Path) -> list[dict[str, str]]:
    with ZipFile(path) as archive:
        shared_strings: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall(f"{{{MAIN_NS}}}si"):
                shared_strings.append(
                    "".join(node.text or "" for node in item.iter(f"{{{MAIN_NS}}}t"))
                )

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheet = workbook.find(f"{{{MAIN_NS}}}sheets/{{{MAIN_NS}}}sheet")
        if sheet is None:
            raise ValueError("A planilha não contém abas.")
        relationship_id = sheet.get(f"{{{REL_NS}}}id")
        relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        target = next(
            (
                rel.get("Target")
                for rel in relationships.findall(f"{{{PACKAGE_REL_NS}}}Relationship")
                if rel.get("Id") == relationship_id
            ),
            None,
        )
        if not target:
            raise ValueError("Não foi possível localizar o arquivo da aba.")
        sheet_path = target.lstrip("/")
        if not sheet_path.startswith("xl/"):
            sheet_path = f"xl/{sheet_path}"

        sheet_root = ET.fromstring(archive.read(sheet_path))
        rows: list[dict[int, str]] = []
        formula_cells: list[str] = []
        for row in sheet_root.findall(f".//{{{MAIN_NS}}}sheetData/{{{MAIN_NS}}}row"):
            values: dict[int, str] = {}
            for cell in row.findall(f"{{{MAIN_NS}}}c"):
                reference = cell.get("r", "")
                index = column_index(reference)
                if cell.find(f"{{{MAIN_NS}}}f") is not None:
                    formula_cells.append(reference)
                cell_type = cell.get("t")
                value_node = cell.find(f"{{{MAIN_NS}}}v")
                if cell_type == "inlineStr":
                    value = "".join(
                        node.text or "" for node in cell.iter(f"{{{MAIN_NS}}}t")
                    )
                elif value_node is None:
                    value = ""
                elif cell_type == "s":
                    value = shared_strings[int(value_node.text or "0")]
                else:
                    value = value_node.text or ""
                values[index] = value.strip()
            rows.append(values)

    if formula_cells:
        raise ValueError(
            "A planilha contém fórmulas. Cole os valores antes de preparar a base: "
            + ", ".join(formula_cells[:5])
        )
    if not rows:
        raise ValueError("A planilha está vazia.")

    headers = rows[0]
    records = [{headers[index]: value for index, value in row.items() if index in headers} for row in rows[1:]]
    return [record for record in records if any(record.values())]


def normalized(value: str) -> str | None:
    cleaned = value.strip()
    return None if cleaned.upper() in INVALID_MARKERS else cleaned


def as_decimal(value: str, field: str, row_number: int) -> Decimal:
    cleaned = normalized(value)
    if cleaned is None:
        raise ValueError(f"Linha {row_number}: {field} vazio ou inválido.")
    try:
        number = Decimal(cleaned)
    except InvalidOperation as error:
        raise ValueError(f"Linha {row_number}: {field} não é numérico: {value!r}") from error
    if not number.is_finite() or number < 0:
        raise ValueError(f"Linha {row_number}: {field} deve ser um número finito não negativo.")
    return number


def prepare_records(records: list[dict[str, str]]) -> tuple[list[dict[str, object]], int]:
    missing = [field for field in SOURCE_FIELDS if field not in records[0]]
    if missing:
        raise ValueError("Campos sanitizados ausentes: " + ", ".join(missing))

    prepared: list[dict[str, object]] = []
    invalid_dates = 0
    for row_number, record in enumerate(records, start=2):
        raw_date = normalized(record["SaleDateSanitized"])
        sale_date = None
        if raw_date is None:
            invalid_dates += 1
        else:
            try:
                sale_date = date.fromisoformat(raw_date).isoformat()
            except ValueError:
                invalid_dates += 1

        year_value = as_decimal(record["ModelYearSanitized"], "ModelYearSanitized", row_number)
        if year_value != year_value.to_integral_value() or not 1900 <= year_value <= 2100:
            raise ValueError(f"Linha {row_number}: ano fora do intervalo aceito.")
        mileage = as_decimal(record["VehicleMileageSanitized"], "VehicleMileageSanitized", row_number)
        if mileage != mileage.to_integral_value():
            raise ValueError(f"Linha {row_number}: quilometragem deve ser inteira.")
        price = as_decimal(record["SalesPriceSanitized"], "SalesPriceSanitized", row_number)

        categorical = {}
        for source, target in SOURCE_FIELDS.items():
            if target in {"data", "ano", "preco", "quilometragem"}:
                continue
            value = normalized(record[source])
            if value is None:
                raise ValueError(f"Linha {row_number}: {source} vazio ou inválido.")
            categorical[target] = value

        prepared.append(
            {
                "data": sale_date,
                "modelo": categorical["modelo"],
                "ano": int(year_value),
                "preco": float(price.quantize(Decimal("0.01"))),
                "quilometragem": int(mileage),
                "pagamento": categorical["pagamento"],
                "cidade": categorical["cidade"],
                "estado": categorical["estado"].upper(),
                "entrega": categorical["entrega"],
            }
        )
    return prepared, invalid_dates


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_outputs(
    rows: list[dict[str, object]],
    invalid_dates: int,
    source_path: Path,
    output_dir: Path,
) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata = {
        "fonte": source_path.name,
        "fonte_sha256": sha256(source_path),
        "registros": len(rows),
        "datas_invalidas": invalid_dates,
        "campos": OUTPUT_FIELDS,
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    payload = {"metadata": metadata, "rows": rows}

    (output_dir / "vendas_sanitizadas.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    with (output_dir / "vendas_sanitizadas.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    report = f"""# Relatório de tratamento

- Fonte: `{source_path.name}`
- SHA-256 da fonte: `{metadata['fonte_sha256']}`
- Registros preparados: {len(rows)}
- Datas inválidas convertidas para nulo: {invalid_dates}
- Campos mantidos: {', '.join(f'`{field}`' for field in OUTPUT_FIELDS)}
- Campos descartados: todas as colunas brutas, incluindo nomes de clientes e vendedores.
- Preço convertido para número decimal; ano e quilometragem para inteiro.
- Data validada no formato ISO; `INVALID` virou nulo.
- Nenhuma fórmula foi mantida.
- Saídas: `vendas_sanitizadas.csv` e `vendas_sanitizadas.json`.
"""
    (output_dir / "RELATORIO_TRATAMENTO.md").write_text(report, encoding="utf-8")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepara a base sanitizada da Porsche para a dashboard.")
    parser.add_argument("--input", type=Path, default=Path("data/porsche_database_sanitized.xlsx"))
    parser.add_argument("--output-dir", type=Path, default=Path("data"))
    args = parser.parse_args()

    records = read_xlsx(args.input)
    rows, invalid_dates = prepare_records(records)
    metadata = write_outputs(rows, invalid_dates, args.input, args.output_dir)
    print(
        f"OK: {metadata['registros']} registros, {invalid_dates} datas inválidas."
    )


if __name__ == "__main__":
    main()
