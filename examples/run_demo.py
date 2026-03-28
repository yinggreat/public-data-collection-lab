from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src" / "public_data_collection"
sys.path.insert(0, str(SRC_ROOT))

from exporters import save_as_csv, save_as_json
from fetcher import fetch_html, load_local_html
from parser import extract_articles


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the public data collection demo.")
    parser.add_argument("--url", help="Optional public URL to fetch instead of the sample HTML file.")
    args = parser.parse_args()

    if args.url:
        html = fetch_html(args.url)
    else:
        html = load_local_html(Path(__file__).resolve().parent / "sample_articles.html")

    records = extract_articles(html)
    output_dir = REPO_ROOT / "examples" / "output"
    save_as_csv(records, output_dir / "articles.csv")
    save_as_json(records, output_dir / "articles.json")

    print(f"Extracted {len(records)} records.")
    for record in records:
        print(f"- {record['title']}")


if __name__ == "__main__":
    main()
