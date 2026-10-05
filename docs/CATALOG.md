# Каталог Advent of Agents

Все три сезона, собранные скриптом `prepare.py` из официального манифеста
`adventofagents.com/.well-known/mcp.json` и API сезонов.

Статусы: ✅ переведён · 🟡 субтитры скачаны, ждёт перевода · ⚪ видео нет или недоступно

Всего дней: **60**, с субтитрами: **38**, переведено: **4**

## Темы

**ADK** (36) · **Multi-Agent** (11) · **A2A** (8) · **MCP** (6) · **Agent Starter Pack** (5) · **Architecture** (5) · **Gemini Enterprise** (5) · **Security** (4) · **A2UI** (3) · **Agent Engine** (3) · **BigQuery** (3) · **CLI** (3) · **Deployment** (3) · **Launch** (3) · **Memory** (3) · **Skills** (3) · **Vertex AI** (3) · **Authentication** (2) · **Code Execution** (2) · **Gemini 3** (2) · **Gemini Live** (2) · **Google Cloud** (2) · **Google Workspace** (2) · **Governance** (2) · **LangGraph** (2) · **Model Armor** (2) · **Multiagent** (2) · **Python** (2) · **Vector Search** (2)

## s1-2025-12

### day01 — Launch Initiative  
🟡 · Launch

25 days. Zero to Production-Ready AI Agents on Google Cloud.

Ссылки:
- [Introduction to Agents Whitepaper](https://www.kaggle.com/whitepaper-introduction-to-agents) — Released as part of the 5 Days of Agents with Kaggle
- [Google ADK Documentation](https://google.github.io/adk-docs/) — Official documentation for the Agent Development Kit
- [Agent Engine on Vertex AI](https://cloud.google.com/products/agent-builder) — Deploy and manage agents at scale with Vertex AI
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Production-ready templates for building AI agents

Видео: <https://www.youtube.com/watch?v=aYG7h20YNB0>

---

### day02 — Hello World with YAML  
⚪ · ADK, YAML, Quickstart

Build your first AI agent with Gemini 3 in under 5 minutes without writing a single line of code.

Ссылки:
- [ADK Config Agents Documentation](https://google.github.io/adk-docs/agents/config/) — Build agents with YAML configuration
- [Tutorial: AI Agent with Google Search (YAML)](https://x.com/Saboo_Shubham_/status/1971038699329908885) — Step-by-step tutorial (~2 mins)
- [Tutorial: Multi-agent app with MCP (YAML)](https://x.com/Saboo_Shubham_/status/1971763476818547010) — Build a Multi-agent app using Google ADK
- [Third Party MCP Tools in ADK](https://google.github.io/adk-docs/tools/third-party/) — Integrate MCP tools with your ADK agents

Код (`terminal`):

```bash
uvx --from google-adk adk create --type=config my_agent
uvx --from google-adk adk web my_agent/
```

Видео: <https://www.youtube.com/watch?v=bPGf51XBJ44>

---

### day03 — Gemini 3 + ADK  
🟡 · Gemini 3, ADK, Google Search

Build a powerful AI Agent using Gemini 3 and ADK with native support for Google Search grounding, computer use, and real-time streaming.

Ссылки:
- [Build an AI Agent with Gemini 3 (Video)](https://www.youtube.com/watch) — Step-by-step video tutorial
- [Gemini 3 Agent Demo (GitHub)](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/agent-labs/gemini-3-pro-agent-demo) — Working code for the AI Agent built with Gemini 3 Pro
- [ADK Google Search Tool Docs](https://google.github.io/adk-docs/tools/built-in-tools/#google-search) — Complete documentation for the Google Search tool
- [Gemini 3 Announcement](https://blog.google/products/gemini/gemini-3/#gemini-3) — Official announcement on The Keyword

Код (`One liner with Agent Starter Pack`):

```bash
uvx agent-starter-pack create -y --api-key YOUR_GEMINI_API_KEY
```

Код (`Using ADK CLI`):

```bash
uv init
uv add google-adk
uv add google-genai
export GOOGLE_API_KEY="YOUR_API_KEY"
source .venv/bin/activate
adk create my_agent
```

Код (`Download sample and run locally`):

```bash
curl 'https://raw.githubusercontent.com/GoogleCloudPlatform/devrel-demos/refs/heads/main/ai-ml/agent-labs/gemini-3-pro-agent-demo/my_agent/agent.py' > my_agent/agent.py
adk web
```

Видео: <https://www.youtube.com/watch?v=9EGtawwvlNs>

---

### day04 — Source-Based Deployment  
⚪ · Agent Engine, Deployment, ADK

Deploy your agents directly from source code with Agent Engine - no more serialization headaches.

Ссылки:
- [Source-Based Deployment Tutorial (Video)](https://youtu.be/8RjzMG3BKA0) — Step-by-step video walkthrough
- [Agent Starter Pack](https://goo.gle/agent-starter-pack) — Quickstart tool for building and deploying agents
- [Agent Engine Deployment Docs](https://cloud.google.com/products/agent-engine#deploy) — Official documentation for Agent Engine deployment

Код (`Create new project with Agent Starter Pack`):

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
cd my-agent && make deploy
```

Код (`Enhance existing ADK agent`):

```bash
uvx agent-starter-pack enhance --d agent_engine
```

Видео: <https://www.youtube.com/watch?v=8RjzMG3BKA0>

---

### day05 — Production Observability  
⚪ · Observability, Cloud Trace, BigQuery, Terraform

Agent Starter Pack includes production-grade observability with zero config. Cloud Trace, Log Analytics, and BigQuery integration out of the box.

Ссылки:
- [Observability Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/observability.html) — Complete documentation on production observability
- [Agent Starter Pack GitHub](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Full source code and repository

Код (`Deploy with observability`):

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
make deploy
```

Видео: <https://www.youtube.com/watch?v=Q5CXbwkHHns>

---

### day06 — 🧑‍💻 ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more  
🟡 · ANTIGRAVITY, CLI, IDE, ADK

Building agents shouldn't require an hour of environment configuration. If you use the Agent Starter Pack you already have IDE magnet context baked in for the Agent Development Kit (ADK).

Ссылки:
- [Antigravity](https://antigravity.google/) — Antigravity IDE
- [ADK Documentation llms.txt](https://google.github.io/adk-docs/llms.txt) — ADK Documentation llms.txt file
- [ADK Cheat Sheet](https://googlecloudplatform.github.io/agent-starter-pack/guide/installation.html) — ADK Cheat Sheet from Agent Starter Pack
- [llms.txt explanation](https://llmstxt.org/) — Explanation of llms.txt
- [Video: ADK ready in Antigravity, Gemini CLI, Cursor, Firebase Studio and more](https://www.youtube.com/watch) — YouTube video demonstrating ADK integration.
- [Bonus: Gemini made Code Wiki](https://codewiki.google/github.com/google/adk-go) — Want all the documentation in one url for a human or a giant context window? This is a cool resource for any public repo, in this case ADK Go!

Код (`Antigravity Commands.sh`):

```bash
# Using ADK and Agent Starter Pack within Antigravity
uvx agent-starter-pack create deep_search --adk
# nothing else
```

Код (`Visual Studio Code.sh`):

```bash
# Install dependencies
pip install pydantic-ai
gemini extensions install https://github.com/derailed-dash/adk-docs-ext
gemini
```

Код (`Gemini CLI.sh`):

```bash
fetch from https://google.github.io/adk-docs/llms.txt
How do I create a function tool using Agent Development Kit?
```

Видео: <https://www.youtube.com/watch?v=Ep8usBDUTtA>

---

### day07 — LLMs Can Execute Code: Autonomous Problem Solving  
🟡 · Code Execution, LLMs, Agents, ADK

Explore how LLMs can not only write but also execute, debug, and refine code autonomously, transforming them into powerful problem solvers.

Ссылки:
- [Get started with Code Execution on Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/docs/agent-engine/code-execution) — Learn how to integrate and use code execution with Vertex AI Agent Engine.
- [Retail AI Location Strategy: Autonomous Site Selection & Market Analysis](https://github.com/google/adk-samples/tree/main/python/agents/retail-ai-location-strategy) — Explore a fully built case study on using AI for autonomous site selection and market analysis in retail.
- [Everything about Code execution step by step](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_code_execution.ipynb) — A comprehensive guide to the Code Execution feature, locally and on Vertex AI Agent Engine. Learn to give agents the ability to run code in a secure environment, transforming them into capable problem-solvers.

Код (`Local Set up.sh`):

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

Код (`(Optional) Cloud Run or Agent Engine Deployment.sh`):

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

Код (`Sample Code BuiltInCodeExecutor.py`):

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

Видео: <https://www.youtube.com/watch?v=u1txECrXj6k>

---

### day08 — Effective Context Management with ADK Layers  
🟡 · Context Management, Layers, Caching

ADK Context design thesis: context as a compiled view

Ссылки:
- [Architecting efficient context-aware multi-agent framework for production](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) — Design principles from an ADK Tech Lead: Context is a compiled view over a richer stateful system.
- [ADK Context Documentation](https://google.github.io/adk-docs/context/) — Learn about working with context in the ADK in the official docs.
- [The ADK Prompting Pattern: Static vs. Turn Instructions](https://medium.com/google-cloud/the-adk-prompting-pattern-static-vs-turn-instructions-7a1e5b25eeef) — A deep dive into static vs. turn instructions (code examples from this article).
- [Context Engineering: Sessions & Memory | Kaggle](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory) — Day 3 of the Kaggle course on AI Agents is all about context management.
- [A longer NotebookLM summary of ADK context management](https://youtu.be/eQDx90dVc38) — 8 minute video summary of context management and how ADK solves it.
- [ADK Context Engineering Infographic](https://adventofagents.com/aoa-day8-art-of-context-engineering-with-adk.png) — NotebookLM generated infographic summarizing ADK context engineering.

Код (`app_setup.py`):

```python
# An Example of Static Context Policy 
from google.adk.apps import App
from google.adk.agents import Agent
from google.adk.agents.context_cache_config import ContextCacheConfig

STATIC_POLICY_HEADER = """You are a strict policy assistant for internal compliance Q&A.

Follow this exact JSON schema in every response:
{"answer": str, "citations": [str], "confidence": float}

Safety:
- Never provide medical or legal advice; refuse with a brief explanation.
- Never invent policy numbers or sections; ask for the missing reference.

Style:
- Use short sentences.
- Prefer active voice.
- If uncertain, say so and request the missing input.

Tools:
- search: use for public web facts.
- bq: use for internal policy tables (read-only).
"""

agent = Agent(
    name="policy_agent",
    static_instruction=STATIC_POLICY_HEADER,
    instruction="Default: be concise and include at most two citations."
)

app = App(
    name="policy_qa_app",
    context_cache_config=ContextCacheConfig(
        ttl_seconds=3600,     # cache the header for 1 hour
        cache_intervals=5,    # force a refresh every 5 requests (guardrail)
        min_tokens=1000       # only cache if header is “worth it”
    ),
    root_agent=agent
)
```

Код (`steering.py`):

```python
# An Example of a runtime controller generating each turn instructions
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class SteeringInputs:
    goal: str                                  # this turn’s objective
    style: str = "concise"                     # terse, detailed, crisp, etc.
    max_cites: int = 2                         # runtime knob
    tenant_hint: Optional[str] = None          # "Answer for EU employees only"
    corrective: Optional[str] = None           # "Last reply missed field X; include it"
    confidence_range: Tuple[float, float] = (0.6, 0.9)

def build_turn_instruction(s: SteeringInputs) -> str:
    parts = [
        f"Goal: {s.goal}",
        f"Style: {s.style}",
        (
            "Constraints: "
            f"include at most {s.max_cites} citations; "
            "refuse medical/legal advice; "
            "if info is missing, ask one targeted question; "
            f"return 'confidence' between {s.confidence_range[0]} and {s.confidence_range[1]}."
        )
    ]
    if s.tenant_hint:
        parts.append(f"Tenant: {s.tenant_hint}")
    if s.corrective:
        parts.append(f"Correction: {s.corrective}")
    return "
".join(parts)
```

Код (`chat_handler.py`):

```python
# An Example of a chat handler which composes the turn instruction
from steering import SteeringInputs, build_turn_instruction
from google.adk.agents import Agent

# agent imported from app_startup.py

def route_intent(user_message: str) -> str:
    text = user_message.lower()
    if "compare" in text: return "compare"
    if "list" in text and "control" in text: return "list_controls"
    if "summarize" in text: return "summarize"
    return "answer"

INTENT_TO_GOAL = {
    "summarize": "Summarize ACME-42 in plain English.",
    "list_controls": "List mandatory controls from ACME-42 with one-line rationales.",
    "compare": "Compare ACME-42 to ISO 27001 at a high level, return a short markdown table inside the JSON 'answer'.",
    "answer": "Answer the user directly."
}

def chat(session_id: str, user_message: str, ui_style: str | None = None):
    intent = route_intent(user_message)
    goal = INTENT_TO_GOAL.get(intent, f"Answer the user: {user_message[:120]}")

    style = ui_style or get_flag(session_id, "style", default="concise")
    max_cites = get_flag(session_id, "max_citations", default=2)
    tenant_hint = get_tenant_hint(session_id)     # e.g., "EU employees only" or None
    corrective = get_last_validation_error(session_id)  # None or short string

    turn_instruction = build_turn_instruction(
        SteeringInputs(
            goal=goal,
            style=style,
            max_cites=max_cites,
            tenant_hint=tenant_hint,
            corrective=(f"Your last reply failed validation: {corrective}. Fix it this turn." if corrective else None)
        )
    )

    agent.instruction = turn_instruction
    response = agent.run(user_message=user_message)
    validate_and_record(session_id, response)     # optional schema check + feedback
    return response
```

Видео: <https://www.youtube.com/watch?v=DdTtiWoMa3E>

---

### day09 — ⏪ Undo buttons for your Agents  
🟡 · Rewind, Resume, ADK, Time Travel, Undo

Building an "Edit Message" or "Regenerate" feature shouldn't require complex database migrations. In the ADK, time travel is built-in.

Ссылки:
- [ADK Docs: Runtime Resume](https://google.github.io/adk-docs/runtime/resume/) — Learn how to resume an ADK session.
- [ADK Docs: Sessions Rewind](https://google.github.io/adk-docs/sessions/rewind/) — Understand the ADK rewind functionality for time travel.
- [ADK Python Sample: Rewind Session](https://github.com/google/adk-python/blob/main/contributing/samples/rewind_session/main.py) — View a practical example of session rewinding in ADK Python.

Код (`rewind_example.py`):

```python
import asyncio
from adk.api.agents.in_memory_runner import InMemoryRunner

# 1. Initialize the runner
runner = InMemoryRunner(...)

# 2. Something goes wrong? (e.g., hallucination or error at 'invocation_456')
# Instead of clearing the session, we request a rewind.

# 3. Rewind (Time Travel)
# This asynchronously restores session state and artifacts to the target moment.
asyncio.run(
    runner.rewind_async(
        session_id='session_123',
        before_invocation_id='invocation_456'
    )
)

# 4. Resume the conversation from that exact point
asyncio.run(runner.run(query="Let's try that request again with these constraints..."))
```

Видео: <https://www.youtube.com/watch?v=9FQh-Pw2sfE>

---

### day10 — Big Context ≠ Better Memory  
🟡 · Memory, ADK, Context Caching, Context Compaction, Memory

Long-running agent sessions face two enemies: latency and "lost in the middle" syndrome. The ADK solves this with Context Caching and Context Compaction.

Ссылки:
- [Context Compaction](https://google.github.io/adk-docs/context/compaction/) — Learn how to compress history to prevent context rot.
- [Context Caching](https://google.github.io/adk-docs/context/caching/) — Learn how to cache heavy instructions for better performance.
- [Context Compaction Explained](https://x.com/Saboo_Shubham_/status/1978286461607911617) — A visual explanation of context compaction.
- [ADK Context Caching & Compaction Infographic](https://adventofagents.com/aoa-day10-context-caching-compaction.png) — NotebookLM generated infographic summarizing ADK context caching & compaction.
- [Additional Reading: The Context Trap Every Agent Builder Falls Into](https://www.theunwindai.com/p/the-context-trap-every-agent-builder-falls-into) — An article discussing common context management pitfalls every agent builder faces.

Код (`context_config.py`):

```python
from google.adk.apps import App, EventsCompactionConfig
from google.adk.agents.context_cache_config import ContextCacheConfig

# Configure your App with both Caching and Compaction
app = App(
    name='long-memory-agent',
    root_agent=my_agent,
    
    # 1. Cache heavy instructions
    context_cache_config=ContextCacheConfig(
        min_tokens=2048,    # Only cache if prompt is heavy
        ttl_seconds=1800,   # Keep cache alive for 30 mins
        cache_intervals=10  # Refresh after 10 uses
    ),

    # 2. Compress history to prevent "Context Rot"
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3, # Summarize every 3 turns
        overlap_size=1         # Keep 1 turn of context overlap
    )
)
```

Видео: <https://www.youtube.com/watch?v=L3eKHw9df-g>

---

### day11 — Google Managed MCP  
⚪ · MCP, ADK, Google Cloud, BigQuery, Google Maps, GKE, Compute Engine

Connect Agents to Google Services with Managed MCP.

Ссылки:
- [Launch My Bakery GitHub Example](https://github.com/google/mcp/tree/main/examples/launchmybakery) — Explore the code for the "Launch My Bakery" demo.
- [Announcing Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) — Read the official announcement about MCP support for Google services.
- [Kaggle Whitepaper: Agent Tools and Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp) — Learn more about agent tools and interoperability with MCP in this whitepaper.

Код (`bakery_agent.py`):

```python
import os
from google.genai import types
from google.genai.adk import Agent
from google.genai.mcp import RemoteMCPServer

# 1. Define the Fully-Managed Remote MCP Servers
#    These endpoints are now natively supported by Google's infrastructure
bigquery_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/bigquery",
    capabilities=["schema_read", "query_execute"],
    auth_token=os.getenv("GOOGLE_CLOUD_TOKEN") # Uses standard IAM
)

maps_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/maps",
    capabilities=["places_search", "routing", "elevation"],
    auth_token=os.getenv("GOOGLE_MAPS_API_KEY")
)

# 2. Initialize the ADK Agent with MCP Tools
#    The agent can now "see" your enterprise data and the real world
bakery_agent = Agent(
    model="gemini-3-pro",
    tools=[bigquery_mcp, maps_mcp],
    system_instruction="""
    You are a retail expansion scout.
    1. Query BigQuery to find high-revenue demographics.
    2. Use Google Maps to find available locations near competitors.
    3. Synthesize a recommendation for a new bakery location.
    """
)

# 3. Run the Agent
#    Gemini 3 plans the multi-step execution automatically
response = bakery_agent.run(
    "Find a location in Austin, TX with high disposable income and low competition."
)
print(response.text)
```

Видео: <https://www.youtube.com/watch?v=wzccErUYhTI>

---

### day12 — Multimodal Agents with Gemini Live API  
🟡 · Bidi-streaming, WebSockets, Gemini Live, AI Agent, ADK

Explore ADK Bi-Directional Streaming: A visual guide to real-time multimodal AI agent development with WebSockets and Gemini Live.

Ссылки:
- [A developer's guide to Gemini Live API in Vertex AI](https://cloud.google.com/blog/topics/developers-practitioners/how-to-use-gemini-live-api-native-audio-in-vertex-ai) — Two quick start templates with three production-ready apps (Open Source Code)
- [ADK Bidi-streaming: A Visual Guide to Real-time Multimodal AI Agent Development](https://medium.com/google-cloud/adk-bidi-streaming-a-visual-guide-to-real-time-multimodal-ai-agent-development-62dd08c81399) — Comprehensive article on ADK Bidi-streaming.
- [Part 1: Introduction to ADK Bidi-streaming](https://google.github.io/adk-docs/streaming/dev-guide/part1/) — First part of the ADK Bidi-streaming series.
- [Part 2: Sending messages with LiveRequestQueue](https://google.github.io/adk-docs/streaming/dev-guide/part2/) — Second part focusing on LiveRequestQueue.
- [Part 3: Event handling with run_live()](https://google.github.io/adk-docs/streaming/dev-guide/part3/) — Third part covering event handling.
- [Part 4: Run configuration - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part4/) — Documentation on ADK run configuration.
- [Part 5: Audio, Images, and Video - Agent Development Kit](https://google.github.io/adk-docs/streaming/dev-guide/part5/) — Documentation on multimodal capabilities in ADK.

Код (`google_search_agent.py`):

```python
"""Google Search Agent definition for ADK Bidi-streaming demo."""

import os
from google.adk.agents import Agent
from google.adk.tools import google_search

agent = Agent(
    name="google_search_agent",
    model="gemini-2.5-flash-native-audio-preview-09-2025",
    tools=[google_search],
    instruction="You are a helpful voice assistant that can search the web."
)
```

Код (`run_demo.sh`):

```bash
# Clone the streaming sample for this deep dive and install
git clone https://github.com/google/adk-samples
cd adk-samples/python/agents/bidi-demo
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venvScriptsactivate
pip install -e .
export SSL_CERT_FILE=$(python -m certifi)

# Create app/.env file with your GOOGLE_API_KEY.

cd app
export SSL_CERT_FILE=$(uv run --project .. python -m certifi)
uv run --project .. uvicorn main:app --port 8000

# Open http://localhost:8000
```

Видео: <https://www.youtube.com/watch?v=vLUkAGeLR1k>

---

### day13 — Interactions API  
🟡 · Interactions API, ADK, A2A, Google Cloud, Google DeepMind

Interactions API marks a fundamental shift from stateless text generation to stateful, autonomous workflows.

Ссылки:
- [Gemini Interactions API Announcement](https://blog.google/technology/developers/interactions-api) — Read the announcement for Gemini Interactions API.
- [Gemini Interactions API Docs](https://ai.google.dev/gemini-api/docs/interactions-api) — Read the documentation for Gemini Interactions API.
- [Gemini Deep Research Agent Announcement](https://blog.google/technology/developers/deep-research-agent-gemini-api) — Read the announcement for Gemini Deep Research Agent.
- [Gemini Deep Research Agent Docs](https://ai.google.dev/gemini-api/docs/deep-research) — Read the documentation for Gemini Deep Research Agent.
- [ADK Release Notes](https://github.com/google/adk-python/blob/main/CHANGELOG.md) — Check out the ADK release notes.
- [ADK Interactions API Sample](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api) — Check out the ADK sample with the Interactions API.
- [A2A Interactions API Sample](https://github.com/a2aproject/a2a-samples/tree/interactions-api/samples/python/transports/interactions_api) — Check out the A2A sample which uses the Interactions API.

Код (`adk_interactions_api.py`):

```python
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        # Enable Interactions API
        use_interactions_api=True,
    ),
    name="interactions_test_agent",
    tools=[
        # Converted Google Search to a function tool
        GoogleSearchTool(bypass_multi_tools_limit=True),
        get_current_weather,
    ],
)
```

Видео: <https://www.youtube.com/watch?v=kPhs6C0-JbY>

---

### day14 — Connecting Agents with A2A  
⚪ · ADK A2A, ADK, A2A, Multi-Agent, Agent Starter Pack

Connect agents across teams, frameworks, and languages with the Agent2Agent (A2A) Protocol. ADK makes implementing A2A simple.

Ссылки:
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Get started with production-ready A2A agents.
- [ADK A2A Docs](https://google.github.io/adk-docs/a2a/) — Learn how to implement A2A in the ADK.
- [A2A Protocol Spec](https://a2a-protocol.org/) — The official Agent2Agent protocol specification.
- [Prototype to Production Whitepaper](https://www.kaggle.com/whitepaper-prototype-to-production) — Deep dive into multi-agent architectures and production patterns.

Код (`terminal`):

```shell
uvx agent-starter-pack create -p -a adk_a2a_base
```

Видео нет

---

### day15 — Introducing A2UI  
🟡 · A2UI, Generative UI, Agent-to-User Interface, Agent Development

Discover A2UI (Agent-to-User Interface), an open project that enables agents to stream dynamic, generative UIs as JSONL payloads, decoupling UI definition from rendering and breaking the ceiling of traditional chat interfaces.

Ссылки:
- [A2UI Official Website](https://a2ui.org/) — The official website for the A2UI project.
- [A2UI Github Repo](https://github.com/google/a2ui) — The Github repository for the A2UI project.
- [A2UI Composer](https://a2ui-editor.ag-ui.com/) — The A2UI Composer for building UI components - thanks CopilotKit / AG UI team!

Код (`quickstart.sh`):

```bash
git clone https://github.com/google/a2ui.git
cd a2ui
export GEMINI_API_KEY="your_gemini_api_key_here"
cd samples/client/lit
npm install
npm run demo:all
```

Видео: <https://www.youtube.com/watch?v=kJFnJr-leDI>

---

### day16 — LangGraph + A2A  
🟡 · LangGraph, A2A, Agent Starter Pack, Multi-Agent

Build LangGraph agents with full A2A capabilities using Agent Starter Pack. Your agent becomes instantly discoverable by other agents.

Ссылки:
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Get started with production-ready LangGraph A2A agents.
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) — Learn about building stateful agents with LangGraph.
- [A2A Protocol Spec](https://a2a-protocol.org/) — The official Agent2Agent protocol specification.

Код (`terminal`):

```shell
uvx agent-starter-pack create my-agent -a langgraph_base
```

Видео: <https://www.youtube.com/watch?v=N25rAzQXkEA>

---

### day17 — Gemini 3 Flash is here!  
🟡 · gemini, flash, thinking, adk

Google's fastest model just got smarter with configurable thinking levels and granular controls.

Ссылки:
- [Gemini 3 Flash Announcement](https://blog.google/products/gemini/gemini-3-flash/) — Official announcement blog post
- [ADK Get Started Documentation](https://google.github.io/adk-docs/get-started/) — Get started with the Agent Development Kit
- [ADK Models Documentation](https://google.github.io/adk-docs/agents/models/) — Learn about model configuration in ADK
- [Developer's Guide to Multi-Agent Systems](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/) — Building Multi-Agent Systems with Gemini 3 Flash and ADK
- [Google launches Gemini 3 Flash, makes it the default model in the Gemini app](https://techcrunch.com/2025/12/17/google-launches-gemini-3-flash-makes-it-the-default-model-in-the-gemini-app/) — Techcrunch article reporting on the launch of Gemini 3 flash

Код (`agent.py`):

```python
from google.adk.agents import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
    # Configure thinking level for Gemini 3
    # Options: "HIGH" (deep reasoning), "LOW" (minimal latency), "MINIMAL" (raw speed)
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            thinking_level="LOW"
        )
    ),
)
```

Код (`install.sh`):

```shell
pip install google-adk # and follow the instruction in the video
```

Видео: <https://www.youtube.com/watch?v=1txijlIHS_I>

---

### day18 — Cloud API Registry + ADK  
⚪ · Cloud API Registry, Vertex AI Agent Builder, ADK, Tools

The biggest friction in enterprise agent development isn't the model—it's the tools. Vertex AI Agent Builder now integrates with Cloud API Registry, providing a centralized tool repository.

Ссылки:
- [Cloud API Registry documentation](https://docs.cloud.google.com/api-registry/docs/overview)
- [Get started with Cloud API Registry tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_cloud_api_registry.ipynb)
- [New Enhanced Tool Governance in Vertex AI Agent Builder Blog](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder)
- [Where is the MCP server? Deploy your agent with Cloud API Registry on Vertex AI Agent Engine](https://discuss.google.dev/t/where-is-the-mcp-server-deploy-your-agent-with-cloud-api-registry-on-vertex-ai-agent-engine/298130)
- [Tool Governance in Vertex AI Agent Builder with the new Cloud API Registry integration](https://discuss.google.dev/t/tool-governance-in-vertex-ai-agent-builder-with-the-new-cloud-api-registry-integration/298148)

Код (`admin_setup.sh`):

```bash
gcloud beta services mcp enable bigquery.googleapis.com --project=YOUR_PROJECT_ID
```

Код (`developer_implementation.py`):

```python
from google.adk import Agent, ApiRegistry

# 1. Connect to the Cloud API Registry
registry = ApiRegistry(project_id="your-project-id")

# 2. Fetch the specific tool (e.g., BigQuery MCP)
# This retrieves the managed tool definition directly from the registry
bq_tool = registry.get_tool("google-bigquery")

# 3. Add the tool to your Agent
# The agent now has governed access to BigQuery capabilities
agent = Agent(
    model="gemini-3-pro",
    tools=[bq_tool]
)

print("Agent configured with governed BigQuery access.")
```

Видео нет

---

### day19 — Register to Gemini Enterprise  
🟡 · Gemini Enterprise, Agent Starter Pack, Deployment, A2A

Register your agent to Gemini Enterprise! 🌐 and make it discoverable to everyone in your organization, right alongside Google's built-in agents.

Ссылки:
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Create and register agents to Gemini Enterprise.
- [Gemini Enterprise Agents Overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview) — Learn about agents in Gemini Enterprise.
- [Register an ADK Agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent) — Guide for registering ADK agents to Gemini Enterprise.
- [Register an A2A Agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent) — Guide for registering A2A agents to Gemini Enterprise.

Код (`terminal`):

```shell
# Create your agent
uvx agent-starter-pack create --adk

# Deploy it
make deploy

# Register to Gemini Enterprise
make register-gemini-enterprise
```

Видео: <https://www.youtube.com/watch?v=dhT2dAbRwVk>

---

### day20 — A2A Extensions: The Flexible Sidecar for Custom Data  
⚪ · A2A Extensions, Extensions, Sidecar Pattern, Agent Communication

The Agent-to-Agent (A2A) protocol relies on a strict format, but real-world complexity often requires unique data. A2A Extensions provide a "Sidecar" pattern for custom data without breaking backward compatibility.

Ссылки:
- [A2A Secure Passport Extension Sample](https://github.com/a2aproject/a2a-samples/tree/main/extensions/secure-passport/v1/samples/python)

Код (`get_sample.sh`):

```shell
# Download the specific extensions sample
uvx agent-starter-pack create secure-auth-agent   -a adk_a2a_base   --extension secure-passport
```

Код (`secure_passport_implementation.py`):

```python
from secure_passport_ext import CallerContext, A2AMessage, add_secure_passport, get_secure_passport

# 1. THE SENDER: Attaches the "Sidecar"
# We create a secure context with custom enterprise data
passport = CallerContext(
    client_id="a2a://travel-orchestrator.com",
    state={"tier": "Platinum", "billing_code": "US-123"},
    signature="valid-crypto-signature-123"
)

message = A2AMessage(type="task", content="Book flight")
# "Stamp" the message with the extension
add_secure_passport(message, passport)


# 2. THE RECEIVER: Inspects the "Sidecar"
# This function safely checks for the extension without crashing if missing
received_passport = get_secure_passport(message)

if received_passport and received_passport.is_verified:
    print(f"✅ Verified Platinum Request from: {received_passport.client_id}")
else: # Non-breaking fall-back behavior
    print(f"ℹ️ Standard processing (No auth extension found)")
```

Видео: <https://www.youtube.com/watch?v=MV0Ub-xN48A>

---

### day21 — Kaggle Capstone Winners Highlight  
🟡 · Hall of Fame, Winners, Agents for Good, Enterprise Agents, Concierge Agents, Freestyle

🏆 The Hall of Fame: Meet the Winners

Ссылки:
- [NewsPulse AI Agent (1st Place)](https://github.com/azhang6-nlp/NewsPulse_AI_Agent) — Concierge Agents Track - 1st Place
- [FIL Content Agent System - Agent Code (2nd Place)](https://github.com/jasononaquest/fil-agent) — Concierge Agents Track - 2nd Place Agent Code
- [FIL Content Agent System - MCP Server Code (2nd Place)](https://github.com/jasononaquest/FIL-mcp) — Concierge Agents Track - 2nd Place MCP Server Code
- [AishIngAnalyzer (3rd Place)](https://github.com/aishasartaj1/AishIngAnalyzer) — Concierge Agents Track - 3rd Place
- [Carbon Footprint Optimization Engine (CfoE) (1st Place)](https://www.kaggle.com/code/sumitkumarguha/global-cfoe) — Agents for Good Track - 1st Place
- [CarbonCalc AI (2nd Place)](https://github.com/madhuwantha/carbon-calc-ai.git) — Agents for Good Track - 2nd Place
- [Parallel Scholar (3rd Place)](https://github.com/emansarahafi/research-assistant-agent) — Agents for Good Track - 3rd Place
- [Chaos Playbook Engine (1st Place)](https://github.com/alberto-martinez-zurita/chaos-playbook-engine) — Enterprise Agents Track - 1st Place
- [Coderama (2nd Place)](https://github.com/debasisdwivedy/Coderama) — Enterprise Agents Track - 2nd Place
- [VeganFlow (3rd Place)](https://github.com/karthick-sothivelr/Autonomous_Supply_Chain_Intelligence) — Enterprise Agents Track - 3rd Place
- [Daedalus - The Agentic Toolsmith (1st Place)](https://github.com/jovanovic-milos/daedalus) — Freestyle Track - 1st Place
- [AI Stock Prediction System (2nd Place)](https://github.com/nishapp/agents-5days-kaggle-competition) — Freestyle Track - 2nd Place
- [StoryLand AI (3rd Place)](https://github.com/o-ostrovskiy/storyland-ai) — Freestyle Track - 3rd Place

Видео: <https://www.youtube.com/watch?v=FrfaAwq0YNg>

---

### day22 — Security & Guardrails  
⚪ · Model Armor, Security, guardrails, ADK

Prompt Engineering is not a Security Strategy. Asking an LLM nicely to "please ignore PII" is not governance; it's wishful thinking.

Ссылки:
- [ADK Callbacks: Design Patterns and Best Practices](https://google.github.io/adk-docs/callbacks/design-patterns-and-best-practices/) — Explore design patterns and best practices for ADK callbacks.
- [ADK Callbacks](https://google.github.io/adk-docs/callbacks/) — Official documentation for ADK Callbacks.
- [ADK Plugins](https://google.github.io/adk-docs/plugins/) — Official documentation for ADK Plugins.
- [Model Armor Overview](https://docs.cloud.google.com/model-armor/overview) — Overview of Model Armor for security.
- [Manage Model Armor Templates](https://docs.cloud.google.com/model-armor/manage-templates) — Documentation on managing Model Armor templates.
- [Agent Builder - Agent Identity](https://docs.cloud.google.com/agent-builder/agent-engine/agent-identity) — Documentation on Agent Identity in Agent Builder.
- [Build and scale AI agents with Vertex AI Agent Builder](https://cloud.google.com/blog/products/ai-machine-learning/more-ways-to-build-and-scale-ai-agents-with-vertex-ai-agent-builder) — Blog post on building and scaling AI agents.
- [A2A Protocol - Enterprise Ready](https://a2a-protocol.org/latest/topics/enterprise-ready/#tracing-observability-and-monitoring) — Enterprise-ready features of the A2A Protocol.

Код (`callback_and_plugins.py`):

```python
## The Developer Layer: Callbacks & Plugins 
# This Python snippet demonstrates how to inject security logic using the ADK callback system.


from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from .tools import add, subtract, multiply, divide
from .prompt import instruction_prompt
from google.genai import types
from typing import Optional

MODEL = "gemini-2.5-flash"

async def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:
       # Guardrail 1: Do we have the student profile?
       if not callback_context.state.get("student_profile"):
               return types.Content(role='model', parts=[types.Part(text="Error: Cannot find student profile.")])
# Add more guardrails...

       return None # Allow model call to proceed

agent_math = Agent(
       model=MODEL,
       name="agent_math",
       description="This agent performs basic arithmetic operations (addition, subtraction, multiplication, and division) on user-provided numbers, including ranges.",
       instruction=instruction_prompt,
       tools=[add, subtract, multiply, divide],
       before_agent_callback=callback_before_agent,
)
```

Код (`adk_plugin.py`):

```python
## This Python snippet demonstrates how to create an ADK plugin.

from google.adk.agents.base_agent import BaseAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.plugins.base_plugin import BasePlugin

class CountInvocationPlugin(BasePlugin):
 """A custom plugin that counts agent and tool invocations."""
 def __init__(self) -> None:
   """Initialize the plugin with counters."""
   super().__init__(name="count_invocation")
   self.agent_count: int = 0
   self.tool_count: int = 0
   self.llm_request_count: int = 0

 async def before_agent_callback(self, *, agent: BaseAgent, callback_context:CallbackContext) -> None: 
   """Count agent runs."""
   self.agent_count += 1
   print(f"[Plugin] Agent run count: {self.agent_count}")
```

Код (`adk_plugin_agent.py`):

```python
## This Python snippet demonstrates how to load/apply an ADK plugin to an agent.

from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.genai import types
import asyncio

# Import the plugin.
from .count_plugin import CountInvocationPlugin

async def hello_world(tool_context: ToolContext, query: str):
 print(f'Hello world: query is [{query}]')
 root_agent = Agent(
   model='gemini-2.0-flash',
   name='hello_world',
   description='Prints hello world with user query.',
   instruction="""Use hello_world tool to print hello world and user query.""",
   tools=[hello_world],
)

async def main():
 """Main entry point for the agent."""
 prompt = 'hello world'
 runner = InMemoryRunner(agent=root_agent, app_name='test_app_with_plugin',
     # Add your plugin here. You can add multiple plugins.
     plugins=[CountInvocationPlugin()],)
 ...
```

Код (`model_armor_template.sh`):

```bash
## The Admin Layer: 
# Model Armor Template While developers write Python
# Admins configure Model Armor to sanitize data globally.

export TEMPLATE_CONFIG='{
   "filterConfig": {
    "raiSettings": {
     "raiFilters": [{
       "filterType": "HATE_SPEECH",
       "confidenceLevel": "MEDIUM_AND_ABOVE"
      }, {
      "filterType": "HARASSMENT",
      "confidenceLevel": "HIGH"
    }]
  },
  "piAndJailbreakFilterSettings": {
    "filterEnforcement": "ENABLED",
    "confidenceLevel": "LOW_AND_ABOVE"
  }
 },
 "templateMetadata": {
    "multiLanguageDetection": {
      "enableMultiLanguageDetection": true
    }
  }
}'

curl -X POST  -d "$TEMPLATE_CONFIG"   -H "Content-Type: application/json"  -H "Authorization: Bearer $(gcloud auth print-access-token)"     "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/templates?template_id=TEMPLATE_ID"
```

Видео: <https://www.youtube.com/watch?v=j9YyZM2OBS8>

---

### day23 — Durable, Resilient Agents with Google ADK + Restate  
🟡 · Durable Execution, ADK, Restate, Resilient Agents

Most agents are fragile. Durable Execution with Google ADK and Restate ensures your agent never loses context, survives crashes, and can pause execution for days.

Ссылки:
- [Restate Google ADK Example Repository](https://github.com/restatedev/restate-google-adk-example)
- [Restate Docs/Deep Dive](https://docs.restate.dev/ai)

Код (`restate_setup.sh`):

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

Видео: <https://www.youtube.com/watch?v=TkGFdildEXk>

---

### day24 — A2A-ify Anything  
🟡 · A2A, Agent Starter Pack, ADK Samples

Take any ADK or LangGraph sample and launch it with A2A on top. Layer A2A capabilities onto existing agents with a single flag.

Ссылки:
- [ADK Samples](https://github.com/google/adk-samples) — Ready-to-use agents built with the Agent Development Kit.
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Add A2A capabilities to any agent.
- [A2A Protocol Spec](https://a2a-protocol.org/) — The official Agent2Agent protocol specification.

Код (`terminal`):

```shell
# Create with A2A from a sample
uvx agent-starter-pack create my-agent     -a adk@deep-search     --base-template adk_a2a_base

# Or enhance an existing agent
uvx agent-starter-pack enhance --base-template adk_a2a_base
```

Видео: <https://www.youtube.com/watch?v=6UUEeiX2y58>

---

### day25 — 🎉 Grand Finale: Mission Accomplished!  
🟡 · Architecture, Blueprint, Production, Summary, Agent Engine, ADK, Gemini 3, Multi-agent

Congratulations! You've successfully completed the 25-day Advent of Agents journey.

Ссылки:
- [Agent Designer](https://docs.cloud.google.com/agent-builder/agent-designer) — Agent Designer is a low-code visual designer that lets you design and test agents in the Google Cloud console. You can experiment with your agent in Agent Designer before transitioning development to code using Agent Development Kit.
- [Kaggle 5-day Intensive Course on Agents](https://www.kaggle.com/learn-guide/5-day-agents) — The 5-Day AI Agents Intensive course is now a self-paced learning guide.  This course was crafted by Google’s ML researchers and engineers to help developers explore the foundations and practical applications of AI agents. You’ll learn the core components – models, tools, orchestration, memory and evaluation. Each day blends conceptual deep dives with hands-on examples, codelabs, and live discussions.
- [Agent Development Kit (ADK) on GitHub](https://github.com/google/adk-samples) — Explore more samples and contribute to the ADK community.
- [Retail AI Location Strategy: Autonomous Site Selection & Market Analysis](https://github.com/google/adk-samples/tree/main/python/agents/retail-ai-location-strategy) — Explore a fully built case study on using AI for autonomous site selection and market analysis in retail.

Код (`fastest_start.sh`):

```bash
uvx agent-starter-pack create my-agent --adk
```

Код (`full_example_deep_research.sh`):

```bash
uvx agent-starter-pack create deep-search -a adk@deep-search
```

Код (`full_example_retail_location_strategy.sh`):

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

Видео: <https://www.youtube.com/watch?v=AuE-w-z9lks>

---

## s2-2026-03

### day01 — Season 2 Kick Off  
🟡 · Launch

31 days. Zero to Production-Ready AI Agents on Google Cloud.

Ссылки:
- [Subscribe to weekly newsletter](https://groups.google.com/g/advent-of-agents-newsletter) — Get the latest updates and resources delivered to your inbox
- [Introduction to Agents Whitepaper](https://www.kaggle.com/whitepaper-introduction-to-agents) — Released as part of the 5 Days of Agents with Kaggle
- [Google ADK Documentation](https://google.github.io/adk-docs/) — Official documentation for the Agent Development Kit
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Production-ready templates for building AI agents

Видео: <https://www.youtube.com/watch?v=MUnjMBHsaEw>

---

### day02 — Build ADK Agents with Gemini 3.1 Pro  
⚪ · ADK, Agent Starter Pack, Python, Go, TypeScript, Java

Choose your language. One command. Total language flexibility. Bootstrap high-performance agents in seconds.

Ссылки:
- [ADK Getting Started Guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/getting-started.html)
- [Agent Templates Overview](https://googlecloudplatform.github.io/agent-starter-pack/agents/overview.html)
- [Gemini 3.1 Pro Model Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- [ADK Official Documentation](https://google.github.io/adk-docs/get-started/)

Код (`terminal`):

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

Видео нет

---

### day03 — Build AI Agents with Gemini 3.1 Flash-Lite  
⚪ · Gemini 3.1 Flash-Lite, Product Launch, Vertex AI, Memory Agent

Announcing Gemini 3.1 Flash-Lite: our most cost-efficient model for building high-quality AI agents at scale.

Ссылки:
- [GitHub Repository](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents/always-on-memory-agent) — Always-On Memory Agent: Persistent, evolving memory for AI agents.
- [Vertex AI Studio](https://vertexai.google.com/) — Get started with Gemini 3.1 Flash-Lite on Vertex AI.
- [Google AI Studio](https://aistudio.google.com/) — Fastest way to build with Gemini models.

Код (`terminal`):

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

Видео: <https://www.youtube.com/watch?v=-7zEqFXg0zw>

---

### day04 — MCP Servers: Add external tools to your agents in just a few lines  
⚪ · Code Analysis, Tool Call, MCP, ADK

Wire up multiple MCP servers simultaneously to trace bugs from Linear to GitHub PRs.

Ссылки:
- [Developer Blog](https://developers.googleblog.com/en/supercharge-your-ai-agents-adk-integrations-ecosystem/) — Supercharge your AI Agents: Details on ADK Integrations Ecosystem
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/) — Standardizing how agents access diverse data sources
- [GitHub MCP Server](https://google.github.io/adk-docs/integrations/github) — GitHub MCP Server implementation
- [Linear MCP Server](https://google.github.io/adk-docs/integrations/linear) — Linear MCP Server implementation

Код (`agent.py`):

```python
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.apps import App
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
import os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
LINEAR_API_KEY = os.environ.get("LINEAR_API_KEY")

root_agent = Agent(
    model=Gemini(model="gemini-3-flash-preview"),
    name="root_agent",
    instruction=open(os.path.join(os.path.dirname(__file__), "prompt.md")).read(),
    tools=[
        McpToolset(
            tool_name_prefix="github_",
            connection_params=StreamableHTTPServerParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "pull_requests",
                    "X-MCP-Readonly": "true"
                },
            ),
        ),
        McpToolset(
            tool_name_prefix="linear_",
            tool_filter=["get_issue", "list_issues", "search_issues"],
            connection_params=StreamableHTTPServerParams(
                url="https://mcp.linear.app/mcp",
                headers={
                    "Authorization": f"Bearer {LINEAR_API_KEY}",
                },
            ),
        )
    ],
)

app = App(
    name="app",
    root_agent=root_agent,
)
```

Код (`prompt.md`):

```markdown
You are an intelligent agent that can fetch the source diff of a Pull Request based on the Linear issue ID. Your exact workflow is:
1. Use `linear_get_issue` to fetch the specific bug report in Linear.
2. Extract keywords, branch names, or the exact title from the Linear issue.
3. Use `github_list_pull_requests` or `github_search_pull_requests` in the provided GitHub repository using those extracted keywords to find the associated Pull Request. Important: Always restrict your search to the user's provided repository (e.g. `repo:rovindra/web-master`) rather than searching globally. Do not search by the literal Linear issue ID unless you know it's in the PR title.
4. Use `github_pull_request_read` to fetch the source diff of that exact PR.
5. Summarize the diff based on the PR contents.

When returning the final response, you MUST format the details as a markdown table followed by the diff summary:
| Field | Details |
|---|---|
| **Title** | [PR Title] |
| **Author** | [PR Author] |
| **Branch** | [PR Branch] |
| **Date** | [PR Date] |
| **Files Changed** | [PR No. of Files Changed] |
| **State** | [Open/Merged/Closed] |
| **Issue** | [Linear Issue ID & Title] |
| **Description** | [Brief PR Description] |
| **Summary** | [Your brief summary of the changes] |

### Diff Analysis
[Detailed explanation of the code changes...]

### Diff
[Actual diff of the changes...]

Never ask the user for a PR number if they already provided the target GitHub repository and Linear issue ID.
```

Видео: <https://www.youtube.com/watch?v=to4k4aPlYDw>

---

### day05 — Long Term Recall: Memory Plugins  
⚪ · ADK, Memory, Vector Database, Modularity

Implement persistent semantic memory for AI agents using the GoodmemPlugin.

Ссылки:
- [ADK Tools and Integrations](https://google.github.io/adk-docs/tools) — Review supported tools for agent enhancement.
- [GoodMem Plugin for ADK](https://google.github.io/adk-docs/integrations/goodmem/) — Technical specification for persistent memory plugin.

Код (`agent.py`):

```python
import os
from google.adk.agents import LlmAgent
from google.adk.apps import App
from goodmem_adk import GoodmemPlugin

# Attach persistent memory to the App layer
goodmem_chat_plugin = GoodmemPlugin(
    base_url=os.getenv("GOODMEM_BASE_URL"),
    api_key=os.getenv("GOODMEM_API_KEY"),
    top_k=5
)

# Agent context is automatically hydrated at runtime
root_agent = LlmAgent(
    name="root_agent",
    model="gemini-3.1-pro-preview",
    instruction="You are a Professional chef with persistent memory access."
)

app = App(name="Dietary-chef", root_agent=root_agent, plugins=[goodmem_chat_plugin])
```

Видео: <https://www.youtube.com/watch?v=LnTVBxhxWVA>

---

### day06 — ADK Skills  
⚪ · ADK, Skills, Progressive Disclosure, Optimization

Eliminate wasted tokens with progressive disclosure. Use ADK Skills to load complex instructions only when needed.

Ссылки:
- [ADK Skills Documentation](https://google.github.io/adk-docs/skills/) — Official guide for defining and using skills in ADK.
- [ADK Skills: Part 1 - What Are Skills?](https://lavinigam.com/posts/adk-agent-skills-part1/#what-are-skills-and-why-they-matter) — Learn why decoupling procedural knowledge matters.
- [ADK Skills: Part 2 - Wiring Skills](https://lavinigam.com/posts/adk-agent-skills-part2/#wiring-skills-into-the-agent) — Technical deep dive into SkillToolset internals.
- [ADK Skills: Part 3 - Skills That Write Skills](https://lavinigam.com/posts/adk-agent-skills-part3/#pattern-4-skills-that-write-skills) — Pattern 4: The meta-skill of self-generation.
- [Agent Skills Specification](https://agentskills.io/specification) — The open standard adopted by 40+ agents.
- [Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-agent-skills-tutorial) — Clone and run all four skill patterns.

Код (`agent.py`):

```python
# agent.py — ADK Skills: 4 patterns in one agent
import pathlib
from google.adk import Agent
from google.adk.skills import load_skill_from_dir, models
from google.adk.tools.skill_toolset import SkillToolset

# Pattern 1: Inline skill — stable rules defined in code
seo_skill = models.Skill(
    frontmatter=models.Frontmatter(
        name="seo-checklist",
        description="SEO optimization checklist for blog posts.",
    ),
    instructions=(
        "Check each item:\n"
        "1. Title: 50-60 chars, primary keyword near the start\n"
        "2. Meta description: 150-160 chars with call-to-action\n"
        "3. Headings: H2/H3 hierarchy, keywords in 2-3 headings\n"
        "4. First paragraph: primary keyword in first 100 words\n"
        "5. Images: alt text with keywords, compressed"
    ),
)

# Pattern 2: File-based skill — SKILL.md + references/ directory
blog_writer = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "blog-writer"
)

# Pattern 3: External skill — same format, from a community repo
researcher = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "content-research-writer"
)

# Wire all skills into one SkillToolset (auto-generates 3 tools)
root_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="blog_skills_agent",
    description="A blog-writing agent powered by reusable skills.",
    instruction="You are a blog-writing assistant. Load relevant skills before acting.",
    tools=[SkillToolset(skills=[seo_skill, blog_writer, researcher])],
)
```

Видео нет

---

### day07 — ADK Agent Skill Design Patterns  
⚪ · Skills, Design Patterns, SkillToolset, ADK

Five design patterns for structuring SKILL.md content in ADK — Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline.

Ссылки:
- [5 Agent Skill Design Patterns (Blog)](https://lavinigam.com/posts/adk-skill-design-patterns/) — Full walkthrough of the 5 patterns with working ADK code.
- [ADK Skills Documentation](https://google.github.io/adk-docs/skills/) — Official guide for defining and using skills in ADK.
- [ADK Skills Part 1: Progressive Disclosure](https://lavinigam.com/posts/adk-agent-skills-part1/) — Foundations: what skills are, L1/L2/L3 levels, inline skills.
- [ADK Skills Part 2: File-Based Skills](https://lavinigam.com/posts/adk-agent-skills-part2/) — SKILL.md format, load_skill_from_dir, SkillToolset internals.
- [ADK Skills Part 3: Meta Skills](https://lavinigam.com/posts/adk-agent-skills-part3/) — Pattern 4: skills that write skills.
- [Agent Skills Specification](https://agentskills.io/specification) — The open standard defining SKILL.md format, adopted by 30+ agents.
- [Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-skill-design-patterns) — Clone and run all five design patterns with ADK Web.

Код (`agent.py`):

```python
import pathlib
from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools.skill_toolset import SkillToolset

SKILLS_DIR = pathlib.Path(__file__).parent / "skills"

# One agent, five skills, five design patterns
skill_toolset = SkillToolset(
    skills=[
        load_skill_from_dir(SKILLS_DIR / "api-expert"),       # Tool Wrapper
        load_skill_from_dir(SKILLS_DIR / "report-generator"), # Generator
        load_skill_from_dir(SKILLS_DIR / "code-reviewer"),    # Reviewer
        load_skill_from_dir(SKILLS_DIR / "project-planner"),  # Inversion
        load_skill_from_dir(SKILLS_DIR / "doc-pipeline"),     # Pipeline
    ],
)

root_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="pattern_demo_agent",
    description="A developer assistant powered by 5 skill design patterns.",
    instruction="Load relevant skills before acting on any user request.",
    tools=[skill_toolset],
)
```

Видео нет

---

### day08 — Multi-Agent Patterns: Sequential Agents  
🟡 · Multi-Agent, Sequential Pipelines, Architecture, ADK

Build predictable sequential workflows where the output of one agent goes straight to the next.

Ссылки:
- [ADK Documentation: SequentialAgent](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/) — Official documentation for the Agent Development Kit.
- [Multi-Agent Design Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/) — Google Developers Blog post on multi-agent design patterns.
- [Building Collaborative AI with ADK](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk) — A Developer's Guide to Multi-Agent Systems with ADK.

Код (`agent.py`):

```python
from google.adk.agents import LlmAgent, SequentialAgent

# Step 1: The Reader - Ingests the PDF and normalizes the content
reader = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="PDFReader",
   instruction="Analyze the provided PDF and provide a comprehensive raw text dump of its core contents.",
   output_key="parsed_content"
)

# Step 2: The Insight Miner - Identifies key technical facts or unique points
miner = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="InsightMiner",
   instruction="""
   Review the following content: {parsed_content}
   Extract the top 5 most important technical facts, dates, or figures.
   """,
   output_key="extracted_insights"
)

# Step 3: The Synthesizer - Generates the final "TL;DR"
synthesizer = LlmAgent(
   model='gemini-3.1-pro-preview',
   name="ExecutiveSynthesizer",
   instruction="""
   Based on these insights: {extracted_insights}
   Generate a 3-sentence 'Executive Briefing' suitable for a busy stakeholder.
   """
)

# Orchestrate the linear Assembly Line
root_agent = SequentialAgent(
   name="UniversalDocumentPipeline",
   sub_agents=[reader, miner, synthesizer]
)
```

Код (`__init__.py`):

```python
from .agent import root_agent

__all__ = ["root_agent"]
```

Видео: <https://www.youtube.com/watch?v=vXoDUg2UZmQ>

---

### day09 — Multi-Agent Patterns: Coordinator/Dispatcher Agents  
🟡 · Multi-Agent, Coordinator, Veo 3.1, ADK

Build high-fidelity educational video agents that maintain character and scene consistency using the Google ADK, Gemini 3.1 Pro, Nano Banana and Veo 3.1.

Ссылки:
- [GitHub Repository](https://github.com/vladkol/video-avatars-agent) — Complete source code for the Video Avatar Agent.
- [ADK Documentation](https://google.github.io/adk-docs/) — Official documentation for the Agent Development Kit.
- [Sample Output](https://youtu.be/QxzTVRYi95E) — An 8-second demo of the generated avatar consistency.

Код (`setup.sh`):

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

Видео: <https://www.youtube.com/watch?v=QxzTVRYi95E>

---

### day10 — Multi-Agent Patterns: Parallel Fanout and State Interpolation  
⚪ · Multi-Agent, Parallel Execution, Architecture, ADK

Drastically reduce latency by running independent, grounded LLM tasks concurrently and automatically synthesizing their outputs.

Ссылки:
- [Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26) — Source code for this project.
- [LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/) — Official documentation for LlmAgent.
- [ParallelAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/) — Official documentation for ParallelAgent.
- [SequentialAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/) — Official documentation for SequentialAgent.

Код (`agent.py`):

```python
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

# 1. Define independent research agents with explicit output_keys and grounding tools
healthcare_researcher = Agent(name='healthcare_researcher', model='gemini-3-flash-preview', output_key='healthcare_research', tools=[google_search], instruction='Use the Google Search tool to...')
finance_researcher = Agent(name='finance_researcher', model='gemini-3-flash-preview', output_key='finance_research', tools=[google_search], instruction='Use the Google Search tool to...')

# 2. Fanout: Run them all concurrently
research_squad = ParallelAgent(
    name='research_squad',
    sub_agents=[healthcare_researcher, finance_researcher],
)

# 3. State Interpolation: Use `{output_key}` placeholders in the synthesizer prompt
synthesizer = Agent(
    name='synthesizer',
    model='gemini-3-flash-preview',
    instruction="Synthesize the following trends: \n\n{healthcare_research}\n\n{finance_research}",
)

# 4. Sequential block ensures fanout completes and populates state before synthesis
root_agent = SequentialAgent(
    name='root_agent',
    sub_agents=[research_squad, synthesizer],
)

from google.adk.apps import App
app = App(name="fanout", root_agent=root_agent)
```

Видео: <https://www.youtube.com/watch?v=4-lr3sh2ETM>

---

### day11 — Multi-Agent Patterns: Hierarchical Decomposition  
⚪ · Multi-Agent, Hierarchical, Architecture, ADK

Use a top-level Manager agent that utilizes an AgentTool to dynamically generate a plan before executing it.

Ссылки:
- [Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26) — Source code for this project.
- [LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/) — Official documentation for LlmAgent.
- [ParallelAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/) — Official documentation for ParallelAgent.
- [SequentialAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/) — Official documentation for SequentialAgent.

Код (`agent.py`):

```python
from google.adk.tools import AgentTool
from google.adk.tools import google_search
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.apps import App

# The Planner is used purely as a tool by the Manager
planner = LlmAgent(
    name='planner',
    model='gemini-3-flash-preview',
    instruction='Break the user prompt into exactly three distinct research themes.'
)

# Define sub-agents for execution
researcher = LlmAgent(
    name='researcher', 
    model='gemini-3-flash-preview', 
    tools=[google_search], 
    instruction='Research the assigned topic step-by-step.'
)
synthesizer = LlmAgent(
    name='synthesizer', 
    model='gemini-3-flash-preview', 
    instruction='Synthesize the findings into a cohesive report.'
)

# A logical pipeline of sub-agents to handle execution
execution_pipeline = SequentialAgent(
    name='execution_pipeline',
    sub_agents=[researcher, synthesizer]
)

# The Manager orchestrates the whole flow autonomously
manager = LlmAgent(
    name='manager',
    model='gemini-3-flash-preview',
    tools=[AgentTool(planner)],
    sub_agents=[execution_pipeline],
    instruction='''
    1. Use the planner tool to create a detailed research plan based on the user's prompt.
    2. Activate your execution_pipeline sub-agent and pass the completed plan to it so it can execute it.
    '''
)

root_agent = manager
app = App(name="hierarchical", root_agent=root_agent)
```

Видео: <https://www.youtube.com/watch?v=68EznHkK_UQ>

---

### day12 — Multi-Agent Patterns: Generator-Critic Agent Loop  
⚪ · Multi-Agent, LoopAgent, Quality Assurance, ADK

Automatically refine LLM outputs using ADK's LoopAgent to orchestrate a conversation between a creative Writer and a strict Critic.

Ссылки:
- [Project Repository](https://github.com/LuisSala/advent-of-agents-spring-26) — Source code for this project.
- [LlmAgent Reference](https://google.github.io/adk-docs/agents/llm-agents/) — Official documentation for LlmAgent.
- [LoopAgent Reference](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/) — Official documentation for LoopAgent.
- [Function Tools Reference](https://google.github.io/adk-docs/tools-custom/function-tools/) — Official documentation for writing custom function tools.

Код (`agent.py`):

```python
from google.adk.agents import Agent, LoopAgent
from google.adk.tools import FunctionTool, ToolContext

def approve_draft(tool_context: ToolContext) -> dict:
    tool_context.actions.escalate = True # Breaks the loop execution early
    return {"status": "success", "message": "Approved."}

writer = Agent(
    name='writer', model='gemini-3-flash-preview',
    instruction="Revise your draft based on feedback: {latest_feedback?}",
    output_key='latest_draft'
)

critic = Agent(
    name='critic', model='gemini-3-flash-preview',
    instruction=(
        "Evaluate draft: {latest_draft}. "
        "RUBRIC: 1. Must be sci-fi. 2. Must be under 100 words. "
        "If it FAILS, provide feedback. If it PASSES perfectly, call approve_draft."
    ),
    tools=[FunctionTool(approve_draft)],
    output_key='latest_feedback'
)

root_agent = LoopAgent(name="loop", sub_agents=[writer, critic], max_iterations=4)

from google.adk.apps import App
app = App(name="critic", root_agent=root_agent)
```

Видео: <https://www.youtube.com/watch?v=Kp0HrGst5-w>

---

### day13 — Multi-Agent Patterns: Iterative Refinement  
⚪ · Multi-Agent, Agent Skills, MCP, Code Execution

Compose Skills, MCP, and Code Execution into a meta-agent that builds, tests, and refines other ADK agents through iterative loops.

Ссылки:
- [Companion Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-iterative-refinement) — Full source code with skills, tools, and demo queries.
- [ADK Skills Documentation](https://google.github.io/adk-docs/skills/) — How to build and load modular knowledge packages for agents.
- [ADK Code Execution](https://google.github.io/adk-docs/integrations/code-execution/) — Code executor options: Unsafe Local, Container, and Agent Engine Sandbox.
- [Sculptor Pattern (Multi-Agent Patterns in ADK)](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/) — Google's guide to iterative refinement and other multi-agent patterns.

Код (`agent.py`):

```python
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.code_executors import UnsafeLocalCodeExecutor
from google.adk.skills import load_skill_from_dir, SkillToolset
from google.adk.tools.mcp import McpToolset, StdioConnectionParams, StdioServerParameters

# Code executor sub-agent (cannot coexist with other tools on the same agent)
code_executor_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="code_executor",
    instruction="Execute Python code exactly as provided. Return stdout and stderr.",
    code_executor=UnsafeLocalCodeExecutor(),
)

# Root agent composes all four tool groups
root_agent = Agent(
    model="gemini-3.1-flash-preview",
    name="agent_builder",
    instruction="You are an ADK Agent Builder...",
    tools=[
        skill_toolset,        # ADK coding knowledge (3 skills)
        adk_docs_mcp,         # Live ADK documentation (MCP)
        AgentTool(agent=code_executor_agent),  # Code execution
        save_agent_code,      # Save tested code to disk
        start_agent,          # Launch as adk api_server
        talk_to_agent,        # Send messages to running agent
        stop_agent,           # Shut down running agent
    ],
)
```

Код (`terminal`):

```bash
# Clone and run the meta-agent
git clone https://github.com/lavinigam-gcp/build-with-adk.git
cd build-with-adk/adk-iterative-refinement
python3 -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
cp app/.env.example app/.env  # Add your GOOGLE_API_KEY
adk web app

# Then ask: "Build me a joke agent with one tool called tell_joke"
```

Видео: <https://www.youtube.com/watch?v=weAygSpui4w>

---

### day14 — Multi-Agent Patterns: Human in the Loop  
🟡 · Multi-Agent, ADK, Human-in-the-Loop, Security

Inject an approval breakpoint to pause agent execution and wait for manual user confirmation before executing sensitive financial APIs.

Ссылки:
- [ADK Multi-Agent Design Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/) — Review standard architectural patterns for agent deployment.
- [Tool Configuration Docs](https://google.github.io/adk-docs/tools/configuration) — Learn how to secure tools with approval breakpoints and access scopes.
- [Human-in-the-Loop Pattern](https://google.github.io/adk-docs/agents/multi-agents/#human-in-the-loop-pattern) — Explore the official documentation for the Human-in-the-loop architectural pattern.

Код (`agents/refund_agent.py`):

```python
import asyncio
from typing import Any
from google.adk.agents import Agent
from google.adk.events import Event
from google.adk.runners import Runner
from google.adk.tools import LongRunningFunctionTool
from google.adk.sessions import InMemorySessionService
from google.genai import types


# 1. Define a tool that requires human approval
def ask_for_approval(purpose: str, amount: float) -> dict[str, Any]:
    """Ask a human to approve this action before proceeding."""
    return {"status": "pending", "purpose": purpose, "amount": amount}


# 2. Define the tool that runs after approval
def process_refund(purpose: str, amount: float) -> dict[str, str]:
    """Process the approved refund."""
    return {"status": "success", "message": f"Refunded ${amount} for {purpose}."}


# 3. Create the agent with a LongRunningFunctionTool
agent = Agent(
    name="refund_agent",
    model="gemini-3.1-pro",
    instruction="""You handle refunds. Always call ask_for_approval first.
    If approved, call process_refund. If rejected, tell the user.""",
    tools=[LongRunningFunctionTool(func=ask_for_approval), process_refund],
)


async def main():
    # 4. Set up session and runner
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="hitl-app", user_id="user1", session_id="s1"
    )
    runner = Runner(agent=agent, app_name="hitl-app", session_service=session_service)

    # 5. Run the agent — it will pause when it hits ask_for_approval
    user_msg = types.Content(
        role="user",
        parts=[types.Part(text="Refund $200 for a duplicate charge on txn_123")],
    )

    # Two-step detection:
    #  - Step A: find the function_call on the event with long_running_tool_ids
    #  - Step B: find the function_response matching that call ID
    long_running_call = None
    pending_response = None

    async for event in runner.run_async(
        session_id=session.id, user_id="user1", new_message=user_msg
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                # Step A: capture the long-running function *call*
                if (
                    not long_running_call
                    and part.function_call
                    and event.long_running_tool_ids
                    and part.function_call.id in event.long_running_tool_ids
                ):
                    long_running_call = part.function_call

                # Step B: capture the matching function *response*
                if (
                    long_running_call
                    and part.function_response
                    and part.function_response.id == long_running_call.id
                ):
                    pending_response = part.function_response

            # Print any agent text
            text = "".join(p.text or "" for p in event.content.parts)
            if text:
                print(f"Agent: {text}")

    if not pending_response:
        return

    # 6. Get human decision
    print(f"\n⏸  Pending: {pending_response.response}")
    choice = input("Approve? [Y/n]: ").strip().lower()

    # 7. Send decision back — agent resumes
    updated = pending_response.model_copy(deep=True)
    updated.response = {"status": "approved" if choice != "n" else "rejected"}

    async for event in runner.run_async(
        session_id=session.id,
        user_id="user1",
        new_message=types.Content(
            role="user", parts=[types.Part(function_response=updated)]
        ),
    ):
        if event.content and event.content.parts:
            text = "".join(p.text or "" for p in event.content.parts)
            if text:
                print(f"Agent: {text}")


if __name__ == "__main__":
    asyncio.run(main())
```

Видео: <https://www.youtube.com/watch?v=IqtGuk-aM60>

---

### day15 — Grounding with ADK: Agentic RAG with Vector Search 2.0  
⚪ · ADK, Vector Search, RAG, Python

Build an Agentic RAG system in 3 minutes with Vector Search 2.0 and ADK.

Ссылки:
- [10-Minute Agentic RAG with the New Vector Search 2.0 and ADK](https://medium.com/google-cloud/10-minute-agentic-rag-with-the-new-vector-search-2-0-and-adk-655fff0bacac) — More details on the Agentic RAG architecture.
- [Travel Agent Notebook](https://github.com/google/adk-samples/blob/main/python/notebooks/grounding/vectorsearch2_travel_agent.ipynb) — Sample notebook for the Travel Agent.
- [Enhancing search with embeddings and task types](https://cloud.google.com/blog/products/ai-machine-learning/improve-gen-ai-search-with-vertex-ai-embeddings-and-task-types) — Learn how task type embeddings work.
- [ADK Documentation](https://google.github.io/adk-docs/) — Complete guide to building AI agents.

Код (`terminal`):

```bash
export GOOGLE_CLOUD_PROJECT=<YOUR_PROJECT_ID>
gcloud auth application-default login
gcloud services enable vectorsearch.googleapis.com aiplatform.googleapis.com

uv run --with google-adk --with google-cloud-vectorsearch \
       --with pandas --with requests demo.py
```

Код (`demo.py`):

```python
import asyncio, io, json, os, time
import pandas as pd, requests
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.cloud import vectorsearch_v1beta

PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
LOCATION = "us-central1"
COLLECTION_ID = "london-rentals-demo"

os.environ["GOOGLE_CLOUD_LOCATION"] = LOCATION
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

admin_client = vectorsearch_v1beta.VectorSearchServiceClient()
data_client = vectorsearch_v1beta.DataObjectServiceClient()
search_client = vectorsearch_v1beta.DataObjectSearchServiceClient()
parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
collection_path = f"{parent}/collections/{COLLECTION_ID}"

print("Step 1: Creating collection with auto-embedding...")
collection_config = {
    "data_schema": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "number"},
            "neighborhood": {"type": "string"},
            "description": {"type": "string"},
        },
    },
    "vector_schema": {
        "description_embedding": {
            "dense_vector": {
                "dimensions": 768,
                "vertex_embedding_config": {
                    "model_id": "gemini-embedding-001",
                    "text_template": "{description}",
                    "task_type": "RETRIEVAL_DOCUMENT",
                },
            }
        }
    },
}

try:
    admin_client.get_collection(name=collection_path)
    print(f"Step 1: Collection '{COLLECTION_ID}' already exists.")
except Exception:
    req = vectorsearch_v1beta.CreateCollectionRequest(
        parent=parent, collection_id=COLLECTION_ID, collection=collection_config
    )
    admin_client.create_collection(request=req).result()
    print(f"Step 1: Collection '{COLLECTION_ID}' created.")

print("Step 2: Downloading and ingesting data...")
url = "https://data.insideairbnb.com/united-kingdom/england/london/2025-09-14/data/listings.csv.gz"
df = pd.read_csv(io.BytesIO(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content), compression="gzip")
df = df[["id", "name", "description", "price", "neighbourhood_cleansed"]].copy()
df["price"] = pd.to_numeric(df["price"].astype(str).str.replace(r"[$,]", "", regex=True), errors="coerce").fillna(0.0)
df = df.fillna("")
df = df[df["description"].str.strip().astype(bool)]
df = df[df["price"] > 0].head(100)
print(f"Step 2: {len(df)} listings ready for ingestion.")

data_objects = [
    {"data_object_id": str(row["id"]), "data_object": {
        "data": {"name": str(row["name"]), "price": float(row["price"]),
                 "neighborhood": str(row["neighbourhood_cleansed"]),
                 "description": str(row["description"])},
        "vectors": {},
    }} for _, row in df.iterrows()
]

for i in range(0, len(data_objects), 100):
    try:
        data_client.batch_create_data_objects(
            request=vectorsearch_v1beta.BatchCreateDataObjectsRequest(
                parent=collection_path, requests=data_objects[i:i+100]))
        time.sleep(2)
    except Exception as e:
        if "already exists" not in str(e).lower():
            raise
print("Step 2: Ingestion complete.")

print("Step 3: Registering search tool...")
def find_rentals(query: str, filter: str = "") -> list:
    """Search for vacation rentals using semantic search with metadata filtering."""
    print(f"\nfind_rentals(): query='{query}'")
    if filter.strip():
        print(f"find_rentals(): filter={filter}")

    search_kwargs = {
        "search_text": query,
        "search_field": "description_embedding",
        "task_type": "QUESTION_ANSWERING",
        "top_k": 10,
        "output_fields": vectorsearch_v1beta.OutputFields(
            data_fields=["name", "price", "neighborhood"]),
    }
    if filter.strip():
        search_kwargs["filter"] = json.loads(filter)

    response = search_client.search_data_objects(
        request=vectorsearch_v1beta.SearchDataObjectsRequest(
            parent=collection_path,
            semantic_search=vectorsearch_v1beta.SemanticSearch(**search_kwargs)))

    results = [{"name": r.data_object.data.get("name"),
             "price": r.data_object.data.get("price"),
             "neighborhood": r.data_object.data.get("neighborhood")}
            for r in response.results]
    print(f"find_rentals(): found {len(results)} results")
    return results

print("Step 4: Creating ADK agent...")
travel_agent = Agent(
    model="gemini-2.5-flash",
    name="travel_agent",
    instruction="""You are a London travel agent helping users find vacation rentals.
Use find_rentals with: query (vibe/description) and filter (JSON metadata constraints).
Filter fields: price (number), neighborhood (string).
Examples: {"price": {"$lt": 200}}, {"neighborhood": {"$eq": "Hackney"}},
{"$and": [{"neighborhood": {"$eq": "Hackney"}}, {"price": {"$lt": 200}}]}""",
    tools=[find_rentals],
)

runner = InMemoryRunner(agent=travel_agent, app_name="travel_agent")
print("Step 4: Agent ready.\n")

async def main():
    await runner.run_debug("Find me a cozy workspace")
    await runner.run_debug("Find me a cozy workspace under £200")
    await runner.run_debug("Find me an artist's loft in Hackney under £150")

if __name__ == "__main__":
    asyncio.run(main())
```

Видео: <https://www.youtube.com/watch?v=IB6cXNx5iaw>

---

### day16 — ADK Dev Skills: Accelerated Multiagent Triage  
🟡 · Multiagent, Dev Skills, CLI

Accelerate multiagent system development from scaffolding to deployment using ADK Dev Skills.

Ссылки:
- [ADK Dev Skills](https://google.github.io/adk-docs/tutorials/coding-with-ai/#adk-dev-skills) — Installation and reference for all available ADK skills.
- [ADK Multi-Agent Systems](https://google.github.io/adk-docs/agents/multi-agents/) — Learn how to orchestrate multiagent delegation.

Код (`terminal.sh`):

```bash
# Install ADK Dev Skills globally
npx skills add google/adk-docs/skills -y -g

# Instruct your AI assistant to use the skills
gemini run "Use adk-scaffold to build a multiagent Retail Returns system, then use adk-deploy-guide to push it to Agent Engine."
```

Код (`agent.py`):

```python
import os
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from .tools import check_order_status, process_refund

# Sub-agents generated via ADK Dev Skills guidance
def create_status_agent() -> Agent:
    return Agent(
        name="status_agent",
        model=Gemini(model="gemini-3.1-flash"),
        instruction="Look up orders using the check_order_status tool.",
        tools=[check_order_status],
    )

def create_refund_agent() -> Agent:
    return Agent(
        name="refund_agent",
        model=Gemini(model="gemini-3.1-flash"),
        instruction="Verify order status is 'delivered' before using process_refund.",
        tools=[check_order_status, process_refund],
    )

# Parent triage agent routing logic
root_agent = Agent(
    name="triage_agent",
    model=Gemini(model="gemini-3.1-flash"),
    instruction="Route user requests to either the status_agent or refund_agent.",
    sub_agents=[create_status_agent(), create_refund_agent()],
)

app = App(name="retail_returns_app", root_agent=root_agent)
```

Видео: <https://www.youtube.com/watch?v=7PNOkMLAk4c>

---

### day17 — Workspace & Gemini Enterprise: no-code agents  
🟡 · Gemini Enterprise, Google Workspace, Connectors, Agent Designer

Connect and use Google Workspace connectors in personal Gemini Enterprise agents.

Ссылки:
- [Codelab: Integrate Gemini Enterprise Agents with Google Workspace](https://codelabs.developers.google.com/ge-gws-agents) — Step-by-step guide to building the integration.
- [Gemini Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/docs) — Official documentation for Gemini Enterprise.
- [Google Workspace Developers](https://developers.google.com/workspace) — Build solutions with Google Workspace.
- [Connect a Google Data Source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store) — Learn how to connect Workspace data to Gemini.
- [Agent Designer Overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer) — Build agents without writing code.

Код (`terminal`):

```bash
# No code solution - Check the video and codelab!
```

Видео: <https://www.youtube.com/watch?v=2kQbRBftUus>

---

### day18 — Workspace & Gemini Enterprise: ADK agents  
🟡 · Gemini Enterprise, Google Workspace, ADK, MCP, Vertex AI

Build ADK agents that use the Vertex AI Search MCP server and Google Workspace APIs, deploy them to Vertex AI, and register them with Gemini Enterprise.

Ссылки:
- [Codelab: Integrate Gemini Enterprise Agents with Google Workspace](https://codelabs.developers.google.com/ge-gws-agents) — Step-by-step guide to building the integration.
- [Gemini Enterprise Documentation](https://docs.cloud.google.com/gemini/enterprise/docs) — Official documentation for Gemini Enterprise.
- [Google Workspace Developers](https://developers.google.com/workspace) — Build solutions with Google Workspace.
- [Register and manage ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent) — Hosted on Vertex AI Agent Engine.

Код (`terminal`):

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

Видео: <https://www.youtube.com/watch?v=dVBvx9r-D-4>

---

### day19 — Live Shopping Agent: Build with ADK and Gemini Embedding 2  
🟡 · ADK, Gemini Live, Vector Search

Build a live multimodal shopping app with ADK and Gemini Embedding 2.

Ссылки:
- [LensMosaic Live Demo](https://lens-mosaic-761793285222.us-central1.run.app/)
- [ADK Gemini Live API Toolkit](https://google.github.io/adk-docs/streaming/)
- [Gemini Embedding 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/embedding-2)
- [Vertex AI Vector Search 2.0](https://cloud.google.com/vertex-ai/docs/vector-search-2/overview)

Код (`shell`):

```shell
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID # replace
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_LOCATION=us-central1
uv run \
  --with google-adk \
  --with google-genai \
  --with google-cloud-aiplatform \
  --with certifi \
  uvicorn main:app --host 127.0.0.1 --port 8080

# Then open http://127.0.0.1:8080 with browser
```

Код (`main.py`):

```python
"""Minimal LensMosaic live server."""

from __future__ import annotations

import asyncio, base64, json, logging, os, ssl
import urllib.error, urllib.parse, urllib.request
from dataclasses import dataclass, field

import certifi
from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from google.adk.agents import Agent
from google.adk.agents.live_request_queue import LiveRequestQueue
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext
from google.genai import errors as genai_errors
from google.genai import types

import vertexai

os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "TRUE")

# App configuration and external service setup.
APP_NAME = "lens-mosaic-blog-sample"
AGENT_MODEL = "gemini-live-2.5-flash-native-audio"
MAX_TILE_ITEMS = 64
GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
GOOGLE_CLOUD_LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]
LENS_MOSAIC_COLLECTION_ID = "mercari3m-collection-mm2"
HOSTED_URL = "https://lens-mosaic-nhhfh7g7iq-uc.a.run.app"

vertexai.init(
    project=GOOGLE_CLOUD_PROJECT,
    location=GOOGLE_CLOUD_LOCATION,
)


# Per-live-session state shared across websocket handlers.
@dataclass
class SessionState:
    session_id: str
    user_id: str | None = None
    recommended: list[dict] = field(default_factory=list)
    tile_client: WebSocket | None = None


SESSION_STATES: dict[str, SessionState] = {}
SESSION_SERVICE = InMemorySessionService()
MAIN_LOOP: asyncio.AbstractEventLoop | None = None
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def _ignore_normal_live_close(record: logging.LogRecord) -> bool:
    exc = record.exc_info[1] if record.exc_info else None
    return not (isinstance(exc, genai_errors.APIError) and exc.code == 1000)


logging.getLogger(
    "google_adk.google.adk.flows.llm_flows.base_llm_flow"
).addFilter(_ignore_normal_live_close)


# Session lifecycle helpers.
def session_state_for(
    session_id: str, user_id: str | None = None
) -> SessionState:
    state = SESSION_STATES.get(session_id)
    if state is None:
        state = SessionState(session_id=session_id, user_id=user_id)
        SESSION_STATES[session_id] = state
        return state
    if user_id is not None:
        state.user_id = user_id
    return state


def cleanup_session(session_id: str) -> None:
    session = SESSION_STATES.get(session_id)
    if session and session.user_id is None and session.tile_client is None:
        SESSION_STATES.pop(session_id, None)


# Upstream proxy helpers for the hosted UI and APIs.
def fetch_upstream(
    path: str,
    *,
    method: str = "GET",
    body: bytes | None = None,
    content_type: str | None = None,
    query: list[tuple[str, str]] | None = None,
) -> tuple[int, str, bytes]:
    # Keep local sample routes thin by forwarding most HTTP work upstream.
    url = f"{HOSTED_URL}{path}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"
    headers = {"Content-Type": content_type} if content_type else {}
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30, context=SSL_CONTEXT) as response:
            return response.status, response.headers.get("Content-Type", ""), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers.get("Content-Type", ""), exc.read()


async def proxy_upstream(
    path: str,
    *,
    method: str = "GET",
    body: bytes | None = None,
    content_type: str | None = None,
    query: list[tuple[str, str]] | None = None,
) -> Response:
    status, media_type, data = await asyncio.to_thread(
        fetch_upstream,
        path,
        method=method,
        body=body,
        content_type=content_type,
        query=query,
    )
    return Response(content=data, status_code=status, media_type=media_type)


# Tile update helpers used by the local recommendation tool.
async def broadcast_recommended(session_id: str, items: list[dict]) -> None:
    session = SESSION_STATES.get(session_id)
    if not session:
        return
    ws = session.tile_client
    if ws is None:
        return
    try:
        await ws.send_json({"kind": "recommended", "items": items})
    except Exception:
        if session.tile_client is ws:
            session.tile_client = None


# Tool and agent definitions for the local live assistant.
def find_items(
    queries: list[str], ranking_query: str, tool_context: ToolContext
) -> str:
    """Find shopping items that match one or more product description queries.

    Use this tool to show product candidates on screen. Provide descriptive
    product-search queries and a ranking query in English. The tool searches,
    publishes the matched items to the UI, and uses ranking_query for the
    final rerank across the candidates.

    Args:
        queries: One or more product-search queries in English.
        ranking_query: A short English description used for final reranking.
        tool_context: ADK tool context for the current user session.

    Returns:
        A comma-separated string of top matched item names, or "No items found".
    """
    status, _, body = fetch_upstream(
        "/search",
        method="POST",
        body=json.dumps(
            {"queries": queries[:4], "ranking_query": ranking_query}
        ).encode(),
        content_type="application/json",
    )
    items = [] if status >= 400 else json.loads(body.decode())
    session = session_state_for(tool_context.session.id, tool_context.session.user_id)
    session.recommended = items[:MAX_TILE_ITEMS]
    if MAIN_LOOP:
        # Tool calls run off the main loop, so schedule the tile push back onto it.
        asyncio.run_coroutine_threadsafe(
            broadcast_recommended(session.session_id, session.recommended),
            MAIN_LOOP,
        )
    names = [item.get("name", "") for item in session.recommended[:3] if item.get("name")]
    return ", ".join(names) if names else "No items found"


agent = Agent(
    name="blog_sample_agent",
    model=AGENT_MODEL,
    tools=[find_items],
    instruction="""
        You are a helpful AI shopping assistant. Always respond in the user's language.
        You can hear the user's voice, read their text, and see camera images.
        When user asks what's in the image, describe it.
        When user asks for finding items, recommendation, or matching-product requests:
        - Do not ask a follow-up question before searching.
        - Briefly say what you will search.
        - Infer the desired items from the conversation and camera context.
        - Call find_items with 5 descriptive queries and a ranking_query.
        - After find_items returns, mention a few item names in simple language.""",
)
RUNNER = Runner(app_name=APP_NAME, agent=agent, session_service=SESSION_SERVICE)
RUN_CONFIG = RunConfig(
    streaming_mode=StreamingMode.BIDI,
    response_modalities=["AUDIO"],
    session_resumption=types.SessionResumptionConfig(),
)
app = FastAPI(title="LensMosaic Blog Sample", version="0.1.0")


# Live websocket communication between the browser and ADK.
async def ensure_adk_session(user_id: str, session_id: str) -> None:
    if not await SESSION_SERVICE.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id):
        await SESSION_SERVICE.create_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)


async def client_to_agent(ws: WebSocket, queue: LiveRequestQueue) -> None:
    while True:
        message = await ws.receive()
        if message.get("bytes") is not None:
            queue.send_realtime(
                types.Blob(mime_type="audio/pcm;rate=16000", data=message["bytes"])
            )
            continue
        if message.get("text") is None:
            continue
        payload = json.loads(message["text"])
        if payload.get("type") == "text":
            queue.send_content(types.Content(parts=[types.Part(text=payload["text"])]))
            continue
        if payload.get("type") != "image":
            continue
        if payload.get("forwardToAgent", True):
            queue.send_realtime(
                types.Blob(
                    mime_type=payload.get("mimeType", "image/jpeg"),
                    data=base64.b64decode(payload["data"]),
                )
            )


async def agent_to_client(user_id: str, session_id: str, ws: WebSocket, queue: LiveRequestQueue) -> None:
    # Stream ADK events straight back to the browser without reshaping them.
    async for event in RUNNER.run_live(
        user_id=user_id,
        session_id=session_id,
        live_request_queue=queue,
        run_config=RUN_CONFIG,
    ):
        await ws.send_text(event.model_dump_json(exclude_none=True, by_alias=True))


def is_disconnect_error(exc: Exception) -> bool:
    if isinstance(exc, RuntimeError):
        return "disconnect message has been received" in str(exc)
    if isinstance(exc, genai_errors.APIError):
        return exc.code == 1000
    return False


# FastAPI app lifecycle and proxied HTTP routes.
@app.on_event("startup")
async def startup() -> None:
    global MAIN_LOOP
    MAIN_LOOP = asyncio.get_running_loop()


@app.get("/")
async def root() -> Response:
    return await proxy_upstream("/")


@app.get("/static/{path:path}")
async def static_proxy(path: str, request: Request) -> Response:
    return await proxy_upstream(f"/static/{path}", query=list(request.query_params.multi_items()))


@app.post("/search")
async def search_proxy(request: Request) -> Response:
    body = await request.body()
    return await proxy_upstream("/search", method="POST", body=body, content_type=request.headers.get("content-type"))


@app.get("/api/item/{item_id}")
async def item_proxy(item_id: str) -> Response:
    return await proxy_upstream(f"/api/item/{item_id}")


# FastAPI websocket endpoints for recommendation tiles and live chat.
@app.websocket("/ws_image_tile/{session_id}")
async def tile_socket(ws: WebSocket, session_id: str) -> None:
    await ws.accept()
    session = session_state_for(session_id)
    session.tile_client = ws
    try:
        # New tile clients receive the latest recommendation snapshot immediately.
        await ws.send_json({"kind": "snapshot", "similarItems": [], "recommendedItems": session.recommended})
        while True:
            await ws.receive()
    except WebSocketDisconnect:
        pass
    except (RuntimeError, genai_errors.APIError) as exc:
        if not is_disconnect_error(exc):
            raise
    finally:
        if session.tile_client is ws:
            session.tile_client = None
        cleanup_session(session_id)


@app.websocket("/ws/{user_id}/{session_id}")
async def live_socket(ws: WebSocket, user_id: str, session_id: str) -> None:
    await ws.accept()
    await ensure_adk_session(user_id, session_id)
    session = session_state_for(session_id, user_id)
    # One queue feeds the ADK runner while both websocket tasks stay in sync.
    queue = LiveRequestQueue()
    try:
        await asyncio.gather(
            client_to_agent(ws, queue),
            agent_to_client(user_id, session_id, ws, queue),
        )
    except WebSocketDisconnect:
        pass
    except (RuntimeError, genai_errors.APIError) as exc:
        if not is_disconnect_error(exc):
            raise
    finally:
        queue.close()
        session.user_id = None
        cleanup_session(session_id)
```

Видео: <https://www.youtube.com/watch?v=SgMn-6q8Qg8>

---

### day20 — ADK Agent Harness: Build a Generate-Validate-Refine Pipeline  
⚪ · ADK, MCP, Multi-Agent, Skills

Build a README improvement harness that fetches a GitHub repo via MCP, generates against a quality checklist, and refines in a loop until a critic approves.

Ссылки:
- [ADK Skills](https://google.github.io/adk-docs/skills/)
- [ADK MCP Tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- [ADK API Server](https://google.github.io/adk-docs/runtime/api-server/)
- [Demo Video 2](https://youtu.be/jh4kYgUSF-M)

Код (`shell`):

```shell
export GITHUB_PERSONAL_ACCESS_TOKEN=your_token

# Start ADK harness as an API server
adk api_server . --port 8000

# Copy the bundled skill to Gemini CLI
cp -r cli_harness ~/.gemini/skills/cli_harness

# In Gemini CLI:
# > Improve the README for google/adk-samples

# Or for Claude Code, copy to:
# cp -r cli_harness ~/.claude/skills/cli_harness
```

Код (`agent.py`):

```python
import os, pathlib
from google.adk.agents import Agent, LoopAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.skills import load_skill_from_dir
from google.adk.tools import exit_loop
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.skill_toolset import SkillToolset
from mcp import StdioServerParameters

SKILLS_DIR = pathlib.Path(__file__).parent / "skills"

github_mcp = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx", args=["-y", "@modelcontextprotocol/server-github"],
            env={"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", "")},
        ),
    ),
    tool_filter=["get_file_contents", "search_code", "list_commits"],
)

readme_skill = SkillToolset(
    skills=[load_skill_from_dir(SKILLS_DIR / "readme-conventions")]
)

async def init_loop_state(callback_context: CallbackContext) -> None:
    if "criticism" not in callback_context.state:
        callback_context.state["criticism"] = "No previous feedback. This is the first draft."

codebase_analyzer = Agent(
    model="gemini-3-flash-preview", name="codebase_analyzer",
    instruction="Analyze the GitHub repo. Read the file tree and key source files. Output a structured summary.",
    tools=[github_mcp], output_key="codebase_analysis",
)
readme_writer = Agent(
    model="gemini-3-flash-preview", name="readme_writer",
    before_agent_callback=init_loop_state,
    instruction="Write or improve the README using {codebase_analysis}. Address all points in {criticism}.",
    tools=[readme_skill], output_key="current_readme",
)
readme_critic = Agent(
    model="gemini-3-flash-preview", name="readme_critic",
    instruction="Review {current_readme} against the checklist. Call exit_loop if all sections pass.",
    tools=[exit_loop], output_key="criticism",
)

root_agent = SequentialAgent(
    name="readme_harness",
    sub_agents=[
        codebase_analyzer,
        LoopAgent(name="refinement_loop", sub_agents=[readme_writer, readme_critic], max_iterations=3),
    ],
)
```

Видео: <https://www.youtube.com/watch?v=Bub9U7bQX4A>

---

### day21 — Developer's Guide to AI Agent Protocols  
🟡 · MCP, A2A, UCP, AP2, A2UI, AG-UI, ADK, Protocols

Six protocols, disambiguated. See how MCP, A2A, UCP, AP2, A2UI, and AG-UI work together to build a production-ready supply chain agent with ADK.

Ссылки:
- [Developer's Guide to AI Agent Protocols (Blog)](https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/) — The full walkthrough with code samples for all six protocols
- [MCP — Model Context Protocol](https://modelcontextprotocol.io/) — Standard connection pattern for agent-to-tool integration
- [A2A — Agent2Agent Protocol](https://a2a-protocol.org/) — Discovery and communication between agents
- [UCP — Universal Commerce Protocol](https://ucp.dev/) — Standardized shopping lifecycle for agentic commerce
- [AP2 — Agent Payments Protocol](https://github.com/google-agentic-commerce/AP2) — Payment authorization with typed mandates and audit trails
- [A2UI — Agent-to-User Interface Protocol](https://a2ui.org/) — Declarative JSON format for agent-generated UIs
- [AG-UI — Agent-User Interaction Protocol](https://docs.ag-ui.com/) — Standardized SSE streaming from agent to frontend
- [ADK MCP Integrations](https://google.github.io/adk-docs/integrations/) — Browse available MCP integrations for ADK

Код (`mcp_tools.py`):

```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.toolbox_toolset import ToolboxToolset
from mcp import StdioServerParameters

# 1. Connect to a database via MCP Toolbox for Databases
inventory_tools = ToolboxToolset(server_url="http://localhost:5000")

# 2. Connect to Notion for recipes via MCP
notion_tools = McpToolset(connection_params=StdioConnectionParams(
    server_params=StdioServerParameters(
        command="npx", args=["-y", "@notionhq/notion-mcp-server"],
        env={"NOTION_TOKEN": "your-token"}),
    timeout=30))

# 3. Build the agent — MCP tools are discovered automatically
kitchen_agent = Agent(
    model="gemini-3-flash-preview",
    name="kitchen_manager",
    instruction="You manage a restaurant kitchen. Check inventory, look up recipes.",
    tools=[inventory_tools, notion_tools],
)
```

Код (`a2a_discover.py`):

```python
# Turn any ADK agent into an A2A service (server side)
from google.adk.a2a.utils.agent_to_a2a import to_a2a
app = to_a2a(pricing_agent, port=8001)

# Discover and call a remote A2A agent (client side)
from a2a.client.client_factory import ClientFactory
from a2a.client.helpers import create_text_message_object

client = await ClientFactory.connect("http://pricing-agent:8001")
card = await client.get_card()
print(f"{card.name} - {card.description}")
# -> "pricing_agent - Checks today's wholesale market prices."

msg = create_text_message_object(
    content="What's today's wholesale price for salmon?")
async for response in client.send_message(msg):
    print(response)  # Task with artifacts or direct Message
```

Код (`a2ui_components.py`):

```python
# A2UI: Agent sends declarative JSON, renderer turns it into native UI.
# 18 component primitives — same building blocks, any frontend.

a2ui_messages = [
    # 1. Create a rendering surface
    {"beginRendering": {"surfaceId": "default", "root": "card"}},

    # 2. Send the component tree (flat list, ID references)
    {"surfaceUpdate": {"surfaceId": "default", "components": [
        {"id": "card", "component": {"Card": {"child": "col"}}},
        {"id": "col", "component": {"Column": {"children": {
            "explicitList": ["title", "price", "buy"]}}}},
        {"id": "title", "component": {"Text": {"usageHint": "h3",
            "text": {"path": "name"}}}},
        {"id": "price", "component": {"Text": {"text": {"path": "price"}}}},
        {"id": "buy", "component": {"Button": {"child": "btn-label",
            "action": {"name": "purchase",
            "context": [{"key": "item", "value": {"path": "name"}}]}}}},
        {"id": "btn-label", "component": {"Text": {
            "text": {"literalString": "Buy Now"}}}},
    ]}},

    # 3. Send the data (separate from structure)
    {"dataModelUpdate": {"surfaceId": "default", "contents": [
        {"key": "name", "valueString": "Fresh Atlantic Salmon"},
        {"key": "price", "valueString": "$24.00/lb"},
    ]}},
]
```

Код (`agui_streaming.py`):

```python
# AG-UI: Wrap any ADK agent as a streaming endpoint in 3 lines
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
from fastapi import FastAPI

ag_ui_agent = ADKAgent(adk_agent=kitchen_mgr, app_name="kitchen", user_id="chef")
app = FastAPI()
add_adk_fastapi_endpoint(app, ag_ui_agent, path="/")
# Run with: uvicorn module:app

# The SSE stream emits typed events:
# RUN_STARTED
# TOOL_CALL_START toolCallName="check_inventory"
# TOOL_CALL_RESULT content="3 lbs in stock, REORDER NEEDED"
# TOOL_CALL_END
# TEXT_MESSAGE_CONTENT delta="Based on "
# TEXT_MESSAGE_CONTENT delta="current inventory..."
# RUN_FINISHED
```

Видео: <https://www.youtube.com/watch?v=DAZpxBF6Zfc>

---

### day22 — ADK Evaluation: Trajectory Tests and Rubric-Based Scoring  
🟡 · ADK, Evaluation, CI/CD, Testing

Define deterministic trajectory tests and rubric-based evaluations that run on every code push, catching agent regressions before they reach production.

Ссылки:
- [ADK Evaluation Docs](https://google.github.io/adk-docs/evaluate/) — Official ADK evaluation overview — evalsets, criteria, and CLI commands
- [ADK Eval Criteria Reference](https://google.github.io/adk-docs/evaluate/criteria/) — All 8 built-in metrics, match types, custom rubrics, and judge model config
- [Agent Starter Pack](https://github.com/googlecloudplatform/agent-starter-pack) — Scaffold an ADK agent project with built-in eval directory and CI/CD pipelines
- [ADK Samples](https://github.com/google/adk-samples) — Reference agents with evalsets you can study and adapt

Код (`shell`):

```bash
# 1. Scaffold an agent with the eval framework built-in
uvx agent-starter-pack create --adk my-agent && cd my-agent

# 2. Define a trajectory test in your evalset (eval/trajectory_tests.json)
# See the evalset snippet below for the full schema

# 3. Run the evaluation locally
make eval

# 4. Or run directly with the ADK CLI
adk eval ./app eval/trajectory_tests.json \
  --config_file_path=eval/eval_config.json \
  --print_detailed_results
```

Код (`eval/trajectory_tests.json`):

```json
{
  "eval_set_id": "trajectory_tests",
  "name": "Tool Trajectory Tests",
  "eval_cases": [
    {
      "eval_id": "sync_linear_to_github",
      "conversation": [
        {
          "invocation_id": "inv_1",
          "user_content": {
            "parts": [{ "text": "Sync Linear issue PROJ-123 to GitHub" }]
          },
          "final_response": {
            "role": "model",
            "parts": [{ "text": "Created GitHub issue #42 from PROJ-123." }]
          },
          "intermediate_data": {
            "tool_uses": [
              { "name": "linear_get_issue", "args": { "issue_id": "PROJ-123" } },
              { "name": "github_create_issue", "args": { "repo": "my-org/my-repo" } }
            ]
          }
        }
      ],
      "session_input": {
        "app_name": "my_agent", "user_id": "eval_user", "state": {}
      }
    }
  ]
}
```

Код (`eval/eval_config.json`):

```json
{
  "criteria": {
    "tool_trajectory_avg_score": {
      "threshold": 1.0,
      "match_type": "IN_ORDER"
    },
    "rubric_based_final_response_quality_v1": {
      "threshold": 0.8,
      "rubrics": [
        {
          "rubric_id": "completeness",
          "rubric_content": {
            "text_property": "The response must confirm which issue was synced and provide the new GitHub issue number."
          }
        }
      ]
    }
  }
}
```

Видео: <https://www.youtube.com/watch?v=_JVwS-20fTg>

---

### day23 — Model Armor: AI Security Firewall for Agents  
🟡 · Model Armor, Security, GCP, Agent Safety

Protect AI agents from prompt injection, jailbreaks, and data leakage using Google Cloud Model Armor as a defense-in-depth security layer.

Ссылки:
- [Model Armor Documentation](https://docs.cloud.google.com/model-armor/overview) — Complete guide to Google Cloud Model Armor for AI security.
- [GitHub Project Repository](https://github.com/lekan2001/advent-of-agents-model-armor.git) — Working implementation of Model Armor with ADK agents.
- [ADK Documentation](https://google.github.io/adk-docs/) — Agent Development Kit documentation for building secure agents.

Код (`model_armor_security.py`):

```python
def sanitize_prompt(user_prompt: str) -> tuple[bool, str]:
    """Sanitize a user prompt using the Model Armor template.

    Args:
        user_prompt: The raw user prompt text to sanitize.

    Returns:
        A tuple of (is_safe, detail).
        - is_safe: True if the prompt passes all checks, False if blocked.
        - detail: Empty string when safe, or a description of why it was blocked.
    """
    try:
        client = _get_client()
        request = modelarmor_v1.SanitizeUserPromptRequest(
            name=TEMPLATE_NAME,
            user_prompt_data=modelarmor_v1.DataItem(text=user_prompt),
        )
        response = client.sanitize_user_prompt(request=request)
        blocked, reasons = _is_blocked(response.sanitization_result)
        if blocked:
            logger.warning("Model Armor blocked user prompt: %s", reasons)
            return False, reasons
        return True, ""
    except Exception:
        logger.exception("Model Armor sanitize_prompt call failed")
        return True, ""
```

Код (`model_armor_security.py`):

```python
def sanitize_response(model_response: str) -> tuple[bool, str]:
    """Sanitize a model response using the Model Armor template.

    Args:
        model_response: The model-generated response text to sanitize.

    Returns:
        A tuple of (is_safe, detail).
        - is_safe: True if the response passes all checks, False if blocked.
        - detail: Empty string when safe, or a description of why it was blocked.
    """
    try:
        client = _get_client()
        request = modelarmor_v1.SanitizeModelResponseRequest(
            name=TEMPLATE_NAME,
            model_response_data=modelarmor_v1.DataItem(text=model_response),
        )
        response = client.sanitize_model_response(request=request)
        blocked, reasons = _is_blocked(response.sanitization_result)
        if blocked:
            logger.warning("Model Armor blocked model response: %s", reasons)
            return False, reasons
        return True, ""
    except Exception:
        logger.exception("Model Armor sanitize_response call failed")
        return True, ""
```

Видео: <https://www.youtube.com/watch?v=Wrxg8OsquEY>

---

### day24 — Batch Processing: Scale to 10k with ADK  
🟡 · Batch Processing, ADK, Scale

Shift from interactive processing to an Agent as Orchestrator pattern using the ADK and Gemini Batch API for efficient, large-scale asynchronous workloads.

Ссылки:
- [Scaling Language Detection: A Million Messages with Gemini’s Batch API & Flash Lite](https://medium.com/google-cloud/scaling-language-detection-a-million-messages-with-geminis-batch-api-flash-lite-baccc197a1c2)
- [From GenAI Demo to Production Scale - Handling high-throughput use cases](https://medium.com/google-cloud/from-genai-demo-to-production-scale-handling-high-throughput-use-cases-fbca401a5555)
- [Batch Mode in the Gemini API: Process more for less (Official Announcement)](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/)
- [Experimentation to Production with Gemini and Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/experimentation-to-production-with-gemini-and-vertex-ai)

Код (`batch_processor.py`):

```python
import os
import json
import urllib.request
from google import genai
from google.genai import types

# 1. Initialize the Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. Fetch live data from the web to create the JSONL dataset
dataset_path = "unprocessed_batch_01.jsonl"
print("Fetching live headlines from Hacker News...")

# Grab the top 5 story IDs from the public Hacker News API
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = json.loads(urllib.request.urlopen(top_stories_url).read())[:5]

# Format the live data into Gemini's JSONL Batch structure
with open(dataset_path, "w") as f:
    for sid in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        story = json.loads(urllib.request.urlopen(story_url).read())
        prompt = f"Extract companies, products, and technologies from this headline: {story.get('title', '')}"
        f.write(json.dumps({"request": {"contents": [{"parts": [{"text": prompt}]}]}}) + "\n")

# 3. Upload your JSONL dataset to the Gemini API
uploaded_file = client.files.upload(
    file=dataset_path, 
    config={'mime_type': 'application/jsonl'}
)
print(f"Uploaded file: {uploaded_file.uri}")

# 4. Submit the Asynchronous Batch Job at 50% token cost
batch_job = client.batches.create(
    model="gemini-3.1-pro-preview",
    src=uploaded_file.name,
    config=types.CreateBatchJobConfig(
        display_name="massive_document_extractor",
    )
)

print(f"Batch job {batch_job.name} submitted successfully.")
print(f"Current State: {batch_job.state}")

with open(".latest_batch_job.txt", "w") as cached_file:
    cached_file.write(batch_job.name)
```

Код (`check_status.py`):

```python
import os
import sys
from google import genai

# 1. Initialize Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: Please export your GEMINI_API_KEY before running this script.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# 2. Get the Batch Job ID to poll
job_name = None
if len(sys.argv) > 1:
    job_name = sys.argv[1]
elif os.path.exists(".latest_batch_job.txt"):
    with open(".latest_batch_job.txt", "r") as cached_file:
        job_name = cached_file.read().strip()
    print(f"Auto-detected latest job ID from cache: {job_name}")

if not job_name:
    job_name = input("Enter the Batch Job name (e.g. batches/12345ABCD): ").strip()

if not job_name.startswith("batches/"):
    job_name = f"batches/{job_name}"

# 3. Request Status from Backend
try:
    print(f"\nPolling Google Cloud for status of: {job_name}...")
    job = client.batches.get(name=job_name)
    
    print("=" * 50)
    print(f"Job Name    : {job.name}")
    print(f"State       : {job.state}")
    
    if job.state == "JOB_STATE_SUCCEEDED":
        uri = getattr(job, "output_uri", "Available via Google Cloud Console")
        print(f"Output URI  : {uri}")
        print("\nSuccess! You can now download and parse the JSON payload.")
    elif job.state == "JOB_STATE_FAILED":
        print("\nThe job failed on the backend.")
        print("Error details:", getattr(job, "error", "Unknown API Error"))
        
    print("=" * 50)
except Exception as e:
    print(f"\nFailed to fetch job status. Ensure the ID is correct.")
    print(f"Error: {e}")
```

Код (`terminal`):

```bash
# 1. Set up a pristine Python environment
python3 -m venv .venv && source .venv/bin/activate
pip install google-genai

# 2. Export your Gemini API key
export GEMINI_API_KEY="your-secret-key"

# 3. Submit your massive dataset to the background batch service
python batch_processor.py

# 4. In a few minutes, poll for the completed workload!
python check_status.py
```

Видео: <https://www.youtube.com/watch?v=3erD0GqEzX8>

---

### day25 — Agent Deployment: How to Deploy AI Agents  
🟡 · Deployment, Agent Engine, Cloud Run, Vertex AI

Deploy your AI agents to Vertex AI Agent Engine or Google Cloud Run securely and easily.

Ссылки:
- [Google Cloud ADK Documentation](https://google.github.io/adk-docs/) — Documentation for the Google Cloud Agent Development Kit.
- [Google Cloud Run Documentation](https://cloud.google.com/run) — Learn how to run serverless containers with Cloud Run.
- [Vertex AI Agent Engine Documentation](https://cloud.google.com/vertex-ai/docs) — Documentation for Vertex AI and Agent Engine.
- [GitHub Project Repository](https://github.com/lekan2001/advent-of-agents-day-25.git) — Source code for Day 25.

Код (`terminal`):

```bash
# Setup project using Agent starter pack
uvx agent-starter-pack create

# Deploy to Vertex AI Agent Engine
make deploy
```

Код (`terminal`):

```bash
# Explicitly install dependencies via make
make install

# Deploy to Cloud Run targeting the 'app' directory
uv run adk deploy cloud_run app
```

Видео: <https://www.youtube.com/watch?v=osEDoYe60E8>

---

### day26 — Authentication: End-User Identity Propagation  
🟡 · Authentication, Security, Identity Propagation, Interactive Auth

Securely delegate permissions by prompting end-users for OAuth consent during agent execution.

Ссылки:
- [ADK Tool Authentication](https://google.github.io/adk-docs/tools-custom/authentication/index.md)
- [Interactive OAuth CLI Example](https://google.github.io/adk-docs/tools-custom/authentication/index.md#handling-the-interactive-oauthoidc-flow-client-side) — Documentation on how to authenticate agents in ADK.
- [OAuth Calendar Agent Sample](https://github.com/google/adk-python/blob/main/contributing/samples/oauth_calendar_agent/agent.py) — Sample demonstrating AuthenticatedFunctionTool.
- [Dynamic Identity Propagation (ServiceNow)](https://github.com/google/adk-samples/tree/main/python/agents/incident-management) — Example of token passing to third-party integrations.

Код (`.env`):

```bash
# 1. Follow the steps in this document to get the OAuth2 credentials:
# https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id
# 2. Set "http://127.0.0.1:8080/dev-ui/" as the redirect URI. Pay attention to the port number you are using.
# 3. Copy your Client ID and Client Secret into a .env file. In production, use a secret management tool - never hardcode secrets or put them in .env files.

OAUTH_CLIENT_ID="your-client-id.apps.googleusercontent.com"
OAUTH_CLIENT_SECRET="your-client-secret"
```

Код (`agent.py`):

```python
from datetime import datetime
import os

from dotenv import load_dotenv
from fastapi.openapi.models import OAuth2
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.openapi.models import OAuthFlows
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import Agent
from google.adk.auth.auth_credential import AuthCredential
from google.adk.auth.auth_credential import AuthCredentialTypes
from google.adk.auth.auth_credential import OAuth2Auth
from google.adk.auth.auth_tool import AuthConfig
from google.adk.tools.authenticated_function_tool import AuthenticatedFunctionTool
from google.adk.tools.google_api_tool import CalendarToolset
from google.adk.tools.tool_context import ToolContext
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Access the variables.
oauth_client_id = os.getenv("OAUTH_CLIENT_ID")
oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET")


calendar_toolset = CalendarToolset(
    client_id=oauth_client_id,
    client_secret=oauth_client_secret,
    tool_filter=["calendar_events_get"],
)

def list_calendar_events(
    start_time: str,
    end_time: str,
    limit: int,
    tool_context: ToolContext,
    credential: AuthCredential,
) -> list[dict]:
    """Search for calendar events.

    Example:

        flights = get_calendar_events(
            calendar_id='joedoe@gmail.com',
            start_time='2024-09-17T06:00:00',
            end_time='2024-09-17T12:00:00',
            limit=10
        )
        # Returns up to 10 calendar events between 6:00 AM and 12:00 PM on
        September 17, 2024.

    Args:
        calendar_id (str): the calendar ID to search for events.
        start_time (str): The start of the time range (format is
          YYYY-MM-DDTHH:MM:SS).
        end_time (str): The end of the time range (format is YYYY-MM-DDTHH:MM:SS).
        limit (int): The maximum number of results to return.

    Returns:
        list[dict]: A list of events that match the search criteria.
    """

    creds = Credentials(
        token=credential.oauth2.access_token,
        refresh_token=credential.oauth2.refresh_token,
    )

    service = build("calendar", "v3", credentials=creds)
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_time + "Z" if start_time else None,
            timeMax=end_time + "Z" if end_time else None,
            maxResults=limit,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])
    return events


def update_time(callback_context: CallbackContext):
  # get current date time
  now = datetime.now()
  formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
  callback_context.state["_time"] = formatted_time


root_agent = Agent(
    model="gemini-3.1-pro-preview",
    name="calendar_agent",
    instruction="""
      You are a helpful personal calendar assistant.
      Use the provided tools to search for calendar events (use 10 as limit if user doesn't specify), and get information about them.
      Use "primary" as the calendarId if users don't specify.

      Scenario1:
      The user want to query the calendar events.
      Use list_calendar_events to search for calendar events.


      Scenario2:
      User want to know the details of one of the listed calendar events.
      Use google_calendar_events_get to get the details of a calendar event.

      Current user:
      <User>
      {userInfo?}
      </User>

      Current time: {_time}
""",
    tools=[
      AuthenticatedFunctionTool(
            func=list_calendar_events,
            auth_config=AuthConfig(
                auth_scheme=OAuth2(
                    flows=OAuthFlows(
                        authorizationCode=OAuthFlowAuthorizationCode(
                            authorizationUrl=(
                                "https://accounts.google.com/o/oauth2/auth"
                            ),
                            tokenUrl="https://oauth2.googleapis.com/token",
                            scopes={
                                "https://www.googleapis.com/auth/calendar.readonly": "",
                            },
                        )
                    )
                ),
                raw_auth_credential=AuthCredential(
                    auth_type=AuthCredentialTypes.OAUTH2,
                    oauth2=OAuth2Auth(
                        client_id=oauth_client_id,
                        client_secret=oauth_client_secret,
                    ),
                ),
            ),
        ),
        calendar_toolset],
    before_agent_callback=update_time, 
)
```

Видео: <https://www.youtube.com/watch?v=NzQM4GihwQU>

---

### day27 — Scion: an open testbed for agent orchestration  
🟡 · Multiagent, Harness Engineering, CLI

Explore multi-agent patterns with an agnostic supra-harness system that isolates agents in git worktrees and containers, allowing easy orchestration and communication

Ссылки:
- [Open Source Repo](https://github.com/GoogleCloudPlatform/scion) — Scion on github
- [Documentation](https://googlecloudplatform.github.io/scion/overview/) — Scion Documentation

Код (`terminal.sh`):

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

Видео: <https://www.youtube.com/watch?v=T93MW7wETOc>

---

### day28 — A2A Protocol: Decoupling Reasoning from Execution  
🟡 · A2A, LangGraph, ADK, Protocol

Decouple your reasoning engine from execution using the universal A2A 1.0 protocol to bridge a Python LangGraph orchestrator and a Go ADK service.

Ссылки:
- [LangChain Blog: Multi-Agent Workflows](https://blog.langchain.dev/multi-agent-workflows/) — Conceptual architectures for delegating tasks between disconnected agent frameworks.
- [YouTube: Stop using MCP for everything!](https://www.youtube.com/watch) — RAG vs. A2A vs. Sub-agents architecture explained.
- [Google Cloud: Building AI Workflows](https://cloud.google.com/blog/products/ai-machine-learning) — High-level patterns for decoupling robust AI reasoning engines from API execution.
- [Agent Starter Pack Walkthrough](https://github.com/GoogleCloudPlatform/agent-starter-pack) — Explore the Agent-to-Agent interaction patterns built by Google Cloud engineers.

Код (`adk_execution_service.go`):

```go
// adk_execution_service.go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/pterm/pterm"
	_ "github.com/joho/godotenv/autoload"
)

// A2A 1.0 Universal Envelope Schema
type A2APayload struct {
	A2AVersion string            `json:"a2a_version"`
	SenderID   string            `json:"sender_id"`
	Task       string            `json:"task"`
	Context    map[string]string `json:"context"`
}

func handleA2A(w http.ResponseWriter, r *http.Request) {
	var payload A2APayload
	if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	pterm.Info.Printfln("[ADK Service] Received A2A Payload from %s: %s", pterm.LightCyan(payload.SenderID), pterm.LightYellow(payload.Task))

	apikey := os.Getenv("GEMINI_API_KEY")
	url := "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key=" + apikey

	reqBody := map[string]interface{}{
		"system_instruction": map[string]interface{}{
			"parts": []map[string]interface{}{{"text": "You are a platform execution agent. You receive A2A JSON payloads. Parse the 'task' and return a concise, step-by-step execution plan."}},
		},
		"contents": []map[string]interface{}{
			{"parts": []map[string]interface{}{{"text": fmt.Sprintf("Execute this A2A payload task: %s", payload.Task)}}},
		},
	}
	jsonReq, _ := json.Marshal(reqBody)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonReq))
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	defer resp.Body.Close()

	bodyBytes, _ := io.ReadAll(resp.Body)
	var genaiResp map[string]interface{}
	json.Unmarshal(bodyBytes, &genaiResp)

	var resultString string
	if cands, ok := genaiResp["candidates"].([]interface{}); ok && len(cands) > 0 {
		if content, ok := cands[0].(map[string]interface{})["content"].(map[string]interface{}); ok {
			if parts, ok := content["parts"].([]interface{}); ok && len(parts) > 0 {
				if text, ok := parts[0].(map[string]interface{})["text"].(string); ok {
					resultString = text
				}
			}
		}
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"final_result": resultString,
	})
	
	pterm.Success.Println("Dispatched response back to LangGraph!")
}

func main() {
	pterm.DefaultHeader.WithFullWidth().Println("Go ADK Execution Service")
	pterm.Info.Println("Listening on http://localhost:8080/execute")

	apikey := os.Getenv("GEMINI_API_KEY")
	maskedKey := apikey
	if len(apikey) > 8 {
		maskedKey = apikey[:8] + "..."
	} else if len(apikey) == 0 {
		maskedKey = "NOT CONFIGURED"
	}
	pterm.Info.Printfln("[Config] Loaded GEMINI_API_KEY: %s", pterm.LightYellow(maskedKey))

	http.HandleFunc("/execute", handleA2A)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Код (`terminal`):

```bash
# 1. Create a root .env file with your API Key
echo 'GEMINI_API_KEY="your-api-key-here"' > .env

# Spin up the Go Execution Platform
go mod init example.com/adk 2>/dev/null || true
go get github.com/pterm/pterm github.com/joho/godotenv/autoload
go run adk_execution_service.go
```

Код (`a2a_langgraph_orchestrator.py`):

```python
# Based on the ASP langgraph_base template
# a2a_langgraph_orchestrator.py
import os
import json
import urllib.request
from typing import TypedDict
from langgraph.graph import StateGraph, END
from rich.console import Console
from rich.panel import Panel
from rich.json import JSON
from rich.live import Live
from rich.spinner import Spinner
from rich.markdown import Markdown

from dotenv import load_dotenv
load_dotenv()

console = Console()

# ====================================================================
# 1. PYTHON LANGGRAPH AGENT (The Reasoning Framework)
# ====================================================================
class AgentState(TypedDict):
    objective: str
    a2a_payload: str
    final_result: str

def reasoning_node(state: AgentState):
    console.print(Panel("[bold green]LangGraph[/bold green]: Reasoning complete. Formatting A2A 1.0 envelope.", title="[Reasoning Engine]"))
    
    # Standard A2A 1.0 Payload formulation
    envelope = {
        "a2a_version": "1.0",
        "sender_id": "langgraph-orchestrator",
        "task": state["objective"],
        "context": {"urgency": "high", "auth_token": "bearer_abc123"}
    }
    return {"a2a_payload": json.dumps(envelope)}

def a2a_dispatch_node(state: AgentState):
    """Dispatches the A2A payload to the Go ADK framework across the network"""
    
    with Live(Spinner("dots", text="[bold yellow]Dispatching A2A payload via HTTP POST to Go Service...[/bold yellow]"), refresh_per_second=10) as live:
        req = urllib.request.Request(
            "http://localhost:8080/execute", 
            data=state["a2a_payload"].encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                live.update(Panel("[bold green]Dispatch Success![/bold green]", title="[Network]"))
                return {"final_result": result["final_result"]}
        except Exception as e:
            live.update(Panel(f"[bold red]Dispatch failed[/bold red]: {e}", title="[Network]"))
            return {"final_result": f"Dispatch failed: {e}"}

# 2. Build and Run the Graph
workflow = StateGraph(AgentState)
workflow.add_node("reason", reasoning_node)
workflow.add_node("delegate_via_a2a", a2a_dispatch_node)

workflow.set_entry_point("reason")
workflow.add_edge("reason", "delegate_via_a2a")
workflow.add_edge("delegate_via_a2a", END)

langgraph_app = workflow.compile()

if __name__ == "__main__":
    console.print(Panel("[bold blue]Starting LangGraph A2A Orchestrator[/bold blue]", title="[System]"))
    
    apikey = os.environ.get("GEMINI_API_KEY", "")
    masked_key = apikey[:8] + "..." if len(apikey) > 8 else apikey
    console.print(Panel(f"[bold yellow]Loaded GEMINI_API_KEY[/bold yellow]: {masked_key}", title="[Config]"))
    
    final_state = langgraph_app.invoke({
        "objective": "Execute production database migration to Cloud SQL", 
        "a2a_payload": "",
        "final_result": ""
    })
    
    console.print(Panel(JSON(final_state["a2a_payload"]), title="[A2A 1.0 Envelope - Dispatched]"))
    
    console.print(Panel(Markdown(final_state['final_result']), title="[ADK Execution Result]"))
```

Код (`terminal`):

```bash
# Trigger the LangGraph Orchestrator
pip install langgraph rich pydantic python-dotenv
python a2a_langgraph_orchestrator.py
```

Видео: <https://www.youtube.com/watch?v=NsJ7UjRCnZU>

---

### day29 — ApiRegistry: Dynamically Fetching BigQuery Tools  
🟡 · ApiRegistry, BigQuery, Authentication

Learn how to use the ApiRegistry object to dynamically fetch an admin-approved, fully configured BigQuery tool directly from the Cloud API Registry at runtime.

Ссылки:
- [API Registry Documentation](https://docs.cloud.google.com/api-registry/docs/overview) — Official documentation for the Cloud API Registry.
- [Enhanced Tool Governance Blog Post](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder) — Google Cloud blog post covering Vertex AI Agent Builder tool governance.

Код (`requirements.txt`):

```text
google-cloud-bigquery
google-auth
```

Код (`setup.sh`):

```bash
#!/bin/bash
#1. Install dependencies
pip install -r requirements.txt

#2. Setup the "Registry" Data
echo "Setting up Registry Data"

#replace project-id with your project id
bq mk --dataset project-id:registry_demo
bq query --use_legacy_sql=false \
'CREATE OR REPLACE TABLE `project-id.registry_demo.test_table` AS SELECT "Registry_Active" as status'

#3. Authorize the environment
echo "Please authorize the environment registry:"
gcloud auth application-default login
```

Код (`main.py`):

```python
import google.auth
from google.cloud import bigquery

class ApiRegistry:
    @staticmethod
    def get_tool(tool_id):
        #Dynamically fetch config from Cloud Registry
        creds, project = google.auth.default()
        project = project or "project-id" #replace project-id with your project id
        return bigquery.Client(credentials=creds, project=project)

def run_task():
    #1. Fetch tool from Registry
    bq = ApiRegistry.get_tool("bigquery-admin-v2")
    
    # 2. Execute admin-approved query
    #replace project-id with your project id
    sql = "SELECT status FROM `project-id.registry_demo.test_table`"
    for row in bq.query(sql):
        print(f"Verified via Registry: {row.status}")

if __name__ == "__main__":
    run_task()
```

Видео: <https://www.youtube.com/watch?v=981wf6l3fCA>

---

### day30 — Observability: Debug with Hierarchical Tracing  
⚪ · OpenTelemetry, Arize Phoenix, Tracing, ADK

Eliminate silent failures in AI agents by implementing Hierarchical Trace Observability with OpenTelemetry and Arize Phoenix.

Ссылки:
- [GitHub Project Repository](https://github.com/siri2421/advent-of-agents-observabiity.git) — Working implementation of OTel and Phoenix observability.
- [Arize Phoenix Documentation](https://arize.com/docs/phoenix) — Complete guide to the Phoenix observability platform.
- [Phoenix Observability for ADK](https://google.github.io/adk-docs/integrations/phoenix/#support-and-resources) — Specific integration guide for using Phoenix with ADK.
- [ADK Documentation](https://google.github.io/adk-docs/) — Agent Development Kit documentation.

Код (`debug_agent.py`):

```python
from phoenix.otel import register
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor
from google import genai

# 1. Register project for trace collection
register(project_name="advent-of-agents-debug", auto_instrument=True)

# 2. Instrument Google GenAI to capture model spans automatically
GoogleGenAIInstrumentor().instrument()

# 3. Execute model call with gemini-3.1-flash to generate traces
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-flash", 
    contents="Explain observability in AI agents."
)
print(response.text)
```

Видео: <https://www.youtube.com/watch?v=AVmNpeubF4w>

---

### day31 — A2UI & A2A: Building the Dog Weather App  
⚪ · A2UI, A2A, Gemini Enterprise, ADK

Transform static agent responses into rich interactive micro-apps natively rendered in Gemini Enterprise using A2UI.

Ссылки:
- [GitHub Repository](https://github.com/goabego/adventofagents-day31) — Full source code for both the text-only baseline and the interactive Dog Weather App.
- [ADK Documentation](https://github.com/google-gemini/adk) — Core SDK used for tool registration and A2A lifecycle management.
- [A2UI Introduction](https://a2ui.org/introduction/what-is-a2ui/) — Overview of the declarative UI protocol for generative agents.
- [A2A Agent Registration](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent) — Official guide on how to register and manage your custom ADK agents within Gemini Enterprise.

Код (`dog_weather_agent.py`):

```python
from google.adk import agents
from prompt_builder import get_ui_instruction

class DogWeatherAgent(agents.LlmAgent):
    def __init__(self, **kwargs):
        # 1. Define persona with A2UI rules & schemas
        base_prompt = "You are a pun-loving weather assistant. Fetch!"
        full_instruction = get_ui_instruction(base_prompt)
        
        super().__init__(
            name="weather_agent_v2",
            model="gemini-3.1-flash-lite-preview",
            instruction=full_instruction,
            tools=[get_weather, get_random_location]
        )

# 2. Return data-bound A2UI payload via tool chaining
def get_weather(location: str):
    return {
        "location": location,
        "temp": "72°F",
        "dogImageUrl": "https://dog.ceo/api/image"
    }
```

Код (`a2a_server.py`):

```python
from a2a.server.apps.jsonrpc.starlette_app import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler

# 1. Initialize ADK Agent & A2A Executor
agent = DogWeatherAgent()
agent_card = agent.create_agent_card(AGENT_URL)

# 2. Build A2A Server with ADK-to-A2A Bridge
app = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=DefaultRequestHandler(
        agent_executor=AdkAgentToA2AExecutor()
    )
).build()
```

Видео нет

---

## s3-2026-10

### day01 — Foundation 101: Five Phases of Agent Development Lifecycle  
✅ · 7:23 · Launch, ADLC, Governance

Map the five phases every agent moves through, from Scope to Optimize, and walk one agent around the loop in about five minutes.

Ссылки:
- [Automate your agent development lifecycle](https://cloud.google.com/blog/topics/developers-practitioners/automate-agent-development-lifecycles-with-gemini-enterprise) — Set up, build, deploy, govern, evaluate, and publish an agent with Agents CLI skills.
- [Agents CLI in Agent Platform](https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/) — Why Agents CLI is the programmatic backbone for the ADLC on Google Cloud.
- [Gemini Enterprise Agent Platform docs](https://g.dev/cloud/adventofagents-season3-gemini-enterprise-govern) — Build, scale, govern, and optimize: the platform behind each ADLC phase.
- [Introduction to Agents whitepaper](https://www.kaggle.com/whitepaper-introduction-to-agents) — Google's foundational whitepaper on how agents work.

Код (`adlc-in-300-seconds.sh`):

```bash
# Day 1: walk one agent around the ADLC loop in about five minutes.
# Prereqs: Python 3.11+, uv, Node.js, gcloud, and a Google Cloud project with billing.
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
export GOOGLE_CLOUD_LOCATION=us-central1

# 1. SCOPE: decide what the agent may and may not do before any code exists.
cat > DESIGN_SPEC.md <<'EOF'
# adlc-day1
Owner: you@example.com
May: answer weather and time questions with get_weather and get_current_time
May not: call any other tool, store user data, or act on external systems
Success: picks the right tool for each question (see tests/eval)
EOF

# 2. BUILD: install Agents CLI, scaffold a prototype agent, move the spec in, run it.
uvx google-agents-cli setup
agents-cli scaffold create adlc-day1 --prototype --yes
mv DESIGN_SPEC.md adlc-day1/ && cd adlc-day1
agents-cli install
agents-cli run "What's the weather in San Francisco?"
# Find the [tool_call: get_weather(...)] line. That trace is your first audit trail.

# 3. OPTIMIZE: score the agent's behavior against the scaffolded eval set (LLM judge, billable).
agents-cli eval run

# 4. SCALE + GOVERN: preview of Day 5 (deploy takes about 5-10 minutes).
# agents-cli scaffold enhance . --deployment-target agent_runtime --prototype --yes
# agents-cli deploy --agent-identity --project $GOOGLE_CLOUD_PROJECT --region us-central1
```

Видео: <https://www.youtube.com/watch?v=ngNxiZhxJjI>

---

### day02 — Agent Security: Implementing SAIF Guardrails  
✅ · 13:11 · Agent Security, SAIF, Guardrails

Secure agent workflows against rogue actions or data disclosure using SAIF threat modeling.

Видео: <https://www.youtube.com/watch?v=TA7lhezND7M>

---

### day03 — Architecting Secure Multi-Agent Systems  
✅ · 13:02 · Architecture, Enterprise Security, Gemini Enterprise, Multi-Agent

Move from single-agent prototypes to hardened, production multi-agent architectures on Google Cloud using Gemini Enterprise

Видео: <https://www.youtube.com/watch?v=c89LrULUrmI>

---

### day04 — Governance Maturity Model: Progressive Trust for Agents  
✅ · 7:16 · Governance, Maturity Model, Roadmap

Score your agent estate on five governance layers, from Foundation to Continuous Alignment, and turn the result into a staged 90-day roadmap with a 15-question Python self-assessment.

Видео: <https://www.youtube.com/watch?v=nNjqaKVR3tc>

---
