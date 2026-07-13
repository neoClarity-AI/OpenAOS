---
title: AOS Workspace Instructions (Example)
file_type: project_instructions
spec_version: 2.3.2
---
# AOS Workspace — Session Instructions

This is an **example** workspace-root `/CLAUDE.md`. During AOS setup,
`build-aos` provisions it into your AOS Workspace root (creating it when absent;
overwriting an existing one only after a separate `Proceed`). Edit it for your
setup after install. It renders the schema in the design spec §16.10.

## Factory-vs-Instance Guard

Before running any workflow, determine whether the request targets the **AOS
Factory** (`aos-factory/`, the builders) or the **generated AOS instance**
(`/[aos-name]/`). There is one AOS Workspace hosting the factory and exactly one
AOS instance as sibling folders (single-instance model, §1.6.6) — there is no
separate router file.

- If the request is ambiguous, **ask — do not silently guess** which target is
  meant.
- The Chief of Staff Agent owns this guard and logs non-trivial guard decisions
  to its own decision log (`/[aos-name]/agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md`).

## Planning-Mode Rules

- Planning mode is active when the user's message begins with "Planning mode" or
  "pmode".
- While in planning mode: show reasoning; offer options with a recommendation;
  do **not** create, edit, rename, move, or delete any files; only read,
  research, and present a proposed plan. Wait for the user to type exactly
  `Proceed` before making any changes.
- `Proceed` is the **only** exact-string command in the AOS. It is the approval
  gate for every Level 2 action (design spec §3.1); refining or approving a plan
  in conversation is not a `Proceed`.

## Include AGENTS.md

@AGENTS.md
