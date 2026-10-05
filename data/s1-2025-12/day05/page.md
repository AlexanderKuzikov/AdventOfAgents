---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 5
title: "Production Observability"
summary: "Agent Starter Pack includes production-grade observability with zero config. Cloud Trace, Log Analytics, and BigQuery integration out of the box."
tags: ["Observability", "Cloud Trace", "BigQuery", "Terraform"]
canonical_url: "https://adventofagents.com/2025/12/05"
markdown_url: "https://adventofagents.com/2025/12/05.md"
video_url: "https://www.youtube.com/embed/Q5CXbwkHHns"
---

# 📊 Day 5: Production Observability

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/05?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day05) · [Raw Markdown](https://adventofagents.com/2025/12/05.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day05)

**Summary:** Agent Starter Pack includes production-grade observability with zero config. Cloud Trace, Log Analytics, and BigQuery integration out of the box.

**Day 5 of Google's Advent of Agents**

Your agent is deployed. But what's it actually doing?

Agent Starter Pack now includes production observability. Zero config required.

Full production-grade observability that enterprises need, built-in from day one.

**Two levels of observability, automatically configured:**

**1. Agent Telemetry**
- Cloud Trace captures every execution
- LLM calls with latency breakdown
- Tool execution timing
- Full conversation flow visibility

**2. Prompt-Response Logging (Auto-enabled)**
- Full E2E journey provisioned via Terraform
- Log Analytics + Log Buckets with custom retention
- BigQuery Delta Lake with custom views for easy querying
- No sensitive data in logs - all content written to GCS

**Deploy with one command:**

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
make deploy
```

Most teams spend weeks setting up observability infrastructure. You get it in minutes. No configuration. No setup. No custom instrumentation. Just deploy and start monitoring.

## Code & Commands

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
make deploy
```

## Resources & Links

- **[Observability Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/observability.html)** — Complete documentation on production observability
- **[Agent Starter Pack GitHub](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day05)** — Full source code and repository
