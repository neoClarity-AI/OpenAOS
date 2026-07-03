---
name: build-security-agent
description: "Build the Security Agent, the required governance agent that owns permission rules, approval requirements, access boundaries, the tool access matrix, and safety checks. Use when standing up an AOS or later via 'Build the Security Agent'."
---

# Build Security Agent

## Builder Purpose

Build the Security Agent, the required governance agent that owns permission
rules, approval requirements, access boundaries, the tool access matrix, and
safety checks (catalog: `security-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` while building the required governance layer
(built before any productive agent, Section 1.6.2), or directly to (re)build the
Security Agent in an existing instance. Refreshing an existing agent requires a
separate `Proceed` (Section 3.2).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until the user types `Proceed` (Section 3.1). Required-agent interview is short
because the role is standardized (Section 26).

## Interview Flow

Batch pattern (Section 9.1). Keep it brief: confirm the instance's privacy
sensitivity and any tools already known, preview the file set, then wait for
`Proceed`.

## Discovery Questions

- How privacy-sensitive is this AOS? (scales escalation thresholds)
- Which tools/integrations are already in use, and at what access level?
- Any actions that must always require approval beyond the Section 3 defaults?

## Recommended Defaults

- Adopt the Section 3 three-level permission model unchanged as the baseline.
- Seed `/configs/tool-access-matrix.md` with every known tool defaulted to
  `Not configured` until access is explicitly granted (Section 22).
- Sensitive-memory approvals handled jointly with the Memory Agent (Section 20.3).

## Configuration Decisions

- Default privacy sensitivity (standard vs. high).
- Initial tool-access rows and their levels (Allowed / Read-only /
  Approval-required / Prohibited / Not configured).

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/security-agent/security-agent.md
/agents/security-agent/memory/security-memory.md
/agents/security-agent/memory/security-learnings.md
/agents/security-agent/workflows/security-primary-workflow.md
/agents/security-agent/templates/security-output-template.md
/agents/security-agent/configs/security-config.md
/agents/security-agent/logs/security-decision-log.md
```

The Security Agent also owns `/configs/tool-access-matrix.md`, created by
`build-aos.md` and maintained by this agent (Section 22).

## Agent Instruction Generation Rules

Render `security-agent.md` to the Section 11 schema. Project the **identity**
sections from the `security-agent` entry in `agent-catalog.yaml` (§7A) — do not
hand-author them:

- Purpose ← `one_line`: owns permission rules, approval requirements, access
  boundaries, the tool access matrix, and safety checks; escalation target for all
  permission, access, and privacy questions.
- Responsibilities ← `domains_owned`: `security.permissions`.
- Non-Responsibilities ← derived: does not orchestrate/route (chief-of-staff), own
  memory governance (memory), or run retrospectives (review).
- Inputs ← none; Outputs ← `security.permissions`.
- Collaboration Rules ← `collaborates_with`: receives matrix-change
  recommendations from Chief of Staff and Review (Section 22); is the escalation
  target for all other agents on permission/access/privacy conflicts (Section 24).
- Approval Requirements ← `approval_required_actions` (grant/change/revoke any
  tool-access entry) + `pre_authorized_actions` (read-only audits of permissions
  and tool access).

Project the **narrative** sections (Workflows, Autonomy Rules, Escalation Rules,
Operating Procedure, Quality Standards, Failure Modes, Example Requests,
Maintenance Notes) from `agent-profiles/security-agent.md` (§7B), tailored with
instance choices. Use direct imperative language and include examples (Section 32).

## Workflow Generation Rules

Create `security-primary-workflow.md` (Section 16.3): review a proposed action →
classify by the three-level model (Section 3.4) → approve (Level 1) / gate with a
`Proceed` request (Level 2) / refuse (Level 3). Add domain workflows only when
useful (Section 26).

## Memory Generation Rules

Seed `security-memory.md` and `security-learnings.md` per Section 16.2, empty of
fabricated content. Record permission decisions and effective safety patterns;
route sensitive items through approval (Section 20.3).

## Config Generation Rules

Write `security-config.md` (Section 16.1). `Inherited Rules` references
`/configs/global-permissions.md` rather than duplicating it; `Tool Access`
references `/configs/tool-access-matrix.md` as authoritative and lists only
agent-specific notes (Sections 3.5, 22).

## Logging Rules

Append-only `security-decision-log.md` (Section 16.5), newest on top. Log
permission changes, refusals, escalations, and matrix edits (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped `spec_version: 2.0.0` +
  `aos_version`.
- Identity rendered from the catalog entry; narrative from the profile; nothing
  restated by hand.
- Tool access matrix present and authoritative; no tool left usable while
  `Not configured`.
- Catalog validation V1–V8 passes for this entry (Section 7A.5).

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/security-agent/logs/security-build-summary.md` (file_type
`build_summary`): files created, key decisions, preferences captured, permissions
and boundaries, open questions, and suggested next agent (typically Memory Agent).
