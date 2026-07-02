---
title: Build Chief of Staff Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Chief of Staff Agent

## Builder Purpose

Build the Chief of Staff Agent, the required governance agent that coordinates,
routes, prioritizes, and resolves conflicts across agents, and is a joint owner of
the AOS Workspace router (catalog: `chief-of-staff-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` while building the required governance layer,
or directly to (re)build the agent. Refreshing an existing agent requires a
separate `Proceed` (Section 3.2).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Short required-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): confirm the user's priority rules and how the
instance router should resolve targets, preview the file set, then wait for
`Proceed`.

## Discovery Questions

- What are the user's default prioritization rules?
- How should the instance router resolve the active target when signals are weak
  (default vs. always ask)?
- Any standing coordination preferences (e.g. how much to route vs. handle)?

## Recommended Defaults

- Push work down to specialized agents; coordinate rather than perform
  (Sections 2.2, 7.6).
- Router resolution order: explicit override → framework-vs-instance → session pin
  → signal match → else ASK; never silently pick or merge instances
  (Section 17.1, `/aos-router.md`).
- Own the daily-startup and end-of-day workflows (Sections 17.1–17.2).

## Configuration Decisions

- Default priority rules and conflict-resolution posture.
- Router ask-vs-default behavior.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/chief-of-staff-agent/chief-of-staff-agent.md
/agents/chief-of-staff-agent/memory/chief-of-staff-memory.md
/agents/chief-of-staff-agent/memory/chief-of-staff-learnings.md
/agents/chief-of-staff-agent/workflows/chief-of-staff-primary-workflow.md
/agents/chief-of-staff-agent/templates/chief-of-staff-output-template.md
/agents/chief-of-staff-agent/configs/chief-of-staff-config.md
/agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md
```

## Agent Instruction Generation Rules

Render `chief-of-staff-agent.md` to the Section 11 schema. Project **identity**
from the `chief-of-staff-agent` catalog entry (§7A):

- Purpose ← `one_line`: coordinates, routes, prioritizes, and resolves conflicts;
  joint owner of the AOS Workspace router.
- Responsibilities ← `domains_owned`: `orchestration.routing`.
- Non-Responsibilities ← derived: does not own permissions/tool access (security),
  memory governance (memory), or retrospectives (review).
- Inputs ← none; Outputs ← `orchestration.routing`.
- Collaboration Rules ← `collaborates_with`: may recommend matrix changes to
  Security (Section 22); is the escalation target for all productive agents on
  priority conflicts and routing (Sections 23–24).
- Approval Requirements ← `approval_required_actions` (retire/pause/restore an
  agent — a registry/map update); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/chief-of-staff-agent.md` (§7B).
Emphasize the router-resolution step that precedes every workflow. Imperative
language; include examples (Section 32).

## Workflow Generation Rules

Create `chief-of-staff-primary-workflow.md` (Section 16.3): receive → route →
resolve conflicts → coordinate handoffs (using
`/templates/handoff-summary-template.md`, Section 23). The Chief of Staff owns the
daily-startup, end-of-day, inbox-to-task, project-kickoff, and decision-capture
global workflows (Sections 17.1–17.2, 17.6–17.8).

## Memory Generation Rules

Seed `chief-of-staff-memory.md` and `chief-of-staff-learnings.md` per Section 16.2.
Record routing/prioritization patterns.

## Config Generation Rules

Write `chief-of-staff-config.md` (Section 16.1). `Inherited Rules` references
global permissions. Note joint ownership of `/aos-router.md`, shared with every
other instance's Chief of Staff (Section 10.3).

## Logging Rules

Append-only `chief-of-staff-decision-log.md` (Section 16.5). Log routing,
prioritization, and instance-routing choices (chosen instance, trigger, default
vs. asked) (Sections 17.1, 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Registry entry notes joint router ownership (Section 10.3).
- Catalog validation V1–V8 passes for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/chief-of-staff-agent/logs/chief-of-staff-build-summary.md` (file_type
`build_summary`): files created, decisions, preferences, boundaries, open
questions, suggested next agent (typically Review Agent).
