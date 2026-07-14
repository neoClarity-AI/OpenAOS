# Open AOS Factory Plugin

The **Open AOS Factory** builds and maintains one or more **Agentic Operating System (AOS)** instances. Each AOS is a personal or professional AI standardized operating environment composed of specialized agents, workflows, memory files, templates, and configuration files that work together to create a complete agentic system. The factory guides both technical and non-technical users through setup via a conversational interview, produces all files automatically once approved, and can add or rebuild individual agents at any time. Although this particular implementation is configured to run on Claude Cowork (for non-technical users) or Claude Code (for developers), it can be easily ported to work with Codex and possibly other platforms.

The **Open AOS Factory** is an open-source project located here: https://github.com/neoClarity-AI/Open-AOS-Factory

**What Is an AI Agent?**

An AI agent is an LLM (like Claude) that has been given a specific role, a defined set of responsibilities, and the autonomy to carry out tasks on your behalf. Rather than simply answering questions, an agent operates from a written set of instructions that tell it what it is responsible for, what tools and data it may use, where its boundaries lie, and when it should escalate back to you. In an AOS, each agent is specialized — one handles your inbox, another manages your calendar, another tracks projects — so that each behaves like a focused, reliable team member instead of a general-purpose assistant. Agents can work on their own, hand tasks off to one another, and follow the same rules every time, which is what makes the overall system predictable and trustworthy.

**What is an Agentic Operating System?**

An Agentic Operating System is not a piece of software you install — it is a structured workspace that gives your LLM a persistent identity, a memory, and a set of specialized agents, each with clear responsibilities, boundaries, and escalation rules. The AOS runs inside your Claude project folder. Once built, Claude reads the agent files at the start of every session and behaves consistently across conversations, routing tasks to the right agent, remembering context, and following the rules you approved when the system was set up.

**What Are the Benefits of an AOS?**

An **Agentic Operating System (AOS)** turns scattered, one-off interactions with an LLM into a dependable system that works the way you do. Because each agent has a fixed role, clear boundaries, and a shared memory, you stop re-explaining context and re-checking output every session. The system remembers your preferences, follows the rules you approved, and behaves consistently across conversations. Specialized agents let you delegate whole categories of work (such as inbox, calendar, projects, and research). Each task is handled by a focused, reliable team member rather than a general-purpose assistant. Built-in escalation rules keep you in control of anything sensitive. The result is less cognitive load, fewer dropped threads, and more leverage: you describe outcomes, the right agent does the work, and you get predictable, trustworthy results. And because the AOS is structured rather than coded, you get these benefits without any technical expertise, and can extend the system by adding new agents whenever your needs grow.

## Claude Cowork

Although the **Open AOS Factory** is generic in nature and can be adapted to a variety of LLMs, **Claude Cowork** is used for this particular implementation. **Claude Cowork** makes Agentic AI accessible to non-technical users. But it is not an AOS. The **Open AOS Factory** adds the structure necessary to make Claude Cowork a true AOS, without requiring any technical expertise to use.  Claude Code's agentic capabilities to the Claude Desktop app for knowledge work beyond coding. Instead of responding to one prompt at a time, Claude can take on complex, multi-step tasks and carry them out on your behalf — reading and writing your local files, running code in an isolated environment, and producing finished deliverables like formatted documents, spreadsheets, and presentations. You describe an outcome, let Claude work, and come back to completed results.

## Prerequisites

Before using the Open AOS Factory, you'll need:

- **A Claude subscription:** Claude Pro is the minimum subscription level, and it's sufficient for most uses of the AOS Factory. See the [Claude plans page](https://claude.com/pricing) for the available options.
- **The Claude Desktop application:** Required to run [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
- An active Internet is required for all **Claude Cowork** sessions.

## Setup

### Create Claude Cowork Project

Follow these steps to create a new in **Claude Cowork** project. You will use this project to interact with all your AOS instances.

1. Setup **Claude Desktop** on your computer.
   - Download and install **Claude Desktop** (see [Getting Started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) for details.)
   - Start **Claude Desktop** and sign in using your Claude subscription.

2. Using **Claude Desktop**:

    - Click on the **Cowork** tab at the top of the lefthand navigation pane.
      
    - Click on **Projects** in the nav menu.
      
    - Click on the **New project** button.
      
    - Click on **Use an existing folder** option.
      
    - Click on **Select a folder...**
      
    - Create a new folder called **AOS Workspace**.
      
    - If necessary, shorten the project **Name** to **AOS Workspace**. 
      No instructions or additional files are required at this time
      
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

     `Copy the template files from the AOS Factory into the project root folder.`

You're now ready to create your first AOS instance!


## Create your first AOS Instance

To create your first AOS instance, invoke the build process as follows. The factory will walk you through the steps.

1. **Open a new session** in your **AOS Workspace** project, then issue the prompt: Build an AOS.
2. **Start the build.** Type: `Build my AOS` — Claude will open the master builder and begin the setup interview.
3. **Answer the interview questions.** The builder acts as an executive coach and collaborator, asking about your work style, the agents you want, and how you want the system to behave. It recommends sensible defaults and documents decisions as it goes. Recommended first agents to install: 
4. **Review the proposed files.** Before anything is created, Claude shows you exactly what it plans to write.
5. **Type `Proceed`** to authorize file creation. Nothing is written until you do.

After your AOS instance is created, start a new conversation in the AOS Workspace. Here are some prompts to get you started.

- `Show me the daily brief.`
- `Show me the AOS User Guide.`
- `Take me on a guided tour of my new AOS.`
- `Let's setup the scheduled tasks.`

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
