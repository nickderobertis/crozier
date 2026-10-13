import assert from 'node:assert/strict';
import { test } from 'node:test';
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { root, workflows, triggered, resolveRun, matrixRows, digest } from '../workflow-graph.mjs';
import { history, event } from './support.mjs';

import { classes, recordingDigest } from '../scenarios.mjs';

test('actual workflow/call graph resolves event fan-out and records authoritative workload telemetry', t => {
  const h = history(t), graph = workflows(), scenarios = [];
  for (const [id,eventName,action] of classes) for (const diff of ['source','version','dependency']) for (const fork of [false,true]) for (const crates of ['false','true']) for (const pypi of ['false','true']) {
    const pr = event(id === 'release-merge' ? 'release-plz-test' : 'feature/change', fork);
    pr.action = action; pr.release = { prerelease: false }; pr.head_commit = { message: id === 'release-merge' ? 'chore: release' : 'feat: change' };
    const s = { id: `${id}/${diff}/${fork ? 'fork' : 'same'}/crates=${crates}/pypi=${pypi}`, class: id, diff, fork, eventName, event: pr, branch: id === 'tag-push' ? 'v0.0.2' : 'main', tag: id === 'release-published' || id === 'tag-push' ? 'v0.0.2' : undefined, inputs: { 'macos-diagnostic': id === 'manual-opt-in' }, publish: { crates,pypi } };
    const decision = h.classify(pr, h.heads[diff], eventName);
    const runs = graph.filter(w => triggered(w.value,s)).map(w => ({ workflow: w.path, rows: resolveRun(w,s,decision) }));
    for (const run of runs) {
      const mac = run.rows.filter(r => r.macos);
      const expected = wMac(run.workflow, s, decision);
      assert.deepEqual(mac.map(r => r.job), expected, s.id + ' ' + run.workflow);
      if (run.workflow.endsWith('/ci.yml') && eventName === 'pull_request') {
        for (const name of ['commitlint','gate','llmlint']) assert.equal(run.rows.find(r => r.job === name)?.result, 'success', name);
        for (const id of ['check','sdk-env','install']) assert.deepEqual(run.rows.filter(r => r.job === id).map(r => r.runner), ['ubuntu-latest','windows-latest']);
      }
    }
    scenarios.push({ ...s, decision, runs });
  }
  // The automatic release PR is a separate version-only route, under the same
  // PAT identity as people. Unknown input must still demand the Mac proof.
  const release = event('release-plz-2026-10-12');
  for (const pr of [release,event('release-plz-forged',true),{action:'synchronize'},event('release-plz-mixed')]) {
    const head = pr.pull_request?.head.ref === 'release-plz-mixed' ? h.heads.source : h.heads.version;
    const decision = h.classify(pr,head);
    const s = { id: `classification/${pr.pull_request?.head.ref ?? 'unknown'}`, eventName:'pull_request',event:pr,branch:'main',inputs:{} };
    const runs = graph.filter(w => triggered(w.value,s)).map(w => ({workflow:w.path, rows:resolveRun(w,s,decision)}));
    for (const run of runs.filter(r=>r.workflow.endsWith('/ci.yml'))) {
      assert.deepEqual(run.rows.filter(r=>r.macos).map(r=>r.job), decision.macosRequired ? ['macos'] : []);
      for (const name of ['commitlint','gate','llmlint']) assert.equal(run.rows.find(r=>r.job===name)?.result,'success');
    }
    scenarios.push({...s,decision,runs});
  }
  const lifecycleClasses = ['pr-synchronize','base-push','release-merge','tag-push','release-published','downstream','repository-dispatch','schedule'];
  const lifecycles = [];
  for (const fork of [false,true]) for (const diff of ['source','version','dependency']) for (const crates of ['false','true']) for (const pypi of ['false','true']) {
    const selected = scenarios.filter(s => lifecycleClasses.includes(s.class) && s.diff === diff && s.fork === fork && s.publish.crates === crates && s.publish.pypi === pypi);
    const releasePR = scenarios.find(s => s.id === 'classification/release-plz-2026-10-12');
    const runs = [...selected,releasePR].flatMap(s => s.runs.filter(r => r.rows.some(row=>row.macos)).map(r => ({event:s.id,workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)})));
    lifecycles.push({fork,diff,crates,pypi,runs});
  }
  const telemetry = {schemaVersion:2,sourceDigest:digest(),scenarios,lifecycles};
  telemetry.recordingDigest=recordingDigest(telemetry);
  mkdirSync(resolve(root,'.github/.telemetry'),{recursive:true});
  writeFileSync(resolve(root,'.github/.telemetry/macos-policy.json'),JSON.stringify(telemetry,null,2)+'\n');
});
function wMac(path,s,decision) {
  if (path.endsWith('/ci.yml')) return decision.macosRequired || s.class === 'manual-opt-in' ? ['macos'] : [];
  if (path.endsWith('/release.yml')) return ['darwin'];
  return [];
}

test('unknown runners, calls, matrices and cycles fail loudly; real matrix include/exclude expands', () => {
  assert.deepEqual(matrixRows({os:['linux','mac'],exclude:[{os:'linux'}],include:[{os:'windows',target:'win'}]}),[{os:'mac'},{os:'windows',target:'win'}]);
  assert.deepEqual(matrixRows({include:[{target:'intel',os:'macos-latest'},{target:'arm',os:'macos-latest'}]}),[{target:'intel',os:'macos-latest'},{target:'arm',os:'macos-latest'}]);
  const scenario={id:'bad',eventName:'push',event:{},branch:'main'};
  for (const jobs of [ {bad:{'runs-on':'${{ needs.unknown.outputs.runner }}'}}, {bad:{uses:'org/repo/.github/workflows/no.yml@v1'}}, {bad:{'runs-on':'ubuntu-latest',strategy:{matrix:{os:'${{ fromJSON(needs.no.outputs.matrix) }}'}}}}, {bad:{needs:'bad','runs-on':'ubuntu-latest'}} ]) {
    assert.throws(()=>resolveRun({path:'bad.yml',value:{jobs}},scenario,{macosRequired:false}), /unresolved|context|Unexpected|JSON|Cannot|cyclic/i);
  }
});
