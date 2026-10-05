---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 16
title: "ADK Dev Skills: Accelerated Multiagent Triage"
summary: "Accelerate multiagent system development from scaffolding to deployment using ADK Dev Skills."
tags: ["Multiagent", "Dev Skills", "CLI"]
canonical_url: "https://adventofagents.com/2026/03/16"
markdown_url: "https://adventofagents.com/2026/03/16.md"
video_url: "https://www.youtube.com/embed/7PNOkMLAk4c"
---

# ⚡ Day 16: ADK Dev Skills: Accelerated Multiagent Triage

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/16?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16) · [Raw Markdown](https://adventofagents.com/2026/03/16.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16)

**Summary:** Accelerate multiagent system development from scaffolding to deployment using ADK Dev Skills.

**Day 16 of Google's Advent of Agents — Season 2**

Building production-ready multiagent systems requires complex scaffolding, strict evaluation, and custom deployment configurations. Manually wiring these components slows down iteration and introduces errors.

**How It Works**

By installing ADK Dev Skills into your environment, you inject expert-level ADK knowledge directly into AI coding assistants like Gemini CLI. This allows you to generate complex multi agent systems entirely through prompts.

- **`adk-scaffold`**: Automatically generates the structural boilerplate, tools directory, and GitHub Actions CI/CD workflows.
- **`adk-cheatsheet`**: Feeds precise Python API patterns to the AI for building the parent-child delegation logic between the Triage, Status, and Refund agents.
- **`adk-eval-guide`**: Structures deterministic test sets to validate that the LLM routes correctly and halts on invalid tool parameters.
- **`adk-deploy-guide`**: Automates infrastructure provisioning and deployment directly to Vertex AI Agent Engine.
- **`adk-dev-guide`**: Development lifecycle and coding guidelines.
- **`adk-observability-guide`**: Tracing, logging, and integrations.

**Resources:**

- [ADK Dev Skills](https://google.github.io/adk-docs/tutorials/coding-with-ai/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16#adk-dev-skills)
- [ADK Multi-Agent Systems](https://google.github.io/adk-docs/agents/multi-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16)

## Code & Commands

```bash
# Install ADK Dev Skills globally
npx skills add google/adk-docs/skills -y -g

# Instruct your AI assistant to use the skills
gemini run "Use adk-scaffold to build a multiagent Retail Returns system, then use adk-deploy-guide to push it to Agent Engine."
```

```python
import os
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from .tools import check_order_status, process_refund

# Sub-agents generated via ADK Dev Skills guidance
def create_status_agent() -> Agent:
    return Agent(
        name="status_agent",
        model=Gemini(model="gemini-3.1-flash"),
        instruction="Look up orders using the check_order_status tool.",
        tools=[check_order_status],
    )

def create_refund_agent() -> Agent:
    return Agent(
        name="refund_agent",
        model=Gemini(model="gemini-3.1-flash"),
        instruction="Verify order status is 'delivered' before using process_refund.",
        tools=[check_order_status, process_refund],
    )

# Parent triage agent routing logic
root_agent = Agent(
    name="triage_agent",
    model=Gemini(model="gemini-3.1-flash"),
    instruction="Route user requests to either the status_agent or refund_agent.",
    sub_agents=[create_status_agent(), create_refund_agent()],
)

app = App(name="retail_returns_app", root_agent=root_agent)
```

## Resources & Links

- **[ADK Dev Skills](https://google.github.io/adk-docs/tutorials/coding-with-ai/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16#adk-dev-skills)** — Installation and reference for all available ADK skills.
- **[ADK Multi-Agent Systems](https://google.github.io/adk-docs/agents/multi-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day16)** — Learn how to orchestrate multiagent delegation.
