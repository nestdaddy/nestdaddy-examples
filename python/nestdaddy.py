"""A tiny NestDaddy API client using only the Python standard library.

Reads the key from the NESTDADDY_API_KEY environment variable. Docs: https://nestdaddy.com/apis
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://nestdaddy.com"


def api_key():
    key = os.environ.get("NESTDADDY_API_KEY", "").strip()
    if not key:
        sys.exit("Set NESTDADDY_API_KEY first. Get a key at https://nestdaddy.com/mcp")
    return key


def get(path, **params):
    """GET an API path and return the decoded JSON. Empty parameters are left out."""
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    url = f"{BASE_URL}{path}" + (f"?{query}" if query else "")
    req = urllib.request.Request(url, headers={
        "X-API-Key": api_key(),
        "Accept": "application/json",
        "User-Agent": "nestdaddy-examples/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            detail = json.load(e)
        except ValueError:
            detail = {}
        sys.exit(f"NestDaddy API error {e.code}: {detail.get('message') or detail.get('error') or e.reason}")
