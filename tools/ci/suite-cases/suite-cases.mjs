#!/usr/bin/env node
// Compare each pinned suite's live collection with its committed case list.
//
//   node tools/ci/suite-cases/suite-cases.mjs check [NAME...]
//   node tools/ci/suite-cases/suite-cases.mjs write NAME...
//
// Quiet on success (one line). `write` re-pins a named suite only, after a change
// that deliberately adds or removes cases. It writes tools/ci/lanes.json's
// `e2eCases` (count and digest) from the same pins in the same step, and refuses —
// writing nothing — when an e2e case the committed pins hold is in none of the
// new ones: a lost case still fails. A case removed on purpose is named in
// CROZIER_SUITE_CASES_RETIRE (comma-separated test paths) for that one write;
// naming a case the write does not lose is refused too.
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { readFileSync } from "node:fs";
import { E2E_SUITE, collect, difference, e2eCaseList, e2eCasesRecord, lanesPath, pinPath, readPin, suitesIn, writeTogether } from "./core.mjs";

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
  const fresh = new Map(suites.map((suite) => [suite.name, collect(root, suite)]));
  let lanes;
  try {
    lanes = JSON.parse(readFileSync(lanesPath(root), "utf8"));
  } catch (error) {
    console.error(`suite-cases: cannot read ${lanesPath(root)}: ${error.message}; restore it with git checkout -- tools/ci/lanes.json`);
    process.exit(1);
  }
  const record = lanes?.e2eCases;
  if (
    !record ||
    typeof record !== "object" ||
    !known.some((suite) => suite.name === record.moved) ||
    typeof record.sha256 !== "string" ||
    !Number.isInteger(record.count)
  ) {
    console.error(
      `suite-cases: ${lanesPath(root)} carries no e2eCases record naming a known suite as \`moved\` with a \`sha256\` and an integer \`count\`; nothing was written. Restore it with git checkout -- tools/ci/lanes.json`,
    );
    process.exit(1);
  }
  const pinned = (name) => readPin(root, known.find((suite) => suite.name === name));
  const current = (name) => fresh.get(name) ?? pinned(name);
  const before = e2eCaseList(pinned(E2E_SUITE), pinned(lanes.e2eCases.moved));
  const after = e2eCaseList(current(E2E_SUITE), current(lanes.e2eCases.moved));
  const retired = new Set((process.env.CROZIER_SUITE_CASES_RETIRE ?? "").split(",").map((name) => name.trim()).filter(Boolean));
  const kept = new Set(after);
  const lost = before.filter((name) => !kept.has(name) && !retired.has(name));
  const removed = new Set(before.filter((name) => !kept.has(name)));
  const mistaken = [...retired].filter((name) => !removed.has(name));
  if (mistaken.length) {
    for (const name of mistaken) console.error(`suite-cases: CROZIER_SUITE_CASES_RETIRE names ${name}, which this write does not lose`);
    console.error("suite-cases: nothing was written. Name exactly the cases this write removes");
    process.exit(1);
  }
  if (lost.length) {
    for (const name of lost) console.error(`suite-cases: e2e case lost: ${name}`);
    console.error(
      "suite-cases: nothing was written. Restore the lost case(s), or, if a removal is deliberate, rerun with CROZIER_SUITE_CASES_RETIRE=<test path>[,<test path>] naming each",
    );
    process.exit(1);
  }
  const files = new Map([...fresh].map(([name, cases]) => [pinPath(root, known.find((suite) => suite.name === name)), `${cases.join("\n")}\n`]));
  const measured = e2eCasesRecord(after);
  const changed = measured.sha256 !== record.sha256 || measured.count !== record.count;
  if (changed) files.set(lanesPath(root), `${JSON.stringify({ ...lanes, e2eCases: { ...record, ...measured } }, null, 2)}\n`);
  writeTogether(files);
  console.log(`suite-cases: wrote ${suites.length} pin(s)${changed ? ` and tools/ci/lanes.json's e2eCases (${measured.count} cases)` : ""}`);
  process.exit(0);
}
const failures = suites.flatMap((suite) => difference(suite.name, readPin(root, suite), collect(root, suite)));
if (failures.length) {
  for (const failure of failures) console.error(failure);
  console.error("suite-cases: a suite's collected cases changed. Restore them, or, if the change is deliberate, run `node tools/ci/suite-cases/suite-cases.mjs write NAME` and commit the pin");
  process.exit(1);
}
console.log(`suite-cases: ${suites.length} suite(s) collect exactly their pinned cases`);
