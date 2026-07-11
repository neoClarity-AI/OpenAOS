---
title: AOS Workspace Instructions
file_type: project_instructions
spec_version: 2.2.2
---
# AOS Workspace Instructions

This is the AOS Workspace root. Copy this file (and `aos-router.md`) here after
installing the `aos-factory` plugin. These instructions apply to every request in
this workspace. Required sections follow (§16.11).

## Router Wiring

Before any workflow, read `/aos-router.md` and resolve the active target using its
Resolution Order. Exactly one target (the factory framework or a single instance)
is active per request. Never blend instance memory; for a cross-instance request,
run each instance separately with labeled output. State the resolved target on the
first line of any routed output (e.g. `**[work-aos]** …`). If routing is ambiguous
or signals are mixed or weak, ASK — do not silently pick.

## Planning-Mode Rules

- Planning mode is active when the user's message begins with "Planning mode" or
  "pmode".
- While in planning mode:
  - Always show reasoning.
  - Offer options and a recommendation when an issue is identified.
  - Do NOT create, edit, rename, move, or delete any files.
  - Only read files, research, and present a proposed plan.
  - Wait for the user to type exactly: `Proceed` — before making any changes.
- Refining, adjusting, or approving a plan in conversation is NOT a `Proceed`.
  Only the exact word counts. This exact-`Proceed` gate applies to every
  file-creating or destructive action (§2.5, §3.1–§3.2), not only planning mode.

## Include the standard AGENTS.md file

@AGENTS.md
