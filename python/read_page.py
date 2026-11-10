"""Get the readable text of any public web page (title, date and main text, without menus or ads).
Handy for RAG pipelines and for agents that need to read an article in full.

    python read_page.py https://peps.python.org/pep-3156/ --max-chars 3000
"""
import argparse

from nestdaddy import get

parser = argparse.ArgumentParser(description="NestDaddy page reader")
parser.add_argument("url")
parser.add_argument("--max-chars", type=int, default=12000, help="500 to 30000")
args = parser.parse_args()

page = get("/api/v1/extract", url=args.url, max_chars=args.max_chars)
print(page.get("title", ""))
print(page.get("final_url", args.url))
if page.get("published"):
    print("Published:", page["published"])
print()
print(page.get("text", ""))
if page.get("truncated"):
    print(f"\n[cut at {args.max_chars} characters; the page has {page.get('length')}]")
