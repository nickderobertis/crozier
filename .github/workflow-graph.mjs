// Repository-local resolver. Remote reusable workflows are reviewed snapshots;
// any new call, dynamic runner or output producer must be resolved explicitly.
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, mkdirSync, mkdtempSync, rmSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { parse } from 'yaml';
import { Parser, Lexer, Evaluator, data } from '@actions/expressions';

export const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
export function workflows() {
  return readdirSync(resolve(root, '.github/workflows')).filter(n => /\.ya?ml$/.test(n)).sort().map(n => ({ path: `.github/workflows/${n}`, value: parse(readFileSync(resolve(root, '.github/workflows', n), 'utf8')) }));
}
export function digest() {
  const files = [];
  function collect(dir) {
    for (const entry of readdirSync(resolve(root, dir), { withFileTypes: true })) {
      if (['node_modules', '.telemetry'].includes(entry.name) || (dir === '.github' && entry.name === 'budgets.yaml')) continue;
      const path = `${dir}/${entry.name}`;
      if (entry.isDirectory()) collect(path);
      else files.push(path);
    }
  }
  collect('.github');
  files.push('screencomp.toml', 'release-plz.toml');
  const hash = createHash('sha256');
  for (const path of files.sort()) hash.update(path).update('\0').update(readFileSync(resolve(root, path))).update('\0');
  return hash.digest('hex');
}
export function expression(source, context, outcomes = []) {
  const functions = new Map(['always', 'success', 'failure', 'cancelled'].map(name => [name, {
    name, minArgs: 0, maxArgs: 0, call: () => new data.BooleanData(name === 'always' || (name === 'success' ? outcomes.every(o => o === 'success') : outcomes.includes(name === 'failure' ? 'failure' : 'cancelled'))),
  }]));
  const text = source.replace(/^\s*\$\{\{\s*/, '').replace(/\s*\}\}\s*$/, '');
  const tokens = new Lexer(text).lex().tokens;
  const parsed = new Parser(tokens, Object.keys(context), [...functions.values()]).parse();
  return new Evaluator(parsed, JSON.parse(JSON.stringify(context), data.reviver), functions).evaluate();
}
function value(input, context, outcomes) {
  if (typeof input !== 'string' || !input.includes('${{')) return input;
  let evaluated;
  try { evaluated = expression(input, context, outcomes); }
  catch (error) { throw new Error(`unresolved expression ${input}: ${error.message}`); }
  return JSON.parse(JSON.stringify(evaluated, data.replacer));
}
export function matrixRows(matrix = {}, context = {}) {
  const resolved = value(matrix, context);
  if (!resolved || typeof resolved !== 'object' || Array.isArray(resolved)) throw new Error('unresolved matrix');
  for (const key of ['include', 'exclude']) {
    const entries = resolved[key];
    if (entries !== undefined && (!Array.isArray(entries) || entries.some(row => !row || typeof row !== 'object' || Array.isArray(row)))) throw new Error(`unresolved matrix ${key}: expected object rows`);
  }
  let rows = [{}];
  for (const [key, input] of Object.entries(resolved)) {
    if (['include', 'exclude'].includes(key)) continue;
    const list = value(input, context);
    if (!Array.isArray(list) || !list.length) throw new Error(`unresolved matrix axis ${key}`);
    rows = rows.flatMap(row => list.map(v => ({ ...row, [key]: v })));
  }
  const axes = Object.keys(resolved).filter(k => !['include', 'exclude'].includes(k));
  rows = rows.filter(row => !(resolved.exclude ?? []).some(ex => Object.entries(ex).every(([k, v]) => row[k] === v)));
  if (!axes.length && resolved.include?.length === 0) throw new Error('unresolved matrix include: no job rows');
  if (!axes.length && resolved.include) return resolved.include.map(row => ({ ...row }));
  for (const include of resolved.include ?? []) {
    const matches = rows.filter(row => axes.every(k => include[k] === undefined || include[k] === row[k]));
    if (!matches.length) rows.push({ ...include });
    else for (const row of matches) Object.assign(row, include);
  }
  return rows;
}
export function triggered(workflow, scenario) {
  const on = workflow.on;
  const config = typeof on === 'string' ? (on === scenario.eventName ? {} : undefined) : Array.isArray(on) ? (on.includes(scenario.eventName) ? {} : undefined) : on?.[scenario.eventName];
  if (config === undefined) return false;
  for (const key of ['branches', 'tags']) {
    const filters = config?.[key];
    if (filters !== undefined && (!Array.isArray(filters) || filters.some(filter => typeof filter !== 'string' || !/^[A-Za-z0-9._/-]+$/.test(filter)))) throw new Error(`unresolved workflow trigger filter: ${key}`);
  }
  const types = config?.types !== undefined ? config.types : scenario.eventName === 'pull_request' ? ['opened', 'synchronize', 'reopened'] : undefined;
  if (types !== undefined && (!Array.isArray(types) || !types.length || types.some(type => typeof type !== 'string' || !type.length))) throw new Error('unresolved workflow trigger types: expected event names');
  if (types && !types.includes(scenario.event.action)) return false;
  if (config?.branches && !config.branches.includes(scenario.branch)) return false;
  if (config?.tags && !config.tags.includes(scenario.tag)) return false;
  if (config?.paths || config?.['paths-ignore'] || config?.['branches-ignore'] || config?.['tags-ignore']) throw new Error('unresolved workflow trigger filter');
  return true;
}
function reusable(call) {
  if (call.startsWith('./.github/workflows/')) return { path: call.slice(2), value: parse(readFileSync(resolve(root, call), 'utf8')) };
  const snapshots = JSON.parse(readFileSync(resolve(root, '.github/tests/reusable/lock.json'), 'utf8'));
  const entry = snapshots[call];
  if (!entry) throw new Error(`unresolved reusable workflow: ${call}`);
  const content = readFileSync(resolve(root, entry.path));
  if (createHash('sha256').update(content).digest('hex') !== entry.sha256) throw new Error(`reusable snapshot digest mismatch: ${call}`);
  if (entry.upstreamSha256 && createHash('sha256').update(content.toString().split('\n').slice(1).join('\n')).digest('hex') !== entry.upstreamSha256) throw new Error(`upstream snapshot bytes changed: ${call}`);
  return { path: call, value: parse(content.toString()) };
}
let captureArches;
const guardOutputs=new Map();
function policyOutput(job,decision) {
  const step=job.steps?.find(s=>s.id==='policy');
  if (job.outputs?.macosRequired !== '${{ steps.policy.outputs.macosRequired }}' || step?.run.trim() !== 'node .github/macos-policy.mjs classify --event "$GITHUB_EVENT_PATH" --base "$PR_BASE" --head "$PR_HEAD"' || step.env?.PR_BASE !== '${{ github.event.pull_request.base.sha }}' || step.env?.PR_HEAD !== '${{ github.event.pull_request.head.sha }}' || step.env?.GITHUB_EVENT_NAME !== undefined) throw new Error('unresolved macos-policy producer wiring');
  return {macosRequired:String(decision.macosRequired)};
}
function registryOutputs(job,publish) {
  const step=job.steps?.find(s=>s.id==='check');
  if (job.outputs?.crates !== '${{ steps.check.outputs.crates }}' || job.outputs?.pypi !== '${{ steps.check.outputs.pypi }}' || step?.env?.CARGO_TOKEN !== '${{ secrets.CARGO_REGISTRY_TOKEN }}' || step?.env?.PYPI_TOKEN !== '${{ secrets.PYPI_TOKEN }}' || typeof step.run !== 'string') throw new Error('unresolved registry guard producer wiring');
  const key=JSON.stringify([step.run,publish]);
  if (!guardOutputs.has(key)) {
    const telemetry=resolve(root,'.github/.telemetry'); mkdirSync(telemetry,{recursive:true});
    const scratch=mkdtempSync(resolve(telemetry,'guard-'));
    try {
      const path=resolve(scratch,'outputs');
      execFileSync('bash',['-e','-c',step.run],{env:{...process.env,GITHUB_OUTPUT:path,CARGO_TOKEN:publish.crates==='true'?'fixture-token':'',PYPI_TOKEN:publish.pypi==='true'?'fixture-token':''},stdio:['ignore','pipe','pipe']});
      const outputs=Object.fromEntries(readFileSync(path,'utf8').trim().split('\n').map(line=>line.split('=')));
      if (!['true','false'].includes(outputs.crates) || !['true','false'].includes(outputs.pypi) || outputs.crates!==publish.crates || outputs.pypi!==publish.pypi) throw new Error('invalid registry token routing outputs');
      guardOutputs.set(key,outputs);
    } catch(error) { throw new Error(`unresolved registry producer: ${error.message}`); }
    finally { rmSync(scratch,{recursive:true,force:true}); }
  }
  return guardOutputs.get(key);
}
export function resolveRun(workflow, scenario, decision, ancestry = []) {
  if (ancestry.includes(workflow.path)) throw new Error('recursive reusable workflow');
  const jobs = workflow.value.jobs;
  const rows = [], needs = {}, pending = new Set(Object.keys(jobs));
  while (pending.size) {
    let progress = false;
    for (const id of pending) {
      const job = jobs[id], dependencies = typeof job.needs === 'string' ? [job.needs] : job.needs ?? [];
      for (const dependency of dependencies) if (!jobs[dependency]) throw new Error(`unresolved need ${dependency}`);
      if (dependencies.some(d => pending.has(d))) continue;
      progress = true; pending.delete(id);
      const outcomes = dependencies.map(d => needs[d].result);
      const context = {
        github: { event_name: scenario.eventName, event: scenario.event, repository: 'nickderobertis/crozier', ref: `refs/heads/${scenario.branch}`, ref_name: scenario.tag ?? scenario.branch, workflow: workflow.value.name },
        needs: Object.fromEntries(dependencies.map(d => [d, needs[d]])), inputs: scenario.inputs ?? {}, matrix: {}, runner: {},
      };
      const enabled = job.if ? expression(job.if, context, outcomes).coerceString() === 'true' && (/\b(always|failure|cancelled|success)\(/.test(job.if) || outcomes.every(o => o === 'success')) : outcomes.every(o => o === 'success');
      needs[id] = { result: enabled ? 'success' : 'skipped', outputs: {} };
      if (id === 'macos-policy') needs[id].outputs=policyOutput(job,decision);
      if (workflow.path.includes('release.yml') && id === 'guard') needs[id].outputs = registryOutputs(job,scenario.publish ?? { crates: 'false', pypi: 'false' });
      if (id === 'arches' && workflow.path.startsWith('nickderobertis/screencomp/')) {
        // The reusable workflow runs `screencomp arches --format json` on this
        // exact configuration; parse the declared architecture source offline.
        const producer=job.steps?.find(s=>s.id==='read');
        if (job.outputs?.matrix !== '${{ steps.read.outputs.matrix }}' || producer?.env?.ARCHES_OVERRIDE !== '${{ inputs.arches }}' || !producer.run.includes('matrix="$(screencomp arches --format json)"') || !producer.run.includes('matrix="$ARCHES_OVERRIDE"') || !producer.run.includes('echo "matrix=$matrix"')) throw new Error('unresolved capture producer wiring');
        const configured = captureArches ??= JSON.parse(execFileSync('python3', ['-c', 'import tomllib,json; print(json.dumps(tomllib.load(open("screencomp.toml","rb"))["capture"]["arches"]))'], { cwd: root, encoding: 'utf8' }));
        const arches=context.inputs.arches ? JSON.parse(context.inputs.arches) : configured;
        if (!Array.isArray(arches) || !arches.length || arches.some(a=>!['x86_64','amd64','arm64','aarch64'].includes(a))) throw new Error(`unresolved capture architectures: ${JSON.stringify(arches)}`);
        needs[id].outputs.matrix = JSON.stringify(arches);
      }
      if (!enabled) { rows.push({ workflow: workflow.path, event: scenario.id, job: id, result: 'skipped', macos: false }); continue; }
      if (job.uses) {
        const child = reusable(job.uses), declared = child.value.on?.workflow_call?.inputs ?? {};
        const supplied = job.with ?? {};
        if (!declared || typeof declared !== 'object' || Array.isArray(declared) || typeof supplied !== 'object' || Array.isArray(supplied)) throw new Error('unresolved reusable inputs: expected mappings');
        for (const key of Object.keys(supplied)) if (!Object.hasOwn(declared, key)) throw new Error(`unresolved reusable input: unknown ${key}`);
        const inputs = Object.create(null);
        for (const [key, definition] of Object.entries(declared)) {
          if (!new data.Dictionary({key, value:new data.BooleanData(true)}).get(key)) throw new Error(`unresolved reusable input: unsupported evaluator key ${key}`);
          if (!definition || typeof definition !== 'object' || !['string', 'number', 'boolean'].includes(definition.type) || (definition.required !== undefined && typeof definition.required !== 'boolean')) throw new Error(`unresolved reusable input declaration: ${key}`);
          const provided = Object.hasOwn(supplied, key), hasDefault = Object.hasOwn(definition, 'default');
          if (definition.required && !provided && !hasDefault) throw new Error(`unresolved reusable input: missing required ${key}`);
          const input = provided ? value(supplied[key], context, outcomes) : hasDefault ? definition.default : {string:'',number:0,boolean:false}[definition.type];
          if (typeof input !== definition.type || (definition.type === 'number' && !Number.isFinite(input))) throw new Error(`unresolved reusable input: ${key} must be ${definition.type}`);
          inputs[key] = input;
        }
        rows.push(...resolveRun(child, { ...scenario, inputs }, decision, [...ancestry, workflow.path]));
        continue;
      }
      for (const matrix of matrixRows(job.strategy?.matrix, context)) {
        const runner = value(job['runs-on'], { ...context, matrix }, outcomes);
        const labels = Array.isArray(runner) ? runner : [runner];
        if (!labels.length || labels.some(l => typeof l !== 'string' || !/^(ubuntu|windows|macos)-[\w.-]+$/.test(l))) throw new Error(`unresolved runner ${workflow.path}:${id}: ${JSON.stringify(runner)}`);
        rows.push({ workflow: workflow.path, event: scenario.id, job: id, matrix, runner, result: 'success', macos: labels.some(l => l.startsWith('macos-')), targets: job.env?.DARWIN_TARGETS?.split(' ') ?? (matrix.target ? [matrix.target] : []) });
      }
    }
    if (!progress) throw new Error(`unresolved/cyclic job graph ${workflow.path}`);
  }
  return rows;
}
