// The Nx results this tier's reuse tests cache must not answer for another
// operating system or other compiler flags. Each case runs a real Nx in a scratch
// workspace over the real target's real `inputs`, with a stand-in for the suite's
// command that counts its runs, and a stand-in tool on PATH for the other host.
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
function scratchWorkspace(t, project, targetName) {
  const root = mkdtempSync(join(tmpdir(), "crozier-cache-key-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const real = JSON.parse(readFileSync(join(ROOT, project, "project.json"), "utf8"));
  const count = `"${process.execPath}" -e "require('fs').appendFileSync('runs','x')"`;
  mkdirSync(join(root, project), { recursive: true });
  writeFileSync(join(root, project, "project.json"), JSON.stringify({
    name: real.name,
    targets: { [targetName]: { command: count, cache: true, inputs: real.targets[targetName].inputs } },
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
  return {
    root,
    /** Run the target through Nx under `env`; returns how many times its command has now run. */
    run(env = {}) {
      const merged = { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true", NX_TUI: "false", NX_ISOLATE_PLUGINS: "false", ...env };
      // This suite itself runs inside an Nx task, and a sweep turns every replay into a rerun.
      for (const name of ["NX_SKIP_NX_CACHE", "NX_WORKSPACE_ROOT_PATH", "NX_WORKSPACE_ROOT", "NX_TASK_TARGET_PROJECT", "NX_TASK_TARGET_TARGET", "NX_TASK_HASH"]) delete merged[name];
      const nx = spawnSync(process.execPath, [NX, "run", task, "--outputStyle=static"], { cwd: root, env: merged, encoding: "utf8", maxBuffer: 16 * 1024 * 1024 });
      assert.equal(nx.status, 0, `${nx.stdout}\n${nx.stderr}`);
      return existsSync(join(root, "runs")) ? readFileSync(join(root, "runs"), "utf8").length : 0;
    },
  };
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
  const key = Object.keys(process.env).find((candidate) => candidate.toUpperCase() === "PATH") ?? "PATH";
  return { [key]: `${bin}${delimiter}${process.env[key]}` };
}

const realRustc = (root) => spawnSync("rustc", ["-vV"], { cwd: root, encoding: "utf8", shell: process.platform === "win32" }).stdout.trim();

test("suite-cases:test replays its result only for the same operating system and compiler flags", (t) => {
  const workspace = scratchWorkspace(t, "tools/ci/suite-cases", "test");
  const { root, run } = workspace;
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
  const other = process.platform === "win32" ? "linux" : "win32";
  assert.equal(run(standIn(root, "node", "-p", other, process.execPath)), 2, "another operating system takes no cached result");
  assert.equal(run(), 2, "the original operating system still replays its own result");
});

test("the key names the operating system and the flags, and survives a missing rustc", () => {
  const key = (env) => {
    const run = spawnSync(process.execPath, [join(ROOT, KEY)], { cwd: ROOT, encoding: "utf8", env: { ...process.env, ...env } });
    assert.equal(run.status, 0, run.stderr);
    return run.stdout;
  };
  const plain = key({ RUSTFLAGS: "--cfg crozier_cache_probe" });
  assert.ok(plain.includes(`os: ${process.platform} ${process.arch}\n`), plain);
  assert.match(plain, /^RUSTFLAGS=--cfg crozier_cache_probe$/m);
  assert.match(plain, /^host: /m);
  const pathKey = Object.keys(process.env).find((candidate) => candidate.toUpperCase() === "PATH") ?? "PATH";
  assert.match(key({ [pathKey]: "" }), /^rustc: absent$/m, "a host without rustc still hashes: Nx stops the whole run when a runtime input fails");
});
