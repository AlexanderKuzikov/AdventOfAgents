---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 9
title: "⏪ Undo buttons for your Agents"
summary: "Building an \"Edit Message\" or \"Regenerate\" feature shouldn't require complex database migrations. In the ADK, time travel is built-in."
tags: ["Rewind", "Resume", "ADK", "Time Travel", "Undo"]
canonical_url: "https://adventofagents.com/2025/12/09"
markdown_url: "https://adventofagents.com/2025/12/09.md"
video_url: "https://www.youtube.com/embed/9FQh-Pw2sfE"
---

# ⏪ Day 9: ⏪ Undo buttons for your Agents

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/09?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09) · [Raw Markdown](https://adventofagents.com/2025/12/09.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09)

**Summary:** Building an "Edit Message" or "Regenerate" feature shouldn't require complex database migrations. In the ADK, time travel is built-in.

**Day 9 of Google's Advent of Agents**

Your agent does step 1, 2, 3, 4... 
but what if you realize step 2 was a mistake and you want to rewind time and start from there?

Now the ADK has time travel and checkpointing!

Instead of destructively deleting history, the runner calculates the difference between "now" and "then" (State & Artifact Deltas) and appends a rewind event to the log. 
This allows you to revert the application state to a specific timestamp or invocation ID while keeping a complete audit trail of what happened.

**The simple fix**

You don't just "go back"—you restore the world to exactly how it was, and you keep the rewound path in case you need it.

Try it out yourself in this sample [adk-python](https://github.com/google/adk-python/blob/main/contributing/samples/rewind_session/main.py?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09).

As a developer, you can use rewind to undo a step in the conversation, or to revert to a previous state of the application.
The agent can also take this action as a tool, if you have configured it to know how to do so.

## Code & Commands

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

## Resources & Links

- **[ADK Docs: Runtime Resume](https://google.github.io/adk-docs/runtime/resume/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09)** — Learn how to resume an ADK session.
- **[ADK Docs: Sessions Rewind](https://google.github.io/adk-docs/sessions/rewind/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09)** — Understand the ADK rewind functionality for time travel.
- **[ADK Python Sample: Rewind Session](https://github.com/google/adk-python/blob/main/contributing/samples/rewind_session/main.py?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day09)** — View a practical example of session rewinding in ADK Python.
