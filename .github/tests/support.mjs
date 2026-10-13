import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { root } from '../workflow-graph.mjs';
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
  function classify(event, head, eventName = 'pull_request', baseRef = base) {
    const path = join(dir, 'event.json'); writeFileSync(path, typeof event === 'string' ? event : JSON.stringify(event));
    const run = spawnSync(process.execPath, [resolve(root, '.github/macos-policy.mjs'), 'classify', '--event', path, '--base', baseRef, '--head', head], { cwd: dir, env: { ...process.env, GITHUB_EVENT_NAME: eventName }, encoding: 'utf8' });
    assert.equal(run.status, 0, run.stderr); return JSON.parse(run.stdout);
  }
  return { dir, base, baseFiles, heads, git, change, classify };
}
export function event(branch = 'feature/change', fork = false) {
  const repo = 'nickderobertis/crozier';
  return { action: 'synchronize', repository: { full_name: repo }, pull_request: { title: 'chore: release', user: { login: 'nickderobertis' }, head: { ref: branch, repo: { full_name: fork ? 'contributor/crozier' : repo } }, base: { ref: 'main', repo: { full_name: repo } } } };
}
