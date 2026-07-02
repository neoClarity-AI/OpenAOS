---
title: Build Review Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Review Agent

## Builder Purpose

Build the Review Agent, the required governance agent that owns retrospectives,
system improvement, the review cadence, decision audits, AOS refinement, the AOS
User Guide, and `aos_version` reconciliation (catalog: `review-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` while building the required governance layer,
or directly to (re)build the agent. Refreshing an existing agent requires a
separate `Proceed` (Section 3.2).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Short required-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): confirm review cadence preferences, preview the file
set, then wait for `Proceed`.

## Discovery Questions

- Preferred timing for weekly / monthly / quarterly reviews?
- Any areas the user especially wants audited (memory, permissions, structure)?

## Recommended Defaults

- Run the standard cadence and review questions (Section 25).
- Regenerate `/docs/aos-user-guide.html` during the monthly review, preserving its
  embedded Change Log (Sections 16.6, 17.4).
- Reconcile `aos_version` against `/logs/change-log.md` monthly (Section 14.3.1).

## Configuration Decisions

- Review scheduling.
- Audit emphasis areas.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/review-agent/review-agent.md
/agents/review-agent/memory/review-memory.md
/agents/review-agent/memory/review-learnings.md
/agents/review-agent/workflows/review-primary-workflow.md
/agents/review-agent/templates/review-output-template.md
/agents/review-agent/configs/review-config.md
/agents/review-agent/logs/review-decision-log.md
```

The Review Agent owns `/docs/aos-user-guide.html` (created by `build-aos.md`,
regenerated monthly).

## Agent Instruction Generation Rules

Render `review-agent.md` to the Section 11 schema. Project **identity** from the
`review-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns retrospectives, system improvement, the review
  cadence, decision audits, AOS refinement, and the AOS User Guide.
- Responsibilities ← `domains_owned`: `review.retrospective`.
- Non-Responsibilities ← derived: does not orchestrate (chief-of-staff), own
  permissions/tool access (security), or own memory governance (memory).
- Inputs ← none; Outputs ← `review.retrospective`.
- Collaboration Rules ← `collaborates_with`: may recommend matrix changes to
  Security (Section 22); supports Memory on deeper monthly hygiene (Section 17.9).
- Approval Requirements ← none required beyond globals; `pre_authorized_actions`:
  regenerate the user guide during monthly review (Sections 16.6, 17.4). Per the
  drift invariant (Section 14.8) it refines only data files and projections, never
  framework-derived definition files.

Project **narrative** sections from `agent-profiles/review-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `review-primary-workflow.md` (Section 16.3): run a review → capture findings
→ propose improvements (`Proceed`-gated where they change files). The Review Agent
is primary owner of the weekly, monthly, and quarterly review workflows
(Sections 17.3–17.5) and supports the memory-review workflow (Section 17.9).

## Memory Generation Rules

Seed `review-memory.md` and `review-learnings.md` per Section 16.2. Record review
outcomes and system-improvement patterns.

## Config Generation Rules

Write `review-config.md` (Section 16.1). `Inherited Rules` references global
permissions. Note ownership of the user guide and `aos_version` reconciliation.

## Logging Rules

Append-only `review-decision-log.md` (Section 16.5). Log review outcomes, audit
findings, and improvement decisions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Review workflows owned; user-guide regeneration and `aos_version` reconciliation
  wired in (Sections 16.6, 14.3.1).
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/review-agent/logs/review-build-summary.md` (file_type `build_summary`):
files created, decisions, preferences, boundaries, open questions, and suggested
next step (select at least one optional productive agent, Section 7.2).
