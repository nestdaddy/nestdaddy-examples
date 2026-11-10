# NestDaddy MCP server

One remote MCP server gives your AI app live web search, news from 45+ countries with full article text,
research papers, and data on new AI models, software and games.

- Server URL: `https://mcp.nestdaddy.com/mcp` (Streamable HTTP)
- Auth: `Authorization: Bearer YOUR_KEY` (or `?key=YOUR_KEY` on the URL when the client cannot set headers)
- Get a key: [nestdaddy.com/mcp](https://nestdaddy.com/mcp)
- Step-by-step guide: [How to give Claude live web search and news with one MCP server](https://nestdaddy.com/blog/add-live-web-search-to-claude-mcp)

## Tools

| Tool | What it does |
|---|---|
| `news_search` | News by key words across 45+ countries and the last 120 days |
| `web_search` | Pages from NestDaddy's own web index |
| `news` | Global, tech and financial headlines |
| `country_news` | Local news by country |
| `read_page` | The full text of an article or page |
| `research_papers` | Papers from arXiv, PubMed, OpenAlex, CrossRef and more |
| `ai_tools` | New AI models with prices, trending models and AI projects |
| `software` | Popular apps and developer tools with their current version |
| `games` | Game data by genre, latest or trending |

## Claude (claude.ai and Claude Desktop)

Settings, then Connectors, then Add custom connector. Name it NestDaddy and paste:

```
https://mcp.nestdaddy.com/mcp?key=YOUR_KEY
```

## Claude Code

```bash
claude mcp add --transport http nestdaddy https://mcp.nestdaddy.com/mcp \
  --header "Authorization: Bearer YOUR_KEY"
```

## Cursor

[`cursor-mcp.json`](cursor-mcp.json) goes in `~/.cursor/mcp.json` or `.cursor/mcp.json` in a project.

## VS Code

[`vscode-mcp.json`](vscode-mcp.json) goes in `.vscode/mcp.json` in your workspace.

## Windsurf

[`windsurf-mcp.json`](windsurf-mcp.json) goes in `~/.codeium/windsurf/mcp_config.json`.

## n8n

1. In your AI Agent node, add an **MCP Client Tool**.
2. Endpoint `https://mcp.nestdaddy.com/mcp`, transport **HTTP Streamable**.
3. Authentication **Bearer**, token `YOUR_KEY`.
