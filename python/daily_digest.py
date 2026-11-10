"""Print a short daily digest: top headlines for a few topics and one country.

    python daily_digest.py --country MY --per-topic 5

Run it from cron or a scheduled task and send the output to email, Slack or Telegram.
"""
import argparse

from nestdaddy import get

parser = argparse.ArgumentParser(description="NestDaddy daily news digest")
parser.add_argument("--country", default="MY", help="two-letter code for the local section")
parser.add_argument("--per-topic", type=int, default=5)
args = parser.parse_args()

sections = [
    ("World", "/api/v1/news/global", {}),
    ("Tech", "/api/v1/news/tech", {}),
    ("Markets", "/api/v1/news/financial", {}),
    (f"Local ({args.country.upper()})", "/api/v1/news/local", {"country": args.country.upper()}),
]

for name, path, params in sections:
    data = get(path, limit=args.per_topic, **params)
    print(f"\n== {name} ==")
    for a in data.get("articles", [])[: args.per_topic]:
        print(f"- {a['title']} ({a.get('source_domain', '')})\n  {a['url']}")
