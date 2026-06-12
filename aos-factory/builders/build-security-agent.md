---
title: Build Security Agent
file_type: agent_builder
spec_version: 1.0.5
created_date: 2026-06-03
last_updated: 2026-06-11
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Security Agent

## Builder Purpose

Build the **Security / Permissions Agent**, a required governance agent. It owns permission rules, approval requirements, access boundaries, the tool access matrix, and safety checks (Section 7.4). This is a required core agent with a mostly standardized purpose, so its interview is short (Section 26).

## When to Use This Builder

Use during initial AOS setup (invoked by `/builders/build-aos.md`) or when restoring or rebuilding the Security Agent. The AOS may not be considered complete without it.

## Builder Operating Mode

Coach + collaborator; default to dry-run / preview; create no files until the user types exactly `Proceed`. Apply the global file-safety rule throughout.

## Interview Flow

Short batch interview (Section 9.1): confirm the standardized responsibilities, ask the few questions below, summarize, recommend defaults, then request `Proceed`.

## Discovery Questions

- Are there any tools, data sources, or actions the user wants prohibited outright from the start?
- Are there actions the user wants to pre-authorize beyond the global defaults (kept minimal)?
- How sensitive is the user about privacy and external communication (affects escalation thresholds)?

## Recommended Defaults

- Adopt the global three-level permission model unchanged (Section 3.4).
- Treat the global tool access matrix as the single source of truth (Section 22).
- Default new tools to `Not configured` until access is explicitly granted.
- Escalate all permission, privacy, and prohibited-action questions to this agent.

## Configuration Decisions

- Confirm that agent configs reference global permissions and the tool access matrix rather than duplicating or overriding them (Sections 3.5, 16.1, 22).
- Decide initial access levels for any tools the user has named.
- Confirm sensitive-memory questions route here in partnership with the Memory Agent.

## Files to Create

```text
/agents/security-agent/security-agent.md
/agents/security-agent/memory/security-memory.md
/agents/security-agent/memory/security-learnings.md
/agents/security-agent/workflows/security-primary-workflow.md
/agents/security-agent/templates/security-output-template.md
/agents/security-agent/configs/security-config.md
/agents/security-agent/logs/security-decision-log.md
```

## Agent Instruction Generation Rules

Generate `security-agent.md` using the Section 11 agent schema with `file_type: agent_instruction` frontmatter (Section 15.2). Emphasize the **Non-Responsibilities** section (this agent governs, it does not do productive domain work). Document its ownership of the tool access matrix, approval gating, and safety audits, and its role as the escalation target for permission, privacy, and prohibited-action questions (Section 24).

## Workflow Generation Rules

Create `security-primary-workflow.md` (Section 16.3) covering how the agent reviews a proposed action, classifies it by permission level, and approves, gates with a `Proceed` request, or refuses. Create agent-specific workflows only when useful.

## Memory Generation Rules

Create `security-memory.md` and `security-learnings.md` (Section 16.2). Store durable security and permission patterns; route sensitive entries through the explicit-approval rule (Section 20.3).

## Config Generation Rules

Create `security-config.md` (Section 16.1). `Inherited Rules` references global permissions; `Tool Access` references the authoritative matrix and lists only agent-specific notes (Sections 3.5, 16.1, 22).

## Logging Rules

Create `security-decision-log.md` (Section 16.5), newest entries on top. Log permission changes, tool-access decisions, and refused/escalated actions (Section 19.3).

## Validation Checklist

```text
[ ] Standard seven-file set created.
[ ] Instruction file follows Section 11 schema with strong Non-Responsibilities.
[ ] Config references global permissions and the tool access matrix (no duplication/override).
[ ] Primary workflow covers classify / approve / gate / refuse.
[ ] Decision log present and append-only.
[ ] Registry and map updated; build logged.
```

## Handoff Summary

Produce a build summary (Section 13): Files Created, Key Decisions, User Preferences Captured, Permissions and Boundaries, Open Questions, Suggested Next Agent (recommend Memory Agent next).
