---
title: Build AOS
file_type: aos_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build AOS

The master builder. It runs the interactive setup interview and, on `Proceed`,
creates a complete AOS instance as a sibling folder inside the AOS Workspace
(Section 4.1).

## Builder Purpose

Build a complete, governed AOS instance from this framework: its folder tree,
global files, the four required governance agents, and at least one user-selected
optional productive agent — all non-destructively and behind the `Proceed` gate.

## When to Use This Builder

Use when a user wants to create a new AOS instance ("Build my AOS", "Set up a new
AOS"). To add a single optional agent to an existing instance instead, use that
agent's `/builders/build-[agent-name]-agent.md` directly (Section 9.4).

## Builder Operating Mode

Combine coach and collaborator behavior (Section 1.5): explain concepts when the
user is unsure, collaborate on design choices, recommend sensible defaults, and
move forward with documented assumptions on low-risk details. Default to
dry-run / preview: describe what will be built and create nothing until the user
types exactly `Proceed` (Sections 3.1, 9.1). Never overwrite an existing file
without a separate `Proceed` (Sections 3.2, 28).

## Interview Flow

Follow the batch pattern (Section 9.1): (1) ask a small batch of questions,
(2) summarize the answers, (3) recommend defaults for anything vague, (4) ask for
approval on important decisions, (5) generate a build plan / pre-build preview,
(6) ask the user to type `Proceed` before creating files. If the user asks to move
faster, ask fewer questions and rely more on documented assumptions.

The step-5 build plan / pre-build preview is shown before any files are created;
it is distinct from the post-build AOS Setup Summary below.

## Discovery Questions

- What is this AOS for (work, personal, or a specific purpose)? — sets scope and
  the proposed name.
- What should the AOS be named? — becomes the instance root folder slug
  (Section 29); propose a default and let the user change it.
- Which optional productive agents do you want first? At least one is required
  (Sections 2.3, 7.2); the rest can be added later (Section 9.4).
- Any known people, projects, tools, or preferences to seed memory with?
- How much autonomy do you want by default, and where should approval always be
  required beyond the global rules (Section 3)?

## Recommended Defaults

- Install all four required governance agents (non-optional, Section 2.3).
- Recommend the Inbox, Task, and Calendar agents as a strong starting set for a
  productivity-focused AOS; recommend Research + Writing for a knowledge-work AOS.
- Propose the instance name from the stated purpose; seed empty (not fabricated)
  memory and log files.
- Global permissions inherit the Section 3 model unchanged unless the user asks
  for a stricter or looser baseline.

## AOS Setup Sequence

Follow the setup sequence in Section 9.3:

1. The factory framework already exists (this plugin).
2. Start the AOS setup interview.
3. Create the top-level folder structure.
4. Provision the AOS Workspace root: ensure `/aos-router.md` and `/CLAUDE.md`
   exist, copying them from the shipped example copies (`templates/aos-router.md`,
   `templates/CLAUDE.md`, Section 28.2). Create them if absent; overwrite an
   existing root file only after a separate `Proceed` (Sections 2.4, 3.2, 4.1).
5. Create global config, memory, log, workflow, template, inbox, and archive files.
6. Confirm builder files for all possible agents exist.
7. Build the four required agents.
8. Ask the user to select at least one optional productive agent.
9. Build the selected optional agents.
10. Update the agent registry and AOS map.
11. Produce an AOS setup summary.

No files are created until the user types `Proceed`.

## Folder Structure to Create

Create the Section 4 tree as a sibling AOS root `/[aos-name]/` (Section 4.1):

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
  /inbox
    /processed
  /archive
```

## Global Files to Create

Create the full Section 6 global file list, including `/docs/aos-user-guide.html`.
Generate the user guide from the Section 16.6 skeleton with the mandatory Table
of Contents, embedded Change Log (seeded with a single initial entry), and an
Invocation Reference table scoped to the agents actually installed. Enforce the
Section 16.6 consistency checks before finishing: every TOC entry resolves to a
matching `id` anchor, every section has a TOC entry, and the Change Log sits
immediately after the TOC with at least one dated entry.

Seed data files (memory, logs) empty or lightly seeded from the interview; write
definition files (workflows, templates, configs) as full renderings of their
Section 16–18 schemas. Stamp every generated file's frontmatter with
`spec_version: 2.0.0` and `aos_version: 1.0.0` (Sections 14.3.1, 15.2–15.3).

## Required Agent Orchestration

Build the four governance agents first, before any productive agent (governance
before productivity, Section 1.6.2), by invoking their builders:

```text
/builders/build-security-agent.md
/builders/build-memory-agent.md
/builders/build-chief-of-staff-agent.md
/builders/build-review-agent.md
```

## Optional Agent Selection

Present the Section 7.2 optional roster and require at least one selection before
setup is complete (Sections 2.3, 7.2). Build each selected agent via its
`/builders/build-[agent-name]-agent.md`. Leave unselected agents as `Available`
in the registry; their builders already exist so they can be added later
(Sections 8.1, 9.4).

## Registry and Map Updates

Write `/configs/agent-registry.md` (Section 10.3) and `/aos-map.md` (Section 10.4):
required agents as `Active`, selected optional agents as `Built`/`Active`, and the
rest as `Available`. Record the Chief of Staff Agent's joint ownership of
`/aos-router.md` in its registry entry (Section 10.3). Absorb each installed
agent's `domains_owned` and `artifacts_owned` into the registry and run the
instance-scope overlap check (Section 10.3.1).

## Validation Checklist

Use the Section 27 completeness checks:

- Required folders, required global files, and the AOS User Guide all present.
- Four required agents built; at least one optional productive agent built.
- Registry entries and AOS map present and consistent.
- Global permissions, tool access matrix, workflows, templates, and logs present.
- Each built agent has its full Section 5.1 file set.
- Catalog and profile validation (Sections 7A.5 V1–V8, 7B.5 V9–V10) passes.
- User-guide TOC / anchor / Change Log consistency checks pass (Section 16.6).

## AOS Setup Summary

After files are created, produce a setup summary listing: the instance name and
path, folders and global files created, agents built and their status, memory
seeded, open questions, and suggested next steps (e.g. selecting additional
optional agents). This is the post-build artifact, distinct from the step-5
pre-build preview.
