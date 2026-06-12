---
title: Build AOS
file_type: aos_builder
spec_version: 1.0.5
created_date: 2026-06-03
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build AOS

## Builder Purpose

This builder runs the interactive setup that creates a complete **Agentic Operating System (AOS) instance**: its folder structure, global files, required governance agents, at least one optional productive agent, workflows, templates, logs, and the AOS User Guide.

It produces a working AOS the user can operate immediately. It does not modify the reusable framework itself; the framework is generated from the design specification and distributed as a Claude plugin, and maintaining it is a separate manual, approval-gated operation (design spec Section 28).

## When to Use This Builder

Use this builder when the user wants to create their AOS for the first time, or to stand up an additional AOS instance. The user typically reaches it through the root entry `/build-aos.md`.

Do not use it to add a single agent to an existing AOS — route that to the relevant `/builders/build-[agent-name]-agent.md`.

## Builder Operating Mode

- Behave as a blend of **executive coach** and **friendly collaborator** (Section 1.5): explain concepts in coach mode when the user needs orientation; switch to collaborator mode for design choices; recommend sensible defaults; ask for approval on important decisions; move forward with documented assumptions on low-risk details; defer to the user.
- **Default to dry-run / preview.** Describe the full set of folders and files to be created, then wait.
- Create no files until the user types exactly `Proceed` (Sections 3.1, 9.3).
- Apply the global file-safety rule and three-level permission model to everything this builder does.

## Interview Flow

Follow the batch pattern (Section 9.1):

```text
1. Ask a small batch of questions.
2. Summarize what the user said.
3. Recommend defaults for anything vague.
4. Ask for approval on important design decisions.
5. Generate a build plan / pre-build preview.
6. Ask the user to type Proceed before creating files.
```

The step-5 preview is shown before any files are created; it is distinct from the post-build AOS Setup Summary (Section 13, 9.1). If the user asks to move faster, reduce the number of questions and rely more on documented assumptions.

## Discovery Questions

Ask in small batches:

- What is this AOS for — personal, professional, or both? What outcomes matter most?
- What domains of work or life should it cover (for example: communications, scheduling, projects, research, writing, finance, health)?
- What should the AOS be named? (Propose a default; the name sets the instance root folder.)
- Which optional productive agents do you want first? (At least one is required — see Optional Agent Selection.)
- What are your communication and approval preferences (how cautious, how much autonomy)?
- Are there tools the AOS should know it can or cannot use yet?
- If this instance will run alongside another that shares an input channel (e.g. a single inbox feeding both `work-aos` and `personal-aos`), what **routing signals** distinguish it — its email aliases, sender domains, and project names? Capture these so `/aos-router.md` can differentiate instances rather than falling back to ASK.

## Recommended Defaults

- AOS name: a short, file-safe slug derived from the user's stated purpose (for example `work-aos`).
- Required agents: all four governance agents, always (Security, Memory, Chief of Staff, Review).
- Starter optional agent: recommend the one that best matches the user's top stated domain; if unclear, recommend the Task / Commitment Agent.
- Permissions: adopt the global three-level model unchanged; capture any user-specific tightening in `/configs/global-permissions.md`.
- Operating rhythms: install all five review workflows plus the four supporting workflows.

## AOS Setup Sequence

Follow the ten-step initial setup sequence (Section 9.3):

```text
0. (Pre-step) The factory framework already exists (generated from the design spec and installed as a Claude plugin).
1. Start the user-facing AOS setup interview.
2. Create the top-level folder structure.
3. Create global config, memory, log, workflow, template, inbox, and archive files.
4. Confirm builder files for all possible agents exist.
5. Build the required agents.
6. Ask the user to select at least one optional productive agent.
7. Build the selected optional agents.
8. Update the agent registry.
9. Update /aos-router.md with this instance's slug and routing signals.
10. Produce an AOS setup summary.
```

File creation in every step waits for `Proceed`.

## Folder Structure to Create

Create the AOS instance as a **sibling folder** of the framework, named for the chosen AOS name (Sections 4, 4.1). All instance-relative paths in the framework resolve against this root.

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
  /inbox
    /processed
  /archive
```

## Global Files to Create

Create these global files at the instance root (Section 6):

```text
/aos-manifest.md
/aos-map.md
/configs/global-permissions.md
/configs/agent-registry.md
/configs/tool-access-matrix.md
/memory/user-profile.md
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md
/logs/aos-decision-log.md
/logs/change-log.md
/workflows/daily-startup-workflow.md
/workflows/end-of-day-shutdown-workflow.md
/workflows/weekly-review-workflow.md
/workflows/monthly-review-workflow.md
/workflows/quarterly-review-workflow.md
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
/docs/aos-user-guide.html
```

Generate each markdown file with the file-type schema from Section 16 and lightweight YAML frontmatter (Section 15), stamping `spec_version` (and `aos_version` on instance files) per the Section 15 stamping rule. Generate `/docs/aos-user-guide.html` as a **projection** (Sections 14.8, 16.6): assemble it from the skeleton plus current instance data (registry, map, permissions), including a mandatory Table of Contents (with in-page anchors), a seeded Change Log immediately after the TOC, and an Invocation Reference table scoped to the agents actually installed; carry metadata via meta tags / an HTML comment rather than YAML. The guide is regenerable, so it is treated as a definition file with its Change Log entries as the data input. Run the Section 16.6 consistency checks before finishing.

## Required Agent Orchestration

Build all four governance agents by invoking their builders in order (governance before productivity — Section 1.6.2):

```text
/builders/build-security-agent.md
/builders/build-memory-agent.md
/builders/build-chief-of-staff-agent.md
/builders/build-review-agent.md
```

Each builder creates that agent's standard file set (Section 5.1). Required-agent interviews are short because their purpose is standardized (Section 26).

## Optional Agent Selection

- Present the optional roster (Section 7.2) in its defined order.
- The user **must** select at least one optional productive agent before setup is considered complete (Sections 2.3, 7.2). Do not finish setup with zero optional agents.
- For each selected agent, invoke `/builders/build-[agent-name]-agent.md`.
- Optional agents not selected remain `available` (their builder files already exist).

## Registry and Map Updates

- Update `/configs/agent-registry.md` with one row per agent: status, required flag, builder file, agent folder, notes. The Chief of Staff entry must note joint ownership of `/aos-router.md` (Section 10.3).
- Update `/aos-map.md` to distinguish installed, available-but-not-installed, required core, optional productive, paused, and retired agents.
- Log the build in `/logs/aos-decision-log.md` and `/logs/change-log.md`.
- In `/aos-manifest.md`, set `AOS Version` to the instance's initial `aos_version` **1.0.0** and `Spec Version` to the `spec_version` this instance was generated from (Sections 14.3, 14.3.1). Stamp every generated file's frontmatter with that `spec_version`, and instance files with `aos_version` (Section 15).
- **Update `/aos-router.md`** (workspace root, sibling to all instance folders): add the new instance slug to the `applies_to` front-matter list; add a classification-signals entry under §2 using the routing signals gathered in the interview (email aliases, sender domains, project keywords); if this is the first non-factory instance, set it as the default instance in §2; bump `last_updated` to today's date. Log this change in `aos-factory/logs/factory-routing-decision-log.md`.

## Instance Routing Signals

When this instance shares an input channel with another (e.g. one inbox feeds both `work-aos` and `personal-aos`), routing only produces different results once the instances' signals diverge. During the build, populate the instance-specific signals the router relies on so it can resolve automatically instead of asking every time:

- Email aliases and sender domains tied to this instance → capture in `/memory/user-profile.md` and `/memory/people.md`.
- This instance's project names → ensure `/memory/projects.md` is populated (the router matches `[instance]/projects` names).
- Add the manifest pointer blockquote under `# AOS Manifest`: "Instance selection is governed by `/aos-router.md`. Do not assume this instance is active."

Without these, the router correctly falls back to ASK rather than guessing — functional but noisier than necessary.

## Validation Checklist

Confirm the AOS is complete (Section 27):

```text
[ ] All required folders exist.
[ ] All required global files exist.
[ ] All four required agents are built and active.
[ ] At least one optional productive agent is built.
[ ] Agent registry has an entry for every agent.
[ ] AOS map is present and current.
[ ] Global permissions, tool access matrix, workflows, templates, and logs exist.
[ ] AOS User Guide (/docs/aos-user-guide.html) exists with a TOC, seeded Change Log, and Invocation Reference scoped to installed agents; Section 16.6 consistency checks pass.
[ ] aos-manifest.md records AOS Version (initial 1.0.0) and Spec Version; generated files carry spec_version (instance files also aos_version).
[ ] /aos-router.md applies_to list includes this instance and §2 has its classification signals.
```

The Review Agent audits completeness and consistency; the Security Agent audits permissions and tool access; the Memory Agent audits memory routing and boundaries.

## AOS Setup Summary

Produce a summary after the build (Section 13, 9.3 step 10). This is the post-build artifact, distinct from the step-5 pre-build preview:

- **AOS name and location:** the instance slug and its sibling-folder path.
- **Agents installed:** the four required governance agents plus each selected optional productive agent, with status.
- **Files and folders created:** the instance tree, global files, workflows, templates, and the AOS User Guide.
- **Key decisions and preferences captured:** name, autonomy/approval settings, and routing signals.
- **Routing:** confirmation that `/aos-router.md` now lists this instance and its §2 classification signals.
- **Open questions and next steps:** optional agents not yet installed and how to add them later (`Build the [X] Agent`).

Save each agent's own build record to `/agents/[agent-name]-agent/logs/[agent-name]-build-summary.md` (Section 13).
