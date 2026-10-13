#!/usr/bin/env node
// GitHub's needs JSON is the sole doubled boundary in the result journeys.
try {
  const needs = JSON.parse(process.env.CI_NEEDS);
  for (const id of ['check', 'sdk-env', 'install', 'package', 'live-e2e', 'macos-policy']) {
    if (needs[id]?.result !== 'success') throw new Error(`${id} did not succeed (${needs[id]?.result ?? 'missing'})`);
  }
  const required = needs['macos-policy'].outputs?.macosRequired;
  if (!['true', 'false'].includes(required)) throw new Error('missing Mac routing decision');
  const mac = needs.macos?.result;
  if (mac !== 'success' && !(mac === 'skipped' && required === 'false')) throw new Error(`Mac proof did not succeed (${mac ?? 'missing'}, required=${required})`);
  console.log(mac === 'success' ? 'all required lanes succeeded, including Mac' : 'Linux/Windows lanes succeeded; classifier authorized Mac omission');
} catch (error) {
  console.error(`::error::${error.message}`);
  process.exitCode = 1;
}
