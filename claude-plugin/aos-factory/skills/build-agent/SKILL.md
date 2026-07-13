---
name: build-agent
description: Build any one AOS agent (required or optional) into an existing AOS instance from its catalog entry, profile, and interview script — creating the standard per-agent file set. The generic engine; one skill covers every agent. Use when adding, rebuilding, or restoring a single agent, e.g. "Build the Research Agent". Nothing is written until the user types exactly `Proceed`.
---
# Build Agent (Generic Engine)

One generic engine that builds **any** one approved agent into an AOS instance
from that agent's design artifacts (design spec §8.1, §12). It replaces the
former per-agent `build-[agent-name]-agent.md` files; there is one engine, not
one builder per agent.

## Engine Purpose

Instantiate a single validated agent — its catalog entry (§7A), profile (§7B),
and interviews file (§7C) — into the standard §5.1 file set inside the target
AOS instance, capturing instance-specific choices through the agent's scripted
Initialization interview. This makes the roster extensible: adding an agent
needs one `agent-specs/` folder plus a catalog entry (§7.5 Phase A), never a new
builder file.

## When to Use This Engine

- During initial setup, invoked by `/builders/build-aos.md` once per required
  agent and once per selected optional agent.
- Later, to add one optional agent to an existing instance, e.g. "Build the
  Research Agent" → resolves to `research-agent` (§9.4).
- To rebuild or restore an agent under the lifecycle rules (§10.2), which remain
  `Proceed`-gated.

## Operating Mode

- Coach + collaborator (§1.5); default to dry-run / preview.
- Gate all file creation behind the user typing exactly `Proceed` (§3.1);
  approval is action-specific (§2.5).
- Never overwrite, delete, move, or rename without a separate `Proceed` (§3.1).
  Refreshing an existing agent's definition files is Level 2 (§14.7).

## Inputs

The target agent's design artifacts, resolved from the invocation (e.g. "Build
the Research Agent" → `research-agent`):

```text
/agent-catalog.yaml → the agent's entry (identity/ownership, §7A)
/agent-specs/[agent-name]-agent/profile.md    (behavior narrative, §7B)
/agent-specs/[agent-name]-agent/interviews.md (scripted interviews, §7C)
```

Also required: the target AOS instance root (established by
`/builders/build-aos.md`), against which all instance paths resolve (§4.1).

## Interview Execution

Execute the agent's §7C **Initialization** interview from its `interviews.md`.
The script is normative for question content, order, and captured fields;
delivery stays conversational in the §9.1 batch pattern (ask, summarize,
recommend, preview, `Proceed`). Fast path (§7C.4): questions marked
`skippable: yes` resolve to their `default:` values; no other question may be
dropped, added, or reordered. Required agents have shorter scripts; optional
productive agents ask about goals, scope, tools, output preferences, approval
boundaries, and collaboration patterns (§26).

## Configuration Decisions

Record the instance-specific choices captured by the interview (scope, tools,
output preferences, approval boundaries, collaboration patterns). These tailor
the projected narrative sections of the instruction file and the agent config.
Log important decisions and assumptions per §19.3.

## Files to Create

Create the standard §5.1 file set for the agent, stamping each with
`spec_version` and the instance `aos_version` (§15.2–15.3):

```text
/agents/[agent-name]-agent/[agent-name]-agent.md
/agents/[agent-name]-agent/memory/[agent-name]-memory.md
/agents/[agent-name]-agent/memory/[agent-name]-learnings.md
/agents/[agent-name]-agent/workflows/[agent-name]-primary-workflow.md
/agents/[agent-name]-agent/templates/[agent-name]-output-template.md
/agents/[agent-name]-agent/configs/[agent-name]-config.md
/agents/[agent-name]-agent/logs/[agent-name]-decision-log.md
/outputs/[agent-name]-agent/            (empty standalone-deliverables folder, §4)
```

Add agent-specific supporting workflows or templates only when useful to that
agent's domain (§26). Rendered outputs from the output template land in
`/outputs/[agent-name]-agent/` by default; project-bound deliverables go in the
project folder instead (§4, §21).

## Agent Instruction Generation Rules

Generate `[agent-name]-agent.md` per the §11 schema as a **projection**, not
hand-authored prose:

- From the **catalog entry** (§7A): `Purpose` (from `one_line`, expanded),
  `Responsibilities` (`domains_owned`), `Non-Responsibilities` (derived
  `non_responsibilities` — the SRP enforcer), `Inputs`, `Outputs`,
  `Collaboration Rules` (`collaborates_with` edges), and `Approval Requirements`
  (`approval_required_actions` + `pre_authorized_actions`).
- From the **profile** Operation section (§7B): `Workflows`, `Autonomy Rules`,
  `Escalation Rules`, `Operating Procedure`, `Quality Standards`,
  `Failure Modes`, `Example Requests`, `Maintenance Notes` — tailored with the
  instance choices captured above.

The engine does not duplicate catalog- or profile-owned content as new prose.
The `Non-Responsibilities` section is required (§11).

## Workflow Generation Rules

Create `[agent-name]-primary-workflow.md` using the §16.3 workflow schema
(Purpose, When to Use, Inputs, Outputs, Steps, Decision Points, Approval Gates,
Escalation Triggers, Completion Criteria), derived from the profile's Primary
Workflow. Add domain-specific workflows only when useful (§26).

## Memory Generation Rules

Create `[agent-name]-memory.md` and `[agent-name]-learnings.md` using the §16.2
memory schema and §6.1 learnings format. Register the agent in
`/memory/agent-learnings-index.md` (§6.1). Seed empty; never fabricate entries.
Apply memory governance (§20.3): memory-worthy only if durable, useful, and
relevant.

## Config Generation Rules

Create `[agent-name]-config.md` using the §16.1 config schema. `Inherited Rules`
references `/configs/global-permissions.md` rather than duplicating it (§3.5).
`Tool Access` references the global tool access matrix
(`/configs/tool-access-matrix.md`), which is authoritative, and lists only
agent-specific notes or requests (§22). For an agent with
`pre_authorized_actions`, add a one-line cross-reference to its catalog entry
rather than restating them (§16.1). Include only additional permissions,
agent-specific restrictions, explicit overrides, tool/memory boundaries, and
unique escalation triggers (§3.5).

## Logging Rules

Create `[agent-name]-decision-log.md` using the §16.5 append-only decision-log
schema (newest on top; corrections added as new entries; no silent rewrites).
Log the must-log categories (§19.3): important preferences, configuration and
permission decisions, files created, approved modifications, workflow changes,
assumptions, escalations, errors, handoffs, and retirement/restoration.

## Validation Checklist

Confirm before completing (§27):

- The full §5.1 file set exists, plus the empty `/outputs/[agent-name]-agent/`
  folder.
- Frontmatter is present and stamped (`spec_version`, `aos_version`, file_type,
  status; §15).
- Instruction-file identity sections match the catalog entry; narrative sections
  trace to the profile; no restatement drift (§7B.4, §11).
- Catalog / profile / interview validation passes for this agent (§7A.5 V1–V8,
  §7B.5 V9–V13).
- Config references (not restates) global permissions and the tool matrix (§3.5,
  §22).
- The registry (`/configs/agent-registry.md`), map (`/aos-map.md`), and manifest
  (`/aos-manifest.md`) are updated with the agent's status.

## Handoff Summary

Emit the canonical end-of-build **Build Summary** (§13), saved to the built
agent's own logs folder as
`/agents/[agent-name]-agent/logs/[agent-name]-build-summary.md`
(file_type `build_summary`, §15.4):

```markdown
# [Agent Name] Build Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Agent
```
