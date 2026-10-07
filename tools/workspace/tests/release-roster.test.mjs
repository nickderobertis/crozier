// release-plz versions, changelogs and tags only the `crozier` package; every
// test-only workspace member (`publish = false`) is listed in release-plz.toml
// with `release = false`. That roster restates the workspace's, so this
// reconciles the two through the real `cargo metadata`: a member added, renamed
// or removed without its release-plz entry fails here, instead of being released
// by default or leaving a stale entry that names nothing.
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");

function members() {
  const metadata = JSON.parse(
    execFileSync("cargo", ["metadata", "--format-version", "1", "--no-deps", "--locked"], {
      cwd: ROOT, encoding: "utf8", maxBuffer: 64 * 1024 * 1024,
    }),
  );
  // `publish = false` reads back as an empty registry list; unset is null.
  return metadata.packages.map((pkg) => ({ name: pkg.name, private: Array.isArray(pkg.publish) && pkg.publish.length === 0 }));
}

function unreleased() {
  const text = readFileSync(join(ROOT, "release-plz.toml"), "utf8");
  return text
    .split("[[package]]")
    .slice(1)
    .filter((block) => /^\s*release\s*=\s*false\s*(#.*)?$/m.test(block))
    .map((block) => {
      const name = /^\s*name\s*=\s*"([^"]+)"/m.exec(block);
      assert.ok(name, `a release-plz [[package]] entry names no package:\n${block}`);
      return name[1];
    })
    .sort();
}

test("every test-only member, and nothing else, is kept out of releases", () => {
  const all = members();
  assert.ok(all.some(({ name, private: isPrivate }) => name === "crozier" && !isPrivate), "crozier must stay publishable");
  assert.deepEqual(
    unreleased(),
    all.filter(({ private: isPrivate }) => isPrivate).map(({ name }) => name).sort(),
    "release-plz.toml's `release = false` entries must be exactly the `publish = false` workspace members; add or remove the [[package]] entry for the member that moved",
  );
});
