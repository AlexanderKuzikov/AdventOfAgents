"""Каталог всех дней Advent of Agents → docs/CATALOG.md.

Использование:
    python scripts/catalog.py

Читает data/<сезон>/<день>/page.json и строит сводную таблицу:
теги, ресурсы, наличие видео, субтитров и перевода.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "CATALOG.md"

STATUS = {
    "translated": ("переведён", "✅"),
    "draft": ("субтитры готовы", "🟡"),
    "page": ("только страница", "⚪"),
}


def collect():
    seasons = {}
    for season_dir in sorted(DATA.glob("s*-*")):
        days = []
        for day_dir in sorted(season_dir.iterdir()):
            page_file = day_dir / "page.json"
            if not page_file.is_dir() and not page_file.exists():
                continue
            page = json.loads(page_file.read_text(encoding="utf-8"))

            has_subs = (day_dir / "en-orig.json3").exists()
            has_tr = (day_dir / "translation.json").exists()
            key = "translated" if has_tr else ("draft" if has_subs else "page")

            days.append({
                "day": day_dir.name,
                "title": page.get("title", ""),
                "summary": page.get("summary", ""),
                "tags": page.get("tags", []),
                "links": page.get("links", []),
                "code": page.get("code_snippets", []),
                "video_id": page.get("video_id"),
                "duration_s": page.get("duration_s", 0),
                "status": key,
                "has_subs": has_subs,
                "video_available": page.get("video_available", True),
                "canonical_url": page.get("canonical_url", ""),
            })
        if days:
            seasons[season_dir.name] = days
    return seasons


def mmss(seconds):
    return f"{int(seconds) // 60}:{int(seconds) % 60:02d}" if seconds else ""


def render(seasons):
    out = []
    out.append("# Каталог Advent of Agents")
    out.append("")
    out.append("Все три сезона, собранные скриптом `prepare.py` из официального манифеста")
    out.append("`adventofagents.com/.well-known/mcp.json` и API сезонов.")
    out.append("")
    out.append("Статусы: ✅ переведён · 🟡 субтитры скачаны, ждёт перевода · ⚪ видео нет или недоступно")
    out.append("")

    total = sum(len(d) for d in seasons.values())
    translated = sum(1 for d in seasons.values() for x in d if x["status"] == "translated")
    with_video = sum(1 for d in seasons.values() for x in d if x["has_subs"])

    out.append(f"Всего дней: **{total}**, с субтитрами: **{with_video}**, переведено: **{translated}**")
    out.append("")

    # Свод по тегам — быстрый вход в тему
    tag_index = {}
    for season, days in seasons.items():
        for d in days:
            for tag in d["tags"] or ["—"]:
                tag_index.setdefault(tag, []).append(f"{season}/{d['day']}")
    top = sorted(tag_index.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    out.append("## Темы")
    out.append("")
    out.append(" · ".join(f"**{t}** ({len(v)})" for t, v in top if len(v) > 1))
    out.append("")

    for season, days in seasons.items():
        out.append(f"## {season}")
        out.append("")
        for d in days:
            label, icon = STATUS[d["status"]]
            head = f"### {d['day']} — {d['title']}"
            bits = [icon]
            if d["duration_s"]:
                bits.append(mmss(d["duration_s"]))
            if d["tags"]:
                bits.append(", ".join(d["tags"]))
            out.append(f"{head}  \n{' · '.join(bits)}")
            out.append("")
            if d["summary"]:
                out.append(f"{d['summary']}")
                out.append("")

            if d["links"]:
                out.append("Ссылки:")
                for link in d["links"]:
                    desc = f" — {link['description']}" if link.get("description") else ""
                    out.append(f"- [{link['title']}]({link['url']}){desc}")
                out.append("")

            for snip in d["code"]:
                code = snip.get("code", "").strip()
                if code:
                    out.append(f"Код (`{snip.get('filename', '')}`):")
                    out.append("")
                    out.append("```" + snip.get("language", ""))
                    out.append(code)
                    out.append("```")
                    out.append("")

            if d["video_id"]:
                out.append(f"Видео: <https://www.youtube.com/watch?v={d['video_id']}>")
            elif not d["video_available"]:
                out.append("Видео недоступно (закрыто/удалено)")
            else:
                out.append("Видео нет")
            out.append("")
            out.append("---")
            out.append("")

    return "\n".join(out)


def main():
    seasons = collect()
    if not seasons:
        raise SystemExit("нет данных: запусти python scripts/prepare.py --all")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(seasons), encoding="utf-8")

    total = sum(len(d) for d in seasons.values())
    ready = sum(1 for d in seasons.values() for x in d if x["has_subs"])
    done = sum(1 for d in seasons.values() for x in d if x["status"] == "translated")
    print(f"{OUT.relative_to(ROOT)}: {total} дней, {ready} с субтитрами, {done} переведено")


if __name__ == "__main__":
    main()