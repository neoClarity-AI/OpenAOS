---
name: build-document-librarian-agent
description: "Add a Document Librarian Agent to an AOS instance — organizes, files, names, and retrieves documents. Use when adding this optional agent during setup, installing it later, or rebuilding the document librarian agent."
---


# Build Document Librarian Agent

## Builder Purpose

Build the **Document Librarian Agent**, an optional productive agent that organizes, catalogs, and helps retrieve documents and files. A specialized worker, not a coordinator (Section 7.6).

## When to Use This Builder

When selected during setup, or later via "Build the Document Librarian Agent" (Section 9.4).

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`.

## Interview Flow

Fuller optional-agent interview (Section 26): goals, scope, tools, output preferences, approval boundaries, collaboration.

## Discovery Questions

- What documents/files should the librarian organize, and where do they live?
- Preferred naming, tagging, and folder conventions?
- How should duplicates and obsolete files be handled?
- What retrieval needs are most common?

## Recommended Defaults

- Build and maintain a catalog/index; creating index files is Level 1 safe.
- **Moving, renaming, archiving, overwriting, or deleting files is approval-required** (`Proceed`) per Sections 3.2 and 30 — propose, do not act.
- Prefer copying to archive over moving when active context matters (Section 30).
- Use file-safe slugs and the duplicate-suffix rule (Section 29).

## Configuration Decisions

- Confirm naming/tagging conventions and catalog location.
- Confirm that all destructive or move operations route through approval.
- Confirm collaboration with Project Manager and Research agents.

## Files to Create

```text
/agents/document-librarian-agent/document-librarian-agent.md
/agents/document-librarian-agent/memory/document-librarian-memory.md
/agents/document-librarian-agent/memory/document-librarian-learnings.md
/agents/document-librarian-agent/workflows/document-librarian-primary-workflow.md
/agents/document-librarian-agent/templates/document-librarian-output-template.md
/agents/document-librarian-agent/configs/document-librarian-config.md
/agents/document-librarian-agent/logs/document-librarian-decision-log.md
```

## Agent Instruction Generation Rules

Generate `document-librarian-agent.md` per Section 11 with `agent_instruction` frontmatter. Non-Responsibilities must stress that it never moves/renames/archives/deletes files without approval and does not own project structure. Include example requests.

## Workflow Generation Rules

Create `document-librarian-primary-workflow.md` (Section 16.3) for cataloging, proposing reorganizations, and executing approved file operations only after `Proceed`.

## Memory Generation Rules

Create `document-librarian-memory.md` and `document-librarian-learnings.md` (Section 16.2). Store taxonomy and naming conventions.

## Config Generation Rules

Create `document-librarian-config.md` (Section 16.1) referencing global permissions and the tool access matrix.

## Logging Rules

Create `document-librarian-decision-log.md` (Section 16.5). Log convention decisions and approved file operations.

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] All move/rename/archive/delete operations gated behind Proceed.
[ ] Naming and duplicate-handling conventions documented.
[ ] Tool access references the global matrix.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13) with a suggested next agent.
