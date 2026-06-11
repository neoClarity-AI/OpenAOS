---
title: AOS Factory Design Specification — Revision History
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 1.0.6
created_date: 2026-06-02
last_updated: 2026-06-10
status: design_ready_for_generation_planning
---

# AOS Factory Design Specification — Revision History

Part of the AOS Factory Design Specification document set. The canonical design is in `aos-factory-design-specification.md`; this file holds its dated revision and consistency-resolution history. The specification remains the single source of truth (Section 1.6.1).

Entries below are in reverse chronological order (newest first).

## Document Restructure (2026-06-10, Light Split)

The specification was split into a small companion set for readability, with no change to normative design content:

```text
1. Revision history extracted — the five dated Design Consistency Resolution passes (2026-06-02 through the fifth 2026-06-10 pass) were moved verbatim from the specification's front matter into this file.

2. Generation runbook extracted — Sections 33-37 (final consolidation decisions, ready-to-generate checklist, proposed builder generation scope, required continuation behavior, and status) were moved verbatim to aos-factory-generation-runbook.md. Section numbering 33-37 is preserved so existing cross-references continue to resolve.

3. Document Set pointer added — the canonical specification now lists the companion files and reaffirms it remains the single source of truth (Section 1.6.1). The Proceed safety gate is unchanged.
```

This pass bumped `spec_version` from 1.0.5 to 1.0.6. No Section 1-32 design content was altered.

## Design Consistency Resolutions (2026-06-10, Fifth Pass)

A further final consistency check identified one inconsistency that would affect the generated factory's behavior, resolved with the user as follows:

```text
1. "build summary" naming collision — The term "build summary" named two distinct artifacts at opposite ends of the build lifecycle. Section 9.1 step 5 ("Generate a build summary") is a pre-Proceed preview shown before any files are created, while Section 13's "Build Summary" is the canonical post-build saved artifact (file_type build_summary), emitted by the builder's final "## Handoff Summary" step and recording the files created. Because they shared the name, a builder generated from this spec could conflate them — emitting only the preview and never saving the Section 13 file, or saving it prematurely with an empty "Files Created" section. Resolution (Option A): Section 9.1 step 5 is renamed "Generate a build plan / pre-build preview"; a clarifying note distinguishing it from the Section 13 Build Summary is added to Section 9.1; and a cross-reference reserving the term "Build Summary" for the post-build saved artifact only is added to Section 13. The Section 27 build_summary validation question was left out of scope at the user's instruction.
```

This pass bumped `spec_version` from 1.0.4 to 1.0.5.

## Design Consistency Resolutions (2026-06-10, Fourth Pass)

A further final consistency check identified four items (one substantive on file naming, three minor), resolved with the user as follows:

```text
1. Project-instructions filename casing — The workspace-root project-instructions file was written as lowercase /claude.md (Sections 1.1, 4.1, 15.4, 28.1, 28.2), but Claude Cowork / Claude Code auto-loads CLAUDE.md (uppercase), which is also the actual file in this workspace. All normative references were renamed /claude.md → /CLAUDE.md, including the shipped example (examples/CLAUDE.md in 28.2). The dated historical resolution entries in earlier passes retain the original lowercase for historical fidelity.

2. Required-agent display names — The full names "Security / Permissions Agent" and "Review / Reflection Agent" were shortened to "Security Agent" and "Review Agent" throughout (Sections 1.6.2, 1.6.7, 2.3, 7.1, 7.4, 16.6, 17, 22, 23, 24, 27), making the existing agent-registry example (Section 10.3) canonical. Slugs (security-agent, review-agent) and builder filenames were already short and are unchanged.

3. Build Summary file_type — The Build Summary (Section 13), previously the canonical end-of-build artifact with no entry in the controlled file_type vocabulary, is now a saved file with file_type build_summary (added to Section 15.4), written to /agents/[agent-name]-agent/logs/[agent-name]-build-summary.md.

4. Design-spec frontmatter vocabulary — file_type design_spec was added to the Section 15.4 vocabulary to cover this source document, and a Section 15.5 note records that the design spec's status field tracks design-phase lifecycle and is exempt from the four controlled artifact-status values.
```

This pass bumped `spec_version` from 1.0.3 to 1.0.4.

## Design Consistency Resolutions (2026-06-10, Third Pass)

A further final consistency check identified three inconsistencies (one substantive, two minor), resolved with the user as follows:

```text
1. Competing end-of-build artifacts — Section 13 defined a "Build Summary" produced at the end of each agent build, while Section 18.4's handoff-summary-template listed "when an agent completes a build" among its uses, and Section 12's builder schema ends with a "## Handoff Summary" step. The scopes are now separated: the Section 13 Build Summary is the canonical end-of-build artifact; Section 18.4's handoff-summary-template scope is narrowed to cross-agent handoffs, escalations, and major-work transfers (build completion removed); and Section 13 now cross-references that the builder's "## Handoff Summary" step (Section 12) emits the Build Summary. Section 23 (cross-agent handoffs use the template) is unchanged and now non-overlapping.

2. Root files absent from folder trees — Section 6 creates /aos-manifest.md and /aos-map.md at the instance root, but the Section 4 and 4.1 trees showed only folders, whereas Section 5's tree shows the agent's .md file. Both instance-root trees now list /aos-manifest.md and /aos-map.md, matching Section 5's convention.

3. Generic builder frontmatter file_type — Section 15.1's example uses file_type: agent_builder, while build-aos.md is aos_builder and the root /build-aos.md is builder_entry. Reviewed and left as-is: Section 15.1 is explicitly illustrative ("like this") and the per-file file_type values are already specified in Sections 12.1 and 15.4. No change.
```

This pass bumped `spec_version` from 1.0.2 to 1.0.3.

## Design Consistency Resolutions (2026-06-10, Second Pass)

A further final consistency check identified three inconsistencies (one substantive, two minor), resolved with the user as follows:

```text
1. Factory-internal path notation — Section 4.1's tree nests build-aos.md, builder-changelog.md, and builders/ inside /aos-factory/, but Sections 6, 8.2, 8.3, 9.3, 10.3, 12.1, 14.5, 28.1, 28.2, and 35 wrote them with workspace-root leading slashes. Section 4.1 now adds a factory-relative path convention (parallel to the instance-relative rule): factory-internal paths resolve against the AOS Factory root (/aos-factory/), so a leading slash denotes the root of the relevant container, not the AOS Workspace root. Existing path text is unchanged.

2. Second exact-string command — Section 36.1's suggested prompt used a second exact-string gate, "Continue," conflicting with the single-exact-string-command principle (1.6.8, 16.6). The continuation is now split into two sequentially gated workflows (Final Design Consistency Check; Framework Generation), each gated by an action-specific "Proceed" per Section 2.5. "Proceed" remains the only exact-string command and the review gate no longer auto-triggers generation.

3. Incomplete workflow ownership — "Primary owner" lines added to the three remaining Section 17 workflows that lacked them, owned by required agents: Chief of Staff Agent for 17.6 (inbox-to-task, with Inbox / Communications Agent support when installed) and 17.7 (project kickoff, with Project Manager Agent support when installed); Chief of Staff Agent with Memory Agent support for 17.8 (decision capture). Every Section 17 subsection now carries a Primary owner line.
```

This pass bumped `spec_version` from 1.0.1 to 1.0.2.

## Design Consistency Resolutions (2026-06-10)

A further final consistency check identified five inconsistencies (three substantive, two minor), resolved with the user as follows:

```text
1. Workspace layout model — Section 4.1 rewritten to the AOS Workspace model: the AOS Workspace root holds /aos-router.md and /claude.md, with the AOS Factory (aos-factory/) and each generated AOS instance (/[aos-name]/) as sibling folders. Reconciled with Sections 7.4, 10.3, 15.4, and 28.1. A three-term definition (AOS Workspace, AOS Factory, AOS) was added to Section 1.1.

2. Hard-coded instance names — "AOS-03" renamed to "AOS Workspace" throughout (Sections 7.4, 10.3, 15.4, 28.1). The hard-coded work-aos/personal-aos instance names in Sections 7.4 and 10.3 were generalized to "every AOS instance's Chief of Staff Agent," matching the instance-agnostic design (1.6.6).

3. Example workspace-root files — Sections 28.1 and 28.2 now state that examples/aos-router.md and examples/claude.md are authored during plugin packaging (28.2, step 3), not during framework generation (Section 35), closing the previously undefined origin of these files.

4. Workflow ownership — "Primary owner" lines added to Section 17 for consistency with 1.6.7 and the existing 17.3/17.9 entries: Chief of Staff Agent for 17.1 (daily startup) and 17.2 (end-of-day); Review Agent for 17.4 (monthly) and 17.5 (quarterly).

5. Self-referential filename — Section 36.1 and the frontmatter title updated to match the actual filename (aos-factory-design-specification.md), and "- Final" dropped from the title.
```

This pass also added `spec_version: 1.0.1` to the frontmatter, treating the originally accepted design as the implicit 1.0.0 baseline and this consistency pass as the first recorded revision.

## Design Consistency Resolutions (2026-06-02)

The following design inconsistencies were identified during the final consistency check and resolved with the user before generation planning continued:

```text
1. Framework vs. instance layout — The reusable builder framework and the AOS instances it produces are sibling structures at the repository root. Instance-relative paths resolve against the target AOS instance root. See Section 4.1.

2. Inbox move approval — Moving files always requires explicit approval, with one narrow pre-authorized exception: moving items into /inbox/processed under the approved inbox-to-task workflow. See Sections 3.2, 17.6, and 31.

3. Tool access source of truth — The global tool access matrix (/configs/tool-access-matrix.md) is authoritative and overrides agent configs on conflict; agent config Tool Access sections only reference it. See Sections 22 and 16.1.

4. Missing builder schemas — A section schema is now defined for /builders/build-aos.md. See Section 12.1.
```

The remaining minor consistency items from that check, together with further consistency passes on 2026-06-03, have since been resolved and are recorded in the Design Consistency Resolutions section above; the full change history is tracked in Git.
