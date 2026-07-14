| ![OpenAOS — AI for the rest of us](https://repository-images.githubusercontent.com/1263423041/c7102ffa-3f2b-4d04-ac2e-2e17a0f31beb) | **AI for the rest of us** |
| ------------------------------------------------------------ | ------------------------- |
# OpenAOS Quick Start for Claude Code

Build a complete, governed **Agentic Operating System (AOS)** — a personal or
professional system of specialized markdown agents, workflows, memory, templates,
configs, logs, and documentation — through a guided, approval-gated interview.

This plugin is a rendering of the AOS Factory design specification
(`spec_version 2.3.2`). The specification is the single source of truth; this
package is generated from it (design spec §1.6.1, §28).

## What's in the box

```text
.claude-plugin/plugin.json     Plugin manifest (name, version, author)
skills/
  build-aos/SKILL.md           Stand up a full AOS instance (master builder)
  build-agent/SKILL.md         Build one agent — the generic engine, covers every agent
agent-catalog.yaml             Agent identity/ownership catalog (read-only in instances)
agent-specs/[agent]/           profile.md + interviews.md for all 15 agents
aos-interviews.md              AOS-level setup interview script
builder-changelog.md           Framework/plugin changelog
templates/
  CLAUDE.md                    Example workspace-root session instructions
  AGENTS.md                    Example workspace-root cross-agent rules
```

The agents built by this factory:

- **Required governance (always built, cannot be removed):** Security, Memory,
  Chief of Staff, Review, Feedback.
- **Optional productive (choose at least one):** Tutor, Inbox, Calendar, Task,
  Project Manager, Research, Writing, Document, Personal CRM, Automation.

## Install

**Using VS Code**

- **Install Claude on VS Code.** Instructions here: https://code.claude.com/docs/en/vs-code
- **Install the OpenAOS plugin.** 
  - In a Claude Code terminal session, enter these commands:
  - `/plugin marketplace add https://github.com/neoClarity-AI/neoClarity-Plugins`
  - `/plugin install aos-factory@neoclarity-plugins`
- **Create an AOS instance**. 
  - Using VS Code, open an empty folder (File | Open Folder...). This will be the home for your new AOS instance

  - In a Claude Code terminal session, enter this command: `/build-aos help`

  - Read the overview to familiarize yourself with the skill, then proceed with the interview to create your AOS.
  - You can begin issuing commands to your new AOS. For details, refer to the **AOS User Guide** (`docs/aos-user-guide.html`) in the `docs` folder of your new AOS.

