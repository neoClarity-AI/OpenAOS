---
title: Build Writing / Content Agent
file_type: agent_builder
spec_version: 1.1.0
created_date: 2026-06-03
last_updated: 2026-06-25
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Writing / Content Agent

## Builder Purpose

Build the **Writing / Content Agent**, an optional productive agent that drafts, edits, and refines written content. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Writing Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- What kinds of content will the agent produce, and for which audiences?
- Voice, tone, and formatting preferences?
- Where do drafts live, and what is the review process?
- What publishing or sending requires approval?

## Recommended Defaults

- Drafting and editing are Level 1 safe; **publishing or sending content is approval-required** (`Proceed`) per Sections 3.2 and 22.
- Capture durable voice/style preferences in memory (and in `/memory/preferences.md` when global).
- Take research input from the Research Agent; do not collect sources itself when Research is installed (Section 23).

## Configuration Decisions

- Confirm publish/send tools are `Approval-required` in the matrix (Section 22).
- Confirm voice/tone/format conventions and output templates.
- Confirm collaboration with Research, Learning, and Inbox agents.

## Files to Create

```text
/agents/writing-agent/writing-agent.md
/agents/writing-agent/memory/writing-memory.md
/agents/writing-agent/memory/writing-learnings.md
/agents/writing-agent/workflows/writing-primary-workflow.md
/agents/writing-agent/templates/writing-output-template.md
/agents/writing-agent/configs/writing-config.md
/agents/writing-agent/logs/writing-decision-log.md
```

## Agent Instruction Generation Rules

Generate `writing-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it drafts but does not publish/send without approval and does not collect primary research. Include example requests.

## Workflow Generation Rules

Create `writing-primary-workflow.md` (Section 16.3) for brief intake, drafting, revision, and an approval gate before any publish/send.

## Memory Generation Rules

Create `writing-memory.md` and `writing-learnings.md` (Section 16.2). Store voice/style preferences and reusable patterns.

## Config Generation Rules

Create `writing-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix (publish/send = approval-required).

## Logging Rules

Create `writing-decision-log.md` (Section 16.5). Log style decisions and approved publications.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Publishing/sending gated behind Proceed; drafting allowed.
[ ] Voice/style conventions captured.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
