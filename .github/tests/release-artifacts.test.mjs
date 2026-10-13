// llmlint: ignore-file[shell_test_tiers_stay_split] Cheap artifact-contract subprocess journeys belong to the fixed .github/tests/*.test.mjs workload; native compilation/install stays behind release-packaging:test. Separating these source-contract checks from the native target keeps workflow changes from invoking expensive packaging.
// Non-native products are packed and inspected, never executed on Linux.
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync, cpSync, chmodSync, readdirSync, globSync, symlinkSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, relative, dirname } from 'node:path';
import { test } from 'node:test';
import { createHash } from 'node:crypto';
import { parse } from 'yaml';
import { expression } from '../workflow-graph.mjs';

function run(args,env={},cwd=undefined) { return spawnSync(args[0],args.slice(1),{encoding:'utf8',cwd,env:{...process.env,...env}}); }
function scratch(t) { const root=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'crozier-artifact-')); t.after(()=>rmSync(root,{recursive:true,force:true})); return root; }
const version=/^version = "([^"]+)"/m.exec(readFileSync('Cargo.toml','utf8'))[1];
function wheel(output,target,kind='valid') {
  const dir=join(output,`wheels-${target}`); mkdirSync(dir,{recursive:true});
  const isMac=target.endsWith('apple-darwin');
  const platform=target.startsWith('aarch64')?(isMac?'arm64':'aarch64'):'x86_64';
  const osTag=isMac?'macosx_11_0':'manylinux_2_34';
  const path=join(dir,`${kind==='filename-name'?'wrong':'crozier'}-${kind==='filename-version'?'999':version}-${kind==='filename-python'?'cp999':'py3'}-${kind==='filename-abi'?'wrong':'none'}-${kind==='wheel-os'?'windows':osTag}_${kind==='wheel-arch'?'wrong':platform}.whl`);
  const made=run(['python3','-c',`import sys,zipfile,struct
p,v,target,kind=sys.argv[1:]
b=(bytes.fromhex('cffaedfe')+struct.pack('<I',0x0100000c if target.startswith('aarch64') else 0x01000007) if target.endswith('apple-darwin') else bytes.fromhex('7f454c46')+bytes(14)+struct.pack('<H',183 if target.startswith('aarch64') else 62))+b'contract-fixture'
with zipfile.ZipFile(p,'w') as z:
 if kind!='executable': z.writestr('crozier-'+v+'.data/scripts/crozier',b if kind not in ('binary-arch','cpu') else b'wrong' if kind=='binary-arch' else (b[:4]+struct.pack('<I',0x0100000c)+b[8:] if target.endswith('apple-darwin') else b[:18]+struct.pack('<H',183)+b[20:]))
 if kind=='duplicate-executable': z.writestr('other.data/scripts/crozier',b)
 if kind=='duplicate-metadata': z.writestr('other.dist-info/METADATA','Name: crozier\\nVersion: '+v+'\\n')
 if kind!='metadata': z.writestr('crozier-'+v+'.dist-info/METADATA','Name: '+('other' if kind=='name' else 'crozier')+'\\nVersion: '+('999' if kind=='version' else v)+'\\n')
`,path,version,target,kind]); assert.equal(made.status,0,made.stderr); return path;
}
function pack(output,target) { return run(['python3','tools/release-packaging/release-native.py','--pack-only','--out',output,'--target',target,'--tag',`v${version}`]); }

test('real packer validates both Darwin architectures and refuses malformed/ambiguous wheels', t=>{
  for (const target of ['x86_64-apple-darwin','aarch64-apple-darwin']) {
    const output=scratch(t); wheel(output,target);
    const previous=join(output,`stage-${target}`); mkdirSync(previous); writeFileSync(join(previous,'stale.txt'),'old unshipped content');
    const built=pack(output,target); assert.equal(built.status,0,built.stderr);
    const contract=JSON.parse(readFileSync(join(output,`contract-${target}.json`),'utf8'));
    assert.equal(contract.target,target); assert.equal(contract.binarySha256,contract.archiveBinarySha256); assert.equal(contract.binarySha256,contract.wheelBinarySha256);
    const hashes=run(['python3','-c',`import tarfile,zipfile,hashlib,json,sys
with tarfile.open(sys.argv[1]) as archive: a=archive.extractfile('crozier').read()
with zipfile.ZipFile(sys.argv[2]) as wheel: w=wheel.read(next(n for n in wheel.namelist() if n.endswith('.data/scripts/crozier')))
print(json.dumps({'archive':hashlib.sha256(a).hexdigest(),'wheel':hashlib.sha256(w).hexdigest(),'same':a==w}))`,contract.archive,contract.wheel]);
    assert.equal(hashes.status,0,hashes.stderr);
    const actual=JSON.parse(hashes.stdout);
    assert.equal(actual.same,true); assert.equal(contract.binarySha256,actual.archive);
    assert.equal(contract.archiveBinarySha256,actual.archive); assert.equal(contract.wheelBinarySha256,actual.wheel);
    const contents=run(['python3','-c','import tarfile,json,sys; a=tarfile.open(sys.argv[1]); print(json.dumps(sorted(a.getnames())))',contract.archive]);
    assert.equal(contents.status,0,contents.stderr);
    const golden=JSON.parse(readFileSync('.github/tests/release-contract.json','utf8'));
    assert.deepEqual(JSON.parse(contents.stdout),[...golden.archiveContents].sort());
    assert.equal(contract.archive.split('/').at(-1),golden.platforms.find(p=>p.target===target).archive.replace('<tag>',`v${version}`));
  }
  for (const target of ['x86_64-apple-darwin','x86_64-unknown-linux-gnu']) for (const kind of ['executable','metadata','version','wheel-arch','binary-arch','cpu','wheel-os','name','duplicate-executable','duplicate-metadata','corrupt','filename-name','filename-version','filename-python','filename-abi','ambiguous']) {
    const output=scratch(t); const path=wheel(output,target,kind);
    if(kind==='corrupt') writeFileSync(path,'invalid zip bytes');
    if(kind==='ambiguous') cpSync(path,join(output,`wheels-${target}`,'duplicate.whl'));
    const refused=pack(output,target); assert.equal(refused.status,1,kind); assert.match(refused.stderr,/rebuild|clean|not a zip file/); assert.doesNotMatch(refused.stderr,/Traceback/);
  }
});

test('production Linux handoff uploads staged Darwin archives/checksums/bundles and carries wheels; missing products or transport failure refuse', t=>{
  const output=scratch(t), bin=join(output,'bin'); mkdirSync(bin);
  for(const target of ['x86_64-apple-darwin','aarch64-apple-darwin']) { wheel(output,target); const built=pack(output,target); assert.equal(built.status,0,built.stderr); }
  const calls=join(output,'calls.json'), fake=join(bin,'gh');
  writeFileSync(fake,`#!/usr/bin/env python3\nimport sys,json,os\njson.dump(sys.argv[1:],open(os.environ['GH_CALLS'],'w'))\nraise SystemExit(int(os.environ.get('GH_FAILURE','0')))\n`); chmodSync(fake,0o755);
  const intel=join(output,'intel.json'), arm=join(output,'arm.json'); writeFileSync(intel,'signed-intel-boundary'); writeFileSync(arm,'signed-arm-boundary');
  const env={PATH:`${bin}:${process.env.PATH}`,GITHUB_REPOSITORY:'nickderobertis/crozier',GH_CALLS:calls};
  const args=['bash','tools/release-packaging/publish-darwin.sh',output,`v${version}`,intel,arm];
  const published=run(args,env); assert.equal(published.status,0,published.stderr);
  const argv=JSON.parse(readFileSync(calls,'utf8')); assert.deepEqual(argv.slice(0,5),['release','upload',`v${version}`,'--repo','nickderobertis/crozier']);
  assert.equal(argv.at(-1),'--clobber');
  const golden=JSON.parse(readFileSync('.github/tests/release-contract.json','utf8'));
  for(const target of ['x86_64-apple-darwin','aarch64-apple-darwin']) {
    const expected=golden.platforms.find(p=>p.target===target);
    for(const kind of ['archive','checksum','attestation']) assert.ok(argv.includes(join(output,`v${version}`,expected[kind].replace('<tag>',`v${version}`))));
    assert.equal(readdirSync(join(output,`wheels-${target}`)).filter(n=>n.endsWith('.whl')).length,1);
  }
  assert.equal(readFileSync(join(output,`v${version}`,`crozier-v${version}-x86_64-apple-darwin.sigstore.json`),'utf8'),'signed-intel-boundary');
  const invalidTag=[...args]; invalidTag[3]='v1.2.3/escape'; const invalid=run(invalidTag,env); assert.equal(invalid.status,1); assert.match(invalid.stderr,/unsupported release tag/);
  for(const index of [4,5]) { const missingBundle=[...args]; missingBundle[index]=join(output,'missing-bundle.json'); const refused=run(missingBundle,env); assert.equal(refused.status,1); assert.match(refused.stderr,/rerun the Linux attestation steps/); }
  const missingRepo=run(args,{...env,GITHUB_REPOSITORY:''}); assert.equal(missingRepo.status,1); assert.match(missingRepo.stderr,/set it to owner\/repository/);
  const wheelDir=join(output,'wheels-aarch64-apple-darwin'), wheelPath=join(wheelDir,readdirSync(wheelDir).find(n=>n.endsWith('.whl')));
  rmSync(wheelPath); const missingWheel=run(args,env); assert.equal(missingWheel.status,1); assert.match(missingWheel.stderr,/missing staged .* wheel/); wheel(output,'aarch64-apple-darwin');
  const failed=run(args,{...env,GH_FAILURE:'1'}); assert.equal(failed.status,1); assert.match(failed.stderr,/retry this Linux publication job/);
  rmSync(join(output,`v${version}`,`crozier-v${version}-aarch64-apple-darwin.tar.gz`));
  const missing=run(args,env); assert.equal(missing.status,1); assert.match(missing.stderr,/missing staged/);
});


test('actual workflow artifact paths and signer subjects feed the actual Linux publication command and wheel handoff', t=>{
  const jobs=parse(readFileSync('.github/workflows/release.yml','utf8')).jobs;
  const root=scratch(t), macTemp=join(root,'mac'), linux=join(root,'linux'); mkdirSync(linux,{recursive:true});
  const tag=`v${version}`, targets=jobs.darwin.env.DARWIN_TARGETS.split(' ');
  const builder=jobs.darwin.steps.find(s=>s.name==='Build and install both staged products');
  const subdirectory=/--out "\$RUNNER_TEMP\/([^"]+)"/.exec(builder.run)[1];
  const sourceRoot=join(macTemp,subdirectory);
  for(const target of targets) { wheel(sourceRoot,target); const packed=pack(sourceRoot,target); assert.equal(packed.status,0,packed.stderr); }
  const upload=jobs.darwin.steps.find(s=>s.uses?.startsWith('actions/upload-artifact'));
  const download=jobs['publish-darwin'].steps.find(s=>s.uses?.startsWith('actions/download-artifact'));
  assert.equal(upload.with.name,download.with.name);
  const context={github:{ref_name:tag,repository:'nickderobertis/crozier'},runner:{temp:macTemp},steps:{},secrets:{GITHUB_TOKEN:'transport-boundary-token'}};
  const render=text=>text.replace(/\$\{\{(.*?)\}\}/g,(_all,body)=>expression(body,context).coerceString());
  const destination=join(linux,download.with.path), transported=new Set();
  // Only GitHub's artifact transport is doubled: enumerate the workflow's
  // real upload globs and preserve their shared-root layout on download.
  for(const pattern of render(upload.with.path).trim().split('\n')) {
    const files=globSync(pattern.trim()); assert.ok(files.length,`empty workflow artifact pattern ${pattern}`);
    for(const file of files) { const name=relative(sourceRoot,file); assert.ok(!name.startsWith('..')); const to=join(destination,name); mkdirSync(dirname(to),{recursive:true}); cpSync(file,to); transported.add(name); }
  }
  symlinkSync(resolve('tools'),join(linux,'tools'),'junction');
  const bin=join(linux,'bin'); mkdirSync(bin); const calls=join(linux,'calls.json'), fake=join(bin,'gh');
  writeFileSync(fake,`#!/usr/bin/env python3\nimport sys,json,os\njson.dump(sys.argv[1:],open(os.environ['GH_CALLS'],'w'))\n`); chmodSync(fake,0o755);
  const subjects=[];
  for(const signer of jobs['publish-darwin'].steps.filter(s=>s.uses?.startsWith('actions/attest-build-provenance'))) {
    const subject=render(signer.with['subject-path']), path=join(linux,subject); assert.equal(existsSync(path),true,subject);
    const target=targets.find(target=>subject.endsWith(`${target}.tar.gz`)); assert.ok(target,subject);
    const golden=JSON.parse(readFileSync('.github/tests/release-contract.json','utf8')).platforms.find(p=>p.target===target);
    assert.equal(subject.split('/').at(-1),golden.archive.replace('<tag>',tag));
    const bundle=join(linux,`${signer.id}-bundle.json`);
    // Opaque signer-output bytes replace that third-party API; no claim of a
    // locally minted GitHub OIDC signature is made.
    writeFileSync(bundle,JSON.stringify({apiBoundary:'attest-build-provenance',subject,sha256:createHash('sha256').update(readFileSync(path)).digest('hex')}));
    context.steps[signer.id]={outputs:{'bundle-path':bundle}}; subjects.push({target,bundle});
  }
  const publish=jobs['publish-darwin'].steps.find(s=>s.name==='Publish Darwin archives and bundles');
  const env=Object.fromEntries(Object.entries(publish.env).map(([key,value])=>[key,render(value)]));
  const result=run(['bash','-e','-c',publish.run],{...env,PATH:`${bin}:${process.env.PATH}`,GITHUB_REF_NAME:tag,GITHUB_REPOSITORY:context.github.repository,GH_CALLS:calls},linux);
  assert.equal(result.status,0,result.stderr);
  const argv=JSON.parse(readFileSync(calls,'utf8'));
  for(const {target,bundle} of subjects) {
    const expected=`crozier-${tag}-${target}.sigstore.json`;
    assert.ok(argv.includes(`${download.with.path}/${tag}/${expected}`));
    assert.equal(readFileSync(join(destination,tag,expected),'utf8'),readFileSync(bundle,'utf8'));
    assert.ok(transported.has(`${tag}/crozier-${tag}-${target}.tar.gz`));
  }
  const handoff=jobs['publish-darwin'].steps.find(s=>s.uses?.startsWith('actions/upload-artifact'));
  const wheels=globSync(handoff.with.path,{cwd:linux});
  for(const target of targets) assert.ok(wheels.some(path=>path.includes(`wheels-${target}/`)),`missing workflow wheel handoff ${target}`);
  assert.ok(jobs['publish-pypi'].steps.some(s=>s.uses?.startsWith('actions/download-artifact') && s.with.pattern==='wheels-*'));
});

test('real release builder rejects unsafe manifest versions before building or deriving paths', t=>{
  const cwd=scratch(t), output=join(cwd,'products'), builder=resolve('tools/release-packaging/release-native.py');
  for(const version of ['../escape','1.2.3/escape','1.2.3\\escape','1.2.3\n']) {
    writeFileSync(join(cwd,'Cargo.toml'),`[package]\nname = "crozier"\nversion = ${JSON.stringify(version)}\n`);
    for(const flags of [[],['--pack-only']]) {
      const refused=run(['python3',builder,'--target','aarch64-apple-darwin','--tag',`v${version}`,'--out',output,...flags],{},cwd);
      assert.notEqual(refused.status,0);
      assert.match(refused.stderr,/unsupported Cargo.toml version/);
      assert.equal(existsSync(output),false,'invalid identity must fail before product paths are created');
    }
  }
});

test('real release builder rejects missing or malformed manifest package tables with actionable errors', t=>{
  const cwd=scratch(t), output=join(cwd,'products'), builder=resolve('tools/release-packaging/release-native.py');
  for(const manifest of ['[workspace]\nmembers = []\n','package = "crozier"\n','package = true\n','[package]\nname = "crozier"\n']) {
    writeFileSync(join(cwd,'Cargo.toml'),manifest);
    for(const flags of [[],['--pack-only']]) {
      const refused=run(['python3',builder,'--target','aarch64-apple-darwin','--tag','v0.0.1','--out',output,...flags],{},cwd);
      assert.notEqual(refused.status,0);
      assert.match(refused.stderr,/Cargo.toml must contain a package table and version/);
      assert.doesNotMatch(refused.stderr,/Traceback/);
      assert.equal(existsSync(output),false);
    }
  }
});


test('real packer refuses an absent wheel and recovers in the same staging directory', t=>{
  const output=scratch(t), target='aarch64-apple-darwin';
  const missing=pack(output,target);
  assert.equal(missing.status,1); assert.match(missing.stderr,/expected one wheel.*clean the output directory and rebuild/);
  assert.doesNotMatch(missing.stderr,/Traceback/);
  assert.equal(existsSync(join(output,`contract-${target}.json`)),false);
  wheel(output,target);
  const recovered=pack(output,target);
  assert.equal(recovered.status,0,recovered.stderr);
  assert.match(recovered.stdout,/staged aarch64-apple-darwin.*validated/);
  assert.equal(existsSync(join(output,`contract-${target}.json`)),true);
});

test('release builder help documents statuses and invalid invocation uses argparse status 2', ()=>{
  const args=['python3','tools/release-packaging/release-native.py'];
  const help=run([...args,'--help']);
  assert.equal(help.status,0); assert.match(help.stdout.replace(/\s+/g,' '),/0 success; 1 operational or validation failure; 2 invalid invocation/);
  const invalid=run([...args,'--target','unknown']);
  assert.equal(invalid.status,2); assert.match(invalid.stderr,/invalid choice/); assert.equal(invalid.stdout,'');
});
