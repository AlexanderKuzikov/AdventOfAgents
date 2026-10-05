"""Сборка артефактов дня: двуязычный HTML и перевод-only DOCX.

Использование:
    python scripts/build.py                 # все дни
    python scripts/build.py day01           # один день
"""

import argparse
import html as H
import json
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DIST = ROOT / "dist"

VIDEO_URL = "https://www.youtube.com/watch?v={}"


def mmss(seconds):
    return f"{int(seconds) // 60:02d}:{int(seconds) % 60:02d}"


def load(day):
    """Сливает page.json (метаданные) и translation.json (сегменты).

    day — путь вида "s3-2026-10/day01" относительно data/.
    """
    day_dir = DATA / day
    tr_path = day_dir / "translation.json"
    if not tr_path.exists():
        sys.exit(f"нет перевода: {tr_path}")

    try:
        tr = json.loads(tr_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        # Обычно неэкранированные кавычки внутри русского текста
        sys.exit(f"{tr_path}: битый JSON — {exc}")
    segments = tr["segments"] if isinstance(tr, dict) else tr

    page_path = day_dir / "page.json"
    meta = json.loads(page_path.read_text(encoding="utf-8")) if page_path.exists() else {}

    note = meta.get("note") or (tr.get("note", "") if isinstance(tr, dict) else "")

    merged = dict(meta)
    merged.update({
        "day": day,
        "season_slug": day.split("/")[0],
        "source_lang": meta.get("source_lang", "en"),
        "target_lang": "ru",
        "subtitle_kind": meta.get("subtitle_kind", "auto (YouTube en-orig)"),
        "duration_s": meta.get("duration_s", 0),
        "note": note,
        "segments": segments,
    })

    if not merged["segments"]:
        sys.exit(f"в {tr_path} нет сегментов")
    if any(not s.get("ru") for s in merged["segments"]):
        empty = [s["t"] for s in merged["segments"] if not s.get("ru")]
        sys.exit(f"не переведены сегменты на секундах: {empty}")

    return merged


# --------------------------------------------------------------------------
# HTML: две колонки, точное противопоставление абзацев
# --------------------------------------------------------------------------

HTML_CSS = """
:root {
  --en-bg: #f7f8fa;
  --line: #dfe3e8;
  --accent: #0b57d0;
  --ts: #8a9099;
  --muted: #5f6672;
  --fix: #fff3cd;
  --fix-line: #e0b100;
}

* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  padding: 32px 20px 72px;
  background: #eef0f3;
  font-family: Calibri, "Segoe UI", system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.45;
  color: #1a1a1a;
}

.page { max-width: 1400px; margin: 0 auto; }

h1 { margin: 0 0 6px; font-size: 30px; font-weight: 700; letter-spacing: -0.01em; }
.head .sub { color: var(--muted); font-size: 15px; }
.head .sub a { color: var(--accent); }

.legend {
  display: flex; flex-wrap: wrap; gap: 18px; align-items: center;
  margin: 14px 0 18px; font-size: 14px; color: var(--muted);
}
.legend label { display: inline-flex; align-items: center; gap: 7px; cursor: pointer; user-select: none; }
.legend input { accent-color: var(--accent); width: 16px; height: 16px; cursor: pointer; }

.bar { display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 18px; }

button {
  font: inherit; font-size: 14px; padding: 7px 14px;
  border: 1px solid var(--line); border-radius: 6px;
  background: #fff; color: #1a1a1a; cursor: pointer;
}
button:hover { border-color: #b9c0ca; background: #fafbfc; }

.grid {
  background: #fff; border: 1px solid var(--line);
  border-radius: 10px; overflow: hidden;
}

.head-row, .row { display: grid; grid-template-columns: 64px 1fr 1fr; }

.head-row {
  background: #2f3541; color: #fff;
  font-size: 13px; letter-spacing: 0.04em;
  text-transform: uppercase; font-weight: 600;
  position: sticky; top: 0; z-index: 5;
}
.head-row > div { padding: 10px 18px; }
.head-row > div:first-child, .head-row > div:nth-child(2) { border-right: 1px solid #454c5a; }

.row > .ts {
  padding: 14px 8px; font-size: 12px;
  font-variant-numeric: tabular-nums;
  color: var(--ts); text-align: right;
  border-right: 1px solid var(--line); background: #fbfbfc;
}
.row > .en, .row > .ru {
  padding: 14px 18px; border-right: 1px solid var(--line); font-size: 15.5px;
}
.row > .en { background: var(--en-bg); }
.row > .ru { border-right: 0; }

.row.cont > .ts::after {
  content: ""; display: block; width: 14px; height: 1px;
  background: var(--line); margin: 8px 0 0 auto;
}
.row.cont > .en, .row.cont > .ru { padding-top: 9px; padding-bottom: 9px; }

.row.fixed > .en { background: var(--fix); }
.row.fixed .tag { display: none; }

body.show-fixes .row.fixed .tag { display: block; }

.tag {
  display: inline-block; margin-top: 6px;
  font-size: 11.5px; line-height: 1.35;
  color: #6b5400; background: var(--fix);
  border-left: 3px solid var(--fix-line);
  padding: 3px 8px; border-radius: 0 4px 4px 0;
}

.app { margin-top: 26px; }
.app h2 { font-size: 19px; margin: 0 0 10px; }

table {
  width: 100%; border-collapse: collapse;
  background: #fff; border: 1px solid var(--line);
  border-radius: 10px; overflow: hidden; font-size: 15px;
}
th, td { text-align: left; vertical-align: top; padding: 10px 14px; border-bottom: 1px solid var(--line); }
th { background: #f2f4f7; font-weight: 600; font-size: 14px; }
tr:last-child td { border-bottom: 0; }
td:first-child { font-family: Consolas, "Cascadia Mono", monospace; font-size: 13.5px; color: #3c424d; }
.note { font-size: 13.5px; color: var(--muted); margin: 10px 0 0; }

body.hide-en .row > .en, body.hide-en .head-row > div:nth-child(2) { display: none; }
body.hide-ru .row > .ru, body.hide-ru .head-row > div:nth-child(3) { display: none; }
body.hide-en .row, body.hide-en .head-row,
body.hide-ru .row, body.hide-ru .head-row { grid-template-columns: 64px 1fr; }

@media (max-width: 900px) {
  .head-row, .row { grid-template-columns: 56px 1fr; }
  .row > .en, .head-row > div:nth-child(2) { border-right: 0; }
  .row > .ru { grid-column: 2; border-top: 1px dashed var(--line); }
}

@media print {
  body { background: #fff; padding: 0; }
  .bar, .legend { display: none; }
  .head-row { position: static; }
  .grid, table { border-radius: 0; }
}
"""

HTML_JS = """
const el = id => document.getElementById(id);

el('tgl-en').addEventListener('change', e =>
  document.body.classList.toggle('hide-en', !e.target.checked));
el('tgl-ru').addEventListener('change', e =>
  document.body.classList.toggle('hide-ru', !e.target.checked));
el('btn-print').addEventListener('click', () => window.print());
el('btn-mark').addEventListener('click', () => {
  const on = !document.body.classList.contains('show-fixes');
  document.body.classList.toggle('show-fixes', on);
  el('btn-mark').textContent = on ? 'Скрыть исправления' : 'Показать исправления';
});
"""


def build_html(day, meta, out):
    rows = []
    fixes = []
    prev_t = None

    for seg in meta["segments"]:
        first = seg["t"] != prev_t
        cls = "row" if first else "row cont"
        if seg.get("fix"):
            cls += " fixed"
            fixes.append(seg)
        stamp = mmss(seg["t"]) if first else ""
        tag = (
            f'<div class="tag">уточнено: {H.escape(seg["fix"])}</div>'
            if seg.get("fix")
            else ""
        )
        rows.append(
            f'    <div class="{cls}">\n'
            f'      <div class="ts">{stamp}</div>\n'
            f'      <div class="en">{H.escape(seg["en"])}{tag}</div>\n'
            f'      <div class="ru">{H.escape(seg["ru"])}</div>\n'
            f'    </div>'
        )
        prev_t = seg["t"]

    fix_table = "\n".join(
        f'      <tr><td>[{mmss(s["t"])}]</td><td>{H.escape(s["en"])}</td>'
        f'<td>{H.escape(s["fix"])}</td><td>{H.escape(s["ru"])}</td></tr>'
        for s in fixes
    )

    fix_block = ""
    if fix_table:
        fix_block = f"""
  <div class="app">
    <h2>Приложение. Где автосубтитры соврали и как это восстановлено</h2>
    <table>
      <thead>
        <tr><th>Время</th><th>Вероятная речь</th><th>Что исправлено</th><th>Перевод</th></tr>
      </thead>
      <tbody>
{fix_table}
      </tbody>
    </table>
    <p class="note">{H.escape(meta.get("note", ""))}</p>
  </div>
"""

    url = meta.get("url") or VIDEO_URL.format(meta["video_id"])
    subtitle_kind = meta.get("subtitle_kind", "")

    doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(meta["title"])} — EN / RU</title>
<style>{HTML_CSS}</style>
</head>
<body>
<div class="page">

  <div class="head">
    <h1>{H.escape(meta["title"])}</h1>
    <div class="sub">Двуязычная транскрипция: английский оригинал слева, русский перевод справа.
      Видео: <a href="{H.escape(url)}">{H.escape(url)}</a> · {mmss(meta["duration_s"])}
      · {H.escape(subtitle_kind)}</div>
  </div>

  <div class="legend">
    <label><input type="checkbox" id="tgl-en" checked> Показывать оригинал</label>
    <label><input type="checkbox" id="tgl-ru" checked> Показывать перевод</label>
  </div>

  <div class="bar">
    <button id="btn-mark">Показать исправления</button>
    <button id="btn-print">Печать / PDF</button>
  </div>

  <div class="grid">
    <div class="head-row">
      <div>Time</div>
      <div>English</div>
      <div>Русский</div>
    </div>
{chr(10).join(rows)}
  </div>
{fix_block}
</div>
<script>{HTML_JS}</script>
</body>
</html>
"""
    out.write_text(doc, encoding="utf-8")


# --------------------------------------------------------------------------
# DOCX: только перевод + приложение с исправлениями
# --------------------------------------------------------------------------

DOCX_GRAY = RGBColor(0x5F, 0x5F, 0x5F)
DOCX_BLUE = RGBColor(0x0B, 0x57, 0xD0)


def build_docx(day, meta, out):
    doc = Document()

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin, sec.right_margin = Cm(2.2), Cm(2.0)
    sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    for attr in ("w:eastAsia", "w:cs"):
        normal.element.rPr.rFonts.set(qn(attr), "Calibri")
    normal.paragraph_format.space_after = Pt(8)
    normal.paragraph_format.line_spacing = 1.15

    def heading(text, size=16, before=16):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before, pf.space_after, pf.keep_with_next = Pt(before), Pt(8), True
        r = p.add_run(text)
        r.font.name, r.font.size, r.bold = "Calibri", Pt(size), True
        r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        return p

    def meta_line(text, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(text)
        r.font.size = Pt(10)
        r.italic = italic
        r.font.color.rgb = DOCX_GRAY
        return p

    url = meta.get("url") or VIDEO_URL.format(meta["video_id"])

    heading(meta["title"])
    meta_line("Перевод видео на русский язык")
    meta_line(f"Видео: {url}")
    meta_line(
        f"Оригинал: {meta.get('source_lang', 'en')}, "
        f"длительность {mmss(meta['duration_s'])} · "
        f"субтитры: {meta.get('subtitle_kind', '')}"
    )
    meta_line(meta.get("note", ""), italic=True)

    heading("Транскрипция", before=18)

    prev_t = None
    for seg in meta["segments"]:
        if seg["t"] != prev_t:
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.space_before, pf.space_after, pf.keep_with_next = Pt(10), Pt(2), True
            r = p.add_run(f"[{mmss(seg['t'])}]")
            r.bold, r.font.size = True, Pt(11)
            r.font.color.rgb = DOCX_BLUE
            prev_t = seg["t"]

        p = doc.add_paragraph(seg["ru"])
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    fixes = [s for s in meta["segments"] if s.get("fix")]
    if not fixes:
        doc.save(out)
        return

    doc.add_page_break()
    heading("Приложение. Исправления распознавания субтитров")
    meta_line(
        "Оригинальные субтитры содержали артефакты распознавания. "
        "В переводе они восстановлены по смыслу:"
    )

    table = doc.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False

    hdr = table.rows[0].cells
    for i, text in enumerate(("Время", "Вероятная речь", "Что исправлено", "Перевод")):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(text)
        r.bold, r.font.name, r.font.size = True, "Calibri", Pt(10)
        tcPr = hdr[i]._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "E8EAED")
        tcPr.append(shd)

    for s in fixes:
        cells = table.add_row().cells
        values = (f"[{mmss(s['t'])}]", s["en"], s["fix"], s["ru"])
        for i, text in enumerate(values):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.name, r.font.size = "Calibri", Pt(10)

    widths = (Cm(1.7), Cm(6.2), Cm(4.4), Cm(5.0))
    for row in table.rows:
        for cell, width in zip(row.cells, widths):
            cell.width = width

    doc.save(out)


# --------------------------------------------------------------------------


def slug(day):
    """s3-2026-10/day01 -> day01-s3-2026-10"""
    return "-".join(day.split("/"))


def build_day(day):
    meta = load(day)
    out_dir = DIST / day
    out_dir.mkdir(parents=True, exist_ok=True)

    base = slug(day)
    html_path = out_dir / f"{base}-en-ru.html"
    docx_path = out_dir / f"{base}-transcript-ru.docx"
    build_html(day, meta, html_path)
    build_docx(day, meta, docx_path)

    fixes = sum(1 for s in meta["segments"] if s.get("fix"))
    print(f"{day}: {len(meta['segments'])} сегментов, {fixes} правок")
    print(f"  {html_path.relative_to(ROOT)}")
    print(f"  {docx_path.relative_to(ROOT)}")


def discover():
    return sorted(
        p.parent.relative_to(DATA).as_posix()
        for p in DATA.glob("*/*/translation.json")
    )


def main():
    ap = argparse.ArgumentParser(description="Сборка артефактов Advent of Agents")
    ap.add_argument("days", nargs="*", help="дни вида day01 (по умолчанию — все)")
    args = ap.parse_args()

    days = args.days or discover()
    if not days:
        sys.exit("нет ни одного дня в data/*/translation.json")

    for day in days:
        build_day(day)


if __name__ == "__main__":
    main()