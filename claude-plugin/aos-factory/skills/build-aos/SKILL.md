---
name: build-aos
description: Build a complete Agentic Operating System (AOS) instance from scratch — run the interactive setup interview, create the instance folder structure and global files, provision the AOS Workspace root, build the required governance agents and the user's selected optional productive agents, and produce an AOS setup summary. The master AOS builder. Use when the user asks to set up, create, stand up, or build a new AOS, an "agentic operating system", or an additional AOS instance. To add or rebuild a single agent inside an existing instance instead, use the build-agent skill.
spec_version: 2.2.2
---
# Build AOS

## Builder Purpose

Build a complete AOS instance: run the interactive setup interview, create the
instance folder structure and global files, provision the AOS Workspace root,
build the required governance agents and the user's selected optional productive
agents, and produce an AOS setup summary. This is the master AOS builder (§12.1).
It reads the factory-shipped design artifacts — `agent-catalog.yaml` (§7A), the
`agent-specs/` profiles and interviews (§7B, §7C), and `aos-interviews.md`
(§7C) — and never hand-authors identity or narrative those sources already
provide.

> Packaged as a Claude plugin skill. The design artifacts referenced below
> (`agent-catalog.yaml`, `agent-specs/`, `aos-interviews.md`) ship with the
> factory framework; resolve them from the installed factory / plugin context.

## When to Use This Builder

Use when the user asks to set up, create, or build a new AOS instance. To add a
single agent to an existing instance instead, use the `build-agent` skill (§9.4).
Maintaining or refreshing the framework files themselves is a separate, manually
approved operation (§8.4, §14.4).

## Builder Operating Mode

Combine coach and collaborator behavior (§1.5): explain in coach mode when a
concept needs it, switch to collaborator mode for design choices, recommend
sensible defaults, and move forward on documented assumptions for low-risk
details. Default to **dry-run / preview**: describe what will be created and gate
every file-creating step behind the user typing exactly `Proceed` (§3.1, §9.1).
Approval is action-specific (§2.5). Never overwrite, delete, move, or rename an
existing file without a separate `Proceed` (§2.4, §3.2). Creating new files and
folders is Level 1 safe-autonomous (§3.3) but is still previewed as part of the
build plan before `Proceed`.

## Interview Flow

Follow the §9.1 batch pattern: (1) ask a small batch of questions, (2) summarize
what the user said, (3) recommend defaults for anything vague, (4) ask approval on
important design decisions, (5) generate a build plan / pre-build preview, (6) ask
the user to type `Proceed` before creating files. Execute the scripted AOS setup
interview in `aos-interviews.md` (§7C): the script is normative for question
content, order, and captured fields; delivery stays conversational (paraphrase
allowed; never add, remove, or reorder questions). Fast path (move-faster
exception, §7C.4): questions marked `skippable: yes` resolve to their `default:`
values; no other question may be dropped.

The step-5 pre-build preview uses this block (§9.1):

```markdown
## Files to Create
## Decisions Applied
## Assumptions
## Approval
[the Proceed ask — type exactly `Proceed` to create the files above]
```

## Discovery Questions

Defined by the scripted AOS setup interview in `aos-interviews.md` (§7C) —
purpose, instance name, optional-agent selection, memory seeds, and optional
call name. This builder references that script and does not restate it
(§12.1).

## Recommended Defaults

Defined by the `default:` values in `aos-interviews.md` (§7C): propose an
instance name from the stated purpose; recommend agents by the stated
aos-purpose category — Inbox + Task + Calendar + Document for Personal
Productivity, Project Manager + Task + Document for Project Management,
Personal CRM + Task + Calendar for Client Specific, and the full §7.2 roster
with no default for Other; seed memory empty and never fabricate; no call name
unless requested. This builder references that script and does not restate
it. The §3 permission model
applies unchanged by default — autonomy is no longer asked about at setup;
instance-specific tightening or loosening happens later in
`/configs/global-permissions.md` (§3.5).

## AOS Setup Sequence

Follow §9.3, gating file creation on `Proceed`:

```text
0. The factory framework already exists (this build runs from it).
1. Start the user-facing AOS setup interview (aos-interviews.md).
2. Create the top-level folder structure (see below), as a sibling AOS root (§4.1).
3. Provision the AOS Workspace root: ensure /aos-router.md and /CLAUDE.md exist,
   copying them from the factory's shipped example copies (templates/aos-router.md,
   templates/CLAUDE.md; §28.2). Create if absent; if either already exists, do
   not overwrite without a separate Proceed (§2.4, §3.2, §4.1).
4. Create global config, memory, log, workflow, template, inbox, and archive files.
5. Confirm the generic build engine and every approved agent's design artifacts
   (catalog entry, profile, interviews) exist.
6. Build the required governance agents.
7. Ask the user to select at least one optional productive agent (§2.3, §7.2).
8. Build the selected optional agents (via the build-agent skill).
9. Update the agent registry and AOS map.
10. Offer to schedule the rhythmic workflows as Cowork Scheduled Tasks (see below).
11. Produce the AOS setup summary (/logs/aos-build-summary.md).
```

## Folder Structure to Create

Use the §4 top-level tree, created as a sibling AOS root named for the user's
chosen AOS name (§4.1):

```text
/[aos-name]
  aos-manifest.md
  aos-map.md
  /agents
  /workflows
  /memory
  /projects
  /logs
  /templates
  /configs
  /docs
  /outputs
    /[agent-name]-agent      (one subfolder per installed agent; §5.1)
  /inbox
    /processed
  /archive
```

## Global Files to Create

Use the §6 list. Stamp every generated file's frontmatter with `spec_version`
(and, for instance files, `aos_version`; §15). Seed data files empty or with only
user-provided content — never fabricate (§14.8, §20.3):

```text
/aos-manifest.md                         (§14.3 schema; aos_version 1.0.0)
/aos-map.md                              (§10.4 schema)
/configs/global-permissions.md           (§16.12 seed — the three §3.4 levels)
/configs/agent-registry.md               (§10.3 table)
/configs/tool-access-matrix.md           (§22; every tool defaults Not configured)
/memory/user-profile.md
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md         (§6.1 index table)
/logs/aos-decision-log.md
/logs/change-log.md
/logs/feedback-log.md                    (§16.7)
/workflows/daily-startup-workflow.md     (§17.1 — includes instance-resolution step
                                          and the nine-category startup brief)
/workflows/end-of-day-shutdown-workflow.md
/workflows/weekly-review-workflow.md
/workflows/monthly-review-workflow.md
/workflows/inbox-to-task-workflow.md
/workflows/project-kickoff-workflow.md
/workflows/decision-capture-workflow.md
/workflows/memory-review-workflow.md
/templates/status-report-template.md
/templates/project-brief-template.md
/templates/decision-entry-template.md
/templates/handoff-summary-template.md
/templates/approval-request-template.md
/templates/memory-entry-template.md
/docs/aos-user-guide.html                (§16.6 skeleton — generate the TOC,
                                          anchors, and seeded Change Log complete;
                                          Invocation Reference scoped to installed
                                          agents; run the §16.6 consistency checks)
```

## Required Agent Orchestration

Build all five required governance agents (Security, Memory, Chief of Staff,
Review, Feedback; §7.1) by invoking the `build-agent` skill for each, resolving
its catalog entry and `agent-specs/[agent-name]-agent/` folder. Required agents
have shorter Initialization interviews (§7C.4). These agents cannot be omitted
(governance before productivity, §1.6.2). Note the Chief of Staff's joint
ownership of the AOS Workspace router in its registry entry (§10.3).

## Optional Agent Selection

Enforce that at least one optional productive agent is chosen before setup is
complete (§2.3, §7.2). Present the §7.2 roster with the recommended defaults;
build each selected agent via the `build-agent` skill. Remaining optional
agents stay `Available` and can be added later (§9.4).

## Registry and Map Updates

Update `/configs/agent-registry.md` (§10.3) and `/aos-map.md` (§10.4) to reflect
each built agent (status `Active`), each `Available` uninstalled agent, and the
instance's folder map. Record installed/active agents in `/aos-manifest.md`
(§14.3). These are mixed/data files — update by targeted merge, never wholesale
overwrite (§14.8).

## Rhythmic Workflow Scheduling

Offer a Cowork Scheduled Task for each of the four cadence-driven workflows —
daily startup, end-of-day shutdown, weekly review, monthly review (§17.1–17.4)
— invoking that workflow's routed execution (through the instance router,
§16.10) on its cadence. This is offered, never assumed: present the standard
cadence (§25) and the Review Agent's captured `review-timing` preference
where set (§26); create a task only for each workflow the user accepts.
Declining any or all leaves that workflow manually triggered. Do not schedule
event-triggered workflows (inbox-to-task, project kickoff, decision capture,
memory review; §17.5–17.8) — they run on their triggering event, not a
cadence. Creating a Scheduled Task is Level 2 (§3.4): preview the proposed
schedule and gate creation behind `Proceed`. Log each accepted schedule to
`/logs/change-log.md`.

Each task's instructions must contain exactly one line pointing to its
workflow file, as an `@`-path reference against the instance root — e.g.
`@/[aos-name]/workflows/daily-startup-workflow.md` — and nothing else; the
workflow file is the single source of truth for the run's behavior.

## Validation Checklist

Run the §27 completeness checks before finishing: every required agent built and
`Active`; at least one optional agent installed; all §6 global files present and
frontmatter-stamped; the AOS Workspace root files provisioned; the user guide
passes the §16.6 consistency checks (TOC ↔ anchors, Change Log present and
non-empty); the registry, map, and manifest agree; every instance path resolved
against the instance root (§4.1). Report and correct any gap before completing.

## AOS Setup Summary

Write `/logs/aos-build-summary.md` (file_type `build_summary`, §15.4) with the
instance-scoped parallel of the §13 schema:

```markdown
# [AOS Name] Build Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Steps
```
