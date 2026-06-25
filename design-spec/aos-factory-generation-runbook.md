---
title: AOS Factory Generation Runbook
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 1.0.5
created_date: 2026-06-02
last_updated: 2026-06-11
status: design_ready_for_factory_generation
important_constraint: Do not generate actual AOS Factory files unless the user explicitly types exactly Proceed.
---

# AOS Factory Generation Runbook

Part of the AOS Factory Design Specification document set. The canonical design is in `aos-factory-design-specification.md` (Sections 1-32); this file holds the build, generation-scope, and handoff procedure (Sections 33-37). Section numbering is preserved from the specification so cross-references continue to resolve. The `Proceed` safety gate applies in full: no AOS Factory files are generated until the user types exactly `Proceed`.

---

# 33. Design Governance Rules

These rules govern how the design specification and generation runbook are
interpreted and maintained going forward.

```text
- The most recent confirmed decisions are authoritative. Where they conflict
  with earlier sections, the later decisions must govern.
- A completed decision must be preserved unless the user explicitly changes it.
- The full design spec must not be rewritten unless the user explicitly
  requests a consolidated version.
- The Agent Maker Agent reference is a design note only and must not be
  treated as authorization to add an agent to the initial roster.
- The revision history and spec_version follow the format and increment rule
  in the specification's "Revision History" section: one increment and one
  consolidated entry per completed maintenance action.
```

Operational gates derived from these rules — the contradiction/gap check,
ready-to-generate checklist, builder generation scope, framework-only build,
and the exact `Proceed` approval — are enforced in Sections 34 and 35.

---

# 34. AOS Factory Design Checklists

## 34.1 Design Completion Checklist

```text
[x] Required governance agents are defined.
[x] Optional productive agent roster is defined.
[x] Folder structures are defined.
[x] Global files are defined.
[x] Agent file sets are defined.
[x] Builder file structure is defined.
[x] Distribution and plugin-packaging mechanics are defined.
[x] Permissions and approval rules are defined.
[x] Tool access model is defined.
[x] Memory governance is defined.
[x] Logging model is defined.
[x] Workflow set is defined.
[x] Template set is defined.
[x] AOS User Guide skeleton (including the Table of Contents and Invocation Reference) is defined.
[x] Project structure is defined.
[x] Inbox policy is defined.
[x] Archive policy is defined.
[x] Validation and QA rules are defined.
[x] Output style standards are defined.
[x] Agent Maker Agent ambiguity has a recommended default.
```

## 34.2 Safety Confirmation Checklist

```text
[x] No user-specific AOS instance will be generated yet.
[x] No existing files will be overwritten without explicit approval.
[x] Any actual generation action requires the user to type exactly: Proceed.
[x] Refreshing, replacing, or overwriting existing builder files requires a separate Proceed approval.
[x] Deleting, renaming, moving, archiving, publishing, sending, spending, or sharing private information requires explicit approval.
```
# 35. AOS Factory Generation

## 35.1 Generation Rules

When generating an AOS Factory instance, you must follow these rules.

- Generate AOS Factory framework files only.
- Do not generate a user-specific AOS instance yet.
- Include root build entry file.
- Include /builders folder files.
- Include builder changelog.
- Include all approved agent builder files.
- Include dry-run / preview mode in all builders.
- Include approval gates before any file overwrite or refresh.
- Stamp every generated file's frontmatter with the `spec_version` it was rendered from (design spec Sections 14.1–14.2, 15.1). Do not emit `builder_version` or `schema_version`; those have been collapsed into `spec_version`.

## 35.2 Generation Scope

The generation phase creates the AOS Factory framework files listed below.

No AOS instance should be generated in this first generation phase unless the user separately requests that after the Builder framework exists.

```text
/build-aos.md
/builder-changelog.md
/builders/build-aos.md
/builders/build-security-agent.md
/builders/build-memory-agent.md
/builders/build-chief-of-staff-agent.md
/builders/build-review-agent.md
/builders/build-learning-agent.md
/builders/build-inbox-agent.md
/builders/build-calendar-agent.md
/builders/build-task-agent.md
/builders/build-project-manager-agent.md
/builders/build-research-agent.md
/builders/build-writing-agent.md
/builders/build-document-librarian-agent.md
/builders/build-personal-crm-agent.md
/builders/build-finance-agent.md
/builders/build-health-life-logistics-agent.md
/builders/build-automation-agent.md
```

---

# 36. AOS Factory Build Process

The AOS Factory build process consists of two separate, sequentially gated workflows. `Proceed` is the only exact-string command (Sections 1.6.8, 16.6); each `Proceed` is action-specific (Section 2.5) and authorizes only the action described immediately before it, so finalizing the consistency review never auto-triggers generation.

### 36.1 Design Readiness Review

When the user requests a "Design Readiness Review", using this workflow.

```text
Read the source file `design-spec/aos-factory-design-specification.md`.
1. Verify with the user that we are entering a Design Readiness Review. When the user types "Proceed", do the following:
   1.1 Update all design specs with the status of "in_review".
   1.2 In Section "34. AOS Factory Design Checklists", mark every checklist item as Not Done. (Replace [ ] with [ ]).
2. Conduct a completeness check by verifying each item in the "34.1 Design Completion Checklist". When an item has been verified, mark it as Done (Replace [ ] with [x]). Report any missing items and recommended actions. Repeat this step until you have marked all items Done.
3. Conduct a safety check by verifying each item in the "34.2 Safety Confirmation Checklist". Report any safety issues and recommended actions. Repeat this step until you have marked all items Done.
4. Review the design in "aos-factory-design-specification.md" for logical consistency. Report any inconsistencies to the user. Include only inconsistencies that impact the functionality of the factory it generates. If no such inconsistencies exist then inform the user. Otherwise, work with the user to resolve each issue one at a time. For each issue, offer the user options and a recommendation.
5. When all inconsistencies are resolved, present the consolidated resolutions and wait for the user to type exactly: Proceed — to finalize the consistency review. This gate authorizes only finalization of the review and update of the spec, not the generation of AOS Factory files.
6. Repeat steps 1 and 2 until no more issues are surfaced.

Do not add, modify or delete any files unless the user types exactly: Proceed.
```
### 36.2 AOS Factory Generation

When the user requests to "Build the factory" or "Rebuild the factory" or "Generate the factory" or "Regenerate the factory", using this workflow.

```
Read the source file `design-spec/aos-factory-design-specification.md`.
1. Verify that all items in the "34.1 Design Completion Checklist" are marked Done ([x]). If any items are not Done, notify the user and stop this workflow.
2. Verify that all items in the "34.2 Safety Confirmation Checklist" are marked Done ([x]). If any items are not Done, notify the user and stop this workflow.
3. Review the proposed Builder generation scope (Section 35) and plan with the user.
4. Answer any additional user questions about the design or generation plan.
5. Wait for the user to type exactly: Proceed — to authorize generation.
6. Only after that exact instruction, generate the AOS Factory framework files.

Do not generate actual AOS Factory files unless the user types exactly: Proceed.
```

### 36.3 Claude Plugin Generation

When the user requests to "Build the plugin" or "Generate the plugin", using this workflow.

```
Read the source file `design-spec/aos-factory-design-specification.md` (Section 28) and the generated framework files from Section 36.2.
1. Verify the precondition: the generated AOS Factory framework files from Section 35.2 exist — the root entry `/build-aos.md`, all `/builders/build-*.md`, and `/builder-changelog.md`. If any are missing, notify the user that the factory must be generated first (Section 36.2) and stop this workflow.
2. Set the target plugin directory (default: refresh the canonical `plugin/aos-factory/`). Read Section 28.2 for the required plugin layout and packaging steps.
3. Build a dry-run preview — list every file to be created or overwritten, writing nothing:
   3.1 `.claude-plugin/plugin.json` — manifest: name `aos-factory`, version synced to the framework `spec_version` (design spec Section 14.1) and `/builder-changelog.md`, plus description, author, keywords.
   3.2 `skills/build-*/SKILL.md` — one skill per builder. Convert each `/builders/build-*.md` into a `SKILL.md` whose frontmatter carries `name` and an invocation-oriented `description` (when-to-use triggers), with the builder body as the skill content. Map `/builders/build-aos.md` → `skills/build-aos/SKILL.md` and each `/builders/build-[agent]-agent.md` → `skills/build-[agent]-agent/SKILL.md`. The root `/build-aos.md` entry pointer is a framework-root convenience and is not packaged separately; the `build-aos` skill replaces it in plugin context.
   3.3 `builder-changelog.md` — copy the framework `/builder-changelog.md` to the plugin root.
   3.4 `templates/aos-router.md` and `templates/CLAUDE.md` — author the example workspace-root files the user copies to their AOS Workspace root after install (Section 28.2).
   3.5 `README.md` — author or refresh the plugin install and usage instructions.
4. Apply the global file-safety and overwrite-approval model: for every existing file the preview would overwrite (e.g. when refreshing `plugin/aos-factory/`), list it explicitly and flag it as an overwrite. Never silently overwrite (Section 28).
5. Present the full preview (files to create, files to overwrite, manifest version) and answer any user questions.
6. Wait for the user to type exactly: Proceed — to authorize plugin generation. This gate authorizes only writing the plugin directory; it does not authorize the local-load test (Section 36.4), zip packaging (step 10), or marketplace publishing (step 11). Each of those is a separate, action-specific approval (Section 2.5).
7. Only after that exact instruction, write the plugin files. If the framework changed since the last packaging, set `plugin.json` version to the framework `spec_version` it was generated from (never an independent bump; design spec Section 14.1) and add a `/builder-changelog.md` entry.
8. Validate the generated plugin against Section 28.2 and the QA checks in Sections 27 and 34: confirm `.claude-plugin/plugin.json` is present and well-formed, every builder maps to a `skills/build-*/SKILL.md`, each `SKILL.md` frontmatter has `name` and `description`, and any in-skill file references resolve.
9. Local-load test (verification gate). Before any packaging or publishing, run the local-load test in Section 36.4 against the written plugin directory. If it does not load cleanly or a builder skill is not invocable, fix the plugin and re-run; do not proceed to packaging until it passes. The local-load test is read-only and creates no files, so it needs no Proceed.
10. Zip packaging (separate gate). Only after the local-load test passes:
   10.1 Confirm the toolchain prerequisite: Claude Code v2.1.128 or later is required to load a plugin from a .zip (Section 28.2 step 6).
   10.2 Present the exact archive command and output path, writing nothing — create `aos-factory-<version>.zip` (where `<version>` is the `plugin.json` version, i.e. the framework `spec_version`) as a zip of the `plugin/aos-factory/` directory so that `.claude-plugin/plugin.json` sits at the archive's expected root.
   10.3 Wait for the user to type exactly: Proceed — to authorize writing the archive. This approval is specific to creating this one archive and does not authorize publishing.
   10.4 After Proceed, create the .zip and report its path and size. Overwriting an existing same-named archive requires a fresh Proceed, flagged as an overwrite (Section 3.2).
11. Marketplace publishing (separate gate). Publishing is a Section 3.2 approval-required action ("Publish content") and pushes to an external host, so it always requires its own Proceed and is never bundled with the steps above:
   11.1 Sync the version: the plugin version always equals the `spec_version` of the design specification the framework was generated from (design spec Sections 14.1, 14.2; step 3.1) — it is never assigned independently. A framework change can only originate in a `spec_version` increment, so set `plugin.json` to that `spec_version` and add a matching `/builder-changelog.md` entry (step 7; Section 28.2 step 8), keeping the plugin-root changelog in sync with the framework changelog.
   11.2 Create or update `.claude-plugin/marketplace.json` listing the plugin (at minimum a name and source). URL-based marketplaces must reference external sources (GitHub, npm, or git URLs); use a Git-based marketplace for plugins referenced by relative path (Section 28.2 step 7).
   11.3 Notify the user that the project is ready to be published to Github. Instructed the user to tag, stage, commit, merge and push the changes to Github.

Do not add, modify, or delete any plugin files, write any distribution archive, or publish to any marketplace unless the user types exactly: Proceed — for that specific action. Each gate (plugin write, zip packaging, marketplace publish) is approved separately (Section 2.5); the local-load test in Section 36.4 is read-only and ungated.
```

### 36.4 Plugin Local-Load Test

When the user requests to "Test the plugin" or "Local-load test the plugin", or as the verification gate in Section 36.3 step 9. This is a manual, read-only check that the packaged plugin loads and its builders are invocable before any zip packaging (Section 36.3 step 10) or marketplace publishing (Section 36.3 step 11). It creates, modifies, deletes, and publishes nothing, so it requires no Proceed.

```
Precondition: the plugin directory exists at the target path (default `plugin/aos-factory/`), written under Section 36.3. Claude Code must be installed (v2.1.128 or later if loading from a .zip; Section 28.2 step 6).

1. Load the plugin without installing it, pointing Claude Code at the plugin directory:
   claude --plugin-dir plugin/aos-factory
   (To test the packaged archive instead, unzip `aos-factory-<version>.zip` and load its contents; loading a .zip requires Claude Code v2.1.128+.)
2. Confirm the plugin is recognized: it loads with no manifest errors and its builder skills are listed — one `build-aos` skill plus one `build-[agent]-agent` skill per roster agent (17 total).
3. Smoke-test invocation in a scratch AOS Workspace (not a real instance):
   3.1 Trigger the master builder (e.g. ask to "set up my AOS") and confirm `build-aos` activates and begins its interview without writing files.
   3.2 Trigger one agent builder (e.g. "Build the Research Agent") and confirm `build-research-agent` activates and produces its dry-run / pre-build preview.
   3.3 Confirm no files are created — every builder must stop at the Proceed gate (design spec Sections 9.1, 28).
4. Confirm the shipped example workspace-root templates resolve: `templates/aos-router.md` and `templates/CLAUDE.md` exist, and `CLAUDE.md` imports `AGENTS.md` as intended.
5. Record the result. On success, the plugin is cleared for packaging (Section 36.3 step 10). On failure, report the error, fix the plugin under Section 36.3 (re-running its Proceed-gated write if files must change), and re-run this test.

This test does not add, modify, delete, or publish any files; no Proceed is required to run it.
```

