---
title: Build Task / Commitment Agent
file_type: agent_builder
builder_version: 1.0.0
schema_version: 1.0.0
created_date: 2026-06-03
last_updated: 2026-06-03
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Task / Commitment Agent

## Builder Purpose

Build the **Task / Commitment Agent**, an optional productive agent that captures, tracks, and surfaces tasks, commitments, and deadlines. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Task Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- How does the user think about tasks (lists, priorities, due dates, contexts)?
- What counts as a commitment worth tracking?
- How should overdue or at-risk items be surfaced?
- Which sources feed tasks (inbox, projects, calendar)?

## Recommended Defaults

- Maintain a structured task list with priority, due date, and source.
- Accept promotions from the inbox-to-task workflow (Section 17.6).
- Surface today's and at-risk items in the daily startup brief (Section 17.1) and follow-ups in weekly review (Section 17.3).
- Creating and updating task files is Level 1 safe; deleting/overwriting requires approval.

## Configuration Decisions

- Confirm task data model and prioritization scheme.
- Confirm collaboration with Inbox, Calendar, and Project Manager agents.
- Confirm what task data is memory-worthy.

## Files to Create

```text
/agents/task-agent/task-agent.md
/agents/task-agent/memory/task-memory.md
/agents/task-agent/memory/task-learnings.md
/agents/task-agent/workflows/task-primary-workflow.md
/agents/task-agent/templates/task-output-template.md
/agents/task-agent/configs/task-config.md
/agents/task-agent/logs/task-decision-log.md
```

## Agent Instruction Generation Rules

Generate `task-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it does not own scheduling (Calendar), project structure (Project Manager), or routing (Chief of Staff). Include example requests.

## Workflow Generation Rules

Create `task-primary-workflow.md` (Section 16.3) for capturing, prioritizing, and reviewing tasks and surfacing at-risk commitments.

## Memory Generation Rules

Create `task-memory.md` and `task-learnings.md` (Section 16.2). Store recurring commitments and prioritization preferences.

## Config Generation Rules

Create `task-config.md` (Section 16.1) referencing global permissions and the tool access matrix.

## Logging Rules

Create `task-decision-log.md` (Section 16.5). Log prioritization-rule changes and significant commitment decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with Non-Responsibilities and examples.
[ ] Promotion intake from inbox-to-task defined.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
