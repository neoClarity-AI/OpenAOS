---
name: build-document-agent
description: "Build the Document Agent, an optional productive AOS agent that owns document management: filing, organizing, and retrieving documents and reference material across the AOS. Use when selected during AOS setup or later via 'Build the Document Agent'."
---

# Build Document Agent

## Builder Purpose

Build the Document Agent, an optional productive agent that owns document
management: filing, organizing, and retrieving documents and reference material
across the AOS (catalog: `document-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output preferences, approval
boundaries, collaboration; summarize; recommend defaults; preview; wait for
`Proceed`.

## Discovery Questions

- What document types and sources need cataloging?
- Preferred taxonomy and naming conventions?
- Confirm: moves, renames, archiving, and deletes are proposed, not acted on,
  without `Proceed`.

## Recommended Defaults

- Build and maintain a catalog/index; propose reorganizations rather than acting on
  them.
- Use file-safe slugs and the duplicate-suffix rule (Section 29); prefer copying to
  archive over moving when active context matters (Section 30).
- Receive finished content from Writing for filing.

## Configuration Decisions

- Taxonomy and naming conventions; catalog location; archive vs. copy policy.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/document-agent/document-agent.md
/agents/document-agent/memory/document-memory.md
/agents/document-agent/memory/document-learnings.md
/agents/document-agent/workflows/document-primary-workflow.md
/agents/document-agent/templates/document-output-template.md
/agents/document-agent/configs/document-config.md
/agents/document-agent/logs/document-decision-log.md
```

## Agent Instruction Generation Rules

Render `document-agent.md` to the Section 11 schema. Project **identity** from the
`document-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns document management — filing, organizing, and
  retrieving documents and reference material.
- Responsibilities ← `domains_owned`: `document-management`.
- Non-Responsibilities ← derived: does not author or draft content (writing).
- Inputs ← `writing`; Outputs ← `document-management`.
- Collaboration Rules ← `collaborates_with`: receives finished content from
  Writing; escalates priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (archive, move, or delete a
  stored document); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/document-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `document-primary-workflow.md` (Section 16.3): catalog → propose
reorganizations → execute approved file operations only after `Proceed`.

## Memory Generation Rules

Seed `document-memory.md` and `document-learnings.md` per Section 16.2. Keep
taxonomy and naming conventions current.

## Config Generation Rules

Write `document-config.md` (Section 16.1). `Inherited Rules` references global
permissions; emphasize that all move/rename/archive/delete operations are
`Proceed`-gated (Sections 3.2, 30).

## Logging Rules

Append-only `document-decision-log.md` (Section 16.5). Log approved file operations
and reorganization decisions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- No unapproved move/rename/archive/delete path; naming and duplicate rules
  followed (Section 29).
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/document-agent/logs/document-build-summary.md` (file_type
`build_summary`).
