---
title: Daily Startup Workflow
file_type: workflow
schema_version: 1.0.0
builder_version: 1.0.0
created_date: 2026-06-04
last_updated: 2026-06-05
status: active
---

# Daily Startup Workflow

Owned (user-facing) by the Chief of Staff Agent. Produces the morning brief.

1. **Resolve the active instance first.** Before gathering any inputs, resolve the target via `/aos-router.md` (explicit override → framework-vs-instance → session pin → signal match → else ASK). Run the brief against exactly one resolved instance; for a cross-instance request, run each separately with labeled output and never blend instance memory. State the resolved target on the first line of the brief (e.g. `**[personal-aos]** Daily Brief — …`).
2. Chief of Staff gathers inputs from installed agents:
   - **Inbox:** summary of processed items and anything waiting.
   - **Calendar:** today's commitments and focus blocks.
   - **Task:** items due today and at-risk commitments.
   - **Project Manager:** projects needing attention.
3. Assemble a single prioritized brief.
4. Surface decisions needing the user and any Level 2 actions ready for `Proceed`.
5. Log notable routing/prioritization choices, including the instance-routing choice.
