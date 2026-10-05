---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 5
title: "Long Term Recall: Memory Plugins"
summary: "Implement persistent semantic memory for AI agents using the GoodmemPlugin."
tags: ["ADK", "Memory", "Vector Database", "Modularity"]
canonical_url: "https://adventofagents.com/2026/03/05"
markdown_url: "https://adventofagents.com/2026/03/05.md"
video_url: "https://www.youtube.com/embed/LnTVBxhxWVA"
---

# 🧠 Day 5: Long Term Recall: Memory Plugins

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/05?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05) · [Raw Markdown](https://adventofagents.com/2026/03/05.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)

**Summary:** Implement persistent semantic memory for AI agents using the GoodmemPlugin.

**Day 5 of Google's Advent of Agents — Season 2**

Traditional agents forget everything the moment a session ends. To build truly human-centric agents, we need to move beyond volatile chat history and into **Persistent Semantic Memory**.

**How It Works**

The **GoodmemPlugin** integrates at the App layer and introduces three key capabilities:

- **The Silent Observer**: By attaching the plugin, every user message is automatically captured, converted into a vector embedding, and stored in a managed "Space." No manual `save()` calls required.
- **Context Injection (The Reflect Pattern)**: Before the LLM sees your message, the plugin runs a similarity search for the `top_k=5` most relevant memories from past sessions. If you mentioned a "walnut allergy" last Tuesday, that memory fragment is retrieved and injected directly into the current prompt's system context.
- **Zero-Shot Continuity**: The agent starts every new session with full knowledge of the user. By the time the LLM generates a response, it already knows your dietary restrictions, preferred coding style, or project history—saving tokens and eliminating repetition.

**Resources:**

- [ADK Tools and Integrations for Agents](https://google.github.io/adk-docs/integrations/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)
- [GoodMem Plugin for ADK](https://google.github.io/adk-docs/integrations/goodmem/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)
- [Supercharge your AI agents with ADK integrations](https://developers.googleblog.com/supercharge-your-ai-agents-adk-integrations-ecosystem/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)

## Code & Commands

```python
import os
from google.adk.agents import LlmAgent
from google.adk.apps import App
from goodmem_adk import GoodmemPlugin

# Attach persistent memory to the App layer
goodmem_chat_plugin = GoodmemPlugin(
    base_url=os.getenv("GOODMEM_BASE_URL"),
    api_key=os.getenv("GOODMEM_API_KEY"),
    top_k=5
)

# Agent context is automatically hydrated at runtime
root_agent = LlmAgent(
    name="root_agent",
    model="gemini-3.1-pro-preview",
    instruction="You are a Professional chef with persistent memory access."
)

app = App(name="Dietary-chef", root_agent=root_agent, plugins=[goodmem_chat_plugin])
```

## Resources & Links

- **[ADK Tools and Integrations](https://google.github.io/adk-docs/tools?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)** — Review supported tools for agent enhancement.
- **[GoodMem Plugin for ADK](https://google.github.io/adk-docs/integrations/goodmem/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day05)** — Technical specification for persistent memory plugin.
