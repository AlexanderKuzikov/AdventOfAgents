---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 18
title: "Cloud API Registry + ADK"
summary: "The biggest friction in enterprise agent development isn't the model—it's the tools. Vertex AI Agent Builder now integrates with Cloud API Registry, providing a centralized tool repository."
tags: ["Cloud API Registry", "Vertex AI Agent Builder", "ADK", "Tools"]
canonical_url: "https://adventofagents.com/2025/12/18"
markdown_url: "https://adventofagents.com/2025/12/18.md"
---

# 🛠️ Day 18: Cloud API Registry + ADK

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/18?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18) · [Raw Markdown](https://adventofagents.com/2025/12/18.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)

**Summary:** The biggest friction in enterprise agent development isn't the model—it's the tools. Vertex AI Agent Builder now integrates with Cloud API Registry, providing a centralized tool repository.

**Day 18 of Google's Advent of Agents**

**Tools for Vertex AI Agent Builder - Cloud API Registry & ADK Integration**

![Tools GIF](/Tools_Demo_Agent Builder.gif)

The biggest friction in enterprise agent development isn't the model—it's the tools. 🛑 Developers waste time wrapping APIs, and admins lose sleep over unapproved data access.

**The Solution: A Centralized Tool Repository** 🏛️ Vertex AI Agent Builder now integrates with **Cloud API Registry**. This acts as a private catalog where administrators curate authorized tools and Model Context Protocol (MCP) servers.

**How it works:**

1. 👨‍💼 **Admins** enable and configure tools (like Google Maps 🗺️ or BigQuery 📊) using the console or CLI.

2. 👨‍💻 **Developers** use the new ApiRegistry object in the ADK to dynamically fetch these definitions at runtime.

This eliminates hardcoded API keys and complex client-side configuration 🔑. The agent simply "checks out" the tool from the library, fully configured and ready to run. 🚀

Get started with [Cloud API Registry on Vertex AI Agent Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_cloud_api_registry.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18).


**Resources:**

- Read the official blog post [New Enhanced Tool Governance in Vertex AI Agent Builder](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder?e=48754805%3Futm_source%3Dlinkedin&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)
- Check out the [Cloud API Registry documentation](https://docs.cloud.google.com/api-registry/docs/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)
- Try out the tutorial at [Cloud API Registry](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_cloud_api_registry.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18).
- Learn more about [Tool Governance in Vertex AI Agent Builder with the new Cloud API Registry integration](https://discuss.google.dev/t/tool-governance-in-vertex-ai-agent-builder-with-the-new-cloud-api-registry-integration/298148)
- Learn more about [Where is the MCP server? Deploy your agent with Cloud API Registry on Vertex AI Agent Engine](https://discuss.google.dev/t/where-is-the-mcp-server-deploy-your-agent-with-cloud-api-registry-on-vertex-ai-agent-engine/298130)

## Code & Commands

### Part 1: Admin setup (CLI) Enable the MCP server for your project:

```bash
gcloud beta services mcp enable bigquery.googleapis.com --project=YOUR_PROJECT_ID
```

### Part 2: Developer Implementation (Python) Fetch the managed tool dynamically using ADK:

```python
from google.adk import Agent, ApiRegistry

# 1. Connect to the Cloud API Registry
registry = ApiRegistry(project_id="your-project-id")

# 2. Fetch the specific tool (e.g., BigQuery MCP)
# This retrieves the managed tool definition directly from the registry
bq_tool = registry.get_tool("google-bigquery")

# 3. Add the tool to your Agent
# The agent now has governed access to BigQuery capabilities
agent = Agent(
    model="gemini-3-pro",
    tools=[bq_tool]
)

print("Agent configured with governed BigQuery access.")
```

## Resources & Links

- **[Cloud API Registry documentation](https://docs.cloud.google.com/api-registry/docs/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)**
- **[Get started with Cloud API Registry tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_cloud_api_registry.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)**
- **[New Enhanced Tool Governance in Vertex AI Agent Builder Blog](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder?e=48754805%3Futm_source%3Dlinkedin&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day18)**
- **[Where is the MCP server? Deploy your agent with Cloud API Registry on Vertex AI Agent Engine](https://discuss.google.dev/t/where-is-the-mcp-server-deploy-your-agent-with-cloud-api-registry-on-vertex-ai-agent-engine/298130)**
- **[Tool Governance in Vertex AI Agent Builder with the new Cloud API Registry integration](https://discuss.google.dev/t/tool-governance-in-vertex-ai-agent-builder-with-the-new-cloud-api-registry-integration/298148)**
