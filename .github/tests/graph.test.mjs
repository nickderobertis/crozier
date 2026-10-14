import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parse, stringify } from 'yaml';
import { spawnSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { pathToFileURL } from 'node:url';
import { mkdirSync, writeFileSync, mkdtempSync, rmSync, readFileSync, cpSync, symlinkSync } from 'node:fs';
import { resolve, join, basename } from 'node:path';
import { root, workflows, triggered, resolveRun, matrixRows, digest, expression } from '../workflow-graph.mjs';
import { history, event, githubApi, liftEvent } from './support.mjs';
import { macJobName } from '../macos-policy.mjs';

import { classes, recordingDigest, validateTelemetry, lifecycleScenarios, liftRoutes } from '../scenarios.mjs';
let recorded;

// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and classifier/producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('actual workflow/call graph resolves event fan-out and records authoritative workload telemetry', async t => {
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
  // Every lift route of the ordinary PR, classified against a doubled GitHub API.
  // None requests a Mac runner; only the proven route can satisfy the Mac check.
  const sha = h.heads.source, earlier = { id: 1, path: '.github/workflows/ci.yml', head_sha: sha, html_url: 'https://github.com/nickderobertis/crozier/actions/runs/1' };
  const macJob = conclusion => ({ name: macJobName, conclusion, head_sha: sha, labels: ['macos-latest'] });
  const routes = {
    proven: { runs: [{ ...earlier, status: 'completed' }], jobs: { 1: [macJob('success')] } },
    'in-progress': { runs: [{ ...earlier, status: 'in_progress' }], jobs: { 1: [macJob(null)] } },
    cancelled: { runs: [{ ...earlier, status: 'completed' }], jobs: { 1: [macJob('cancelled')] } },
    failed: { runs: [{ ...earlier, status: 'completed' }], jobs: { 1: [macJob('failure')] } },
    absent: { runs: [], jobs: {} },
    'api-unavailable': { status: 503 },
  };
  assert.deepEqual(Object.keys(routes), liftRoutes);
  for (const [route, state] of Object.entries(routes)) {
    const api = await githubApi(t, state);
    const pr = liftEvent(sha), decision = await h.lift(pr, sha, { GITHUB_API_URL: api.url });
    const s = { id: `lift/${route}`, eventName: 'pull_request', event: pr, branch: 'main', inputs: {} };
    const runs = graph.filter(w => triggered(w.value, s)).map(w => ({ workflow: w.path, rows: resolveRun(w, s, decision) }));
    const ci = runs.find(r => r.workflow.endsWith('/ci.yml'));
    assert.deepEqual(runs.flatMap(r => r.rows.filter(row => row.macos)), [], route);
    assert.deepEqual(ci.rows.filter(r => r.job === 'macos').map(r => r.runner), ['ubuntu-latest'], route);
    assert.equal(decision.macosRequired, false, route);
    if (route === 'proven') assert.equal(decision.reusedRun, earlier.html_url);
    else assert.match(decision.liftRefusal, /draft lift has no Mac proof/, route);
    for (const name of ['commitlint', 'gate', 'llmlint']) assert.equal(ci.rows.find(r => r.job === name)?.result, 'success', name);
    scenarios.push({ ...s, decision, runs });
  }
  const lifecycles = [];
  for (const fork of [false,true]) for (const diff of ['source','version','dependency']) for (const crates of ['false','true']) for (const pypi of ['false','true']) for (const lift of ['none',...liftRoutes]) {
    const runs = lifecycleScenarios(scenarios,{fork,diff,crates,pypi,lift}).flatMap(s => s.runs.filter(r => r.rows.some(row=>row.macos)).map(r => ({event:s.id,workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)})));
    lifecycles.push({fork,diff,crates,pypi,lift,runs});
  }
  const telemetry = {schemaVersion:4,sourceDigest:digest(),scenarios,lifecycles};
  telemetry.recordingDigest=recordingDigest(telemetry);
  recorded=telemetry;
  mkdirSync(resolve(root,'.github/.telemetry'),{recursive:true});
  writeFileSync(resolve(root,'.github/.telemetry/macos-policy.json'),JSON.stringify(telemetry,null,2)+'\n');
});
// llmlint: ignore-end[shell_test_tiers_stay_split]
test('a draft lift reports every required context, never requests Mac and never cancels the draft run', () => {
  const graph = workflows(), ci = graph.find(w => w.path.endsWith('/ci.yml'));
  const url = 'https://github.com/nickderobertis/crozier/actions/runs/1';
  for (const [branch, fork, decision, runner] of [
    ['feature/change', false, { macosRequired: false, reusedRun: url }, 'ubuntu-latest'],
    ['feature/change', false, { macosRequired: false, liftRefusal: 'draft lift has no Mac proof on head x: absent' }, 'ubuntu-latest'],
    ['release-plz-test', false, { macosRequired: false }, undefined],
    ['release-plz-test', true, { macosRequired: false, liftRefusal: 'draft lift has no Mac proof on head x: absent' }, 'ubuntu-latest'],
  ]) {
    const pr = event(branch, fork);
    pr.action = 'ready_for_review';
    const scenario = { id: 'draft-lift', eventName: 'pull_request', event: pr, branch: 'main', inputs: {} };
    assert.equal(triggered(ci.value, scenario), true, 'the lift supplies the post-draft verdict');
    const rows = resolveRun(ci, scenario, decision);
    assert.deepEqual(rows.filter(row => row.job === 'macos' && row.result === 'success').map(row => row.runner), runner ? [runner] : []);
    assert.equal(rows.filter(row => row.macos).length, 0);
    for (const name of ['commitlint', 'gate', 'llmlint']) assert.equal(rows.find(row => row.job === name)?.result, 'success', name);
  }
  // The lift waits behind the draft's run; every other event still cancels its predecessor.
  const cancel = action => expression(ci.value.concurrency['cancel-in-progress'], { github: { event: { action } } }).coerceString();
  assert.equal(cancel('ready_for_review'), 'false');
  for (const action of ['opened', 'synchronize', 'reopened', undefined]) assert.equal(cancel(action), 'true', action);
  // The classifier matches the API's job name; a renamed job must fail here, not silently stop reusing.
  assert.equal(ci.value.jobs.macos.name, macJobName);
  const steps = ci.value.jobs.macos.steps;
  assert.equal(steps[0].if, "env.MAC_REUSED_RUN != ''");
  assert.equal(steps[1].if, "env.MAC_LIFT_REFUSAL != ''");
  assert.match(steps[1].run, /exit 1/);
  for (const step of steps.slice(0, 2)) assert.doesNotMatch(step.run, /just|cargo|crozier --version/);
  for (const step of steps.slice(2)) assert.equal(step.if, "env.MAC_REUSED_RUN == '' && env.MAC_LIFT_REFUSAL == ''", step.name ?? step.uses);
  for (const bad of [{ macosRequired: true, reusedRun: url }, { macosRequired: false, reusedRun: url, liftRefusal: 'x' }, { macosRequired: true, liftRefusal: 'x' }]) {
    assert.throws(() => resolveRun(ci, { id: 'bad', eventName: 'pull_request', event: event(), branch: 'main', inputs: {} }, bad), /reuse decision/);
  }
});

function wMac(path,s,decision) {
  if (path.endsWith('/ci.yml')) return decision.macosRequired || s.class === 'manual-opt-in' ? ['macos'] : [];
  if (path.endsWith('/release.yml')) return ['darwin'];
  return [];
}

test('unknown runners, calls, matrices and cycles fail loudly; real matrix include/exclude expands', () => {
  assert.deepEqual(matrixRows({os:['linux','mac'],exclude:[{os:'linux'}],include:[{os:'windows',target:'win'}]}),[{os:'mac'},{os:'windows',target:'win'}]);
  assert.deepEqual(matrixRows({include:[{target:'intel',os:'macos-latest'},{target:'arm',os:'macos-latest'}]}),[{target:'intel',os:'macos-latest'},{target:'arm',os:'macos-latest'}]);
  assert.deepEqual(matrixRows({os:['ubuntu-latest','macos-latest'],include:[{os:'macos-latest',target:'arm'}]}),[{os:'ubuntu-latest'},{os:'macos-latest',target:'arm'}]);
  for (const matrix of [{include:'bad'}, {exclude:'bad'}, {include:[null]}, {include:[1]}, {include:['bad']}, {include:[[]]}, {exclude:[false]}, {exclude:[[]]}, {include:[]}]) {
    assert.throws(()=>matrixRows(matrix), /unresolved matrix (include|exclude)/);
  }
  const scenario={id:'bad',eventName:'push',event:{},branch:'main'};
  for (const jobs of [ {bad:{'runs-on':[]}}, {bad:{'runs-on':'${{ needs.unknown.outputs.runner }}'}}, {bad:{uses:'org/repo/.github/workflows/no.yml@v1'}}, {bad:{'runs-on':'ubuntu-latest',strategy:{matrix:{os:'${{ fromJSON(needs.no.outputs.matrix) }}'}}}}, {bad:{needs:'bad','runs-on':'ubuntu-latest'}} ]) {
    assert.throws(()=>resolveRun({path:'bad.yml',value:{jobs}},scenario,{macosRequired:false}), /unresolved|context|Unexpected|JSON|Cannot|cyclic/i);
  }
});


test('shorthand triggers route declared events and unsupported glob filters fail explicitly', () => {
  const scenario = { eventName: 'push', event: {}, branch: 'main', tag: 'v0.0.2' };
  assert.equal(triggered({ on: 'push' }, scenario), true);
  assert.equal(triggered({ on: 'pull_request' }, scenario), false);
  assert.equal(triggered({ on: ['push', 'pull_request'] }, scenario), true);
  assert.equal(triggered({ on: ['release'] }, scenario), false);
  const pr = { ...scenario, eventName:'pull_request', event:{action:'opened'} };
  for (const types of ['reopened', [null], [7], [], {}]) assert.throws(()=>triggered({on:{pull_request:{types}}},pr), /unresolved workflow trigger types/);
  assert.equal(triggered({on:{pull_request:{types:['opened']}}},pr),true);
  assert.equal(triggered({on:{pull_request:{types:['reopened']}}},pr),false);
  assert.equal(triggered({on:{pull_request:null}},pr),true);
  assert.equal(triggered({on:{pull_request:null}},{...pr,event:{action:'ready_for_review'}}),false);
  for (const filter of ['branches', 'tags']) {
    for (const pattern of ['v*', '**', '!main', 'v[0-9]', 'release?', 'v+']) {
      assert.throws(() => triggered({ on: { push: { [filter]: [pattern] } } }, scenario), /unresolved workflow trigger filter/);
    }
    assert.equal(triggered({ on: { push: { [filter]: [filter === 'branches' ? 'main' : 'v0.0.2'] } } }, scenario), true);
    assert.equal(triggered({ on: { push: { [filter]: ['other'] } } }, scenario), false);
  }
});

test('the real telemetry reader reports both actual graph metrics and event/architecture detail through the SDK', t=>{
  const dir=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'macos-report-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  for(const metric of ['jobs-per-run','runs-per-change']) {
    const resultFile=join(dir,`${metric}.json`);
    const run=spawnSync(process.execPath,[resolve(root,'.github/macos-budget.mjs'),'--metric',metric,'--telemetry',resolve(root,'.github/.telemetry/macos-policy.json')],{encoding:'utf8',env:{...process.env,ONEBUDGETSPEC_RESULT:resultFile}});
    assert.equal(run.status,0,run.stderr);
    const report=JSON.parse(readFileSync(resultFile,'utf8'));
    const values=metric==='jobs-per-run'?recorded.scenarios.flatMap(s=>s.runs.map(r=>r.rows.filter(row=>row.macos).length)):recorded.lifecycles.map(l=>l.runs.length);
    assert.equal(report.value,Math.max(...values));
    const detail=JSON.parse(report.detail); assert.equal(detail.sourceDigest,recorded.sourceDigest); assert.equal(detail.metric,metric);
    assert.deepEqual(detail.scenarios.map(s=>s.event),recorded.scenarios.map(s=>s.id)); assert.deepEqual(detail.lifecycles,recorded.lifecycles);
    const darwinTargets=detail.scenarios.flatMap(s=>s.runs.flatMap(r=>r.jobs.flatMap(j=>j.targets ?? []))).filter(target=>target.endsWith('apple-darwin'));
    assert.ok(darwinTargets.length); assert.deepEqual([...new Set(darwinTargets)],['aarch64-apple-darwin']);
  }
});

test('recorded workload integrity rejects truncation, bad rows/runners and lifecycle inconsistencies', ()=>{
  const corrupt=structuredClone(recorded); corrupt.scenarios.pop();
  assert.throws(()=>validateTelemetry(corrupt,recorded.sourceDigest),/corrupted/);
  for(const change of [
    t=>t.scenarios.find(s=>s.runs.length).runs.pop(),
    t=>{for(const s of t.scenarios)s.runs=[]; for(const l of t.lifecycles)l.runs=[];},
    t=>t.scenarios.pop(), t=>t.lifecycles.pop(), t=>t.scenarios[0].class='manual-default', t=>t.scenarios[0].publish.crates='unknown',
    t=>t.scenarios.find(s=>s.runs.length).runs[0].rows.splice(0),
    t=>t.scenarios.find(s=>s.runs.length).runs[0].rows[0].job=null,
    t=>t.scenarios.find(s=>s.runs.some(r=>r.rows.some(row=>row.runner))).runs.find(r=>r.rows.some(row=>row.runner)).rows.find(row=>row.runner).runner='unresolved-runner',
    t=>t.lifecycles[0].runs.splice(0),
    t=>{t.scenarios.find(s=>s.id==='lift/failed').decision.macosRequired=true;},
    t=>{delete t.scenarios.find(s=>s.id==='lift/absent').decision.liftRefusal;},
    t=>{t.lifecycles=t.lifecycles.filter(l=>l.lift!=='in-progress');},
  ]) {
    const bad=structuredClone(recorded); change(bad); bad.recordingDigest=recordingDigest(bad);
    assert.throws(()=>validateTelemetry(bad,recorded.sourceDigest),/incomplete|invalid|inconsistent/);
  }
});


// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and classifier/producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('actual local reusable workflows resolve Mac jobs and missing calls/capture configurations fail', async t=>{
  const dir=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'macos-capture-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  cpSync(resolve(root,'.github'),join(dir,'.github'),{recursive:true,filter:path=>!['node_modules','.telemetry'].includes(basename(path))});
  symlinkSync(resolve(root,'.github/node_modules'),join(dir,'.github/node_modules'),'junction');
  writeFileSync(join(dir,'screencomp.toml'),'[capture]\narches = ["unsupported"]\n');
  const graph=await import(pathToFileURL(join(dir,'.github/workflow-graph.mjs')).href);
  const visual=graph.workflows().find(w=>w.path.endsWith('/visual-docs.yml'));
  assert.throws(()=>graph.resolveRun(visual,{id:'unsupported-capture',eventName:'pull_request',event:event(),branch:'main'},{macosRequired:true}),/unresolved capture architectures/);
  writeFileSync(join(dir,'.github/workflows/local-proof.yml'), 'on:\n  workflow_call:\n    inputs:\n      runner:\n        type: string\n        required: true\n      enabled:\n        type: boolean\n        default: true\n      attempts:\n        type: number\n        default: 1\njobs:\n  native:\n    if: inputs.enabled\n    runs-on: ${{ inputs.runner }}\n    steps:\n      - run: echo proof\n');
  writeFileSync(join(dir,'.github/workflows/local-caller.yml'), 'on: workflow_dispatch\njobs:\n  proof:\n    uses: ./.github/workflows/local-proof.yml\n    with:\n      runner: macos-latest\n');
  const caller = graph.workflows().find(w=>w.path.endsWith('/local-caller.yml'));
  const scenario = { id:'local-call',eventName:'workflow_dispatch',event:{},branch:'main',inputs:{} };
  assert.equal(graph.triggered(caller.value,scenario),true);
  const rows = graph.resolveRun(caller,scenario,{macosRequired:false});
  assert.equal(rows.length,1);
  assert.equal(rows[0].workflow,'.github/workflows/local-proof.yml');
  assert.equal(rows[0].runner,'macos-latest');
  assert.equal(rows[0].macos,true);
  for (const inputs of [{runner:'macos-latest',enabled:'false'}, {}, {runner:'macos-latest',extra:true}, {runner:'macos-latest',attempts:'1'}, {runner:null}]) {
    caller.value.jobs.proof.with=inputs;
    assert.throws(()=>graph.resolveRun(caller,scenario,{macosRequired:false}),/unresolved reusable input/);
  }
  caller.value.jobs.proof.with={runner:'macos-latest',enabled:false,attempts:2};
  const disabled=graph.resolveRun(caller,scenario,{macosRequired:false});
  assert.equal(disabled[0].result,'skipped');
  assert.equal(disabled[0].macos,false);
  caller.value.jobs.proof.with={runner:'macos-latest',enabled:true,attempts:2};
  assert.equal(graph.resolveRun(caller,scenario,{macosRequired:false})[0].macos,true);
  const childPath=join(dir,'.github/workflows/local-proof.yml'), child=readFileSync(childPath,'utf8');
  for (const key of ['__proto__','constructor']) {
    writeFileSync(childPath,child.replace('    inputs:\n',`    inputs:\n      ${key}:\n        type: boolean\n        default: true\n`));
    assert.throws(()=>graph.resolveRun(caller,scenario,{macosRequired:false}),new RegExp(`unresolved reusable input: unsupported evaluator key ${key}`));
  }
  writeFileSync(childPath,child);
  caller.value.jobs.proof.uses='./.github/workflows/missing.yml';
  assert.throws(()=>graph.resolveRun(caller,scenario,{macosRequired:false}),/ENOENT/);

});
// llmlint: ignore-end[shell_test_tiers_stay_split]


// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and classifier/producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('producer wiring changes refuse measurement instead of silently using assumed outputs', ()=>{
  const graph=workflows(), ci=graph.find(w=>w.path.endsWith('/ci.yml')), release=graph.find(w=>w.path.endsWith('/release.yml'));
  const scenario={id:'producer-drift',eventName:'pull_request',event:event(),branch:'main',publish:{crates:'true',pypi:'false'}};
  for(const change of [w=>delete w.value.jobs['macos-policy'].outputs.macosRequired,w=>delete w.value.jobs['macos-policy'].outputs.macosReusedRun,w=>delete w.value.jobs['macos-policy'].outputs.macosLiftRefusal,w=>delete w.value.jobs['macos-policy'].permissions,w=>delete w.value.jobs['macos-policy'].steps.find(s=>s.id==='policy').env.GITHUB_TOKEN,w=>w.value.jobs['macos-policy'].steps.find(s=>s.id==='policy').env.PR_HEAD='HEAD']) {
    const changed=structuredClone(ci); change(changed); assert.throws(()=>resolveRun(changed,scenario,{macosRequired:true}),/producer wiring/);
  }
  for(const change of [w=>delete w.value.jobs.guard.outputs.crates,w=>w.value.jobs.guard.steps.find(s=>s.id==='check').run='echo crates=false >> "$GITHUB_OUTPUT"; echo pypi=false >> "$GITHUB_OUTPUT"']) {
    const changed=structuredClone(release); change(changed); assert.throws(()=>resolveRun(changed,{...scenario,eventName:'release'},{macosRequired:false}),/producer wiring|token routing/);
  }
  const visual=structuredClone(graph.find(w=>w.path.endsWith('/visual-docs.yml'))); visual.value.jobs['visual-docs'].with.arches='["arm64"]';
  const rows=resolveRun(visual,scenario,{macosRequired:true}); assert.ok(rows.some(r=>r.job==='capture' && r.runner==='ubuntu-24.04-arm'));
  visual.value.jobs['visual-docs'].with.arches='["unsupported"]'; assert.throws(()=>resolveRun(visual,scenario,{macosRequired:true}),/unresolved capture architectures/);
});
// llmlint: ignore-end[shell_test_tiers_stay_split]


test('budget CLI distinguishes invalid invocation from telemetry IO failure', () => {
  const command = resolve(root, '.github/macos-budget.mjs');
  const invalid = spawnSync(process.execPath, [command], { encoding: 'utf8' });
  assert.equal(invalid.status, 2);
  assert.match(invalid.stderr, /usage:/);
  const missing = spawnSync(process.execPath, [command, '--metric', 'jobs-per-run', '--telemetry', resolve(root, '.github/.telemetry/absent.json')], { encoding: 'utf8' });
  assert.equal(missing.status, 1);
  assert.match(missing.stderr, /ENOENT/);
});


test('the budget wrapper accepts actual telemetry and rejects each exceeded limit through the SDK', t => {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'macos-budget-verdicts-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  cpSync(resolve(root, '.github'), join(dir, '.github'), { recursive: true, filter: path => !['node_modules', '.telemetry'].includes(basename(path)) });
  symlinkSync(resolve(root, '.github/node_modules'), join(dir, '.github/node_modules'), 'junction');
  for (const path of ['screencomp.toml', 'release-plz.toml']) cpSync(resolve(root, path), join(dir, path));
  mkdirSync(join(dir, '.github/.telemetry'));
  writeFileSync(join(dir, '.github/.telemetry/macos-policy.json'), JSON.stringify(recorded));
  const specification = join(dir, '.github/budgets.yaml'), original = readFileSync(specification, 'utf8');
  const invoke = () => spawnSync(process.execPath, [join(dir, '.github/check-budgets.mjs')], { cwd: dir, encoding: 'utf8' });
  const accepted = invoke();
  assert.equal(accepted.status, 0, accepted.stderr);
  assert.equal(accepted.stderr, '');
  const budgets = parse(original).budgets;
  for (const budget of budgets) assert.ok(accepted.stdout.includes(`${budget.id}: within`));
  for (const budget of budgets) {
    const lowered = parse(original);
    // Induce rejection in an isolated copy; the SDK alone compares measurements.
    lowered.budgets.find(entry => entry.id === budget.id).threshold = 0;
    writeFileSync(specification, stringify(lowered));
    const rejected = invoke();
    assert.equal(rejected.status, 1, rejected.stderr);
    assert.ok(rejected.stdout.includes(`${budget.id}: over`), rejected.stdout);
    assert.equal(rejected.stderr, '');
  }
});
