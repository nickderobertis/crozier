#!/usr/bin/env node
// SPIKE ONLY (spike-windows-lane-breakdown): the two small records the profiling workflow
// writes beside its measurements, and the checks ci-profile.mjs reads them back with, so
// the writer and the reader are one source.
//
//   node tools/ci-profile/spike/record.mjs runner <out.json>
//   node tools/ci-profile/spike/record.mjs step <out.json> <step> <seconds> <exit>
import { writeFileSync } from "node:fs";
import { cpus, platform, release, totalmem } from "node:os";

const object = (v) => v !== null && typeof v === "object" && !Array.isArray(v);
const natural = (v) => Number.isSafeInteger(v) && v >= 0;
const text = (v) => v === undefined || v === null || typeof v === "string";

/** The runner a job ran on: its platform, processors and Nx parallelism. */
export function runnerRecord(env = process.env) {
  return { job: env.GITHUB_JOB, platform: platform(), release: release(), cpus: cpus().length, cpu_model: cpus()[0]?.model, memory_bytes: totalmem(), nx_parallel: env.NX_PARALLEL };
}

/** One measured workflow step: its wall seconds and exit status. */
export function stepRecord(step, seconds, exit) {
  return { step, seconds, exit };
}

export const isRunner = (v) => object(v) && Number.isSafeInteger(v.cpus) && v.cpus > 0 && [v.job, v.platform, v.release, v.cpu_model, v.nx_parallel].every(text) && (v.memory_bytes === undefined || natural(v.memory_bytes));
export const isStep = (v) => object(v) && typeof v.step === "string" && v.step !== "" && natural(v.seconds) && natural(v.exit);

function main() {
  const [kind, out, ...rest] = process.argv.slice(2);
  const fail = (message) => {
    console.error(`record: ${message}`);
    console.error("record: usage: record.mjs runner <out.json> | record.mjs step <out.json> <step> <seconds> <exit>");
    process.exit(2);
  };
  if (!out) fail("an output path is required");
  let record;
  if (kind === "runner" && rest.length === 0) record = runnerRecord();
  else if (kind === "step" && rest.length === 3 && rest.slice(1).every((v) => /^\d+$/.test(v))) record = stepRecord(rest[0], Number(rest[1]), Number(rest[2]));
  else fail(`'${[kind, ...rest].join(" ")}' is not a record this writes`);
  if (!(kind === "runner" ? isRunner : isStep)(record)) fail(`the ${kind} record would not read back: ${JSON.stringify(record)}`);
  writeFileSync(out, `${JSON.stringify(record)}\n`);
}

if (process.argv[1] && import.meta.filename === (await import("node:fs")).realpathSync(process.argv[1])) main();
