---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 20
title: "ADK Agent Harness: Build a Generate-Validate-Refine Pipeline"
summary: "Build a README improvement harness that fetches a GitHub repo via MCP, generates against a quality checklist, and refines in a loop until a critic approves."
tags: ["ADK", "MCP", "Multi-Agent", "Skills"]
canonical_url: "https://adventofagents.com/2026/03/20"
markdown_url: "https://adventofagents.com/2026/03/20.md"
video_url: "https://www.youtube.com/embed/Bub9U7bQX4A"
---

# 🔧 Day 20: ADK Agent Harness: Build a Generate-Validate-Refine Pipeline

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/20?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20) · [Raw Markdown](https://adventofagents.com/2026/03/20.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)

**Summary:** Build a README improvement harness that fetches a GitHub repo via MCP, generates against a quality checklist, and refines in a loop until a critic approves.

**Day 20 of Google's Advent of Agents — Season 2**

Ask Gemini CLI or Claude Code to improve a README and you get a one-shot result: no validation against a checklist, no refinement, no guarantee the output covers installation, configuration, or API documentation. The problem is not the model — it is the harness. ADK lets you build a harness you own.

**How It Works**

The harness is a two-stage `SequentialAgent` pipeline. Stage 1 fetches and analyzes the repository via GitHub MCP. Stage 2 runs a `LoopAgent` pairing a writer and a critic until the critic approves every section or `max_iterations` is reached.

- **`SequentialAgent` + `LoopAgent`**: Execution order is defined in code, not by the model. The analyzer always runs before the writer, and the writer always runs before the critic.
- **`McpToolset` with `tool_filter`**: Connects to the GitHub MCP server with read-only access — `get_file_contents`, `search_code`, `list_commits`. The agent cannot push or modify the repository.
- **`SkillToolset`**: Loads README conventions in layers — a one-line description at startup, full checklist only when the writer activates the skill. Context stays lean until the knowledge is required.
- **`output_key`**: Passes state between agents without manual wiring. The analyzer writes `codebase_analysis`, the writer reads it and writes `current_readme`, the critic reads that and writes `criticism` — or calls `exit_loop` to stop.

Run `adk api_server .` to expose the harness as a REST endpoint, then copy the bundled skill to Gemini CLI or Claude Code. The CLI is the interface. ADK is the engine.

**Resources:**

- [ADK LoopAgent](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)
- [ADK MCP Tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)
- [ADK Skills](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)
- [ADK API Server](https://google.github.io/adk-docs/runtime/api-server/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)
- [GitHub MCP Server](https://github.com/github/github-mcp-server?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)
- [adk-samples: readme-harness](https://github.com/google/adk-samples/tree/main/python/agents/readme-harness?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)

## Code & Commands

### Run the Harness

```shell
export GITHUB_PERSONAL_ACCESS_TOKEN=your_token

# Start ADK harness as an API server
adk api_server . --port 8000

# Copy the bundled skill to Gemini CLI
cp -r cli_harness ~/.gemini/skills/cli_harness

# In Gemini CLI:
# > Improve the README for google/adk-samples

# Or for Claude Code, copy to:
# cp -r cli_harness ~/.claude/skills/cli_harness
```

### The Harness Pipeline

```python
import os, pathlib
from google.adk.agents import Agent, LoopAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.skills import load_skill_from_dir
from google.adk.tools import exit_loop
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.skill_toolset import SkillToolset
from mcp import StdioServerParameters

SKILLS_DIR = pathlib.Path(__file__).parent / "skills"

github_mcp = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx", args=["-y", "@modelcontextprotocol/server-github"],
            env={"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", "")},
        ),
    ),
    tool_filter=["get_file_contents", "search_code", "list_commits"],
)

readme_skill = SkillToolset(
    skills=[load_skill_from_dir(SKILLS_DIR / "readme-conventions")]
)

async def init_loop_state(callback_context: CallbackContext) -> None:
    if "criticism" not in callback_context.state:
        callback_context.state["criticism"] = "No previous feedback. This is the first draft."

codebase_analyzer = Agent(
    model="gemini-3-flash-preview", name="codebase_analyzer",
    instruction="Analyze the GitHub repo. Read the file tree and key source files. Output a structured summary.",
    tools=[github_mcp], output_key="codebase_analysis",
)
readme_writer = Agent(
    model="gemini-3-flash-preview", name="readme_writer",
    before_agent_callback=init_loop_state,
    instruction="Write or improve the README using {codebase_analysis}. Address all points in {criticism}.",
    tools=[readme_skill], output_key="current_readme",
)
readme_critic = Agent(
    model="gemini-3-flash-preview", name="readme_critic",
    instruction="Review {current_readme} against the checklist. Call exit_loop if all sections pass.",
    tools=[exit_loop], output_key="criticism",
)

root_agent = SequentialAgent(
    name="readme_harness",
    sub_agents=[
        codebase_analyzer,
        LoopAgent(name="refinement_loop", sub_agents=[readme_writer, readme_critic], max_iterations=3),
    ],
)
```

## Resources & Links

- **[ADK Skills](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)**
- **[ADK MCP Tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)**
- **[ADK API Server](https://google.github.io/adk-docs/runtime/api-server/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day20)**
- **[Demo Video 2](https://youtu.be/jh4kYgUSF-M)**
