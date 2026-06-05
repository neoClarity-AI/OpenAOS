---
title: AOS Change Summary — Instance Routing
file_type: change_summary
schema_version: 1.0.0
builder_version: 1.0.0
created_date: 2026-06-05
last_updated: 2026-06-05
status: builder_pass_complete
purpose: Starting point for a new conversation to fold these changes into the builder files.
---

# AOS Change Summary — Instance Routing

## Context / motivation
AOS-03 holds two parallel instances (`work-aos`, `personal-aos`) that share one
Gmail inbox (martin@neoclarity.ai), plus the **factory framework**
(`aos-factory/`) that builds and maintains those instances. A daily-brief
request surfaced that nothing designated an active instance, so routing was
ambiguous and an agent could silently pick or blend the two. These changes add
an explicit, model-robust routing layer (ask-don't-guess) so the arrangement
holds up even on a lighter model such as Sonnet 4.6. Default instance is
**work-aos**. A later pass extended the router to treat `aos-factory` as a
first-class routing target distinct from the instances.

## Files created

### 1. `/claude.md` (project root) — NEW
Root project instruction file; now serves as the session-start instruction file
(it replaces `nc-common-instructions.md`, so the router is wired into the
session-start chain here — no external edit needed). Contains AOS frontmatter
(`file_type: project_instructions`) plus two sections:
- **Planning mode** — on "Planning mode"/"pmode", make no file changes until the
  user says "Proceed"; display proposed changes and ask first.
- **Instance routing** — "read `/aos-router.md` and resolve the active instance
  before running any workflow."
(Note: a `clod.md` was created earlier in the session and then deleted; net new
file is `claude.md` only.)

### 2. `/aos-router.md` (project root) — NEW
New file type `aos_router`. Top-level router read before any target loads.
`applies_to` covers `aos-factory`, `work-aos`, `personal-aos`. Sections:
- **§1 Resolution order:** explicit user override → **framework vs. instance**
  (build/install/framework-edit requests route to `aos-factory` and skip
  instance resolution) → session pin → signal match → fallback ASK (never
  silently pick or merge instances).
- **§2 Classification signals:** factory/framework signals (build/install,
  edits under `aos-factory/` or `/builders/`, `build-*.md` references); default
  = `work-aos`; work vs. personal signal lists; note that the shared inbox is
  not itself a routing signal.
- **§3 Confidence bar:** auto-route only on clear one-sided signals; factory vs.
  instance is usually unambiguous but ambiguous cases (e.g. "add a finance
  agent") fall through to ASK; cross-instance requests run each instance
  separately and stay labeled.
- **§4 Session pin:** set/clear an active target for the session (including
  "work in the factory"); state the active target on the first line of routed
  output.
- **§5 Logging:** instance routing → active instance's
  `agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md`; factory
  routing → `aos-factory/logs/factory-routing-decision-log.md`.

### 3. `aos-factory/logs/factory-routing-decision-log.md` — NEW
Decision-log home for routing choices that resolve to `aos-factory` (the
factory has no Chief of Staff). Frontmatter `file_type: decision_log`; holds an
append-only table (date, request, trigger, notes).

## Files edited

### 4. `personal-aos/aos-manifest.md` and `work-aos/aos-manifest.md`
Added a pointer blockquote directly under `# AOS Manifest`:
> Instance selection is governed by `/aos-router.md`. Do not assume this
> instance is active.

## Builder pass — done 2026-06-05 (factory + spec only)
Scope this pass: factory builders and the design spec (source of truth). The
two already-built instances were intentionally left for a later sync.
- **Schema registration — DONE.** Added `aos_router` and `project_instructions`
  to the controlled `file_type` vocabulary in design spec §15.4, with
  file-type-by-file assignments (`/aos-router.md`, `/claude.md`) and an
  explanatory note that both live at the AOS-03 root, above instances/factory.
- **Chief of Staff ownership — DONE.** Router joint-ownership now reflected in
  design spec §7.4 (responsibilities), §10.3 (agent-registry table row + note),
  and `builders/build-chief-of-staff-agent.md` (purpose, instruction-generation
  rules, logging rules, validation checklist).
- **Daily startup workflow — DONE (spec).** Design spec §17.1 now mandates an
  instance-resolution-via-router step ahead of input gathering, with the active
  target stated on the brief's first line. Generated workflows will include it.
- **Differentiated content — DONE (builder).** `builders/build-aos.md` now adds
  a discovery question for instance-distinguishing routing signals and an
  "Instance Routing Signals" section directing the build to populate aliases,
  sender domains, and project lists in memory.

## Instance-sync pass — done 2026-06-05
- **Daily-startup workflows — DONE.** Both `work-aos/` and `personal-aos/`
  `daily-startup-workflow.md` now open with a router-resolution step and an
  instance-labeled first line; later steps renumbered.
- **Chief of Staff ownership — DONE.** Both instances' `chief-of-staff-agent.md`
  gained a router joint-ownership responsibility, and each
  `configs/agent-registry.md` Chief of Staff row now notes ownership of
  `/aos-router.md`.
- **Routing signals — DONE.** Each instance's `/memory/user-profile.md` now
  carries a "Routing signals" section mirroring the router's agreed signals
  (work topics/aliases; personal senders/aliases). Specific work domains/aliases
  remain marked for enumeration as they surface.

## Still open
- Enumerate the concrete work-tied sender domains/aliases in
  `work-aos/memory/user-profile.md` (left as placeholders, pending real values).

## Decisions made by the user this session
- Default instance set to **work-aos**.
- Safety posture: ASK on weak/mixed signals rather than auto-select.
- Planning-mode rule added to root instructions.
- `aos-factory` added as a distinct routing target; framework/build requests
  route to it ahead of instance signal-matching.
- Factory routing decisions logged to a new `aos-factory/logs/` file (rather
  than skipped or folded into the design changelog).
