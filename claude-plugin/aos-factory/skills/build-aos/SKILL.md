---
name: build-aos
description: Build a complete Agentic Operating System (AOS) instance from scratch. Use when the user wants to create, set up, build, or stand up their AOS or 'agentic operating system' — including its folder structure, the five required governance agents (Security, Memory, Chief of Staff, Review, Feedback), at least one optional productive agent, global workflows, templates, configs, logs, and the AOS User Guide. Master entry point; orchestrates the build-agent engine per agent. No files are created until the user types exactly Proceed.
---


# Build AOS

## Builder Purpose

Build a complete Agentic Operating System (AOS) instance from the AOS Factory: the instance folder structure (§4), the global files (§6), the five required governance agents, at least one user-selected optional productive agent (§2.3, §7), the global workflows and templates (§17, §18), and the AOS User Guide (§16.6). The design spec is the single source of truth (§1.6.1); this builder is a rendering of it.

## When to Use This Builder

- The user asks to create, set up, build, or stand up their AOS / agentic operating system.
- Invoked via the root entry pointer `/build-aos.md` or directly.
- Not for adding a single agent to an existing instance — that is `/builders/build-agent.md` (§9.4).

## Builder Operating Mode

Coach + collaborator (§1.5): explain concepts in coach mode, switch to collaborator mode for design choices, recommend sensible defaults, ask approval on important decisions, move forward with documented assumptions on low-risk details, defer to the user. Default to dry-run / preview; create no file until the user types exactly `Proceed` (§3.1, §9.1). Non-destructive by default; every overwrite of an existing file is listed and separately approved (§2.4, §2.5, §3.2).

## Interview Flow

Execute the scripted AOS setup interview in `/aos-interviews.md` (§7C) using the §9.1 batch pattern:

1. Ask a small batch of questions.
2. Summarize what the user said.
3. Recommend defaults for anything vague.
4. Ask for approval on important design decisions.
5. Generate the build plan / pre-build preview (Files to Create / Decisions Applied / Assumptions / Approval).
6. Ask the user to type `Proceed` before creating files.

The script is normative for question content, order, and captured fields; delivery is conversational — paraphrase allowed, never adding, removing, or reordering questions. Fast path (only when the user explicitly asks to move faster): `skippable: yes` questions resolve to their defaults; no other question may be dropped (§7C.4).

## Discovery Questions

Defined in `/aos-interviews.md`; this builder references that script and does not restate it (§12.1). The script covers AOS purpose, domains, the AOS name (proposed by the builder, modifiable by the user, rendered as a file-safe slug per §29), optional-agent selection, and tool/approval baselines.

## Recommended Defaults

Defaults and `skippable` markers are carried per-question in `/aos-interviews.md`. General posture: recommend the default, note the assumption, and keep moving (§1.5); required governance agents use standardized choices with defaults (§26).

## AOS Setup Sequence

Follow §9.3:

```text
1. Start the AOS setup interview (above).
2. Create the top-level folder structure (§4) as a sibling AOS root (§4.1).
3. Provision the AOS Workspace root: ensure /CLAUDE.md exists, copying the
   factory's shipped example (templates/CLAUDE.md, §28.2). Create it if
   absent; never overwrite an existing root file without a separate Proceed.
4. Create global config, memory, log, workflow, template, inbox, and archive
   files (§6).
5. Confirm the generic build engine (/builders/build-agent.md) and every
   approved agent's design artifacts (catalog entry, profile, interviews)
   exist at the factory root.
6. Build the five required governance agents.
7. Ask the user to select at least one optional productive agent.
8. Build the selected optional agents.
9. Update /configs/agent-registry.md and /aos-map.md.
10. Produce the AOS setup summary (/logs/aos-build-summary.md).
```

All instance paths resolve against the target AOS root established in step 2; factory paths resolve against the factory root (§4.1). File creation waits for `Proceed`.

## Folder Structure to Create

The §4 tree at `/[aos-name]/`:

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
    /[agent-name]-agent      (one per installed agent, created at that agent's build)
  /inbox
    /processed
  /archive
```

## Global Files to Create

The §6 list, each rendered per its §16 schema with §15.3 frontmatter (`spec_version: 2.2.0` + the instance `aos_version`, initially 1.0.0 per §14.3.1):

```text
/aos-manifest.md                          (§14.3 schema; aos_version 1.0.0)
/aos-map.md                               (§10.4 schema)
/configs/global-permissions.md            (§16.11 seed: the three §3.4 levels mapping §3.2/§3.3)
/configs/agent-registry.md                (§10.3 table)
/configs/tool-access-matrix.md            (§22 schema; owned by the Security Agent)
/memory/user-profile.md                   (§16.2 / §20.2)
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md          (§6.1 index table)
/logs/aos-decision-log.md                 (§16.5)
/logs/change-log.md                       (§16.8 entries)
/logs/feedback-log.md                     (§16.7)
/workflows/daily-startup-workflow.md      (§17.1: factory-vs-instance check first; 9-category startup brief)
/workflows/end-of-day-shutdown-workflow.md (§17.2)
/workflows/weekly-review-workflow.md      (§17.3: includes the advertising check)
/workflows/monthly-review-workflow.md     (§17.4: guide regeneration + aos_version reconciliation + Feedback self-examination)
/workflows/quarterly-review-workflow.md   (§17.5: advertising re-raise + retirement signals; anti-nagging rule)
/workflows/inbox-to-task-workflow.md      (§17.6: /inbox/processed move pre-authorized within the approved workflow)
/workflows/project-kickoff-workflow.md    (§17.7)
/workflows/decision-capture-workflow.md   (§17.8)
/workflows/memory-review-workflow.md      (§17.9)
/templates/status-report-template.md      (§18.1)
/templates/project-brief-template.md      (§18.2)
/templates/decision-entry-template.md     (§18.3: embeds the §16.5 entry block)
/templates/handoff-summary-template.md    (§18.4)
/templates/approval-request-template.md   (§18.5: the five §3.1 elements)
/templates/memory-entry-template.md       (§18.6: embeds the §16.2/§20.3 entry block)
/docs/aos-user-guide.html                 (§16.6 skeleton — see below)
```

**AOS User Guide generation (mandatory rules, §16.6).** Generate from the §16.6 skeleton: header metadata (file_type documentation, AOS name, aos_version, spec_version, last_updated), title/subtitle, then a Table of Contents listing — in order — Change Log, Introduction, Folder Orientation, Agents Overview, Core Rules & Safety, Operating Rhythms, Managing Agents, Invocation Reference. Every section carries its stable `id` anchor; every TOC entry is an in-page link; the TOC mirrors exactly the sections emitted. Seed the Change Log (immediately after the TOC) with one dated entry: "[last_updated] — Initial guide generated during AOS setup." The Invocation Reference states that trigger phrases are matched by intent and `Proceed` is the only exact-string command, carries the global trigger table scoped to the installed agents, and points to each installed agent's `## Example Requests` section. The guide is invalid until the §16.6 consistency checks pass (every TOC entry resolves, every section has a TOC entry, Change Log present and non-empty).

## Required Agent Orchestration

Build, in order, by invoking `/builders/build-agent.md` per agent: Security Agent, Memory Agent, Chief of Staff Agent, Review Agent, Feedback Agent (§1.6.2 — governance before productivity). The Chief of Staff Agent's registry entry notes its ownership of the factory-vs-instance guard in `/CLAUDE.md` (§10.3, §16.10).

## Optional Agent Selection

Present the §7.2 roster in order (Tutor, Inbox, Calendar, Task, Project Manager, Research, Writing, Document, Personal CRM, Automation). **At least one optional productive agent must be selected before setup is complete (§2.3, §7.2)** — do not close setup with zero. Build each selected agent via the generic engine. Unselected agents remain `Available` in the registry/map (§10.1, §10.4) and are surfaced later by the Review Agent's advertising checks (§17.3, §17.5).

## Registry and Map Updates

After each agent build and at the end of setup, update `/configs/agent-registry.md` (§10.3) and `/aos-map.md` (§10.4) so every §7.3 agent appears with the correct status (Active / Available), tier, and folder. Record the setup in `/logs/change-log.md` and `/logs/aos-decision-log.md`; set the manifest (§14.3) with `aos_version: 1.0.0` and `spec_version: 2.2.0`.

## Validation Checklist

Per §27, before declaring setup complete:

```text
[ ] Required folders (§4) and global files (§6) all exist.
[ ] Five governance agents built and Active; at least one optional agent built.
[ ] Every built agent passes the build-agent validation checklist (§5.1 file set).
[ ] Registry, map, and manifest are consistent with each other and with the folders on disk.
[ ] Catalog/profile/interview validation passes (§7A.5 V1–V8, §7B.5 V9–V13).
[ ] Global permissions, tool access matrix, workflows, templates, and logs conform to their §16 schemas.
[ ] AOS User Guide passes the §16.6 consistency checks.
[ ] /CLAUDE.md exists at the AOS Workspace root (created from the shipped example if it was absent).
```

## AOS Setup Summary

Save `/logs/aos-build-summary.md` (`file_type: build_summary`, §9.3/§15.4) with the §13-parallel schema at instance scope:

```markdown
# AOS Setup Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Steps
```
