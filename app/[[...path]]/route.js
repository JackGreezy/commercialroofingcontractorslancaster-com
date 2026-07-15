import fs from "node:fs/promises";
import path from "node:path";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

const publicDir = path.join(process.cwd(), "public");
const analytics = '<script defer src="/_vercel/insights/script.js" data-sdkn="@vercel/analytics/next" data-sdkv="2.0.1"></script>';

function withVercelAnalytics(html) {
  if (!html || html.includes("/_vercel/insights/script.js")) return html;
  return /<\/head>/i.test(html) ? html.replace(/<\/head>/i, `${analytics}\n</head>`) : `${analytics}\n${html}`;
}

function routeFromParams(params = {}) {
  const parts = Array.isArray(params.path) ? params.path : [];
  return parts.map((part) => String(part).replace(/[^a-zA-Z0-9._-]/g, "")).filter(Boolean);
}

function pageCandidates(parts) {
  if (!parts.length) return [path.join(publicDir, "index.html")];
  const clean = parts.join("/");
  return [path.join(publicDir, `${clean}.html`), path.join(publicDir, clean, "index.html")];
}

async function readFirst(candidates) {
  for (const file of candidates) {
    if (!file.startsWith(publicDir + path.sep)) continue;
    try {
      return await fs.readFile(file, "utf8");
    } catch (error) {
      if (error?.code !== "ENOENT") throw error;
    }
  }
  return null;
}

function withRuntimeAdditions(html, request) {
  if (!html) return html;
  const url = new URL(request.url);
  if (url.searchParams.get("submitted") === "1" && /<\/form>/i.test(html)) {
    const notice = '<p role="status" style="margin-top:20px;font-weight:700">Thank you. Your commercial roofing request has been received.</p>';
    return html.replace(/<\/form>/i, `</form>${notice}`);
  }
  return html;
}

async function htmlResponse(parts, request, status = 200) {
  const html = await readFirst(pageCandidates(parts));
  if (!html) return null;
  return new Response(withVercelAnalytics(withRuntimeAdditions(html, request)), {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "public, max-age=0, s-maxage=3600, stale-while-revalidate=86400"
    }
  });
}

export async function GET(request, context) {
  const parts = routeFromParams(await context.params);
  const page = await htmlResponse(parts, request);
  if (page) return page;
  const notFound = await htmlResponse(["404"], request, 404);
  return notFound || new Response("Not found", { status: 404 });
}
