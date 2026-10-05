---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 4
title: "Source-Based Deployment"
summary: "Deploy your agents directly from source code with Agent Engine - no more serialization headaches."
tags: ["Agent Engine", "Deployment", "ADK"]
canonical_url: "https://adventofagents.com/2025/12/04"
markdown_url: "https://adventofagents.com/2025/12/04.md"
video_url: "https://www.youtube.com/embed/8RjzMG3BKA0"
---

# 🚀 Day 4: Source-Based Deployment

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/04?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day04) · [Raw Markdown](https://adventofagents.com/2025/12/04.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day04)

**Summary:** Deploy your agents directly from source code with Agent Engine - no more serialization headaches.

**Day 4 of Google's Advent of Agents**

Agent Engine now supports source-based deployment. Your source code deploys directly to production, eliminating common deployment friction.

**No more dealing with:**

- Pickle errors
- Serialization nightmares
- Module path headaches

What runs locally now runs in production. The gap between development and deployment is gone.

**Get started with Agent Starter Pack:**

For a new project:

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
```

Already have an ADK agent? Use enhance:

```bash
uvx agent-starter-pack enhance --d agent_engine
```

Then run `make deploy` and you're done.

**Resources:**

- Video walkthrough of source-based deployment
- Agent Starter Pack repository
- Agent Engine deployment documentation

## Code & Commands

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
cd my-agent && make deploy
```

```bash
uvx agent-starter-pack enhance --d agent_engine
```

## Resources & Links

- **[Source-Based Deployment Tutorial (Video)](https://youtu.be/8RjzMG3BKA0)** — Step-by-step video walkthrough
- **[Agent Starter Pack](https://goo.gle/agent-starter-pack)** — Quickstart tool for building and deploying agents
- **[Agent Engine Deployment Docs](https://cloud.google.com/products/agent-engine?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day04#deploy)** — Official documentation for Agent Engine deployment
