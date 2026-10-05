---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 14
title: "Multi-Agent Patterns: Human in the Loop"
summary: "Inject an approval breakpoint to pause agent execution and wait for manual user confirmation before executing sensitive financial APIs."
tags: ["Multi-Agent", "ADK", "Human-in-the-Loop", "Security"]
canonical_url: "https://adventofagents.com/2026/03/14"
markdown_url: "https://adventofagents.com/2026/03/14.md"
video_url: "https://www.youtube.com/embed/IqtGuk-aM60"
---

# 🛡️ Day 14: Multi-Agent Patterns: Human in the Loop

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/14?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14) · [Raw Markdown](https://adventofagents.com/2026/03/14.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14)

**Summary:** Inject an approval breakpoint to pause agent execution and wait for manual user confirmation before executing sensitive financial APIs.

**Day 14 of Google's Advent of Agents — Season 2**

Autonomous agents are incredibly capable, but running them in production requires safeguards. When an agent has access to sensitive environments—like financial APIs or production databases—you cannot rely on prompt engineering alone to prevent destructive actions.

**The Solution:**
The Human-in-the-Loop (HITL) pattern. We introduce a strict approval breakpoint: the agent must pause its execution and wait for manual human confirmation before firing a sensitive tool.

**How It Works:**
While there are many ways to solve this (like building custom async UI hooks or Slack workflows), ADK provides robust built-in capabilities for managing long-running tasks and interceptions natively.

- **Long Running Tools**: Wrap your confirmation function in a `LongRunningFunctionTool`. This signals to ADK that the function requires external intervention and should pause execution automatically.
- **Event Interception**: During the `run_async` loop, the client watches the stream. When the agent attempts to call the tool, it surfaces the pending call inside `event.long_running_tool_ids`.
- **State Resumption**: The runner safely suspends the loop. Once the human provides a decision (like approving a CLI prompt), you inject the updated `function_response` back into the runner. The agent picks up exactly where it left off, armed with the human's ruling.

**Resources:**

- [ADK Multi-Agent Design Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14)
- [Securing Agent Tools with ADK](https://google.github.io/adk-docs/tools/configuration?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14)
- [Human-in-the-Loop Pattern](https://google.github.io/adk-docs/agents/multi-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14#human-in-the-loop-pattern)

## Code & Commands

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

## Resources & Links

- **[ADK Multi-Agent Design Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14)** — Review standard architectural patterns for agent deployment.
- **[Tool Configuration Docs](https://google.github.io/adk-docs/tools/configuration?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14)** — Learn how to secure tools with approval breakpoints and access scopes.
- **[Human-in-the-Loop Pattern](https://google.github.io/adk-docs/agents/multi-agents/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day14#human-in-the-loop-pattern)** — Explore the official documentation for the Human-in-the-loop architectural pattern.
