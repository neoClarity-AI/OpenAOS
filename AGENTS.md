# Agent Instructions

These instructions apply to any AI coding agent working in this repository
(Claude, Codex, Cursor, Aider, etc.).

## Planning mode

When the user prompts "Planning mode", "P mode", or "pmode": do not create,
edit, or delete any file unless the user prompts "Proceed". Planning mode means
the session is for discussing and designing changes to the agent — not
implementing them. Always display proposed changes to the user and ask to proceed.

## Instance routing

Read `/aos-router.md` and resolve the active instance before running any workflow.

## Contributing

All changes flow through the design spec first. See [CONTRIBUTING.md](CONTRIBUTING.md) —
only pull requests for `design-spec/aos-factory-design-specification.md` are considered.
