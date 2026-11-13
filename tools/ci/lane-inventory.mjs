#!/usr/bin/env node
// Every test, build, coverage and budget entrypoint against tools/ci/lanes.json and ci.yml,
// so none can leave the pull request flow unnoticed: a row whose target or project is gone,
// or whose platform was dropped, a new target with no row, a promoted project with no lane,
// a lane no step runs, a lost platform command, or a workflow on push to main that is not
// declared as gating nothing.
//
// Exit 0 when they reconcile; 1 naming each difference; 2 when a file cannot be read or has the wrong shape.
import { spawnSync } from "node:child_process";
import { readdirSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const ENTRYPOINT = /^(test|test-.*|budgets|budgets-host|coverage|build|cold-registry-build)$/;

const isMapping = (value) => value !== null && typeof value === "object" && !Array.isArray(value);

function refuse(message) {
  console.error(`lane-inventory: ${message}`);
  console.error("lane-inventory: restore the file, or run this from a full checkout");
  process.exit(2);
}

function read(path) {
  try {
    return readFileSync(join(ROOT, path), "utf8");
  } catch (error) {
    return refuse(`cannot read ${path}: ${error.message}`);
  }
}

const listing = spawnSync("git", ["ls-files", "-co", "--exclude-standard", "-z", "--", "*project.json"], { cwd: ROOT, encoding: "utf8" });
if (listing.status !== 0) {
  console.error(`lane-inventory: git ls-files failed: ${listing.stderr}`);
  process.exit(2);
}
const graph = new Map();
for (const path of listing.stdout.split("\0").filter(Boolean)) {
  // A tracked manifest deleted in the working tree is a project that is gone.
  let text;
  try {
    text = readFileSync(join(ROOT, path), "utf8");
  } catch {
    continue;
  }
  let project;
  try {
    project = JSON.parse(text.replace(/^\s*\/\/.*$/gm, ""));
  } catch (error) {
    refuse(`${path} is not JSON: ${error.message}`);
  }
  const isDependency = (entry) => typeof entry === "string" || (typeof entry?.target === "string" && (entry.projects === undefined || (Array.isArray(entry.projects) && entry.projects.every((name) => typeof name === "string"))));
  const isTarget = (target) => isMapping(target) && (target.dependsOn === undefined || (Array.isArray(target.dependsOn) && target.dependsOn.every(isDependency)));
  const tagsOk = project?.tags === undefined || (Array.isArray(project.tags) && project.tags.every((tag) => typeof tag === "string"));
  const targetsOk = project?.targets === undefined || (isMapping(project.targets) && Object.values(project.targets).every(isTarget));
  if (typeof project?.name !== "string" || !tagsOk || !targetsOk) refuse(`${path} needs a string name, a list of string tags and a mapping of targets with valid dependsOn`);
  graph.set(project.name, project);
}

let inventory;
try {
  inventory = JSON.parse(read("tools/ci/lanes.json"));
} catch (error) {
  refuse(`tools/ci/lanes.json is not JSON: ${error.message}`);
}
const rows = isMapping(inventory?.entrypoints) ? Object.entries(inventory.entrypoints) : undefined;
const commands = isMapping(inventory?.commands) ? Object.entries(inventory.commands) : undefined;
const added = isMapping(inventory?.added) ? Object.entries(inventory.added) : undefined;
const isEntrypoint = (value) => typeof value === "string" && /^[^:]+:[^:]+$/.test(value);
const nonCheck = isMapping(inventory?.nonCheckWorkflows) ? Object.entries(inventory.nonCheckWorkflows) : undefined;
const isPlatformList = (list) => Array.isArray(list) && list.every((platform) => ["linux", "macos", "windows"].includes(platform));
if (!nonCheck || !nonCheck.every(([path, why]) => /^\.github\/workflows\/[^/]+\.yml$/.test(path) && typeof why === "string" && why !== "")) {
  refuse("tools/ci/lanes.json needs a nonCheckWorkflows mapping of .github/workflows/<name>.yml to why it gates nothing");
}
if (!rows || !commands || !added || !added.every(([name, list]) => isEntrypoint(name) && isPlatformList(list))
  || !rows.every(([entry, row]) => isEntrypoint(row?.now ?? entry) && isPlatformList(row?.platforms)) || !commands.every(([, list]) => isPlatformList(list))) {
  refuse("tools/ci/lanes.json needs entrypoints and commands naming project:target and linux, macos or windows, and an added mapping of the same");
}
const ci = read(".github/workflows/ci.yml");
const problems = [];
const at = (from, to) => ci.slice(ci.indexOf(`  ${from}:\n`), to ? ci.indexOf(`  ${to}:\n`) : undefined);
const lanes = { linux: at("test-linux", "test-windows"), windows: at("test-windows", "test-macos"), macos: at("test-macos") };

// What each platform's recipes start, through every `dependsOn`: a row whose target nothing
// starts on a platform it owes runs nowhere there, however present it is.
const justfile = read("justfile");
const listed = /^lane_test_targets := if os\(\) == "windows" \{ "([^"]+)" \} else if os\(\) == "macos" \{ "([^"]+)" \} else \{ "([^"]+)" \}$/m.exec(justfile);
const hostBudgets = /^lane-budgets-host \*args:\n.*--targets=(\S+)$/m.exec(justfile);
if (!listed || !hostBudgets) refuse("the justfile's lane_test_targets and lane-budgets-host recipes are not in the form this check reads");
const started = {
  windows: listed[1].split(","),
  macos: listed[2].split(","),
  // Only test-linux runs the host budget step (asserted against ci.yml below).
  linux: [...listed[3].split(","), ...hostBudgets[1].split(",")],
};
if (!lanes.linux.includes("just ci-budgets-host")) problems.push("test-linux no longer runs `just ci-budgets-host`");
const reachedOn = {};
for (const [platform, targets] of Object.entries(started)) {
  const reached = new Set();
  const reach = (name, target) => {
    const id = `${name}:${target}`;
    const spec = graph.get(name)?.targets?.[target];
    if (!spec || reached.has(id)) return;
    reached.add(id);
    for (const dependency of spec.dependsOn ?? []) {
      if (typeof dependency === "object") for (const other of dependency.projects ?? [name]) reach(other, dependency.target);
      else if (dependency.startsWith("^")) continue;
      else if (dependency.includes(":")) reach(...dependency.split(":"));
      else reach(name, dependency);
    }
  };
  for (const name of graph.keys()) for (const target of targets) reach(name, target);
  reachedOn[platform] = reached;
}

const accounted = new Set();
// A target another one runs in full through its recipe, so a lane runs it once, inside that
// carrier: still a target, accounted as the carrier's, which must itself be a lane's, and
// held to the recipe that names it and the carrier's own source that runs that recipe.
const carried = inventory.carried === undefined ? [] : isMapping(inventory.carried) ? Object.entries(inventory.carried) : undefined;
// Recipe, group and variable names are plain words; anything else is refused before it reaches a pattern.
const isName = (value) => typeof value === "string" && /^[A-Za-z0-9_-]+$/.test(value);
const literal = (text) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const isSelector = (value) => isMapping(value) && isName(value.env) && isName(value.group);
if (!carried || !carried.every(([entry, row]) => isEntrypoint(entry) && isEntrypoint(row?.by) && isName(row?.recipe) && typeof row?.source === "string" && isSelector(row?.selector))) {
  refuse("tools/ci/lanes.json's carried needs project:target keys, each with a by (project:target), a recipe name, a source file and a selector {env, group} of plain names");
}
for (const [entry, row] of carried) {
  accounted.add(entry);
  const [name, target] = entry.split(":");
  if (!graph.get(name)?.targets?.[target]) problems.push(`${entry}: carried by ${row.by}, but the target is gone`);
  if (!new RegExp(`^${literal(row.recipe)}:[^\n]*\n(?:[ \t]+[^\n]*\n)*?[ \t]+@?just nx run ${literal(entry)}$`, "m").test(justfile)) {
    problems.push(`${entry}: carried by ${row.by} through \`just ${row.recipe}\`, which no longer runs it`);
  }
  let source = "";
  try {
    source = readFileSync(join(ROOT, row.source), "utf8");
  } catch {
    problems.push(`${entry}: carried by ${row.by}, whose source ${row.source} is gone`);
  }
  // The carrier runs the source, selecting the group that holds the recipe: a carrier pointed at
  // another script or group would carry nothing, however present the recipe's name.
  const [byName, byTarget] = row.by.split(":");
  const options = graph.get(byName)?.targets?.[byTarget]?.options ?? {};
  const commands = [options.command, ...(options.commands ?? [])].filter((command) => typeof command === "string");
  if (!commands.some((command) => command.split(/\s+/).includes(row.source))) problems.push(`${entry}: its carrier ${row.by} no longer runs ${row.source}`);
  if (options.env?.[row.selector.env] !== row.selector.group) problems.push(`${entry}: its carrier ${row.by} no longer selects ${row.selector.env}=${row.selector.group}`);
  const group = new RegExp(`^\\s*"${literal(row.selector.group)}": \\(.*\\("${literal(row.recipe)}",\\)`, "m");
  if (source && !group.test(source)) problems.push(`${entry}: ${row.source}'s ${row.selector.group} group no longer runs \`just ${row.recipe}\``);
}
for (const [entry, row] of [...rows, ...added.map(([name, platforms]) => [name, { platforms }])]) {
  const now = row.now ?? entry;
  accounted.add(now);
  const [name, target] = now.split(":");
  const project = graph.get(name);
  if (!project) {
    problems.push(`${now}: project ${name} is gone, and its row says it runs on ${row.platforms.join(", ")}`);
    continue;
  }
  if (!project.targets?.[target]) {
    problems.push(`${now}: the target is gone, and its row says it runs on ${row.platforms.join(", ")}`);
    continue;
  }
  const owners = (project.tags ?? []).filter((tag) => tag.startsWith("platform:")).map((tag) => tag.slice("platform:".length));
  // The step that runs this project in each lane its row owes: its lane's, or the offline one.
  const lane = (project.tags ?? []).find((tag) => tag.startsWith("lane:"));
  const step = (project.tags ?? []).includes("tier:promoted") ? `--projects=tag:${lane}` : "--exclude=tag:tier:promoted";
  for (const platform of row.platforms) {
    if (owners.length > 0 && !owners.includes(platform)) problems.push(`${now}: no longer runs on ${platform}, which its row owes`);
    else if (!reachedOn[platform].has(now)) problems.push(`${now}: no lane reaches it on ${platform}: no recipe starts it and no target it serves depends on it`);
    else if (target !== "budgets-host" && !lanes[platform].includes(step)) problems.push(`${now}: test-${platform} has no step \`${step}\`, which its row owes`);
  }
}
for (const [entry, row] of carried) {
  if (!rows.some(([other, otherRow]) => (otherRow.now ?? other) === row.by)) problems.push(`${entry}: carried by ${row.by}, which no lane row names`);
}
for (const [name, project] of graph) {
  const tags = project.tags ?? [];
  for (const [target, spec] of Object.entries(project.targets ?? {})) {
    if (ENTRYPOINT.test(target) && spec.executor !== "nx:noop" && !accounted.has(`${name}:${target}`)) {
      problems.push(`${name}:${target}: not in tools/ci/lanes.json; add it under "added" with the platforms that owe it`);
    }
  }
  if (tags.includes("tier:promoted")) {
    const lane = tags.find((tag) => tag.startsWith("lane:"));
    if (!lane) problems.push(`${name}: tier:promoted with no lane: tag, so no lane step would run it`);
    else if (!ci.includes(`--projects=tag:${lane}`)) problems.push(`${name}: no step in ci.yml runs ${lane}`);
  }
}
for (const [command, platforms] of commands) {
  for (const platform of platforms) {
    if (!lanes[platform].includes(`run: ${command}`)) problems.push(`test-${platform} no longer runs \`${command}\``);
  }
}

// Whether a push to main starts a workflow: true, false, or undefined for a form this check
// does not read, which fails rather than being guessed at. Its forms are `on: <event>`,
// `on: [<event>, ...]`, and a block of `<event>:` keys, whose `push` has no filter,
// `branches: [main]` or tags alone.
function mainPushVerdict(text) {
  const on = /^on:([^\n]*)\n((?:[ #][^\n]*\n|\n)*)/m.exec(text);
  if (!on) return undefined;
  const inline = on[1].trim();
  if (inline !== "") return /^(?:\w+|\[\s*\w+(?:\s*,\s*\w+)*\s*\])$/.test(inline) ? /\bpush\b/.test(inline) : undefined;
  const events = on[2].split("\n").filter((line) => /^ {1,2}\S/.test(line) && !/^ *#/.test(line));
  if (events.length === 0 || !events.every((line) => /^ {2}\w+:[ \t]*$/.test(line))) return undefined;
  const push = /^ {2}push:[ \t]*\n((?: {4,}[^\n]*\n)*)/m.exec(on[2]);
  if (!push) return false;
  const filters = push[1].trimEnd();
  if (filters === "" || filters === "    branches: [main]") return true;
  return /^ {4}tags:/.test(filters) && !/^ {4}(?!tags:)\S/m.test(filters) ? false : undefined;
}
const startedByPullRequest = (text) => /^ {2}pull_request|^on:.*\bpull_request\b/m.test(text);

const listedNonCheck = new Map(nonCheck);
for (const path of listedNonCheck.keys()) {
  const text = read(path);
  if (mainPushVerdict(text) === false) problems.push(`${path}: listed as a non-check workflow, but no push to main starts it`);
  if (startedByPullRequest(text)) problems.push(`${path}: listed as a non-check workflow, but a pull request starts it`);
}
for (const name of readdirSync(join(ROOT, ".github/workflows"))) {
  const path = `.github/workflows/${name}`;
  const verdict = mainPushVerdict(read(path));
  if (verdict === undefined) problems.push(`${path}: cannot tell whether a push to main starts it; write it as \`on: <event>\`, a list of events, or a block of \`<event>:\` keys whose \`push\` has no filter, \`branches: [main]\` or tags alone`);
  else if (verdict && !listedNonCheck.has(path)) problems.push(`${path}: runs on push to main and is not in nonCheckWorkflows; CI's proof belongs in a pull request lane`);
}

if (problems.length > 0) {
  for (const problem of problems) console.error(`lane-inventory: ${problem}`);
  console.error("lane-inventory: restore the proof, or edit tools/ci/lanes.json in the change that deliberately retires it");
  // Not process.exit: a pipe takes its writes asynchronously, and exiting drops them.
  process.exitCode = 1;
}
