---
name: build-calendar-agent
description: "Add a Calendar / Scheduling Agent to an AOS instance — manages scheduling, meetings, and time blocking. Use when adding this optional agent during setup, installing it later, or rebuilding the calendar or scheduling agent."
---


# Build Calendar / Scheduling Agent

## Builder Purpose

Build the **Calendar / Scheduling Agent**, an optional productive agent that helps the user manage time, scheduling, and calendar logistics. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Calendar Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- Which calendars should the agent read and help manage?
- Default working hours, focus blocks, and scheduling preferences?
- How should conflicts and double-bookings be handled?
- What requires approval before changing (especially events involving other people)?

## Recommended Defaults

- Calendar read is allowed within approved scope; **calendar modify is approval-required**, especially when other people are involved (Sections 3.2, 22).
- Propose schedules and focus blocks autonomously; apply changes only after `Proceed`.
- Surface upcoming commitments in the daily startup brief (Section 17.1).

## Configuration Decisions

- Confirm calendar read/modify access levels in the matrix (Section 22).
- Confirm rules for events involving other people (Section 3.2).
- Confirm collaboration with Inbox and Task agents.

## Files to Create

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

Generate `calendar-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it does not modify others' calendars or send invitations without approval. Include example requests.

## Workflow Generation Rules

Create `calendar-primary-workflow.md` (Section 16.3) for reviewing the calendar, proposing scheduling, and applying approved changes (modify gated by `Proceed`).

## Memory Generation Rules

Create `calendar-memory.md` and `calendar-learnings.md` (Section 16.2). Store scheduling preferences and recurring commitments.

## Config Generation Rules

Create `calendar-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix (modify = approval-required).

## Logging Rules

Create `calendar-decision-log.md` (Section 16.5). Log approved calendar changes and scheduling-rule decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Calendar modify gated behind Proceed; read allowed within scope.
[ ] Other-people rule documented.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
