// The Nx results this tier's reuse tests cache must not answer for another
// operating system, interpreter or other compiler flags. Each case runs a real Nx
// in a scratch workspace over the real target's real `inputs`, with a stand-in for
// the suite's command that counts its runs, and a stand-in tool on PATH for the
// other host.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { chmodSync, cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { delimiter, dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");
const NX = join(ROOT, "node_modules/nx/dist/bin/nx.js");
const KEY = "tools/ci/suite-cases/cache-key.mjs";

/** A workspace holding `project` with the real project's real `test`-like target's inputs, its command only counting. */
function scratchWorkspace(t, project, targetName, suiteCommand) {
  const root = mkdtempSync(join(tmpdir(), "crozier-cache-key-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const real = JSON.parse(readFileSync(join(ROOT, project, "project.json"), "utf8"));
  const count = `"${process.execPath}" -e "require('fs').appendFileSync('runs','x')"`;
  mkdirSync(join(root, project), { recursive: true });
  writeFileSync(join(root, project, "project.json"), JSON.stringify({
    name: real.name,
    targets: { [targetName]: { command: suiteCommand ?? count, cache: true, inputs: real.targets[targetName].inputs } },
  }));
  writeFileSync(join(root, "nx.json"), JSON.stringify({ namedInputs: JSON.parse(readFileSync(join(ROOT, "nx.json"), "utf8")).namedInputs }));
  writeFileSync(join(root, ".gitignore"), "/node_modules\n/.nx\n/runs\n/stand-in\n");
  cpSync(join(ROOT, "package.json"), join(root, "package.json"));
  cpSync(join(ROOT, "rust-toolchain.toml"), join(root, "rust-toolchain.toml"));
  mkdirSync(join(root, dirname(KEY)), { recursive: true });
  cpSync(join(ROOT, KEY), join(root, KEY));
  // A junction on Windows needs no privilege; elsewhere it is a symlink.
  symlinkSync(join(ROOT, "node_modules"), join(root, "node_modules"), "junction");
  const task = `${real.name}:${targetName}`;
  /** The target through Nx under `env`, whatever it exits. */
  const nx = (env = {}) => {
    const merged = { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true", NX_TUI: "false", NX_ISOLATE_PLUGINS: "false", ...env };
    // This suite itself runs inside an Nx task, and a sweep turns every replay into a rerun.
    for (const name of ["NX_SKIP_NX_CACHE", "NX_WORKSPACE_ROOT_PATH", "NX_WORKSPACE_ROOT", "NX_TASK_TARGET_PROJECT", "NX_TASK_TARGET_TARGET", "NX_TASK_HASH"]) delete merged[name];
    return spawnSync(process.execPath, [NX, "run", task, "--outputStyle=static"], { cwd: root, env: merged, encoding: "utf8", maxBuffer: 16 * 1024 * 1024 });
  };
  /** Run the target through Nx under `env`; returns how many times its command has now run. */
  const run = (env = {}) => {
    const result = nx(env);
    assert.equal(result.status, 0, `${result.stdout}\n${result.stderr}`);
    return existsSync(join(root, "runs")) ? readFileSync(join(root, "runs"), "utf8").length : 0;
  };
  return { root, nx, run };
}

/** The workspace's members, split as the boundary rule splits them: declared inputs and tier manifests. */
function members() {
  const manifest = readFileSync(join(ROOT, "pyproject.toml"), "utf8");
  const list = manifest.match(/\[tool\.uv\.workspace\]\s*members = \[([\s\S]*?)\n\]/)[1];
  const all = [...list.replace(/#.*$/gm, "").matchAll(/"([^"]+)"/g)].map((match) => match[1]);
  const isTier = (member) => JSON.parse(readFileSync(join(ROOT, member, "project.json"), "utf8")).tags.includes("type:tier");
  return { tooling: all.filter((member) => !isTier(member)), tier: all.filter(isTier) };
}

/** PATH with a stand-in `name` first: it answers `output` to the query the key makes and defers everything else to `fallback`. */
function standIn(root, name, query, output, fallback) {
  const bin = join(root, "stand-in", name);
  mkdirSync(bin, { recursive: true });
  const sh = output.split("\n").map((line) => `echo "${line}"`).join("\n");
  const cmd = output.split("\n").map((line) => `echo ${line}`).join("\r\n");
  writeFileSync(join(bin, name), `#!/bin/sh\nif [ "$1" = "${query}" ]; then\n${sh}\nexit 0\nfi\nexec "${fallback}" "$@"\n`);
  chmodSync(join(bin, name), 0o755);
  writeFileSync(join(bin, `${name}.cmd`), `@echo off\r\nif "%~1"=="${query}" (\r\n${cmd}\r\nexit /b 0\r\n)\r\n"${fallback}" %*\r\n`);
  const key = pathKey();
  return { [key]: `${bin}${delimiter}${process.env[key]}` };
}

const pathKey = () => Object.keys(process.env).find((candidate) => candidate.toUpperCase() === "PATH") ?? "PATH";

/** The first `name` on PATH, for a stand-in that defers to the real tool. */
function onPath(name) {
  const names = process.platform === "win32" ? [`${name}.exe`, `${name}.cmd`] : [name];
  const found = process.env[pathKey()].split(delimiter).flatMap((directory) => names.map((candidate) => join(directory, candidate))).find(existsSync);
  assert.ok(found, `${name} is not on PATH`);
  return found;
}

/** PATH where `uv python find` names an interpreter that reports `version`; `uv` itself is otherwise the real one. */
function otherInterpreter(root, version) {
  const bin = join(root, "stand-in", "interpreter");
  mkdirSync(bin, { recursive: true });
  const python = join(bin, process.platform === "win32" ? "python.cmd" : "python");
  writeFileSync(python, process.platform === "win32" ? `@echo off\r\necho cpython ${version}\r\n` : `#!/bin/sh\ncat >/dev/null\necho "cpython ${version}"\n`);
  chmodSync(python, 0o755);
  return standIn(root, "uv", "python", python, onPath("uv"));
}

/** PATH where `node` runs the key for real on an operating system that reports `name`. */
function otherOperatingSystem(root, name) {
  const bin = join(root, "stand-in", "operating-system");
  mkdirSync(bin, { recursive: true });
  const preload = join(bin, "preload.cjs");
  writeFileSync(preload, `const os = require("node:os");\nos.platform = () => "${name}";\nrequire("node:module").syncBuiltinESMExports();\n`);
  writeFileSync(join(bin, "node"), `#!/bin/sh\nexec "${process.execPath}" --require "${preload}" "$@"\n`);
  chmodSync(join(bin, "node"), 0o755);
  writeFileSync(join(bin, "node.cmd"), `@echo off\r\n"${process.execPath}" --require "${preload}" %*\r\n`);
  return { [pathKey()]: `${bin}${delimiter}${process.env[pathKey()]}` };
}

/** The key's output, line by line, in `cwd` under `env`. */
function keyLines(cwd, env = {}, ...args) {
  const run = spawnSync(process.execPath, [join(ROOT, KEY), ...args], { cwd, encoding: "utf8", env: { ...process.env, ...env } });
  assert.equal(run.status, 0, run.stderr);
  return run.stdout.split("\n").filter(Boolean);
}

const pythonLine = (lines) => lines.find((line) => line.startsWith("python: "));

/** An installed interpreter of another Python minor than `line` names, or nothing on a host with only the one. */
function secondInterpreter(line) {
  const listed = spawnSync("uv", ["python", "list", "--only-installed", "--output-format", "json"], { encoding: "utf8", shell: process.platform === "win32" });
  if (listed.status !== 0) return undefined;
  const current = line.match(/^python: \S+ (\d+\.\d+)\./)?.[1];
  return JSON.parse(listed.stdout).find((entry) => entry.implementation === "cpython" && entry.path && !entry.version.startsWith(`${current}.`))?.path;
}

const realRustc = (root) => spawnSync("rustc", ["-vV"], { cwd: root, encoding: "utf8", shell: process.platform === "win32" }).stdout.trim();

test("suite-cases:test replays its result only for the same operating system and compiler flags", (t) => {
  const { root, run } = scratchWorkspace(t, "tools/ci/suite-cases", "test");
  assert.equal(run(), 1, "the first run executes");
  assert.equal(run(), 1, "the same host and flags replay from cache");

  // Another operating system: all the same but the host rustc reports.
  const here = realRustc(root);
  const otherHost = here.includes("host: aarch64-apple-darwin") ? "x86_64-pc-windows-msvc" : "aarch64-apple-darwin";
  const elsewhere = here.replace(/^host: .*$/m, `host: ${otherHost}`);
  assert.equal(run(standIn(root, "rustc", "-vV", elsewhere, "rustc-is-only-asked-its-version")), 2, "another operating system takes no cached result");

  assert.equal(run({ RUSTFLAGS: "--cfg crozier_cache_probe" }), 3, "other compiler flags take no cached result");
  assert.equal(run({ RUSTFLAGS: "--cfg crozier_cache_probe" }), 3, "those flags replay their own result");
  assert.equal(run({ RUSTFLAGS: "--cfg crozier_cache_probe_two" }), 4, "and different flags again do not");
  assert.equal(run({ CARGO_PROFILE_DEV_OPT_LEVEL: "1" }), 5, "another build profile takes no cached result");

  const home = join(root, "stand-in", "cargo-home");
  mkdirSync(home, { recursive: true });
  writeFileSync(join(home, "config.toml"), '[build]\nrustflags = ["--cfg", "crozier_cache_probe"]\n');
  assert.equal(run({ CARGO_HOME: home }), 6, "flags from the user-level cargo config take no cached result");

  assert.equal(run(), 6, "the original host and flags still replay their own result");
});

test("surface-census:test-reuse replays its result only for the same operating system", (t) => {
  const { root, run } = scratchWorkspace(t, "tools/surface-census", "test-reuse");
  assert.equal(run(), 1);
  assert.equal(run(), 1, "the same operating system replays from cache");
  const other = otherOperatingSystem(root, process.platform === "win32" ? "linux" : "win32");
  assert.equal(run(other), 2, "another operating system takes no cached result");
  assert.equal(run(other), 2, "that operating system replays its own result");
  assert.equal(run(), 2, "the original operating system still replays its own result");
});

for (const [project, target] of [["tools/ci/suite-cases", "test"], ["tools/surface-census", "test-reuse"]]) {
  test(`${project}:${target} takes no cached result from another Python interpreter`, (t) => {
    const { root, run } = scratchWorkspace(t, project, target);
    assert.equal(run(), 1);
    assert.equal(run(), 1, "the same interpreter replays from cache");
    const other = otherInterpreter(root, "3.99.0 (stand-in)");
    assert.equal(run(other), 2, "another interpreter takes no cached result");
    assert.equal(run(other), 2, "that interpreter replays its own result");
    assert.equal(run(otherInterpreter(root, "3.99.1 (stand-in)")), 3, "a patch release of it is another interpreter");
    assert.equal(run({ PYTHONHASHSEED: "1" }), 4, "a variable the interpreter obeys takes no cached result");
    assert.equal(run(), 4, "the original interpreter still replays its own result");
  });

  test(`${project}:${target} takes no cached result from a real second interpreter`, (t) => {
    const { root, run } = scratchWorkspace(t, project, target);
    const second = secondInterpreter(pythonLine(keyLines(root)));
    if (!second) return t.skip("this host has one Python minor; the stand-in case still holds");
    assert.equal(run(), 1);
    assert.equal(run({ UV_PYTHON: second }), 2, "uv selecting another installed interpreter takes no cached result");
    assert.equal(run(), 2, "the original interpreter still replays its own result");
  });
}

test("only the interpreter's line moves when the interpreter does", (t) => {
  const root = mkdtempSync(join(tmpdir(), "crozier-cache-key-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const moved = (env, ...args) => {
    const [before, after] = [keyLines(root, {}, ...args), keyLines(root, env, ...args)];
    return after.filter((line) => !before.includes(line));
  };
  const other = otherInterpreter(root, "3.99.0 (stand-in)");
  assert.deepEqual(moved(other), ["python: cpython 3.99.0 (stand-in)"]);
  assert.deepEqual(moved(other, "python"), ["python: cpython 3.99.0 (stand-in)"]);
});

test("the key names the interpreter `uv run` runs the suites under", () => {
  const run = spawnSync("uv", ["run", "--locked", "--all-packages", "python", "-c", "import sys; print(sys.implementation.name, sys.version)"], { cwd: ROOT, encoding: "utf8" });
  assert.equal(run.status, 0, run.stderr);
  const line = pythonLine(keyLines(ROOT));
  assert.ok(line.startsWith(`python: ${run.stdout.trim()} `), `${line}\nagainst ${run.stdout}`);
});

test("a requested interpreter is the one the key names, as `uv run` obeys it", (t) => {
  const root = mkdtempSync(join(tmpdir(), "crozier-cache-key-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const second = secondInterpreter(pythonLine(keyLines(root)));
  if (!second) return t.skip("this host has one Python minor");
  writeFileSync(join(root, "pyproject.toml"), '[project]\nname = "probe"\nversion = "0"\nrequires-python = ">=3.8"\n\n[tool.uv]\npackage = false\n');
  const env = { ...process.env, UV_PYTHON: second };
  const run = spawnSync("uv", ["run", "python", "-c", "import sys; print(sys.implementation.name, sys.version)"], { cwd: root, encoding: "utf8", env });
  assert.equal(run.status, 0, run.stderr);
  const line = pythonLine(keyLines(root, { UV_PYTHON: second }));
  assert.ok(line.startsWith(`python: ${run.stdout.trim()} `), `${line}\nagainst ${run.stdout}`);
});

// A reading the suite makes outside the target's own directory, changed the way a later commit would.
for (const [project, target, read] of [
  ["tools/surface-census", "test-reuse", "docs/openapi-surface/handwritten-reach.tsv"],
  ["tools/surface-census", "test-reuse", "src/openapi.rs"],
  ["tools/surface-census", "test-reuse", "tests/fixtures/corpus-aliases.tsv"],
  ["tools/surface-census", "test-reuse", "tools/fern-refusals/sdk_evaluation.py"],
  ["tools/ci/suite-cases", "test", "tools/surface-census/port_pins.py"],
  ["tools/ci/suite-cases", "test", "tools/witness-search/witness_screen.py"],
  ["tools/ci/suite-cases", "test", "docs/fern-limitations.md"],
  ["tools/ci/suite-cases", "test", "bun.lock"],
]) {
  test(`${project}:${target} reruns when ${read} changes`, (t) => {
    const { root, run } = scratchWorkspace(t, project, target);
    mkdirSync(dirname(join(root, read)), { recursive: true });
    // Nx parses a lockfile, so that one stays valid: only trailing bytes differ.
    const body = read === "bun.lock" ? readFileSync(join(ROOT, read), "utf8") : "";
    writeFileSync(join(root, read), `${body}\n`);
    assert.equal(run(), 1);
    assert.equal(run(), 1, "an unchanged read replays from cache");
    writeFileSync(join(root, read), `${body}\n\n`);
    assert.equal(run(), 2, `${read} decides the result, so a change to it takes no cached result`);
  });
}

const TARGETS = [["tools/ci/suite-cases", "test"], ["tools/surface-census", "test-reuse"]];
const write = (root, path, text) => {
  mkdirSync(dirname(join(root, path)), { recursive: true });
  writeFileSync(join(root, path), text);
};

for (const [project, target] of TARGETS) {
  test(`${project}:${target} reruns when any member manifest changes, and replays while none has`, (t) => {
    const { root, run } = scratchWorkspace(t, project, target);
    const { tooling, tier } = members();
    assert.equal(tooling.length, 19);
    assert.equal(tier.length, 6);
    const manifests = [...tooling, ...tier].map((member) => `${member}/pyproject.toml`);
    for (const manifest of manifests) write(root, manifest, "[project]\n");
    let runs = run();
    assert.equal(runs, 1);
    assert.equal(run(), 1, "unchanged manifests replay from cache");
    for (const manifest of manifests) {
      write(root, manifest, "[project]\n# changed\n");
      runs += 1;
      assert.equal(run(), runs, `${manifest} changed, so its cached success must not replay`);
      assert.equal(run(), runs, `${manifest}'s new content replays its own result`);
      write(root, manifest, "[project]\n");
    }
    assert.equal(run(), 1 + manifests.length, "the original manifests still replay their own result");
  });

  // The failure the inputs exist for, with a real uv and a real lock.
  for (const member of ["tools/witness-search", "tests/runtime"]) {
    test(`${project}:${target} does not replay a success once ${member}'s manifest makes uv reject the lock`, (t) => {
      const suite = "uv run --locked --all-packages python -c pass";
      const { root, nx } = scratchWorkspace(t, project, target, suite);
      const manifest = (dependencies, sources = "") => `[project]\nname = "probe-member"\nversion = "0"\nrequires-python = ">=3.8"\ndependencies = [${dependencies}]\n\n[tool.uv]\npackage = false\n${sources}`;
      write(root, "pyproject.toml", `[project]\nname = "probe"\nversion = "0"\nrequires-python = ">=3.8"\n\n[tool.uv]\npackage = false\n\n[tool.uv.workspace]\nmembers = ["${member}", "probe-sibling"]\n`);
      write(root, "probe-sibling/pyproject.toml", '[project]\nname = "probe-sibling"\nversion = "0"\nrequires-python = ">=3.8"\n\n[tool.uv]\npackage = false\n');
      write(root, `${member}/pyproject.toml`, manifest(""));
      const lock = spawnSync("uv", ["lock", "--offline"], { cwd: root, encoding: "utf8" });
      assert.equal(lock.status, 0, lock.stderr);
      const first = nx({ UV_NO_SYNC: "0" });
      assert.equal(first.status, 0, `${first.stdout}\n${first.stderr}`);
      const replay = nx({ UV_NO_SYNC: "0" });
      assert.equal(replay.status, 0, `${replay.stdout}\n${replay.stderr}`);
      assert.match(replay.stdout, /existing outputs match the cache|local cache/i, "unchanged inputs hit the cache");
      write(root, `${member}/pyproject.toml`, manifest('"probe-sibling"', "\n[tool.uv.sources]\nprobe-sibling = { workspace = true }\n"));
      const stale = nx({ UV_NO_SYNC: "0" });
      assert.notEqual(stale.status, 0, `the cached success was replayed over a lock uv rejects:\n${stale.stdout}`);
      assert.match(`${stale.stdout}\n${stale.stderr}`, /lockfile|--locked/i);
    });
  }
}

const LINT_PROJECT = "tools/ci/suite-cases";
const SHARED_BUILD = "scripts/share-instrumented-build.mjs";
const REPLAYED = /existing outputs match the cache|local cache/i;
const realLint = () => JSON.parse(readFileSync(join(ROOT, LINT_PROJECT, "project.json"), "utf8")).targets.lint;
const syntaxChecked = () => realLint().options.commands.filter((command) => command.startsWith("node --check ")).map((command) => command.slice("node --check ".length));

/**
 * The real `suite-cases:lint`, real inputs and real `node --check` commands, over copies of
 * the files it checks. Its boundary command is left out: it needs the real project graph
 * and `cargo metadata`, and no file here decides it.
 */
function lintWorkspace(t) {
  const { root, nx } = scratchWorkspace(t, LINT_PROJECT, "lint");
  const lint = realLint();
  for (const path of syntaxChecked()) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    cpSync(join(ROOT, path), join(root, path));
  }
  writeFileSync(join(root, LINT_PROJECT, "project.json"), JSON.stringify({
    name: "suite-cases",
    targets: {
      lint: {
        executor: lint.executor,
        cache: lint.cache,
        inputs: lint.inputs,
        options: { ...lint.options, commands: syntaxChecked().map((path) => `node --check ${path}`) },
      },
    },
  }));
  return { root, nx };
}

function assertRan(run, because) {
  assert.equal(run.status, 0, `${run.stdout}\n${run.stderr}`);
  assert.doesNotMatch(run.stdout, REPLAYED, because);
}

function assertReplayed(run, because) {
  assert.equal(run.status, 0, `${run.stdout}\n${run.stderr}`);
  assert.match(run.stdout, REPLAYED, because);
}

test("suite-cases:lint replays while its inputs hold, and a syntax error in the shared-build script reruns it and fails", (t) => {
  const { root, nx } = lintWorkspace(t);
  const script = join(root, SHARED_BUILD);
  const original = readFileSync(script, "utf8");
  assertRan(nx(), "the first run has nothing to replay");
  assertReplayed(nx(), "unchanged inputs replay the success");

  writeFileSync(script, `${original}\nfunction {\n`);
  for (const attempt of ["first", "second"]) {
    const broken = nx();
    assert.notEqual(broken.status, 0, `the ${attempt} run after the edit replayed a stale success:\n${broken.stdout}`);
    assert.doesNotMatch(broken.stdout, REPLAYED, "a failing edit is checked, not replayed");
    assert.match(`${broken.stdout}\n${broken.stderr}`, /SyntaxError/);
    assert.ok(`${broken.stdout}\n${broken.stderr}`.includes("share-instrumented-build.mjs"), "the failure names the script");
  }

  writeFileSync(script, original);
  assertReplayed(nx(), "the original script replays its own success");
});

test("suite-cases:lint takes no cached result from another Node version", (t) => {
  const { root, nx } = lintWorkspace(t);
  const otherNode = standIn(root, "node", "--version", "v0.0.0-crozier-probe", process.execPath);
  assertRan(nx(), "the first run has nothing to replay");
  assertReplayed(nx(), "the same Node replays");
  assertRan(nx(otherNode), "another Node version must check the files itself");
  assertReplayed(nx(otherNode), "that version replays its own success");
  assertReplayed(nx(), "the original Node still replays its own success");
});

test("every file suite-cases:lint syntax-checks decides its cache key", () => {
  const { inputs } = realLint();
  assert.ok(inputs.includes("default"), "the project's own files come from `default`");
  const outside = syntaxChecked().filter((path) => !path.startsWith(`${LINT_PROJECT}/`));
  assert.ok(outside.includes(SHARED_BUILD));
  for (const path of outside) assert.ok(inputs.includes(`{workspaceRoot}/${path}`), `${path} is checked but is no input of suite-cases:lint`);
});

test("every member's manifest is either declared by both targets or hashed by the key", () => {
  const { tooling, tier } = members();
  const lines = keyLines(ROOT);
  const hashed = lines.filter((line) => line.startsWith("tier manifest ")).map((line) => line.split(" ")[2].replace(/:$/, ""));
  assert.deepEqual(hashed.sort(), tier.map((member) => `${member}/pyproject.toml`).sort(), "a tier member belongs in the key's TIER_MANIFESTS");
  assert.deepEqual(keyLines(ROOT, {}, "python").filter((line) => line.startsWith("tier manifest ")), lines.filter((line) => line.startsWith("tier manifest ")));
  for (const [project, target] of TARGETS) {
    const inputs = JSON.parse(readFileSync(join(ROOT, project, "project.json"), "utf8")).targets[target].inputs;
    for (const member of tooling) assert.ok(inputs.includes(`{workspaceRoot}/${member}/pyproject.toml`), `${project}:${target} does not declare ${member}'s manifest`);
    assert.ok(!inputs.some((input) => tier.some((member) => String(input).includes(`${member}/`))), "a tier manifest as a declared input breaks the boundary rule");
  }
});

test("the key names the operating system, the interpreter and the flags, and survives missing tools", () => {
  const key = (env, ...args) => `${keyLines(ROOT, env, ...args).join("\n")}\n`;
  const plain = key({ RUSTFLAGS: "--cfg crozier_cache_probe", PYTHONPATH: "probe" });
  assert.ok(plain.includes(`os: ${process.platform} ${process.arch}\n`), plain);
  assert.ok(plain.includes(`node: ${process.version}\n`), plain);
  assert.match(plain, /^RUSTFLAGS=--cfg crozier_cache_probe$/m);
  assert.match(plain, /^PYTHONPATH=probe$/m);
  assert.match(plain, /^host: /m);
  assert.match(plain, /^python: \S+ \d+\.\d+\.\d+/m);
  assert.match(plain, /^uv: /m);

  const python = key({ RUSTFLAGS: "--cfg crozier_cache_probe", PYTHONPATH: "probe" }, "python");
  assert.match(python, /^python: \S+ \d+\.\d+\.\d+/m);
  assert.match(python, /^PYTHONPATH=probe$/m);
  assert.doesNotMatch(python, /^(rustc|RUSTFLAGS)/m, "a suite that compiles nothing does not rerun for flags");

  const bare = key({ [pathKey()]: "" });
  assert.match(bare, /^rustc: absent$/m, "a host without rustc still hashes: Nx stops the whole run when a runtime input fails");
  assert.match(bare, /^python: absent$/m, "nor does a host without uv stop it");
});
