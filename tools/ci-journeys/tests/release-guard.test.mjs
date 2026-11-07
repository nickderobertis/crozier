// The release branch's content guard, over real git histories built from this
// repository's own manifests: the test lanes skip a release branch only because
// this passes, so anything the guard lets through merges untested.
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { mkdtempSync, readFileSync, rmSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";
import { REPO, write } from "./support.mjs";

const GUARD = join(REPO, "scripts/release-branch-guard.mjs");
const CURRENT = /^version = "(\d+\.\d+\.\d+)"$/m.exec(readFileSync(join(REPO, "Cargo.toml"), "utf8"))[1];
const NEXT = CURRENT.replace(/\d+$/, (patch) => String(Number(patch) + 1));

const real = (path) => readFileSync(join(REPO, path), "utf8");
const bumpManifest = (text) => text.replace(`version = "${CURRENT}"`, `version = "${NEXT}"`);
const bumpLock = (text) => text.replace(new RegExp(`(name = "crozier"\\nversion = ")${CURRENT.replaceAll(".", "\\.")}"`), `$1${NEXT}"`);

function history(t) {
  const dir = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), "release-guard-"));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const git = (...args) => execFileSync("git", args, { cwd: dir, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
  git("init", "--quiet", "--initial-branch=main");
  git("config", "user.email", "t@example.com");
  git("config", "user.name", "t");
  write(dir, {
    "Cargo.toml": real("Cargo.toml"),
    "Cargo.lock": real("Cargo.lock"),
    "CHANGELOG.md": "# Changelog\n",
    "package.json": real("package.json"),
    "pyproject.toml": real("pyproject.toml"),
    "src/lib.rs": "// source\n",
  });
  git("add", "-A");
  git("commit", "--quiet", "-m", "tested main");
  const base = git("rev-parse", "HEAD");
  const change = (files, remove = []) => {
    git("checkout", "--quiet", "--detach", base);
    write(dir, files);
    for (const path of remove) git("rm", "--quiet", path);
    git("add", "-A");
    git("commit", "--quiet", "--allow-empty", "-m", "release");
    return git("rev-parse", "HEAD");
  };
  const guard = (head, args = ["--base", base, "--head", head]) => spawnSync(process.execPath, [GUARD, ...args], { cwd: dir, encoding: "utf8" });
  return { dir, git, base, change, guard };
}

test("release-plz's own edit of the real manifests passes: versions and changelog on tested main", (t) => {
  const h = history(t);
  const head = h.change({
    "Cargo.toml": bumpManifest(real("Cargo.toml")),
    "Cargo.lock": bumpLock(real("Cargo.lock")),
    "CHANGELOG.md": `# Changelog\n\n## ${NEXT}\n\n- A fix\n`,
  });
  assert.notEqual(real("Cargo.toml"), bumpManifest(real("Cargo.toml")), "the journey must really bump the version");
  assert.notEqual(real("Cargo.lock"), bumpLock(real("Cargo.lock")), "the journey must really bump the lock");
  const run = h.guard(head);
  assert.equal(run.status, 0, run.stderr);
  assert.match(run.stdout, /3 file\(s\) changed, all release-tool version and changelog edits/);
});

test("a changelog alone, or a package.json version alone, is a release edit", (t) => {
  const h = history(t);
  assert.equal(h.guard(h.change({ "CHANGELOG.md": "# Changelog\n\n## notes\n" })).status, 0);
  const pkg = JSON.parse(real("package.json"));
  assert.equal(h.guard(h.change({ "package.json": `${JSON.stringify({ ...pkg, version: NEXT }, null, 2)}\n` })).status, 0);
});

test("a dependency, build setting or script edited inside an allowed file fails naming the file", (t) => {
  const h = history(t);
  const toml = bumpManifest(real("Cargo.toml"));
  const pkg = JSON.parse(real("package.json"));
  const cases = [
    ["Cargo.toml", { "Cargo.toml": `${toml}\n[profile.release]\nopt-level = 0\n` }, /Cargo\.toml: it changes more than the package version/],
    ["Cargo.toml", { "Cargo.toml": toml.replace(/^clap = .*$/m, 'clap = "1"') }, /Cargo\.toml: it changes more than the package version/],
    ["Cargo.lock", { "Cargo.lock": bumpLock(real("Cargo.lock")).replace(/(name = "serde"\nversion = ")[^"]+"/, '$19.9.9"') }, /Cargo\.lock: it changes more than workspace members' versions/],
    ["package.json", { "package.json": JSON.stringify({ ...pkg, version: NEXT, scripts: { postinstall: "curl evil" } }) }, /package\.json: it changes more than its top-level version/],
    ["package.json", { "package.json": JSON.stringify({ ...pkg, version: "latest" }) }, /package\.json: its version "latest" is not a semantic version/],
    ["package.json", { "package.json": "{malformed" }, /package\.json: its head side is not JSON/],
    ["pyproject.toml", { "pyproject.toml": real("pyproject.toml").replace('dynamic = ["version"]', 'version = "9.9.9"') }, /pyproject\.toml: the release tool edits only versions and changelogs/],
    ["Cargo.toml", { "Cargo.toml": toml.replace(`version = "${NEXT}"`, 'version = "not-a-version"') }, /Cargo\.toml: it changes more than the package version/],
  ];
  for (const [path, files, why] of cases) {
    const run = h.guard(h.change(files));
    assert.equal(run.status, 1, `${path} must fail: ${run.stdout}`);
    assert.match(run.stderr, why);
    assert.match(run.stderr, /next: the test jobs skip a release branch/);
  }
});

test("a workspace crate's inline version may move; a look-alike or anything beside it may not", (t) => {
  const h = history(t);
  const manifest = (dependency) => `[package]\nname = "crozier"\nversion = "0.0.1"\n\n[dependencies]\n${dependency}\n`;
  const inline = (version, extra = "") => `helper = { path = "crates/helper", version = "${version}"${extra} }`;
  const base = h.change({ "Cargo.toml": manifest(inline("0.0.1")) });
  const compare = (text) => {
    h.git("checkout", "--quiet", "--detach", base);
    write(h.dir, { "Cargo.toml": text });
    h.git("add", "-A");
    h.git("commit", "--quiet", "-m", "release");
    const head = h.git("rev-parse", "HEAD");
    return spawnSync(process.execPath, [GUARD, "--base", base, "--head", head], { cwd: h.dir, encoding: "utf8" });
  };
  assert.equal(compare(manifest(inline("0.0.2"))).status, 0, "a workspace crate's own version");
  assert.equal(compare(manifest(inline("0.0.2", ', features = ["x"]'))).status, 1, "a feature beside it");
  // The `path` here is text inside a comment, so this is a registry dependency.
  const registry = h.change({ "Cargo.toml": manifest('serde = { version = "1.0.0" } # path = "not/a/field"') });
  h.git("checkout", "--quiet", "--detach", registry);
  write(h.dir, { "Cargo.toml": manifest('serde = { version = "2.0.0" } # path = "not/a/field"') });
  h.git("add", "-A");
  h.git("commit", "--quiet", "-m", "release");
  const bumped = spawnSync(process.execPath, [GUARD, "--base", registry, "--head", h.git("rev-parse", "HEAD")], { cwd: h.dir, encoding: "utf8" });
  assert.equal(bumped.status, 1, "a path named only in a comment makes nothing a workspace crate");
});

test("a manifest holding a multi-line string may not change at all", (t) => {
  const h = history(t);
  const text = 'description = """\nversion = "0.0.1"\n"""\n[package]\nversion = "0.0.1"\n';
  const base = h.change({ "Cargo.toml": text });
  h.git("checkout", "--quiet", "--detach", base);
  write(h.dir, { "Cargo.toml": text.replace('[package]\nversion = "0.0.1"', '[package]\nversion = "0.0.2"') });
  h.git("add", "-A");
  h.git("commit", "--quiet", "-m", "release");
  const run = spawnSync(process.execPath, [GUARD, "--base", base, "--head", h.git("rev-parse", "HEAD")], { cwd: h.dir, encoding: "utf8" });
  assert.equal(run.status, 1);
  assert.match(run.stderr, /Cargo\.toml: it changes more than the package version/);
});

test("a dependency list naming a workspace member follows its version; a registry package's does not", (t) => {
  const h = history(t);
  const lock = (member, external) => `version = 4\n\n[[package]]\nname = "crozier"\nversion = "${member}"\ndependencies = [\n "helper ${member}",\n "serde ${external}",\n]\n\n[[package]]\nname = "helper"\nversion = "${member}"\n\n[[package]]\nname = "serde"\nversion = "${external}"\nsource = "registry+test"\n`;
  const base = h.change({ "Cargo.lock": lock("0.0.1", "1.0.0") });
  const compare = (text) => {
    h.git("checkout", "--quiet", "--detach", base);
    write(h.dir, { "Cargo.lock": text });
    h.git("add", "-A");
    h.git("commit", "--quiet", "-m", "release");
    return spawnSync(process.execPath, [GUARD, "--base", base, "--head", h.git("rev-parse", "HEAD")], { cwd: h.dir, encoding: "utf8" });
  };
  assert.equal(compare(lock("0.0.2", "1.0.0")).status, 0, "members and references to them");
  const moved = compare(lock("0.0.2", "9.9.9"));
  assert.equal(moved.status, 1, "a registry package moved beside them");
  assert.match(moved.stderr, /Cargo\.lock: it changes more than workspace members' versions/);
});

test("a release-please manifest may change only its versions", (t) => {
  const h = history(t);
  const base = h.change({ ".release-please-manifest.json": JSON.stringify({ ".": "0.0.1" }) });
  const compare = (value) => {
    h.git("checkout", "--quiet", "--detach", base);
    write(h.dir, { ".release-please-manifest.json": JSON.stringify(value) });
    h.git("add", "-A");
    h.git("commit", "--quiet", "-m", "release");
    return spawnSync(process.execPath, [GUARD, "--base", base, "--head", h.git("rev-parse", "HEAD")], { cwd: h.dir, encoding: "utf8" });
  };
  assert.equal(compare({ ".": "0.0.2" }).status, 0);
  assert.match(compare({ ".": "0.0.2", extra: "0.0.1" }).stderr, /it adds or removes a package/);
  assert.match(compare({ ".": "latest" }).stderr, /\. is not given a semantic version/);
});

test("a same-named registry package's version is not a workspace member's", (t) => {
  const h = history(t);
  const registry = '\n[[package]]\nname = "crozier"\nversion = "1.0.0"\nsource = "registry+test"\nchecksum = "abc"\n';
  const base = h.change({ "Cargo.lock": `${real("Cargo.lock")}${registry}` });
  h.git("checkout", "--quiet", "--detach", base);
  write(h.dir, { "Cargo.lock": `${real("Cargo.lock")}${registry.replace("1.0.0", "2.0.0")}` });
  h.git("add", "-A");
  h.git("commit", "--quiet", "-m", "release");
  const run = h.guard("HEAD", ["--base", base, "--head", h.git("rev-parse", "HEAD")]);
  assert.equal(run.status, 1, run.stdout);
  assert.match(run.stderr, /Cargo\.lock: it changes more than workspace members' versions/);
});

test("an unrelated file, a new file, a deletion and a rename all fail, alone or beside a real bump", (t) => {
  const h = history(t);
  const bump = { "Cargo.toml": bumpManifest(real("Cargo.toml")), "Cargo.lock": bumpLock(real("Cargo.lock")) };
  for (const [files, remove, why] of [
    [{ ...bump, "src/lib.rs": "// changed\n" }, [], /src\/lib\.rs: the release tool edits only versions and changelogs/],
    [{ "src/new.rs": "// new\n" }, [], /src\/new\.rs: it is new/],
    [{ "NEW_CHANGELOG.md": "notes\n" }, ["CHANGELOG.md"], /CHANGELOG\.md: it is deleted/],
    [{}, ["CHANGELOG.md"], /CHANGELOG\.md: it is deleted/],
    [{ ".github/workflows/ci.yml": "name: changed\n" }, [], /\.github\/workflows\/ci\.yml: it is new/],
  ]) {
    const run = h.guard(h.change(files, remove));
    assert.equal(run.status, 1, run.stdout);
    assert.match(run.stderr, why);
  }
});

test("a branch off an older main compares against its merge base, not main's newer commits", (t) => {
  const h = history(t);
  const head = h.change({ "CHANGELOG.md": "# Changelog\n\n## notes\n" });
  h.git("checkout", "--quiet", "main");
  write(h.dir, { "src/lib.rs": "// main moved on\n" });
  h.git("add", "-A");
  h.git("commit", "--quiet", "-m", "main moved");
  const main = h.git("rev-parse", "HEAD");
  assert.equal(h.guard(head, ["--base", main, "--head", head]).status, 0);
});

test("the guard refuses an invocation it cannot read and a commit it cannot find", (t) => {
  const h = history(t);
  const head = h.change({ "CHANGELOG.md": "notes\n" });
  for (const args of [[], ["--head", head], ["--base"], ["--unknown", "x"]]) {
    const run = h.guard(head, args);
    assert.equal(run.status, 2, args.join(" "));
    assert.match(run.stderr, /usage:/);
  }
  const missing = h.guard(head, ["--base", "f".repeat(40), "--head", head]);
  assert.equal(missing.status, 2);
  assert.match(missing.stderr, /next: fetch the full history/);
});

test("the workflow's own guard command, as written in ci.yml, holds a branch to these edits", (t) => {
  const h = history(t);
  const workflow = real(".github/workflows/ci.yml");
  const command = /^\s+run: (node scripts\/release-branch-guard\.mjs .*)$/m.exec(workflow)?.[1];
  assert.ok(command, "ci.yml runs the guard");
  const asWritten = (head) => {
    h.git("checkout", "--quiet", "--detach", head);
    return spawnSync("bash", ["-e", "-c", command.replace("scripts/release-branch-guard.mjs", JSON.stringify(GUARD))], {
      cwd: h.dir, env: { ...process.env, BASE_SHA: h.base, GITHUB_OUTPUT: join(h.dir, ".git/outputs") }, encoding: "utf8",
    });
  };
  assert.equal(asWritten(h.change({ "CHANGELOG.md": "notes\n" })).status, 0);
  assert.match(readFileSync(join(h.dir, ".git/outputs"), "utf8"), /^releaseGuard=passed$/m);
  rmSync(join(h.dir, ".git/outputs"));
  assert.equal(asWritten(h.change({ "src/lib.rs": "// not a release edit\n" })).status, 1);
  assert.throws(() => statSync(join(h.dir, ".git/outputs")), "a failed guard records no pass the gate could read");
});

test("the copied reference scripts match the adopted reference's checksums, with its command contract", () => {
  const provenance = JSON.parse(real("scripts/reference-copies.json"));
  assert.equal(provenance.commit, "a73a309");
  const sha = (text) => createHash("sha256").update(text).digest("hex");
  for (const [path, entry] of Object.entries(provenance.files)) {
    const lines = readFileSync(join(REPO, path), "utf8").split("\n");
    if (entry.replacedLine) lines[entry.replacedLine.index] = Buffer.from(entry.replacedLine.base64, "base64").toString("utf8");
    assert.equal(sha(lines.join("\n")), entry.sha256, `${path} differs from the adopted reference`);
  }
  const figures = readFileSync(join(REPO, "scripts/actions-budget-figures.sh"));
  const lines = figures.toString("utf8").split("\n");
  const entry = provenance.files["scripts/actions-budget-figures.sh"];
  assert.equal(lines[1], "# Copied from dero-skills' create-repo skill and edited only there, never in a copy.");
  assert.equal(lines[2], `# source: ${provenance.source}/${entry.from}`);
  assert.equal(lines[3], `# version: ${entry.version}`);
  assert.equal(lines[4], `# sha256: ${entry.bodySha256}`);
  assert.equal(sha(lines.slice(5).join("\n")), entry.bodySha256, "the header's checksum covers every line after it");
  if (process.platform !== "win32") assert.ok(statSync(join(REPO, "scripts/actions-budget-figures.sh")).mode & 0o100, "the budget command runs it directly");
  for (const verb of ["longest-job --stage pr|cd", "job-count   --stage pr|cd", "release-cycle-time", "release-read-requests", "pr-read-requests"]) {
    assert.ok(lines.some((line) => line.startsWith(`#   scripts/actions-budget-figures.sh ${verb}`)), verb);
  }
  const unsupervised = spawnSync("bash", [join(REPO, "scripts/actions-budget-figures.sh"), "job-count"], { encoding: "utf8" });
  assert.equal(unsupervised.status, 2);
  assert.match(unsupervised.stderr, /ONEBUDGETSPEC_RESULT is unset/);
  const invalid = spawnSync("bash", [join(REPO, "scripts/actions-budget-figures.sh"), "not-a-verb"], { encoding: "utf8", env: { ...process.env, ONEBUDGETSPEC_RESULT: join(tmpdir(), "unwritten-figure.json") } });
  assert.equal(invalid.status, 2);
  assert.match(invalid.stderr, /usage: scripts\/actions-budget-figures\.sh longest-job/);
});
