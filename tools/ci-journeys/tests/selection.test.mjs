// Which suites a change really executes, through the real gate and Nx. The first group runs
// over a scratch copy of this repository's real graph: each project keeps its real name,
// tags, inputs and dependencies, and each runnable target becomes a recorder (or a failure,
// on request), so a journey observes what would run for a real path. The second group runs
// a tiny real generator with real suites, to see edits reach them and caches give way.
// Suite-inventory reconciliation is the third.
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { cpSync, existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, symlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { connect } from "node:net";
import { serveResults } from "../../ci/result-cache.mjs";
import { REPO, write } from "./support.mjs";

/** This environment without what an enclosing Nx task or sweep set, which would change a journey's answers. */
function clean(env) {
  const merged = { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true", ...env };
  for (const name of Object.keys(merged)) if (/^(NX_(SKIP_NX_CACHE|WORKSPACE_ROOT|TASK_|PROFILE|CLI_SET|LOAD_DOT|SELF_HOSTED_)|CROZIER_RESULT_CACHE$)/.test(name) && !(name in env)) delete merged[name];
  return merged;
}
// Nx reuses an archived file hash whenever a file's mtime matches, and that mtime is in whole
// seconds off Windows: an edit in the second of the last run would keep the old hash.
const forgetFileHashes = (root) => rmSync(join(root, ".nx/workspace-data/nx_files.nxt"), { force: true });
const gitIn = (cwd, ...args) => execFileSync("git", ["-c", "user.name=t", "-c", "user.email=t@example.com", ...args], { cwd, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
const tracked = () => execFileSync("git", ["ls-files", "--", "*project.json"], { cwd: REPO, encoding: "utf8" }).trim().split("\n");
const readProject = (path) => JSON.parse(readFileSync(join(REPO, path), "utf8").replace(/^\s*\/\/.*$/gm, ""));

const RECORD = `node -e "const f=require('fs');f.appendFileSync(process.env.RAN_LOG,process.argv[1]+'\\n');if((process.env.FAIL_TASK||'')===process.argv[1])process.exit(7)"`;

/** The real graph, with every runnable target replaced by a recorder of `project:target`. */
function realGraph(t) {
  const root = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), "crozier-graph-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  for (const path of ["justfile", "nx.json", "package.json", "tools/ci/lane-inventory.mjs", "tools/ci/lanes.json", "tools/ci/project-files-digest.mjs", "tools/ci/gate.mjs", "tools/ci/result-cache.mjs", "tools/ci/gate-timing.mjs", "tools/ci/gate-timing/core.mjs", "tools/ci/ci-tier.mjs", "tests/corpus_match/corpus_offline_test.py"]) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    cpSync(join(REPO, path), join(root, path));
  }
  cpSync(join(REPO, ".github/workflows"), join(root, ".github/workflows"), { recursive: true });
  // Its line endings, or a checkout here turns the workflows CRLF on a Windows runner's core.autocrlf.
  cpSync(join(REPO, ".gitattributes"), join(root, ".gitattributes"));
  symlinkSync(join(REPO, "node_modules"), join(root, "node_modules"), "junction");
  for (const path of tracked()) {
    const project = readProject(path);
    for (const [name, target] of Object.entries(project.targets ?? {})) {
      const inputs = target.inputs?.filter((input) => typeof input === "string" || !("runtime" in input));
      const id = `${project.name}:${name}`;
      project.targets[name] = id === "lane-inventory:lint"
        ? { command: "node tools/ci/lane-inventory.mjs", cache: false, inputs }
        : target.executor === "nx:noop"
        ? { ...target, ...(inputs ? { inputs } : {}) }
        : { command: `${RECORD} ${id}`, cache: false, ...(target.dependsOn ? { dependsOn: target.dependsOn } : {}), ...(inputs ? { inputs } : {}), ...(target.parallelism === false ? { parallelism: false } : {}) };
    }
    write(root, { [path]: JSON.stringify(project) });
  }
  const nx = JSON.parse(readFileSync(join(root, "nx.json"), "utf8"));
  nx.namedInputs.generator = nx.namedInputs.generator.filter((input) => typeof input === "string");
  write(root, { "nx.json": JSON.stringify(nx), ".gitignore": "/node_modules\n/.nx\n/ran.log\n" });
  gitIn(root, "init", "--quiet", "--initial-branch=main");
  gitIn(root, "add", "-A");
  gitIn(root, "commit", "--quiet", "-m", "base");
  return { root, base: gitIn(root, "rev-parse", "HEAD") };
}

/** Run one lane recipe after `edit`, in a clean tree, returning what really executed. */
function lane(graph, edit, recipe, args = [], env = {}) {
  const { root, base } = graph;
  gitIn(root, "checkout", "--quiet", "--detach", base);
  gitIn(root, "clean", "-fdq");
  if (typeof edit === "function") edit(root);
  else write(root, Object.fromEntries(edit.map((path) => [path, path === "rust-toolchain.toml" ? `${readFileSync(join(REPO, path), "utf8")}# edited\n` : `edited ${path}\n`])));
  gitIn(root, "add", "-A");
  gitIn(root, "commit", "--quiet", "--allow-empty", "-m", "edit");
  const log = join(root, "ran.log");
  rmSync(log, { force: true });
  const run = spawnSync("just", [...[recipe].flat(), ...args], {
    cwd: root, encoding: "utf8", shell: process.platform === "win32",
    env: clean({ NX_BASE: base, RAN_LOG: log, ...env }),
  });
  const ran = existsSync(log) ? readFileSync(log, "utf8").trim().split("\n") : [];
  // Nx may lose a fast task's output under load, while its status always holds.
  const inventory = spawnSync(process.execPath, ["tools/ci/lane-inventory.mjs"], { cwd: root, encoding: "utf8" });
  gitIn(root, "add", "-A");
  gitIn(root, "reset", "--quiet", "--hard", "HEAD");
  gitIn(root, "checkout", "--quiet", "--detach", base);
  return { inventory, status: run.status, output: `${run.stdout}${run.stderr}`, ran: new Set(ran), projects: /gate: projects: (.*)/.exec(run.stdout)?.[1].split(", ") ?? [] };
}
const offline = ["lane-test", ["--platform=windows", "--exclude=tag:tier:promoted"]];
const every = (ran, names) => names.filter((name) => !ran.has(name));

// Every full journey a change to what crozier generates can alter.
const JOURNEYS = ["crozier:test", "crozier-e2e:test", "nested-discriminator-golden:test", "surface-census:test-census", "golden-reach:test-reach", "golden-reach:test-reach-portable"];
const PROMOTED = {
  "tag:lane:sdk-env": ["sdk-env:test", "runtime:test", "nested-discriminator-runtime:test"],
  "tag:lane:live": ["live-e2e:test", "corpus-match:test-offline", "corpus-offline-tools:test", "corpus-match-selection:test"],
};

test("a generator, template, lockfile or toolchain edit executes every dependent full journey", (t) => {
  const graph = realGraph(t);
  for (const edit of ["src/lib.rs", "templates/client.py.jinja", "Cargo.lock", "rust-toolchain.toml", ".ruff-version"]) {
    const { ran, status, output } = lane(graph, [edit], "lane-test", ["--exclude=tag:tier:promoted"]);
    assert.equal(status, 0, output);
    assert.deepEqual(every(ran, JOURNEYS), [], `${edit} left journeys unrun:\n${output}`);
    for (const [tag, suites] of Object.entries(PROMOTED)) {
      const promoted = lane(graph, [edit], "lane-test", [`--projects=${tag}`, "--platform=linux"]);
      assert.equal(promoted.status, 0, promoted.output);
      assert.deepEqual(every(promoted.ran, suites), [], `${edit}, ${tag}`);
    }
  }
});

test("a shared-harness or corpus edit executes every journey built on it", (t) => {
  const graph = realGraph(t);
  for (const [edit, owners] of [
    ["tests/support/departures_ledger.rs", ["crozier-e2e:test", "golden-reach:test-reach"]],
    ["tests/fixtures/CORPUS.md", ["crozier-e2e:test", "surface-census:test-census", "golden-reach:test-reach"]],
    ["tests/fixtures/discord.com/expected/README.md", ["crozier-e2e:test", "surface-census:test-census", "golden-reach:test-reach"]],
  ]) {
    const { ran, status, output } = lane(graph, [edit], ...offline);
    assert.equal(status, 0, output);
    assert.deepEqual(every(ran, owners), [], `${edit}:\n${output}`);
  }
  const corpus = lane(graph, ["tests/fixtures/CORPUS.md"], "lane-test", ["--projects=tag:lane:live", "--platform=linux"]);
  assert.deepEqual(every(corpus.ran, ["corpus-match:test-offline"]), [], corpus.output);
  // test-offline runs the byte-match and its strict form through their recipes, so the lane
  // never runs them a second time beside it (tools/ci/lanes.json `carried`).
  for (const name of ["corpus-match:test-match", "corpus-match:test-strict"]) assert.ok(!corpus.ran.has(name), `${name} ran twice:\n${corpus.output}`);
});

// Every target that byte-compares crozier's output with a committed golden.
const GOLDEN_COMPARISONS = ["crozier-e2e:test", "nested-discriminator-golden:test", "corpus-match:test-offline", "corpus-match:test-match", "corpus-match:test-strict"];
const LINUX_LANE = ["lane-test", ["--platform=linux", "--include-promoted"]];

test("delivery tooling reruns no golden byte comparison, and every generator input still does (#817)", (t) => {
  const graph = realGraph(t);
  for (const edit of [
    "scripts/install.sh",
    ".github/workflows/ci-caches.yml",
    "tools/ci/require-tools.mjs",
    "tools/llmlint/llmlint-diff.py",
    "tools/llmlint-resolution/tests/judged_lint_job_test.py",
    "tools/fern-refusals/fern-refusals.py",
    "tools/fern-refusals-strict/AGENTS.md",
    "screenshots/capture-visual-docs.sh",
  ]) {
    const { ran, status, output } = lane(graph, [edit], ...LINUX_LANE);
    assert.equal(status, 0, output);
    const compared = GOLDEN_COMPARISONS.filter((name) => ran.has(name));
    assert.deepEqual(compared, [], `${edit} reran golden comparisons whose inputs it is not:\n${[...ran].join(" ")}`);
  }
  for (const edit of ["src/lib.rs", "assets/departures.yml", "tests/fixtures/discord.com/expected/README.md", "tests/fixtures/corpus-sources/swagger-petstore/openapi.yaml"]) {
    const { ran, status, output } = lane(graph, [edit], ...LINUX_LANE);
    assert.equal(status, 0, output);
    assert.deepEqual(every(ran, ["crozier-e2e:test", "corpus-match:test-offline"]), [], `${edit} left a golden comparison unrun:\n${output}`);
  }
});

test("a census-only edit runs the census, not the reach or golden suites; a reach-only edit the reverse", (t) => {
  const graph = realGraph(t);
  // Windows holds no Python floor, so this is exactly what the two edits own. On Linux and
  // macOS the floor also needs every tooling suite's coverage (next test).
  const census = lane(graph, ["tools/surface-census/apis-guru-gap-screen.py"], ...offline);
  assert.equal(census.status, 0, census.output);
  assert.ok(census.ran.has("surface-census:test-census"), census.output);
  for (const name of ["golden-reach:test-reach", "golden-reach:test-reach-portable", "crozier-e2e:test", "crozier:test", "surface-reach:test-handwritten-reach"]) {
    assert.ok(!census.ran.has(name), `${name} cannot read the gap screen:\n${[...census.ran].join(" ")}`);
  }
  const reach = lane(graph, ["tools/golden-reach/tests/golden_reach_test.py"], ...offline);
  assert.equal(reach.status, 0, reach.output);
  assert.deepEqual(every(reach.ran, ["golden-reach:test-reach", "golden-reach:test-reach-portable"]), [], reach.output);
  for (const name of ["surface-census:test-census", "crozier-e2e:test", "crozier:test", "fern-goldens:test"]) {
    assert.ok(!reach.ran.has(name), `${name} cannot read the reach suite:\n${[...reach.ran].join(" ")}`);
  }
});

test("a script both read reaches both, and the coverage floor takes every suite's data, never a missing one", (t) => {
  const graph = realGraph(t);
  const shared = lane(graph, ["tools/surface-census/openapi-surface-census.py"], ...offline);
  assert.deepEqual(every(shared.ran, ["surface-census:test-census", "golden-reach:test-reach", "crozier-e2e:test"]), [], shared.output);
  const floored = lane(graph, ["tools/golden-reach/tests/golden_reach_test.py"], "lane-test", ["--platform=linux", "--exclude=tag:tier:promoted"]);
  assert.equal(floored.status, 0, floored.output);
  const members = readProject("tools/python-workspace/project.json").implicitDependencies;
  assert.ok(members.includes("golden-reach"), "the floor combines the split suite's coverage");
  assert.ok(floored.ran.has("python-workspace:coverage"), floored.output);
  const owedTests = members.flatMap((name) => {
    const path = tracked().find((candidate) => readProject(candidate).name === name);
    const { targets } = readProject(path);
    return Object.entries(targets).filter(([target, spec]) => target.startsWith("test") && spec.executor !== "nx:noop").map(([target]) => `${name}:${target}`);
  });
  assert.deepEqual(every(floored.ran, owedTests), [], "the floor must read every member's data");
  assert.ok(!floored.ran.has("crozier-e2e:test") && !floored.ran.has("crozier:test"), "the Python floor reaches no Rust suite");
});

test("every census script is a declared input of its readers, or one no other suite loads", () => {
  const { namedInputs } = JSON.parse(readFileSync(join(REPO, "nx.json"), "utf8"));
  const declared = new Set(namedInputs.censusScripts.map((input) => input.replace("{workspaceRoot}/tools/surface-census/", "")));
  const onlyCensus = new Set(["apis-guru-gap-screen.py", "update-predicate-grammar.py", "probe-differential-isolation.py"]);
  for (const name of readdirSync(join(REPO, "tools/surface-census"))) {
    if (name.endsWith(".py") || name.endsWith(".sh")) assert.ok(declared.has(name) || onlyCensus.has(name), `${name}: add it to censusScripts in nx.json, or its readers never rerun`);
  }
});

test("a tool journey's surface runs that journey without paying for the golden suite", (t) => {
  const graph = realGraph(t);
  for (const edit of ["action.yml", "scripts/update-major-tag.sh", "docs/migrating-from-fern.md", "tools/github-action/run.sh"]) {
    const { ran, output } = lane(graph, [edit], ...offline);
    assert.ok(ran.has("crozier-tool-journeys:test"), `${edit}:\n${output}`);
    assert.ok(!ran.has("crozier-e2e:test"), `${edit} must not run crozier-e2e:\n${[...ran].join(" ")}`);
  }
});

test("an unrelated documentation edit runs none of the expensive suites", (t) => {
  const graph = realGraph(t);
  const docs = lane(graph, ["docs/float-literal-parity.md"], "lane-test", ["--platform=linux", "--exclude=tag:tier:promoted"]);
  assert.equal(docs.status, 0, docs.output);
  for (const name of [...JOURNEYS, "fern-goldens-weekly:test", "witness-search:test-acquisition", "crozier-tool-journeys:test"]) assert.ok(!docs.ran.has(name), `${name}:\n${[...docs.ran].join(" ")}`);
  for (const tag of Object.keys(PROMOTED)) {
    const promoted = lane(graph, ["docs/float-literal-parity.md"], "lane-test", [`--projects=${tag}`, "--platform=linux"]);
    assert.equal(promoted.ran.size, 0, `${tag}:\n${[...promoted.ran].join(" ")}`);
  }
});

test("a selected suite's failure fails the lane, and nothing else stands in for it", (t) => {
  const graph = realGraph(t);
  const failed = lane(graph, ["src/lib.rs"], ...offline, { FAIL_TASK: "crozier-e2e:test" });
  assert.notEqual(failed.status, 0, failed.output);
  assert.match(failed.output, /gate: a target failed/);
  const passed = lane(graph, ["docs/float-literal-parity.md"], ...offline, { FAIL_TASK: "crozier-e2e:test" });
  assert.equal(passed.status, 0, "an unselected suite cannot fail the lane");
});

test("the lint and test lanes are disjoint in what they execute, and no target runs twice on a platform", (t) => {
  const graph = realGraph(t);
  const edit = ["src/lib.rs"];
  const lint = lane(graph, edit, "lane-lint");
  assert.equal(lint.status, 0, lint.output);
  for (const name of lint.ran) assert.ok(!/:(test|test-.*|budgets.*|coverage|build|cold-registry-build)$/.test(name), `lint ran ${name}`);
  // The recipe's target list keys on the host's OS, and this asks what Linux's lane owes, whichever
  // host runs the question: Windows' list adds typecheck, which lint runs on another platform.
  const linuxTargets = /else \{ "([^"]+)" \}/.exec(/^lane_test_targets := .*$/m.exec(readFileSync(join(REPO, "justfile"), "utf8"))[0])[1];
  for (const [platform, owed] of [["linux", ["--platform=linux"]]]) {
    const lanes = [["--exclude=tag:tier:promoted"], ["--projects=tag:lane:sdk-env"], ["--projects=tag:lane:packaging"], ["--projects=tag:lane:live"]];
    const seen = new Map();
    for (const scope of lanes) {
      const { ran, output, status } = lane(graph, edit, [`lane_test_targets=${linuxTargets}`, "lane-test"], [...owed, ...scope]);
      assert.equal(status, 0, output);
      for (const name of ran) {
        assert.ok(!lint.ran.has(name), `${name} runs in both lint and the ${platform} lane`);
        if (name !== "crozier:build" && name !== "corpus-match:cold-registry-build") {
          assert.ok(!seen.has(name), `${name} ran in two steps: ${seen.get(name)} and ${scope}`);
        }
        seen.set(name, scope.join());
      }
    }
  }
  assert.ok(lint.ran.has("workspace:supply-chain") && lint.ran.has("crozier:lint"), [...lint.ran].join(" "));
  const workflows = lane(graph, [".github/workflows/visual-docs.yml"], "lane-lint");
  assert.ok(workflows.ran.has("github-workflows:lint"), [...workflows.ran].join(" "));
  assert.ok(!workflows.ran.has("github-workflows:test") && !workflows.ran.has("github-workflows:budgets"), "lint no longer runs the workflow tests");
  // The recipe's target list keys on the host's OS, so run Windows' list through the same gate.
  const windowsTargets = /if os\(\) == "windows" \{ "([^"]+)" \}/.exec(readFileSync(join(REPO, "justfile"), "utf8"))[1];
  gitIn(graph.root, "checkout", "--quiet", "--detach", graph.base);
  write(graph.root, { "src/lib.rs": "edited\n" });
  const log = join(graph.root, "ran.log");
  rmSync(log, { force: true });
  const windows = spawnSync(process.execPath, ["tools/ci/gate.mjs", "--platform=windows", "--exclude=tag:tier:promoted", "--", "nx", "run-many", `--targets=${windowsTargets}`], {
    cwd: graph.root, encoding: "utf8", env: clean({ NX_BASE: graph.base, RAN_LOG: log }),
  });
  assert.equal(windows.status, 0, windows.stdout + windows.stderr);
  const ranOnWindows = readFileSync(log, "utf8").trim().split("\n");
  assert.ok(ranOnWindows.includes("crozier:lint-windows") && !ranOnWindows.includes("crozier:lint"), ranOnWindows.join(" "));
});

test("platform tags keep what only Linux proves off the other lanes", (t) => {
  const graph = realGraph(t);
  for (const platform of ["windows", "macos"]) {
    const live = lane(graph, ["src/lib.rs"], "lane-test", [`--platform=${platform}`, "--projects=tag:lane:live"]);
    assert.equal(live.ran.size, 0, [...live.ran].join(" "));
    const sdk = lane(graph, ["src/lib.rs"], "lane-test", [`--platform=${platform}`, "--projects=tag:lane:sdk-env"]);
    assert.ok(sdk.ran.has("sdk-env:test"), sdk.output);
  }
  const windows = lane(graph, ["tools/golden-reach/tests/golden_reach_test.py"], ...offline);
  assert.ok(!windows.ran.has("python-workspace:coverage"), "the floor holds on Linux and macOS, whose suites run every case");
});

const editManifest = (path, change) => (root) => {
  const project = JSON.parse(readFileSync(join(root, path), "utf8"));
  change(project);
  write(root, { [path]: JSON.stringify(project) });
};

test("the real inventory check holds this tree: every pre-refactor entrypoint on every platform that ran it", () => {
  const run = spawnSync(process.execPath, [join(REPO, "tools/ci/lane-inventory.mjs")], { encoding: "utf8" });
  assert.equal(run.status, 0, run.stderr);
});

test("a change to a tier manifest alone selects the inventory check, which fails when a row no longer matches", (t) => {
  const graph = realGraph(t);
  const SDK = "tests/sdk_env/project.json";
  const cases = [
    ["a test target added with no row", editManifest(SDK, (p) => { p.targets["test-extra"] = { command: "true" }; }), /sdk-env:test-extra: not in tools\/ci\/lanes\.json/],
    ["a target removed", editManifest("tests/runtime/project.json", (p) => { delete p.targets.test; }), /runtime:test: the target is gone/],
    ["a platform dropped", editManifest(SDK, (p) => { p.tags.push("platform:linux"); }), /sdk-env:test: no longer runs on macos/],
    ["a lane removed", editManifest("tests/live_e2e/project.json", (p) => { p.tags = p.tags.filter((tag) => !tag.startsWith("lane:")); }), /live-e2e: tier:promoted with no lane: tag/],
    ["a lane only Linux has", editManifest(SDK, (p) => { p.tags = p.tags.map((tag) => (tag === "lane:sdk-env" ? "lane:packaging" : tag)); }), /sdk-env:test: test-windows has no step `--projects=tag:lane:packaging`/],
    ["a target no lane reaches any more", editManifest("tests/corpus_match/project.json", (p) => { p.targets.test.dependsOn = p.targets.test.dependsOn.filter((name) => name !== "test-strict"); }), /corpus-match:test-strict: no lane reaches it/],
    ["a tier deleted outright", (root) => rmSync(join(root, "tests/live_e2e/project.json")), /live-e2e:test: project live-e2e is gone/],
  ];
  for (const [what, edit, message] of cases) {
    const { status, output, projects, inventory } = lane(graph, edit, "lane-lint");
    assert.ok(projects.includes("lane-inventory"), `${what} did not select the check:\n${output}`);
    assert.notEqual(status, 0, `${what} passed the lint lane:\n${output}`);
    assert.match(output, /gate: task lane-inventory:lint: [\d.]+s \(failure\)/, what);
    assert.match(output, /gate: a target failed/, what);
    assert.match(inventory.stderr, message, what);
  }
  const kept = lane(graph, editManifest(SDK, (p) => { p.metadata = { note: "no proof changed" }; }), "lane-lint");
  assert.equal(kept.status, 0, `a manifest edit that keeps every row passes:\n${kept.output}`);
  assert.ok(kept.projects.includes("lane-inventory"), kept.output);
  const unrelated = lane(graph, ["docs/float-literal-parity.md"], "lane-lint");
  assert.ok(!unrelated.projects.includes("lane-inventory"), "an unrelated edit does not pay for it");
});

test("a workflow on push to main must be declared as gating nothing, and stay that", (t) => {
  const graph = realGraph(t);
  const rewrite = (path, change) => (root) => write(root, { [path]: change(readFileSync(join(root, path), "utf8")) });
  const WRITER = ".github/workflows/ci-caches.yml";
  const onMain = "on:\n  push:\n    branches: [main]\njobs: {}\n";
  const cases = [
    ["an undeclared workflow on main", (root) => write(root, { ".github/workflows/extra.yml": onMain }), /extra\.yml: runs on push to main and is not in nonCheckWorkflows/],
    ["an undeclared one in an inline list", (root) => write(root, { ".github/workflows/extra.yml": "on: [push, pull_request]\njobs: {}\n" }), /extra\.yml: runs on push to main/],
    ["a branch list on its own lines, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on:\n  push:\n    branches:\n      - main\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["an event list on its own line, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on:\n  [push, pull_request]\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["an inline mapping, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on: { workflow_dispatch: { inputs: { push: {} } } }\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["an undeclared one with no filter", (root) => write(root, { ".github/workflows/extra.yml": "on: push\njobs: {}\n" }), /extra\.yml: runs on push to main/],
    ["a wildcard filter, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on:\n  push:\n    branches: ['**']\njobs: {}\n" }), /extra\.yml: cannot tell whether a push to main starts it/],
    ["an ignore filter, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on:\n  push:\n    branches-ignore: [main]\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["a quoted on key, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "\"on\":\n  push:\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["a path filter beside main, which it does not read", (root) => write(root, { ".github/workflows/extra.yml": "on:\n  push:\n    branches: [main]\n    paths: [src/**]\njobs: {}\n" }), /extra\.yml: cannot tell/],
    ["a declared one a pull request starts", rewrite(WRITER, (text) => text.replace("on:\n  push:", "on:\n  pull_request:\n  push:")), /ci-caches\.yml: listed as a non-check workflow, but a pull request starts it/],
    ["a declared one main no longer starts", rewrite(WRITER, (text) => text.replace("branches: [main]", "tags: [v1]")), /ci-caches\.yml: listed as a non-check workflow, but no push to main starts it/],
    ["a declared one that is gone", (root) => rmSync(join(root, WRITER)), /cannot read \.github\/workflows\/ci-caches\.yml/],
  ];
  for (const [what, edit, message] of cases) {
    const { inventory } = lane(graph, edit, "lane-lint");
    assert.notEqual(inventory.status, 0, what);
    assert.match(inventory.stderr, message, what);
  }
  const tagged = lane(graph, (root) => write(root, { ".github/workflows/extra.yml": "on:\n  push:\n    tags: ['v*']\njobs: {}\n" }), "lane-lint");
  assert.equal(tagged.inventory.status, 0, `a tag push is not a push to main:\n${tagged.inventory.stderr}`);
});

test("a manifest or inventory of the wrong shape is refused, not read past", (t) => {
  const graph = realGraph(t);
  for (const [what, edit] of [
    ["a manifest that is not JSON", (root) => write(root, { "tests/runtime/project.json": "{broken" })],
    ["a target that is not a mapping", (root) => write(root, { "tests/runtime/project.json": JSON.stringify({ name: "runtime", tags: [], targets: { test: null } }) })],
    ["a tag that is not a string", (root) => write(root, { "tests/runtime/project.json": JSON.stringify({ name: "runtime", tags: [null], targets: {} }) })],
    ["a malformed dependency", (root) => write(root, { "tests/runtime/project.json": JSON.stringify({ name: "runtime", tags: [], targets: { test: { dependsOn: [7] } } }) })],
    ["targets that are a list", (root) => write(root, { "tests/runtime/project.json": JSON.stringify({ name: "runtime", tags: [], targets: [] }) })],
    ["a dependency naming no project", (root) => write(root, { "tests/runtime/project.json": JSON.stringify({ name: "runtime", tags: [], targets: { test: { dependsOn: [{ target: "x", projects: [null] }] } } }) })],
    ["commands that are a list", (root) => {
      const inventory = JSON.parse(readFileSync(join(root, "tools/ci/lanes.json"), "utf8"));
      write(root, { "tools/ci/lanes.json": JSON.stringify({ ...inventory, commands: [] }) });
    }],
    ["a row whose new name is not a string", (root) => {
      const inventory = JSON.parse(readFileSync(join(root, "tools/ci/lanes.json"), "utf8"));
      inventory.entrypoints["runtime:test"].now = ["runtime:test"];
      write(root, { "tools/ci/lanes.json": JSON.stringify(inventory) });
    }],
    ["an added entry with no platform list", (root) => {
      const inventory = JSON.parse(readFileSync(join(root, "tools/ci/lanes.json"), "utf8"));
      write(root, { "tools/ci/lanes.json": JSON.stringify({ ...inventory, added: { "runtime:test": "linux" } }) });
    }],
    ["an inventory with no rows", (root) => write(root, { "tools/ci/lanes.json": JSON.stringify({ added: [] }) })],
    ["a row with an unknown platform", (root) => {
      const inventory = JSON.parse(readFileSync(join(root, "tools/ci/lanes.json"), "utf8"));
      inventory.entrypoints["runtime:test"].platforms = ["solaris"];
      write(root, { "tools/ci/lanes.json": JSON.stringify(inventory) });
    }],
  ]) {
    gitIn(graph.root, "checkout", "--quiet", "--detach", graph.base);
    edit(graph.root);
    const run = spawnSync(process.execPath, ["tools/ci/lane-inventory.mjs"], { cwd: graph.root, encoding: "utf8" });
    assert.equal(run.status, 2, what);
    assert.match(run.stderr, /lane-inventory: .*\n.*restore the file/, what);
    gitIn(graph.root, "checkout", "--quiet", "--", ".");
  }
});

test("the manifest digest moves with every manifest, and a failed listing never matches a good one", (t) => {
  const root = mkdtempSync(join(tmpdir(), "crozier-digest-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const SCRIPT = join(REPO, "tools/ci/project-files-digest.mjs");
  const digest = (cwd = root) => spawnSync(process.execPath, [SCRIPT], { cwd, encoding: "utf8" });
  gitIn(root, "init", "--quiet");
  write(root, { "a/project.json": "{}\n", "b/project.json": "{}\n", "b/other.txt": "x\n" });
  gitIn(root, "add", "-A");
  const first = digest();
  assert.equal(first.status, 0, first.stderr);
  assert.equal(digest().stdout, first.stdout, "unchanged manifests keep their digest");
  write(root, { "b/other.txt": "y\n" });
  assert.equal(digest().stdout, first.stdout, "only manifests count");
  write(root, { "a/project.json": '{"name":"a"}\n' });
  const edited = digest().stdout;
  assert.notEqual(edited, first.stdout, "an edit moves it");
  write(root, { "c/project.json": "{}\n" });
  const added = digest().stdout;
  assert.notEqual(added, edited, "an untracked manifest moves it");
  rmSync(join(root, "c/project.json"));
  assert.equal(digest().stdout, edited, "and removing it moves it back");
  rmSync(join(root, "a/project.json"));
  const deleted = digest();
  assert.equal(deleted.status, 0, "a tracked manifest gone from disk must not fail Nx's hashing");
  assert.notEqual(deleted.stdout, edited, "a deletion moves it");
  const elsewhere = mkdtempSync(join(tmpdir(), "crozier-digest-outside-"));
  t.after(() => rmSync(elsewhere, { recursive: true, force: true }));
  const failed = digest(elsewhere);
  assert.equal(failed.status, 0, "a runtime input must never fail");
  assert.notEqual(failed.stdout, digest(elsewhere).stdout, "a failed listing is never reused");
});

test("the inventory reads each platform's lane targets: a loss on one is a loss", (t) => {
  const graph = realGraph(t);
  gitIn(graph.root, "checkout", "--quiet", "--detach", graph.base);
  const justfile = readFileSync(join(graph.root, "justfile"), "utf8");
  const dropped = justfile.replace('"test,build,coverage,budgets,lint-windows,typecheck"', '"build,coverage,budgets,lint-windows,typecheck"');
  assert.notEqual(dropped, justfile);
  write(graph.root, { justfile: dropped });
  const run = spawnSync(process.execPath, ["tools/ci/lane-inventory.mjs"], { cwd: graph.root, encoding: "utf8" });
  assert.equal(run.status, 1, run.stderr);
  assert.match(run.stderr, /crozier-tool-journeys:test: no lane reaches it on windows/, "added entries are held too");
  assert.match(run.stderr, /crozier-e2e:test: no lane reaches it on windows/);
  assert.doesNotMatch(run.stderr, /on (linux|macos):/);
  gitIn(graph.root, "checkout", "--quiet", "--", ".");
});

test("a retired row in the same change passes: only an unrecorded loss fails", (t) => {
  const graph = realGraph(t);
  const retired = lane(graph, (root) => {
    editManifest("tests/runtime/project.json", (p) => { delete p.targets.test; })(root);
    const inventory = JSON.parse(readFileSync(join(root, "tools/ci/lanes.json"), "utf8"));
    delete inventory.entrypoints["runtime:test"];
    write(root, { "tools/ci/lanes.json": JSON.stringify(inventory) });
  }, "lane-lint");
  assert.equal(retired.status, 0, retired.output);
  assert.ok(retired.projects.includes("lane-inventory"), retired.output);
});

test("the prune stays alone and in the pull request flow, with no scheduled replacement for a test", () => {
  const ci = readFileSync(join(REPO, ".github/workflows/ci.yml"), "utf8");
  assert.ok(ci.includes("run: just ci-budgets-host"));
  assert.equal(readProject("pool-maintenance/project.json").targets["budgets-host"].parallelism, false);
  assert.ok(!/schedule|ci-broader/.test(ci.slice(0, ci.indexOf("jobs:"))));
});

test("the result cache refuses what it is not, and a failed upload leaves nothing to replay", async (t) => {
  const directory = mkdtempSync(join(tmpdir(), "crozier-results-"));
  t.after(() => rmSync(directory, { recursive: true, force: true }));
  const { env, stop } = await serveResults(directory);
  t.after(stop);
  const url = (path) => `${env.NX_SELF_HOSTED_REMOTE_CACHE_SERVER}${path}`;
  const headers = { Authorization: `Bearer ${env.NX_SELF_HOSTED_REMOTE_CACHE_ACCESS_TOKEN}` };
  assert.equal((await fetch(url("/v1/cache/abc"))).status, 401, "no token");
  assert.equal((await fetch(url("/v1/cache/abc"), { headers: { Authorization: "Bearer wrong" } })).status, 401);
  for (const route of ["/v1/cache/../secret", "/v1/cache/a.b", "/v1/other/abc"]) assert.equal((await fetch(url(route), { headers })).status, 404, route);
  assert.equal((await fetch(url("/v1/cache/abc"), { headers })).status, 404, "nothing stored yet");
  assert.equal((await fetch(url("/v1/cache/abc"), { method: "DELETE", headers })).status, 405);
  assert.equal((await fetch(url("/v1/cache/abc"), { method: "PUT", headers, body: "tar" })).status, 200);
  assert.equal((await fetch(url("/v1/cache/abc"), { method: "PUT", headers, body: "other" })).status, 409, "a stored result is never overwritten");
  assert.equal(await (await fetch(url("/v1/cache/abc"), { headers })).text(), "tar");
  const { port } = new URL(url("/"));
  await new Promise((resolve) => {
    const cut = connect(Number(port), "127.0.0.1", () => {
      cut.write(`PUT /v1/cache/interrupted HTTP/1.1\r\nHost: x\r\nAuthorization: ${headers.Authorization}\r\nContent-Length: 100\r\n\r\npartial`, () => cut.destroy());
    });
    cut.on("close", resolve);
  });
  await new Promise((resolve) => setTimeout(resolve, 200));
  assert.equal((await fetch(url("/v1/cache/interrupted"), { headers })).status, 404, "an interrupted upload is a miss");
  assert.deepEqual(readdirSync(directory), ["abc.tar"], "and leaves no partial file");
});

test("no e2e case was lost when the tooling journeys moved out", () => {
  const { e2eCases } = JSON.parse(readFileSync(join(REPO, "tools/ci/lanes.json"), "utf8"));
  const pin = (name) => readFileSync(join(REPO, `tools/ci/suite-cases/pins/${name}.txt`), "utf8").trim().split("\n");
  const cases = [
    ...pin("crozier-e2e-test").map((line) => line.replace(/^crozier-e2e::e2e /, "")),
    ...pin(e2eCases.moved).map((line) => line.replace(/^crozier-tool-journeys::tool_journeys /, "")).filter((line) => !line.startsWith("yaml::")),
  ];
  const unique = [...new Set(cases)].sort();
  assert.equal(unique.length, e2eCases.count);
  const digest = createHash("sha256").update(`${[...unique].map((line) => Buffer.from(line)).sort(Buffer.compare).map(String).join("\n")}\n`).digest("hex");
  assert.equal(digest, e2eCases.sha256);
});

function tinyRepo(t) {
  const root = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), "crozier-tiny-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  for (const path of ["justfile", "package.json", "tools/ci/gate.mjs", "tools/ci/result-cache.mjs", "tools/ci/gate-timing.mjs", "tools/ci/gate-timing/core.mjs", "tools/ci/ci-tier.mjs"]) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    cpSync(join(REPO, path), join(root, path));
  }
  symlinkSync(join(REPO, "node_modules"), join(root, "node_modules"), "junction");
  // The real namedInputs' shape: generator, locks and toolchain as inputs of a suite.
  const { namedInputs } = JSON.parse(readFileSync(join(REPO, "nx.json"), "utf8"));
  const suite = (name, table) => JSON.stringify({ name, tags: ["type:e2e"], targets: { test: {
    command: `node harness/suite.js ${name}:test ${table}`, cache: true,
    inputs: ["{projectRoot}/**/*", "{workspaceRoot}/generator/**/*", "{workspaceRoot}/harness/**/*", "{workspaceRoot}/spec/**/*", "cargo", "generator", { env: "RUSTFLAGS" }],
  } } });
  write(root, {
    ".gitignore": "/node_modules\n/.nx\n/ran.log\n/.results\n",
    "nx.json": JSON.stringify({ defaultBase: "main", cacheDirectory: ".nx/cache", namedInputs: { default: ["{projectRoot}/**/*"], cargo: namedInputs.cargo, generator: [namedInputs.generator[0]] } }),
    // A real, tiny generator CLI, and a suite that drives it and runs what it generated.
    "generator/cli.js": "const f=require('fs');process.stdout.write('module.exports={call(){return '+JSON.stringify(f.readFileSync('generator/template.txt','utf8').trim()+':'+f.readFileSync('spec/api.txt','utf8').trim())+'}}\\n');\n",
    "harness/suite.js": "const {execFileSync}=require('child_process');const f=require('fs'),os=require('os'),p=require('path');const [name,table]=process.argv.slice(2);f.appendFileSync(process.env.RAN_LOG,name+'\\n');const dir=f.mkdtempSync(p.join(os.tmpdir(),'sdk-'));const sdk=p.join(dir,'sdk.js');f.writeFileSync(sdk,execFileSync(process.execPath,['generator/cli.js']));const got=require(sdk).call();f.rmSync(dir,{recursive:true});const want=f.readFileSync(table,'utf8').trim();if(got!==want){console.error('stale table: got '+got+' want '+want);process.exit(1)}\n",
    "generator/template.txt": "v1\n",
    "spec/api.txt": "pets\n",
    "cli/project.json": suite("cli", "cli/expected.txt"),
    "cli/expected.txt": "v1:pets\n",
    "sdk/project.json": suite("sdk", "sdk/expected.txt"),
    "sdk/expected.txt": "v1:pets\n",
    "other/project.json": JSON.stringify({ name: "other", tags: ["type:tooling"], targets: { test: { command: `node -e "require('fs').appendFileSync(process.env.RAN_LOG,'other:test\\n')"`, cache: true, inputs: ["{projectRoot}/**/*"] } } }),
    "other/readme.txt": "x\n",
    "Cargo.toml": "[package]\n", "Cargo.lock": "version = 4\n", "rust-toolchain.toml": readFileSync(join(REPO, "rust-toolchain.toml"), "utf8"), ".cargo/config.toml": "\n", ".ruff-version": "0.1.0\n",
    "docs/note.md": "note\n",
  });
  gitIn(root, "init", "--quiet", "--initial-branch=main");
  gitIn(root, "add", "-A");
  gitIn(root, "commit", "--quiet", "-m", "base");
  const base = gitIn(root, "rev-parse", "HEAD");
  const run = (env = {}) => {
    const log = join(root, "ran.log");
    rmSync(log, { force: true });
    forgetFileHashes(root);
    const result = spawnSync("just", ["check", "--projects=cli,sdk,other"], {
      cwd: root, encoding: "utf8", shell: process.platform === "win32",
      env: clean({ NX_BASE: base, RAN_LOG: log, ...env }),
    });
    return { status: result.status, output: `${result.stdout}${result.stderr}`, ran: existsSync(log) ? readFileSync(log, "utf8").trim().split("\n").sort() : [] };
  };
  return { root, base, run };
}

test("a real generator edit reruns real suites and a stale table fails them; only changed inputs lose the cache", (t) => {
  const { root, run } = tinyRepo(t);
  write(root, { "docs/note.md": "edited\n" });
  const nothing = run();
  assert.equal(nothing.status, 0, nothing.output);
  assert.deepEqual(nothing.ran, [], "a docs edit reaches neither suite");

  write(root, { "generator/template.txt": "v2\n" });
  const stale = run();
  assert.notEqual(stale.status, 0, "the suites still expect v1");
  assert.match(stale.output, /stale table: got v2:pets want v1:pets/);
  assert.deepEqual(stale.ran, ["cli:test", "sdk:test"], stale.output);

  write(root, { "cli/expected.txt": "v2:pets\n", "sdk/expected.txt": "v2:pets\n" });
  const fresh = run();
  assert.equal(fresh.status, 0, fresh.output);
  assert.deepEqual(fresh.ran, ["cli:test", "sdk:test"]);

  const replay = run();
  assert.equal(replay.status, 0, replay.output);
  assert.deepEqual(replay.ran, [], "unchanged inputs replay from the cache");

  for (const [path, text] of [["Cargo.lock", "version = 4\n# moved\n"], ["rust-toolchain.toml", `${readFileSync(join(REPO, "rust-toolchain.toml"), "utf8")}# moved\n`], [".ruff-version", "0.2.0\n"], ["spec/api.txt", "pets\n\n"], ["harness/suite.js", `${readFileSync(join(root, "harness/suite.js"), "utf8")}// moved\n`]]) {
    write(root, { [path]: text });
    const again = run();
    assert.equal(again.status, 0, `${path}: ${again.output}`);
    assert.deepEqual(again.ran, ["cli:test", "sdk:test"], `${path} must not replay a stale result`);
  }
  const flags = run({ RUSTFLAGS: "-C opt-level=1" });
  assert.deepEqual(flags.ran, ["cli:test", "sdk:test"], "other compiler flags must not replay");

  // A goldens edit alone: the expected table changes under a cached result, and the suite must see it.
  write(root, { "sdk/expected.txt": "v0:pets\n" });
  const wrong = run();
  assert.notEqual(wrong.status, 0, "a stale table cannot be replayed past");
  assert.deepEqual(wrong.ran, ["sdk:test"], wrong.output);
  assert.match(wrong.output, /stale table/);
  write(root, { "sdk/expected.txt": "v2:pets\n" });
});

test("results restored onto a runner with no Nx state replay by input hash, outputs included, and changed inputs do not", (t) => {
  const { root, run } = tinyRepo(t);
  const results = join(root, ".results");
  write(root, { "generator/template.txt": "v3\n", "cli/expected.txt": "v3:pets\n", "sdk/expected.txt": "v3:pets\n" });
  const carried = { CROZIER_RESULT_CACHE: ".results" };
  const first = run(carried);
  assert.deepEqual(first.ran, ["cli:test", "sdk:test"], first.output);
  assert.equal(readdirSync(results).filter((name) => name.endsWith(".tar")).length, 2, "each result is stored by its hash");

  // A new runner: the Nx database and local cache are gone; only the carried results remain.
  rmSync(join(root, ".nx"), { recursive: true, force: true });
  const replayed = run(carried);
  assert.equal(replayed.status, 0, replayed.output);
  assert.deepEqual(replayed.ran, [], `the carried results must replay:\n${replayed.output}`);

  rmSync(join(root, ".nx"), { recursive: true, force: true });
  write(root, { "spec/api.txt": "owners\n" });
  const changed = run(carried);
  assert.notEqual(changed.status, 0, "a stale table is never replayed past");
  assert.match(changed.output, /stale table: got v3:owners want v3:pets/);
  assert.deepEqual(changed.ran, ["cli:test", "sdk:test"]);
  write(root, { "spec/api.txt": "pets\n" });

  rmSync(join(root, ".nx"), { recursive: true, force: true });
  rmSync(results, { recursive: true, force: true });
  assert.deepEqual(run(carried).ran, ["cli:test", "sdk:test"], "nothing carried, nothing replayed");
});

test("main's cache writer proves every project into the store, and a pull request's first push replays from it", (t) => {
  const { root } = tinyRepo(t);
  const results = join(root, ".results");
  const log = join(root, "ran.log");
  // A suite reading less than its project, so a pull request can reach the project and not the suite's inputs.
  write(root, {
    "narrow/project.json": JSON.stringify({ name: "narrow", tags: ["type:tooling"], targets: { test: { command: `node -e "require('fs').appendFileSync(process.env.RAN_LOG,'narrow:test\\n')"`, cache: true, inputs: ["{projectRoot}/src/**/*"] } } }),
    "narrow/src/a.txt": "a\n",
    "narrow/readme.txt": "x\n",
    "tier/project.json": JSON.stringify({ name: "tier", tags: ["type:tier", "tier:promoted"], targets: { test: { command: `node -e "require('fs').appendFileSync(process.env.RAN_LOG,'tier:test\\n')"`, cache: false } } }),
  });
  gitIn(root, "add", "-A");
  gitIn(root, "commit", "--quiet", "-m", "two more projects");
  const main = gitIn(root, "rev-parse", "HEAD");
  const invoke = (args, env = {}) => {
    rmSync(log, { force: true });
    forgetFileHashes(root);
    const result = spawnSync("just", args, { cwd: root, encoding: "utf8", shell: process.platform === "win32", env: clean({ RAN_LOG: log, CROZIER_RESULT_CACHE: ".results", ...env }) });
    return { status: result.status, output: `${result.stdout}${result.stderr}`, ran: existsSync(log) ? readFileSync(log, "utf8").trim().split("\n").sort() : [] };
  };
  const stored = () => readdirSync(results).filter((name) => name.endsWith(".tar")).length;

  // A red suite on main: what the writer's continue-on-error is for. The rest are still stored.
  write(root, { "sdk/expected.txt": "stale\n" });
  const red = invoke(["ci-caches-test"]);
  assert.notEqual(red.status, 0, "the failure is reported");
  assert.match(red.output, /stale table/);
  assert.deepEqual(red.ran, ["cli:test", "narrow:test", "other:test", "sdk:test"], "every project, no base compared against, and the promoted tier left to its own step");
  assert.equal(stored(), 3, "the three that passed are stored and the failure is not");
  write(root, { "sdk/expected.txt": "v1:pets\n" });

  // The next push to main, on a new runner: only what is missing executes.
  rmSync(join(root, ".nx"), { recursive: true, force: true });
  const next = invoke(["ci-caches-test"]);
  assert.equal(next.status, 0, next.output);
  assert.deepEqual(next.ran, ["sdk:test"], next.output);
  assert.equal(stored(), 4);

  // A pull request's first push, on a new runner, restoring main's store: it reaches the
  // project and replays the suite whose inputs it left alone; an edit to an input reruns it.
  rmSync(join(root, ".nx"), { recursive: true, force: true });
  write(root, { "narrow/readme.txt": "edited\n" });
  const affected = ["lane-test", "--projects=narrow"];
  const replayed = invoke(affected, { NX_BASE: main });
  assert.equal(replayed.status, 0, replayed.output);
  assert.match(replayed.output, /gate: projects: narrow/, "the change reaches the project");
  assert.deepEqual(replayed.ran, [], `main's result must replay:\n${replayed.output}`);
  write(root, { "narrow/src/a.txt": "b\n" });
  assert.deepEqual(invoke(affected, { NX_BASE: main }).ran, ["narrow:test"], "a changed input never replays main's result");
});

test("a target's declared outputs come back with its carried result", (t) => {
  const { root, base } = tinyRepo(t);
  write(root, { "cov/project.json": JSON.stringify({ name: "cov", tags: ["type:tooling"], targets: { test: {
    command: `node -e "const f=require('fs');f.appendFileSync(process.env.RAN_LOG,'cov:test\\n');f.mkdirSync('.coverage-data/cov',{recursive:true});f.writeFileSync('.coverage-data/cov/.coverage','data')"`,
    cache: true, inputs: ["{projectRoot}/**/*"], outputs: ["{workspaceRoot}/.coverage-data/cov"],
  } } }), ".gitignore": "/node_modules\n/.nx\n/ran.log\n/.coverage-data\n/.results\n" });
  const log = join(root, "ran.log");
  const invoke = () => forgetFileHashes(root) ?? spawnSync("just", ["check", "--projects=cov"], { cwd: root, encoding: "utf8", shell: process.platform === "win32",
    env: clean({ NX_BASE: base, RAN_LOG: log, CROZIER_RESULT_CACHE: ".results" }) });
  assert.equal(invoke().status, 0);
  assert.equal(readFileSync(log, "utf8"), "cov:test\n");
  rmSync(join(root, ".nx"), { recursive: true, force: true });
  rmSync(join(root, ".coverage-data"), { recursive: true, force: true });
  rmSync(log);
  assert.equal(invoke().status, 0);
  assert.ok(!existsSync(log), "replayed, not rerun");
  assert.equal(readFileSync(join(root, ".coverage-data/cov/.coverage"), "utf8"), "data", "the floor would read this file");
});
