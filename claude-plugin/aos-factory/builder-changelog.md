---
title: AOS Factory Builder Changelog
file_type: builder_changelog
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
---

# AOS Factory Builder Changelog

This changelog tracks changes to the AOS Factory **framework files and packaging**
— the builders in `/builders/`, the root entry pointer, and the plugin package.
It is distinct from the design `aos-factory-revision-history.md` (the design audit
trail that lives with the spec) and from a generated instance's
`/logs/change-log.md`. All three are numbered by `spec_version`; this file ships
inside the plugin (Section 28) and, when distributed, tracks the plugin version.

Entries are in reverse chronological order (newest first).

| spec_version | Date       | Change |
|--------------|------------|--------|
| 2.0.0        | 2026-07-01 | Initial framework generation. Root entry `/build-aos.md`, master builder `/builders/build-aos.md`, and the 14 agent builders (4 governance + 10 productive) generated from design spec 2.0.0, rendering identity from `agent-catalog.yaml` (§7A) and behavior from `agent-profiles/` (§7B). |

## 2.0.0 — Initial Framework Generation (2026-07-01)

Generated the AOS Factory framework files per the Section 35.2 generation scope,
authorized by `Proceed` under the Section 36.2 workflow:

- Root entry pointer `/build-aos.md` (file_type `builder_entry`).
- Master AOS builder `/builders/build-aos.md` (file_type `aos_builder`, Section 12.1).
- 14 agent builders (file_type `agent_builder`, Section 12), one per agent in the
  Section 7.3 roster: 4 governance (security, memory, chief-of-staff, review) and
  10 productive (tutor, inbox, calendar, task, project-manager, research, writing,
  document, personal-crm, automation).

Each agent builder renders its identity sections (Purpose, Responsibilities,
Non-Responsibilities, Inputs, Outputs, Collaboration, Approval) from the agent's
`agent-catalog.yaml` entry and its narrative sections from the agent's profile,
rather than hand-authoring them (Sections 11, 12, 7A, 7B).

Not included in this phase (per Section 35.2 scope): no user AOS instance was
created, and the rendered factory-root copies of `agent-catalog.yaml` and
`agent-profiles/` are added separately (Sections 7A.4, 7B.2).

## 2.0.0 — Plugin Repackaging: Roster Reconciliation (2026-07-02)

Repackaged the `aos-factory` plugin from the current framework (`spec_version`
2.0.0) under the Section 36.3 workflow, authorized by `Proceed`:

- Regenerated all 15 builder skills (`build-aos` + 14 agents) from
  `/builders/build-*.md` into `skills/build-*/SKILL.md`, body verbatim with
  `name` + invocation-oriented `description` frontmatter.
- Added `build-tutor-agent` skill (new in the current roster).
- Removed three stale skills no longer in the framework roster:
  `build-finance-agent`, `build-health-life-logistics-agent`,
  `build-learning-agent` (approved deletion, Section 33).
- Bumped `plugin.json` version 1.1.0 → 2.0.0 to sync with the framework
  `spec_version`.
- Refreshed `README.md`, `templates/aos-router.md`, and `templates/CLAUDE.md`.
