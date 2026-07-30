# Goose CLI - Core Commands

The Goose CLI uses a simple verb-based structure. Here are the most frequently used commands to get started.

| Command | Description | Example |
|---------|-------------|---------|
| `goose session` | Starts an interactive AI agent session in your terminal. | `goose session` |
| `goose run` | Executes a single prompt and exits (non-interactive). | `goose run "Explain the architecture of this project"` |
| `goose configure` | Opens the interactive wizard to configure LLM providers, API keys, and extensions. | `goose configure` |
| `goose info` | Displays the current active configuration, including provider, model, and loaded extensions. | `goose info` |
| `goose --version` | Displays the currently installed version of Goose. | `goose --version` |
| `goose update` | Updates Goose to the latest available version. | `goose update` |


# Goose CLI - Input & Execution Options

When using `goose run` or `goose session`, you can pass specific flags to control how Goose processes your request.

| Flag | Description | Example |
|------|-------------|---------|
| `-t`, `--text` | Passes input text directly to Goose (useful for scripting). | `goose run -t "List all .js files"` |
| `-i`, `--instructions` | Passes a path to a file containing instructions. Use `-` for standard input. | `goose run -i my_prompt.txt` |
| `--system` | Provides additional system instructions to customize the agent's behaviour for that specific run. | `goose session --system "Always reply in Spanish"` |
| `--recipe` | Loads a custom workflow (YAML recipe) into the session. | `goose run --recipe ./build-docs.yaml` |

# Goose CLI - Session Management

Goose allows you to pause, resume, and review previous workflows.

| Command / Flag | Description | Example |
|---------------|-------------|---------|
| `goose session list` | Lists all previous sessions. Use `-f json` for JSON output. | `goose session list` |
| `--resume`, `-r` | Resumes a previous session. You can specify a session ID or resume the most recent session. | `goose session --resume` |
| `--fork` | Creates a duplicate of an existing session, allowing you to explore a different workflow without modifying the original session. | `goose session --resume --fork --name my-project` |
| `--history` | Displays previous conversation history when resuming a session to provide context. | `goose session --resume --history` |
| `goose session remove` | Deletes a specific session. Requires either `--session-id` or `--name`. | `goose session remove --name task-1` |

# Goose CLI - Interactive Slash Commands (Inside a Session)

Once you are inside an active `goose session`, you can use the following slash commands directly in the chat prompt to control the agent.

| Slash Command | Description |
|--------------|-------------|
| `/prompt` | Uses a specific saved prompt. |
| `/prompts` | Lists all available saved prompts. |
| `/compact` | Compacts the conversation history to reduce token usage, useful when approaching context limits. |
| `/clear` | Clears the current conversation history and starts a new session. |

---

# Goose CLI - Extensions & MCP (Model Context Protocol)

Goose integrates with external tools (such as databases, GitHub, browsers, and IDEs) using the **Model Context Protocol (MCP)**.

| Command | Description | Example |
|---------|-------------|---------|
| `goose mcp` | Manages Model Context Protocol (MCP) servers. | `goose mcp list` |
| `goose acp` | Manages Agent Client Protocol (ACP) connections for integrations such as Zed or Visual Studio Code. | `goose acp` |
| `goose serve` | Runs Goose as a background server. Use `--port` to specify the listening port. | `goose serve --port 3284` |

# Goose CLI - Practical Examples & Usage Scenarios

The following examples demonstrate common ways to use Goose for development, automation, and troubleshooting tasks.

## 1. Fast File Refactoring

Refactor an existing Python file to use asynchronous programming and improve code readability.

```bash
goose run -t "Refactor authentication.py to use async/await syntax and add comments."
```

---

## 2. Resume a Complex Debugging Session

Continue working on a previous debugging session while displaying the earlier conversation for context.

```bash
goose session --resume --history
```

---

## 3. Schedule an Automated Task Using Recipes

If you have a recipe (for example, `daily-report.yaml`) that generates a daily summary of Git commits, you can schedule it to run automatically.

```bash
goose schedule add \
  --schedule-id daily-report \
  --cron "0 9 * * *" \
  --recipe-source ./recipes/daily-report.yaml
```

**What this does:**
- Creates a scheduled task named `daily-report`
- Executes every day at **09:00**
- Runs the recipe located at `./recipes/daily-report.yaml`

---

## 4. Review Goose Configuration and Loaded Tools

Display the current Goose configuration along with detailed information about loaded providers, extensions, tools, and accessible paths.

```bash
goose info -v
```

> **Note:** The `-v` (verbose) flag provides additional diagnostic information, making it useful for troubleshooting configuration and integration issues.