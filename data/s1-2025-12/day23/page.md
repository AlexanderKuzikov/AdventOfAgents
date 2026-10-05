---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 23
title: "Durable, Resilient Agents with Google ADK + Restate"
summary: "Most agents are fragile. Durable Execution with Google ADK and Restate ensures your agent never loses context, survives crashes, and can pause execution for days."
tags: ["Durable Execution", "ADK", "Restate", "Resilient Agents"]
canonical_url: "https://adventofagents.com/2025/12/23"
markdown_url: "https://adventofagents.com/2025/12/23.md"
video_url: "https://www.youtube.com/embed/TkGFdildEXk"
---

# 🛡️ Day 23: Durable, Resilient Agents with Google ADK + Restate

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/23?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day23) · [Raw Markdown](https://adventofagents.com/2025/12/23.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day23)

**Summary:** Most agents are fragile. Durable Execution with Google ADK and Restate ensures your agent never loses context, survives crashes, and can pause execution for days.

**Day 23 of Google's Advent of Agents**

**Durable Execution: The Unkillable Agent** 🛡️

Most agents are fragile: if the process dies, the memory dies 🪦. If your server crashes while waiting for a user reply, you lose the entire context.

**Enter Durable Execution.** By combining the **Restate plugin** with Google ADK, you give your agent a persistent brain. Restate acts as a "durability engine" that wraps your code, ensuring that every step, tool call, and state change is recorded in a log-based journal.

**I'm not talking about saving state to a database manually.** I'm talking about code that can pause execution for days (waiting for a human approval signal 🚦), survive a full server reboot, and wake up exactly on the line of code where it left off.

**With the Restate Plugin, your agents can:**

- ✅ **Never lose progress** - If the pod crashes, it resumes exactly where it stopped.
- ✅ **Sleep for days** - Pause execution for human approval without keeping resources active.
- ✅ **Recover gracefully** - Automatic retries and timeouts for every tool call.
- ✅ **Simplify Logic** - Write complex, long-running workflows as standard procedural code.

**Resources:**
- Check out the [Restate Plugin](https://google.github.io/adk-docs/plugins/restate/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day23)
- Check out the [Restate Overview](https://docs.restate.dev/ai)

## Code & Commands

### CLI Commands Snippet:

```bash
#This CLI snippet gets you a local durable environment in seconds.

# 1. Get the Claims Processing sample
git clone https://github.com/restatedev/restate-google-adk-example
cd restate-google-adk-example

# 2. Start the Durable Agent (uses uv)
# The agent will register itself and wait for work
export GOOGLE_API_KEY="YOUR_KEY_HERE"
uv run .

# 3. In a new terminal, start the Restate Server
# This acts as the durable log and orchestrator
docker run --name restate --rm -p 8080:8080 -p 9070:9070   --add-host host.docker.internal:host-gateway   docker.restate.dev/restatedev/restate:latest

# 4. Open the UI to trace execution
# http://localhost:9070
```

## Resources & Links

- **[Restate Google ADK Example Repository](https://github.com/restatedev/restate-google-adk-example?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day23)**
- **[Restate Docs/Deep Dive](https://docs.restate.dev/ai)**
