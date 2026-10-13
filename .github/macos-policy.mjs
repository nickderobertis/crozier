#!/usr/bin/env node
// One authority for release-only omission. The PAT author is also a human;
// only same-repository release-plz heads with a semantic release diff qualify.
// A draft lift (`ready_for_review`) may instead reuse a Mac proof this same
// workflow already passed on the exact head; anything short of that proof runs Mac.
import { execFileSync } from 'node:child_process';
import { readFileSync, appendFileSync, realpathSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

// Exit 0 emits a routing decision (unreadable PRs require Mac); 1 is output IO failure; 2 is invalid invocation.
class InvocationError extends Error {}
const versionPattern = /^\d+\.\d+\.\d+(?:[-+][\w.-]+)?$/;
const repositoryPattern = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;
const refPattern = /^[A-Za-z0-9][A-Za-z0-9._/-]*$/;
const shaPattern = /^[0-9a-f]{40}$/;
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
async function api(env, path) {
  const response = await fetch(`${env.GITHUB_API_URL}${path}`, {
    headers: { Accept: 'application/vnd.github+json', Authorization: `Bearer ${env.GITHUB_TOKEN}`, 'X-GitHub-Api-Version': '2022-11-28' },
    signal: AbortSignal.timeout(20000),
  });
  if (!response.ok) throw new Error(`GitHub API ${path.split('?')[0]} answered ${response.status}`);
  return response.json();
}
// Resolves to the earlier run's URL only when this workflow's Mac job already
// succeeded on a macOS runner at exactly the lifted head and no other Mac job
// there disagrees; every other outcome is a reason to run Mac again.
export async function provenMacRun(event, env = process.env) {
  const sha = event?.pull_request?.head?.sha, repository = event?.repository?.full_name;
  if (typeof sha !== 'string' || !shaPattern.test(sha)) return { reason: 'no exact head SHA to match' };
  if (typeof repository !== 'string' || !repositoryPattern.test(repository)) return { reason: 'malformed repository.full_name' };
  if (!env.GITHUB_TOKEN || !/^https?:\/\/[^\s]+$/.test(env.GITHUB_API_URL ?? '')) return { reason: 'no GitHub API credential or URL' };
  const workflow = env.GITHUB_WORKFLOW_REF?.startsWith(`${repository}/`) ? env.GITHUB_WORKFLOW_REF.slice(repository.length + 1).split('@')[0] : '';
  if (!/^\.github\/workflows\/[\w.-]+\.ya?ml$/.test(workflow)) return { reason: 'unknown workflow path' };
  try {
    const listed = await api(env, `/repos/${repository}/actions/runs?head_sha=${sha}&event=pull_request&status=completed&per_page=100`);
    if (!Array.isArray(listed?.workflow_runs)) return { reason: 'unreadable workflow run list' };
    const runs = listed.workflow_runs.filter(run => run?.path === workflow && run.head_sha === sha && String(run.id) !== String(env.GITHUB_RUN_ID));
    const proofs = [];
    for (const run of runs) {
      if (!Number.isSafeInteger(run.id) || typeof run.html_url !== 'string') return { reason: 'unreadable workflow run' };
      const jobs = await api(env, `/repos/${repository}/actions/runs/${run.id}/jobs?filter=latest&per_page=100`);
      if (!Array.isArray(jobs?.jobs)) return { reason: `unreadable jobs of ${run.html_url}` };
      for (const job of jobs.jobs.filter(job => job?.name === macJobName)) {
        if (job.conclusion === 'skipped') continue;
        if (job.conclusion !== 'success' || job.head_sha !== sha) return { reason: `Mac job concluded ${job.conclusion ?? 'unknown'} at ${job.head_sha ?? 'unknown head'} in ${run.html_url}` };
        if (Array.isArray(job.labels) && job.labels.some(label => typeof label === 'string' && label.startsWith('macos-'))) proofs.push(run.html_url);
      }
    }
    return proofs.length ? { url: proofs[0] } : { reason: 'no completed Mac job on this head' };
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
    decision = proof.url
      ? { isReleaseOnly: false, macosRequired: false, reason: `draft lift: Mac proof reused from ${proof.url} on head ${event.pull_request.head.sha}`, reusedRun: proof.url }
      : { ...decision, reason: `${decision.reason}; draft lift: ${proof.reason}, so the Mac job runs` };
  }
  if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `macosRequired=${decision.macosRequired}\nmacosReusedRun=${decision.reusedRun ?? ''}\n`);
  console.log(JSON.stringify(decision));
}
if (process.argv[1] && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(error => { console.error(error.message); process.exitCode = error instanceof InvocationError ? 2 : 1; });
}
