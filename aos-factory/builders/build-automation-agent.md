---
title: Build Automation Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Automation Agent

## Builder Purpose

Build the Automation Agent, an optional productive agent that owns automation and
tool-use: scripting, integrations, and recurring automated actions on behalf of
other agents (catalog: `automation-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26). Because this agent
operates tools, coordinate closely with Security, which owns the matrix
(Section 22).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools/integrations, approval
boundaries, collaboration; summarize; recommend defaults; preview; wait for
`Proceed`.

## Discovery Questions

- What recurring actions or integrations should be automated?
- Which tools are involved, and what is their matrix status?
- Confirm: side-effecting runs (send/publish/spend/share/affect others) require
  `Proceed`.

## Recommended Defaults

- Design → validate tool access against the matrix → run approved steps → report
  results and failures.
- New tools default to `Not configured` and may not be used until access is
  explicitly granted (Section 22); request changes from Security, never grant.
- Accept recurring-task handoffs from the Task Agent.

## Configuration Decisions

- Automations in scope; tools/integrations and their matrix status; approval
  boundaries.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/automation-agent/automation-agent.md
/agents/automation-agent/memory/automation-memory.md
/agents/automation-agent/memory/automation-learnings.md
/agents/automation-agent/workflows/automation-primary-workflow.md
/agents/automation-agent/templates/automation-output-template.md
/agents/automation-agent/configs/automation-config.md
/agents/automation-agent/logs/automation-decision-log.md
```

## Agent Instruction Generation Rules

Render `automation-agent.md` to the Section 11 schema. Project **identity** from
the `automation-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns automation and tool-use — scripting, integrations, and
  recurring automated actions on behalf of other agents.
- Responsibilities ← `domains_owned`: `automation`.
- Non-Responsibilities ← derived: does not track tasks or commitments (task).
- Inputs ← `task-tracking`; Outputs ← `automation`.
- Collaboration Rules ← `collaborates_with`: receives recurring-task handoffs from
  Task; escalates elevated/unclear tool access to Security and priority conflicts
  to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (run an automation that
  modifies files outside its own domain); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/automation-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `automation-primary-workflow.md` (Section 16.3): design an automation →
validate tool access against the matrix → run approved steps → report results and
failures.

## Memory Generation Rules

Seed `automation-memory.md` and `automation-learnings.md` per Section 16.2. Keep
automation definitions and reliability notes current.

## Config Generation Rules

Write `automation-config.md` (Section 16.1). `Tool Access` references the matrix:
elevated/scripted access = Approval-required; never restates or overrides matrix
grants (Section 22).

## Logging Rules

Append-only `automation-decision-log.md` (Section 16.5). Log tool-access requests,
approved runs, and failed actions affecting future behavior (Sections 19.3, 24).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- No use of `Not configured` tools; side-effecting runs gated by `Proceed`.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/automation-agent/logs/automation-build-summary.md` (file_type
`build_summary`).
