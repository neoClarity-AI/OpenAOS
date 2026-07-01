# Open AOS Factory

## Why This Exists

Claude Cowork and Claude Code give you a powerful general-purpose platform: project memory, skills, subagents, plugins, scheduled tasks, and a permission system. What they deliberately don't give you is framework for assembling those primitives into a trustworthy, coordinated team of agents. A non-technical person has no straightforward path from the generic platform to agents built for their own specific needs. The **Open AOS Factory** closes that gap. It lets anyone turn the general-purpose platform into purpose-built, governed agents through an interview-style conversation.  No config, no code. Governance comes first, not as an afterthought. Every consequential action waits on a one-word human approval (`Proceed`), and the entire system is generated from a single canonical specification, so the design, the docs, and the shipped code cannot quietly drift apart.

## Overview

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), the design spec is a portable artifact. it can be rendered on Codex or any similar agentic platform.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install. It's a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

### What Makes the Open AOS Factory Unique?

The **Open AOS Factory** sits in three active areas of agent design and contributes a distinct combination rather than a single from-scratch invention.

**1. A factory that builds operating systems, not just agents.** "Agent factory" tooling already exists (Microsoft's Agent Factory, Mozilla's "agent-factory", Oracle's Private Agent Factory, research like MetaGPT and Automated Design of Agentic Systems). All of them generate *individual agents* or *multi-agent workflows*. The **Open AOS Factory** instead generates a complete, governed **Agentic Operating System** (workspace, persistent identity, shared memory, governance layer, router, and a coordinated agent team) and it builds and maintains a **fleet** of these systems, not just one. Factory-of-systems, not factory-of-agents, is the difference.

**2. A router that resolves across whole system instances.** Routing a request to the right *agent* is well-established. What's less common is a router that resolves across **separate, memory-isolated AOS instances** (for example, a personal AOS, a work AOS, a client AOS) using a priority-ordered resolution chain (explicit override → framework vs. instance → session pin → signal match → ask) where the router is itself a generated, spec-defined artifact that a non-technical user configures by talking, never by editing code.

**3. Mandatory governance agents that bootstrap the system.** "Governance-first" is now an emerging, named paradigm, but the literature treats governance as a *layer* or *control plane* bolted around the agents. This project makes governance **four required agents** (security/permissions, memory, coordination, and review/reflection) that *must* be instantiated before any productive agent exists. Governance isn't a wrapper; it's the founding membership of every system the factory builds.

Individually, each idea has neighbors in the field. The **combination** of a factory that generates governed AOS instances as a fleet, a cross-instance router, governance reified as required agents, all regenerated from a single canonical spec, and aimed at non-technical users, is one we have not found assembled in any single existing project. That combination is the contribution.

### How the Factory Relates to Claude Cowork and Claude Code

The Factory is not a replacement for the Claude Cowork and Code. Rather, the Factory is complements and extends them. These platforms provide the primitives and stays general-purpose by design. The Factory turns those primitives into a specific, governed system shaped to a user's needs.

Some of what the Factory adds is genuinely new ground: cross-instance routing with memory isolation, governance reified as required agents, and spec-driven regeneration of the whole system. Some of it deliberately overlaps the platform — most notably the `Proceed` gate (see below).

------

## Prerequisites

The factory implementation included with this repo requires:

- **The Claude Desktop application:** Required to run [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
- **A Claude subscription:** Also required to run Claude Cowork. Claude Pro is the minimum subscription level, and it's sufficient for most uses of the **Open AOS Factory**. See the [Claude plans page](https://claude.com/pricing) for the available options.
- **An active Internet connection:** Required by the Claude Desktop application.

---

## Pick Your Entry Point

You can adopt the factory at whatever depth suits you:

- **A Claude plugin:** easy install, no clutter.
- **A prebuilt factory:** fork the full repo to run it directly (built with Claude Opus 4.8, and can be rebuilt with newer models as they ship).
- **The design spec:** this is the best way to modify the factory itself and contribute to the open source project. Only pull requests for the design spec will be considered.

### Quick Start with the Claude Plugin

If you're using Claude Cowork, follow the instructions here: https://github.com/neoClarity-AI/neoClarity-Plugins/tree/main/aos-factory 

If you're using VS Code with Claude Code, follow these instructions:

**Using VS Code**

- **Install Claude on VS Code.** Instructions here: https://code.claude.com/docs/en/vs-code
- **Create a folder for the AOS.**  File -> Open Folder... -> New Folder. You can name it anything you like. For these instructions, lets call it **AOS Workspace**.
- **Install the aos-factory plugin.** In a Claude Code terminal session, enter these commands:
```
/plugin marketplace add https://github.com/neoClarity-AI/neoClarity-Plugins
/plugin install aos-factory@neoclarity-plugins
```

- **Create an AOS instance**. In a Claude Code terminal session, enter this command:

```
/biuld-aos help
```

- Review the overview to familiarize yourself with the skill, then proceed with the interview to create your first AOS instance.
- You can begin issuing commands to your new agents. See the **AOS User Guide** (`docs/aos-user-guide.html`) in the `docs` folder of your new AOS instance for details.

---

## Key Features

**Governance-first architecture.** Every AOS includes four required governance agents that must be set up before any productive agents are added. These agents own the system's safety, memory, coordination, and quality, not any one task domain.

**Three-level permission model.** Actions are classified as Level 1 (safe autonomous: the agent may act without asking), Level 2 (approval-required: the agent must describe the action and ask the user to type `Proceed`), or Level 3 (prohibited: the agent must not do this at all). The global tool-access matrix is the authoritative source for permissions and overrides any agent-level setting in the event of a conflict.

**Non-destructive by default.** No agent deletes, overwrites, renames, moves, or bulk-modifies files without explicit approval — when in doubt it creates a new file, appends to a log, or asks. Every Level 2 action requires the user to type exactly `Proceed`; anything short of that exact word is a hold. This sits on top of the platform's own safeguards by design: Cowork and Code already gate consequential actions, but both will sometimes edit files before you're ready, so the `Proceed` gate guarantees nothing changes until you're satisfied and gives you a clean point to abandon a direction before anything is committed.

**Single Responsibility Principle.** Each agent has a well-defined purpose and set of responsibilities. The Factory ensures that responsibilities don't overlap. For instance, the Chief of Staff agent coordinates and routes without taking on any other responsibilities.

**Works for personal and professional use.** The factory is designed as a reusable template. A user can build a personal AOS, a work AOS, or both, as sibling instances in the same workspace (see Repository Structure below). The user can build as many AOS instances as they need, with each specialized for a specific purpose. A routing mechanism activates the appropriate AOS and agents for a specific task.

**Scheduled, recurring work.** Agents don't only act when prompted. They run on a cadence. Each AOS includes daily, weekly, monthly, and quarterly operating rhythms: a daily start-of-day briefing and inbox pass driven by the Chief of Staff, plus a weekly review, a monthly health check and user-guide refresh, and a quarterly retrospective owned by the Review Agent. You approve the schedule once. The system maintains the rhythm so routine work happens on its own.

## Key Benefits

**You can trust it with real work.** Governance comes first, not as an afterthought. Before any productive agent is added, four governance agents (security, memory, coordination, and quality review) are already in place. The system never deletes, overwrites, or moves your files on its own. Anything consequential waits for you to type one word: `Proceed`.

**It's built for non-technical people.** Setup is an interview, not a config file. You talk. It builds. There's no command grammar to memorize. You trigger things by plain intent ("Start my day," "Process my inbox").

**It documents and improves itself.** Every system generates its own plain-language user guide, and a built-in review agent keeps it clean daily, healthy monthly, and aligned with your goals quarterly. It gets better on a schedule instead of rotting.

**It grows with you.** Run one AOS or many (work, personal, a client project) side by side, with smart routing that always picks the right one and never mixes their memories. Add new agents anytime without redesigning anything.

**It's designed to be forked and extended.** Everything is plain markdown built from standardized schemas. The whole system is generated from one canonical design spec, so the design, the docs, and even this pitch can't quietly drift apart. That same discipline is what makes outside contribution easy.

**It's portable.** Tuned for Claude, it easily adapts to other LLMs

---

## Available Agents

| Agent | Role |
|---|---|
| **Chief of Staff Agent** *(required)* | Owns orchestration, routing, prioritization, conflict resolution, and user-facing coordination. Joint owner of the instance router |
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
| Document Agent | Organizes, files, names, and retrieves documents |
| Automation / Tool-Use Agent | Wires up tools, integrations, and repeatable automations |

At least one optional productive agent must be added before initial AOS setup is considered complete.

---

## Repository Structure

```
Open AOS Factory/                ← project root
│
├── CLAUDE.md                    ← session-start instructions for Claude
├── aos-router.md                ← instance router (read first every session)
├── README.md
├── CONTRIBUTING.md
├── LICENSE
│
├── design-spec/                 ← canonical design specification document set
│   ├── aos-factory-design-specification.md  ← canonical design spec
│   ├── aos-factory-generation-runbook.md    ← build/regeneration runbook
│   └── aos-factory-revision-history.md      ← spec revision history
│
├── aos-factory/                 ← factory source (not an AOS instance)
│   ├── build-aos.md             ← entry-point pointer to the master builder
│   ├── builder-changelog.md
│   ├── builders/                ← 17 builder files (one per agent + master build-aos)
│   └── logs/
│       └── factory-routing-decision-log.md
│
└── claude-plugin/               ← packaged plugin (for Claude Cowork users)
    └── aos-factory/
        ├── .claude-plugin/
        │   └── plugin.json      ← plugin manifest
        ├── README.md
        ├── builder-changelog.md
        ├── skills/              ← 17 SKILL.md files, one per builder
        └── templates/           ← starter CLAUDE.md and aos-router.md to copy to workspace root
```

AOS instances are created as **sibling folders** at the project root alongside `aos-factory/`. For example: `work-aos/` or `personal-aos/`. The factory never writes into an instance except through an authorized build.

---

## Technical Overview

**Design philosophy.** The **Open AOS Factory** applies the **Single Responsibility Principle** at every level: each agent owns exactly one domain, and coordination is the Chief of Staff's job rather than being absorbed into a catch-all central agent. The governance layer (the four required agents) is mandatory because safety, memory, coordination, and quality review must exist before any productive work happens. Optional productive agents are additive and replaceable.

**`CLAUDE.md` and `aos-router.md`.** These two files are the load-bearing wiring of the system. `CLAUDE.md` is read by Claude at the start of every session. It sets Planning mode behavior and instructs Claude to resolve the active instance before doing anything else. `aos-router.md` is that resolution mechanism: it classifies each incoming request as targeting the factory, a specific AOS instance, or a cross-instance query, using a priority-ordered resolution chain (explicit user override → framework vs. instance → session pin → signal match → ask). Example copies of both files ship under `claude-plugin/aos-factory/templates/` and should be copied to the workspace root after install.

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

**Versioning.** Builder and plugin versions are tracked in `claude-plugin/aos-factory/builder-changelog.md`. Instance-level changes belong in each instance's own `/logs/change-log.md`.

---

## Open AOS Factory Design Specification

The canonical source of truth for the factory is `design-spec/aos-factory-design-specification.md`. It records every design decision made during the factory's development: the governance model, the permission levels, the folder schema, the builder section structure, agent responsibilities and boundaries, workflow definitions, escalation rules, and the framework-vs-instance layout. If the spec and a builder file ever disagree, the spec wins.

The spec is also the correct starting point for any change to the factory itself. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow.

---

## Maintainer and Project Status

The Open AOS Factory is built and actively maintained by Martin Danner, founder of neoClarity, with decades in software engineering, technical training, and IT management. neoClarity is a human-centered AI learning community focused on making capable AI accessible to non-technical professionals.

The project is under active development with ongoing commits on `main`, a published architecture and a spec-driven contribution model, and labeled good-first-issues for new contributors. The reference factory was built with Claude Opus 4.8 and is designed to be rebuilt as newer models ship. Issues and design-spec pull requests are welcome.

## Contributing

Contributions follow the same governance model the factory enforces for its own users: every change flows through the design specification first, and **only pull requests for the design spec will be considered.** See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full workflow, including how to propose a change, add a new agent builder, and what not to edit directly.
