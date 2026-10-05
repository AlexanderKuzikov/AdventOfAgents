---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 2
title: "Hello World with YAML"
summary: "Build your first AI agent with Gemini 3 in under 5 minutes without writing a single line of code."
tags: ["ADK", "YAML", "Quickstart"]
canonical_url: "https://adventofagents.com/2025/12/02"
markdown_url: "https://adventofagents.com/2025/12/02.md"
video_url: "https://www.youtube.com/embed/bPGf51XBJ44"
---

# 📝 Day 2: Hello World with YAML

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/02?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day02) · [Raw Markdown](https://adventofagents.com/2025/12/02.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day02)

**Summary:** Build your first AI agent with Gemini 3 in under 5 minutes without writing a single line of code.

**Day 2 of Google's Advent of Agents**

Build your first AI agent with Gemini 3 in under 5 minutes without writing a single line of code.

**4 lines of text = 1 working AI agent.**

No Python. No coding. Just YAML.

I'm not talking about no-code tools with limitations. I'm talking about code-first agents. The ones developers build for real world deployment.

**What you get with 4 lines of YAML:**

- A working AI agent powered by Gemini 3
- Google Search integration
- Ready to deploy
- Zero programming knowledge needed

Copy. Paste. Run with built in web UI. That's it.

**And here's where it gets interesting:**

Once you have your YAML agent, you can add:

- Built-in tools (google_search, code_execution)
- Custom Python tools (when you're ready)
- Sub-agents for complex workflows
- Multi-agent orchestration

Start simple. Scale when needed.

**What you'll build today:**

Try building a multi-agent app with MCP using Google ADK (pure YAML).

You can find helpful resources in the links section.

## Code & Commands

```bash
uvx --from google-adk adk create --type=config my_agent
uvx --from google-adk adk web my_agent/
```

## Resources & Links

- **[ADK Config Agents Documentation](https://google.github.io/adk-docs/agents/config/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day02)** — Build agents with YAML configuration
- **[Tutorial: AI Agent with Google Search (YAML)](https://x.com/Saboo_Shubham_/status/1971038699329908885)** — Step-by-step tutorial (~2 mins)
- **[Tutorial: Multi-agent app with MCP (YAML)](https://x.com/Saboo_Shubham_/status/1971763476818547010)** — Build a Multi-agent app using Google ADK
- **[Third Party MCP Tools in ADK](https://google.github.io/adk-docs/tools/third-party/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day02)** — Integrate MCP tools with your ADK agents
