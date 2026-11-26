#!/usr/bin/env node
// SPIKE ONLY (spike-windows-lane-breakdown): read one `ci.yml` run of the spike's
// profiling workflow into per-lane, per-Nx-target and per-test-case seconds plus
// the aggregated crozier phase profile, as JSON. The durable reader is the plan's
// `test-profiling` node; this one writes that node's agreed `schema_version: 1`
// shape, with the spike's extra measurements under each lane's `schedule`,
// `crozier_profile` and `spike` keys.
//
//   node tools/ci-profile/ci-profile.mjs run <run-id> [--cache-dir DIR] [--out FILE]
//   node tools/ci-profile/ci-profile.mjs local <artifact-dir> [--out FILE]
//
// `run` fetches the run's jobs, each job's log and every artifact through `gh`,
// caching them under DIR (default ${XDG_CACHE_HOME:-~/.cache}/crozier/ci-profile/<run-id>)
// and reading the cache before the network; it refuses to fetch with under 40% of
// the core rate limit left. `local` reads an already-downloaded artifact tree
// (one sub-directory per artifact, as `gh run download` writes it).
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, realpathSync, renameSync, rmSync, statSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { basename, join } from "node:path";

const TOOL = "ci-profile";
const REPOSITORY = "nickderobertis/crozier";
const USAGE = `usage: node tools/ci-profile/ci-profile.mjs run <run-id> [--cache-dir DIR] [--out FILE]
       node tools/ci-profile/ci-profile.mjs local <artifact-dir> [--out FILE]`;

function die(message, action, code = 1) {
  console.error(`${TOOL}: ${message}`);
  if (action) console.error(`${TOOL}: ${action}`);
  process.exit(code);
}

function gh(args, options = {}) {
  return execFileSync("gh", args, { encoding: options.encoding ?? "utf8", maxBuffer: 1024 * 1024 * 1024, stdio: ["ignore", "pipe", "pipe"] });
}

function checkQuota() {
  const core = JSON.parse(gh(["api", "rate_limit"]))?.resources?.core;
  if (![core?.limit, core?.remaining, core?.reset].every(Number.isSafeInteger) || core.limit < 1) {
    die(`'gh api rate_limit' answered no core limit: ${JSON.stringify(core)}`, "check `gh auth status`, then rerun");
  }
  if (core.remaining / core.limit < 0.4) {
    die(`only ${core.remaining}/${core.limit} of the GitHub core rate limit remains (under 40%); no fetch made`,
      `rerun after ${new Date(core.reset * 1000).toISOString()}, or read a cached run`);
  }
}

function cached(path, fetch) {
  if (existsSync(path)) return readFileSync(path, "utf8");
  const body = fetch();
  writeFileSync(path, body);
  return body;
}

// llmlint: ignore[changed_behavior_has_e2e] SPIKE ONLY: fetching needs GitHub, its quota and a finished run, which no committed test may spend; this path read runs 45840622476 and 45863948064 (jobs, logs, artifacts) for the report, and the cache-read half is proved offline in reader.test.mjs.
function fetchRun(runId, cacheDir) {
  mkdirSync(cacheDir, { recursive: true });
  const runPath = join(cacheDir, "run.json");
  let run = existsSync(runPath) ? JSON.parse(readFileSync(runPath, "utf8")) : undefined;
  // A run still in progress is re-read; a finished one is cached for good.
  if (!run || run.status !== "completed") {
    checkQuota();
    run = JSON.parse(gh(["run", "view", String(runId), "--repo", REPOSITORY, "--json", "databaseId,headSha,status,conclusion,createdAt,updatedAt,jobs,event,headBranch"]));
    writeFileSync(runPath, JSON.stringify(run, null, 2));
  }
  const when = (v) => v === null || v === undefined || (typeof v === "string" && Number.isFinite(Date.parse(v)));
  const stepOk = (step) => typeof step?.name === "string" && when(step.startedAt) && when(step.completedAt);
  const jobOk = (job) => Number.isSafeInteger(job?.databaseId) && typeof job.name === "string" && when(job.startedAt) && when(job.completedAt) && Array.isArray(job.steps) && job.steps.every(stepOk);
  if (String(run?.databaseId) !== String(runId) || typeof run.headSha !== "string" || !Array.isArray(run.jobs) || !run.jobs.every(jobOk)) {
    die(`run ${runId}'s metadata is not a run with jobs (${runPath})`, `delete ${runPath} and rerun to fetch it again`);
  }
  if (run.status !== "completed") die(`run ${runId} is ${run.status}`, "wait for it to finish, then rerun");
  for (const job of run.jobs) {
    const logPath = join(cacheDir, `job-${job.databaseId}.log`);
    if (!existsSync(logPath)) checkQuota();
    cached(logPath, () => gh(["api", "--allow-escape-sequences", `repos/${REPOSITORY}/actions/jobs/${job.databaseId}/logs`]));
  }
  // Downloaded beside the cache and moved in whole, so a failed download is retried next time.
  const artifacts = join(cacheDir, "artifacts");
  if (!existsSync(artifacts)) {
    checkQuota();
    const partial = `${artifacts}.partial`;
    rmSync(partial, { recursive: true, force: true });
    mkdirSync(partial, { recursive: true });
    try {
      gh(["run", "download", String(runId), "--repo", REPOSITORY, "--dir", partial]);
    } catch (error) {
      const message = String(error.stderr || error.message).trim();
      if (!/no valid artifacts found/i.test(message)) {
        rmSync(partial, { recursive: true, force: true });
        die(`could not download run ${runId}'s artifacts: ${message}`, "check `gh auth status` and the run's artifact retention, then rerun");
      }
      console.error(`${TOOL}: run ${runId} has no artifacts; its report carries job-log figures only`);
    }
    renameSync(partial, artifacts);
  }
  return { run, artifacts };
}

const ANSI = /\u001b\[[0-9;]*[A-Za-z]/g;
const clean = (line) => line.replace(ANSI, "").replace(/\r$/, "");
const seconds = (a, b) => (Date.parse(b) - Date.parse(a)) / 1000;

/** A duration as a runner printed it, refused unless it is a plain finite decimal. */
function duration(text) {
  const value = Number(text);
  if (!/^\d+(\.\d+)?$/.test(text) || !Number.isFinite(value)) throw new Error(`'${text}' is not a duration a runner prints`);
  return value;
}

/** The `gate: task` lines of a job log, each with the step command that printed it. */
export function gateTaskLines(log) {
  const targets = [];
  let step;
  for (const raw of log.split("\n")) {
    const line = clean(raw).replace(/^\d{4}-\d\d-\d\dT[\d:.]+Z /, "");
    if (line.startsWith("##[group]Run ")) {
      step = line.slice("##[group]Run ".length).trim();
      continue;
    }
    const m = /^gate: task (\S+): (\d+(?:\.\d+)?)s \(([^)]+)\)$/.exec(line);
    if (m) targets.push({ target: m[1], seconds: duration(m[2]), status: m[3], cached: m[3].includes("cache"), step });
  }
  return targets;
}

const NEXTEST = /^\s*(PASS|FAIL|FLAKY|TIMEOUT|SIGSEGV|SIGABRT|LEAK|LEAK-FAIL)\s+\[\s*(\d+(?:\.\d+)?)s\]\s+(?:\(\s*\d+\/\s*\d+\)\s+)?(\S+)\s+(.+?)\s*$/;
const PYTEST = /^(\d+(?:\.\d+)?)s (setup|call|teardown)\s+(\S+::\S.*?)\s*$/;
// Node's test runner prints TAP when its output is not a terminal (CI) and its spec reporter otherwise.
const TAP_OK = /^(\s*)(?:not )?ok \d+ - (.+?)(?:\s+#.*)?$/;
const TAP_DURATION = /^\s*duration_ms: (\d+(?:\.\d+)?)$/;
const NODE = /^(\s*)[✔✖﹣]\s+(.+?)\s+\((\d+(?:\.\d+)?)ms\)(?:\s+#.*)?$/;

/** Every test case a gate log's Nx output records, attributed to the task whose section it is in. */
export function parseCases(gateLog, knownTasks) {
  const cases = [];
  const pytest = new Map();
  let target;
  let tap;
  for (const raw of gateLog.split("\n")) {
    const line = clean(raw);
    // On GitHub, Nx opens each task's output as a log group with its status icon.
    const header = /^(?:::group::\S*\s*)?>\s+nx run (\S+?)(?:\s.*)?$/.exec(line);
    if (header && (!knownTasks || knownTasks.has(header[1]))) {
      target = header[1];
      continue;
    }
    if (!target) continue;
    let m = NEXTEST.exec(line);
    if (m) {
      cases.push({ target, case: `${m[3]} ${m[4]}`, seconds: duration(m[2]), kind: "nextest", outcome: m[1] });
      continue;
    }
    m = PYTEST.exec(line);
    if (m) {
      const key = `${target}\u0000${m[3]}`;
      const entry = pytest.get(key) ?? { target, case: m[3], seconds: 0, kind: "pytest", setup: 0, call: 0, teardown: 0 };
      entry[m[2]] += duration(m[1]);
      entry.seconds += duration(m[1]);
      pytest.set(key, entry);
      continue;
    }
    m = TAP_OK.exec(line);
    if (m) {
      tap = { target, case: m[2], depth: Math.floor(m[1].length / 4) };
      continue;
    }
    m = TAP_DURATION.exec(line);
    if (m && tap) {
      cases.push({ ...tap, seconds: duration(m[1]) / 1000, kind: "node" });
      tap = undefined;
      continue;
    }
    m = NODE.exec(line);
    if (m) cases.push({ target, case: m[2], seconds: duration(m[3]) / 1000, kind: "node", depth: Math.floor(m[1].length / 2) });
  }
  return [...cases, ...pytest.values()];
}

/** Each task's start, end and slot from an Nx profile, with slot utilisation over the run. */
export function schedule(events) {
  if (!Array.isArray(events)) throw new Error("an Nx profile is a JSON array of trace events");
  if (!events.every((e) => e !== null && typeof e === "object")) throw new Error("an Nx profile holds an entry that is not a trace event");
  for (const e of events.filter((x) => x.ph === "X")) {
    if (typeof e.name !== "string" || ![e.ts, e.dur].every(Number.isFinite) || e.dur < 0 || !Number.isSafeInteger(e.tid) || e.tid < 0) throw new Error(`an Nx trace event is not a timed task: ${JSON.stringify(e).slice(0, 200)}`);
  }
  const tasks = events.filter((e) => e.ph === "X").map((e) => ({ target: e.name, start: e.ts / 1e6, end: (e.ts + e.dur) / 1e6, seconds: e.dur / 1e6, slot: e.tid, status: e.args?.status }));
  if (tasks.length === 0) return { tasks: [], wall_seconds: 0, task_seconds: 0, running_seconds: {} };
  const t0 = Math.min(...tasks.map((t) => t.start));
  const t1 = Math.max(...tasks.map((t) => t.end));
  for (const t of tasks) {
    t.start -= t0;
    t.end -= t0;
  }
  const edges = tasks.flatMap((t) => [[t.start, 1], [t.end, -1]]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const running = {};
  let level = 0;
  let at = 0;
  for (const [time, delta] of edges) {
    running[level] = (running[level] ?? 0) + (time - at);
    level += delta;
    at = time;
  }
  delete running[undefined];
  return {
    wall_seconds: t1 - t0,
    task_seconds: tasks.reduce((sum, t) => sum + t.seconds, 0),
    slots: new Set(tasks.map((t) => t.slot)).size,
    running_seconds: running,
    tasks: tasks.sort((a, b) => a.start - b.start),
  };
}

function quantiles(values) {
  const a = [...values].sort((x, y) => x - y);
  const n = a.length;
  const q = (p) => (n ? a[Math.min(n - 1, Math.floor(p * (n - 1)))] : null);
  return { n, mean: n ? a.reduce((s, x) => s + x, 0) / n : null, median: q(0.5), p90: q(0.9), max: n ? a[n - 1] : null, sum: a.reduce((s, x) => s + x, 0) };
}

/** Sum crozier's per-process profiles: by command, phase, program and Nx task. */
export function aggregateProfiles(lines) {
  const profiles = lines.filter((l) => l.trim()).map((l) => JSON.parse(l));
  for (const p of profiles) {
    const seconds = (v) => Number.isFinite(v) && v >= 0;
    const timed = (list, key, count) => Array.isArray(list) && list.every((x) => typeof x?.[key] === "string" && seconds(x.seconds) && Number.isSafeInteger(x[count]) && x[count] >= 0);
    const named = (v) => v === null || v === undefined || typeof v === "string";
    if (p?.schema_version !== 1 || typeof p.command !== "string" || !named(p.spike?.nx_project) || !named(p.spike?.nx_target) || !seconds(p.total_seconds) || !timed(p.phases, "name", "count") || !timed(p.subprocesses, "program", "spawns")) {
      throw new Error(`not a schema_version 1 CROZIER_PROFILE record: ${JSON.stringify(p).slice(0, 200)}`);
    }
  }
  const add = (map, key, seconds, count = 1) => {
    const e = map[key] ?? (map[key] = { seconds: 0, count: 0 });
    e.seconds += seconds;
    e.count += count;
  };
  // Names come from outside: null-prototype maps, so `__proto__` or `constructor` is just a key.
  const map = () => Object.create(null);
  const byCommand = map();
  const phases = map();
  const subprocesses = map();
  const byTask = map();
  const generate = profiles.filter((p) => p.command === "generate");
  for (const p of profiles) {
    add(byCommand, p.command, p.total_seconds);
    const task = p.spike?.nx_project ? `${p.spike.nx_project}:${p.spike.nx_target}` : "(no Nx task)";
    const t = byTask[task] ?? (byTask[task] = { processes: 0, seconds: 0, phases: map(), subprocesses: map() });
    t.processes += 1;
    t.seconds += p.total_seconds;
    for (const ph of p.phases) {
      add(phases, ph.name, ph.seconds, ph.count);
      add(t.phases, ph.name, ph.seconds, ph.count);
    }
    for (const s of p.subprocesses) {
      add(subprocesses, s.program, s.seconds, s.spawns);
      add(t.subprocesses, s.program, s.seconds, s.spawns);
    }
  }
  const ruffOf = (p) => p.subprocesses.find((s) => s.program === "ruff") ?? { spawns: 0, seconds: 0 };
  const generateTotal = generate.reduce((s, p) => s + p.total_seconds, 0);
  const generatePhases = map();
  for (const p of generate) for (const ph of p.phases) add(generatePhases, ph.name, ph.seconds, ph.count);
  const ruffSpawns = generate.reduce((s, p) => s + ruffOf(p).spawns, 0);
  const ruffSeconds = generate.reduce((s, p) => s + ruffOf(p).seconds, 0);
  return {
    processes: profiles.length,
    seconds: profiles.reduce((s, p) => s + p.total_seconds, 0),
    by_command: byCommand,
    phases,
    subprocesses,
    generate: {
      processes: generate.length,
      seconds: generateTotal,
      phase_share: Object.fromEntries(Object.entries(generatePhases).map(([k, v]) => [k, { ...v, share: generateTotal ? v.seconds / generateTotal : null }])),
      ruff_spawns_per_generation: quantiles(generate.map((p) => ruffOf(p).spawns)),
      ruff_seconds_per_generation: quantiles(generate.map((p) => ruffOf(p).seconds)),
      seconds_per_generation: quantiles(generate.map((p) => p.total_seconds)),
      ruff_seconds_per_spawn: ruffSpawns ? ruffSeconds / ruffSpawns : null,
    },
    by_nx_task: byTask,
  };
}

function walk(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    return statSync(path).isDirectory() ? walk(path) : [path];
  });
}

/** An artifact's JSON file, refused unless `valid` holds for it; undefined when it is absent. */
function readJson(path, valid) {
  if (!existsSync(path)) return undefined;
  const value = JSON.parse(readFileSync(path, "utf8"));
  if (!valid(value)) throw new Error(`${path} is not the record the spike's workflow writes there`);
  return value;
}
const object = (v) => v !== null && typeof v === "object" && !Array.isArray(v);
const natural = (v) => Number.isSafeInteger(v) && v >= 0;
const RUNNER = (v) => object(v) && Number.isSafeInteger(v.cpus) && v.cpus > 0;
const STEP = (v) => object(v) && typeof v.step === "string" && natural(v.seconds) && natural(v.exit);
const timing = (s) => object(s) && Number.isSafeInteger(s.n) && s.n > 0 && [s.median, s.mean, s.min, s.max].every((x) => Number.isFinite(x) && x >= 0);
// spawn-bench.mjs writes this schema: a timed spawn has n and median, a failed one an error.
const SPAWN_BENCH = (v) => object(v) && v.schema === "spike-spawn-bench-1" && Array.isArray(v.spawns) && v.spawns.every((s) => typeof s?.label === "string" && (typeof s.error === "string" || timing(s))) && object(v.fs) && Object.values(v.fs).every(timing);

/** One lane's figures from its job (if read from a run) and its two artifacts. */
function lane(job, jobLog, artifacts) {
  const name = job?.name ?? "local";
  const timings = join(artifacts, `test-timings-${name}`);
  const spike = join(artifacts, `spike-profile-${name}`);
  const missing = [];
  const steps = (job?.steps ?? []).map((s) => ({ name: s.name, seconds: s.startedAt && s.completedAt ? seconds(s.startedAt, s.completedAt) : null, conclusion: s.conclusion }));
  const files = walk(timings);
  const gateSteps = {};
  const logs = files.filter((f) => /gate-\d+\.log$/.test(f));
  const dirOf = (log) => basename(join(log, ".."));
  for (const log of logs) {
    // A step that ran the gate more than once keeps each run apart, named by its log.
    const shared = logs.filter((other) => dirOf(other) === dirOf(log)).length > 1;
    const stepName = shared ? `${dirOf(log)}/${basename(log, ".log")}` : dirOf(log);
    const profilePath = log.replace(/\.log$/, ".profile.json");
    const sched = existsSync(profilePath) ? schedule(JSON.parse(readFileSync(profilePath, "utf8"))) : undefined;
    const known = sched ? new Set(sched.tasks.map((t) => t.target)) : undefined;
    const text = readFileSync(log, "utf8");
    const parallel = /--parallel[= ](\d+)/.exec(text)?.[1];
    gateSteps[stepName] = { log, schedule: sched, cases: parseCases(text, known), parallel };
  }
  // Each gate step's Nx profile is the source of its targets, with their start, end and slot.
  // The job log's `gate: task` lines (which name no step) add what no kept profile covers:
  // one line per target is spent for each profiled run of that target.
  const profiled = Object.entries(gateSteps).filter(([, g]) => g.schedule);
  const targets = profiled.flatMap(([stepName, g]) => g.schedule.tasks.map((t) => ({ target: t.target, seconds: t.seconds, status: t.status, cached: String(t.status).includes("cache"), gate_step: stepName, start: t.start, end: t.end, slot: t.slot })));
  const covered = new Map();
  for (const t of targets) covered.set(t.target, (covered.get(t.target) ?? 0) + 1);
  for (const line of jobLog ? gateTaskLines(jobLog) : []) {
    const left = covered.get(line.target) ?? 0;
    if (left > 0) covered.set(line.target, left - 1);
    else targets.push(line);
  }
  if (Object.keys(gateSteps).length === 0) missing.push(`no gate logs in artifact test-timings-${name}`);
  const cases = Object.entries(gateSteps).flatMap(([stepName, g]) => g.cases.map((c) => ({ ...c, gate_step: stepName })));
  const casedTargets = new Set(cases.map((c) => c.target));
  for (const t of targets) if (t.seconds > 30 && !casedTargets.has(t.target)) missing.push(`per-case seconds for ${t.target} (its runner prints none: unittest, a script, or a cargo build)`);
  const crozier = {};
  for (const f of walk(spike).filter((f) => /crozier-profile-.*\.jsonl$/.test(f))) {
    crozier[basename(f).replace(/^crozier-profile-|\.jsonl$/g, "")] = aggregateProfiles(readFileSync(f, "utf8").split("\n"));
  }
  const ruffBatch = {};
  const runsTsv = join(spike, "ruff-batch", "runs.tsv");
  if (existsSync(runsTsv)) {
    const [header, ...lines] = readFileSync(runsTsv, "utf8").trim().split("\n");
    if (header !== "mode\tround\tseconds\texit") throw new Error(`${runsTsv} does not start with the header ruff-batch-experiment.sh writes`);
    const rows = lines.map((l) => l.split("\t"));
    const MODES = new Set(["per-file", "batch", "verify"]);
    const count = (v) => /^\d+$/.test(v) && Number.isSafeInteger(Number(v));
    const secs = (v) => /^\d+(\.\d+)?$/.test(v) && Number.isFinite(Number(v));
    if (!rows.every((r) => r.length === 4 && MODES.has(r[0]) && count(r[1]) && secs(r[2]) && count(r[3]))) throw new Error(`${runsTsv} has a row that is not mode, round, seconds, exit`);
    ruffBatch.runs = rows.map(([mode, round, secs, exit]) => ({ mode, round: Number(round), seconds: Number(secs), exit: Number(exit) }));
    for (const f of walk(join(spike, "ruff-batch")).filter((f) => f.endsWith(".jsonl"))) {
      ruffBatch[basename(f, ".jsonl")] = aggregateProfiles(readFileSync(f, "utf8").split("\n"));
    }
  }
  const stepFiles = walk(spike).filter((f) => /step-.*\.json$/.test(f)).map((f) => readJson(f, STEP));
  return {
    job: name,
    os: job ? (name.includes("windows") ? "windows" : name.includes("macos") ? "macos" : "linux") : process.platform,
    seconds: job?.startedAt && job?.completedAt ? seconds(job.startedAt, job.completedAt) : null,
    steps,
    targets,
    cases: cases.sort((a, b) => b.seconds - a.seconds),
    missing,
    schedule: Object.fromEntries(Object.entries(gateSteps).map(([k, g]) => [k, g.schedule && { ...g.schedule, tasks: undefined, parallel: g.parallel }])),
    crozier_profile: crozier,
    spike: {
      runner: readJson(join(spike, "runner.json"), RUNNER),
      gate_steps: stepFiles,
      spawn_bench: readJson(join(spike, "spawn-bench.json"), SPAWN_BENCH),
      ruff_batch: ruffBatch,
    },
  };
}

function main() {
  const argv = process.argv.slice(2);
  const verb = argv.shift();
  const flags = {};
  const positional = [];
  while (argv.length) {
    const arg = argv.shift();
    if (arg === "--cache-dir" || arg === "--out") {
      const value = argv.shift();
      if (!value || value.startsWith("--")) die(`${arg} takes a path`, USAGE, 2);
      flags[arg.slice(2)] = value;
    } else if (arg.startsWith("--")) die(`unknown argument '${arg}'`, USAGE, 2);
    else positional.push(arg);
  }
  if (positional.length !== 1) die(`expected one ${verb === "local" ? "artifact directory" : "run id"}, got ${positional.length}`, USAGE, 2);
  let report;
  if (verb === "run" && /^[1-9]\d{0,15}$/.test(positional[0]) && Number.isSafeInteger(Number(positional[0]))) {
    const runId = positional[0];
    const cacheDir = flags["cache-dir"] ?? join(process.env.XDG_CACHE_HOME || join(homedir(), ".cache"), "crozier", "ci-profile", runId);
    const { run, artifacts } = fetchRun(runId, cacheDir);
    report = {
      schema_version: 1,
      source: { kind: "run", run_id: Number(runId), head_sha: run.headSha },
      lanes: run.jobs.map((job) => lane(job, readFileSync(join(cacheDir, `job-${job.databaseId}.log`), "utf8"), artifacts)),
    };
  } else if (verb === "local" && existsSync(positional[0])) {
    const dir = positional[0];
    const names = readdirSync(dir).filter((n) => n.startsWith("test-timings-")).map((n) => n.slice("test-timings-".length));
    report = { schema_version: 1, source: { kind: "local", run_id: null, head_sha: null }, lanes: names.map((name) => lane({ name }, undefined, dir)) };
  } else {
    die("expected `run <run-id>` or `local <artifact-dir>`", USAGE, 2);
  }
  const text = `${JSON.stringify(report, null, 2)}\n`;
  if (flags.out) {
    writeFileSync(flags.out, text);
    console.log(`${TOOL}: wrote ${flags.out}`);
  } else process.stdout.write(text);
}

if (process.argv[1] && existsSync(process.argv[1]) && realpathSync(process.argv[1]) === import.meta.filename) main();
