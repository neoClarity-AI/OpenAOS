# AOS Factory — Claude Plugin

Build your own **Agentic Operating System (AOS)**: a personal or professional system of specialized markdown-based agents with governance, memory, workflows, templates, logs, and operating rhythms — generated collaboratively through a guided interview.

Version **2.2.0** (= design `spec_version`, see `builder-changelog.md`). Generated from the [Open AOS Factory design specification](https://github.com/neoClarity-AI/Open-AOS-Factory), the single source of truth.

## What you get

- **Five required governance agents** (built first, always): Security, Memory, Chief of Staff, Review, and Feedback.
- **Ten optional productive agents** (pick at least one): Tutor, Inbox, Calendar, Task, Project Manager, Research, Writing, Document, Personal CRM, Automation.
- Global workflows (daily startup through quarterly review), templates, configs, logs, an inbox/archive policy, and a plain-language HTML **AOS User Guide**.
- Safety by design: non-destructive by default; anything consequential waits for you to type exactly `Proceed`.

## Install

From the marketplace (recommended):

```text
/plugin marketplace add neoClarity-AI/Open-AOS-Factory
/plugin install aos-factory@open-aos-factory
```

Or load locally without installing:

```text
claude --plugin-dir path/to/claude-plugin/aos-factory
```

## Usage

1. Open a session in the folder you want to use as your **AOS Workspace**.
2. Copy `templates/CLAUDE.md` from this plugin to the workspace root (the setup skill will offer to do this for you; it never overwrites an existing file without a separate `Proceed`).
3. Say: **"Build my AOS"** — the `build-aos` skill runs the setup interview, previews every file, and creates your AOS instance only after you type exactly `Proceed`.
4. Add agents later at any time: **"Build the Research Agent"** (or any approved agent) — the `build-agent` skill handles all fifteen.

## Contents

```text
.claude-plugin/plugin.json    manifest
skills/build-aos/             master AOS setup skill
skills/build-agent/           generic agent build engine (one skill, all agents)
agent-catalog.yaml            agent identity/ownership catalog (read-only)
agent-specs/                  per-agent profile.md + interviews.md (read-only)
aos-interviews.md             the AOS setup interview script (read-only)
templates/CLAUDE.md           example workspace-root instructions
builder-changelog.md          framework/plugin changelog
```

## Contributing

Pull requests are accepted **only against the design specification** — the factory and this plugin are regenerated from the approved spec. See [CONTRIBUTING.md](https://github.com/neoClarity-AI/Open-AOS-Factory/blob/main/CONTRIBUTING.md).
