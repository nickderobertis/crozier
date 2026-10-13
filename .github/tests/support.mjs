import assert from 'node:assert/strict';
import { execFileSync, spawnSync, execFile } from 'node:child_process';
import { createServer } from 'node:http';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { root } from '../workflow-graph.mjs';
// llmlint: ignore-block[shell_test_tiers_stay_split] The task requires real Git histories and classifier subprocess journeys in node --test .github/tests/*.test.mjs. This shared fixture implements that mandated boundary proof; the manager-approved workload exception keeps it with its callers in this private recording project instead of moving it to a separate tier.
export function history(t) {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), 'macos-policy-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const git = (...args) => execFileSync('git', args, { cwd: dir, encoding: 'utf8' }).trim();
  git('init', '-q', '-b', 'main'); git('config', 'user.email', 'test@example.com'); git('config', 'user.name', 'test');
  const baseFiles = { 'Cargo.toml': '[package]\nname = "crozier"\nversion = "0.0.1"\n[dependencies]\nserde = "1"\n', 'Cargo.lock': 'version = 4\n[[package]]\nname = "crozier"\nversion = "0.0.1"\ndependencies = ["serde"]\n[[package]]\nname = "serde"\nversion = "1.0.0"\nsource = "registry+test"\nchecksum = "abc"\n', 'CHANGELOG.md': '# Changes\n', 'source.rs': 'fn main() {}\n', 'package.json': '{"name":"crozier","version":"0.0.1","dependencies":{"x":"1"}}\n', 'pyproject.toml': '[project]\nname = "crozier"\nversion = "0.0.1"\n' };
  for (const [name, contents] of Object.entries(baseFiles)) writeFileSync(join(dir, name), contents);
  function commit() { git('add', '-A'); git('commit', '-qm', 'fixture'); return git('rev-parse', 'HEAD'); }
  const base = commit();
  function change(files) { git('reset', '--hard', base); for (const [name, content] of Object.entries(files)) writeFileSync(join(dir, name), content); return commit(); }
  const heads = {
    version: change({ 'Cargo.toml': baseFiles['Cargo.toml'].replace('0.0.1','0.0.2'), 'Cargo.lock': baseFiles['Cargo.lock'].replace('0.0.1','0.0.2'), 'CHANGELOG.md': '# Changes\n\n## 0.0.2\nFixed bugs\n' }),
    source: change({ 'source.rs': 'fn main() { println!("hi"); }\n' }),
    dependency: change({ 'Cargo.toml': baseFiles['Cargo.toml'].replace('serde = "1"','serde = "2"') }),
  };
  function invoke(event, head, eventName = 'pull_request', baseRef = base, extraEnv = {}) {
    const path = join(dir, '.git/event.json'); writeFileSync(path, typeof event === 'string' ? event : JSON.stringify(event));
    return spawnSync(process.execPath, [resolve(root, '.github/macos-policy.mjs'), 'classify', '--event', path, '--base', baseRef, '--head', head], { cwd: dir, env: { ...process.env, GITHUB_EVENT_NAME: eventName, GITHUB_OUTPUT: '', ...extraEnv }, encoding: 'utf8' });
  }
  function classify(event, head, eventName = 'pull_request', baseRef = base) {
    const run=invoke(event,head,eventName,baseRef);
    assert.equal(run.status,0,run.stderr); return JSON.parse(run.stdout);
  }
  // Asynchronous, so an in-process API double can answer the subprocess.
  function lift(event, head, env = {}) {
    const path = join(dir, '.git/lift-event.json'); writeFileSync(path, JSON.stringify(event));
    return new Promise((done, fail) => execFile(process.execPath, [resolve(root, '.github/macos-policy.mjs'), 'classify', '--event', path, '--base', base, '--head', head], { cwd: dir, env: { ...process.env, GITHUB_EVENT_NAME: 'pull_request', GITHUB_OUTPUT: '', GITHUB_TOKEN: 'fixture-token', GITHUB_WORKFLOW_REF: 'nickderobertis/crozier/.github/workflows/ci.yml@refs/pull/1/merge', GITHUB_RUN_ID: '900', ...env }, encoding: 'utf8' }, (error, stdout, stderr) => error ? fail(new Error(stderr || error.message)) : done(JSON.parse(stdout))));
  }
  return { dir, base, baseFiles, heads, git, change, classify, invoke, lift };
}
// llmlint: ignore-end[shell_test_tiers_stay_split]
export function event(branch = 'feature/change', fork = false) {
  const repo = 'nickderobertis/crozier';
  return { action: 'synchronize', repository: { full_name: repo }, pull_request: { title: 'chore: release', user: { login: 'nickderobertis' }, head: { ref: branch, repo: { full_name: fork ? 'contributor/crozier' : repo } }, base: { ref: 'main', repo: { full_name: repo } } } };
}

// GitHub's REST API is the third-party boundary a draft lift reads; this double
// answers its two run/job listings from `state` and records every request.
export async function githubApi(t, state) {
  const requests = [];
  const server = createServer((request, response) => {
    requests.push({ url: request.url, authorization: request.headers.authorization });
    const url = new URL(request.url, 'http://double');
    const jobs = url.pathname.match(/^\/repos\/nickderobertis\/crozier\/actions\/runs\/(\d+)\/jobs$/);
    let body;
    if (state.status) { response.writeHead(state.status); response.end('{}'); return; }
    if (url.pathname === '/repos/nickderobertis/crozier/actions/runs') body = { workflow_runs: state.runs };
    else if (jobs) body = { jobs: state.jobs[jobs[1]] ?? [] };
    if (!body) { response.writeHead(404); response.end('{}'); return; }
    response.writeHead(200, { 'content-type': 'application/json' }); response.end(JSON.stringify(body));
  });
  await new Promise(done => server.listen(0, '127.0.0.1', done));
  t.after(() => server.close());
  return { url: `http://127.0.0.1:${server.address().port}`, requests };
}
export function liftEvent(sha, branch = 'feature/change', fork = false) {
  const pr = event(branch, fork);
  pr.action = 'ready_for_review'; pr.pull_request.head.sha = sha;
  return pr;
}
