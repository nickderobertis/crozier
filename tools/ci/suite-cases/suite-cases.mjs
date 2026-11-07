#!/usr/bin/env node
// Compare each pinned suite's live collection with its committed case list.
//
//   node tools/ci/suite-cases/suite-cases.mjs check [NAME...]
//   node tools/ci/suite-cases/suite-cases.mjs write NAME...
//
// Quiet on success (one line). `write` re-pins a named suite only, after a change
// that deliberately adds or removes cases.
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { collect, difference, readPin, suitesIn, writePin } from "./core.mjs";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
const [verb, ...names] = process.argv.slice(2);
const known = suitesIn(root);
const unknown = names.filter((name) => !known.some((suite) => suite.name === name));
if (!["check", "write"].includes(verb) || unknown.length || (verb === "write" && !names.length)) {
  console.error(`suite-cases: usage: suite-cases.mjs check [NAME...] | write NAME...${unknown.length ? ` (unknown: ${unknown.join(", ")})` : ""}`);
  console.error(`suite-cases: known suites: ${known.map((suite) => suite.name).join(", ")}`);
  process.exit(2);
}
// A suite another project's target checks is left to it: this project's inputs may not reach that project.
const suites = known.filter((suite) => (names.length ? names.includes(suite.name) : !suite.checkedBy));
if (verb === "write") {
  for (const suite of suites) writePin(root, suite, collect(root, suite));
  console.log(`suite-cases: wrote ${suites.length} pin(s)`);
  process.exit(0);
}
const failures = suites.flatMap((suite) => difference(suite.name, readPin(root, suite), collect(root, suite)));
if (failures.length) {
  for (const failure of failures) console.error(failure);
  console.error("suite-cases: a suite's collected cases changed. Restore them, or, if the change is deliberate, run `node tools/ci/suite-cases/suite-cases.mjs write NAME` and commit the pin");
  process.exit(1);
}
console.log(`suite-cases: ${suites.length} suite(s) collect exactly their pinned cases`);
