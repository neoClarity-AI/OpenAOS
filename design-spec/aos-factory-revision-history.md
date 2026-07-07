---
title: AOS Factory Design Specification — Revision History
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 2.1.0
created_date: 2026-06-02
last_updated: 2026-07-06
status: design_ready_for_factory_generation
---

# AOS Factory Design Specification — Revision History

Part of the AOS Factory Design Specification document set. The canonical design is in `aos-factory-design-specification.md`; this file holds its dated revision and consistency-resolution history. The specification remains the single source of truth (Section 1.6.1).

Entries below are in reverse chronological order (newest first).

| spec_version | Date       | Change |
|--------------|------------|--------|
| 2.1.0        | 2026-07-06 | Lifecycle Profiles, Agent Advertising, Feedback Agent, Call-Name Routing + Schema Explicitness (Phase 2 of v2.0): §7B profiles gain five lifecycle sections; new §7C scripted interviews (H20); 14 per-agent builders collapsed into the generic build engine `build-agent.md`; `agent-profiles/` reorganized into per-agent `agent-specs/` folders; Feedback Agent added as fifth governance agent (`feedback.upstream`); F2 review-time advertising; F4 call-name routing (§16.10 router schema); BF-001 routing + attribution rules; U1 explicit schemas (§16.7–16.12 and in-place upgrades, items A1–H20); U2 `catalog.schema.json` + repo CI; U3 `/outputs` folder |
| 2.0.0        | 2026-06-30 | Agent Catalog + Agent Profiles (Phase 1 of v2.0): new §7A (machine-checked agent identity/ownership catalog) and §7B (per-agent behavioral profiles), both as source under design-spec/; `agent-catalog.yaml` + 14 profiles authored for the 14-agent §7.3 roster; §7.4 demoted to a generated view; §11/§12 made catalog+profile projections; §10.3.1 instance-scope overlap check; §7.5 Phase A/Phase B split; §14.8/§15.4/§27 updated for the new `agent_catalog` and `agent_profile` file types |
| 1.0.5        | 2026-06-11 | Version model simplified: `builder_version`/`schema_version` collapsed into `spec_version`; `aos_version` assignment/increment rule + Review-Agent ownership added; definition/data file definitions + drift invariant added; AOS User Guide reclassified as a regenerable projection |
| 1.0.4        | 2026-06-11 | §36.3 Claude Plugin Generation workflow authored; §28.2 aligned to the shipped plugin (examples/ → templates/, README.md added) |
| 1.0.3        | 2026-06-11 | §36.1 Design Readiness Review cycle — checklists verified; §34.2 item 1 dispositioned N/A; §28.1 step 3 citation corrected; no functionality-impacting inconsistencies found |
| 1.0.2        | 2026-06-10 | Document restructure — light split into the 3-file set |
| 1.0.1        | 2026-06-10 | Design consistency resolution cycle — 16 items, surfaced across 5 re-read iterations of the §36.1 loop |
| 1.0.0        | 2026-06-02 | Baseline design accepted; initial consistency resolution (4 items) |

## Review Log (no-version entries)

These entries record completed activities that did not change the design content and therefore did not increment `spec_version` (per the content-only versioning principle, §1.6.1).

- **2026-07-06 — §36.1 Design Readiness Review against spec_version 2.1.0 (no version increment).** All 20 §34 checklist items were reset to Not Done, independently re-verified against the design, and re-marked Done; the §33 safety governance rules were confirmed satisfied. The canonical design (Sections 1–32) and companion source artifacts were reviewed for logical consistency. No functionality-impacting inconsistencies were found and no design content changed, so no `spec_version` increment was made (§1.6.1 content-only versioning). One transient false positive was noted and dispositioned: an early pass flagged `agent-catalog.yaml` as missing the `personal-crm-agent` and `automation-agent` entries with a truncated `document-agent` entry, but this was traced to a stale sandbox file mount, not the file on disk. The on-disk catalog is complete and internally consistent — all 15 §7.3 agents have catalog entries with owned domains (including `contacts` and `automation`) and reciprocal collaboration edges.

- **2026-07-01 — Canonical plugin directory aligned to the repo (no version increment).** The §36.3 default plugin target was corrected from `plugin/aos-factory/` (an empty directory in the repo) to `claude-plugin/aos-factory/`, the path the repo's `.claude-plugin/marketplace.json` actually publishes (`source: ./claude-plugin/aos-factory`). Runbook §36.3 steps 2 and 4 were updated; the historical 1.0.4 revision entries that mention the old path are left unchanged for fidelity. Held at `spec_version` 2.0.0 per the standing decision. Note: the live `claude-plugin/aos-factory/` is still stale (plugin.json 1.1.0; skills for the removed learning/finance/health agents; missing tutor) and will be regenerated when §36.3 plugin generation runs.

- **2026-07-01 — Factory self-containment and workspace-root provisioning (no version increment, per user decision to hold spec_version 2.0.0 for this build).** Two design changes were applied during the factory build. (1) The factory now renders root copies of `agent-catalog.yaml` and `agent-profiles/[agent-name]-agent.md` — added to the generation scope (runbook §35.1, §35.2) and the §28.1 generation steps/summary, reconciling them with §4.1, §7A.4, and §7B.2, which already stated the factory ships these copies. (2) The AOS instance build now provisions the AOS Workspace root files `/aos-router.md` and `/CLAUDE.md` from the shipped example copies, non-destructively — created when absent and overwritten only after a separate `Proceed` — updating §4.1, §9.3 (new step 3, list renumbered), §12.1, and §28.2. Per user direction both were folded in at `spec_version` 2.0.0 with no increment; `last_updated` bumped to 2026-07-01 on the edited files.

- **2026-07-01 — §36.1 Design Readiness Review against spec_version 2.0.0.** All 20 §34 checklist items were reset, independently re-verified, and re-marked Done; the §33 safety governance rules were confirmed. One functionality-impacting inconsistency was found and resolved: the runbook §35.2 generation scope had drifted from the canonical 14-agent roster (§7.3, §8.2, `agent-catalog.yaml`) — it omitted `build-tutor-agent`, misnamed document as `build-document-librarian-agent`, and listed three non-roster agents (`learning`, `finance`, `health-life-logistics`). §35.2 was corrected to `build-aos` plus the 14 canonical agent builders, and the runbook frontmatter was caught up from `spec_version` 1.0.5 to 2.0.0. Per user decision this correction was folded into 2.0.0 as completion of the roster consolidation, with **no version increment**.

- **2026-06-11 — §36.1 Design Readiness Review against spec_version 1.0.5.** All §34.1 (20) and §34.2 (5) checklist items were reset, independently re-verified, and re-marked Done; the canonical design (Sections 1–32) was reviewed for logical consistency. No functionality-impacting inconsistencies were found and no design content changed, so no version increment was made. One non-blocking observation was noted and dispositioned "leave as-is" by the user: §27's enumerated agent-completeness list does not name the per-agent Build Summary (§13/§15.4), which is still produced via the §12 Handoff Summary step.

## 2.1.0 — Lifecycle Profiles, Agent Advertising, Feedback Agent, Call-Name Routing, Schema Explicitness (Phase 2 of v2.0) (2026-07-06)

Phase 2 of the v2.0 release (internal-only/feature-specs/v2.0-phase-2-agent-improvements.md; approved 2026-07-05, amended through 2026-07-06), implemented as one consolidated increment covering seven items (F1–F4, U1–U3) plus the two BF-001 generalized rules. This is an internal milestone: no plugin is published at 2.1.0. Open questions resolved with the user on 2026-07-06: **O2** — the 14 per-agent builder files are removed entirely (no thin wrappers); **O5** — call name is opt-in at instance build with a suggested default; **O6** — call-name collisions are rejected with alternatives suggested; **O7** — dog names are the suggested default framing, any single-word name accepted (guidance against human-sounding names); **O8** — no call name is reserved for unbuilt instances; **O9** — interview `ask` wording may be paraphrased (content, order, and captured fields fixed). Deferred with notes: **O3** email transport (submissions queue as `staged`; user prompted to send manually; connector choice lands with Phase 3 portability); **U1-C11** seeded section lists for the global memory files; the optional U2 extension of JSON Schema validation to §15 frontmatter.

1. **F1 — Full-lifecycle agent profiles.** §7B.3 reorganized into five normative lifecycle sections (Initialization, Operation, Usage-Driven Evolution, Update, Retirement); evolution is data-layer only, strengthening the §14.8 drift invariant in effect (§14.8 semantics unedited); Update sections carry MIGRATION INSTRUCTIONS executed by the factory's update flow; retirement gains usage signals surfaced at quarterly review. All 15 profiles conform; governance profiles state the no-retirement rule. New validation checks V11–V13 (§7B.5, §27).

2. **U1-H20 — New §7C "Agent Interviews".** Scripted interviews (`file_type: interview_script`, 8-field question-entry schema) as the third per-agent design artifact; §7.5/§7B.5 Phase A extends to three artifacts. The §9.1 move-faster exception is now deterministic (skippable questions resolve to defaults). §26 restated as script properties.

3. **Generic build engine (O2).** §8/§12 restructured: `/builders` = `build-aos.md` + `build-agent.md`; the engine instantiates any catalog entry + profile + interviews into the §5.1 file set. §9.3/§9.4/§10.1/§10.3/§14/§28/runbook §35 references re-pointed; registry and map carry no per-agent builder column (MF2 resolved by O2).

4. **agent-specs/ reorganization (H20).** `design-spec/agent-profiles/[slug].md` → `design-spec/agent-specs/[slug]/profile.md` + new `interviews.md` per agent (14 authored from the former builders' interview content, §26 properties preserved); `aos-interviews.md` authored at the design-spec root from build-aos's discovery questions, including the F4 call-name entry. Document Set listing, §4.1, §7A.4, §7B.2, §14.8 path mention, §15.4 rows, §28.1, and runbook §35 updated (MF6 resolved — F1 and H20 authored together).

5. **F3 — Feedback Agent.** Fifth governance agent (roster edits: §1.6.2, §2.3, §7.1, §7.3, §7.4, AGENTS.md); new governance domain token `feedback.upstream` (§7A.6); catalog entry + reciprocal review-agent edge (catalog_version 1.1.0); §22 matrix row; §17.4/§17.5 self-examination steps; §6 gains `/logs/feedback-log.md` with the U1-B8 entry schema as new §16.7 (MF1 previously resolved; MF3 resolved — A4 wraps the same table). The "escalates-to user" edge is expressed as an approval_required_action (edges must resolve to agent slugs per V5). New `agent-specs/feedback-agent/` profile + interviews. `feedback_log` added to §15.4.

6. **F2 — Advertising uninstalled agents.** Rhythm-bound suggestion-only surfacing: §10.4 (map as data source), §16.6 (Available Agents subsection under Managing Agents), §17.3/§17.5 (advertising checks), normative anti-nagging rule; CoS and Review profile Operation sections updated.

7. **F4 + U1-F14 — Call-name routing and router schema (authored together; MF5 resolved).** New §16.10 router file schema: Resolution Order with the call-name match as the explicit-override tier subject to the framework-vs-instance carve-out; Registered Targets table with Call name column; matching rules (case-insensitive, start-of-prompt, registry-only, unique per router); session-pin effect. §17.1 prose gains the tier; §28.2 examples become renderings of §16.10/§16.11.

8. **U1 — Explicit schemas.** New §16.8 (B6 change-log entries), §16.9 (B7 builder-changelog), §16.11 (F15 workspace CLAUDE.md), §16.12 (A5 global-permissions seed); in-place upgrades: §14.3 manifest example (A1), §10.4 map schema (A2), §10.3/§10.3.1 registry + absorbed-ownership block (A3), §22 file schema (A4), §16.2/§20.3 memory entry block (C8), §6.1 learnings index + entry format (C9/C10 — C10 carries the BF-001 attribution rule: learnings are filed under the process-owning agent, recorded in Applies To), §18 template body skeletons (D12), §21 project-file schemas (E13), §9.1 pre-build preview block (G16), §9.3 `/logs/aos-build-summary.md` (G17), §28 upgrade-recommendation block (G18), §17.1 startup-brief skeleton (G19). Numbering note: B8 landed first as §16.7 (per the feature spec's implementation order), so B6/B7 took §16.8/§16.9 rather than the sketch's pencilled §16.7.

9. **BF-001 routing rule (rides F1).** §2.2 gains the designated-owner routing language ("workflow owner"); the CoS profile's Operation section carries the rule with the review workflows named as the motivating instance.

10. **U2 — Schema format decision.** Markdown skeletons remain normative; derived `design-spec/catalog.schema.json` + `scripts/validate-catalog.py` + `.github/workflows/validate-catalog.yml` enforce the mechanical surface of V1–V4 and V5's slug half on catalog PRs (noted in §7A.5). Validated clean: 0 errors, 15 agents, 16 domains.

11. **U3 — /outputs folder (MF4 resolved).** §4 tree gains root-level `/outputs` with one subfolder per installed agent; boundary rule with `/projects` (standalone deliverables only); cross-agent lineage via handoff summary; §5.1 creates the subfolder at agent build; every catalog entry's artifacts_owned gains its `/outputs/[slug]/**` glob (catalog_version 1.2.0); §14.8's data-file examples line now includes `/outputs` — **§14.8 thereby moves from Untouched to Extended** (example line + agent-specs path fix only; the drift invariant and file-kind definitions are unchanged); §29 naming rule; §30 archive-policy lines.

Not in scope at this milestone: factory regeneration (the `aos-factory/` rendered tree remains at 2.0.0 pending a §36.2 generation run) and plugin packaging/publication (deferred to Phase 3 close per O1).

## 2.0.0 — Agent Catalog and Agent Profiles (Phase 1 of v2.0) (2026-06-30)

Phase 1 of the v2.0 release (internal-only/v2.0-phased-plan.md): moved each agent's identity and ownership out of prose buried in `build-*-agent.md` builders into a structured, machine-checkable, framework-level catalog, and each agent's behavioral narrative into a per-agent profile. Single-responsibility and non-overlap are now verified, not merely asserted. Five open design decisions (O1–O5, from the catalog proposal / GitHub issue #4) were resolved with the user, all accepting the recommended default: pre_authorized_actions stays in the catalog (O1); the controlled-vocabulary rule stays in the spec while the vocabulary list lives in the catalog (O2); §7.4 is demoted to a generated view (O3); the instance-scope overlap check is specified in §10.3 (O4); agent creation is split into a Phase A design step and a Phase B build step (O5). The roster was held at the 14-agent §7.3 set (Tutor and Document retained; no Finance or Health/Life-Logistics agent). The catalog and profiles are versioned as **source under design-spec/**, with rendered copies shipped in the factory.

1. **New §7A "Agent Catalog" section** — defines the catalog's intent and three-layer model (spec = rules, catalog = data, §11 instruction file = projection), the normative controlled-vocabulary rule, the per-agent entry schema, the catalog file's source location/format/ownership (`design-spec/agent-catalog.yaml`, YAML, framework-owned, with a rendered copy at the AOS Factory root), and the Review Agent's eight validation procedures (V1–V8).

2. **New §7B "Agent Profiles" section** — defines a per-agent narrative file (`design-spec/agent-profiles/[agent-name]-agent.md`) that holds behavior only and references the catalog for identity; its schema, its projection into §11's narrative sections, and two additional validation procedures (V9–V10). Profiles are framework-owned definition files (§14.8).

3. **`agent-catalog.yaml` authored for the full 14-agent §7.3 roster** — 4 governance + 10 productive entries with disjoint `domains_owned` drawn from the controlled vocabulary, disjoint `artifacts_owned`, reciprocal `collaborates_with` edges, and derived `non_responsibilities`; validated against V1–V8.

4. **14 agent profiles authored** — one per §7.3 agent, derived from the existing builders, behavior-only.

5. **§7.4 demoted to a generated view; §2.1 points at catalog validation** (§7A.5, §27) as the SRP enforcement surface (O3).

6. **§11 and §12 made catalog + profile projections** — §11's identity sections project from the catalog entry and its narrative sections from the profile; §12 gained rendering rules for builders to read both; §16.1 gained the `pre_authorized_actions` cross-reference note so agent configs don't restate the catalog (O1).

7. **§10.3 gains the instance-scope overlap check (new §10.3.1)** (O4); **§7.5 rewritten for the Phase A / Phase B design-vs-build split** (O5) — a design-time primitive, not a runtime Agent Maker Agent.

8. **§14.8, §15.4, §27 updated** — the catalog and profiles are classified as definition files (framework-owned, read-only in instances); the instance registry's absorbed ownership fields are classified as data (targeted, approval-gated merge only); new controlled `file_type` tokens `agent_catalog` and `agent_profile` were added to the §15.4 vocabulary and file-type-by-file table; §27 requires catalog + profile validation (V1–V10) to pass before an AOS or an agent build is considered complete.

Deferred (explicitly out of scope for this release, per user instruction): the continuous learning-capture loop is not reintroduced. Framework files (the on-disk builders and the factory's rendered catalog copy) are reconciled to this 2.0.0 spec in a separate, approval-gated rebuild; the public plugin is not re-packaged in this phase — that happens once, at the end of Phase 2 (platform portability), per the phased plan.

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
3. **Example workspace-root files** — Sections 28.1 and 28.2 now state that examples/aos-router.md and examples/claude.md are authored during plugin packaging (28.2, step 3), not during framewo