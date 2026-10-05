---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 3
title: "Gemini 3 + ADK"
summary: "Build a powerful AI Agent using Gemini 3 and ADK with native support for Google Search grounding, computer use, and real-time streaming."
tags: ["Gemini 3", "ADK", "Google Search"]
canonical_url: "https://adventofagents.com/2025/12/03"
markdown_url: "https://adventofagents.com/2025/12/03.md"
video_url: "https://www.youtube.com/embed/9EGtawwvlNs"
---

# 🚀 Day 3: Gemini 3 + ADK

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/03?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day03) · [Raw Markdown](https://adventofagents.com/2025/12/03.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day03)

**Summary:** Build a powerful AI Agent using Gemini 3 and ADK with native support for Google Search grounding, computer use, and real-time streaming.

**Day 3 of Google's Advent of Agents**

Gemini 3 is Google's most intelligent model yet. In just a few minutes, you can build a powerful AI Agent using Gemini 3 and ADK with native, day-one support for its most advanced capabilities.

**What you get with ADK and Gemini 3:**

- **Google Search grounding:** Native access to real-time web data
- **Computer use:** Agents that navigate and interact with UIs
- **Live API:** Real-time streaming for voice and video agents
- **Native observability:** Full visibility into Gemini calls, tool use, and agent reasoning

**Get started with just one command:**

```bash
uvx agent-starter-pack create -y --api-key YOUR_GEMINI_API_KEY
```

No need to code from scratch. Use Gemini CLI or Antigravity IDE to generate your agent. The agent-starter-pack includes an ADK cheatsheet to guide you through everything.

**Resources:**

- Video tutorial to build an AI Agent with Gemini 3 and ADK
- GitHub repo with working code
- Complete docs for the ADK Google Search Tool

## Code & Commands

```bash
uvx agent-starter-pack create -y --api-key YOUR_GEMINI_API_KEY
```

```bash
uv init
uv add google-adk
uv add google-genai
export GOOGLE_API_KEY="YOUR_API_KEY"
source .venv/bin/activate
adk create my_agent
```

```bash
curl 'https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/refs/heads/main/ai-ml/agent-labs/gemini-3-pro-agent-demo/my_agent/agent.py' > my_agent/agent.py
adk web
```

## Resources & Links

- **[Build an AI Agent with Gemini 3 (Video)](https://www.youtube.com/watch?v=9EGtawwvlNs&list=PLOU2XLYxmsIJCVXV1bLV7qnT5hilN3YJ7&index=4&t=1s)** — Step-by-step video tutorial
- **[Gemini 3 Agent Demo (GitHub)](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/agent-labs/gemini-3-pro-agent-demo?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day03)** — Working code for the AI Agent built with Gemini 3 Pro
- **[ADK Google Search Tool Docs](https://google.github.io/adk-docs/tools/built-in-tools/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day03#google-search)** — Complete documentation for the Google Search tool
- **[Gemini 3 Announcement](https://blog.google/products/gemini/gemini-3/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day03#gemini-3)** — Official announcement on The Keyword
