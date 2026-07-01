---
title: Build AOS (Entry)
file_type: builder_entry
spec_version: 1.1.0
created_date: 2026-06-03
last_updated: 2026-06-25
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build AOS (Entry)

This is a short entry pointer. The full AOS instance builder lives at:

```text
/builders/build-aos.md
```

When the user asks to build, set up, or create their AOS, open `/builders/build-aos.md` and run its interview and setup sequence from there. This entry file intentionally contains no build logic of its own — it exists so the user can start a build from the framework root.

Note: this file does not build or maintain the framework itself. The factory framework is generated once from the design specification and distributed as a Claude plugin; maintaining it is a manual, approval-gated operation (see design spec Section 28).
