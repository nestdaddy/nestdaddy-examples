"""Find research papers from arXiv, PubMed, OpenAlex, CrossRef and more.

    python research_papers.py "retrieval augmented generation" --limit 5
"""
import argparse

from nestdaddy import get

parser = argparse.ArgumentParser(description="NestDaddy research papers")
parser.add_argument("query")
parser.add_argument("--limit", type=int, default=10)
args = parser.parse_args()

data = get("/api/v1/research", q=args.query, per_page=args.limit)
for i, p in enumerate(data.get("results", []), 1):
    title = p.get("title", "")
    link = p.get("url") or p.get("link") or ""
    year = p.get("year") or str(p.get("published_date") or "")[:4]
    source = p.get("source", "")
    print(f"{i}. {title}\n   {year} {source}\n   {link}\n")
