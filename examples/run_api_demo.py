from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src" / "public_data_collection"
sys.path.insert(0, str(SRC_ROOT))

from cleaners import filter_by_keyword, normalize_records
from exporters import save_as_csv, save_as_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the API cleaning demo.")
    parser.add_argument("--keyword", help="Optional keyword filter, such as python or ai")
    args = parser.parse_args()

    raw_records = json.loads((Path(__file__).resolve().parent / "sample_api_response.json").read_text(encoding="utf-8"))
    records = normalize_records(raw_records)
    records = filter_by_keyword(records, args.keyword)

    output_dir = REPO_ROOT / "examples" / "output"
    save_as_csv(records, output_dir / "api_records.csv")
    save_as_json(records, output_dir / "api_records.json")

    print(f"Cleaned {len(records)} records.")
    for record in records:
        print(f"- {record['title']} [{record['tags']}]")


if __name__ == "__main__":
    main()
