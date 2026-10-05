---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 13
title: "Multi-Agent Patterns: Iterative Refinement"
summary: "Compose Skills, MCP, and Code Execution into a meta-agent that builds, tests, and refines other ADK agents through iterative loops."
tags: ["Multi-Agent", "Agent Skills", "MCP", "Code Execution"]
canonical_url: "https://adventofagents.com/2026/03/13"
markdown_url: "https://adventofagents.com/2026/03/13.md"
video_url: "https://www.youtube.com/embed/weAygSpui4w"
---

# 🏗️ Day 13: Multi-Agent Patterns: Iterative Refinement

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/13?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13) · [Raw Markdown](https://adventofagents.com/2026/03/13.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)

**Summary:** Compose Skills, MCP, and Code Execution into a meta-agent that builds, tests, and refines other ADK agents through iterative loops.

**Day 13 of Google's Advent of Agents — Season 2**

LLMs generate broken agent code. They reach for `google.generativeai` instead of `google.adk`, use deprecated methods, and declare victory without testing. This meta-agent closes the loop by building ADK agents, testing them through code execution, and refining until everything passes.

![Architecture](/season2-day13-architecture.png)

**How It Works**

The builder composes four tool groups into a single agent, each solving a different problem in the code generation pipeline:

- **SkillToolset**: Injects curated ADK coding conventions and a custom testing protocol. Skills fix structural failures that persist despite prompt instructions.
- **McpToolset**: Connects to live ADK documentation via MCP, serving the latest API surface at generation time.
- **AgentTool + Code Executor**: ADK does not allow `code_executor` and other tools on the same agent. The workaround is wrapping `UnsafeLocalCodeExecutor` in a dedicated sub-agent and exposing it via `AgentTool`.
- **Lifecycle FunctionTools**: Four tools manage the built agent's full lifecycle to save, test, talk to, and stop the agent.

**Resources:**

- [Companion Repo](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-iterative-refinement?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)
- [ADK Skills](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)
- [ADK Code Execution](https://google.github.io/adk-docs/integrations/code-execution/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)
- [Sculptor Pattern](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)

## Code & Commands

```python
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.code_executors import UnsafeLocalCodeExecutor
from google.adk.skills import load_skill_from_dir, SkillToolset
from google.adk.tools.mcp import McpToolset, StdioConnectionParams, StdioServerParameters

# Code executor sub-agent (cannot coexist with other tools on the same agent)
code_executor_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="code_executor",
    instruction="Execute Python code exactly as provided. Return stdout and stderr.",
    code_executor=UnsafeLocalCodeExecutor(),
)

# Root agent composes all four tool groups
root_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="agent_builder",
    instruction="You are an ADK Agent Builder...",
    tools=[
        skill_toolset,        # ADK coding knowledge (3 skills)
        adk_docs_mcp,         # Live ADK documentation (MCP)
        AgentTool(agent=code_executor_agent),  # Code execution
        save_agent_code,      # Save tested code to disk
        start_agent,          # Launch as adk api_server
        talk_to_agent,        # Send messages to running agent
        stop_agent,           # Shut down running agent
    ],
)
```

```bash
# Clone and run the meta-agent
git clone https://github.com/lavinigam-gcp/build-with-adk.git
cd build-with-adk/adk-iterative-refinement
python3 -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
cp app/.env.example app/.env  # Add your GOOGLE_API_KEY
adk web app

# Then ask: "Build me a joke agent with one tool called tell_joke"
```

## Resources & Links

- **[Companion Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-iterative-refinement?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)** — Full source code with skills, tools, and demo queries.
- **[ADK Skills Documentation](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)** — How to build and load modular knowledge packages for agents.
- **[ADK Code Execution](https://google.github.io/adk-docs/integrations/code-execution/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)** — Code executor options: Unsafe Local, Container, and Agent Engine Sandbox.
- **[Sculptor Pattern (Multi-Agent Patterns in ADK)](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day13)** — Google's guide to iterative refinement and other multi-agent patterns.
