---
title: AOS Factory Design Specification
file_type: design_spec
project: Script to Build Agentic OS Factory
created_date: 2026-06-02
last_updated: 2026-07-06
spec_version: 2.1.0
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
agent-catalog.yaml                    - the Agent Catalog: structured agent identity/ownership data (Section 7A)
agent-specs/                          - one folder per agent: profile.md (behavioral narrative, Section 7B) + interviews.md (scripted interviews, Section 7C)
aos-interviews.md                     - the AOS-level setup interview script, owned by build-aos (Sections 7C, 12.1)
```

The canonical specification remains the single source of truth (Section 1.6.1); the companion files are extracted from it for readability and are governed by the same `Proceed` safety gate. `agent-catalog.yaml`, the `agent-specs/` files (one folder per agent holding `profile.md` and `interviews.md`), and `aos-interviews.md` are design-time **source** artifacts that live with the spec here in `design-spec/` (versioned by `spec_version`); they are framework-owned and read-only inside instances (Section 14.8), and the factory ships rendered copies of them (Sections 7A.4, 7B.2, 7C).

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
                 files (/aos-router.md, /CLAUDE.md). Each AOS instance live 
                 inside it as sibling folders. An instance of the AOS Factory
                 may also live inside a sibling folder, though it is not necessary
                 if the AOS Factory is being used as a plugin.

AOS Factory    - The reusable builder framework (aos-factory/) that generates
                 AOS instances.

AOS            - A generated Agentic Operating System instance (/[aos-name]/),
                 a sibling within the AOS Workspace.
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
- The AOS builder and the generic agent build engine
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

Safety, memory, coordination, and quality review must exist before any productive work happens. The five required governance agents (Security, Memory, Chief of Staff, Review, Feedback) are mandatory and are built before any optional productive agent (Section 2.3). Productivity is additive; governance is foundational. A user cannot end up with a fast, capable, ungoverned system.

### 1.6.3 Single Responsibility at Every Level

Each agent owns exactly one domain, with explicit non-responsibilities and escalation rules; coordination is the Chief of Staff's job rather than being absorbed into a catch-all central agent (Sections 2.1, 2.2). The same discipline applies to files: one file, one purpose, scope recoverable from its path. This keeps the system legible to non-technical users and extensible without redesign.

### 1.6.4 Non-Destructive and Approval-Gated by Default

The system prefers actions that cannot lose work. Agents create, append, or ask rather than overwrite, delete, move, or bulk-modify (Section 2.4). Anything consequential is gated behind a single, unambiguous approval signal — the user typing exactly `Proceed` (Section 3.1) — and approval is specific to the action described, never a standing grant (Section 2.5). The goal is that a user can trust the AOS with real work without fear that it will quietly damage their files.

### 1.6.5 Standardization and Extensibility

Uniform schemas — builder files, agent instruction files, configs, memory, workflows, logs (Sections 11, 12, 15, 16) — let new agents and capabilities be added without inventing new formats. The factory ships the generic build engine (Section 8) plus the design artifacts (catalog entry, profile, interviews — Sections 7A–7C) for every approved agent even when they are not initially installed (Section 8.1), so the collection is extensible by design rather than by exception.

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

The project is released openly on Github. Openness reinforces key principles that make external contribution tractable: a single-source-of-truth spec, standardized schemas, and self-documenting output.

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

Single responsibility and non-overlap are verified, not merely asserted: the Agent Catalog (§7A) records each agent's `domains_owned` and `artifacts_owned`, and the Review Agent's catalog validation (§7A.5, §27) is the enforcement surface for this principle.

## 2.2 Chief of Staff as Coordinator, Not Universal Worker

The **Chief of Staff Agent** should coordinate, route, prioritize, and resolve conflicts.

As much responsibility as possible should be pushed down to specialized agents.

**Designated-owner routing (normative).** When a workflow has a designated **workflow owner** — an agent named as owning that workflow (for example, the Review Agent owns the weekly, monthly, and quarterly review workflows, Section 17) — the Chief of Staff Agent routes execution to that owner and never executes the workflow directly. Orchestration (the Chief of Staff's responsibility: which agent runs what, in what order) and execution (the designated owner's responsibility: running the workflow steps) are distinct. Absent an explicit routing step, the Chief of Staff must route, not default to doing the work itself.

## 2.3 Required Governance Layer Plus Optional Productive Agents

The AOS should have a small required governance layer and optional productive agents.

Required governance agents:

```text
1. Security Agent
2. Memory Agent
3. Chief of Staff Agent
4. Review Agent
5. Feedback Agent
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
  /outputs
    /[agent-name]-agent      (one subfolder per installed agent; §5.1)
  /inbox
    /processed
  /archive
```

The `aos-manifest.md` and `aos-map.md` files sit at the instance root (see Section 6); all other generated files live inside the subfolders shown above.

`/outputs` is the root-level home for **standalone agent deliverables** — artifacts that are not configs, definitions, memory, or anything else related to agent operation. It sits at the root (not inside `/agents/*`) because deliverables are user-facing, not system plumbing. Rules:

```text
- One subfolder per installed agent: /outputs/[agent-name]-agent/ — created
  empty at that agent's build (§5.1). No flat shared folder.
- Boundary with /projects: deliverables belonging to an active project go in
  that project's folder as today; /outputs holds STANDALONE deliverables only.
- Cross-agent work: the output lives under the agent that produced the FINAL
  artifact; the handoff summary (§18.4) records lineage.
- §14.8 classification: /outputs and its subfolders are DATA files — never
  touched by a factory update, preserved on agent retirement. Writing a new
  file there is Level 1 safe-autonomous (§3.3); modifying or archiving an
  existing output follows the normal §3 rules.
- Naming: YYYY-MM-DD-[slug].md, or the appropriate extension (§29).
- Ownership: each catalog entry's artifacts_owned includes its
  /outputs/[agent-name]-agent/** glob (§7A), keeping the pairwise-
  disjointness check mechanical.
```

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
  /agent-catalog.yaml        (rendered copy of the design-spec source; §7A)
  /agent-specs/              (rendered copies of the design-spec sources: profile.md + interviews.md per agent; §7B, §7C)
  /aos-interviews.md         (rendered copy of the design-spec source; §7C)
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

The AOS Factory never writes files inside an AOS instance except through `/builders/build-aos.md` (or the root entry `/build-aos.md`) during an authorized build. It writes to the AOS Workspace root files (`/aos-router.md`, `/CLAUDE.md`) only through `/builders/build-aos.md` during an authorized build, and only non-destructively: it creates them from the shipped example copies (Section 28.2) when they are absent, and overwrites an existing root file only after a separate `Proceed` (Sections 2.4, 3.2).

---

# 5. Per-Agent Folder Structure

In this document, the placeholder `[agent-name]` means the agent's **bare domain stem** in lowercase kebab-case, without the `-agent` suffix (for example `research`, `chief-of-staff`, `project-manager`). The full agent folder/file slug is therefore `[agent-name]-agent` (for example `research-agent`). The names listed in Section 7.3 are these full folder slugs, not the bare `[agent-name]` value.

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

Each agent's build also creates its (empty) standalone-deliverables subfolder at the instance root: `/outputs/[agent-name]-agent/` (§4). Outputs rendered from `[agent-name]-output-template.md` land there by default (project-bound deliverables go in the project's folder instead, §4/§21).

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
/logs/feedback-log.md
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

`/memory/agent-learnings-index.md` uses this index table:

```markdown
| Agent | Learnings File | Last Reviewed | Highlights |
|---|---|---|---|
```

Entries in each `[agent-name]-learnings.md` use this format:

```markdown
### YYYY-MM-DD — [Learning]

**Learning:**
**Context/Evidence:**
**Confidence:** [high | medium | low]
**Applies To:** [the owning process]
**Captured:** YYYY-MM-DD
**Review Date:** YYYY-MM-DD
```

**Attribution rule (normative).** A learning is filed in the learnings file of the agent that **owns the process** where the issue occurred — not the agent that happened to be active in the session. The `Applies To` field records the owning process. (Example: a routing miss discovered while another agent was active is filed under the Chief of Staff Agent's learnings, `Applies To: request routing`.)

---

# 7. Agent Roster

## 7.1 Required Agents

Every AOS must include:

```text
1. Security Agent
2. Memory Agent
3. Chief of Staff Agent
4. Review Agent
5. Feedback Agent
```

## 7.2 Optional Productive Agents

The user must select at least one optional productive agent.

Approved optional agents, in the desired order:

```text
1. Tutor Agent
2. Inbox Agent
3. Calendar Agent
4. Task Agent
5. Project Manager Agent
6. Research Agent
7. Writing Agent
8. Document Agent
9. Personal CRM Agent
10. Automation Agent
```

## 7.3 File-Safe Agent Names

Generated folders and files should use lowercase kebab-case names. The names below are the full agent folder slugs (`[agent-name]-agent`); the `[agent-name]` placeholder used elsewhere is the bare stem without `-agent` (see Section 5):

```text
security-agent
memory-agent
chief-of-staff-agent
review-agent
feedback-agent
tutor-agent
inbox-agent
calendar-agent
task-agent
project-manager-agent
research-agent
writing-agent
document-agent
personal-crm-agent
automation-agent
```

## 7.4 Required Agent Responsibilities

The five agent descriptions below are a generated projection of the `agent-catalog.yaml` entries where `kind: governance` (§7A). The catalog is authoritative (§1.6.1); this rendering is kept here for readers and must be reconciled to the catalog whenever a governance entry changes.

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

Feedback Agent
Owns the upstream feedback channel (feedback.upstream): captures user bug reports and enhancement requests into the local feedback log (/logs/feedback-log.md, Section 16.7); at monthly/quarterly review examines the instance's learnings and preferences for enhancement candidates and presents them for accept / edit / discard; drafts outbound submissions, routes each through Security Agent scrubbing, and sends to aos-factory@neoclarity.ai only after the user types Proceed (Section 3.2). Its channel covers both instance feedback and factory/spec feedback. When no email capability is configured, submissions remain queued in the feedback log as staged and the user is prompted to send manually.
```

## 7.5 Agent Maker Agent Clarification

Earlier design notes referenced an Agent Maker Agent. Do not add Agent Maker Agent to the required or optional roster; it is not a runtime agent.

Agent creation and modification is a builder-framework capability, front-ended by a two-phase process:

```text
Phase A - Design: author and validate the agent's three design artifacts —
its catalog (or instance-registry) entry (§7A), its profile (§7B), and its
interviews file (§7C) — running the §10.3.1 overlap check, before the agent
may exist.

Phase B - Build: the generic build engine (§8, §12) executes the agent's
§7C Initialization interview and instantiates the validated entry + profile
+ interviews into the standard §5.1 file set.
```

Rationale:

```text
This avoids adding a new agent late in the design, preserves the approved roster, and avoids responsibility overlap.
```

## 7.6 Optional Agent Boundary Rule

Optional productive agents should be treated as specialized workers, not general coordinators.

Coordination remains primarily with the Chief of Staff Agent.

---

# 7A. Agent Catalog

## 7A.1 Definition and Intent

The Agent Catalog is a framework-level, design-time **data** file capturing each agent's identity and ownership. It separates concerns into three layers:

```text
Spec     = the rules (schema, vocabulary rule, validation, the SRP itself, §2.1).
Catalog  = the data (per-agent identity/ownership, machine-checked fields).
Generated §11 instruction file = a projection of the catalog entry plus
           instance choices. Narrative lives here, not in the catalog.
```

The catalog is distinct from the instance-level §10.3 Agent Registry and §10.4 AOS Map: the catalog is framework-level and read-only inside instances, governed by the §14.8 drift invariant (definition file, factory-owned).

## 7A.2 Controlled Vocabulary Rule (normative)

```text
- domains_owned MUST be drawn from vocabulary.domains (defined in the catalog
  file, §7A.6).
- domains_owned MUST be pairwise disjoint across all agents.
- Governance domain tokens MUST appear only on entries with kind: governance.
```

A new domain is a catalog edit, not a spec revision (§7A.6); this disjointness rule is the normative spec-level constraint the catalog must satisfy.

## 7A.3 Per-Agent Entry Schema

Only cross-cutting, machine-checked fields live here; narrative stays in the §11 instruction file.

```yaml
# Schema for each item under `agents:` in agent-catalog.yaml
slug: string                  # kebab-case, unique, matches §7.3
display_name: string
kind: governance | productive
tier: required | optional
one_line: string              # single-sentence identity

domains_owned: [domain-token] # from vocabulary; pairwise disjoint across all agents;
                              # governance tokens only when kind: governance

artifacts_owned: [glob]       # paths this agent is sole writer of;
                              # pairwise disjoint across all agents;
                              # includes own folder glob, the agent's
                              # /outputs/[agent-name]-agent/** glob (§4),
                              # + any SHARED paths claimed

inputs:  [domain-token]       # domains it consumes (owned by others) — informational
outputs: [domain-token]       # domains it produces into (should equal domains_owned)

collaborates_with:
  - agent: slug
    direction: handoff-to | handoff-from | escalates-to
    "on": string               # what triggers the edge (quoted: bare `on` is a
                               # YAML 1.1 boolean literal and must be quoted)

pre_authorized_actions: [string]   # the ONLY autonomous exceptions to non-destructive
                                    # default (§3.2/§3.3); kept in the catalog (§7A
                                    # decision O1) — agent configs (§16.1/§22)
                                    # cross-reference this rather than restating it
approval_required_actions: [string]
tool_notes: string                 # references the global matrix (§22); agent-specific
                                    # notes only, never restates matrix grants

# DERIVED — generated, not hand-authored. Listed for transparency/review.
non_responsibilities:
  - { claim: string, owned_by: slug }   # auto-generated from adjacent domains
```

## 7A.4 Catalog Data File

A pointer to the catalog data file and its shape; full content in §7A.6.

```text
Source:   design-spec/agent-catalog.yaml — the single source of truth,
          versioned with the spec (§1.6.1). Lives with the spec in design-spec/,
          alongside the agent-specs/ folders (§7B, §7C).
Rendered: the factory ships a RENDERED COPY at its root (/agent-catalog.yaml,
          sibling to /build-aos.md and /builders/) that all builders read.
Format:   YAML (machine-validated).
Ownership: framework-owned. Created/updated only by the framework; never
          edited by an operating agent (§14.8). Read-only inside instances.
```

## 7A.5 Validation Procedures

The Review Agent runs these checks against the catalog (tied to §27):

```text
V1. Every domain in domains_owned exists in vocabulary.domains.
V2. Governance domain tokens appear only on entries with kind: governance.
V3. domains_owned is pairwise disjoint across all entries.
V4. artifacts_owned is pairwise disjoint across all entries.
V5. Every collaborates_with.agent resolves to a real slug; reciprocal edges
    are consistent (every handoff-to has a matching handoff-from).
V6. non_responsibilities is consistent with neighbors' domains_owned.
V7. Every installed instance agent traces to a catalog entry OR an
    instance-registry entry (the two-scope check, §10.3.1).
V8. kind: governance entries match the AGENTS.md governance set; the
    removal prohibition becomes a machine-checkable property, not a prose
    name list.
```

**Derived CI artifact.** The repo ships `design-spec/catalog.schema.json` — a JSON Schema rendering of the §7A.3/§7A.6 shape — plus `scripts/validate-catalog.py`, run by repo CI on catalog pull requests. Together they mechanically enforce the shape/type surface of V1–V4 and V5's slug-resolution half. The JSON Schema is a **rendering, never the source of truth** (§1.6.1): markdown skeletons remain the normative expression for all document schemas, and no other schema is expressed in JSON. (Optionally extending JSON Schema validation to §15 frontmatter is deferred.)

## 7A.6 Catalog File Shape and Versioning

```yaml
# agent-catalog.yaml (framework-level, read-only in instances)
catalog_version: <semver>     # the catalog's own version track
spec_version: <semver>        # the spec it was rendered against

vocabulary:
  domains:
    # governance (reserved — kind: governance only)
    - security.permissions
    - memory.governance
    - orchestration.routing
    - review.retrospective
    - feedback.upstream
    # productive
    - communications.triage
    - communications.drafting
    - scheduling
    - task-tracking
    - project-coordination
    - research
    - writing
    - document-management
    - contacts
    - automation
    - learning

agents:
  - <per-agent entry, schema in §7A.3>
```

A new domain or new agent entry bumps `catalog_version`; a spec-driven schema change bumps `spec_version` (mirrors the `aos_version` vs `spec_version` split in §14.3).

---

# 7B. Agent Profiles

## 7B.1 Definition and Intent

An **Agent Profile** is a framework-level, design-time **narrative** file — one per agent — that holds the agent's behavioral detail: how it operates, its quality bar, failure modes, and example requests. It complements the Agent Catalog (§7A):

```text
Catalog (§7A) = structured, machine-checked identity/ownership (the DATA).
Profile (§7B) = human-readable behavioral narrative (the BEHAVIOR).
Generated §11 instruction file = catalog identity + profile narrative +
                                 instance-specific choices (the PROJECTION).
```

A profile MUST reference the catalog for identity and MUST NOT restate `domains_owned`, responsibilities, non-responsibilities, collaboration edges, inputs/outputs, or approval actions — those are catalog-owned and projected into §11 (§7A, §11). This confines the profile to behavior and keeps a single source of truth for identity (§1.6.1). Profiles are framework-owned **definition files** (§14.8), read-only inside instances.

## 7B.2 Location and Files

```text
Source:   design-spec/agent-specs/[agent-name]-agent/profile.md — one per-agent
          folder for each agent in §7.3, the single source of truth, versioned
          with the spec. The same folder holds the agent's interviews.md (§7C).
Rendered: the factory ships rendered copies (/agent-specs/) that the build
          engine reads.
Ownership: framework-owned; read-only inside instances (§14.8).
```

## 7B.3 Profile Schema — Full Agent Lifecycle

Every profile describes the agent's **complete lifecycle** in five sections. Frontmatter carries `file_type: agent_profile` (§15.4) and the `slug` that matches §7.3 and the catalog entry.

```markdown
---
title: [Display Name] — Agent Profile
file_type: agent_profile
slug: [agent-name]-agent
spec_version: <semver>
---
# [Display Name] — Profile

> Identity (Purpose, Responsibilities, Non-Responsibilities, Inputs, Outputs,
> Collaboration, Approval) is defined in the catalog entry (§7A) and projected
> into §11. This profile adds behavior only; it does not restate identity.

## Initialization
## Operation
### Behavioral Summary
### Operating Procedure
### Primary Workflow
### Autonomy & Judgment
### Escalation Behavior     (narrative only; identity edges live in the catalog)
### Quality Standards
### Failure Modes
### Example Requests
### Maintenance Notes
## Usage-Driven Evolution
## Update
## Retirement
```

The five lifecycle sections are normative:

**Initialization.** REFERENCES the agent's scripted Initialization interview in its interviews file (§7C) and MUST NOT restate its questions (mirrors the §7B.1 no-restatement rule). The script is normative for question content, order, and captured fields; delivery stays conversational (§1.5, §9.1).

**Operation.** The behavioral narrative — the nine sub-sections above, unchanged in meaning from the pre-lifecycle profile schema. This is what §7B.4 projects into the §11 instruction file.

**Usage-Driven Evolution.** How usage learnings and user requests are implemented as changes to the agent instance's **data layer only**: the agent's memory and learnings files and `/memory/preferences.md`, which shape behavior at runtime. Factory-generated definition files are **never modified during evolution — not by regeneration, not by in-place edit**. (This strengthens the §14.8 drift invariant in effect — from "route definition changes through the factory" to "definition files do not change at all during evolution"; §14.8 itself is unchanged.) A desired change that cannot be expressed in the data layer is out of evolution's scope: it is handed to the Feedback Agent as an enhancement candidate (an upstream proposal), never implemented locally.

**Update.** What happens when a new factory release (`spec_version` change) is applied to an existing AOS: the agent's definition files are regenerated (`Proceed`-gated per §14.7/§14.8); its data files are never overwritten; and this section carries any **MIGRATION INSTRUCTIONS** needed to preserve accumulated memory, learnings, preferences, and data-layer behavior — e.g. carrying entries forward when a release changes an entry-block schema, renames a memory field, or relocates a file. Where a migration requires user input, the questions live in the Update interview of the agent's §7C interviews file; the MIGRATION INSTRUCTIONS reference them. Ends with a post-update verification that accumulated preferences still shape the agent's behavior as before. Update sections are executed by the factory's update flow (§14.4 modes), never by the agents themselves. A release with no structural changes has a trivial Update section ("no migration required").

**Retirement.** The user-request and usage-pattern signals indicating the agent is no longer needed (e.g. no invocations across N review cycles — surfaced by the Review Agent at quarterly review, suggestion only), and the retirement procedure (§10.2). Retirement remains `Proceed`-gated (§3.2, §10.2). Required governance agents state here that they cannot be retired (§2.3).

Lifecycle **states** (§10.1) stay in the registry/manifest; the profile describes lifecycle **behavior** only.

## 7B.4 Projection into the Instruction File

The generated §11 instruction file draws its **identity** sections from the catalog (§7A, §11) and its **narrative** sections — `Workflows`, `Autonomy Rules`, `Escalation Rules`, `Operating Procedure`, `Quality Standards`, `Failure Modes`, `Example Requests`, `Maintenance Notes` — from the agent's profile, tailored with instance-specific choices. Builders (§12) read BOTH the catalog entry and the profile; they do not hand-author identity or narrative that these sources already provide.

## 7B.5 Contributor Path and Validation

Adding an agent is a two-phase, design-first process (the §7.5 "Agent Maker" primitive):

```text
Phase A - Design: author the agent's THREE design artifacts — catalog entry
          (§7A), profile (§7B), and interviews file (§7C) — then run the
          §7A.5 and §10.3.1 checks before the agent may exist.
Phase B - Build: the generic build engine (§8, §12, §26) executes the §7C
          Initialization interview and instantiates the validated entry +
          profile + interviews into the standard §5.1 file set.
```

The Review Agent's catalog validation (§7A.5, §27) extends with these profile and interview checks:

```text
V9.  Every agent in §7.3 has exactly one profile, and every profile's slug
     resolves to a catalog entry (full, one-to-one coverage).
V10. No profile restates catalog-owned identity fields (behavior-only check):
     domains_owned, responsibilities/non-responsibilities, collaboration edges,
     inputs/outputs, and approval actions live only in the catalog.
V11. Every profile carries the five §7B.3 lifecycle sections (Initialization,
     Operation, Usage-Driven Evolution, Update, Retirement).
V12. Every §7.3 agent has exactly one agent-specs/[agent-name]-agent/ folder
     containing profile.md and an interviews.md conforming to the §7C schema.
     (The V9 one-to-one rule applies to agents only; aos-interviews.md sits
     outside it.)
V13. No profile restates interview content — the Initialization and Update
     sections reference the §7C scripts only (mirrors V9/V10).
```

---

# 7C. Agent Interviews

## 7C.1 Definition and Intent

An **Agent Interviews file** is a framework-level, design-time artifact — one per agent, sibling to the profile — holding every **scripted interview** the agent runs to configure itself from user input:

```text
Initialization interview — executed by the generic build engine (§8, §12)
                           when the agent is built (§7B.3 Initialization).
Update interview          — the user-input questions a factory-release
                           migration needs (§7B.3 Update); "no questions"
                           when the release requires no migration input.
```

The script is **NORMATIVE for question content, order, and captured fields**; delivery stays conversational (§1.5, §9.1) — paraphrase is allowed (wording may adapt; the canonical `ask` text is not verbatim-required), but questions are never added, removed, or reordered. Evolution-time preference capture is OUT of scope (emergent by design; the §7B.3 Usage-Driven Evolution data-layer rules govern it).

## 7C.2 Location and Files

```text
Source:   design-spec/agent-specs/[agent-name]-agent/interviews.md — in the
          same per-agent folder as profile.md (§7B.2). The AOS-level setup
          interview lives at design-spec/aos-interviews.md, owned by
          build-aos.md (§12.1).
Rendered: the factory ships rendered copies (/agent-specs/, /aos-interviews.md)
          that the build engine and build-aos read.
Ownership: framework-owned; read-only inside instances (§14.8).
file_type: interview_script (§15.4).
```

## 7C.3 Interview File Schema

```markdown
---
title: [Display Name] — Agent Interviews
file_type: interview_script
slug: [agent-name]-agent
spec_version: <semver>
---
# [Display Name] — Interviews

## Initialization Interview
[question entries]

## Update Interview
[question entries, or "No questions — no migration required at this release."]
```

Each question is an entry with this schema:

```yaml
- id:        stable slug
  ask:       canonical question wording
  type:      choice | text | boolean | path
  options:   [ ... ]            # choice only
  default:   value | none
  skippable: yes | no           # yes ⇒ fast path resolves to default
  when:      condition on earlier answers | always
  captures:  target field / file the answer configures
```

## 7C.4 Execution Rules

```text
- The §9.1 batch style (ask, summarize, recommend, preview, Proceed) is
  unchanged; the script feeds it.
- Fast path (deterministic §9.1 move-faster exception): skippable questions
  resolve to their defaults; no other question may be dropped.
- Required agents have shorter scripts; optional productive agents ask about
  goals, scope, tools, output preferences, approval boundaries, and
  collaboration patterns (§26).
- Profiles reference these scripts and never restate them (V13, §7B.5).
```

---

# 8. Builder Framework Structure

## 8.1 Build Coverage for All Agents

The factory must be able to build every approved agent, even if the user does not initially install every agent. This coverage is provided by **one generic build engine** plus per-agent design artifacts: the engine instantiates any validated catalog entry (§7A) + profile (§7B) + interviews file (§7C) into the standard §5.1 file set. Adding an agent requires one `agent-specs/` folder (profile.md + interviews.md) plus a catalog entry (§7.5 Phase A) — no new builder file.

This makes the AOS extensible.

The engine is a **builder-framework file, not a runtime agent** (consistent with §7.5). The former per-agent `build-[agent-name]-agent.md` files are removed; their interview content lives on as §7C scripts.

## 8.2 Builder Folder Location

Builder files should live in:

```text
/builders
```

Approved structure:

```text
/builders
  build-aos.md      (the master AOS builder; §12.1)
  build-agent.md    (the generic agent build engine; §12)
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
Runs the interactive setup process (executing aos-interviews.md, §7C/§12.1)
and builds a specific AOS instance.

build-agent.md
The generic build engine: builds any one agent inside an AOS instance by
executing that agent's §7C Initialization interview and instantiating its
catalog entry + profile + interviews into the §5.1 file set.
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

The pre-build preview uses this defined block:

```markdown
## Files to Create
## Decisions Applied
## Assumptions
## Approval
[the Proceed ask — type exactly `Proceed` to create the files above]
```

Exception:

```text
If the user explicitly asks to move faster, Cowork can ask fewer questions and rely more heavily on documented assumptions.
```

**Script vs. delivery (normative).** Interview questions are defined as scripted entries in the relevant §7C interviews file (per-agent `interviews.md`, or `aos-interviews.md` for AOS setup). The script is normative for question content, order, and captured fields; delivery stays conversational in the batch pattern above — paraphrase allowed, never adding, removing, or reordering questions. The move-faster exception is deterministic: **fast path = questions marked `skippable: yes` resolve to their `default:` values; no other question may be dropped** (§7C.4).

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
3. Provision the AOS Workspace root: ensure /aos-router.md and /CLAUDE.md exist, copying them from the factory's shipped example copies (templates/aos-router.md, templates/CLAUDE.md; Section 28.2). Create them if absent; if either already exists, do not overwrite without a separate Proceed (Sections 2.4, 3.2, 4.1).
4. Create global config, memory, log, workflow, template, inbox, and archive files
5. Confirm the generic build engine and every approved agent's design artifacts (catalog entry, profile, interviews) exist
6. Build required agents
7. Ask the user to select at least one optional productive agent
8. Build selected optional agents
9. Update the agent registry
10. Produce an AOS setup summary
```

The step 10 **AOS setup summary** is a saved file: `/logs/aos-build-summary.md`, file_type `build_summary` (§15.4), with a schema parallel to the Section 13 per-agent Build Summary (Files Created, Key Decisions, User Preferences Captured, Permissions and Boundaries, Open Questions, Suggested Next Steps) at instance scope.

Actual file creation still waits until the user types:

```text
Proceed
```

## 9.4 Installing Optional Agents Later

The user can add optional agents later by invoking the generic build engine for that agent.

Example:

```text
Build the Research Agent
```

Routes to:

```text
/builders/build-agent.md  (resolving the research-agent catalog entry and
                           its /agent-specs/research-agent/ folder)
```

---

# 10. Agent Lifecycle and Registry

## 10.1 Agent Lifecycle States

Every possible agent should have one of these lifecycle states:

```text
Available
The agent's design artifacts (catalog entry, profile, interviews) exist in the factory, but the agent has not been selected or built.

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

| Agent | Status | Required? | Agent Folder | Notes |
|---|---|---:|---|---|
| Security Agent | Active | Yes | /agents/security-agent/ | Required core agent |
| Chief of Staff Agent | Active | Yes | /agents/chief-of-staff-agent/ | Required core agent; joint owner of /aos-router.md |
| Research Agent | Available | No | Not created | Optional productive agent |
```

This table is normative: frontmatter carries `file_type: config` (§15.4); the file is a mixed file under §14.8 (rendered structure + instance rows), updated by targeted, approval-gated merge. All agents are built by the generic build engine (`/builders/build-agent.md`, §8) from their `agent-specs/` design artifacts, so the registry carries no per-agent builder column.

The Chief of Staff Agent's registry entry should note its joint ownership of the AOS Workspace router (`/aos-router.md`), shared with every other AOS instance's Chief of Staff Agent, so router responsibility is discoverable from the registry as well as the agent definition.

### 10.3.1 Instance-Scope Overlap Check

The instance Agent Registry absorbs the catalog's ownership fields (`domains_owned`, `artifacts_owned`) for any agent that exists in an instance, including contributor/user-created agents born inside that instance.

When a new instance agent is added, its `domains_owned` and `artifacts_owned` are validated against BOTH:

```text
1. The framework catalog's reserved domains and existing entries (§7A).
2. Every other agent already registered in this instance.
```

A new agent may not claim a reserved governance token or a domain/artifact already owned at either scope. This keeps the §14.8 drift invariant intact: the framework catalog stays read-only in instances; the instance registry is the instance-scope ownership ledger.

Each instance-born agent's registry entry carries an **absorbed-ownership block** in this format (making the overlap check mechanical):

```yaml
- slug: <agent-name>-agent
  domains_owned: [ ... ]
  artifacts_owned: [ ... ]
  validated_against: catalog <catalog_version> + registry on <date>
```

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

The map's installed-vs-available distinction is the data source for proactive surfacing of uninstalled agents: the Review Agent's weekly/quarterly advertising check (§17.3, §17.5) and the user guide's Available Agents subsection (§16.6) are both projected from the registry/map (regenerable projections per §14.8). Surfacing is suggestion only; installation remains the normal §9.4 flow.

File schema (`/aos-map.md`, file_type `aos_map`, §15.4):

```markdown
---
title: AOS Map
file_type: aos_map
---
# AOS Map

## Overview
[one paragraph: instance name, purpose, agent counts by status]

## Agents

| Agent | Status | Required? | Folder |
|---|---|---:|---|
[one row per agent — installed, available, paused, and retired;
all agents are built by the generic build engine (§8), so there
is no per-agent builder column]

## Folder Map
[the top-level §4 tree with one line of purpose per folder]
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

The sections below are **projected from the agent's catalog entry** (§7A) rather than hand-written:

```text
# Purpose                <- one_line (expanded)
# Responsibilities       <- domains_owned
# Non-Responsibilities   <- DERIVED non_responsibilities (the SRP enforcer)
# Inputs                 <- inputs
# Outputs                <- outputs
# Collaboration Rules    <- collaborates_with edges
# Approval Requirements  <- approval_required_actions + pre_authorized_actions
```

The remaining sections are **projected from the agent's profile** (§7B) — `Workflows`, `Autonomy Rules`, `Escalation Rules`, `Operating Procedure`, `Quality Standards`, `Failure Modes`, `Example Requests`, `Maintenance Notes` — tailored with instance-specific choices rather than hand-authored from scratch. Identity comes from the catalog; behavior comes from the profile.

The **Non-Responsibilities** section is especially important because it enforces the Single Responsibility Principle.

---

# 12. Generic Build Engine Schema

The generic build engine `/builders/build-agent.md` (file_type `agent_builder`) builds any one approved agent. It should follow this structure:

```markdown
# Build Agent (Generic Engine)

## Engine Purpose

## When to Use This Engine

## Operating Mode

## Inputs
   (the target agent's catalog entry (§7A), profile (§7B), and
    interviews file (§7C) — resolved from the invocation, e.g.
    "Build the Research Agent" → research-agent)

## Interview Execution
   (execute the agent's §7C Initialization interview: script normative
    for content/order/captures, delivery conversational per §9.1;
    fast path = skippable questions resolve to defaults)

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

`Agent Instruction Generation Rules` must render `Purpose` / `Responsibilities` / `Non-Responsibilities` / `Inputs` / `Outputs` / `Collaboration Rules` / `Approval Requirements` from the agent's `agent-catalog.yaml` entry (§7A); the engine does not duplicate this content as hand-authored prose. It must likewise render the narrative sections (`Workflows`, `Autonomy Rules`, `Escalation Rules`, `Operating Procedure`, `Quality Standards`, `Failure Modes`, `Example Requests`, `Maintenance Notes`) from the agent's profile Operation section (§7B), tailored with instance choices captured by the Initialization interview; the engine reads the catalog entry, the profile, and the interviews file.

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

`Builder Operating Mode` should combine coach and collaborator behavior (Section 1.5), default to dry-run / preview, and gate file creation behind `Proceed`. `Interview Flow` follows the batch pattern in Section 9.1, executing the scripted AOS setup interview in `aos-interviews.md` (Section 7C) — the script is normative for question content, order, and captured fields; `Discovery Questions` and `Recommended Defaults` reference that script rather than restating it. `AOS Setup Sequence` follows the setup sequence in Section 9.3, which includes provisioning the AOS Workspace root files (`/aos-router.md`, `/CLAUDE.md`) from the shipped example copies (Section 28.2), non-destructively — created when absent and overwritten only after a separate `Proceed`. `Folder Structure to Create` uses the Section 4 tree, created as a sibling AOS root per Section 4.1. `Global Files to Create` uses the Section 6 list, including `/docs/aos-user-guide.html`, which is generated from the skeleton in Section 16.6 with an Invocation Reference table scoped to the installed agents. `Optional Agent Selection` must enforce that at least one optional productive agent is chosen (Sections 2.3 and 7.2). `Validation Checklist` uses the completeness checks in Section 27.

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

`/aos-manifest.md` should include (full example; frontmatter carries `file_type: aos_manifest`, §15.4, and the version/date facts; the four agent lists use the table format shown):

```markdown
---
title: AOS Manifest
file_type: aos_manifest
spec_version: <semver>
aos_version: <semver>
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
# AOS Manifest

## AOS Name
[instance name]

## AOS Version
[aos_version — the authoritative live value, §14.3.1]

## Spec Version
[spec_version the instance was generated from / last conformed to]

## Created Date

## Last Updated

## Installed Agents

| Agent | Status | Tier | Installed date |
|---|---|---|---|

## Active Agents

| Agent | Status | Tier | Installed date |
|---|---|---|---|

## Paused Agents

| Agent | Status | Tier | Installed date |
|---|---|---|---|

## Retired Agents

| Agent | Status | Tier | Installed date |
|---|---|---|---|
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
  that made the change (the Chief of Staff coordinates), using the Section 16.8
  entry schema (its Type and Version Impact fields drive this reconciliation).
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

This changelog describes changes to the builder framework itself, not changes to a generated AOS instance. Its release-entry schema is defined in Section 16.9.

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

**Data file.** A file whose content accumulates from the instance's operation and the user's input, and is therefore not derivable from the spec. *Test: regenerating this file from the factory would destroy information the user or agents rely on.* If true, it is a data file. Data files are **owned by the operating agents**: the factory creates each one once (empty or seeded) and never overwrites it on update; agents append to and maintain it under the normal non-destructive and approval rules (Sections 2.4, 3). Examples: everything in `/memory`, `/logs`, `/projects`, `/outputs` (standalone agent deliverables, Section 4), `/inbox`, and `/archive`, and the instance-specific values in `/aos-manifest.md`.

**Mixed and derived files.** Where a file combines a rendered structure with instance data (for example the rows of `/configs/agent-registry.md`, the values in `/aos-manifest.md`), apply the strict test: if the file contains *any* non-regenerable information it is treated as a **data file** for update purposes — updated by targeted, approval-gated merge, never wholesale overwrite — or it is split so each file is purely one kind. A **projection** (for example the AOS User Guide, Section 16.6) is a regenerable view built from definitions plus named data inputs; it is treated as a **definition file** for update purposes (safe to regenerate), with its data inputs stored separately as data files.

`agent-catalog.yaml` (§7A) is a **definition file**: framework-owned, created and updated only by the framework, never edited by an operating agent. It is read-only inside instances. The instance registry's absorbed ownership fields (§10.3.1) are **data** — they describe instance-born agents — and are treated per the strict mixed-file test above: targeted, approval-gated merge, never wholesale overwrite. The `agent-specs/` files — each agent's `profile.md` (§7B) and `interviews.md` (§7C), and `aos-interviews.md` — are likewise **definition files**: framework-owned, created and updated only by the framework, read-only inside instances, and regenerable from the spec.

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

**Stamping rule (mandatory).** Every file the factory generates — builder files, agent instruction files, and all other generated markdown — records, in its frontmatter, the `spec_version` it was rendered from. Generated instance files additionally carry `aos_version` (Sections 15.2–15.3). `agent-catalog.yaml`'s `catalog_version` + `spec_version` header keys (§7A.6) satisfy this same stamping rule for the catalog.

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
feedback_log
builder_changelog
documentation
project_doc
handoff_summary
build_summary
agent_instruction
aos_router
project_instructions
design_spec
agent_catalog
agent_profile
interview_script
```

`design_spec` applies to this design specification itself (`aos-factory-design-specification.md`), the source document the AOS Factory is generated from. It is the one source/design artifact in the vocabulary; the other types all describe factory-generated files.

`aos_router` applies to the AOS Workspace root router (`/aos-router.md`) that resolves the active target — the AOS Factory, or a generated AOS instance — before any workflow runs. `project_instructions` applies to the root project instruction file (`/CLAUDE.md`) that serves as the session-start instruction file and wires in the router. Both files live at the AOS Workspace root, alongside the AOS Factory and AOS instance folders, because they govern selection *across* targets rather than belonging to any one of them.

`change_log` applies to a generated AOS instance log (`/logs/change-log.md`). `builder_changelog` applies to the reusable builder framework changelog (`/builder-changelog.md`), which also tracks the plugin version when the framework is distributed (Section 28). The two are tracked separately so framework files can be distinguished from instance files via frontmatter. `feedback_log` applies to the Feedback Agent's staging log (`/logs/feedback-log.md`, Section 16.7) — a data file per Section 14.8.

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
              (the end-of-build record; see Section 13) and the instance-level
              /logs/aos-build-summary.md (the AOS setup summary; Section 9.3)

project_doc   project-brief.md, project-plan.md, project-status.md,
              and project-notes.md

documentation /docs/aos-user-guide.html (HTML metadata is carried via meta
              tags or an HTML comment rather than YAML frontmatter)

aos_router    /aos-router.md (AOS Workspace root, shared across instances and factory)

project_instructions
              /CLAUDE.md (AOS Workspace root, session-start instruction file)

agent_catalog design-spec/agent-catalog.yaml (source) and its rendered factory
              copy /agent-catalog.yaml; framework-level, read-only in
              instances; see Section 7A

agent_profile design-spec/agent-specs/[agent-name]-agent/profile.md (source)
              and its rendered factory copy; framework-level lifecycle and
              behavior narrative per agent, read-only in instances; see
              Section 7B

interview_script
              design-spec/agent-specs/[agent-name]-agent/interviews.md and
              design-spec/aos-interviews.md (sources) and their rendered
              factory copies; scripted configuration interviews, read-only
              in instances; see Section 7C
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

For agent configs, `Inherited Rules` is especially important because agent configs should reference global permissions instead of duplicating them. Likewise, the `Tool Access` section must reference the global tool access matrix (`/configs/tool-access-matrix.md`), which is authoritative, and list only agent-specific notes or requests rather than restating or overriding matrix grants (see Section 22). For an agent with `pre_authorized_actions`, the config's `Tool Access` section adds a one-line cross-reference to the agent's catalog entry (§7A) rather than restating the pre-authorized actions.

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

Entries under `## Memory Entries` use this dated entry block — the seven §20.3 fields, embedded by `/templates/memory-entry-template.md` (§18.6):

```markdown
### YYYY-MM-DD — [Entry Title]

**Type:** [preference | fact | decision | person | project | learning]
**Summary:**
**Source:**
**Confidence:** [high | medium | low]
**Owner:** [agent or user]
**Review Date:** YYYY-MM-DD
**Notes:**
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
- Managing Agents — how to add, pause, retire, and restore agents (points to /builders); includes an Available Agents subsection listing agents not yet installed, projected from /configs/agent-registry.md and /aos-map.md (Section 10.4)
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

## 16.7 Feedback Log Schema

The Feedback Agent's staging log (`/logs/feedback-log.md`, file_type `feedback_log`, §15.4) — a **data file** per §14.8: created once (empty) at build, never overwritten by a factory update, appended by the Feedback Agent. Staged entries work offline; nothing leaves the machine without scrubbing and `Proceed`.

```markdown
---
title: Feedback Log
file_type: feedback_log
---
# Feedback Log

## Log Rules

- Append-only; entries are never deleted (mark discarded instead).
- Every outbound send requires Security Agent scrub + Proceed (§3.2).

## Entries

### YYYY-MM-DD — [Title]

**Type:** bug | enhancement
**Status:** staged | approved | sent | discarded
**Scrub:** pending | done (Security Agent, date)
**Summary:** [what was observed or proposed, scrubbed of names, project
content, and memory quotes before send]
**Sent:** date | —
```

## 16.8 Change Log Entry Schema

Entries in `/logs/change-log.md` (file_type `change_log`, a data file per §14.8) use this schema; the §14.3.1 `aos_version` reconciliation reads it:

```markdown
### YYYY-MM-DD — [Change Title]

**Change:** [what changed]
**Type:** PATCH | MINOR | MAJOR
**Agent:** [agent that made the change]
**Files Affected:** [paths]
**Version Impact:** none | bump applied | bump pending
```

## 16.9 Builder Changelog Schema

`/builder-changelog.md` (file_type `builder_changelog`, §14.5) mirrors the revision-history conventions: a version table at the top mapping each `spec_version` to its date and one-line summary, followed by versioned entries in reverse chronological order. Each entry is headed `## <spec_version> — <title> (<date>)` and notes the plugin version when the framework is distributed (§28).

## 16.10 Router File Schema

`/aos-router.md` (AOS Workspace root, file_type `aos_router`, §15.4) follows this schema. The shipped example (`templates/aos-router.md`, §28.2) is a rendering of it; the build-aos router-generation step emits this structure — including the call-name resolution language and the registry's Call name column — by default.

```markdown
---
title: AOS Instance Router
file_type: aos_router
spec_version: <semver>
---
# AOS Instance Router

## Resolution Order      (stop at the first tier that applies)

1. Explicit user override — the user names a target, or opens the prompt
   with a registered call name.
2. Framework vs. instance — unambiguous factory work routes to the factory.
3. Session pin.
4. Signal match — only on a clear winner per the confidence bar.
5. Fallback: ASK. Never silently pick; never merge instances.

## Registered Targets

| Target | Type | Call name | Folder | Signals |
|---|---|---|---|---|

## Session Pin

## Logging
```

Normative rules:

```text
- Call-name matching: case-insensitive; start-of-prompt only (a mid-sentence
  mention is not a trigger); a leading greeting and/or trailing comma is
  handled gracefully. Addressing by call name also sets the session pin,
  same as "switch to <instance-name>".
- Registry as source of truth: call names live only in the Registered
  Targets table; the matching rule references the registry and never
  hardcodes a name. A call name is unique within a router's registry; at
  build time a collision is rejected and unused alternatives are suggested.
  A call name is optional — an instance without one is routed by the other
  tiers.
- Framework-vs-instance carve-out: a call-name match is an explicit user
  override — the highest tier — but it does not override the
  framework-vs-instance check. A prompt that both opens with a call name
  and is unambiguously factory work is treated as AMBIGUOUS: ask, or note
  the routing choice; never silently route.
- Ask-Don't-Guess: mixed or weak signals fall through to ASK.
- Session Pin: "use/switch to <target>" pins; "clear AOS" unpins; state the
  active target on the first line of any routed output.
- Logging: non-trivial routing choices are recorded per §17.1/§19.3.
```

## 16.11 Workspace-Root CLAUDE.md Schema

`/CLAUDE.md` (AOS Workspace root, file_type `project_instructions`, §15.4) has these required sections: **router wiring** (read `/aos-router.md` and resolve the active target before any workflow), **planning-mode rules** (the exact-`Proceed` gate), and the **AGENTS.md include**. The shipped example (`templates/CLAUDE.md`, §28.2) is a rendering of this schema.

## 16.12 Global Permissions Seed

`/configs/global-permissions.md` (file_type `config`, §16.1) is seeded as a skeleton mapping the three §3.4 permission levels to the §3.2/§3.3 action lists — Level 1 sections list the §3.3 safe autonomous actions, Level 2 sections list the §3.2 approval-required actions, Level 3 lists prohibited actions. The seed restates nothing beyond those lists and does not modify §3 itself; instance-specific tightening or loosening happens in this file per §3.5.

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

Instance resolution (first step): before gathering any inputs, the Chief of Staff resolves the active target via `/aos-router.md` — explicit override (a named target, or a registered call name opening the prompt; §16.10), then framework-vs-instance, then session pin, then signal match, else ASK. A call-name match is the highest tier but does not override the framework-vs-instance check (§16.10 carve-out). The brief runs against exactly one resolved instance (or, for a cross-instance request, each instance separately with labeled output); it never blends instance memory. State the resolved target on the first line of the brief (e.g. `**[work-aos]** Daily Brief — …`). Generated `daily-startup-workflow.md` files must include this resolution step ahead of input gathering.

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

These promotion categories mirror the full set of promotion targets in the inbox-to-task workflow (Sections 17.6 and 31). The nine categories above are the startup brief's defined skeleton: generated `daily-startup-workflow.md` files render the brief with these categories as its sections, in this order.

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

The weekly review includes an advertising check: the Review Agent asks whether any `Available` (uninstalled) agent would close a gap observed this week (Section 10.4), including request patterns the Chief of Staff has handed over. Suggestion only — installation remains the Section 9.4 flow. A declined suggestion is logged and not re-raised until the next quarterly review or a material change in usage pattern (Section 17.5).

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

The Feedback Agent's self-examination also runs at monthly review: it examines the instance's learnings and preferences for enhancement candidates and presents them to the user for accept / edit / discard (staged in `/logs/feedback-log.md`, Section 16.7); outbound submissions are sent only after Security Agent scrubbing and `Proceed`.

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

The Feedback Agent's self-examination also runs at quarte