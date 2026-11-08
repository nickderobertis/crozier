#!/usr/bin/env node
// One instrumented build per clone. `crozier:test` keeps its coverage profiles in
// target/llvm-cov-gate, because a reach recipe's `llvm-cov clean --profraw-only`
// in target/llvm-cov-target must not erase the ones `workspace:coverage` reports
// on. The profiles sit at each directory's top; the compiled tree is `debug/`, and
// the two directories hold one of those: cargo's own fingerprints then decide what
// is fresh, so a changed input still rebuilds. Idempotent; quiet on success.
// The link is made afresh on every run, never trusted: a restored build cache
// brings it back by name, and on Windows the archive restores it before its
// target exists, as a file symlink cargo cannot enter as a directory.
import { mkdirSync, rmSync, symlinkSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = process.env.CROZIER_SHARED_BUILD_ROOT ?? resolve(dirname(fileURLToPath(import.meta.url)), "..");
const shared = join(root, "target", "llvm-cov-target", "debug");
const link = join(root, "target", "llvm-cov-gate", "debug");

try {
  mkdirSync(shared, { recursive: true });
  mkdirSync(dirname(link), { recursive: true });
  // Removes the link itself, never what it points at.
  rmSync(link, { recursive: true, force: true });
  // A junction takes no privilege on Windows; everywhere else the type is ignored.
  symlinkSync(shared, link, "junction");
} catch (error) {
  console.error(`share-instrumented-build: cannot link ${link} to ${shared}: ${error.message}`);
  console.error("share-instrumented-build: remove target/llvm-cov-gate by hand and re-run");
  process.exit(1);
}
