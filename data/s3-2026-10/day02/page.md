---
season: 3
season_name: "Season 3 — October 2026 (Autumn / Halloween Edition)"
day: 2
title: "Agent Security: Implementing SAIF Guardrails"
summary: "Secure agent workflows against rogue actions or data disclosure using SAIF threat modeling."
tags: ["Agent Security", "SAIF", "Guardrails"]
canonical_url: "https://adventofagents.com/2026/10/02"
markdown_url: "https://adventofagents.com/2026/10/02.md"
video_url: "https://www.youtube.com/embed/TA7lhezND7M"
primary_video:
  title: "Day 2: Why is Securing Agents Different? — 5-Minute Google Cloud Kata"
  creator_name: "Google Cloud Engineering"
  duration: "13:11"
  video_url: "https://www.youtube.com/embed/TA7lhezND7M"
---

# 🛡️ Day 2: Agent Security: Implementing SAIF Guardrails

> **Season 3 — October 2026 (Autumn / Halloween Edition)** · [Interactive Web View](https://adventofagents.com/2026/10/02?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s3_2026&utm_content=day02) · [Raw Markdown](https://adventofagents.com/2026/10/02.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s3_2026&utm_content=day02)

**Summary:** Secure agent workflows against rogue actions or data disclosure using SAIF threat modeling.

**Day 2 of Google's Advent of Agents — Season 3**

Presenters: Mika Devonshire & Anirudh Kannan

AI agents operating in enterprise environments require robust security controls to prevent rogue actions and sensitive data leakage. Implementing Google's Secure AI Framework (SAIF) ensures agents maintain strict operational boundaries while processing untrusted inputs.

**How It Works**

This threat modeling tutorial demonstrates how to scan agents for defense-in-depth using SAIF. The framework provides a structured approach to identify and mitigate risks associated with agentic workflows, including:

- **Input Sanitization**: Pre-filters malformed or malicious prompts before passing context to the model reasoning loop.
- **Rogue Actions**: Restricts tool execution and scope based on caller credentials and authenticated on-behalf-of user roles.
- **Sensitive Data Disclosure**: Scans generated responses for sensitive data patterns and redacts or masks data before returning output.

**Resources:**

- [Google Secure AI Framework (SAIF)](https://g.dev/cloud/adventofagents-season3-google-saif)
- [SAIF GitHub Repository](https://github.com/google/saif-data?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s3_2026&utm_content=day02)
- [OWASP Top 10 for LLMs](https://owasp.org/projects/top-10-for-large-language-model-applications)

## Code & Commands

```bash
export CLOUDSDK_METRICS_ENVIRONMENT="advent-of-agents-s3-day02"

gcloud auth application-default login
git clone https://github.com/google/saif-data.git
./launch_saif_demo.sh --serve
```

## Resources & Links

- **[Google Secure AI Framework (SAIF)](https://g.dev/cloud/adventofagents-season3-google-saif)** — Learn about Google's framework for securing AI systems and agentic workflows.
- **[SAIF GitHub Repository](https://github.com/google/saif-data?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s3_2026&utm_content=day02)** — GitHub repository for the Google Secure AI Framework (SAIF).
- **[OWASP Top 10 for LLMs](https://owasp.org/projects/top-10-for-large-language-model-applications)** — A list of the top 10 security risks for AI systems.
