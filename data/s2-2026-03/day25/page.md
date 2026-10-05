---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 25
title: "Agent Deployment: How to Deploy AI Agents"
summary: "Deploy your AI agents to Vertex AI Agent Engine or Google Cloud Run securely and easily."
tags: ["Deployment", "Agent Engine", "Cloud Run", "Vertex AI"]
canonical_url: "https://adventofagents.com/2026/03/25"
markdown_url: "https://adventofagents.com/2026/03/25.md"
video_url: "https://www.youtube.com/embed/osEDoYe60E8"
---

# 🚀 Day 25: Agent Deployment: How to Deploy AI Agents

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/25?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25) · [Raw Markdown](https://adventofagents.com/2026/03/25.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)

**Summary:** Deploy your AI agents to Vertex AI Agent Engine or Google Cloud Run securely and easily.

**Day 25 of Google's Advent of Agents — Season 2**

As Generative AI shifts from prototyping to production, developers face the challenge of robustly hosting and scaling their AI agents. Knowing the correct pathways to deploy ensures your agent transitions seamlessly from a local playground to highly available cloud infrastructure.

**How It Works**

ADK abstracts away complex infrastructure boilerplate, allowing you to deploy to either Agent Engine or Cloud Run with just a few commands. Here is how you execute deployments for both targets using ADK.

**Deploying to Vertex AI Agent Engine**

Agent Engine is the recommended target if your project was scaffolded using the agent-starter-pack. This automatically packages your `app/` directory, resolves dependencies via `uv`, and pushes the reasoning engine to Vertex AI.

- **Dependencies**: Exported and resolved via `uv`.
- **Packaging**: A tarball of your `app/` source packages is created in-memory.
- **Provisioning**: ADK provisions the reasoning engine on Google Cloud in 3-5 minutes.
- **Metadata**: A deployment JSON file (`deployment_metadata.json`) is populated with your remote agent ID.

**Deploying to Google Cloud Run**

Cloud Run is ideal if you need your agent to run as a serverless container, responding to standard HTTP requests, Webhooks, or Eventarc triggers.

- **Initialization**: ADK copies your agent source code and automatically generates a Dockerfile for your application.
- **Configuration**: An interactive prompt asks you to select your preferred Google Cloud region.
- **Access Control**: You will be prompted on whether to allow unauthenticated invocations.
- **Deployment**: The container is built via Cloud Build and deployed directly to Cloud Run.

**Resources:**

- [Google Cloud ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)
- [Google Cloud Run Documentation](https://cloud.google.com/run?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)
- [Vertex AI Agent Engine Documentation](https://cloud.google.com/vertex-ai/docs?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)
- [Github Project Repository](https://github.com/lekan2001/advent-of-agents-day-25.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)

## Code & Commands

### Deploy to Agent Engine

```bash
# Setup project using Agent starter pack
uvx agent-starter-pack create

# Deploy to Vertex AI Agent Engine
make deploy
```

### Deploy to Cloud Run

```bash
# Explicitly install dependencies via make
make install

# Deploy to Cloud Run targeting the 'app' directory
uv run adk deploy cloud_run app
```

## Resources & Links

- **[Google Cloud ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)** — Documentation for the Google Cloud Agent Development Kit.
- **[Google Cloud Run Documentation](https://cloud.google.com/run?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)** — Learn how to run serverless containers with Cloud Run.
- **[Vertex AI Agent Engine Documentation](https://cloud.google.com/vertex-ai/docs?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)** — Documentation for Vertex AI and Agent Engine.
- **[GitHub Project Repository](https://github.com/lekan2001/advent-of-agents-day-25.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day25)** — Source code for Day 25.
