# NestDaddy API and MCP examples

[![mcptry](https://mcptry.com/badge/com.nestdaddy/nestdaddy)](https://mcptry.com/servers/com.nestdaddy/nestdaddy)

Working examples for [NestDaddy](https://nestdaddy.com): give your AI today's internet.
Use them to give your app or AI agent live web search, real-time breaking news from around the world,
the full text of any article, and research papers, all from NestDaddy's own index.

- **REST API**: plain HTTPS + JSON, any language. Docs: [nestdaddy.com/apis](https://nestdaddy.com/apis)
- **MCP server**: one remote server for Claude, Cursor, VS Code, n8n and any MCP client.
  Setup: [nestdaddy.com/mcp](https://nestdaddy.com/mcp)

## Get a key

Get an API key on [nestdaddy.com/mcp](https://nestdaddy.com/mcp) (one All-in-One key works for every endpoint
below and for the MCP server). Then put it in an environment variable:

```bash
export NESTDADDY_API_KEY="your_key"          # macOS / Linux
setx NESTDADDY_API_KEY "your_key"            # Windows (open a new terminal after)
```

Send the key in the `X-API-Key` header (or as `?key=` on the URL when a client cannot set headers).

## Endpoints used in these examples

| Endpoint | What it returns |
|---|---|
| `GET /api/v1/search?q=` | Web results from NestDaddy's own index |
| `GET /api/v1/news/search?q=&country=&days=` | News by key words, worldwide, last 120 days |
| `GET /api/v1/news/global` `/tech` `/financial` | Latest headlines by topic |
| `GET /api/v1/news/local?country=SG` | Latest headlines from one country |
| `GET /api/v1/extract?url=` | The readable text of one web page |
| `GET /api/v1/research?q=&per_page=` | Research papers (arXiv, PubMed, OpenAlex, CrossRef and more) |

Base URL: `https://nestdaddy.com`. Full reference: [nestdaddy.com/apis](https://nestdaddy.com/apis).
OpenAPI 3.1 spec (import into Postman, Insomnia or a code generator): [nestdaddy.com/openapi.json](https://nestdaddy.com/openapi.json).

## Examples

| Folder | What is inside |
|---|---|
| [`curl/`](curl/) | One-line requests for every endpoint |
| [`python/`](python/) | Web search, news search, a daily news digest, read a page in full, research papers (standard library only) |
| [`python/ai-agent-from-scratch/`](python/ai-agent-from-scratch/) | Build an AI agent from scratch in ~60 lines: a model, tools and a loop (free with Ollama) |
| [`javascript/`](javascript/) | Node 18+ with the built-in `fetch` |
| [`mcp/`](mcp/) | Config for Claude, Claude Code, Cursor, VS Code, Windsurf and n8n |

Ready-to-use template: [**news-digest-bot**](https://github.com/nestdaddy/news-digest-bot), a daily news digest
to Telegram, Slack or email that runs free on GitHub Actions.

Quick start:

```bash
git clone https://github.com/nestdaddy/nestdaddy-examples
cd nestdaddy-examples
python python/news_search.py "interest rate" --country US
node javascript/search.mjs "rust error handling"
```

## Links

- Website: [nestdaddy.com](https://nestdaddy.com)
- MCP server: [nestdaddy.com/mcp](https://nestdaddy.com/mcp)
- API docs: [nestdaddy.com/apis](https://nestdaddy.com/apis)
- Blog and guides: [nestdaddy.com/blog](https://nestdaddy.com/blog)
- Contact: hello@nestdaddy.com

The examples in this repository are MIT licensed. Use of the API follows the
[NestDaddy terms](https://nestdaddy.com/terms).
