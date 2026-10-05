---
season: 2
season_name: "Season 2 — March 2026 (Spring Cherry Blossom Edition)"
day: 26
title: "Authentication: End-User Identity Propagation"
summary: "Securely delegate permissions by prompting end-users for OAuth consent during agent execution."
tags: ["Authentication", "Security", "Identity Propagation", "Interactive Auth"]
canonical_url: "https://adventofagents.com/2026/03/26"
markdown_url: "https://adventofagents.com/2026/03/26.md"
video_url: "https://www.youtube.com/embed/NzQM4GihwQU"
---

# 🔐 Day 26: Authentication: End-User Identity Propagation

> **Season 2 — March 2026 (Spring Cherry Blossom Edition)** · [Interactive Web View](https://adventofagents.com/2026/03/26?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26) · [Raw Markdown](https://adventofagents.com/2026/03/26.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26)

**Summary:** Securely delegate permissions by prompting end-users for OAuth consent during agent execution.

**Day 26 of Google's Advent of Agents — Season 2**

Today we tackle something every production agent eventually needs: **acting on behalf of a real user**. When an agent needs to access an end-user's private data, like reading their Calendar, Mail or access any resource tied to a specific user's identity - you need to propagate the user's identity to the agent's tool.

**Solution: OAuth 2.0**

OAuth 2.0 lets the agent act on behalf of a specific user, with their explicit permission. The user sees a consent screen, approves access, and the auth server issues a short-lived access token scoped to that user's data. ADK has built-in support for this flow, but the approach differs depending on what kind of tool you're authenticating.

![OAuth2 Flow](/day26-oauth2flow.png)

**Server Side: Authentication Patterns in ADK**

| Pattern | What It Solves | Where to use |
|----------|---------------|-----------|
| **Using pre-built Authenticated Tools** | You configure the tool with an 1. **Auth scheme** (the type of authentication the API expects, e.g. OAuth2) and an 2. **Auth credential** (your app's `client_id` and `client_secret`). ADK automates everything else: it detects when credentials are missing, triggers the consent flow, exchanges the authorization code for an access token, stores it in the session, and automatically retries the original tool call once the user has authenticated.| Google Workspace tools (Calendar, Gmail, Drive etc.), GoogleApiToolSet, as well as OpenAPI and APIHub toolsets. |
| **Building custom FunctionTools** | When building pure custom tools from scratch, you manually orchestrate the full OAuth lifecycle inside your tool function. This provides you with granular control. | Because you supply the authorization endpoint, token endpoint, and auth scopes, this works with any OAuth 2.0 provider: Github, Salesforce, Notion, Spotify etc., |

**AuthenticatedFunctionTool:** This is a convenience wrapper that you can use for both the above patterns. If you have your own custom function but don't want to implement the full Pattern 2 auth logic, wrap it with an `[AuthConfig](https://github.com/google/adk-python/blob/main/contributing/samples/oauth_calendar_agent/agent.py?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26#L165-L186)` specifying the scopes you need. ADK handles credential detection, the consent flow, token exchange, and tool retry and you just write the function logic.


**Client Side: Handling the OAuth Flow**

OAuth 2.0 is a multi-step back-and-forth between your app, the user's browser, and the Auth Server. `adk web` handles all of this automatically during development. It acts as the local redirect handler, detects the auth event, opens the browser for the user, intercepts the OAuth callback, exchanges the code for a token, and resumes the agent automatically. But if you are building your own custom clients in production, you need to handle this flow. See the [ADK Authentication docs](https://google.github.io/adk-docs/tools-custom/authentication/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26#2-handling-the-interactive-oauthoidc-flow-client-side) for how to do that.

**Resources:**

- [Pre-built Tool Authentication](https://google.github.io/adk-docs/tools-custom/authentication/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26#1-configuring-tools-with-authentication)
- [Custom Tool Authentication](https://google.github.io/adk-docs/tools-custom/authentication/?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26#journey-2-building-custom-tools-functiontool-requiring-authentication)
- [OAuth Calendar Agent Sample Code](https://github.com/google/adk-python/blob/main/contributing/samples/oauth_calendar_agent/agent.py?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26)

## Code & Commands

### Setup Credentials

```bash
# 1. Follow the steps in this document to get the OAuth2 credentials:
# https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id
# 2. Set "http://127.0.0.1:8080/dev-ui/" as the redirect URI. Pay attention to the port number you are using.
# 3. Copy your Client ID and Client Secret into a .env file. In production, use a secret management tool - never hardcode secrets or put them in .env files.

OAUTH_CLIENT_ID="your-client-id.apps.googleusercontent.com"
OAUTH_CLIENT_SECRET="your-client-secret"
```

```python
from datetime import datetime
import os

from dotenv import load_dotenv
from fastapi.openapi.models import OAuth2
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.openapi.models import OAuthFlows
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import Agent
from google.adk.auth.auth_credential import AuthCredential
from google.adk.auth.auth_credential import AuthCredentialTypes
from google.adk.auth.auth_credential import OAuth2Auth
from google.adk.auth.auth_tool import AuthConfig
from google.adk.tools.authenticated_function_tool import AuthenticatedFunctionTool
from google.adk.tools.google_api_tool import CalendarToolset
from google.adk.tools.tool_context import ToolContext
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Access the variables.
oauth_client_id = os.getenv("OAUTH_CLIENT_ID")
oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET")


calendar_toolset = CalendarToolset(
    client_id=oauth_client_id,
    client_secret=oauth_client_secret,
    tool_filter=["calendar_events_get"],
)

def list_calendar_events(
    start_time: str,
    end_time: str,
    limit: int,
    tool_context: ToolContext,
    credential: AuthCredential,
) -> list[dict]:
    """Search for calendar events.

    Example:

        flights = get_calendar_events(
            calendar_id='joedoe@gmail.com',
            start_time='2024-09-17T06:00:00',
            end_time='2024-09-17T12:00:00',
            limit=10
        )
        # Returns up to 10 calendar events between 6:00 AM and 12:00 PM on
        September 17, 2024.

    Args:
        calendar_id (str): the calendar ID to search for events.
        start_time (str): The start of the time range (format is
          YYYY-MM-DDTHH:MM:SS).
        end_time (str): The end of the time range (format is YYYY-MM-DDTHH:MM:SS).
        limit (int): The maximum number of results to return.

    Returns:
        list[dict]: A list of events that match the search criteria.
    """

    creds = Credentials(
        token=credential.oauth2.access_token,
        refresh_token=credential.oauth2.refresh_token,
    )

    service = build("calendar", "v3", credentials=creds)
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_time + "Z" if start_time else None,
            timeMax=end_time + "Z" if end_time else None,
            maxResults=limit,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])
    return events


def update_time(callback_context: CallbackContext):
  # get current date time
  now = datetime.now()
  formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
  callback_context.state["_time"] = formatted_time


root_agent = Agent(
    model="gemini-3.1-pro-preview",
    name="calendar_agent",
    instruction="""
      You are a helpful personal calendar assistant.
      Use the provided tools to search for calendar events (use 10 as limit if user doesn't specify), and get information about them.
      Use "primary" as the calendarId if users don't specify.

      Scenario1:
      The user want to query the calendar events.
      Use list_calendar_events to search for calendar events.


      Scenario2:
      User want to know the details of one of the listed calendar events.
      Use google_calendar_events_get to get the details of a calendar event.

      Current user:
      <User>
      {userInfo?}
      </User>

      Current time: {_time}
""",
    tools=[
      AuthenticatedFunctionTool(
            func=list_calendar_events,
            auth_config=AuthConfig(
                auth_scheme=OAuth2(
                    flows=OAuthFlows(
                        authorizationCode=OAuthFlowAuthorizationCode(
                            authorizationUrl=(
                                "https://accounts.google.com/o/oauth2/auth"
                            ),
                            tokenUrl="https://oauth2.googleapis.com/token",
                            scopes={
                                "https://www.googleapis.com/auth/calendar.readonly": "",
                            },
                        )
                    )
                ),
                raw_auth_credential=AuthCredential(
                    auth_type=AuthCredentialTypes.OAUTH2,
                    oauth2=OAuth2Auth(
                        client_id=oauth_client_id,
                        client_secret=oauth_client_secret,
                    ),
                ),
            ),
        ),
        calendar_toolset],
    before_agent_callback=update_time, 
)
```

## Resources & Links

- **[ADK Tool Authentication](https://google.github.io/adk-docs/tools-custom/authentication/index.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26)**
- **[Interactive OAuth CLI Example](https://google.github.io/adk-docs/tools-custom/authentication/index.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26#handling-the-interactive-oauthoidc-flow-client-side)** — Documentation on how to authenticate agents in ADK.
- **[OAuth Calendar Agent Sample](https://github.com/google/adk-python/blob/main/contributing/samples/oauth_calendar_agent/agent.py?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26)** — Sample demonstrating AuthenticatedFunctionTool.
- **[Dynamic Identity Propagation (ServiceNow)](https://github.com/google/adk-samples/tree/main/python/agents/incident-management?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s2_2026&utm_content=day26)** — Example of token passing to third-party integrations.
