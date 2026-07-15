---
title: AOS Factory Generation Runbook
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 2.3.3
created_date: 2026-06-02
last_updated: 2026-07-14
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
- No user-specific AOS instance may be generated during the framework build
  phase; instance generation happens only if the user separately requests it
  after the Builder framework exists.
- No existing file may be overwritten without explicit user approval.
- Any actual generation action requires the user to type exactly `Proceed`.
- Refreshing, replacing, or overwriting existing builder files requires a
  separate `Proceed` approval.
- Deleting, renaming, moving, archiving, publishing, sending, spending, or
  sharing private information requires explicit user approval.
```

Operational gates derived from these rules — the contradiction/gap check,
ready-to-generate checklist, builder generation scope, framework-only build,
and the exact `Proceed` approval — are enforced in Sections 34 and 35.

---

# 34. Design Completion Checklist

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

# 35. AOS Factory Generation

## 35.1 Generation Rules

When generating an AOS Factory instance, you must follow these rules.

- Generate AOS Factory framework files only.
- Do not generate a user-specific AOS instance yet.
- Include root build entry file.
- Include /builders folder files.
- Include builder changelog.
- Include the generic agent build engine (`build-agent.md`), which builds every approved agent from its design artifacts (design spec Sections 8, 12).
- Include dry-run / preview mode in all builders.
- Include approval gates before any file overwrite or refresh.
- Render factory-root copies of `agent-catalog.yaml`, `agent-specs/[agent-name]-agent/` (profile.md + interviews.md per agent), and `aos-interviews.md` from the design-spec sources (design spec Sections 7A.4, 7B.2, 7C.2); they are read-only inside instances.
- Stamp every generated file's frontmatter with the `spec_version` it was rendered from (design spec Sections 14.1–14.2, 15.1). Do not emit `builder_version` or `schema_version`; those have been collapsed into `spec_version`.

## 35.2 Generation Scope

The generation phase creates the AOS Factory framework files listed below.

No AOS instance should be generated in this first generation phase unless the user separately requests that after the Builder framework exists.

```text
/build-aos.md
/builder-changelog.md
/agent-catalog.yaml
/agent-specs/[agent-name]-agent/profile.md      (one per Section 7.3 agent — 15 folders)
/agent-specs/[agent-name]-agent/interviews.md   (one per Section 7.3 agent)
/aos-interviews.md
/builders/build-aos.md
/builders/build-agent.md                        (generic engine — replaces the former 14 per-agent builders)
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
   1.2 In Section "34. Design Completion Checklist", mark every checklist item as Not Done. (Replace [x] with [ ]).
2. Conduct a completeness check by verifying each item in the "34. Design Completion Checklist". When an item has been verified, mark it as Done (Replace [ ] with [x]). Report any missing items and recommended actions. Repeat this step until you have marked all items Done.
3. Conduct a safety check by verifying the design complies with each safety-related governance rule in Section 33. Report any safety issues and recommended actions.
4. Review the design in "aos-factory-design-specification.md" for logical consistency. Report any inconsistencies to the user. Include only inconsistencies that impact the functionality of the factory it generates. If no such inconsistencies exist then inform the user and add a revision-history entry noting the review found no inconsistencies, logged at the current `spec_version` (no increment — Section 14, revision history rule). Otherwise, work with the user to resolve each issue one at a time. For each issue, offer the user options and a recommendation.
5. When all inconsistencies are resolved, present the consolidated resolutions and wait for the user to type exactly: Proceed — to finalize the consistency review. This gate authorizes only finalization of the review and update of the spec, not the generation of AOS Factory files. Finalizing increments `spec_version` and adds the consolidated revision-history entry.
6. Repeat steps 1 and 2 until no more issues are surfaced.

Do not add, modify or delete any files unless the user types exactly: Proceed.
```
### 36.2 AOS Factory Generation

When the user requests to "Build the factory" or "Rebuild the factory" or "Generate the factory" or "Regenerate the factory", using this workflow.

```
Read the source file `design-spec/aos-factory-design-specification.md`.
1. Verify that all items in the "34. Design Completion Checklist" are marked Done ([x]). If any items are not Done, notify the user and stop this workflow.
2. Verify the design complies with the safety-related governance rules in Section 33. If any are not satisfied, notify the user and stop this workflow.
3. Review the proposed Builder generation scope (Section 35) and plan with the user.
4. Answer any additional user questions about the design or generation plan.
5. Wait for the user to type exactly: Proceed — to authorize generation.
6. Only after that exact instruction, generate the AOS Factory framework files. Add a revision-history entry for this generation cycle. If the generated output differs from the prior generation, increment `spec_version`; if it is a no-op regeneration (no diff), log the entry at the current `spec_version` (no increment — Section 14, revision history rule).

Do not generate actual AOS Factory files unless the user types exactly: Proceed.
```

### 36.3 Claude Plugin Generation

When the user requests to "Build the plugin" or "Generate the plugin", using this workflow.

```
Read the source file `design-spec/aos-factory-design-specification.md` (Section 28) and the generated framework files from Section 36.2.
1. Verify the precondition: the generated AOS Factory framework files from Section 35.2 exist — the root entry `/build-aos.md`, all `/builders/build-*.md`, and `/builder-changelog.md`. If any are missing, notify the user that the factory must be generated first (Section 36.2) and stop this workflow.
2. Set the target plugin directory (default: refresh the canonical `claude-plugin/aos-factory/`, the path the repo's `.claude-plugin/marketplace.json` publishes as its `source`). Read Section 28.2 for the required plugin layout and packaging steps.
3. Build a dry-run preview — list every file to be created or overwritten, writing nothing:
   3.1 `.claude-plugin/plugin.json` — manifest: name `aos-factory`, version synced to the framework `spec_version` (design spec Section 14.1) and `/builder-changelog.md`, plus description, author, keywords.
   3.2 `skills/build-*/SKILL.md` — one skill per builder. Convert each `/builders/build-*.md` into a `SKILL.md` whose frontmatter carries `name` and an invocation-oriented `description` (when-to-use triggers), with the builder body as the skill content. Map `/builders/build-aos.md` → `skills/build-aos/SKILL.md` and `/builders/build-agent.md` → `skills/build-agent/SKILL.md` (the generic engine; one skill covers every agent). The root `/build-aos.md` entry pointer is a framework-root convenience and is not packaged separately; the `build-aos` skill replaces it in plugin context.
   3.3 `agent-catalog.yaml`, `agent-specs/` (profile.md + interviews.md per agent), and `aos-interviews.md` — copy the rendered design artifacts from the factory root to the plugin root, byte-identical to their factory-root sources, so the installed plugin can run a spec-faithful build (Section 28.2).
   3.4 `builder-changelog.md` — copy the framework `/builder-changelog.md` to the plugin root.
   3.5 `templates/CLAUDE.md` and `templates/AGENTS.md` — author the example workspace-root files the user copies (or build-aos provisions) to their AOS Workspace root after install (Section 28.2).
   3.6 `README.md` — author or refresh the plugin install and usage instructions.
4. Apply the global file-safety and overwrite-approval model: for every existing file the preview would overwrite (e.g. when refreshing `claude-plugin/aos-factory/`), list it explicitly and flag it as an overwrite. Never silently overwrite (Section 28).
5. Present the full preview (files to create, files to overwrite, manifest version) and answer any user questions.
6. Wait for the user to type exactly: Proceed — to authorize plugin generation. This gate authorizes only writing the plugin directory; it does not authorize zipping, local-load testing, or marketplace publishing (those remain manual — Section 28.2 steps 5-8).
7. Only after that exact instruction, write the plugin files. Add a revision-history entry for this packaging cycle. If the framework changed since the last packaging, bump `plugin.json` version (synced to `spec_version`) and add a `/builder-changelog.md` entry; if nothing changed, log the revision-history entry at the current `spec_version` (no increment — Section 14, revision history rule) and do not bump `plugin.json` or add a changelog entry.
8. Validate the generated plugin against Section 28.2 and the QA checks in Sections 27 and 34: confirm `.claude-plugin/plugin.json` is present and well-formed, every builder maps to a `skills/build-*/SKILL.md`, each `SKILL.md` frontmatter has `name` and `description`, any in-skill file references resolve, and the rendered design artifacts (`agent-catalog.yaml`, `agent-specs/` with profile.md + interviews.md for every agent, `aos-interviews.md`) are present at the plugin root and byte-identical to their factory-root sources (an empty diff against the factory root).

Do not add, modify, or delete any plugin files unless the user types exactly: Proceed.
```
