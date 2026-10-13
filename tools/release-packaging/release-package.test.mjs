// The production builder with forge/registry transport replaced by staged URLs.
// This compiles, packs, installs and generates through the real CLI. It never
// executes a non-native binary on the host.
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';

test('production native archive and wheel share a binary and both install and generate; mismatched tags fail before build', t => {
  const scratch = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(),'crozier-packaging-'));
  t.after(()=>rmSync(scratch,{recursive:true,force:true}));
  const version = /^version = "([^"]+)"/m.exec(readFileSync('Cargo.toml','utf8'))[1];
  const target = process.platform === 'darwin' ? `${process.arch === 'arm64' ? 'aarch64' : 'x86_64'}-apple-darwin` : `${process.arch === 'arm64' ? 'aarch64' : 'x86_64'}-unknown-linux-gnu`;
  const args = ['tools/release-packaging/release-native.py','--target',target,'--out',scratch,'--tag'];
  const refused = spawnSync('python3',[...args,'v999.0.0'],{encoding:'utf8'});
  assert.notEqual(refused.status,0); assert.match(refused.stderr,/does not match Cargo.toml/);
  const built = spawnSync('python3',[...args,`v${version}`],{encoding:'utf8',timeout:1200000,maxBuffer:16*1024*1024});
  assert.equal(built.status,0,`${built.stdout}\n${built.stderr}`);
  assert.match(built.stdout,/both installed and generated a working Python SDK/);
  for (const product of [join(scratch,`installed-${target}`,'crozier'),join(scratch,`wheel-installed-${target}`,'bin/crozier')]) {
    assert.equal(existsSync(product),true,`missing installed product ${product}`);
    const user=spawnSync('bash',['scripts/smoke.sh',version],{encoding:'utf8',env:{...process.env,CROZIER_BIN:product}});
    assert.equal(user.status,0,`${user.stdout}\n${user.stderr}`); assert.match(user.stdout,/generated a working Python SDK/);
  }
  const contract=JSON.parse(readFileSync(join(scratch,`contract-${target}.json`),'utf8'));
  assert.equal(contract.schemaVersion,1); assert.equal(contract.target,target); assert.equal(contract.tag,`v${version}`);
  assert.equal(contract.archiveBinarySha256,contract.wheelBinarySha256); assert.match(contract.binarySha256,/^[a-f0-9]{64}$/);
});
