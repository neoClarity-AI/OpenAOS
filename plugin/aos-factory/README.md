# Open AOS Factory Plugin

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), it can be easily ported to work with Codex and possibly other platforms.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install — it is a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

## Setup

### Claude Cowork

Follow these steps to install the Open AOS Factory in Claude Cowork.

1. Open Claude Cowork
2. Create a new project called **AOS Workspace**.
   - Create a new folder for the project. A good location would be:
     **For Windows:** `C:\Users\[account]\Claude\AOS Workspace`, where [account] is your current login account. 
     **For Mac:** TBD

3. Click on **Customize** button
4. Click on **Browse plugins** button
5. Click on **Personal** button
6. Click on Plus sign (**+**) to add new plugin
7. Click on **Add Marketplace** button
8. Click on **Add from a repository** button
9. Enter this URL: https://github.com/neoClarity-AI/claude-plugins
10. Click on the **Sync** button
11. Copy the templates to your AOS workspace root folder:
    - `aos-factory/templates/aos-router.md` → `<workspace>/aos-router.md`
    - `aos-factory/templates/CLAUDE.md` → `<workspace>/CLAUDE.md`




## Usage

To create your first AOS instance, invoke the build process as follows. The factory will walk you through the steps.

- **In Claude Cowork:** Open the **AOS** project, then type the prompt "Build an AOS"
- **In Claude Code:** Type the command "/build-aos"

After your AOS instance is created, refer to the user guide for that instance: `/[aos-instance-folder]/docs/aos-user-guide.html`. The [aos-instance-folder] is the name of your AOS instance in kebab format (ex. `Personal AOS` would be `personal-aos`).



## Workspace-root files

`aos-router.md` (instance router) and `CLAUDE.md` (project / session-start
instructions) govern selection across instances and the factory. They live at
your workspace root, above any instance. Example copies are in `templates/`;
copy them to your workspace root after install and edit for your setup.

See `builder-changelog.md` for version history.

## Skills

- **build-aos** — master entry point; stands up a complete AOS instance.
- **build-{security,memory,chief-of-staff,review}-agent** — the four required
  governance agents.
- **build-{learning,inbox,calendar,task,project-manager,research,writing,
  document-librarian,personal-crm,finance,health-life-logistics,automation}-agent**
  — optional productive agents (add at least one).
