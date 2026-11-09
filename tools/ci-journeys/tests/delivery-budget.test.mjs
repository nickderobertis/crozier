// The registered delivery budget, run the way the host's success hook runs it: real
// onebudgetspec over the repository's budgets.yaml and the real timing CLI, with only the
// onepipeline, onevcs and gh processes doubled. budget-heads.json holds answers recorded
// from GitHub; variants edit one recorded fact to reach states no sampled head reached.
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { chmodSync, existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { delimiter, join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { RELEASE_SKIPPED_LANES } from '../../ci/gate-timing/core.mjs';

const REPO = fileURLToPath(new URL('../../../', import.meta.url));
const CLI = join(REPO, 'tools/ci/gate-timing.mjs');
const recorded = JSON.parse(readFileSync(new URL('./fixtures/gate-timing-budget-heads.json', import.meta.url), 'utf8'));
const CONTEXTS = ['lint', 'test-linux', 'test-macos', 'test-windows'];
const posix = { skip: process.platform === 'win32' ? 'the doubles are POSIX executables' : false };
const RUN = 'landing-run';
const NODE = 'landing-node';

const STUB = `#!/usr/bin/env node
const fs = require('fs');
const a = JSON.parse(fs.readFileSync(process.env.ANSWERS, 'utf8'));
const args = process.argv.slice(2);
const program = require('path').basename(process.argv[1]);
fs.appendFileSync(process.env.CALLS, JSON.stringify([program, ...args]) + '\\n');
const out = (answer) => { process.stdout.write(JSON.stringify(answer)); process.exit(0); };
const refuse = (why) => { console.error(why); process.exit(1); };
if (program === 'gh' && args[0] === 'auth') { process.stdout.write('replay-token'); process.exit(0); }
if (program === 'onepipeline') {
  if (args.join(' ') !== 'telemetry ${RUN} --changes --json' || !process.env.ONEPIPELINE_RUNS_DIR) refuse('onepipeline double: unexpected ' + args.join(' '));
  out(a.telemetry);
}
if (program === 'onevcs' && args[0] === 'status') out(a.status);
const byId = (id) => a.runs.find((r) => r.run.id === Number(id));
if (program === 'onevcs' && args[1] === 'run-jobs') { const id = Number(args[args.indexOf('--run') + 1]); const r = byId(id); out({ jobs: r ? r.attempts[r.run.run_attempt] : [] }); }
const path = args.at(-1);
if (args.includes('rate_limit')) out({ resources: { core: { limit: 5000, remaining: 5000, reset: 0 } } });
if (path.endsWith('/protection')) out({ required_status_checks: { contexts: a.contexts } });
if (path.endsWith('/rules/branches/main')) out([]);
if (/\\/pulls\\/\\d+$/.test(path)) out(a.pull);
if (path.includes('/actions/runs?')) { if (!path.includes('head_sha=' + a.pull.head.sha) || !path.includes('event=pull_request')) refuse('gh double: asked another head: ' + path); const page = Number(new URL('https://api.invalid/' + path).searchParams.get('page')); const listed = a.runs.map((r) => r.run); out({ workflow_runs: a.paginate ? (page === 1 ? [...listed, ...Array.from({ length: 100 - listed.length }, (_, i) => ({ ...listed[0], id: 7000000 + i }))] : []) : listed }); }
let m = /\\/actions\\/runs\\/(\\d+)\\/attempts\\/(\\d+)\\/jobs/.exec(path);
if (m) out({ jobs: byId(m[1]).attempts[m[2]] });
m = /\\/actions\\/runs\\/(\\d+)$/.exec(path);
if (m) out(byId(m[1])?.run ?? { ...a.runs[0].run, id: Number(m[1]) });
refuse('unexpected external request: ' + program + ' ' + args.join(' '));
`;

function hook(t, name, edit = () => {}) {
  const root = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'crozier-budget-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const runs = structuredClone(recorded[name]);
  const head = runs[0].run.head_sha;
  const url = 'https://github.com/nickderobertis/crozier/pull/794';
  const answers = {
    runs, contexts: CONTEXTS,
    pull: { number: 794, head: { sha: head }, merged_at: '2026-11-08T17:27:01Z' },
    status: { publication: { landed: { state: 'yes' } } },
    telemetry: { schema_version: 1, run_id: RUN, changes: [{ node: NODE, lineage: [NODE], repository: 'github.com/nickderobertis/crozier', change_url: url, outcome: 'landed' }] },
  };
  edit(answers);
  writeFileSync(join(root, 'answers.json'), JSON.stringify(answers));
  for (const program of ['gh', 'onevcs', 'onepipeline']) { writeFileSync(join(root, program), STUB); chmodSync(join(root, program), 0o755); }
  const env = { ...process.env, PATH: [root, join(REPO, 'node_modules', '.bin'), process.env.PATH].join(delimiter), ANSWERS: join(root, 'answers.json'), CALLS: join(root, 'calls.jsonl'), XDG_CACHE_HOME: join(root, 'cache'), GH_TOKEN: 'replay', ONEPIPELINE_RUN_ID: RUN, ONEPIPELINE_NODE_ID: NODE, ONEPIPELINE_RUNS_DIR: join(root, 'runs') };
  const spawn = (program, args, extra = {}) => spawnSync(program, args, { cwd: REPO, encoding: 'utf8', env: { ...env, ...extra } });
  const check = () => {
    const run = spawn('onebudgetspec', ['check', 'budgets.yaml', '--label', 'onepipeline', '--json']);
    const results = JSON.parse(run.stdout).results;
    assert.equal(results.length, 1, run.stdout);
    return { status: run.status, result: results[0], raw: run.stdout + run.stderr };
  };
  return { root, head, spawn, check, calls: () => readFileSync(join(root, 'calls.jsonl'), 'utf8').trim().split('\n').map((line) => JSON.parse(line)) };
}

const latest = (entry) => entry.attempts[entry.run.run_attempt];
const onlyLanes = (runs) => runs[0];
const clamp = (job, base, seconds) => { job.completed_at = new Date(Date.parse(base) + seconds * 1000).toISOString().replace(/\.000Z$/, 'Z'); };

test('an accepted landed head inside the line reports its span and verdicts', posix, (t) => {
  const h = hook(t, 'accepted', ({ runs }) => {
    const entry = onlyLanes(runs);
    for (const job of latest(entry)) clamp(job, entry.run.created_at, 1800);
  });
  const { status, result } = h.check();
  assert.equal(status, 0, JSON.stringify(result));
  assert.equal(result.verdict, 'within');
  assert.equal(result.actual, 1800);
  assert.equal(result.threshold, 3599);
  assert.match(result.detail, /lint=success, test-linux=success, test-macos=success, test-windows=success/);
});

test('a recorded four-lane head over the line is over, with every job explained', posix, (t) => {
  const h = hook(t, 'accepted');
  const { status, result } = h.check();
  assert.equal(status, 1, JSON.stringify(result));
  assert.equal(result.verdict, 'over');
  assert.equal(result.actual, 8380);
  assert.match(result.detail, new RegExp(`head ${h.head} of change #794, merged 2026-11-08T17:27:01Z`));
  assert.match(result.detail, /push proxy/);
  assert.match(result.detail, /terminal: test-linux/);
  assert.match(result.detail, /test-linux\[run 42489795217 attempt 1\] success needs=23s queue=2s execution=8355s/);
  assert.match(result.detail, /test-macos\[run 42489795217 attempt 1\] success needs=23s queue=135s execution=5991s/);
  assert.match(result.detail, /failed attempts: none/);
  const asked = h.calls().map((call) => call.join(' '));
  assert.ok(asked.some((call) => call.includes('telemetry landing-run --changes --json')));
  assert.ok(asked.some((call) => call.startsWith('onevcs status https://github.com/nickderobertis/crozier/pull/794')));
});

test('a rerun spans every attempt and names the ones that failed', posix, (t) => {
  const h = hook(t, 'rerun');
  const { status, result } = h.check();
  assert.equal(status, 1, JSON.stringify(result));
  assert.equal(result.actual, 16363);
  assert.match(result.detail, /test-windows\[run 42481455354 attempt 1\] cancelled/);
  assert.match(result.detail, /test-windows\[run 42481455354 attempt 3\] success/);
  assert.match(result.detail, /run 42481455354 attempt 1: test-windows=cancelled, gate=failure/);
});

test('a guarded release head accepts its skipped platform lanes', posix, (t) => {
  const h = hook(t, 'release');
  const { status, result } = h.check();
  assert.equal(status, 0, JSON.stringify(result));
  assert.equal(result.actual, 425);
  assert.match(result.detail, /test-linux=skipped, test-macos=skipped, test-windows=skipped/);
});

const errored = (t, name, edit, message) => {
  const h = hook(t, name, edit);
  const { status, result, raw } = h.check();
  assert.equal(status, 3, raw);
  assert.equal(result.verdict, 'error', raw);
  assert.equal(result.actual, null, raw);
  assert.match(raw, message);
};

test('a skipped lane off the guarded release path is a missing verdict', posix, (t) => errored(t, 'release', ({ runs }) => { for (const entry of runs) entry.run.head_branch = 'feature/ordinary'; }, /test-linux: skipped outside the guarded release path/));
test('a release head whose lint failed cannot admit skipped lanes', posix, (t) => errored(t, 'release', ({ runs }) => { latest(runs[0]).find((job) => job.name === 'lint').conclusion = 'failure'; }, /test-linux: skipped outside the guarded release path/));
test('a skipped release from a fork is a missing verdict', posix, (t) => errored(t, 'release', ({ runs }) => { runs[0].run.head_repository.full_name = 'someone/crozier'; }, /skipped outside the guarded release path/));
test('a cancelled head is an error, never a span', posix, (t) => errored(t, 'cancelled', () => {}, /missing required verdict.*test-macos: cancelled is not an accepted verdict/));
test('a null verdict is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { const job = latest(runs[0]).find((j) => j.name === 'test-macos'); job.status = 'in_progress'; job.conclusion = null; job.completed_at = null; runs[0].run.status = 'in_progress'; runs[0].run.conclusion = null; }, /test-macos: in_progress is not an accepted verdict/));
test('a failed final verdict is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { latest(runs[0]).find((j) => j.name === 'test-linux').conclusion = 'failure'; }, /test-linux: failure is not an accepted verdict/));
test('a neutral required verdict is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { latest(runs[0]).find((j) => j.name === 'test-linux').conclusion = 'neutral'; }, /test-linux: neutral is not an accepted verdict/));
test('a guarded release cannot accept a skipped context outside its lanes', posix, (t) => errored(t, 'release', (a) => { const jobs = latest(a.runs[0]); jobs.push({ ...jobs.find((j) => j.name === 'test-linux'), id: 99, name: 'extra-check' }); a.contexts = [...CONTEXTS, 'extra-check']; }, /extra-check: skipped outside the guarded release path/));
test('a required context no job reported is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { runs[0].attempts[1] = latest(runs[0]).filter((j) => j.name !== 'test-macos'); }, /test-macos: no job reported this context/));
test('a context that became required after the head ran is an error', posix, (t) => errored(t, 'accepted', (a) => { a.contexts = [...CONTEXTS, 'test-freebsd']; }, /test-freebsd: no job reported this context/));
test('an unlanded node has no landing to measure', posix, (t) => errored(t, 'accepted', (a) => { a.telemetry.changes[0].change_url = null; a.telemetry.changes[0].outcome = 'running'; }, /records no change request \(outcome running\)/));
test('a change onevcs says did not land is an error', posix, (t) => errored(t, 'accepted', (a) => { a.status.publication.landed.state = 'no'; }, /has not landed according to onevcs/));
test('a node this run never recorded is an error', posix, (t) => errored(t, 'accepted', (a) => { a.telemetry.changes = []; }, /recorded no nickderobertis\/crozier change for node landing-node/));
test('a head with no pull_request run is an error', posix, (t) => errored(t, 'accepted', (a) => { a.runs = []; a.pull.head.sha = 'a'.repeat(40); }, /no pull_request workflow run at landed head/));

test('a node named only in a retry lineage selects its change', posix, (t) => {
  const h = hook(t, 'release', (a) => { a.telemetry.changes[0].node = 'landing-node-r1'; a.telemetry.changes[0].lineage = [NODE, 'landing-node-r1']; });
  assert.equal(h.check().result.actual, 425);
});
test('malformed telemetry is an error', posix, (t) => errored(t, 'accepted', (a) => { a.telemetry.run_id = 'other'; }, /invalid per-change telemetry for run landing-run/));
test('a string lineage cannot select a change by substring', posix, (t) => errored(t, 'accepted', (a) => { a.telemetry.changes[0].node = 'other'; a.telemetry.changes[0].lineage = 'prefix-landing-node-suffix'; }, /recorded no nickderobertis\/crozier change for node landing-node/));
test('a pull request without merged metadata is an error', posix, (t) => errored(t, 'accepted', (a) => { a.pull.merged_at = null; }, /reports no merged head/));
test('a listed run at another head is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { runs[0].run.head_sha = 'b'.repeat(40); }, /is not a pull_request run at landed head/));
test('a listed run from another event is an error', posix, (t) => errored(t, 'accepted', ({ runs }) => { runs[0].run.event = 'push'; }, /is not a pull_request run at landed head/));
test('accepted verdicts on an unknown workflow state are an error, never a span', posix, (t) => errored(t, 'accepted', ({ runs }) => { runs[0].run.status = 'mystery'; }, /no measurable span at .*unknown workflow state/));
test('every page of a head\'s workflow runs is read', posix, (t) => {
  const h = hook(t, 'release', (a) => { a.paginate = true; });
  assert.equal(h.check().result.actual, 425);
  const pages = h.calls().filter((call) => call.at(-1).includes('/actions/runs?')).map((call) => new URL('https://api.invalid/' + call.at(-1)).searchParams.get('page'));
  assert.deepEqual(pages, ['1', '2']);
});

test('the guarded release exception is exactly what ci.yml skips', posix, () => {
  const workflow = readFileSync(join(REPO, '.github/workflows/ci.yml'), 'utf8');
  const required = JSON.parse(readFileSync(join(REPO, '.github/governance.json'), 'utf8')).required_checks;
  const guardExpression = "!(github.event.pull_request.head.repo.full_name == github.repository && startsWith(github.head_ref, 'release-plz-'))";
  const condition = (lane) => { const job = workflow.slice(workflow.indexOf(`\n  ${lane}:\n`) + 1); return job.slice(0, job.indexOf('runs-on:')); };
  const skipped = required.filter((lane) => condition(lane).includes(guardExpression));
  assert.deepEqual([...RELEASE_SKIPPED_LANES].sort(), [...skipped].sort());
  assert.ok(workflow.includes('scripts/release-branch-guard.mjs'), 'lint holds the release branch to the guard');
  assert.ok(!RELEASE_SKIPPED_LANES.includes('lint'));
});

test('exit codes: 0 measured, 1 missing data, 2 invalid invocation', posix, (t) => {
  const measured = hook(t, 'release');
  const result = join(measured.root, 'result.json');
  const ok = measured.spawn(process.execPath, [CLI, 'budget'], { ONEBUDGETSPEC_RESULT: result });
  assert.equal(ok.status, 0, ok.stderr);
  const written = JSON.parse(readFileSync(result, 'utf8'));
  assert.deepEqual(Object.keys(written).sort(), ['detail', 'value']);
  assert.equal(written.value, 425);

  const missing = hook(t, 'cancelled');
  const absent = join(missing.root, 'result.json');
  const refused = missing.spawn(process.execPath, [CLI, 'budget'], { ONEBUDGETSPEC_RESULT: absent });
  assert.equal(refused.status, 1, refused.stderr);
  assert.equal(existsSync(absent), false, 'missing data never writes a figure');

  for (const unset of ['ONEPIPELINE_RUN_ID', 'ONEPIPELINE_NODE_ID', 'ONEPIPELINE_RUNS_DIR', 'ONEBUDGETSPEC_RESULT']) {
    const run = measured.spawn(process.execPath, [CLI, 'budget'], { ONEBUDGETSPEC_RESULT: result, [unset]: '' });
    assert.equal(run.status, 2, `${unset}: ${run.stderr}`);
    assert.match(run.stderr, new RegExp(`${unset} is not set`));
  }
  const extra = measured.spawn(process.execPath, [CLI, 'budget', '--limit', '1'], { ONEBUDGETSPEC_RESULT: result });
  assert.equal(extra.status, 2, extra.stderr);
});

test('a finished attempt read once is reused from the persistent cache', posix, (t) => {
  const h = hook(t, 'accepted', ({ runs }) => { for (const job of latest(onlyLanes(runs))) clamp(job, runs[0].run.created_at, 1800); });
  assert.equal(h.check().status, 0);
  assert.equal(h.check().status, 0);
  assert.equal(h.calls().filter((call) => call[0] === 'onevcs' && call[1] === 'host').length, 1);
});

test('only the delivery hook selects this budget', posix, (t) => {
  const registry = readFileSync(join(REPO, 'budgets.yaml'), 'utf8');
  const entry = registry.slice(registry.indexOf('- id: crozier-pr-gate-minutes'));
  assert.match(entry, /command: \[node, tools\/ci\/gate-timing\.mjs, budget\]/);
  assert.match(entry, /threshold: 3599/);
  assert.match(entry, /labels: \[onepipeline\]/);
  const h = hook(t, 'accepted');
  const gate = h.spawn('onebudgetspec', ['list', 'budgets.yaml', '--exclude-label', 'release-tail', '--exclude-label', 'onepipeline', '--json']);
  assert.equal(gate.status, 0, gate.stderr);
  assert.deepEqual(JSON.parse(gate.stdout).budgets ?? [], []);
  const recipe = readFileSync(join(REPO, 'justfile'), 'utf8').split('\n').find((line) => line.includes('onebudgetspec check budgets.yaml'));
  assert.match(recipe, /--exclude-label release-tail --exclude-label onepipeline/);
  const workflows = ['ci.yml', 'release.yml'].map((file) => readFileSync(join(REPO, '.github/workflows', file), 'utf8')).join('\n');
  assert.doesNotMatch(workflows, /--label onepipeline|gate-timing\.mjs budget/);
});
