// The collected-case pins: each suite's collected test cases, committed, compared
// with what that suite collects now. A speed-up may change how a suite runs its
// cases, never which cases it has. See docs/ci-gate-timing.md.
import { spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

/** The pytest arguments naming a test target's files, read off its own command so a pin cannot watch other files. */
export function pytestFiles(command) {
  const words = command.split(/\s+/);
  const start = words.indexOf("pytest");
  if (start < 0) throw new Error(`'${command}' runs no pytest; pin this suite with its own collector`);
  return words.slice(start + 1).filter((word) => !word.startsWith("-"));
}

/** Every string command a target runs. */
function commandsOf(root, project, target) {
  const parsed = JSON.parse(readFileSync(join(root, project, "project.json"), "utf8"));
  const options = parsed.targets?.[target]?.options;
  if (!options) throw new Error(`${project}/project.json has no target '${target}'`);
  return options.commands ?? [options.command];
}

function collectorOutput(root, program, args, env) {
  const run = spawnSync(program, args, { cwd: root, encoding: "utf8", maxBuffer: 256 * 1024 * 1024, env: { ...process.env, ...env } });
  if (run.status !== 0) {
    throw new Error(`'${program} ${args.join(" ")}' exited ${run.status ?? run.error}: ${`${run.stdout}\n${run.stderr}`.trim().slice(-4000)}`);
  }
  return run.stdout;
}

const COLLECTORS = {
  /** The node ids `pytest --collect-only` prints for the target's files. */
  pytest(root, suite) {
    const command = commandsOf(root, suite.project, suite.target).find((candidate) => candidate.includes("pytest"));
    const output = collectorOutput(root, "uv", ["run", "--locked", "--all-packages", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", ...pytestFiles(command)]);
    return output.split(/\r?\n/).filter((line) => line.includes("::"));
  },
  /** Every test id a unittest file defines, for a target that runs its files as scripts. */
  unittest(root, suite) {
    const files = suite.files ?? commandsOf(root, suite.project, suite.target).flatMap((command) => command.match(/\S+_test\.py/g) ?? []);
    const script = `
import importlib.util, sys, unittest
def walk(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from walk(item)
        else:
            yield item
for path in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location("__suite_cases__", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    for case in walk(unittest.defaultTestLoader.loadTestsFromModule(module)):
        print(path + "::" + case.id().removeprefix("__suite_cases__."))
`;
    return collectorOutput(root, "uv", ["run", "--locked", "--all-packages", "python", "-c", script, ...files]).split(/\r?\n/).filter((line) => line.includes("::"));
  },
  /** `<binary> <test>` for every test `cargo nextest list` selects with the target's own arguments. */
  nextest(root, suite) {
    const output = collectorOutput(root, "cargo", ["nextest", "list", "--message-format", "oneline", "--color", "never", ...suite.arguments]);
    return output.split(/\r?\n/).filter((line) => line.trim());
  },
};

/** What `suite` collects in the checkout at `root`, sorted. */
export function collect(root, suite) {
  const collector = COLLECTORS[suite.collector];
  if (!collector) throw new Error(`no collector '${suite.collector}'`);
  return [...new Set(collector(root, suite))].sort();
}

const pinsDirectory = (root) => process.env.CROZIER_SUITE_CASES_PINS ?? join(root, "tools/ci/suite-cases/pins");

export const pinPath = (root, suite) => join(pinsDirectory(root), `${suite.name}.txt`);

export function readPin(root, suite) {
  return readFileSync(pinPath(root, suite), "utf8").split("\n").filter(Boolean);
}

export function writePin(root, suite, cases) {
  mkdirSync(pinsDirectory(root), { recursive: true });
  writeFileSync(pinPath(root, suite), `${cases.join("\n")}\n`);
}

/** One line per case the live collection lost or gained against its pin; empty when they are the same set. */
export function difference(name, pinned, live) {
  const [before, now] = [new Set(pinned), new Set(live)];
  return [
    ...pinned.filter((id) => !now.has(id)).map((id) => `${name}: lost ${id}`),
    ...live.filter((id) => !before.has(id)).map((id) => `${name}: gained ${id}`),
  ];
}

export function suitesIn(root) {
  return JSON.parse(readFileSync(join(root, "tools/ci/suite-cases/suites.json"), "utf8"));
}
