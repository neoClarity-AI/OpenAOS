---
name: build-project-manager-agent
description: "Build the Project Manager Agent, an optional productive AOS agent that owns project coordination: briefs, plans, milestones, stakeholders, and cross-task tracking for active projects. Use when selected during AOS setup or later via 'Build the Project Manager Agent'."
---

# Build Project Manager Agent

## Builder Purpose

Build the Project Manager Agent, an optional productive agent that owns project
coordination: briefs, plans, milestones, stakeholders, and cross-task tracking for
active projects (catalog: `project-manager-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator across the whole AOS
(Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output preferences, approval
boundaries, collaboration; summarize; recommend defaults; preview; wait for
`Proceed`.

## Discovery Questions

- What kinds of projects, and what review cadence?
- Which project-brief fields matter most (Section 18.2)?
- How should tasks, research, and stakeholder tracking be delegated?

## Recommended Defaults

- Use the Section 21 project structure (five standard files + `/assets` +
  `/archive`) via the project-kickoff workflow (Section 17.7) and the project-brief
  template (Section 18.2).
- Record lifecycle state in the body of `project-status.md` and reflect it in
  `/memory/projects.md` (not frontmatter, Section 21).
- Delegate tasks to Task, research to Research, external stakeholders to Personal
  CRM.

## Configuration Decisions

- Project types; review cadence; delegation rules.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/project-manager-agent/project-manager-agent.md
/agents/project-manager-agent/memory/project-manager-memory.md
/agents/project-manager-agent/memory/project-manager-learnings.md
/agents/project-manager-agent/workflows/project-manager-primary-workflow.md
/agents/project-manager-agent/templates/project-manager-output-template.md
/agents/project-manager-agent/configs/project-manager-config.md
/agents/project-manager-agent/logs/project-manager-decision-log.md
```

## Agent Instruction Generation Rules

Render `project-manager-agent.md` to the Section 11 schema. Project **identity**
from the `project-manager-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns project coordination — briefs, plans, milestones,
  stakeholders, and cross-task tracking.
- Responsibilities ← `domains_owned`: `project-coordination`.
- Non-Responsibilities ← derived: does not track individual tasks (task),
  triage/draft communications (inbox), or conduct research (research).
- Inputs ← `communications.triage`, `task-tracking`; Outputs ←
  `project-coordination`.
- Collaboration Rules ← `collaborates_with`: receives project items from Inbox and
  project tasks from Task; hands off to Research (support) and Personal CRM
  (stakeholders); escalates cross-project priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (close out or cancel a
  project); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/project-manager-agent.md`
(§7B). Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `project-manager-primary-workflow.md` (Section 16.3): kickoff → planning →
status updates → project reviews. Supports the global project-kickoff workflow
(Section 17.7).

## Memory Generation Rules

Seed `project-manager-memory.md` and `project-manager-learnings.md` per Section
16.2. Track project conventions and lessons learned.

## Config Generation Rules

Write `project-manager-config.md` (Section 16.1). `Inherited Rules` references
global permissions; note that moving files into a project `/archive` and
closing/cancelling a project are `Proceed`-gated (Sections 21, 30).

## Logging Rules

Append-only `project-manager-decision-log.md` (Section 16.5); project-specific
decisions go in each project's `project-decisions.md` (Section 21).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Project structure and lifecycle-state handling correct (Section 21); file-safe
  slugs (Section 29).
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/project-manager-agent/logs/project-manager-build-summary.md` (file_type
`build_summary`).
