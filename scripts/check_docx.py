"""Проверка собранных DOCX без Word COM.

COM-рендер требует интерактивного Word и зависает, если процессы зависли.
Эта проверка ловит то, что ловится на файле: шрифт, кегль, число абзацев,
наличие приложения с правками, отсутствие пустых переводов.

Использование:
    python scripts/check_docx.py            # все собранные файлы
    python scripts/check_docx.py dist/...   # один файл
"""

import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent.parent


def check(path):
    problems = []

    doc = Document(path)

    normal = doc.styles["Normal"]
    font = normal.font.name
    size = normal.font.size.pt if normal.font.size else None
    if font != "Calibri":
        problems.append(f"шрифт Normal = {font!r}, ожидался Calibri")
    if size != 11:
        problems.append(f"кегль Normal = {size}, ожидался 11")

    empties = [p.text for p in doc.paragraphs if p.text.strip() == ""]
    texts = [p.text for p in doc.paragraphs if p.text.strip()]

    if not texts:
        problems.append("пустой документ")
    if len(empties) > len(texts) // 3:
        problems.append(f"много пустых абзацев: {len(empties)} из {len(doc.paragraphs)}")

    stamps = [p.text for p in doc.paragraphs if p.text.startswith("[") and p.text.endswith("]")]
    if not stamps:
        problems.append("нет ни одного таймкода")

    cjk = [t for t in texts if any("一" <= c <= "鿿" for c in t)]
    if cjk:
        problems.append(f"CJK-символы в {len(cjk)} абзацах")

    tables = doc.tables
    if tables:
        table = tables[0]
        if len(table.columns) != 4:
            problems.append(f"в приложении {len(table.columns)} колонок, ожидалось 4")
        widths = [c.width for c in table.rows[0].cells]
        if any(w is None for w in widths):
            problems.append("в таблице есть ячейки без ширины")

    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            problems.append(f"повреждён элемент архива: {bad}")

    return {
        "paragraphs": len(texts),
        "stamps": len(stamps),
        "tables": len(tables),
        "fix_rows": len(tables[0].rows) - 1 if tables else 0,
        "font": f"{font} {size}",
        "problems": problems,
    }


def docx_files():
    return sorted(
        p for p in ROOT.glob("dist/*/*/*.docx")
        if not p.name.startswith("~$")  # lock-файл зависшего Word
    )


def main():
    if len(sys.argv) > 1:
        files = [Path(a) for a in sys.argv[1:]]
    else:
        files = docx_files()

    if not files:
        raise SystemExit("нет docx: сначала python scripts/build.py")

    failed = 0
    for path in files:
        rel = path.relative_to(ROOT)
        try:
            info = check(path)
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL {rel}\n      ! не читается: {exc}")
            failed += 1
            continue

        flag = "OK " if not info["problems"] else "FAIL"
        print(
            "{} {}  абзацев {} · таймкодов {} · правок {} · {}".format(
                flag, rel, info["paragraphs"], info["stamps"],
                info["fix_rows"], info["font"],
            )
        )
        for problem in info["problems"]:
            print("      ! " + problem)
            failed += 1

    print(f"\n{len(files)} файлов, замечаний: {failed}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()