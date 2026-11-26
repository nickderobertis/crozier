// SPIKE ONLY (spike-windows-lane-breakdown): keeps the measurement harness honest. Every
// case drives a real process: the built crozier binary, the reader, the replay, the spawn
// hooks, the spawn bench, the experiment script and the gate.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
const EXE = process.platform === "win32" ? ".exe" : "";
const CROZIER = join(ROOT, "target", "debug", `crozier${EXE}`);
const READER = join(ROOT, "tools", "ci-profile", "ci-profile.mjs");
const SPEC = `openapi: 3.0.0
info: {title: Tiny, version: "1"}
paths:
  /things/{id}:
    get:
      operationId: getThing
      tags: [Things]
      parameters: [{name: id, in: path, required: true, schema: {type: string}}]
      responses:
        "200":
          description: OK
          content: {application/json: {schema: {$ref: "#/components/schemas/Thing"}}}
components:
  schemas:
    Thing: {type: object, properties: {name: {type: string}}}
`;

const scratch = () => mkdtempSync(join(tmpdir(), "ci-profile-test-"));
const run = (program, args, env = {}, cwd = ROOT) => spawnSync(program, args, { cwd, encoding: "utf8", env: { ...process.env, ...env } });

function generate(dir, env) {
  const spec = join(dir, "spec.yml");
  writeFileSync(spec, SPEC);
  const out = join(dir, `out-${Object.values(env).join("-") || "plain"}`);
  return { out, result: run(CROZIER, ["generate", "--spec", spec, "--output", out, "--package-name", "tiny", "--project-name", "tiny", "--no-config"], env) };
}

function tree(dir) {
  const files = {};
  const walk = (d) => {
    for (const name of readdirSync(d, { withFileTypes: true })) {
      const path = join(d, name.name);
      if (name.isDirectory()) walk(path);
      else files[path.slice(dir.length)] = readFileSync(path, "utf8");
    }
  };
  walk(dir);
  return files;
}

const profilesIn = (dir) => (existsSync(dir) ? readdirSync(dir).map((f) => JSON.parse(readFileSync(join(dir, f), "utf8"))) : []);

test("crozier writes one schema-1 profile per process only when CROZIER_PROFILE names a directory", { skip: !existsSync(CROZIER) && "build crozier first (crozier:build)" }, () => {
  const dir = scratch();
  const profile = join(dir, "profile");
  assert.equal(generate(dir, {}).result.status, 0);
  assert.equal(existsSync(profile), false, "no profile without CROZIER_PROFILE");
  const { result } = generate(dir, { CROZIER_PROFILE: profile });
  assert.equal(result.status, 0, result.stderr);
  const [one] = profilesIn(profile);
  assert.equal(one.schema_version, 1);
  assert.equal(one.command, "generate");
  const phases = Object.fromEntries(one.phases.map((p) => [p.name, p]));
  for (const name of ["settings", "load", "refusal-checks", "lower", "emit", "format", "write"]) assert.ok(phases[name], `phase ${name}`);
  const ruff = one.subprocesses.find((s) => s.program === "ruff");
  assert.equal(ruff.spawns, phases.format.count, "one ruff spawn per formatted file");
  assert.equal(one.spike.exit_code, 0);
  assert.equal(run(CROZIER, ["--version"], { CROZIER_PROFILE: join(dir, "v") }).status, 0);
  assert.equal(profilesIn(join(dir, "v"))[0].command, "version");
  const failed = run(CROZIER, ["generate", "--spec", join(dir, "missing.yml"), "--output", join(dir, "x"), "--package-name", "t", "--project-name", "t", "--no-config"], { CROZIER_PROFILE: join(dir, "f") });
  assert.equal(failed.status, 1);
  assert.deepEqual(profilesIn(join(dir, "f")).map((p) => [p.command, p.spike.exit_code]), [["generate", 1]]);
});

test("one batched ruff writes the same bytes as one ruff per file, verify agrees, and an unknown mode is refused", { skip: !existsSync(CROZIER) && "build crozier first (crozier:build)" }, () => {
  const dir = scratch();
  const plain = generate(dir, {});
  const batched = generate(dir, { CROZIER_SPIKE_RUFF_BATCH: "1", CROZIER_PROFILE: join(dir, "b") });
  assert.equal(batched.result.status, 0, batched.result.stderr);
  assert.deepEqual(tree(batched.out), tree(plain.out));
  const [profile] = profilesIn(join(dir, "b"));
  assert.equal(profile.subprocesses.find((s) => s.program === "ruff").spawns, 1);
  assert.equal(generate(dir, { CROZIER_SPIKE_RUFF_BATCH: "verify" }).result.status, 0);
  const bogus = generate(dir, { CROZIER_SPIKE_RUFF_BATCH: "bogus" }).result;
  assert.equal(bogus.status, 1);
  assert.match(bogus.stderr, /CROZIER_SPIKE_RUFF_BATCH must be empty, `1` or `verify`/);
});

function artifactTree(profiles) {
  const dir = scratch();
  const timings = join(dir, "test-timings-test-linux", "sweep");
  const spike = join(dir, "spike-profile-test-linux");
  mkdirSync(timings, { recursive: true });
  mkdirSync(join(spike, "ruff-batch"), { recursive: true });
  writeFileSync(join(timings, "gate-1.log"), [
    "$ nx run-many --targets=test --projects=a,b,c",
    "::group::✅ > nx run a:test",
    "        PASS [   1.500s] (1/2) crate::bin first_case",
    "        PASS [   0.250s] crate::bin second_case",
    "::endgroup::",
    "> nx run b:test",
    "2.00s call     tools/b_test.py::Case::test_one",
    "0.50s setup    tools/b_test.py::Case::test_one",
    "ok 1 - a node case",
    "  ---",
    "  duration_ms: 750.5",
    "✔ a spec case (125ms)",
    "",
  ].join("\n"));
  const x = (name, ts, dur, tid) => ({ name, ph: "X", ts, dur, tid, args: { status: "success" } });
  writeFileSync(join(timings, "gate-1.profile.json"), JSON.stringify([x("a:test", 0, 4e6, 0), x("b:test", 0, 2e6, 1), x("c:test", 2e6, 1e6, 1)]));
  writeFileSync(join(spike, "crozier-profile-sweep.jsonl"), profiles.map((p) => JSON.stringify(p)).join("\n"));
  writeFileSync(join(spike, "ruff-batch", "runs.tsv"), "mode\tround\tseconds\texit\nper-file\t1\t10\t0\nbatch\t1\t4\t0\n");
  writeFileSync(join(spike, "runner.json"), JSON.stringify({ cpus: 4 }));
  return dir;
}

test("the reader turns an artifact tree into per-target, per-case, slot and crozier-phase figures", { skip: !existsSync(CROZIER) && "build crozier first (crozier:build)" }, () => {
  const dir = scratch();
  generate(dir, { CROZIER_PROFILE: join(dir, "p") });
  const artifacts = artifactTree(profilesIn(join(dir, "p")));
  const out = join(dir, "report.json");
  const result = run("node", [READER, "local", artifacts, "--out", out]);
  assert.equal(result.status, 0, result.stderr);
  const [lane] = JSON.parse(readFileSync(out, "utf8")).lanes;
  assert.deepEqual(lane.targets.map((t) => [t.target, t.seconds, t.slot]), [["a:test", 4, 0], ["b:test", 2, 1], ["c:test", 1, 1]]);
  const cases = Object.fromEntries(lane.cases.map((c) => [`${c.kind}:${c.case}`, [c.target, c.seconds]]));
  assert.deepEqual(cases["nextest:crate::bin first_case"], ["a:test", 1.5]);
  assert.deepEqual(cases["pytest:tools/b_test.py::Case::test_one"], ["b:test", 2.5]);
  assert.deepEqual(cases["node:a node case"], ["b:test", 0.7505]);
  assert.deepEqual(cases["node:a spec case"], ["b:test", 0.125]);
  assert.deepEqual(lane.schedule.sweep.running_seconds, { 0: 0, 1: 1, 2: 3 });
  const generated = lane.crozier_profile.sweep.generate;
  assert.equal(generated.processes, 1);
  assert.ok(generated.ruff_spawns_per_generation.median >= 1);
  assert.deepEqual(lane.spike.ruff_batch.runs.map((r) => r.mode), ["per-file", "batch"]);
});

test("the reader refuses a bad invocation and a record that is not a schema-1 profile", () => {
  assert.equal(run("node", [READER, "run", "1", "2"]).status, 2);
  assert.equal(run("node", [READER, "local", scratch(), "--out"]).status, 2);
  const artifacts = artifactTree([{ schema_version: 2 }]);
  const result = run("node", [READER, "local", artifacts]);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /not a schema_version 1 CROZIER_PROFILE record/);
});

test("the workflow uploads the artifacts the reader reads", () => {
  const workflow = readFileSync(join(ROOT, ".github", "workflows", "ci.yml"), "utf8");
  const reader = readFileSync(READER, "utf8");
  for (const prefix of ["test-timings-", "spike-profile-"]) {
    assert.ok(workflow.includes(`name: ${prefix}\${{ github.job }}`), `ci.yml uploads ${prefix}<job>`);
    assert.ok(reader.includes(`\`${prefix}\${name}\``), `the reader reads ${prefix}<job>`);
  }
  assert.ok(readFileSync(join(ROOT, "tools", "ci-profile", "spike", "ruff-batch-experiment.sh"), "utf8").includes("printf 'mode\\tround\\tseconds\\texit\\n'"));
  assert.ok(reader.includes('"mode\\tround\\tseconds\\texit"'));
});

test("the replay reproduces a measured schedule and separates Nx's exclusive tasks from a mutex", () => {
  const dir = scratch();
  const at = (target, start, seconds) => ({ target, seconds, start, end: start + seconds, gate_step: "sweep" });
  // a and x run alone (parallelism: false); b and c run in parallel; d depends on b.
  writeFileSync(join(dir, "report.json"), JSON.stringify({ lanes: [{ job: "j", schedule: { sweep: { wall_seconds: 30 } }, targets: [at("b", 0, 10), at("c", 0, 10), at("d", 10, 10), at("a", 20, 5), at("x", 25, 5)] }] }));
  const task = (parallelism) => ({ parallelism });
  writeFileSync(join(dir, "tasks.json"), JSON.stringify({ tasks: { tasks: { a: task(false), x: task(false), b: task(true), c: task(true), d: task(true) }, dependencies: { d: ["b"] } } }));
  const result = run("node", [join(ROOT, "tools/ci-profile/spike/schedule.mjs"), join(dir, "report.json"), "j", "sweep", join(dir, "tasks.json")]);
  assert.equal(result.status, 0, result.stderr);
  const out = JSON.parse(result.stdout);
  assert.equal(out.simulated.alone.observed[2], 30, "replays the measured 30 s");
  assert.equal(out.simulated.mutex.observed[2], 20, "a mutex lets a and x run beside b, c and d");
  assert.deepEqual(out.critical_path.chain, ["b", "d"]);
  const scaled = run("node", [join(ROOT, "tools/ci-profile/spike/schedule.mjs"), join(dir, "report.json"), "j", "sweep", join(dir, "tasks.json"), "--scale", "d=0.5"]);
  assert.equal(JSON.parse(scaled.stdout).simulated.alone.observed[2], 25);
  assert.equal(run("node", [join(ROOT, "tools/ci-profile/spike/schedule.mjs"), join(dir, "report.json"), "j", "sweep", join(dir, "tasks.json"), "--scale", "nope=1"]).status, 2);
});

test("the spawn hooks charge each child and tree copy to the test that started it", () => {
  const dir = scratch();
  const hooks = join(ROOT, "tools", "ci-profile", "spike", "spawncount");
  const env = { SPIKE_SPAWN_LOG: dir, PYTHONPATH: hooks, PYTEST_CURRENT_TEST: "t.py::case (call)", NODE_OPTIONS: `--import ${new URL(`file://${join(hooks, "spawncount.mjs")}`).href}` };
  const py = run(process.platform === "win32" ? "python" : "python3", ["-c", "import shutil, subprocess, sys, tempfile; subprocess.run([sys.executable, '-c', 'pass']); d = tempfile.mkdtemp(); shutil.copytree(sys.argv[1], d + '/c'); shutil.rmtree(d)", hooks], env);
  assert.equal(py.status, 0, py.stderr);
  const nodeRun = run("node", ["-e", "require('node:child_process').spawnSync(process.execPath, ['-e', '0'])"], env);
  assert.equal(nodeRun.status, 0, nodeRun.stderr);
  const records = readdirSync(dir).flatMap((f) => readFileSync(join(dir, f), "utf8").trim().split("\n").map((l) => JSON.parse(l)));
  const events = (kind) => records.filter((r) => r.event === kind);
  assert.ok(events("spawn").some((r) => r.test === "t.py::case (call)"), "a Python spawn under its test");
  assert.ok(events("child").every((r) => Number.isFinite(r.seconds)));
  assert.equal(events("copytree").length, 1, "one outermost copy, however deep the tree");
  assert.equal(events("rmtree").length, 1);
  assert.ok(records.some((r) => r.event === "child" && r.program === "node"), "a Node child with its seconds");
});

test("the spawn bench writes per-program samples and refuses a bad repeat count", () => {
  const out = join(scratch(), "bench.json");
  const result = run("node", [join(ROOT, "tools/ci-profile/spike/spawn-bench.mjs"), out, "1"]);
  assert.equal(result.status, 0, result.stderr);
  const bench = JSON.parse(readFileSync(out, "utf8"));
  const git = bench.spawns.find((s) => s.label === "git --version");
  assert.equal(git.n, 1);
  assert.ok(git.median > 0);
  assert.ok(bench.fs["write and remove 1000 small files"].median > 0);
  assert.equal(run("node", [join(ROOT, "tools/ci-profile/spike/spawn-bench.mjs"), out, "0"]).status, 2);
});

test("the experiment script refuses a bad round count before running anything", () => {
  const result = run("bash", [join(ROOT, "tools/ci-profile/spike/ruff-batch-experiment.sh"), scratch(), "x"]);
  assert.equal(result.status, 2);
  assert.match(result.stderr, /rounds must be a positive integer/);
});

test("the gate streams Nx's output, line by line with its seconds, when CROZIER_SPIKE_STREAM is set", () => {
  const stream = join(scratch(), "stream.log");
  const result = run("node", [join(ROOT, "tools/ci/gate.mjs"), "--sweep", "--projects=workspace", "--", "nx", "run-many", "--targets=test"], { CROZIER_SPIKE_STREAM: stream });
  assert.equal(result.status, 0, result.stdout + result.stderr);
  const lines = readFileSync(stream, "utf8").trim().split("\n");
  assert.ok(lines.every((l) => /^\d+\.\d{3}\t/.test(l)), "every line carries the seconds since the gate started");
  assert.ok(lines.some((l) => l.includes("nx run workspace:test")));
});
