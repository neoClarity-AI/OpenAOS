---
name: build-tutor-agent
description: "Build the Tutor Agent, an optional productive AOS agent that owns learning: structuring material into lessons, tracking progress, and supporting study or skill-building goals. Use when selected during AOS setup or later via 'Build the Tutor Agent'."
---

# Build Tutor Agent

## Builder Purpose

Build the Tutor Agent, an optional productive agent that owns learning:
structuring material into lessons, tracking progress, and supporting study or
skill-building goals (catalog: `tutor-agent`).

## When to Use This Builder

Invoked by `/builders/build-aos.md` when the user selects this agent, or directly
to add it later (Section 9.4). It is a specialized worker, not a coordinator
(Section 7.6).

## Builder Operating Mode

Coach + collaborator (Section 1.5); dry-run / preview by default; create nothing
until `Proceed`. Fuller optional-agent interview (Section 26).

## Interview Flow

Batch pattern (Section 9.1): ask about goals, scope, tools, output preferences,
approval boundaries, and collaboration; summarize; recommend defaults; preview the
file set; wait for `Proceed`.

## Discovery Questions

- What does the user want to learn, and at what level?
- Preferred learning style and format (explanations, practice, worked examples)?
- Should the agent use web search (if granted in the matrix), or only provided
  materials?
- How should progress be tracked and surfaced?

## Recommended Defaults

- Produce a study plan → lessons/practice → review checkpoints.
- Work from provided materials unless web search is granted (Section 22).
- Hand research-heavy requests to the Research Agent when installed (Section 23).

## Configuration Decisions

- Subjects/goals in scope; learning style; tool access requests; progress-tracking
  cadence.

## Files to Create

Standard agent file set (Section 5.1):

```text
/agents/tutor-agent/tutor-agent.md
/agents/tutor-agent/memory/tutor-memory.md
/agents/tutor-agent/memory/tutor-learnings.md
/agents/tutor-agent/workflows/tutor-primary-workflow.md
/agents/tutor-agent/templates/tutor-output-template.md
/agents/tutor-agent/configs/tutor-config.md
/agents/tutor-agent/logs/tutor-decision-log.md
```

## Agent Instruction Generation Rules

Render `tutor-agent.md` to the Section 11 schema. Project **identity** from the
`tutor-agent` catalog entry (§7A):

- Purpose ← `one_line`: owns learning — structuring material into lessons,
  tracking progress, and supporting study/skill-building.
- Responsibilities ← `domains_owned`: `learning`.
- Non-Responsibilities ← derived: does not conduct primary research (research).
- Inputs ← `research`; Outputs ← `learning`.
- Collaboration Rules ← `collaborates_with`: receives restructured research from
  Research; escalates priority conflicts to Chief of Staff.
- Approval Requirements ← none beyond globals; tool use follows the matrix.

Project **narrative** sections from `agent-profiles/tutor-agent.md` (§7B), tailored
with instance choices. Imperative language; include examples (Section 32).

## Workflow Generation Rules

Create `tutor-primary-workflow.md` (Section 16.3): learning goal → study plan →
lessons/practice → review checkpoints. Add domain workflows only when useful.

## Memory Generation Rules

Seed `tutor-memory.md` and `tutor-learnings.md` per Section 16.2. Track learning
goals, progress, and effective approaches.

## Config Generation Rules

Write `tutor-config.md` (Section 16.1). `Inherited Rules` references global
permissions; `Tool Access` references the matrix and lists only agent-specific
requests (e.g. web search).

## Logging Rules

Append-only `tutor-decision-log.md` (Section 16.5). Log configuration decisions and
important assumptions (Section 19.3).

## Validation Checklist

- Full Section 5.1 file set present; frontmatter stamped.
- Identity from catalog, narrative from profile.
- Research handoff wired in (Section 23).
- Catalog validation V1–V8 and profile validation V9–V10 pass for this entry.

## Handoff Summary

Emit the Section 13 Build Summary to
`/agents/tutor-agent/logs/tutor-build-summary.md` (file_type `build_summary`).
