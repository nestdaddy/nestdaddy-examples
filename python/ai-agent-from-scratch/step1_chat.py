"""Step 1: talk to a model. It is smart, but it only knows its training data."""
import os

from openai import OpenAI

llm = OpenAI(base_url=os.getenv("LLM_BASE_URL", "http://localhost:11434/v1"),
             api_key=os.getenv("LLM_API_KEY", "ollama"))

reply = llm.chat.completions.create(
    model=os.getenv("LLM_MODEL", "qwen2.5:7b"),
    messages=[{"role": "user", "content": "What happened in AI today?"}],
)
print(reply.choices[0].message.content)
