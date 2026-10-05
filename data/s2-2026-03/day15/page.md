---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 15
title: "Grounding with ADK: Agentic RAG with Vector Search 2.0"
summary: "Build an Agentic RAG system in 3 minutes with Vector Search 2.0 and ADK."
tags: ["ADK", "Vector Search", "RAG", "Python"]
canonical_url: "https://adventofagents.com/2026/03/15"
markdown_url: "https://adventofagents.com/2026/03/15.md"
video_url: "https://www.youtube.com/embed/IB6cXNx5iaw"
---

# 🔎 Day 15: Grounding with ADK: Agentic RAG with Vector Search 2.0

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/15?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15) · [Raw Markdown](https://adventofagents.com/2026/03/15.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)

**Summary:** Build an Agentic RAG system in 3 minutes with Vector Search 2.0 and ADK.

**Day 15 of Google's Advent of Agents — Season 2**

Vertex AI Vector Search 2.0 gives you auto embeddings generation, unified storage, and hybrid search in a single managed service. Agent Development Kit (ADK) gives you an agent that can reason about user intent and call tools. Wire them together with one Python function, and you get an Agentic RAG system where the LLM doesn't just retrieve-and-summarize — it parses intent, builds filters, and orchestrates searches.

**How It Works**

The glue between the agent and the search backend is a single Python function registered as an ADK tool. ADK inspects the function signature and docstring to generate the tool schema. The model decomposes natural language into a semantic query and structured filters, decides which constraints to apply, and synthesizes results into a conversational response, based on the user intent understanding.

- **Intent Parsing**: Decomposes natural language into a semantic query ("cozy workspace") and a structured filter (e.g. `{"$and": [{"neighborhood": {"$eq": "Hackney"}}, {"price": {"$lt": 150}}]}`).
- **Vector Search 2.0**: Auto-generates embeddings from text data during ingestion and provides managed hybrid search.
- **Task Types**: Utilizing the `QUESTION_ANSWERING` task type with Gemini embeddings ensures that semantic search leverages relevance-based retrieval for improved search quality.

**Resources:**

- [Vector Search 2.0 Overview](https://cloud.google.com/vertex-ai/docs/vector-search-2/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)
- [10-Minute Agentic RAG with the New Vector Search 2.0 and ADK](https://medium.com/google-cloud/10-minute-agentic-rag-with-the-new-vector-search-2-0-and-adk-655fff0bacac)
- [Travel Agent Notebook](https://github.com/google/adk-samples/blob/main/python/notebooks/grounding/vectorsearch2_travel_agent.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)
- [ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)

## Code & Commands

```bash
export GOOGLE_CLOUD_PROJECT=<YOUR_PROJECT_ID>
gcloud auth application-default login
gcloud services enable vectorsearch.googleapis.com aiplatform.googleapis.com

uv run --with google-adk --with google-cloud-vectorsearch \
       --with pandas --with requests demo.py
```

```python
import asyncio, io, json, os, time
import pandas as pd, requests
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.cloud import vectorsearch_v1beta

PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
LOCATION = "us-central1"
COLLECTION_ID = "london-rentals-demo"

os.environ["GOOGLE_CLOUD_LOCATION"] = LOCATION
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

admin_client = vectorsearch_v1beta.VectorSearchServiceClient()
data_client = vectorsearch_v1beta.DataObjectServiceClient()
search_client = vectorsearch_v1beta.DataObjectSearchServiceClient()
parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
collection_path = f"{parent}/collections/{COLLECTION_ID}"

print("Step 1: Creating collection with auto-embedding...")
collection_config = {
    "data_schema": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "number"},
            "neighborhood": {"type": "string"},
            "description": {"type": "string"},
        },
    },
    "vector_schema": {
        "description_embedding": {
            "dense_vector": {
                "dimensions": 768,
                "vertex_embedding_config": {
                    "model_id": "gemini-embedding-001",
                    "text_template": "{description}",
                    "task_type": "RETRIEVAL_DOCUMENT",
                },
            }
        }
    },
}

try:
    admin_client.get_collection(name=collection_path)
    print(f"Step 1: Collection '{COLLECTION_ID}' already exists.")
except Exception:
    req = vectorsearch_v1beta.CreateCollectionRequest(
        parent=parent, collection_id=COLLECTION_ID, collection=collection_config
    )
    admin_client.create_collection(request=req).result()
    print(f"Step 1: Collection '{COLLECTION_ID}' created.")

print("Step 2: Downloading and ingesting data...")
url = "https://data.insideairbnb.com/united-kingdom/england/london/2025-09-14/data/listings.csv.gz"
df = pd.read_csv(io.BytesIO(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content), compression="gzip")
df = df[["id", "name", "description", "price", "neighbourhood_cleansed"]].copy()
df["price"] = pd.to_numeric(df["price"].astype(str).str.replace(r"[$,]", "", regex=True), errors="coerce").fillna(0.0)
df = df.fillna("")
df = df[df["description"].str.strip().astype(bool)]
df = df[df["price"] > 0].head(100)
print(f"Step 2: {len(df)} listings ready for ingestion.")

data_objects = [
    {"data_object_id": str(row["id"]), "data_object": {
        "data": {"name": str(row["name"]), "price": float(row["price"]),
                 "neighborhood": str(row["neighbourhood_cleansed"]),
                 "description": str(row["description"])},
        "vectors": {},
    }} for _, row in df.iterrows()
]

for i in range(0, len(data_objects), 100):
    try:
        data_client.batch_create_data_objects(
            request=vectorsearch_v1beta.BatchCreateDataObjectsRequest(
                parent=collection_path, requests=data_objects[i:i+100]))
        time.sleep(2)
    except Exception as e:
        if "already exists" not in str(e).lower():
            raise
print("Step 2: Ingestion complete.")

print("Step 3: Registering search tool...")
def find_rentals(query: str, filter: str = "") -> list:
    """Search for vacation rentals using semantic search with metadata filtering."""
    print(f"\nfind_rentals(): query='{query}'")
    if filter.strip():
        print(f"find_rentals(): filter={filter}")

    search_kwargs = {
        "search_text": query,
        "search_field": "description_embedding",
        "task_type": "QUESTION_ANSWERING",
        "top_k": 10,
        "output_fields": vectorsearch_v1beta.OutputFields(
            data_fields=["name", "price", "neighborhood"]),
    }
    if filter.strip():
        search_kwargs["filter"] = json.loads(filter)

    response = search_client.search_data_objects(
        request=vectorsearch_v1beta.SearchDataObjectsRequest(
            parent=collection_path,
            semantic_search=vectorsearch_v1beta.SemanticSearch(**search_kwargs)))

    results = [{"name": r.data_object.data.get("name"),
             "price": r.data_object.data.get("price"),
             "neighborhood": r.data_object.data.get("neighborhood")}
            for r in response.results]
    print(f"find_rentals(): found {len(results)} results")
    return results

print("Step 4: Creating ADK agent...")
travel_agent = Agent(
    model="gemini-2.5-flash",
    name="travel_agent",
    instruction="""You are a London travel agent helping users find vacation rentals.
Use find_rentals with: query (vibe/description) and filter (JSON metadata constraints).
Filter fields: price (number), neighborhood (string).
Examples: {"price": {"$lt": 200}}, {"neighborhood": {"$eq": "Hackney"}},
{"$and": [{"neighborhood": {"$eq": "Hackney"}}, {"price": {"$lt": 200}}]}""",
    tools=[find_rentals],
)

runner = InMemoryRunner(agent=travel_agent, app_name="travel_agent")
print("Step 4: Agent ready.\n")

async def main():
    await runner.run_debug("Find me a cozy workspace")
    await runner.run_debug("Find me a cozy workspace under £200")
    await runner.run_debug("Find me an artist's loft in Hackney under £150")

if __name__ == "__main__":
    asyncio.run(main())
```

## Resources & Links

- **[10-Minute Agentic RAG with the New Vector Search 2.0 and ADK](https://medium.com/google-cloud/10-minute-agentic-rag-with-the-new-vector-search-2-0-and-adk-655fff0bacac)** — More details on the Agentic RAG architecture.
- **[Travel Agent Notebook](https://github.com/google/adk-samples/blob/main/python/notebooks/grounding/vectorsearch2_travel_agent.ipynb?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)** — Sample notebook for the Travel Agent.
- **[Enhancing search with embeddings and task types](https://cloud.google.com/blog/products/ai-machine-learning/improve-gen-ai-search-with-vertex-ai-embeddings-and-task-types?e=48754805&hl=en&utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)** — Learn how task type embeddings work.
- **[ADK Documentation](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day15)** — Complete guide to building AI agents.
