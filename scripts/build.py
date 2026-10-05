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

from assets import APP_JS, STYLE
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
# Общие файлы сайта
# --------------------------------------------------------------------------

ASSETS = DIST / "assets"


def write_assets():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "style.css").write_text(STYLE, encoding="utf-8")
    (ASSETS / "app.js").write_text(APP_JS, encoding="utf-8")


def head(title, depth=0, extra=""):
    """Шапка страницы. depth — насколько подняться до dist/ за ../."""
    up = "../" * depth
    return (
        "<!DOCTYPE html>\n"
        '<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{H.escape(title)}</title>\n"
        f'<link rel="stylesheet" href="{up}assets/style.css">\n'
        f"{extra}"
        "</head>\n<body>\n"
        '<div class="top"><div class="inner">\n'
        f'<a class="brand" href="{up}index.html">Advent of Agents — перевод</a>\n'
        "<nav>"
        f'<a href="{up}index.html#seasons">Сезоны</a>\n'
        f'<a href="{up}index.html#materials">Материалы</a>\n'
        f'<a href="https://adventofagents.com/">Оригинал</a>\n'
        "</nav>\n"
        '<div class="spacer"></div>\n'
        f'<a href="https://github.com/AlexanderKuzikov/AdventOfAgents">репозиторий</a>\n'
        "</div></div>\n"
    )


def footer(depth=0):
    up = "../" * depth
    return (
        '<div class="page">\n'
        '<p class="note">Перевод с английского. Субтитры автоматические (YouTube auto), '
        "поэтому в приложении указано, где распознавание было исправлено. "
        f'Исходный ролик: <a href="https://www.youtube.com/watch?v=VIDEOID">YouTube</a>.</p>\n'
        "</div>\n"
        f'<script src="{up}assets/app.js"></script>\n'
        "</body>\n</html>\n"
    )

def build_day_html(day, meta, nav):
    """Страница дня: двуязычная сетка в обвязке сайта."""
    out_dir = DIST / day
    out_dir.mkdir(parents=True, exist_ok=True)
    base = slug(day)
    path = out_dir / f"{base}-en-ru.html"

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
        tag = f'<div class="tagline">уточнено: {H.escape(seg["fix"])}</div>' if seg.get("fix") else ""
        rows.append(
            f'    <div class="{cls}">\n'
            f'      <div class="ts">{stamp}</div>\n'
            f'      <div class="en">{H.escape(seg["en"])}{tag}</div>\n'
            f'      <div class="ru">{H.escape(seg["ru"])}</div>\n'
            f'    </div>'
        )
        prev_t = seg["t"]

    fix_block = ""
    if fixes:
        table = "\n".join(
            f'      <tr><td>{H.escape(mmss(s["t"]))}</td><td>{H.escape(s["en"])}</td>'
            f'<td>{H.escape(s["fix"])}</td><td>{H.escape(s["ru"])}</td></tr>'
            for s in fixes
        )
        fix_block = f"""
  <h2 id="fixes">Где автосубтитры соврали и как это восстановлено</h2>
  <table class="plain">
    <thead>
      <tr><th>Время</th><th>Вероятная речь</th><th>Что исправлено</th><th>Перевод</th></tr>
    </thead>
    <tbody>
{table}
    </tbody>
  </table>
  <p class="note">{H.escape(meta.get("note", ""))}</p>
"""

    video_url = meta.get("video_url") or ""
    extra_link = ""
    if video_url:
        extra_link = (
            f'<a href="{H.escape(video_url)}" target="_blank" rel="noopener">оригинальный ролик</a>'
        )

    doc = (
        head(f'{meta["title"]} — EN / RU', depth=2)
        + '<div class="page">\n'
        f'<p class="crumbs"><a href="../../index.html">Все дни</a> '
        f'&rsaquo; <a href="../../index.html#{H.escape(day.split("/")[0])}">'
        f'{H.escape(day.split("/")[0])}</a> &rsaquo; {H.escape(day.split("/")[1])}</p>\n'
        f'<h1>{H.escape(meta["title"])}</h1>\n'
        '<p class="lede">Двуязычная транскрипция: английский оригинал слева, '
        "русский перевод справа, абзацы стоят строго напротив друг друга.</p>\n"
        '<div class="stats">\n'
        f'  <div class="stat"><div class="n">{mmss(meta["duration_s"])}</div>'
        '<div class="k">длительность</div></div>\n'
        f'  <div class="stat"><div class="n">{len(meta["segments"])}</div>'
        '<div class="k">абзацев</div></div>\n'
        f'  <div class="stat"><div class="n">{len(fixes)}</div>'
        '<div class="k">правок распознавания</div></div>\n'
        "</div>\n"
        '<div class="bar">\n'
        '  <label class="legend"><input type="checkbox" id="tgl-en" checked> оригинал</label>\n'
        '  <label class="legend"><input type="checkbox" id="tgl-ru" checked> перевод</label>\n'
        "</div>\n"
        '<div class="bar">\n'
        '  <button id="btn-mark">Показать исправления</button>\n'
        '  <button id="btn-print">Печать / PDF</button>\n'
        f'  <a class="btn" href="{slug(day)}-transcript-ru.docx">Скачать DOCX</a>\n'
        f"  {extra_link}\n"
        "</div>\n"
        '  <div class="grid">\n'
        '    <div class="head-row">\n'
        "      <div>Time</div>\n      <div>English</div>\n      <div>Русский</div>\n"
        "    </div>\n"
        f"{chr(10).join(rows)}\n"
        "  </div>\n"
        f"{fix_block}"
        f"{nav}"
        "</div>\n"
        + footer(depth=2).replace("VIDEOID", meta.get("video_id", ""))
    )

    path.write_text(doc, encoding="utf-8")
    return path

# --------------------------------------------------------------------------
# Индекс: все дни сайта + материалы
# --------------------------------------------------------------------------

# Домены, чьи ссылки попадают в раздел «Материалы» как документы, а не как ссылки дня
DOC_HOSTS = (
    "kaggle.com/whitepaper", "a2a-protocol.org", "modelcontextprotocol.io",
    "docs.ag-ui.com", "a2ui.org", "ucp.dev", "owasp.org",
    "langchain-ai.github.io", "blog.langchain.dev", "a2a-editor.ag-ui.com",
    "google.github.io/adk-docs", "cloud.google.com/blog", "developers.googleblog.com",
    "codelabs.developers.google.com", "developers.google.com", "docs.cloud.google.com",
)

# Организации, чьи репозитории показываем отдельно от проектов участников
KNOWN_ORGS = {
    "google", "google-gemini", "googlecloudplatform", "google-agentic-commerce",
    "a2aproject", "modelcontextprotocol", "restatedev",
}

# Заголовки-заглушки в site: у репозитория нет имени, есть «Open Source Repo»
PLACEHOLDER_TITLES = {
    "open source repo", "project repository", "github repository", "repository",
    "open source repository", "source code", "code", "repo", "github repo",
}


def host_of(url):
    return url.split("//", 1)[-1].split("/", 1)[0]


def collect_site():
    """Все дни из page.json — включая те, что ещё не переведены."""
    seasons = {}
    for page_file in sorted(DATA.glob("s*/*/page.json")):
        day_dir = page_file.parent
        page = json.loads(page_file.read_text(encoding="utf-8"))
        key = day_dir.parent.name
        seasons.setdefault(key, []).append({
            "day": day_dir.name,
            "title": page.get("title", ""),
            "summary": page.get("summary", ""),
            "tags": page.get("tags", []),
            "video_id": page.get("video_id"),
            "video_available": page.get("video_available", True),
            "duration_s": page.get("duration_s", 0),
            "creator_name": page.get("creator_name", ""),
            "canonical_url": page.get("canonical_url", ""),
            "links": page.get("links", []),
            "translated": (day_dir / "translation.json").exists(),
            "has_subs": (day_dir / "en-orig.json3").exists(),
        })
    return seasons


def collect_materials(seasons):
    """Ссылки со всех дней, разложенные по типам.

    Два разных правила отбора, потому что ссылки разного качества:

    * официальные репозитории берём все, что принадлежат известной
      организации, — их единицы, и каждая по делу (заголовок у таких
      ссылок часто «Open Source Repo», так что по заголовку их не отличить);
    * остальное отбираем по частоте: материалом считается ссылка,
      встретившаяся в двух и более разных днях. Разовая ссылка —
      это штука конкретного туториала.
    """
    seen = {}
    for days in seasons.values():
        for day in days:
            for link in day["links"]:
                url = link["url"]
                if not url:
                    continue
                if url in seen:
                    seen[url]["days"].add(day["day"])
                else:
                    seen[url] = {"title": link["title"], "days": {day["day"]}}

    docs, repos_known, repos_community = [], [], []

    for url, info in sorted(seen.items()):
        host = host_of(url)
        title = info["title"]

        if "github.com" in host:
            if title.strip().lower() in PLACEHOLDER_TITLES:
                continue  # «Open Source Repo» — имени нет, оставить нечего
            org = url.split("github.com/")[1].split("/")[0].lower()
            if org in KNOWN_ORGS:
                repos_known.append((title, url))
            elif len(info["days"]) >= 2:
                repos_community.append((title, url))
            continue

        if any(h in url for h in DOC_HOSTS) and len(info["days"]) >= 2:
            docs.append((title, url, host))

    # Один и тот же репозиторий сайт упоминает под разными URL (регистр в пути,
    # архивная ветка): в списке оставляем первый вариант.
    def dedupe(items):
        out, seen = [], set()
        for item in items:
            key = item[0].strip().lower()
            if key in seen:
                continue
            seen.add(key)
            out.append(item)
        return out

    return {
        "docs": dedupe(docs),
        "repos_known": dedupe(repos_known),
        "repos_community": dedupe(repos_community),
        "total": len(seen),
    }

def day_card(season, day):
    name = day["day"]
    base = slug(f"{season}/{name}")
    translated = day["translated"]

    # теги через ||, а не пробелом: «Agent Starter Pack» содержит пробелы,
    # регистр приводим к нижнему — подписи на сайте не приведены к единому виду
    tags = "||".join(t.lower() for t in day["tags"])
    pill = '<span class="pill done">переведён</span>' if translated else (
        '<span class="pill draft">субтитры</span>' if day["has_subs"]
        else '<span class="pill">только страница</span>'
    )

    links = []
    if translated:
        links.append(f'<a href="{H.escape(season)}/{name}/{base}-en-ru.html">EN | RU</a>')
        links.append(f'<a href="{season}/{name}/{base}-transcript-ru.docx">DOCX</a>')
    if day["video_id"] and day["video_available"]:
        links.append(f'<a href="https://www.youtube.com/watch?v={day["video_id"]}" '
                     'target="_blank" rel="noopener">видео</a>')
    if day["canonical_url"]:
        links.append(f'<a href="{H.escape(day["canonical_url"])}" target="_blank" '
                     'rel="noopener">страница</a>')

    tag_html = "".join(f'<span class="tag">{H.escape(t)}</span>' for t in day["tags"][:4])

    return (
        f'    <div class="day" data-tags="{H.escape(tags)}">\n'
        f'      <div class="n">{H.escape(season)} &middot; {name} &middot; {mmss(day["duration_s"])}</div>\n'
        f'      <div class="t">{H.escape(day["title"])}</div>\n'
        f'      <div class="s">{H.escape(day["summary"][:150])}</div>\n'
        f'      <div class="tags">{tag_html}</div>\n'
        f'      <div class="links">{pill} {" ".join(links)}</div>\n'
        "    </div>"
    )


def build_index(seasons, mats):
    total_days = sum(len(d) for d in seasons.values())
    translated = sum(1 for d in seasons.values() for x in d if x["translated"])
    with_subs = sum(1 for d in seasons.values() for x in d if x["has_subs"])

    tag_freq = {}
    for days in seasons.values():
        for day in days:
            for tag in day["tags"]:
                tag_freq[tag] = tag_freq.get(tag, 0) + 1
    top_tags = [t for t, n in sorted(tag_freq.items(), key=lambda kv: (-kv[1], kv[0])) if n > 1]

    filters = "".join(f'<button data-tag="{H.escape(t)}">{H.escape(t)}</button>' for t in top_tags)

    season_blocks = []
    for season in sorted(seasons, reverse=True):
        days = sorted(seasons[season], key=lambda d: d["day"])
        cards = "\n".join(day_card(season, d) for d in days)
        done = sum(1 for d in days if d["translated"])
        season_blocks.append(
            f'  <h3 id="{H.escape(season)}">{H.escape(season)} '
            f'<span class="pill">{done} из {len(days)} переведено</span></h3>\n'
            f'  <div class="days">\n{cards}\n  </div>\n'
        )

    def mat_list(items, with_host=False):
        out = []
        for entry in items:
            title, url = entry[0], entry[1]
            host = f' <span class="host">{H.escape(entry[2])}</span>' if with_host else ""
            out.append(f'<li><a href="{H.escape(url)}" target="_blank" rel="noopener">'
                       f'{H.escape(title)}</a>{host}</li>')
        return "\n        ".join(out)

    community_block = ""
    if mats["repos_community"]:
        community_block = (
            f'    <div class="mat"><h3>Репозитории участников ({len(mats["repos_community"])})</h3>\n'
            f"      <ul>\n        {mat_list(mats['repos_community'])}\n      </ul></div>\n"
        )

    doc = (
        head("Advent of Agents — двуязычные переводы", depth=0)
        + '<div class="page">\n'
        '<h1>Advent of Agents — двуязычные переводы</h1>\n'
        '<p class="lede">Все ролики Google Cloud Advent of Agents с английским оригиналом '
        "и русским переводом, выстроенным абзац в абзац. Источник — "
        '<a href="https://adventofagents.com/" target="_blank" rel="noopener">adventofagents.com</a>, '
        "данные собраны из официального манифеста сайта.</p>\n"
        '<div class="stats">\n'
        f'  <div class="stat"><div class="n">{len(seasons)}</div><div class="k">сезона</div></div>\n'
        f'  <div class="stat"><div class="n">{total_days}</div><div class="k">дней на сайте</div></div>\n'
        f'  <div class="stat"><div class="n">{with_subs}</div><div class="k">с субтитрами</div></div>\n'
        f'  <div class="stat"><div class="n">{translated}</div><div class="k">переведено</div></div>\n'
        f'  <div class="stat"><div class="n">{mats["total"]}</div><div class="k">ссылок собрано</div></div>\n'
        "</div>\n"
        '<h2 id="seasons">Дни по сезонам</h2>\n'
        f'<div class="filters" id="filters">\n'
        f'  <button data-tag="" class="on">все темы</button>\n  {filters}\n'
        "</div>\n"
        + "\n".join(season_blocks)
        + '\n<h2 id="materials">Материалы со всех дней</h2>\n'
        f'<p class="lede">Из {mats["total"]} собранных ссылок эти выглядят полезными: '
        "спецификации и whitepaper’ы, официальные репозитории и проекты участников.</p>\n"
        '  <div class="mats">\n'
        f'    <div class="mat"><h3>Документы и спецификации ({len(mats["docs"])})</h3>\n'
        f"      <ul>\n        {mat_list(mats['docs'], with_host=True)}\n      </ul></div>\n"
        f'    <div class="mat"><h3>Официальные репозитории ({len(mats["repos_known"])})</h3>\n'
        f"      <ul>\n        {mat_list(mats['repos_known'])}\n      </ul></div>\n"
        f"{community_block}"
        "  </div>\n"
        '<h2>Как это устроено</h2>\n'
        "<p>Данные лежат в <code>data/&lt;сезон&gt;/&lt;день&gt;/</code>: страница сайта, "
        "автосубтитры и ручной перевод. Генераторы — в <code>scripts/</code>, "
        "сборка одной командой <code>python scripts/build.py</code>. "
        "Английский текст в колонке рядом с переводом взят из тех же автосубтитров, "
        "поэтому обе колонки показывают ровно один и тот же фрагмент ролика.</p>\n"
        "</div>\n"
        + footer(depth=0).replace("VIDEOID", "")
    )

    path = DIST / "index.html"
    path.write_text(doc, encoding="utf-8")
    return path

# --------------------------------------------------------------------------

def slug(day):
    """s3-2026-10/day01 -> day01-s3-2026-10"""
    return "-".join(day.split("/"))


def discover():
    return sorted(
        p.parent.relative_to(DATA).as_posix()
        for p in DATA.glob("*/*/translation.json")
    )


def nav_html(season_days, day):
    """Навигация по соседним дням того же сезона."""
    idx = season_days.index(day)
    out = []

    def link(target, cls, label, rel):
        # мы уже внутри dist/<сезон>/<день>/, поэтому сосед — это ../<день>/
        name = target.split("/")[1]
        base = f"{slug(target)}-en-ru.html"
        return (f'  <a class="{cls}" href="../{name}/{base}" rel="{rel}">'
                f'{H.escape(label)} &rarr;</a>')

    if idx > 0:
        out.append(link(season_days[idx - 1], "prev", f'← {season_days[idx - 1].split("/")[1]}', "prev"))
    if idx < len(season_days) - 1:
        out.append(link(season_days[idx + 1], "next", f'{season_days[idx + 1].split("/")[1]} →', "next"))

    return f'  <div class="pager">\n' + "\n".join(out) + "\n  </div>\n" if out else ""


def build_day(day, season_days):
    meta = load(day)
    out_dir = DIST / day
    out_dir.mkdir(parents=True, exist_ok=True)

    base = slug(day)
    html_path = build_day_html(day, meta, nav_html(season_days, day))
    docx_path = out_dir / f"{base}-transcript-ru.docx"
    build_docx(day, meta, docx_path)

    fixes = sum(1 for s in meta["segments"] if s.get("fix"))
    print(f"{day}: {len(meta['segments'])} абзацев, {fixes} правок")


def main():
    ap = argparse.ArgumentParser(description="Сборка dist/: сайт с индексом и страницами дней")
    ap.add_argument("days", nargs="*", help="дни вида s3-2026-10/day04 (по умолчанию — все)")
    ap.add_argument("--no-index", action="store_true", help="не пересобирать индекс")
    args = ap.parse_args()

    days = args.days or discover()
    if not days and not args.no_index:
        sys.exit("нет ни одного дня в data/*/*/translation.json")

    write_assets()

    by_season = {}
    for day in days:
        by_season.setdefault(day.split("/")[0], []).append(day)

    for season_days in by_season.values():
        for day in season_days:
            build_day(day, season_days)

    if not args.no_index:
        seasons = collect_site()
        mats = collect_materials(seasons)
        path = build_index(seasons, mats)
        print(f"\n{path.relative_to(ROOT)}: дней {sum(len(d) for d in seasons.values())}, "
              f"ссылок {mats['total']}, документов {len(mats['docs'])}, "
              f"репозиториев {len(mats['repos_known']) + len(mats['repos_community'])}")


if __name__ == "__main__":
    main()
