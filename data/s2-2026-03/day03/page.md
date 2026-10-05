---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 3
title: "Build AI Agents with Gemini 3.1 Flash-Lite"
summary: "Announcing Gemini 3.1 Flash-Lite: our most cost-efficient model for building high-quality AI agents at scale."
tags: ["Gemini 3.1 Flash-Lite", "Product Launch", "Vertex AI", "Memory Agent"]
canonical_url: "https://adventofagents.com/2026/03/03"
markdown_url: "https://adventofagents.com/2026/03/03.md"
video_url: "https://www.youtube.com/embed/-7zEqFXg0zw"
---

# ⚡ Day 3: Build AI Agents with Gemini 3.1 Flash-Lite

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/03?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day03) · [Raw Markdown](https://adventofagents.com/2026/03/03.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day03)

**Summary:** Announcing Gemini 3.1 Flash-Lite: our most cost-efficient model for building high-quality AI agents at scale.

**Day 3 of Google's Advent of Agents — Season 2**

We’re announcing **Gemini 3.1 Flash-Lite** today, our most cost-efficient model yet, built specifically for intelligence at scale. It is a leaner, more efficient model designed for developers building high-quality AI apps while managing strict budget constraints. 

Cost and efficiency are the critical metrics for large-scale deployments. The model is cheap and low latency, making it extremely fast. Gemini 3.1 Flash-Lite delivers the ultra-low latency required to power responsive, real-time applications and high-frequency agentic workflows at a fraction of the cost. 

**Why Gemini 3.1 Flash-Lite for Always On Agents?**

This agent runs continuously. Cost and speed matter more than raw intelligence for background processing:

* **Fast:** Ultra-low latency ingestion and retrieval, required to power responsive, high-frequency agentic workflows.  

* **Cheap:** Negligible cost per session, making 24/7 operation practical.  

* **Smart:** Extracts structured data, identifies connections, and synthesizes answers.  

* **Multimodal:** Extracts structured information from 27+ file types including text, images, audio, and video.

**How it Works**

![How it works](/season2-day03-how-it-works.png)

1. **Ingest:** The agent watches a folder (auto-ingesting within 5 to 10 seconds) or API and uses Flash Lite's multimodal capabilities to extract structured data from any file.  

2. **Consolidate:** Like a human brain during sleep, the **ConsolidateAgent** runs on a timer to find connections between memories and generate cross-cutting insights.  

3. **Query:** Ask any question, and the **QueryAgent** synthesizes an answer by reading through all stored memories and consolidated insights with full citations.

**Get Started Today**

Build with Gemini 3.1 Flash-Lite and explore the Always On Memory Agent tutorial:

* **Get the Code & try it out (fork and star):** [GitHub Repo](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents/always-on-memory-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day03)  

* **Get your API Key:** Available now via [Vertex AI Studio](https://vertexai.google.com/) or [Google AI Studio](https://aistudio.google.com/).

Share the cool things you are building with Gemini 3.1 Flash-Lite.

## Code & Commands

```bash
# 1. Install
git clone https://github.com/GoogleCloudPlatform/generative-ai.git
cd generative-ai/gemini/agents/always-on-memory-agent
pip install -r requirements.txt

# 2. Set your API key
export GOOGLE_API_KEY="your-gemini-api-key"
# Get your API key from Vertex AI Studio or Google AI Studio

# 3. Start the agent
python agent.py

# That's it. The agent is now running:
# - Watching ./inbox/ for new files (text, images, audio, video, PDFs)
# - Consolidating every 30 minutes
# - Serving queries at http://localhost:8888

# 4. Feed it information

# Option A: Drop any file
echo "Some important information" > inbox/notes.txt
cp photo.jpg inbox/
cp meeting.mp3 inbox/
cp report.pdf inbox/
# Agent auto-ingests within 5-10 seconds

# Option B: HTTP API
curl -X POST http://localhost:8888/ingest \
  -H "Content-Type: application/json" \
  -d '{"text": "AI agents are the future", "source": "article"}'

# 5. Query
curl "http://localhost:8888/query?q=what+do+you+know"
```

## Resources & Links

- **[GitHub Repository](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents/always-on-memory-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day03)** — Always-On Memory Agent: Persistent, evolving memory for AI agents.
- **[Vertex AI Studio](https://vertexai.google.com/)** — Get started with Gemini 3.1 Flash-Lite on Vertex AI.
- **[Google AI Studio](https://aistudio.google.com/)** — Fastest way to build with Gemini models.
