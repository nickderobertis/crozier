// One compile of crozier per profile within a job, through the commands the gate
// and the suites really run. The compile is a scratch copy's, in its own target
// directory; its dependencies come from the real manifests and lock, so a feature
// split between `crozier:build` and a suite's build fails here.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { appendFileSync, cpSync, existsSync, lstatSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { after, before, test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");
const SHARE = join(ROOT, "scripts/share-instrumented-build.mjs");
const COPIED = ["Cargo.toml", "Cargo.lock", "rust-toolchain.toml", ".cargo", "src", "templates", "assets", "crates/crozier-e2e", "tests/support", "tests/nested-discriminator/golden", "pool-maintenance", "tools/ci", "tools/ci-journeys", "tools/github-action", "README.md", "LICENSE", "NOTICE", "licenses"];

function target(project, name) {
  return JSON.parse(readFileSync(join(ROOT, project, "project.json"), "utf8")).targets[name].options;
}

/** A target's cargo command, split, with `extra` before any `--` it does not have. */
function cargoArgs(command, ...extra) {
  const words = command.match(/"[^"]*"|\S+/g).map((word) => word.replace(/^"|"$/g, ""));
  assert.equal(words[0], "cargo", command);
  return [...words.slice(1), ...extra];
}

function cargo(cwd, args, env = {}) {
  const { CARGO_TARGET_DIR: _outerTarget, ...inherited } = process.env;
  const run = spawnSync("cargo", args, { cwd, encoding: "utf8", maxBuffer: 256 * 1024 * 1024, env: { ...inherited, ...env } });
  assert.equal(run.status, 0, `cargo ${args.join(" ")}\n${run.stdout?.slice(-2000)}\n${run.stderr?.slice(-4000)}`);
  return run;
}

/** Whether cargo compiled (true) or reused (false) each crozier artifact a JSON-message build reports, by target kind. */
function crozierUnits(stdout) {
  const units = {};
  for (const line of stdout.split(/\r?\n/)) {
    if (!line.startsWith("{")) continue;
    const message = JSON.parse(line);
    if (message.reason === "compiler-artifact" && message.target.name === "crozier" && !message.profile.test) {
      units[message.target.kind[0]] = !message.fresh;
    }
  }
  return units;
}

const build = (cwd) => crozierUnits(cargo(cwd, cargoArgs(target("src", "build").command, "--message-format=json")).stdout);
const suiteBuild = (cwd) => crozierUnits(cargo(cwd, cargoArgs(target("crates/crozier-e2e", "test").command, "--no-run", "--cargo-message-format", "json")).stdout);
// The build tests/corpus_match/match.sh starts with; `corpus-match` is a tier, so this project cannot read it.
const matchBuild = (cwd) => crozierUnits(cargo(cwd, ["build", "--locked", "--quiet", "-p", "crozier", "--bin", "crozier", "--message-format=json"]).stdout);

let scratch;
before(() => {
  scratch = mkdtempSync(join(tmpdir(), "crozier-build-reuse-"));
  for (const path of COPIED) cpSync(join(ROOT, path), join(scratch, path), { recursive: true });
  // The real manifest and so the real feature resolution; the suite's sources embed
  // committed documents and take minutes to compile, and what they say is not at stake.
  writeFileSync(join(scratch, "crates/crozier-e2e/tests/e2e.rs"), "#[test]\nfn compiles() {}\n");
});
after(() => rmSync(scratch, { recursive: true, force: true }));

test("a later step uses the build the first produced, and a changed source rebuilds it for both", () => {
  assert.deepEqual(build(scratch), { lib: true, bin: true }, "the first step compiles crozier");
  const binary = join(scratch, "target/debug", `crozier${process.platform === "win32" ? ".exe" : ""}`);
  const built = statSync(binary).mtimeMs;
  assert.deepEqual(suiteBuild(scratch), { lib: false }, "a suite's build reuses crozier's library rather than compiling its own");
  assert.deepEqual(matchBuild(scratch), { lib: false, bin: false }, "the corpus recipe reuses crozier");
  assert.deepEqual(build(scratch), { lib: false, bin: false }, "a later `crozier:build` still answers from the first");
  assert.equal(statSync(binary).mtimeMs, built, "no later step rewrote the binary");

  appendFileSync(join(scratch, "src/lib.rs"), "\n// a changed input\n");
  assert.deepEqual(suiteBuild(scratch), { lib: true }, "a changed source reaches the suite's build");
  assert.deepEqual(build(scratch), { lib: false, bin: true }, "and the binary links the rebuilt library, once");
  assert.notEqual(statSync(binary).mtimeMs, built);
});

test("other compiler flags compile their own build instead of taking this one", () => {
  build(scratch);
  const flags = crozierUnits(cargo(scratch, cargoArgs(target("src", "build").command, "--message-format=json"), { RUSTFLAGS: "--cfg crozier_reuse_probe" }).stdout);
  assert.deepEqual(flags, { lib: true, bin: true });
});

function miniWorkspace() {
  const root = mkdtempSync(join(tmpdir(), "crozier-shared-build-"));
  writeFileSync(join(root, "Cargo.toml"), '[package]\nname = "lantern"\nversion = "0.0.0"\nedition = "2021"\n\n[workspace]\n');
  mkdirSync(join(root, "src"));
  writeFileSync(join(root, "src/lib.rs"), "pub fn lit() -> bool { true }\n\n#[test]\nfn is_lit() { assert!(lit()); }\n");
  cpSync(join(ROOT, "rust-toolchain.toml"), join(root, "rust-toolchain.toml"));
  cargo(root, ["generate-lockfile", "--offline"]);
  return root;
}

const profiles = (directory) => (existsSync(directory) ? readdirSync(directory).filter((name) => name.endsWith(".profraw")) : []);

test("the gate's and the reach recipes' instrumented runs share one compile and keep their own profiles", () => {
  const root = miniWorkspace();
  try {
    const share = () => {
      const run = spawnSync(process.execPath, [SHARE], { encoding: "utf8", env: { ...process.env, CROZIER_SHARED_BUILD_ROOT: root } });
      assert.equal(run.status, 0, run.stderr);
      assert.equal(run.stdout + run.stderr, "", "quiet on success");
    };
    const coverage = (env, ...args) => cargo(root, ["llvm-cov", "--no-report", "nextest", ...args], env).stderr;
    const gate = { CARGO_LLVM_COV_TARGET_DIR: "target/llvm-cov-gate" };
    share();
    share();
    assert.ok(lstatSync(join(root, "target/llvm-cov-gate/debug")).isSymbolicLink());

    assert.match(coverage(gate), /Compiling lantern/, "the gate compiles the instrumented build");
    const held = profiles(join(root, "target/llvm-cov-gate"));
    assert.ok(held.length > 0, "the gate wrote its profiles");
    assert.doesNotMatch(coverage({}), /Compiling lantern/, "the reach recipe's directory reuses that compile");
    cargo(root, ["llvm-cov", "clean", "--profraw-only"]);
    assert.deepEqual(profiles(join(root, "target/llvm-cov-target")), [], "the reach recipe clears its own profiles");
    assert.deepEqual(profiles(join(root, "target/llvm-cov-gate")), held, "and not the ones the coverage floor reads");

    appendFileSync(join(root, "src/lib.rs"), "\n// a changed input\n");
    assert.match(coverage({}), /Compiling lantern/, "a changed source rebuilds through the shared tree");
    assert.doesNotMatch(coverage(gate), /Compiling lantern/, "and the gate takes that rebuild");
    const report = cargo(root, ["llvm-cov", "report", "--fail-under-lines", "50"], gate);
    assert.match(report.stdout, /lib\.rs/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("a directory where the link belongs is replaced, and a blocked path names what to remove", () => {
  const root = mkdtempSync(join(tmpdir(), "crozier-shared-build-"));
  try {
    const run = () => spawnSync(process.execPath, [SHARE], { encoding: "utf8", env: { ...process.env, CROZIER_SHARED_BUILD_ROOT: root } });
    mkdirSync(join(root, "target/llvm-cov-gate/debug/deps"), { recursive: true });
    assert.equal(run().status, 0);
    assert.ok(lstatSync(join(root, "target/llvm-cov-gate/debug")).isSymbolicLink());
    rmSync(join(root, "target"), { recursive: true });
    writeFileSync(join(root, "target"), "a file where the build tree belongs\n");
    const blocked = run();
    assert.equal(blocked.status, 1);
    assert.match(blocked.stderr, /remove target\/llvm-cov-gate by hand/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
