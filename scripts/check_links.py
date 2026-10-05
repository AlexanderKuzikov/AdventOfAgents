"""Проверка локальных ссылок в собранном сайте.

Проверяет все href в dist/**/*.html: индекс, страницы дней, ассеты и ссылки
на DOCX. Ловит то, что не видно на глаз: страница собрана с именем файла,
которое уже не совпадает с реальным.

Использование:
    python scripts/check_links.py
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

HREF = re.compile(r'(?:href|src)="([^"]+)"')


def check():
    if not DIST.exists():
        sys.exit("нет dist/: сначала python scripts/build.py")

    pages = sorted(DIST.rglob("*.html"))
    if not pages:
        sys.exit("в dist/ нет ни одного html")

    broken = []
    checked = 0

    for page in pages:
        text = page.read_text(encoding="utf-8")
        for href in HREF.findall(text):
            url = href.strip()
            if not url or url.startswith(("#", "http://", "https://", "mailto:", "data:")):
                continue

            parsed = urlparse(url)
            if parsed.scheme in ("http", "https"):
                continue

            target = unquote(parsed.path)
            if not target:
                continue  # якорь на той же странице

            checked += 1
            resolved = (page.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{page.relative_to(ROOT)}  →  {target}")

    print(f"страниц: {len(pages)}, локальных ссылок: {checked}, битых: {len(broken)}")
    for item in broken[:40]:
        print("  " + item)

    return broken


def main():
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())