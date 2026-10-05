---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 24
title: "A2A-ify Anything"
summary: "Take any ADK or LangGraph sample and launch it with A2A on top. Layer A2A capabilities onto existing agents with a single flag."
tags: ["A2A", "Agent Starter Pack", "ADK Samples"]
canonical_url: "https://adventofagents.com/2025/12/24"
markdown_url: "https://adventofagents.com/2025/12/24.md"
video_url: "https://www.youtube.com/embed/6UUEeiX2y58"
---

# ✨ Day 24: A2A-ify Anything

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/24?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day24) · [Raw Markdown](https://adventofagents.com/2025/12/24.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day24)

**Summary:** Take any ADK or LangGraph sample and launch it with A2A on top. Layer A2A capabilities onto existing agents with a single flag.

**Day 24 of Google's Advent of Agents**

A2A-ify anything! Take any ADK or LangGraph sample and launch it with A2A on top.

The [google/adk-samples](https://github.com/google/adk-samples?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day24) repository contains ready-to-use agents built with the Agent Development Kit. You'll find agents for deep research, customer service, data engineering, financial advising, travel planning, and more—covering a range of real-world use cases.

These samples are great starting points. But what if you need your agent to collaborate with other agents, or connect to different UIs?

That's where Agent Starter Pack comes in. You can now layer A2A on top of any ADK sample with a single flag. This takes any sample (deep-search, customer-service, data-science, travel-concierge) and wraps it with full A2A capabilities:

- **Auto-generated agent card**: The A2A metadata is created for you
- **A2A endpoint exposed**: Your agent can receive requests from other agents or UIs
- **Production infrastructure**: Terraform, CI/CD, and observability included

You get the best of both worlds: a proven sample agent, ready for multi-agent collaboration.

Already have an agent? Use the 
`enhance`
 command to add A2A capabilities to your existing code.

## Code & Commands

```shell
# Create with A2A from a sample
uvx agent-starter-pack create my-agent     -a adk@deep-search     --base-template adk_a2a_base

# Or enhance an existing agent
uvx agent-starter-pack enhance --base-template adk_a2a_base
```

## Resources & Links

- **[ADK Samples](https://github.com/google/adk-samples?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day24)** — Ready-to-use agents built with the Agent Development Kit.
- **[Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day24)** — Add A2A capabilities to any agent.
- **[A2A Protocol Spec](https://a2a-protocol.org/)** — The official Agent2Agent protocol specification.
