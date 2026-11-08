#!/usr/bin/env node
// Exit 0 accepts every lane's real result; 1 rejects invalid, missing or unsuccessful ones.
// GitHub's needs JSON is the sole doubled boundary in the result journeys. A skipped test
// lane counts only where lint's real release guard step passed on this run; nothing else
// can excuse one, whatever the branch is called.
const ALWAYS = ['lint', 'commitlint', 'llmlint'];
const TEST_LANES = ['test-linux', 'test-windows', 'test-macos'];
try {
  const needs = JSON.parse(process.env.CI_NEEDS);
  for (const id of ALWAYS) {
    if (needs[id]?.result !== 'success') throw new Error(`${id} did not succeed (${needs[id]?.result ?? 'missing'})`);
  }
  const guarded = needs.lint.outputs?.releaseGuard === 'passed';
  for (const id of TEST_LANES) {
    const result = needs[id]?.result;
    if (result === 'success' || (result === 'skipped' && guarded)) continue;
    throw new Error(`${id} did not succeed (${result ?? 'missing'}, release guard ${guarded ? 'passed' : 'did not pass'})`);
  }
  console.log(guarded ? 'release guard passed: lint and the transitional checks succeeded, test lanes need not run' : 'all four lanes and the transitional checks succeeded');
} catch (error) {
  console.error(`::error::${error.message}`);
  process.exitCode = 1;
}
