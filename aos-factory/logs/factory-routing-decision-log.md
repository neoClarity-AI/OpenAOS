---
title: Factory Routing Decision Log
file_type: decision_log
spec_version: 1.0.5
created_date: 2026-06-05
last_updated: 2026-06-11
status: active
applies_to:
  - aos-factory
---

# Factory Routing Decision Log

Append one row per non-trivial routing choice that resolved to `aos-factory`
(per `/aos-router.md` §5). Columns: date, request summary, trigger
(override / framework-match / pin / asked), notes.

| Date | Request | Trigger | Notes |
| ---- | ------- | ------- | ----- |
| 2026-06-05 | Update builder files for the routing change (formalize not-yet-done items) | framework-match | Edited design spec §15.4/§7.4/§10.3/§17.1 and builders build-aos / build-chief-of-staff-agent. |
| 2026-06-05 | Instance-sync pass propagating router changes into work-aos and personal-aos | framework-match | Updated both instances' daily-startup workflow, chief-of-staff agent def, agent-registry, and user-profile routing signals. |
| 2026-06-05 | Eliminate install-aos-factory.md; add factory-generation + plugin-packaging instructions | framework-match | Removed installer from design spec (§8, §12.2, §15.4, §28, §34/§35) and builder/router refs; reframed §28 as Distribution and added §28.1 (generate factory) and §28.2 (package as Claude plugin). |
