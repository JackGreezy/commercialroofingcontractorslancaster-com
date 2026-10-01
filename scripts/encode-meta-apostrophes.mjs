// Final prebuild step: write apostrophes inside meta description attributes as &#39; so simple
// attribute parsers (which stop at the first quote character) read the whole description.
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const SKIP = new Set(["node_modules", ".next", ".git", ".vercel"]);
const DIRS = ["public", "data/rendered-pages", "data/leak-first-rendered", "data/audit-recovered-pages", "rendered", ".site/pages"];
function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    if (SKIP.has(e.name)) return [];
    const p = path.join(dir, e.name);
    return e.isDirectory() ? walk(p) : [p];
  });
}
const META = /<meta\b[^>]*>/gi;
const DESC_KEY = /\b(?:name|property)=["'](?:description|og:description|twitter:description)["']/i;
let changed = 0;
for (const file of DIRS.flatMap((d) => walk(path.join(root, d))).filter((f) => f.endsWith(".html"))) {
  const before = fs.readFileSync(file, "utf8");
  const after = before.replace(META, (tag) => {
    if (!DESC_KEY.test(tag)) return tag;
    return tag.replace(/(\bcontent=)"([^"]*)"/i, (_, a, value) => `${a}"${value.replace(/'/g, "&#39;")}"`);
  });
  if (after !== before) {
    fs.writeFileSync(file, after);
    changed++;
  }
}
console.log(`Encoded apostrophes in meta descriptions: ${changed} files`);
