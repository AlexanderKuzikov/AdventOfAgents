---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 22
title: "ADK Evaluation: Trajectory Tests and Rubric-Based Scoring"
summary: "Define deterministic trajectory tests and rubric-based evaluations that run on every code push, catching agent regressions before they reach production."
tags: ["ADK", "Evaluation", "CI/CD", "Testing"]
canonical_url: "https://adventofagents.com/2026/03/22"
markdown_url: "https://adventofagents.com/2026/03/22.md"
video_url: "https://www.youtube.com/embed/_JVwS-20fTg"
---

# ✅ Day 22: ADK Evaluation: Trajectory Tests and Rubric-Based Scoring

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/22?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22) · [Raw Markdown](https://adventofagents.com/2026/03/22.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)

**Summary:** Define deterministic trajectory tests and rubric-based evaluations that run on every code push, catching agent regressions before they reach production.

**Day 22 of Google's Advent of Agents — Season 2**

Building an agent that "usually works" is easy — building one that reliably follows a specific reasoning path is the real challenge. As agents scale, "vibes-based testing" (refreshing the prompt and hoping for the best) breaks down, and you need a way to ensure your agent doesn't just give the right answer but arrives there using the correct tool trajectory. ADK Evalsets solve this by letting you define deterministic trajectory tests and rubric-based evaluations that hook directly into your CI pipeline.

**How It Works**

An evalset is a JSON file containing test cases, each specifying a user prompt, the expected tool call sequence, and an optional reference response. ADK's evaluation engine replays these cases against your agent and scores them using configurable criteria:

- **`tool_trajectory_avg_score`**: Checks whether the agent called the right tools in the right order. Use `IN_ORDER` match type to tolerate extra calls between expected ones, or `EXACT` for strict matching.
- **`rubric_based_final_response_quality_v1`**: Uses a stronger judge model (like Gemini 3.0 Flash) to grade the agent's output against custom rubrics, with no reference answer required.
- **`final_response_match_v2`**: Semantic comparison between the agent's response and a reference answer, tolerant of phrasing differences.

**CI/CD Integration**

The `agent-starter-pack` scaffolds a project with a `tests/eval/` directory and a pre-configured `make eval` target. Wire it into GitHub Actions so that any commit causing a trajectory deviation or a rubric score drop fails the build automatically, catching regressions before they reach production.

**Resources:**

- [ADK Evaluation Docs](https://google.github.io/adk-docs/evaluate/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)
- [ADK Eval Criteria Reference](https://google.github.io/adk-docs/evaluate/criteria/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)
- [Agent Starter Pack](https://github.com/googlecloudplatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)

## Code & Commands

### Bootstrap and Run

```bash
# 1. Scaffold an agent with the eval framework built-in
uvx agent-starter-pack create --adk my-agent && cd my-agent

# 2. Define a trajectory test in your evalset (eval/trajectory_tests.json)
# See the evalset snippet below for the full schema

# 3. Run the evaluation locally
make eval

# 4. Or run directly with the ADK CLI
adk eval ./app eval/trajectory_tests.json \
  --config_file_path=eval/eval_config.json \
  --print_detailed_results
```

### Evalset: Define the Golden Path

```json
{
  "eval_set_id": "trajectory_tests",
  "name": "Tool Trajectory Tests",
  "eval_cases": [
    {
      "eval_id": "sync_linear_to_github",
      "conversation": [
        {
          "invocation_id": "inv_1",
          "user_content": {
            "parts": [{ "text": "Sync Linear issue PROJ-123 to GitHub" }]
          },
          "final_response": {
            "role": "model",
            "parts": [{ "text": "Created GitHub issue #42 from PROJ-123." }]
          },
          "intermediate_data": {
            "tool_uses": [
              { "name": "linear_get_issue", "args": { "issue_id": "PROJ-123" } },
              { "name": "github_create_issue", "args": { "repo": "my-org/my-repo" } }
            ]
          }
        }
      ],
      "session_input": {
        "app_name": "my_agent", "user_id": "eval_user", "state": {}
      }
    }
  ]
}
```

### Eval Config: Set Pass/Fail Criteria

```json
{
  "criteria": {
    "tool_trajectory_avg_score": {
      "threshold": 1.0,
      "match_type": "IN_ORDER"
    },
    "rubric_based_final_response_quality_v1": {
      "threshold": 0.8,
      "rubrics": [
        {
          "rubric_id": "completeness",
          "rubric_content": {
            "text_property": "The response must confirm which issue was synced and provide the new GitHub issue number."
          }
        }
      ]
    }
  }
}
```

## Resources & Links

- **[ADK Evaluation Docs](https://google.github.io/adk-docs/evaluate/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)** — Official ADK evaluation overview — evalsets, criteria, and CLI commands
- **[ADK Eval Criteria Reference](https://google.github.io/adk-docs/evaluate/criteria/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)** — All 8 built-in metrics, match types, custom rubrics, and judge model config
- **[Agent Starter Pack](https://github.com/googlecloudplatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)** — Scaffold an ADK agent project with built-in eval directory and CI/CD pipelines
- **[ADK Samples](https://github.com/google/adk-samples?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day22)** — Reference agents with evalsets you can study and adapt
