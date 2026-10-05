---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 12
title: "Multimodal Agents with Gemini Live API"
summary: "Explore ADK Bi-Directional Streaming: A visual guide to real-time multimodal AI agent development with WebSockets and Gemini Live."
tags: ["Bidi-streaming", "WebSockets", "Gemini Live", "AI Agent", "ADK"]
canonical_url: "https://adventofagents.com/2025/12/12"
markdown_url: "https://adventofagents.com/2025/12/12.md"
video_url: "https://www.youtube.com/embed/vLUkAGeLR1k"
---

# ✨ Day 12: Multimodal Agents with Gemini Live API

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/12?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12) · [Raw Markdown](https://adventofagents.com/2025/12/12.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)

**Summary:** Explore ADK Bi-Directional Streaming: A visual guide to real-time multimodal AI agent development with WebSockets and Gemini Live.

**Day 12 of Google's Advent of Agents**

**The magic isn't in the prompt—it's in the Event Loop.**

Most AI agents rely on HTTP (Request → Wait → Response). This introduces latency and makes "interrupting" the AI impossible. We break that cycle using **Bi-Directional Streaming**, better known as **ADK Bidi-streaming**. By opening a persistent WebSocket connection to Gemini, we create a session where client input (audio/video/text) and server output (audio/text/tool calls) flow simultaneously. We can control Gemini Live and equip it using the ADK.

![ADK Bidi-streaming Diagram](/bidi.png)

**How it works:**

- **Application Initialization:** Creates Agent, SessionService, and Runner at startup
- **Session Initialization:** Establishes Session, RunConfig, and LiveRequestQueue per connection
- **Bidirectional Streaming:** Concurrent upstream (client → queue) and downstream (events → client) tasks
- **Graceful Termination:** Proper cleanup of LiveRequestQueue and WebSocket connections

**Features:**

- **WebSocket Communication:** Real-time bidirectional streaming via /ws/{user_id}/{session_id}
- **Multimodal Requests:** Text, audio, and image/video input with automatic audio transcription
- **Flexible Responses:** Text or audio output, automatically determined based on model architecture
- **Session Resumption:** Reconnection support configured via RunConfig
- **Concurrent Tasks:** Separate upstream/downstream async tasks for optimal performance
- **Interactive UI:** Web interface with event console for monitoring Live API events
- **Google Search Integration:** Agent equipped with google_search tool

**Resources:**

- Read the blog post [ADK Bidi-streaming: A Visual Guide to Real-time Multimodal AI Agent Development](https://medium.com/google-cloud/adk-bidi-streaming-a-visual-guide-to-real-time-multimodal-ai-agent-development-62dd08c81399?postPublishedType=repub)
- Check out the [Part 1: Introduction to ADK Bidi-streaming](https://google.github.io/adk-docs/streaming/dev-guide/part1/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)
- Check out the [Part 2: Sending messages with LiveRequestQueue](https://google.github.io/adk-docs/streaming/dev-guide/part2/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)
- Check out the [Part 3: Event handling with run_live()](https://google.github.io/adk-docs/streaming/dev-guide/part3/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)
- Check out the [Part 4: Run configuration - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part4/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)
- Check out the [Part 5: Audio, Images, and Video - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part5/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)

## Code & Commands

```python
"""Google Search Agent definition for ADK Bidi-streaming demo."""

import os
from google.adk.agents import Agent
from google.adk.tools import google_search

agent = Agent(
    name="google_search_agent",
    model="gemini-2.5-flash-native-audio-preview-09-2025",
    tools=[google_search],
    instruction="You are a helpful voice assistant that can search the web."
)
```

```bash
# Clone the streaming sample for this deep dive and install
git clone https://github.com/google/adk-samples
cd adk-samples/python/agents/bidi-demo
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venvScriptsactivate
pip install -e .
export SSL_CERT_FILE=$(python -m certifi)

# Create app/.env file with your GOOGLE_API_KEY.

cd app
export SSL_CERT_FILE=$(uv run --project .. python -m certifi)
uv run --project .. uvicorn main:app --port 8000

# Open http://localhost:8000
```

## Resources & Links

- **[A developer's guide to Gemini Live API in Vertex AI](https://cloud.google.com/blog/topics/developers-practitioners/how-to-use-gemini-live-api-native-audio-in-vertex-ai?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — Two quick start templates with three production-ready apps (Open Source Code)
- **[ADK Bidi-streaming: A Visual Guide to Real-time Multimodal AI Agent Development](https://medium.com/google-cloud/adk-bidi-streaming-a-visual-guide-to-real-time-multimodal-ai-agent-development-62dd08c81399?postPublishedType=repub)** — Comprehensive article on ADK Bidi-streaming.
- **[Part 1: Introduction to ADK Bidi-streaming](https://google.github.io/adk-docs/streaming/dev-guide/part1/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — First part of the ADK Bidi-streaming series.
- **[Part 2: Sending messages with LiveRequestQueue](https://google.github.io/adk-docs/streaming/dev-guide/part2/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — Second part focusing on LiveRequestQueue.
- **[Part 3: Event handling with run_live()](https://google.github.io/adk-docs/streaming/dev-guide/part3/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — Third part covering event handling.
- **[Part 4: Run configuration - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part4/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — Documentation on ADK run configuration.
- **[Part 5: Audio, Images, and Video - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part5/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day12)** — Documentation on multimodal capabilities in ADK.
