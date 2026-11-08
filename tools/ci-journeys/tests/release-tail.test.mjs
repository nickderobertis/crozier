// The release tail: release.yml's final `major-tag` step, run as GitHub runs it, with the
// real onebudgetspec and the copied figures script, inside a real temporary git release.
// Only onevcs's GitHub answers are doubled: a PATH stand-in serves answers recorded from
// `onevcs host` and logs each question. These are consumers of recorded answers; GitHub
// Actions produced the run and job records, and onevcs's HTTP reads the costs, they replay.
//
// fixtures/release-tail/v0.0.160-*.json were captured on 2026-11-08 with onevcs 0.60.0
// against the public v0.0.160 release: #791 is an ordinary pull request of the four-lane
// shape (its head still ran the transitional jobs, which these fixtures drop), #777 a
// release-plz pull request whose test lanes the content guard let skip. The same three
// questions asked through onevcs-cli@0.57.6, the version release.yml installs, returned
// answers identical to these (compared with `jq -S`, 2026-11-08).
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { delimiter, join } from "node:path";
import { test } from "node:test";
import { REPO, write } from "./support.mjs";

const FIXTURES = join(REPO, "tools/ci-journeys/tests/fixtures/release-tail");
const recorded = (name) => JSON.parse(readFileSync(join(FIXTURES, `v0.0.160-${name}.json`), "utf8"));
const LANES = JSON.parse(readFileSync(join(REPO, ".github/governance.json"), "utf8")).required_checks;
const TAIL_IDS = ["crozier-ci-check-time", "crozier-ci-job-count", "crozier-pr-read-requests"];
const real = (path) => readFileSync(join(REPO, path), "utf8");
// The tail runs on ubuntu-latest alone, and the stand-in is a bash script on PATH.
const posix = { skip: process.platform === "win32" ? "the release tail runs on Linux only" : false };

/** release.yml's last `major-tag` step: its one-line `run:` and its `env:` keys. */
function tailStep() {
  const workflow = real(".github/workflows/release.yml");
  const job = workflow.slice(workflow.indexOf("\n  major-tag:\n"));
  const step = job.slice(job.lastIndexOf("\n      - name: ") + 1).split("\n").filter((line) => line.startsWith("        ") || line.startsWith("      - "));
  const run = step.find((line) => line.startsWith("        run: "));
  assert.ok(run && !run.endsWith("|"), "the tail step runs one command");
  const env = step.slice(step.indexOf("        env:") + 1).filter((line) => /^ {10}\w+:/.test(line)).map((line) => line.trim().split(":")[0]);
  return { name: step[0].replace("      - name: ", ""), run: run.replace("        run: ", ""), env };
}

const hex = (seed) => createHash("sha256").update(String(seed)).digest("hex").slice(0, 40);
const at = (base, seconds) => new Date(Date.parse(base) + seconds * 1000).toISOString().replace(/\.000Z$/, "Z");

/**
 * One pull request's `change-checks` answer, from a recorded one: its head's `ci` run with
 * the jobs the four-lane shape reports, each lasting `seconds(job)` from its recorded start.
 */
function changeChecks(template, number, merged, seconds = (job) => (Date.parse(job.completed_at) - Date.parse(job.started_at)) / 1000) {
  const answer = structuredClone(recorded(`change-checks-${template}`));
  const head = hex(`head-${number}`);
  const text = JSON.stringify(answer).replaceAll(answer.change.head_sha, head);
  const out = JSON.parse(text);
  out.change = { number, head_sha: head, merged_at: merged };
  for (const run of out.runs) {
    run.jobs = run.jobs.filter((job) => LANES.includes(job.name));
    for (const job of run.jobs) if (job.runner_name !== null) job.completed_at = at(job.started_at, seconds(job));
  }
  return out;
}

/**
 * A real git release in a temporary directory: the repository's budgets.yaml and figures
 * script at a tagged commit, the floating major tag beside it, and a published artifact
 * outside the tree; plus recorded answers for `prs` (template, seconds) and a stand-in onevcs.
 */
function release(t, prs, { budgets = real("budgets.yaml"), drop = [] } = {}) {
  const base = mkdtempSync(join(process.env.ONEPIPELINE_NODE_SCRATCH_DIR ?? tmpdir(), "release-tail-"));
  t.after(() => rmSync(base, { recursive: true, force: true }));
  const repo = join(base, "repo"), answers = join(base, "answers"), bin = join(base, "bin"), runnerTemp = join(base, "runner-temp");
  for (const dir of [repo, answers, bin, runnerTemp]) mkdirSync(dir, { recursive: true });
  const git = (...args) => execFileSync("git", args, { cwd: repo, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
  write(repo, { "budgets.yaml": budgets, "scripts/actions-budget-figures.sh": real("scripts/actions-budget-figures.sh"), "justfile": real("justfile") });
  git("init", "--quiet", "--initial-branch=main");
  git("-c", "user.name=t", "-c", "user.email=t@example.com", "add", "-A");
  git("-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "--quiet", "-m", "chore: release v0.0.2");
  git("tag", "v0.0.2");
  git("tag", "v0");
  symlinkSync(join(REPO, "node_modules"), join(repo, "node_modules"), "junction");
  const artifact = join(base, "published", "crozier-v0.0.2-x86_64-unknown-linux-gnu.tar.gz");
  write(join(base, "published"), { "crozier-v0.0.2-x86_64-unknown-linux-gnu.tar.gz": "the published archive\n" });

  const commit = git("rev-parse", "HEAD");
  const changes = prs.map(([template, seconds], i) => changeChecks(template, 800 + i, at("2026-11-08T08:00:00Z", 600 * i), seconds));
  const rc = recorded("release-changes");
  rc.tag = "v0.0.2"; rc.commit = commit; rc.previous_tag = "v0.0.1"; rc.previous_commit = hex("previous");
  rc.commits = changes.map((c) => ({ sha: hex(`merge-${c.change.number}`), change: c.change.number }));
  rc.changes = changes.map((c) => ({ ...rc.changes[0], number: c.change.number, title: `change ${c.change.number}`, head_sha: c.change.head_sha, merged_at: c.change.merged_at, merge_commit_sha: hex(`merge-${c.change.number}`) }));
  write(answers, { "release-changes.json": JSON.stringify(rc) });
  for (const c of changes) if (!drop.includes(c.change.number)) write(answers, { [`change-checks-${c.change.number}.json`]: JSON.stringify(c) });
  // The stand-in answers only the questions the figures ask, for this release, and refuses
  // any it has no recording of the way onevcs refuses a failed read: a non-zero exit.
  write(bin, { onevcs: `#!/usr/bin/env bash
set -euo pipefail
printf '%s\\n' "$*" >> ${JSON.stringify(join(base, "calls.log"))}
[ "$1 $3 $4" = "host --repo nickderobertis/crozier" ] || { echo "onevcs double: unexpected $*" >&2; exit 2; }
case "$2" in
  release-changes) [ "$5 $6" = "--tag v0.0.2" ] || { echo "onevcs: no release $6" >&2; exit 1; }; file=release-changes ;;
  change-checks) file="change-checks-$6"
    [ -f ${JSON.stringify(answers)}/"$file.json" ] || { echo "onevcs: GitHub answered 404 for #$6" >&2; exit 1; }
    jq -e --arg head "$8" --arg merged "\${10}" '.change.head_sha == $head and .change.merged_at == $merged' ${JSON.stringify(answers)}/"$file.json" >/dev/null ||
      { echo "onevcs double: #$6 asked at a head or merge it did not record" >&2; exit 2; } ;;
  *) echo "onevcs double: unexpected $2" >&2; exit 2 ;;
esac
cat ${JSON.stringify(answers)}/"$file.json"
` });
  chmodSync(join(bin, "onevcs"), 0o755);
  writeFileSync(join(base, "event.json"), JSON.stringify({ action: "published", release: { tag_name: "v0.0.2", prerelease: false } }));
  const env = {
    ...process.env,
    PATH: [bin, join(REPO, "node_modules", ".bin"), process.env.PATH].join(delimiter),
    GH_TOKEN: "recorded-answers-need-no-token",
    GITHUB_REPOSITORY: "nickderobertis/crozier", GITHUB_EVENT_NAME: "release", GITHUB_EVENT_PATH: join(base, "event.json"),
    GITHUB_REF_TYPE: "tag", GITHUB_REF_NAME: "v0.0.2", GITHUB_RUN_ID: "42460000000", RUNNER_NAME: "GitHub Actions 1", RUNNER_TEMP: runnerTemp,
  };
  for (const key of ["ONEBUDGETSPEC_RESULT", "ONEVCS", "GITHUB_TOKEN"]) delete env[key];
  const shell = (command) => spawnSync("bash", ["--noprofile", "--norc", "-eo", "pipefail", "-c", command], { cwd: repo, env, encoding: "utf8" });
  const calls = () => (existsSync(join(base, "calls.log")) ? readFileSync(join(base, "calls.log"), "utf8").trim().split("\n") : []);
  const published = () => ({ tags: git("show-ref", "--tags"), head: git("rev-parse", "HEAD"), status: git("status", "--porcelain"), artifact: readFileSync(artifact, "utf8") });
  return { repo, shell, calls, published, changes };
}

const ordinary = (seconds) => ["791", seconds];
const guarded = ["777"];
const within = (job) => ({ lint: 1150, "test-linux": 1700, "test-windows": 1500, "test-macos": 1600 })[job.name];
const line = (out, id) => out.split("\n").find((l) => l.startsWith(`budget ${id}:`)) ?? "";

test("release.yml's tail is major-tag's last step: onebudgetspec over the release-tail label, with the token alone", () => {
  const step = tailStep();
  assert.deepEqual(step, { name: "Report the release-tail budgets", run: "onebudgetspec check budgets.yaml --label release-tail", env: ["GH_TOKEN"] });
});

test("over 30 pull requests the tail reports each figure within its line, asking each question once", posix, (t) => {
  const r = release(t, [...Array.from({ length: 29 }, () => ordinary(within)), guarded]);
  const before = r.published();
  const run = r.shell(tailStep().run);
  assert.equal(run.status, 0, run.stdout + run.stderr);
  assert.match(line(run.stdout, "crozier-ci-check-time"), /actual 1700 seconds, budget 1800 seconds.* within/);
  assert.match(line(run.stdout, "crozier-ci-job-count"), /actual 4 jobs, budget 4 jobs.* within/);
  assert.match(line(run.stdout, "crozier-pr-read-requests"), /actual 2 requests, budget 2 requests.* within/);
  // One release read and one read per pull request, shared by all three figures.
  const calls = r.calls();
  assert.equal(calls.length, 31, calls.join("\n"));
  assert.equal(calls.filter((c) => c.startsWith("host release-changes ")).length, 1);
  assert.deepEqual(calls.filter((c) => c.startsWith("host change-checks ")).map((c) => c.split(" ")[5]), r.changes.map((c) => String(c.change.number)));
  assert.deepEqual(r.published(), before, "the tail moves no tag, writes no file and leaves the artifact as published");

  // The saved answers keep their original cost: a second pass asks nothing and still reports
  // each read the first one made, with the detail by workflow, job and runner OS.
  const json = r.shell("onebudgetspec check budgets.yaml --label release-tail --json");
  assert.equal(json.status, 0, json.stderr);
  assert.equal(r.calls().length, 31, "the second pass read the saved answers");
  const results = Object.fromEntries(JSON.parse(json.stdout).results.map((b) => [b.id, b]));
  assert.deepEqual(Object.keys(results), TAIL_IDS, "the label selects the three tail budgets");
  assert.equal(results["crozier-pr-read-requests"].actual, 2);
  const reads = results["crozier-pr-read-requests"].detail;
  assert.equal(reads.split("\n").filter((l) => / 2 requests$/.test(l)).length, 30);
  assert.match(reads, /#800: 2 requests\n {2}repos\/nickderobertis\/crozier\/actions\/runs\?per_page=100&head_sha=[0-9a-f]{40}&event=pull_request\n {2}repos\/nickderobertis\/crozier\/actions\/runs\/\d+\/jobs/);
  const jobs = results["crozier-ci-job-count"].detail;
  assert.match(jobs, /#800: 4 jobs\n {2}per workflow:\n {4}ci: 4\n {2}per runner OS:\n {4}Linux: 2\n {4}Windows: 1\n {4}macOS: 1/);
  assert.match(jobs, /#829: 1 jobs\n {2}per workflow:\n {4}ci: 1\n {2}per runner OS:\n {4}Linux: 1/, "the guarded release pull request ran lint alone");
  assert.match(results["crozier-ci-check-time"].detail, /#800:\n {2}ci \/ test-linux: 1700s\n/);
  assert.match(results["crozier-ci-check-time"].detail, /longest per runner OS:\n {4}Linux: ci \/ test-linux: 1700s\n {4}Windows: ci \/ test-windows: 1500s\n {4}macOS: ci \/ test-macos: 1600s/);
});

test("a one-pull-request release is measured the same way", posix, (t) => {
  const r = release(t, [ordinary(within)]);
  const run = r.shell(tailStep().run);
  assert.equal(run.status, 0, run.stdout + run.stderr);
  assert.match(line(run.stdout, "crozier-ci-job-count"), /actual 4 jobs/);
  assert.equal(r.calls().length, 2);
});

test("an over reading turns the step red after publication, changing nothing published", posix, (t) => {
  // The recorded job durations of #791's head: its Mac lane ran 110 minutes.
  const r = release(t, [ordinary(), ordinary(within), guarded]);
  const before = r.published();
  const run = r.shell(tailStep().run);
  assert.equal(run.status, 1, run.stdout + run.stderr);
  assert.match(line(run.stdout, "crozier-ci-check-time"), /actual 6614 seconds, budget 1800 seconds.* over/);
  assert.match(line(run.stdout, "crozier-ci-job-count"), /within/);
  assert.match(run.stderr, /#800:\n {2}ci \/ test-macos: 6614s/, "the breakdown is in the step's log");
  assert.deepEqual(r.published(), before, "v0.0.2, v0 and the artifact are exactly as published");
});

test("the figure is judged by onebudgetspec alone: the same answers read over a lowered line", posix, (t) => {
  const lowered = real("budgets.yaml").replace("threshold: 4\n", "threshold: 3\n");
  assert.notEqual(lowered, real("budgets.yaml"));
  const r = release(t, [ordinary(within)], { budgets: lowered });
  const run = r.shell(tailStep().run);
  assert.equal(run.status, 1);
  assert.match(line(run.stdout, "crozier-ci-job-count"), /actual 4 jobs, budget 3 jobs.* over/);
});

test("missing data is an error, never a zero: an unread pull request, and a pull request with no run", posix, (t) => {
  const unread = release(t, [ordinary(within), ordinary(within)], { drop: [801] });
  const run = unread.shell(tailStep().run);
  assert.equal(run.status, 3, run.stdout + run.stderr);
  for (const id of TAIL_IDS) assert.match(line(run.stdout, id), /error/, id);
  assert.match(run.stderr + run.stdout, /GitHub answered 404 for #801/);

  const r = release(t, [ordinary(within)]);
  const answer = join(r.repo, "..", "answers", "change-checks-800.json");
  writeFileSync(answer, JSON.stringify({ ...JSON.parse(readFileSync(answer, "utf8")), runs: [] }));
  const none = r.shell(tailStep().run);
  assert.equal(none.status, 3, none.stdout + none.stderr);
  assert.match(none.stderr + none.stdout, /missing: #800 has no pull_request run at its head/);
  assert.doesNotMatch(none.stdout, /actual 0/);
});

test("the strict gate's budgets invocation leaves the tail out and asks GitHub nothing", posix, (t) => {
  const recipe = real("justfile").split("\n").find((l) => l.includes("onebudgetspec check budgets.yaml"));
  assert.equal(recipe, "    @[ ! -f budgets.yaml ] || bunx onebudgetspec check budgets.yaml --exclude-label release-tail --exclude-label onepipeline");
  const r = release(t, [ordinary()]);
  const run = r.shell(recipe.trim().replace(/^@/, ""));
  assert.equal(run.status, 0, run.stdout + run.stderr);
  assert.equal(run.stdout, "", "no root budget is measured by the gate");
  assert.deepEqual(r.calls(), []);
});
