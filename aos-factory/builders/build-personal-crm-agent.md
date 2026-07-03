---
title: Build Personal CRM Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Personal CRM Agent

## Builder Purpose

Build the Personal CRM Agent, an optional productive agent that owns contacts:
relationship context, communication preferences, and collaboration notes about
people (catalog: `personal-crm-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26). Handle
person-related data with the Section 20.3 privacy rules.

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output preferences, approval
boundaries, collaboration, privacy sensitivity; summarize; recommend defaults;
preview; wait for `Proceed`.

## Discovery Questions

- Which relationships to track, and what context matters?
- What counts as sensitive (requires approval before storage)?
- Follow-up cadence and outreach drafting preferences?

## Recommended Defaults

- Maintain relationship context in coordination with `/memory/people.md`
  boundaries (Section 20.2).
- Surface follow-ups during daily and weekly reviews; draft outreach but never send
  without `Proceed`.
- Avoid third-party private information; sensitive-entry approval coordinated with
  Security + Memory (Section 20.3).

## Configuration Decisions

- Relationships in scope; sensitivity categories; follow-up cadence.

## Files to Create

Standard agent file set (Section 5.1):

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

Render `personal-crm-agent.md` to the Section 11 schema. Project **identity** from
the `personal-crm-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns contacts — relationship context, communication
  preferences, and collaboration notes about people.
- Responsibilities ← `domains_owned`: `contacts`.
- Non-Responsibilities ← derived: does not coordinate/own projects
  (project-manager).
- Inputs ← `project-coordination`; Outputs ← `contacts`.
- Collaboration Rules ← `collaborates_with`: receives external-stakeholder handoffs
  from Project Manager; escalates privacy questions to Security (with Memory) and
  priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (share private contact
  information externally); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/personal-crm-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `personal-crm-primary-workflow.md` (Section 16.3): capture relationship
context → schedule follow-ups → draft outreach, with sending gated by `Proceed`.

## Memory Generation Rules

Seed `personal-crm-memory.md` and `personal-crm-learnings.md` per Section 16.2.
Keep relationship context current within `/memory/people.md` boundaries; apply the
sensitive-entry approval rule (Section 20.3).

## Config Generation Rules

Write `personal-crm-config.md` (Section 16.1). `Inherited Rules` references global
permissions; note that storing sensitive personal details and sharing/sending
private information are `Proceed`-gated (Section 20.3).

## Logging Rules

Append-only `personal-crm-decision-log.md` (Section 16.5). Log sensitivity
approvals and outreach approvals (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Privacy boundaries and sensitive-data approval honored; no unapproved
  share/send.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/personal-crm-agent/logs/personal-crm-build-summary.md` (file_type
`build_summary`).
