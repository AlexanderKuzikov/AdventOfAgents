---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 12
title: "Multi-Agent Patterns: Generator-Critic Agent Loop"
summary: "Automatically refine LLM outputs using ADK's LoopAgent to orchestrate a conversation between a creative Writer and a strict Critic."
tags: ["Multi-Agent", "LoopAgent", "Quality Assurance", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/12"
markdown_url: "https://adventofagents.com/2026/03/12.md"
video_url: "https://www.youtube.com/embed/Kp0HrGst5-w"
---

# 🔁 Day 12: Multi-Agent Patterns: Generator-Critic Agent Loop

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/12?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12) · [Raw Markdown](https://adventofagents.com/2026/03/12.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12)

**Summary:** Automatically refine LLM outputs using ADK's LoopAgent to orchestrate a conversation between a creative Writer and a strict Critic.

**Day 12 of Google's Advent of Agents — Season 2**

**The Problem / Why it matters:**

LLMs hallucinate or fail strict formatting rubrics (like word count logic or structural requirements) on the first try. Manually reprompting wastes developer time.

**The Solution:**

The **Writer-Critic (Generator-Evaluator)** pattern. We pit two agents against each other: a creative Writer and a strict Critic who evaluates the draft against a rubric, iterating until perfection.

**How It Works:**

* **LoopAgent:** We wrap the Writer and Critic inside an ADK `LoopAgent`, which automatically cycles execution back-and-forth between its sub-agents up to a `max_iterations` limit.

* **output_key injection:** The Writer saves to `{latest_draft}` and the Critic saves to `{latest_feedback}`. They use these template variables in their prompts to seamlessly read each other's outputs on the next loop cycle.

* **Early Escalation:** The Critic has access to an `approve_draft` function tool. Once the Critic decides the rubric is fully passed, it calls the tool. The tool sets `tool_context.actions.escalate = True`, immediately breaking out of the loop execution early and returning the successful payload.

## Code & Commands

```python
from google.adk.agents import Agent, LoopAgent
from google.adk.tools import FunctionTool, ToolContext

def approve_draft(tool_context: ToolContext) -> dict:
    tool_context.actions.escalate = True # Breaks the loop execution early
    return {"status": "success", "message": "Approved."}

writer = Agent(
    name='writer', model='gemini-3-flash-preview',
    instruction="Revise your draft based on feedback: {latest_feedback?}",
    output_key='latest_draft'
)

critic = Agent(
    name='critic', model='gemini-3-flash-preview',
    instruction=(
        "Evaluate draft: {latest_draft}. "
        "RUBRIC: 1. Must be sci-fi. 2. Must be under 100 words. "
        "If it FAILS, provide feedback. If it PASSES perfectly, call approve_draft."
    ),
    tools=[FunctionTool(approve_draft)],
    output_key='latest_feedback'
)

root_agent = LoopAgent(name="loop", sub_agents=[writer, critic], max_iterations=4)

from google.adk.apps import App
app = App(name="critic", root_agent=root_agent)
```

## Resources & Links

- **[Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12)** — Source code for this project.
- **[LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12)** — Official documentation for LlmAgent.
- **[LoopAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12)** — Official documentation for LoopAgent.
- **[Function Tools Reference](https://google.github.io/adk-docs/tools-custom/function-tools/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day12)** — Official documentation for writing custom function tools.
