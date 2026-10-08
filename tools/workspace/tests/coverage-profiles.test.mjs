// `crozier:test` writes the coverage profiles and `workspace:coverage` reports on
// them, each naming the profile directory in its own project.json. The two must
// name the same directory, or the report reads a directory the suite never
// wrote. This reconciles the two settings, so neither project can move it alone;
// `workspace:lint` runs it, beside the other checks over the project files.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");

function profileDirectory(projectFile, target) {
  const project = JSON.parse(readFileSync(join(ROOT, projectFile), "utf8"));
  const directory = project.targets?.[target]?.options?.env?.CARGO_LLVM_COV_TARGET_DIR;
  assert.ok(directory, `${projectFile} ${target} sets no CARGO_LLVM_COV_TARGET_DIR`);
  return directory;
}

test("the coverage report reads the profile directory the suite writes", () => {
  assert.equal(
    profileDirectory("tools/workspace/project.json", "coverage"),
    profileDirectory("src/project.json", "test"),
    "crozier:test and workspace:coverage name different CARGO_LLVM_COV_TARGET_DIR values; set both to one directory",
  );
});
