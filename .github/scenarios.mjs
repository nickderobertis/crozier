import { createHash } from 'node:crypto';
import { workflows, triggered } from './workflow-graph.mjs';
// Workload identities, not scheduling counts. Both recorder and reader require
// the same complete event/diff/ownership/publish population.
export const classes = [
  ['pr-opened','pull_request','opened'], ['pr-synchronize','pull_request','synchronize'], ['pr-reopened','pull_request','reopened'],
  ['base-push','push'], ['release-merge','push'], ['tag-push','push'], ['release-published','release','published'],
  ['downstream','workflow_run','completed'], ['repository-dispatch','repository_dispatch'], ['schedule','schedule'],
  ['manual-default','workflow_dispatch'], ['manual-opt-in','workflow_dispatch'],
];
export const classificationIds=['classification/release-plz-2026-10-12','classification/release-plz-forged','classification/unknown','classification/release-plz-mixed'];
// Every draft-lift (`ready_for_review`) route of the ordinary PR: its head's
// Mac proof completed, still running, cancelled, failed, only on another head,
// or unreadable because the API is unavailable; or `fallback`, where no earlier
// run of the PR requested a Mac job. `none` is a PR that was never a draft.
export const liftRoutes=['proven','in-progress','cancelled','failed','other-head','api-unavailable','fallback'];
export const liftIds=liftRoutes.map(route=>`lift/${route}`);
const routeIds=[...classificationIds,...liftIds];
export function scenarioIds() {
  return [...classes.flatMap(([id])=>['source','version','dependency'].flatMap(diff=>['same','fork'].flatMap(owner=>['false','true'].flatMap(crates=>['false','true'].map(pypi=>`${id}/${diff}/${owner}/crates=${crates}/pypi=${pypi}`))))),...routeIds].sort();
}
// The single-push lifecycle: its synchronize run, the lift of its draft along
// one route (or none), base/release/downstream automation and the release PR.
export function lifecycleScenarios(scenarios, lifecycle) {
  // The fallback route is reachable only when the classifier read every earlier
  // run of the PR and none requested a Mac job (say the push's run was
  // cancelled before its Mac job), so that run contributes no Mac run here.
  const prRuns=lifecycle.lift==='fallback'?[]:['pr-synchronize'];
  const selected=scenarios.filter(s=>[...prRuns,'base-push','release-merge','tag-push','release-published','downstream','repository-dispatch','schedule'].includes(s.class) && s.diff===lifecycle.diff && s.fork===lifecycle.fork && s.publish.crates===lifecycle.crates && s.publish.pypi===lifecycle.pypi);
  const lift=lifecycle.lift==='none'?[]:[scenarios.find(s=>s.id===`lift/${lifecycle.lift}`)];
  return [...selected,...lift,scenarios.find(s=>s.id==='classification/release-plz-2026-10-12')];
}
export function lifecycleIds() {
  return [false,true].flatMap(fork=>['source','version','dependency'].flatMap(diff=>['false','true'].flatMap(crates=>['false','true'].flatMap(pypi=>['none',...liftRoutes].map(lift=>JSON.stringify([fork,diff,crates,pypi,lift])))))).sort();
}
export function recordingDigest(telemetry) {
  const {recordingDigest:_,...payload}=telemetry;
  return createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}
export function validateTelemetry(telemetry, sourceDigest) {
  if (telemetry.schemaVersion !== 5 || telemetry.sourceDigest !== sourceDigest) throw new Error('missing/stale telemetry: run github-workflows:test on this tree');
  if (telemetry.recordingDigest !== recordingDigest(telemetry)) throw new Error('incomplete/corrupted workload telemetry: rerun github-workflows:test');
  const scenarios=telemetry.scenarios, lifecycles=telemetry.lifecycles;
  if (!Array.isArray(scenarios) || !Array.isArray(lifecycles) || JSON.stringify(scenarios.map(s=>s.id).sort()) !== JSON.stringify(scenarioIds()) || JSON.stringify(lifecycles.map(l=>JSON.stringify([l.fork,l.diff,l.crates,l.pypi,l.lift])).sort()) !== JSON.stringify(lifecycleIds())) throw new Error('incomplete workload telemetry: run github-workflows:test');
  const graph = workflows();
  // llmlint: ignore[boundary_inputs_validated] Manager ruling c-7641e823c143fd3f2d19efbbe2653e65: this recorded telemetry is produced by this repository's own recorder in the same job. Readers never rerun scenarios; forged-row resistance is out of scope for a cost report. Keep source-digest, workload identity, trigger/run population and structural checks for stale or incomplete recordings.
  for (const scenario of scenarios) {
    if (!routeIds.includes(scenario.id)) {
      const [eventClass,diff,ownership,crates,pypi]=scenario.id.split('/');
      if (scenario.class !== eventClass || scenario.diff !== diff || scenario.fork !== (ownership === 'fork') || scenario.publish?.crates !== crates.slice(7) || scenario.publish?.pypi !== pypi.slice(5)) throw new Error(`invalid telemetry scenario identity ${scenario.id}`);
    }
    if (!Array.isArray(scenario.runs) || typeof scenario.decision?.macosRequired !== 'boolean') throw new Error(`invalid telemetry scenario ${scenario.id}`);
    if (liftIds.includes(scenario.id)) {
      const route=scenario.id.slice('lift/'.length), d=scenario.decision;
      if (d.macosRequired !== (route==='fallback') || (route==='proven') !== (typeof d.reusedRun === 'string') || !['proven','fallback'].includes(route) !== (typeof d.liftRefusal === 'string')) throw new Error(`invalid telemetry lift decision ${scenario.id}`);
    }
    const expected = graph.filter(workflow => triggered(workflow.value, scenario)).map(workflow => workflow.path).sort();
    if (JSON.stringify(scenario.runs.map(run => run.workflow).sort()) !== JSON.stringify(expected)) throw new Error(`incomplete workflow runs for ${scenario.id}`);
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
    const expected=lifecycleScenarios(scenarios,lifecycle).flatMap(s=>s.runs.filter(r=>r.rows.some(row=>row.macos)).map(r=>({event:s.id,workflow:r.workflow,jobs:r.rows.filter(row=>row.macos)})));
    if (JSON.stringify(lifecycle.runs)!==JSON.stringify(expected)) throw new Error('inconsistent lifecycle telemetry');
  }
}
