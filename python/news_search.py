"""Find news about anything across 45+ countries (last 120 days).

    python news_search.py "interest rate" --country US --days 7
    python news_search.py "electric vehicles" --topic tech
"""
import argparse

from nestdaddy import get

parser = argparse.ArgumentParser(description="NestDaddy news search")
parser.add_argument("query")
parser.add_argument("--country", help="two-letter code, for example US, GB, SG, MY")
parser.add_argument("--topic", choices=["global", "tech", "financial", "local"])
parser.add_argument("--days", type=int, default=30, help="1 to 120")
parser.add_argument("--limit", type=int, default=10, help="1 to 50")
args = parser.parse_args()

data = get("/api/v1/news/search", q=args.query, country=args.country, topic=args.topic,
           days=args.days, limit=args.limit)
print(f"{data.get('total', 0)} articles found\n")
for a in data.get("results", []):
    when = (a.get("published_timestamp") or "")[:16].replace("T", " ")
    print(f"[{when}] {a['title']}\n   {a.get('source_domain', '')}  {a['url']}\n")
