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
# Add your instance names here once you build them, e.g.:
#  - work-aos
#  - personal-aos
---

# AOS Instance Router

Read this BEFORE loading any target. This workspace contains the **factory
framework** (`aos-factory/`, which builds and maintains instances) and any
**instances** you have created (e.g. `work-aos`, `personal-aos`). Exactly one
target is active per request. This file decides which.

> **New workspace?** No instances exist yet — all requests route to `aos-factory`
> by default. The `build-aos` builder updates this file automatically when it
> creates a new instance — adding the slug to `applies_to` and populating §2
> with the instance's routing signals. No manual editing required.

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

> **Fill this section in** after building your instances. The examples below
> are illustrative; replace them with your actual instance names and signals.

- **Factory/framework signals:** build/set-up/create an AOS; install or refresh
  the factory; add or modify a builder or agent definition; edits under
  `aos-factory/` or `/builders/`; references to `build-*.md`;
  schema/builder maintenance. The factory operates
  *on* instances but is not itself an instance.
- **Default instance:** _(set to your primary instance slug once built, e.g. `work-aos`)_
- **Instance A signals:** _(e.g. work-related requests, client names, work
  project names, work email aliases)_
- **Instance B signals:** _(e.g. personal requests, family/friends, personal
  project names, personal email aliases)_
- **Shared inbox note:** If one inbox feeds multiple instances, route on
  sender, alias, and request intent — not on the mere presence of email.

## 3. Confidence bar
- Act automatically only when one side has clear signals AND the other has
  none. Mixed or weak signals → fall through to §1.5 (ASK).
- Factory vs. instance is usually unambiguous (build/install verbs vs.
  run-a-workflow verbs). Ambiguous cases fall through to ASK.
- Cross-instance requests ("brief me on everything") → run each instance
  separately and label the output by instance; never blend their memory.

## 4. Session pin
- "Use [instance-name] for now" or "switch to [instance-name]" sets the pin
  for the session.
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
