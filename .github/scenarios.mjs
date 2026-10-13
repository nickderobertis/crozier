import { createHash } from 'node:crypto';
// Workload identities, not scheduling counts. Both recorder and reader require
// the same complete event/diff/ownership/publish population.
export const classes = [
  ['pr-opened','pull_request','opened'], ['pr-synchronize','pull_request','synchronize'], ['pr-reopened','pull_request','reopened'],
  ['base-push','push'], ['release-merge','push'], ['tag-push','push'], ['release-published','release','published'],
  ['downstream','workflow_run','completed'], ['repository-dispatch','repository_dispatch'], ['schedule','schedule'],
  ['manual-default','workflow_dispatch'], ['manual-opt-in','workflow_dispatch'],
];
export const classificationIds=['classification/release-plz-2026-10-12','classification/release-plz-forged','classification/unknown','classification/release-plz-mixed'];
export function scenarioIds() {
  return [...classes.flatMap(([id])=>['source','version','dependency'].flatMap(diff=>['same','fork'].flatMap(owner=>['false','true'].flatMap(crates=>['false','true'].map(pypi=>`${id}/${diff}/${owner}/crates=${crates}/pypi=${pypi}`))))),...classificationIds].sort();
}
export function lifecycleIds() {
  return [false,true].flatMap(fork=>['source','version','dependency'].flatMap(diff=>['false','true'].flatMap(crates=>['false','true'].map(pypi=>JSON.stringify([fork,diff,crates,pypi]))))).sort();
}
export function recordingDigest(telemetry) {
  const {recordingDigest:_,...payload}=telemetry;
  return createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}
export function validateTelemetry(telemetry, sourceDigest) {
  if (telemetry.schemaVersion !== 2 || telemetry.sourceDigest !== sourceDigest) throw new Error('missing/stale telemetry: run github-workflows:test on this tree');
  if (telemetry.recordingDigest !== recordingDigest(telemetry)) throw new Error('incomplete/corrupted workload telemetry: rerun github-workflows:test');
  const scenarios=telemetry.scenarios, lifecycles=telemetry.lifecycles;
  if (!Array.isArray(scenarios) || !Array.isArray(lifecycles) || JSON.stringify(scenarios.map(s=>s.id).sort()) !== JSON.stringify(scenarioIds()) || JSON.stringify(lifecycles.map(l=>JSON.stringify([l.fork,l.diff,l.crates,l.pypi])).sort()) !== JSON.stringify(lifecycleIds())) throw new Error('incomplete workload telemetry: run github-workflows:test');
  for (const scenario of scenarios) {
    if (!Array.isArray(scenario.runs) || typeof scenario.decision?.macosRequired !== 'boolean') throw new Error(`invalid telemetry scenario ${scenario.id}`);
    for (const run of scenario.runs) {
      if (typeof run.workflow !== 'string' || !Array.isArray(run.rows) || !run.rows.length) throw new Error(`invalid telemetry run ${scenario.id}`);
      for (const row of run.rows) {
        if (typeof row.job !== 'string' || typeof row.macos !== 'boolean' || !['success','skipped'].includes(row.result)) throw new Error(`invalid telemetry job ${scenario.id}`);
        if (row.result === 'success') {
          const labels=Array.isArray(row.runner)?row.runner:[row.runner];
          if (!labels.length || labels.some(l=>typeof l!=='string' || !/^(ubuntu|windows|macos)-[\w.-]+$/.test(l)) || row.macos !== labels.some(l=>l.startsWith('macos-'))) throw new Error(`invalid telemetry runner ${scenario.id}`);
        } else if (row.macos) throw new Error('skipped job cannot request Mac');
      }
    }
  }
  for (const lifecycle of lifecycles) {
    const selected=scenarios.filter(s=>['pr-synchronize','base-push','release-merge','tag-push','release-published','downstream','repository-dispatch','schedule'].includes(s.class) && s.diff===lifecycle.diff && s.fork===lifecycle.fork && s.publish.crates===lifecycle.crates && s.publish.pypi===lifecycle.pypi);
    selected.push(scenarios.find(s=>s.id==='classification/release-plz-2026-10-12'));
    const expected=selected.flatMap(s=>s.runs.filter(r=>r.rows.some(row=>row.macos)).map(r=>({event:s.id,workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)})));
    if (JSON.stringify(lifecycle.runs)!==JSON.stringify(expected)) throw new Error('inconsistent lifecycle telemetry');
  }
}
