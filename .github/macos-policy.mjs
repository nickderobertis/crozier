#!/usr/bin/env node
// One authority for release-only omission. The PAT author is also a human;
// only same-repository release-plz heads with a semantic release diff qualify.
// A draft lift (`ready_for_review`) reuses a Mac proof this same workflow
// already passed on the exact head. It requests a Mac runner only when no
// earlier run of the pull request requested one at all; otherwise its Mac
// check fails on Linux with the reason (.github/AGENTS.md names the recovery).
import { execFileSync } from 'node:child_process';
import { readFileSync, appendFileSync, realpathSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

// Exit 0 emits a routing decision (unreadable PRs require Mac); 1 is output IO failure; 2 is invalid invocation.
class InvocationError extends Error {}
const versionPattern = /^\d+\.\d+\.\d+(?:[-+][\w.-]+)?$/;
const repositoryPattern = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;
const refPattern = /^[A-Za-z0-9][A-Za-z0-9._/-]*$/;
const shaPattern = /^[0-9a-f]{40}$/;
// A run reference is written into line-oriented GITHUB_OUTPUT and named by the gate.
export const runUrlPattern = /^https:\/\/[^\s/]+\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/actions\/runs\/\d+$/;
// The display name of ci.yml's Mac job; a renamed job proves nothing.
export const macJobName = 'macOS check, SDK environment and install';
function git(...args) {
  return execFileSync('git', args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
}
function commit(ref) {
  if (!refPattern.test(ref ?? '') || ref.includes('..')) throw new Error('unusable git ref');
  return git('rev-parse', '--verify', '--end-of-options', `${ref}^{commit}`).trim();
}
function parsedToml(text) {
  return JSON.parse(execFileSync('python3', ['-c', 'import sys,json,tomllib; print(json.dumps(tomllib.loads(sys.stdin.read())))'], { input: text, encoding: 'utf8' }));
}
function withoutVersion(path, text) {
  const parsed = path.endsWith('.json') ? JSON.parse(text) : parsedToml(text);
  if (path === 'Cargo.lock') {
    const own = parsed.package?.filter(p => p.name === 'crozier' && !p.source);
    if (own?.length !== 1 || typeof own[0].version !== 'string' || !versionPattern.test(own[0].version)) throw new Error('missing root lock package');
    delete own[0].version;
  } else {
    const owner = path === 'Cargo.toml' ? parsed.package : path === 'pyproject.toml' ? parsed.project : parsed;
    if (typeof owner?.version !== 'string' || !versionPattern.test(owner.version)) throw new Error('missing literal version');
    delete owner.version;
  }
  return parsed;
}
function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(k => [k, stable(value[k])]));
  return value;
}
export function classify(event, base, head, eventName = process.env.GITHUB_EVENT_NAME ?? 'pull_request') {
  const ordinary = reason => ({ isReleaseOnly: false, macosRequired: true, reason });
  if (!['pull_request','push','release','workflow_run','repository_dispatch','schedule','workflow_dispatch'].includes(eventName)) return ordinary(`unknown event name '${eventName || '(empty)'}': Mac coverage required`);
  if (eventName !== 'pull_request') return { isReleaseOnly: false, macosRequired: false, reason: `automatic ${eventName}: no Mac lane` };
  try {
    const pr = event.pull_request, repository = event.repository?.full_name;
    for (const [field, value] of [
      ['repository.full_name', repository],
      ['pull_request.head.repo.full_name', pr?.head?.repo?.full_name],
      ['pull_request.base.repo.full_name', pr?.base?.repo?.full_name],
    ]) if (typeof value !== 'string' || !repositoryPattern.test(value)) return ordinary(`malformed ${field}: expected repository name`);
    if (typeof pr?.head?.ref !== 'string') return ordinary('malformed pull_request.head.ref: expected branch name');
    if (pr.head.repo.full_name !== repository || pr.base.repo.full_name !== repository || !/^release-plz-[A-Za-z0-9._-]+$/.test(pr.head.ref)) return ordinary('ordinary or unknown PR ownership/branch');
    const from = commit(base), to = commit(head);
    const paths = git('diff', '--name-status', '--no-renames', '-z', from, to).split('\0');
    if (paths.at(-1) === '') paths.pop();
    if (!paths.length) return ordinary('empty diff does not prove a release');
    for (let i = 0; i < paths.length; i += 2) {
      const status = paths[i], path = paths[i + 1];
      if (status !== 'M') return ordinary(`non-release file operation: ${status} ${path}`);
      if (path === 'CHANGELOG.md') continue;
      if (!['Cargo.toml', 'Cargo.lock', 'pyproject.toml', 'package.json'].includes(path)) return ordinary(`non-release file: ${path}`);
      const before = withoutVersion(path, git('show', `${from}:${path}`));
      const after = withoutVersion(path, git('show', `${to}:${path}`));
      if (JSON.stringify(stable(before)) !== JSON.stringify(stable(after))) return ordinary(`non-version content changed: ${path}`);
    }
    return { isReleaseOnly: true, macosRequired: false, reason: 'same-repository release-plz branch; semantic version/changelog-only diff' };
  } catch (error) {
    return ordinary(`unreadable release classification: ${error.message}`);
  }
}
// A listing proves completeness only when it reports a valid total that its
// single page holds in full, and every entry carries the fields the decision
// reads; anything else could hide a Mac request or a failed Mac job.
function incomplete(listing, key, what, readable) {
  const total = listing?.total_count, page = listing?.[key];
  if (!Array.isArray(page)) return `unreadable ${what}`;
  if (!Number.isSafeInteger(total) || total < 0) return `unverifiable ${what}: total_count ${JSON.stringify(total) ?? 'missing'}`;
  if (total !== page.length) return `ambiguous ${what}: total_count ${total} but ${page.length} returned`;
  const unreadable = page.findIndex(entry => !(entry && typeof entry === 'object' && readable(entry)));
  return unreadable < 0 ? '' : `unreadable ${what} entry ${unreadable}`;
}
const readableRun = run => Number.isSafeInteger(run.id) && typeof run.path === 'string' && typeof run.head_repository?.full_name === 'string'
  && typeof run.head_sha === 'string' && typeof run.status === 'string' && typeof run.html_url === 'string' && runUrlPattern.test(run.html_url);
// Only a Mac-named job's conclusion, head and labels decide anything.
const readableJob = job => typeof job.name === 'string' && (job.name !== macJobName
  || ((typeof job.conclusion === 'string' || job.conclusion === null) && typeof job.head_sha === 'string' && Array.isArray(job.labels) && job.labels.every(label => typeof label === 'string')));
async function api(env, path) {
  const response = await fetch(`${env.GITHUB_API_URL}${path}`, {
    headers: { Accept: 'application/vnd.github+json', Authorization: `Bearer ${env.GITHUB_TOKEN}`, 'X-GitHub-Api-Version': '2022-11-28' },
    signal: AbortSignal.timeout(20000),
  });
  if (!response.ok) throw new Error(`GitHub API ${path.split('?')[0]} answered ${response.status}`);
  return response.json();
}
// A Mac-named job requested a Mac runner unless it was skipped or its labels
// show it ran on Linux (an earlier lift's reuse or refusal lane).
function requestedMac(job) {
  if (job.conclusion === 'skipped') return false;
  return !(Array.isArray(job.labels) && job.labels.length && job.labels.every(label => typeof label === 'string' && !label.startsWith('macos-')));
}
// Resolves to the earlier run's URL only when this workflow's Mac job already
// succeeded on a macOS runner at exactly the lifted head and no other Mac job
// there disagrees; to `fallback` only when every earlier run of this pull
// request was read and none requested a Mac runner; every other outcome is the
// reason the lift's Mac check fails.
export async function provenMacRun(event, env = process.env) {
  const sha = event?.pull_request?.head?.sha, repository = event?.repository?.full_name;
  const branch = event?.pull_request?.head?.ref, headRepository = event?.pull_request?.head?.repo?.full_name;
  if (typeof sha !== 'string' || !shaPattern.test(sha)) return { reason: 'no exact head SHA to match' };
  if (typeof repository !== 'string' || !repositoryPattern.test(repository)) return { reason: 'malformed repository.full_name' };
  if (typeof branch !== 'string' || !refPattern.test(branch) || typeof headRepository !== 'string' || !repositoryPattern.test(headRepository)) return { reason: 'malformed pull_request head branch or repository' };
  if (!env.GITHUB_TOKEN || !/^https?:\/\/[^\s]+$/.test(env.GITHUB_API_URL ?? '')) return { reason: 'no GitHub API credential or URL' };
  const workflow = env.GITHUB_WORKFLOW_REF?.startsWith(`${repository}/`) ? env.GITHUB_WORKFLOW_REF.slice(repository.length + 1).split('@')[0] : '';
  if (!/^\.github\/workflows\/[\w.-]+\.ya?ml$/.test(workflow)) return { reason: 'unknown workflow path' };
  try {
    // Every earlier run of this workflow for the pull request's head branch, at
    // any head: the exact head supplies the proof, and all of them decide
    // whether the pull request has spent a Mac runner yet.
    const listed = await api(env, `/repos/${repository}/actions/runs?branch=${encodeURIComponent(branch)}&event=pull_request&per_page=100`);
    const unlisted = incomplete(listed, 'workflow_runs', 'workflow run list', readableRun);
    if (unlisted) return { reason: unlisted };
    const runs = listed.workflow_runs.filter(run => run.path === workflow && run.head_repository.full_name === headRepository && String(run.id) !== String(env.GITHUB_RUN_ID));
    const proofs = [];
    let requested = false;
    for (const run of runs) {
      const same = run.head_sha === sha;
      const pending = run.status !== 'completed' && `Mac proof still ${run.status.replace(/\W/g, '')} in ${run.html_url}`;
      // An unfinished run may still request a Mac runner, so it never permits the fallback.
      if (pending) { if (same) return { reason: pending }; requested = true; }
      const jobs = await api(env, `/repos/${repository}/actions/runs/${run.id}/jobs?filter=latest&per_page=100`);
      const unread = incomplete(jobs, 'jobs', `jobs of ${run.html_url}`, readableJob);
      if (unread) return { reason: unread };
      for (const job of jobs.jobs.filter(job => job.name === macJobName)) {
        if (!requestedMac(job)) continue;
        requested = true;
        if (!same) continue;
        if (job.conclusion !== 'success' || job.head_sha !== sha) return { reason: `Mac job concluded ${job.conclusion ?? 'unknown'} at ${job.head_sha ?? 'unknown head'} in ${run.html_url}` };
        if (Array.isArray(job.labels) && job.labels.some(label => typeof label === 'string' && label.startsWith('macos-'))) proofs.push(run.html_url);
      }
    }
    if (proofs.length) return { url: proofs[0] };
    return requested ? { reason: 'no completed Mac job on this head' } : { fallback: true, reason: 'no earlier run of this pull request requested a Mac job' };
  } catch (error) {
    return { reason: `unreadable Mac proof: ${error.message}` };
  }
}
async function main() {
  const args = process.argv.slice(2);
  if (args[0] !== 'classify' || args.length !== 7 || args[1] !== '--event' || args[3] !== '--base' || args[5] !== '--head') throw new InvocationError('usage: node .github/macos-policy.mjs classify --event JSON --base REF --head REF');
  let decision, event;
  try { event = JSON.parse(readFileSync(args[2], 'utf8')); decision = classify(event, args[4], args[6]); }
  catch (error) { decision = classify({}, args[4], args[6]); decision.reason += `; unreadable event: ${error.message}`; }
  if (decision.macosRequired && (process.env.GITHUB_EVENT_NAME ?? 'pull_request') === 'pull_request' && event?.action === 'ready_for_review') {
    const proof = await provenMacRun(event);
    // One line, so it can travel through GITHUB_OUTPUT to the failing check.
    const refusal = `draft lift has no Mac proof on head ${event.pull_request?.head?.sha}: ${proof.reason}`.replace(/\s+/g, ' ');
    decision = proof.url
      ? { isReleaseOnly: false, macosRequired: false, reason: `draft lift: Mac proof reused from ${proof.url} on head ${event.pull_request.head.sha}`, reusedRun: proof.url }
      : proof.fallback
      ? { isReleaseOnly: false, macosRequired: true, reason: `${decision.reason}; draft lift: ${proof.reason}, so this run requests the Mac job` }
      : { isReleaseOnly: false, macosRequired: false, reason: `${decision.reason}; ${refusal}; no Mac runner is requested and the Mac check fails`, liftRefusal: refusal };
  }
  if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `macosRequired=${decision.macosRequired}\nmacosReusedRun=${decision.reusedRun ?? ''}\nmacosLiftRefusal=${decision.liftRefusal ?? ''}\n`);
  console.log(JSON.stringify(decision));
}
if (process.argv[1] && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(error => { console.error(error.message); process.exitCode = error instanceof InvocationError ? 2 : 1; });
}
