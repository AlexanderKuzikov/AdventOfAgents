---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 15
title: "Introducing A2UI"
summary: "Discover A2UI (Agent-to-User Interface), an open project that enables agents to stream dynamic, generative UIs as JSONL payloads, decoupling UI definition from rendering and breaking the ceiling of traditional chat interfaces."
tags: ["A2UI", "Generative UI", "Agent-to-User Interface", "Agent Development"]
canonical_url: "https://adventofagents.com/2025/12/15"
markdown_url: "https://adventofagents.com/2025/12/15.md"
video_url: "https://www.youtube.com/embed/kJFnJr-leDI"
---

# 🚀 Day 15: Introducing A2UI

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/15?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day15) · [Raw Markdown](https://adventofagents.com/2025/12/15.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day15)

**Summary:** Discover A2UI (Agent-to-User Interface), an open project that enables agents to stream dynamic, generative UIs as JSONL payloads, decoupling UI definition from rendering and breaking the ceiling of traditional chat interfaces.

**Day 15 of Google's Advent of Agents**

🚧 **Chat interfaces have a ceiling.**
When an agent needs to collect structured data or present complex options, simple text becomes tedious.

🚀 **Today we are making A2UI (Agent-to-User Interface) available to the public.**
We decouple the UI definition from the rendering engine.
Instead of hardcoding screens, your agent generated structured outputs and streams JSON lines to the client.

The client 📲 listens to the stream and renders native components—buttons, forms, carousels.
The client controls the UI and all styling, but remote agents can make layouts for widgets and select from both a set of common component and custom components.

**What you get with A2UI:**

- 🔌 **Transport Agnostic:** Currently we have A2A but HTTP, SSE, WebSockets, etc are feasible.
- 🏗️ **Framework Agnostic:** Write once; render on Angular, React, Flutter, or Android.
- 🔒 **Security:** Native secure message format, not remote code execution.
- ✨ **Generative:** Agents can generate UI components on the fly, or hydrate existing UI components with values.

**⚠️ ️Status: Early Stage Public Preview:**

A2UI is currently in v0.8 (Public Preview). The specification and implementations are functional but are still evolving. We are opening the project to foster collaboration, gather feedback, and solicit contributions (e.g., on client renderers). Expect changes.

**Resources:**
- Check out the [A2UI Official Website](https://a2ui.org/)
- Check out the [A2UI Github Repo](https://github.com/google/a2ui?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day15)
- Check out the [A2UI Composer](https://a2ui-editor.ag-ui.com/) thanks CopilotKit / AG UI team!

## Code & Commands

```bash
git clone https://github.com/google/a2ui.git
cd a2ui
export GEMINI_API_KEY="your_gemini_api_key_here"
cd samples/client/lit
npm install
npm run demo:all
```

## Resources & Links

- **[A2UI Official Website](https://a2ui.org/)** — The official website for the A2UI project.
- **[A2UI Github Repo](https://github.com/google/a2ui?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day15)** — The Github repository for the A2UI project.
- **[A2UI Composer](https://a2ui-editor.ag-ui.com/)** — The A2UI Composer for building UI components - thanks CopilotKit / AG UI team!
