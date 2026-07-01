---
title: Build Research Agent
file_type: agent_builder
spec_version: 1.1.0
created_date: 2026-06-03
last_updated: 2026-06-25
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Research Agent

## Builder Purpose

Build the **Research Agent**, an optional productive agent that gathers, evaluates, and synthesizes information into useful outputs. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Research Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- What topics or domains will research focus on?
- Should the agent use web search, and any source-quality preferences?
- Preferred output format (briefs, annotated sources, comparison tables)?
- How should sources and confidence be recorded?

## Recommended Defaults

- Web search is `Allowed` for research tasks when granted in the matrix (Section 22).
- Output synthesized briefs with cited sources and confidence notes.
- Store durable findings in agent memory; large source documents belong in `/projects` or a project's `/assets`, not memory (Section 20.3).
- Hand finished material to the Writing Agent when polished content is needed (Section 23).

## Configuration Decisions

- Confirm web-search access level in the matrix (Section 22).
- Confirm output templates and citation conventions.
- Confirm collaboration with Writing, Learning, and Document agents.

## Files to Create

```text
/agents/research-agent/research-agent.md
/agents/research-agent/memory/research-memory.md
/agents/research-agent/memory/research-learnings.md
/agents/research-agent/workflows/research-primary-workflow.md
/agents/research-agent/templates/research-output-template.md
/agents/research-agent/configs/research-config.md
/agents/research-agent/logs/research-decision-log.md
```

## Agent Instruction Generation Rules

Generate `research-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it does not publish content or make decisions for the user. Include example requests.

## Workflow Generation Rules

Create `research-primary-workflow.md` (Section 16.3) for scoping a question, gathering and evaluating sources, and producing a synthesized output.

## Memory Generation Rules

Create `research-memory.md` and `research-learnings.md` (Section 16.2). Store durable findings and reliable sources with confidence.

## Config Generation Rules

Create `research-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix (web search).

## Logging Rules

Create `research-decision-log.md` (Section 16.5). Log methodology decisions and significant findings affecting future work.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Web-search access references the global matrix.
[ ] Output template includes sources and confidence.
[ ] Large-document storage routed away from memory.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
