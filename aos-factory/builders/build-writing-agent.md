---
title: Build Writing Agent
file_type: agent_builder
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build Writing Agent

## Builder Purpose

Build the Writing Agent, an optional productive agent that owns long-form content
and drafting: documents, posts, and written deliverables distinct from message
replies (catalog: `writing-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, voice/format preferences,
approval boundaries, collaboration; summarize; recommend defaults; preview; wait
for `Proceed`.

## Discovery Questions

- What kinds of content, and for what audiences?
- What voice, tone, and formatting conventions should drafts follow?
- Should research come from the Research Agent when installed (Section 23)?

## Recommended Defaults

- Brief intake → draft → revision → approval gate before any publish/send.
- Take research input from Research rather than collecting sources itself.
- Hand finished content to the Document Agent for filing.

## Configuration Decisions

- Content types; voice/tone/format; publish-approval rules.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/writing-agent/writing-agent.md
/agents/writing-agent/memory/writing-memory.md
/agents/writing-agent/memory/writing-learnings.md
/agents/writing-agent/workflows/writing-primary-workflow.md
/agents/writing-agent/templates/writing-output-template.md
/agents/writing-agent/configs/writing-config.md
/agents/writing-agent/logs/writing-decision-log.md
```

## Agent Instruction Generation Rules

Render `writing-agent.md` to the Section 11 schema. Project **identity** from the
`writing-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns long-form content and drafting — documents, posts, and
  written deliverables distinct from message replies.
- Responsibilities ← `domains_owned`: `writing`.
- Non-Responsibilities ← derived: does not conduct primary research (research),
  triage/draft message replies (inbox), or file/archive finished documents
  (document).
- Inputs ← `research`; Outputs ← `writing`.
- Collaboration Rules ← `collaborates_with`: receives research from Research; hands
  off finished content to Document; escalates priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (publish or send finished
  content externally); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/writing-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `writing-primary-workflow.md` (Section 16.3): brief intake → drafting →
revision → an approval gate before any publish or send.

## Memory Generation Rules

Seed `writing-memory.md` and `writing-learnings.md` per Section 16.2. Keep
voice/style preferences and reusable patterns current; put global style in
`/memory/preferences.md`.

## Config Generation Rules

Write `writing-config.md` (Section 16.1). `Tool Access` references the matrix:
drafting = Allowed; external publishing = Approval-required (Section 22).

## Logging Rules

Append-only `writing-decision-log.md` (Section 16.5). Log publish approvals and
important assumptions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- No unapproved publish/send path; research and document handoffs wired in.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/writing-agent/logs/writing-build-summary.md` (file_type `build_summary`).
