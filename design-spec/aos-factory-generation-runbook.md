---
title: AOS Factory Generation Runbook
file_type: design_spec
project: Script to Build Agentic OS Factory
spec_version: 1.0.6
created_date: 2026-06-02
last_updated: 2026-06-10
status: design_ready_for_generation_planning
important_constraint: Do not generate actual AOS Factory files unless the user explicitly types exactly Proceed.
---

# AOS Factory Generation Runbook

Part of the AOS Factory Design Specification document set. The canonical design is in `aos-factory-design-specification.md` (Sections 1-32); this file holds the build, generation-scope, and handoff procedure (Sections 33-37). Section numbering is preserved from the specification so cross-references continue to resolve. The `Proceed` safety gate applies in full: no AOS Factory files are generated until the user types exactly `Proceed`.

---

# 33. Final Consolidation Decisions

The user accepted final consolidation recommendations.

Approved consolidation defaults:

```text
- Treat Part 4 as the authoritative design handoff.
- Preserve all completed decisions unless the user explicitly modifies them.
- Reconcile older sections with later addenda where Part 4 decisions supersede earlier open statuses.
- Do not rewrite the full design spec unless the user asks for a cleaned consolidated version.
- Produce a compact contradiction and gap check before builder generation.
- Produce a ready-to-generate checklist.
- Produce a proposed builder generation scope.
- Require the user to type exactly Proceed before creating any actual AOS Factory files.
- Do not generate a user-specific AOS instance during the first generation phase.
- Generate only the reusable AOS Factory framework when authorized.
- Treat the Agent Maker Agent reference as a design note, not as authorization to add a new agent to the initial roster.
```

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
[x] No builder files have been generated yet.
[x] No user-specific AOS instance will be generated yet.
[x] No existing files will be overwritten without explicit approval.
[x] Any actual generation action requires the user to type exactly: Proceed.
[x] Refreshing, replacing, or overwriting existing builder files requires a separate Proceed approval.
[x] Deleting, renaming, moving, archiving, publishing, sending, spending, or sharing private information requires explicit approval.
```

## 

```text

```

---

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

### Workflow 1 — Design Readiness Review

When the user requests a "Design Readiness Review", using this workflow.

```text
Read the source file `design-spec/aos-factory-design-specification.md`.
1. Verify with the user that we are entering a Design Readiness Review. When the user types "Proceed", do the following:
   1.1 Update all design specs with the status of "in_review".
   1.2 In Section "34. Ready-to-Generate Checklists", mark every checklist item as Not Done. (Replace [x] with [ ]).
2. Conduct a completeness check by verifying each item in the "34.1 Design Completion Checklist". When an item has been verified, mark it as Done (Replace [ ] with [x]). Report any missing items and recommended actions. Repeat this step until all items are marked Done.
3. Conduct a safety check by verifying each item in the "34.3 Generation Scope Checklist". Report any safety issues and recommended actions.
4. Review the design in "aos-factory-design-specification.md" for logical consistency. Report any inconsistencies to the user. Include only inconsistencies that impact the functionality of the factory it generates. If no such inconsistencies exist then inform the user. Otherwise, work with the user to resolve each issue one at a time. For each issue, offer the user options and a recommendation.
5. When all inconsistencies are resolved, present the consolidated resolutions and wait for the user to type exactly: Proceed — to finalize the consistency review. This gate authorizes only finalization of the review and update of the spec, not the generation of AOS Factory files.
6. Repeat steps 1 and 2 until no more issues are surfaced.

Do not add, modify or delete any files unless the user types exactly: Proceed.
```
### Workflow 2 — AOS Factory Generation

When the user requests to "Build the factory", using this workflow.

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

