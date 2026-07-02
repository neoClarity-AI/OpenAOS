---
title: Build Calendar Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Calendar Agent

## Builder Purpose

Build the Calendar Agent, an optional productive agent that owns scheduling:
reading availability, proposing times, and creating or changing calendar events
under approval (catalog: `calendar-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, calendar tools, approval boundaries,
collaboration; summarize; recommend defaults; preview; wait for `Proceed`.

## Discovery Questions

- Which calendar(s), and what read scope is approved?
- Scheduling preferences (working hours, focus blocks, buffers)?
- How should conflicts and double-bookings be handled?
- Confirm: all calendar modifications and any change involving other people
  require `Proceed`.

## Recommended Defaults

- Read within approved scope; propose times and focus blocks autonomously; apply
  create/move/delete only after `Proceed`, with extra care for events involving
  other people (Section 3.2).
- Surface upcoming commitments in the daily startup brief (Section 17.1).

## Configuration Decisions

- Calendar sources and read scope; scheduling preferences; conflict rules.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/calendar-agent/calendar-agent.md
/agents/calendar-agent/memory/calendar-memory.md
/agents/calendar-agent/memory/calendar-learnings.md
/agents/calendar-agent/workflows/calendar-primary-workflow.md
/agents/calendar-agent/templates/calendar-output-template.md
/agents/calendar-agent/configs/calendar-config.md
/agents/calendar-agent/logs/calendar-decision-log.md
```

## Agent Instruction Generation Rules

Render `calendar-agent.md` to the Section 11 schema. Project **identity** from the
`calendar-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns scheduling — reading availability, proposing times,
  and creating/changing events under approval.
- Responsibilities ← `domains_owned`: `scheduling`.
- Non-Responsibilities ← derived: does not triage/draft communications (inbox) or
  own task tracking (task).
- Inputs ← `communications.triage`, `task-tracking`; Outputs ← `scheduling`.
- Collaboration Rules ← `collaborates_with`: receives event/booking handoffs from
  Inbox and time-blocking handoffs from Task; escalates competing time demands to
  Chief of Staff.
- Approval Requirements ← `approval_required_actions` (create/move/delete an event;
  any change involving other people); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/calendar-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `calendar-primary-workflow.md` (Section 16.3): review the calendar → propose
scheduling → apply approved changes (modify gated by `Proceed`).

## Memory Generation Rules

Seed `calendar-memory.md` and `calendar-learnings.md` per Section 16.2. Track
scheduling preferences and recurring commitments.

## Config Generation Rules

Write `calendar-config.md` (Section 16.1). `Tool Access` references the matrix:
calendar read = Allowed; calendar modify = Approval-required, especially with
other people (Section 22).

## Logging Rules

Append-only `calendar-decision-log.md` (Section 16.5). Log approved calendar
changes and escalations (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- No unapproved calendar-modify path; other-people rule honored.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/calendar-agent/logs/calendar-build-summary.md` (file_type
`build_summary`).
