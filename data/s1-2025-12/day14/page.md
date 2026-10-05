---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 14
title: "Connecting Agents with A2A"
summary: "Connect agents across teams, frameworks, and languages with the Agent2Agent (A2A) Protocol. ADK makes implementing A2A simple."
tags: ["ADK A2A", "ADK", "A2A", "Multi-Agent", "Agent Starter Pack"]
canonical_url: "https://adventofagents.com/2025/12/14"
markdown_url: "https://adventofagents.com/2025/12/14.md"
---

# 🔗 Day 14: Connecting Agents with A2A

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/14?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14) · [Raw Markdown](https://adventofagents.com/2025/12/14.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14)

**Summary:** Connect agents across teams, frameworks, and languages with the Agent2Agent (A2A) Protocol. ADK makes implementing A2A simple.

**Day 14 of Google's Advent of Agents**

Your Customer Service Agent needs product info. Your Product Catalog Agent has it. But they're separate services, maybe even built by different teams in different languages.

How do they talk to each other?

That's exactly what the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org) solves. A2A is a standard for agents to communicate—across teams, frameworks, and languages. It shines when:

- Agents run as **separate services** (microservices architecture)
- Agents are maintained by **different teams**
- You need to connect agents in **different languages or frameworks**
- You want a **formal contract** between system components

ADK makes implementing A2A simple. To **expose** your agent, wrap it in an `A2AServer`—now other agents can discover it and send requests. To **consume** a remote agent, use `RemoteA2aAgent`. It handles network communication, auth, and data formatting. Feels just like calling a local tool.

No manual protocol work. ADK abstracts the network layer.

The easiest way to get started? [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14). You get:

- Production-ready A2A agent with discovery endpoint
- Integration and load tests included
- Terraform and CI/CD generated
- Observability pre-configured

Deploy to Agent Engine or Cloud Run. Your agent becomes a discoverable micro-service, ready to collaborate.

For a deeper dive into multi-agent architectures, check out the A2A section in the [Prototype to Production](https://www.kaggle.com/whitepaper-prototype-to-production) whitepaper.

**Resources:**

- Check out the [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14)
- Check out the [ADK A2A Docs](https://google.github.io/adk-docs/a2a/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14)
- Check out the [A2A Protocol Spec](https://a2a-protocol.org/)
- Read the [Prototype to Production Whitepaper](https://www.kaggle.com/whitepaper-prototype-to-production)

## Code & Commands

```shell
uvx agent-starter-pack create -p -a adk_a2a_base
```

## Resources & Links

- **[Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14)** — Get started with production-ready A2A agents.
- **[ADK A2A Docs](https://google.github.io/adk-docs/a2a/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day14)** — Learn how to implement A2A in the ADK.
- **[A2A Protocol Spec](https://a2a-protocol.org/)** — The official Agent2Agent protocol specification.
- **[Prototype to Production Whitepaper](https://www.kaggle.com/whitepaper-prototype-to-production)** — Deep dive into multi-agent architectures and production patterns.
