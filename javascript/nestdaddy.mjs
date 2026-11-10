// A tiny NestDaddy API client for Node 18+ (built-in fetch, no packages).
// Reads the key from NESTDADDY_API_KEY. Docs: https://nestdaddy.com/apis

const BASE_URL = "https://nestdaddy.com";

export async function get(path, params = {}) {
  const key = (process.env.NESTDADDY_API_KEY || "").trim();
  if (!key) {
    console.error("Set NESTDADDY_API_KEY first. Get a key at https://nestdaddy.com/mcp");
    process.exit(1);
  }
  const qs = new URLSearchParams(
    Object.entries(params).filter(([, v]) => v !== undefined && v !== null && v !== "")
  );
  const res = await fetch(`${BASE_URL}${path}${qs.size ? `?${qs}` : ""}`, {
    headers: { "X-API-Key": key, Accept: "application/json", "User-Agent": "nestdaddy-examples/1.0" },
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(`NestDaddy API error ${res.status}: ${data.message || data.error || res.statusText}`);
  }
  return data;
}
