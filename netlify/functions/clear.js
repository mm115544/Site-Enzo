import { getStore } from "@netlify/blobs";

export default async (req) => {
  const expected = process.env.ADMIN_PASSWORD;
  const provided = req.headers.get("x-admin-password") || "";

  if (!expected || provided !== expected) {
    return new Response(JSON.stringify({ error: "unauthorized" }), {
      status: 401,
      headers: { "content-type": "application/json" },
    });
  }

  if (req.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  try {
    const store = getStore("visits");
    const { blobs } = await store.list();
    await Promise.all(blobs.map(b => store.delete(b.key)));

    return new Response(JSON.stringify({ ok: true, deleted: blobs.length }), {
      status: 200,
      headers: { "content-type": "application/json", "cache-control": "no-store" },
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: "store", message: String(e) }), {
      status: 500,
      headers: { "content-type": "application/json" },
    });
  }
};

export const config = { path: "/api/clear" };
