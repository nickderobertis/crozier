#!/usr/bin/env node
// Maintainer timing contract. No generation or target execution occurs here.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';
import { isDeepStrictEqual } from 'node:util';

export const SCHEMA_VERSION = 1;
export const REPOSITORY = 'nickderobertis/crozier';
export const CI_WORKFLOW_PATH = '.github/workflows/ci.yml';
const isCIWorkflow = (run) => run.path.split('@')[0] === CI_WORKFLOW_PATH;
export const CLI_OPTIONS = Object.freeze({ since: 'RFC3339', until: 'RFC3339', limit: 'N', 'head-contains': 'SHA', 'cache-dir': 'DIR', format: 'json|markdown' });
export const HELP = `usage: node tools/ci/gate-timing.mjs runs ${Object.entries(CLI_OPTIONS).map(([name, value]) => ['since', 'until'].includes(name) ? `--${name} ${value}` : `[--${name} ${value}]`).join(' ')}
Defaults: repository ${REPOSITORY}; format json; cache
  \${XDG_CACHE_HOME:-$HOME/.cache}/crozier/gate-timing.
JSON schema_version: ${SCHEMA_VERSION}; required_contexts, window, runs, summary.
Gate: first workflow creation at a head to latest required-context completion,
including failed attempts and waiting. Cancelled/missing contexts yield null and
reason, excluded from passing summaries. Main measures CI completion separately.
Workflow creation is a proxy seconds after push; commit authored time is never used.
Queue is job created-to-start, not workflow-to-job dependency/eligibility delay.
Contexts are observed now from branch protection and rulesets; historical settings
are ambiguous. Completed attempt responses are cached; run metadata is refreshed.
Exit: 0 answer; 1 failed/missing read; 2 invalid invocation.`;

export function validTimestamp(value) {
  if (typeof value !== 'string') return false;
  const match = /^(\d{4})-(\d\d)-(\d\d)[Tt](?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:[Zz]|[+-]\d\d:\d\d)$/.exec(value);
  if (!match || !Number.isFinite(Date.parse(value))) return false;
  const [, y, m, d] = match.map(Number);
  const leap = y % 4 === 0 && (y % 100 !== 0 || y % 400 === 0);
  const days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return m >= 1 && m <= 12 && d >= 1 && d <= days[m - 1];
}

// Consumed-subset read boundary: validate only fields used by this tool from
// GitHub REST responses, not the entire upstream response schema. Source:
// https://github.com/github/rest-api-description/tree/30b3f7ce34286e7f3070945e44d10593e0cb50d3
// This pinned observation contract deliberately rejects malformed consumed fields;
// unrelated upstream additions are ignored. It is not a second public API schema.
// Job enums are pinned to github/rest-api-description commit
// 30b3f7ce34286e7f3070945e44d10593e0cb50d3, components.schemas.job.
// Workflow-run status/conclusion are open nullable strings in that same schema.
// llmlint: ignore[contracts_have_one_source_or_a_drift_gate] These job-only enum values deliberately freeze the observed API boundary at rest-api-description 30b3f7ce34286e7f3070945e44d10593e0cb50d3 (components.schemas.job), per maintainer ruling; future job values fail the read until deliberately adopted, while workflow states remain open nullable strings. No live-schema drift update is intended.
export const ACTION_STATUSES = Object.freeze(['completed', 'in_progress', 'queued', 'requested', 'waiting', 'pending']);
// llmlint: ignore[contracts_have_one_source_or_a_drift_gate] This job-only conclusion set uses the same pinned components.schemas.job contract at 30b3f7ce34286e7f3070945e44d10593e0cb50d3; the maintainer explicitly requires a small in-code constant, with unknown values rejected rather than a moving live-schema dependency.
export const ACTION_CONCLUSIONS = Object.freeze(['success', 'failure', 'neutral', 'cancelled', 'skipped', 'timed_out', 'action_required']);

// llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] Workflow fields are the consumed-subset read boundary documented above; local identity and timestamp checks protect calculation inputs, not a restatement of the full workflow schema.
export function validateRun(run) {
  if (!run || !Number.isSafeInteger(run.id) || run.id < 1 || !Number.isSafeInteger(run.run_attempt) || run.run_attempt < 1 || !/^(?:[a-f0-9]{40}|[a-f0-9]{64})$/.test(run.head_sha ?? '') || typeof run.head_branch !== 'string' || typeof run.event !== 'string' || !validTimestamp(run.created_at)) throw new Error('missing or invalid run metadata');
  if (typeof run.name !== 'string' || !run.name.trim() || typeof run.path !== 'string' || !run.path.trim()) throw new Error('invalid workflow name/path');
  if ((run.status !== null && typeof run.status !== 'string') || (run.conclusion !== null && typeof run.conclusion !== 'string')) throw new Error('invalid run state');
  return run;
}
// llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]

// llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] Quota fields are the consumed-subset read boundary documented above; local range checks enforce the observation safety policy rather than duplicate the upstream response contract.
export function validateQuota(response) {
  const core = response?.resources?.core;
  if (!core || !Number.isSafeInteger(core.limit) || core.limit < 1 || !Number.isSafeInteger(core.remaining) || core.remaining < 0 || core.remaining > core.limit || !Number.isSafeInteger(core.reset) || core.reset < 0 || !Number.isFinite(new Date(core.reset * 1000 + 1000).getTime())) throw new Error('invalid quota response');
  return core;
}
// llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]

// llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] Protection and rules fields are the consumed-subset read boundary documented above; this extraction validates only observed context names used by the gate calculation.
export function requiredContexts(protection, rules) {
  if (!protection || typeof protection !== 'object' || Array.isArray(protection) || !Array.isArray(rules)) throw new Error('invalid protection/rules response');
  const status = protection.required_status_checks;
  if (status != null && (typeof status !== 'object' || Array.isArray(status))) throw new Error('invalid required status checks');
  const names = [];
  const add = (values, objects = false) => {
    if (!Array.isArray(values)) throw new Error('invalid required context list');
    for (const item of values) {
      const name = objects ? item?.context : item;
      if (typeof name !== 'string' || !name.trim()) throw new Error('invalid required context name');
      names.push(name);
    }
  };
  add(status?.contexts ?? []);
  add(status?.checks ?? [], true);
  for (const rule of rules) {
    if (!rule || typeof rule.type !== 'string') throw new Error('invalid branch rule');
    if (rule.type === 'required_status_checks') add(rule.parameters?.required_status_checks, true);
  }
  return [...new Set(names)].sort();
}
// llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]

export function parseArgs(args) {
  if (args.length === 1 && ['--help', '-h'].includes(args[0])) return { help: true };
  if (args.shift() !== 'runs') throw new TypeError('expected runs (see --help)');
  const options = { format: 'json', limit: 100, 'cache-dir': join(process.env.XDG_CACHE_HOME || join(homedir(), '.cache'), 'crozier/gate-timing') };
  const seen = new Set();
  while (args.length) {
    const flag = args.shift();
    if (!Object.hasOwn(CLI_OPTIONS, flag.slice(2)) || !flag.startsWith('--') || seen.has(flag)) throw new TypeError(`invalid argument ${flag}`);
    seen.add(flag);
    const value = args.shift();
    if (!value || value.startsWith('--')) throw new TypeError(`missing value for ${flag}`);
    options[flag.slice(2)] = value;
  }
  for (const key of ['since', 'until']) if (!validTimestamp(options[key])) throw new TypeError(`${key} must be RFC3339`);
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
const seconds = (a, b) => a && b && Number.isFinite(Date.parse(a)) && Number.isFinite(Date.parse(b)) && Date.parse(b) >= Date.parse(a) ? (Date.parse(b) - Date.parse(a)) / 1000 : null;

// llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] Job fields are the consumed-subset read boundary documented above; identity and timestamp checks protect cached evidence and do not publish a duplicate GitHub schema.
export function validateAttempt(attempt) {
  const { run, jobs } = attempt ?? {};
  validateRun(run);
  if (!Array.isArray(jobs)) throw new Error(`missing jobs for run ${run.id}`);
  for (const job of jobs) {
    if (!job || typeof job.name !== 'string' || !job.name.trim() || !ACTION_STATUSES.includes(job.status) || (job.conclusion != null && !ACTION_CONCLUSIONS.includes(job.conclusion))) throw new Error(`invalid job for run ${run.id}`);
    if (!Number.isSafeInteger(job.id) || job.id < 1 || job.run_id !== run.id || job.run_attempt !== run.run_attempt) throw new Error(`job identity mismatch for run ${run.id}/${run.run_attempt}`);
    for (const key of ['created_at', 'started_at', 'completed_at']) if (job[key] != null && !validTimestamp(job[key])) throw new Error(`invalid job ${key}`);
  }
  return attempt;
}
// llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]

export function calculateHead(attempts, required) {
  if (!attempts.length) throw new Error('missing head attempts');
  attempts.forEach(validateAttempt);
  const sorted = [...attempts].sort((a, b) => Date.parse(a.run.created_at) - Date.parse(b.run.created_at) || a.run.run_attempt - b.run.run_attempt);
  const first = sorted[0].run;
  const last = sorted.at(-1).run;
  const kind = first.event === 'push' ? 'main' : first.head_branch.startsWith('release-plz-') ? 'release-pr' : 'pr';
  const allJobs = sorted.flatMap(({ run, jobs }) => jobs.map((job) => ({ ...job, run_id: run.id, run_attempt: run.run_attempt })));
  // A later attempt replaces only contexts it supplies: successful contexts
  // survive a failed-job-only retry. Attempt number outranks timestamp order.
  const latest = new Map();
  for (const { run, jobs } of [...sorted].sort((a, b) => a.run.run_attempt - b.run.run_attempt)) {
    const merged = new Map();
    for (const job of latest.get(run.id)?.jobs ?? []) {
      if (!merged.has(job.name)) merged.set(job.name, []);
      merged.get(job.name).push(job);
    }
    const supplied = new Map();
    for (const job of jobs) {
      if (!supplied.has(job.name)) supplied.set(job.name, []);
      supplied.get(job.name).push(job);
    }
    for (const [name, results] of supplied) merged.set(name, results);
    latest.set(run.id, { run, jobs: [...merged.values()].flat() });
  }
  const finalJobs = [...latest.values()].flatMap(({ jobs }) => jobs);
  const mainJobs = [...latest.values()].filter(({ run }) => isCIWorkflow(run)).flatMap(({ jobs }) => jobs);
  const contexts = kind === 'main' ? mainJobs : required.flatMap((name) => { const matches = finalJobs.filter((job) => job.name === name); return matches.length ? matches : [undefined]; });
  let reason = null;
  if (!contexts.length || contexts.some((j) => !j || !j.completed_at)) reason = sorted.some(({ run }) => run.conclusion === 'cancelled') ? 'cancelled workflow; missing or incomplete context' : 'missing or incomplete context';
  else if (contexts.some((j) => j.conclusion === 'cancelled')) reason = 'cancelled context';
  const relevant = [...latest.values()].filter(({ run, jobs }) => kind === 'main' ? isCIWorkflow(run) : jobs.some(job => required.includes(job.name)));
  if (relevant.some(({ run }) => !ACTION_STATUSES.includes(run.status) || (run.conclusion !== null && !ACTION_CONCLUSIONS.includes(run.conclusion)))) reason = 'unknown workflow state; completion cannot be established';
  if (kind === 'main' && relevant.some(({ run }) => run.status !== 'completed')) reason = 'incomplete CI workflow';
  const spanJobs = kind === 'main' ? sorted.filter(({ run }) => isCIWorkflow(run)).flatMap(({ jobs }) => jobs) : allJobs.filter((job) => required.includes(job.name));
  const end = reason ? null : spanJobs.map((job) => job.completed_at).filter(Boolean).sort().at(-1);
  const failed = contexts.some((j) => j && !['success', 'skipped', 'neutral'].includes(j.conclusion));
  return {
    run_id: first.id, attempt: Math.max(...sorted.map(({ run }) => run.run_attempt)), event: first.event, kind,
    head_sha: first.head_sha, pr_number: first.pull_requests?.[0]?.number ?? null, created_at: first.created_at,
    conclusion: reason ? (reason.startsWith('cancelled') ? 'cancelled' : null) : failed ? 'failure' : 'success',
    gate_seconds: seconds(first.created_at, end), reason,
    // llmlint: ignore[names_match_behavior] The frozen schema-1 consumer contract requires this key; GitHub exposes no needs DAG, so the report explicitly limits it to terminal required contexts rather than inventing ancestry.
    critical_path: end ? [...new Set(spanJobs.filter((j) => j.completed_at === end).map((j) => j.name))] : [],
    jobs: allJobs.map((job) => ({ name: job.name, conclusion: job.conclusion ?? null,
      queue_seconds: seconds(job.created_at, job.started_at), run_seconds: seconds(job.started_at, job.completed_at),
      start_offset_seconds: seconds(first.created_at, job.started_at) ?? 0,
      ...(seconds(first.created_at, job.started_at) !== null ? {} : { start_offset_reason: job.started_at ? 'inconsistent start timestamp; zero is an unavailable-offset sentinel' : 'job never started; zero is an unavailable-offset sentinel' }),
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
  if (!report || !report.window || !validTimestamp(report.window.since) || !validTimestamp(report.window.until) || Date.parse(report.window.since) >= Date.parse(report.window.until)) throw new Error('invalid timing window');
  if (report.schema_version !== SCHEMA_VERSION || !Array.isArray(report.required_contexts) || !report.required_contexts.every((s) => typeof s === 'string' && s.trim()) || !Array.isArray(report.runs)) throw new Error('invalid timing report envelope');
  for (const run of report.runs) {
    if (!run || !Number.isSafeInteger(run.run_id) || run.run_id < 1 || !Number.isSafeInteger(run.attempt) || run.attempt < 1 || !['pr', 'release-pr', 'main'].includes(run.kind) || !Array.isArray(run.jobs) || !Array.isArray(run.critical_path)) throw new Error('invalid timing run');
    if (typeof run.head_sha !== 'string' || typeof run.event !== 'string' || !validTimestamp(run.created_at) || (run.pr_number !== null && (!Number.isSafeInteger(run.pr_number) || run.pr_number < 1)) || (run.conclusion !== null && typeof run.conclusion !== 'string') || !run.critical_path.every((s) => typeof s === 'string' && s.trim())) throw new Error('invalid timing run fields');
    if (run.gate_seconds === null && (typeof run.reason !== 'string' || !run.reason.trim())) throw new Error('null gate span needs a reason');
    if (run.gate_seconds !== null && (!Number.isFinite(run.gate_seconds) || run.gate_seconds < 0)) throw new Error('invalid timing gate_seconds');
    for (const job of run.jobs) {
      if (!job || typeof job.name !== 'string' || !job.name.trim() || (job.conclusion !== null && typeof job.conclusion !== 'string') || !Number.isFinite(job.start_offset_seconds) || job.start_offset_seconds < 0) throw new Error('invalid timing job fields');
      for (const key of ['queue_seconds', 'run_seconds']) if (job[key] !== null && (!Number.isFinite(job[key]) || job[key] < 0)) throw new Error(`invalid timing ${key}`);
    }
  }
  if (!isDeepStrictEqual(report.summary, summarize(report.runs))) throw new Error('summary does not reconcile');
  return report;
}

function command(program, args) {
  const env = { ...process.env };
  if (program === 'onevcs' && !env.GH_TOKEN && !env.GITHUB_TOKEN) {
    const auth = spawnSync('gh', ['auth', 'token'], { encoding: 'utf8' });
    if (auth.status === 0) env.GH_TOKEN = auth.stdout.trim();
  }
  const result = spawnSync(program, args, { env, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
  if (result.status !== 0) {
    const error = new Error(`${program} ${args.join(' ')}: ${result.stderr || result.error?.message || 'read failed'}`);
    error.code = result.error?.code;
    throw error;
  }
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
      const core = validateQuota(command('gh', ['api', 'rate_limit']));
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
  const required = requiredContexts(protection, rules);
  if (!required.length) throw new Error('missing required contexts at observation');
  writeFileSync(join(dir, `contexts-${observed_at.replaceAll(':', '-')}.json`), JSON.stringify({ observed_at, required_contexts: required, protection, rules }, null, 2));
  const runs = [];
  let complete = true;
  for (let page = 1;; page++) {
    const answer = await get(`${root}/actions/runs?per_page=100&page=${page}&created=${encodeURIComponent(`${options.since}..${options.until}`)}`);
    if (!Array.isArray(answer.workflow_runs)) throw new Error('missing workflow_runs');
    writeFileSync(join(dir, `runs-page-${page}.json`), JSON.stringify({ observed_at, response: answer }, null, 2));
    runs.push(...answer.workflow_runs.map(validateRun));
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
    validateRun(fresh);
    if (fresh.id !== run.id || fresh.head_sha !== run.head_sha) throw new Error(`run identity mismatch for ${run.id}`);
    writeFileSync(join(dir, `run-${run.id}-metadata.json`), JSON.stringify({ observed_at, run: fresh }, null, 2));
    const key = `${fresh.event}:${fresh.head_sha}`;
    if (!groups.has(key)) groups.set(key, []);
    for (let attempt = 1; attempt <= fresh.run_attempt; attempt++) {
      const file = join(dir, `run-${run.id}-attempt-${attempt}.json`);
      let raw;
      if (existsSync(file)) {
        try { raw = JSON.parse(readFileSync(file, 'utf8')); } catch (error) { throw new Error(`invalid cached attempt ${file}; remove this cache file and retry: ${error.message}`); }
      }
      else {
        let jobs;
        let useGh = attempt !== fresh.run_attempt;
        if (!useGh) {
          await guard();
          // onevcs supports latest jobs, not historical attempt selection.
          try {
            jobs = command('onevcs', ['host', 'run-jobs', '--repo', REPOSITORY, '--run', String(run.id), '--json']).jobs;
          } catch (error) {
            if (error.code !== 'ENOENT' && !/unrecognized subcommand/.test(error.message)) throw error;
            useGh = true;
          }
        }
        if (useGh) {
          jobs = [];
          for (let page = 1;; page++) {
            const response = await get(`${root}/actions/runs/${run.id}/attempts/${attempt}/jobs?per_page=100&page=${page}`);
            if (!Array.isArray(response.jobs)) throw new Error('missing jobs');
            jobs.push(...response.jobs);
            if (response.jobs.length < 100) break;
          }
        }
        if (!Array.isArray(jobs) || jobs.some((j) => !j || j.run_attempt !== attempt)) throw new Error(`missing or mismatched jobs for ${run.id}/${attempt}`);
        raw = { observed_at, required_contexts: required, run: { ...fresh, run_attempt: attempt }, jobs };
        validateAttempt(raw);
        if ((attempt < fresh.run_attempt || fresh.status === 'completed') && ACTION_CONCLUSIONS.includes(fresh.conclusion) && jobs.every((j) => j.status === 'completed')) writeFileSync(file, JSON.stringify(raw, null, 2));
      }
      if (raw?.run?.id !== fresh.id || raw?.run?.run_attempt !== attempt || raw?.run?.head_sha !== fresh.head_sha) throw new Error(`cached attempt identity mismatch: ${file}; remove this cache file and retry`);
      groups.get(key).push(validateAttempt(attempt === fresh.run_attempt ? { ...raw, run: fresh } : raw));
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

export async function main(args = process.argv.slice(2)) {
  let options;
  try { options = parseArgs(args); } catch (e) { console.error(`gate-timing: ${e.message}`); process.exitCode = 2; }
  if (options?.help) console.log(HELP);
  else if (options) try { const report = await collect(options); console.log(options.format === 'markdown' ? markdown(report) : JSON.stringify(report, null, 2)); } catch (e) { console.error(`gate-timing: ${e.message}`); process.exitCode = 1; }
}
