---
title: AOS Factory Builder Changelog
file_type: builder_changelog
spec_version: 2.2.2
created_date: 2026-07-06
last_updated: 2026-07-11
status: active
---
# AOS Factory Builder Changelog

Tracks changes to the reusable builder framework files and their packaging (§14.5,
§16.9). Numbered by `spec_version` but distinct from the design
`aos-factory-revision-history.md`: that file is the **design** audit trail and
lives with the spec; this changelog tracks **framework-file and packaging**
changes and ships inside the plugin (§28). When the framework is distributed as a
Claude plugin, entries note the plugin version.

Entries are in reverse chronological order (newest first).

| spec_version | Date       | Plugin version | Summary |
|--------------|------------|----------------|---------|
| 2.2.2        | 2026-07-11 | 2.2.2 (packaged, not published) | Re-render of the full framework from `spec_version` 2.2.2 (runbook §36.2) after deletion of the prior framework. Carries in the 2.1.4–2.2.1 design changes already reflected in the rendered artifacts and `/builders/build-aos.md` (purpose-category agent bundles, quarterly-review retirement, Rhythmic Workflow Scheduling with single `@`-path task instructions); 2.2.2 itself is a version reconciliation only — authored files restamped, no content changes |
| 2.1.1        | 2026-07-09 | not published  | Re-render of the full framework from `spec_version` 2.1.1 (§4.1 `/outputs` subtree fix, §16.6 spec_version-stamp fix carried in from the design spec) — no structural changes to the builder files themselves, all frontmatter restamped |
| 2.1.0        | 2026-07-06 | not published  | Initial framework generation: root entry, generic build engine + master AOS builder, and rendered design artifacts (catalog, agent-specs, aos-interviews) |

## 2.2.2 — Full re-render at version reconciliation (2026-07-11)

Full re-render of the AOS Factory framework files from `spec_version` 2.2.2
(runbook §36.2), following deletion of the prior framework files. Between the
last generation (2.1.1) and this one, the design advanced through 2.1.4–2.2.1
(purpose-category default agent bundles in `aos-interviews.md`; retirement of
the Quarterly Review Workflow into the Monthly Review; the new Rhythmic
Workflow Scheduling step in `build-aos.md` with the single `@`-path
Scheduled-Task instruction rule) — those changes were already applied to the
rendered artifacts and `/builders/build-aos.md` as the spec evolved, and this
generation carries them forward. Spec 2.2.2 itself was a §36.1 version
reconciliation (runbook frontmatter drift) with no content changes, so the
authored files are restamped to 2.2.2 with no substantive edits, and the
rendered artifacts (catalog, agent-specs, aos-interviews) are verified
byte-identical to their `design-spec/` sources, which retain their own
per-file `spec_version` stamps (catalog 2.2.0, interviews 2.1.4, profiles
2.2.0/2.2.1).

## 2.1.1 — Version-sync re-render (2026-07-09)

Full re-render of the AOS Factory framework files from `spec_version` 2.1.1
(runbook §36.2), following a manual deletion of the prior 2.1.0 framework. The
design spec advanced from 2.1.0 → 2.1.1 via a §36.1 Design Readiness Review that
resolved two functionality-impacting inconsistencies (revision history 2.1.1):
the §4.1 instance tree gained the missing `/outputs` subtree, and the §16.6
guide-skeleton metadata line gained the missing `spec_version` stamp. Neither
change altered the content of the four authored builder files — the `/outputs`
subtree was already present in `/builders/build-aos.md`'s Folder Structure to
Create, and §16.6 is generated dynamically at instance-build time from the
design spec rather than hardcoded here. This generation therefore carries the
four authored files forward unchanged in substance, restamped to 2.1.1, and
re-copies the three rendered-artifact categories fresh from their (already
2.1.1) `design-spec/` sources.

Framework files generated (§35.2):

1. **Root entry** — `/build-aos.md` (`file_type: builder_entry`), a short pointer
   to `/builders/build-aos.md` (§8.3).

2. **Builders** — `/builders/build-aos.md` (`aos_builder`, §12.1, the master AOS
   builder) and `/builders/build-agent.md` (`agent_builder`, §12, the generic
   build engine).

3. **Rendered design artifacts** (read-only inside instances, §14.8) — a factory-root
   copy of `agent-catalog.yaml` (§7A.4), the `agent-specs/[agent-name]-agent/`
   folders holding `profile.md` (§7B) and `interviews.md` (§7C) for all 15
   §7.3 agents, and `aos-interviews.md` (§7C/§12.1). Each is rendered from its
   `design-spec/` source.

4. **Changelog** — this file (`builder_changelog`, §16.9).

Every generated file's frontmatter is stamped with `spec_version: 2.1.1` (§35.1,
§15). No user-specific AOS instance was generated in this phase (§35.1).

## 2.1.0 — Initial framework generation (2026-07-06)

First generation of the AOS Factory framework files from `spec_version` 2.1.0
(runbook §36.2), following a manual deletion of the prior framework. This is an
internal milestone: no plugin is published at 2.1.0 (§36.3 plugin generation is a
separate, later step).

Framework files generated (§35.2):

1. **Root entry** — `/build-aos.md` (`file_type: builder_entry`), a short pointer
   to `/builders/build-aos.md` (§8.3).

2. **Builders** — `/builders/build-aos.md` (`aos_builder`, §12.1, the master AOS
   builder) and `/builders/build-agent.md` (`agent_builder`, §12, the generic
   build engine). The former 14 per-agent builders are collapsed into the single
   generic engine (§8.1); their interview content lives on as the §7C scripts.

3. **Rendered design artifacts** (read-only inside instances, §14.8) — a factory-root
   copy of `agent-catalog.yaml` (§7A.4), the `agent-specs/[agent-name]-agent/`
   folders holding `profile.md` (§7B) and `interviews.md` (§7C) for all 15
   §7.3 agents, and `aos-interviews.md` (§7C/§12.1). Each is rendered from its
   `design-spec/` source.

4. **Changelog** — this file (`builder_changelog`, §16.9).

Every generated file's frontmatter is stamped with `spec_version: 2.1.0` (§35.1,
§15). No user-specific AOS instance was generated in this phase (§35.1).
