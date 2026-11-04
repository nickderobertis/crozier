import assert from "node:assert/strict";
import { test } from "node:test";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
// The real timing CLI with only its external read processes doubled. Seeds are
// recorded GitHub responses; variants induce cancellation, missing contexts and
// later attempts without changing any calculation in the implementation.
import { calculateHead, CLI_OPTIONS, SCHEMA_VERSION, summarize, validateReport } from '../core.mjs';
import { chmodSync, existsSync, mkdtempSync, readFileSync, readdirSync, rmSync, symlinkSync, unlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';
const timingCLI = fileURLToPath(new URL('../../gate-timing.mjs', import.meta.url));
const timingRecords = JSON.parse(readFileSync(new URL('./fixtures/gate-timing.json', import.meta.url), 'utf8'));

function timingReplay(t) {
  const root = mkdtempSync(join(tmpdir(), 'crozier-timing-replay-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const records = structuredClone(timingRecords);
  const answerFile = join(root, 'answers.json');
  const calls = join(root, 'calls.jsonl');
  writeFileSync(answerFile, JSON.stringify({ records }));
  const stub = `#!/usr/bin/env node
const fs = require('fs');
const a = JSON.parse(fs.readFileSync(process.env.ANSWERS, 'utf8'));
const args = process.argv.slice(2);
fs.appendFileSync(process.env.CALLS, JSON.stringify(args) + '\\n');
fs.appendFileSync(process.env.CALLS+'.timeline', JSON.stringify({args,at:Date.now()}) + '\\n');
let answer;
if(args[0] === 'auth' && args[1] === 'token') { process.stdout.write('replay-token'); process.exit(0); }
if(a.auth && args[0] === 'host' && process.env.GH_TOKEN !== 'replay-token') { console.error('missing bootstrapped token'); process.exit(1); }
if(a.noOnevcs && args[0] === 'host') { console.error('unrecognized subcommand run-jobs'); process.exit(2); }
const path = args.at(-1);
if(args.includes('rate_limit')) {
 const waited = fs.existsSync(process.env.CALLS+'.waited');
 if((a.quota || a.quotaFuture) && !waited) { fs.writeFileSync(process.env.CALLS+'.waited',''); answer={resources:{core:{limit:100,remaining:39,reset:a.quotaFuture ? Math.floor(Date.now()/1000)+1 : 0}}}; }
 else answer={resources:{core:{limit:100,remaining:100,reset:0}}};
} else if(path.endsWith('/protection')) answer=a.protection || {required_status_checks:{contexts:a.contexts || ['gate','llmlint']}};
else if(path.endsWith('/rules/branches/main')) answer=a.rules || [];
else if(path.includes('/actions/runs?')) { const page=Number(new URL('https://api.invalid/'+path).searchParams.get('page')); answer={workflow_runs:a.records.map(r=>r.run).slice(a.paginate ? (page-1)*100 : 0, a.paginate ? page*100 : undefined)}; }
else if(args.includes('run-jobs')) { const record=a.records.find(r=>r.run.id===Number(args[args.indexOf('--run')+1])); answer={jobs:record.jobs.map(j=>({...j,run_id:record.run.id,run_attempt:record.run.run_attempt}))}; }
else if(/\\/attempts\\//.test(path)) { const jobs=a.previous || a.records.find(r=>r.run.id===Number(path.split('/')[5])).jobs; const page=Number(new URL('https://api.invalid/'+path).searchParams.get('page')); const selected=a.paginateJobs ? jobs.slice((page-1)*100,page*100) : jobs; answer={jobs:selected.map(j=>({...j,run_id:Number(path.split('/')[5]),run_attempt:Number(path.split('/')[7])}))}; }
else if(/\\/actions\\/runs\\/\\d+$/.test(path)) answer=a.records.find(r=>r.run.id===Number(path.split('/').at(-1)))?.run;
if(a.missing && path.includes('/actions/runs?')) answer={};
if(a.badQuota && args.includes('rate_limit')) answer={resources:{core:{limit:'100',remaining:39,reset:null}}};
if(a.badProtection && path.endsWith('/protection')) answer={required_status_checks:{contexts:[null]}};
if(a.badRules && path.endsWith('/rules/branches/main')) answer=[{type:'required_status_checks',parameters:{required_status_checks:'bad'}}];
if(a.badRun && path.includes('/actions/runs?')) answer={workflow_runs:[{...a.records[0].run,id:'bad'}]};
if(a.badRunStatus && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,status:42};
if(a.badRunConclusion && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,conclusion:{invalid:true}};
if(a.badName && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,name:7};
if(a.badPath && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,path:null};
if(a.badFresh && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,head_sha:'0'.repeat(40)};
if(a.jobDamage && answer.jobs) { const job=answer.jobs[0]; if(a.jobDamage==='timestamp') job.started_at=123; else if(a.jobDamage==='name') job.name=null; else if(a.jobDamage==='identity') job.run_id+=1; else if(a.jobDamage==='attempt') job.run_attempt+=1; else if(a.jobDamage==='missing') answer={}; else if(a.jobDamage==='status') job.status='unrecognized'; else if(a.jobDamage==='conclusion') job.conclusion='unrecognized'; }
if(a.invalidJson && args[0]==='host') { process.stdout.write('{'); process.exit(0); }
if(a.secondary && args[0]==='host') { console.error('API secondary rate limit refused'); process.exit(1); }
if(a.fail) { console.error('read refused'); process.exit(1); }
if(!answer) { console.error('unexpected external request: '+args.join(' ')); process.exit(1); }
process.stdout.write(JSON.stringify(answer));
`;
  for (const name of ['gh', 'onevcs']) { writeFileSync(join(root, name), stub); chmodSync(join(root, name), 0o755); }
  const run = (extra = [], overrides = {}, window = {}, defaultCache = false) => spawnSync(process.execPath, [timingCLI, 'runs', '--since', window.since ?? '2026-10-31T00:00:00Z', '--until', window.until ?? '2026-11-04T00:00:00Z', ...(defaultCache ? [] : ['--cache-dir', join(root, 'cache')]), ...extra], { encoding: 'utf8', env: { ...process.env, GH_TOKEN: 'replay', PATH: `${root}:${process.env.PATH}`, ANSWERS: answerFile, CALLS: calls, ...overrides } });
  return { root, records, answerFile, calls, run };
}

test('timing CLI reconciles recorded heads, all jobs, real queue, filters and help', { skip: process.platform === 'win32' }, (t) => {
  const replay = timingReplay(t);
  const run = replay.run();
  assert.equal(run.status, 0, run.stderr);
  const report = validateReport(JSON.parse(run.stdout));
  assert.equal(report.runs.length, replay.records.length);
  assert.equal(report.observation.jobs, replay.records.reduce((n, r) => n + r.jobs.length, 0));
  for (const record of replay.records) {
    const actual = report.runs.find((r) => r.run_id === record.run.id);
    assert.deepEqual(actual, calculateHead([record], ['gate', 'llmlint']));
  }
  // Recorded release PR: last required gate completed 20:00:13, creation
  // 17:53:39. Job queue uses its own creation, not workflow creation.
  assert.equal(report.runs[0].gate_seconds, 7594);
  assert.deepEqual(report.runs[0].critical_path,['gate']);
  const seed = replay.records[0];
  const job = seed.jobs.find((j) => j.name === 'llmlint');
  const measured = report.runs[0].jobs.find((j) => j.name === 'llmlint');
  assert.equal(measured.queue_seconds, 2);
  assert.equal(measured.start_offset_seconds, 136);
  assert.equal(measured.run_seconds, 526);
  assert.notEqual(job.created_at, seed.run.created_at);
  assert.deepEqual(report.summary, summarize(report.runs));
  const filtered = replay.run(['--head-contains', replay.records.at(-1).run.head_sha.slice(0, 7)]);
  assert.equal(filtered.status, 0, filtered.stderr);
  assert.equal(JSON.parse(filtered.stdout).runs.length, 1);
  const help = spawnSync(process.execPath, [timingCLI, '--help'], { encoding: 'utf8' });
  assert.equal(help.status, 0);
  for (const token of [...Object.keys(CLI_OPTIONS).map((key) => '--'+key), `schema_version: ${SCHEMA_VERSION}`]) assert.ok(help.stdout.includes(token));
  const md = replay.run(['--format', 'markdown']);
  assert.equal(md.status, 0, md.stderr);
  assert.match(md.stdout, /release-pr/);
});

test('timing CLI refreshes later attempts while reusing completed responses', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run().status, 0);
  const before = readFileSync(r.calls, 'utf8').trim().split('\n');
  const seed = r.records[0];
  const previous = structuredClone(seed.jobs);
  seed.run.run_attempt = 2;
  seed.jobs = seed.jobs.map((j) => ({ ...j, run_attempt: 2, completed_at: '2026-11-03T23:00:00Z' }));
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, previous }));
  const second = r.run();
  assert.equal(second.status, 0, second.stderr);
  const after = readFileSync(r.calls, 'utf8').trim().split('\n').slice(before.length).map(JSON.parse);
  assert.equal(after.filter((a) => a.includes('run-jobs')).length, 1);
  assert.ok(after.some((a) => a.at(-1) === `repos/nickderobertis/crozier/actions/runs/${seed.run.id}`));
  const measured = JSON.parse(second.stdout).runs.find((x) => x.run_id === seed.run.id);
  assert.equal(measured.attempt, 2);
  assert.equal(measured.jobs.length, previous.length * 2);
  assert.equal(measured.gate_seconds, 18381);
});

test('timing CLI excludes cancelled and missing contexts from passing summary and waits for quota', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  r.records[0].jobs.find((j) => j.name === 'gate').conclusion = 'cancelled';
  r.records[1].jobs = r.records[1].jobs.filter((j) => j.name !== 'gate');
  // Main measures every job's completion independently of PR contexts.
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, quota: true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.equal(report.runs[0].gate_seconds, null);
  assert.match(report.runs[0].reason, /cancelled/);
  assert.equal(report.summary.kinds['release-pr'].unsuccessful, 1);
  assert.deepEqual(report.observation.events.map((e) => e.event), ['quota_wait', 'quota_resume']);
  // Induce a missing PR context independently of the main seed.
  r.records.at(-1).jobs = r.records.at(-1).jobs.filter((j) => j.name !== 'gate');
  rmSync(join(r.root, 'cache'), { recursive: true });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const missing = JSON.parse(r.run().stdout).runs.at(-1);
  assert.equal(missing.gate_seconds, null);
  assert.match(missing.reason, /missing/);
});

test('timing CLI rejects invalid invocation and failed or missing reads', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run(['--limit', '0']).status, 2);
  assert.equal(r.run([], {}, {until:'yesterday'}).status, 2);
  for (const variant of ['fail', 'missing']) {
    writeFileSync(r.answerFile, JSON.stringify({ records: r.records, [variant]: true }));
    const run = r.run();
    assert.equal(run.status, 1, run.stderr);
    assert.equal(run.stdout, '');
  }
});


test('timing CLI counts sibling workflows and excludes failed gates', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const pr = r.records.at(-1);
  pr.jobs.find((j) => j.name === 'llmlint').conclusion = 'failure';
  r.records.push({ run: { ...pr.run, id: 999 }, jobs: [{ ...pr.jobs[0], name: 'visual sibling', run_id: 999 }] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  const measured = report.runs.find((head) => head.head_sha === pr.run.head_sha);
  assert.equal(measured.jobs.length, pr.jobs.length + 1);
  assert.equal(measured.conclusion, 'failure');
  assert.equal(typeof measured.gate_seconds, 'number');
  assert.equal(report.summary.kinds.pr.n, 0);
  assert.equal(report.summary.kinds.pr.unsuccessful, 1);
});


test('timing CLI refreshes jobs while an attempt is unfinished', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records[0];
  seed.run.status = 'in_progress';
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  assert.equal(r.run().status, 0);
  const count = readFileSync(r.calls, 'utf8').trim().split('\n').length;
  seed.run.status = 'completed';
  seed.jobs.push({ ...seed.jobs[0], name: 'late matrix job' });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  assert.ok(JSON.parse(run.stdout).runs[0].jobs.some((j) => j.name === 'late matrix job'));
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').slice(count).map(JSON.parse);
  assert.equal(calls.filter((a) => a.includes('run-jobs')).length, 1);
});


test('timing CLI retains workflows cancelled before any job was created', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  r.records.push({ run: { ...r.records.at(-1).run, id: 41395650386, head_sha: 'b'.repeat(40), conclusion: 'cancelled' }, jobs: [] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.at(-1);
  assert.equal(head.gate_seconds, null);
  assert.equal(head.conclusion, 'cancelled');
  assert.match(head.reason, /cancelled workflow/);
  assert.deepEqual(head.jobs, []);
});


test('timing CLI reports main CI completion separately from other workflows', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const main = r.records.find((record) => record.run.event === 'push');
  assert.equal(main.run.name, 'ci');
  assert.equal(main.run.path, '.github/workflows/ci.yml');
  const expected = 4271; // Recorded 17:51:10 creation to 19:02:21 completion.
  r.records.push({ run: { ...main.run, id: 998, name: 'Visual docs', path: '.github/workflows/visual-docs.yml' }, jobs: [{ ...main.jobs[0], name: 'gallery', completed_at: '2026-11-04T00:00:00Z' }] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const measured = JSON.parse(run.stdout).runs.find((head) => head.head_sha === main.run.head_sha);
  assert.equal(measured.gate_seconds, expected);
  assert.equal(measured.jobs.length, main.jobs.length + 1);
});


test('timing CLI uses gh when the onevcs host verb is unavailable', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, noOnevcs: true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  assert.equal(JSON.parse(run.stdout).runs.length, r.records.length);
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').map(JSON.parse);
  assert.ok(calls.some((args) => args.at(-1).includes('/attempts/1/jobs')));
});


test('timing CLI replays recorded crozier attempts even when timestamp order differs', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const records = JSON.parse(readFileSync(new URL('./fixtures/gate-timing-rerun.json', import.meta.url), 'utf8'));
  const context = 'visual-docs / report (x86_64)';
  r.records.push(records[0]);
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, contexts: [context] }));
  const first = r.run();
  assert.equal(first.status, 0, first.stderr);
  assert.equal(JSON.parse(first.stdout).runs.find((h) => h.run_id === 41288057298).gate_seconds, 2669);
  r.records[r.records.length-1] = records[1];
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, previous: records[0].jobs, contexts: [context] }));
  const second = r.run();
  assert.equal(second.status, 0, second.stderr);
  const head = JSON.parse(second.stdout).runs.find((h) => h.run_id === 41288057298);
  assert.equal(head.attempt, 2);
  assert.equal(head.conclusion, 'success');
  // 09:04:05 earliest observed creation to 09:59:36 last context completion,
  // including the failed attempt, even though attempt 2 completed earlier.
  assert.equal(head.gate_seconds, 3331);
  assert.equal(head.jobs.length, 10);
  // A failed-job-only retry leaves successful contexts on the earlier attempt.
  // Replay that partial-answer variant using the same recorded job responses.
  rmSync(join(r.root,'cache'),{recursive:true});
  r.records[r.records.length-1] = { run:records[1].run, jobs:records[1].jobs.filter(j=>j.name===context) };
  writeFileSync(r.answerFile,JSON.stringify({records:r.records,previous:records[0].jobs,contexts:[context,'visual-docs / arches']}));
  const partial=r.run();
  assert.equal(partial.status,0,partial.stderr);
  const carried=JSON.parse(partial.stdout).runs.find(h=>h.run_id===41288057298);
  assert.equal(carried.conclusion,'success');
  assert.equal(carried.gate_seconds,3331);
});


test('timing CLI independently verifies statistics and empty populations', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records.at(-1);
  const spans = [10, 20, 30, 40];
  r.records = spans.map((span, i) => ({ run: { ...seed.run, id: 800+i, head_sha: (i+1).toString(16).repeat(40), created_at: '2026-11-01T00:00:00Z' }, jobs: [{ ...seed.jobs[0], name: 'gate', created_at: '2026-11-01T00:00:00Z', started_at: '2026-11-01T00:00:02Z', completed_at: `2026-11-01T00:00:${span}Z` }] }));
  for (const record of r.records) record.jobs.push({...record.jobs[0],name:'llmlint'});
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, contexts: ['gate','llmlint'] }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.deepEqual(report.summary.kinds.pr, { n:4, median:25, p95:40, max:40, observed:4, unsuccessful:0 });
  assert.deepEqual(report.summary.kinds.main, { n:0, median:null, p95:null, max:null, observed:0, unsuccessful:0 });
  assert.deepEqual(report.summary.jobs.gate.run, { n:4, median:23, p95:38, max:38 });
  assert.deepEqual(report.summary.jobs.gate.queue, { n:4, median:2, p95:2, max:2 });
  for (const head of report.runs) assert.deepEqual(head.critical_path,['gate','llmlint']);
  const md=r.run(['--format','markdown']);
  assert.equal(md.status,0,md.stderr);
  assert.equal(md.stdout.trim(),[
    'Window: 2026-10-31T00:00:00Z — 2026-11-04T00:00:00Z', '',
    '| Kind | Passing n | Median seconds | p95 | Max | Unsuccessful |',
    '|---|---:|---:|---:|---:|---:|',
    '| pr | 4 | 25 | 40 | 40 | 0 |',
    '| release-pr | 0 | unknown | unknown | unknown | 0 |',
    '| main | 0 | unknown | unknown | unknown | 0 |',
  ].join('\n'));
});

test('timing CLI retains unfinished and never-started required jobs', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const gate = r.records.at(-1).jobs.find((j) => j.name === 'gate');
  Object.assign(gate, { status:'queued', conclusion:null, started_at:null, completed_at:null });
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.at(-1);
  assert.equal(head.gate_seconds, null);
  assert.deepEqual(head.critical_path,[]);
  assert.match(head.reason, /incomplete/);
  const job = head.jobs.find((j) => j.name === 'gate');
  assert.equal(job.queue_seconds, null);
  assert.equal(job.run_seconds, null);
  assert.equal(job.start_offset_seconds, 0);
  assert.match(job.start_offset_reason, /never started/);
});

test('timing CLI discovers credentials and unions protection with rulesets', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, auth:true, protection:{ required_status_checks:{ checks:[{context:'gate'}], contexts:['llmlint'] } }, rules:[{type:'required_status_checks',parameters:{required_status_checks:[{context:'gate'},{context:'llmlint'}]}}] }));
  const run = r.run([], { GH_TOKEN:undefined, GITHUB_TOKEN:undefined });
  assert.equal(run.status, 0, run.stderr);
  assert.deepEqual(JSON.parse(run.stdout).required_contexts, ['gate','llmlint']);
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').map(JSON.parse);
  assert.ok(calls.some((args) => args[0] === 'auth' && args[1] === 'token'));
});

test('timing CLI pauses external reads until the observed quota reset', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, quotaFuture:true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  const until = Date.parse(report.observation.events[0].until);
  const timeline = readFileSync(r.calls+'.timeline', 'utf8').trim().split('\n').map(JSON.parse);
  const firstRead = timeline.find((event) => !event.args.includes('rate_limit'));
  assert.ok(firstRead.at >= until, 'no protected read precedes the reset supplied by the quota response');
  assert.deepEqual(report.observation.events.map((e) => e.event), ['quota_wait','quota_resume']);
});

test('timing CLI paginates workflow history, excludes events, and reports capped sampling', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const excluded = Array.from({length:98}, (_,i) => ({ run:{...r.records[0].run,id:99000+i,event:'workflow_dispatch'},jobs:r.records[0].jobs }));
  writeFileSync(r.answerFile, JSON.stringify({ records:[...excluded,...r.records], paginate:true }));
  const run = r.run(['--limit','200']);
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.equal(report.runs.length, r.records.length);
  assert.equal(report.observation.workflow_runs, r.records.length);
  assert.equal(report.observation.complete, true);
  assert.ok(readFileSync(r.calls,'utf8').includes('page=2'));
  const capped = r.run(['--limit','2']);
  assert.equal(capped.status, 0, capped.stderr);
  assert.equal(JSON.parse(capped.stdout).observation.complete, false);
  assert.equal(JSON.parse(capped.stdout).observation.workflow_runs, 2);
});

test('timing CLI fetches uncached historical attempts and every job page', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records[0];
  const previous = structuredClone(seed.jobs);
  while (previous.length < 101) previous.push({...previous[0],name:'historical-'+previous.length});
  seed.run.run_attempt = 2;
  seed.jobs = seed.jobs.map((j) => ({...j,run_attempt:2}));
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, previous, paginateJobs:true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.find((h) => h.run_id === seed.run.id);
  assert.equal(head.jobs.length, 101 + seed.jobs.length);
  const calls = readFileSync(r.calls,'utf8').trim().split('\n').map(JSON.parse);
  assert.equal(calls.filter((a) => a.at(-1).includes('/attempts/1/jobs')).length, 2);
  assert.ok(calls.some((a) => a.at(-1).includes('/attempts/1/jobs?per_page=100&page=2')));
});

test('timing CLI rejects malformed boundary data and mismatched cached identities', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run([], {}, {until:'2026-02-30T00:00:00Z'}).status, 2);
  for (const field of ['badQuota','badProtection','badRules','badRun','badFresh','badName','badPath']) {
    writeFileSync(r.answerFile, JSON.stringify({records:r.records,[field]:true}));
    const run = r.run();
    assert.equal(run.status, 1, field+': '+run.stderr);
    assert.equal(run.stdout, '');
  }
  writeFileSync(r.answerFile, JSON.stringify({records:r.records}));
  assert.equal(r.run().status, 0);
  const file = join(r.root,'cache',`run-${r.records[0].run.id}-attempt-1.json`);
  const cached = JSON.parse(readFileSync(file,'utf8'));
  cached.run.id += 1;
  writeFileSync(file,JSON.stringify(cached));
  const run = r.run();
  assert.equal(run.status,1);
  assert.match(run.stderr,/cached attempt identity mismatch/);
});

test('timing CLI reports inconsistent job timestamps as unknown', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const job = r.records[0].jobs[0];
  job.created_at = '2026-11-03T18:01:00Z';
  job.started_at = '2026-11-03T17:00:00Z';
  job.completed_at = '2026-11-03T16:59:00Z';
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const run = r.run();
  assert.equal(run.status,0,run.stderr);
  const measured = JSON.parse(run.stdout).runs[0].jobs[0];
  assert.equal(measured.queue_seconds,null);
  assert.equal(measured.run_seconds,null);
  assert.equal(measured.start_offset_seconds,0);
  assert.match(measured.start_offset_reason,/inconsistent start timestamp/);
});


test('timing CLI rejects invalid invocation before making external reads', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  for (const args of [['--unknown','x'],['--format','json','--format','markdown'],['--limit'],['--format','csv'],['--head-contains','not-a-sha']]) {
    const run = r.run(args);
    assert.equal(run.status,2,run.stderr);
    assert.equal(run.stdout,'');
  }
  for (const window of [{since:'2026-11-04T00:00:00Z',until:'2026-11-01T00:00:00Z'},{until:'2026-11-03T24:00:00Z'},{since:'2026-02-30T00:00:00Z'}]) assert.equal(r.run([],{},window).status,2);
  assert.equal(existsSync(r.calls),false);
});

test('timing CLI validates job fields, timestamps and run/attempt identities', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  for (const jobDamage of ['timestamp','name','identity','attempt','missing']) {
    writeFileSync(r.answerFile,JSON.stringify({records:r.records,jobDamage}));
    const run=r.run();
    assert.equal(run.status,1,jobDamage+': '+run.stderr);
    assert.equal(run.stdout,'');
    assert.match(run.stderr,/invalid job|job identity mismatch|missing or mismatched jobs/);
  }
});

test('timing CLI stops on secondary limits and reports empty history and damaged caches', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile,JSON.stringify({records:r.records,secondary:true}));
  const refusal=r.run();
  assert.equal(refusal.status,1,refusal.stderr);
  assert.match(refusal.stderr,/secondary rate limit/);
  const calls=readFileSync(r.calls,'utf8').trim().split('\n').map(JSON.parse);
  assert.equal(calls.filter(a=>a[0]==='host').length,1);
  assert.equal(calls.at(-1)[0],'host');
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const empty=r.run(['--head-contains','f'.repeat(40)]);
  assert.equal(empty.status,1);
  assert.equal(empty.stdout,'');
  assert.match(empty.stderr,/no matching runs/);
  assert.equal(r.run().status,0);
  const file=join(r.root,'cache',`run-${r.records[0].run.id}-attempt-1.json`);
  const valid=JSON.parse(readFileSync(file,'utf8'));
  for (const content of ['{',JSON.stringify({}),JSON.stringify({...valid,jobs:[{...valid.jobs[0],run_id:1}]})]) {
    writeFileSync(file,content);
    const run=r.run();
    assert.equal(run.status,1);
    assert.equal(run.stdout,'');
    assert.match(run.stderr,/invalid cached attempt|cached attempt identity mismatch|job identity mismatch/);
  }
});


test('timing CLI defaults and persisted observations reconcile through the public entry point', { skip: process.platform === 'win32' }, async (t) => {
  const api=await import(new URL('../../gate-timing.mjs',import.meta.url));
  assert.equal(api.calculateHead,calculateHead);
  assert.equal(api.SCHEMA_VERSION,SCHEMA_VERSION);
  const r=timingReplay(t);
  const cacheFixture=join(r.root,'xdg');
  const homeFixture=join(r.root,'home');
  const cases=[
    [{XDG_CACHE_HOME:cacheFixture},join(cacheFixture,'crozier','gate-timing')],
    [{XDG_CACHE_HOME:'',HOME:homeFixture},join(homeFixture,'.cache','crozier','gate-timing')],
  ];
  for (const [environment,dir] of cases) {
    const run=r.run([],environment,{},true);
    assert.equal(run.status,0,run.stderr);
    const report=JSON.parse(run.stdout);
    assert.deepEqual(JSON.parse(readFileSync(join(dir,'latest-report.json'),'utf8')),report);
    const file=readdirSync(dir).find(name=>name.startsWith('contexts-'));
    assert.ok(file);
    const observation=JSON.parse(readFileSync(join(dir,file),'utf8'));
    assert.equal(observation.observed_at,report.observation.observed_at);
    assert.deepEqual(observation.required_contexts,report.required_contexts);
    assert.deepEqual(observation.protection,{required_status_checks:{contexts:['gate','llmlint']}});
    assert.deepEqual(observation.rules,[]);
    const page=JSON.parse(readFileSync(join(dir,'runs-page-1.json'),'utf8'));
    assert.equal(page.observed_at,report.observation.observed_at);
    assert.deepEqual(page.response.workflow_runs,r.records.map(record=>record.run));
    for (const record of r.records) {
      const metadata=JSON.parse(readFileSync(join(dir,`run-${record.run.id}-metadata.json`),'utf8'));
      assert.deepEqual(metadata,{observed_at:report.observation.observed_at,run:record.run});
    }
  }
});


test('timing CLI rejects mistyped workflow states and unsupported job states', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  for (const variant of [{badRunStatus:true},{badRunConclusion:true},{jobDamage:'status'},{jobDamage:'conclusion'}]) {
    writeFileSync(r.answerFile,JSON.stringify({records:r.records,...variant}));
    const run=r.run();
    assert.equal(run.status,1,JSON.stringify(variant)+': '+run.stderr);
    assert.equal(run.stdout,'');
    assert.match(run.stderr,/invalid run state|invalid job/);
  }
  r.records[0].run.status='waiting';
  r.records[0].run.conclusion=null;
  r.records[0].jobs=[];
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const waiting=r.run();
  assert.equal(waiting.status,0,waiting.stderr);
  assert.equal(JSON.parse(waiting.stdout).runs[0].gate_seconds,null);
  assert.equal(existsSync(join(r.root,'cache',`run-${r.records[0].run.id}-attempt-1.json`)),false);
});

test('timing CLI rejects invalid external JSON and an empty required-context set', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  writeFileSync(r.answerFile,JSON.stringify({records:r.records,invalidJson:true}));
  const invalid=r.run();
  assert.equal(invalid.status,1);
  assert.equal(invalid.stdout,'');
  assert.match(invalid.stderr,/returned invalid JSON/);
  writeFileSync(r.answerFile,JSON.stringify({records:r.records,protection:{required_status_checks:{contexts:[],checks:[]}},rules:[]}));
  const empty=r.run();
  assert.equal(empty.status,1);
  assert.equal(empty.stdout,'');
  assert.match(empty.stderr,/missing required contexts/);
});

test('timing CLI falls back to gh when onevcs is absent from PATH', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  unlinkSync(join(r.root,'onevcs'));
  symlinkSync(process.execPath,join(r.root,'node'));
  const run=r.run([],{PATH:r.root});
  assert.equal(run.status,0,run.stderr);
  assert.equal(JSON.parse(run.stdout).runs.length,r.records.length);
  const calls=readFileSync(r.calls,'utf8').trim().split('\n').map(JSON.parse);
  assert.equal(calls.filter(a=>a[0]==='host').length,0);
  assert.equal(calls.filter(a=>a.at(-1).includes('/attempts/1/jobs')).length,r.records.length);
});


test('timing CLI treats every duplicate required context as an obligation', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  const seed=r.records[0];
  const rival={run:{...seed.run,id:901,name:'other',path:'.github/workflows/other.yml'},jobs:[{...seed.jobs.find(j=>j.name==='gate'),id:999999999,created_at:'2026-11-03T17:54:00Z',started_at:'2026-11-03T17:54:00Z',completed_at:'2026-11-03T18:00:00Z',conclusion:'failure'}]};
  r.records.push(rival);
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const failed=r.run();
  assert.equal(failed.status,0,failed.stderr);
  const head=JSON.parse(failed.stdout).runs.find(h=>h.head_sha===seed.run.head_sha);
  assert.equal(head.conclusion,'failure');
  assert.equal(head.gate_seconds,7594);
  rmSync(join(r.root,'cache'),{recursive:true});
  rival.run.status='in_progress';
  rival.run.conclusion=null;
  Object.assign(rival.jobs[0],{status:'in_progress',conclusion:null,completed_at:null});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const pending=r.run();
  assert.equal(pending.status,0,pending.stderr);
  const incomplete=JSON.parse(pending.stdout).runs.find(h=>h.head_sha===seed.run.head_sha);
  assert.equal(incomplete.gate_seconds,null);
  assert.match(incomplete.reason,/incomplete/);
  assert.deepEqual(incomplete.critical_path,[]);
});

test('timing CLI accepts neutral contexts and refreshes unfinished jobs in completed workflow metadata', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  const seed=r.records[0];
  const gate=seed.jobs.find(j=>j.name==='gate');
  gate.conclusion='neutral';
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const neutral=r.run();
  assert.equal(neutral.status,0,neutral.stderr);
  assert.equal(JSON.parse(neutral.stdout).runs[0].conclusion,'success');
  assert.equal(JSON.parse(neutral.stdout).summary.kinds['release-pr'].n,2);
  rmSync(join(r.root,'cache'),{recursive:true});
  Object.assign(gate,{status:'in_progress',conclusion:null,completed_at:null});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const pending=r.run();
  assert.equal(pending.status,0,pending.stderr);
  assert.equal(JSON.parse(pending.stdout).runs[0].gate_seconds,null);
  const cache=join(r.root,'cache',`run-${seed.run.id}-attempt-1.json`);
  assert.equal(existsSync(cache),false);
  const before=readFileSync(r.calls,'utf8').trim().split('\n').length;
  Object.assign(gate,{status:'completed',conclusion:'success',completed_at:'2026-11-03T20:00:13Z'});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const completed=r.run();
  assert.equal(completed.status,0,completed.stderr);
  assert.equal(JSON.parse(completed.stdout).runs[0].gate_seconds,7594);
  assert.equal(existsSync(cache),true);
  const calls=readFileSync(r.calls,'utf8').trim().split('\n').slice(before).map(JSON.parse);
  assert.equal(calls.filter(a=>a.includes('run-jobs')).length,1);
});


test('public schema validation rejects mistyped reports without relying on summary mismatches', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  const run=r.run();
  assert.equal(run.status,0,run.stderr);
  const report=JSON.parse(run.stdout);
  const invalid=structuredClone(report);
  invalid.window.since=123;
  assert.throws(()=>validateReport(invalid),/invalid timing window/);
  for (const mutate of [
    data=>{data.runs[0].jobs[0].conclusion={invalid:true};},
    data=>{data.runs[0].jobs[0].start_offset_seconds=null;},
    data=>{data.runs[0].created_at=123;},
  ]) {
    const data=structuredClone(report);
    mutate(data);
    assert.throws(()=>validateReport(data),/invalid timing/);
  }
  const reordered=structuredClone(report);
  reordered.summary=Object.fromEntries(Object.entries(reordered.summary).reverse());
  assert.doesNotThrow(()=>validateReport(reordered));
});


test('timing CLI preserves open workflow states without inferring completion or freezing cache', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  const seed=r.records[0];
  for (const state of [{status:'future_state',conclusion:'future_outcome'}, {status:null,conclusion:null}]) {
    Object.assign(seed.run,state);
    writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
    const result=r.run();
    assert.equal(result.status,0,result.stderr);
    const head=JSON.parse(result.stdout).runs.find(h=>h.head_sha===seed.run.head_sha);
    assert.equal(head.gate_seconds,null);
    assert.equal(head.conclusion,null);
    assert.match(head.reason,/unknown workflow/);
    assert.equal(existsSync(join(r.root,'cache',`run-${seed.run.id}-attempt-1.json`)),false);
  }
  Object.assign(seed.run,{status:'completed',conclusion:'success'});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  assert.equal(r.run().status,0);
  assert.equal(existsSync(join(r.root,'cache',`run-${seed.run.id}-attempt-1.json`)),true);
  Object.assign(seed.run,{status:'future_state',conclusion:null});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const refreshed=r.run();
  assert.equal(refreshed.status,0,refreshed.stderr);
  assert.equal(JSON.parse(refreshed.stdout).runs.find(h=>h.head_sha===seed.run.head_sha).gate_seconds,null);
});

test('timing CLI waits for recorded main workflow metadata even when its jobs completed', { skip: process.platform === 'win32' }, (t) => {
  const r=timingReplay(t);
  const main=r.records.find(record=>record.run.event==='push');
  Object.assign(main.run,{status:'in_progress',conclusion:null});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const pending=r.run();
  assert.equal(pending.status,0,pending.stderr);
  const head=JSON.parse(pending.stdout).runs.find(h=>h.kind==='main');
  assert.equal(head.gate_seconds,null);
  assert.equal(head.conclusion,null);
  assert.match(head.reason,/incomplete CI workflow/);
  assert.equal(JSON.parse(pending.stdout).summary.kinds.main.n,1); // The other recorded main head remains complete.
  Object.assign(main.run,{status:'completed',conclusion:'success'});
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const finished=r.run();
  assert.equal(finished.status,0,finished.stderr);
  assert.equal(JSON.parse(finished.stdout).runs.find(h=>h.kind==='main').gate_seconds,4271);
});
