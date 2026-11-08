import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { test } from 'node:test';
import { resolve } from 'node:path';
import { root, workflows } from '../workflow-graph.mjs';

const job = workflows().find(w => w.path.endsWith('/ci.yml')).value.jobs.gate;
const TEST_LANES = ['test-linux', 'test-windows', 'test-macos'];
function run(needs) {
  return spawnSync(process.execPath, [resolve(root, job.steps.find(s => s.run).run.slice(5))], { env: { ...process.env, CI_NEEDS: JSON.stringify(needs) }, encoding: 'utf8' });
}
const good = () => Object.fromEntries(job.needs.map(id => [id, { result: 'success' }]));

test('the real gate result command propagates failed, cancelled, missing and unauthorized skipped work', () => {
  assert.equal(job.if, "always() && github.event_name == 'pull_request'"); assert.equal(job.name, 'gate'); assert.equal(job['runs-on'], 'ubuntu-latest');
  assert.deepEqual(job.needs, ['lint', ...TEST_LANES, 'commitlint', 'llmlint']);
  assert.equal(job.steps.find(s => s.run)?.run, 'node .github/require-ci-results.mjs');
  assert.equal(run(good()).status, 0);
  for (const id of job.needs) {
    for (const result of ['failure', 'cancelled', 'skipped', undefined]) {
      const needs = good();
      if (result === undefined) delete needs[id]; else needs[id].result = result;
      assert.equal(run(needs).status, 1, `${id} ${result}`);
    }
  }
  for (const needs of [undefined, 'not json', '{}']) {
    const failed = spawnSync(process.execPath, [resolve(root, '.github/require-ci-results.mjs')], { env: { ...process.env, CI_NEEDS: needs }, encoding: 'utf8' });
    assert.equal(failed.status, 1, String(needs));
  }
});

test('skipped test lanes count only on the real guard step having passed, never by branch name', () => {
  const skipped = (lint) => ({ ...good(), lint, ...Object.fromEntries(TEST_LANES.map(id => [id, { result: 'skipped' }])) });
  const accepted = run(skipped({ result: 'success', outputs: { releaseGuard: 'passed' } }));
  assert.equal(accepted.status, 0, accepted.stderr); assert.match(accepted.stdout, /release guard passed/);
  for (const lint of [{ result: 'success' }, { result: 'success', outputs: {} }, { result: 'success', outputs: { releaseGuard: 'failed' } }, { result: 'failure', outputs: { releaseGuard: 'passed' } }]) {
    assert.equal(run(skipped(lint)).status, 1, JSON.stringify(lint));
  }
  for (const id of TEST_LANES) for (const result of ['failure', 'cancelled', undefined]) {
    const needs = skipped({ result: 'success', outputs: { releaseGuard: 'passed' } });
    if (result === undefined) delete needs[id]; else needs[id].result = result;
    assert.equal(run(needs).status, 1, `guard does not excuse ${id} ${result}`);
  }
});
