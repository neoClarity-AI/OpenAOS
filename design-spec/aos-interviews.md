---
title: AOS Setup — Interviews
file_type: interview_script
slug: build-aos
spec_version: 2.1.3
---
# AOS Setup — Interviews

The AOS-level setup interview, owned by `build-aos.md` (§12.1) and executed
during initial AOS setup (§9.3). Schema and execution rules: §7C.

## Initialization Interview

```yaml
- id: aos-purpose
  ask: What is this AOS for (work, personal, or a specific purpose)?
  type: text
  default: none
  skippable: no
  when: always
  captures: scope; proposed instance name; /aos-manifest.md

- id: aos-name
  ask: What should the AOS be named?
  type: text
  default: proposed from the stated purpose (file-safe slug, §29)
  skippable: yes
  when: always
  captures: instance root folder slug; /aos-manifest.md; router registry row

- id: optional-agents
  ask: Which optional productive agents do you want first? At least one is required (§2.3, §7.2); the rest can be added later (§9.4).
  type: text
  default: none — recommend Inbox + Task + Calendar for a productivity AOS, or Research + Writing for a knowledge-work AOS
  skippable: no
  when: always
  captures: agent selection; /configs/agent-registry.md; /aos-map.md

- id: memory-seeds
  ask: Any known people, projects, tools, or preferences to seed memory with?
  type: text
  default: none — seed empty, never fabricate
  skippable: yes
  when: always
  captures: /memory global files initial entries

- id: autonomy-baseline
  ask: How much autonomy do you want by default, and where should approval always be required beyond the global rules (§3)?
  type: text
  default: the §3 model unchanged
  skippable: yes
  when: always
  captures: /configs/global-permissions.md

- id: call-name
  ask: Would you like a call name for this instance — a single word (dog names suggested, e.g. "Lassie") you can say at the start of a prompt to route straight to it?
  type: text
  default: none — skipping means the instance has no call name; routing uses the other resolution tiers
  skippable: yes
  when: always
  captures: /aos-router.md registry Call name column
```

Call-name rules (F4): the name must be unique within the router's registry —
if the requested name is already registered, the builder rejects it and
suggests unused alternatives. Dog names are the suggested default framing (a
dog name presents the instance as a smart, trainable tool rather than a
person); any single-word name is accepted, with guidance to avoid
human-sounding names, which invite over-trust. No name is reserved for
instances that have not been built.

## Update Interview

No questions — no migration required at this release.
