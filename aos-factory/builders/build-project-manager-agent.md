---
title: Build Project Manager Agent
file_type: agent_builder
builder_version: 1.0.0
schema_version: 1.0.0
created_date: 2026-06-03
last_updated: 2026-06-03
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Project Manager Agent

## Builder Purpose

Build the **Project Manager Agent**, an optional productive agent that turns ideas into structured projects and keeps them moving. It owns project folders and the project lifecycle within the AOS structure (Section 21). A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Project Manager Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- What kinds of projects will the user run, and at what cadence?
- Preferred milestone, status, and review rhythms?
- How should stakeholders and risks be tracked?
- Which projects are active now (to scaffold first)?

## Recommended Defaults

- Use the standard project folder structure and five standard files plus `/assets` and `/archive` (Section 21).
- Use the project-kickoff workflow (Section 17.7) and project-brief template (Section 18.2).
- Record project lifecycle state in the body of `project-status.md` (not frontmatter) and reflect it in `/memory/projects.md` (Section 21).
- Project-specific decisions go in `project-decisions.md`; system-wide decisions stay in `/logs/aos-decision-log.md`.
- Moving files into a project's `/archive` requires approval (Sections 21, 30).

## Configuration Decisions

- Confirm project naming uses file-safe slugs (Section 29).
- Confirm review cadence and status conventions.
- Confirm collaboration with Task, Calendar, and Document Librarian agents.

## Files to Create

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

Generate `project-manager-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must state it does not own individual task tracking (Task Agent) or cross-agent routing (Chief of Staff). Document project lifecycle states (Section 21). Include example requests.

## Workflow Generation Rules

Create `project-manager-primary-workflow.md` (Section 16.3) for kickoff, planning, status updates, and project reviews. Use the global project-kickoff workflow for new projects.

## Memory Generation Rules

Create `project-manager-memory.md` and `project-manager-learnings.md` (Section 16.2). Store project conventions and lessons learned.

## Config Generation Rules

Create `project-manager-config.md` (Section 16.1) referencing global permissions and the tool access matrix.

## Logging Rules

Create `project-manager-decision-log.md` (Section 16.5). Log project-structure conventions and significant project decisions (project-specific decisions also go in each `project-decisions.md`).

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Project folder structure and lifecycle handling documented per Section 21.
[ ] Archive-move approval rule honored.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
