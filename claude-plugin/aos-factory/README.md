# AOS Factory — Claude Plugin

Build a complete, governed **Agentic Operating System (AOS)** — a personal or
professional system of specialized markdown agents, workflows, memory, templates,
configs, logs, and documentation — through a guided, approval-gated interview.

This plugin is a rendering of the AOS Factory design specification
(`spec_version 2.3.2`). The specification is the single source of truth; this
package is generated from it (design spec §1.6.1, §28).

## What's in the box

```text
.claude-plugin/plugin.json     Plugin manifest (name, version, author)
skills/
  build-aos/SKILL.md           Stand up a full AOS instance (master builder)
  build-agent/SKILL.md         Build one agent — the generic engine, covers every agent
agent-catalog.yaml             Agent identity/ownership catalog (read-only in instances)
agent-specs/[agent]/           profile.md + interviews.md for all 15 agents
aos-interviews.md              AOS-level setup interview script
builder-changelog.md           Framework/plugin changelog
templates/
  CLAUDE.md                    Example workspace-root session instructions
  AGENTS.md                    Example workspace-root cross-agent rules
```

The agents built by this factory:

- **Required governance (always built, cannot be removed):** Security, Memory,
  Chief of Staff, Review, Feedback.
- **Optional productive (choose at least one):** Tutor, Inbox, Calendar, Task,
  Project Manager, Research, Writing, Document, Personal CRM, Automation.

## Install

**Via marketplace (recommended):**

```text
/plugin marketplace add neoClarity-AI/Open-AOS-Factory
/plugin install aos-factory
```

**Local, without installing (for testing):**

```text
claude --plugin-dir <path-to>/claude-plugin/aos-factory
```

Local `.zip` loading requires Claude Code v2.1.128 or later.

## Usage

1. **Build your AOS.** Ask to *"Build my AOS"* (or run the `build-aos` skill).
   The builder runs a short setup interview — purpose, name, and which optional
   agents you want first — then previews everything it will create.
2. **Approve.** Nothing is written until you type exactly `Proceed`. `Proceed`
   is the **only** exact-string command in the AOS; it is the approval gate for
   every consequential action (design spec §3.1).
3. **Provision the workspace root.** During setup the builder provisions
   `/CLAUDE.md` and `/AGENTS.md` at your AOS Workspace root from the shipped
   `templates/` examples — non-destructively (created when absent; an existing
   file is overwritten only after a separate `Proceed`).
4. **Add agents later.** Ask to *"Build the Research Agent"* (or any agent) to
   run the generic `build-agent` engine against an existing instance.

## Safety model

- **Non-destructive by default** — agents create, append, or ask; they never
  delete, overwrite, move, rename, or archive without explicit approval.
- **Approval is action-specific** — a `Proceed` authorizes only the action just
  described, never future ones.
- **Governance before productivity** — the five governance agents are built
  first and cannot be removed.

## Contributing

Changes flow through the design specification only. The repository accepts pull
requests **against the spec**; the factory and this plugin are regenerated and
published from the approved spec (design spec §1.6.10).

Project home: https://github.com/neoClarity-AI/Open-AOS-Factory
