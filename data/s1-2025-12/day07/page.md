---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 7
title: "LLMs Can Execute Code: Autonomous Problem Solving"
summary: "Explore how LLMs can not only write but also execute, debug, and refine code autonomously, transforming them into powerful problem solvers."
tags: ["Code Execution", "LLMs", "Agents", "ADK"]
canonical_url: "https://adventofagents.com/2025/12/07"
markdown_url: "https://adventofagents.com/2025/12/07.md"
video_url: "https://www.youtube.com/embed/u1txECrXj6k"
---

# 💡 Day 7: LLMs Can Execute Code: Autonomous Problem Solving

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/07?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07) · [Raw Markdown](https://adventofagents.com/2025/12/07.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07)

**Summary:** Explore how LLMs can not only write but also execute, debug, and refine code autonomously, transforming them into powerful problem solvers.

**Day 7 of Google's Advent of Agents**

LLMs can write code, and in a sandbox, they can execute it too. 

Code execution is not just for vibecoding. It's one of the most effective ways to solve complex problems.

Certainly useful for math, but we aren't only talking about math. I'm talking about agents that can write, execute, debug, refine, and deliver working "tools", whenever they are needed.

**Why code execution matters for agents:**
Many times, a few lines of code is the most efficient solution. Code is deterministic. Code is precise. And code is simply another language for describing a process.

**What you get with ADK's Code Executor:**

- BuiltInCodeExecutor that works out of the box
- Runs on your local machine or in managed cloud sandboxes
- Compatible with cloud sandboxes like Agent Engine, Google Kubernetes Engine, and Daytona
- Agents can write, test, debug, and iterate on code
- Final output: either the result of code execution or the working code itself
- No complex setup. Just enable the tool.

**See it in action:**
We have some great resources to get you started.

- A new [adk-samples](https://github.com/google/adk-samples?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07) for [retail location strategy](https://github.com/google/adk-samples/tree/main/python/agents/retail-ai-location-strategy?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07) showcases code execution, along with Google Search and Google Maps
- Our [Step by step introduction notebook showing everything about Code execution](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_code_execution.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07)

This is a gold mine of information about very important skills.

## Code & Commands

```bash
git clone https://github.com/google/adk-samples.git
cd adk-samples/python/agents/retail-ai-location-strategy

cp .env.example .env
# Edit .env with your keys:
#   GOOGLE_API_KEY=your_ai_studio_key
#   GOOGLE_GENAI_USE_VERTEXAI=FALSE
#   MAPS_API_KEY=your_maps_key

# Install & Run
make install && make dev
```

```bash
# Set up Google Cloud:
gcloud auth application-default login

# Deploy to Vertex AI Agent Engine
gcloud config set project YOUR_PROJECT_ID
make backend

# Deploy to Cloud Run
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
make deploy-cloud-run
```

```python
gap_analysis_agent = LlmAgent(
    name="GapAnalysisAgent",
    model=CODE_EXEC_MODEL,
    description="Performs quantitative gap analysis using Python code execution for zone rankings and viability scores",
    instruction=GAP_ANALYSIS_INSTRUCTION,
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(
                initial_delay=RETRY_INITIAL_DELAY,
                attempts=RETRY_ATTEMPTS,
            ),
        ),
    ),

# This enables the "Code Execution" capability.
# It allows the agent to write Python, run it in a sandbox, and use the
# actual output (variables, dataframes) as the response.

    code_executor=BuiltInCodeExecutor(),
    output_key="gap_analysis",
    before_agent_callback=before_gap_analysis,
    after_agent_callback=after_gap_analysis,
)
```

## Resources & Links

- **[Get started with Code Execution on Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/docs/agent-engine/code-execution?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07)** — Learn how to integrate and use code execution with Vertex AI Agent Engine.
- **[Retail AI Location Strategy: Autonomous Site Selection & Market Analysis](https://github.com/google/adk-samples/tree/main/python/agents/retail-ai-location-strategy?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07)** — Explore a fully built case study on using AI for autonomous site selection and market analysis in retail.
- **[Everything about Code execution step by step](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_code_execution.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day07)** — A comprehensive guide to the Code Execution feature, locally and on Vertex AI Agent Engine. Learn to give agents the ability to run code in a secure environment, transforming them into capable problem-solvers.
