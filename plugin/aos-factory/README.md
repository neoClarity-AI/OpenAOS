# Open AOS Factory Plugin

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), it can be easily ported to work with Codex and possibly other platforms.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install — it is a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

## Setup

### Create Claude Cowork Project

Follow these steps to create a new in **Claude Cowork** project. You will use this project to interact with all your AOS instances.

#### Useful resources

- [Getting Started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Getting Started with Claude Cowork projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)



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
      No instructions or add
  
    - Click on the **Create** button.
  


You now have a workspace for your AOS. Before you can create your AOS, you first need to install the **AOS Factory** plugin.

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

     **Copy the template files from the AOS Factory into the project root folder.**

You're now ready to create your first AOS instance!


## Usage

To create your first AOS instance, invoke the build process as follows. The factory will walk you through the steps.

- **In Claude Cowork:** Open the **AOS Workspace** project, then type the prompt "Build an AOS"
- **In Claude Code:** Type the command "/build-aos"

After your AOS instance is created, refer to the user guide for that instance: `/[aos-instance-folder]/docs/aos-user-guide.html`. The [aos-instance-folder] is the name of your AOS instance in kebab format (ex. `Personal AOS` would be `personal-aos`).



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
