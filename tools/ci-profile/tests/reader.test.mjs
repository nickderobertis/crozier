// SPIKE ONLY (spike-windows-lane-breakdown): the offline half of the harness's proof.
// The reader and the replay run as real processes over files written here; nothing
// is built, fetched or spawned beyond node. The host-tool half is ci-profile-journeys.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
const READER = join(ROOT, "tools", "ci-profile", "ci-profile.mjs");
const REPLAY = join(ROOT, "tools", "ci-profile", "spike", "schedule.mjs");
const scratch = () => mkdtempSync(join(tmpdir(), "ci-profile-test-"));
const node = (args) => spawnSync(process.execPath, args, { cwd: ROOT, encoding: "utf8" });

// The shape `CROZIER_PROFILE` writes (src/profile.rs); ci-profile-journeys reads real ones.
const PROFILE = {
  schema_version: 1,
  command: "generate",
  total_seconds: 2,
  phases: [{ name: "format", seconds: 1.5, count: 3 }, { name: "write", seconds: 0.1, count: 1 }],
  subprocesses: [{ program: "ruff", spawns: 3, seconds: 1.5 }],
  spike: { exit_code: 0, nx_project: "a", nx_target: "test", pytest_test: null, nextest_test: null, args: [] },
};

function artifactTree({ profiles = [PROFILE], runs = "mode\tround\tseconds\texit\nper-file\t1\t10\t0\nbatch\t1\t4\t0\n" } = {}) {
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
    "        FAIL [   3.000s] crate::bin failing_case",
    "       FLAKY [   0.500s] crate::bin flaky_case",
    "::endgroup::",
    "> nx run b:test",
    "2.00s call     tools/b_test.py::Case::test_one",
    "0.50s setup    tools/b_test.py::Case::test_one",
    "0.25s teardown tools/b_test.py::Case::test_one",
    "ok 1 - a node case",
    "  ---",
    "  duration_ms: 750.5",
    "    not ok 1 - a failing subtest",
    "      ---",
    "      duration_ms: 20",
    "\u001b[32m✔ a spec case \u001b[90m(125ms)\u001b[39m\r",
    "> nx run not-a-task-of-this-run",
    "        PASS [   9.000s] nested::bin a_nested_gates_case",
    "",
  ].join("\n"));
  const x = (name, ts, dur, tid) => ({ name, ph: "X", ts, dur, tid, args: { status: "success" } });
  writeFileSync(join(timings, "gate-1.profile.json"), JSON.stringify([x("a:test", 0, 4e6, 0), x("b:test", 0, 2e6, 1), x("c:test", 2e6, 1e6, 1)]));
  writeFileSync(join(spike, "crozier-profile-sweep.jsonl"), profiles.map((p) => JSON.stringify(p)).join("\n"));
  writeFileSync(join(spike, "ruff-batch", "runs.tsv"), runs);
  writeFileSync(join(spike, "runner.json"), JSON.stringify({ cpus: 4 }));
  return dir;
}

function report(dir) {
  const out = join(dir, "report.json");
  const result = node([READER, "local", dir, "--out", out]);
  assert.equal(result.status, 0, result.stderr);
  return JSON.parse(readFileSync(out, "utf8"));
}

test("the reader turns an artifact tree into per-target, per-case, slot and crozier-phase figures", () => {
  const [lane] = report(artifactTree()).lanes;
  assert.deepEqual(lane.targets.map((t) => [t.target, t.seconds, t.slot]), [["a:test", 4, 0], ["b:test", 2, 1], ["c:test", 1, 1]]);
  const cases = Object.fromEntries(lane.cases.map((c) => [`${c.kind}:${c.case}`, [c.target, c.seconds]]));
  assert.deepEqual(cases["nextest:crate::bin first_case"], ["a:test", 1.5]);
  assert.deepEqual(cases["nextest:crate::bin failing_case"], ["a:test", 3], "a failure keeps its time");
  assert.deepEqual(lane.cases.find((c) => c.case === "crate::bin flaky_case").outcome, "FLAKY");
  assert.deepEqual(cases["pytest:tools/b_test.py::Case::test_one"], ["b:test", 2.75], "setup, call and teardown are one case");
  assert.deepEqual(lane.cases.filter((c) => c.case === "a failing subtest").map((c) => [c.depth, c.seconds]), [[1, 0.02]], "a nested TAP failure keeps its depth and time");
  assert.deepEqual(cases["node:a node case"], ["b:test", 0.7505]);
  assert.deepEqual(cases["node:a spec case"], ["b:test", 0.125], "colour and a carriage return are stripped");
  assert.deepEqual(cases["nextest:nested::bin a_nested_gates_case"], ["b:test", 9], "a header naming no task of this run stays in the open section");
  assert.deepEqual(lane.schedule.sweep.running_seconds, { 0: 0, 1: 1, 2: 3 });
  const generated = lane.crozier_profile.sweep.generate;
  assert.equal(generated.ruff_seconds_per_spawn, 0.5);
  assert.equal(generated.phase_share.format.share, 0.75);
  assert.deepEqual(lane.crozier_profile.sweep.by_nx_task["a:test"].subprocesses.ruff, { seconds: 1.5, count: 3 });
  assert.deepEqual(lane.spike.ruff_batch.runs.map((r) => [r.mode, r.seconds]), [["per-file", 10], ["batch", 4]]);
});

test("the reader sums several processes by command, phase, program and Nx task", () => {
  const compare = { ...PROFILE, command: "compare", total_seconds: 1, phases: [], subprocesses: [{ program: "git", spawns: 2, seconds: 0.5 }], spike: { ...PROFILE.spike, nx_project: null, nx_target: null } };
  const sweep = report(artifactTree({ profiles: [PROFILE, PROFILE, compare] })).lanes[0].crozier_profile.sweep;
  assert.equal(sweep.processes, 3);
  assert.deepEqual(sweep.by_command, { generate: { seconds: 4, count: 2 }, compare: { seconds: 1, count: 1 } });
  assert.deepEqual(sweep.subprocesses, { ruff: { seconds: 3, count: 6 }, git: { seconds: 0.5, count: 2 } });
  assert.deepEqual(sweep.generate.ruff_spawns_per_generation.sum, 6);
  assert.equal(sweep.by_nx_task["(no Nx task)"].processes, 1);
  assert.equal(report(artifactTree({ profiles: [] })).lanes[0].crozier_profile.sweep.processes, 0);
});

test("a run is read from its cache with no fetch, its targets from the job log when no Nx profile was kept", () => {
  const cache = scratch();
  const job = { databaseId: 7, name: "test-windows", startedAt: "2026-11-26T10:00:00Z", completedAt: "2026-11-26T11:00:00Z", steps: [{ name: "Test", startedAt: "2026-11-26T10:00:00Z", completedAt: "2026-11-26T10:30:00Z" }] };
  writeFileSync(join(cache, "run.json"), JSON.stringify({ databaseId: 9, headSha: "abc", status: "completed", jobs: [job] }));
  writeFileSync(join(cache, "job-7.log"), ["2026-11-26T10:00:00.0Z ##[group]Run just ci-test", "2026-11-26T10:29:00.0Z gate: task a:test: 12.500s (success)", "2026-11-26T10:29:00.0Z gate: task b:test: 0.100s (local-cache)", ""].join("\n"));
  mkdirSync(join(cache, "artifacts"));
  // gh is not on this PATH: a fetch would fail, so success proves the cache was read.
  const result = spawnSync(process.execPath, [READER, "run", "9", "--cache-dir", cache], { cwd: ROOT, encoding: "utf8", env: { ...process.env, PATH: dirname(process.execPath) } });
  assert.equal(result.status, 0, result.stderr);
  const [lane] = JSON.parse(result.stdout).lanes;
  assert.equal(lane.seconds, 3600);
  assert.deepEqual(lane.steps.map((s) => [s.name, s.seconds]), [["Test", 1800]]);
  assert.deepEqual(lane.targets.map((t) => [t.target, t.seconds, t.cached, t.step]), [["a:test", 12.5, false, "just ci-test"], ["b:test", 0.1, true, "just ci-test"]]);
  assert.ok(lane.missing.some((m) => m.includes("no gate logs")));
});

test("two gate runs in one step stay apart, and a step without a profile keeps its job-log targets", () => {
  const cache = scratch();
  const job = { databaseId: 7, name: "test-linux", startedAt: null, completedAt: null, steps: [] };
  writeFileSync(join(cache, "run.json"), JSON.stringify({ databaseId: 9, headSha: "abc", status: "completed", jobs: [job] }));
  writeFileSync(join(cache, "job-7.log"), ["gate: task a:test: 4.000s (success)", "gate: task z:test: 2.000s (success)", ""].join("\n"));
  const timings = join(cache, "artifacts", "test-timings-test-linux", "sweep");
  mkdirSync(timings, { recursive: true });
  const x = (name, dur) => ({ name, ph: "X", ts: 0, dur, tid: 0, args: { status: "success" } });
  for (const [pid, task] of [["1", "a:test"], ["2", "b:test"]]) {
    writeFileSync(join(timings, `gate-${pid}.log`), `> nx run ${task}\n`);
    writeFileSync(join(timings, `gate-${pid}.profile.json`), JSON.stringify([x(task, 4e6)]));
  }
  const result = spawnSync(process.execPath, [READER, "run", "9", "--cache-dir", cache], { cwd: ROOT, encoding: "utf8", env: { ...process.env, PATH: dirname(process.execPath) } });
  assert.equal(result.status, 0, result.stderr);
  const [lane] = JSON.parse(result.stdout).lanes;
  assert.deepEqual(Object.keys(lane.schedule).sort(), ["sweep/gate-1", "sweep/gate-2"]);
  assert.deepEqual(lane.targets.map((t) => [t.target, t.gate_step ?? null]).sort(), [["a:test", "sweep/gate-1"], ["b:test", "sweep/gate-2"], ["z:test", null]], "a:test's job-log line is the profiled run; z:test's has no profile and is kept");
});

test("the reader refuses a bad invocation and records it cannot trust", () => {
  assert.equal(node([READER, "run", "1", "2"]).status, 2);
  assert.equal(node([READER, "run", "0"]).status, 2);
  assert.equal(node([READER, "local", scratch(), "--out"]).status, 2);
  assert.equal(node([READER, "fetch", "1"]).status, 2);
  const refused = (tree, pattern) => {
    const result = node([READER, "local", tree]);
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, pattern);
  };
  refused(artifactTree({ profiles: [{ schema_version: 2 }] }), /not a schema_version 1 CROZIER_PROFILE record/);
  refused(artifactTree({ profiles: [{ ...PROFILE, phases: [{ name: "format", seconds: -1, count: 1 }] }] }), /not a schema_version 1 CROZIER_PROFILE record/);
  refused(artifactTree({ profiles: [{ ...PROFILE, subprocesses: [{ program: "ruff", spawns: 1.5, seconds: 1 }] }] }), /not a schema_version 1 CROZIER_PROFILE record/);
  refused(artifactTree({ runs: "round\tmode\n" }), /does not start with the header/);
  const trace = artifactTree();
  writeFileSync(join(trace, "test-timings-test-linux", "sweep", "gate-1.profile.json"), JSON.stringify([null]));
  refused(trace, /not a trace event/);
  writeFileSync(join(trace, "test-timings-test-linux", "sweep", "gate-1.profile.json"), JSON.stringify([{ name: "a:test", ph: "X", ts: 0 }]));
  refused(trace, /not a timed task/);
  const bench = artifactTree();
  writeFileSync(join(bench, "spike-profile-test-linux", "spawn-bench.json"), JSON.stringify({ schema: "something-else", spawns: [] }));
  refused(bench, /not the record the spike's workflow writes there/);
  refused(artifactTree({ runs: "mode\tround\tseconds\texit\nsideways\t1\t2\t0\n" }), /not mode, round, seconds, exit/);
  refused(artifactTree({ runs: "mode\tround\tseconds\texit\nbatch\t1\t\t0\n" }), /not mode, round, seconds, exit/);
});

test("the gate's stream keeps each line whole across chunks, flushes the last one, and survives a failed write", () => {
  const dir = scratch();
  // The gate reads CROZIER_SPIKE_STREAM when it loads, so each child imports it with the variable set.
  const script = `
    const { spikeStream } = await import(${JSON.stringify(join(ROOT, "tools", "ci", "gate.mjs"))});
    const out = spikeStream(), err = spikeStream();
    const bytes = Buffer.from("café line\\nsecond", "utf8");
    out.push(bytes.subarray(0, 4)); err.push(Buffer.from("err one\\n")); out.push(bytes.subarray(4)); out.end(); err.end();`;
  const stream = (path) => spawnSync(process.execPath, ["--input-type=module", "-e", script], { cwd: ROOT, encoding: "utf8", env: { ...process.env, CROZIER_SPIKE_STREAM: path } });
  const path = join(dir, "stream.log");
  const result = stream(path);
  assert.equal(result.status, 0, result.stderr);
  assert.deepEqual(readFileSync(path, "utf8").trim().split("\n").map((l) => l.split("\t")[1]), ["err one", "café line", "second"]);
  const blocked = stream(dir);
  assert.equal(blocked.status, 0, "a stream that cannot be written never fails the run");
  assert.equal(blocked.stderr.match(/could not append to CROZIER_SPIKE_STREAM/g)?.length, 1, "it says so once");
});

function replayFixture() {
  const dir = scratch();
  const at = (target, start, seconds) => ({ target, seconds, start, end: start + seconds, gate_step: "sweep" });
  // a and x run alone (parallelism: false); b and c run in parallel; d depends on b.
  writeFileSync(join(dir, "report.json"), JSON.stringify({ lanes: [{ job: "j", schedule: { sweep: { wall_seconds: 30 } }, targets: [at("b", 0, 10), at("c", 0, 10), at("d", 10, 10), at("a", 20, 5), at("x", 25, 5)] }] }));
  const graph = (dependencies) => JSON.stringify({ tasks: { tasks: { a: { parallelism: false }, x: { parallelism: false }, b: {}, c: {}, d: {} }, dependencies } });
  writeFileSync(join(dir, "tasks.json"), graph({ d: ["b"] }));
  writeFileSync(join(dir, "cycle.json"), graph({ d: ["b"], b: ["d"] }));
  writeFileSync(join(dir, "loose.json"), JSON.stringify({ tasks: { tasks: { a: { parallelism: "no" } }, dependencies: {} } }));
  writeFileSync(join(dir, "twice.json"), JSON.stringify({ lanes: [{ job: "j", targets: [at("b", 0, 10), at("b", 10, 10)] }] }));
  return dir;
}

const replay = (dir, ...extra) => node([REPLAY, join(dir, "report.json"), "j", "sweep", join(dir, extra[0] ?? "tasks.json"), ...extra.slice(1)]);

test("the replay reproduces a measured schedule and separates Nx's exclusive tasks from a mutex", () => {
  const dir = replayFixture();
  const result = replay(dir);
  assert.equal(result.status, 0, result.stderr);
  const out = JSON.parse(result.stdout);
  assert.equal(out.simulated.alone.observed[2], 30, "replays the measured 30 s");
  assert.equal(out.simulated.mutex.observed[2], 20, "a mutex lets a and x run beside b, c and d");
  assert.equal(out.simulated.none.observed[3], 20);
  assert.equal(out.simulated.none["longest-chain-first"][5], 20, "five slots still wait on the b → d chain");
  assert.deepEqual(out.critical_path.chain, ["b", "d"]);
  assert.deepEqual(out.exclusive.sort(), ["a", "x"]);
  assert.equal(JSON.parse(replay(dir, "tasks.json", "--scale", "d=0.5").stdout).simulated.alone.observed[2], 25);
});

test("the replay refuses scale factors, lanes and graphs it cannot use", () => {
  const dir = replayFixture();
  for (const args of [["tasks.json", "--scale", "nope=1"], ["tasks.json", "--scale", "d=-1"], ["tasks.json", "--scale", `d=${"9".repeat(400)}`], ["tasks.json", "--bogus"], ["cycle.json"]]) {
    const result = replay(dir, ...args);
    assert.equal(result.status, 2, `${args.join(" ")}: ${result.stdout}${result.stderr}`);
  }
  assert.match(replay(dir, "cycle.json").stderr, /cycle/);
  assert.equal(replay(dir, "loose.json").status, 2, "parallelism must be a boolean");
  const twice = node([REPLAY, join(dir, "twice.json"), "j", "sweep", join(dir, "tasks.json")]);
  assert.equal(twice.status, 2);
  assert.match(twice.stderr, /more than once/);
  assert.equal(node([REPLAY, join(dir, "report.json"), "nobody", "sweep", join(dir, "tasks.json")]).status, 2);
});
