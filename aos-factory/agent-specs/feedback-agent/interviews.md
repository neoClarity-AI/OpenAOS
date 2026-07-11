---
title: Feedback Agent — Agent Interviews
file_type: interview_script
slug: feedback-agent
spec_version: 2.2.0
---
# Feedback Agent — Interviews

## Initialization Interview

```yaml
- id: email-capability
  ask: Is an email capability configured for this AOS that can send to aos-factory@neoclarity.ai?
  type: boolean
  default: no — submissions stay staged in the feedback log and you are prompted to send manually
  skippable: yes
  when: always
  captures: feedback-config.md transport note; tool-access-matrix.md Email send row (Approval-required)

- id: candidate-presentation
  ask: At which reviews should enhancement candidates be presented — monthly and quarterly (standard), or quarterly only?
  type: choice
  options: [monthly and quarterly, quarterly only]
  default: monthly and quarterly
  skippable: yes
  when: always
  captures: feedback-config.md self-examination rhythm (§17.4–17.5)
```

## Update Interview

No questions — no migration required at this release.
