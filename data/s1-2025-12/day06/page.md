---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 6
title: "🧑‍💻 ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more"
summary: "Building agents shouldn't require an hour of environment configuration. If you use the Agent Starter Pack you already have IDE magnet context baked in for the Agent Development Kit (ADK)."
tags: ["ANTIGRAVITY", "CLI", "IDE", "ADK"]
canonical_url: "https://adventofagents.com/2025/12/06"
markdown_url: "https://adventofagents.com/2025/12/06.md"
video_url: "https://www.youtube.com/embed/Ep8usBDUTtA"
---

# 🧑‍💻 Day 6: 🧑‍💻 ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/06?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day06) · [Raw Markdown](https://adventofagents.com/2025/12/06.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day06)

**Summary:** Building agents shouldn't require an hour of environment configuration. If you use the Agent Starter Pack you already have IDE magnet context baked in for the Agent Development Kit (ADK).

**Day 6 of Google's Advent of Agents**

Building agents shouldn't require an hour of environment configuration. If you use the Agent Starter Pack you already have IDE magnet context baked in for the Agent Development Kit (ADK).

In the attached video, you can see the antigravity with zero config aware of how ADK works, thanks to that default-on ADK cheatsheet which ships with the Agent Starter Pack and works with most IDEs.

If you aren’t using the Agent Starter Pack, here are a few ideas how you might configure a few IDEs.

**Super Short Command:**

```bash
uvx agent-starter-pack create deep_search --adk
```

**Resources:**

- Check out the [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day06)
- Check out the [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day06)
- Check out the [ADK Cheat Sheet](https://googlecloudplatform.github.io/agent-starter-pack/guide/installation.html)
- Check out the [llms.txt explanation](https://llmstxt.org/)
- Check out the [Video: ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more](https://www.youtube.com/watch?v=Ep8usBDUTtA)
- Bonus: Gemini made [Code Wiki](https://codewiki.google/github.com/google/adk-go)

## Code & Commands

```bash
# Using ADK and Agent Starter Pack within Antigravity
uvx agent-starter-pack create deep_search --adk
# nothing else
```

```bash
# Install dependencies
pip install pydantic-ai
gemini extensions install https://github.com/derailed-dash/adk-docs-ext
gemini
```

```bash
fetch from https://google.github.io/adk-docs/llms.txt
How do I create a function tool using Agent Development Kit?
```

## Resources & Links

- **[Antigravity](https://antigravity.google/)** — Antigravity IDE
- **[ADK Documentation llms.txt](https://google.github.io/adk-docs/llms.txt?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day06)** — ADK Documentation llms.txt file
- **[ADK Cheat Sheet](https://googlecloudplatform.github.io/agent-starter-pack/guide/installation.html)** — ADK Cheat Sheet from Agent Starter Pack
- **[llms.txt explanation](https://llmstxt.org/)** — Explanation of llms.txt
- **[Video: ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more](https://www.youtube.com/watch?v=Ep8usBDUTtA)** — YouTube video demonstrating ADK integration.
- **[Bonus: Gemini made Code Wiki](https://codewiki.google/github.com/google/adk-go)** — Want all the documentation in one url for a human or a giant context window? This is a cool resource for any public repo, in this case ADK Go!
