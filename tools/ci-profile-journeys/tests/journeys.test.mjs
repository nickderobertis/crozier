// SPIKE ONLY (spike-windows-lane-breakdown): the host-tool half of the harness's proof.
// Every case drives a real process: the built crozier binary, ruff, python, bash, the spawn
// hooks, the spawn bench and the gate. The offline reader and replay are ci-profile's.
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

// The target depends on crozier:build; run by hand, a missing binary fails here, never skips.
const requireCrozier = () => assert.ok(existsSync(CROZIER), `${CROZIER} is missing: run \`just nx run crozier:build\` first`);
const scratch = () => mkdtempSync(join(tmpdir(), "ci-profile-test-"));
// NODE_TEST_CONTEXT would make a nested `node --test` (a suite Nx starts) skip its files.
const { NODE_TEST_CONTEXT: _testContext, ...parentEnv } = process.env;
const run = (program, args, env = {}, cwd = ROOT) => spawnSync(program, args, { cwd, encoding: "utf8", env: { ...parentEnv, ...env } });

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

test("crozier writes one schema-1 profile per process only when CROZIER_PROFILE names a directory", () => {
  requireCrozier();
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
  const strip = join(dir, "strip.py");
  writeFileSync(strip, "x = 1  # a comment\n");
  for (const [args, command, code] of [[["--version"], "version", 0], [["--help"], "help", 0], [["--no-such-flag"], "usage-error", 2], [["schema"], "schema", 0], [["config", "--no-config"], "config", 0], [["internal-strip", strip], "internal-strip", 0], [["compare", join(dir, "nowhere")], "compare", 1]]) {
    const where = join(dir, command);
    assert.equal(run(CROZIER, args, { CROZIER_PROFILE: where }).status, code, args.join(" "));
    assert.deepEqual(profilesIn(where).map((p) => [p.command, p.spike.exit_code]), [[command, code]]);
  }
  assert.equal(profilesIn(profile)[0].spike.args[0], "generate", "the arguments are recorded");
  // Every argument and attribution value round-trips through the JSON, however it is spelled.
  const awkward = 'quote " backslash \\ tab \t bell \u0007 é';
  const attributed = { NX_TASK_TARGET_PROJECT: "proj", NX_TASK_TARGET_TARGET: "test", PYTEST_CURRENT_TEST: awkward, NEXTEST_TEST_NAME: "crate::case" };
  run(CROZIER, ["generate", "--spec", awkward, "--output", join(dir, "o"), "--package-name", "t", "--project-name", "t", "--no-config"], { CROZIER_PROFILE: join(dir, "esc"), ...attributed });
  const [escaped] = profilesIn(join(dir, "esc"));
  assert.equal(escaped.spike.args[2], awkward);
  assert.deepEqual([escaped.spike.nx_project, escaped.spike.nx_target, escaped.spike.pytest_test, escaped.spike.nextest_test], ["proj", "test", awkward, "crate::case"]);
  // Bare `crozier` runs every configured generator, and `init` writes a starter config.
  const project = scratch();
  writeFileSync(join(project, "spec.yml"), SPEC);
  assert.equal(run(CROZIER, ["init"], { CROZIER_PROFILE: join(dir, "init") }, project).status, 0);
  writeFileSync(join(project, "crozier.yml"), "spec: spec.yml\noutput: out\npackage-name: tiny\nproject-name: tiny\n");
  assert.equal(run(CROZIER, [], { CROZIER_PROFILE: join(dir, "bare") }, project).status, 0);
  assert.deepEqual(profilesIn(join(dir, "init")).map((p) => p.command), ["init"]);
  assert.deepEqual(profilesIn(join(dir, "bare")).map((p) => p.command), ["generate"]);
  // A destination that cannot be a directory loses the profile, never the run.
  const blocked = join(dir, "a-file");
  writeFileSync(blocked, "");
  const kept = run(CROZIER, ["--version"], { CROZIER_PROFILE: blocked });
  assert.equal(kept.status, 0);
  assert.match(kept.stdout, /^crozier /);
  assert.match(kept.stderr, /could not write the profile/);
  const failed = run(CROZIER, ["generate", "--spec", join(dir, "missing.yml"), "--output", join(dir, "x"), "--package-name", "t", "--project-name", "t", "--no-config"], { CROZIER_PROFILE: join(dir, "f") });
  assert.equal(failed.status, 1);
  assert.deepEqual(profilesIn(join(dir, "f")).map((p) => [p.command, p.spike.exit_code]), [["generate", 1]]);
});

test("one batched ruff writes the same bytes as one ruff per file, verify agrees, and an unknown mode is refused", () => {
  requireCrozier();
  const dir = scratch();
  const plain = generate(dir, {});
  const batched = generate(dir, { CROZIER_SPIKE_RUFF_BATCH: "1", CROZIER_PROFILE: join(dir, "b") });
  assert.equal(batched.result.status, 0, batched.result.stderr);
  assert.deepEqual(tree(batched.out), tree(plain.out));
  const [profile] = profilesIn(join(dir, "b"));
  assert.equal(profile.subprocesses.find((s) => s.program === "ruff").spawns, 1);
  assert.equal(generate(dir, { CROZIER_SPIKE_RUFF_BATCH: "verify" }).result.status, 0);
  // A caller's ruff configuration reaches the per-file path but not the isolated batch,
  // so verify must refuse the generation rather than write either side.
  const caller = scratch();
  writeFileSync(join(caller, "pyproject.toml"), '[tool.ruff.format]\nquote-style = "single"\n');
  writeFileSync(join(caller, "spec.yml"), SPEC);
  const mismatch = run(CROZIER, ["generate", "--spec", "spec.yml", "--output", "out", "--package-name", "tiny", "--project-name", "tiny", "--no-config"], { CROZIER_SPIKE_RUFF_BATCH: "verify" }, caller);
  assert.equal(mismatch.status, 1);
  assert.match(mismatch.stderr, /SPIKE: one batched `ruff format` differs from the per-file output/);
  assert.equal(existsSync(join(caller, "out")), false, "nothing is written");
  assert.deepEqual(readdirSync(tmpdir()).filter((n) => n.startsWith(`crozier-spike-ruff-`) && n.includes(`-${mismatch.pid}-`)), [], "the staging tree is removed");
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

test("a generation of a thousand files is formatted in several batched ruff processes to the same bytes", () => {
  requireCrozier();
  const dir = scratch();
  const spec = join(ROOT, "tests", "fixtures", "corpus-sources", "zulip", "openapi.yaml");
  const generateZulip = (out, env) => run(CROZIER, ["generate", "--spec", spec, "--output", join(dir, out), "--package-name", "zulip", "--project-name", "zulip", "--no-config"], env);
  assert.equal(generateZulip("plain", {}).status, 0);
  const batched = generateZulip("batched", { CROZIER_SPIKE_RUFF_BATCH: "1", CROZIER_PROFILE: join(dir, "p") });
  assert.equal(batched.status, 0, batched.stderr);
  assert.deepEqual(tree(join(dir, "batched")), tree(join(dir, "plain")));
  const spawns = profilesIn(join(dir, "p"))[0].subprocesses.find((s) => s.program === "ruff").spawns;
  assert.ok(spawns > 1 && spawns < 100, `the command line is split into a few processes, not one per file (${spawns})`);
});

test("the reader reads the profiles crozier really writes", () => {
  requireCrozier();
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

test("the spawn hooks charge each child and tree copy to the test that started it", () => {
  const dir = scratch();
  const hooks = join(ROOT, "tools", "ci-profile", "spike", "spawncount");
  const env = { SPIKE_SPAWN_LOG: dir, PYTHONPATH: hooks, PYTEST_CURRENT_TEST: "t.py::case (call)", NODE_OPTIONS: `--import ${new URL(`file://${join(hooks, "spawncount.mjs")}`).href}` };
  const py = run(process.platform === "win32" ? "python" : "python3", ["-c", "import shutil, subprocess, sys, tempfile; subprocess.run([sys.executable, '-c', 'pass']); d = tempfile.mkdtemp(); shutil.copytree(sys.argv[1], d + '/c'); shutil.rmtree(d)", hooks], env);
  assert.equal(py.status, 0, py.stderr);
  const failing = run(process.platform === "win32" ? "python" : "python3", ["-c", "import subprocess, sys; subprocess.run([sys.executable, '-c', 'raise SystemExit(3)'])"], env);
  assert.equal(failing.status, 0, failing.stderr);
  const forms = [
    "c.spawnSync(process.execPath, ['-e', '0'])",
    "c.execFileSync(process.execPath, ['-e', '0'])",
    "c.execSync(JSON.stringify(process.execPath) + ' -e 0')",
    "c.execFile(process.execPath, ['-e', '0'], () => {})",
    "c.exec(JSON.stringify(process.execPath) + ' -e 0', () => {})",
    "c.spawn(process.execPath, ['-e', '0'])",
    "c.fork('-e', [], { execArgv: ['-e', '0'] })",
  ];
  const nodeRun = run("node", ["-e", `const c = require('node:child_process'); ${forms.join("; ")};`], env);
  assert.equal(nodeRun.status, 0, nodeRun.stderr);
  const records = readdirSync(dir).flatMap((f) => readFileSync(join(dir, f), "utf8").trim().split("\n").map((l) => JSON.parse(l)));
  const events = (kind) => records.filter((r) => r.event === kind);
  assert.ok(events("spawn").some((r) => r.test === "t.py::case (call)"), "a Python spawn under its test");
  assert.ok(events("child").every((r) => Number.isFinite(r.seconds)));
  assert.equal(events("copytree").length, 1, "one outermost copy, however deep the tree");
  assert.equal(events("rmtree").length, 1);
  assert.ok(records.some((r) => r.event === "child" && r.pid === failing.pid), "a child that fails is still timed");
  const nodeChildren = records.filter((r) => r.event === "child" && r.pid === nodeRun.pid);
  assert.equal(nodeChildren.length, forms.length, "every child_process form records its child once it closes");
  assert.ok(nodeChildren.every((r) => Number.isFinite(r.seconds)));
  // A failed copy still raises and still resets the copy timer; a timed-out child is timed once.
  const recover = scratch();
  const recovered = run(process.platform === "win32" ? "python" : "python3", ["-c", [
    "import shutil, subprocess, sys, tempfile",
    "d = tempfile.mkdtemp()",
    "try:\n    shutil.copytree(d + '/missing', d + '/x')\nexcept FileNotFoundError:\n    pass\nelse:\n    raise SystemExit('the failed copy did not raise')",
    "shutil.copytree(sys.argv[1], d + '/ok')",
    "try:\n    subprocess.run([sys.executable, '-c', 'import time; time.sleep(30)'], timeout=0.5)\nexcept subprocess.TimeoutExpired:\n    pass",
  ].join("\n"), hooks], { ...env, SPIKE_SPAWN_LOG: recover });
  assert.equal(recovered.status, 0, recovered.stderr);
  const after = readdirSync(recover).flatMap((f) => readFileSync(join(recover, f), "utf8").trim().split("\n").map((l) => JSON.parse(l)));
  assert.equal(after.filter((r) => r.event === "copytree").length, 2, "the failed and the next copy are both timed at the outermost level");
  assert.equal(after.filter((r) => r.event === "child").length, 1, "the killed child is timed exactly once");
  // A program that cannot start keeps its own error, and is still counted.
  const failedSpawn = run("node", ["-e", "const c = require('node:child_process'); const r = c.spawnSync('no-such-program-anywhere'); if (r.error?.code !== 'ENOENT') process.exit(7); try { c.execFileSync('no-such-program-anywhere'); process.exit(8); } catch (e) { if (e.code !== 'ENOENT') process.exit(9); }"], { ...env, SPIKE_SPAWN_LOG: recover });
  assert.equal(failedSpawn.status, 0, failedSpawn.stderr);
  const nodeFailed = readdirSync(recover).flatMap((f) => readFileSync(join(recover, f), "utf8").trim().split("\n").map((l) => JSON.parse(l))).filter((r) => r.pid === failedSpawn.pid);
  assert.deepEqual(nodeFailed.map((r) => [r.event, r.program]), [["spawn", "no-such-program-anywhere"], ["child", "no-such-program-anywhere"], ["spawn", "no-such-program-anywhere"], ["child", "no-such-program-anywhere"]]);
  // A log that cannot be written loses records, never the measured call.
  const blockedLog = join(scratch(), "a-file");
  writeFileSync(blockedLog, "");
  const blockedPy = run(process.platform === "win32" ? "python" : "python3", ["-c", "import subprocess, sys; raise SystemExit(subprocess.run([sys.executable, '-c', 'raise SystemExit(4)']).returncode)"], { ...env, SPIKE_SPAWN_LOG: blockedLog });
  assert.equal(blockedPy.status, 4, blockedPy.stderr);
  const blockedNode = run("node", ["-e", "process.exit(require('node:child_process').spawnSync(process.execPath, ['-e', 'process.exit(5)']).status)"], { ...env, SPIKE_SPAWN_LOG: blockedLog });
  assert.equal(blockedNode.status, 5, blockedNode.stderr);
  const off = scratch();
  const quiet = run("node", ["-e", forms[0].replace("c.", "require('node:child_process').")], { ...env, SPIKE_SPAWN_LOG: "", SPIKE_SPAWN_OFF: "1" });
  assert.equal(quiet.status, 0);
  const quietPy = run(process.platform === "win32" ? "python" : "python3", ["-c", "import subprocess, sys; subprocess.run([sys.executable, '-c', 'pass'])"], { ...env, SPIKE_SPAWN_LOG: off, SPIKE_SPAWN_OFF: "1" });
  assert.equal(quietPy.status, 0);
  assert.deepEqual(readdirSync(off), [], "switched off, the hooks write nothing");
});

test("the spawn bench writes per-program samples the reader accepts, records a missing program, and refuses a bad repeat count", () => {
  const artifacts = scratch();
  const spike = join(artifacts, "spike-profile-test-linux");
  mkdirSync(join(artifacts, "test-timings-test-linux"), { recursive: true });
  mkdirSync(spike);
  const out = join(spike, "spawn-bench.json");
  const result = run("node", [join(ROOT, "tools/ci-profile/spike/spawn-bench.mjs"), out, "1"]);
  assert.equal(result.status, 0, result.stderr);
  const bench = JSON.parse(readFileSync(out, "utf8"));
  const git = bench.spawns.find((s) => s.label === "git --version");
  assert.equal(git.n, 1);
  assert.ok(git.median > 0);
  assert.ok(bench.fs["write and remove 1000 small files"].median > 0);
  const read = run("node", [READER, "local", artifacts]);
  assert.equal(read.status, 0, read.stderr);
  assert.equal(JSON.parse(read.stdout).lanes[0].spike.spawn_bench.spawns.length, bench.spawns.length);
  // With only node on PATH, every other program fails to start and is recorded as an error.
  const missing = join(scratch(), "bench.json");
  assert.equal(run(process.execPath, [join(ROOT, "tools/ci-profile/spike/spawn-bench.mjs"), missing, "1"], { PATH: dirname(process.execPath) }).status, 0);
  const ruff = JSON.parse(readFileSync(missing, "utf8")).spawns.find((s) => s.label === "ruff --version");
  assert.match(ruff.error, /ENOENT/);
  assert.equal(run("node", [join(ROOT, "tools/ci-profile/spike/spawn-bench.mjs"), out, "0"]).status, 2);
});

test("the experiment script refuses a bad round count before running anything", () => {
  const result = run("bash", [join(ROOT, "tools/ci-profile/spike/ruff-batch-experiment.sh"), scratch(), "x"]);
  assert.equal(result.status, 2);
  assert.match(result.stderr, /rounds must be a positive integer/);
});

test("the reader and the replay read what the pinned Nx really writes: its trace and its task graph", () => {
  const dir = scratch();
  const gate = run("node", [join(ROOT, "tools/ci/gate.mjs"), "--sweep", "--projects=workspace,gate-timing", "--", "nx", "run-many", "--targets=test"]);
  assert.equal(gate.status, 0, gate.stdout + gate.stderr);
  const log = /output in (\S+)\)/.exec(gate.stdout)[1];
  const artifacts = join(dir, "artifacts");
  const timings = join(artifacts, "test-timings-test-linux", "sweep");
  mkdirSync(timings, { recursive: true });
  writeFileSync(join(timings, "gate-1.log"), readFileSync(log, "utf8"));
  writeFileSync(join(timings, "gate-1.profile.json"), readFileSync(log.replace(/\.log$/, ".profile.json"), "utf8"));
  const out = join(dir, "report.json");
  assert.equal(run("node", [READER, "local", artifacts, "--out", out]).status, 0);
  const [lane] = JSON.parse(readFileSync(out, "utf8")).lanes;
  assert.deepEqual(lane.targets.map((t) => t.target).sort(), ["gate-timing:test", "workspace:test"]);
  assert.ok(lane.targets.every((t) => t.seconds > 0 && t.end > t.start && Number.isInteger(t.slot)));
  assert.ok(lane.cases.some((c) => c.kind === "node" && c.target === "workspace:test"), "Node's cases are attributed to their task");
  const graph = join(dir, "tasks.json");
  assert.equal(run(join(ROOT, "node_modules", ".bin", `nx${process.platform === "win32" ? ".cmd" : ""}`), ["run-many", "--targets=test", "--projects=workspace,gate-timing", `--graph=${graph}`], { NX_DAEMON: "false", NX_TUI: "false" }).status, 0);
  const replay = run("node", [join(ROOT, "tools/ci-profile/spike/schedule.mjs"), out, "test-linux", "sweep", graph]);
  assert.equal(replay.status, 0, replay.stderr);
  const wall = JSON.parse(replay.stdout).simulated.alone.observed[3];
  assert.ok(Math.abs(wall - lane.schedule.sweep.wall_seconds) < 0.5, `the replay of a real run reproduces its wall (${wall} against ${lane.schedule.sweep.wall_seconds})`);
});

test("the gate streams Nx's output, line by line with its seconds, when CROZIER_SPIKE_STREAM is set", () => {
  const stream = join(scratch(), "stream.log");
  const result = run("node", [join(ROOT, "tools/ci/gate.mjs"), "--sweep", "--projects=workspace", "--", "nx", "run-many", "--targets=test"], { CROZIER_SPIKE_STREAM: stream });
  assert.equal(result.status, 0, result.stdout + result.stderr);
  const lines = readFileSync(stream, "utf8").trim().split("\n");
  assert.ok(lines.every((l) => /^\d+\.\d{3}\t/.test(l)), "every line carries the seconds since the gate started");
  assert.ok(lines.some((l) => l.includes("nx run workspace:test")));
});
