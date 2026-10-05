"""Дополняет page.json метаданными ролика с YouTube.

Нужно для архивных сезонов: в их .md-страницах нет блока primary_video,
поэтому длительность, название и автор остаются пустыми.

Использование:
    python scripts/enrich.py            # все дни с en-orig.json3
    python scripts/enrich.py --force    # перезаписать уже заполненное
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

FIELDS = "%(duration)s\t%(title)s\t%(channel)s\t%(upload_date)s\t%(webpage_url)s"
WATCH = "https://www.youtube.com/watch?v={}"


def video_meta(vid):
    """Один вызов yt-dlp на ролик — только метаданные, без медиа."""
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp не найден: pip install -U yt-dlp")

    proc = subprocess.run(
        ["yt-dlp", "--skip-download", "--no-update", "--print", FIELDS, WATCH.format(vid)],
        capture_output=True,
        text=True,
    )
    line = proc.stdout.strip().splitlines()
    if not line:
        return None

    parts = line[-1].split("\t")
    if len(parts) < 5:
        return None

    duration, title, channel, upload_date, url = parts[:5]
    return {
        "duration_s": int(duration or 0),
        "video_title": title,
        "creator_name": channel,
        "upload_date": upload_date,
        "video_url": url,
    }


def main():
    ap = argparse.ArgumentParser(description="Дополнить метаданные роликов")
    ap.add_argument("--force", action="store_true", help="перезаписать заполненное")
    args = ap.parse_args()

    files = sorted(DATA.glob("s*/*/page.json"))
    done = skipped = failed = 0

    for page_file in files:
        day_dir = page_file.parent
        page = json.loads(page_file.read_text(encoding="utf-8"))
        vid = page.get("video_id")

        if not vid or not (day_dir / "en-orig.json3").exists():
            continue
        if page.get("duration_s") and not args.force:
            skipped += 1
            continue

        meta = video_meta(vid)
        if not meta:
            failed += 1
            print(f"  ! {day_dir.relative_to(DATA)}: метаданные не получились")
            continue

        page.update(meta)
        page_file.write_text(json.dumps(page, ensure_ascii=False, indent=2), encoding="utf-8")
        done += 1
        print(
            "  {} {:>4}с  {:<34} {}".format(
                str(day_dir.relative_to(DATA)).ljust(18),
                meta["duration_s"],
                meta["video_title"][:34],
                meta["creator_name"],
            )
        )

    print(f"\nобновлено: {done}, пропущено: {skipped}, ошибок: {failed}")


if __name__ == "__main__":
    main()