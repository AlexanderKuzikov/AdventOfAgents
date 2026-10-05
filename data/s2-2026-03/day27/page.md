---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 27
title: "Scion: an open testbed for agent orchestration"
summary: "Explore multi-agent patterns with an agnostic supra-harness system that isolates agents in git worktrees and containers, allowing easy orchestration and communication"
tags: ["Multiagent", "Harness Engineering", "CLI"]
canonical_url: "https://adventofagents.com/2026/03/27"
markdown_url: "https://adventofagents.com/2026/03/27.md"
video_url: "https://www.youtube.com/embed/T93MW7wETOc"
---

# 🌱 Day 27: Scion: an open testbed for agent orchestration

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/27?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day27) · [Raw Markdown](https://adventofagents.com/2026/03/27.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day27)

**Summary:** Explore multi-agent patterns with an agnostic supra-harness system that isolates agents in git worktrees and containers, allowing easy orchestration and communication

**Day 27 of Google's Advent of Agents — Season 2**


**What is Scion**

Scion is a container-based orchestration platform for managing concurrent LLM-powered deep agents across local machines and remote clusters. It enables developers to run groups of specialized agents in parallel — each with isolated identities, credentials, and workspaces — to tackle tasks like coding, research, auditing, and testing simultaneously. It's goal is to provide an open experimental testbed to explore multi-agent orchestration patterns.

**How It Works**

- **Container-isolated agents** — Each agent runs in its own OCI container with a dedicated home directory, environment, and credentials, preventing cross-contamination between concurrent sessions.
- **Harness abstraction** — A unified CLI ('start', 'stop', 'attach', 'resume') works consistently across supported LLM tools including Gemini CLI, ADK, Claude Code, OpenAI Codex, and OpenCode.
- **Git worktree workspaces** — Every agent gets an independent git worktree and feature branch, allowing multiple agents to modify the same repository concurrently without conflicts.
- **Pluggable runtimes** — Supports Docker, Podman, Apple Virtualization Framework, and Kubernetes as execution backends, scaling from a single laptop to production clusters.
- **Hub + Runtime Broker architecture** — An optional centralized Hub coordinates state, authentication, and orchestration across distributed Runtime Brokers, enabling multi-user and multi-machine deployments.
- **Template system** — Agents are created from customizable templates that define system prompts, tools, and configurations, allowing specialized roles like "Security Auditor" or "React Specialist."
- **Interactive and detached modes** — Agents can run in the background and be attached to on-demand for human-in-the-loop intervention, with a layered state model (phase, activity, detail) providing real-time observability.

**Resources:**

- [Code Repository](https://github.com/GoogleCloudPlatform/scion?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day27)
- [Docs](https://googlecloudplatform.github.io/scion/overview/)
- [Relics of Athenaeum - demo agent game](https://github.com/ptone/scion-athenaeum?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day27)

## Code & Commands

```bash
# Prerequisites
# - golang toolchain go.dev 
# - a container runtime (podman suggested) podman.io
# - The github CLI cli.github.com

# Scion is open source, but we aren't able to provide pre-built images. Github makes it pretty easy
# But it does take some time

# Get your Github username 
export GH_USER=$(gh api user --jq '.login')

# Fork the repo
gh repo fork GoogleCloudPlatform/scion --clone=false

# Disable the docs workflow in your fork
gh workflow disable "Build and Deploy Documentation" --repo $GH_USER/scion

# Build the images
gh workflow run build-images.yml --repo $GH_USER/scion -f registry=ghcr.io/$GH_USER/scion -f target=all

# Go get a snack - this build step takes about 1.5 hours

# Install the scion cli
go install github.com/GoogleCloudPlatform/scion/cmd/scion@latest

# Initialize your machine, you will enter your github registry ghcr.io/$GH_USER/scion
scion init --global

create a test local 'grove'

mkdir my-project
cd my-project
scion init


# start your first agent

scion start my-agent

# attach to your agent

scion attach my-agent

# Note you will then use tmux keys to detach
# use C-b d (means hold control key, type 'b' then release and type d)
```

## Resources & Links

- **[Open Source Repo](https://github.com/GoogleCloudPlatform/scion?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day27)** — Scion on github
- **[Documentation](https://googlecloudplatform.github.io/scion/overview/)** — Scion Documentation
