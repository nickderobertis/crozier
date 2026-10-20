#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { report } from '@onebudgetspec/sdk';
// Reports the weekly Fern goldens run's predicted minutes from the plan the
// shard planner recorded; it never plans anything itself.
// Exit 0 reports existing telemetry; 1 is telemetry/IO/report failure; 2 is invalid invocation.
class InvocationError extends Error {}
const finite = value => typeof value === 'number' && Number.isFinite(value) && value >= 0;
try {
  const [flag, path, ...extra] = process.argv.slice(2);
  if (flag !== '--telemetry' || !path || extra.length) throw new InvocationError('usage: fern-goldens-budget.mjs --telemetry JSON');
  const plan = JSON.parse(readFileSync(resolve(path), 'utf8'));
  const incomplete = reason => { throw new Error(`incomplete telemetry ${path}: ${reason}; record it with the github-workflows test, which runs tools/fern-goldens/weekly.py plan over the whole inventory`); };
  const families = plan?.families;
  const shards = plan?.shards;
  const estimate = plan?.estimate;
  if (plan?.schema_version !== 1 || plan.complete !== true) incomplete('it is no plan of the whole inventory');
  if (!families || typeof families !== 'object' || !Object.keys(families).length) incomplete('it names no family');
  if (!Object.values(families).every(family => Number.isInteger(family?.items) && family.items > 0 && finite(family.seconds))) incomplete('a family has no items or no seconds');
  if (!Array.isArray(shards) || !shards.length || !shards.every(shard => finite(shard?.minutes) && Array.isArray(shard.items))) incomplete('it plans no shard');
  if (!finite(estimate?.minutes)) incomplete('it predicts no minutes');
  const planned = shards.flatMap(shard => shard.items);
  const keys = new Set(planned.map(entry => `${entry?.family}\t${entry?.item}`));
  if (keys.size !== planned.length) incomplete('it plans an item twice');
  for (const [name, family] of Object.entries(families)) {
    if (planned.filter(entry => entry.family === name).length !== family.items) incomplete(`its shards do not hold every ${name} item`);
  }
  if (planned.some(entry => !(entry.family in families))) incomplete('a shard holds an item of no planned family');
  const items = planned.length;
  const detail = JSON.stringify({
    items,
    families,
    shards: shards.length,
    shardMinutes: shards.map(shard => shard.minutes),
    longestShardMinutes: estimate.longest_shard_minutes,
    setupMinutesPerJob: estimate.setup_minutes_per_job,
    assemblyMinutes: estimate.assembly_minutes,
    stages: estimate.stages,
    waves: estimate.waves,
  });
  report(estimate.minutes, detail);
  console.log(`weekly minutes: ${estimate.minutes}`);
} catch (error) { console.error(`fern-goldens-budget: ${error.message}`); process.exitCode = error instanceof InvocationError ? 2 : 1; }
