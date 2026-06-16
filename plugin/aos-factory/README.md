# Open AOS Factory Plugin

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), it can be easily ported to work with Codex and possibly other platforms.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install — it is a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

## Setup

Follow these steps to create and use the Open AOS Factory in **Claude Cowork**.

### Install the Claude Cowork on your computer

**Claude Cowork** is a feature within the **Claude Desktop** application. Follow the instructions in this link to install it on your computer

- [Getting Started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)

### Install AOS Factory plugin

1. Using **Claude Desktop**:
   
   - Click on the **Cowork** tab at the top of the lefthand navigation pane.
   - Click on **Customize** button
   - Click on **Browse plugins** button
   - Click on **Personal** button
   - Click on Plus sign (**+**) to add new plugin
   - Click on **Add Marketplace** button
   - Click on **Add from a repository** button
   - Enter this URL: [https://github.com/neoClarity-AI/neoClarity-Plugins](https://github.com/neoClarity-AI/neoClarity-Plugins)
   - Click on the **Sync** button
   - Click on the **Aos factory** plugin.
   - Click on the **Install** button.
   - Verify that the **Install** button had changed to a **Manage** button.
     The plugin is now installed!
   - Click the back arrow ()
2. To complete the setup, copy the template files into your AOS workspace root folder. Here's how:

   - Click on the **Cowork** tab at the top of the lefthand navigation pane.
   - Click on **Projects** in the nav menu.
   - Click on the **AOS Workspace** project.
   - Set the model to **Sonnet Medium**. This model works well for most **AOS** tasks.
   - Type this prompt into the message box: 
     `Copy the template files from the AOS Factory into the project root folder.` 
     Note: you need do this only once when setting up your **AOS Workspace**.

### Create the AOS Workspace project

The **AOS Factory** operates in the context of a **Claude Cowork Project** - a dedicated workspace within the **Claude Desktop** app that allow you to group related files, instructions, and tasks for a specific purpose. We will create a project called the **AOS Workspace**.  

1. Create a new folder called **AOS Workspace** on your computer. This will be the home for your AOS instances. 

   - **For Windows:**
     - Open the **Command Prompt** window. ([help](https://learn.microsoft.com/en-us/answers/questions/4197900/how-to-access-command-prompt))
     - Type the command: `mkdir %USERPROFILE%"\Claude\AOS Workspace"` ([help](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mkdir))
     - Verify the directory exists: `chdir %USERPROFILE%"\Claude\AOS Workspace"` 
   - **For Mac:** 
     - TBD
2. Open **Claude Desktop**. Using **Claude Desktop**:

   - Click on the **Cowork** tab at the top of the lefthand navigation pane.

   - Click on **Projects** in the nav menu.

   - Click on the **New project** button.

   - Click on **Use an existing folder** option.

   - Click on **Select a folder...**

   - Double-click on the **Claude** folder, double-click on the **AOS Workspace** folder, then click on the **Select Folder** button.

   - Change the **Name** to **AOS Workspace**. 
     No instructions or additional files are required.

   - Click on the **Create** button.

You're now ready to create your first AOS instance!


## Create your first AOS instance

To create your first AOS instance, invoke the build process as follows. The factory will walk you through the steps.

1. **Start a new session.** Using  Claude Desktop:
   - Select the **Cowork** tab
   - Click on Projects.
   - Select the **AOS Workspace** project.
   - **Start a new build.** Type this prompt into the message box: `Build an AOS.`

2. **Answer the interview questions.** The builder acts as an executive coach and collaborator, asking about your work style, the agents you want, and how you want the system to behave. It recommends sensible defaults and documents decisions as it goes. Recommended first agents to install: 
3. **Review the proposed files.** Before anything is created, Claude shows you exactly what it plans to write.
4. **Authorize file creation.** Nothing is written until you do.

After your AOS instance is created, start a new conversation in the AOS Workspace. Here are some prompts to get you started.

- Show me the daily brief.
- Show me the AOS User Guide.
- Take me on a guided tour of my new AOS.
- Let's setup the scheduled tasks.

**Best practice:** Always start a new conversation when you switch topics. Conversations that grow too long invite drift, which causes erratic results.

**Pro tip:** You can multi-task in Claude Cowork. While Claude is working on one request, you can navigate back to the **AOS Workspace** home page and start a new conversation. You can have as many conversations going as you like. But, keep in mind that you'll be burning through your session limits faster.

## Workspace root files

The AOS Factory plugin contains two template files (**CLAUDE.md** and **aos-router.md**) that must be in your workspace root folder. Both of these files are required for your AOS to work correctly.

These two files contain important instructions that include:

- How to operate in **Planning Mode**.
- Which AOS instance to use when you start a new conversation in the **AOS Workspace**.

## Planning Mode

If you start any conversation with the words, "Planning mode" or "P mode" or "pmode", Claude will not create, edit, or delete any file until you give it the instruction to "Proceed" (using that exact word). Planning mode means the session is for discussing and designing changes — not implementing them. Instead, Claude will display proposed changes and ask you to proceed. You can either continue the conversation or type "Proceed" to implement the proposed changes. It's a great way to collaborate with Claude without creating unintended changes.

## Skills

- **build-aos** — master entry point; stands up a complete AOS instance.
- **build-{security,memory,chief-of-staff,review}-agent** — the four required
  governance agents.
- **build-{learning,inbox,calendar,task,project-manager,research,writing,
  document-librarian,personal-crm,finance,health-life-logistics,automation}-agent**
  — optional productive agents (add at least one).
