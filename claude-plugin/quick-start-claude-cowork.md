| ![OpenAOS — AI for the rest of us](https://repository-images.githubusercontent.com/1263423041/c7102ffa-3f2b-4d04-ac2e-2e17a0f31beb) | **AI for the rest of us** |
| ------------------------------------------------------------ | ------------------------- |

# OpenAOS Quick Start for Claude Cowork

## Prerequisites

Before using the OpenAOS, you'll need:

- **A Claude subscription:** Claude Pro is the minimum subscription level, and it's sufficient for most uses of the AOS Factory. See the [Claude plans page](https://claude.com/pricing) for the available options.
- **The Claude Desktop application:** Required to run [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
- An active Internet is required for all **Claude Cowork** sessions.

## Setup

### Create a Claude Cowork Project

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

You now have a workspace for your AOS. Before you can create your AOS, you first need to install the **OpenAOS ** plugin.

### Install the OpenAOS plugin

Using **Claude Desktop**:

1. Click on the **Home** tab at the top of the lefthand navigation pane.

2. Click on **Customize** button
3. Click on **Browse plugins** button
4. Click on **Personal** button
5. Click on Plus sign (**+**) to add new plugin
6. Click on **Add Marketplace** button
7. Click on **Add from a repository** button
8. Enter this URL: [https://github.com/neoClarity-AI/OpenAOS](https://github.com/neoClarity-AI/OpenAOS)
9. Click on the **Sync** button
10. Click on the **OpenAOS** plugin.
11. Click on the **Install** button.
12. Verify that the **Install** button had changed to a **Manage** button.
   The plugin is now installed!
   - Click the back arrow ()

You're now ready to create your first AOS instance!


## Create your first AOS Instance

To create your AOS, invoke the build process as follows. **OpenAOS** will walk you through the steps.

Using **Claude Desktop**:

1. **Open a new session** in your **AOS Workspace** project.
2. Set the model to Sonnet Medium ([help](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings))
3. **Familiarize yourself with the OpenAOS build process**. Type: `/build-aos help` — Claude will explain how the OpenAOS plugin works. You can ask Claude follow-up questions if you like.
4. **Start the build.** Type: `Build my AOS` — Claude will open the master builder and begin the setup interview.
5. **Answer the interview questions.** The builder acts as an executive coach and collaborator, asking about your work style, the agents you want, and how you want the system to behave. It recommends sensible defaults and documents decisions as it goes. Recommended first agents to install: 
6. **Review the proposed files.** Before anything is created, Claude shows you exactly what it plans to write.
7. **Type `Proceed`** to authorize file creation. Nothing is written until you do.

After your AOS instance is created, start a new conversation in the AOS Workspace. Here are some prompts to get you started.

- `Show me the daily brief.`
- `Show me the AOS User Guide.`
- `Take me on a guided tour of my new AOS.`
- `Let's setup the scheduled tasks.`

**Best practice:** Always start a new conversation when you switch topics. Conversations that grow too long invite drift, which causes erratic results.

**Pro tip:** You can multi-task in Claude Cowork. While Claude is working on one request, you can navigate back to the **AOS Workspace** home page and start a new conversation. You can have as many conversations going as you like. But, keep in mind that you'll be burning through your session limits faster.

## Workspace root files

The **OpenAOS** plugin contains two template files (**CLAUDE.md** and **AGENTS.md**) that must be in your workspace root folder. Both of these files are required for your AOS to work correctly.

These two files contain important instructions for Claude that include:

- How to operate in **Planning Mode**.
- How to invoke the AOS when you start a new conversation.

## Planning Mode

If you start any conversation with the words, "Planning mode" or "P mode" or "pmode", Claude will not create, edit, or delete any file until you give it the instruction to "Proceed" (using that exact word). Planning mode means the session is for discussing and designing changes — not implementing them. Instead, Claude will display proposed changes and ask you to proceed. You can either continue the conversation or type "Proceed" to implement the proposed changes. It's a great way to collaborate with Claude without creating unintended changes.

## Skills

- **build-aos** — master entry point; stands up a complete AOS instance.
- **build-agent** — adds or updates an agent.
