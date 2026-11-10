// Web search with NestDaddy's own index.
//   node search.mjs "rust error handling"
import { get } from "./nestdaddy.mjs";

const query = process.argv.slice(2).join(" ");
if (!query) {
  console.error('Usage: node search.mjs "your query"');
  process.exit(1);
}

const data = await get("/api/v1/search", { q: query, limit: 5 });
data.results.forEach((r, i) => {
  console.log(`${i + 1}. ${r.title}\n   ${r.url}\n   ${(r.snippet || "").slice(0, 160)}\n`);
});
