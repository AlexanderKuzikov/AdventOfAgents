---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 30
title: "Observability: Debug with Hierarchical Tracing"
summary: "Eliminate silent failures in AI agents by implementing Hierarchical Trace Observability with OpenTelemetry and Arize Phoenix."
tags: ["OpenTelemetry", "Arize Phoenix", "Tracing", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/30"
markdown_url: "https://adventofagents.com/2026/03/30.md"
video_url: "https://www.youtube.com/embed/AVmNpeubF4w"
---

# 🔍 Day 30: Observability: Debug with Hierarchical Tracing

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/30?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30) · [Raw Markdown](https://adventofagents.com/2026/03/30.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30)

**Summary:** Eliminate silent failures in AI agents by implementing Hierarchical Trace Observability with OpenTelemetry and Arize Phoenix.

**Day 30 of Google's Advent of Agents — Season 2**

Traditional logging fails to capture the non-linear reasoning of AI agents, leaving developers "debugging in the dark" when silent failures occur. Without granular visibility, it is impossible to isolate whether a failure stems from model hallucinations, infrastructure outages, or policy violations.

**How It Works**

**Hierarchical Trace Observability** provides process transparency by treating agent reasoning as discrete, measurable units using **OpenTelemetry (OTel)** and **Arize Phoenix**:

- **Auto-Instrumentation**: Use OpenInference instrumentors to automatically capture spans from Google GenAI and other LLM providers.
- **Trace Visualization**: View the hierarchical structure of agent calls in Arize Phoenix to isolate problematic spans like hallucinations.
- **Span Replay**: Troubleshoot by replaying specific "thoughts" in a Prompt Playground sandbox with original variables to experiment with fixes.

**Resources:**

- [GitHub Project Repository](https://github.com/siri2421/advent-of-agents-observabiity.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30)
- [Arize Phoenix Documentation](https://arize.com/docs/phoenix)
- [Phoenix Observability for ADK](https://google.github.io/adk-docs/integrations/phoenix/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30#support-and-resources)
- [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30)

## Code & Commands

### Observability & Model Call

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

## Resources & Links

- **[GitHub Project Repository](https://github.com/siri2421/advent-of-agents-observabiity.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30)** — Working implementation of OTel and Phoenix observability.
- **[Arize Phoenix Documentation](https://arize.com/docs/phoenix)** — Complete guide to the Phoenix observability platform.
- **[Phoenix Observability for ADK](https://google.github.io/adk-docs/integrations/phoenix/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30#support-and-resources)** — Specific integration guide for using Phoenix with ADK.
- **[ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day30)** — Agent Development Kit documentation.
