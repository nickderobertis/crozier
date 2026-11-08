#!/usr/bin/env node
// Every project.json's digest, as a runtime input of `ci-journeys:test`, whose inventory and
// selection journeys read all of them, and of `lane-inventory:lint`. The boundary rule forbids
// a tooling target naming a tier's files, so an edit to one misses the journeys' cache here
// without making them affected; `lane-inventory:lint` is what that edit selects, and fails.
// It must never fail: a failing runtime input stops Nx hashing the whole run.
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";

const listing = spawnSync("git", ["ls-files", "-co", "--exclude-standard", "-z", "--", "*project.json"], { encoding: "utf8" });
const hash = createHash("sha256");
// A failed listing must not read as an empty, cacheable one: this hash then matches nothing.
if (listing.status !== 0) hash.update(`listing failed ${listing.status} ${process.pid} ${Date.now()} ${listing.stderr}`);
for (const path of (listing.stdout ?? "").split("\0").filter(Boolean).sort()) {
  hash.update(path).update("\0");
  try {
    hash.update(readFileSync(path));
  } catch {
    hash.update("unreadable");
  }
}
console.log(hash.digest("hex"));
