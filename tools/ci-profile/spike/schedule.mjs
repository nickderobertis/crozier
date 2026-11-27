#!/usr/bin/env node
// SPIKE ONLY (spike-windows-lane-breakdown): replay one lane's measured task
// durations through Nx's dependency graph under other parallelism and task
// orders, to separate what ordering alone could save from what needs a task
// to get shorter.
//
//   node tools/ci-profile/spike/schedule.mjs <report.json> <job> <gate-step> <tasks.json> [--scale task=factor,...]
//
// <report.json> is `ci-profile.mjs run`'s output; <tasks.json> is the task graph
// `nx run-many ... --graph=<tasks.json>` writes for the same selection. Each task
// keeps its measured duration (times an optional factor, for projecting a repair);
// tasks Nx ran but the graph lacks (none, normally) are scheduled with no edges.
// Prints JSON: the critical path, and the simulated wall for each exclusivity mode and order at 2–6 slots.
import { readFileSync } from "node:fs";

const [reportPath, job, step, graphPath, ...rest] = process.argv.slice(2);
if (!graphPath) {
  console.error("schedule: usage: node tools/ci-profile/spike/schedule.mjs <report.json> <job> <gate-step> <tasks.json> [--scale task=factor,...]");
  process.exit(2);
}
const fail = (message) => {
  console.error(`schedule: ${message}`);
  process.exit(2);
};
const scale = new Map();
for (let i = 0; i < rest.length; i++) {
  if (rest[i] !== "--scale" || !rest[i + 1]) fail(`unknown or incomplete argument '${rest[i]}'; only --scale task=factor,... follows the four paths`);
  for (const pair of rest[++i].split(",")) {
    const [task, factor, extra] = pair.split("=");
    if (!task || extra !== undefined || !/^\d+(\.\d+)?$/.test(factor ?? "") || !Number.isFinite(Number(factor))) fail(`--scale takes task=factor pairs with a finite non-negative factor, not '${pair}'`);
    scale.set(task, Number(factor));
  }
}
const readJson = (path) => {
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch (error) {
    return fail(`${path} is not readable JSON: ${error.message}`);
  }
};
const report = readJson(reportPath);
const lane = Array.isArray(report?.lanes) ? report.lanes.find((l) => l?.job === job) : undefined;
if (!lane) fail(`${reportPath} has no lane '${job}'`);
if (!Array.isArray(lane.targets) || !lane.targets.every((t) => t !== null && typeof t === "object")) fail(`lane '${job}' has no list of targets`);
const measured = lane.targets.filter((t) => t.gate_step === step && t.start !== undefined);
if (measured.length === 0) fail(`lane '${job}' has no timed targets for gate step '${step}'`);
if (!measured.every((t) => typeof t.target === "string" && Number.isFinite(t.seconds) && t.seconds >= 0 && Number.isFinite(t.start))) fail(`lane '${job}' has a target without a name, a start and non-negative seconds`);
const graph = readJson(graphPath)?.tasks;
const isMap = (v) => v !== null && typeof v === "object" && !Array.isArray(v);
const goodDeps = isMap(graph?.dependencies) && Object.values(graph.dependencies).every((d) => Array.isArray(d) && d.every((x) => typeof x === "string"));
const goodTask = (t) => isMap(t) && (t.parallelism === undefined || typeof t.parallelism === "boolean");
if (!isMap(graph?.tasks) || !Object.values(graph.tasks).every(goodTask) || !goodDeps) fail(`${graphPath} is not the task graph \`nx run-many --graph=<file>\` writes`);
const deps = graph.dependencies;
const repeated = measured.map((t) => t.target).filter((id, i, all) => all.indexOf(id) !== i);
if (repeated.length) fail(`gate step '${step}' times ${repeated[0]} more than once; replay one gate run at a time`);
const duration = new Map(measured.map((t) => [t.target, t.seconds * (scale.get(t.target) ?? 1)]));
if (![...duration.values()].every(Number.isFinite)) fail("a scaled duration is not finite; use smaller --scale factors");
const unknown = [...scale.keys()].filter((task) => !duration.has(task));
if (unknown.length) fail(`--scale names task(s) the lane did not run: ${unknown.join(", ")}`);
const observedStart = new Map(measured.map((t) => [t.target, t.start]));
const ids = [...duration.keys()];

// Longest path from each task to the end of the graph (its own duration included).
const dependents = new Map(ids.map((id) => [id, []]));
for (const id of ids) for (const d of deps[id] ?? []) if (dependents.has(d)) dependents.get(d).push(id);
const tail = new Map();
const visiting = new Set();
const tailOf = (id) => {
  if (visiting.has(id)) fail(`the task graph has a cycle through ${id}`);
  if (!tail.has(id)) {
    visiting.add(id);
    tail.set(id, duration.get(id) + Math.max(0, ...dependents.get(id).map(tailOf)));
    visiting.delete(id);
  }
  return tail.get(id);
};
// The critical path: the chain of dependencies with the largest summed duration.
const head = new Map();
const headOf = (id) => {
  if (!head.has(id)) {
    const before = (deps[id] ?? []).filter((d) => duration.has(d));
    const best = before.sort((a, b) => headOf(b).seconds - headOf(a).seconds)[0];
    const prior = best ? headOf(best) : { seconds: 0, chain: [] };
    head.set(id, { seconds: prior.seconds + duration.get(id), chain: [...prior.chain, id] });
  }
  return head.get(id);
};
// Walking every tail first refuses a cyclic graph before the head walk could recurse forever.
for (const id of ids) tailOf(id);
const critical = ids.map(headOf).sort((a, b) => b.seconds - a.seconds)[0];

// llmlint: ignore[contracts_have_one_source_or_a_drift_gate] Reconciled against real Nx where it can be: replaying run 45840622476's own durations under "alone" reproduced its measured 7,346 s (Windows) and 4,041 s (Linux) walls exactly, and run 45863948064's 8,142 s; a committed check would need an hours-long CI run, and the pinned Nx's trace and graph envelopes are checked by ci-profile-journeys.
// Tasks Nx runs with `parallelism: false`. Nx starts one only with nothing else running and
// starts nothing beside it ("alone"); "mutex" holds them only to one at a time among
// themselves, which is what their shared cargo build directory needs; "none" ignores it.
const exclusive = new Set(Object.entries(graph.tasks).filter(([, t]) => t.parallelism === false).map(([id]) => id));

/** List scheduling: whenever a slot frees, start the ready tasks the order ranks first. */
function simulate(slots, rank, mode) {
  const done = new Map();
  const running = [];
  const pending = new Set(ids);
  let now = 0;
  while (pending.size || running.length) {
    const ready = [...pending].filter((id) => (deps[id] ?? []).every((d) => !duration.has(d) || (done.has(d) && done.get(d) <= now)));
    ready.sort((a, b) => rank(a) - rank(b));
    for (const id of ready) {
      if (running.length >= slots) break;
      const runningExclusive = running.some((r) => exclusive.has(r.id));
      if (mode === "alone") {
        if (runningExclusive) break;
        if (exclusive.has(id) && running.length > 0) continue;
      } else if (mode === "mutex" && exclusive.has(id) && runningExclusive) continue;
      pending.delete(id);
      running.push({ id, end: now + duration.get(id) });
      if (mode === "alone" && exclusive.has(id)) break;
    }
    running.sort((a, b) => a.end - b.end);
    const next = running.shift();
    if (!next) break;
    now = next.end;
    done.set(next.id, now);
    while (running.length && running[0].end <= now) {
      const also = running.shift();
      done.set(also.id, also.end);
    }
  }
  return now;
}

const orders = {
  // The order Nx actually started them in, replayed: the check that the model fits the run.
  observed: (id) => observedStart.get(id) ?? Infinity,
  // Longest remaining chain first (critical-path first).
  "longest-chain-first": (id) => -tailOf(id),
};
const result = {
  job,
  step,
  measured_wall_seconds: lane.schedule?.[step]?.wall_seconds ?? null,
  task_seconds: [...duration.values()].reduce((a, b) => a + b, 0),
  critical_path: critical,
  exclusive: [...exclusive],
  simulated: Object.fromEntries(["alone", "mutex", "none"].map((mode) => [mode, Object.fromEntries(Object.entries(orders).map(([name, rank]) => [name, Object.fromEntries([2, 3, 4, 5, 6].map((p) => [p, Math.round(simulate(p, rank, mode))]))]))])),
  scaled: Object.fromEntries(scale),
};
console.log(JSON.stringify(result, null, 2));
