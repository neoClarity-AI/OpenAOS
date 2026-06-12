---
title: Build Review / Reflection Agent
file_type: agent_builder
spec_version: 1.0.5
created_date: 2026-06-03
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Review / Reflection Agent

## Builder Purpose

Build the **Review / Reflection Agent**, a required governance agent. It owns retrospectives, system improvement, weekly reviews, decision audits, AOS refinement, the AOS User Guide (`/docs/aos-user-guide.html`), and the instance version (`aos_version`). It regenerates the guide during the monthly review and reconciles `aos_version` then (Sections 7.4, 14.3.1, 16.6, 17.4). Standardized purpose, short interview.

## When to Use This Builder

During initial AOS setup (via `/builders/build-aos.md`) or when restoring or rebuilding the Review / Reflection Agent.

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Short batch interview (Section 9.1).

## Discovery Questions

- Preferred depth and timing for weekly, monthly, and quarterly reviews?
- What signals matter most to the user (stale projects, loose ends, memory hygiene, misalignment)?
- Any reporting format preferences for review outputs?

## Recommended Defaults

- Primary owner of the weekly review (Section 17.3) and the monthly review, including the AOS User Guide regeneration (Section 17.4).
- Owns and reconciles `aos_version` in `/aos-manifest.md`: reconciles against `/logs/change-log.md` at the monthly review and verifies it in the completeness audit; breaking/MAJOR bumps are applied at the time of change (Section 14.3.1). The triggering event is logged by the agent that made the change (Chief of Staff coordinating).
- Supports the Memory Agent on the memory-review workflow (Section 17.9).
- Audits generated files for completeness and consistency (Section 27).
- Regenerates the AOS User Guide as a projection (Sections 14.8, 16.6) rather than hand-editing prose; per the drift invariant (Section 14.8) it does not modify framework-derived definition files.
- Review questions follow Section 25 (weekly: "What needs follow-up soon?"; monthly: "What is stale, misplaced, or structurally messy?"; quarterly: "Is the whole system still aimed at the right goals?").

## Configuration Decisions

- Confirm ownership of `/docs/aos-user-guide.html` (regenerated monthly as a projection) and of `aos_version` reconciliation.
- Confirm audit scope (completeness and consistency) versus Security (permissions) and Memory (routing) audits.
- Confirm the user guide skeleton (Section 16.6) is used when regenerating the guide, and that its embedded Change Log is preserved as the data input.

## Files to Create

```text
/agents/review-agent/review-agent.md
/agents/review-agent/memory/review-memory.md
/agents/review-agent/memory/review-learnings.md
/agents/review-agent/workflows/review-primary-workflow.md
/agents/review-agent/templates/review-output-template.md
/agents/review-agent/configs/review-config.md
/agents/review-agent/logs/review-decision-log.md
```

## Agent Instruction Generation Rules

Generate `review-agent.md` per Section 11 with `agent_instruction` frontmatter. Emphasize Non-Responsibilities (it reviews and refines; it does not own day-to-day domain work or coordination, and per Section 14.8 it does not modify framework-derived definition files). Document ownership of weekly/monthly/quarterly reviews, completeness audits, the AOS User Guide (regenerated as a projection), and `aos_version` reconciliation (Section 14.3.1).

## Workflow Generation Rules

Create `review-primary-workflow.md` (Section 16.3) covering how a review is run, findings captured, and improvements proposed (each gated by `Proceed` where it would change files). Connect to the global weekly, monthly, and quarterly review workflows.

## Memory Generation Rules

Create `review-memory.md` and `review-learnings.md` (Section 16.2). Store recurring review findings and improvement patterns.

## Config Generation Rules

Create `review-config.md` (Section 16.1) referencing global permissions and the tool access matrix.

## Logging Rules

Create `review-decision-log.md` (Section 16.5). Log review outcomes, audit findings, and system-improvement decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with strong Non-Responsibilities.
[ ] Ownership of weekly/monthly/quarterly reviews, the AOS User Guide (projection), and aos_version reconciliation documented.
[ ] Completeness/consistency audit scope defined; drift invariant (Section 14.8) respected.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13). Suggested next step: select and build at least one optional productive agent.
