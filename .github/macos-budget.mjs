#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { report } from '@onebudgetspec/sdk';
import { digest } from './workflow-graph.mjs';
import { validateTelemetry } from './scenarios.mjs';
// Exit 0 reports existing telemetry; 1 is telemetry/IO/report failure; 2 is invalid invocation.
class InvocationError extends Error {}
try {
  const [flag,metric,telemetryFlag,path,...extra] = process.argv.slice(2);
  if (flag !== '--metric' || telemetryFlag !== '--telemetry' || extra.length || !path || !['jobs-per-run','runs-per-change'].includes(metric)) throw new InvocationError('usage: macos-budget.mjs --metric jobs-per-run|runs-per-change --telemetry JSON');
  const telemetry = JSON.parse(readFileSync(resolve(path), 'utf8'));
  validateTelemetry(telemetry,digest());
  const counts = metric === 'jobs-per-run' ? telemetry.scenarios.flatMap(s => s.runs.map(r => r.rows.filter(row => row.macos).length)) : telemetry.lifecycles.map(l => l.runs.length);
  const actual = Math.max(...counts);
  const detail = JSON.stringify({sourceDigest:telemetry.sourceDigest,metric,scenarios:telemetry.scenarios.map(s=>({event:s.id,runs:s.runs.filter(r=>r.rows.some(row=>row.macos)).map(r=>({workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)}))})),lifecycles:telemetry.lifecycles});
  report(actual,detail);
  console.log(`${metric}: ${actual}`);
} catch (error) { console.error(`macos-budget: ${error.message}`); process.exitCode=error instanceof InvocationError ? 2 : 1; }
