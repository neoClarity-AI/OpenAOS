---
title: AOS Instance Router
file_type: aos_router
schema_version: 1.0.0
builder_version: 1.0.0
created_date: 2026-06-05
last_updated: 2026-06-05
status: active
applies_to:
  - aos-factory
  - work-aos
  - personal-aos
---

# AOS Instance Router

Read this BEFORE loading any target. AOS-03 contains the **factory framework**
(`aos-factory/`, which builds and maintains instances) and two **instances**
(`work-aos`, `personal-aos`). Exactly one target is active per request. This
file decides which, and is owned jointly by the two Chief of Staff agents.

## 1. Resolution order (stop at the first that applies)
1. **Explicit user override** — the user names a target ("in work-aos…",
   "personal brief", "in the factory", "the builder"). Use it.
2. **Framework vs. instance** — if the request is to build, install, validate,
   refresh, or edit the AOS framework itself (the factory or its builders),
   route to `aos-factory` and skip instance resolution. The factory is a
   framework, not an instance; do not run instance signal-matching for it.
3. **Session pin** — if the user has set an active target this session
   (see §4), use it until they change or clear it.
4. **Signal match** — classify from the request signals in §2. Use a side
   only if it wins by the confidence bar in §3.
5. **Fallback: ASK.** If none of the above resolves it, ask the user which
   target to use. Do NOT silently pick, and do NOT merge instances.

## 2. Classification signals
- **Factory/framework signals:** build/set-up/create an AOS; install or refresh
  the factory; add or modify a builder or agent definition; edits under
  `aos-factory/` or `/builders/`; references to `build-*.md`;
  schema/builder maintenance. The factory operates
  *on* instances but is not itself an instance.
- **Default instance:** `work-aos`.
- **Work signals:** requests mentioning clients, the company, billing,
  hiring, work projects in `work-aos/projects`, or recipients/aliases tied
  to work.
- **Personal signals:** family/friends (e.g. dan@danner.org threads),
  personal admin, community/newsletter aliases (m25@, m26+*, martin+*),
  personal projects in `personal-aos/projects`.
- **Shared inbox note:** martin@neoclarity.ai feeds BOTH instances, so inbox
  alone is not a routing signal. Route on sender/alias and request intent,
  not on the fact that mail exists.

## 3. Confidence bar
- Act automatically only when one side has clear signals AND the other has
  none. Mixed or weak signals → fall through to §1.5 (ASK).
- Factory vs. instance is usually unambiguous (build/install verbs vs.
  run-a-workflow verbs). Ambiguous cases — e.g. "add a finance agent" could
  mean build the agent (factory) or a work task (instance) — fall through to ASK.
- Cross-instance requests ("brief me on everything") → run each instance
  separately and label the output by instance; never blend their memory.

## 4. Session pin
- "Use work-aos for now" or "switch to personal" sets the pin for the session.
- "Work in the factory" / "switch to the builder" pins `aos-factory`.
- "Clear AOS" or "ask me each time" removes the pin.
- State the active target in the first line of any brief or routed output
  (e.g. "**[work-aos]** Daily Brief — …" or "**[aos-factory]** …").

## 5. Logging
- Instance routing → record each non-trivial choice (chosen instance, trigger,
  default vs. asked) to the active instance's
  `agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md`.
- Factory routing → record to `aos-factory/logs/factory-routing-decision-log.md`
  (the factory has no Chief of Staff).
