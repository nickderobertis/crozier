import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { test } from 'node:test';
import { root } from '../workflow-graph.mjs';

const telemetry = resolve(root, '.github/.telemetry/fern-goldens-plan.json');
const reader = resolve(root, '.github/fern-goldens-budget.mjs');

// Records, never bounds: the budget check reads these figures; this test only
// makes the workflow's real planner write them over the finished tree.
test('the weekly shard planner records its plan of the whole reference inventory', () => {
  const env = { ...process.env };
  delete env.CROZIER_FERN_WEEKLY_ROOT;
  const run = spawnSync('python3', [resolve(root, 'tools/fern-goldens/weekly.py'), 'plan', '--telemetry', telemetry], { cwd: root, env, encoding: 'utf8' });
  assert.equal(run.status, 0, run.stderr);
  const plan = JSON.parse(readFileSync(telemetry, 'utf8'));
  assert.equal(plan.complete, true);
  assert.deepEqual(Object.keys(plan.families), ['corpus', 'overlays', 'handwritten', 'measurements', 'probes', 'authored-probes', 'refusals', 'departure-evidence']);
  const planned = plan.shards.flatMap(shard => shard.items);
  assert.equal(planned.length, Object.values(plan.families).reduce((sum, family) => sum + family.items, 0));
  console.log(`fern-goldens plan: ${planned.length} items, ${plan.shards.length} shards, ${plan.estimate.minutes} minutes predicted`);
});

test('the reader reports the recorded minutes and their detail through the SDK', t => {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'fern-goldens-report-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const env = { ...process.env };
  delete env.CROZIER_FERN_WEEKLY_ROOT;
  const recorded = join(dir, 'plan.json');
  const planned = spawnSync('python3', [resolve(root, 'tools/fern-goldens/weekly.py'), 'plan', '--telemetry', recorded], { cwd: root, env, encoding: 'utf8' });
  assert.equal(planned.status, 0, planned.stderr);
  const plan = JSON.parse(readFileSync(recorded, 'utf8'));
  const result = join(dir, 'result.json');
  const run = spawnSync(process.execPath, [reader, '--telemetry', recorded], { encoding: 'utf8', env: { ...process.env, ONEBUDGETSPEC_RESULT: result } });
  assert.equal(run.status, 0, run.stderr);
  const reported = JSON.parse(readFileSync(result, 'utf8'));
  assert.equal(reported.value, plan.estimate.minutes);
  const detail = JSON.parse(reported.detail);
  assert.deepEqual(detail.families, plan.families);
  assert.equal(detail.shards, plan.shards.length);
  assert.deepEqual(detail.shardMinutes, plan.shards.map(shard => shard.minutes));
  assert.equal(detail.longestShardMinutes, Math.max(...plan.shards.map(shard => shard.minutes)));
  assert.equal(detail.setupMinutesPerJob, plan.estimate.setup_minutes_per_job);
  assert.equal(detail.assemblyMinutes, plan.estimate.assembly_minutes);
});

test('the reader refuses a usage error, missing telemetry and a subset plan', t => {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'fern-goldens-refusals-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const usage = spawnSync(process.execPath, [reader], { encoding: 'utf8' });
  assert.equal(usage.status, 2);
  assert.match(usage.stderr, /usage:/);
  const missing = spawnSync(process.execPath, [reader, '--telemetry', join(dir, 'absent.json')], { encoding: 'utf8' });
  assert.equal(missing.status, 1);
  assert.match(missing.stderr, /ENOENT/);
  const subset = join(dir, 'subset.json');
  writeFileSync(subset, JSON.stringify({ schema_version: 1, complete: false, families: {}, shards: [], estimate: { minutes: 1 } }));
  const partial = spawnSync(process.execPath, [reader, '--telemetry', subset], { encoding: 'utf8' });
  assert.equal(partial.status, 1);
  assert.match(partial.stderr, /incomplete telemetry/);
  const item = { family: 'corpus', item: 'anchore.io', seconds: 16.2 };
  const shard = { index: 0, seconds: 32.4, minutes: 4.54, items: [item, item] };
  for (const [plan, reason] of [
    [{ families: { corpus: { items: 2, seconds: 32.4 } }, shards: [shard] }, /plans an item twice/],
    [{ families: { corpus: { items: 1, seconds: 16.2 }, probes: { items: 1, seconds: 16.2 } }, shards: [{ ...shard, items: [item] }] }, /do not hold every probes item/],
    [{ families: {}, shards: [shard] }, /names no family/],
  ]) {
    const file = join(dir, 'bad.json');
    writeFileSync(file, JSON.stringify({ schema_version: 1, complete: true, estimate: { minutes: 9 }, ...plan }));
    const refused = spawnSync(process.execPath, [reader, '--telemetry', file], { encoding: 'utf8' });
    assert.equal(refused.status, 1);
    assert.match(refused.stderr, reason);
  }
});
