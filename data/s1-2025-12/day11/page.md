---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 11
title: "Google Managed MCP"
summary: "Connect Agents to Google Services with Managed MCP."
tags: ["MCP", "ADK", "Google Cloud", "BigQuery", "Google Maps", "GKE", "Compute Engine"]
canonical_url: "https://adventofagents.com/2025/12/11"
markdown_url: "https://adventofagents.com/2025/12/11.md"
video_url: "https://www.youtube.com/embed/wzccErUYhTI"
---

# ☁️ Day 11: Google Managed MCP

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/11?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11) · [Raw Markdown](https://adventofagents.com/2025/12/11.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11)

**Summary:** Connect Agents to Google Services with Managed MCP.

**Day 11 of Google's Advent of Agents**

**Connect Agents to Google Services with Managed MCP.** While MCP as described in [Day 2 Kaggle AI Agent's intensive course Whitepaper](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp) has standardized how models connect to tools, the burden of maintaining community-built servers often leads to fragile, unmanaged implementations. Google’s new **Managed MCP support** eliminates this overhead by upgrading our existing API infrastructure into a unified, remote layer across Google Cloud services.

**A Unified, Governed Interface.** Instead of parsing brittle CLI output, your agents now have structured, discoverable interfaces for complex systems:

-   **Google Maps:** Provides "Grounding Lite" to give agents fresh geospatial data and routing details, preventing hallucinations about physical locations.
-   **BigQuery:** Enables agents to interpret schemas and execute queries in-place without moving massive datasets into the context window, reducing latency and security risks.
-   **GKE & Compute Engine:** Exposes infrastructure management (provisioning, resizing, diagnosing) as discoverable tools, allowing for true "Day-2" autonomous operations.

**Security built-in, not bolted on.** Because these are managed endpoints, you don't lose control. Administrators can govern access via **Google Cloud IAM** and defend against indirect prompt injection using **Google Cloud Model Armor**.

Explore the code for the [Launch My Bakery](https://github.com/google/mcp/tree/main/examples/launchmybakery?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11) demo.

**Resources:**

- Read the blog post [Announcing Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11)
- Read the [Kaggle Whitepaper: Agent Tools and Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp)
- Check out the [Launch My Bakery GitHub Example](https://github.com/google/mcp/tree/main/examples/launchmybakery?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11)

## Code & Commands

```python
import os
from google.genai import types
from google.genai.adk import Agent
from google.genai.mcp import RemoteMCPServer

# 1. Define the Fully-Managed Remote MCP Servers
#    These endpoints are now natively supported by Google's infrastructure
bigquery_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/bigquery",
    capabilities=["schema_read", "query_execute"],
    auth_token=os.getenv("GOOGLE_CLOUD_TOKEN") # Uses standard IAM
)

maps_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/maps",
    capabilities=["places_search", "routing", "elevation"],
    auth_token=os.getenv("GOOGLE_MAPS_API_KEY")
)

# 2. Initialize the ADK Agent with MCP Tools
#    The agent can now "see" your enterprise data and the real world
bakery_agent = Agent(
    model="gemini-3-pro",
    tools=[bigquery_mcp, maps_mcp],
    system_instruction="""
    You are a retail expansion scout.
    1. Query BigQuery to find high-revenue demographics.
    2. Use Google Maps to find available locations near competitors.
    3. Synthesize a recommendation for a new bakery location.
    """
)

# 3. Run the Agent
#    Gemini 3 plans the multi-step execution automatically
response = bakery_agent.run(
    "Find a location in Austin, TX with high disposable income and low competition."
)
print(response.text)
```

## Resources & Links

- **[Launch My Bakery GitHub Example](https://github.com/google/mcp/tree/main/examples/launchmybakery?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11)** — Explore the code for the "Launch My Bakery" demo.
- **[Announcing Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day11)** — Read the official announcement about MCP support for Google services.
- **[Kaggle Whitepaper: Agent Tools and Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp)** — Learn more about agent tools and interoperability with MCP in this whitepaper.
