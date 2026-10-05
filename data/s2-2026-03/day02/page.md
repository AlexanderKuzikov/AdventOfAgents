---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 2
title: "Build ADK Agents with Gemini 3.1 Pro"
summary: "Choose your language. One command. Total language flexibility. Bootstrap high-performance agents in seconds."
tags: ["ADK", "Agent Starter Pack", "Python", "Go", "TypeScript", "Java"]
canonical_url: "https://adventofagents.com/2026/03/02"
markdown_url: "https://adventofagents.com/2026/03/02.md"
---

# 💻 Day 2: Build ADK Agents with Gemini 3.1 Pro

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/02?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02) · [Raw Markdown](https://adventofagents.com/2026/03/02.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02)

**Summary:** Choose your language. One command. Total language flexibility. Bootstrap high-performance agents in seconds.

**Day 2 of Google's Advent of Agents — Season 2**

**Build your first ADK Agent with Gemini 3.1 Pro: Choose Your Language** 💻

**ADK** abstracts LLM orchestration into a unified schema for tool-calling and memory management. Instead of manual prompt engineering, a single template binds **Gemini 3.1 Pro’s** reasoning to language-native functions. Whether you are using Spring Boot or Go routines, the "Reflect" and "Observe" loops maintain strict schema adherence.

🚀 **One command. Total language flexibility.** By specification of the language flag upfront, the **Agent Starter Pack** bootstraps high-performance agents in seconds. This "Template-First" approach allows you to leverage language-specific strengths:

- **Go's** concurrency
- **Python's** RAG ecosystem
- **TypeScript's** full-stack integration
- **Java's** enterprise patterns

...without rewriting core agentic behavior.

***📚 Resource Reference**

- **Getting Started** [Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/getting-started.html)
- **Templates** [Overview](https://googlecloudplatform.github.io/agent-starter-pack/agents/overview.html)
- **Gemini 3.1** [Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02)
- **ADK Docs** [Docs](https://google.github.io/adk-docs/get-started/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02)

## Code & Commands

```bash
# Pick your language and deploy instantly 🚀
# Python
uvx agent-starter-pack@latest create my-agent -a adk

# Go
uvx agent-starter-pack@latest create my-go-agent -a adk_go

# TypeScript/Node.js
uvx agent-starter-pack@latest create my-ts-agent -a adk_ts

# Java
uvx agent-starter-pack@latest create my-java-agent -a adk_java

# Authenticate and Run
gcloud auth application-default login
cd my-agent && make install && make playground
```

## Resources & Links

- **[ADK Getting Started Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/getting-started.html)**
- **[Agent Templates Overview](https://googlecloudplatform.github.io/agent-starter-pack/agents/overview.html)**
- **[Gemini 3.1 Pro Model Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02)**
- **[ADK Official Documentation](https://google.github.io/adk-docs/get-started/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day02)**
