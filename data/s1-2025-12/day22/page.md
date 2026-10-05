---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 22
title: "Security & Guardrails"
summary: "Prompt Engineering is not a Security Strategy. Asking an LLM nicely to \"please ignore PII\" is not governance; it's wishful thinking."
tags: ["Model Armor", "Security", "guardrails", "ADK"]
canonical_url: "https://adventofagents.com/2025/12/22"
markdown_url: "https://adventofagents.com/2025/12/22.md"
video_url: "https://www.youtube.com/embed/j9YyZM2OBS8"
---

# 🛡️ Day 22: Security & Guardrails

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/22?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22) · [Raw Markdown](https://adventofagents.com/2025/12/22.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)

**Summary:** Prompt Engineering is not a Security Strategy. Asking an LLM nicely to "please ignore PII" is not governance; it's wishful thinking.

**Day 22 of Google's Advent of Agents**

**Prompt Engineering is not a Security Strategy 🚫**
Asking an LLM nicely to "please ignore PII" is not governance; it's wishful thinking 🔮. Enterprise security requires **deterministic enforcement**, not probabilistic compliance 🎲.
To survive a security audit 👮, you need a **defense-in-depth** strategy. You must treat the LLM as an untrusted component, sandwiching it between rigid logic and infrastructure firewalls 🧱.

**ADK replaces "trust" with "verification" through a tiered architecture:**
• **The Developer Layer (Callbacks) 👨‍💻** Stop leaking data before it leaves your container 🛑. Use **ADK Callbacks** to inject deterministic Python logic before_agent execution. This acts as middleware—stripping PII 🕵️, validating schemas, and blocking unauthorized intents before the model ever sees the prompt.
• **The Infrastructure Layer (Model Armor) 🛡️** We cannot rely on developer discipline alone. Model Armor sits at the gateway level, inspecting every input and output 🔍. It provides a global kill-switch 🔌 for toxic content and injection attacks, ensuring safety even if the agent code is compromised.

**Secure the Payload, then Secure the Entity 🔐** Once the data is clean, **Agent Identity** ensures your "Service Agent" cannot authenticate into "HR Tools," while the **A2A Protocol** ensures that every handshake between agents is traceable, observable, and strictly authorized 🤖💬🤖.

**The guardrail level with a glance:**
![The guardrail level with a glance](/guardrail.png)

**How to augment it with custom Model Gateways and applying your own Guardrail agent for every input/output of a model:**
![How to augment it with custom Model Gateways and applying your own Guardrail agent for every input/output of a model](/guardrails%20with%20gcp.png)

## Code & Commands

```python
## The Developer Layer: Callbacks & Plugins 
# This Python snippet demonstrates how to inject security logic using the ADK callback system.


from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from .tools import add, subtract, multiply, divide
from .prompt import instruction_prompt
from google.genai import types
from typing import Optional

MODEL = "gemini-2.5-flash"

async def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:
       # Guardrail 1: Do we have the student profile?
       if not callback_context.state.get("student_profile"):
               return types.Content(role='model', parts=[types.Part(text="Error: Cannot find student profile.")])
# Add more guardrails...

       return None # Allow model call to proceed

agent_math = Agent(
       model=MODEL,
       name="agent_math",
       description="This agent performs basic arithmetic operations (addition, subtraction, multiplication, and division) on user-provided numbers, including ranges.",
       instruction=instruction_prompt,
       tools=[add, subtract, multiply, divide],
       before_agent_callback=callback_before_agent,
)
```

```python
## This Python snippet demonstrates how to create an ADK plugin.

from google.adk.agents.base_agent import BaseAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.plugins.base_plugin import BasePlugin

class CountInvocationPlugin(BasePlugin):
 """A custom plugin that counts agent and tool invocations."""
 def __init__(self) -> None:
   """Initialize the plugin with counters."""
   super().__init__(name="count_invocation")
   self.agent_count: int = 0
   self.tool_count: int = 0
   self.llm_request_count: int = 0

 async def before_agent_callback(self, *, agent: BaseAgent, callback_context:CallbackContext) -> None: 
   """Count agent runs."""
   self.agent_count += 1
   print(f"[Plugin] Agent run count: {self.agent_count}")
```

```python
## This Python snippet demonstrates how to load/apply an ADK plugin to an agent.

from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.genai import types
import asyncio

# Import the plugin.
from .count_plugin import CountInvocationPlugin

async def hello_world(tool_context: ToolContext, query: str):
 print(f'Hello world: query is [{query}]')
 root_agent = Agent(
   model='gemini-2.0-flash',
   name='hello_world',
   description='Prints hello world with user query.',
   instruction="""Use hello_world tool to print hello world and user query.""",
   tools=[hello_world],
)

async def main():
 """Main entry point for the agent."""
 prompt = 'hello world'
 runner = InMemoryRunner(agent=root_agent, app_name='test_app_with_plugin',
     # Add your plugin here. You can add multiple plugins.
     plugins=[CountInvocationPlugin()],)
 ...
```

```bash
## The Admin Layer: 
# Model Armor Template While developers write Python
# Admins configure Model Armor to sanitize data globally.

export TEMPLATE_CONFIG='{
   "filterConfig": {
    "raiSettings": {
     "raiFilters": [{
       "filterType": "HATE_SPEECH",
       "confidenceLevel": "MEDIUM_AND_ABOVE"
      }, {
      "filterType": "HARASSMENT",
      "confidenceLevel": "HIGH"
    }]
  },
  "piAndJailbreakFilterSettings": {
    "filterEnforcement": "ENABLED",
    "confidenceLevel": "LOW_AND_ABOVE"
  }
 },
 "templateMetadata": {
    "multiLanguageDetection": {
      "enableMultiLanguageDetection": true
    }
  }
}'

curl -X POST  -d "$TEMPLATE_CONFIG"   -H "Content-Type: application/json"  -H "Authorization: Bearer $(gcloud auth print-access-token)"     "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/templates?template_id=TEMPLATE_ID"
```

## Resources & Links

- **[ADK Callbacks: Design Patterns and Best Practices](https://google.github.io/adk-docs/callbacks/design-patterns-and-best-practices/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Explore design patterns and best practices for ADK callbacks.
- **[ADK Callbacks](https://google.github.io/adk-docs/callbacks/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Official documentation for ADK Callbacks.
- **[ADK Plugins](https://google.github.io/adk-docs/plugins/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Official documentation for ADK Plugins.
- **[Model Armor Overview](https://docs.cloud.google.com/model-armor/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Overview of Model Armor for security.
- **[Manage Model Armor Templates](https://docs.cloud.google.com/model-armor/manage-templates?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Documentation on managing Model Armor templates.
- **[Agent Builder - Agent Identity](https://docs.cloud.google.com/agent-builder/agent-engine/agent-identity?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Documentation on Agent Identity in Agent Builder.
- **[Build and scale AI agents with Vertex AI Agent Builder](https://cloud.google.com/blog/products/ai-machine-learning/more-ways-to-build-and-scale-ai-agents-with-vertex-ai-agent-builder?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day22)** — Blog post on building and scaling AI agents.
- **[A2A Protocol - Enterprise Ready](https://a2a-protocol.org/latest/topics/enterprise-ready/#tracing-observability-and-monitoring)** — Enterprise-ready features of the A2A Protocol.
