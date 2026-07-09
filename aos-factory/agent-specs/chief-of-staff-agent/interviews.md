---
title: Chief of Staff Agent — Agent Interviews
file_type: interview_script
slug: chief-of-staff-agent
spec_version: 2.1.1
---
# Chief of Staff Agent — Interviews

## Initialization Interview

```yaml
- id: priority-rules
  ask: What are your default prioritization rules?
  type: text
  default: no standing rules — escalate the first conflict and capture the ruling as a preference
  skippable: yes
  when: always
  captures: chief-of-staff memory (priority rules); /memory/preferences.md when global

- id: router-weak-signals
  ask: When routing signals are weak, should the router pick the default instance or always ask?
  type: choice
  options: [always ask, use default instance]
  default: always ask
  skippable: yes
  when: always
  captures: /aos-router.md Ask-Don't-Guess behavior noted in chief-of-staff config

- id: coordination-preferences
  ask: Any standing coordination preferences (e.g. how much to route vs. handle directly)?
  type: text
  default: push work down to specialized agents; coordinate rather than perform (§2.2, §7.6)
  skippable: yes
  when: always
  captures: chief-of-staff-config.md coordination notes
```

## Update Interview

No questions — no migration required at this release.
