---
title: Build AOS — Entry Pointer
file_type: builder_entry
spec_version: 2.1.1
created_date: 2026-07-06
last_updated: 2026-07-09
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---
# Build AOS — Entry Pointer

This is the AOS Factory root entry file (§8.3). It is a short pointer only; it
does not repeat the builder schema.

To build a new AOS instance, use the master builder:

```text
/builders/build-aos.md
```

The master builder runs the interactive setup interview (`aos-interviews.md`,
§7C/§12.1) and builds a complete AOS instance as a sibling folder within the AOS
Workspace (§4.1). To install a single agent into an existing instance later, use
the generic build engine `/builders/build-agent.md` (§9.4).

All file creation is preview-first and gated behind the user typing exactly
`Proceed` (§3.1, §9.1). This factory generates framework files and AOS instances
only; it never generates a user-specific instance during the framework build
phase (§35.1).
