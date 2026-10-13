import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { test } from 'node:test';
import { resolve } from 'node:path';
import { root, workflows } from '../workflow-graph.mjs';

test('the real gate result command propagates failed, cancelled, missing and unauthorized skipped work', () => {
  const job = workflows().find(w => w.path.endsWith('/ci.yml')).value.jobs.gate;
  assert.equal(job.if, 'always()'); assert.equal(job.name, 'gate'); assert.equal(job['runs-on'], 'ubuntu-latest');
  const command = job.steps.find(s => s.run)?.run;
  assert.equal(command, 'node .github/require-ci-results.mjs');
  const good = Object.fromEntries(job.needs.map(id => [id, { result: 'success' }]));
  good['macos-policy'].outputs = { macosRequired: 'true' };
  function run(needs) {
    return spawnSync(process.execPath, [resolve(root, command.slice(5))], { env: { ...process.env, CI_NEEDS: JSON.stringify(needs) }, encoding: 'utf8' });
  }
  assert.equal(run(good).status, 0);
  for (const id of job.needs) {
    for (const result of ['failure','cancelled','skipped',undefined]) {
      const needs = structuredClone(good);
      if (result === undefined) delete needs[id]; else needs[id].result = result;
      assert.equal(run(needs).status, 1, `${id} ${result}`);
    }
  }
  const omitted = structuredClone(good); omitted.macos.result = 'skipped'; omitted['macos-policy'].outputs.macosRequired = 'false';
  const allowed = run(omitted); assert.equal(allowed.status, 0); assert.match(allowed.stdout, /authorized Mac omission/);
  for (const result of ['failure','cancelled',undefined]) {
    omitted.macos.result = result; assert.equal(run(omitted).status, 1);
  }
  delete omitted['macos-policy'].outputs; assert.equal(run(omitted).status, 1);
  // A draft lift's reuse lane succeeds by naming the earlier run, never by skipping.
  const url = 'https://github.com/nickderobertis/crozier/actions/runs/1';
  const reused = structuredClone(good); reused['macos-policy'].outputs = { macosRequired: 'false', macosReusedRun: url };
  const proven = run(reused); assert.equal(proven.status, 0, proven.stderr);
  assert.match(proven.stdout, /no Mac job ran in this run/); assert.ok(proven.stdout.includes(url));
  assert.doesNotMatch(proven.stdout, /including Mac/);
  for (const result of ['skipped', 'failure', 'cancelled', undefined]) {
    const bad = structuredClone(reused);
    if (result === undefined) delete bad.macos; else bad.macos.result = result;
    const refused = run(bad); assert.equal(refused.status, 1, `${result}`); assert.match(refused.stderr, /Mac reuse lane did not succeed/);
  }
  for (const outputs of [{ macosRequired: 'true', macosReusedRun: url }, { macosRequired: 'false', macosReusedRun: 7 }]) {
    const bad = structuredClone(reused); bad['macos-policy'].outputs = outputs;
    assert.match(run(bad).stderr, /malformed Mac reuse decision/);
  }
});
