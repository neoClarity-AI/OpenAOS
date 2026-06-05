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
- **AOS purpose:** Professional / work
- **Autonomy preference:** Balanced

## Context
_(Add role, goals, constraints, and recurring contexts as they surface.)_

## Routing signals (work-aos)
Used by `/aos-router.md` to distinguish this instance from `personal-aos`, which shares the martin@neoclarity.ai inbox. Inbox alone is not a signal — route on sender/alias and intent.

- **Topics:** clients, the company, billing/invoicing, hiring, work projects in `work-aos/projects`.
- **Sender domains / aliases:** work-tied recipients and aliases _(enumerate the specific work domains and aliases as they surface)_.
- **Projects:** kept current in `/memory/projects.md` — the router matches `work-aos/projects` names.
- **Default:** `work-aos` is the default instance when signals are otherwise balanced.
