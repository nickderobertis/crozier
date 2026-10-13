import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { writeFileSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { test } from 'node:test';
import { root } from '../workflow-graph.mjs';

test('measurement refuses missing or stale telemetry instead of rerunning scenarios', t => {
  const dir=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'macos-telemetry-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  const file=join(dir,'stale.json');
  writeFileSync(file,JSON.stringify({schemaVersion:1,sourceDigest:'old-tree'}));
  for (const path of [file,join(dir,'missing.json')]) for (const metric of ['jobs-per-run','runs-per-change']) {
    const run=spawnSync(process.execPath,[resolve(root,'.github/macos-budget.mjs'),'--metric',metric,'--telemetry',path],{encoding:'utf8'});
    assert.equal(run.status,1); assert.match(run.stderr,/stale telemetry|ENOENT/);
  }
});
