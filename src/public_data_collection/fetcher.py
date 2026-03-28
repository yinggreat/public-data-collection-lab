from __future__ import annotations

from pathlib import Path

import requests


DEFAULT_HEADERS = {
    "User-Agent": "PythonTrainerBrandKit/1.0 (+https://example.com/teaching-demo)"
}


def load_local_html(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fetch_html(url: str, timeout: int = 10) -> str:
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
    response.raise_for_status()
    return response.text
