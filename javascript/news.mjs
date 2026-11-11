// News search across 45+ countries, or the latest headlines for one country.
//   node news.mjs "interest rate" US      -> news search in the US, last 7 days
//   node news.mjs --latest SG             -> latest Singapore headlines
import { get } from "./nestdaddy.mjs";

const args = process.argv.slice(2);

if (args[0] === "--latest") {
  const country = (args[1] || "US").toUpperCase();
  const data = await get("/api/v1/news/local", { country, limit: 10 });
  for (const a of data.articles) console.log(`- ${a.title} (${a.source_domain})\n  ${a.url}`);
} else {
  const [query, country] = args;
  if (!query) {
    console.error('Usage: node news.mjs "query" [COUNTRY]  or  node news.mjs --latest [COUNTRY]');
    process.exit(1);
  }
  const data = await get("/api/v1/news/search", { q: query, country, days: 7, limit: 10 });
  console.log(`${data.total} articles found\n`);
  for (const a of data.results) {
    console.log(`[${(a.published_timestamp || "").slice(0, 16)}] ${a.title}\n   ${a.source_domain}  ${a.url}\n`);
  }
}
