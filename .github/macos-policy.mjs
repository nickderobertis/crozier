#!/usr/bin/env node
// One authority for release-only omission. The PAT author is also a human;
// only same-repository release-plz heads with a semantic release diff qualify.
import { execFileSync } from 'node:child_process';
import { readFileSync, appendFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

const refPattern = /^[A-Za-z0-9][A-Za-z0-9._/-]*$/;
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
    if (own?.length !== 1 || typeof own[0].version !== 'string') throw new Error('missing root lock package');
    delete own[0].version;
  } else {
    const owner = path === 'Cargo.toml' ? parsed.package : path === 'pyproject.toml' ? parsed.project : parsed;
    if (typeof owner?.version !== 'string' || !/^\d+\.\d+\.\d+(?:[-+][\w.-]+)?$/.test(owner.version)) throw new Error('missing literal version');
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
  if (eventName !== 'pull_request') return { isReleaseOnly: false, macosRequired: false, reason: `automatic ${eventName}: no Mac lane` };
  try {
    const pr = event.pull_request;
    if (!pr || !event.repository?.full_name || pr.head?.repo?.full_name !== event.repository.full_name || pr.base?.repo?.full_name !== event.repository.full_name || !/^release-plz-[A-Za-z0-9._-]+$/.test(pr.head?.ref ?? '')) return ordinary('ordinary or unknown PR ownership/branch');
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
function main() {
  const args = process.argv.slice(2);
  if (args[0] !== 'classify' || args.length !== 7 || args[1] !== '--event' || args[3] !== '--base' || args[5] !== '--head') throw new Error('usage: node .github/macos-policy.mjs classify --event JSON --base REF --head REF');
  const eventName=process.env.GITHUB_EVENT_NAME ?? 'pull_request';
  if (!['pull_request','push','release','workflow_run','repository_dispatch','schedule','workflow_dispatch'].includes(eventName)) throw new Error(`unknown event name '${eventName}'; supply the actual GitHub event before routing`);
  let decision;
  try { decision = classify(JSON.parse(readFileSync(args[2], 'utf8')), args[4], args[6]); }
  catch (error) { decision = classify({}, args[4], args[6]); decision.reason = `unreadable event: ${error.message}`; }
  if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `macosRequired=${decision.macosRequired}\n`);
  console.log(JSON.stringify(decision));
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 2; }
}
