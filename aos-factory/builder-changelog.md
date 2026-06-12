---
title: Builder Changelog
file_type: builder_changelog
spec_version: 1.0.5
created_date: 2026-06-11
last_updated: 2026-06-11
status: active
---

# Builder Changelog

Tracks changes to the reusable AOS Factory framework itself — the root build
entry, the `/builders/build-*.md` files, and this changelog. Instance-level
changes belong in each generated instance's `/logs/change-log.md` and
`/logs/aos-decision-log.md`, not here (design spec Sections 14.5, 15.4).

Entries are numbered by `spec_version`: because the factory is a pure rendering
of the spec (Section 1.6.1), the framework version *is* the `spec_version` it was
generated from (Section 14.1). When the framework is distributed as a Claude
plugin (Section 28), the plugin version is kept in sync with that `spec_version`.
This changelog is distinct from the design `aos-factory-revision-history.md`:
that file is the design audit trail and lives with the spec, while this one
tracks framework-file and packaging changes and ships inside the plugin
(Section 14.5).

## Entries

### 1.0.5 — 2026-06-11

- Version model simplified across the framework files. Removed `builder_version`
  and `schema_version` from every builder file's frontmatter; added
  `spec_version` (= the spec the file was rendered from). `compatible_aos_versions`
  retained as the separate builder→instance compatibility axis.
- Updated `/builders/build-aos.md`: stamps generated files with `spec_version`
  (instance files also `aos_version`), sets the initial instance `aos_version`
  to 1.0.0 and `Spec Version` in `/aos-manifest.md`, and generates the AOS User
  Guide as a regenerable projection (Sections 14.8, 16.6).
- Updated `/builders/build-review-agent.md`: the Review Agent now owns and
  reconciles `aos_version` and regenerates the user guide as a projection rather
  than hand-editing prose (Sections 14.3.1, 14.8, 16.6).
- Re-stamped this changelog to `spec_version` numbering.
- **Integrity repair (2026-06-11, Section 36.2 rebuild pass).** A `Rebuild the
  factory` pass detected and repaired three framework files damaged by an earlier
  bad write, regenerating them from the design spec at `spec_version` 1.0.5: the
  root entry `/build-aos.md` (24 trailing NUL bytes stripped), the master
  `/builders/build-aos.md` (was truncated mid-`Validation Checklist`; restored
  through `## AOS Setup Summary`), and `/builders/build-review-agent.md` (was
  truncated mid-sentence at `## Memory Generation Rules`; restored through
  `## Handoff Summary`). The remaining 16 framework files were verified
  byte-clean and schema-conformant and left unchanged. No spec change; no version
  bump.
- Source: design spec / runbook at `spec_version` 1.0.5.

### 1.0.4 — 2026-06-11

- Full framework rebuild from `design-spec/aos-factory-design-specification.md`
  (then at `spec_version` 1.0.4) under the Section 36.2 generation workflow.
- Regenerated the root entry pointer `/build-aos.md` and the master AOS builder
  `/builders/build-aos.md`.
- Regenerated all 16 agent builders: 4 required governance agents (security,
  memory, chief-of-staff, review) and 12 optional productive agents (learning,
  inbox, calendar, task, project-manager, research, writing, document-librarian,
  personal-crm, finance, health-life-logistics, automation).
- Added this framework-root `/builder-changelog.md`, bringing the factory into
  conformance with Sections 14.5 and 35.2.
- No runtime installer; the factory is generated from the design spec and
  distributed via the Claude plugin (Section 28).

> Note: the prior entry was originally labelled "1.0.0" under the retired
> `builder_version` scheme; it is renumbered here to the `spec_version` (1.0.4)
> the rebuild was generated from, per the 1.0.5 version-model change.
