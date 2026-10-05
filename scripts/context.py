"""Шпаргалка для перевода: контекст дня + сегменты.

Использование:
    python scripts/context.py s2-2026-03 day08 day14
    python scripts/context.py s2-2026-03 day08 --segs   # без контекста
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def show(day_dir):
    page = json.loads((day_dir / "page.json").read_text(encoding="utf-8"))

    print("=" * 78)
    print("{}  {}  ·  {}  ·  {:,}с  ·  {}".format(
        day_dir.parent.name, day_dir.name, page.get("title", ""),
        page.get("duration_s", 0), page.get("creator_name", ""),
    ))
    print("теги: " + ", ".join(page.get("tags", [])))
    if page.get("summary"):
        print("суть: " + page["summary"])

    desc = (page.get("description") or "").strip()
    desc = re.sub(r"\*\*(.+?)\*\*", r"\1", desc)
    desc = re.sub(r"\n{2,}", "\n", desc)
    if desc:
        print("--- описание дня ---")
        print(desc[:900])

    links = page.get("links", [])
    if links:
        print("--- ссылки ---")
        for link in links:
            desc_part = f" — {link['description']}" if link.get("description") else ""
            print("  {}{}".format(link["url"], desc_part))

    for snip in page.get("code_snippets", []):
        code = (snip.get("code") or "").strip()
        if code:
            print("--- код ({}) ---".format(snip.get("filename", "")))
            print(code[:700])

    draft = day_dir / "draft.json"
    if draft.exists():
        segs = json.loads(draft.read_text(encoding="utf-8"))
        print("--- сегменты ({}): заполнить ru ---".format(len(segs)))
        for i, seg in enumerate(segs):
            t = seg["t"]
            stamp = "{:02d}:{:02d}".format(t // 60, t % 60)
            print("[{}] {}".format(stamp, seg["en"]))
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season")
    ap.add_argument("days", nargs="+")
    ap.add_argument("--segs", action="store_true", help="только сегменты")
    args = ap.parse_args()

    for day in args.days:
        day_dir = DATA / args.season / day
        if not day_dir.exists():
            sys.exit(f"нет {day_dir}")
        if args.segs:
            page = json.loads((day_dir / "page.json").read_text(encoding="utf-8"))
            print("=== {} {} {} {:,}с".format(
                args.season, day, page.get("title", ""), page.get("duration_s", 0)))
            for seg in json.loads((day_dir / "draft.json").read_text(encoding="utf-8")):
                t = seg["t"]
                print("[{:02d}:{:02d}] {}".format(t // 60, t % 60, seg["en"]))
            print()
        else:
            show(day_dir)


if __name__ == "__main__":
    main()