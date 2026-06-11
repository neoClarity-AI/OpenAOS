# Open AOS Factory

## Overview

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), it can be easily ported to work with Codex and possibly other platforms.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install — it is a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

---

## Prerequisites

- **Claude Cowork** (recommended for non-technical users) or **Claude Code** (v2.1.128 or later, required for zip-based plugin install)
- A workspace folder that Claude can read and write — Cowork will ask you to select one during setup
- No coding required; the factory is entirely conversational

---

## Quick Start

These steps are written for Claude Cowork users. Claude Code users can follow the same flow from the terminal.

1. **Install the plugin.** Open Cowork settings, go to Plugins, and install the **Open AOS Factory** plugin. If you received a `.plugin` zip file, use the "Install from file" option (requires Claude Code v2.1.128+).
2. **Open a new session** in your workspace folder.
3. **Start the build.** Type: `Build my AOS` — Claude will open the master builder and begin the setup interview.
4. **Answer the interview questions.** The builder acts as an executive coach and collaborator, asking about your work style, the agents you want, and how you want the system to behave. It recommends sensible defaults and documents decisions as it goes.
5. **Review the proposed files.** Before anything is created, Claude shows you exactly what it plans to write.
6. **Type `Proceed`** to authorize file creation. Nothing is written until you do.
7. Review the **AOS User Guide** (`docs/aos-user-guide.html`) in the `docs` folder of the AOS instance.
8. **Add more agents any time.** Once your AOS is running, you can add optional productive agents by asking Claude to build them (e.g., `Add an Inbox Agent to my AOS`).

---

## Key Features

**Governance-first architecture.** Every AOS includes four required governance agents that must be set up before any productive agents are added. These agents own the system's safety, memory, coordination, and quality — not any one task domain.

**Non-destructive by default.** No agent may delete, overwrite, rename, move, or bulk-modify files without explicit user approval. When in doubt, agents create a new file, append to a log, or ask for clarification rather than modify something that already exists.

**Three-level permission model.** Actions are classified as Level 1 (safe autonomous — the agent may act without asking), Level 2 (approval-required — the agent must describe the action and ask the user to type `Proceed`), or Level 3 (prohibited — the agent must not do this at all). The global tool-access matrix is the authoritative source for permissions and overrides any agent-level setting in the event of a conflict.

**`Proceed` gate.** Every Level 2 action requires the user to type exactly `Proceed`. A summarized description of the action is not enough; anything short of that exact word is treated as a hold. This applies to the factory builders and to agents in a running AOS instance alike.

**Single Responsibility Principle.** Each agent has a defined purpose, a list of explicit non-responsibilities, and clear escalation rules. The Chief of Staff coordinates and routes; it does not absorb work that belongs to a specialized agent.

**Works for personal and professional use.** The factory is designed as a reusable template. A user can build a personal AOS, a work AOS, or both — as sibling instances in the same workspace (see Repository Structure below). The user can build as many AOS instances as they need, with each specialized for a specific purpose. A routing mechanism activates the appropriate AOS and agents for a specific task.

---

## Available Agents

| Agent | Role |
|---|---|
| **Chief of Staff Agent** *(required)* | Owns orchestration, routing, prioritization, conflict resolution, and user-facing coordination; joint owner of the instance router |
| **Security / Permissions Agent** *(required)* | Owns the global permission rules, tool-access matrix, approval requirements, and safety checks |
| **Memory Agent** *(required)* | Owns shared memory structure, memory hygiene, preference capture, and cross-agent memory routing |
| **Review / Reflection Agent** *(required)* | Owns completeness audits, consistency checks, retrospectives, and quality review |
| Task / Commitment Agent | Tracks tasks, commitments, deadlines, and follow-ups |
| Calendar / Scheduling Agent | Manages scheduling, meetings, and time blocking |
| Inbox / Communications Agent | Triages email and messages, drafts replies, and runs the inbox-to-task workflow |
| Project Manager Agent | Runs projects, milestones, kickoffs, and status tracking |
| Research Agent | Gathers, synthesizes, and cites information |
| Writing / Content Agent | Drafts, edits, and refines written content |
| Finance / Admin Agent | Handles finances, budgets, invoices, and administrative tasks |
| Health / Life Logistics Agent | Manages health appointments, errands, and life logistics |
| Learning / Tutor Agent | Builds study plans, explains concepts, and tracks learning goals |
| Personal CRM Agent | Tracks people, relationships, interactions, and follow-ups |
| Document Librarian Agent | Organizes, files, names, and retrieves documents |
| Automation / Tool-Use Agent | Wires up tools, integrations, and repeatable automations |

At least one optional productive agent must be added before initial AOS setup is considered complete.

---

## Repository Structure

```
AOS/                             ← project root
│
├── claude.md                    ← session-start instructions for Claude
├── aos-router.md                ← instance router (read first every session)
│
├── design-spec/                 ← canonical design specification document set
│   └── aos-factory-design-specification.md  ← canonical design spec
│
├── aos-factory/                 ← factory source (not an AOS instance)
│   ├── build-aos.md             ← entry-point pointer to the master builder
│   ├── builders/                ← one builder file per agent + master build-aos
│   └── logs/
│       └── factory-routing-decision-log.md
│
└── dist/                        ← packaged plugin (what gets distributed)
    └── aos-factory/
        ├── .claude-plugin/
        │   └── plugin.json      ← plugin manifest
        ├── skills/              ← 17 SKILL.md files, one per builder
        ├── examples/            ← starter aos-router.md and claude.md to copy
        └── builder-changelog.md
```

AOS instances are created as **sibling folders** at the project root alongside `aos-factory/` — for example, `work-aos/` or `personal-aos/`. The factory never writes into an instance except through an authorized build.

---

## Technical Overview

**Design philosophy.** The **Open AOS Factory** applies the **Single Responsibility Principle** at every level: each agent owns exactly one domain, and coordination is the Chief of Staff's job rather than being absorbed into a catch-all central agent. The governance layer (the four required agents) is mandatory because safety, memory, coordination, and quality review must exist before any productive work happens. Optional productive agents are additive and replaceable.

**`claude.md` and `aos-router.md`.** These two files are the load-bearing wiring of the system. `claude.md` is read by Claude at the start of every session; it sets Planning mode behavior and instructs Claude to resolve the active instance before doing anything else. `aos-router.md` is that resolution mechanism — it classifies each incoming request as targeting the factory, a specific AOS instance, or a cross-instance query, using a priority-ordered resolution chain (explicit user override → framework vs. instance → session pin → signal match → ask). Example copies of both files ship under `dist/aos-factory/examples/` and should be copied to the workspace root after install.

**Builder schema.** Each builder file in `builders/` follows a standardized YAML front matter schema (`title`, `file_type`, `builder_version`, `schema_version`, `created_date`, `last_updated`, `status`, `compatible_aos_versions`, `requires_approval_for_overwrite`) and a common markdown section structure: Builder Purpose, When to Use, Builder Operating Mode, Interview Flow, Discovery Questions, Recommended Defaults, Configuration Decisions, and Output Files. This consistency allows the factory to be extended with new agent builders without redesigning the document format.

**What a built instance looks like.** When `build-aos` completes an authorized build, it creates a folder with the user's chosen AOS name containing:

```
[aos-name]/
  agents/          ← one subfolder per installed agent
  workflows/       ← cross-agent workflow files
  memory/          ← shared memory and user profile
  projects/        ← active project folders
  logs/            ← decision and activity logs
  templates/       ← reusable document templates
  configs/         ← global permissions, tool-access matrix, preferences
  docs/            ← the AOS User Guide and build documentation
  inbox/
    processed/
  archive/
```

**Versioning.** Builder and plugin versions are tracked in `dist/aos-factory/builder-changelog.md`. Instance-level changes belong in each instance's own `/logs/change-log.md`.

---

## Open AOS Factory Design Specification

The canonical source of truth for the factory is `design-spec/aos-factory-design-specification.md`. It records every design decision made during the factory's development: the governance model, the permission levels, the folder schema, the builder section structure, agent responsibilities and boundaries, workflow definitions, escalation rules, and the framework-vs-instance layout. If the spec and a builder file ever disagree, the spec wins.

The spec is also the correct starting point for any change to the factory itself. The workflow is: propose a change in the spec → review with the user → receive explicit approval → regenerate the affected builder file(s) → rebuild and repackage `dist/`. Direct edits to builder files in `builders/` or skill files in `dist/` without a corresponding spec update are discouraged; they create drift between the design record and the implementation.

The spec uses the same `Proceed` gate as the rest of the system. No regeneration of factory files happens without that explicit authorization.

---

## Contributing

Contributions to the **Open AOS Factory** follow the same governance model the factory enforces for its own users: every change flows through the design specification first. Use this guide to learn how to contribute to this Github project: [Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

**To propose a change:**

1. Open `design-spec/aos-factory-design-specification.md` and identify the section(s) your change affects.
2. Draft the proposed revision and discuss it in a Planning mode session (`pmode` at the start of your Claude session). Claude will not create or modify any files in this mode.
3. Once the revision is agreed, type `Proceed` to authorize the spec update.
4. Identify which builder file(s) in `builders/` are affected by the spec change and regenerate them (one builder at a time, each gated by `Proceed`).
5. Update `dist/` by rebuilding the plugin package, bump the version in `plugin.json`, and add an entry to `dist/aos-factory/builder-changelog.md`.

**What not to do:** Do not edit builder files in `builders/` or skill files in `dist/aos-factory/skills/` directly without first updating the spec. The spec is the design record; a builder that diverges from it is a bug.

**Adding a new agent builder** follows the same sequence plus one additional step: add the new agent to the available-agent roster in the spec (Section 2.3 or equivalent), define its full section schema, then generate the builder file and SKILL.md together.

For questions or to discuss larger architectural changes before drafting spec language, open an issue 