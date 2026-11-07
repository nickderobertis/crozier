#!/usr/bin/env node
// Every test, build, coverage and budget entrypoint against tools/ci/lanes.json and ci.yml,
// so none can leave the pull request flow unnoticed: a row whose target or project is gone,
// or whose platform was dropped, a new target with no row, a promoted project with no lane,
// a lane no step runs, or a lost platform command.
//
// Exit 0 when they reconcile; 1 naming each difference; 2 when a file cannot be read or has the wrong shape.
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
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
const isPlatformList = (list) => Array.isArray(list) && list.every((platform) => ["linux", "macos", "windows"].includes(platform));
if (!rows || !commands || !Array.isArray(inventory.added) || !inventory.added.every((entry) => /^[^:]+:[^:]+$/.test(entry))
  || !rows.every(([entry, row]) => /^[^:]+:[^:]+$/.test(row?.now ?? entry) && isPlatformList(row?.platforms)) || !commands.every(([, list]) => isPlatformList(list))) {
  refuse("tools/ci/lanes.json needs entrypoints and commands naming project:target and linux, macos or windows, and an added list");
}
const ci = read(".github/workflows/ci.yml");
const problems = [];
const at = (from, to) => ci.slice(ci.indexOf(`  ${from}:\n`), to ? ci.indexOf(`  ${to}:\n`) : undefined);
const lanes = { linux: at("test-linux", "test-windows"), windows: at("test-windows", "test-macos"), macos: at("test-macos", "gate") };

// What the lanes' recipes start, through every `dependsOn`: a row whose target nothing starts
// runs nowhere, however present it is.
const justfile = read("justfile");
const LANE_TARGETS = [...justfile.matchAll(/^lane-(?:test|budgets-host) \*args:\n.*--targets=(.+)$/gm), ...justfile.matchAll(/^lane_test_targets := (.+)$/gm)]
  .flatMap((match) => match[1].match(/[a-z][a-z,-]*[a-z]/g) ?? [])
  .flatMap((list) => list.split(","))
  .filter((target) => ENTRYPOINT.test(target));
if (!LANE_TARGETS.includes("test") || !LANE_TARGETS.includes("budgets-host")) {
  console.error("lane-inventory: cannot read the lane recipes' target lists from the justfile");
  console.error("lane-inventory: keep `lane_test_targets` and the `lane-*` recipes' --targets= lists readable");
  process.exit(2);
}
const reached = new Set();
function reach(name, target) {
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
}
for (const name of graph.keys()) for (const target of LANE_TARGETS) reach(name, target);

const accounted = new Set(inventory.added);
for (const [entry, row] of rows) {
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
  if (!reached.has(now)) problems.push(`${now}: no lane reaches it: no recipe starts it and no target it serves depends on it`);
  const owners = (project.tags ?? []).filter((tag) => tag.startsWith("platform:")).map((tag) => tag.slice("platform:".length));
  for (const platform of row.platforms) {
    if (owners.length > 0 && !owners.includes(platform)) problems.push(`${now}: no longer runs on ${platform}, which its row owes`);
  }
}
for (const added of inventory.added) {
  const [name, target] = added.split(":");
  if (!graph.get(name)?.targets?.[target]) problems.push(`${added}: listed under "added", and the target is gone`);
}
for (const [name, project] of graph) {
  const tags = project.tags ?? [];
  for (const [target, spec] of Object.entries(project.targets ?? {})) {
    if (ENTRYPOINT.test(target) && spec.executor !== "nx:noop" && !accounted.has(`${name}:${target}`)) {
      problems.push(`${name}:${target}: not in tools/ci/lanes.json; add it under "added"`);
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

if (problems.length > 0) {
  for (const problem of problems) console.error(`lane-inventory: ${problem}`);
  console.error("lane-inventory: restore the proof, or edit tools/ci/lanes.json in the change that deliberately retires it");
  // Not process.exit: a pipe takes its writes asynchronously, and exiting drops them.
  process.exitCode = 1;
}
