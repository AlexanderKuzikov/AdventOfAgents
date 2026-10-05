---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 10
title: "Multi-Agent Patterns: Parallel Fanout and State Interpolation"
summary: "Drastically reduce latency by running independent, grounded LLM tasks concurrently and automatically synthesizing their outputs."
tags: ["Multi-Agent", "Parallel Execution", "Architecture", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/10"
markdown_url: "https://adventofagents.com/2026/03/10.md"
video_url: "https://www.youtube.com/embed/4-lr3sh2ETM"
---

# ⚡ Day 10: Multi-Agent Patterns: Parallel Fanout and State Interpolation

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/10?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10) · [Raw Markdown](https://adventofagents.com/2026/03/10.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)

**Summary:** Drastically reduce latency by running independent, grounded LLM tasks concurrently and automatically synthesizing their outputs.

**Day 10 of Google's Advent of Agents — Season 2**

Sequential LLM calls are painfully slow. In multi-agent systems involving independent tasks (like running multiple research queries), executing them one by one creates unacceptable latency. ADK **Parallel Fanout** solves this by spinning up multiple independent agents concurrently and automatically synthesizing their results.

**How It Works**

- **ParallelAgent**: Groups independent agents together so they execute simultaneously, dramatically cutting wall-clock time.
- **output_key**: Assigning an `output_key` to each parallel worker saves its return payload directly into the session state.
- **State Interpolation**: A downstream `SequentialAgent` handles synthesis. Because the parallel workers populated the state dictionary, we use `{bracket}` templating (e.g., `{healthcare_research}`) in the synthesizer's instruction prompt. No custom data-passing code required.

**Resources:**

- [ParallelAgent Documentation](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)
- [SequentialAgent Documentation](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)
- [Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)

## Code & Commands

```python
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

# 1. Define independent research agents with explicit output_keys and grounding tools
healthcare_researcher = Agent(name='healthcare_researcher', model='gemini-3-flash-preview', output_key='healthcare_research', tools=[google_search], instruction='Use the Google Search tool to...')
finance_researcher = Agent(name='finance_researcher', model='gemini-3-flash-preview', output_key='finance_research', tools=[google_search], instruction='Use the Google Search tool to...')

# 2. Fanout: Run them all concurrently
research_squad = ParallelAgent(
    name='research_squad',
    sub_agents=[healthcare_researcher, finance_researcher],
)

# 3. State Interpolation: Use `{output_key}` placeholders in the synthesizer prompt
synthesizer = Agent(
    name='synthesizer',
    model='gemini-3-flash-preview',
    instruction="Synthesize the following trends: \n\n{healthcare_research}\n\n{finance_research}",
)

# 4. Sequential block ensures fanout completes and populates state before synthesis
root_agent = SequentialAgent(
    name='root_agent',
    sub_agents=[research_squad, synthesizer],
)

from google.adk.apps import App
app = App(name="fanout", root_agent=root_agent)
```

## Resources & Links

- **[Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)** — Source code for this project.
- **[LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)** — Official documentation for LlmAgent.
- **[ParallelAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)** — Official documentation for ParallelAgent.
- **[SequentialAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day10)** — Official documentation for SequentialAgent.
