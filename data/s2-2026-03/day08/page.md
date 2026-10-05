---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 8
title: "Multi-Agent Patterns: Sequential Agents"
summary: "Build predictable sequential workflows where the output of one agent goes straight to the next."
tags: ["Multi-Agent", "Sequential Pipelines", "Architecture", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/08"
markdown_url: "https://adventofagents.com/2026/03/08.md"
video_url: "https://www.youtube.com/embed/vXoDUg2UZmQ"
---

# ⚙️ Day 8: Multi-Agent Patterns: Sequential Agents

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/08?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08) · [Raw Markdown](https://adventofagents.com/2026/03/08.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08)

**Summary:** Build predictable sequential workflows where the output of one agent goes straight to the next.

**Day 8 of Google's Advent of Agents — Season 2**

The **SequentialAgent** in ADK lets you build a predictable workflow where the output of one agent goes straight to the next.

This keeps things simple because the agent does not have to guess what to do next. Since the flow is always the same, you get consistent results without the extra thinking time or randomness you might see in more complex setups.

**How it works**

- **Session state management** where one agent saves its work to an **output_key** and the next one grabs it using the raw text placeholder in the prompt.
- **Simple debugging** because the flow is just a straight line, debugging is easy since you can check the data at every single step to see exactly what happened.

Check out the [ADK Documentation: SequentialAgent](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08) for more information.

## Code & Commands

```python
from google.adk.agents import LlmAgent, SequentialAgent

# Step 1: The Reader - Ingests the PDF and normalizes the content
reader = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="PDFReader",
   instruction="Analyze the provided PDF and provide a comprehensive raw text dump of its core contents.",
   output_key="parsed_content"
)

# Step 2: The Insight Miner - Identifies key technical facts or unique points
miner = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="InsightMiner",
   instruction="""
   Review the following content: {parsed_content}
   Extract the top 5 most important technical facts, dates, or figures.
   """,
   output_key="extracted_insights"
)

# Step 3: The Synthesizer - Generates the final "TL;DR"
synthesizer = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="ExecutiveSynthesizer",
   instruction="""
   Based on these insights: {extracted_insights}
   Generate a 3-sentence 'Executive Briefing' suitable for a busy stakeholder.
   """
)

# Orchestrate the linear Assembly Line
root_agent = SequentialAgent(
   name="UniversalDocumentPipeline",
   sub_agents=[reader, miner, synthesizer]
)
```

```python
from .agent import root_agent

__all__ = ["root_agent"]
```

## Resources & Links

- **[ADK Documentation: SequentialAgent](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08)** — Official documentation for the Agent Development Kit.
- **[Multi-Agent Design Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08)** — Google Developers Blog post on multi-agent design patterns.
- **[Building Collaborative AI with ADK](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day08)** — A Developer's Guide to Multi-Agent Systems with ADK.
