---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 7
title: "ADK Agent Skill Design Patterns"
summary: "Five design patterns for structuring SKILL.md content in ADK — Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline."
tags: ["Skills", "Design Patterns", "SkillToolset", "ADK"]
canonical_url: "https://adventofagents.com/2026/03/07"
markdown_url: "https://adventofagents.com/2026/03/07.md"
---

# 🧩 Day 7: ADK Agent Skill Design Patterns

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/07?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day07) · [Raw Markdown](https://adventofagents.com/2026/03/07.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day07)

**Summary:** Five design patterns for structuring SKILL.md content in ADK — Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline.

**Day 7 of Google's Advent of Agents — Season 2**

Yesterday we introduced ADK Skills and progressive disclosure. Today we tackle the next question: you know how to create a skill, but how should you structure the content inside? The [Agent Skills specification](https://agentskills.io/specification) defines the format (SKILL.md + references/ + assets/), but five distinct design patterns define what goes inside.

**The Five Patterns**

Each pattern uses the same SKILL.md format but structures the content differently:

- **Tool Wrapper**: Wraps a library's conventions into on-demand expertise. The agent becomes a domain expert when the skill is loaded. Uses `references/` for convention docs — no templates, no scripts, pure knowledge.

- **Generator**: Produces structured output from templates. Uses `assets/` for the template (WHAT to produce) and `references/` for style rules (HOW to produce it). The agent fills the template based on user input.

- **Reviewer**: Evaluates code or content against a checklist. Separates WHAT to check (`references/checklist.md`) from HOW to check (the review protocol in instructions). Swap the checklist for a different review type.

- **Inversion**: The skill interviews the user before acting. Phased questions gather requirements across multiple turns, then the agent synthesizes output using an `assets/` template. Prevents acting on assumptions.

- **Pipeline**: Enforces a multi-step workflow with gate conditions. "Do NOT proceed until the user confirms." The most complex pattern — combines all resource types and adds control flow.

**Choosing the Right Pattern**

- **Tool Wrapper** — Library expertise → uses **references/**
- **Generator** — Structured output → uses **assets/ + references/**
- **Reviewer** — Quality evaluation → uses **references/**
- **Inversion** — Requirements gathering → uses **assets/**
- **Pipeline** — Multi-step workflow → uses **all directories**

Patterns compose — a Pipeline can include a Reviewer step, and a Generator can use Inversion to gather inputs first. The [companion blog post](https://lavinigam.com/posts/adk-skill-design-patterns/) walks through each pattern with working ADK code and SKILL.md examples.

**Resources:**

- [5 Agent Skill Design Patterns (Blog)](https://lavinigam.com/posts/adk-skill-design-patterns/)
- [ADK Skills Part 1: Progressive Disclosure](https://lavinigam.com/posts/adk-agent-skills-part1/)
- [ADK Skills Part 2: File-Based Skills](https://lavinigam.com/posts/adk-agent-skills-part2/)
- [ADK Skills Part 3: Meta Skills](https://lavinigam.com/posts/adk-agent-skills-part3/)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-skill-design-patterns?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day07)

## Code & Commands

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

## Resources & Links

- **[5 Agent Skill Design Patterns (Blog)](https://lavinigam.com/posts/adk-skill-design-patterns/)** — Full walkthrough of the 5 patterns with working ADK code.
- **[ADK Skills Documentation](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day07)** — Official guide for defining and using skills in ADK.
- **[ADK Skills Part 1: Progressive Disclosure](https://lavinigam.com/posts/adk-agent-skills-part1/)** — Foundations: what skills are, L1/L2/L3 levels, inline skills.
- **[ADK Skills Part 2: File-Based Skills](https://lavinigam.com/posts/adk-agent-skills-part2/)** — SKILL.md format, load_skill_from_dir, SkillToolset internals.
- **[ADK Skills Part 3: Meta Skills](https://lavinigam.com/posts/adk-agent-skills-part3/)** — Pattern 4: skills that write skills.
- **[Agent Skills Specification](https://agentskills.io/specification)** — The open standard defining SKILL.md format, adopted by 30+ agents.
- **[Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-skill-design-patterns?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day07)** — Clone and run all five design patterns with ADK Web.
