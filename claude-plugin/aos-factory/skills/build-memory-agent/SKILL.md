---
name: build-memory-agent
description: "Build the Memory Agent, the required governance agent that owns shared memory structure, memory hygiene, preference capture, and cross-agent memory routing. Use when standing up an AOS or later via 'Build the Memory Agent'."
---

# Build Memory Agent

## Builder Purpose

Build the Memory Agent, the required governance agent that owns shared memory
structure, memory hygiene, preference capture, and cross-agent memory routing
(catalog: `memory-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` while building the required governance layer,
or directly to (re)build the Memory Agent. Refreshing an existing agent requires a
separate `Proceed` (Section 3.2).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed` (Section 3.1). Short required-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): confirm what durable facts/preferences to seed and
any sensitivity concerns, preview the file set, then wait for `Proceed`.

## Discovery Questions

- Any durable user facts or preferences to seed the global memory files with?
- Any categories the user considers sensitive (require approval before storage)?
- Preferred review cadence beyond the default weekly-light / monthly-deep?

## Recommended Defaults

- Use the Section 20.1 global memory files as-is.
- Lightweight weekly review + deeper monthly review (Sections 20.3, 17.9).
- Keep `/memory/agent-learnings-index.md` a routing map, not a dump (Section 6.1).

## Configuration Decisions

- Sensitivity categories requiring approval.
- Which global memory files to seed vs. leave empty.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/memory-agent/memory-agent.md
/agents/memory-agent/memory/memory-memory.md
/agents/memory-agent/memory/memory-learnings.md
/agents/memory-agent/workflows/memory-primary-workflow.md
/agents/memory-agent/templates/memory-output-template.md
/agents/memory-agent/configs/memory-config.md
/agents/memory-agent/logs/memory-decision-log.md
```

The Memory Agent maintains the global memory files (`/memory/*.md`), created by
`build-aos.md`.

## Agent Instruction Generation Rules

Render `memory-agent.md` to the Section 11 schema. Project **identity** from the
`memory-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns shared memory structure, hygiene, preference capture,
  and cross-agent memory routing.
- Responsibilities ← `domains_owned`: `memory.governance`.
- Non-Responsibilities ← derived: does not orchestrate (chief-of-staff), own
  permissions/tool access (security), or run retrospectives (review).
- Inputs ← none; Outputs ← `memory.governance`.
- Collaboration Rules ← `collaborates_with`: receives deeper monthly
  memory-hygiene support from Review (Section 17.9); escalates sensitive/privacy
  questions to Security (Section 24).
- Approval Requirements ← `approval_required_actions` (archive or delete a memory
  entry); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/memory-agent.md` (§7B),
tailored with instance choices. Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `memory-primary-workflow.md` (Section 16.3): capture → classify → route →
review. The Memory Agent is primary owner of the global
`/workflows/memory-review-workflow.md` (Section 17.9), with Review Agent support.

## Memory Generation Rules

Seed `memory-memory.md` and `memory-learnings.md` per Section 16.2. Enforce the
Section 20.3 governance rules: store only durable, useful, relevant items with the
standard fields (Type, Summary, Source, Confidence, Owner, Review Date, Notes);
never silently delete stale memory.

## Config Generation Rules

Write `memory-config.md` (Section 16.1). `Inherited Rules` references
`/configs/global-permissions.md`; `Memory Access` states the agent's routing
authority across global and agent memory (Section 20.2).

## Logging Rules

Append-only `memory-decision-log.md` (Section 16.5). Log routing decisions,
sensitivity approvals, and hygiene actions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Global memory files present and correctly bounded (Section 20.2); learnings
  index is a routing map, not a dump.
- Catalog validation V1–V8 passes for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/memory-agent/logs/memory-build-summary.md` (file_type `build_summary`):
files created, key decisions, preferences captured, boundaries, open questions,
suggested next agent (typically Chief of Staff Agent).
