from __future__ import annotations

from bs4 import BeautifulSoup


def extract_articles(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[dict] = []

    for card in soup.select(".article-card"):
        title_node = card.select_one(".article-title")
        summary_node = card.select_one(".article-summary")
        tag_nodes = [tag.get_text(strip=True) for tag in card.select(".tag")]
        link = title_node.get("href", "") if title_node else ""

        if not title_node:
            continue

        records.append(
            {
                "title": title_node.get_text(strip=True),
                "url": link,
                "summary": summary_node.get_text(strip=True) if summary_node else "",
                "tags": ",".join(tag_nodes),
            }
        )

    return records
