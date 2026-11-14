"""Step 3: the agent loop with one tool (news_search). agent.py is the final version.

Works with any OpenAI-compatible model: Ollama (free, on your own PC), Gemini, OpenAI, Groq...

    pip install openai requests
    export NESTDADDY_API_KEY="your-key"   # free key, 1,000 calls a month: https://nestdaddy.com/apis
    python agent.py "What happened in AI today?"
"""
import json
import os
import sys
from datetime import date

import requests
from openai import OpenAI

# 1. The brain: any OpenAI-compatible model. Ollama runs it free on your own computer.
llm = OpenAI(base_url=os.getenv("LLM_BASE_URL", "http://localhost:11434/v1"),
             api_key=os.getenv("LLM_API_KEY", "ollama"))
MODEL = os.getenv("LLM_MODEL", "qwen2.5:7b")

# 2. The hands: plain Python functions the model is allowed to call.
NEWS_API = "https://nestdaddy.com/api/v1"
HEADERS = {"X-API-Key": os.getenv("NESTDADDY_API_KEY", "")}


def news_search(query, days=3):
    r = requests.get(f"{NEWS_API}/news/search", headers=HEADERS, timeout=30,
                     params={"q": query, "days": days, "limit": 5})
    r.raise_for_status()
    return [{"title": a["title"], "source": a.get("source_domain"),
             "date": a.get("published_timestamp"), "url": a["url"]}
            for a in r.json().get("results", [])]


TOOLS = {"news_search": news_search}

# 3. The manual: tell the model what each tool does and which arguments it takes (JSON schema).
TOOL_SPECS = [
    {"type": "function", "function": {
        "name": "news_search",
        "description": "Search the latest news. Use it for anything that happened recently.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "Short key words, like a search box"},
            "days": {"type": "integer", "description": "How many days back to search, 1 to 30"}},
            "required": ["query"]}}}
]


# 4. The loop: the model decides, we run the tool, the model reads the result... until it answers.
def run_agent(question, max_steps=6):
    messages = [
        {"role": "system", "content": f"You are a helpful assistant. Today is {date.today()}. "
                                      "Use your tools for anything recent. Cite the URLs you used."},
        {"role": "user", "content": question},
    ]
    for _ in range(max_steps):
        reply = llm.chat.completions.create(model=MODEL, messages=messages, tools=TOOL_SPECS).choices[0].message
        if not reply.tool_calls:          # no tool needed: this is the final answer
            return reply.content
        messages.append(reply)
        for call in reply.tool_calls:     # the model asked for one or more tools
            args = json.loads(call.function.arguments or "{}")
            print(f"  -> {call.function.name}({args})")
            try:
                result = TOOLS[call.function.name](**args)
            except Exception as e:        # give errors back to the model instead of crashing
                result = f"error: {e}"
            messages.append({"role": "tool", "tool_call_id": call.id,
                             "content": json.dumps(result, ensure_ascii=False)[:6000]})
    return "Stopped: too many steps."


if __name__ == "__main__":
    print(run_agent(" ".join(sys.argv[1:]) or "What happened in AI today?"))
