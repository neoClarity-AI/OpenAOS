---
title: AOS Workspace Instructions
file_type: project_instructions
spec_version: 2.1.3
---
# AOS Workspace Instructions

This is the AOS Workspace root. Copy this file (and `aos-router.md`) here after
installing the `aos-factory` plugin. These instructions apply to every request in
this workspace. Required sections follow (§16.11).

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
