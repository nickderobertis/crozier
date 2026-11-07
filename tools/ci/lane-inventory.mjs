#!/usr/bin/env node
// Every test, build, coverage and budget entrypoint against tools/ci/lanes.json and ci.yml,
// so none can leave the pull request flow unnoticed: a row whose target or project is gone,
// or whose platform was dropped, a new target with no row, a promoted project with no lane,
// a lane no step runs, or a lost platform command.
//
// Exit 0 when they reconcile; 1 naming each difference; 2 when a file cannot be read.
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const ENTRYPOINT = /^(test|test-.*|budgets|budgets-host|coverage|build|cold-registry-build)$/;

function read(path) {
  try {
    return readFileSync(join(ROOT, path), "utf8");
  } catch (error) {
    console.error(`lane-inventory: cannot read ${path}: ${error.message}`);
    console.error("lane-inventory: restore the file, or run this from a full checkout");
    process.exit(2);
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
  const project = JSON.parse(text.replace(/^\s*\/\/.*$/gm, ""));
  graph.set(project.name, project);
}

const inventory = JSON.parse(read("tools/ci/lanes.json"));
const ci = read(".github/workflows/ci.yml");
const problems = [];
const at = (from, to) => ci.slice(ci.indexOf(`  ${from}:\n`), to ? ci.indexOf(`  ${to}:\n`) : undefined);
const lanes = { linux: at("test-linux", "test-windows"), windows: at("test-windows", "test-macos"), macos: at("test-macos", "gate") };

const accounted = new Set(inventory.added);
for (const [entry, row] of Object.entries(inventory.entrypoints)) {
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
for (const [command, platforms] of Object.entries(inventory.commands)) {
  for (const platform of platforms) {
    if (!lanes[platform].includes(`run: ${command}`)) problems.push(`test-${platform} no longer runs \`${command}\``);
  }
}

if (problems.length > 0) {
  for (const problem of problems) console.error(`lane-inventory: ${problem}`);
  console.error("lane-inventory: restore the proof, or edit tools/ci/lanes.json in the change that deliberately retires it");
  process.exit(1);
}
