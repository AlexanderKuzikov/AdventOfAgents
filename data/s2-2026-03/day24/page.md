---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 24
title: "Batch Processing: Scale to 10k with ADK"
summary: "Shift from interactive processing to an Agent as Orchestrator pattern using the ADK and Gemini Batch API for efficient, large-scale asynchronous workloads."
tags: ["Batch Processing", "ADK", "Scale"]
canonical_url: "https://adventofagents.com/2026/03/24"
markdown_url: "https://adventofagents.com/2026/03/24.md"
video_url: "https://www.youtube.com/embed/3erD0GqEzX8"
---

# ⚙️ Day 24: Batch Processing: Scale to 10k with ADK

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/24?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24) · [Raw Markdown](https://adventofagents.com/2026/03/24.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)

**Summary:** Shift from interactive processing to an Agent as Orchestrator pattern using the ADK and Gemini Batch API for efficient, large-scale asynchronous workloads.

**Day 24 of Google's Advent of Agents - Season 2**

Forcing an agent into a real-time synchronous loop to extract data from 10,000 documents guarantees throttled API limits, broken connections, and massive token costs. To achieve production scale, you must shift your architecture from interactive processing to an "Agent as Orchestrator" pattern.

![Architecture](/season2-day24-architecture.png)

**How It Works**

Instead of an agent reading documents one by one, ADK enables you to equip your agent with a dedicated tool that offloads massive datasets directly to Google's backend infrastructure.

- **Tool-Based Offloading**: The agent autonomously recognizes high-volume requests (like "process this bucket") and uses a custom tool to bundle the instructions and data into a managed job queue, rather than awaiting immediate inference.
- **Token Efficiency**: The tool routes the request through the Gemini Batch API, executing the workload asynchronously in the background. This flex processing operates at a 50% token cost reduction compared to standard synchronous LLM calls.
- **State Retrieval**: Once the agent confirms the batch job is submitted, the session can safely terminate. Developers can poll the job status or configure a webhook callback to retrieve the structured output once the entire dataset completes processing.

**Resources:**

- [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)
- [Gemini Batch Prediction Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)
- [Gemini Batch API Limits and Pricing](https://cloud.google.com/vertex-ai/pricing?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)
- [Google GenAI Python SDK (GitHub)](https://github.com/googleapis/python-genai?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)
- [Deep Dive: How Batch Mode Cuts Costs](https://medium.com/@linz07m/how-gemini-apis-batch-mode-cuts-costs-and-increases-throughput-27cb9863a1c8)

## Code & Commands

### Batch Processor

```python
import os
import json
import urllib.request
from google import genai
from google.genai import types

# 1. Initialize the Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. Fetch live data from the web to create the JSONL dataset
dataset_path = "unprocessed_batch_01.jsonl"
print("Fetching live headlines from Hacker News...")

# Grab the top 5 story IDs from the public Hacker News API
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = json.loads(urllib.request.urlopen(top_stories_url).read())[:5]

# Format the live data into Gemini's JSONL Batch structure
with open(dataset_path, "w") as f:
    for sid in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        story = json.loads(urllib.request.urlopen(story_url).read())
        prompt = f"Extract companies, products, and technologies from this headline: {story.get('title', '')}"
        f.write(json.dumps({"request": {"contents": [{"parts": [{"text": prompt}]}]}}) + "\n")

# 3. Upload your JSONL dataset to the Gemini API
uploaded_file = client.files.upload(
    file=dataset_path, 
    config={'mime_type': 'application/jsonl'}
)
print(f"Uploaded file: {uploaded_file.uri}")

# 4. Submit the Asynchronous Batch Job at 50% token cost
batch_job = client.batches.create(
    model="gemini-3.1-pro-preview",
    src=uploaded_file.name,
    config=types.CreateBatchJobConfig(
        display_name="massive_document_extractor",
    )
)

print(f"Batch job {batch_job.name} submitted successfully.")
print(f"Current State: {batch_job.state}")

with open(".latest_batch_job.txt", "w") as cached_file:
    cached_file.write(batch_job.name)
```

### Status Polling Script

```python
import os
import sys
from google import genai

# 1. Initialize Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: Please export your GEMINI_API_KEY before running this script.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# 2. Get the Batch Job ID to poll
job_name = None
if len(sys.argv) > 1:
    job_name = sys.argv[1]
elif os.path.exists(".latest_batch_job.txt"):
    with open(".latest_batch_job.txt", "r") as cached_file:
        job_name = cached_file.read().strip()
    print(f"Auto-detected latest job ID from cache: {job_name}")

if not job_name:
    job_name = input("Enter the Batch Job name (e.g. batches/12345ABCD): ").strip()

if not job_name.startswith("batches/"):
    job_name = f"batches/{job_name}"

# 3. Request Status from Backend
try:
    print(f"\nPolling Google Cloud for status of: {job_name}...")
    job = client.batches.get(name=job_name)
    
    print("=" * 50)
    print(f"Job Name    : {job.name}")
    print(f"State       : {job.state}")
    
    if job.state == "JOB_STATE_SUCCEEDED":
        uri = getattr(job, "output_uri", "Available via Google Cloud Console")
        print(f"Output URI  : {uri}")
        print("\nSuccess! You can now download and parse the JSON payload.")
    elif job.state == "JOB_STATE_FAILED":
        print("\nThe job failed on the backend.")
        print("Error details:", getattr(job, "error", "Unknown API Error"))
        
    print("=" * 50)
except Exception as e:
    print(f"\nFailed to fetch job status. Ensure the ID is correct.")
    print(f"Error: {e}")
```

### Run Locally

```bash
# 1. Set up a pristine Python environment
python3 -m venv .venv && source .venv/bin/activate
pip install google-genai

# 2. Export your Gemini API key
export GEMINI_API_KEY="your-secret-key"

# 3. Submit your massive dataset to the background batch service
python batch_processor.py

# 4. In a few minutes, poll for the completed workload!
python check_status.py
```

## Resources & Links

- **[Scaling Language Detection: A Million Messages with Gemini’s Batch API & Flash Lite](https://medium.com/google-cloud/scaling-language-detection-a-million-messages-with-geminis-batch-api-flash-lite-baccc197a1c2)**
- **[From GenAI Demo to Production Scale - Handling high-throughput use cases](https://medium.com/google-cloud/from-genai-demo-to-production-scale-handling-high-throughput-use-cases-fbca401a5555)**
- **[Batch Mode in the Gemini API: Process more for less (Official Announcement)](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)**
- **[Experimentation to Production with Gemini and Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/experimentation-to-production-with-gemini-and-vertex-ai?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day24)**
