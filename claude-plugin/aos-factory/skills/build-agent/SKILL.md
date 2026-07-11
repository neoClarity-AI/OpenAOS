---
name: build-agent
description: Build, add, restore, or rebuild any single approved AOS agent inside an existing AOS instance (e.g. 'Build the Research Agent', 'Add the Calendar Agent'). Generic engine covering all 15 approved agents: resolves the agent's catalog entry, profile, and interviews from the plugin's agent-specs, runs its scripted Initialization interview, and creates the standard agent file set. No files are created until the user types exactly Proceed.
---


# Build Agent (Generic Engine)

## Engine Purpose

Build any one approved agent inside an existing AOS instance. This engine replaces the former per-agent builder files: it instantiates a validated agent-catalog entry (§7A) + profile (§7B) + interviews file (§7C) into the standard §5.1 agent file set. It is a builder-framework file, not a runtime agent (§7.5, §8.1).

## When to Use This Engine

- During initial AOS setup, invoked by `/builders/build-aos.md` for each required governance agent and each selected optional agent.
- Later, when the user asks to install an agent, e.g. "Build the Research Agent" (§9.4).
- When restoring or rebuilding an agent's definition files after an authorized factory update (§14.4, `Proceed`-gated for any overwrite).

## Operating Mode

Coach + collaborator (§1.5). Default to dry-run / preview: no file is written until the user types exactly `Proceed` (§3.1, §9.1). Every overwrite of an existing file requires its own explicit listing and approval (§2.5, §3.2). Non-destructive by default (§2.4).

## Inputs

Resolve the target agent from the invocation ("Build the Research Agent" → `research-agent`, per the §7.3 slugs), then load its three design artifacts from the factory root:

1. Its entry in `/agent-catalog.yaml` (§7A) — identity and ownership.
2. `/agent-specs/[agent-name]-agent/profile.md` (§7B) — behavioral narrative.
3. `/agent-specs/[agent-name]-agent/interviews.md` (§7C) — scripted interviews.

Also required: the target AOS instance root (established by build-aos or confirmed with the user), and the instance's `/configs/agent-registry.md` and `/aos-map.md` for the §10.3.1 instance-scope overlap check. If any design artifact is missing, stop and report; do not hand-author a substitute (§1.6.1).

## Interview Execution

Execute the agent's §7C Initialization interview. The script is normative for question content, order, and captured fields; delivery is conversational in the §9.1 batch pattern (ask, summarize, recommend, preview, `Proceed`). Paraphrase is allowed; never add, remove, or reorder questions. Fast path (only when the user explicitly asks to move faster): questions marked `skippable: yes` resolve to their `default:` values; no other question may be dropped (§7C.4).

## Configuration Decisions

Record every captured answer against its `captures:` target. Recommend defaults for anything vague; ask for approval on important design decisions; document assumptions for low-risk details (§1.5). Validate the agent against the instance before building: its `domains_owned` and `artifacts_owned` must not collide with the framework catalog's reserved domains or any agent already registered in this instance (§10.3.1).

## Files to Create

The standard §5.1 set, all paths relative to the instance root:

```text
/agents/[agent-name]-agent/[agent-name]-agent.md
/agents/[agent-name]-agent/memory/[agent-name]-memory.md
/agents/[agent-name]-agent/memory/[agent-name]-learnings.md
/agents/[agent-name]-agent/workflows/[agent-name]-primary-workflow.md
/agents/[agent-name]-agent/templates/[agent-name]-output-template.md
/agents/[agent-name]-agent/configs/[agent-name]-config.md
/agents/[agent-name]-agent/logs/[agent-name]-decision-log.md
/outputs/[agent-name]-agent/          (empty standalone-deliverables folder, §4)
```

Plus agent-specific supporting files only when useful to the agent's domain (§26). Present the full list in the §9.1 pre-build preview (Files to Create / Decisions Applied / Assumptions / Approval) and wait for `Proceed`.

## Agent Instruction Generation Rules

Generate `[agent-name]-agent.md` per the §11 schema with §15.2 frontmatter (`file_type: agent_instruction`, `agent_name`, `agent_status: active`, `required`, `aos_version`, `spec_version`, dates).

- Render `Purpose`, `Responsibilities`, `Non-Responsibilities`, `Inputs`, `Outputs`, `Collaboration Rules`, `Approval Requirements` from the catalog entry (`one_line`, `domains_owned`, derived `non_responsibilities`, `inputs`, `outputs`, `collaborates_with`, `approval_required_actions` + `pre_authorized_actions`). Never hand-author identity.
- Render `Workflows`, `Autonomy Rules`, `Escalation Rules`, `Operating Procedure`, `Quality Standards`, `Failure Modes`, `Example Requests`, `Maintenance Notes` from the profile's Operation section, tailored with the instance choices captured by the Initialization interview.
- Use direct imperative language and must/should/may consistently; include examples (§32).

## Workflow Generation Rules

Generate `[agent-name]-primary-workflow.md` per the §16.3 workflow schema (Purpose, When to Use, Inputs, Outputs, Steps, Decision Points, Approval Gates, Escalation Triggers, Completion Criteria), derived from the profile's Primary Workflow narrative and interview answers. Frontmatter per §15.3 (`file_type: workflow`, `owner: [agent-name]-agent`).

## Memory Generation Rules

Generate `[agent-name]-memory.md` and `[agent-name]-learnings.md` per the §16.2 memory schema, created once and seeded empty (data files, §14.8 — never overwritten by a later update). Learnings entries follow the §6.1 entry format and attribution rule. Add or update the agent's row in `/memory/agent-learnings-index.md`.

## Config Generation Rules

Generate `[agent-name]-config.md` per the §16.1 config schema. `Inherited Rules` references `/configs/global-permissions.md`; `Tool Access` references `/configs/tool-access-matrix.md` and lists only agent-specific notes or requests — never restating or overriding global permissions or matrix grants (§3.5, §16.1, §22). If the catalog entry has `pre_authorized_actions`, add a one-line cross-reference to the catalog entry rather than restating them.

## Logging Rules

Create `[agent-name]-decision-log.md` per the §16.5 append-only decision-log schema (newest on top; no deletions; corrections as new entries). Log the build itself to `/logs/change-log.md` (Type: MINOR — an agent built, §14.3.1/§16.8) and record must-log events per §19.3.

## Validation Checklist

Before declaring the build complete (§27):

```text
[ ] All seven §5.1 files exist with correct §15 frontmatter (spec_version + aos_version stamps).
[ ] /outputs/[agent-name]-agent/ exists.
[ ] Instruction-file identity sections match the catalog entry; narrative sections trace to the profile.
[ ] §10.3.1 overlap check passed (domains and artifacts pairwise disjoint at both scopes).
[ ] /configs/agent-registry.md and /aos-map.md updated (status Active).
[ ] /memory/agent-learnings-index.md row added.
[ ] Build logged to /logs/change-log.md.
[ ] Config references global permissions and the tool access matrix instead of duplicating them.
```

## Handoff Summary

Emit the §13 Build Summary and save it to `/agents/[agent-name]-agent/logs/[agent-name]-build-summary.md` (`file_type: build_summary`):

```markdown
# [Agent Name] Build Summary

## Files Created
## Key Decisions
## User Preferences Captured
## Permissions and Boundaries
## Open Questions
## Suggested Next Agent
```
