---
updatedAt: 2026-11-10T19:35:11.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# AI Agent Tools

Connect AI agents to Alpaca's Trading API, Market Data API, and Broker API with plugins, MCP servers, the Alpaca CLI, and agent skills.

# Connect your AI agent to Alpaca

Alpaca gives AI agents direct access to trading, market data, and brokerage operations. Pick the tool that fits how you work, connect it in a few minutes, and start in paper trading or sandbox before moving to live.

## Choose your path

Start with who you are building for:

* **Trading for yourself or your business.** Use the Trading MCP server or the Alpaca CLI with your Alpaca brokerage account. Both cover the Trading API and Market Data API: account, orders, positions, portfolio history, and market data for stocks, ETFs, options, and crypto.
* **Building for your end customers or operating as a Broker API partner.** Use the Broker MCP server to inspect accounts, review transactions, and build and test operational workflows against your correspondent data.

Then pick how your agent connects:

| Tool                     | Best for                                                                        | Auth                               | Get started                                                |
| ------------------------ | ------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------- |
| Agent plugins            | The fastest setup in Cursor, Claude Code, and Codex                             | Sign in with Alpaca (OAuth)        | [Install a plugin](#install-an-agent-plugin)               |
| Hosted MCP servers       | Any other MCP client that supports remote servers                               | Sign in with Alpaca (OAuth)        | [Configure hosted MCP](#configure-hosted-mcp-servers)      |
| Local Trading MCP server | Running the open-source server yourself, with API keys and toolset filtering    | API keys                           | [Trading API MCP](./trading-api-mcp)                       |
| Broker MCP server        | Broker API partners                                                             | Sign in with Alpaca (OAuth)        | [Broker API MCP](./broker-api-mcp)                         |
| Alpaca CLI               | Terminal, scripts, CI, and focused agent actions with structured JSON output    | API keys or `alpaca profile login` | [Alpaca CLI](./alpacas-cli)                                |
| Agent skills             | Step-by-step playbooks your agent follows, such as backtesting or paper trading | Uses the Alpaca CLI                | [Alpaca skills](https://github.com/alpacahq/alpaca-skills) |

Not sure? Install the `alpaca-trading` plugin and connect to paper trading first. You can add the CLI or skills later.

## Prerequisites

* An [Alpaca account](https://app.alpaca.markets/signup). A free paper trading account is enough to start.
* An AI client such as [Cursor](https://cursor.com), [Claude Code](https://www.anthropic.com/claude-code), [Codex](https://github.com/openai/codex), VS Code, or another MCP-compatible tool.

## Install an agent plugin

Plugins connect Cursor, Claude Code, and Codex to Alpaca's hosted MCP servers. There are no API keys to copy: you sign in with your Alpaca account the first time a server starts.

| Plugin           | Includes                                                                    |
| ---------------- | --------------------------------------------------------------------------- |
| `alpaca-trading` | Trading MCP (live) and Trading MCP (paper), including Market Data API tools |
| `alpaca-broker`  | Broker MCP (live) and Broker MCP (sandbox)                                  |

### Cursor

1. Open the command palette with `Cmd + Shift + P` (macOS) or `Ctrl + Shift + P` (Windows and Linux).
2. Run **Open Customize**, then click **Browse Marketplace**.
3. Click **Add Marketplace**, choose **Import from GitHub**, and enter `https://github.com/alpacahq/agentic`.
4. Install `alpaca-trading`, `alpaca-broker`, or both.
5. Start an Alpaca MCP server and complete the sign-in in your browser.

### Claude Code

```bash
claude plugin marketplace add alpacahq/agentic
```

Start a session and run `/plugin`. Select the `alpaca-plugins` marketplace and install `alpaca-trading`, `alpaca-broker`, or both. Run `/reload-plugins`, then use `/mcp` to start a server and sign in.

### Codex

```bash
codex plugin marketplace add alpacahq/agentic
```

Install a plugin from the `alpaca-plugins` marketplace, then sign in:

```bash
codex mcp login <mcp-name>
```

## Configure hosted MCP servers

If you prefer not to use a plugin, or your client is not listed above, add a hosted server to your MCP client configuration directly.

| Server           | Endpoint                                        |
| ---------------- | ----------------------------------------------- |
| Trading (live)   | `https://api.alpaca.markets/mcp`                |
| Trading (paper)  | `https://paper-api.alpaca.markets/mcp`          |
| Broker (live)    | `https://broker-api.alpaca.markets/mcp`         |
| Broker (sandbox) | `https://broker-api.sandbox.alpaca.markets/mcp` |

Each client needs its own sign-in settings. Copy the configuration for your client from the [agentic repository](https://github.com/alpacahq/agentic#manual-remote-mcp-configuration). For Broker MCP in VS Code, see [Broker API MCP](./broker-api-mcp#vs-code).

## Verify the connection

Restart your client if needed, then ask your agent a question for the server you connected. If you get account details back, you are connected.

* **Trading API:** "What is my Alpaca paper account balance and buying power?"
* **Broker API:** "List the five most recently created accounts in my Broker API sandbox."

Try a few more prompts:

* **Trading API:** "Show me AAPL's daily bars for the last week."
* **Trading API:** "What are the most active stocks right now?"
* **Trading API:** "Place a limit order to buy 10 shares of MSFT at $400 in my paper account."
* **Broker API:** "Show recent transactions for account `{account_id}` in my Broker API sandbox."

## Before you use live environments

* **Start in paper or sandbox.** Test agent workflows against paper trading or the Broker sandbox before switching to live.
* **Review orders.** Agents submit orders through Trading API and Broker API; execution is not guaranteed. Review what your agent proposes before you confirm it.
* **Protect your keys.** Never paste API keys into a chat. Keep them in your client configuration or your OS secret store.
* **Rate limits and data plans apply.** Agent traffic counts against your account's API rate limits, and some real-time data requires a market data subscription.

## Get help

* Request support for another client or report a problem in the [agentic repository](https://github.com/alpacahq/agentic/issues).
* Contact [Alpaca Support](mailto:support@alpaca.markets).

## Disclosure

Insights generated by our MCP servers and connected AI agents are for educational and informational purposes only and should not be taken as investment advice. Past performance from models does not guarantee future results. Conduct your own due diligence before making any decisions.