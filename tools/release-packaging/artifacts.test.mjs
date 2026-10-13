// Non-native products are packed and inspected, never executed on Linux.
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync, cpSync, chmodSync, readdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { test } from 'node:test';

function run(args,env={}) { return spawnSync(args[0],args.slice(1),{encoding:'utf8',env:{...process.env,...env}}); }
function scratch(t) { const root=mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'crozier-artifact-')); t.after(()=>rmSync(root,{recursive:true,force:true})); return root; }
const version=/^version = "([^"]+)"/m.exec(readFileSync('Cargo.toml','utf8'))[1];
function wheel(output,target,kind='valid') {
  const dir=join(output,`wheels-${target}`); mkdirSync(dir,{recursive:true});
  const isMac=target.endsWith('apple-darwin');
  const platform=target.startsWith('aarch64')?(isMac?'arm64':'aarch64'):'x86_64';
  const osTag=isMac?'macosx_11_0':'manylinux_2_34';
  const path=join(dir,`crozier-${version}-py3-none-${kind==='wheel-os'?'windows':osTag}_${kind==='wheel-arch'?'wrong':platform}.whl`);
  const made=run(['python3','-c',`import sys,zipfile,struct
p,v,target,kind=sys.argv[1:]
b=(bytes.fromhex('cffaedfe')+struct.pack('<I',0x0100000c if target.startswith('aarch64') else 0x01000007) if target.endswith('apple-darwin') else bytes.fromhex('7f454c46')+bytes(14)+struct.pack('<H',183 if target.startswith('aarch64') else 62))+b'contract-fixture'
with zipfile.ZipFile(p,'w') as z:
 if kind!='executable': z.writestr('crozier-'+v+'.data/scripts/crozier',b if kind!='binary-arch' else b'wrong')
 if kind!='metadata': z.writestr('crozier-'+v+'.dist-info/METADATA','Name: crozier\\nVersion: '+('999' if kind=='version' else v)+'\\n')
`,path,version,target,kind]); assert.equal(made.status,0,made.stderr); return path;
}
function pack(output,target) { return run(['python3','tools/release-packaging/release-native.py','--pack-only','--out',output,'--target',target,'--tag',`v${version}`]); }

test('real packer validates both Darwin architectures and refuses malformed/ambiguous wheels', t=>{
  for (const target of ['x86_64-apple-darwin','aarch64-apple-darwin']) {
    const output=scratch(t); wheel(output,target);
    const built=pack(output,target); assert.equal(built.status,0,built.stderr);
    const contract=JSON.parse(readFileSync(join(output,`contract-${target}.json`),'utf8'));
    assert.equal(contract.target,target); assert.equal(contract.binarySha256,contract.archiveBinarySha256); assert.equal(contract.binarySha256,contract.wheelBinarySha256);
    const contents=run(['python3','-c','import tarfile,json,sys; a=tarfile.open(sys.argv[1]); print(json.dumps(sorted(a.getnames())))',contract.archive]);
    assert.equal(contents.status,0,contents.stderr);
    const golden=JSON.parse(readFileSync('.github/tests/release-contract.json','utf8'));
    assert.deepEqual(JSON.parse(contents.stdout),[...golden.archiveContents].sort());
    assert.equal(contract.archive.split('/').at(-1),golden.platforms.find(p=>p.target===target).archive.replace('<tag>',`v${version}`));
  }
  for (const target of ['x86_64-apple-darwin','x86_64-unknown-linux-gnu']) for (const kind of ['executable','metadata','version','wheel-arch','binary-arch','wheel-os','ambiguous']) {
    const output=scratch(t); const path=wheel(output,target,kind);
    if(kind==='ambiguous') cpSync(path,join(output,`wheels-${target}`,'duplicate.whl'));
    const refused=pack(output,target); assert.equal(refused.status,1,kind); assert.match(refused.stderr,/rebuild|clean/); assert.doesNotMatch(refused.stderr,/Traceback/);
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
