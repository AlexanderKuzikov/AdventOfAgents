---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 11
title: "Multi-Agent Patterns: Hierarchical Decomposition"
summary: "Use a top-level Manager agent that utilizes an AgentTool to dynamically generate a plan before executing it."
tags: ["Multi-Agent", "Hierarchical", "Architecture", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/11"
markdown_url: "https://adventofagents.com/2026/03/11.md"
video_url: "https://www.youtube.com/embed/68EznHkK_UQ"
---

# 🪆 Day 11: Multi-Agent Patterns: Hierarchical Decomposition

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/11?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11) · [Raw Markdown](https://adventofagents.com/2026/03/11.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11)

**Summary:** Use a top-level Manager agent that utilizes an AgentTool to dynamically generate a plan before executing it.

**Day 11 of Google's Advent of Agents — Season 2**

**The Problem / Why it matters:**

Complex user requests cannot always be decomposed ahead of time. Hardcoding a static sequence of agent steps fails when the prompt requires a dynamically generated plan of attack.

**The Solution:**

The **Hierarchical Agent (Russian Doll)** pattern. We use a top-level Manager agent to orchestrate the flow, leaning on sub-agents to do the heavy lifting.

**How It Works:**

* **AgentTool:** We wrap a "Planner" LLM agent inside an `AgentTool`. The Manager calls this tool at runtime to break the complex problem into smaller, logical steps.

* **Sub-agents block:** The Manager oversees a downstream `SequentialAgent` pipeline (in this case, consisting of a Researcher and Synthesizer).

* **Autonomous Handoff:** Once the Manager receives the generated plan from the Planner tool, it activates the `SequentialAgent` execution pipeline, passing the plan as input so the workers can execute it entirely autonomously without needing a human-in-the-loop.

## Code & Commands

```python
from google.adk.tools import AgentTool
from google.adk.tools import google_search
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.apps import App

# The Planner is used purely as a tool by the Manager
planner = LlmAgent(
    name='planner',
    model='gemini-3-flash-preview',
    instruction='Break the user prompt into exactly three distinct research themes.'
)

# Define sub-agents for execution
researcher = LlmAgent(
    name='researcher', 
    model='gemini-3-flash-preview', 
    tools=[google_search], 
    instruction='Research the assigned topic step-by-step.'
)
synthesizer = LlmAgent(
    name='synthesizer', 
    model='gemini-3-flash-preview', 
    instruction='Synthesize the findings into a cohesive report.'
)

# A logical pipeline of sub-agents to handle execution
execution_pipeline = SequentialAgent(
    name='execution_pipeline',
    sub_agents=[researcher, synthesizer]
)

# The Manager orchestrates the whole flow autonomously
manager = LlmAgent(
    name='manager',
    model='gemini-3-flash-preview',
    tools=[AgentTool(planner)],
    sub_agents=[execution_pipeline],
    instruction='''
    1. Use the planner tool to create a detailed research plan based on the user's prompt.
    2. Activate your execution_pipeline sub-agent and pass the completed plan to it so it can execute it.
    '''
)

root_agent = manager
app = App(name="hierarchical", root_agent=root_agent)
```

## Resources & Links

- **[Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11)** — Source code for this project.
- **[LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11)** — Official documentation for LlmAgent.
- **[ParallelAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11)** — Official documentation for ParallelAgent.
- **[SequentialAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day11)** — Official documentation for SequentialAgent.
