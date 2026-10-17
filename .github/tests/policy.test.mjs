// llmlint: ignore-file[shell_test_tiers_stay_split] This entire file is the task-mandated real-Git classifier journey inside node --test .github/tests/*.test.mjs; the manager approved keeping the recorder and shared classifier proofs in this one private project rather than moving them to a sibling tier.
import assert from 'node:assert/strict';
import { readFileSync, writeFileSync, symlinkSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { test } from 'node:test';
import { spawnSync } from 'node:child_process';
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


test('real routing persists its decision; unknown/empty event names emit no omission, and release file operations are refused', t => {
  const h=history(t), pr=event('release-plz-test'), output=join(h.dir,'.git/output');
  for (const [head,required] of [[h.heads.version,false],[h.heads.source,true]]) {
    writeFileSync(output,'');
    const run=h.invoke(pr,head,'pull_request',h.base,{GITHUB_OUTPUT:output});
    assert.equal(run.status,0,run.stderr); assert.equal(readFileSync(output,'utf8'),`macosRequired=${required}\n`);
  }
  for (const name of ['', 'unknown-event']) {
    writeFileSync(output,'');
    const run=h.invoke(pr,h.heads.version,name,h.base,{GITHUB_OUTPUT:output});
    assert.equal(run.status,0,run.stderr);
    const decision=JSON.parse(run.stdout);
    assert.equal(decision.macosRequired,true); assert.equal(decision.isReleaseOnly,false);
    assert.ok(decision.reason.includes(name || '(empty)'));
    assert.equal(readFileSync(output,'utf8'),'macosRequired=true\n');
    const malformed=h.classify('{broken',h.heads.version,name);
    assert.equal(malformed.macosRequired,true);
    assert.ok(malformed.reason.includes(name || '(empty)'));
  }
  const added=h.change({'NEW_CHANGELOG.md':'release notes\n'});
  assert.match(h.classify(pr,added).reason,/non-release file operation/);
  h.git('reset','--hard',h.base); h.git('rm','CHANGELOG.md'); h.git('commit','-qm','deleted release notes');
  assert.match(h.classify(pr,h.git('rev-parse','HEAD')).reason,/non-release file operation/);
  h.git('reset','--hard',h.base); h.git('mv','CHANGELOG.md','NEW_CHANGELOG.md'); h.git('commit','-qm','renamed release notes');
  assert.equal(h.classify(pr,h.git('rev-parse','HEAD')).macosRequired,true);
});


test('a same-named registry dependency version cannot authorize release-only omission', t => {
  const h=history(t), pr=event('release-plz-test');
  const registry='\n[[package]]\nname = "crozier"\nversion = "1.0.0"\nsource = "registry+test"\nchecksum = "abc"\n';
  const base=h.change({'Cargo.lock':h.baseFiles['Cargo.lock']+registry});
  const head=h.change({'Cargo.lock':h.baseFiles['Cargo.lock']+registry.replace('1.0.0','2.0.0')});
  const decision=h.classify(pr,head,'pull_request',base);
  assert.equal(decision.macosRequired,true);
  assert.equal(decision.isReleaseOnly,false);
  assert.match(decision.reason,/non-version content changed: Cargo.lock/);
});


test('classifier runs through a filesystem alias as on macOS temporary directories', t => {
  const h=history(t), alias=join(h.dir,'.git/classifier-directory'), input=join(h.dir,'.git/event.json');
  symlinkSync(resolve('.github'),alias,'junction');
  writeFileSync(input,JSON.stringify(event('release-plz-test')));
  const run=spawnSync(process.execPath,[join(alias,'macos-policy.mjs'),'classify','--event',input,'--base',h.base,'--head',h.heads.source],{cwd:h.dir,encoding:'utf8',env:{...process.env,GITHUB_EVENT_NAME:'pull_request',GITHUB_OUTPUT:''}});
  assert.equal(run.status,0,run.stderr);
  assert.equal(JSON.parse(run.stdout).macosRequired,true);
});


test('malformed root lockfile versions require Mac coverage and valid versions recover', t => {
  const h = history(t), pr = event('release-plz-test');
  for (const version of ['', 'invalid', '1.2']) {
    const head = h.change({ 'Cargo.lock': h.baseFiles['Cargo.lock'].replace('0.0.1', version) });
    const decision = h.classify(pr, head);
    assert.equal(decision.macosRequired, true, version);
    assert.equal(decision.isReleaseOnly, false, version);
    assert.match(decision.reason, /unreadable release classification/);
  }
  assert.equal(h.classify(pr, h.heads.version).isReleaseOnly, true);
});

test('classifier distinguishes invalid invocation from output transport failure', t => {
  const h = history(t);
  const invalid = spawnSync(process.execPath, [resolve('.github/macos-policy.mjs')], { encoding: 'utf8' });
  assert.equal(invalid.status, 2);
  assert.match(invalid.stderr, /usage:/);
  const failed = h.invoke(event(), h.heads.source, 'pull_request', h.base, { GITHUB_OUTPUT: h.dir });
  assert.equal(failed.status, 1);
  assert.equal(failed.stdout, '');
  assert.match(failed.stderr, /EISDIR/);
  assert.equal(h.invoke(event(), h.heads.source).status, 0);
});


test('structured malformed ownership and branch values cannot authorize Mac omission', t => {
  const h = history(t);
  for (const fullName of [true, 42, 'invalid-repository']) {
    const pr = event('release-plz-test');
    pr.repository.full_name = fullName;
    pr.pull_request.head.repo.full_name = fullName;
    pr.pull_request.base.repo.full_name = fullName;
    const decision=h.classify(pr, h.heads.version);
    assert.equal(decision.macosRequired, true);
    assert.match(decision.reason,/repository.full_name/);
  }
  const pr = event('release-plz-test');
  pr.pull_request.head.ref = ['release-plz-test'];
  const decision=h.classify(pr, h.heads.version);
  assert.equal(decision.macosRequired, true);
  assert.match(decision.reason,/pull_request.head.ref/);
  assert.equal(h.classify(event('release-plz-test'), h.heads.version).isReleaseOnly, true);
});

