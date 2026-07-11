---
name: build-agent
description: Build any one approved agent inside an existing AOS instance — execute that agent's initialization interview and instantiate its catalog entry, profile, and interviews into the standard agent file set. The generic build engine used both during initial AOS setup and to add an optional agent later. Use when the user says things like "build the Research Agent", "add a Calendar agent", "create the Inbox agent", or otherwise asks to add or rebuild a single agent in an AOS instance. To stand up a whole new AOS instance instead, use the build-aos skill.
spec_version: 2.2.2
---
# Build Agent (Generic Engine)

## Engine Purpose

Build any one approved agent inside an AOS instance by executing that agent's
Initialization interview and instantiating its validated catalog entry (§7A),
profile (§7B), and interviews file (§7C) into the standard §5.1 file set. One
generic engine provides build coverage for every approved agent (§8.1); there are
no per-agent builder files. It is a builder-framework file, not a runtime agent
(§7.5, §8.1).

> Packaged as a Claude plugin skill. The design artifacts referenced below
> (`agent-catalog.yaml`, `agent-specs/`) ship with the factory framework;
> resolve them from the installed factory / plugin context.

## When to Use This Engine

Use during initial setup (driven by the `build-aos` skill) to build required
and selected optional agents, and later to add an optional agent to an existing
instance (§9.4) — e.g. "Build the Research Agent" resolves to `research-agent`.

## Operating Mode

Default to dry-run / preview and gate file creation behind the user typing
exactly `Proceed` (§3.1, §9.1). Creating the new agent's files and folders is
Level 1 safe-autonomous (§3.3) but is previewed in the build plan first. Never
overwrite, move, or delete an existing file without a separate `Proceed` (§2.4,
§3.2). Refuse to build an agent whose design artifacts fail the §7A.5/§10.3.1
overlap and validation checks (Phase A must pass before Phase B, §7.5).

## Inputs

Resolve the target agent from the invocation (e.g. "Build the Research Agent" →
`research-agent`), then read all three design artifacts:

```text
- the agent's catalog entry in agent-catalog.yaml (§7A) — identity/ownership
- agent-specs/[agent-name]-agent/profile.md (§7B) — behavior narrative
- agent-specs/[agent-name]-agent/interviews.md (§7C) — scripted interviews
```

Validate before building: the slug matches §7.3; `domains_owned` and
`artifacts_owned` are pairwise-disjoint against the catalog and against every
agent already in this instance registry (§7A.5, §10.3.1); no reserved governance
token is claimed by a productive agent.

## Interview Execution

Execute the agent's §7C Initialization interview. The script is normative for
question content, order, and captured fields; delivery is conversational per the
§9.1 batch pattern (paraphrase allowed; never add, remove, or reorder questions).
Fast path (§7C.4): questions marked `skippable: yes` resolve to their `default:`
values; no other question may be dropped. Required agents have shorter scripts;
optional productive agents ask about goals, scope, tools, output preferences,
approval boundaries, and collaboration patterns (§26).

## Configuration Decisions

Map each captured answer to the file/field named in its `captures:` entry.
Recommend defaults for anything left vague (§1.5); record low-risk assumptions in
the pre-build preview's `## Assumptions` block. Tool requests are recorded as
requests against `/configs/tool-access-matrix.md` and granted only by the
Security Agent (§22) — never self-granted here.

## Files to Create

Create the standard §5.1 agent file set plus the empty outputs subfolder (§4):

```text
/agents/[agent-name]-agent/[agent-name]-agent.md
/agents/[agent-name]-agent/memory/[agent-name]-memory.md
/agents/[agent-name]-agent/memory/[agent-name]-learnings.md
/agents/[agent-name]-agent/workflows/[agent-name]-primary-workflow.md
/agents/[agent-name]-agent/templates/[agent-name]-output-template.md
/agents/[agent-name]-agent/configs/[agent-name]-config.md
/agents/[agent-name]-agent/logs/[agent-name]-decision-log.md
/outputs/[agent-name]-agent/                    (empty; standalone deliverables, §4)
```

Stamp every generated file's frontmatter with `spec_version` and `aos_version`
(§15). Builders may add agent-specific supporting files as needed (§5.1).

## Agent Instruction Generation Rules

Render `[agent-name]-agent.md` to the §11 schema. Draw the **identity** sections
— Purpose (from `one_line`), Responsibilities (`domains_owned`), Non-Responsibilities
(derived `non_responsibilities` — the SRP enforcer), Inputs, Outputs, Collaboration
Rules (`collaborates_with`), and Approval Requirements (`approval_required_actions`
+ `pre_authorized_actions`) — from the catalog entry (§7A/§7B.4). Draw the
**narrative** sections — Workflows, Autonomy Rules, Escalation Rules, Operating
Procedure, Quality Standards, Failure Modes, Example Requests, Maintenance Notes —
from the agent's profile Operation section (§7B), tailored with the instance
choices captured in the interview. Do not duplicate catalog- or profile-owned
content as hand-authored prose.

## Workflow Generation Rules

Create `[agent-name]-primary-workflow.md` to the §16.3 schema, based on the
profile's Primary Workflow. Add agent-specific workflows only where the profile or
captured configuration calls for one.

## Memory Generation Rules

Create `[agent-name]-memory.md` and `[agent-name]-learnings.md` to the §16.2 /
§6.1 schemas, seeded empty (or with only user-provided seeds — never fabricated).
Register the learnings file in `/memory/agent-learnings-index.md`. Memory and
learnings are data files, owned by the agent thereafter (§14.8).

## Config Generation Rules

Create `[agent-name]-config.md` to the §16.1 schema. `Inherited Rules` references
`/configs/global-permissions.md` rather than duplicating it; `Tool Access`
references `/configs/tool-access-matrix.md` as authoritative and lists only
agent-specific notes (§16.1, §22). For an agent with `pre_authorized_actions`, add
a one-line cross-reference to its catalog entry rather than restating them.

## Logging Rules

Create `[agent-name]-decision-log.md` to the §16.5 append-only schema (newest on
top; corrections added as new entries, never rewritten).

## Validation Checklist

Confirm: all §5.1 files created and frontmatter-stamped; the instruction file
matches §11 with identity from the catalog and narrative from the profile;
non-responsibilities present (SRP); learnings file registered in the index; config
references global permissions and the tool matrix without restating them; the
outputs subfolder created; registry, map, and manifest updated for this agent;
the §10.3.1 overlap check passed. Correct any gap before finishing.

## Handoff Summary

Emit the §13 Build Summary as `/agents/[agent-name]-agent/logs/[agent-name]-build-summary.md`
(file_type `build_summary`):

```markdown
# [Agent Name] Build Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Agent
```
