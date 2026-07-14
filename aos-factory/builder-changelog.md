---
title: AOS Factory Builder Changelog
file_type: builder_changelog
spec_version: 2.3.2
created_date: 2026-07-13
last_updated: 2026-07-13
status: active
---
# AOS Factory Builder Changelog

Tracks changes to the **framework files** and their **packaging** (design spec
§14.5, §16.9). This is distinct from `design-spec/aos-factory-revision-history.md`,
which is the design audit trail: same `spec_version` numbering, different purpose
and audience. When the framework is distributed as a Claude plugin (§28), the
plugin version is kept in sync with `spec_version` (§14.1) and noted below.

Entries are in reverse chronological order (newest first).

| spec_version | Plugin version | Date       | Summary                                                        |
| ------------ | -------------- | ---------- | -------------------------------------------------------------- |
| 2.3.2        | 2.3.2          | 2026-07-13 | Factory framework generated from spec_version 2.3.2 (§36.2).   |
| 2.1.0        | 2.1.0          | 2026-07-06 | Generic build engine replaces the 14 per-agent builders.       |
| 2.0.0        | 2.0.0          | 2026-07-01 | Agent Catalog + per-agent profiles; factory ships rendered artifacts. |
| 1.0.4        | 1.0.4          | 2026-06-11 | Claude plugin packaging defined (§28.2).                       |

## 2.3.2 — Factory framework generation (2026-07-13)

Plugin version: **2.3.2** (synced to `spec_version`).

Generated the AOS Factory framework files from the design specification at
`spec_version 2.3.2` (runbook §36.2, generation scope §35.2):

- `/build-aos.md` — root entry pointer to `/builders/build-aos.md` (§8.3).
- `/builders/build-aos.md` — master AOS instance builder (§12.1).
- `/builders/build-agent.md` — generic agent build engine (§12).
- `/builder-changelog.md` — this file (§16.9).
- Rendered factory-root copies of the design-spec sources, byte-identical to
  their sources (§7A.4, §7B.2, §7C.2): `/agent-catalog.yaml`, `/aos-interviews.md`,
  and `/agent-specs/[agent-name]-agent/` (profile.md + interviews.md) for all
  15 agents in §7.3.

No functional change to the builder logic relative to the design at 2.3.2; this
is the framework rendering of the current spec.

## 2.1.0 — Generic build engine (2026-07-06)

Plugin version: **2.1.0**. Collapsed the 14 per-agent `build-[agent-name]-agent.md`
builders into a single generic engine, `/builders/build-agent.md`, that
instantiates any validated catalog entry + profile + interviews into the §5.1
file set (§8.1). Per-agent interview content moved to §7C `interviews.md`
scripts. Feedback Agent added as the fifth governance agent.

## 2.0.0 — Agent Catalog and Profiles; factory self-containment (2026-07-01)

Plugin version: **2.0.0**. Factory now renders root copies of `agent-catalog.yaml`
and the per-agent design artifacts so an installed plugin can run a spec-faithful
build. Builder files became projections of the catalog (§7A) and profiles (§7B).

## 1.0.4 — Plugin packaging (2026-06-11)

Plugin version: **1.0.4**. Defined the Claude plugin layout and packaging steps
(§28.2): `.claude-plugin/plugin.json` manifest, one skill per builder, shipped
example workspace-root templates, and README.
