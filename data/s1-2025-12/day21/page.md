---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 21
title: "Kaggle Capstone Winners Highlight"
summary: "🏆 The Hall of Fame: Meet the Winners"
tags: ["Hall of Fame", "Winners", "Agents for Good", "Enterprise Agents", "Concierge Agents", "Freestyle"]
canonical_url: "https://adventofagents.com/2025/12/21"
markdown_url: "https://adventofagents.com/2025/12/21.md"
video_url: "https://www.youtube.com/embed/FrfaAwq0YNg"
---

# 🏆 Day 21: Kaggle Capstone Winners Highlight

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/21?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21) · [Raw Markdown](https://adventofagents.com/2025/12/21.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)

**Summary:** 🏆 The Hall of Fame: Meet the Winners

**Day 21 of Google's Advent of Agents**


**🏆 The Hall of Fame: Meet the Winners**

Over 11,000 teams competed to build the most effective agents. Here are the winners who took home the prizes across our four specialized tracks.

**🟢 Agents for Good Track**. Solving problems in education, healthcare, and sustainability.

- **🏆 1st Place:** [Carbon Footprint Optimization Engine](https://www.kaggle.com/code/sumitkumarguha/global-cfoe)
- Authors: Sumit Kumar Guha
- Concept: A compliance engine that pauses for human verification before making high-stakes supply chain decisions.

- **🥈 2nd Place:** [CarbonCalc AI](https://github.com/madhuwantha/carbon-calc-ai.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Madhuwantha Priyashan, Sanduni Pavithra
- Concept: An intelligent calculator that routes queries to specialized fuel or electricity agents for accurate emission reporting.

- **🥉 3rd Place:** [Parallel Scholar](https://github.com/emansarahafi/research-assistant-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Eman Afi, Yousef Elsonbaty
- Concept: An automated research assistant that synthesizes academic papers using parallel discovery and persistent memory.

**🏢 Enterprise Agents Track**. Improving business workflows and automating support.

- **🏆 1st Place:** [Chaos Playbook Engine](https://github.com/alberto-martinez-zurita/chaos-playbook-engine?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Alberto Martinez Zurita, Alessandro A. Russo
- Concept: A resilience lab that injects chaos (failures) into agents to test their recovery playbooks.

- **🥈 2nd Place:** [Coderama](https://github.com/debasisdwivedy/coderama?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Debasis Dwivedy
- Concept: An autonomous software delivery lifecycle agent managing requirements, planning, and development.

- **🥉 3rd Place:** [VeganFlow](https://github.com/karthiksothivelr/veganflow?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Karthick Sothivelr (Kart)
- Concept: Autonomous supply chain intelligence that negotiates with external vendor agents to prevent stockouts.

** 🛎️ Concierge Agents Track**. Streamlining daily life, travel, and shopping.

- **🏆 1st Place:** [NewsPulse AI Agent](https://github.com/azhang6-nlp/NewsPulse_AI_Agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Andy Zhang, S Tan, Vivien, Adelie Yang
- Concept: A self-correcting news analyst that verifies citations before delivering executive summaries.

- **🥈 2nd Place:** [FIL Content Agent System](https://github.com/jasononaquest/fil-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Jason Harrison
- Concept: A CMS agent that researches, writes, and publishes waterfall hiking guides in under 60 seconds.

- **🥉 3rd Place:** [AishIngAnalyzer](https://github.com/aishasartaj1/AishIngAnalyzer?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Aisha Sartaj
- Concept: A cosmetic ingredient analyzer that personalizes safety reports based on user allergies and skin type.

**🎨 Freestyle Track**. Innovative agents that break the mold.

- **🏆 1st Place:** [Daedalus - The Agentic Toolsmith](https://github.com/jovanovicmilos/daedalus-agentic-toolsmith?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Jovanovic Milos
- Concept: A self-expanding system that writes, tests, and registers its own new Python tools on the fly.
- **🥈 2nd Place:** [AI Stock Prediction System](https://github.com/nishantpithia/ai-stock-prediction-system?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Nishant Pithia, Vagge Sneha
- Concept: A multi-agent system analyzing stocks via 6 specialized agents (Macro, Sentiment, Regulatory).
- **🥉 3rd Place:** [StoryLand AI](https://github.com/ostrovskiy/storyland-ai?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)
- Authors: Ostrovskiy
- Concept: A literary travel planner that groups locations geographically to turn books into itineraries.

**🧠 Winning Architectures**

Success left clues. The top teams relied on rigid orchestration patterns rather than open-ended prompting:

1.  **The "Safety Gate" Pattern:** The Global CFOE used a SequentialAgent pipeline that explicitly pauses execution via `tool_context.request_confirmation()` if risk scores exceed 0.80, ensuring no "rogue" decisions.

2.  **The "Self-Correcting" Pattern:** Daedalus employed a LoopAgent to iteratively write and test code until it passed unit tests. Similarly, NewsPulse used a verification loop to reject any content lacking valid citations.

3.  **The "Parallel Specialist" Pattern:** StoryLand AI and Parallel Scholar dispatched multiple sub-agents simultaneously (e.g., City Agent, Landmark Agent) to reduce research time from hours to seconds.

## Resources & Links

- **[NewsPulse AI Agent (1st Place)](https://github.com/azhang6-nlp/NewsPulse_AI_Agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Concierge Agents Track - 1st Place
- **[FIL Content Agent System - Agent Code (2nd Place)](https://github.com/jasononaquest/fil-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Concierge Agents Track - 2nd Place Agent Code
- **[FIL Content Agent System - MCP Server Code (2nd Place)](https://github.com/jasononaquest/FIL-mcp?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Concierge Agents Track - 2nd Place MCP Server Code
- **[AishIngAnalyzer (3rd Place)](https://github.com/aishasartaj1/AishIngAnalyzer?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Concierge Agents Track - 3rd Place
- **[Carbon Footprint Optimization Engine (CfoE) (1st Place)](https://www.kaggle.com/code/sumitkumarguha/global-cfoe)** — Agents for Good Track - 1st Place
- **[CarbonCalc AI (2nd Place)](https://github.com/madhuwantha/carbon-calc-ai.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Agents for Good Track - 2nd Place
- **[Parallel Scholar (3rd Place)](https://github.com/emansarahafi/research-assistant-agent?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Agents for Good Track - 3rd Place
- **[Chaos Playbook Engine (1st Place)](https://github.com/alberto-martinez-zurita/chaos-playbook-engine?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Enterprise Agents Track - 1st Place
- **[Coderama (2nd Place)](https://github.com/debasisdwivedy/Coderama?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Enterprise Agents Track - 2nd Place
- **[VeganFlow (3rd Place)](https://github.com/karthick-sothivelr/Autonomous_Supply_Chain_Intelligence?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Enterprise Agents Track - 3rd Place
- **[Daedalus - The Agentic Toolsmith (1st Place)](https://github.com/jovanovic-milos/daedalus?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Freestyle Track - 1st Place
- **[AI Stock Prediction System (2nd Place)](https://github.com/nishapp/agents-5days-kaggle-competition?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Freestyle Track - 2nd Place
- **[StoryLand AI (3rd Place)](https://github.com/o-ostrovskiy/storyland-ai?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day21)** — Freestyle Track - 3rd Place
