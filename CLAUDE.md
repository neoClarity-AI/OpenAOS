## Planning mode rules

- Planning mode is active when the user's message begins with "Planning mode" or "pmode".
- While in planning mode:
  - Claude must always show it's reasoning
  - Claude should offer options and a recommendation when an issue is identified
  - Claude must NOT create, edit, rename, move, or delete any files.
  - Claude may only read files, research, and present a proposed plan.
  - Claude must wait for the user to type exactly: Proceed — before making any changes.

- Refining, adjusting, or approving a plan in conversation is NOT a "Proceed". Only the exact word counts.

## Commonly used files and folders

"design spec" = "/design-spec/aos-factory-design-specification.md"
"runbook" = "/design-spec/aos-factory-generation-runbook.md"
"feature-specs" = "/internal-only/feature-specs"

## Include the standard AGENTS.md file

@AGENTS.md
