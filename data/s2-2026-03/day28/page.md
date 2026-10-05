---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 28
title: "A2A Protocol: Decoupling Reasoning from Execution"
summary: "Decouple your reasoning engine from execution using the universal A2A 1.0 protocol to bridge a Python LangGraph orchestrator and a Go ADK service."
tags: ["A2A", "LangGraph", "ADK", "Protocol"]
canonical_url: "https://adventofagents.com/2026/03/28"
markdown_url: "https://adventofagents.com/2026/03/28.md"
video_url: "https://www.youtube.com/embed/NsJ7UjRCnZU"
---

# 🤝 Day 28: A2A Protocol: Decoupling Reasoning from Execution

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/28?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day28) · [Raw Markdown](https://adventofagents.com/2026/03/28.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day28)

**Summary:** Decouple your reasoning engine from execution using the universal A2A 1.0 protocol to bridge a Python LangGraph orchestrator and a Go ADK service.

**Day 28 of Google's Advent of Agents — Season 2**

As AI development scales, teams often find themselves locked inside single-framework, single-language silos. If your reasoning team builds in Python using LangGraph, but your enterprise platform team builds scalable services in Go using ADK, how do they securely communicate?

**How It Works**

![A2A Cross-Framework Architecture](/season2-day28-architecture.png)

Enter A2A 1.0 (Agent-to-Agent Protocol). You don't need to rewrite your entire architecture into one mono-language monolith. A2A provides a standardized schema for agents to securely delegate tasks and share context across networks and varying programming languages.

- **Break the Silo**: Instantly connect a LangGraph orchestrator with an executing ADK agent using the universal A2A protocol. Because the payload is strictly standardized JSON, the receiving service can be natively written in Go, Python, or Java without requiring custom translation layers!
- **Protocol Over Framework**: Instead of building brittle, bespoke REST APIs for every single tool handoff, A2A 1.0 establishes a universal network contract. It standardizes the Task, Context, and Authenticated validation between any two heterogeneous AI microservices.
- **The Orchestrator Pattern**: Watch a local Python LangGraph node autonomously format an A2A 1.0 payload and dispatch it over HTTP POST to an external Go ADK execution service—completely decoupling the reasoning engine from the execution environment.

**Resources:**

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/): The orchestrator formatting the JSON A2A envelope.
- [Google GenAI SDK](https://ai.google.dev/docs?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day28): The API powering the underlying execution of the Gemini models.
- [Pydantic Reference](https://docs.pydantic.dev/): Recommended for strictly typing and parsing the A2A JSON dictionaries.
- [FastAPI Framework](https://fastapi.tiangolo.com/): Standard for receiving A2A POST payloads in production Python/Go microservices.

## Code & Commands

### Execution Framework (Go)

```go
// adk_execution_service.go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/pterm/pterm"
	_ "github.com/joho/godotenv/autoload"
)

// A2A 1.0 Universal Envelope Schema
type A2APayload struct {
	A2AVersion string            `json:"a2a_version"`
	SenderID   string            `json:"sender_id"`
	Task       string            `json:"task"`
	Context    map[string]string `json:"context"`
}

func handleA2A(w http.ResponseWriter, r *http.Request) {
	var payload A2APayload
	if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	pterm.Info.Printfln("[ADK Service] Received A2A Payload from %s: %s", pterm.LightCyan(payload.SenderID), pterm.LightYellow(payload.Task))

	apikey := os.Getenv("GEMINI_API_KEY")
	url := "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key=" + apikey

	reqBody := map[string]interface{}{
		"system_instruction": map[string]interface{}{
			"parts": []map[string]interface{}{{"text": "You are a platform execution agent. You receive A2A JSON payloads. Parse the 'task' and return a concise, step-by-step execution plan."}},
		},
		"contents": []map[string]interface{}{
			{"parts": []map[string]interface{}{{"text": fmt.Sprintf("Execute this A2A payload task: %s", payload.Task)}}},
		},
	}
	jsonReq, _ := json.Marshal(reqBody)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonReq))
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	defer resp.Body.Close()

	bodyBytes, _ := io.ReadAll(resp.Body)
	var genaiResp map[string]interface{}
	json.Unmarshal(bodyBytes, &genaiResp)

	var resultString string
	if cands, ok := genaiResp["candidates"].([]interface{}); ok && len(cands) > 0 {
		if content, ok := cands[0].(map[string]interface{})["content"].(map[string]interface{}); ok {
			if parts, ok := content["parts"].([]interface{}); ok && len(parts) > 0 {
				if text, ok := parts[0].(map[string]interface{})["text"].(string); ok {
					resultString = text
				}
			}
		}
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"final_result": resultString,
	})
	
	pterm.Success.Println("Dispatched response back to LangGraph!")
}

func main() {
	pterm.DefaultHeader.WithFullWidth().Println("Go ADK Execution Service")
	pterm.Info.Println("Listening on http://localhost:8080/execute")

	apikey := os.Getenv("GEMINI_API_KEY")
	maskedKey := apikey
	if len(apikey) > 8 {
		maskedKey = apikey[:8] + "..."
	} else if len(apikey) == 0 {
		maskedKey = "NOT CONFIGURED"
	}
	pterm.Info.Printfln("[Config] Loaded GEMINI_API_KEY: %s", pterm.LightYellow(maskedKey))

	http.HandleFunc("/execute", handleA2A)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

### Run Go Service (Terminal 1)

```bash
# 1. Create a root .env file with your API Key
echo 'GEMINI_API_KEY="your-api-key-here"' > .env

# Spin up the Go Execution Platform
go mod init example.com/adk 2>/dev/null || true
go get github.com/pterm/pterm github.com/joho/godotenv/autoload
go run adk_execution_service.go
```

### Reasoning Framework (Python)

```python
# Based on the ASP langgraph_base template
# a2a_langgraph_orchestrator.py
import os
import json
import urllib.request
from typing import TypedDict
from langgraph.graph import StateGraph, END
from rich.console import Console
from rich.panel import Panel
from rich.json import JSON
from rich.live import Live
from rich.spinner import Spinner
from rich.markdown import Markdown

from dotenv import load_dotenv
load_dotenv()

console = Console()

# ====================================================================
# 1. PYTHON LANGGRAPH AGENT (The Reasoning Framework)
# ====================================================================
class AgentState(TypedDict):
    objective: str
    a2a_payload: str
    final_result: str

def reasoning_node(state: AgentState):
    console.print(Panel("[bold green]LangGraph[/bold green]: Reasoning complete. Formatting A2A 1.0 envelope.", title="[Reasoning Engine]"))
    
    # Standard A2A 1.0 Payload formulation
    envelope = {
        "a2a_version": "1.0",
        "sender_id": "langgraph-orchestrator",
        "task": state["objective"],
        "context": {"urgency": "high", "auth_token": "bearer_abc123"}
    }
    return {"a2a_payload": json.dumps(envelope)}

def a2a_dispatch_node(state: AgentState):
    """Dispatches the A2A payload to the Go ADK framework across the network"""
    
    with Live(Spinner("dots", text="[bold yellow]Dispatching A2A payload via HTTP POST to Go Service...[/bold yellow]"), refresh_per_second=10) as live:
        req = urllib.request.Request(
            "http://localhost:8080/execute", 
            data=state["a2a_payload"].encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                live.update(Panel("[bold green]Dispatch Success![/bold green]", title="[Network]"))
                return {"final_result": result["final_result"]}
        except Exception as e:
            live.update(Panel(f"[bold red]Dispatch failed[/bold red]: {e}", title="[Network]"))
            return {"final_result": f"Dispatch failed: {e}"}

# 2. Build and Run the Graph
workflow = StateGraph(AgentState)
workflow.add_node("reason", reasoning_node)
workflow.add_node("delegate_via_a2a", a2a_dispatch_node)

workflow.set_entry_point("reason")
workflow.add_edge("reason", "delegate_via_a2a")
workflow.add_edge("delegate_via_a2a", END)

langgraph_app = workflow.compile()

if __name__ == "__main__":
    console.print(Panel("[bold blue]Starting LangGraph A2A Orchestrator[/bold blue]", title="[System]"))
    
    apikey = os.environ.get("GEMINI_API_KEY", "")
    masked_key = apikey[:8] + "..." if len(apikey) > 8 else apikey
    console.print(Panel(f"[bold yellow]Loaded GEMINI_API_KEY[/bold yellow]: {masked_key}", title="[Config]"))
    
    final_state = langgraph_app.invoke({
        "objective": "Execute production database migration to Cloud SQL", 
        "a2a_payload": "",
        "final_result": ""
    })
    
    console.print(Panel(JSON(final_state["a2a_payload"]), title="[A2A 1.0 Envelope - Dispatched]"))
    
    console.print(Panel(Markdown(final_state['final_result']), title="[ADK Execution Result]"))
```

### Run Python Orchestrator (Terminal 2)

```bash
# Trigger the LangGraph Orchestrator
pip install langgraph rich pydantic python-dotenv
python a2a_langgraph_orchestrator.py
```

## Resources & Links

- **[LangChain Blog: Multi-Agent Workflows](https://blog.langchain.dev/multi-agent-workflows/)** — Conceptual architectures for delegating tasks between disconnected agent frameworks.
- **[YouTube: Stop using MCP for everything!](https://www.youtube.com/watch?v=ks4M8b9Ul6E)** — RAG vs. A2A vs. Sub-agents architecture explained.
- **[Google Cloud: Building AI Workflows](https://cloud.google.com/blog/products/ai-machine-learning?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day28)** — High-level patterns for decoupling robust AI reasoning engines from API execution.
- **[Agent Starter Pack Walkthrough](https://github.com/GoogleCloudPlatform/agent-starter-pack?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day28)** — Explore the Agent-to-Agent interaction patterns built by Google Cloud engineers.
