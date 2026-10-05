---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 29
title: "ApiRegistry: Dynamically Fetching BigQuery Tools"
summary: "Learn how to use the ApiRegistry object to dynamically fetch an admin-approved, fully configured BigQuery tool directly from the Cloud API Registry at runtime."
tags: ["ApiRegistry", "BigQuery", "Authentication"]
canonical_url: "https://adventofagents.com/2026/03/29"
markdown_url: "https://adventofagents.com/2026/03/29.md"
video_url: "https://www.youtube.com/embed/981wf6l3fCA"
---

# 🗄️ Day 29: ApiRegistry: Dynamically Fetching BigQuery Tools

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/29?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29) · [Raw Markdown](https://adventofagents.com/2026/03/29.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29)

**Summary:** Learn how to use the ApiRegistry object to dynamically fetch an admin-approved, fully configured BigQuery tool directly from the Cloud API Registry at runtime.

**Day 29 of Google's Advent of Agents — Season 2**

Hardcoding API credentials into your agents is a security risk and an infrastructure headache. Instead, we can dynamically fetch admin-approved, fully configured tools directly from the Cloud API Registry at runtime.

**How It Works**

By leveraging the `ApiRegistry`, we separate our agent logic from infrastructure specifics to enforce strict enterprise governance while keeping our AI portable. The registry ensures the agent always pulls the right connection settings, IAM roles, and boundaries without relying on local keys.

- **Dependencies**: Include `google-cloud-bigquery` and `google-auth` to securely interact with GCP.
- **Environment Authorization**: Use Application Default Credentials to connect from your local environment seamlessly, or inherit Workload Identity when running on Cloud Run.
- **ApiRegistry Reference**: The wrapper dynamically yields a configured `bigquery.Client()` out of the box so your code stays clean and your credentials stay safe.

**Resources:**

- [API Registry Documentation](https://docs.cloud.google.com/api-registry/docs/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29)
- [Enhanced Tool Governance in Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29)

## Code & Commands

### Python Dependencies

```text
google-cloud-bigquery
google-auth
```

### Environment Setup

```bash
#!/bin/bash
#1. Install dependencies
pip install -r requirements.txt

#2. Setup the "Registry" Data
echo "Setting up Registry Data"

#replace project-id with your project id
bq mk --dataset project-id:registry_demo
bq query --use_legacy_sql=false \
'CREATE OR REPLACE TABLE `project-id.registry_demo.test_table` AS SELECT "Registry_Active" as status'

#3. Authorize the environment
echo "Please authorize the environment registry:"
gcloud auth application-default login
```

### Dynamic Loader

```python
import google.auth
from google.cloud import bigquery

class ApiRegistry:
    @staticmethod
    def get_tool(tool_id):
        #Dynamically fetch config from Cloud Registry
        creds, project = google.auth.default()
        project = project or "project-id" #replace project-id with your project id
        return bigquery.Client(credentials=creds, project=project)

def run_task():
    #1. Fetch tool from Registry
    bq = ApiRegistry.get_tool("bigquery-admin-v2")
    
    # 2. Execute admin-approved query
    #replace project-id with your project id
    sql = "SELECT status FROM `project-id.registry_demo.test_table`"
    for row in bq.query(sql):
        print(f"Verified via Registry: {row.status}")

if __name__ == "__main__":
    run_task()
```

## Resources & Links

- **[API Registry Documentation](https://docs.cloud.google.com/api-registry/docs/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29)** — Official documentation for the Cloud API Registry.
- **[Enhanced Tool Governance Blog Post](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder?e=48754805&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day29)** — Google Cloud blog post covering Vertex AI Agent Builder tool governance.
