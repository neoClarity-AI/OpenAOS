---
title: Build Learning / Tutor Agent
file_type: agent_builder
spec_version: 1.1.0
created_date: 2026-06-03
last_updated: 2026-06-25
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Learning / Tutor Agent

## Builder Purpose

Build the **Learning / Tutor Agent**, an optional productive agent that helps the user learn topics, build study plans, explain concepts, and track learning progress. It is a specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When the user selects this agent during setup, or later via the request "Build the Learning Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): ask about goals, scope, tools, output preferences, approval boundaries, and collaboration patterns. Batch the questions (Section 9.1), summarize, recommend defaults, request `Proceed`.

## Discovery Questions

- What does the user want to learn, and at what depth?
- Preferred learning style (explanations, worked examples, practice questions, spaced repetition)?
- Should the agent use web search or rely on provided materials?
- How should progress be tracked and reviewed?

## Recommended Defaults

- Output study plans, plain-language explanations, and practice questions (Section 32: include examples).
- Track progress in agent memory; surface stale or overdue topics during reviews.
- Use web search only if granted in the tool access matrix; otherwise work from provided materials.
- Hand off research-heavy requests to the Research Agent when installed (Section 23).

## Configuration Decisions

- Confirm tool access (e.g., web search) via the global matrix (Section 22).
- Confirm collaboration boundaries with Research and Writing agents.
- Confirm what learning data is memory-worthy versus transient.

## Files to Create

```text
/agents/learning-agent/learning-agent.md
/agents/learning-agent/memory/learning-memory.md
/agents/learning-agent/memory/learning-learnings.md
/agents/learning-agent/workflows/learning-primary-workflow.md
/agents/learning-agent/templates/learning-output-template.md
/agents/learning-agent/configs/learning-config.md
/agents/learning-agent/logs/learning-decision-log.md
```

## Agent Instruction Generation Rules

Generate `learning-agent.md` per Section 11 with `agent_instruction` frontmatter and a strong Non-Responsibilities section (it teaches; it does not own research collection, content publishing, or scheduling). Include example requests (Section 32).

## Workflow Generation Rules

Create `learning-primary-workflow.md` (Section 16.3) for turning a learning goal into a study plan, lessons, and practice with review checkpoints. Add domain workflows only when useful.

## Memory Generation Rules

Create `learning-memory.md` and `learning-learnings.md` (Section 16.2). Store learning goals, progress, and effective approaches using the standard entry fields (Section 20.3).

## Config Generation Rules

Create `learning-config.md` (Section 16.1) referencing global permissions; `Tool Access` references the matrix and lists agent-specific notes only.

## Logging Rules

Create `learning-decision-log.md` (Section 16.5). Log significant changes to learning plans and approach decisions.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with examples and Non-Responsibilities.
[ ] Tool access references the global matrix.
[ ] Collaboration boundaries with Research/Writing defined.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13): Files Created, Key Decisions, User Preferences Captured, Permissions and Boundaries, Open Questions, Suggested Next Agent.
