---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 6
title: "ADK Skills"
summary: "Eliminate wasted tokens with progressive disclosure. Use ADK Skills to load complex instructions only when needed."
tags: ["ADK", "Skills", "Progressive Disclosure", "Optimization"]
canonical_url: "https://adventofagents.com/2026/03/06"
markdown_url: "https://adventofagents.com/2026/03/06.md"
---

# 🥋 Day 6: ADK Skills

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/06?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06) · [Raw Markdown](https://adventofagents.com/2026/03/06.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06)

**Summary:** Eliminate wasted tokens with progressive disclosure. Use ADK Skills to load complex instructions only when needed.

**Day 6 of Google's Advent of Agents — Season 2** 🌸

Most agents load every instruction into the **system prompt** on every LLM call — compliance rules, style guides, API references — whether the user's question needs them or not. At ten capabilities, that's thousands of **wasted tokens** per call. **ADK Skills** solve this with **progressive disclosure**: the agent sees only a lightweight listing of skill names at startup, then loads full instructions on demand.

**Progressive Disclosure: L1 / L2 / L3**

![Progressive Disclosure Diagram](/s2-day06-progressive-disclosure.png)

**How It Works**

**ADK SkillToolset** auto-registers three tools that map to three disclosure levels:

- **L1 — Metadata (list_skills)**: Returns skill names and descriptions (~100 tokens each). Always present. This is the "menu" the agent scans to decide what's relevant.

- **L2 — Instructions (load_skill)**: Fetches the full skill body when the agent decides it's needed. Called explicitly per skill.

- **L3 — Resources (load_skill_resource)**: Loads reference files (style guides, checklists, specs) only when skill instructions reference them.

Skills can be defined **inline** in Python, loaded from **local directories** with SKILL.md files, pulled from **community repos**, or even generated on demand by a **meta skill**. The [companion blog series](https://lavinigam.com/posts/adk-agent-skills-part1/#what-are-skills-and-why-they-matter) walks through all four patterns.

**Resources:**

- [ADK Skills Documentation](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06)
- [ADK Skills: Part 1 - What Are Skills?](https://lavinigam.com/posts/adk-agent-skills-part1/#what-are-skills-and-why-they-matter)
- [ADK Skills: Part 2 - Wiring Skills](https://lavinigam.com/posts/adk-agent-skills-part2/#wiring-skills-into-the-agent)
- [ADK Skills: Part 3 - Skills That Write Skills](https://lavinigam.com/posts/adk-agent-skills-part3/#pattern-4-skills-that-write-skills)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-agent-skills-tutorial?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06)

## Code & Commands

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

## Resources & Links

- **[ADK Skills Documentation](https://google.github.io/adk-docs/skills/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06)** — Official guide for defining and using skills in ADK.
- **[ADK Skills: Part 1 - What Are Skills?](https://lavinigam.com/posts/adk-agent-skills-part1/#what-are-skills-and-why-they-matter)** — Learn why decoupling procedural knowledge matters.
- **[ADK Skills: Part 2 - Wiring Skills](https://lavinigam.com/posts/adk-agent-skills-part2/#wiring-skills-into-the-agent)** — Technical deep dive into SkillToolset internals.
- **[ADK Skills: Part 3 - Skills That Write Skills](https://lavinigam.com/posts/adk-agent-skills-part3/#pattern-4-skills-that-write-skills)** — Pattern 4: The meta-skill of self-generation.
- **[Agent Skills Specification](https://agentskills.io/specification)** — The open standard adopted by 40+ agents.
- **[Companion Code Repository](https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-agent-skills-tutorial?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day06)** — Clone and run all four skill patterns.
