"""Реестр сезонов Advent of Agents.

Единственный источник правды по структуре сайта. Берёт официальный манифест
`/.well-known/mcp.json` — там есть все сезоны, дни, теги и роуты.

Использование:
    python scripts/registry.py            # показать сезоны и дни
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REGISTRY = DATA / "_registry"

ORIGIN = "https://adventofagents.com"
MCP_URL = ORIGIN + "/.well-known/mcp.json"
API_URL = ORIGIN + "/api/season{}.json"

UA = "Mozilla/5.0 (adventofagents-translator)"


def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8")


def slug(meta):
    """/2026/10/ сезон 3 -> s3-2026-10"""
    parts = [p for p in meta["route"].strip("/").split("/") if p]
    year, month = parts[0], int(parts[1])
    return "s{}-{}-{:02d}".format(meta["season"], year, month)


def fetch_manifest(refresh=False):
    """Манифест сайта: сезоны, роуты, дни, теги. Кэшируется локально."""
    REGISTRY.mkdir(parents=True, exist_ok=True)
    cache = REGISTRY / "mcp.json"

    if cache.exists() and not refresh:
        return json.loads(cache.read_text(encoding="utf-8"))

    data = json.loads(http_get(MCP_URL))
    cache.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


def fetch_season_api(season, refresh=False):
    """API сезона: описания, ссылки, сниппеты кода, видео. Кэшируется локально."""
    REGISTRY.mkdir(parents=True, exist_ok=True)
    cache = REGISTRY / f"season{season}.json"

    if cache.exists() and not refresh:
        return json.loads(cache.read_text(encoding="utf-8"))

    data = json.loads(http_get(API_URL.format(season)))
    cache.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


def video_id(url):
    if not url:
        return None
    m = re.search(r"(?:embed/|watch\?v=|youtu\.be/|/v/)([\w-]{11})", url)
    return m.group(1) if m else None


def seasons(refresh=False):
    """[(meta, api)] — сезоны от свежих к новым, с данными API."""
    manifest = fetch_manifest(refresh)
    out = []

    for s in sorted(manifest.get("seasons", []), key=lambda x: x["season"]):
        try:
            api = fetch_season_api(s["season"], refresh)
        except Exception as exc:  # noqa: BLE001 — один сезон не должен ронять сбор
            print(f"  ! сезон {s['season']}: {exc}", file=sys.stderr)
            continue
        out.append((s, api))

    return out


def day_url(meta, day):
    return ORIGIN + meta["route"].rstrip("/") + f"/{day:02d}"


def main():
    for meta, api in seasons():
        days = api.get("days", [])
        with_video = sum(1 for d in days if video_id(d.get("videoURL")))
        print(
            "{}  {:<46}  дней {:>2} (опубликовано {:>2}), видео {:>2}".format(
                slug(meta),
                meta.get("label", "")[:46],
                len(days),
                api.get("currentDay", len(days)),
                with_video,
            )
        )


if __name__ == "__main__":
    main()