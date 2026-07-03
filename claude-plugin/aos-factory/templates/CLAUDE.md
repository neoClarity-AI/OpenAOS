## Planning Mode Rules

- Planning mode is active when the user's message begins with "Planning mode" or "pmode".
- In planning mode, Claude must NOT create, edit, rename, move, or delete any files.
- Claude may only read files, research, and present a proposed plan.
- Claude must wait for the user to type exactly: Proceed — before making any changes.
- Refining, adjusting, or approving a plan in conversation is NOT a "Proceed". Only the exact word counts.

## Planning mode

When the user prompts "Planning mode", "P mode", or "pmode": do not create,
edit, or delete any file unless the user prompts "Proceed". Planning mode means
the session is for discussing and designing changes to the agent — not
implementing them. Always display proposed changes to the user and ask to proceed.

## Include the standard AGENTS.md file

@AGENTS.md
