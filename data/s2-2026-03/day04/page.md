---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 4
title: "MCP Servers: Add external tools to your agents in just a few lines"
summary: "Wire up multiple MCP servers simultaneously to trace bugs from Linear to GitHub PRs."
tags: ["Code Analysis", "Tool Call", "MCP", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/04"
markdown_url: "https://adventofagents.com/2026/03/04.md"
video_url: "https://www.youtube.com/embed/to4k4aPlYDw"
---

# 🐞 Day 4: MCP Servers: Add external tools to your agents in just a few lines

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/04?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04) · [Raw Markdown](https://adventofagents.com/2026/03/04.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)

**Summary:** Wire up multiple MCP servers simultaneously to trace bugs from Linear to GitHub PRs.

**Day 4 of Google's Advent of Agents — Season 2**

Connecting a single external tool to an agent is useful, but routing context across multiple specialized tools unlocks complex workflows. 🌐 

The **Model Context Protocol (MCP)** standardizes how agents access these diverse data sources. By configuring our triage agent with both the **GitHub** and **Linear** MCP servers simultaneously, it can cross-reference system records natively without manual intervention! 🤖✨

**🐛 The Triaging Workflow**

When diagnosing a reported bug, developers typically piece together context across issue trackers and version control. We can automate this painful triaging process:

1. **Bug Extraction:** The agent first queries the `[Linear MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/linear?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)` to extract the details of a specific bug report. 📋

2. **Context Routing:** Using those identifiers or branch names, the agent seamlessly pivots to query the `[GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)` to locate the corresponding pull request. 🔀

3. **Analysis & Summary:** Finally, it analyzes the code diffs and summarizes the exact changes introduced, bridging the gap between the product issue and the committed code. 🔍💻.  

Say goodbye to context-switching between tabs! 🎉

## Code & Commands

```python
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.apps import App
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
import os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
LINEAR_API_KEY = os.environ.get("LINEAR_API_KEY")

root_agent = Agent(
    model=Gemini(model="gemini-3-flash-preview"),
    name="root_agent",
    instruction=open(os.path.join(os.path.dirname(__file__), "prompt.md")).read(),
    tools=[
        McpToolset(
            tool_name_prefix="github_",
            connection_params=StreamableHTTPServerParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "pull_requests",
                    "X-MCP-Readonly": "true"
                },
            ),
        ),
        McpToolset(
            tool_name_prefix="linear_",
            tool_filter=["get_issue", "list_issues", "search_issues"],
            connection_params=StreamableHTTPServerParams(
                url="https://mcp.linear.app/mcp",
                headers={
                    "Authorization": f"Bearer {LINEAR_API_KEY}",
                },
            ),
        )
    ],
)

app = App(
    name="app",
    root_agent=root_agent,
)
```

```markdown
You are an intelligent agent that can fetch the source diff of a Pull Request based on the Linear issue ID. Your exact workflow is:
1. Use `linear_get_issue` to fetch the specific bug report in Linear.
2. Extract keywords, branch names, or the exact title from the Linear issue.
3. Use `github_list_pull_requests` or `github_search_pull_requests` in the provided GitHub repository using those extracted keywords to find the associated Pull Request. Important: Always restrict your search to the user's provided repository (e.g. `repo:rovindra/web-master`) rather than searching globally. Do not search by the literal Linear issue ID unless you know it's in the PR title.
4. Use `github_pull_request_read` to fetch the source diff of that exact PR.
5. Summarize the diff based on the PR contents.

When returning the final response, you MUST format the details as a markdown table followed by the diff summary:
| Field | Details |
|---|---|
| **Title** | [PR Title] |
| **Author** | [PR Author] |
| **Branch** | [PR Branch] |
| **Date** | [PR Date] |
| **Files Changed** | [PR No. of Files Changed] |
| **State** | [Open/Merged/Closed] |
| **Issue** | [Linear Issue ID & Title] |
| **Description** | [Brief PR Description] |
| **Summary** | [Your brief summary of the changes] |

### Diff Analysis
[Detailed explanation of the code changes...]

### Diff
[Actual diff of the changes...]

Never ask the user for a PR number if they already provided the target GitHub repository and Linear issue ID.
```

## Resources & Links

- **[Developer Blog](https://developers.googleblog.com/en/supercharge-your-ai-agents-adk-integrations-ecosystem/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)** — Supercharge your AI Agents: Details on ADK Integrations Ecosystem
- **[Model Context Protocol Documentation](https://modelcontextprotocol.io/)** — Standardizing how agents access diverse data sources
- **[GitHub MCP Server](https://google.github.io/adk-docs/integrations/github?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)** — GitHub MCP Server implementation
- **[Linear MCP Server](https://google.github.io/adk-docs/integrations/linear?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day04)** — Linear MCP Server implementation
