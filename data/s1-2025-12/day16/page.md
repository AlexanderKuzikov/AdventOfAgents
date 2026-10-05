---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 16
title: "LangGraph + A2A"
summary: "Build LangGraph agents with full A2A capabilities using Agent Starter Pack. Your agent becomes instantly discoverable by other agents."
tags: ["LangGraph", "A2A", "Agent Starter Pack", "Multi-Agent"]
canonical_url: "https://adventofagents.com/2025/12/16"
markdown_url: "https://adventofagents.com/2025/12/16.md"
video_url: "https://www.youtube.com/embed/N25rAzQXkEA"
---

# 🦜 Day 16: LangGraph + A2A

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/16?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day16) · [Raw Markdown](https://adventofagents.com/2025/12/16.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day16)

**Summary:** Build LangGraph agents with full A2A capabilities using Agent Starter Pack. Your agent becomes instantly discoverable by other agents.

**Day 16 of Google's Advent of Agents**

Build LangGraph agents with A2A support!

[LangGraph](https://langchain-ai.github.io/langgraph/) is a popular framework for building stateful, multi-actor applications with LLMs. Now you can build LangGraph agents with full A2A capabilities using Agent Starter Pack.

The `langgraph_base` template in the Agent Starter Pack gives you a production-ready LangGraph agent that speaks the A2A protocol. This means:

- **A2A server out of the box**: Your LangGraph agent is instantly discoverable by other agents—regardless of what framework they use
- **Connect to any UI**: Expose your agent via A2A and plug it into chatbots, dashboards, or custom interfaces
- **Production-ready testing**: Integration and load tests included
- **Deployment ready**: Terraform and CI/CD generated for Cloud Run or Agent Engine
- **Gemini Enterprise ready**: Register your agent to Gemini Enterprise with one command

Create your agent with one command.

## Code & Commands

```shell
uvx agent-starter-pack create my-agent -a langgraph_base
```

## Resources & Links

- **[Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day16)** — Get started with production-ready LangGraph A2A agents.
- **[LangGraph Documentation](https://langchain-ai.github.io/langgraph/)** — Learn about building stateful agents with LangGraph.
- **[A2A Protocol Spec](https://a2a-protocol.org/)** — The official Agent2Agent protocol specification.
