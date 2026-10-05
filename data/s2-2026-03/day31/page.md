---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 31
title: "A2UI & A2A: Building the Dog Weather App"
summary: "Transform static agent responses into rich interactive micro-apps natively rendered in Gemini Enterprise using A2UI."
tags: ["A2UI", "A2A", "Gemini Enterprise", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/31"
markdown_url: "https://adventofagents.com/2026/03/31.md"
---

# 🐶 Day 31: A2UI & A2A: Building the Dog Weather App

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/31?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31) · [Raw Markdown](https://adventofagents.com/2026/03/31.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)

**Summary:** Transform static agent responses into rich interactive micro-apps natively rendered in Gemini Enterprise using A2UI.

**Day 31 of Google's Advent of Agents — Season 2**

Standard agents often hit a wall when communicating complex, stateful data through raw text or basic Markdown. This demo showcases how to leverage A2UI to deliver high-fidelity, interactive micro-apps directly within Gemini Enterprise without deploying any frontend code.

**Technical Orchestration**

By integrating A2UI templates into the system prompt, we enable the model to generate strictly validated JSON that the client renders natively. ADK orchestrates the session state and tool execution, bridging the gap between the model and the enterprise environment.

- **Declarative UI**: Uses A2UI protocol to define component trees (Cards, Columns, Rows) and data binding via `valueStruct` for efficient updates.
- **Dynamic Interaction**: Implements `sendText` actions with @-mentions to maintain session context and route button clicks reliably back to ADK.
- **Multi-modal Chaining**: Demonstrates deterministic tool chaining where ADK manages the flow between random location selection, weather retrieval, and live image fetching in a single turn.

**Resources:**

- [A2UI Specification](https://a2ui.org)
- [Google ADK Repository](https://github.com/google-gemini/adk?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)
- [Day 31 Article](https://adventofagents.com/2026/03/31?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)

## Code & Commands

### Agent Definition with A2UI

```python
from google.adk import agents
from prompt_builder import get_ui_instruction

class DogWeatherAgent(agents.LlmAgent):
    def __init__(self, **kwargs):
        # 1. Define persona with A2UI rules & schemas
        base_prompt = "You are a pun-loving weather assistant. Fetch!"
        full_instruction = get_ui_instruction(base_prompt)
        
        super().__init__(
            name="weather_agent_v2",
            model="gemini-3.1-flash-lite-preview",
            instruction=full_instruction,
            tools=[get_weather, get_random_location]
        )

# 2. Return data-bound A2UI payload via tool chaining
def get_weather(location: str):
    return {
        "location": location,
        "temp": "72°F",
        "dogImageUrl": "https://dog.ceo/api/image"
    }
```

### ADK Integration with A2A & A2UI

```python
from a2a.server.apps.jsonrpc.starlette_app import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler

# 1. Initialize ADK Agent & A2A Executor
agent = DogWeatherAgent()
agent_card = agent.create_agent_card(AGENT_URL)

# 2. Build A2A Server with ADK-to-A2A Bridge
app = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=DefaultRequestHandler(
        agent_executor=AdkAgentToA2AExecutor()
    )
).build()
```

## Resources & Links

- **[GitHub Repository](https://github.com/goabego/adventofagents-day31?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)** — Full source code for both the text-only baseline and the interactive Dog Weather App.
- **[ADK Documentation](https://github.com/google-gemini/adk?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)** — Core SDK used for tool registration and A2A lifecycle management.
- **[A2UI Introduction](https://a2ui.org/introduction/what-is-a2ui/)** — Overview of the declarative UI protocol for generative agents.
- **[A2A Agent Registration](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day31)** — Official guide on how to register and manage your custom ADK agents within Gemini Enterprise.
