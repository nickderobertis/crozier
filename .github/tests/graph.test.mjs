import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parse, stringify } from 'yaml';
import { spawnSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { pathToFileURL } from 'node:url';
import { mkdirSync, writeFileSync, mkdtempSync, rmSync, readFileSync, cpSync, symlinkSync } from 'node:fs';
import { resolve, join, basename } from 'node:path';
import { root, workflows, triggered, resolveRun, matrixRows, digest } from '../workflow-graph.mjs';
import { event } from './support.mjs';

import { classes, recordingDigest, validateTelemetry, lifecycleScenarios } from '../scenarios.mjs';
let recorded;

// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and classifier/producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('actual workflow/call graph resolves event fan-out and records authoritative workload telemetry', async t => {
  const graph = workflows(), scenarios = [];
  for (const [id,eventName,action] of classes) for (const diff of ['source','version','dependency']) for (const fork of [false,true]) for (const crates of ['false','true']) for (const pypi of ['false','true']) {
    const pr = event(id === 'release-merge' ? 'release-plz-test' : 'feature/change', fork);
    pr.action = action; pr.release = { prerelease: false }; pr.head_commit = { message: id === 'release-merge' ? 'chore: release' : 'feat: change' };
    const s = { id: `${id}/${diff}/${fork ? 'fork' : 'same'}/crates=${crates}/pypi=${pypi}`, class: id, diff, fork, eventName, event: pr, branch: id === 'tag-push' ? 'v0.0.2' : 'main', tag: id === 'release-published' || id === 'tag-push' ? 'v0.0.2' : undefined, inputs: { 'macos-diagnostic': id === 'manual-opt-in' }, publish: { crates,pypi } };
    const runs = graph.filter(w => triggered(w.value,s)).map(w => ({ workflow: w.path, rows: resolveRun(w,s) }));
    for (const run of runs) {
      const mac = run.rows.filter(r => r.macos);
      const expected = wMac(run.workflow, s);
      assert.deepEqual(mac.map(r => r.job), expected, s.id + ' ' + run.workflow);
      if (run.workflow.endsWith('/ci.yml') && eventName === 'pull_request') {
        for (const name of ['lint','commitlint','gate','llmlint']) assert.equal(run.rows.find(r => r.job === name)?.result, 'success', name);
        assert.deepEqual(run.rows.filter(r => r.job.startsWith('test-')).map(r => [r.job, r.runner]), [['test-linux','ubuntu-latest'],['test-windows','windows-latest'],['test-macos','macos-latest']]);
      }
    }
    scenarios.push({ ...s, runs });
  }
  // The automatic release PR skips its test lanes by the job's own condition on ownership
  // and branch; lint's guard step then holds the content (journeys in ci-journeys).
  const release = event('release-plz-2026-10-12');
  for (const pr of [release,event('release-plz-forged',true),{action:'synchronize'},event('release-plz-mixed')]) {
    const s = { id: `classification/${pr.pull_request?.head.ref ?? 'unknown'}`, eventName:'pull_request',event:pr,branch:'main',inputs:{} };
    const runs = graph.filter(w => triggered(w.value,s)).map(w => ({workflow:w.path, rows:resolveRun(w,s)}));
    for (const run of runs.filter(r=>r.workflow.endsWith('/ci.yml'))) {
      const sameRepositoryRelease = pr === release || pr.pull_request?.head.ref === 'release-plz-mixed';
      assert.deepEqual(run.rows.filter(r=>r.macos).map(r=>r.job), sameRepositoryRelease ? [] : ['test-macos'], s.id);
      for (const name of ['lint','commitlint','gate','llmlint']) assert.equal(run.rows.find(r=>r.job===name)?.result,'success');
    }
    scenarios.push({...s,runs});
  }
  const lifecycles = [];
  for (const fork of [false,true]) for (const diff of ['source','version','dependency']) for (const crates of ['false','true']) for (const pypi of ['false','true']) {
    const runs = lifecycleScenarios(scenarios,{fork,diff,crates,pypi}).flatMap(s => s.runs.filter(r => r.rows.some(row=>row.macos)).map(r => ({event:s.id,workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)})));
    lifecycles.push({fork,diff,crates,pypi,runs});
  }
  const telemetry = {schemaVersion:8,sourceDigest:digest(),scenarios,lifecycles};
  telemetry.recordingDigest=recordingDigest(telemetry);
  recorded=telemetry;
  mkdirSync(resolve(root,'.github/.telemetry'),{recursive:true});
  writeFileSync(resolve(root,'.github/.telemetry/macos-policy.json'),JSON.stringify(telemetry,null,2)+'\n');
});
// llmlint: ignore-end[shell_test_tiers_stay_split]
// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and classifier/producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('marking a draft ready starts no run; the head\'s opened or synchronize run already reports every required context, Mac included', t => {
  const graph = workflows(), ci = graph.find(w => w.path.endsWith('/ci.yml'));
  for (const action of ['opened', 'synchronize', 'reopened']) {
    const pr = event(); pr.action = action;
    const scenario = { id: `pr-${action}`, eventName: 'pull_request', event: pr, branch: 'main', inputs: {} };
    assert.equal(triggered(ci.value, scenario), true, action);
    const rows = resolveRun(ci, scenario);
    for (const name of ['lint', 'commitlint', 'gate', 'llmlint']) assert.equal(rows.find(row => row.job === name)?.result, 'success', `${action} ${name}`);
    assert.deepEqual(rows.filter(row => row.macos).map(row => [row.job, row.runner]), [['test-macos', 'macos-latest']], action);
  }
  const lift = event(); lift.action = 'ready_for_review';
  const scenario = { id: 'pr-ready-for-review', eventName: 'pull_request', event: lift, branch: 'main', inputs: {} };
  assert.equal(triggered(ci.value, scenario), false, 'ci.yml must not run when a draft is marked ready');
  assert.deepEqual(graph.filter(w => triggered(w.value, scenario)).map(w => w.path), []);
  assert.equal(ci.value.concurrency['cancel-in-progress'], true);
});
// llmlint: ignore-end[shell_test_tiers_stay_split]

function wMac(path,s) {
  if (path.endsWith('/ci.yml')) return s.eventName === 'pull_request' || s.class === 'manual-opt-in' ? ['test-macos'] : [];
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
    assert.throws(()=>resolveRun({path:'bad.yml',value:{jobs}},scenario), /unresolved|context|Unexpected|JSON|Cannot|cyclic/i);
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
  ]) {
    const bad=structuredClone(recorded); change(bad); bad.recordingDigest=recordingDigest(bad);
    assert.throws(()=>validateTelemetry(bad,recorded.sourceDigest),/incomplete|invalid|inconsistent/);
  }
});


// llmlint: ignore-block[shell_test_tiers_stay_split] This host-tool graph journey is part of the task-mandated node --test .github/tests/*.test.mjs workload, whose recorder and producer proofs must remain together inside .github; the manager approved this scoped exception rather than splitting the required recording surface.
test('a local reusable workflow resolves its jobs; a remote one, or a missing one, fails rather than hiding its slots', t=>{
  const dir=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'workflow-calls-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  cpSync(resolve(root,'.github'),join(dir,'.github'),{recursive:true,filter:path=>!['node_modules','.telemetry'].includes(basename(path))});
  writeFileSync(join(dir,'.github/workflows/callee.yml'),stringify({on:{workflow_call:{inputs:{runner:{type:'string',required:true}}}},jobs:{inner:{'runs-on':'${{ inputs.runner }}',steps:[{run:'true'}]}}}));
  symlinkSync(resolve(root,'.github/node_modules'),join(dir,'.github/node_modules'),'junction');
  return import(pathToFileURL(join(dir,'.github/workflow-graph.mjs')).href).then(graph=>{
    const scenario={id:'calls',eventName:'pull_request',event:event(),branch:'main'};
    const call=(uses,withs)=>({path:'caller.yml',value:{jobs:{outer:{uses,with:withs}}}});
    assert.deepEqual(graph.resolveRun(call('./.github/workflows/callee.yml',{runner:'macos-latest'}),scenario).filter(r=>r.macos).map(r=>r.job),['inner']);
    assert.throws(()=>graph.resolveRun(call('nickderobertis/screencomp/.github/workflows/visual-docs-reusable.yml@v0.4.2',{}),scenario),/unresolved reusable workflow/);
    assert.throws(()=>graph.resolveRun(call('./.github/workflows/absent.yml',{}),scenario),/ENOENT/);
    assert.throws(()=>graph.resolveRun(call('./.github/workflows/callee.yml',{}),scenario),/missing required runner/);
    assert.throws(()=>graph.resolveRun(call('./.github/workflows/callee.yml',{runner:'macos-latest',extra:'x'}),scenario),/unknown extra/);
  });
});
test('producer wiring changes refuse measurement instead of silently using assumed outputs', ()=>{
  const release=workflows().find(w=>w.path.endsWith('/release.yml'));
  const scenario={id:'producer-drift',eventName:'release',event:event(),branch:'main',publish:{crates:'true',pypi:'false'}};
  for(const change of [w=>delete w.value.jobs.guard.outputs.crates,w=>w.value.jobs.guard.steps.find(s=>s.id==='check').run='echo crates=false >> "$GITHUB_OUTPUT"; echo pypi=false >> "$GITHUB_OUTPUT"']) {
    const changed=structuredClone(release); change(changed); assert.throws(()=>resolveRun(changed,scenario),/producer wiring|token routing/);
  }
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
  // The weekly Fern goldens budget reads the plan the workflow's real planner makes.
  const env = { ...process.env }; delete env.CROZIER_FERN_WEEKLY_ROOT;
  const planned = spawnSync('python3', [resolve(root, 'tools/fern-goldens/weekly.py'), 'plan', '--telemetry', join(dir, '.github/.telemetry/fern-goldens-plan.json')], { cwd: root, env, encoding: 'utf8' });
  assert.equal(planned.status, 0, planned.stderr);
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

const pushed = () => { const pr = event(); pr.action = 'synchronize'; return { id: 'push', eventName: 'pull_request', event: pr, branch: 'main', inputs: {} }; };
const prRows = (scenario, graph = workflows()) => graph.filter(w => triggered(w.value, scenario)).flatMap(w => resolveRun(w, scenario).map(row => ({ ...row, workflow: w.path })));

test('an ordinary pull request push runs exactly seven jobs: four independent lanes and three transitional ones', () => {
  const rows = prRows(pushed());
  assert.deepEqual(rows.map(r => r.job).sort(), ['commitlint', 'gate', 'lint', 'llmlint', 'test-linux', 'test-macos', 'test-windows']);
  assert.ok(rows.every(r => r.workflow === '.github/workflows/ci.yml' && r.result === 'success'));
  const by = Object.fromEntries(rows.map(r => [r.job, r]));
  assert.deepEqual(rows.filter(r => r.needs.length).map(r => r.job), ['gate'], 'only the transitional gate has a needs edge');
  assert.deepEqual([...by.gate.needs].sort(), ['commitlint', 'lint', 'llmlint', 'test-linux', 'test-macos', 'test-windows']);
  for (const id of ['lint', 'commitlint', 'llmlint', 'gate']) assert.equal(by[id].timeout, 30, id);
  // Manager rulings c-de8af5d0b87584fa7cfb48d4c2b4deed and c-602a8b0c568f2b4c9e7f3104a9e7a581 (Mac):
  // measured transitional ceilings until the re-measure.
  assert.equal(by['test-linux'].timeout, 150); assert.equal(by['test-windows'].timeout, 90); assert.equal(by['test-macos'].timeout, 120);
  const ci = workflows().find(w => w.path.endsWith('/ci.yml')).value;
  for (const id of ['test-linux', 'test-windows', 'test-macos']) assert.equal(ci.jobs[id].strategy, undefined, `${id} is one job, no matrix or shards`);
});

test('no run on push to main comes from CI: only delivery and the workflows that gate nothing', () => {
  const graph = workflows();
  const scenario = { id: 'main', eventName: 'push', event: {}, branch: 'main', inputs: {} };
  assert.deepEqual(graph.filter(w => triggered(w.value, scenario)).map(w => w.path).sort(), ['.github/workflows/ci-caches.yml', '.github/workflows/golden-reach-base.yml', '.github/workflows/release-plz.yml', '.github/workflows/visual-docs-gallery.yml']);
  const base = graph.find(w => w.path.endsWith('/golden-reach-base.yml')).value;
  assert.deepEqual(Object.keys(base.jobs), ['golden-reach-base']);
  assert.equal(Object.keys(base.on).join(), 'push', 'a pull request push never starts the measurement');
});

test('a release branch runs lint, its guard and the transitional checks; a fork or other branch of that name owes every lane', () => {
  const ci = workflows().find(w => w.path.endsWith('/ci.yml'));
  const release = event('release-plz-2026-10-12'); release.action = 'synchronize';
  const rows = resolveRun(ci, { id: 'release', eventName: 'pull_request', event: release, branch: 'main', inputs: {} });
  assert.deepEqual(rows.filter(r => r.result === 'success').map(r => r.job).sort(), ['commitlint', 'gate', 'lint', 'llmlint']);
  assert.deepEqual(rows.filter(r => r.result === 'skipped').map(r => r.job).sort(), ['test-linux', 'test-macos', 'test-windows']);
  const fork = event('release-plz-2026-10-12', true); fork.action = 'synchronize';
  const forked = resolveRun(ci, { id: 'fork', eventName: 'pull_request', event: fork, branch: 'main', inputs: {} });
  assert.deepEqual(forked.filter(r => r.job.startsWith('test-')).map(r => r.result), ['success', 'success', 'success']);
  const guard = ci.value.jobs.lint.steps.find(s => s.id === 'release-guard');
  assert.equal(guard.if, "github.event.pull_request.head.repo.full_name == github.repository && startsWith(github.head_ref, 'release-plz-')");
  assert.equal(ci.value.jobs.lint.outputs.releaseGuard, '${{ steps.release-guard.outputs.releaseGuard }}');
});

test('the final governance declaration names the four lanes, non-strict, and every one is a real job', () => {
  const governance = JSON.parse(readFileSync(resolve(root, '.github/governance.json'), 'utf8'));
  assert.deepEqual(governance, { required_checks: ['lint', 'test-linux', 'test-windows', 'test-macos'], strict: false });
  const jobs = workflows().find(w => w.path.endsWith('/ci.yml')).value.jobs;
  for (const id of governance.required_checks) assert.ok(jobs[id] && !jobs[id].needs && jobs[id].name === undefined, id);
});

test('every former platform proof is a step of the lane that owes it, each project in one step per lane', () => {
  const jobs = workflows().find(w => w.path.endsWith('/ci.yml')).value.jobs;
  const runs = id => jobs[id].steps.filter(s => s.run).map(s => s.run.trim());
  const shared = ['just bootstrap', 'just ci-test --exclude=tag:tier:promoted', 'just ci-test --projects=tag:lane:sdk-env', 'cargo install --path . --locked', 'crozier --version'];
  for (const id of ['test-linux', 'test-windows', 'test-macos']) for (const command of shared) assert.ok(runs(id).includes(command), `${id}: ${command}`);
  for (const command of ['just ci-test --projects=tag:lane:live', 'just ci-test --projects=tag:lane:packaging', 'cargo publish --dry-run --locked', 'just ci-budgets-host']) {
    assert.ok(runs('test-linux').includes(command), command);
    for (const id of ['test-windows', 'test-macos', 'lint']) assert.ok(!runs(id).includes(command), `${id} must not repeat ${command}`);
  }
  const live = jobs['test-linux'].steps.find(s => s.run === 'just ci-test --projects=tag:lane:live');
  assert.equal(live.env.CROZIER_COLD_REGISTRY_HANDOFF, '1'); assert.equal(live.env.CARGO_HOME, '${{ runner.temp }}/cold-cargo-home');
  assert.ok(runs('lint').includes('just ci-lint'));
  for (const id of ['test-linux', 'test-windows', 'test-macos']) assert.ok(!runs(id).includes('just ci-lint'));
  for (const [id, job] of Object.entries(jobs)) for (const step of job.steps) {
    assert.ok(!/\bnx (run|affected)\b|just check\b/.test(step.run ?? ''), `${id}: CI goes through the lane recipes, never a second gate`);
  }
});

test('visual docs are lint steps over the same x86_64 baseline, and only its upkeep has its own events', () => {
  const graph = workflows(), lint = graph.find(w => w.path.endsWith('/ci.yml')).value.jobs.lint;
  const visual = lint.steps.find(s => s.uses?.startsWith('nickderobertis/screencomp/visual-docs@'));
  assert.equal(visual.with.arch, 'x86_64'); assert.equal(visual.with['fail-on-drift'], true); assert.equal(visual.with['verify-second'], 'shots/verify');
  assert.ok(lint.steps.some(s => s.run === './screenshots/capture-visual-docs.sh'));
  assert.match(readFileSync(resolve(root, 'screencomp.toml'), 'utf8'), /^arches = \["x86_64"\]$/m);
  const upkeep = graph.find(w => w.path.endsWith('/visual-docs.yml'));
  assert.deepEqual(Object.keys(upkeep.value.on).sort(), ['pull_request', 'schedule']);
  assert.deepEqual(upkeep.value.on.pull_request.types, ['closed']);
  const closed = event(); closed.action = 'closed'; closed.pull_request.number = 7;
  assert.deepEqual(resolveRun(upkeep, { id: 'closed', eventName: 'pull_request', event: closed, branch: 'main' }).filter(r => r.result === 'success').map(r => r.job), ['cleanup-preview']);
  assert.deepEqual(resolveRun(upkeep, { id: 'monthly', eventName: 'schedule', event: {}, branch: 'main' }).filter(r => r.result === 'success').map(r => r.job), ['prune-history']);
});

test('release.yml keeps its build, install and publish proof with no test sweep', () => {
  const jobs = workflows().find(w => w.path.endsWith('/release.yml')).value.jobs;
  assert.equal(jobs.test, undefined);
  for (const job of Object.values(jobs)) for (const step of job.steps ?? []) assert.ok(!/just (check|ci-)/.test(step.run ?? ''), step.run);
  for (const id of ['darwin', 'upload', 'publish-crate', 'verify-crate', 'build-wheels', 'build-sdist', 'publish-pypi', 'verify-pypi', 'verify-install-script', 'verify-attestation', 'major-tag']) assert.ok(jobs[id], id);
});
