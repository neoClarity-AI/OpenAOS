---
title: User Profile
file_type: memory_store
schema_version: 1.0.0
builder_version: 1.0.0
created_date: 2026-06-04
last_updated: 2026-06-05
status: active
owner: memory-agent
---

# User Profile

Durable facts about the user that help agents assist well. Maintained by the Memory Agent; sensitive entries require explicit approval.

- **Name:** Martin
- **Email:** martin@neoclarity.ai
- **AOS purpose:** Personal
- **Autonomy preference:** Balanced

## Context
_(Add role, goals, constraints, and recurring contexts as they surface.)_

## Routing signals (personal-aos)
Used by `/aos-router.md` to distinguish this instance from `work-aos`, which shares the martin@neoclarity.ai inbox. Inbox alone is not a signal — route on sender/alias and intent.

- **Topics:** family/friends, personal admin, community/newsletter activity.
- **Senders / aliases:** dan@danner.org threads; aliases `m25@`, `m26+*`, `martin+*`.
- **Projects:** kept current in `/memory/projects.md` — the router matches `personal-aos/projects` names.
- **Note:** `work-aos` is the system default; personal routing needs a positive personal signal or an explicit override.
