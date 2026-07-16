#!/usr/bin/env python3
"""
Generiert aus produkte.csv fertige HTML-Zwischenseiten (template.html als Vorlage).

Nutzung:
    python3 generate.py

Erwartet:
    - produkte.csv  (Spalten: slug, amazon_link)
    - template.html (Platzhalter: __AMAZON_LINK__)

Erzeugt:
    - output/<slug>.html  für jede Zeile
"""

import csv
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "produkte.csv"
TEMPLATE_PATH = BASE_DIR / "template.html"
OUTPUT_DIR = BASE_DIR / "output"

SLUG_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def validate_slug(slug: str) -> bool:
    return bool(SLUG_PATTERN.match(slug))


def validate_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def main():
    if not CSV_PATH.exists():
        sys.exit(f"Fehler: {CSV_PATH.name} nicht gefunden. Liegt sie im selben Ordner wie das Script?")

    if not TEMPLATE_PATH.exists():
        sys.exit(f"Fehler: {TEMPLATE_PATH.name} nicht gefunden. Liegt sie im selben Ordner wie das Script?")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    OUTPUT_DIR.mkdir(exist_ok=True)

    created = 0
    skipped = 0

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_cols = {"slug", "amazon_link"}
        if not required_cols.issubset(set(reader.fieldnames or [])):
            sys.exit(f"Fehler: CSV braucht die Spalten {required_cols}, gefunden: {reader.fieldnames}")

        for row_num, row in enumerate(reader, start=2):  # Zeile 1 = Header
            slug = (row.get("slug") or "").strip()
            amazon_link = (row.get("amazon_link") or "").strip()

            if not slug or not amazon_link:
                print(f"⚠️  Zeile {row_num}: slug oder amazon_link fehlt — übersprungen")
                skipped += 1
                continue

            if not validate_slug(slug):
                print(f"⚠️  Zeile {row_num}: ungültiger slug '{slug}' (nur a-z, 0-9, Bindestriche) — übersprungen")
                skipped += 1
                continue

            if not validate_url(amazon_link):
                print(f"⚠️  Zeile {row_num}: ungültiger Link '{amazon_link}' — übersprungen")
                skipped += 1
                continue

            page = template.replace("__AMAZON_LINK__", amazon_link)

            out_path = OUTPUT_DIR / f"{slug}.html"
            out_path.write_text(page, encoding="utf-8")
            created += 1
            print(f"✅  {out_path.relative_to(BASE_DIR)}")

    print(f"\nFertig: {created} Seite(n) erstellt, {skipped} übersprungen.")


if __name__ == "__main__":
    main()
