---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 21
title: "Developer's Guide to AI Agent Protocols"
summary: "Six protocols, disambiguated. See how MCP, A2A, UCP, AP2, A2UI, and AG-UI work together to build a production-ready supply chain agent with ADK."
tags: ["MCP", "A2A", "UCP", "AP2", "A2UI", "AG-UI", "ADK", "Protocols"]
canonical_url: "https://adventofagents.com/2026/03/21"
markdown_url: "https://adventofagents.com/2026/03/21.md"
video_url: "https://www.youtube.com/embed/DAZpxBF6Zfc"
---

# 🔗 Day 21: Developer's Guide to AI Agent Protocols

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/21?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21) · [Raw Markdown](https://adventofagents.com/2026/03/21.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21)

**Summary:** Six protocols, disambiguated. See how MCP, A2A, UCP, AP2, A2UI, and AG-UI work together to build a production-ready supply chain agent with ADK.

**Day 21 of Google's Advent of Agents — Season 2**

The agent protocol landscape is exploding: MCP, A2A, UCP, AP2, A2UI, AG-UI... If the alphabet soup feels overwhelming, today's guide cuts through the noise.

This companion walkthrough follows the [Developer's Guide to AI Agent Protocols](https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21) blog post, which builds a restaurant supply chain agent using ADK by adding one protocol at a time until it can check real inventory, get specialist quotes, place orders, authorize payments, and stream interactive dashboards.

**The Six Protocols at a Glance**

| Protocol | What It Solves | Discovery |
|----------|---------------|-----------|
| **MCP** | Agent ↔ Tools & Data | Server advertises tools |
| **A2A** | Agent ↔ Agent | `/.well-known/agent-card.json` |
| **UCP** | Standardized Commerce | `/.well-known/ucp` |
| **AP2** | Payment Authorization | Typed mandates + audit trail |
| **A2UI** | Agent → Rich UI | Declarative JSON components |
| **AG-UI** | Agent → Streaming Frontend | Standardized SSE events |

**When to Use What**

- **Start with MCP**: Connect your agent to databases, APIs, and services without writing custom integration code.
- **Add A2A**: When you need to talk to remote agents built by other teams or on other frameworks.
- **Add UCP + AP2**: When your agent needs to transact (commerce + payment authorization).
- **Add A2UI**: When plain text isn't enough and your agent needs to render interactive UIs.
- **Add AG-UI**: When you need real-time streaming of tool calls and text to the frontend.

**Key Takeaway:** You don't need all six on day one. Add protocols as your requirements grow. Each one eliminates a category of custom integration code.

## Code & Commands

```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.toolbox_toolset import ToolboxToolset
from mcp import StdioServerParameters

# 1. Connect to a database via MCP Toolbox for Databases
inventory_tools = ToolboxToolset(server_url="http://localhost:5000")

# 2. Connect to Notion for recipes via MCP
notion_tools = McpToolset(connection_params=StdioConnectionParams(
    server_params=StdioServerParameters(
        command="npx", args=["-y", "@notionhq/notion-mcp-server"],
        env={"NOTION_TOKEN": "your-token"}),
    timeout=30))

# 3. Build the agent — MCP tools are discovered automatically
kitchen_agent = Agent(
    model="gemini-3-flash-preview",
    name="kitchen_manager",
    instruction="You manage a restaurant kitchen. Check inventory, look up recipes.",
    tools=[inventory_tools, notion_tools],
)
```

```python
# Turn any ADK agent into an A2A service (server side)
from google.adk.a2a.utils.agent_to_a2a import to_a2a
app = to_a2a(pricing_agent, port=8001)

# Discover and call a remote A2A agent (client side)
from a2a.client.client_factory import ClientFactory
from a2a.client.helpers import create_text_message_object

client = await ClientFactory.connect("http://pricing-agent:8001")
card = await client.get_card()
print(f"{card.name} - {card.description}")
# -> "pricing_agent - Checks today's wholesale market prices."

msg = create_text_message_object(
    content="What's today's wholesale price for salmon?")
async for response in client.send_message(msg):
    print(response)  # Task with artifacts or direct Message
```

```python
# A2UI: Agent sends declarative JSON, renderer turns it into native UI.
# 18 component primitives — same building blocks, any frontend.

a2ui_messages = [
    # 1. Create a rendering surface
    {"beginRendering": {"surfaceId": "default", "root": "card"}},

    # 2. Send the component tree (flat list, ID references)
    {"surfaceUpdate": {"surfaceId": "default", "components": [
        {"id": "card", "component": {"Card": {"child": "col"}}},
        {"id": "col", "component": {"Column": {"children": {
            "explicitList": ["title", "price", "buy"]}}}},
        {"id": "title", "component": {"Text": {"usageHint": "h3",
            "text": {"path": "name"}}}},
        {"id": "price", "component": {"Text": {"text": {"path": "price"}}}},
        {"id": "buy", "component": {"Button": {"child": "btn-label",
            "action": {"name": "purchase",
            "context": [{"key": "item", "value": {"path": "name"}}]}}}},
        {"id": "btn-label", "component": {"Text": {
            "text": {"literalString": "Buy Now"}}}},
    ]}},

    # 3. Send the data (separate from structure)
    {"dataModelUpdate": {"surfaceId": "default", "contents": [
        {"key": "name", "valueString": "Fresh Atlantic Salmon"},
        {"key": "price", "valueString": "$24.00/lb"},
    ]}},
]
```

```python
# AG-UI: Wrap any ADK agent as a streaming endpoint in 3 lines
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
from fastapi import FastAPI

ag_ui_agent = ADKAgent(adk_agent=kitchen_mgr, app_name="kitchen", user_id="chef")
app = FastAPI()
add_adk_fastapi_endpoint(app, ag_ui_agent, path="/")
# Run with: uvicorn module:app

# The SSE stream emits typed events:
# RUN_STARTED
# TOOL_CALL_START toolCallName="check_inventory"
# TOOL_CALL_RESULT content="3 lbs in stock, REORDER NEEDED"
# TOOL_CALL_END
# TEXT_MESSAGE_CONTENT delta="Based on "
# TEXT_MESSAGE_CONTENT delta="current inventory..."
# RUN_FINISHED
```

## Resources & Links

- **[Developer's Guide to AI Agent Protocols (Blog)](https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21)** — The full walkthrough with code samples for all six protocols
- **[MCP — Model Context Protocol](https://modelcontextprotocol.io/)** — Standard connection pattern for agent-to-tool integration
- **[A2A — Agent2Agent Protocol](https://a2a-protocol.org/)** — Discovery and communication between agents
- **[UCP — Universal Commerce Protocol](https://ucp.dev/)** — Standardized shopping lifecycle for agentic commerce
- **[AP2 — Agent Payments Protocol](https://github.com/google-agentic-commerce/AP2?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21)** — Payment authorization with typed mandates and audit trails
- **[A2UI — Agent-to-User Interface Protocol](https://a2ui.org/)** — Declarative JSON format for agent-generated UIs
- **[AG-UI — Agent-User Interaction Protocol](https://docs.ag-ui.com/)** — Standardized SSE streaming from agent to frontend
- **[ADK MCP Integrations](https://google.github.io/adk-docs/integrations/?topic=mcp&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day21)** — Browse available MCP integrations for ADK
