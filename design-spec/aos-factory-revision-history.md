---
title: AOS Factory Design Specification — Revision History
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 1.0.5
created_date: 2026-06-02
last_updated: 2026-06-11
status: design_ready_for_factory_generation
---

# AOS Factory Design Specification — Revision History

Part of the AOS Factory Design Specification document set. The canonical design is in `aos-factory-design-specification.md`; this file holds its dated revision and consistency-resolution history. The specification remains the single source of truth (Section 1.6.1).

Entries below are in reverse chronological order (newest first).

| spec_version | Date       | Change |
|--------------|------------|--------|
| 1.0.5        | 2026-06-11 | Version model simplified: `builder_version`/`schema_version` collapsed into `spec_version`; `aos_version` assignment/increment rule + Review-Agent ownership added; definition/data file definitions + drift invariant added; AOS User Guide reclassified as a regenerable projection |
| 1.0.4        | 2026-06-11 | §36.3 Claude Plugin Generation workflow authored; §28.2 aligned to the shipped plugin (examples/ → templates/, README.md added) |
| 1.0.3        | 2026-06-11 | §36.1 Design Readiness Review cycle — checklists verified; §34.2 item 1 dispositioned N/A; §28.1 step 3 citation corrected; no functionality-impacting inconsistencies found |
| 1.0.2        | 2026-06-10 | Document restructure — light split into the 3-file set |
| 1.0.1        | 2026-06-10 | Design consistency resolution cycle — 16 items, surfaced across 5 re-read iterations of the §36.1 loop |
| 1.0.0        | 2026-06-02 | Baseline design accepted; initial consistency resolution (4 items) |

## Review Log (no-version entries)

These entries record completed activities that did not change the design content and therefore did not increment `spec_version` (per the content-only versioning principle, §1.6.1).

- **2026-06-11 — §36.1 Design Readiness Review against spec_version 1.0.5.** All §34.1 (20) and §34.2 (5) checklist items were reset, independently re-verified, and re-marked Done; the canonical design (Sections 1–32) was reviewed for logical consistency. No functionality-impacting inconsistencies were found and no design content changed, so no version increment was made. One non-blocking observation was noted and dispositioned "leave as-is" by the user: §27's enumerated agent-completeness list does not name the per-agent Build Summary (§13/§15.4), which is still produced via the §12 Handoff Summary step.

## 1.0.5 — Version Model Simplification and Drift Control (2026-06-11)

The versioning and update policy (§14) and the frontmatter standards (§15) were simplified, and the supporting drift-control and instance-versioning rules were made explicit. No agent roster, workflow, template, or path convention changed.

1. **`builder_version` and `schema_version` collapsed into `spec_version`** — because the factory is a pure rendering of the spec (§1.6.1), a framework change can only come from a spec change, and a file-schema change is itself a spec change. The two derived numbers carried no independent information and invited drift, so they were removed. §14.1 now states the framework version *is* the `spec_version`; §14.2 and the §15.1–15.3 frontmatter examples were updated; a mandatory stamping rule was added (every generated file records the `spec_version` it was rendered from). `compatible_aos_versions` is retained as the separate builder→instance compatibility axis.

2. **Instance versioning made explicit** — §14.3 now defines two independent instance axes: `spec_version` (provenance / last-conformed design) and `aos_version` (the instance's own evolving version). §14.3.1 adds the previously-missing assignment and increment rule (start at 1.0.0; PATCH/MINOR/MAJOR semantics, with MAJOR as the line that interacts with `compatible_aos_versions`). The `/aos-manifest.md` schema replaced "Builder Version Used / Schema Version Used" with "Spec Version." Per-file version fields are clarified as creation/regeneration provenance stamps; the live instance version lives only in the manifest.

3. **`aos_version` ownership assigned** — the Review Agent owns and reconciles `aos_version` (monthly reconciliation against `/logs/change-log.md`, plus verification in its completeness audit); the triggering event is logged by the agent that made the change (Chief of Staff coordinating); breaking/MAJOR bumps are applied at the time of change. Recorded in §7.4 and §14.3.1.

4. **Definition/data file definitions and the drift invariant added** — new §14.8 defines a *definition file* (fully determined by spec + instance configuration; factory-owned; regenerable) and a *data file* (accumulates from operation/user input; agent-owned; never overwritten by the factory), with an operational test for each and a rule for mixed/derived files. The invariant: agents write data files, the factory owns definition files, and no operating agent modifies a framework-derived definition file. This bounds drift to data and keeps factory updates a clean overwrite rather than a three-way merge.

5. **AOS User Guide reclassified as a regenerable projection** — §16.6 and §17.4 now describe the guide as a projection (§14.8): a regenerable view assembled from definition files plus its embedded Change Log as the sole data input. The Review Agent regenerates it rather than hand-editing prose, so a newer factory can regenerate it wholesale without a merge.

6. **Compatibility-note and plugin-sync wording updated** — §14.6 reframes compatibility detection around `spec_version` (a coarser signal: warn on mismatch, block only when explicitly broken). §28.2 and runbook §36.3 now sync the plugin version to `spec_version`. §14.5 adds a note distinguishing `/builder-changelog.md` (framework/packaging changes, ships in the plugin) from this revision history (design audit trail), now that both are numbered by `spec_version`.

Deferred (noted, not yet authored): the factory→instance migration/reconciliation workflow that a MAJOR `aos_version` bump implies (§14.4, §28 hold its current scope).

## 1.0.4 — Plugin Generation Workflow (2026-06-11)

The §36.3 Claude Plugin Generation workflow was authored in the generation
runbook, completing the third of the three gated build workflows in §36
(alongside §36.1 Design Readiness Review and §36.2 AOS Factory Generation).

1. **§36.3 workflow authored** — the `Insert workflow here.` placeholder was
   replaced with an eight-step, `Proceed`-gated workflow. It packages the
   already-generated framework files (§35.2 output) into the Claude plugin
   layout of §28.2: a precondition check that the framework exists, a dry-run
   preview, the global file-safety/overwrite-approval model when refreshing the
   canonical `plugin/aos-factory/`, the exact-string `Proceed` gate (scoped to
   writing the plugin directory only — not zipping, local-load testing, or
   marketplace publishing), and a closing validation step against §§27–28.2 and
   §34. Builders map to `skills/build-*/SKILL.md`; the root `/build-aos.md`
   entry pointer is not packaged separately.
2. **§28.2 aligned to the shipped plugin** — the canonical plugin layout and
   packaging steps were reconciled with the real `plugin/aos-factory/`: the
   shipped example workspace-root files now live under `templates/` (was
   `examples/`), and `README.md` (plugin install + usage instructions) was added
   to the layout diagram and packaging step 3. The `CLAUDE.md` filename is
   unchanged (already uppercase per 1.0.1 item 12). The plugin `README.md` copy
   instructions were corrected to `CLAUDE.md` to match.

## 1.0.3 — Design Readiness Review (2026-06-11)

A §36.1 Design Readiness Review was run end to end. The cycle surfaced no inconsistencies that impact the functionality of the generated factory; the design remained internally consistent across path conventions (§4.1), the file_type/status vocabularies (§15.4–15.5), the agent roster and builder set (§7–§8, §35.2), workflow/template ownership (§17–§18), and the inbox-move exception (§3.2/17.6/31). The items below record the cycle's dispositions.

1. **§34.1 Design Completion Checklist** — all 20 items re-verified against current spec content and confirmed Done. Cross-checks reconciled: 4 required + 12 optional agents = 16, matching the 16 agent builders (§8.2) and the §35.2 generation scope; 9 global workflows (§17) and 6 templates (§18) match the §6 global-files list.
2. **§34.2 Safety Confirmation Checklist** — items 2–6 verified Done. Item 1 ("No builder files have been generated yet") is no longer literally true: the factory builders already exist under `aos-factory/`. Per user decision, item 1 is dispositioned **N/A** for the post-generation state, with its wording left unchanged; the operative safety property (no overwrite without a separate `Proceed`) remains enforced by §34.2 items 3 and 5 and by §3.2. Consequence noted: a §36.2 generation run will halt at its step-2 check on item 1 and notify the user, which is acceptable safe behavior.
3. **§28.1 step 3 citation corrected** — step 3 previously called `Proceed` "the safety gate in Section 34.2"; the exact-string approval gate is defined in §3.1, while §34.2 is the Safety Confirmation Checklist. Step 3 now reads "the approval gate in Section 3.1; the §34.2 Safety Confirmation Checklist must also be satisfied." This corrects user-facing generation documentation only; no normative behavior changed.

## 1.0.2 — Document Restructure (2026-06-10, Light Split)

The specification was split into a small companion set for readability, with no change to normative design content:

1. **Revision history extracted** — the dated Design Consistency Resolution cycles (2026-06-02 and 2026-06-10) were moved verbatim from the specification's front matter into this file.
2. **Generation runbook extracted** — Sections 33-37 (final consolidation decisions, ready-to-generate checklist, proposed builder generation scope, required continuation behavior, and status) were moved verbatim to aos-factory-generation-runbook.md. Section numbering 33-37 is preserved so existing cross-references continue to resolve.
3. **Document Set pointer added** — the canonical specification now lists the companion files and reaffirms it remains the single source of truth (Section 1.6.1). The `Proceed` safety gate is unchanged.

No Section 1-32 design content was altered.

## 1.0.1 — Design Consistency Resolutions (2026-06-10)

The final consistency check ran as the §36.1 loop — re-reading the spec until no further issues surfaced. It took five successive re-read iterations, which collectively resolved the sixteen items below. They are recorded here as the single resolution cycle they constitute (1.0.0 baseline → 1.0.1). Items are in the order resolved.

1. **Workspace layout model** — Section 4.1 rewritten to the AOS Workspace model: the AOS Workspace root holds /aos-router.md and /claude.md, with the AOS Factory (aos-factory/) and each generated AOS instance (/[aos-name]/) as sibling folders. Reconciled with Sections 7.4, 10.3, 15.4, and 28.1. A three-term definition (AOS Workspace, AOS Factory, AOS) was added to Section 1.1.
2. **Hard-coded instance names** — "AOS-03" renamed to "AOS Workspace" throughout (Sections 7.4, 10.3, 15.4, 28.1). The hard-coded work-aos/personal-aos instance names in Sections 7.4 and 10.3 were generalized to "every AOS instance's Chief of Staff Agent," matching the instance-agnostic design (1.6.6).
3. **Example workspace-root files** — Sections 28.1 and 28.2 now state that examples/aos-router.md and examples/claude.md are authored during plugin packaging (28.2, step 3), not during framework generation (Section 35), closing the previously undefined origin of these files.
4. **Workflow ownership (first set)** — "Primary owner" lines added to Section 17 for consistency with 1.6.7 and the existing 17.3/17.9 entries: Chief of Staff Agent for 17.1 (daily startup) and 17.2 (end-of-day); Review Agent for 17.4 (monthly) and 17.5 (quarterly).
5. **Self-referential filename** — Section 36.1 and the frontmatter title updated to match the actual filename (aos-factory-design-specification.md), and "- Final" dropped from the title.
6. **Factory-internal path notation** — Section 4.1's tree nests build-aos.md, builder-changelog.md, and builders/ inside /aos-factory/, but Sections 6, 8.2, 8.3, 9.3, 10.3, 12.1, 14.5, 28.1, 28.2, and 35 wrote them with workspace-root leading slashes. Section 4.1 now adds a factory-relative path convention (parallel to the instance-relative rule): factory-internal paths resolve against the AOS Factory root (/aos-factory/), so a leading slash denotes the root of the relevant container, not the AOS Workspace root. Existing path text is unchanged.
7. **Second exact-string command** — Section 36.1's suggested prompt used a second exact-string gate, "Continue," conflicting with the single-exact-string-command principle (1.6.8, 16.6). The continuation is now split into two sequentially gated workflows (Final Design Consistency Check; Framework Generation), each gated by an action-specific "Proceed" per Section 2.5. "Proceed" remains the only exact-string command and the review gate no longer auto-triggers generation.
8. **Incomplete workflow ownership** — "Primary owner" lines added to the three remaining Section 17 workflows that lacked them, owned by required agents: Chief of Staff Agent for 17.6 (inbox-to-task, with Inbox / Communications Agent support when installed) and 17.7 (project kickoff, with Project Manager Agent support when installed); Chief of Staff Agent with Memory Agent support for 17.8 (decision capture). Every Section 17 subsection now carries a Primary owner line.
9. **Competing end-of-build artifacts** — Section 13 defined a "Build Summary" produced at the end of each agent build, while Section 18.4's handoff-summary-template listed "when an agent completes a build" among its uses, and Section 12's builder schema ends with a "## Handoff Summary" step. The scopes are now separated: the Section 13 Build Summary is the canonical end-of-build artifact; Section 18.4's handoff-summary-template scope is narrowed to cross-agent handoffs, escalations, and major-work transfers (build completion removed); and Section 13 now cross-references that the builder's "## Handoff Summary" step (Section 12) emits the Build Summary. Section 23 (cross-agent handoffs use the template) is unchanged and now non-overlapping.
10. **Root files absent from folder trees** — Section 6 creates /aos-manifest.md and /aos-map.md at the instance root, but the Section 4 and 4.1 trees showed only folders, whereas Section 5's tree shows the agent's .md file. Both instance-root trees now list /aos-manifest.md and /aos-map.md, matching Section 5's convention.
11. **Generic builder frontmatter file_type** — Section 15.1's example uses file_type: agent_builder, while build-aos.md is aos_builder and the root /build-aos.md is builder_entry. Reviewed and left as-is: Section 15.1 is explicitly illustrative ("like this") and the per-file file_type values are already specified in Sections 12.1 and 15.4. No change.
12. **Project-instructions filename casing** — the workspace-root project-instructions file was written as lowercase /claude.md (Sections 1.1, 4.1, 15.4, 28.1, 28.2), but Claude Cowork / Claude Code auto-loads CLAUDE.md (uppercase), which is also the actual file in this workspace. All normative references were renamed /claude.md → /CLAUDE.md, including the shipped example (examples/CLAUDE.md in 28.2). The earlier dated entry (2026-06-02) retains the original lowercase for historical fidelity.
13. **Required-agent display names** — the full names "Security / Permissions Agent" and "Review / Reflection Agent" were shortened to "Security Agent" and "Review Agent" throughout (Sections 1.6.2, 1.6.7, 2.3, 7.1, 7.4, 16.6, 17, 22, 23, 24, 27), making the existing agent-registry example (Section 10.3) canonical. Slugs (security-agent, review-agent) and builder filenames were already short and are unchanged.
14. **Build Summary file_type** — the Build Summary (Section 13), previously the canonical end-of-build artifact with no entry in the controlled file_type vocabulary, is now a saved file with file_type build_summary (added to Section 15.4), written to /agents/[agent-name]-agent/logs/[agent-name]-build-summary.md.
15. **Design-spec frontmatter vocabulary** — file_type design_spec was added to the Section 15.4 vocabulary to cover this source document, and a Section 15.5 note records that the design spec's status field tracks design-phase lifecycle and is exempt from the four controlled artifact-status values.
16. **"build summary" naming collision** — the term "build summary" named two distinct artifacts at opposite ends of the build lifecycle. Section 9.1 step 5 ("Generate a build summary") is a pre-Proceed preview shown before any files are created, while Section 13's "Build Summary" is the canonical post-build saved artifact (file_type build_summary), emitted by the builder's final "## Handoff Summary" step and recording the files created. Because they shared the name, a builder generated from this spec could conflate them — emitting only the preview and never saving the Section 13 file, or saving it prematurely with an empty "Files Created" section. Resolution (Option A): Section 9.1 step 5 is renamed "Generate a build plan / pre-build preview"; a clarifying note distinguishing it from the Section 13 Build Summary is added to Section 9.1; and a cross-reference reserving the term "Build Summary" for the post-build saved artifact only is added to Section 13. The Section 27 build_summary validation question was left out of scope at the user's instruction.

## Design Consistency Resolutions (2026-06-02)

The following design inconsistencies were identified during the final consistency check and resolved with the user before generation planning continued:

1. **Framework vs. instance layout** — The reusable builder framework and the AOS instances it produces are sibling structures at the repository root. Instance-relative paths resolve against the target AOS instance root. See Section 4.1.

2. **Inbox move approval** — Moving files always requires explicit approval, with one narrow pre-authorized exception: moving items into /inbox/processed under the approved inbox-to-task workflow. See Sections 3.2, 17.6, and 31.

3. **Tool access source of truth** — The global tool access matrix (/configs/tool-access-matrix.md) is authoritative and overrides agent configs on conflict; agent config Tool Access sections only reference it. See Sections 22 and 16.1.

4. **Missing builder schemas** — A section schema is now defined for /builders/build-aos.md. See Section 12.1.

The remaining minor consistency items from that check, together with further consistency passes on 2026-06-03, have since been resolved and are recorded in the Design Consistency Resolutions section above; the full change history is tracked in Git.

**Note:** Many design consistency resolution loops were run prior to the implementation of this revision history log, culminating in the baseline design committed to Git.
