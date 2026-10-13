import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { root, workflows } from '../workflow-graph.mjs';
const contract=JSON.parse(readFileSync(resolve(root,'.github/tests/release-contract.json'),'utf8'));

test('release retains every platform/artifact; Darwin proof precedes publication and all publisher jobs use Linux', () => {
  const jobs=workflows().find(w=>w.path.endsWith('/release.yml')).value.jobs;
  const archiveTargets=jobs.upload.strategy.matrix.include.map(r=>r.target);
  const wheelTargets=jobs['build-wheels'].strategy.matrix.include.map(r=>r.target);
  const darwin=jobs.darwin.env.DARWIN_TARGETS.split(' ');
  assert.deepEqual([...archiveTargets,...darwin].sort(),contract.platforms.map(p=>p.target).sort());
  assert.deepEqual([...wheelTargets,...darwin].sort(),contract.platforms.map(p=>p.target).sort());
  assert.equal(jobs.darwin['runs-on'],'macos-latest'); assert.equal(jobs.darwin.strategy,undefined);
  const build=jobs.darwin.steps.find(s=>s.name==='Build and install both staged products');
  assert.match(build.run,/for target in \$DARWIN_TARGETS/);
  assert.match(build.run,/python3 scripts\/release-native.py --target "\$target" --tag "\$GITHUB_REF_NAME" --out/);
  assert.ok(jobs.darwin.steps.some(s=>s.run==='softwareupdate --install-rosetta --agree-to-license'));
  const helper=readFileSync(resolve(root,'scripts/release-native.py'),'utf8');
  for (const command of ['maturin', 'scripts/install.sh', 'scripts/smoke.sh', 'pip']) assert.ok(helper.includes(command));
  for (const id of ['publish-darwin','publish-pypi','publish-crate','major-tag']) {
    assert.equal(jobs[id]['runs-on'],'ubuntu-latest');
    assert.ok(jobs[id].needs.includes(id==='publish-pypi' ? 'publish-darwin' : 'darwin'),id);
  }
  assert.ok(jobs.upload.needs.includes('darwin'));
  assert.equal(jobs['publish-darwin'].steps.find(s=>s.uses?.startsWith('actions/download-artifact')).with.name, jobs.darwin.steps.find(s=>s.uses?.startsWith('actions/upload-artifact')).with.name);
  assert.ok(jobs['publish-pypi'].steps.some(s=>s.uses?.startsWith('actions/download-artifact') && s.with.pattern==='wheels-*'));
  assert.equal(jobs['verify-install-script'].strategy.matrix.os.includes('macos-latest'),false);
  assert.ok(jobs['verify-install-script'].steps.some(s=>s.run?.includes('./scripts/smoke.sh')));
  assert.ok(jobs['verify-pypi'].steps.some(s=>s.run?.includes('./scripts/smoke.sh')));
  assert.ok(jobs['verify-crate'].steps.some(s=>s.run?.includes('./scripts/smoke.sh')));
});

test('Mac PR lane retains every previous Mac check sequentially and ordinary Linux/Windows scopes remain unchanged', () => {
  const jobs=workflows().find(w=>w.path.endsWith('/ci.yml')).value.jobs;
  const runs=jobs.macos.steps.filter(s=>s.run).map(s=>s.run);
  const required=['just bootstrap','just ci-check --exclude=tag:tier:promoted','just ci-check --projects=sdk-env,runtime','cargo install --path . --locked','crozier --version'];
  let position=-1;
  for (const command of required) { const next=runs.indexOf(command); assert.ok(next>position,command); position=next; }
  assert.equal(jobs.macos.strategy,undefined);
  assert.equal(jobs.check.steps.find(s=>s.name==='Check').run,"just ci-check --exclude=tag:tier:promoted${{ runner.os == 'Windows' && ',python-workspace' || '' }}");
  assert.equal(jobs['sdk-env'].steps.find(s=>s.name==='SDK Python-environment tier').run,'just ci-check --projects=sdk-env,runtime');
  assert.ok(jobs.install.steps.some(s=>s.run==='cargo install --path . --locked'));
  assert.equal(jobs.package.steps.find(s=>s.name==='Verify the published crate tarball builds').run,'cargo publish --dry-run --locked');
});
