---
title: AOS Factory Builder Changelog
file_type: builder_changelog
spec_version: 2.2.0
created_date: 2026-07-10
last_updated: 2026-07-10
status: active
---

# AOS Factory Builder Changelog

Tracks changes to the AOS Factory framework files and plugin packaging (§14.5, §16.9). Versioned by `spec_version`; the design audit trail lives separately in `design-spec/aos-factory-revision-history.md`. Entries are in reverse chronological order (newest first).

| spec_version | Date       | Change |
|--------------|------------|--------|
| 2.2.0        | 2026-07-10 | Factory regenerated from spec 2.2.0 (single-instance model); full framework file set rendered fresh |

## 2.2.0 — Factory regeneration at spec 2.2.0 (2026-07-10)

Complete regeneration of the AOS Factory framework from design specification 2.2.0, following a clean §36.1 Design Readiness Review (all 20 §34 items verified; no functionality-impacting inconsistencies). The previous factory tree had been removed from the repository at the 2.2.0 spec release; this build recreates it fresh.

1. **Framework files authored:** root entry `/build-aos.md`, master builder `/builders/build-aos.md` (§12.1 schema), generic agent build engine `/builders/build-agent.md` (§12 schema — the single engine covering all 15 agents; no per-agent builders), and this changelog.
2. **Rendered copies shipped:** `/agent-catalog.yaml` (catalog_version 1.2.0), `/agent-specs/` (15 per-agent folders, each with profile.md + interviews.md), and `/aos-interviews.md`, all stamped `spec_version: 2.2.0` and read-only inside instances (§7A.4, §7B.2, §7C.2, §14.8).
3. **Single-instance model:** no router file; the factory-vs-instance guard lives in the workspace-root `/CLAUDE.md` (§1.6.6, §16.10).
4. **Plugin:** re-packaged at 2.2.0 on 2026-07-10 (`claude-plugin/aos-factory/`, plugin.json 2.2.0): skills `build-aos` + `build-agent`, the 32 rendered design artifacts included at the plugin root, templates/CLAUDE.md and README.md authored. Zipping/publishing remain manual (§28.2 steps 5–8).
