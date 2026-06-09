---
title: Builder Changelog
file_type: builder_changelog
builder_version: 1.0.0
schema_version: 1.0.0
last_updated: 2026-06-08
status: active
---

# Builder Changelog

Tracks changes to the reusable AOS Factory framework (and the plugin version it
is distributed as). Instance-level changes belong in each instance's
`/logs/change-log.md`, not here.

## 1.0.0 — 2026-06-08
- Initial plugin packaging of the AOS Factory.
- 17 builder skills: `build-aos` plus one builder per agent in the roster
  (4 required governance agents, 12 optional productive agents).
- Ships example workspace-root files under `examples/` (`aos-router.md`,
  `claude.md`).
- No runtime installer; the factory is generated from the design spec and
  distributed via this plugin.
