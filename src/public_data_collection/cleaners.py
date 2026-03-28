from __future__ import annotations


def normalize_records(records: list[dict]) -> list[dict]:
    cleaned: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for record in records:
        title = str(record.get("title", "")).strip()
        url = str(record.get("url", "")).strip()
        summary = " ".join(str(record.get("summary", "")).split())
        tags = record.get("tags", [])

        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
        else:
            tags = [str(tag).strip() for tag in tags if str(tag).strip()]

        key = (title.lower(), url.lower())
        if not title or key in seen:
            continue
        seen.add(key)

        cleaned.append(
            {
                "title": title,
                "url": url,
                "summary": summary,
                "tags": ",".join(sorted(set(tags))),
            }
        )

    return cleaned


def filter_by_keyword(records: list[dict], keyword: str | None) -> list[dict]:
    if not keyword:
        return records
    keyword = keyword.lower()
    return [
        record
        for record in records
        if keyword in record["title"].lower()
        or keyword in record["summary"].lower()
        or keyword in record["tags"].lower()
    ]
