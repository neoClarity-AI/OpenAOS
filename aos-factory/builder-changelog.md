---
title: Builder Changelog
file_type: builder_changelog
spec_version: 1.1.0
created_date: 2026-06-11
last_updated: 2026-06-25
status: active
---

# Builder Changelog

Tracks changes to the reusable AOS Factory framework itself - the root build
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

### 2026-06-30 — Document Librarian Agent renamed to Document Agent

- **Manual rename, no spec_version bump.** Renamed `Document Librarian Agent` to
  `Document Agent` across the framework (slug `document-librarian-agent` ->
  `document-agent`) to match the corresponding design-spec rename:
  - `/builders/build-document-librarian-agent.md` renamed to
    `/builders/build-document-agent.md`; title, headings, file paths, and
    generated-file names updated throughout (bare stem `document-librarian` ->
    `document`).
  - `agent-catalog.yaml` - updated the agent's `slug`, `display_name`, and
    `artifacts_owned` path, plus cross-references from `writing-agent`'s
    `collaborates_with` and `non_responsibilities`.
  - `/builders/build-project-manager-agent.md` and
    `/builders/build-research-agent.md` - updated collaboration mentions.
  - Companion plugin files updated to match (see plugin changelog).
- This is a hand-applied patch, not a full Section 36.2 regeneration; the
  framework's `spec_version` stamp is unchanged. A future full rebuild from the
  design spec will re-derive the same result.

### 1.1.0 — 2026-06-25

- **Full framework rebuild from the design spec at `spec_version` 1.1.0** under
  the Section 36.2 generation workflow (`Rebuild the factory`). All 19 framework
  files were regenerated and re-stamped from `spec_version` 1.0.5 to 1.1.0: the
  root entry `/build-aos.md`, this `/builder-changelog.md`, the master
  `/builders/build-aos.md`, and all 16 agent builders.
- **Continuous Learning Loop wired into the affected builders** (the 1.1.0 spec
  change; revision-history "Continuous Learning Loop", Sections 6.1, 7.4,
  17.3-17.4, 17.10, 25):
  - `/builders/build-aos.md` - added `/workflows/learning-capture-workflow.md`
    to the Global Files to Create list and noted its Section 17.10 generation
    (Memory owns intake, Chief of Staff invokes at handoff, Review consolidates).
  - `/builders/build-memory-agent.md` - Memory Agent now owns the
    learning-capture loop: candidate intake, the agent-learnings index,
    candidate hygiene, the candidate-to-confirmed lifecycle, and primary
    ownership of `/workflows/learning-capture-workflow.md` (capture is Level 1
    append-only).
  - `/builders/build-review-agent.md` - Review Agent now owns learning
    consolidation: weekly merge/prune/promote to confirmed and monthly deeper
    consolidation with `Proceed`-gated template proposals; consolidation is
    data-file-only per the Section 14.8 drift invariant.
  - `/builders/build-chief-of-staff-agent.md` - Chief of Staff may invoke the
    learning-capture workflow at task handoff (Section 17.10).
- **Display-name conformance.** Corrected the lingering "Review / Reflection
  Agent" display name to "Review Agent" in `/builders/build-review-agent.md`
  (title + headings) and in the Chief of Staff builder's suggested-next-agent
  line, matching the shortened naming adopted spec-wide (revision history 1.0.1
  item 13). Slugs (`review-agent`) were already short and are unchanged.
- **The remaining 13 builders** (security, learning, inbox, calendar, task,
  project-manager, research, writing, document-librarian, personal-crm, finance,
  health-life-logistics, automation) and the root entry required no content
  change beyond the `spec_version` re-stamp; the learning loop is additive and
  does not touch their domains. All files remain free of the retired
  `builder_version`/`schema_version` fields and conformant to their
  required-heading schemas (Sections 12, 12.1).
- Source: design spec / runbook at `spec_version` 1.1.0.

### 1.0.5 — 2026-06-11

- Version model simplified across the framework files. Removed `builder_version`
  and `schema_version` from every builder file's frontmatter; added
  `spec_version` (= the spec the file was rendered from). `compatible_aos_versions`
  retained as the separate builder->instance compatibility axis.
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
- **Conformance rebuild (2026-06-25, Section 36.2 pass).** A `Rebuild the
  factory` pass re-verified all 19 framework files against the design spec at
  `spec_version` 1.0.5 - the root entry `/build-aos.md`, the framework
  `/builder-changelog.md`, the master `/builders/build-aos.md`, and all 16
  agent builders. Every file was confirmed byte-clean (no NUL or control-byte
  damage), free of the retired `builder_version`/`schema_version` fields,
  correctly stamped `file_type` and `spec_version: 1.0.5`, and complete against
  its required-heading schema (design spec Sections 12, 12.1). No file required
  regeneration; the framework was already a faithful 1.0.5 rendering. No spec
  change; no version bump (Section 14.1).
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
