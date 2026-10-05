---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 9
title: "Multi-Agent Patterns: Coordinator/Dispatcher Agents"
summary: "Build high-fidelity educational video agents that maintain character and scene consistency using the Google ADK, Gemini 3.1 Pro, Nano Banana and Veo 3.1."
tags: ["Multi-Agent", "Coordinator", "Veo 3.1", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/09"
markdown_url: "https://adventofagents.com/2026/03/09.md"
video_url: "https://www.youtube.com/embed/QxzTVRYi95E"
---

# 📹 Day 9: Multi-Agent Patterns: Coordinator/Dispatcher Agents

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/09?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09) · [Raw Markdown](https://adventofagents.com/2026/03/09.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09)

**Summary:** Build high-fidelity educational video agents that maintain character and scene consistency using the Google ADK, Gemini 3.1 Pro, Nano Banana and Veo 3.1.

**Day 9 of Google's Advent of Agents — Season 2**

The **Coordinator/Dispatcher** pattern uses an LLM-based root agent to dynamically route tasks to specialist sub-agents. Unlike a hardcoded `SequentialAgent` pipeline, the Coordinator reasons about user input and decides which specialists to invoke and in what order. Here we apply it to long-form video generation, where visual consistency across shots is the core challenge.

**How It Works**

An **Orchestrator** root agent receives the user's request and dispatches work to two specialists:

- **Script Sequencer**: Converts dense documentation into natural speech, segmenting content into 8-second chunks to match **Veo 3.1's** peak performance window.
- **Video Agent**: Generates video clips using the Orchestrator's instructions and a reference frame, maintaining character and scene consistency across all chunks.

The Orchestrator coordinates the handoff between these agents, ensuring each video chunk receives the correct script segment and visual reference. The full application deploys on [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09) with [Vertex AI Agent Engine Sessions](https://docs.cloud.google.com/agent-builder/agent-engine/sessions/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09) for state management.

**Resources:**

- [GitHub Repository](https://github.com/vladkol/video-avatars-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09)
- [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09)

## Code & Commands

```bash
# 1. Clone the repository
git clone https://github.com/vladkol/video-avatars-agent
cd video-avatars-agent

# 2. Setup Virtual Environment
uv venv .venv
source .venv/bin/activate

# 3. Install Agent & MCP Dependencies
uv pip install pip
uv pip install -r agents/video_avatar_agent/requirements.txt
uv pip install -r mcp/requirements.txt

# 4. Configure Environment
cp .env-template .env
# Edit .env with your Google Cloud Project ID and GCS Bucket

# 5. Run Locally
# Start MCP Server
./deployment/run_mcp_local.sh 

# In a new terminal, run the Agent
./deployment/run_agent_local.sh

# 6. Deploy to Cloud Run
./deployment/deploy.sh
```

## Resources & Links

- **[GitHub Repository](https://github.com/vladkol/video-avatars-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09)** — Complete source code for the Video Avatar Agent.
- **[ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day09)** — Official documentation for the Agent Development Kit.
- **[Sample Output](https://youtu.be/QxzTVRYi95E)** — An 8-second demo of the generated avatar consistency.
