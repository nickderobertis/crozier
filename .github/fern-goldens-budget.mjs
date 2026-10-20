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
  const families = plan?.families;
  const shards = plan?.shards;
  const estimate = plan?.estimate;
  if (plan?.schema_version !== 1 || plan.complete !== true || !families || !Array.isArray(shards) || !shards.length
    || !finite(estimate?.minutes) || !shards.every(shard => finite(shard?.minutes) && Array.isArray(shard.items))
    || !Object.values(families).every(family => finite(family?.items) && finite(family?.seconds))) {
    throw new Error(`incomplete telemetry ${path}: record it with the github-workflows test, which runs tools/fern-goldens/weekly.py plan over the whole inventory`);
  }
  const items = Object.values(families).reduce((sum, family) => sum + family.items, 0);
  if (items !== shards.reduce((sum, shard) => sum + shard.items.length, 0)) throw new Error(`incomplete telemetry ${path}: its shards do not hold every planned item`);
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
