---
title: Build Personal CRM Agent
file_type: agent_builder
spec_version: 1.0.5
created_date: 2026-06-03
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Personal CRM Agent

## Builder Purpose

Build the **Personal CRM Agent**, an optional productive agent that helps the user maintain relationships — tracking people, context, and follow-ups. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Personal CRM Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- Which relationships does the user want to nurture, and how?
- What context is worth remembering about people (roles, preferences, history)?
- Desired follow-up cadence and reminders?
- Sensitivity boundaries for personal details?

## Recommended Defaults

- Maintain relationship context in coordination with `/memory/people.md` boundaries (Section 20.2).
- **Sensitive personal details require explicit approval before storage**; avoid third-party private information (Section 20.3).
- Surface follow-ups during daily/weekly reviews.
- Drafting outreach is allowed; sending is approval-required (Sections 3.2, 22).

## Configuration Decisions

- Confirm privacy boundaries and what counts as sensitive (with the Security and Memory agents).
- Confirm follow-up cadence and reminder routing (Task/Calendar agents).
- Confirm send tools are approval-required in the matrix.

## Files to Create

```text
/agents/personal-crm-agent/personal-crm-agent.md
/agents/personal-crm-agent/memory/personal-crm-memory.md
/agents/personal-crm-agent/memory/personal-crm-learnings.md
/agents/personal-crm-agent/workflows/personal-crm-primary-workflow.md
/agents/personal-crm-agent/templates/personal-crm-output-template.md
/agents/personal-crm-agent/configs/personal-crm-config.md
/agents/personal-crm-agent/logs/personal-crm-decision-log.md
```

## Agent Instruction Generation Rules

Generate `personal-crm-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must stress privacy limits, the sensitive-data approval rule, and that it does not send messages without approval. Include example requests.

## Workflow Generation Rules

Create `personal-crm-primary-workflow.md` (Section 16.3) for capturing relationship context, scheduling follow-ups, and drafting outreach with sending gated by `Proceed`.

## Memory Generation Rules

Create `personal-crm-memory.md` and `personal-crm-learnings.md` (Section 16.2). Apply sensitive-entry approval; avoid storing third-party private information (Section 20.3).

## Config Generation Rules

Create `personal-crm-config.md` (Section 16.1) referencing global permissions; `Memory Access` and `Tool Access` note privacy boundaries and reference the matrix.

## Logging Rules

Create `personal-crm-decision-log.md` (Section 16.5). Log privacy decisions and approved outreach.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Sensitive-data approval and privacy boundaries documented.
[ ] Sending gated behind Proceed.
[ ] Memory/tool access reference global rules and matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
