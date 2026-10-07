#!/usr/bin/env node
// The gate: one recipe (`just check`), two tiers, chosen by a flag.
//
//   node tools/ci/gate.mjs [--sweep] [--projects=p,q] [--exclude=p,q] -- nx run-many --targets=a,b
//
// The recipe names the Nx command it runs (`just check`, `just test` and `just
// lint` differ only in their target list); this driver validates the base,
// selects the projects for the tier, and runs that command over them.
//
// The affected tier (the default) runs the gate targets of every project a
// change can reach, keyed off an explicitly derived base:
//   * `NX_BASE`, when set — a plain ref name or a commit SHA, validated here at
//     the boundary because it reaches git as an argument; anything else, or a
//     ref that names no commit in this checkout, fails closed naming it;
//   * otherwise the merge base of HEAD with `origin/main`.
// The selection compares that base with the working tree, so uncommitted work
// is included. Projects tagged `tier:promoted` (the suites that leave the
// affected tier because of what they touch) run only when `--projects` names
// them, which is how CI runs each one on the runner holding its toolchain.
//
// The broader tier (`--sweep`) runs the same targets over every project,
// promoted ones included, with the cache skipped: it exists to catch what
// affected detection or a stale cache could miss.
//
// Quiet on success: the selection line, then one line. Nx's own output goes to
// a log that is printed in full when a target fails.
import { execFileSync, spawnSync } from "node:child_process";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const TOOL = "gate";
const PROMOTED_TAG = "tier:promoted";
const DEFAULT_BASE_REF = "origin/main";

function die(message, action, code = 2) {
  console.error(`${TOOL}: ${message}`);
  if (action) console.error(`${TOOL}: ${action}`);
  process.exit(code);
}

const USAGE = `usage: just check|test|lint [--sweep] [--projects=p,q] [--exclude=p,q]
  (default)    affected tier: the projects a change since the base can reach;
               the base is NX_BASE (a ref name or commit SHA) or the merge base
               of HEAD with ${DEFAULT_BASE_REF}
  --sweep      broader tier: every project, promoted tiers included, uncached
  --projects   only these projects (promoted ones run only when named)
  --exclude    never these projects
  Each list takes project names and tag:<tag> patterns.`;

// A project or target name, or `tag:<tag>` for every project carrying it:
// what project.json allows, and nothing a shell or an Nx pattern would read as
// syntax.
const LIST_ITEM = String.raw`(?:tag:[a-z0-9][a-z0-9:-]*|[a-z0-9][a-z0-9-]*)`;
const NAME_LIST = new RegExp(`^${LIST_ITEM}(,${LIST_ITEM})*$`);

// The one command a recipe may hand over: `nx run-many --targets=<names>`.
const COMMAND = /^--targets=(.+)$/;

function parseArgs(argv) {
  const options = { sweep: false, targets: undefined, projects: undefined, exclude: [] };
  const split = argv.indexOf("--");
  const command = split < 0 ? [] : argv.slice(split + 1);
  const targets = command.length === 3 && command[0] === "nx" && command[1] === "run-many" && COMMAND.exec(command[2]);
  if (!targets || !NAME_LIST.test(targets[1]) || targets[1].includes("tag:")) {
    die("the recipe must end its arguments with `-- nx run-many --targets=a,b`", USAGE);
  }
  options.targets = targets[1].split(",");
  argv = argv.slice(0, split);
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    const [flag, inline] = arg.includes("=") ? [arg.slice(0, arg.indexOf("=")), arg.slice(arg.indexOf("=") + 1)] : [arg, undefined];
    const value = () => {
      const v = inline ?? argv[++i];
      if (v === undefined || !NAME_LIST.test(v)) {
        die(`${flag} takes a comma-separated list of project or target names, not '${v ?? ""}'`, USAGE);
      }
      return v.split(",");
    };
    switch (flag) {
      case "--sweep":
        options.sweep = true;
        break;
      case "--projects":
        options.projects = value();
        break;
      case "--exclude":
        options.exclude = value();
        break;
      case "-h":
      case "--help":
        console.log(USAGE);
        process.exit(0);
        break;
      default:
        die(`unknown argument '${arg}'`, USAGE);
    }
  }
  return options;
}

function git(args) {
  const result = spawnSync("git", args, { cwd: ROOT, encoding: "utf8" });
  return { ok: result.status === 0, out: (result.stdout ?? "").trim(), err: (result.stderr ?? "").trim() };
}

// A plain ref name — what `git check-ref-format --allow-onelevel` accepts, held
// to a character set with no shell, glob or revision syntax in it — or a SHA.
const SHA = /^[0-9a-f]{7,64}$/;
const REF_NAME = /^[A-Za-z0-9][A-Za-z0-9._/-]*$/;

/** The commit the affected tier compares against, and how it was chosen. */
export function resolveBase(env = process.env) {
  const raw = env.NX_BASE;
  if (raw !== undefined && raw !== "") {
    const plain = SHA.test(raw) || (REF_NAME.test(raw) && !raw.includes("..") && git(["check-ref-format", "--allow-onelevel", raw]).ok);
    if (!plain) {
      die(
        `NX_BASE '${raw}' is neither a plain ref name nor a commit SHA; no target ran`,
        "set NX_BASE to a branch, tag or commit SHA (e.g. NX_BASE=origin/main), or unset it to use the merge base with origin/main",
      );
    }
    const commit = git(["rev-parse", "--verify", "--quiet", "--end-of-options", `${raw}^{commit}`]);
    if (!commit.ok || !SHA.test(commit.out)) {
      die(
        `NX_BASE '${raw}' does not name a commit in this checkout; no target ran`,
        "fetch it first (e.g. git fetch origin main), or unset NX_BASE to use the merge base with origin/main",
      );
    }
    return { sha: commit.out, how: `NX_BASE=${raw}` };
  }
  const base = git(["merge-base", DEFAULT_BASE_REF, "HEAD"]);
  if (!base.ok || !SHA.test(base.out)) {
    die(
      `no merge base between HEAD and ${DEFAULT_BASE_REF}${base.err ? ` (${base.err})` : ""}; no target ran`,
      `run 'git fetch origin main', set NX_BASE to the commit to compare against, or run the broader tier with 'just check --sweep'`,
    );
  }
  return { sha: base.out, how: `merge base with ${DEFAULT_BASE_REF}` };
}

function nxBin() {
  for (const candidate of ["nx", "nx.exe", "nx.cmd"]) {
    const path = join(ROOT, "node_modules", ".bin", candidate);
    if (existsSync(path)) return path;
  }
  return die("Nx is not installed (no node_modules/.bin/nx)", "run 'just bootstrap', which installs the pinned Nx from bun.lock");
}

// Nx reads NX_BASE / NX_HEAD from its environment on its own, and hands them to a
// shell: the gate passes the base it validated explicitly instead, so Nx never
// sees the raw value.
const NX_ENV = { ...process.env, NX_DAEMON: process.env.NX_DAEMON ?? "false", NX_NO_CLOUD: "true", NX_TUI: "false" };
delete NX_ENV.NX_BASE;
delete NX_ENV.NX_HEAD;

function nx(args) {
  try {
    return execFileSync(nxBin(), args, { cwd: ROOT, env: NX_ENV, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"], maxBuffer: 64 * 1024 * 1024, shell: process.platform === "win32" });
  } catch (error) {
    return die(`'nx ${args.join(" ")}' failed: ${String(error.stderr || error.stdout || error.message).trim()}`, "fix the project.json or nx.json it names, then rerun");
  }
}

function nxJson(args) {
  const out = nx(args);
  try {
    return JSON.parse(out);
  } catch {
    return die(`'nx ${args.join(" ")}' printed no JSON: ${out.trim()}`, "run it by hand (just nx ...) to see why");
  }
}

/** Every project's tags, as Nx computes the graph for this checkout. */
function projectTags() {
  const scratch = mkdtempSync(join(tmpdir(), "crozier-gate-"));
  try {
    const file = join(scratch, "graph.json");
    nx(["graph", `--file=${file}`]);
    const nodes = JSON.parse(readFileSync(file, "utf8")).graph.nodes;
    return Object.fromEntries(Object.entries(nodes).map(([name, node]) => [name, node.data.tags ?? []]));
  } finally {
    rmSync(scratch, { recursive: true, force: true });
  }
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  // Validated before Nx runs at all.
  const base = options.sweep ? undefined : resolveBase();
  const tags = projectTags();
  const expand = (list) =>
    list.flatMap((entry) => {
      if (entry.startsWith("tag:")) {
        const tag = entry.slice("tag:".length);
        const carriers = Object.keys(tags).filter((name) => tags[name].includes(tag));
        if (carriers.length === 0) die(`no project carries the tag '${tag}'`, USAGE);
        return carriers;
      }
      if (!Object.hasOwn(tags, entry)) {
        die(`no project named '${entry}' (projects: ${Object.keys(tags).sort().join(", ")})`, USAGE);
      }
      return [entry];
    });
  if (options.projects) options.projects = expand(options.projects);
  options.exclude = expand(options.exclude);

  let candidates;
  let tierLine;
  if (options.sweep) {
    candidates = Object.keys(tags);
    tierLine = "broader tier (--sweep): every project, cache skipped";
  } else {
    candidates = nxJson(["show", "projects", "--affected", `--base=${base.sha}`, "--json"]);
    tierLine = `affected tier against ${base.sha.slice(0, 12)} (${base.how})`;
  }
  const named = options.projects ? new Set(options.projects) : undefined;
  const selected = candidates
    .filter((name) => (named ? named.has(name) : options.sweep || !tags[name].includes(PROMOTED_TAG)))
    .filter((name) => !options.exclude.includes(name))
    .sort();
  const skippedPromoted = named || options.sweep ? [] : candidates.filter((name) => tags[name].includes(PROMOTED_TAG)).sort();
  console.log(`${TOOL}: ${tierLine}`);
  console.log(`${TOOL}: projects: ${selected.join(", ") || "(none)"}`);
  if (skippedPromoted.length > 0) {
    console.log(`${TOOL}: promoted, run by their own CI legs: ${skippedPromoted.join(", ")}`);
  }
  if (selected.length === 0) {
    console.log(`${TOOL}: ok (nothing to run)`);
    return;
  }

  const args = ["run-many", `--targets=${options.targets.join(",")}`, `--projects=${selected.join(",")}`, "--outputStyle=static"];
  // The broader tier trusts no cache, including the nested Nx a target runs.
  if (options.sweep) {
    args.push("--skipNxCache");
    NX_ENV.NX_SKIP_NX_CACHE = "true";
  }
  const logDir = join(ROOT, ".nx", "logs");
  mkdirSync(logDir, { recursive: true });
  const log = join(logDir, `gate-${process.pid}.log`);
  const run = spawnSync(nxBin(), args, { cwd: ROOT, env: NX_ENV, encoding: "utf8", maxBuffer: 1024 * 1024 * 1024, shell: process.platform === "win32" });
  writeFileSync(log, `$ nx ${args.join(" ")}\n${run.stdout ?? ""}${run.stderr ?? ""}`);
  if (run.status !== 0) {
    process.stderr.write(readFileSync(log, "utf8"));
    die(`a target failed (full output above and in ${log})`, "fix what it reports, then rerun the same recipe", 1);
  }
  console.log(`${TOOL}: ok (${options.targets.join(", ")}; output in ${log})`);
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
