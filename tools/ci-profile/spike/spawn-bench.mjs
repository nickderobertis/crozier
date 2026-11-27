#!/usr/bin/env node
// SPIKE ONLY (spike-windows-lane-breakdown): what one process spawn, and one
// file-system operation the suites repeat, costs on this runner, so a test's
// cost can be divided into spawns and tree copies.
//
//   node tools/ci-profile/spike/spawn-bench.mjs <out.json> [repeats]
//
// Each program runs `repeats` times (default 20) after one unmeasured warm-up;
// the JSON holds every sample's seconds and their median, mean and minimum.
import { spawnSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, mkdtempSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { cpus, platform, tmpdir } from "node:os";
import { join, resolve } from "node:path";

const [out, repeatsArg] = process.argv.slice(2);
if (!out) {
  console.error("spawn-bench: usage: node tools/ci-profile/spike/spawn-bench.mjs <out.json> [repeats]");
  process.exit(2);
}
const repeats = Number(repeatsArg ?? 20);
if (!Number.isSafeInteger(repeats) || repeats < 1 || repeats > 1000) {
  console.error(`spawn-bench: repeats must be an integer from 1 to 1000, not '${repeatsArg}'`);
  process.exit(2);
}
const ROOT = resolve(import.meta.dirname, "..", "..", "..");
const exe = process.platform === "win32" ? ".exe" : "";

function summary(samples) {
  const sorted = [...samples].sort((a, b) => a - b);
  const n = sorted.length;
  return {
    n,
    median: n ? (sorted[Math.floor((n - 1) / 2)] + sorted[Math.ceil((n - 1) / 2)]) / 2 : null,
    mean: n ? sorted.reduce((a, b) => a + b, 0) / n : null,
    min: n ? sorted[0] : null,
    max: n ? sorted[n - 1] : null,
    samples: sorted,
  };
}

function time(fn) {
  const start = process.hrtime.bigint();
  const ok = fn();
  return { seconds: Number(process.hrtime.bigint() - start) / 1e9, ok };
}

function bench(label, program, args, input) {
  const run = () => {
    const r = spawnSync(program, args, { cwd: ROOT, input, encoding: "utf8", stdio: [input === undefined ? "ignore" : "pipe", "pipe", "pipe"] });
    return r.status === 0 ? true : `${r.error?.message ?? `exit ${r.status}`}: ${(r.stderr ?? "").slice(0, 300)}`;
  };
  const warm = run();
  if (warm !== true) return { label, program, args, error: warm };
  const samples = [];
  for (let i = 0; i < repeats; i++) {
    const t = time(run);
    if (t.ok !== true) return { label, program, args, error: t.ok };
    samples.push(t.seconds);
  }
  return { label, program, args, ...summary(samples) };
}

function newest(dir, prefix) {
  if (!existsSync(dir)) return undefined;
  const hits = readdirSync(dir)
    .filter((name) => name.startsWith(prefix) && (exe ? name.endsWith(exe) : !name.includes(".")))
    .map((name) => join(dir, name))
    .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs);
  return hits[0];
}

const crozier = [join(ROOT, "target", "e2e", `crozier${exe}`), join(ROOT, "target", "debug", `crozier${exe}`)].find(existsSync);
const e2eTests = newest(join(ROOT, "target", "e2e", "deps"), "e2e-");
const small = "x={'a':1,'b':2}\n";
const programs = [
  ["ruff --version", "ruff", ["--version"]],
  ["ruff format (one small file on stdin)", "ruff", ["format", "--line-length", "120", "--stdin-filename", "x.py", "-"], small],
  ["python3 -c pass", "python3", ["-c", "pass"]],
  ["python -c pass", "python", ["-c", "pass"]],
  ["uv run --locked --all-packages python -c pass", "uv", ["run", "--locked", "--all-packages", "python", "-c", "pass"]],
  ["git --version", "git", ["--version"]],
  ["git rev-parse HEAD", "git", ["rev-parse", "HEAD"]],
  ["bash -c true", "bash", ["-c", "true"]],
  ["node -e 0", "node", ["-e", "0"]],
  ["just --version", "just", ["--version"]],
  ["cargo --version", "cargo", ["--version"]],
  ...(crozier ? [["crozier --version", crozier, ["--version"]]] : []),
  ...(e2eTests ? [["crozier-e2e test binary --list", e2eTests, ["--list", "--format", "terse"]]] : []),
];
const spawns = programs.map(([label, program, args, input]) => bench(label, program, args, input));

// The file-system work the suites repeat: a tree of small files written and
// removed, and a golden tree copied, as a fixture copy or a staged corpus is.
function fsBench() {
  const base = mkdtempSync(join(tmpdir(), "crozier-spike-fs-"));
  const results = {};
  try {
    const writes = [];
    for (let i = 0; i < Math.min(repeats, 5); i++) {
      const dir = join(base, `w${i}`);
      writes.push(time(() => {
        for (let f = 0; f < 1000; f++) {
          const sub = join(dir, String(f % 20));
          if (f < 20) mkdirSync(sub, { recursive: true });
          writeFileSync(join(sub, `f${f}.py`), "x = 1\n");
        }
        rmSync(dir, { recursive: true, force: true });
        return true;
      }).seconds);
    }
    results["write and remove 1000 small files"] = summary(writes);
    const golden = join(ROOT, "tests", "fixtures", "zulip", "expected");
    if (existsSync(golden)) {
      const copies = [];
      for (let i = 0; i < Math.min(repeats, 5); i++) {
        const dest = join(base, `c${i}`);
        copies.push(time(() => {
          cpSync(golden, dest, { recursive: true });
          rmSync(dest, { recursive: true, force: true });
          return true;
        }).seconds);
      }
      results["copy and remove the zulip golden tree"] = summary(copies);
    }
  } finally {
    rmSync(base, { recursive: true, force: true });
  }
  return results;
}

writeFileSync(out, `${JSON.stringify({ schema: "spike-spawn-bench-1", platform: platform(), cpus: cpus().length, cpu_model: cpus()[0]?.model, repeats, spawns, fs: fsBench() }, null, 2)}\n`);
console.log(`spawn-bench: wrote ${out}`);
