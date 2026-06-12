---
title: AOS Factory Design Specification
file_type: design_spec
project: Script to Build Agentic OS Factory
created_date: 2026-06-02
last_updated: 2026-06-11
spec_version: 1.0.5
status: design_ready_for_factory_generation
important_constraint: Do not generate actual AOS Factory files unless the user explicitly types exactly Proceed.
---

# AOS Factory Design Specification

## Purpose of This Document

This document is the consolidated design specification for the **Agentic Operating System (AOS) Factory**.

This document is a design artifact only. It does **not** authorize creation of actual AOS Factory files.

The assistant must not generate actual AOS Factory files unless the user explicitly types exactly:

```text
Proceed
```

## Required Next-Step Instructions

The assistant continuing from this document must:

```text
- Review the next steps with the user.
- The user may ask additional questions about the design or next steps.
- Wait for the user to enter the exact instruction “Proceed” to generate the AOS Factory files.
```

## Document Set

This specification is maintained as a small set of companion files in this folder:

```text
aos-factory-design-specification.md   - the canonical design (this file), Sections 1-32
aos-factory-generation-runbook.md     - build, generation scope, and handoff procedure (Sections 33-37)
aos-factory-revision-history.md       - dated revision and consistency-resolution history
```

The canonical specification remains the single source of truth (Section 1.6.1); the companion files are extracted from it for readability and are governed by the same `Proceed` safety gate.

## Revision History

The full revision history of this specification — including all dated Design Consistency Resolution cycles — is maintained in a companion file:

```text
aos-factory-revision-history.md
```

Entries there are maintained in reverse chronological order (newest first); new entries are added at the top. Each release is a single entry headed `## <spec_version> — <title> (<date>)`, with resolved items as a numbered list whose bold lead-in names the issue. A version table at the top of the file maps each `spec_version` to its date and a one-line summary.

`spec_version` increments once per completed maintenance action. A full §36.1 consistency-review cycle is one increment and one consolidated entry — not one per re-read iteration, however many iterations the loop takes. A structural change (for example, a document restructure) is its own separate increment.

---

# 1. Project Overview

## 1.1 Project Name

Working project name:

```text
AOS Factory Project
```

The generated system is referred to as:

```text
Agentic Operating System
AOS
```

The builder framework is referred to as:

```text
AOS Factory
Reusable AOS Factory
```

Three terms are used together throughout this document and should not be conflated:

```text
AOS Workspace  - The top-level container. Its root holds the workspace-governing
                 files (/aos-router.md, /CLAUDE.md). The AOS Factory and each
                 AOS instance live inside it as sibling folders.

AOS Factory    - The reusable builder framework (aos-factory/) that generates
                 AOS instances.

AOS            - A generated Agentic Operating System instance (/[aos-name]/),
                 a sibling of the AOS Factory within the AOS Workspace.
```

## 1.2 Target Platform

The current target platform is:

```text
Claude Cowork
```

Portability to other platforms may be considered later, but is outside the current design scope.

## 1.3 Overall Purpose

The AOS Factory should help a user collaboratively create a personal or professional Agentic Operating System composed of specialized markdown-based agents, workflows, memory files, templates, configs, logs, routines, and project documentation.

The builder is intended to be:

```text
A reusable template others could adopt.
```

It should not be only a one-off personal productivity setup, although it should work well for personal productivity.

## 1.4 What the AOS Factory Ultimately Produces

When authorized, the AOS Factory may produce:

```text
- Agent instruction files
- Agent builder files
- Build documentation
- Workflows
- Configuration files
- Decision logs
- Daily, weekly, monthly, and quarterly operating routines
- Templates
- Memory files
- The actual folder structure for the AOS
```

The system should actually create folders and files when authorized, not merely describe them.

## 1.5 Build Process Philosophy

The build process should feel like a combination of:

```text
Executive coach
Friendly collaborator
```

The builder should:

```text
- Explain concepts in coach mode when needed.
- Switch to collaborator mode when making design choices.
- Recommend sensible defaults.
- Ask for approval on important design decisions.
- Move forward with documented assumptions for low-risk details.
- Defer to the user’s wishes.
```

## 1.6 Design Principles and Goals

This section states the principles and goals that motivate the rest of this specification. Section 2 and beyond define *how* the AOS Factory behaves; this section defines *why*. When a future design decision is ambiguous, it should be resolved in favor of these principles. They are normative, not aspirational.

### 1.6.1 Design Spec as the Single Source of Truth

The AOS Factory is generated from this design specification, not the other way around. The spec is canonical; the factory framework, the builder files, the plugin package, and any outward-facing description of the project are all **renderings** of it.

```text
- Every builder, agent schema, workflow, and config traces back to a decision
  recorded here.
- When the spec and a generated artifact disagree, the spec wins and the
  artifact is corrected.
- Outward-facing material (README, pitch, user guide) derives from the spec so
  that documentation and marketing cannot silently drift away from the design.
```

This is what makes the system auditable and reproducible: anyone can regenerate the factory from the spec and get the same result.

### 1.6.2 Governance Before Productivity

Safety, memory, coordination, and quality review must exist before any productive work happens. The four required governance agents (Security, Memory, Chief of Staff, Review) are mandatory and are built before any optional productive agent (Section 2.3). Productivity is additive; governance is foundational. A user cannot end up with a fast, capable, ungoverned system.

### 1.6.3 Single Responsibility at Every Level

Each agent owns exactly one domain, with explicit non-responsibilities and escalation rules; coordination is the Chief of Staff's job rather than being absorbed into a catch-all central agent (Sections 2.1, 2.2). The same discipline applies to files: one file, one purpose, scope recoverable from its path. This keeps the system legible to non-technical users and extensible without redesign.

### 1.6.4 Non-Destructive and Approval-Gated by Default

The system prefers actions that cannot lose work. Agents create, append, or ask rather than overwrite, delete, move, or bulk-modify (Section 2.4). Anything consequential is gated behind a single, unambiguous approval signal — the user typing exactly `Proceed` (Section 3.1) — and approval is specific to the action described, never a standing grant (Section 2.5). The goal is that a user can trust the AOS with real work without fear that it will quietly damage their files.

### 1.6.5 Standardization and Extensibility

Uniform schemas — builder files, agent instruction files, configs, memory, workflows, logs (Sections 11, 12, 15, 16) — let new agents and capabilities be added without inventing new formats. The factory ships builder files for every approved agent even when they are not initially installed (Section 8.1), so the collection is extensible by design rather than by exception.

### 1.6.6 Multiple Instances, Intelligent Routing

One workspace can host the factory framework and many AOS instances (work, personal, or purpose-specific) as siblings, with a router that resolves exactly one active target per request and never blends instance memory (Section 4.1 and the instance router). A user grows from one AOS to several without re-architecting.

### 1.6.7 Self-Documenting and Self-Improving

The system explains itself and improves itself on a cadence. Every instance generates a plain-language HTML user guide (Section 16.6). A set of operating rhythms running from daily through quarterly keeps the system operationally clean, structurally healthy, and aligned with the user's actual goals (Section 25). The Review Agent owns the improvement rhythms — the weekly review, the monthly review (including the user-guide refresh), and the quarterly review — while the daily startup and end-of-day rhythms are driven by the Chief of Staff Agent (Sections 17.1–17.5, 7.4). Maintenance is a built-in behavior, not a manual afterthought.

### 1.6.8 Built for Non-Technical Users, Portable Across Platforms

The primary user is non-technical and the primary interface is conversational: setup is an interview, invocation is by intent-matched trigger phrases, and the only exact-string command is `Proceed` (Sections 1.5, 9.1, 16.6). The target platform is Claude Cowork, but because the entire system is plain markdown plus a thin routing layer, it is portable to Claude Code and adaptable to other LLMs. The design avoids platform-specific mechanisms wherever a portable one exists.

### 1.6.9 Multiple Delivery Formats

The same design is consumable at three levels of readiness, so adopters can enter at whatever depth suits them:

```text
- The design specification — for those who want to understand or fork the design.
- A prebuilt factory instance — for those who want to run it directly.
- A Claude plugin — for those who want one-step install (Section 28).
```

The prebuilt factory instance was generated using Claude Opus 4.8. Because the spec is the single source of truth (Section 1.6.1), the instance can be regenerated against newer models as they ship; the model used is a property of a given build, not of the design.

### 1.6.10 Open Source

The project is released openly in the hope of attracting contributors and evolving into a widely used application on Claude. Openness reinforces the principles above: a single-source-of-truth spec, standardized schemas, and self-documenting output are precisely what make external contribution tractable.

The project is hosted at:

```text
https://github.com/neoClarity-AI/Open-AOS-Factory
```

The contribution model follows directly from Section 1.6.1 (design spec as the single source of truth). The repository accepts pull requests **only against the design specification**. The prebuilt factory instance and the Claude plugin are not accepted as direct contributions; they are regenerated and published by neoClarity from the approved spec, so that quality and safety can be maintained and every released artifact provably traces back to a reviewed design. Although you can generate your own factory and plugin, the way to change the "official" neoClarity factory or plugin is to change the spec.

### 1.6.11 Goals (Summary)

```text
G1. Give non-technical users a full-featured, extensible, self-improving AOS.
G2. Keep the system safe and trustworthy by default (governance-first,
    non-destructive, approval-gated).
G3. Keep the design auditable and reproducible (spec as single source of truth).
G4. Keep the system extensible without redesign (standardized schemas,
    builder-per-agent).
G5. Support many instances with reliable routing and no memory bleed.
G6. Stay portable across Claude Cowork, Claude Code, and other LLMs.
G7. Be self-documenting and self-maintaining.
G8. Be open source and contributor-friendly.
```

---

# 2. Core Architectural Principles

## 2.1 Single Responsibility Principle

The AOS should follow the **Single Responsibility Principle**.

Each agent should have a clear purpose, responsibilities, non-responsibilities, inputs, outputs, boundaries, and escalation rules.

The system should avoid creating a bloated central agent that does everything.

## 2.2 Chief of Staff as Coordinator, Not Universal Worker

The **Chief of Staff Agent** should coordinate, route, prioritize, and resolve conflicts.

As much responsibility as possible should be pushed down to specialized agents.

## 2.3 Required Governance Layer Plus Optional Productive Agents

The AOS should have a small required governance layer and optional productive agents.

Required governance agents:

```text
1. Security Agent
2. Memory Agent
3. Chief of Staff Agent
4. Review Agent
```

Optional productive agents are selected by the user. The user must select at least one optional productive agent before initial AOS setup is considered complete.

## 2.4 Non-Destructive by Default

The AOS should prefer non-destructive actions.

Agents should create new files, append to logs, create dated or versioned copies, or ask for clarification when the safest action is unclear.

No agent may delete, overwrite, rename, move, archive, or bulk-modify files without explicit approval.

## 2.5 Approval Is Action-Specific

User permission applies only to the specific action described by the agent.

```text
- Permission to modify one file does not imply permission to modify other files.
- Permission to perform one overwrite does not imply permission for future overwrites.
- Permission to proceed with a batch action applies only to the listed files and changes.
```

---

# 3. Global Safety and Approval Rules

## 3.1 Global File Safety Rule

```text
Never delete, overwrite, rename, move, archive, or bulk-modify files unless the user has given explicit permission.

When an agent proposes one of these actions, it must first:

1. Explain exactly what action it wants to take.
2. Identify the affected file or files.
3. Explain why the action is recommended.
4. Explain the likely consequence of the action.
5. Ask the user to type exactly: Proceed

If the user does not type Proceed, the agent must not take the action.

The agent may suggest safer alternatives, such as copying the file, creating a backup, appending new content, or creating a new versioned file instead of modifying the original.
```

## 3.2 Actions Requiring Explicit Approval

The following actions always require approval:

```text
- Delete files
- Overwrite files
- Rename files
- Move files (except moving items into /inbox/processed under the approved inbox-to-task workflow, which is pre-authorized as part of that workflow — see Sections 17.6 and 31)
- Archive files
- Bulk-modify files
- Send messages
- Publish content
- Spend money
- Share private information
- Change calendar events involving other people
- Make irreversible or difficult-to-reverse changes
- Pause or retire an agent
- Refresh, replace, or overwrite existing builder files
- Restore a retired agent to Active status
```

The user must type exactly:

```text
Proceed
```

## 3.3 Safe Autonomous Actions

Agents may autonomously perform low-risk actions such as:

```text
- Create new files
- Create new folders
- Append to logs
- Draft content
- Summarize information
- Propose plans
- Create non-destructive templates
- Read files within their approved scope
- Recommend next actions
```

This is allowed only when the action does not overwrite, delete, move, rename, archive, publish, send, spend money, or expose private information.

## 3.4 Permission Levels

The AOS uses a three-level permission model:

```text
Level 1: Safe autonomous actions
The agent may do these without asking.

Level 2: Approval-required actions
The agent may recommend these, but must ask the user to type Proceed.

Level 3: Prohibited actions
The agent must not do these at all.
```

## 3.5 Global Versus Agent-Specific Permissions

Global permissions establish the baseline.

Agent permission settings within the agent config should not duplicate the global permissions by default.

Agent-level permissions should include only:

```text
1. Additional permissions granted to that agent
2. Restrictions specific to that agent
3. Explicit overrides to global defaults
4. Tool access and memory access boundaries
5. Escalation triggers unique to that agent
```

---

# 4. Top-Level AOS Folder Structure

The generated AOS should use this top-level folder structure:

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
  /docs
  /inbox
    /processed
  /archive
```

The `aos-manifest.md` and `aos-map.md` files sit at the instance root (see Section 6); all other generated files live inside the subfolders shown above.

The AOS should propose a name during setup and allow the user to modify it.

The top-level folder name should reflect the user’s chosen AOS name.

## 4.1 Framework vs. Instance Layout

The **AOS Workspace** is the top-level container. Its root holds the workspace-governing files:

```text
/aos-router.md
/CLAUDE.md
```

Inside the AOS Workspace, the **AOS Factory** (the reusable builder framework) and each generated **AOS** instance are **sibling folders**:

```text
/aos-factory/
  /build-aos.md
  /builder-changelog.md
  /builders/

/[aos-name]/
  aos-manifest.md
  aos-map.md
  /agents
  /workflows
  /memory
  /projects
  /logs
  /templates
  /configs
  /docs
  /inbox
    /processed
  /archive
```

Each AOS instance is created as a sibling folder named for the user’s chosen AOS name.

All instance-relative paths in this document (for example `/configs/global-permissions.md`, `/memory/user-profile.md`, `/agents/[agent-name]-agent/`) are interpreted relative to the **target AOS instance root** (`/[aos-name]/`), not the AOS Factory root. `/builders/build-aos.md` establishes the target AOS root at build time and resolves all instance paths against it.

Likewise, all factory-internal paths in this document (for example `/build-aos.md`, `/builders/build-aos.md`, `/builder-changelog.md`) are interpreted relative to the **AOS Factory root** (`/aos-factory/`), per the factory tree above — for example, `/builders/build-aos.md` resolves to `/aos-factory/builders/build-aos.md`. In short, a leading slash denotes the root of the relevant container (the AOS Factory root for factory files, the target AOS instance root for instance files), not the AOS Workspace root. The AOS Workspace root itself is referenced only by the two workspace-governing files named explicitly as such (`/aos-router.md`, `/CLAUDE.md`).

The AOS Factory never writes files inside an AOS instance except through `/builders/build-aos.md` (or the root entry `/build-aos.md`) during an authorized build, and never writes to the AOS Workspace root files (`/aos-router.md`, `/CLAUDE.md`) except via the example copies described in Section 28.2, which the user copies and edits manually.

---

# 5. Per-Agent Folder Structure

In this document, the placeholder `[agent-name]` means the agent's **bare domain stem** in lowercase kebab-case, without the `-agent` suffix (for example `research`, `chief-of-staff`, `health-life-logistics`). The full agent folder/file slug is therefore `[agent-name]-agent` (for example `research-agent`). The names listed in Section 7.3 are these full folder slugs, not the bare `[agent-name]` value.

Each generated agent should use this structure:

```text
/agents/[agent-name]-agent/
  [agent-name]-agent.md
  /memory
  /workflows
  /templates
  /configs
  /logs
```

Example:

```text
/agents/research-agent/
  research-agent.md
  /memory
  /workflows
  /templates
  /configs
  /logs
```

## 5.1 Standard Files Per Agent

For each agent, the builder should create this standard file set:

```text
/agents/[agent-name]-agent/
  [agent-name]-agent.md
  /memory/[agent-name]-memory.md
  /memory/[agent-name]-learnings.md
  /workflows/[agent-name]-primary-workflow.md
  /templates/[agent-name]-output-template.md
  /configs/[agent-name]-config.md
  /logs/[agent-name]-decision-log.md
```

Builders may add agent-specific supporting files as needed.

---

# 6. Global AOS Files

During setup, `/builders/build-aos.md` should create these global files when authorized:

```text
/aos-manifest.md
/aos-map.md
/configs/global-permissions.md
/configs/agent-registry.md
/configs/tool-access-matrix.md
/memory/user-profile.md
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md
/logs/aos-decision-log.md
/logs/change-log.md
/workflows/daily-startup-workflow.md
/workflows/end-of-day-shutdown-workflow.md
/workflows/weekly-review-workflow.md
/workflows/monthly-review-workflow.md
/workflows/quarterly-review-workflow.md
/workflows/inbox-to-task-workflow.md
/workflows/project-kickoff-workflow.md
/workflows/decision-capture-workflow.md
/workflows/memory-review-workflow.md
/templates/status-report-template.md
/templates/project-brief-template.md
/templates/decision-entry-template.md
/templates/handoff-summary-template.md
/templates/approval-request-template.md
/templates/memory-entry-template.md
/docs/aos-user-guide.html
```

## 6.1 Agent Learnings Design

The approved approach is:

```text
/memory/agent-learnings-index.md
/agents/[agent-name]-agent/memory/[agent-name]-learnings.md
```

The global file is an index or routing map, not a centralized dumping ground for every agent’s learning.

---

# 7. Agent Roster

## 7.1 Required Agents

Every AOS must include:

```text
1. Security Agent
2. Memory Agent
3. Chief of Staff Agent
4. Review Agent
```

## 7.2 Optional Productive Agents

The user must select at least one optional productive agent.

Approved optional agents, in the desired order:

```text
1. Learning / Tutor Agent
2. Inbox / Communications Agent
3. Calendar / Scheduling Agent
4. Task / Commitment Agent
5. Project Manager Agent
6. Research Agent
7. Writing / Content Agent
8. Document Librarian Agent
9. Personal CRM Agent
10. Finance / Admin Agent
11. Health / Life Logistics Agent
12. Automation / Tool-Use Agent
```

## 7.3 File-Safe Agent Names

Generated folders and files should use lowercase kebab-case names. The names below are the full agent folder slugs (`[agent-name]-agent`); the `[agent-name]` placeholder used elsewhere is the bare stem without `-agent` (see Section 5):

```text
security-agent
memory-agent
chief-of-staff-agent
review-agent
learning-agent
inbox-agent
calendar-agent
task-agent
project-manager-agent
research-agent
writing-agent
document-librarian-agent
personal-crm-agent
finance-agent
health-life-logistics-agent
automation-agent
```

## 7.4 Required Agent Responsibilities

```text
Security Agent
Owns permission rules, approval requirements, access boundaries, the tool access matrix, and safety checks.

Memory Agent
Owns shared memory structure, memory hygiene, preference capture, and cross-agent memory routing.

Chief of Staff Agent
Owns orchestration, routing, prioritization, conflict resolution, and user-facing coordination.
Also a joint owner of the AOS Workspace router (/aos-router.md): every AOS instance's Chief of Staff Agent is a joint owner of the router that resolves the active target before any workflow runs. Each must honor router resolution (ask-don't-guess; never silently pick or merge instances) and log instance-routing choices to its own /agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md.

Review Agent
Owns retrospectives, system improvement, weekly reviews, decision audits, AOS refinement, and the AOS User Guide (/docs/aos-user-guide.html), which it regenerates during the monthly review.
Also owns and reconciles the instance version (aos_version in /aos-manifest.md): it reconciles the value against /logs/change-log.md during the monthly review and verifies it in its completeness audit, while breaking/MAJOR bumps are applied at the time of change (Section 14.3.1). It refines and regenerates only data files and projections; per the drift invariant (Section 14.8) it does not modify framework-derived definition files.
```

## 7.5 Agent Maker Agent Clarification

Earlier design notes referenced an Agent Maker Agent. The final consolidation recommendation is:

```text
Do not add Agent Maker Agent to the initial required or optional roster.

Treat agent creation and modification as a builder-framework capability unless the user explicitly decides to add Agent Maker Agent later.
```

Rationale:

```text
This avoids adding a new agent late in the design, preserves the approved roster, and avoids responsibility overlap.
```

## 7.6 Optional Agent Boundary Rule

Optional productive agents should be treated as specialized workers, not general coordinators.

Coordination remains primarily with the Chief of Staff Agent.

---

# 8. Builder Framework Structure

## 8.1 Builder Files for All Agents

The project should include builder files for all possible approved agents, even if the user does not initially install every agent.

This makes the AOS extensible.

## 8.2 Builder Folder Location

Builder files should live in:

```text
/builders
```

Approved structure:

```text
/builders
  build-aos.md
  build-security-agent.md
  build-memory-agent.md
  build-chief-of-staff-agent.md
  build-review-agent.md
  build-learning-agent.md
  build-inbox-agent.md
  build-calendar-agent.md
  build-task-agent.md
  build-project-manager-agent.md
  build-research-agent.md
  build-writing-agent.md
  build-document-librarian-agent.md
  build-personal-crm-agent.md
  build-finance-agent.md
  build-health-life-logistics-agent.md
  build-automation-agent.md
```

## 8.3 Root Entry File

The project should include a root-level:

```text
/build-aos.md
```

Decision:

```text
The root build-aos.md is a short entry file that points to /builders/build-aos.md.
```

## 8.4 Separation of Concerns

There is no runtime installer. The factory framework is generated once from this design specification and then manually packaged and distributed as a Claude plugin (see Section 28). Within the generated framework, responsibilities separate as:

```text
build-aos.md
Runs the interactive setup process and builds a specific AOS instance.

build-[agent-name]-agent.md
Builds one specific agent inside an AOS instance.
```

Maintaining or refreshing the framework files themselves is a manual, approval-gated operation followed by re-packaging the plugin (Section 28); it is never an automatic build step.

---

# 9. Build Flow

## 9.1 Shared Build Interview Style

The builder interview should follow this pattern:

```text
1. Ask a small batch of questions.
2. Summarize what the user said.
3. Recommend defaults for anything vague.
4. Ask for approval on important design decisions.
5. Generate a build plan / pre-build preview.
6. Ask the user to type Proceed before creating files.
```

The step 5 **build plan / pre-build preview** is shown *before* the user types Proceed and before any files are created; it previews what will be built. It is distinct from the **Build Summary** (Section 13), which is generated *after* files are created — the canonical end-of-build artifact (file_type `build_summary`) saved to the agent's logs folder. "Build Summary" refers only to the Section 13 post-build artifact and is not used for the pre-Proceed preview.

Exception:

```text
If the user explicitly asks to move faster, Cowork can ask fewer questions and rely more heavily on documented assumptions.
```

## 9.2 Recommended Build Sequence

The overall design process should support both guided sequencing and direct access.

Recommended sequence:

```text
1. Define AOS purpose
2. Define domains
3. Choose agents
4. Define folder structure
5. Build core agents
6. Build optional agents
7. Create workflows
8. Create review routines
9. Validate autonomy and permissions
10. Generate final project map
```

## 9.3 Initial Setup Sequence

Initial setup should use this sequence:

```text
0. The factory framework already exists (generated from this design spec and installed as a Claude plugin; see Section 28)
1. /builders/build-aos.md starts the user-facing AOS setup interview
2. Create top-level folder structure
3. Create global config, memory, log, workflow, template, inbox, and archive files
4. Confirm builder files for all possible agents exist
5. Build required agents
6. Ask the user to select at least one optional productive agent
7. Build selected optional agents
8. Update the agent registry
9. Produce an AOS setup summary
```

Actual file creation still waits until the user types:

```text
Proceed
```

## 9.4 Installing Optional Agents Later

The user can add optional agents later by invoking the corresponding builder file.

Example:

```text
Build the Research Agent
```

Routes to:

```text
/builders/build-research-agent.md
```

---

# 10. Agent Lifecycle and Registry

## 10.1 Agent Lifecycle States

Every possible agent should have one of these lifecycle states:

```text
Available
The builder file exists, but the agent has not been selected or built.

Selected
The user has chosen this agent for installation, but it has not been fully built yet.

Built
The agent files have been created.

Active
The agent is available for use in normal AOS operations.

Paused
The agent exists but should not be used unless explicitly reactivated.

Retired
The agent is no longer in active use, but its files are preserved for history.
```

## 10.2 Pausing, Retiring, and Restoring Agents

Pausing or retiring an agent requires explicit approval.

The agent files should not be deleted.

Retired agents should remain in `/agents` with status `Retired` unless the user explicitly approves moving copies to `/archive`.

When an agent is retired:

```text
- Update /configs/agent-registry.md.
- Update /aos-map.md.
- Log the retirement in /logs/aos-decision-log.md.
- Log the change in /logs/change-log.md.
```

Restoring a retired agent requires:

```text
- Checking registry status
- Checking permissions
- Checking tool access
- Checking file completeness
- Checking compatibility
- Explicit approval with Proceed
```

Restoring a retired agent changes its status back to `Active`.

Retired agent folders are not renamed by default.

## 10.3 Agent Registry

`/configs/agent-registry.md` should track agent status.

Recommended table:

```markdown
# Agent Registry

| Agent | Status | Required? | Builder File | Agent Folder | Notes |
|---|---|---:|---|---|---|
| Security Agent | Active | Yes | /builders/build-security-agent.md | /agents/security-agent/ | Required core agent |
| Chief of Staff Agent | Active | Yes | /builders/build-chief-of-staff-agent.md | /agents/chief-of-staff-agent/ | Required core agent; joint owner of /aos-router.md |
| Research Agent | Available | No | /builders/build-research-agent.md | Not created | Optional productive agent |
```

The Chief of Staff Agent's registry entry should note its joint ownership of the AOS Workspace router (`/aos-router.md`), shared with every other AOS instance's Chief of Staff Agent, so router responsibility is discoverable from the registry as well as the agent definition.

## 10.4 AOS Map

`/aos-map.md` should distinguish between:

```text
- Installed agents
- Available but not installed agents
- Required core agents
- Optional productive agents
- Paused agents
- Retired agents
```

---

# 11. Agent Instruction File Schema

Every generated `[agent-name]-agent.md` should follow this structure:

```markdown
# [Agent Name] Agent

## Purpose

## Responsibilities

## Non-Responsibilities

## Inputs

## Outputs

## Workflows

## Collaboration Rules

## Autonomy Rules

## Approval Requirements

## Escalation Rules

## Operating Procedure

## Quality Standards

## Failure Modes

## Example Requests

## Maintenance Notes
```

The **Non-Responsibilities** section is especially important because it enforces the Single Responsibility Principle.

---

# 12. Builder File Schema

Every `build-[agent-name]-agent.md` should follow this structure:

```markdown
# Build [Agent Name] Agent

## Builder Purpose

## When to Use This Builder

## Builder Operating Mode

## Interview Flow

## Discovery Questions

## Recommended Defaults

## Configuration Decisions

## Files to Create

## Agent Instruction Generation Rules

## Workflow Generation Rules

## Memory Generation Rules

## Config Generation Rules

## Logging Rules

## Validation Checklist

## Handoff Summary
```

## 12.1 AOS Factory File Schema

`/builders/build-aos.md` (file_type `aos_builder`) builds a complete AOS instance and should follow this structure:

```markdown
# Build AOS

## Builder Purpose

## When to Use This Builder

## Builder Operating Mode

## Interview Flow

## Discovery Questions

## Recommended Defaults

## AOS Setup Sequence

## Folder Structure to Create

## Global Files to Create

## Required Agent Orchestration

## Optional Agent Selection

## Registry and Map Updates

## Validation Checklist

## AOS Setup Summary
```

`Builder Operating Mode` should combine coach and collaborator behavior (Section 1.5), default to dry-run / preview, and gate file creation behind `Proceed`. `Interview Flow` follows the batch pattern in Section 9.1. `AOS Setup Sequence` follows the ten steps in Section 9.3. `Folder Structure to Create` uses the Section 4 tree, created as a sibling AOS root per Section 4.1. `Global Files to Create` uses the Section 6 list, including `/docs/aos-user-guide.html`, which is generated from the skeleton in Section 16.6 with an Invocation Reference table scoped to the installed agents. `Optional Agent Selection` must enforce that at least one optional productive agent is chosen (Sections 2.3 and 7.2). `Validation Checklist` uses the completeness checks in Section 27.

The root entry `/build-aos.md` (file_type `builder_entry`) is a short pointer to `/builders/build-aos.md` and does not repeat this schema.

---

# 13. Completion Artifact

At the end of each agent build, Cowork should produce a short Build Summary. This is the canonical end-of-build artifact: the builder's `## Handoff Summary` step (Section 12) emits this Build Summary. It is distinct from the general `/templates/handoff-summary-template.md` (Section 18.4), which covers cross-agent handoffs, escalations, and major-work transfers rather than build completion. It is also distinct from the Section 9.1 step-5 **build plan / pre-build preview**, which is shown before the user types Proceed and before any files are created; the term "Build Summary" refers only to this Section 13 post-build saved artifact.

The Build Summary is a saved file (file_type `build_summary`; see Section 15.4), written to the built agent's own logs folder as `/agents/[agent-name]-agent/logs/[agent-name]-build-summary.md`, so each agent retains a durable record of its build.

```markdown
# [Agent Name] Build Summary

## Files Created

## Key Decisions

## User Preferences Captured

## Permissions and Boundaries

## Open Questions

## Suggested Next Agent
```

---

# 14. Versioning and Update Policy

## 14.1 Framework Version Is the Spec Version

The AOS Factory does not carry an independent version number. Because the factory is a pure rendering of this design specification (Section 1.6.1), its version *is* the `spec_version` of the spec it was generated from. There is no separate `builder_version` or `schema_version`: a change to the framework can only come from a change to the spec, and a change to the file schemas is itself a change to this spec (Sections 11, 12, 15, 16), so both would already be captured by a `spec_version` increment. Carrying separate numbers would only invite drift between them.

When a human-facing framework version is needed (for example, the plugin version in Section 28), use the `spec_version`.

Example:

```text
AOS Factory Version: 1.0.5   (= spec_version)
```

## 14.2 Per-File Version Metadata

Each builder file should record, in its YAML frontmatter, the `spec_version` it was rendered from.

Example:

```yaml
---
title: Build Research Agent
spec_version: 1.0.5
last_updated: 2026-06-11
---
```

## 14.3 Generated AOS Version

Each generated AOS instance tracks **two independent version facts**, because an instance is not a frozen rendering of the spec — it accumulates user data and changes after it is built:

```text
spec_version  - The spec design the instance was generated from / last conformed
                to. This is the provenance/compatibility axis, shared with the
                factory. It changes only when the instance is regenerated or
                migrated to a newer spec.
aos_version   - The instance's own evolving version, on its own track. This is
                the change axis: it reflects how the instance itself has grown.
```

`/aos-manifest.md` should include:

```markdown
# AOS Manifest

## AOS Name

## AOS Version

## Spec Version

## Created Date

## Last Updated

## Installed Agents

## Active Agents

## Paused Agents

## Retired Agents
```

`Spec Version` records the `spec_version` the instance was generated from / last conformed to (provenance). `AOS Version` records the instance's own version (below). The authoritative *live* instance version lives only here in `/aos-manifest.md`; the per-file `spec_version` and `aos_version` in each generated file's frontmatter are **provenance stamps set at creation/regeneration**, not values re-stamped across every file on each bump.

### 14.3.1 AOS Version Assignment and Increment

```text
- A new instance is created at aos_version 1.0.0.
- PATCH (1.0.0 -> 1.0.1): content-level fixes (corrected memory entries,
  template wording, guide refresh).
- MINOR (1.0.x -> 1.1.0): additive, non-breaking changes (an agent built, a
  workflow added).
- MAJOR (1.x -> 2.0.0): breaking or structural changes (instance schema
  migration, folder restructure, an agent retired in a contract-changing way).
  This is the line that interacts with compatible_aos_versions (Section 15.1).
```

Ownership and triggers:

```text
- The Review Agent owns and reconciles aos_version. It updates /aos-manifest.md
  during the monthly review, reconciling against /logs/change-log.md, and
  verifies it during its completeness audit (Section 27).
- The triggering event for a bump is logged to /logs/change-log.md by the agent
  that made the change (the Chief of Staff coordinates).
- A breaking/MAJOR bump is applied at the time of the change, not deferred to
  the monthly review.
```

The factory-driven migration path that a MAJOR bump implies is defined later (the update/reconciliation workflow remains a deferred design item; Sections 14.4 and 28 hold its current scope).

## 14.4 Update Modes

When the framework is maintained manually (then re-packaged as a plugin; see Section 28), these update modes apply:

```text
Check only
Report what is missing or outdated, but make no changes.

Install missing
Create missing builder files only.

Update with approval
Refresh existing builder files only after the user types Proceed.

Full rebuild
Recreate the builder framework, requiring explicit approval for every overwrite.
```

## 14.5 Builder Changelog

The reusable builder framework should include:

```text
/builder-changelog.md
```

This changelog describes changes to the builder framework itself, not changes to a generated AOS instance.

`/builder-changelog.md` and the design `aos-factory-revision-history.md` are both numbered by `spec_version` but are not duplicates: the revision history is the **design** audit trail and lives with the spec; the builder changelog tracks **framework-file and packaging** changes and ships *inside the plugin* (Section 28). Same number, different purpose and audience.

Generated AOS instance changes belong in:

```text
/logs/change-log.md
/logs/aos-decision-log.md
```

## 14.6 Compatibility Notes

Builder files should include compatibility notes when a spec change could affect generated AOS instances. Note that `spec_version` is a coarser compatibility signal than a dedicated schema version: it increments for changes that do not affect file structure at all (for example a documentation restructure). Following Section 28, the system therefore **warns** on a `spec_version` mismatch and **blocks** only when compatibility is explicitly marked broken; the revision history indicates whether a given increment is structurally relevant.

## 14.7 Updating Existing Builder Files

Creating missing builder files is Level 1: Safe autonomous.

Refreshing, replacing, or overwriting existing builder files is Level 2: Approval-required.

Deleting builder files should generally be avoided and should require explicit approval.

## 14.8 Definition Files, Data Files, and the Drift Invariant

An AOS instance is a living system: its files change after it is built. To keep that change controllable — and to keep a future factory able to update an existing instance without destroying its accumulated state — every file in an instance is one of two kinds.

**Definition file.** A file whose entire content is determined by the spec plus the instance's declared configuration (its name and selected agents). It is a rendering of the design and holds no information that originated inside the instance. *Test: the factory could regenerate this file from the spec plus the instance's configuration with zero loss of anything the user or agents rely on.* If true, it is a definition file. Definition files are **owned by the factory**: created and updated only by builders, never edited by an operating agent, and a factory update may overwrite them (with `Proceed`). Examples: every `[agent-name]-agent.md` instruction file, workflow definitions in `/workflows`, templates in `/templates`, and the builder files themselves.

**Data file.** A file whose content accumulates from the instance's operation and the user's input, and is therefore not derivable from the spec. *Test: regenerating this file from the factory would destroy information the user or agents rely on.* If true, it is a data file. Data files are **owned by the operating agents**: the factory creates each one once (empty or seeded) and never overwrites it on update; agents append to and maintain it under the normal non-destructive and approval rules (Sections 2.4, 3). Examples: everything in `/memory`, `/logs`, `/projects`, `/inbox`, and `/archive`, and the instance-specific values in `/aos-manifest.md`.

**Mixed and derived files.** Where a file combines a rendered structure with instance data (for example the rows of `/configs/agent-registry.md`, the values in `/aos-manifest.md`), apply the strict test: if the file contains *any* non-regenerable information it is treated as a **data file** for update purposes — updated by targeted, approval-gated merge, never wholesale overwrite — or it is split so each file is purely one kind. A **projection** (for example the AOS User Guide, Section 16.6) is a regenerable view built from definitions plus named data inputs; it is treated as a **definition file** for update purposes (safe to regenerate), with its data inputs stored separately as data files.

**The drift invariant.** Agents write data files; the factory owns definition files; **no operating agent modifies a framework-derived definition file.** This bounds drift to data (which is supposed to grow) and keeps definition files pristine renderings, so a factory update is a clean overwrite of definitions with `Proceed` rather than a three-way merge.

---

# 15. YAML Frontmatter Standards

## 15.1 Builder File Frontmatter

Every builder file should use YAML frontmatter like this:

```yaml
---
title: Build Research Agent
file_type: agent_builder
spec_version: 1.0.5
created_date: 2026-06-02
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---
```

`spec_version` records the spec the file was rendered from (Section 14.1–14.2). `compatible_aos_versions` is the separate compatibility axis: it declares which `aos_version` lines a builder may operate on, matched against the MAJOR line of an instance's `aos_version` (Section 14.3.1).

**Stamping rule (mandatory).** Every file the factory generates — builder files, agent instruction files, and all other generated markdown — records, in its frontmatter, the `spec_version` it was rendered from. Generated instance files additionally carry `aos_version` (Sections 15.2–15.3).

## 15.2 Generated Agent File Frontmatter

Every generated agent instruction file should include YAML frontmatter.

Example:

```yaml
---
title: Research Agent
file_type: agent_instruction
agent_name: research-agent
agent_status: active
required: false
aos_version: 1.0.0
spec_version: 1.0.5
created_date: 2026-06-02
last_updated: 2026-06-02
---
```

Here `aos_version` is the instance's own version at the time the file was created/regenerated, and `spec_version` is the spec design the file was rendered from; both are provenance stamps (Section 14.3).

## 15.3 Other Generated Markdown File Frontmatter

All generated markdown files should include lightweight YAML frontmatter.

Example:

```yaml
---
title: Research Agent Primary Workflow
file_type: workflow
owner: research-agent
aos_version: 1.0.0
spec_version: 1.0.5
created_date: 2026-06-02
last_updated: 2026-06-02
---
```

## 15.4 Controlled `file_type` Vocabulary

Approved initial vocabulary:

```text
builder_entry
aos_builder
agent_builder
aos_manifest
aos_map
config
memory
workflow
template
decision_log
change_log
builder_changelog
documentation
project_doc
handoff_summary
build_summary
agent_instruction
aos_router
project_instructions
design_spec
```

`design_spec` applies to this design specification itself (`aos-factory-design-specification.md`), the source document the AOS Factory is generated from. It is the one source/design artifact in the vocabulary; the other types all describe factory-generated files.

`aos_router` applies to the AOS Workspace root router (`/aos-router.md`) that resolves the active target — the AOS Factory, or a generated AOS instance — before any workflow runs. `project_instructions` applies to the root project instruction file (`/CLAUDE.md`) that serves as the session-start instruction file and wires in the router. Both files live at the AOS Workspace root, alongside the AOS Factory and AOS instance folders, because they govern selection *across* targets rather than belonging to any one of them.

`change_log` applies to a generated AOS instance log (`/logs/change-log.md`). `builder_changelog` applies to the reusable builder framework changelog (`/builder-changelog.md`), which also tracks the plugin version when the framework is distributed (Section 28). The two are tracked separately so framework files can be distinguished from instance files via frontmatter.

`config` and `memory` each cover both global and agent scope, because scope is fully recoverable from a file's path (instance root vs. an agent subfolder). File-type assignments by file:

```text
config        /configs/global-permissions.md, /configs/agent-registry.md,
              /configs/tool-access-matrix.md, and each agent's
              /configs/[agent-name]-config.md

memory        /memory/user-profile.md, /memory/preferences.md,
              /memory/people.md, /memory/projects.md, /memory/decisions.md,
              /memory/agent-learnings-index.md, and each agent's
              /memory/[agent-name]-memory.md and
              /memory/[agent-name]-learnings.md

decision_log  /logs/aos-decision-log.md, each agent's
              /logs/[agent-name]-decision-log.md, and project
              project-decisions.md

build_summary each agent's /logs/[agent-name]-build-summary.md
              (the end-of-build record; see Section 13)

project_doc   project-brief.md, project-plan.md, project-status.md,
              and project-notes.md

documentation /docs/aos-user-guide.html (HTML metadata is carried via meta
              tags or an HTML comment rather than YAML frontmatter)

aos_router    /aos-router.md (AOS Workspace root, shared across instances and factory)

project_instructions
              /CLAUDE.md (AOS Workspace root, session-start instruction file)
```

## 15.5 Controlled Status Vocabulary

Approved initial vocabulary, split by the field it applies to:

Allowed `agent_status` values (agent lifecycle, per Section 10.1):

```text
available
selected
built
active
paused
retired
```

Allowed `status` values (file, builder, template, workflow, or other artifact):

```text
draft
active
deprecated
archived
```

`active` is the only value valid for both fields. All other values belong to exactly one field.

The controlled `status` values above govern factory-generated files. This design specification itself (file_type `design_spec`) is a source/design artifact, not a generated file, and its `status` field tracks design-phase lifecycle (for example, `design_ready_for_factory_generation`); it is exempt from the four controlled artifact-status values.

Important distinction:

```text
agent_status
Tracks lifecycle state of an agent.

status
Tracks the state of a file, builder, template, workflow, or other artifact.

Note: project lifecycle states (Idea, Proposed, Active, Paused, Waiting,
Completed, Canceled, Archived; see Section 21) are not frontmatter values.
They live in the body of project-status.md, not in the status field.
```

Casing: in YAML frontmatter, the `agent_status` and `status` fields must use the lowercase controlled values above. Display tables and prose may use human-readable capitalized forms (for example, `Active` or `Available`) for readability; the example tables in Sections 10.3 and 14.3 are illustrative display, not frontmatter.

## 15.6 Date Format

All frontmatter dates should use ISO format:

```text
YYYY-MM-DD
```

Use timestamps only when there is a specific need to track time of day.

---

# 16. Generated File Schemas by File Type

## 16.1 Config File Schema

Global and agent config files should follow:

```markdown
# [Config Name]

## Purpose

## Scope

## Inherited Rules

## Allowed Autonomous Actions

## Approval-Required Actions

## Prohibited Actions

## Tool Access

## Memory Access

## Escalation Triggers

## Notes
```

For agent configs, `Inherited Rules` is especially important because agent configs should reference global permissions instead of duplicating them. Likewise, the `Tool Access` section must reference the global tool access matrix (`/configs/tool-access-matrix.md`), which is authoritative, and list only agent-specific notes or requests rather than restating or overriding matrix grants (see Section 22).

## 16.2 Memory File Schema

Memory files should follow:

```markdown
# [Memory Name]

## Purpose

## Scope

## What Belongs Here

## What Does Not Belong Here

## Memory Entries

## Review / Cleanup Notes
```

## 16.3 Workflow File Schema

Workflow files should follow:

```markdown
# [Workflow Name]

## Purpose

## When to Use

## Inputs

## Outputs

## Steps

## Decision Points

## Approval Gates

## Escalation Triggers

## Completion Criteria
```

## 16.4 Template File Schema

Template files should follow:

```markdown
# [Template Name]

## Purpose

## When to Use

## Template

## Completion Checklist

## Notes
```

## 16.5 Decision Log Schema

Decision logs should be append-only, with newest entries at the top.

```markdown
# [Decision Log Name]

## Log Rules

- Add newest entries at the top.
- Do not delete prior entries.
- Corrections should be added as new entries.
- Do not silently rewrite history.

## Entries

### YYYY-MM-DD — [Decision Title]

**Decision:**  
**Context:**  
**Reasoning:**  
**Approved By:**  
**Impacted Files:**  
**Follow-Up Needed:**  
```

## 16.6 AOS User Guide Schema

Per-folder README files have been retired in favor of a single consolidated user document, `/docs/aos-user-guide.html`, owned by the Review Agent and regenerated during the monthly review (Sections 6, 7.4, 17.4). The guide documents each folder's purpose and handling rules, provides plain-language orientation to the AOS structure, and includes an embedded change-log section so the user can see what is new in the guide itself.

The guide is a **projection** in the sense of Section 14.8: a regenerable view assembled from definition files plus named data inputs. Almost all of its content is derived — Folder Orientation mirrors the Section 4 tree, Agents Overview and the Invocation Reference are projected from `/configs/agent-registry.md` and `/aos-map.md`, and Core Rules points at `/configs/global-permissions.md`. The only genuinely instance-unique content is the embedded Change Log, which is the guide's data input and is preserved across regenerations (sourced from a stored change-log fragment, or filtered from `/logs/change-log.md`). Because the guide is regenerable, the Review Agent **regenerates** it rather than hand-editing prose, and a newer factory may regenerate it wholesale without a merge. For update purposes the guide is therefore treated as a definition file (Section 14.8), with its Change Log entries treated as data.

Because the guide is an HTML file, it carries its metadata via meta tags or an HTML comment (file_type `documentation`, AOS name, `aos_version`, `spec_version`, `last_updated`) rather than YAML frontmatter.

The guide has a defined **skeleton** so that `/builders/build-aos.md` can always generate a valid, useful file. The Review Agent regenerates the guide from this skeleton plus current instance data during the monthly review (Section 17.4). Every section below the Table of Contents carries a unique HTML bookmark (an `id` anchor), and every Table of Contents item is an in-page link to the corresponding bookmark. The skeleton is a minimal valid HTML document with these fixed top-level sections, in order:

```text
- Header metadata (meta tags / HTML comment: file_type documentation, AOS name, aos_version, last_updated)
- Title and subtitle — the title is the AOS instance name; the subtitle shows the revision (last_updated) date
- Table of Contents — lists every subsequent section below and links to each section's HTML bookmark
- Change Log — what is new in the guide itself (placed immediately after the Table of Contents)
- Introduction — what this AOS is, in plain language
- Folder Orientation — each top-level folder's purpose and handling rules (mirrors the Section 4 tree)
- Agents Overview — points to /configs/agent-registry.md and /aos-map.md (does not duplicate them)
- Core Rules & Safety — the Proceed rule and the three permission levels, pointing to /configs/global-permissions.md
- Operating Rhythms — daily / weekly / monthly / quarterly review pointers
- Managing Agents — how to add, pause, retire, and restore agents (points to /builders)
- Invocation Reference — how the user triggers workflows and agents (see below)
```

**Invocation Reference.** Invocation on Cowork uses flexible **canonical trigger phrases matched by intent**, not a rigid command grammar. The only exact-string command in the AOS is `Proceed`, the approval gate (Section 3.1); the guide must state this contrast explicitly. The Invocation Reference contains a global trigger table (workflow triggers such as "Start my day," "Process my inbox," "Weekly review," and lifecycle triggers such as "Build / Pause / Retire / Restore the [X] Agent," with the information the user supplies in the same message) and, for per-agent task invocation, points to each installed agent's `## Example Requests` section (Section 11) rather than duplicating examples. `/builders/build-aos.md` generates this table scoped to the agents actually installed.

### Table of Contents — Generation Rule (mandatory)

`/builders/build-aos.md` MUST generate the Table of Contents explicitly; it is a required, not optional, element of every generated guide:

- Place the TOC immediately after the title/subtitle and before the Change Log.
- List, in order, every section that follows the TOC — beginning with the Change Log and ending with the Invocation Reference.
- Each section after the TOC MUST carry a unique, stable `id` anchor, using a lowercase, hyphenated slug derived from the section title: `change-log`, `introduction`, `folder-orientation`, `agents-overview`, `core-rules-safety`, `operating-rhythms`, `managing-agents`, `invocation-reference`.
- Each TOC entry MUST be an in-page link (`<a href="#id">`) to its matching anchor.
- The TOC MUST mirror the sections actually emitted. If a section is conditionally added or omitted for a given instance, its TOC entry is added or omitted to match. No TOC entry may point to a missing anchor, and no emitted section may lack a TOC entry.

### Change Log — Generation Rule (mandatory)

The guide carries its own embedded Change Log, distinct from the global `/logs/change-log.md`; it records changes to the guide itself.

- Place the Change Log immediately after the Table of Contents, under `<h2 id="change-log">`.
- On initial generation, seed it with a single dated entry recording that the guide was created, for example: `[last_updated] — Initial guide generated during AOS setup.`
- The Review Agent appends a dated entry at each monthly refresh (Section 17.4), **newest on top** (matching the convention used by `/logs/change-log.md` and `/logs/aos-decision-log.md`).
- The Change Log is always present and never empty; it always holds at least the initial entry.

### Skeleton HTML Pattern

The builder emits a structure equivalent to the following. Section bodies are placeholders refined later by the Review Agent, but the TOC, anchors, and Change Log are generated complete:

```html
<h1>[AOS name]</h1>
<p class="subtitle">Revised [last_updated]</p>

<nav id="table-of-contents" aria-label="Table of contents">
  <h2>Contents</h2>
  <ol>
    <li><a href="#change-log">Change Log</a></li>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#folder-orientation">Folder Orientation</a></li>
    <li><a href="#agents-overview">Agents Overview</a></li>
    <li><a href="#core-rules-safety">Core Rules &amp; Safety</a></li>
    <li><a href="#operating-rhythms">Operating Rhythms</a></li>
    <li><a href="#managing-agents">Managing Agents</a></li>
    <li><a href="#invocation-reference">Invocation Reference</a></li>
  </ol>
</nav>

<section id="change-log">
  <h2>Change Log</h2>
  <ul><li>[last_updated] — Initial guide generated during AOS setup.</li></ul>
</section>
<section id="introduction">
  <h2>Introduction</h2>
  <!-- ... -->
</section>
<!-- remaining sections, each with a matching id anchor -->
```

### Consistency Checks (acceptance criteria)

The generated guide is invalid, and `/builders/build-aos.md` must correct it before finishing, if any of these fail:

- Every TOC entry resolves to a section with a matching `id` anchor.
- Every section after the TOC has a corresponding TOC entry.
- The Change Log section exists, sits immediately after the TOC, and contains at least one dated entry.

The Review Agent verifies these checks at generation and at every monthly refresh (Section 17.4).

---

# 17. Global Workflows

Every generated AOS should include these global workflows.

## 17.1 Daily Startup Workflow

Create:

```text
/workflows/daily-startup-workflow.md
```

Purpose:

```text
Help the user start the day by reviewing priorities, calendar, commitments, inbox items, active projects, and recently processed inbox items.
```

Instance resolution (first step): before gathering any inputs, the Chief of Staff resolves the active target via `/aos-router.md` — explicit override, then framework-vs-instance, then session pin, then signal match, else ASK. The brief runs against exactly one resolved instance (or, for a cross-instance request, each instance separately with labeled output); it never blends instance memory. State the resolved target on the first line of the brief (e.g. `**[work-aos]** Daily Brief — …`). Generated `daily-startup-workflow.md` files must include this resolution step ahead of input gathering.

Approved review question:

```text
What matters today?
```

The daily startup workflow should include a startup brief section summarizing recently processed inbox items.

The startup brief should distinguish between:

```text
- Items processed today
- Items still unresolved
- Items promoted to tasks
- Items promoted to projects
- Items promoted to calendar items
- Items promoted to memory
- Items promoted to decisions
- Items promoted to archive
- Items requiring user approval
```

These promotion categories mirror the full set of promotion targets in the inbox-to-task workflow (Sections 17.6 and 31).

Primary owner:

```text
Chief of Staff Agent
```

## 17.2 End-of-Day Shutdown Workflow

Create:

```text
/workflows/end-of-day-shutdown-workflow.md
```

Purpose:

```text
Capture what changed today, what must not be lost, unresolved obligations, decisions made, follow-ups needed, and next-day carryover.
```

Approved review question:

```text
What changed today, and what must not be lost?
```

Primary owner:

```text
Chief of Staff Agent
```

## 17.3 Weekly Review Workflow

Create:

```text
/workflows/weekly-review-workflow.md
```

Purpose:

```text
Review commitments, projects, decisions, unresolved items, agent performance, stale memory signals, and next-week priorities.
```

Approved review question:

```text
What needs follow-up soon?
```

Primary owner:

```text
Review Agent
```

## 17.4 Monthly Review Workflow

Create:

```text
/workflows/monthly-review-workflow.md
```

Purpose:

```text
Review stale projects, memory hygiene, workflow quality, permission boundaries, tool access, structural clutter, and system cleanup needs.
```

Approved review question:

```text
What is stale, misplaced, or structurally messy?
```

Stale project review is part of monthly review.

Memory hygiene receives lightweight weekly review and deeper monthly review.

The Review Agent regenerates the AOS User Guide (`/docs/aos-user-guide.html`) as part of the monthly review, re-projecting it from current instance data and preserving its embedded Change Log (Section 16.6). It also reconciles the instance `aos_version` in `/aos-manifest.md` against `/logs/change-log.md` at this time (Section 14.3.1).

Primary owner:

```text
Review Agent
```

## 17.5 Quarterly Review Workflow

Create:

```text
/workflows/quarterly-review-workflow.md
```

Purpose:

```text
Review whether the AOS is still aimed at the right goals, whether agents remain useful, and whether workflows still support the user’s priorities.
```

Approved review question:

```text
Is the whole system still aimed at the right goals?
```

Primary owner:

```text
Review Agent
```

## 17.6 Inbox-to-Task Workflow

Create:

```text
/workflows/inbox-to-task-workflow.md
```

Purpose:

```text
Convert raw inbox notes, messages, or captured thoughts into tasks, projects, calendar items, memory updates, decisions, or archive items.
```

Processed inbox items should be moved to:

```text
/inbox/processed
```

Moving an item to `/inbox/processed` is treated as part of normal inbox processing and should be allowed if the user has approved the inbox-processing workflow. This is the single pre-authorized exception to the Section 3.2 rule that moving files requires explicit approval.

Primary owner:

```text
Chief of Staff Agent, with Inbox / Communications Agent support when installed.
```

## 17.7 Project Kickoff Workflow

Create:

```text
/workflows/project-kickoff-workflow.md
```

Purpose:

```text
Turn a new project idea into a project folder, project brief, goals, stakeholders, milestones, tasks, and review cadence.
```

Primary owner:

```text
Chief of Staff Agent, with Project Manager Agent support when installed.
```

## 17.8 Decision Capture Workflow

Create:

```text
/workflows/decision-capture-workflow.md
```

Purpose:

```text
Capture important decisions consistently in the correct decision log, including context, rationale, affected files, and follow-up.
```

Primary owner:

```text
Chief of Staff Agent, with Memory Agent support.
```

## 17.9 Memory Review Workflow

Create:

```text
/workflows/memory-review-workflow.md
```

Purpose:

```text
Review memory files for stale, duplicated, misplaced, sensitive, or low-value information.
```

Primary owner:

```text
Memory Agent, with Review Agent support.
```

---

# 18. Global Templates

Every generated AOS should include these global templates.

## 18.1 Status Report Template

Create:

```text
/templates/status-report-template.md
```

Purpose:

```text
Give the user a concise summary of current priorities, active projects, pending approvals, recent decisions, next actions, and processed inbox items.
```

## 18.2 Project Brief Template

Create:

```text
/templates/project-brief-template.md
```

Purpose:

```text
Define a project’s purpose, desired outcome, scope, stakeholders, milestones, risks, next actions, and review cadence.
```

This template should exist even if the Project Manager Agent is not installed.

## 18.3 Decision Entry Template

Create:

```text
/templates/decision-entry-template.md
```

Purpose:

```text
Provide a standard format for recording decisions in global, project-level, or agent-level decision logs.
```

## 18.4 Handoff Summary Template

Create:

```text
/templates/handoff-summary-template.md
```

Purpose:

```text
Create consistent summaries when an agent finishes major work, escalates, or transfers context to another agent. Build completion is covered separately by the Build Summary (Section 13), not by this template.
```

## 18.5 Approval Request Template

Create:

```text
/templates/approval-request-template.md
```

Purpose:

```text
Standardize how agents ask the user to approve Level 2 actions requiring Proceed.
```

The request must explain the proposed action, affected files, reason, consequence, and ask the user to type exactly `Proceed`.

## 18.6 Memory Entry Template

Create:

```text
/templates/memory-entry-template.md
```

Purpose:

```text
Standardize how important preferences, facts, decisions, people, projects, and agent learnings are recorded.
```

---

# 19. Logging Model

## 19.1 Global Logs

The AOS should maintain:

```text
/logs/aos-decision-log.md
/logs/change-log.md
```

Global logs should capture:

```text
- System-wide decisions
- Major configuration changes
- Build history
- Global workflow changes
- Permission policy changes
```

## 19.2 Agent-Level Logs

Each agent should maintain:

```text
/agents/[agent-name]-agent/logs/[agent-name]-decision-log.md
```

Agent logs should capture local decisions within the agent’s domain.

## 19.3 Must-Log Categories

Agents should log these events:

```text
- Important user preferences
- Configuration decisions
- Permission changes
- Files created
- Files modified with approval
- Workflows created or changed
- Important assumptions
- Escalations
- Errors or failed actions
- Handoff summaries
- Agent retirement or restoration
```

Logs should not capture every trivial action. They should preserve decisions that affect future behavior.

---

# 20. Global Memory Files and Governance

## 20.1 Required Global Memory Files

Every generated AOS should include:

```text
/memory/user-profile.md
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md
```

## 20.2 Memory File Boundaries

```text
/memory/user-profile.md
Stores durable, user-approved facts about the user that help the AOS personalize assistance. Avoid sensitive personal attributes unless explicitly approved.

/memory/preferences.md
Stores durable user preferences about communication style, workflows, defaults, formatting, decision-making, tools, and collaboration.

/memory/people.md
Stores relevant people, roles, relationship context, communication preferences, and collaboration notes. Avoid sensitive personal details unless explicitly approved.

/memory/projects.md
Tracks active, paused, completed, and potential projects at a high level. Detailed project files live in /projects.

/memory/decisions.md
Captures durable decisions that affect future AOS behavior, user preferences, projects, permissions, workflows, and defaults. Decision logs remain the authoritative chronological record.

/memory/agent-learnings-index.md
Provides a global index of agent-specific learning files without centralizing all learnings in one global file.
```

## 20.3 Memory Governance Rules

```text
- Information is memory-worthy only if durable, useful, relevant to the AOS, and likely to improve future assistance.
- Do not store trivial one-time facts, short-lived temporary details, sensitive personal attributes unless explicitly approved, inappropriate third-party private information, raw notes better suited for /inbox, or large source documents better suited for /projects or a project's /assets folder.
- Sensitive memory entries require explicit user approval.
- Memory entries should include Type, Summary, Source, Confidence, Owner, Review Date, and Notes.
- Memory should receive lightweight review during weekly review and deeper hygiene review monthly.
- Stale memory should not be silently deleted; it should be marked stale, superseded, corrected with a new entry, or archived only with approval.
```

---

# 21. Project Folder Structure

Every project created inside the AOS should have its own folder.

Approved standard structure:

```text
/projects/[project-name]/
  project-brief.md
  project-plan.md
  project-status.md
  project-decisions.md
  project-notes.md
  /assets
  /archive
```

Approved rules:

```text
- Every project gets its own folder.
- Project folder names use file-safe slugs.
- Every project includes the five standard project files.
- Every project includes /assets and /archive.
- Moving files into /archive requires explicit approval.
- Projects use lifecycle states: Idea, Proposed, Active, Paused, Waiting, Completed, Canceled, Archived.
- Project-specific decisions go in project-decisions.md.
- System-wide AOS decisions stay in /logs/aos-decision-log.md.
```

A project's lifecycle state (Idea, Proposed, Active, Paused, Waiting, Completed, Canceled, Archived) is recorded in the body of `project-status.md` and reflected at a high level in `/memory/projects.md`. It is **not** a frontmatter field. The YAML `status` field on a project file remains the file-artifact status (`draft`, `active`, `deprecated`, `archived`) per Section 15.5, and should not be set to a project lifecycle value.

---

# 22. Tool Access Matrix

Every generated AOS should include:

```text
/configs/tool-access-matrix.md
```

Approved rules:

```text
- Every AOS includes a required global tool access matrix.
- Tool access is tracked by agent in a table.
- Access levels are: Allowed, Read-only, Approval-required, Prohibited, Not configured.
- Not configured means the agent may not use the tool until access is explicitly granted.
- Sending, publishing, spending money, sharing private information, or affecting other people requires explicit approval.
- Security Agent owns the tool access matrix.
- The global tool access matrix is the single source of truth for tool access and overrides any agent config on conflict.
- Agent config Tool Access sections reference the matrix and list only agent-specific notes or requests; they do not restate or override matrix grants (parallel to the permissions pattern in Section 3.5).
- Chief of Staff Agent and Review Agent may recommend changes.
```

Recommended table structure:

```markdown
| Agent | Tool | Access Level | Approval Required? | Notes |
|---|---|---|---:|---|
| Research Agent | Web search | Allowed | No | For research tasks |
| Inbox Agent | Email send | Approval-required | Yes | Drafting is allowed; sending requires Proceed |
| Calendar Agent | Calendar read | Allowed | No | Within approved scope |
| Calendar Agent | Calendar modify | Approval-required | Yes | Especially when other people are involved |
```

---

# 23. Agent Collaboration Rules

Approved decisions:

```text
- Chief of Staff Agent is the default coordinator for cross-agent routing.
- Agents may directly hand off to another agent only when the receiving agent has clear domain ownership and no safety, permission, or priority conflict exists.
- Conflicts between agents escalate to Chief of Staff Agent.
- Permission or access conflicts escalate to Security Agent.
- Cross-agent handoffs should use /templates/handoff-summary-template.md.
```

---

# 24. Escalation Model

Approved decisions:

```text
- Escalate to the user for approval-required actions, ambiguity with material consequences, external communication, publishing, spending, sensitive information, or irreversible changes.
- Escalate to Security Agent for permission conflicts, prohibited actions, tool access uncertainty, privacy risk, or sensitive memory questions.
- Escalate to Chief of Staff Agent for priority conflicts, cross-agent routing issues, unclear ownership, or competing project demands.
- Failed actions should be reported to the user when relevant and logged if they affect future behavior, files, permissions, or project status.
```

---

# 25. Global Operating Rhythms

Approved rhythms:

```text
- Daily startup workflow
- End-of-day shutdown workflow
- Weekly review workflow
- Monthly review workflow
- Quarterly review workflow
- Stale project review as part of monthly review
- Memory hygiene as lightweight weekly review plus deeper monthly review
- AOS User Guide refresh as part of monthly review
```

Approved review scopes:

```text
Daily startup:
What matters today?

End-of-day shutdown:
What changed today, and what must not be lost?

Weekly review:
What needs follow-up soon?

Monthly review:
What is stale, misplaced, or structurally messy?

Quarterly review:
Is the whole system still aimed at the right goals?
```

Approved rationale:

```text
- The weekly review keeps the AOS operationally clean and prevents loose ends from becoming forgotten obligations.
- The monthly review keeps the AOS structurally healthy by reviewing stale projects, memory hygiene, workflows, boundaries, and tool access.
- The quarterly review keeps the AOS aligned with larger goals and prevents the system from being well-maintained but aimed at outdated priorities.
```

---

# 26. Agent-Specific Builder Interviews

Approved decisions:

```text
- Every agent builder should use a common interview pattern.
- Required agents should have shorter interviews because their purpose is mostly standardized.
- Optional productive agents should ask about user goals, scope, tools, output preferences, approval boundaries, and collaboration patterns.
- Each builder should create the standard agent file set already approved.
- Agent-specific workflows and templates should be created only when useful to that agent’s domain.
- Each builder should end with a validation checklist and handoff summary.
```

---

# 27. Validation and QA

Approved decisions:

```text
- A complete AOS must include required folders, required global files, required agents, at least one optional productive agent, registry entries, AOS map, permissions, workflows, templates, logs, and the AOS User Guide.
- A complete agent build must include instruction file, memory file, learnings file, primary workflow, output template, config, and decision log.
- Review Agent audits generated files for completeness and consistency.
- Security Agent audits permissions and tool access.
- Memory Agent audits memory routing and memory file boundaries.
```

---

# 28. Distribution and Update Mechanics

The AOS Factory is generated once from this design specification and then **manually packaged and distributed as a Claude plugin**. There is no runtime installer. Framework maintenance and re-distribution are manual, approval-gated operations.

Approved decisions:

```text
- Use frontmatter as the primary update detection mechanism.
- Use expected file lists and required-heading checks as secondary validation.
- Warn on schema mismatches by default.
- Block only when compatibility is explicitly marked as broken.
- Present upgrade recommendations with affected files, reason, consequence, and approval requirement.
- Require dry-run / preview mode in all builders.
- Never silently update existing builder files.
- Require Proceed before refreshing, replacing, or overwriting any existing builder file.
```

Files affected when the framework is updated:

```text
/builders/build-aos.md
/builders/build-[agent-name]-agent.md
/builder-changelog.md
/aos-manifest.md
/logs/change-log.md
/logs/aos-decision-log.md
```

## 28.1 Generating a Factory Instance

These are the user-facing steps to generate the reusable factory framework from this design specification:

```text
1. Open a Claude session with this design specification available.
2. Review the proposed generation scope in Section 35 — the exact list of
   framework files to be created.
3. Type exactly `Proceed` to authorize generation (the approval gate in
   Section 3.1; the §34.2 Safety Confirmation Checklist must also be
   satisfied). Nothing is written before this.
4. Claude previews, then on `Proceed` writes the framework files:
   - the root entry pointer `/build-aos.md`,
   - all `/builders/build-*.md` files (one master AOS builder plus one
     builder per agent in the Section 7 roster),
   - the framework changelog `/builder-changelog.md`.
5. This phase does NOT create a user AOS instance. Instructions for creating an AOS instance are outside the scope of this document.
6. Validate the generated framework against the QA checks in Sections 27 and 34.
```

The workspace-root router (`/aos-router.md`, file_type `aos_router`) and project instructions (`/CLAUDE.md`, file_type `project_instructions`) govern target selection *across* instances and the factory; they live at the AOS Workspace root alongside the factory and instances and are not produced by the factory build.

Framework generation, as scoped above and in Section 35, produces only the AOS Factory's own files: the root build entry (`/build-aos.md`), the `/builders/build-*.md` files, and `/builder-changelog.md`. The example workspace-root files referenced in Section 28.2 (`templates/aos-router.md`, `templates/CLAUDE.md`) are not part of this generation phase — they are authored separately during plugin packaging.

## 28.2 Packaging the Factory as a Claude Plugin

Once generated, the factory is distributed as a Claude plugin. A plugin is a directory whose only required file is a manifest at `.claude-plugin/plugin.json`; all functional components live at the plugin root (not inside `.claude-plugin/`).

```text
my-aos-factory/                 (plugin root)
  .claude-plugin/
    plugin.json                 (REQUIRED manifest: name, version, description, author)
  skills/                       (each builder exposed as a skill, or as commands/)
    build-aos/ ...
    build-security-agent/ ...
    ...
  commands/                     (optional: slash-command entry points)
  agents/                       (optional)
  .mcp.json                     (optional: bundled MCP servers)
  builder-changelog.md          (framework/plugin changelog)
  README.md                     (plugin install + usage instructions)
  templates/                    (shipped example workspace-root files)
    aos-router.md               (example router; user copies to workspace root)
    CLAUDE.md                   (example project instructions; user copies to root)
```

Steps:

```text
1. Create the plugin directory and add .claude-plugin/plugin.json with the
   plugin's name, version, description, and author. Keep the plugin version in
   sync with the framework spec_version (Section 14.1) and /builder-changelog.md.
2. Place the generated factory content at the plugin root: expose the builder
   files (build-aos.md and each /builders/build-*.md) as skills or slash
   commands so Claude can invoke them after install. Components must sit at the
   plugin root, never inside .claude-plugin/.
3. Author the example workspace-root files under templates/ (aos-router.md,
   CLAUDE.md), and author or refresh README.md with install and usage
   instructions. These are written during this packaging step, not during
   framework generation (Section 35) — the templates are starting-point copies
   of the AOS Workspace root files described below.
4. (Optional) Bundle MCP servers via .mcp.json at the plugin root.
5. Test locally before publishing: load the plugin without installing using
   `claude --plugin-dir <path>`.
6. Package for distribution as a .zip archive of the plugin directory
   (requires Claude Code v2.1.128 or later), OR publish via a marketplace.
7. To distribute via a marketplace, create .claude-plugin/marketplace.json
   listing the plugin (at minimum a name and source) and host it on GitHub,
   GitLab, or another git host. URL-based marketplaces must reference external
   sources (GitHub, npm, or git URLs); use a Git-based marketplace for plugins
   referenced by relative path.
8. On each framework change, bump plugin.json version and /builder-changelog.md,
   then re-package and re-publish.
```

The router (`/aos-router.md`) and project instructions (`/CLAUDE.md`) are AOS Workspace root files, not factory components, but the plugin **ships example copies** of both under `templates/`, authored at packaging time per step 3 above. After installing the plugin and generating their first instance, the user copies these examples to their AOS Workspace root and edits them (default instance, routing signals, planning-mode rules) for their setup. Shipping them as examples — rather than writing them to the workspace automatically — keeps the plugin from overwriting a user's existing root files.

---

# 29. Naming and Slug Rules

Approved decisions:

```text
- Use lowercase kebab-case for generated folder and file slugs.
- Strip or replace special characters.
- Do not use spaces in generated folder names.
- Preserve human-readable names in frontmatter and headings.
- Handle duplicates by appending a short numeric suffix, such as -2 or -3.
```

---

# 30. Archive Policy

Approved decisions:

```text
- /archive stores retired, superseded, obsolete, or historical materials.
- Archiving requires explicit approval because it moves files.
- Archived files or folders should be dated when useful.
- Retired agents should remain in /agents with status Retired unless the user explicitly approves moving copies to /archive.
- Prefer copying to archive over moving when preserving active context is important.
- When an agent is retired, update /configs/agent-registry.md and /aos-map.md.
- Retiring an agent should be logged in /logs/aos-decision-log.md and /logs/change-log.md.
- Restoring a retired agent requires checking registry status, permissions, tool access, file completeness, and compatibility.
- Restoring a retired agent changes its status back to Active.
- Restoring a retired agent requires explicit approval with Proceed.
```

Clarification:

```text
Retired agent folders are not renamed by default.
```

---

# 31. Inbox Policy

Approved decisions:

```text
- /inbox is for raw notes, unresolved items, imported material, quick captures, and items awaiting routing.
- /inbox should be reviewed during daily startup when relevant and during weekly review by default.
- Inbox items should be promoted to tasks, projects, memory, decisions, calendar items, or archive according to the inbox-to-task workflow.
- Inbox items should not be deleted after processing unless explicitly approved.
- Processed inbox items should be moved to /inbox/processed to avoid duplicate processing.
- Moving an item to /inbox/processed is treated as part of normal inbox processing and should be allowed if the user has approved the inbox-processing workflow. This is the sole pre-authorized exception to the move-approval rule in Section 3.2.
- The daily startup workflow should include a startup brief section summarizing recently processed inbox items.
- The startup brief should distinguish between items processed today, items still unresolved, items promoted to tasks, items promoted to projects, items promoted to calendar items, items promoted to memory, items promoted to decisions, items promoted to archive, and items requiring user approval. These promotion categories mirror the full set of promotion targets in the inbox-to-task workflow (Section 17.6).
```

Files affected later:

```text
/docs/aos-user-guide.html
/workflows/inbox-to-task-workflow.md
/workflows/daily-startup-workflow.md
/templates/status-report-template.md
/templates/decision-entry-template.md
/logs/change-log.md
```

---

# 32. Output Style Standards

Approved decisions:

```text
- Generated files should be detailed enough to be useful but not bloated.
- Agent instructions should use direct imperative language.
- Use must/should/may consistently: must for requirements, should for strong defaults, may for optional behavior.
- Include examples in agent instruction files and important templates.
- Templates should include placeholders plus brief guidance, not long sample completed entries unless useful.
```

---

# 33. Generation Runbook

Sections 33-37 — the final consolidation decisions, ready-to-generate checklist, proposed builder generation scope, required continuation behavior, and status — have been moved to a companion file so this specification holds the design and the runbook holds the build-and-handoff procedure:

```text
aos-factory-generation-runbook.md
```

Cross-references elsewhere in this document to Sections 33-37 (for example Section 34.2 and Section 35 in Section 28.1) resolve to the runbook, where the original 33-37 numbering is preserved. The `Proceed` safety gate is unchanged: actual AOS Factory file generation remains blocked until the user types exactly `Proceed`, per the Purpose section above and the runbook.
