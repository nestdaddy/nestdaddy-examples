# curl examples

Set your key once (get one at [nestdaddy.com/mcp](https://nestdaddy.com/mcp)):

```bash
export NESTDADDY_API_KEY="your_key"
```

## Web search

```bash
curl -s "https://nestdaddy.com/api/v1/search?q=python+asyncio+guide&limit=5" \
  -H "X-API-Key: $NESTDADDY_API_KEY"
```

## News search (worldwide, last 120 days)

```bash
curl -s "https://nestdaddy.com/api/v1/news/search?q=interest+rate&country=US&days=7&limit=10" \
  -H "X-API-Key: $NESTDADDY_API_KEY"
```

`country` is a two-letter code (US, GB, SG, ID, MY ...), `topic` is one of `global`, `tech`,
`financial`, `local`, `days` is 1 to 120, `limit` is 1 to 50.

## Latest headlines

```bash
curl -s "https://nestdaddy.com/api/v1/news/global?limit=10"    -H "X-API-Key: $NESTDADDY_API_KEY"
curl -s "https://nestdaddy.com/api/v1/news/tech?limit=10"      -H "X-API-Key: $NESTDADDY_API_KEY"
curl -s "https://nestdaddy.com/api/v1/news/financial?limit=10" -H "X-API-Key: $NESTDADDY_API_KEY"
curl -s "https://nestdaddy.com/api/v1/news/local?country=SG&limit=10" -H "X-API-Key: $NESTDADDY_API_KEY"
```

## Read a page in full

```bash
curl -s "https://nestdaddy.com/api/v1/extract?url=https://peps.python.org/pep-3156/&max_chars=3000" \
  -H "X-API-Key: $NESTDADDY_API_KEY"
```

## Research papers

```bash
curl -s "https://nestdaddy.com/api/v1/research?q=retrieval+augmented+generation&per_page=5" \
  -H "X-API-Key: $NESTDADDY_API_KEY"
```

Every response includes a `quota` object with `used`, `limit` and `remaining`.
Full reference: [nestdaddy.com/apis](https://nestdaddy.com/apis).
