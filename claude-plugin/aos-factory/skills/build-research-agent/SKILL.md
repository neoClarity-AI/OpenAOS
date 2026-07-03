---
name: build-research-agent
description: "Build the Research Agent, an optional productive AOS agent that owns research: gathering, synthesizing, and sourcing information in support of projects, decisions, and learning. Use when selected during AOS setup or later via 'Build the Research Agent'."
---

# Build Research Agent

## Builder Purpose

Build the Research Agent, an optional productive agent that owns research:
gathering, synthesizing, and sourcing information in support of projects,
decisions, and learning (catalog: `research-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when selected, or directly to add it later
(Section 9.4). Specialized worker, not a coordinator (Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): goals, scope, tools, output preferences, approval
boundaries, collaboration; summarize; recommend defaults; preview; wait for
`Proceed`.

## Discovery Questions

- What research topics/domains, and what output format (brief, comparison,
  synthesis)?
- Should web search be requested in the matrix (Section 22)?
- How should sources and confidence be reported?

## Recommended Defaults

- Scope → gather/evaluate sources → synthesized output with citations and
  confidence notes.
- Store durable findings in agent memory; route large source documents to
  `/projects` or a project's `/assets`, not memory (Section 20.3).
- Hand finished material to Writing (content) or Tutor (learning module),
  Section 23.

## Configuration Decisions

- Research domains; tool access requests; output/citation format.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/research-agent/research-agent.md
/agents/research-agent/memory/research-memory.md
/agents/research-agent/memory/research-learnings.md
/agents/research-agent/workflows/research-primary-workflow.md
/agents/research-agent/templates/research-output-template.md
/agents/research-agent/configs/research-config.md
/agents/research-agent/logs/research-decision-log.md
```

## Agent Instruction Generation Rules

Render `research-agent.md` to the Section 11 schema. Project **identity** from the
`research-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns research — gathering, synthesizing, and sourcing
  information for projects, decisions, and learning.
- Responsibilities ← `domains_owned`: `research`.
- Non-Responsibilities ← derived: does not coordinate/own projects
  (project-manager) or produce finished written content (writing).
- Inputs ← `project-coordination`; Outputs ← `research`.
- Collaboration Rules ← `collaborates_with`: receives requests from Project
  Manager; hands off to Writing (drafting) and Tutor (learning module); escalates
  priority conflicts to Chief of Staff.
- Approval Requirements ← `approval_required_actions` (cite or rely on a source
  requiring access approval); no pre-authorized exceptions.

Project **narrative** sections from `agent-profiles/research-agent.md` (§7B).
Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `research-primary-workflow.md` (Section 16.3): scope a question → gather and
evaluate sources → produce a synthesized output.

## Memory Generation Rules

Seed `research-memory.md` and `research-learnings.md` per Section 16.2. Keep
durable findings and reliable sources with confidence; keep large documents out of
memory (Section 20.3).

## Config Generation Rules

Write `research-config.md` (Section 16.1). `Tool Access` references the matrix:
web search = Allowed for research tasks (Section 22).

## Logging Rules

Append-only `research-decision-log.md` (Section 16.5). Log source-access decisions
and important assumptions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Handoffs to Writing / Tutor wired in; large-document routing correct.
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/research-agent/logs/research-build-summary.md` (file_type
`build_summary`).
