---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 19
title: "Register to Gemini Enterprise"
summary: "Register your agent to Gemini Enterprise! 🌐 and make it discoverable to everyone in your organization, right alongside Google's built-in agents."
tags: ["Gemini Enterprise", "Agent Starter Pack", "Deployment", "A2A"]
canonical_url: "https://adventofagents.com/2025/12/19"
markdown_url: "https://adventofagents.com/2025/12/19.md"
video_url: "https://www.youtube.com/embed/dhT2dAbRwVk"
---

# 🏢 Day 19: Register to Gemini Enterprise

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/19?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19) · [Raw Markdown](https://adventofagents.com/2025/12/19.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19)

**Summary:** Register your agent to Gemini Enterprise! 🌐 and make it discoverable to everyone in your organization, right alongside Google's built-in agents.

**Day 19 of Google's Advent of Agents**

Register your agent to Gemini Enterprise! 🌐

[Gemini Enterprise](https://cloud.google.com/gemini-enterprise?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19) is Google's intranet search 🔍, AI assistant 🤖, and agentic platform for organizations. It gives knowledge workers a single interface to access enterprise data 📊, perform tasks ✅, and work with agents—without switching between multiple tools.

The Agents Gallery 🖼️ At the heart of Gemini Enterprise is the Agents Gallery. Google-made agents like Deep Research and Data Insights live here—but you're not limited to Google's agents. You can register your own custom agents 🛠️. Once registered, your agent becomes discoverable to everyone in your organization 👥, right alongside the built-in ones.

Simple Registration ⚡ Agent Starter Pack makes registration simple.

The registration command handles everything:

- **Auto-detects agent type**: ADK on Agent Engine or A2A on Cloud Run
- **Lists available apps**: Shows which Gemini Enterprise apps you can register to
- **Fetches display name**: Pulls the name from your deployed agent
- **Direct console link**: Takes you straight to your agent in the catalog

Your agent goes from deployed to discoverable. Enterprise-wide visibility, zero friction.

## Code & Commands

```shell
# Create your agent
uvx agent-starter-pack create --adk

# Deploy it
make deploy

# Register to Gemini Enterprise
make register-gemini-enterprise
```

## Resources & Links

- **[Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19)** — Create and register agents to Gemini Enterprise.
- **[Gemini Enterprise Agents Overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19)** — Learn about agents in Gemini Enterprise.
- **[Register an ADK Agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19)** — Guide for registering ADK agents to Gemini Enterprise.
- **[Register an A2A Agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day19)** — Guide for registering A2A agents to Gemini Enterprise.
