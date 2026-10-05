---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 17
title: "Gemini 3 Flash is here!"
summary: "Google's fastest model just got smarter with configurable thinking levels and granular controls."
tags: ["gemini", "flash", "thinking", "adk"]
canonical_url: "https://adventofagents.com/2025/12/17"
markdown_url: "https://adventofagents.com/2025/12/17.md"
video_url: "https://www.youtube.com/embed/1txijlIHS_I"
---

# ⚡ Day 17: Gemini 3 Flash is here!

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/17?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17) · [Raw Markdown](https://adventofagents.com/2025/12/17.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17)

**Summary:** Google's fastest model just got smarter with configurable thinking levels and granular controls.

**Day 17 of Google's Advent of Agents**

**Google's fastest model just got a lot smarter.**
Gemini 3 Flash combines flagship-level reasoning with the speed and cost-efficiency you expect from the Flash series.

Flash scored **33.7%** without tool use on Humanity’s Last Exam, in comparison to Gemini 3 Pro at 37.5%, Gemini 2.5 Flash at 11%, and the newly released GPT-5.2 scored 34.5%.

On the multimodality and reasoning benchmark MMMU-Pro, the new model outscored all competitors with an **81.2%** score.

And this is for only $0.50/1M input tokens and $3.00/1M output tokens, redefining the pareto frontier between quality, price, and performance.

It introduces powerful new controls for developers:

- **🧠 Configurable Thinking Levels:** explicit control over the model's reasoning budget. (`high`, `low`, `minimal`)
- **👁️ Granular Media Resolution:** Optimize your token usage by adjusting vision processing resolution (`low`, `medium`, `high`) per image or video frame.
- **🔐 Robust Thought Signatures:** Encrypted tokens that preserve the model's reasoning state during multi-turn function calling, ensuring context isn't lost when the model pauses to use a tool.

**ADK makes these features seamless.** The ADK automatically handles the complex circulation of **Thought Signatures** for you, so you can focus on building agents, not managing encrypted tokens.

## Code & Commands

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

```shell
pip install google-adk # and follow the instruction in the video
```

## Resources & Links

- **[Gemini 3 Flash Announcement](https://blog.google/products/gemini/gemini-3-flash/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17)** — Official announcement blog post
- **[ADK Get Started Documentation](https://google.github.io/adk-docs/get-started/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17)** — Get started with the Agent Development Kit
- **[ADK Models Documentation](https://google.github.io/adk-docs/agents/models/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17)** — Learn about model configuration in ADK
- **[Developer's Guide to Multi-Agent Systems](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day17)** — Building Multi-Agent Systems with Gemini 3 Flash and ADK
- **[Google launches Gemini 3 Flash, makes it the default model in the Gemini app](https://techcrunch.com/2025/12/17/google-launches-gemini-3-flash-makes-it-the-default-model-in-the-gemini-app/)** — Techcrunch article reporting on the launch of Gemini 3 flash
