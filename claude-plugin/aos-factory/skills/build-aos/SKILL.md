---
name: build-aos
description: Build a complete Agentic Operating System (AOS) instance from scratch — folder structure, the five required governance agents (Security, Memory, Chief of Staff, Review, Feedback), at least one optional productive agent, global workflows, templates, configs, logs, and the AOS User Guide. Use when the user wants to create, set up, or stand up their AOS. Nothing is written until the user types exactly `Proceed`.
---
# Build AOS

The master builder. It runs the interactive setup process and builds a complete
AOS instance from the design artifacts shipped with the factory (design spec
§8.4, §12.1).

## Builder Purpose

Stand up one complete, governed AOS instance: its folder structure, the five
required governance agents, at least one optional productive agent, the global
config / memory / log / workflow / template files, the AOS User Guide, and the
setup summary. The instance is created as a sibling folder inside the AOS
Workspace (§4.1). This builder never writes into an instance except during an
authorized build, and never writes destructively (§4.1).

## When to Use This Builder

- Initial AOS setup ("Build my AOS", "Set up my AOS", "Stand up an AOS").
- There must be no existing AOS instance in the workspace, or the user must
  explicitly authorize working against a new sibling instance (single-instance
  model, §1.6.6). To add one agent to an existing instance, use
  `/builders/build-agent.md` instead (§9.4).

## Builder Operating Mode

- Combine **coach** and **collaborator** behavior (§1.5): explain concepts when
  the user needs orientation; switch to collaborator when making design choices;
  recommend sensible defaults; move forward with documented assumptions on
  low-risk details; defer to the user on important decisions.
- Default to **dry-run / preview**: describe what will be built before building.
- Gate all file creation behind the user typing exactly `Proceed` (§3.1). No
  folders or files are created before that. Approval is action-specific (§2.5).
- Apply the global file-safety rule (§3.1): never overwrite, delete, move,
  rename, or archive without a separate `Proceed`.

## Interview Flow

Execute the scripted AOS setup interview in `/aos-interviews.md` (§7C, §12.1).
That script is **normative** for question content, order, and captured fields;
this builder does not restate it. Deliver it conversationally in the batch
pattern (§9.1):

1. Ask a small batch of questions (from the script).
2. Summarize what the user said.
3. Recommend defaults for anything vague.
4. Ask for approval on important design decisions.
5. Generate a build plan / pre-build preview (the block below).
6. Ask the user to type `Proceed` before creating files.

Fast-path exception (§9.1, §7C.4): if the user asks to move faster, questions
marked `skippable: yes` resolve to their `default:` values; no other question
may be dropped, added, or reordered.

Pre-build preview block (shown before `Proceed`, before any files exist — §9.1;
this is distinct from the post-build AOS Setup Summary below):

```markdown
## Files to Create
## Decisions Applied
## Assumptions
## Approval
[the Proceed ask — type exactly `Proceed` to create the files above]
```

## Discovery Questions

Defined by the `/aos-interviews.md` Initialization Interview (§7C): AOS purpose,
AOS name, first optional productive agent(s), and optional memory seeds. Do not
restate the questions here — read them from the script.

## Recommended Defaults

Defined by the `default:` values in `/aos-interviews.md` (§7C): propose an AOS
name as a file-safe slug from the stated purpose (§29); recommend a starter set
of optional agents by purpose category; seed memory only from what the user
supplies (never fabricate). Confirm important defaults with the user (§1.5).

## AOS Setup Sequence

Follow §9.3, in order:

1. The factory framework already exists (this plugin/factory).
2. Create the top-level folder structure (below).
3. Provision the AOS Workspace root: ensure `/CLAUDE.md` and `/AGENTS.md` exist,
   copying each from the factory's shipped example copies (`templates/CLAUDE.md`,
   `templates/AGENTS.md`; §28.2). Create each when absent; if either already
   exists, do **not** overwrite it without a separate `Proceed` (§2.4, §3.2,
   §4.1).
4. Create the global config, memory, log, workflow, template, inbox, and archive
   files (below).
5. Confirm the generic build engine and every approved agent's design artifacts
   (catalog entry, profile, interviews) exist.
6. Build the five required governance agents (via the generic engine).
7. Ask the user to select at least one optional productive agent (§2.3, §7.2).
8. Build the selected optional agents (via the generic engine).
9. Update the agent registry and AOS map.
10. Offer to schedule the rhythmic workflows as Cowork Scheduled Tasks.
11. Produce the AOS setup summary (`/logs/aos-build-summary.md`).

Actual file creation waits until the user types `Proceed`.

## Folder Structure to Create

Create the instance as a sibling AOS root `/[aos-name]/` (§4, §4.1):

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

## Global Files to Create

Create the §6 global files. Stamp each with `spec_version` and `aos_version`
(§15). Use the schemas in §16 and the seeds noted:

```text
/aos-manifest.md                         (§14.3; aos_version starts at 1.0.0)
/aos-map.md                              (§10.4)
/configs/global-permissions.md           (seed from §3.4 levels + §3.2/§3.3 lists — §16.11)
/configs/agent-registry.md               (§10.3)
/configs/tool-access-matrix.md           (§22; Security Agent owns)
/memory/user-profile.md
/memory/preferences.md
/memory/people.md
/memory/projects.md
/memory/decisions.md
/memory/agent-learnings-index.md          (§6.1 index table)
/logs/aos-decision-log.md                 (§16.5)
/logs/change-log.md                       (§16.8)
/logs/feedback-log.md                     (§16.7; empty, owned by Feedback Agent)
/workflows/daily-startup-workflow.md      (§17.1)
/workflows/end-of-day-shutdown-workflow.md (§17.2)
/workflows/weekly-review-workflow.md      (§17.3)
/workflows/monthly-review-workflow.md     (§17.4)
/workflows/inbox-to-task-workflow.md      (§17.5)
/workflows/project-kickoff-workflow.md    (§17.6)
/workflows/decision-capture-workflow.md   (§17.7)
/workflows/memory-review-workflow.md      (§17.8)
/templates/status-report-template.md      (§18.1)
/templates/project-brief-template.md      (§18.2)
/templates/decision-entry-template.md     (§18.3)
/templates/handoff-summary-template.md    (§18.4)
/templates/approval-request-template.md   (§18.5)
/templates/memory-entry-template.md       (§18.6)
/docs/aos-user-guide.html                 (§16.6 skeleton; see below)
```

**AOS User Guide (`/docs/aos-user-guide.html`).** Generate from the §16.6
skeleton with an Invocation Reference table scoped to the agents actually
installed. The Table of Contents and the embedded Change Log are **mandatory**
and generated complete (§16.6 generation rules): every section below the TOC
carries a unique `id` anchor (`change-log`, `introduction`, `folder-orientation`,
`agents-overview`, `core-rules-safety`, `operating-rhythms`, `managing-agents`,
`invocation-reference`); every TOC entry is an in-page link to its anchor; the
Change Log sits immediately after the TOC and is seeded with one dated
"Initial guide generated during AOS setup" entry. Run the §16.6 consistency
checks and correct the guide before finishing. Carry metadata via meta
tags / an HTML comment (file_type `documentation`, AOS name, `aos_version`,
`spec_version`, `last_updated`) — not YAML frontmatter.

## Required Agent Orchestration

Build all five required governance agents by invoking the generic build engine
(`/builders/build-agent.md`) for each, resolving each agent's catalog entry
(`/agent-catalog.yaml`) and its `/agent-specs/[agent-name]-agent/` folder
(profile + interviews):

```text
security-agent
memory-agent
chief-of-staff-agent
review-agent
feedback-agent
```

Governance before productivity (§1.6.2): build all five before any optional
agent. These agents cannot be removed (§2.3, AGENTS.md hard rule).

## Optional Agent Selection

Enforce that **at least one** optional productive agent is chosen before setup
is complete (§2.3, §7.2). Present the §7.2 roster; recommend a starter set by
the captured AOS purpose (per the `optional-agents` default in
`/aos-interviews.md`). Build each selected agent via the generic engine. The
remaining agents stay `Available` and can be added later (§9.4).

## Registry and Map Updates

- Update `/configs/agent-registry.md` (§10.3): one row per agent with Status,
  Required?, Agent Folder, Notes. Note the Chief of Staff Agent's ownership of
  the factory-vs-instance guard in `/CLAUDE.md`.
- Update `/aos-map.md` (§10.4): Overview, the Agents table (installed,
  available, paused, retired), and the Folder Map. The installed-vs-available
  distinction feeds the Review Agent's advertising check and the guide's
  Available Agents subsection (regenerable projections, §14.8).
- Update `/aos-manifest.md` Installed / Active / Paused / Retired agent tables
  (§14.3).

## Rhythmic Workflow Scheduling

Follow §9.3 step 10. Offer a Cowork Scheduled Task for **each** of the four
cadence-driven workflows — daily startup, end-of-day shutdown, weekly review,
monthly review (§17.1–17.4) — presenting each with its standard cadence (§25)
and any captured preferred timing (e.g. the Review Agent's `review-timing`
answer, §26). Create a task only for each one the user accepts; declining leaves
that workflow manually triggered. Event-triggered workflows (inbox-to-task,
project kickoff, decision capture, memory review) are **never** scheduled.

Each Scheduled Task's instructions contain **exactly one line** — an `@`-path
reference to the workflow file, resolved against the instance root, e.g.
`@/[aos-name]/workflows/daily-startup-workflow.md`. No other embedded
instructions; the workflow file stays the single source of truth. Creating a
Scheduled Task is Level 2 (§3.4): preview the schedule and gate creation behind
`Proceed`. Log each accepted schedule to `/logs/change-log.md`.

## Validation Checklist

Run the §27 completeness checks before declaring the build complete:

- Required folders, required global files, all five required agents, and at
  least one optional productive agent are present.
- Registry entries, AOS map, permissions, workflows, templates, logs, and the
  AOS User Guide are present.
- Each built agent has its full §5.1 file set (instruction file, memory,
  learnings, primary workflow, output template, config, decision log) plus its
  empty `/outputs/[agent-name]-agent/` folder.
- Catalog / profile / interview validation passes (§7A.5 V1–V8, §7B.5 V9–V13).
- The AOS User Guide passes its §16.6 consistency checks (TOC ↔ anchors,
  Change Log present).
- Have the Review Agent audit completeness/consistency, the Security Agent audit
  permissions and tool access, and the Memory Agent audit memory routing and
  boundaries (§27).

## AOS Setup Summary

Write `/logs/aos-build-summary.md` (file_type `build_summary`, §9.3 step 11)
with an instance-scope schema parallel to the §13 per-agent Build Summary:

```markdown
# [AOS Name] Setup Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Steps
```
