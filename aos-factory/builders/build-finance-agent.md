---
title: Build Finance / Admin Agent
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

# Build Finance / Admin Agent

## Builder Purpose

Build the **Finance / Admin Agent**, an optional productive agent that helps with budgeting, tracking, and administrative logistics. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Finance Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- What financial or admin areas should the agent help with (budgets, bills, records)?
- What information is in scope, and how sensitive is it?
- What reporting cadence is useful?
- What absolutely requires approval (anything involving spending)?

## Recommended Defaults

- Tracking, summarizing, and drafting are Level 1 safe; **spending money is always approval-required** and never autonomous (Sections 3.2, 22).
- Treat financial details as sensitive; storage of sensitive specifics requires explicit approval (Section 20.3).
- Produce periodic summaries; surface admin deadlines in reviews.

## Configuration Decisions

- Confirm spend-related tools are `Approval-required` or `Prohibited` in the matrix (Section 22).
- Confirm sensitivity boundaries with the Security and Memory agents.
- Confirm reporting templates and cadence.

## Files to Create

```text
/agents/finance-agent/finance-agent.md
/agents/finance-agent/memory/finance-memory.md
/agents/finance-agent/memory/finance-learnings.md
/agents/finance-agent/workflows/finance-primary-workflow.md
/agents/finance-agent/templates/finance-output-template.md
/agents/finance-agent/configs/finance-config.md
/agents/finance-agent/logs/finance-decision-log.md
```

## Agent Instruction Generation Rules

Generate `finance-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must stress that it never spends money autonomously, gives no formal financial advice, and treats financial data as sensitive. Include example requests.

## Workflow Generation Rules

Create `finance-primary-workflow.md` (Section 16.3) for tracking, summarizing, and surfacing admin deadlines, with any spend action gated by `Proceed`.

## Memory Generation Rules

Create `finance-memory.md` and `finance-learnings.md` (Section 16.2). Apply sensitive-entry approval for financial specifics (Section 20.3).

## Config Generation Rules

Create `finance-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix (spend = approval-required/prohibited).

## Logging Rules

Create `finance-decision-log.md` (Section 16.5). Log approved financial actions and admin decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Spending always gated behind Proceed; no autonomous spend.
[ ] Sensitive-data handling documented.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
