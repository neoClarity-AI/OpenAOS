---
title: Build Inbox Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Inbox Agent

## Builder Purpose

Build the Inbox Agent, an optional productive agent that triages incoming
communications and drafts responses, promoting items into other agents' domains
(catalog: `inbox-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output/drafting preferences,
approval boundaries, collaboration; summarize; recommend defaults; preview; wait
for `Proceed`.

## Discovery Questions

- What sources feed the inbox, and what triage taxonomy does the user use
  (urgent / waiting / FYI / archive)?
- Should the agent draft replies automatically, and in what voice?
- Which promotions should be aggressive vs. conservative?
- What sending/publishing must always require `Proceed`?

## Recommended Defaults

- Triage → draft (where configured) → promote via the inbox-to-task workflow
  (Section 17.6) → move processed items to `/inbox/processed` (the single
  pre-authorized move).
- Drafting autonomous; sending/publishing gated by `Proceed` (Sections 3.2, 22).
- Feed the daily startup brief's processed-inbox summary (Section 17.1).

## Configuration Decisions

- Triage taxonomy; drafting voice; promotion thresholds; send-approval rules.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/inbox-agent/inbox-agent.md
/agents/inbox-agent/memory/inbox-memory.md
/agents/inbox-agent/memory/inbox-learnings.md
/agents/inbox-agent/workflows/inbox-primary-workflow.md
/agents/inbox-agent/templates/inbox-output-template.md
/agents/inbox-agent/configs/inbox-config.md
/agents/inbox-agent/logs/inbox-decision-log.md
```

## Agent Instruction Generation Rules

Render `inbox-agent.md` to the Section 11 schema. Project **identity** from the
`inbox-agent` catalog entry (§7A):

- Purpose ← `one_line`: triages incoming communications and drafts responses;
  promotes items into other domains but owns none of them.
- Responsibilities ← `domains_owned`: `communications.triage`,
  `communications.drafting`.
- Non-Responsibilities ← derived: does not schedule (calendar), track tasks
  (task), or coordinate projects (project-manager).
- Inputs ← none; Outputs ← `communications.triage`, `communications.drafting`.
- Collaboration Rules ← `collaborates_with`: hands off to Task (commitments),
  Calendar (events), Project Manager (project items); escalates unclear ownership
  to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (send or publish any
  message) + `pre_authorized_actions` (move processed items to `/inbox/processed`,
  the sole pre-authorized move, Sections 3.2, 17.6).

Project **narrative** sections from `agent-profiles/inbox-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `inbox-primary-workflow.md` (Section 16.3): triage → inbox-to-task
promotion; the `/inbox/processed` move is pre-authorized; sending is gated by
`Proceed`. Supports the global inbox-to-task workflow (Section 17.6).

## Memory Generation Rules

Seed `inbox-memory.md` and `inbox-learnings.md` per Section 16.2. Track
recurring-sender and triage preferences; route sensitive details through approval
(Section 20.3).

## Config Generation Rules

Write `inbox-config.md` (Section 16.1). `Tool Access` references the matrix:
email/message send = Approval-required; read/draft = Allowed (Section 22).

## Logging Rules

Append-only `inbox-decision-log.md` (Section 16.5). Log promotions, sends
(approved), and escalations (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- `/inbox/processed` move pre-authorized; no unapproved send path.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/inbox-agent/logs/inbox-build-summary.md` (file_type `build_summary`).
