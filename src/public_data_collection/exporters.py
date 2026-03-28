from __future__ import annotations

from csv import DictWriter
import json
from pathlib import Path


def save_as_csv(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(file, fieldnames=["title", "url", "summary", "tags"])
        writer.writeheader()
        writer.writerows(records)


def save_as_json(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
