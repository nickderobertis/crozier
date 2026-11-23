// Every pinned suite's live collection against its committed case list, through
// the real command, and that command's refusal when the two differ.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { cpSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import { collect, pytestFiles, suitesIn, writeTogether } from "../core.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");
const SCRIPT = join(ROOT, "tools/ci/suite-cases/suite-cases.mjs");
// The pins were taken on Linux; a Windows or macOS collection is the re-measure's to confirm.
const LINUX = process.platform === "linux" ? {} : { skip: "pins record this suite's Linux collection" };

function command(env, ...args) {
  return spawnSync(process.execPath, [SCRIPT, ...args], { cwd: ROOT, encoding: "utf8", maxBuffer: 64 * 1024 * 1024, env: { ...process.env, ...env } });
}

test("every pinned suite collects exactly its committed cases", LINUX, () => {
  const run = command({}, "check");
  assert.equal(run.status, 0, run.stderr);
  assert.match(run.stdout, /collect exactly their pinned cases/);
});

test("a lost or gained case fails the check, names the case and leaves the pin alone", LINUX, () => {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-suite-cases-"));
  try {
    const [suite] = suitesIn(ROOT);
    cpSync(join(ROOT, "tools/ci/suite-cases/pins"), scratch, { recursive: true });
    const pin = join(scratch, `${suite.name}.txt`);
    const [first, ...rest] = readFileSync(pin, "utf8").split("\n");
    const tampered = ["tools/imaginary_test.py::never_collected", ...rest].join("\n");
    writeFileSync(pin, tampered);
    const run = command({ CROZIER_SUITE_CASES_PINS: scratch }, "check", suite.name);
    assert.equal(run.status, 1, run.stderr);
    assert.match(run.stderr, new RegExp(`${suite.name}: lost tools/imaginary_test.py::never_collected`));
    assert.ok(run.stderr.includes(`${suite.name}: gained ${first}`), run.stderr);
    assert.match(run.stderr, /suite-cases.mjs write NAME/);
    assert.equal(readFileSync(pin, "utf8"), tampered);
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
});

// Issue #887: a repin writes lanes.json's e2eCases from the same pins in the same
// step, and a case the committed pins held that no new pin holds refuses the
// whole write. Driven over the cheapest pin feeding e2eCases, the tooling journeys'.
test("a repin refreshes lanes.json's e2e count with its pins, and a lost case writes nothing", LINUX, () => {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-suite-cases-"));
  try {
    const pins = join(scratch, "pins");
    const lanes = join(scratch, "lanes.json");
    cpSync(join(ROOT, "tools/ci/suite-cases/pins"), pins, { recursive: true });
    const committed = readFileSync(join(ROOT, "tools/ci/lanes.json"), "utf8");
    const { e2eCases } = JSON.parse(committed);
    const env = { CROZIER_SUITE_CASES_PINS: pins, CROZIER_SUITE_CASES_LANES: lanes };
    const journeys = join(pins, `${e2eCases.moved}.txt`);
    const pinned = readFileSync(journeys, "utf8");

    // A stale inventory: the pins gained a case lanes.json does not count yet.
    const [dropped, ...rest] = pinned.trimEnd().split("\n");
    writeFileSync(journeys, `${rest.join("\n")}\n`);
    writeFileSync(lanes, committed.replace(`"count": ${e2eCases.count}`, `"count": ${e2eCases.count - 1}`).replace(e2eCases.sha256, "0".repeat(64)));
    const repinned = command(env, "write", e2eCases.moved);
    assert.equal(repinned.status, 0, repinned.stderr);
    assert.match(repinned.stdout, new RegExp(`and tools/ci/lanes.json's e2eCases \\(${e2eCases.count} cases\\)`));
    assert.ok(readFileSync(journeys, "utf8").includes(`${dropped}\n`), "the pin was not rewritten");
    assert.equal(readFileSync(lanes, "utf8"), committed, "lanes.json is not the committed inventory");

    // A case the committed pins hold that the collection lost: nothing is written.
    const lost = `${pinned}crozier-tool-journeys::tool_journeys imaginary::never_collected\n`;
    writeFileSync(journeys, lost);
    const refused = command(env, "write", e2eCases.moved);
    assert.equal(refused.status, 1, refused.stderr);
    assert.match(refused.stderr, /e2e case lost: imaginary::never_collected/);
    assert.match(refused.stderr, /nothing was written.*CROZIER_SUITE_CASES_RETIRE/);
    assert.equal(readFileSync(journeys, "utf8"), lost, "the pin was rewritten after a lost case");
    assert.equal(readFileSync(lanes, "utf8"), committed);

    // A retirement naming a case the write does not lose is refused, so a typo cannot hide a loss.
    const typo = command({ ...env, CROZIER_SUITE_CASES_RETIRE: "imaginary::never_colected" }, "write", e2eCases.moved);
    assert.equal(typo.status, 1, typo.stderr);
    assert.match(typo.stderr, /names imaginary::never_colected, which this write does not lose/);
    assert.equal(readFileSync(journeys, "utf8"), lost);

    // Named as retired, the same removal is repinned, lanes.json with it.
    const retired = command({ ...env, CROZIER_SUITE_CASES_RETIRE: "imaginary::never_collected" }, "write", e2eCases.moved);
    assert.equal(retired.status, 0, retired.stderr);
    assert.equal(readFileSync(journeys, "utf8"), pinned);
    assert.equal(readFileSync(lanes, "utf8"), committed);
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
});

test("a repin refuses a lanes.json whose e2eCases record is malformed, writing nothing", () => {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-suite-cases-"));
  try {
    const pins = join(scratch, "pins");
    const lanes = join(scratch, "lanes.json");
    cpSync(join(ROOT, "tools/ci/suite-cases/pins"), pins, { recursive: true });
    const committed = JSON.parse(readFileSync(join(ROOT, "tools/ci/lanes.json"), "utf8"));
    const env = { CROZIER_SUITE_CASES_PINS: pins, CROZIER_SUITE_CASES_LANES: lanes };
    const journeys = join(pins, `${committed.e2eCases.moved}.txt`);
    const pinned = readFileSync(journeys, "utf8");
    for (const [label, text] of [
      ["no JSON", "{"],
      ["no e2eCases", JSON.stringify({ ...committed, e2eCases: undefined })],
      ["an unknown moved suite", JSON.stringify({ ...committed, e2eCases: { ...committed.e2eCases, moved: "no-such-suite" } })],
      ["a count that is no integer", JSON.stringify({ ...committed, e2eCases: { ...committed.e2eCases, count: "12" } })],
    ]) {
      writeFileSync(lanes, text);
      const refused = command(env, "write", committed.e2eCases.moved);
      assert.equal(refused.status, 1, `${label}: ${refused.stderr}`);
      assert.match(refused.stderr, /restore it with git checkout -- tools\/ci\/lanes\.json/i, label);
      assert.equal(readFileSync(lanes, "utf8"), text, `${label}: lanes.json was rewritten`);
      assert.equal(readFileSync(journeys, "utf8"), pinned, `${label}: the pin was rewritten`);
    }
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
});

test("a write that fails part-way restores every file it already moved into place", () => {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-suite-cases-"));
  try {
    const pin = join(scratch, "pin.txt");
    const fresh = join(scratch, "fresh.txt");
    const lanes = join(scratch, "lanes.json");
    writeFileSync(pin, "committed\n");
    // A directory where lanes.json belongs: its rename fails after the others succeed.
    mkdirSync(lanes);
    writeFileSync(join(lanes, "occupied"), "");
    assert.throws(() => writeTogether(new Map([[pin, "repinned\n"], [fresh, "new\n"], [lanes, "{}\n"]])));
    assert.equal(readFileSync(pin, "utf8"), "committed\n", "the pin kept the repinned bytes");
    assert.deepEqual(readdirSync(scratch).sort(), ["lanes.json", "pin.txt"], "a new file or a staged one was left");
    rmSync(lanes, { recursive: true });
    writeTogether(new Map([[pin, "repinned\n"], [lanes, "{}\n"]]));
    assert.equal(readFileSync(pin, "utf8"), "repinned\n");
    assert.equal(readFileSync(lanes, "utf8"), "{}\n");
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
});

test("an unknown suite is refused with the known names", () => {
  const run = command({}, "check", "no-such-suite");
  assert.equal(run.status, 2);
  assert.match(run.stderr, /unknown: no-such-suite/);
  assert.match(run.stderr, /known suites:/);
});

test("pytest's files are read off the target's own command", () => {
  assert.deepEqual(pytestFiles("uv run --locked --all-packages pytest --cov --cov-report= a_test.py b_test.py"), ["a_test.py", "b_test.py"]);
  assert.deepEqual(pytestFiles("uv run pytest --cov --deselect=a_test.py::Slow a_test.py"), ["--deselect=a_test.py::Slow", "a_test.py"], "what a target deselects, its collection does too");
  assert.throws(() => pytestFiles("cargo nextest run"), /runs no pytest/);
});

test("the census's two halves run every census case exactly once between them", LINUX, () => {
  const suites = suitesIn(ROOT);
  const half = (name) => collect(ROOT, suites.find((suite) => suite.name === name));
  const [census, verdicts] = [half("surface-census-test-census"), half("surface-census-test-census-verdicts")];
  assert.ok(verdicts.length > 0, "the verdicts half collects cases");
  assert.deepEqual(census.filter((id) => verdicts.includes(id)), [], "no case runs in both halves");
  // The whole of the census's files, as one pytest collection of them sees it.
  const project = JSON.parse(readFileSync(join(ROOT, "tools/surface-census/project.json"), "utf8"));
  const files = pytestFiles(project.targets["test-census"].options.command).filter((word) => !word.startsWith("--"));
  const whole = spawnSync("uv", ["run", "--locked", "--all-packages", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", ...files], { cwd: ROOT, encoding: "utf8", maxBuffer: 64 * 1024 * 1024 });
  assert.equal(whole.status, 0, whole.stderr);
  const all = whole.stdout.split(/\r?\n/).filter((line) => line.includes("::"));
  assert.deepEqual([...census, ...verdicts].sort(), all.sort(), "together the halves are the whole census");
});
