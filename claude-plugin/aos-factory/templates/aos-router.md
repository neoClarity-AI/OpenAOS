---
title: AOS Instance Router
file_type: aos_router
spec_version: 2.1.3
---
# AOS Instance Router

Read this BEFORE loading any target. This workspace contains the **factory
framework** (installed as the `aos-factory` plugin, which builds and maintains
instances) and any **instances** you have created (e.g. `work-aos`,
`personal-aos`). Exactly one target is active per request. This file decides
which.

> **New workspace?** No instances exist yet — factory/framework requests route to
> the `aos-factory` builders by default. The `build-aos` skill updates this file
> automatically when it creates a new instance — adding the instance to the
> Registered Targets table below. No manual editing required.

## Resolution Order      (stop at the first tier that applies)

1. **Explicit user override** — the user names a target, or opens the prompt
   with a registered call name. A call-name match is case-insensitive and only
   at the start of the prompt (a leading greeting and/or trailing comma is
   handled gracefully; a mid-sentence mention is not a trigger). Addressing by
   call name also sets the session pin, same as "switch to <instance-name>".
2. **Framework vs. instance** — if the request is to build, install, validate,
   refresh, or edit the AOS framework itself (the factory or its builders),
   route to the factory and skip instance resolution. A call-name match is the
   highest tier but does **not** override this check: a prompt that both opens
   with a call name and is unambiguously factory work is AMBIGUOUS — ask, or
   note the routing choice; never silently route.
3. **Session pin** — if the user has set an active target this session (see
   Session Pin), use it until they change or clear it.
4. **Signal match** — classify from the request signals in the registry. Use a
   side only if it wins clearly (clear signals on one side, none on the other).
5. **Fallback: ASK.** If none of the above resolves it, ask the user which
   target to use. Do NOT silently pick, and do NOT merge instances.

## Registered Targets

The registry is the single source of truth for call names and routing signals.
A call name is unique within this table; it is optional (an instance without one
is routed by the other tiers). Fill in each instance's row as it is built.

| Target | Type | Call name | Folder | Signals |
|---|---|---|---|---|
| aos-factory | framework | factory | (plugin) | build/set-up/create an AOS; install or refresh the factory; add or modify a builder or agent definition; references to the `build-aos` / `build-agent` skills; schema/builder maintenance |
| _work-aos_ | _instance_ | _work_ | _/work-aos_ | _(e.g. work requests, client names, work project names, work email aliases)_ |
| _personal-aos_ | _instance_ | _home_ | _/personal-aos_ | _(e.g. personal requests, family/friends, personal project names, personal email aliases)_ |

> The italic rows above are illustrative examples — replace them with your
> actual instances once built (the `build-aos` skill does this automatically),
> or delete them.

## Session Pin

- "Use [target] for now" or "switch to [target]" sets the pin for the session;
  addressing a target by its registered call name does the same.
- "Work in the factory" / "switch to the builder" pins the factory.
- "Clear AOS" or "ask me each time" removes the pin.
- State the active target on the first line of any brief or routed output
  (e.g. "**[work-aos]** Daily Brief — …" or "**[aos-factory]** …").

## Logging

- Instance routing → record each non-trivial choice (chosen target, trigger,
  default vs. asked) to the active instance's
  `agents/chief-of-staff-agent/logs/chief-of-staff-decision-log.md` (§17.1/§19.3).
- Cross-instance requests ("brief me on everything") → run each instance
  separately and label the output by instance; never blend their memory.
