#!/usr/bin/env node
// Exit 0 accepts all required results; 1 rejects invalid, missing or unsuccessful results.
// GitHub's needs JSON is the sole doubled boundary in the result journeys.
import { runUrlPattern } from './macos-policy.mjs';
try {
  const needs = JSON.parse(process.env.CI_NEEDS);
  for (const id of ['check', 'sdk-env', 'install', 'package', 'live-e2e', 'macos-policy']) {
    if (needs[id]?.result !== 'success') throw new Error(`${id} did not succeed (${needs[id]?.result ?? 'missing'})`);
  }
  const required = needs['macos-policy'].outputs?.macosRequired;
  if (!['true', 'false'].includes(required)) throw new Error('missing Mac routing decision');
  const reused = needs['macos-policy'].outputs?.macosReusedRun ?? '';
  if (typeof reused !== 'string' || (reused && (required !== 'false' || !runUrlPattern.test(reused)))) throw new Error('malformed Mac reuse decision');
  const mac = needs.macos?.result;
  if (reused) {
    // The reuse lane succeeds only by naming the earlier run; it never stands in for a skip.
    if (mac !== 'success') throw new Error(`Mac reuse lane did not succeed (${mac ?? 'missing'}, reused=${reused})`);
    console.log(`Linux/Windows lanes succeeded; no Mac job ran in this run, its proof on this head is ${reused}`);
  } else {
    if (mac !== 'success' && !(mac === 'skipped' && required === 'false')) throw new Error(`Mac proof did not succeed (${mac ?? 'missing'}, required=${required})`);
    console.log(mac === 'success' ? 'all required lanes succeeded, including Mac' : 'Linux/Windows lanes succeeded; classifier authorized Mac omission');
  }
} catch (error) {
  console.error(`::error::${error.message}`);
  process.exitCode = 1;
}
