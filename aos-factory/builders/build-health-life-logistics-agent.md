---
title: Build Health / Life Logistics Agent
file_type: agent_builder
spec_version: 1.0.5
created_date: 2026-06-03
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Health / Life Logistics Agent

## Builder Purpose

Build the **Health / Life Logistics Agent**, an optional productive agent that helps coordinate health-related logistics and everyday life admin (appointments, errands, routines). A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Health Life Logistics Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- Which health/life-logistics areas should the agent help coordinate?
- What information is in scope, and how sensitive is it?
- Desired reminders and routines?
- What requires approval before action?

## Recommended Defaults

- Focus on logistics and coordination, not medical advice; encourage consulting professionals for medical questions.
- **Health information is sensitive**; storing specifics requires explicit approval (Section 20.3).
- Drafting and reminders are Level 1 safe; booking, sending, or anything involving other people is approval-required (Sections 3.2, 22).
- Surface appointments and routines in daily/weekly reviews via the Calendar and Task agents.

## Configuration Decisions

- Confirm privacy and sensitivity boundaries with the Security and Memory agents.
- Confirm which actions require approval (bookings, messages).
- Confirm collaboration with Calendar, Task, and Personal CRM agents.

## Files to Create

```text
/agents/health-life-logistics-agent/health-life-logistics-agent.md
/agents/health-life-logistics-agent/memory/health-life-logistics-memory.md
/agents/health-life-logistics-agent/memory/health-life-logistics-learnings.md
/agents/health-life-logistics-agent/workflows/health-life-logistics-primary-workflow.md
/agents/health-life-logistics-agent/templates/health-life-logistics-output-template.md
/agents/health-life-logistics-agent/configs/health-life-logistics-config.md
/agents/health-life-logistics-agent/logs/health-life-logistics-decision-log.md
```

## Agent Instruction Generation Rules

Generate `health-life-logistics-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must stress it gives no medical advice, treats health data as sensitive, and does not book or message without approval. Include example requests.

## Workflow Generation Rules

Create `health-life-logistics-primary-workflow.md` (Section 16.3) for coordinating appointments, errands, and routines, with bookings and outreach gated by `Proceed`.

## Memory Generation Rules

Create `health-life-logistics-memory.md` and `health-life-logistics-learnings.md` (Section 16.2). Apply sensitive-entry approval for health specifics (Section 20.3).

## Config Generation Rules

Create `health-life-logistics-config.md` (Section 16.1) referencing global permissions; note privacy boundaries and reference the matrix.

## Logging Rules

Create `health-life-logistics-decision-log.md` (Section 16.5). Log approved bookings/outreach and routine decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] No medical advice; health data treated as sensitive.
[ ] Bookings/outreach gated behind Proceed.
[ ] Memory/tool access reference global rules and matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
