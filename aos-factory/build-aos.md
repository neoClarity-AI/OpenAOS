---
title: Build AOS (Entry)
file_type: builder_entry
spec_version: 2.3.3
created_date: 2026-07-13
last_updated: 2026-07-13
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---
# Build AOS — Entry Pointer

This is the root entry point for standing up an Agentic Operating System (AOS)
instance. It is a short pointer only (design spec §8.3); it does not repeat the
builder logic.

To build an AOS, run the master builder:

```text
/builders/build-aos.md
```

That builder runs the interactive setup interview (`/aos-interviews.md`, §7C),
creates the AOS instance as a sibling folder inside the AOS Workspace (§4.1),
builds the five required governance agents plus at least one optional productive
agent, and produces the AOS setup summary. Nothing is written until the user
types exactly `Proceed` (§3.1).

To add a single agent to an existing instance later, run the generic build
engine `/builders/build-agent.md` (for example, "Build the Research Agent";
§9.4).
