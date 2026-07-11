<!-- file_type: project_instructions | spec_version: 2.2.0
     Example AOS Workspace root file, shipped with the aos-factory plugin (spec §16.10, §28.2).
     Copy this file to your AOS Workspace root as CLAUDE.md and edit it for your setup.
     During AOS setup, build-aos provisions it automatically when absent; it never
     overwrites an existing root file without a separate Proceed. -->

# AOS Workspace Instructions

This workspace hosts the AOS Factory and exactly one AOS instance as sibling folders.

## Factory-vs-instance guard

Before running any workflow, determine whether the request targets the **AOS Factory** (building or rebuilding the AOS or its agents) or the **AOS instance** (day-to-day work with your agents, workflows, memory, and projects).

- If the request is ambiguous, **ask — never silently guess**.
- The Chief of Staff Agent owns this guard and logs non-trivial guard decisions to its decision log (`/agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md`).

## Approval rules (the `Proceed` gate)

- Never delete, overwrite, rename, move, archive, or bulk-modify files — and never send, publish, spend, or share private information — without explicit approval.
- Consequential actions require the user to type exactly: `Proceed`
- Approval is action-specific: a `Proceed` authorizes only the action described immediately before it, never a standing grant.
- Refining or discussing a plan is NOT approval. Only the exact word counts.

## Include the standard AGENTS.md file

@AGENTS.md
