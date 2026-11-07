// Every pinned suite's live collection against its committed case list, through
// the real command, and that command's refusal when the two differ.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { cpSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import { pytestFiles, suitesIn } from "../core.mjs";

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

test("an unknown suite is refused with the known names", () => {
  const run = command({}, "check", "no-such-suite");
  assert.equal(run.status, 2);
  assert.match(run.stderr, /unknown: no-such-suite/);
  assert.match(run.stderr, /known suites:/);
});

test("pytest's files are read off the target's own command", () => {
  assert.deepEqual(pytestFiles("uv run --locked --all-packages pytest --cov --cov-report= a_test.py b_test.py"), ["a_test.py", "b_test.py"]);
  assert.throws(() => pytestFiles("cargo nextest run"), /runs no pytest/);
});
