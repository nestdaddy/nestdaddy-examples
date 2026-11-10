"""Search the web with NestDaddy's own index.

    python web_search.py "python asyncio guide" --limit 5
"""
import argparse

from nestdaddy import get

parser = argparse.ArgumentParser(description="NestDaddy web search")
parser.add_argument("query")
parser.add_argument("--limit", type=int, default=10)
args = parser.parse_args()

data = get("/api/v1/search", q=args.query, limit=args.limit)
for i, r in enumerate(data.get("results", []), 1):
    print(f"{i}. {r['title']}\n   {r['url']}\n   {r.get('snippet', '')[:160]}\n")
