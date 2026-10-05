---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 13
title: "Interactions API"
summary: "Interactions API marks a fundamental shift from stateless text generation to stateful, autonomous workflows."
tags: ["Interactions API", "ADK", "A2A", "Google Cloud", "Google DeepMind"]
canonical_url: "https://adventofagents.com/2025/12/13"
markdown_url: "https://adventofagents.com/2025/12/13.md"
video_url: "https://www.youtube.com/embed/kPhs6C0-JbY"
---

# ☁️ Day 13: Interactions API

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/13?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13) · [Raw Markdown](https://adventofagents.com/2025/12/13.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)

**Summary:** Interactions API marks a fundamental shift from stateless text generation to stateful, autonomous workflows.

**Day 13 of Google's Advent of Agents**

The landscape of AI development is shifting from stateless request-response cycles to stateful, multi-turn agentic workflows. 
With the beta launch of the [Interactions API](https://blog.google/technology/developers/interactions-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13), 
Google is providing a unified interface designed specifically for this new era—offering a single gateway to both raw models and the fully managed 
[Gemini Deep Research Agent](https://blog.google/technology/developers/deep-research-agent-gemini-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13).

Two ways to use this today:

1. **The "Engine" Upgrade (ADK):** By setting `use_interactions_api=True` in your ADK agent, you move the conversation history and state management to the server. This allows for background execution—perfect for long-running tasks where you don't want your client to timeout while the model "thinks."

2. **The "Bridge" (A2A):** If you have a mesh of agents speaking the Agent2Agent (A2A) protocol, you can now treat Google's hosted agents as remote peers. The new `InteractionsApiTransport` maps A2A messages directly to the Interactions API, allowing your existing clients to send tasks to the Deep Research Agent without writing custom API wrappers.


**Interactions API** marks a fundamental shift from stateless text generation to stateful, autonomous workflows.

- Instead of manually juggling context windows and fragile client-side loops, developers can now offload the entire reasoning state and history management to Google's infrastructure.
- This enables "fire-and-forget" background execution for long-running tasks, solving the timeout issues common in complex agentic chains.
- It provides a single, unified primitive for accessing both raw models and fully managed agents like Gemini Deep Research.

**Resources:**

- Read the [announcement for Gemini Interactions API](https://blog.google/technology/developers/interactions-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13) and [docs](http://ai.google.dev/gemini-api/docs/interactions-api)  
- Read the [announcement for Gemini Deep Research Agent](https://blog.google/technology/developers/deep-research-agent-gemini-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13) and [docs](https://ai.google.dev/gemini-api/docs/deep-research?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)  
- Check out the [ADK release notes](https://github.com/google/adk-python/blob/main/CHANGELOG.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13), [docs](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13) and the [ADK sample with the Interactions API](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)  
- Check out the [A2A sample which uses the Interactions API](https://github.com/a2aproject/a2a-samples/tree/interactions-api/samples/python/transports/interactions_api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)

## Code & Commands

```python
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        # Enable Interactions API
        use_interactions_api=True,
    ),
    name="interactions_test_agent",
    tools=[
        # Converted Google Search to a function tool
        GoogleSearchTool(bypass_multi_tools_limit=True),
        get_current_weather,
    ],
)
```

## Resources & Links

- **[Gemini Interactions API Announcement](https://blog.google/technology/developers/interactions-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Read the announcement for Gemini Interactions API.
- **[Gemini Interactions API Docs](https://ai.google.dev/gemini-api/docs/interactions-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Read the documentation for Gemini Interactions API.
- **[Gemini Deep Research Agent Announcement](https://blog.google/technology/developers/deep-research-agent-gemini-api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Read the announcement for Gemini Deep Research Agent.
- **[Gemini Deep Research Agent Docs](https://ai.google.dev/gemini-api/docs/deep-research?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Read the documentation for Gemini Deep Research Agent.
- **[ADK Release Notes](https://github.com/google/adk-python/blob/main/CHANGELOG.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Check out the ADK release notes.
- **[ADK Interactions API Sample](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Check out the ADK sample with the Interactions API.
- **[A2A Interactions API Sample](https://github.com/a2aproject/a2a-samples/tree/interactions-api/samples/python/transports/interactions_api?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day13)** — Check out the A2A sample which uses the Interactions API.
