---
season: 1
season_name: "Season 1 — December 2025 (Winter Holiday Edition)"
day: 20
title: "A2A Extensions: The Flexible Sidecar for Custom Data"
summary: "The Agent-to-Agent (A2A) protocol relies on a strict format, but real-world complexity often requires unique data. A2A Extensions provide a \"Sidecar\" pattern for custom data without breaking backward compatibility."
tags: ["A2A Extensions", "Extensions", "Sidecar Pattern", "Agent Communication"]
canonical_url: "https://adventofagents.com/2025/12/20"
markdown_url: "https://adventofagents.com/2025/12/20.md"
video_url: "https://www.youtube.com/embed/MV0Ub-xN48A"
---

# 🧩 Day 20: A2A Extensions: The Flexible Sidecar for Custom Data

> **Season 1 — December 2025 (Winter Holiday Edition)** · [Interactive Web View](https://adventofagents.com/2025/12/20?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day20) · [Raw Markdown](https://adventofagents.com/2025/12/20.md?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day20)

**Summary:** The Agent-to-Agent (A2A) protocol relies on a strict format, but real-world complexity often requires unique data. A2A Extensions provide a "Sidecar" pattern for custom data without breaking backward compatibility.

**Day 20 of Google's Advent of Agents**

**The "Sidecar" Pattern for Agents 🏍️**

The Agent-to-Agent (A2A) protocol relies on a strict format 📋 to ensure agents from different teams can talk to each other 🤝. But real-world complexity often requires unique data that isn't in the spec (e.g., billing_id 💳 or security_clearance 🔐).

**The Solution: A2A Extensions 🧩** Instead of forcing data into fields where it doesn't belong, A2A defines a dedicated extension field. Think of this like a "Sidecar" attached to your message 🏍️. It travels with the payload 📦, carrying custom dictionaries or objects, but doesn't alter the driver or the vehicle.

**The Golden Rule: Non-Breaking ✨** Extensions follow a strict backward-compatibility rule: **If you don't understand it, ignore it 🙈**. This allows you to upgrade agents 🆙 with new capabilities (like the "Secure Passport" below 🛂) without breaking communication with older agents that haven't been updated yet.

**Resources**:

- Check out the [A2A Extensions Sample](https://github.com/a2aproject/a2a-samples/tree/main/extensions/secure-passport/v1/samples/python?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day20)

## Code & Commands

### Get the Sample:

```shell
# Download the specific extensions sample
uvx agent-starter-pack create secure-auth-agent   -a adk_a2a_base   --extension secure-passport
```

### The Implementation: This snippet attaches a "Passport" extension. If the receiver supports it, they verify the signature. If not, they process the message as a standard request.

```python
from secure_passport_ext import CallerContext, A2AMessage, add_secure_passport, get_secure_passport

# 1. THE SENDER: Attaches the "Sidecar"
# We create a secure context with custom enterprise data
passport = CallerContext(
    client_id="a2a://travel-orchestrator.com",
    state={"tier": "Platinum", "billing_code": "US-123"},
    signature="valid-crypto-signature-123"
)

message = A2AMessage(type="task", content="Book flight")
# "Stamp" the message with the extension
add_secure_passport(message, passport)


# 2. THE RECEIVER: Inspects the "Sidecar"
# This function safely checks for the extension without crashing if missing
received_passport = get_secure_passport(message)

if received_passport and received_passport.is_verified:
    print(f"✅ Verified Platinum Request from: {received_passport.client_id}")
else: # Non-breaking fall-back behavior
    print(f"ℹ️ Standard processing (No auth extension found)")
```

## Resources & Links

- **[A2A Secure Passport Extension Sample](https://github.com/a2aproject/a2a-samples/tree/main/extensions/secure-passport/v1/samples/python?utm_source=adventofagents&utm_medium=markdown&utm_campaign=adventofagents_s1_2025&utm_content=day20)**
