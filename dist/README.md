# AOS Factory — Plugin Distribution

This repo is a **Claude plugin marketplace** containing the **AOS Factory** plugin.

```
dist/
  .claude-plugin/marketplace.json   marketplace manifest (lists the plugin)
  aos-factory/                       the plugin
    .claude-plugin/plugin.json       plugin manifest
    skills/                          17 builder skills
    examples/                        example workspace-root files to copy after install
    builder-changelog.md             framework / plugin version history
    README.md                        plugin usage
```

## Distribute to others

**Marketplace (recommended).** Push this `dist/` directory to a git host
(GitHub/GitLab). Others install with:

```
/plugin marketplace add <owner>/<repo>
/plugin install aos-factory
```

Updates: bump the version in `aos-factory/.claude-plugin/plugin.json` and
`marketplace.json`, note changes in `builder-changelog.md`, push. Users update
from the marketplace.

**Zip (quick share).** Zip the `aos-factory/` directory and send it; the
recipient installs it from the local path via the `/plugin` menu. Zip install
requires Claude Code v2.1.128+.

## Test locally before publishing

```
claude --plugin-dir dist/aos-factory
```

## After install

Copy the shipped examples to your AOS workspace root and edit them:

- `aos-factory/examples/aos-router.md` → `<workspace>/aos-router.md`
- `aos-factory/examples/claude.md` → `<workspace>/claude.md`

Then run the `build-aos` skill to stand up your first AOS instance.
