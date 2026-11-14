# Build an AI agent from scratch (Python, free)

An AI agent is a model + tools + a loop. This folder builds one in about 60 lines, with no framework, so you can see
exactly how function calling works. Video walkthrough: *How to Build an AI Agent from Scratch* on
[YouTube @nestdaddy_search](https://www.youtube.com/@nestdaddy_search).

| File | Step |
|---|---|
| `step1_chat.py` | Talk to the model. It doesn't know what happened today. |
| `step3_agent_loop.py` | One tool (`news_search`) + the agent loop. |
| `agent.py` | Final: a second tool (`read_page`) and a system message that stops it from inventing details. |

## Run it

```bash
pip install -r requirements.txt

# 1. A free model on your own computer (https://ollama.com)
ollama pull qwen2.5:7b

# 2. A free news & web search key (1,000 calls a month, no card): https://nestdaddy.com/apis
export NESTDADDY_API_KEY="your-key"

python agent.py "What happened in AI today?"
```

Any OpenAI-compatible model works. Set `LLM_BASE_URL`, `LLM_API_KEY` and `LLM_MODEL`, for example Gemini:

```bash
export LLM_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
export LLM_API_KEY="your-gemini-key"
export LLM_MODEL="gemini-2.5-flash"   # any current Gemini model name from Google AI Studio
```

## How it works

1. **Model** (the brain): decides whether it can answer or needs a tool.
2. **Tools** (the hands): plain Python functions, here `news_search` and `read_page`.
3. **Manual**: `TOOL_SPECS`, a JSON schema per tool. The description tells the model *when* to use it.
4. **Loop**: send messages + tools; if the reply asks for tools, run them, add the results as `tool` messages, repeat.

The lesson from the video: with only headlines, the model invented ten "key points". One rule in the system message
("search results are only headlines: read the best article before you give details, only state facts you found")
made it read the article first and answer from it.

MIT License.
