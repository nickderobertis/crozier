#!/usr/bin/env node
// The module-boundary rule, over the real project graph.
//
//   node scripts/check-project-boundaries.mjs PROJECT
//
// Checks every edge into and out of PROJECT. Each project's `lint` target runs
// it for itself, so a change that draws an edge fails the lint of the project
// that drew it, and a change to a project's tags fails that project's lint for
// the edges other projects already draw into it.
//
// An edge is a dependency of any kind the gate acts on, so one cannot hide in a
// form this check does not read:
//   * the graph Nx computes (`nx graph --file`): every `implicitDependencies`
//     entry;
//   * a target `dependsOn` entry naming another project's target;
//   * a target input naming a file under another project's root — Nx marks a
//     project affected by a change to any file its inputs name, so reading
//     another project's files is depending on it (Markdown aside: prose, not
//     behaviour);
//   * a Cargo path dependency between workspace members (`cargo metadata`).
//
// The rules live in nx.json's `boundaries` table:
//   * `allow`: each project carries exactly one `type:` tag, and may depend only
//     on projects whose `type:` tag its own type's entry lists;
//   * `unreachable`: a project carrying one of these tags (the expensive suites)
//     may be depended on only by a project carrying a tag its entry's `from`
//     lists, or by one tagged `measures:<that project>` — the one recorded
//     exception, for a suite that measures another;
//   * the `implicitDependencies` graph is acyclic.
//
// Quiet on success (one line); on failure, one line per violation naming the
// rule and the edge, then the fix.
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { dirname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const require = createRequire(join(root, "package.json"));
const NAME = "check-project-boundaries";

function fail(lines) {
  for (const line of lines) console.error(`${NAME}: ${line}`);
  process.exit(1);
}

/** `what`'s failure, with its own output and the next step, as a failed run. */
function failedRun(what, error, action) {
  const output = [error?.stdout, error?.stderr ?? error?.message ?? error]
    .map((stream) => String(stream ?? "").trim())
    .filter(Boolean)
    .join("\n");
  fail([`${what} failed: ${output || "no output"}`, `ACTION: ${action}`]);
}

/** The project graph exactly as Nx computes it for this checkout. */
function nxGraph() {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-graph-"));
  try {
    const manifest = require.resolve("nx/package.json");
    const nx = join(dirname(manifest), require(manifest).bin.nx);
    const file = join(scratch, "graph.json");
    execFileSync(process.execPath, [nx, "graph", `--file=${file}`], {
      cwd: root,
      env: { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true" },
      stdio: ["ignore", "pipe", "pipe"],
      maxBuffer: 64 * 1024 * 1024,
    });
    const graph = JSON.parse(readFileSync(file, "utf8")).graph;
    const strings = (value) => Array.isArray(value) && value.every((item) => typeof item === "string");
    // A `dependsOn` entry is `target`, `project:target`, or { target, projects? }.
    const dependency = (dep) =>
      typeof dep === "string" ||
      (typeof dep?.target === "string" &&
        (dep.projects === undefined || typeof dep.projects === "string" || strings(dep.projects)));
    const input = (entry) => typeof entry === "string" || (entry !== null && typeof entry === "object" && !Array.isArray(entry));
    const target = (value) =>
      value !== null &&
      typeof value === "object" &&
      !Array.isArray(value) &&
      (value.dependsOn === undefined || (Array.isArray(value.dependsOn) && value.dependsOn.every(dependency))) &&
      (value.inputs === undefined || (Array.isArray(value.inputs) && value.inputs.every(input)));
    const namedInputs = (value) =>
      value === undefined ||
      (value !== null && typeof value === "object" && !Array.isArray(value) &&
        Object.values(value).every((entries) => Array.isArray(entries) && entries.every(input)));
    const shaped =
      graph?.nodes &&
      typeof graph.nodes === "object" &&
      graph.dependencies &&
      typeof graph.dependencies === "object" &&
      !Array.isArray(graph.dependencies) &&
      Object.values(graph.nodes).every(
        (node) =>
          typeof node?.data?.root === "string" &&
          (node.data.tags === undefined ||
            (Array.isArray(node.data.tags) && node.data.tags.every((tag) => typeof tag === "string"))) &&
          (node.data.targets === undefined ||
            (typeof node.data.targets === "object" &&
              !Array.isArray(node.data.targets) &&
              Object.values(node.data.targets).every(target))) &&
          namedInputs(node.data.namedInputs),
      ) &&
      Object.values(graph.dependencies).every(
        (deps) => Array.isArray(deps) && deps.every((dep) => typeof dep?.target === "string"),
      );
    if (!shaped) throw new Error("its `nodes` / `dependencies` are not the shape this check reads");
    return graph;
  } catch (error) {
    return failedRun(
      "computing the Nx project graph (`nx graph`)",
      error,
      "run `just bootstrap` to install the pinned Nx, then fix the project.json the message names",
    );
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
}

/** Cargo's path dependencies between workspace members, as [fromDir, toDir]. */
function cargoEdges() {
  if (!existsSync(join(root, "Cargo.toml"))) return [];
  let metadata;
  try {
    metadata = JSON.parse(
      execFileSync("cargo", ["metadata", "--format-version", "1", "--no-deps", "--locked"], {
        cwd: root,
        encoding: "utf8",
        maxBuffer: 64 * 1024 * 1024,
        stdio: ["ignore", "pipe", "pipe"],
      }),
    );
  } catch (error) {
    return failedRun(
      "reading the Cargo workspace (`cargo metadata`)",
      error,
      "fix the Cargo.toml the message names (`cargo metadata --no-deps` reproduces it)",
    );
  }
  const shaped =
    Array.isArray(metadata?.packages) &&
    metadata.packages.every(
      (pkg) =>
        typeof pkg?.name === "string" &&
        typeof pkg.manifest_path === "string" &&
        (pkg.dependencies === undefined ||
          (Array.isArray(pkg.dependencies) &&
            pkg.dependencies.every(
              (dep) => typeof dep?.name === "string" && (dep.path === undefined || typeof dep.path === "string"),
            ))),
    );
  if (!shaped) {
    failedRun(
      "reading the Cargo workspace",
      "its `packages` are not a list of { name, manifest_path, dependencies: [{ name, path? }] }",
      "check `cargo metadata --format-version 1 --no-deps` and the cargo on PATH",
    );
  }
  const edges = [];
  for (const pkg of metadata.packages) {
    for (const dep of pkg.dependencies ?? []) {
      if (typeof dep.path === "string") {
        edges.push([dirname(pkg.manifest_path), dep.path, `Cargo path dependency ${pkg.name} -> ${dep.name}`]);
      }
    }
  }
  return edges;
}

let nxJson;
try {
  nxJson = JSON.parse(readFileSync(join(root, "nx.json"), "utf8"));
} catch (error) {
  fail([`nx.json could not be read: ${error.message}`, "ACTION: restore a readable, valid nx.json"]);
}
const boundaries = nxJson?.boundaries;
const allow = boundaries?.allow;
const unreachable = boundaries?.unreachable;
const typeTag = /^type:[a-z][a-z0-9-]*$/;
const wellFormed =
  allow !== null &&
  typeof allow === "object" &&
  !Array.isArray(allow) &&
  Object.entries(allow).every(
    ([type, allowed]) =>
      typeTag.test(type) &&
      Array.isArray(allowed) &&
      allowed.every((target) => typeof target === "string" && Object.hasOwn(allow, target)),
  ) &&
  unreachable !== null &&
  typeof unreachable === "object" &&
  !Array.isArray(unreachable) &&
  Object.entries(unreachable).every(
    ([tag, entry]) =>
      /^[a-z][a-z0-9-]*:[a-z0-9:-]+$/.test(tag) &&
      typeof entry?.rule === "string" &&
      entry.rule.length > 0 &&
      typeof entry.why === "string" &&
      Array.isArray(entry.from) &&
      entry.from.every((from) => typeof from === "string" && /^[a-z][a-z0-9-]*:[a-z0-9:-]+$/.test(from)),
  );
const named = nxJson?.namedInputs;
if (
  named !== undefined &&
  (named === null || typeof named !== "object" || Array.isArray(named) ||
    !Object.values(named).every((entries) => Array.isArray(entries)))
) {
  fail(['nx.json\'s "namedInputs" is not a map of input names to lists', "ACTION: restore nx.json's namedInputs from git"]);
}
if (!wellFormed) {
  fail([
    'nx.json has no well-formed "boundaries" table to enforce',
    "ACTION: restore `boundaries.allow` (one `type:` tag per key, each listing the `type:` tags it may depend on) and `boundaries.unreachable` (tag -> { rule, from: [tags], why })",
  ]);
}

const requested = process.argv.slice(2);
if (requested.length !== 1) {
  fail(["usage: node scripts/check-project-boundaries.mjs PROJECT", "ACTION: name the project whose edges to check"]);
}
const [subject] = requested;

const graph = nxGraph();
const projects = graph.nodes;
if (!Object.hasOwn(projects, subject)) {
  fail([
    `no project named ${subject} in the Nx graph (projects: ${Object.keys(projects).sort().join(", ")})`,
    "ACTION: pass a listed project, or add a project.json naming it",
  ]);
}

const problems = [];
const tagsOf = (name) => projects[name].data.tags ?? [];
const typeOf = {};
for (const name of Object.keys(projects)) {
  const types = tagsOf(name).filter((tag) => tag.startsWith("type:"));
  if (types.length !== 1) {
    if (name === subject) problems.push(`${name} carries ${types.length} type: tags (${types.join(", ") || "none"}); give it exactly one`);
  } else if (!Object.hasOwn(allow, types[0])) {
    if (name === subject) problems.push(`${name} is tagged ${types[0]}, which nx.json "boundaries.allow" does not declare`);
  } else {
    typeOf[name] = types[0];
  }
}

// Longest-root-first, so a file maps to the deepest project that owns it, as
// Nx itself assigns files to projects.
const roots = Object.entries(projects)
  .map(([name, node]) => [name, node.data.root.replace(/\/+$/, "")])
  .sort((a, b) => b[1].length - a[1].length);
function ownerOf(path) {
  const normalized = path.split(sep).join("/").replace(/^\.\//, "");
  for (const [name, projectRoot] of roots) {
    if (projectRoot === "" || projectRoot === ".") return name;
    if (normalized === projectRoot || normalized.startsWith(`${projectRoot}/`)) return name;
  }
  return undefined;
}

// Named inputs expand recursively; a `^name` input reads the dependencies'
// files through an edge that is already counted, so it adds none.
const namedInputs = (name) => ({ ...(nxJson.namedInputs ?? {}), ...(projects[name].data.namedInputs ?? {}) });
function workspacePaths(name, inputs, seen = new Set()) {
  const paths = [];
  for (const input of inputs ?? []) {
    if (typeof input !== "string") continue;
    if (input.startsWith("{workspaceRoot}/")) {
      const pattern = input.slice("{workspaceRoot}/".length);
      // Markdown is prose every project carries (its AGENTS.md); a check that
      // reads all of it, like the corpus-licensing lint, depends on none of them.
      if (pattern.endsWith(".md")) continue;
      // The fixed directory prefix before any glob character names where the
      // files read live; the rest says whether the glob can descend from there.
      const glob = pattern.search(/[*?[{]/);
      const fixed = glob < 0 ? pattern : pattern.slice(0, glob);
      const rest = glob < 0 ? "" : pattern.slice(glob);
      const prefix = glob < 0 ? pattern : fixed.slice(0, fixed.lastIndexOf("/") + 1);
      paths.push({ path: prefix.replace(/\/+$/, ""), descends: rest.includes("**") || rest.includes("/") });
    } else if (!input.startsWith("^") && !input.startsWith("{") && !input.startsWith("!")) {
      const named = namedInputs(name)[input];
      if (named && !seen.has(input)) {
        seen.add(input);
        paths.push(...workspacePaths(name, named, seen));
      }
    }
  }
  return paths;
}

const edges = new Map();
function addEdge(source, target, how) {
  if (!source || !target || source === target) return;
  const key = `${source} -> ${target}`;
  if (!edges.has(key)) edges.set(key, { source, target, how });
}
for (const [source, deps] of Object.entries(graph.dependencies)) {
  for (const dep of deps) {
    if (Object.hasOwn(projects, dep.target)) addEdge(source, dep.target, `implicitDependencies (${dep.type})`);
  }
}
for (const [name, node] of Object.entries(projects)) {
  for (const [targetName, target] of Object.entries(node.data.targets ?? {})) {
    for (const dep of target.dependsOn ?? []) {
      const named = typeof dep === "string" ? (dep.includes(":") ? [dep.split(":")[0]] : []) : dep.projects ?? [];
      for (const other of [named].flat()) {
        if (Object.hasOwn(projects, other)) addEdge(name, other, `${name}:${targetName} dependsOn ${other}:${dep.target ?? dep.split(":")[1]}`);
      }
    }
    const inputs = target.inputs ?? nxJson.targetDefaults?.[targetName]?.inputs ?? ["default"];
    for (const { path, descends } of workspacePaths(name, inputs)) {
      // A glob that descends from a directory holding project roots reads them.
      const owners = new Set([ownerOf(path)]);
      for (const [other, projectRoot] of roots) {
        if (descends && (path === "" || projectRoot.startsWith(`${path}/`))) owners.add(other);
      }
      for (const owner of owners) addEdge(name, owner, `${name}:${targetName} input {workspaceRoot}/${path}`);
    }
  }
}
for (const [fromDir, toDir, how] of cargoEdges()) {
  const from = ownerOf(relative(root, fromDir)) ?? cargoOwner(fromDir);
  const to = ownerOf(relative(root, toDir)) ?? cargoOwner(toDir);
  addEdge(from, to, how);
}
// The root package's manifest sits above every project root; the project whose
// metadata names that directory as `cargoManifestDir` owns it.
function cargoOwner(dir) {
  const rel = relative(root, dir);
  for (const [name, node] of Object.entries(projects)) {
    const manifest = node.data.metadata?.cargoManifestDir;
    if (typeof manifest === "string" && manifest.replace(/^\.\/?/, "") === rel) return name;
  }
  return undefined;
}

for (const { source, target, how } of edges.values()) {
  if (source !== subject && target !== subject) continue;
  const sourceType = typeOf[source];
  const targetType = typeOf[target];
  if (sourceType && targetType && !allow[sourceType].includes(targetType)) {
    problems.push(
      `type-allow: ${source} (${sourceType}) may not depend on ${target} (${targetType}) — via ${how}; nx.json boundaries.allow["${sourceType}"] lists ${allow[sourceType].join(", ") || "nothing"}`,
    );
  }
  for (const [tag, entry] of Object.entries(unreachable)) {
    if (!tagsOf(target).includes(tag)) continue;
    const allowed = tagsOf(source).some((t) => entry.from.includes(t)) || tagsOf(source).includes(`measures:${target}`);
    if (!allowed) {
      problems.push(`${entry.rule}: ${source} may not depend on ${target} (tagged ${tag}) — via ${how}; ${entry.why}`);
    }
  }
}

// Cycles through the subject in the implicit graph.
const adjacency = {};
for (const [source, deps] of Object.entries(graph.dependencies)) {
  adjacency[source] = deps.map((dep) => dep.target).filter((t) => Object.hasOwn(projects, t));
}
function pathBack(from, to, seen = new Set()) {
  if (from === to) return [to];
  if (seen.has(from)) return undefined;
  seen.add(from);
  for (const next of adjacency[from] ?? []) {
    const rest = pathBack(next, to, seen);
    if (rest) return [from, ...rest];
  }
  return undefined;
}
for (const next of adjacency[subject] ?? []) {
  const cycle = pathBack(next, subject);
  if (cycle) problems.push(`acyclic-graph: ${[subject, ...cycle].join(" -> ")} is a cycle`);
}

if (problems.length > 0) {
  fail([
    ...problems,
    "ACTION: remove the edge, or — if the dependency is real and the rule is wrong for it — change the tags or nx.json boundaries with the reason recorded in that project's AGENTS.md",
  ]);
}
console.log(`${NAME}: ${subject} ok (${[...edges.values()].filter((e) => e.source === subject || e.target === subject).length} edges)`);
