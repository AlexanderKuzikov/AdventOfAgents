---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 10
title: "Big Context ≠ Better Memory"
summary: "Long-running agent sessions face two enemies: latency and \"lost in the middle\" syndrome. The ADK solves this with Context Caching and Context Compaction."
tags: ["Memory", "ADK", "Context Caching", "Context Compaction", "Memory"]
canonical_url: "https://adventofagents.com/2025/12/10"
markdown_url: "https://adventofagents.com/2025/12/10.md"
video_url: "https://www.youtube.com/embed/L3eKHw9df-g"
---

# 🧠 Day 10: Big Context ≠ Better Memory

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/10?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10) · [Raw Markdown](https://adventofagents.com/2025/12/10.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10)

**Summary:** Long-running agent sessions face two enemies: latency and "lost in the middle" syndrome. The ADK solves this with Context Caching and Context Compaction.

**Day 10 of Google's Advent of Agents**

Long-running agent sessions face two enemies: latency and "lost in the middle" syndrome. As conversation history grows, re-sending massive system instructions becomes expensive, and the model struggles to prioritize earlier rules against recent noise.

The ADK solves this with a two-prong approach. First, [Context Caching](https://google.github.io/adk-docs/context/caching/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10) allows you to cache the immutable parts of your prompt (system instructions, few-shot examples) so you don't pay the compute cost on every turn. Second, [Context Compaction](https://google.github.io/adk-docs/context/compaction/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10) prevents history bloat.

Instead of appending raw messages indefinitely, the ADK uses a sliding window to summarize older events into a concise "memory" block while keeping recent interactions verbatim for precision.

## Code & Commands

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

## Resources & Links

- **[Context Compaction](https://google.github.io/adk-docs/context/compaction/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10)** — Learn how to compress history to prevent context rot.
- **[Context Caching](https://google.github.io/adk-docs/context/caching/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10)** — Learn how to cache heavy instructions for better performance.
- **[Context Compaction Explained](https://x.com/Saboo_Shubham_/status/1978286461607911617)** — A visual explanation of context compaction.
- **[ADK Context Caching & Compaction Infographic](https://adventofagents.com/aoa-day10-context-caching-compaction.png?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day10)** — NotebookLM generated infographic summarizing ADK context caching & compaction.
- **[Additional Reading: The Context Trap Every Agent Builder Falls Into](https://www.theunwindai.com/p/the-context-trap-every-agent-builder-falls-into)** — An article discussing common context management pitfalls every agent builder faces.
