---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 23
title: "Model Armor: AI Security Firewall for Agents"
summary: "Protect AI agents from prompt injection, jailbreaks, and data leakage using Google Cloud Model Armor as a defense-in-depth security layer."
tags: ["Model Armor", "Security", "GCP", "Agent Safety"]
canonical_url: "https://adventofagents.com/2026/03/23"
markdown_url: "https://adventofagents.com/2026/03/23.md"
video_url: "https://www.youtube.com/embed/Wrxg8OsquEY"
---

# 🛡️ Day 23: Model Armor: AI Security Firewall for Agents

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/23?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23) · [Raw Markdown](https://adventofagents.com/2026/03/23.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)

**Summary:** Protect AI agents from prompt injection, jailbreaks, and data leakage using Google Cloud Model Armor as a defense-in-depth security layer.

**Day 23 of Google's Advent of Agents — Season 2**

As AI agents become more advanced and autonomous, ensuring their security becomes a paramount concern. Developers must be vigilant against emerging threats that exploit the unique vulnerabilities of LLMs. To address this, developers can leverage **Google Cloud Model Armor** to build a robust defense-in-depth strategy, protecting their agents from manipulation and unintended data exposure.

**The Solution**

Google Cloud Model Armor serves as a specialized security layer—an "AI firewall" designed to protect generative AI applications by proactively screening both user prompts and model responses. It effectively mitigates critical risks such as prompt injection and jailbreak attacks, where malicious actors attempt to subvert a model's behavior or bypass safety constraints.

Beyond intent analysis, Model Armor prevents sensitive data leakage by identifying and redacting personally identifiable information (PII) or intellectual property. It also utilizes malicious URL detection to block phishing links embedded within AI interactions. Because it is model-agnostic and cloud-agnostic, you can use its REST API to enforce consistent safety and compliance policies across any Large Language Model (LLM) or agent, whether hosted on Google Cloud, another provider, or on-premises.

**How It Works**

- **Define Security Template**: Configure a Model Armor template with your security policies, threat detection rules, and PII redaction requirements.

- **Sanitize User Prompts**: Screen incoming prompts before they reach your LLM to detect and block prompt injection, jailbreak attempts, and malicious URLs.

- **Sanitize Model Responses**: Validate generated responses before returning to users, preventing sensitive data leakage and ensuring compliance with safety policies.

**Resources:**

- [Model Armor Documentation](https://docs.cloud.google.com/model-armor/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)
- [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)
- [GitHub Project Repository](https://github.com/lekan2001/advent-of-agents-model-armor.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)

## Code & Commands

### Sanitize User Prompts

```python
def sanitize_prompt(user_prompt: str) -> tuple[bool, str]:
    """Sanitize a user prompt using the Model Armor template.

    Args:
        user_prompt: The raw user prompt text to sanitize.

    Returns:
        A tuple of (is_safe, detail).
        - is_safe: True if the prompt passes all checks, False if blocked.
        - detail: Empty string when safe, or a description of why it was blocked.
    """
    try:
        client = _get_client()
        request = modelarmor_v1.SanitizeUserPromptRequest(
            name=TEMPLATE_NAME,
            user_prompt_data=modelarmor_v1.DataItem(text=user_prompt),
        )
        response = client.sanitize_user_prompt(request=request)
        blocked, reasons = _is_blocked(response.sanitization_result)
        if blocked:
            logger.warning("Model Armor blocked user prompt: %s", reasons)
            return False, reasons
        return True, ""
    except Exception:
        logger.exception("Model Armor sanitize_prompt call failed")
        return True, ""
```

### Sanitize Model Responses

```python
def sanitize_response(model_response: str) -> tuple[bool, str]:
    """Sanitize a model response using the Model Armor template.

    Args:
        model_response: The model-generated response text to sanitize.

    Returns:
        A tuple of (is_safe, detail).
        - is_safe: True if the response passes all checks, False if blocked.
        - detail: Empty string when safe, or a description of why it was blocked.
    """
    try:
        client = _get_client()
        request = modelarmor_v1.SanitizeModelResponseRequest(
            name=TEMPLATE_NAME,
            model_response_data=modelarmor_v1.DataItem(text=model_response),
        )
        response = client.sanitize_model_response(request=request)
        blocked, reasons = _is_blocked(response.sanitization_result)
        if blocked:
            logger.warning("Model Armor blocked model response: %s", reasons)
            return False, reasons
        return True, ""
    except Exception:
        logger.exception("Model Armor sanitize_response call failed")
        return True, ""
```

## Resources & Links

- **[Model Armor Documentation](https://docs.cloud.google.com/model-armor/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)** — Complete guide to Google Cloud Model Armor for AI security.
- **[GitHub Project Repository](https://github.com/lekan2001/advent-of-agents-model-armor.git?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)** — Working implementation of Model Armor with ADK agents.
- **[ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day23)** — Agent Development Kit documentation for building secure agents.
