---
name: build-chief-of-staff-agent
description: "Build the Chief of Staff Agent, a required AOS governance agent that owns orchestration, routing, prioritization, conflict resolution, user-facing coordination, and joint ownership of the instance router. Use during initial AOS setup or when restoring or rebuilding the chief of staff agent."
---


# Build Chief of Staff Agent

## Builder Purpose

Build the **Chief of Staff Agent**, a required governance agent. It owns orchestration, routing, prioritization, conflict resolution, and user-facing coordination (Section 7.4). It coordinates rather than doing the work itself; responsibility is pushed down to specialized agents (Sections 2.2, 7.6). Standardized purpose, short interview.

It is also a **joint owner of the instance router** (`/aos-router.md`): when multiple instances exist (e.g. `work-aos` and `personal-aos`), their Chief of Staff agents share ownership of the router that resolves the active target before any workflow runs. This agent must honor router resolution — ask on weak or mixed signals, never silently pick or merge instances — and log instance-routing choices to its own decision log.

## When to Use This Builder

During initial AOS setup (via `/builders/build-aos.md`) or when restoring or rebuilding the Chief of Staff Agent.

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Short batch interview (Section 9.1).

## Discovery Questions

- How does the user want priorities decided when agents or projects compete?
- How much should the Chief of Staff decide autonomously versus surface to the user?
- Preferred default for the daily startup brief and status reporting?

## Recommended Defaults

- Default coordinator for all cross-agent routing (Section 23).
- Direct agent-to-agent handoff only when the receiving agent has clear ownership and there is no safety, permission, or priority conflict; otherwise route through Chief of Staff (Section 23).
- Priority conflicts and unclear ownership escalate here; permission conflicts escalate to Security (Section 24).
- Owns user-facing coordination of the daily startup and status reporting.

## Configuration Decisions

- Confirm the handoff protocol uses `/templates/handoff-summary-template.md` (Section 23).
- Confirm escalation routing (Section 24).
- Confirm the Chief of Staff does not absorb specialized work (Section 2.2).

## Files to Create

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

Generate `chief-of-staff-agent.md` per Section 11 with `agent_instruction` frontmatter. Emphasize Non-Responsibilities: it coordinates, prioritizes, routes, and resolves conflicts; it is not a universal worker (Sections 2.2, 7.6). Document routing, prioritization, and conflict-resolution behavior, and its default-coordinator role (Section 23). Document its **joint ownership of the instance router** (`/aos-router.md`): resolve the active target before running any workflow, honor the ask-don't-guess rule on weak or mixed signals, and never silently pick or merge instances.

## Workflow Generation Rules

Create `chief-of-staff-primary-workflow.md` (Section 16.3) for receiving a request, routing it to the owning agent, resolving conflicts, and coordinating handoffs. Connect to the global daily-startup workflow.

## Memory Generation Rules

Create `chief-of-staff-memory.md` and `chief-of-staff-learnings.md` (Section 16.2). Store routing patterns and prioritization preferences.

## Config Generation Rules

Create `chief-of-staff-config.md` (Section 16.1) referencing global permissions and the tool access matrix.

## Logging Rules

Create `chief-of-staff-decision-log.md` (Section 16.5). Log routing and prioritization decisions and conflict resolutions that affect future behavior. This log is also the home for **instance-routing choices** resolved via `/aos-router.md` (chosen instance, trigger, default vs. asked), per the router's logging rule.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with strong Non-Responsibilities.
[ ] Routing, prioritization, and conflict-resolution behavior documented.
[ ] Joint ownership of /aos-router.md documented, with ask-don't-guess and no silent instance merge.
[ ] Handoff protocol references the global handoff template.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13). Suggested next agent: Review / Reflection Agent.
