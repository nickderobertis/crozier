#!/usr/bin/env node
// Maintainer timing contract. No generation or target execution occurs here.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const SCHEMA_VERSION = 1;
export const REPOSITORY = 'nickderobertis/crozier';
export const HELP = `usage: node tools/ci/gate-timing.mjs runs --since RFC3339 --until RFC3339
  [--limit N] [--head-contains SHA] [--cache-dir DIR] [--format json|markdown]
Defaults: repository ${REPOSITORY}; format json; cache
  \${XDG_CACHE_HOME:-$HOME/.cache}/crozier/gate-timing.
JSON schema_version: 1; required_contexts, window, runs, summary.
Gate: first workflow creation at a head to latest required-context completion,
including failed attempts and waiting. Cancelled/missing contexts yield null and
reason, excluded from passing summaries. Main measures CI completion separately.
Workflow creation is a proxy seconds after push; commit authored time is never used.
Queue is job created-to-start, not workflow-to-job dependency/eligibility delay.
Contexts are observed now from branch protection and rulesets; historical settings
are ambiguous. Completed attempt responses are cached; run metadata is refreshed.
Exit: 0 answer; 1 failed/missing read; 2 invalid invocation.`;

export function parseArgs(args) {
  if (args.length === 1 && ['--help', '-h'].includes(args[0])) return { help: true };
  if (args.shift() !== 'runs') throw new TypeError('expected runs (see --help)');
  const options = { format: 'json', limit: 100, 'cache-dir': join(process.env.XDG_CACHE_HOME || join(homedir(), '.cache'), 'crozier/gate-timing') };
  const seen = new Set();
  while (args.length) {
    const flag = args.shift();
    if (!['--since', '--until', '--limit', '--head-contains', '--cache-dir', '--format'].includes(flag) || seen.has(flag)) throw new TypeError(`invalid argument ${flag}`);
    seen.add(flag);
    const value = args.shift();
    if (!value || value.startsWith('--')) throw new TypeError(`missing value for ${flag}`);
    options[flag.slice(2)] = value;
  }
  const rfc3339 = /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)$/;
  for (const key of ['since', 'until']) if (!rfc3339.test(options[key] ?? '') || !Number.isFinite(Date.parse(options[key]))) throw new TypeError(`${key} must be RFC3339`);
  if (Date.parse(options.since) >= Date.parse(options.until)) throw new TypeError('since must precede until');
  if (!/^[1-9]\d*$/.test(String(options.limit)) || !Number.isSafeInteger(Number(options.limit))) throw new TypeError('limit must be a positive integer');
  options.limit = Number(options.limit);
  if (!['json', 'markdown'].includes(options.format)) throw new TypeError('format must be json or markdown');
  if (options['head-contains'] && !/^[a-f0-9]{7,40}$/.test(options['head-contains'])) throw new TypeError('head-contains must be a SHA');
  return options;
}

/** Nx Chrome trace duration is in microseconds, including cache replay status. */
export function taskTimings(events) {
  if (!Array.isArray(events)) throw new Error('Nx profile is not an event array');
  return events.filter((event) => event.ph === 'X').map((event) => {
    if (typeof event.name !== 'string' || !Number.isFinite(event.dur) || event.dur < 0 || typeof event.args?.status !== 'string') throw new Error('invalid Nx task timing');
    return { name: event.name, seconds: event.dur / 1_000_000, status: event.args.status };
  });
}

export function statistics(values) {
  const a = values.filter((x) => typeof x === 'number' && Number.isFinite(x)).sort((x, y) => x - y);
  const n = a.length;
  return { n, median: n ? (a[Math.floor((n - 1) / 2)] + a[Math.ceil((n - 1) / 2)]) / 2 : null, p95: n ? a[Math.ceil(n * .95) - 1] : null, max: n ? a[n - 1] : null };
}
const seconds = (a, b) => a && b && Number.isFinite(Date.parse(a)) && Number.isFinite(Date.parse(b)) ? Math.max(0, (Date.parse(b) - Date.parse(a)) / 1000) : null;

export function validateAttempt(attempt) {
  const { run, jobs } = attempt ?? {};
  if (!run || !Number.isSafeInteger(run.id) || !Number.isSafeInteger(run.run_attempt) || run.run_attempt < 1 || typeof run.head_sha !== 'string' || typeof run.head_branch !== 'string' || typeof run.event !== 'string' || !Number.isFinite(Date.parse(run.created_at))) throw new Error('missing or invalid run metadata');
  if (!Array.isArray(jobs) || (!jobs.length && !['cancelled', 'skipped'].includes(run.conclusion))) throw new Error(`missing jobs for run ${run.id}`);
  for (const job of jobs) {
    if (typeof job.name !== 'string' || typeof job.status !== 'string' || (job.conclusion !== null && typeof job.conclusion !== 'string')) throw new Error(`invalid job for run ${run.id}`);
    for (const key of ['created_at', 'started_at', 'completed_at']) if (job[key] != null && !Number.isFinite(Date.parse(job[key]))) throw new Error(`invalid job ${key}`);
  }
  return attempt;
}

export function calculateHead(attempts, required) {
  if (!attempts.length) throw new Error('missing head attempts');
  attempts.forEach(validateAttempt);
  const sorted = [...attempts].sort((a, b) => Date.parse(a.run.created_at) - Date.parse(b.run.created_at) || a.run.run_attempt - b.run.run_attempt);
  const first = sorted[0].run;
  const last = sorted.at(-1).run;
  const kind = first.event === 'push' ? 'main' : first.head_branch.startsWith('release-plz-') ? 'release-pr' : 'pr';
  const allJobs = sorted.flatMap(({ run, jobs }) => jobs.map((job) => ({ ...job, run_id: run.id, run_attempt: run.run_attempt })));
  // Latest attempt of each workflow replaces its predecessor's context result,
  // but all attempts remain in the elapsed span and job inventory.
  const latest = new Map();
  for (const { run, jobs } of sorted) latest.set(run.id, { run, jobs });
  const finalJobs = [...latest.values()].flatMap(({ jobs }) => jobs);
  const mainJobs = [...latest.values()].filter(({ run }) => run.name === 'ci' || run.path === '.github/workflows/ci.yml').flatMap(({ jobs }) => jobs);
  const contexts = kind === 'main' ? mainJobs : required.map((name) => finalJobs.filter((job) => job.name === name).sort((a, b) => Date.parse(a.completed_at ?? 0) - Date.parse(b.completed_at ?? 0)).at(-1));
  let reason = null;
  if (!contexts.length || contexts.some((j) => !j || !j.completed_at)) reason = sorted.some(({ run }) => run.conclusion === 'cancelled') ? 'cancelled workflow; missing or incomplete context' : 'missing or incomplete context';
  else if (contexts.some((j) => j.conclusion === 'cancelled')) reason = 'cancelled context';
  const end = reason ? null : contexts.map((j) => j.completed_at).sort().at(-1);
  const failed = contexts.some((j) => j && !['success', 'skipped', 'neutral'].includes(j.conclusion));
  return {
    run_id: first.id, attempt: Math.max(...sorted.map(({ run }) => run.run_attempt)), event: first.event, kind,
    head_sha: first.head_sha, pr_number: first.pull_requests?.[0]?.number ?? null, created_at: first.created_at,
    conclusion: reason ? (reason.startsWith('cancelled') ? 'cancelled' : null) : failed ? 'failure' : 'success',
    gate_seconds: seconds(first.created_at, end), reason,
    critical_path: end ? contexts.filter((j) => j.completed_at === end).map((j) => j.name) : [],
    jobs: allJobs.map((job) => ({ name: job.name, conclusion: job.conclusion ?? null,
      queue_seconds: seconds(job.created_at, job.started_at), run_seconds: seconds(job.started_at, job.completed_at),
      start_offset_seconds: seconds(first.created_at, job.started_at) ?? 0,
      ...(job.started_at ? {} : { start_offset_reason: 'job never started; zero is an unavailable-offset sentinel' }),
      run_id: job.run_id, attempt: job.run_attempt, created_at: job.created_at ?? null, started_at: job.started_at ?? null, completed_at: job.completed_at ?? null,
    })),
    last_observed_run_id: last.id,
  };
}

export function summarize(runs) {
  const kinds = Object.fromEntries(['pr', 'release-pr', 'main'].map((kind) => [kind, {
    ...statistics(runs.filter((r) => r.kind === kind && r.conclusion === 'success').map((r) => r.gate_seconds)),
    observed: runs.filter((r) => r.kind === kind).length,
    unsuccessful: runs.filter((r) => r.kind === kind && r.conclusion !== 'success').length,
  }]));
  const jobs = {};
  for (const name of [...new Set(runs.flatMap((r) => r.jobs.map((j) => j.name)))].sort()) {
    const matches = runs.flatMap((r) => r.jobs).filter((j) => j.name === name);
    jobs[name] = { run: statistics(matches.map((j) => j.run_seconds)), queue: statistics(matches.map((j) => j.queue_seconds)) };
  }
  return { kinds, jobs };
}

export function validateReport(report) {
  if (!report.window || !Number.isFinite(Date.parse(report.window.since)) || !Number.isFinite(Date.parse(report.window.until))) throw new Error('invalid timing window');
  if (report.schema_version !== SCHEMA_VERSION || !Array.isArray(report.required_contexts) || !report.required_contexts.every((s) => typeof s === 'string') || !Array.isArray(report.runs)) throw new Error('invalid timing report envelope');
  for (const run of report.runs) {
    if (!Number.isInteger(run.run_id) || !Number.isInteger(run.attempt) || !['pr', 'release-pr', 'main'].includes(run.kind) || !Array.isArray(run.jobs) || !Array.isArray(run.critical_path)) throw new Error('invalid timing run');
    if (typeof run.head_sha !== 'string' || typeof run.event !== 'string' || !Number.isFinite(Date.parse(run.created_at)) || (run.pr_number !== null && !Number.isInteger(run.pr_number)) || (run.conclusion !== null && typeof run.conclusion !== 'string') || !run.critical_path.every((s) => typeof s === 'string')) throw new Error('invalid timing run fields');
    if (run.gate_seconds === null && !run.reason) throw new Error('null gate span needs a reason');
    for (const key of ['gate_seconds']) if (run[key] !== null && (!Number.isFinite(run[key]) || run[key] < 0)) throw new Error(`invalid ${key}`);
    for (const job of run.jobs) for (const key of ['queue_seconds', 'run_seconds', 'start_offset_seconds']) if (job[key] !== null && (!Number.isFinite(job[key]) || job[key] < 0)) throw new Error(`invalid ${key}`);
  }
  if (JSON.stringify(report.summary) !== JSON.stringify(summarize(report.runs))) throw new Error('summary does not reconcile');
  return report;
}

function command(program, args) {
  const env = { ...process.env };
  if (program === 'onevcs' && !env.GH_TOKEN && !env.GITHUB_TOKEN) {
    const auth = spawnSync('gh', ['auth', 'token'], { encoding: 'utf8' });
    if (auth.status === 0) env.GH_TOKEN = auth.stdout.trim();
  }
  const result = spawnSync(program, args, { env, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
  if (result.status !== 0) throw new Error(`${program} ${args.join(' ')}: ${result.stderr || result.error?.message || 'read failed'}`);
  try { return JSON.parse(result.stdout); } catch { throw new Error(`${program} returned invalid JSON`); }
}

export async function collect(options) {
  const dir = options['cache-dir'];
  mkdirSync(dir, { recursive: true });
  const observed_at = new Date().toISOString();
  const events = [];
  // Every scan observes the budget before issuing reads. Secondary-limit errors
  // are propagated immediately; they must never be retried by a quota loop.
  const guard = async () => {
    for (;;) {
      const { resources: { core } } = command('gh', ['api', 'rate_limit']);
      if (core.remaining >= core.limit * .4) return;
      const until = new Date(core.reset * 1000 + 1000).toISOString();
      events.push({ event: 'quota_wait', observed_at: new Date().toISOString(), until });
      console.error(`gate-timing: quota_wait until ${until}`);
      while (Date.now() < Date.parse(until)) await new Promise((r) => setTimeout(r, Math.min(1000, Date.parse(until) - Date.now())));
      events.push({ event: 'quota_resume', observed_at: new Date().toISOString() });
      console.error('gate-timing: quota_resume');
    }
  };
  const get = async (path) => { await guard(); return command('gh', ['api', '--method', 'GET', path]); };
  const root = `repos/${REPOSITORY}`;
  const protection = await get(`${root}/branches/main/protection`);
  const rules = await get(`${root}/rules/branches/main`);
  const required = [...new Set([
    ...(protection.required_status_checks?.contexts ?? []),
    ...(protection.required_status_checks?.checks ?? []).map((c) => c.context),
    ...rules.filter((r) => r.type === 'required_status_checks').flatMap((r) => r.parameters.required_status_checks.map((c) => c.context)),
  ])].sort();
  if (!required.length) throw new Error('missing required contexts at observation');
  writeFileSync(join(dir, `contexts-${observed_at.replaceAll(':', '-')}.json`), JSON.stringify({ observed_at, required_contexts: required, protection, rules }, null, 2));
  const runs = [];
  let complete = true;
  for (let page = 1;; page++) {
    const answer = await get(`${root}/actions/runs?per_page=100&page=${page}&created=${encodeURIComponent(`${options.since}..${options.until}`)}`);
    if (!Array.isArray(answer.workflow_runs)) throw new Error('missing workflow_runs');
    writeFileSync(join(dir, `runs-page-${page}.json`), JSON.stringify({ observed_at, response: answer }, null, 2));
    runs.push(...answer.workflow_runs);
    if (answer.workflow_runs.length < 100) break;
    if (runs.length >= options.limit) { complete = false; break; }
  }
  const eligible = runs.filter((r) => (r.event === 'pull_request' || (r.event === 'push' && r.head_branch === 'main')) && (!options['head-contains'] || r.head_sha.includes(options['head-contains'])));
  const selected = eligible.slice(0, options.limit);
  if (eligible.length > options.limit) complete = false;
  if (!selected.length) throw new Error('no matching runs in window');
  const groups = new Map();
  for (const run of selected) {
    // Refresh metadata even for a cached run: a rerun adds immutable attempts.
    const fresh = await get(`${root}/actions/runs/${run.id}`);
    if (!Number.isInteger(fresh.run_attempt) || !fresh.created_at) throw new Error(`missing metadata for run ${run.id}`);
    writeFileSync(join(dir, `run-${run.id}-metadata.json`), JSON.stringify({ observed_at, run: fresh }, null, 2));
    const key = `${fresh.event}:${fresh.head_sha}`;
    if (!groups.has(key)) groups.set(key, []);
    for (let attempt = 1; attempt <= fresh.run_attempt; attempt++) {
      const file = join(dir, `run-${run.id}-attempt-${attempt}.json`);
      let raw;
      if (existsSync(file)) raw = JSON.parse(readFileSync(file, 'utf8'));
      else {
        let jobs;
        if (attempt === fresh.run_attempt) {
          await guard();
          // onevcs supports latest jobs, not historical attempt selection.
          jobs = command('onevcs', ['host', 'run-jobs', '--repo', REPOSITORY, '--run', String(run.id), '--json']).jobs;
        } else {
          jobs = [];
          for (let page = 1;; page++) {
            const response = await get(`${root}/actions/runs/${run.id}/attempts/${attempt}/jobs?per_page=100&page=${page}`);
            if (!Array.isArray(response.jobs)) throw new Error('missing jobs');
            jobs.push(...response.jobs);
            if (response.jobs.length < 100) break;
          }
        }
        if (!Array.isArray(jobs) || (!jobs.length && !['cancelled', 'skipped'].includes(fresh.conclusion)) || jobs.some((j) => j.run_attempt !== attempt)) throw new Error(`missing or mismatched jobs for ${run.id}/${attempt}`);
        raw = { observed_at, required_contexts: required, run: { ...fresh, run_attempt: attempt }, jobs };
        if ((attempt < fresh.run_attempt || fresh.status === 'completed') && jobs.every((j) => j.status === 'completed')) writeFileSync(file, JSON.stringify(raw, null, 2));
      }
      groups.get(key).push(validateAttempt(raw));
    }
  }
  const measured = [...groups.values()].map((attempts) => calculateHead(attempts, required));
  const report = validateReport({ schema_version: SCHEMA_VERSION, required_contexts: required, window: { since: options.since, until: options.until }, runs: measured, summary: summarize(measured),
    observation: { observed_at, complete, workflow_runs: selected.length, jobs: measured.reduce((n, r) => n + r.jobs.length, 0), events,
      limitations: ['Current protection/rulesets cannot establish historical required contexts.', 'First workflow creation is a proxy seconds after push.', 'critical_path lists terminal contexts; job DAG ancestry is unavailable.', 'Main measures CI completion, not PR required checks.'] } });
  writeFileSync(join(dir, 'latest-report.json'), JSON.stringify(report, null, 2));
  return report;
}

export function markdown(report) {
  return `Window: ${report.window.since} — ${report.window.until}\n\n| Kind | Passing n | Median seconds | p95 | Max | Unsuccessful |\n|---|---:|---:|---:|---:|---:|\n` + Object.entries(report.summary.kinds).map(([kind, s]) => `| ${kind} | ${s.n} | ${s.median ?? 'unknown'} | ${s.p95 ?? 'unknown'} | ${s.max ?? 'unknown'} | ${s.unsuccessful} |`).join('\n') + '\n';
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  let options;
  try { options = parseArgs(process.argv.slice(2)); } catch (e) { console.error(`gate-timing: ${e.message}`); process.exitCode = 2; }
  if (options?.help) console.log(HELP);
  else if (options) try { const report = await collect(options); console.log(options.format === 'markdown' ? markdown(report) : JSON.stringify(report, null, 2)); } catch (e) { console.error(`gate-timing: ${e.message}`); process.exitCode = 1; }
}
