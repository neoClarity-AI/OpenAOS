---
name: build-inbox-agent
description: "Add an Inbox / Communications Agent to an AOS instance — triages email and messages, drafts replies, and runs the inbox-to-task workflow. Use when adding this optional agent during setup, installing it later, or rebuilding the inbox or communications agent."
---


# Build Inbox / Communications Agent

## Builder Purpose

Build the **Inbox / Communications Agent**, an optional productive agent that triages incoming items and communications and drafts responses. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Inbox Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration. Batch, summarize, recommend, request `Proceed`.

## Discovery Questions

- Which channels/inboxes should the agent help with?
- What should be drafted automatically versus only when asked?
- Triage categories the user wants (urgent, waiting, FYI, archive)?
- How aggressively should items be promoted to tasks/projects/calendar?

## Recommended Defaults

- Drafting messages is allowed; **sending requires approval** (`Proceed`) per the tool access matrix (Sections 3.2, 22).
- Use the inbox-to-task workflow to promote items to tasks, projects, calendar items, memory, decisions, or archive (Section 17.6).
- Moving processed items to `/inbox/processed` is the single pre-authorized move (Sections 3.2, 17.6, 31); all other moves require approval.
- Feed the daily startup brief's processed-inbox summary (Section 17.1).

## Configuration Decisions

- Confirm send/publish tools are `Approval-required` in the matrix (Section 22).
- Confirm triage taxonomy and promotion thresholds.
- Confirm collaboration with Task, Calendar, and Project Manager agents.

## Files to Create

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

Generate `inbox-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it drafts but does not send without approval and does not own scheduling or task tracking. Include example requests.

## Workflow Generation Rules

Create `inbox-primary-workflow.md` (Section 16.3) implementing triage and the inbox-to-task promotion flow, with the `/inbox/processed` move as the only pre-authorized move and sending gated by `Proceed`.

## Memory Generation Rules

Create `inbox-memory.md` and `inbox-learnings.md` (Section 16.2). Store recurring senders, triage preferences, and draft styles; route sensitive details through approval (Section 20.3).

## Config Generation Rules

Create `inbox-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix (send = approval-required).

## Logging Rules

Create `inbox-decision-log.md` (Section 16.5). Log promotion decisions, approved sends, and triage rule changes.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Sending gated behind Proceed; drafting allowed.
[ ] Inbox-to-task promotion and /inbox/processed exception implemented correctly.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
