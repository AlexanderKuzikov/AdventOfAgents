---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 8
title: "Effective Context Management with ADK Layers"
summary: "ADK Context design thesis: context as a compiled view"
tags: ["Context Management", "Layers", "Caching"]
canonical_url: "https://adventofagents.com/2025/12/08"
markdown_url: "https://adventofagents.com/2025/12/08.md"
video_url: "https://www.youtube.com/embed/DdTtiWoMa3E"
---

# 🧱 Day 8: Effective Context Management with ADK Layers

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/08?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day08) · [Raw Markdown](https://adventofagents.com/2025/12/08.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day08)

**Summary:** ADK Context design thesis: context as a compiled view

**Day 8 of Google's Advent of Agents**

**Stop stuffing spaghetti context into your agent's LLM.**

The "append-everything" strategy is a one-way ticket to latency spirals and "lost in the middle" hallucinations.
Google ADK shifts the paradigm by treating context as a **compiled view** (not a giant string).
Instead of shoveling raw history into the window, ADK uses a pipeline of processors to dynamically filter, compact, and format a clean "working context" derived from a structured, durable session state.  
As a developer, you can control that pipeline to customize the behavior to your needs.

**Real engineering requires granular control, not just a bigger context window.**

ADK’s tiered architecture separates storage from presentation, allowing you to externalize massive files as Artifacts (using a handle pattern) and retrieve long-term data via searchable Memory only when strictly necessary.
Whether you are managing strict multi-agent handoffs or debugging tool interactions, specialized objects like ToolContext ensure your agents access exactly the scope they need—and nothing they don't.

**Build for production scale with patterns that optimize for model capabilities.**

ADK operationalizes Context Caching by enforcing a clear separation between "Static Instructions" (invariant policies and schemas) and "Turn Instructions" (dynamic, controller-owned steering).
This design keeps your heavy system headers stable to slash costs and latency, while ensuring that per-turn directives remain legally distinct from user input for better security and validation.

As described in [Day 3 of our Kaggle 5 Day intensive course](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory), Agents are largely "context management".

This is how you do it.

## Code & Commands

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

## Resources & Links

- **[Architecting efficient context-aware multi-agent framework for production](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day08)** — Design principles from an ADK Tech Lead: Context is a compiled view over a richer stateful system.
- **[ADK Context Documentation](https://google.github.io/adk-docs/context/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day08)** — Learn about working with context in the ADK in the official docs.
- **[The ADK Prompting Pattern: Static vs. Turn Instructions](https://medium.com/google-cloud/the-adk-prompting-pattern-static-vs-turn-instructions-7a1e5b25eeef)** — A deep dive into static vs. turn instructions (code examples from this article).
- **[Context Engineering: Sessions & Memory | Kaggle](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory)** — Day 3 of the Kaggle course on AI Agents is all about context management.
- **[A longer NotebookLM summary of ADK context management](https://youtu.be/eQDx90dVc38)** — 8 minute video summary of context management and how ADK solves it.
- **[ADK Context Engineering Infographic](https://adventofagents.com/aoa-day8-art-of-context-engineering-with-adk.png?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day08)** — NotebookLM generated infographic summarizing ADK context engineering.
