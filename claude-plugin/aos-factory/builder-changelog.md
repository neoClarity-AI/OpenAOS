---
title: AOS Factory Builder Changelog
file_type: builder_changelog
spec_version: 2.1.0
created_date: 2026-07-06
last_updated: 2026-07-06
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
| 2.1.0        | 2026-07-06 | not published  | Initial framework generation: root entry, generic build engine + master AOS builder, and rendered design artifacts (catalog, agent-specs, aos-interviews) |

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
