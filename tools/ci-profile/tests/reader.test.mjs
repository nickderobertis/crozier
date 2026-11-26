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
    "::endgroup::",
    "> nx run b:test",
    "2.00s call     tools/b_test.py::Case::test_one",
    "0.50s setup    tools/b_test.py::Case::test_one",
    "ok 1 - a node case",
    "  ---",
    "  duration_ms: 750.5",
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
  assert.deepEqual(cases["pytest:tools/b_test.py::Case::test_one"], ["b:test", 2.5]);
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
  refused(artifactTree({ runs: "mode\tround\tseconds\texit\nsideways\t1\t2\t0\n" }), /not mode, round, seconds, exit/);
  refused(artifactTree({ runs: "mode\tround\tseconds\texit\nbatch\t1\t\t0\n" }), /not mode, round, seconds, exit/);
});

test("the workflow uploads the artifacts the reader reads, and the experiment writes the columns it parses", () => {
  const workflow = readFileSync(join(ROOT, ".github", "workflows", "ci.yml"), "utf8");
  const reader = readFileSync(READER, "utf8");
  for (const prefix of ["test-timings-", "spike-profile-"]) {
    assert.ok(workflow.includes(`name: ${prefix}\${{ github.job }}`), `ci.yml uploads ${prefix}<job>`);
    assert.ok(reader.includes(`\`${prefix}\${name}\``), `the reader reads ${prefix}<job>`);
  }
  assert.ok(readFileSync(join(ROOT, "tools", "ci-profile", "spike", "ruff-batch-experiment.sh"), "utf8").includes("printf 'mode\\tround\\tseconds\\texit\\n'"));
  assert.ok(reader.includes('"mode\\tround\\tseconds\\texit"'));
});

function replayFixture() {
  const dir = scratch();
  const at = (target, start, seconds) => ({ target, seconds, start, end: start + seconds, gate_step: "sweep" });
  // a and x run alone (parallelism: false); b and c run in parallel; d depends on b.
  writeFileSync(join(dir, "report.json"), JSON.stringify({ lanes: [{ job: "j", schedule: { sweep: { wall_seconds: 30 } }, targets: [at("b", 0, 10), at("c", 0, 10), at("d", 10, 10), at("a", 20, 5), at("x", 25, 5)] }] }));
  const graph = (dependencies) => JSON.stringify({ tasks: { tasks: { a: { parallelism: false }, x: { parallelism: false }, b: {}, c: {}, d: {} }, dependencies } });
  writeFileSync(join(dir, "tasks.json"), graph({ d: ["b"] }));
  writeFileSync(join(dir, "cycle.json"), graph({ d: ["b"], b: ["d"] }));
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
  assert.equal(node([REPLAY, join(dir, "report.json"), "nobody", "sweep", join(dir, "tasks.json")]).status, 2);
});
