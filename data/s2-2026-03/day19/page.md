---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 19
title: "Live Shopping Agent: Build with ADK and Gemini Embedding 2"
summary: "Build a live multimodal shopping app with ADK and Gemini Embedding 2."
tags: ["ADK", "Gemini Live", "Vector Search"]
canonical_url: "https://adventofagents.com/2026/03/19"
markdown_url: "https://adventofagents.com/2026/03/19.md"
video_url: "https://www.youtube.com/embed/SgMn-6q8Qg8"
---

# 🛒 Day 19: Live Shopping Agent: Build with ADK and Gemini Embedding 2

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/19?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19) · [Raw Markdown](https://adventofagents.com/2026/03/19.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)

**Summary:** Build a live multimodal shopping app with ADK and Gemini Embedding 2.

**Day 19 of Google's Advent of Agents — Season 2**

LensMosaic is a live multimodal shopping app. You point your camera at an item to find a similar one from one million items instantly, talk to the app, and get product matches or recommendations back in the same browser session.

**Live Shopping Agent**

The app supports two core flows: similar-item search from live visual input, and recommendation queries grounded in what the user is looking at and asking for. Under the hood, LensMosaic uses FastAPI and WebSockets for live browser sessions, ADK for the agent loop, ADK Gemini Live API Toolkit for multimodal interaction, Gemini Embedding 2 for retrieval text and image vectors, Vertex AI Vector Search 2.0 for candidate lookup, and Ranking API for final reranking. The result is a single-origin app that handles UI, live session traffic, and product retrieval in one place.

The `main.py` in this post is a digested version of that app. The user experience is intentionally narrower for the sake of clarity: you still get a live voice, text, and camera conversation with product recommendations in the browser, but you do not get the full similar-item search experience. The interesting parts are the live agent loop and recommendation flow, where you can see how FastAPI and ADK Gemini Live API Toolkit work together to realize a real-time interactive UX from browser input to model events, tool calls, and product tiles on screen.

**Resources:**

- [LensMosaic Live Demo](https://lens-mosaic-761793285222.us-central1.run.app/)
- [LensMosaic GitHub Repo](https://github.com/kazunori279/lens-mosaic/tree/main?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)
- [ADK](https://google.github.io/adk-docs/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)
- [ADK Gemini Live API Toolkit](https://google.github.io/adk-docs/streaming/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)
- [Gemini Embedding 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/embedding-2?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)
- [Vertex AI Vector Search 2.0](https://cloud.google.com/vertex-ai/docs/vector-search-2/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)
- [Vertex AI Ranking API](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)

## Code & Commands

### Run the Server

```shell
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID # replace
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_LOCATION=us-central1
uv run \
  --with google-adk \
  --with google-genai \
  --with google-cloud-aiplatform \
  --with certifi \
  uvicorn main:app --host 127.0.0.1 --port 8080

# Then open http://127.0.0.1:8080 with browser
```

### LensMosaic Server

```python
"""Minimal LensMosaic live server."""

from __future__ import annotations

import asyncio, base64, json, logging, os, ssl
import urllib.error, urllib.parse, urllib.request
from dataclasses import dataclass, field

import certifi
from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from google.adk.agents import Agent
from google.adk.agents.live_request_queue import LiveRequestQueue
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext
from google.genai import errors as genai_errors
from google.genai import types

import vertexai

os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "TRUE")

# App configuration and external service setup.
APP_NAME = "lens-mosaic-blog-sample"
AGENT_MODEL = "gemini-live-2.5-flash-native-audio"
MAX_TILE_ITEMS = 64
GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
GOOGLE_CLOUD_LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]
LENS_MOSAIC_COLLECTION_ID = "mercari3m-collection-mm2"
HOSTED_URL = "https://lens-mosaic-nhhfh7g7iq-uc.a.run.app"

vertexai.init(
    project=GOOGLE_CLOUD_PROJECT,
    location=GOOGLE_CLOUD_LOCATION,
)


# Per-live-session state shared across websocket handlers.
@dataclass
class SessionState:
    session_id: str
    user_id: str | None = None
    recommended: list[dict] = field(default_factory=list)
    tile_client: WebSocket | None = None


SESSION_STATES: dict[str, SessionState] = {}
SESSION_SERVICE = InMemorySessionService()
MAIN_LOOP: asyncio.AbstractEventLoop | None = None
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def _ignore_normal_live_close(record: logging.LogRecord) -> bool:
    exc = record.exc_info[1] if record.exc_info else None
    return not (isinstance(exc, genai_errors.APIError) and exc.code == 1000)


logging.getLogger(
    "google_adk.google.adk.flows.llm_flows.base_llm_flow"
).addFilter(_ignore_normal_live_close)


# Session lifecycle helpers.
def session_state_for(
    session_id: str, user_id: str | None = None
) -> SessionState:
    state = SESSION_STATES.get(session_id)
    if state is None:
        state = SessionState(session_id=session_id, user_id=user_id)
        SESSION_STATES[session_id] = state
        return state
    if user_id is not None:
        state.user_id = user_id
    return state


def cleanup_session(session_id: str) -> None:
    session = SESSION_STATES.get(session_id)
    if session and session.user_id is None and session.tile_client is None:
        SESSION_STATES.pop(session_id, None)


# Upstream proxy helpers for the hosted UI and APIs.
def fetch_upstream(
    path: str,
    *,
    method: str = "GET",
    body: bytes | None = None,
    content_type: str | None = None,
    query: list[tuple[str, str]] | None = None,
) -> tuple[int, str, bytes]:
    # Keep local sample routes thin by forwarding most HTTP work upstream.
    url = f"{HOSTED_URL}{path}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"
    headers = {"Content-Type": content_type} if content_type else {}
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30, context=SSL_CONTEXT) as response:
            return response.status, response.headers.get("Content-Type", ""), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers.get("Content-Type", ""), exc.read()


async def proxy_upstream(
    path: str,
    *,
    method: str = "GET",
    body: bytes | None = None,
    content_type: str | None = None,
    query: list[tuple[str, str]] | None = None,
) -> Response:
    status, media_type, data = await asyncio.to_thread(
        fetch_upstream,
        path,
        method=method,
        body=body,
        content_type=content_type,
        query=query,
    )
    return Response(content=data, status_code=status, media_type=media_type)


# Tile update helpers used by the local recommendation tool.
async def broadcast_recommended(session_id: str, items: list[dict]) -> None:
    session = SESSION_STATES.get(session_id)
    if not session:
        return
    ws = session.tile_client
    if ws is None:
        return
    try:
        await ws.send_json({"kind": "recommended", "items": items})
    except Exception:
        if session.tile_client is ws:
            session.tile_client = None


# Tool and agent definitions for the local live assistant.
def find_items(
    queries: list[str], ranking_query: str, tool_context: ToolContext
) -> str:
    """Find shopping items that match one or more product description queries.

    Use this tool to show product candidates on screen. Provide descriptive
    product-search queries and a ranking query in English. The tool searches,
    publishes the matched items to the UI, and uses ranking_query for the
    final rerank across the candidates.

    Args:
        queries: One or more product-search queries in English.
        ranking_query: A short English description used for final reranking.
        tool_context: ADK tool context for the current user session.

    Returns:
        A comma-separated string of top matched item names, or "No items found".
    """
    status, _, body = fetch_upstream(
        "/search",
        method="POST",
        body=json.dumps(
            {"queries": queries[:4], "ranking_query": ranking_query}
        ).encode(),
        content_type="application/json",
    )
    items = [] if status >= 400 else json.loads(body.decode())
    session = session_state_for(tool_context.session.id, tool_context.session.user_id)
    session.recommended = items[:MAX_TILE_ITEMS]
    if MAIN_LOOP:
        # Tool calls run off the main loop, so schedule the tile push back onto it.
        asyncio.run_coroutine_threadsafe(
            broadcast_recommended(session.session_id, session.recommended),
            MAIN_LOOP,
        )
    names = [item.get("name", "") for item in session.recommended[:3] if item.get("name")]
    return ", ".join(names) if names else "No items found"


agent = Agent(
    name="blog_sample_agent",
    model=AGENT_MODEL,
    tools=[find_items],
    instruction="""
        You are a helpful AI shopping assistant. Always respond in the user's language.
        You can hear the user's voice, read their text, and see camera images.
        When user asks what's in the image, describe it.
        When user asks for finding items, recommendation, or matching-product requests:
        - Do not ask a follow-up question before searching.
        - Briefly say what you will search.
        - Infer the desired items from the conversation and camera context.
        - Call find_items with 5 descriptive queries and a ranking_query.
        - After find_items returns, mention a few item names in simple language.""",
)
RUNNER = Runner(app_name=APP_NAME, agent=agent, session_service=SESSION_SERVICE)
RUN_CONFIG = RunConfig(
    streaming_mode=StreamingMode.BIDI,
    response_modalities=["AUDIO"],
    session_resumption=types.SessionResumptionConfig(),
)
app = FastAPI(title="LensMosaic Blog Sample", version="0.1.0")


# Live websocket communication between the browser and ADK.
async def ensure_adk_session(user_id: str, session_id: str) -> None:
    if not await SESSION_SERVICE.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id):
        await SESSION_SERVICE.create_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)


async def client_to_agent(ws: WebSocket, queue: LiveRequestQueue) -> None:
    while True:
        message = await ws.receive()
        if message.get("bytes") is not None:
            queue.send_realtime(
                types.Blob(mime_type="audio/pcm;rate=16000", data=message["bytes"])
            )
            continue
        if message.get("text") is None:
            continue
        payload = json.loads(message["text"])
        if payload.get("type") == "text":
            queue.send_content(types.Content(parts=[types.Part(text=payload["text"])]))
            continue
        if payload.get("type") != "image":
            continue
        if payload.get("forwardToAgent", True):
            queue.send_realtime(
                types.Blob(
                    mime_type=payload.get("mimeType", "image/jpeg"),
                    data=base64.b64decode(payload["data"]),
                )
            )


async def agent_to_client(user_id: str, session_id: str, ws: WebSocket, queue: LiveRequestQueue) -> None:
    # Stream ADK events straight back to the browser without reshaping them.
    async for event in RUNNER.run_live(
        user_id=user_id,
        session_id=session_id,
        live_request_queue=queue,
        run_config=RUN_CONFIG,
    ):
        await ws.send_text(event.model_dump_json(exclude_none=True, by_alias=True))


def is_disconnect_error(exc: Exception) -> bool:
    if isinstance(exc, RuntimeError):
        return "disconnect message has been received" in str(exc)
    if isinstance(exc, genai_errors.APIError):
        return exc.code == 1000
    return False


# FastAPI app lifecycle and proxied HTTP routes.
@app.on_event("startup")
async def startup() -> None:
    global MAIN_LOOP
    MAIN_LOOP = asyncio.get_running_loop()


@app.get("/")
async def root() -> Response:
    return await proxy_upstream("/")


@app.get("/static/{path:path}")
async def static_proxy(path: str, request: Request) -> Response:
    return await proxy_upstream(f"/static/{path}", query=list(request.query_params.multi_items()))


@app.post("/search")
async def search_proxy(request: Request) -> Response:
    body = await request.body()
    return await proxy_upstream("/search", method="POST", body=body, content_type=request.headers.get("content-type"))


@app.get("/api/item/{item_id}")
async def item_proxy(item_id: str) -> Response:
    return await proxy_upstream(f"/api/item/{item_id}")


# FastAPI websocket endpoints for recommendation tiles and live chat.
@app.websocket("/ws_image_tile/{session_id}")
async def tile_socket(ws: WebSocket, session_id: str) -> None:
    await ws.accept()
    session = session_state_for(session_id)
    session.tile_client = ws
    try:
        # New tile clients receive the latest recommendation snapshot immediately.
        await ws.send_json({"kind": "snapshot", "similarItems": [], "recommendedItems": session.recommended})
        while True:
            await ws.receive()
    except WebSocketDisconnect:
        pass
    except (RuntimeError, genai_errors.APIError) as exc:
        if not is_disconnect_error(exc):
            raise
    finally:
        if session.tile_client is ws:
            session.tile_client = None
        cleanup_session(session_id)


@app.websocket("/ws/{user_id}/{session_id}")
async def live_socket(ws: WebSocket, user_id: str, session_id: str) -> None:
    await ws.accept()
    await ensure_adk_session(user_id, session_id)
    session = session_state_for(session_id, user_id)
    # One queue feeds the ADK runner while both websocket tasks stay in sync.
    queue = LiveRequestQueue()
    try:
        await asyncio.gather(
            client_to_agent(ws, queue),
            agent_to_client(user_id, session_id, ws, queue),
        )
    except WebSocketDisconnect:
        pass
    except (RuntimeError, genai_errors.APIError) as exc:
        if not is_disconnect_error(exc):
            raise
    finally:
        queue.close()
        session.user_id = None
        cleanup_session(session_id)
```

## Resources & Links

- **[LensMosaic Live Demo](https://lens-mosaic-761793285222.us-central1.run.app/)**
- **[ADK Gemini Live API Toolkit](https://google.github.io/adk-docs/streaming/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)**
- **[Gemini Embedding 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/embedding-2?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)**
- **[Vertex AI Vector Search 2.0](https://cloud.google.com/vertex-ai/docs/vector-search-2/overview?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day19)**
