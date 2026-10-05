---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 18
title: "Workspace & Gemini Enterprise: ADK agents"
summary: "Build ADK agents that use the Vertex AI Search MCP server and Google Workspace APIs, deploy them to Vertex AI, and register them with Gemini Enterprise."
tags: ["Gemini Enterprise", "Google Workspace", "ADK", "MCP", "Vertex AI"]
canonical_url: "https://adventofagents.com/2026/03/18"
markdown_url: "https://adventofagents.com/2026/03/18.md"
video_url: "https://www.youtube.com/embed/dVBvx9r-D-4"
---

# 🤖 Day 18: Workspace & Gemini Enterprise: ADK agents

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/18?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18) · [Raw Markdown](https://adventofagents.com/2026/03/18.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)

**Summary:** Build ADK agents that use the Vertex AI Search MCP server and Google Workspace APIs, deploy them to Vertex AI, and register them with Gemini Enterprise.

**Day 18 of Google's Advent of Agents — Season 2**

Yesterday we demonstrated how **Google Workspace** connectors can be used in **Gemini Enterprise** to build no-code personal agents with the Agent Designer. Today, we take the **pro-code path** and showcase:

- How to use the Google-managed **Vertex AI Search MCP server** and Google **Workspace APIs** in an ADK agent.
- How to deploy the **ADK agent to Vertex AI** Agent Engine.
- How to register the deployed **ADK agent to Gemini Enterprise** and make it accessible at an organizational level.

Note: Google Workspace-enabled ADK agents can be deployed and accessed from anywhere, you are not limited to Vertex AI Agent Engine and Gemini Enterprise. For example, we could have used Cloud Run or Google Workspace applications (Gmail, Calendar, Chat, etc.)

**Resources:**

- [Codelab: Integrate Gemini Enterprise Agents with Google Workspace](https://codelabs.developers.google.com/ge-gws-agents?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)
- [Gemini Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/docs?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)
- [Google Workspace Developers](https://developers.google.com/workspace?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)
- [Register and manage ADK agents hosted on Vertex AI Agent Engine](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)

## Code & Commands

```bash
# Google Cloud Console: Create a Gemini Enterprise application and connect Google Workspace data stores

# Download ADK agent locally
git clone https://github.com/PierrickVoulet/adk-samples.git adk-samples-advent-agents
cd adk-samples-advent-agents
git checkout origin/advent-agents
cd python/agents/enterprise-ai-agent

# Enable Google Cloud APIs
gcloud services enable \
    calendar-json.googleapis.com \
    aiplatform.googleapis.com \
    cloudresourcemanager.googleapis.com

# Enable Google Cloud Vertex AI Search MCP
gcloud beta services mcp enable discoveryengine.googleapis.com \
     --project=$(gcloud config get-value project)

# Build and deploy agent in Vertex AI Agent Engine
uv sync
uv run adk deploy agent_engine \
  --project=$(gcloud config get-value project) \
  --region=us-central1 \
  --display_name="Enterprise AI" \
  enterprise_ai

# Set up Vertex AI Reasoning Engine access to Vertex AI Search
PROJECT_ID=$(gcloud config get-value project)
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:$SERVICE_ACCOUNT" \
     --role="roles/discoveryengine.viewer"

# Google Cloud Console: Register deployed agent to Gemini Enterprise application with required OAuth accesses.
```

## Resources & Links

- **[Codelab: Integrate Gemini Enterprise Agents with Google Workspace](https://codelabs.developers.google.com/ge-gws-agents?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)** — Step-by-step guide to building the integration.
- **[Gemini Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/docs?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)** — Official documentation for Gemini Enterprise.
- **[Google Workspace Developers](https://developers.google.com/workspace?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)** — Build solutions with Google Workspace.
- **[Register and manage ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day18)** — Hosted on Vertex AI Agent Engine.
