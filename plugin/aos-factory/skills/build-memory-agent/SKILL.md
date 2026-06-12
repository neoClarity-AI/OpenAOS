---
name: build-memory-agent
description: "Build the Memory Agent, a required AOS governance agent that owns shared memory structure, memory hygiene, preference capture, and cross-agent memory routing. Use during initial AOS setup or when restoring or rebuilding the memory agent."
---

# Build Memory Agent

## Builder Purpose

Build the **Memory Agent**, a required governance agent. It owns shared memory structure, memory hygiene, preference capture, and cross-agent memory routing (Section 7.4). Standardized purpose, so a short interview (Section 26).

## When to Use This Builder

During initial AOS setup (via `/builders/build-aos.md`) or when restoring or rebuilding the Memory Agent.

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Short batch interview (Section 9.1): confirm responsibilities, ask the questions below, summarize, recommend defaults, request `Proceed`.

## Discovery Questions

- Are there categories of information the user definitely wants remembered, or definitely not?
- How sensitive is the user about storing personal facts (gates the explicit-approval rule)?
- Preferred cadence for memory review beyond the default weekly-light / monthly-deep?

## Recommended Defaults

- Use the six required global memory files and their boundaries (Section 20).
- Apply the agent-learnings index model: a routing map, not a central dump (Section 6.1).
- Memory-worthy only if durable, useful, relevant, and likely to improve future assistance (Section 20.3).
- Lightweight weekly review, deeper monthly review; never silently delete stale memory.

## Configuration Decisions

- Confirm which entries count as sensitive and therefore require explicit approval.
- Confirm routing: which content belongs in which global memory file versus an agent's own memory.
- Confirm coordination with the Security Agent on sensitive-memory approvals.

## Files to Create

```text
/agents/memory-agent/memory-agent.md
/agents/memory-agent/memory/memory-memory.md
/agents/memory-agent/memory/memory-learnings.md
/agents/memory-agent/workflows/memory-primary-workflow.md
/agents/memory-agent/templates/memory-output-template.md
/agents/memory-agent/configs/memory-config.md
/agents/memory-agent/logs/memory-decision-log.md
```

## Agent Instruction Generation Rules

Generate `memory-agent.md` per Section 11 with `agent_instruction` frontmatter. Emphasize Non-Responsibilities (it curates memory; it does not own domain work). Document memory boundaries (Section 20.2), governance rules (Section 20.3), and ownership of the memory-review workflow with Review Agent support (Section 17.9).

## Workflow Generation Rules

Create `memory-primary-workflow.md` (Section 16.3) for capturing, classifying, routing, and reviewing memory entries. The Memory Agent is primary owner of `/workflows/memory-review-workflow.md` at the global level.

## Memory Generation Rules

Create `memory-memory.md` and `memory-learnings.md` (Section 16.2). Use the standard entry fields: Type, Summary, Source, Confidence, Owner, Review Date, Notes (Section 20.3).

## Config Generation Rules

Create `memory-config.md` (Section 16.1) referencing global permissions; `Memory Access` defines this agent's read/write scope across global memory files.

## Logging Rules

Create `memory-decision-log.md` (Section 16.5). Log memory-routing decisions, sensitivity approvals, and hygiene actions (mark-stale, supersede, archive-with-approval).

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with strong Non-Responsibilities.
[ ] Memory boundaries and governance rules documented.
[ ] Sensitive-entry approval path defined with Security Agent.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13). Suggested next agent: Chief of Staff Agent.
