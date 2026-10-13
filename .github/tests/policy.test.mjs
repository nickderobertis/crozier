import assert from 'node:assert/strict';
import { test } from 'node:test';
import { history, event } from './support.mjs';

test('real git histories admit only release-plz semantic versions/changelog; ownership, title and author cannot forge omission', t => {
  const h = history(t);
  for (const login of ['nickderobertis', 'github-actions[bot]', 'stranger']) {
    const release = event('release-plz-2026-10-12'); release.pull_request.user.login = login;
    assert.equal(h.classify(release, h.heads.version).isReleaseOnly, true);
    for (const head of [h.heads.source, h.heads.dependency, h.base, 'missing']) assert.equal(h.classify(release, head).macosRequired, true);
  }
  for (const pr of [event(), event('release-plz-2026-10-12', true), {}, { pull_request: {} }]) {
    assert.equal(h.classify(pr, h.heads.version).macosRequired, true);
  }
  assert.equal(h.classify('{broken', h.heads.version).macosRequired, true);
  assert.equal(h.classify(event('release-plz-2026-10-12'), h.heads.version, 'pull_request', '--bad').macosRequired, true);
  for (const name of ['push','release','workflow_run','schedule','repository_dispatch','workflow_dispatch']) {
    assert.equal(h.classify('{broken', 'missing', name).macosRequired, false);
  }
});

test('semantic manifests/lockfiles preserve every non-version field and fail closed on malformed content', t => {
  const h = history(t), release = event('release-plz-test');
  for (const path of ['Cargo.toml', 'Cargo.lock', 'package.json', 'pyproject.toml']) {
    const version = h.baseFiles[path].replace('0.0.1','0.0.2');
    const head = h.change({ [path]: version });
    assert.equal(h.classify(release, head).isReleaseOnly, true, path);
    for (const content of ['{malformed', version.replace('crozier','forged'), version.replace('serde','different').replace('"x"','"y"').replace('name = "crozier"','name = "different"')]) {
      if (content === version) continue;
      const bad = h.change({ [path]: content });
      assert.equal(h.classify(release, bad).macosRequired, true, path);
    }
  }
  const mixed = h.change({ 'Cargo.toml': h.baseFiles['Cargo.toml'].replace('0.0.1','0.0.2'), 'source.rs': 'changed\n' });
  assert.equal(h.classify(release, mixed).macosRequired, true);
  const lock = h.change({ 'Cargo.lock': h.baseFiles['Cargo.lock'].replace('1.0.0','2.0.0') });
  assert.equal(h.classify(release, lock).macosRequired, true);
});
