# AOS Factory (Claude Plugin)

The **AOS Factory** stands up a complete **Agentic Operating System (AOS)** inside
a Claude workspace: the required governance agents, the productive agents you
choose, plus the workflows, templates, configs, logs, and a User Guide that make
them work together. It can also add or rebuild a single agent later.

This plugin is a **rendering** of the AOS Factory design specification
(`spec_version` 2.2.2). The specification is the single source of truth; the
builders, skills, and templates here are generated from it.

## What's inside

- **`skills/build-aos/`** — the master builder. Runs the interactive setup
  interview, creates the instance folder tree and global files, provisions the
  workspace root, builds the required governance agents and your selected
  optional agents, and writes a setup summary.
- **`skills/build-agent/`** — the generic build engine. Builds any one approved
  agent from its catalog entry, profile, and interview script — used during
  initial setup and to add an optional agent later.
- **`templates/aos-router.md`** and **`templates/CLAUDE.md`** — example
  workspace-root files you copy to your AOS Workspace root after install.
- **`builder-changelog.md`** — framework-file and packaging change history.

## Install

1. Add the marketplace that publishes this plugin, then install `aos-factory`
   from it (the repo's `.claude-plugin/marketplace.json` points at this
   directory as the plugin `source`).
2. After installing, copy the two example files from `templates/` into your AOS
   Workspace root:
   - `templates/aos-router.md` → `/aos-router.md`
   - `templates/CLAUDE.md` → `/CLAUDE.md`
   The `build-aos` skill will also create these for you (non-destructively) on
   first build if they are absent.

## Usage

Ask Claude to build an AOS and the `build-aos` skill takes over:

> "Set up a new AOS for my consulting work."

It runs the setup interview, previews everything it will create, and waits for you
to type exactly `Proceed` before writing any files. To add one agent to an
existing instance, the `build-agent` engine handles it:

> "Build the Research Agent."

### Safety model

Every builder defaults to **dry-run / preview** and gates file creation behind the
exact string `Proceed`. Approval is action-specific: each `Proceed` authorizes
only the action described immediately before it. Existing files are never
overwritten, moved, renamed, or deleted without a separate `Proceed`.

## Versioning

The plugin version tracks the framework `spec_version` and the
`builder-changelog.md`. This release is **2.2.2**.

## Contributing

The repository accepts pull requests **only against the design specification**.
The prebuilt factory and this plugin are regenerated and published from the
approved spec, so every released artifact traces back to a reviewed design. To
change the official factory or plugin, change the spec.

## License

MIT © neoClarity
