import { getStore } from "@netlify/blobs";

export default async (req, context) => {
  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  let body = {};
  try { body = await req.json(); } catch (_) {}

  const ua = req.headers.get("user-agent") || "";

  if (isBot(ua)) {
    return new Response(JSON.stringify({ ok: true, skipped: "bot" }), {
      status: 200,
      headers: { "content-type": "application/json", "cache-control": "no-store" },
    });
  }
  const ip =
    req.headers.get("x-nf-client-connection-ip") ||
    (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() ||
    "";
  const referrer = req.headers.get("referer") || "";
  const geo = context.geo || {};

  const visit = {
    timestamp: new Date().toISOString(),
    ip,
    country: geo.country?.name || geo.country?.code || "",
    countryCode: geo.country?.code || "",
    city: geo.city || "",
    subdivision: geo.subdivision?.name || "",
    referrer,
    userAgent: ua,
    screen: typeof body.screen === "string" ? body.screen.slice(0, 20) : "",
    lang: typeof body.lang === "string" ? body.lang.slice(0, 20) : "",
    tz: typeof body.tz === "string" ? body.tz.slice(0, 64) : "",
    ...parseUA(ua),
  };

  try {
    const store = getStore("visits");
    const key = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
    await store.setJSON(key, visit);
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: "store" }), {
      status: 500,
      headers: { "content-type": "application/json" },
    });
  }

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });
};

function parseUA(ua) {
  let browser = "Inconnu";
  let os = "Inconnu";
  let device = "Desktop";

  if (/iPad/.test(ua)) { os = "iPadOS"; device = "Tablet"; }
  else if (/iPhone|iPod/.test(ua)) { os = "iOS"; device = "Mobile"; }
  else if (/Android/.test(ua)) {
    os = "Android";
    device = /Mobile/.test(ua) ? "Mobile" : "Tablet";
  }
  else if (/Windows NT/.test(ua)) os = "Windows";
  else if (/Mac OS X/.test(ua)) os = "macOS";
  else if (/CrOS/.test(ua)) os = "ChromeOS";
  else if (/Linux/.test(ua)) os = "Linux";

  if (/Instagram/.test(ua)) browser = "Instagram (in-app)";
  else if (/FBAN|FBAV|FB_IAB/.test(ua)) browser = "Facebook (in-app)";
  else if (/TikTok/i.test(ua)) browser = "TikTok (in-app)";
  else if (/Snapchat/i.test(ua)) browser = "Snapchat (in-app)";
  else if (/Twitter/i.test(ua)) browser = "X/Twitter (in-app)";
  else if (/EdgiOS|Edg/.test(ua)) browser = "Edge";
  else if (/OPR|Opera/.test(ua)) browser = "Opera";
  else if (/Firefox|FxiOS/.test(ua)) browser = "Firefox";
  else if (/CriOS/.test(ua)) browser = "Chrome iOS";
  else if (/Chrome/.test(ua)) browser = "Chrome";
  else if (/Safari/.test(ua)) browser = "Safari";

  return { browser, os, device };
}

function isBot(ua) {
  if (!ua) return true;
  return /Headless|bot|crawler|spider|curl|wget|node-fetch|axios|python-requests|Go-http-client|facebookexternalhit|Pingdom|UptimeRobot|GTmetrix|Lighthouse|monitoring|preview|prerender/i.test(ua);
}

export const config = { path: "/api/track" };
