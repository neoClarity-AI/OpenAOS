---
title: Build AOS — Entry Pointer
file_type: builder_entry
spec_version: 2.0.0
created_date: 2026-07-01
last_updated: 2026-07-01
status: active
compatible_aos_versions:
  - 1.x
requires_approval_for_overwrite: true
---

# Build AOS

This is the root entry pointer for the AOS Factory. It does not contain the
build logic itself; it points to the master builder.

To build a new AOS instance, run the master builder:

```text
/builders/build-aos.md
```

The master builder runs the interactive setup interview and, on `Proceed`,
creates a complete AOS instance as a sibling folder inside the AOS Workspace
(Section 4.1). This root pointer exists so that the framework has a single,
obvious starting point; all build behavior is defined in `/builders/build-aos.md`
(file_type `aos_builder`) and the per-agent builders in `/builders/`.

To add a single optional agent to an existing instance later, run that agent's
builder directly, for example:

```text
/builders/build-research-agent.md
```

## Safety

No files are created until the user types exactly `Proceed` (Section 3.1). All
builders default to dry-run / preview and gate every file overwrite or refresh
behind a separate `Proceed` (Sections 28, 35.1).
