"""Подготовка дня к переводу: страница сезона + субтитры + черновик сегментов.

Использование:
    python scripts/prepare.py --all                    # весь сайт: страницы + субтитры
    python scripts/prepare.py s3-2026-10 day05         # один день
    python scripts/prepare.py s3-2026-10 --all         # один сезон
    python scripts/prepare.py --all --pages-only       # без субтитров
    python scripts/prepare.py --all --refresh           # перекачать манифест и API

Результат в data/<сезон>/<день>/:
    page.md          исходная страница сайта (.md)
    page.json        разобранные метаданные: title, теги, ссылки, код, видео
    en-orig.json3    автосубтитры YouTube (если у дня есть видео)
    draft.json       сегменты с пустым "ru" — черновик для перевода

Только стандартная библиотека.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from registry import ORIGIN, seasons, slug, video_id  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

WATCH = "https://www.youtube.com/watch?v={}"
UA = "Mozilla/5.0 (adventofagents-translator)"

DEFAULT_GAP = 3.0
DEFAULT_MAX_CHARS = 500


def http_get(url, tries=3):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except Exception as exc:  # noqa: BLE001
            if attempt == tries - 1:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("unreachable")


# --------------------------------------------------------------------------
# Разбор страницы дня (.md)
# --------------------------------------------------------------------------

def split_frontmatter(text):
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].lstrip("\n"), parts[2]


def scalar(raw):
    raw = raw.strip()
    if raw.startswith(("[", "{")):
        try:
            return json.loads(raw.replace("'", '"'))
        except ValueError:
            return raw
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw in ("true", "false"):
        return raw == "true"
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def parse_frontmatter(block):
    """Мини-парсер YAML: scalars, [inline lists], вложенный dict по отступу."""
    root = {}
    stack = [(-1, root)]

    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())
        key, _, raw = line.strip().partition(":")
        if not _:
            continue
        key, raw = key.strip(), raw.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1] if stack else root

        if raw == "":
            child = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = scalar(raw)

    return root


def duration_seconds(text):
    m = re.fullmatch(r"(\d+):(\d{2})", (text or "").strip())
    return int(m.group(1)) * 60 + int(m.group(2)) if m else 0


def parse_page(md, day_dir_name):
    fm_raw, body = split_frontmatter(md)
    fm = parse_frontmatter(fm_raw)
    primary = fm.get("primary_video") or {}

    url = primary.get("video_url") or fm.get("video_url", "")
    vid = video_id(url)
    duration = primary.get("duration", "")

    resources = re.search(r"##\s+Resources\s*&\s*Links\s*\n(.*?)(?=\n##\s|\Z)", body, re.S)
    links = []
    if resources:
        seen = set()
        for title, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", resources.group(1)):
            href = href.split("?")[0]
            if href in seen:
                continue
            seen.add(href)
            links.append({"title": title, "url": href})

    return {
        "day": day_dir_name,
        "season": fm.get("season", 0),
        "season_name": fm.get("season_name", ""),
        "title": fm.get("title", ""),
        "summary": fm.get("summary", ""),
        "tags": fm.get("tags", []),
        "canonical_url": fm.get("canonical_url", ""),
        "video_id": vid,
        "video_url": WATCH.format(vid) if vid else "",
        "video_title": primary.get("title", ""),
        "creator_name": primary.get("creator_name", ""),
        "duration": duration,
        "duration_s": duration_seconds(duration),
        "links": links,
        "code": "\n".join(re.findall(r"```bash\n(.*?)```", body, re.S)),
        "body": body.strip(),
    }


def merge_api(page, api_day):
    """API сезона богаче .md-страницы: ссылки с описаниями и сниппеты кода."""
    page["tags"] = api_day.get("tags") or page["tags"]
    page["summary"] = api_day.get("summary") or page["summary"]
    page["icon"] = api_day.get("icon", "")
    page["resource_link"] = api_day.get("resourceLink", "")
    page["links"] = [
        {"title": x["label"], "url": x["url"].split("?")[0], "description": x.get("description", "")}
        for x in api_day.get("links", [])
    ] or page["links"]
    page["code_snippets"] = api_day.get("codeSnippets", [])
    page["description"] = api_day.get("description", "")
    page.pop("body", None)  # .md целиком лежит рядом в page.md

    vid = video_id(api_day.get("videoURL"))
    if vid and not page["video_id"]:
        page["video_id"] = vid
        page["video_url"] = WATCH.format(vid)

    meta = api_day.get("primaryVideoMeta") or {}
    for src, dst in (("title", "video_title"), ("creatorName", "creator_name"), ("duration", "duration")):
        if meta.get(src) and not page[dst]:
            page[dst] = meta[src]
    if not page["duration_s"]:
        page["duration_s"] = duration_seconds(page["duration"])

    return page


# --------------------------------------------------------------------------
# Субтитры
# --------------------------------------------------------------------------

def video_available(vid):
    """YouTube oEmbed: 404 → видео удалено, приватно или регион закрыт.

    Дешевле, чем просить yt-dlp: один HTTP-запрос вместо полной загрузки
    плеера. Нужен, потому что у архивных сезонов часть роликов закрыта.
    """
    url = f"https://www.youtube.com/oembed?url={WATCH.format(vid)}&format=json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status == 200
    except Exception:  # noqa: BLE001
        return False


def download_subs(vid, day_dir, force=False):
    """Кладёт автосубтитры en-orig в day_dir/en-orig.json3.

    yt-dlp дописывает язык к имени файла (ID.en-orig.json3), поэтому приводим
    к каноническому виду. Цель удаляется заранее: shutil.move на Windows
    перезаписывает файл, и следующий unlink снёс бы свежий.
    """
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp не найден: pip install -U yt-dlp")

    canonical = day_dir / "en-orig.json3"
    if canonical.exists() and not force:
        return canonical

    if not video_available(vid):
        return None

    proc = subprocess.run(
        [
            "yt-dlp", "--skip-download", "--no-update",
            "--write-auto-subs",
            "--sub-langs", "en-orig",
            "--sub-format", "json3",
            "--force-overwrites",
            "-o", str(day_dir / "raw.%(ext)s"),
            WATCH.format(vid),
        ],
        capture_output=True,
        text=True,
    )

    downloaded = sorted(day_dir.glob("raw.*.json3"))
    if not downloaded:
        return None  # доступен по oEmbed, но субтитров нет — не фатально

    if canonical.exists():
        canonical.unlink()
    downloaded[0].rename(canonical)
    for extra in downloaded[1:]:
        extra.unlink()

    return canonical


def parse_json3(path):
    """[(секунды, текст)] — одно событие = одна реплика, без дублей."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    out, prev = [], None

    for event in payload.get("events", []):
        text = "".join(s.get("utf8", "") for s in event.get("segs", []))
        text = " ".join(text.split()).strip()
        if not text or text == prev:
            continue
        out.append((event.get("tStartMs", 0) / 1000, text))
        prev = text

    return out


def group(segments, gap, max_chars):
    """Склеивает соседние реплики: пауза >= gap или длина > max_chars → новый сегмент."""
    out = []
    for start, text in segments:
        if out and start - out[-1]["last"] < gap and len(out[-1]["text"]) + len(text) <= max_chars:
            out[-1]["text"] += " " + text
            out[-1]["last"] = start
        else:
            out.append({"t": start, "text": text, "last": start})
    return [{"t": round(s["t"]), "en": s["text"], "ru": ""} for s in out]


# --------------------------------------------------------------------------


def run_season(meta, api, args):
    slug_name = slug(meta)
    days = api.get("days", [])
    print(f"\n=== {slug_name}  {meta.get('label', '')}")

    total = len(days)
    for i, api_day in enumerate(days, 1):
        n = api_day["day"]
        day_name = f"day{n:02d}"
        day_dir = DATA / slug_name / day_name
        day_dir.mkdir(parents=True, exist_ok=True)

        if (day_dir / "translation.json").exists():
            print(f"  [{i:>2}/{total}] {day_name}: переведён, пропускаю")
            continue

        url = ORIGIN + meta["route"].rstrip("/") + f"/{n:02d}.md"
        try:
            md = http_get(url)
        except Exception as exc:  # noqa: BLE001
            print(f"  [{i:>2}/{total}] {day_name}: ! страница недоступна ({exc})")
            continue

        (day_dir / "page.md").write_text(md, encoding="utf-8")
        page = merge_api(parse_page(md, day_name), api_day)
        (day_dir / "page.json").write_text(
            json.dumps(page, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        note = ""
        if args.pages_only or not page["video_id"]:
            note = "без субтитров" if args.pages_only else "видео нет"
        else:
            subs = download_subs(page["video_id"], day_dir, args.force)
            if subs is None:
                page["video_available"] = False
                (day_dir / "page.json").write_text(
                    json.dumps(page, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                note = "видео недоступно/нет субтитров"
            else:
                segs = group(parse_json3(subs), args.gap, args.max_chars)
                (day_dir / "draft.json").write_text(
                    json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                note = f"{len(segs)} сегм."

        print(f"  [{i:>2}/{total}] {day_name}: {api_day.get('title', '')[:52]:<52} {note}")
        time.sleep(0.3)


def main():
    ap = argparse.ArgumentParser(description="Подготовить дни к переводу")
    ap.add_argument("season", nargs="?", help="например s3-2026-10")
    ap.add_argument("day", nargs="?", help="day05")
    ap.add_argument("--all", action="store_true", help="весь сайт или указанный сезон")
    ap.add_argument("--pages-only", action="store_true", help="не качать субтитры")
    ap.add_argument("--refresh", action="store_true", help="перекачать манифест и API")
    ap.add_argument("--force", action="store_true", help="перекачать субтитры заново")
    ap.add_argument("--gap", type=float, default=DEFAULT_GAP)
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS)
    args = ap.parse_args()

    if not args.season and not args.all:
        ap.error("укажи сезон и день, либо --all")

    all_seasons = seasons(refresh=args.refresh)

    if args.season and args.day:
        n = int(re.sub(r"\D", "", args.day))
        for meta, api in all_seasons:
            if slug(meta) != args.season:
                continue
            api_day = next(d for d in api["days"] if d["day"] == n)
            md = http_get(ORIGIN + meta["route"].rstrip("/") + f"/{n:02d}.md")
            day_dir = DATA / args.season / f"day{n:02d}"
            day_dir.mkdir(parents=True, exist_ok=True)
            (day_dir / "page.md").write_text(md, encoding="utf-8")
            page = merge_api(parse_page(md, f"day{n:02d}"), api_day)
            (day_dir / "page.json").write_text(
                json.dumps(page, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            if page["video_id"] and not args.pages_only:
                subs = download_subs(page["video_id"], day_dir, args.force)
                if subs is not None:
                    segs = group(parse_json3(subs), args.gap, args.max_chars)
                    (day_dir / "draft.json").write_text(
                        json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8"
                    )
            print(f"{args.season}/day{n:02d}: {page['title']}  →  {day_dir}")
            return

        sys.exit(f"сезон {args.season} не найден")

    targets = [(m, a) for m, a in all_seasons if not args.season or slug(m) == args.season]
    for meta, api in targets:
        run_season(meta, api, args)


if __name__ == "__main__":
    main()