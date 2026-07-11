---
title: Review Agent — Agent Interviews
file_type: interview_script
slug: review-agent
spec_version: 2.2.0
---
# Review Agent — Interviews

## Initialization Interview

```yaml
- id: review-timing
  ask: Preferred timing for the weekly, monthly, and quarterly reviews?
  type: text
  default: standard cadence (§25) at the user's first convenient slot
  skippable: yes
  when: always
  captures: review-config.md cadence settings

- id: audit-focus
  ask: Any areas you especially want audited (memory, permissions, structure)?
  type: text
  default: balanced coverage per §27
  skippable: yes
  when: always
  captures: review-config.md audit focus areas
```

## Update Interview

No questions — no migration required at this release.
