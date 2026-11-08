// The results the CI lanes carry between runners, served to Nx over its self-hosted cache
// protocol on loopback. A plain restore of `.nx/cache` replays nothing on a new runner: Nx
// finds entries through a database named after the machine's id, so another machine never
// sees them. Over this protocol Nx asks by input hash alone, and unpacks the entry's outputs.
//
// Holds one tarball per hash under `directory`. Hashes are held to digits and letters at
// this boundary, because they become file names.
import { randomBytes } from "node:crypto";
import { createReadStream, createWriteStream, existsSync, mkdirSync, renameSync, rmSync } from "node:fs";
import { createServer } from "node:http";
import { join } from "node:path";
import { pipeline } from "node:stream/promises";

const ROUTE = /^\/v1\/cache\/([A-Za-z0-9]+)$/;

/** Start serving `directory`; answers the environment Nx needs, and how to stop. */
export async function serveResults(directory) {
  mkdirSync(directory, { recursive: true });
  const token = randomBytes(24).toString("hex");
  const server = createServer(async (request, response) => {
    const answer = (status) => {
      response.statusCode = status;
      response.end();
    };
    const hash = ROUTE.exec(request.url ?? "")?.[1];
    if (request.headers.authorization !== `Bearer ${token}`) return answer(401);
    if (!hash) return answer(404);
    const path = join(directory, `${hash}.tar`);
    try {
      if (request.method === "GET") {
        if (!existsSync(path)) return answer(404);
        response.setHeader("Content-Type", "application/octet-stream");
        await pipeline(createReadStream(path), response);
        return undefined;
      }
      if (request.method === "PUT") {
        if (existsSync(path)) return answer(409);
        const partial = `${path}.${process.pid}.partial`;
        try {
          await pipeline(request, createWriteStream(partial));
          renameSync(partial, path);
        } finally {
          rmSync(partial, { force: true });
        }
        return answer(200);
      }
      return answer(405);
    } catch {
      // A failed transfer is a cache miss for Nx, never a failed target.
      return response.headersSent ? response.destroy() : answer(500);
    }
  });
  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });
  return {
    env: { NX_SELF_HOSTED_REMOTE_CACHE_SERVER: `http://127.0.0.1:${server.address().port}`, NX_SELF_HOSTED_REMOTE_CACHE_ACCESS_TOKEN: token },
    stop: () => new Promise((resolve) => { server.closeAllConnections(); server.close(resolve); }),
  };
}
