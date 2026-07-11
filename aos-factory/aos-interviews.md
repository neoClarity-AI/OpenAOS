---
title: AOS Setup — Interviews
file_type: interview_script
slug: build-aos
spec_version: 2.1.4
---
# AOS Setup — Interviews

The AOS-level setup interview, owned by `build-aos.md` (§12.1) and executed
during initial AOS setup (§9.3). Schema and execution rules: §7C.

## Initialization Interview

```yaml
- id: aos-purpose
  ask: What is this AOS for?
  type: choice
  options: [Personal Productivity, Project Management, Client Specific, Other]
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
  default: recommend by the stated aos-purpose category — Inbox + Task + Calendar + Document for Personal Productivity, Project Manager + Task + Document for Project Management, Personal CRM + Task + Calendar for Client Specific; for Other, present the full §7.2 roster with no default
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

- id: call-name
  ask: Would you like a call name for this instance — a single word (dog names suggested, e.g. "Lassie") you can say at the start of a prompt to route straight to it?
  type: text
  default: none — skipping means the instance has no call name; routing uses the other resolution tiers
  skippable: yes
  when: always
  captures: /aos-router.md registry Call name column
```

Purpose categories: Personal Productivity merges the former separate "work"
and "personal" answers, since neither carried distinct downstream behavior. If
the user selects Other, capture a short free-text description alongside it —
that description substitutes for the category name wherever purpose feeds
`aos-name`'s default slug (§29) and the /aos-manifest.md scope field.

Call-name rules (F4): the name must be unique within the router's registry —
if the requested name is already registered, the builder rejects it and
suggests unused alternatives. Dog names are the suggested default framing (a
dog name presents the instance as a smart, trainable tool rather than a
person); any single-word name is accepted, with guidance to avoid
human-sounding names, which invite over-trust. No name is reserved for
instances that have not been built.

## Update Interview

No questions — no migration required at this release.
