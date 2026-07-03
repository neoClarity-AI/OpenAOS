---
name: build-task-agent
description: "Build the Task Agent, an optional productive AOS agent that owns task and commitment tracking: capturing, prioritizing, and closing out tasks from inbox items, projects, and direct requests. Use when selected during AOS setup or later via 'Build the Task Agent'."
---

# Build Task Agent

## Builder Purpose

Build the Task Agent, an optional productive agent that owns task and commitment
tracking: capturing, prioritizing, and closing out tasks from inbox items,
projects, and direct requests (catalog: `task-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output preferences, approval
boundaries, collaboration; summarize; recommend defaults; preview; wait for
`Proceed`.

## Discovery Questions

- How does the user want tasks structured (priority, due date, source)?
- What counts as "at risk", and when should it be surfaced?
- Which handoffs matter (Calendar for time, Project Manager for projects,
  Automation for recurring)?

## Recommended Defaults

- Maintain a structured task list; accept promotions from the inbox-to-task
  workflow (Section 17.6).
- Surface today's and at-risk items in the daily startup brief (Section 17.1) and
  follow-ups in the weekly review (Section 17.3).
- Creating/updating tasks is autonomous; deleting/bulk-modifying, or
  closing/cancelling another agent's task, is gated by `Proceed`.

## Configuration Decisions

- Task fields and priority scheme; at-risk thresholds; handoff rules.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/task-agent/task-agent.md
/agents/task-agent/memory/task-memory.md
/agents/task-agent/memory/task-learnings.md
/agents/task-agent/workflows/task-primary-workflow.md
/agents/task-agent/templates/task-output-template.md
/agents/task-agent/configs/task-config.md
/agents/task-agent/logs/task-decision-log.md
```

## Agent Instruction Generation Rules

Render `task-agent.md` to the Section 11 schema. Project **identity** from the
`task-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns task and commitment tracking — capturing,
  prioritizing, and closing out tasks.
- Responsibilities ← `domains_owned`: `task-tracking`.
- Non-Responsibilities ← derived: does not triage/draft communications (inbox),
  schedule (calendar), or coordinate multi-task projects (project-manager).
- Inputs ← `communications.triage`; Outputs ← `task-tracking`.
- Collaboration Rules ← `collaborates_with`: receives commitments from Inbox; hands
  off to Calendar (time blocking), Project Manager (project tasks), Automation
  (recurring tasks); escalates priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (close or cancel a task
  created by another agent); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/task-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `task-primary-workflow.md` (Section 16.3): capture → prioritize → review
tasks → surface at-risk commitments.

## Memory Generation Rules

Seed `task-memory.md` and `task-learnings.md` per Section 16.2. Track recurring
commitments and prioritization preferences.

## Config Generation Rules

Write `task-config.md` (Section 16.1). `Inherited Rules` references global
permissions; `Tool Access` references the matrix.

## Logging Rules

Append-only `task-decision-log.md` (Section 16.5). Log important configuration and
prioritization decisions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Handoffs to Calendar / Project Manager / Automation wired in.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/task-agent/logs/task-build-summary.md` (file_type `build_summary`).
