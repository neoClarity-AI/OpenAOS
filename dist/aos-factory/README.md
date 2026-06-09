# AOS Factory (Claude plugin)

Builders that create and maintain Agentic Operating System (AOS) instances.

## Skills

- **build-aos** — master entry point; stands up a complete AOS instance.
- **build-{security,memory,chief-of-staff,review}-agent** — the four required
  governance agents.
- **build-{learning,inbox,calendar,task,project-manager,research,writing,
  document-librarian,personal-crm,finance,health-life-logistics,automation}-agent**
  — optional productive agents (add at least one).

## Usage

Ask Claude to build an AOS, or invoke a builder skill directly. Each builder
defaults to dry-run / preview and creates no files until you type `Proceed`.

## Workspace-root files

`aos-router.md` (instance router) and `claude.md` (project / session-start
instructions) govern selection across instances and the factory. They live at
your workspace root, above any instance. Example copies are in `examples/`;
copy them to your workspace root after install and edit for your setup.

See `builder-changelog.md` for version history.
