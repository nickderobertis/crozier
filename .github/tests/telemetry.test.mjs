import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { writeFileSync, mkdtempSync, rmSync, cpSync, symlinkSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join, basename } from 'node:path';
import { test } from 'node:test';
import { root, digest } from '../workflow-graph.mjs';

test('measurement refuses missing or stale telemetry instead of rerunning scenarios', t => {
  const dir=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'macos-telemetry-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  const file=join(dir,'stale.json');
  writeFileSync(file,JSON.stringify({schemaVersion:2,sourceDigest:'old-tree'}));
  const incomplete=join(dir,'incomplete.json');
  writeFileSync(incomplete,JSON.stringify({schemaVersion:2,sourceDigest:digest(),scenarios:[],lifecycles:[]}));
  for (const path of [file,incomplete,join(dir,'missing.json')]) for (const metric of ['jobs-per-run','runs-per-change']) {
    const run=spawnSync(process.execPath,[resolve(root,'.github/macos-budget.mjs'),'--metric',metric,'--telemetry',path],{encoding:'utf8'});
    assert.equal(run.status,1); assert.match(run.stderr,/stale telemetry|incomplete|ENOENT/);
  }
});


test('budget check wrapper exposes real SDK measurement diagnostics on stderr', t => {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'macos-budget-errors-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  cpSync(resolve(root, '.github'), join(dir, '.github'), { recursive: true, filter: path => !['node_modules', '.telemetry'].includes(basename(path)) });
  symlinkSync(resolve(root, '.github/node_modules'), join(dir, '.github/node_modules'), 'junction');
  const run = spawnSync(process.execPath, [join(dir, '.github/check-budgets.mjs')], { cwd: dir, encoding: 'utf8' });
  assert.equal(run.status, 1);
  assert.equal(run.stdout, '');
  for (const id of ['crozier-macos-jobs-per-run', 'crozier-macos-runs-per-change']) assert.ok(run.stderr.includes(id), id);
  assert.match(run.stderr, /ENOENT/);
});
