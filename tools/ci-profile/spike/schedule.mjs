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
// Prints JSON: the critical path, and the simulated wall for each order at 2–6 slots.
import { readFileSync } from "node:fs";

const [reportPath, job, step, graphPath, ...rest] = process.argv.slice(2);
if (!graphPath) {
  console.error("schedule: usage: node tools/ci-profile/spike/schedule.mjs <report.json> <job> <gate-step> <tasks.json> [--scale task=factor,...]");
  process.exit(2);
}
const scale = new Map();
for (let i = 0; i < rest.length; i++) {
  if (rest[i] === "--scale") for (const pair of rest[++i].split(",")) {
    const [task, factor] = pair.split("=");
    scale.set(task, Number(factor));
  }
}
const report = JSON.parse(readFileSync(reportPath, "utf8"));
const lane = report.lanes.find((l) => l.job === job);
if (!lane) throw new Error(`no lane ${job}`);
const measured = lane.targets.filter((t) => t.gate_step === step && t.start !== undefined);
const graph = JSON.parse(readFileSync(graphPath, "utf8")).tasks;
const deps = graph.dependencies;
const duration = new Map(measured.map((t) => [t.target, t.seconds * (scale.get(t.target) ?? 1)]));
const observedStart = new Map(measured.map((t) => [t.target, t.start]));
const ids = [...duration.keys()];

// Longest path from each task to the end of the graph (its own duration included).
const dependents = new Map(ids.map((id) => [id, []]));
for (const id of ids) for (const d of deps[id] ?? []) if (dependents.has(d)) dependents.get(d).push(id);
const tail = new Map();
const tailOf = (id) => {
  if (!tail.has(id)) tail.set(id, duration.get(id) + Math.max(0, ...dependents.get(id).map(tailOf)));
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
const critical = ids.map(headOf).sort((a, b) => b.seconds - a.seconds)[0];

/** List scheduling: whenever a slot frees, start the ready task the order ranks first. */
function simulate(slots, rank) {
  const done = new Map();
  const running = [];
  const pending = new Set(ids);
  let now = 0;
  while (pending.size || running.length) {
    const ready = [...pending].filter((id) => (deps[id] ?? []).every((d) => !duration.has(d) || (done.has(d) && done.get(d) <= now)));
    ready.sort((a, b) => rank(a) - rank(b));
    while (running.length < slots && ready.length) {
      const id = ready.shift();
      pending.delete(id);
      running.push({ id, end: now + duration.get(id) });
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
  // Longest remaining chain first (critical-path first), then longest task.
  "longest-chain-first": (id) => -tailOf(id),
};
const result = {
  job,
  step,
  measured_wall_seconds: lane.schedule?.[step]?.wall_seconds ?? null,
  task_seconds: [...duration.values()].reduce((a, b) => a + b, 0),
  critical_path: critical,
  simulated: Object.fromEntries(Object.entries(orders).map(([name, rank]) => [name, Object.fromEntries([2, 3, 4, 5, 6].map((p) => [p, simulate(p, rank)]))])),
  scaled: Object.fromEntries(scale),
};
console.log(JSON.stringify(result, null, 2));
