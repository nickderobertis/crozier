"""The weekly Fern goldens run, phase by phase, as the workflow's jobs run it:
each job a fresh clone of a bare local repository standing in for crozier's
remote, the real `tools/fern-goldens/weekly.py` and the real per-family recipe
behind it. Only Fern (`fern`, and the `docker` it would need) and the GitHub
API client (`gh`) are stood in; crozier's comparison engine runs for real as
the `crozier` binary `crozier:build` leaves in `target/debug/`, and so does its
refusal path.

The synthetic tree carries one reference of each kind the decision reads: a
vendored corpus fixture (`alpha`), a CORPUS.md row fetched over a stood-in
`curl` (`beta`), a hand-written fixture (`lantern`) and a refusal class
(`default-not-enum-value`, copied from the real registry). Its committed
references are what the recipe wrote at an older stand-in pair; each run checks
the pair the real `metadata.json` declares, so crozier's own version stamps are
the candidate's, as they are once the decision job builds crozier from the tree.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
import unittest.mock
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, NamedTuple

os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
RECORD = json.loads((REPO / "assets/scaffolding/metadata.json").read_text(encoding="utf-8"))


class Versions(NamedTuple):
    """A Fern pair as these journeys spell it."""

    cli: str
    generator: str


CANDIDATE = Versions(RECORD["cliVersion"], RECORD["generatorVersion"])


def older(version: str) -> str:
    """A version the candidate is not: its minor lowered (or its major, at minor 0)."""
    major, minor, _patch = (int(part) for part in version.split("."))
    return f"{major}.{minor - 1}.0" if minor else f"{major - 1}.0.0"


OLD = Versions(older(CANDIDATE.cli), older(CANDIDATE.generator))
CROZIER = Path(os.environ.get("CROZIER_WEEKLY_TEST_BIN") or REPO / "target" / "debug" / "crozier")
REFUSAL_CLASS = "default-not-enum-value"
KNOWN_FAILURE = REPO / "tests/fixtures/calorieninjas.com/known-fern-failure.json"

MIRRORED = (
    "tools/fern-goldens/weekly.py",
    "tools/fern-goldens/fern-references.py",
    "tools/fern-goldens/fern-goldens",
    "tools/fern-goldens/generate-fern-fixture.sh",
    "tools/fern-goldens/golden_overlay.py",
    "tools/fern-goldens/certified_pair.py",
    "tools/fern-refusals/fern-refusals.py",
    "tools/corpus/corpus-lib.sh",
    "tools/corpus/corpus_remote_ref_pins.py",
    "tools/corpus/fetch-corpus.sh",
    "tools/surface-census/openapi-surface-census.py",
    "scripts/lib.sh",
    "tests/fixtures/corpus-aliases.tsv",
    "tests/fixtures/corpus-remote-ref-pins.tsv",
)

DOCUMENT = """\
openapi: 3.0.3
info:
  title: {title}
  version: 1.0.0
paths:
  /lanterns/{{lanternId}}:
    get:
      operationId: getLantern
      parameters:
        - name: lanternId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: A lantern
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Lantern"
components:
  schemas:
    Lantern:
      type: object
      properties:
        name:
          type: string
        lit:
          type: boolean
"""

# Every gate here is one the decision reads from the tree's own table; each is
# the real crozier: `crozier compare` (the parity engine and the departure
# catalog) for an SDK tree, and crozier's refusal of a class's probe for a
# refusal class (what tests/refusal_registry.rs asserts, a refusal exiting 1).
GATES = """\
family\tscope\tverdict\tcommand
corpus\titem\texit:0/3\t{root}/target/release/crozier compare {root}/tests/fixtures/{item}/crozier.yml
handwritten\titem\texit:0/3\t{root}/target/release/crozier compare {root}/docs/openapi-surface/handwritten/{item}/crozier.yml
refusals\titem\texit:1/0\t{root}/target/release/crozier --no-config generate --spec {root}/docs/fern-refusals/{item}/probe.yml --output {scratch}/out
"""

# A stand-in for Fern: it answers `fern check` and `fern generate` in the
# workspace the recipe scaffolds, from rules keyed by the document's title, and
# writes the tree the test prepared for that title, stamped with the CLI and
# generator versions the workspace names, as Fern stamps its own.
FERN = r"""
#!/usr/bin/env python3
import json, os, pathlib, re, shutil, sys

args = sys.argv[1:]
workspace = pathlib.Path.cwd()
text = (workspace / "openapi" / "openapi.yml").read_text(encoding="utf-8")
title = re.search(r"(?m)^  title: (.+)$", text).group(1).strip()
config = json.loads(pathlib.Path(os.environ["STAND_IN_FERN"]).read_text(encoding="utf-8"))
rule = config.get("rules", {}).get(title, {})
with open(config["calls"], "a", encoding="utf-8") as calls:
    calls.write(json.dumps({"command": args[0], "title": title}) + "\n")
if args[0] == "check":
    code, message = rule.get("check", [0, ""])
    print(f"issue: {message}" if message else "All checks passed")
    sys.exit(code)
code, message = rule.get("generate", [0, ""])
if code:
    print(message if rule.get("raw") else f"[api]: python-sdk [error] {message}")
    sys.exit(code)
cli = json.loads((workspace / "fern.config.json").read_text(encoding="utf-8"))["version"]
generator = re.search(r"(?m)^\s+version: (\S+)$", (workspace / "generators.yml").read_text(encoding="utf-8")).group(1)
if "--preview" in args:
    out = pathlib.Path(args[args.index("--output") + 1]) / "fern-python-sdk"
else:
    out = workspace.parent / "generated" / "python"
shutil.copytree(pathlib.Path(config["trees"]) / title, out, dirs_exist_ok=True)
metadata = out / ".fern" / "metadata.json"
record = json.loads(metadata.read_text(encoding="utf-8"))
record["cliVersion"], record["generatorVersion"] = cli, generator
record["generatorConfig"].update(config.get("generator_config", {}))
metadata.write_text(json.dumps(record, indent=2), encoding="utf-8")
wrapper = next(out.rglob("core/client_wrapper.py"))
source = wrapper.read_text(encoding="utf-8")
if config.get("sdk_headers"):
    package = wrapper.parent.parent.name
    source = re.sub(
        r'(?m)^(\s+)("X-Fern-Platform": .*\n)',
        lambda m: f'{m.group(1)}{m.group(2)}{m.group(1)}"X-Fern-SDK-Name": "{package}",\n'
        f'{m.group(1)}"X-Fern-SDK-Version": "{generator}",\n',
        source,
    )
wrapper.write_text(source, encoding="utf-8")
for suffix, old, new in config.get("tweaks", {}).get(title, []):
    target = next(path for path in out.rglob("*") if path.as_posix().endswith(suffix))
    if old is None:
        target.unlink()  # Fern no longer writes this file
    else:
        target.write_text(target.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
"""

GH = r"""
#!/usr/bin/env python3
import json, os, pathlib, sys

state_path = pathlib.Path(os.environ["GH_STATE"])
state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {"labels": [], "pulls": []}
args = sys.argv[1:]
args = args[: args.index("--repo")] + args[args.index("--repo") + 2 :]
command = " ".join(args[:2])


def option(name):
    return args[args.index(name) + 1] if name in args else None


def save():
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def done(output=""):
    save()
    if command in os.environ.get("GH_LOSE", "").split(","):
        print(f"gh: {command}: connection reset after the request was sent", file=sys.stderr)
        sys.exit(1)
    sys.stdout.write(output)
    sys.exit(0)


if not os.environ.get("GH_TOKEN"):
    print("gh: not authenticated", file=sys.stderr)
    sys.exit(4)
state.setdefault("calls", []).append(args)
if command in os.environ.get("GH_FAIL", "").split(","):
    save()
    print(f"gh: {command}: refused by the stand-in", file=sys.stderr)
    sys.exit(1)
pulls = state["pulls"]
if command == "label list":
    done(json.dumps([{"name": name} for name in state["labels"]]))
if command == "label create":
    state["labels"].append(args[2])
    done()
if command == "pr list":
    found = [p for p in pulls if p["head"] == option("--head") and p["state"] == option("--state")]
    done(json.dumps(found))
if command == "pr create":
    if option("--label") not in state["labels"]:
        print("gh: label not found", file=sys.stderr)
        sys.exit(1)
    number = len(pulls) + 1
    pulls.append({
        "number": number, "url": f"https://example.test/pull/{number}", "head": option("--head"),
        "base": option("--base"), "title": option("--title"),
        "body": pathlib.Path(option("--body-file")).read_text(encoding="utf-8"),
        "labels": [{"name": option("--label")}], "autoMergeRequest": None, "state": "open",
    })
    done(f"https://example.test/pull/{number}\n")
pull = next(p for p in pulls if str(p["number"]) == args[2])
if command == "pr edit":
    pull["title"] = option("--title")
    pull["body"] = pathlib.Path(option("--body-file")).read_text(encoding="utf-8")
    if {"name": option("--add-label")} not in pull["labels"]:
        pull["labels"].append({"name": option("--add-label")})
    done()
if command == "pr merge":
    pull["autoMergeRequest"] = None if "--disable-auto" in args else {"mergeMethod": "SQUASH"}
    done()
print(f"gh stand-in: unsupported {args}", file=sys.stderr)
sys.exit(2)
"""

JUST = r"""
#!/usr/bin/env python3
import os, pathlib, subprocess, sys

args = sys.argv[1:]
if "fetch-corpus" not in args:
    print(f"just stand-in: only fetch-corpus, not {args}", file=sys.stderr)
    sys.exit(2)
root = pathlib.Path(os.environ["CROZIER_FERN_WEEKLY_ROOT"])
result = subprocess.run(
    [root / "tools" / "corpus" / "fetch-corpus.sh", *args[args.index("fetch-corpus") + 1 :]],
    cwd=root, text=True, capture_output=True, check=False,
)
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
sys.exit(result.returncode)
"""

CURL = r"""
#!/usr/bin/env python3
import json, os, pathlib, sys

args = sys.argv[1:]
served = json.loads(os.environ.get("SERVED_DOCUMENTS", "{}"))
url = next((arg for arg in args if arg.startswith("https://")), "")
if any(name and name in url for name in os.environ.get("FAIL_FETCH", "").split(",")):
    print("curl: (22) The requested URL returned error: 404", file=sys.stderr)
    sys.exit(22)
body = next((body for fragment, body in served.items() if fragment in url), None)
if body is None:
    print(f"curl stand-in: nothing served at {url}", file=sys.stderr)
    sys.exit(6)
if "--output" in args:
    pathlib.Path(args[args.index("--output") + 1]).write_text(body, encoding="utf-8")
    pathlib.Path(args[args.index("--dump-header") + 1]).write_text("HTTP/1.1 200 OK\n", encoding="utf-8")
    sys.stdout.write("200")
elif "-o" in args:
    pathlib.Path(args[args.index("-o") + 1]).write_text(body, encoding="utf-8")
else:
    sys.stdout.write(body)
"""


Completed = subprocess.CompletedProcess[str]


@dataclass
class Journey:
    """One workflow run as the journeys drive it: each phase's process, in the
    order the jobs run, and the artifacts they leave."""

    artifacts: Path
    resolve: Completed | None = None
    plan: Completed | None = None
    shards: list[Completed] = field(default_factory=list)
    assemble: Completed | None = None
    decide: Completed | None = None
    decision: dict[str, object] | None = None
    publish: Completed | None = None

    def ran(self, phase: str) -> Completed:
        result = getattr(self, phase)
        if not isinstance(result, subprocess.CompletedProcess):
            raise AssertionError(f"the {phase} phase did not run")
        return result

    def recorded(self) -> dict[str, object]:
        if self.decision is None:
            raise AssertionError("the decision phase recorded no decision")
        return self.decision

    def outcome(self) -> object:
        return self.recorded()["outcome"]

    def failing(self) -> dict[str, list[str]]:
        failing = self.recorded()["failing"]
        assert isinstance(failing, dict)
        return {family: [entry["item"] for entry in entries] for family, entries in failing.items()}

    def unfetchable(self) -> list[str]:
        entries = self.recorded()["unfetchable"]
        assert isinstance(entries, list)
        return [entry["item"] for entry in entries]

    def gate_commands(self) -> list[object]:
        runs = self.recorded()["gates"]
        assert isinstance(runs, list)
        return [entry["command"] for entry in runs]


def write_executable(path: Path, source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(source).lstrip(), encoding="utf-8", newline="\n")
    path.chmod(0o755)


@unittest.skipIf(os.name == "nt", "the weekly workflow runs its scripts on Linux")
@unittest.skipUnless(CROZIER.is_file(), f"build crozier first: {CROZIER} (crozier:build, which test-weekly depends on)")
class WeeklyRunTests(unittest.TestCase):
    # The seed tree and the stand-in's Fern trees, built once for the class:
    # every case starts from a copy of the same committed references.
    pristine: tempfile.TemporaryDirectory[str] | None = None

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.pristine is not None:
            cls.pristine.cleanup()
            cls.pristine = None

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.scratch = Path(self.temporary.name)
        git_config = self.scratch / "gitconfig"
        git_config.write_text(
            "[maintenance]\n\tauto = false\n[receive]\n\tautoGc = false\n"
            "[user]\n\tname = Weekly Test\n\temail = weekly@example.test\n[init]\n\tdefaultBranch = main\n",
            encoding="utf-8",
        )
        patched = unittest.mock.patch.dict(os.environ, {"GIT_CONFIG_GLOBAL": str(git_config)})
        patched.start()
        self.addCleanup(patched.stop)
        self.bin = self.scratch / "bin"
        write_executable(self.bin / "fern", FERN)
        write_executable(self.bin / "gh", GH)
        write_executable(self.bin / "just", JUST)
        write_executable(self.bin / "curl", CURL)
        write_executable(self.bin / "docker", "#!/bin/sh\nexit 0\n")
        self.fern = self.scratch / "fern.json"
        self.gh_state = self.scratch / "gh.json"
        self.remote = self.scratch / "remote.git"
        self.clones = 0
        # A CORPUS.md row's document is what it fetches; the copy beside it is crozier's input.
        self.served = {"example.test/beta/": DOCUMENT.format(title="Beta Lanterns")}
        self.refusal_rule = {"check": [1, "Default value '-createdAt' is not a valid enum value"], "generate": [1, ""]}
        cls = type(self)
        if cls.pristine is None:
            cls.pristine = tempfile.TemporaryDirectory()
            self.trees = Path(cls.pristine.name) / "fern-trees"
            self.stand_in({"rules": {"probe": self.refusal_rule}})
            self.build_seed(Path(cls.pristine.name) / "seed")
        self.trees = Path(cls.pristine.name) / "fern-trees"
        self.seed = self.scratch / "seed"
        shutil.copytree(Path(cls.pristine.name) / "seed", self.seed, symlinks=True)
        self.stand_in({"rules": {"probe": self.refusal_rule}})

    def stand_in(self, config: dict[str, object]) -> None:
        """The stood-in Fern's behaviour for the next generation."""
        self.fern.write_text(
            json.dumps({"trees": str(self.trees), "calls": str(self.scratch / "fern-calls.jsonl"), **config}),
            encoding="utf-8",
        )

    def fern_tree(self, title: str, spec: Path) -> None:
        """Fern's tree for one document, as the stand-in writes it: crozier's own
        output in Fern's spelling (its header comment, `X-Fern-*` identity
        headers and no published SDK name or version)."""
        out = self.trees / title
        subprocess.run(
            [str(CROZIER), "--no-config", "generate", "--spec", str(spec), "--output", str(out)],
            check=True,
            capture_output=True,
        )
        for path in out.rglob("*.py"):
            text = path.read_text(encoding="utf-8").replace(
                "auto-generated by crozier from an OpenAPI document", "auto-generated by Fern from our API Definition"
            )
            if path.name == "client_wrapper.py":
                text = re.sub(r'(?m)^\s+"X-Crozier-SDK-(Name|Version)": .*\n', "", text).replace(
                    "X-Crozier-", "X-Fern-"
                )
            path.write_text(text, encoding="utf-8")

    def build_seed(self, root: Path) -> None:
        for path in MIRRORED:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / path, root / path)
        (root / "assets/scaffolding").mkdir(parents=True)
        (root / "assets/scaffolding/metadata.json").write_text(
            json.dumps({**RECORD, "cliVersion": OLD.cli, "generatorVersion": OLD.generator}, indent=2) + "\n",
            encoding="utf-8",
        )
        (root / ".gitignore").write_text("/.local\n/target\n", encoding="utf-8")
        (root / "justfile").write_text("default:\n    @true\n", encoding="utf-8")
        fixtures = root / "tests/fixtures"
        (fixtures / "CORPUS.md").write_text(
            "# Corpus\n\n| # | name | method | source | pinned ref | license | decision | shapes |\n"
            "|---:|---|---|---|---|---|---|---|\n"
            "| 1 | `beta` | test | https://example.test/beta/openapi.yaml | `1` | MIT | link-ok | beta |\n",
            encoding="utf-8",
        )
        (fixtures / "flat-goldens.txt").write_text("# fixture|spec\n", encoding="utf-8")
        (fixtures / "fern-generator-config.txt").write_text("# fixture|audiences|…\n", encoding="utf-8")
        (fixtures / "fern-pair-checks.tsv").write_text(
            "fern_cli_version\tfern_python_sdk_version\tchecked_on\toutcome\n", encoding="utf-8"
        )
        compare = 'spec: ./openapi.yml\nreference:\n  command: cp -R {tree}/. "$CROZIER_REFERENCE_OUTPUT"\n'
        for fixture, title in (("alpha", "Alpha Lanterns"), ("beta", "Beta Lanterns")):
            # An empty golden directory is what lists the fixture in the corpus family.
            (fixtures / fixture / "expected").mkdir(parents=True)
            (fixtures / fixture / "openapi.yml").write_text(DOCUMENT.format(title=title), encoding="utf-8")
            (fixtures / fixture / "crozier.yml").write_text(compare.format(tree="expected"), encoding="utf-8")
            self.fern_tree(title, fixtures / fixture / "openapi.yml")
        handwritten = root / "docs/openapi-surface/handwritten/lantern"
        handwritten.mkdir(parents=True)
        (handwritten / "openapi.yml").write_text(DOCUMENT.format(title="Harbour Lanterns"), encoding="utf-8")
        (handwritten / "crozier.yml").write_text(compare.format(tree="fern-expected"), encoding="utf-8")
        # Placeholder provenance the recipe restates when it generates the tree.
        placeholder = 'fern_cli_version = "0.0.0"\nfern_python_sdk_version = "0.0.0"\n'  # certified-pair: stand-in
        (handwritten / "evidence.toml").write_text(placeholder + 'digest = "0"\n', encoding="utf-8")
        self.fern_tree("Harbour Lanterns", handwritten / "openapi.yml")
        (root / "docs/fern-measurements").mkdir(parents=True)
        (root / "docs/fern-measurements/cases.tsv").write_text(
            "case\tdocument\tenum_type\tlayout\toverlay\n", encoding="utf-8"
        )
        (root / "docs/openapi-surface/probes").mkdir(parents=True)
        (root / "docs/openapi-surface/probe-expected").mkdir(parents=True)
        (root / "docs/openapi-surface/probe-expected/MANIFEST.tsv").write_text(
            "key\tform\tverdict\tartifact\tcontrol\tdigest\n", encoding="utf-8"
        )
        registry = root / "docs/fern-refusals"
        (registry / REFUSAL_CLASS).mkdir(parents=True)
        real = REPO / "docs/fern-refusals"
        classes = (real / "classes.tsv").read_text(encoding="utf-8").splitlines()
        row = next(line for line in classes if line.startswith(f"{REFUSAL_CLASS}\t"))
        (registry / "classes.tsv").write_text(f"{classes[0]}\n{row}\n", encoding="utf-8")
        findings = (real / "findings.tsv").read_text(encoding="utf-8").splitlines()[0]
        (registry / "findings.tsv").write_text(f"{findings}\n", encoding="utf-8")
        shutil.copy2(real / REFUSAL_CLASS / "probe.yml", registry / REFUSAL_CLASS / "probe.yml")
        (root / "tools/fern-goldens/decision-gates.tsv").write_text(GATES, encoding="utf-8")
        # The committed references: what the recipe writes at the older pair.
        target = root / "target/release"
        target.mkdir(parents=True)
        (target / "crozier").symlink_to(CROZIER)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        environment = self.environment(root)
        for family in ("corpus", "handwritten", "refusals"):
            generated = subprocess.run(
                [sys.executable, str(root / "tools/fern-goldens/fern-references.py"), "generate", family],
                cwd=root,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, generated.returncode, generated.stdout + generated.stderr)
        shutil.rmtree(root / ".local", ignore_errors=True)

    def add_refused_class(self) -> None:
        """A refusal class whose probe crozier generates from, its record what
        the recipe writes when the stand-in Fern refuses that probe."""
        registry = self.seed / "docs/fern-refusals"
        classes = (registry / "classes.tsv").read_text(encoding="utf-8").splitlines()
        cells = classes[1].split("\t")
        header = classes[0].split("\t")
        cells[header.index("class")] = "lantern-refused"
        cells[header.index("diagnostic")] = "Lantern <…> cannot be lit"
        cells[header.index("fern_stage")], cells[header.index("fern_exit")] = "generate", "1"
        (registry / "classes.tsv").write_text("\n".join([*classes, "\t".join(cells)]) + "\n", encoding="utf-8")
        (registry / "lantern-refused").mkdir()
        (registry / "lantern-refused/probe.yml").write_text(DOCUMENT.format(title="Refused Lanterns"), encoding="utf-8")
        refused = {"generate": [1, "Lantern 'harbour' cannot be lit"]}
        self.stand_in({"rules": {"probe": self.refusal_rule, "Refused Lanterns": refused}})
        generated = subprocess.run(
            [
                sys.executable,
                str(self.seed / "tools/fern-goldens/fern-references.py"),
                "generate",
                "refusals",
                "lantern-refused",
            ],
            cwd=self.seed,
            env=self.environment(self.seed),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, generated.returncode, generated.stderr)
        shutil.rmtree(self.seed / ".local", ignore_errors=True)

    def publish_seed(self, root: Path | None = None) -> None:
        root = root or self.seed
        self.git(root, "add", "-A")
        self.git(root, "commit", "-qm", "seed")
        subprocess.run(["git", "init", "-q", "--bare", str(self.remote)], check=True)
        self.git(root, "push", "-q", str(self.remote), "HEAD:refs/heads/main")

    def clone(self) -> Path:
        """A job's checkout: a fresh clone of the remote's `main`, with the
        release crozier the job would build beside it."""
        self.clones += 1
        root = self.scratch / f"job-{self.clones}"
        subprocess.run(["git", "clone", "-q", str(self.remote), str(root)], check=True)
        (root / "target/release").mkdir(parents=True)
        (root / "target/release/crozier").symlink_to(CROZIER)
        return root

    def environment(self, root: Path, **updates: str) -> dict[str, str]:
        env = {
            **os.environ,
            "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            "CROZIER_FERN_WEEKLY_ROOT": str(root),
            "CROZIER_FERN_GOLDENS_ROOT": str(root),
            "CROZIER_FERN_NO_DOCKER_SHIM": "1",
            "STAND_IN_FERN": str(self.fern),
            "GH_STATE": str(self.gh_state),
            "GH_TOKEN": "stand-in-token",
            "SERVED_DOCUMENTS": json.dumps(getattr(self, "served", {})),
        }
        env.pop("GITHUB_RUN_ID", None)
        env.update(updates)
        return {key: value for key, value in env.items() if value != "<unset>"}

    @staticmethod
    def git(root: Path, *args: str) -> str:
        return subprocess.run(
            ["git", "-C", str(root), *args], check=True, capture_output=True, text=True, encoding="utf-8"
        ).stdout.strip()

    def phase(self, root: Path, *args: str, **env: str) -> subprocess.CompletedProcess[str]:
        summary = self.scratch / "summary.md"
        return subprocess.run(
            [sys.executable, str(root / "tools/fern-goldens/weekly.py"), *args, "--summary", str(summary)],
            cwd=root,
            env=self.environment(root, **env),
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def summary(self) -> str:
        path = self.scratch / "summary.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def run_workflow(self, items: str = "", *, stop_after: str = "", **env: str) -> Journey:
        """The workflow's jobs in order, each in its own checkout, stopping
        where a job's failure stops the workflow: a red phase skips every phase
        after it, as `needs` does."""
        artifacts = self.scratch / f"artifacts-{self.clones}"
        outputs = artifacts / "outputs"
        artifacts.mkdir()
        state = Journey(artifacts)
        planner = self.clone()
        resolved = self.phase(
            planner,
            "resolve",
            "--ref",
            "refs/heads/main",
            "--cli-version",
            CANDIDATE.cli,
            "--generator-version",
            CANDIDATE.generator,
            "--items",
            items,
            "--github-output",
            str(outputs),
            *(() if env.pop("NO_TOKEN", "") else ("--token-present",)),
            **env,
        )
        state.resolve = resolved
        values = (
            dict(line.split("=", 1) for line in outputs.read_text(encoding="utf-8").splitlines())
            if outputs.exists()
            else {}
        )
        if resolved.returncode != 0 or values.get("run") != "true" or stop_after == "resolve":
            return state
        plan = artifacts / "plan.json"
        planned = self.phase(
            planner,
            "plan",
            "--items",
            items,
            "--cli",
            values["cli"],
            "--generator",
            values["generator"],
            "--base",
            self.git(planner, "rev-parse", "HEAD"),
            "--output",
            str(plan),
            **env,
        )
        state.plan = planned
        if planned.returncode != 0:
            return state
        shards = json.loads(plan.read_text(encoding="utf-8"))["shards"]
        for shard in shards:
            job = self.clone()
            result = self.phase(
                job,
                "shard",
                "--plan",
                str(plan),
                "--index",
                str(shard["index"]),
                "--output",
                str(artifacts / f"fern-goldens-shard-{shard['index']}"),
                **env,
            )
            state.shards.append(result)
        if stop_after == "shards":
            return state
        bundle = artifacts / "bundle"
        assembled = self.phase(
            self.clone(), "assemble", "--plan", str(plan), "--shards", str(artifacts), "--output", str(bundle), **env
        )
        state.assemble = assembled
        if assembled.returncode != 0:
            return state
        decider = self.clone()
        applied = self.phase(decider, "apply", "--bundle", str(bundle), **env)
        self.assertEqual(0, applied.returncode, applied.stderr)
        decision = artifacts / "decision"
        decided = self.phase(decider, "decide", "--bundle", str(bundle), "--output", str(decision), **env)
        state.decide = decided
        state.decision = (
            json.loads((decision / "decision.json").read_text(encoding="utf-8"))
            if (decision / "decision.json").exists()
            else None
        )
        if decided.returncode != 0 or values.get("complete") != "true" or stop_after == "decide":
            return state
        state.publish = self.publish(bundle, decision, **env)
        return state

    def publish(self, bundle: Path, decision: Path, **env: str) -> subprocess.CompletedProcess[str]:
        return self.phase(
            self.clone(),
            "publish",
            "--bundle",
            str(bundle),
            "--decision",
            str(decision),
            "--repo",
            "owner/crozier",
            "--checked-on",
            "2026-10-19",
            **env,
        )

    def pulls(self) -> list[dict[str, Any]]:
        """The stood-in GitHub's pull requests, as the JSON gh returns them (so
        `Any`: each field's type is gh's)."""
        return json.loads(self.gh_state.read_text(encoding="utf-8"))["pulls"] if self.gh_state.exists() else []

    def remote_branches(self) -> list[str]:
        listed = self.git(self.remote, "for-each-ref", "--format=%(refname:short)", "refs/heads")
        return sorted(listed.splitlines())

    def remote_file(self, ref: str, path: str) -> str:
        return self.git(self.remote, "show", f"{ref}:{path}")

    def assert_untouched(self) -> None:
        self.assertEqual(["main"], self.remote_branches())
        self.assertEqual([], self.pulls())
        self.assertEqual(1, int(self.git(self.remote, "rev-list", "--count", "main")))

    def test_no_diff_adopts_the_pair_through_one_auto_merged_pull_request(self) -> None:
        """References that differ from the committed ones only where crozier's
        engine finds no difference — provenance, `generatorConfig`, the SDK
        identity headers — plus a byte difference crozier matches, across two
        shards, adopt the pair in one change set Fern and crozier both agree on."""
        timings = self.seed / "tools/fern-goldens/generation-seconds.tsv"
        timings.write_text(
            "family\titem\tseconds\ncorpus\talpha\t4000.0\ncorpus\tbeta\t10.0\nhandwritten\tlantern\t4000.0\n"
            f"refusals\t{REFUSAL_CLASS}\t10.0\n",
            encoding="utf-8",
        )
        self.publish_seed()
        self.stand_in(
            {"rules": {"probe": self.refusal_rule}, "sdk_headers": True, "generator_config": {"stand_in_revision": 2}}
        )
        state = self.run_workflow()
        self.assertEqual(2, len(state.shards), "two 4,000-second items cannot share one shard")
        self.assertEqual("match", state.outcome(), state.ran("decide").stdout + self.summary())
        published = state.ran("publish")
        self.assertEqual(0, published.returncode, published.stderr + self.summary())

        self.assertEqual(["fern-goldens/update", "main"], self.remote_branches())
        self.assertEqual(1, int(self.git(self.remote, "rev-list", "--count", "main")), "nothing is pushed to main")
        (pull,) = self.pulls()
        title = f"test(fern-goldens): regenerate at Fern CLI {CANDIDATE.cli} / fern-python-sdk {CANDIDATE.generator}"
        self.assertEqual((title, "fern-goldens/update", "main"), (pull["title"], pull["head"], pull["base"]))
        self.assertEqual([{"name": "fern-goldens"}], pull["labels"])
        self.assertEqual({"mergeMethod": "SQUASH"}, pull["autoMergeRequest"])
        self.assertIn("**No diff**", pull["body"])

        branch = "fern-goldens/update"
        self.assertEqual(1, int(self.git(self.remote, "rev-list", "--count", f"main..{branch}")))
        changed = self.git(self.remote, "diff", "--name-only", f"main...{branch}").splitlines()
        metadata = json.loads(self.remote_file(branch, "assets/scaffolding/metadata.json"))
        self.assertEqual(CANDIDATE, (metadata["cliVersion"], metadata["generatorVersion"]))
        checks = self.remote_file(branch, "tests/fixtures/fern-pair-checks.tsv").splitlines()
        self.assertEqual(f"{CANDIDATE.cli}\t{CANDIDATE.generator}\t2026-10-19\tmatch", checks[-1])
        for regenerated in (
            "tests/fixtures/alpha/expected/.fern/metadata.json",
            "tests/fixtures/alpha/expected/.crozier-fern-golden.json",
            "tests/fixtures/beta/expected/.crozier-fern-golden.json",
            "docs/openapi-surface/handwritten/lantern/fern-expected/.fern/metadata.json",
            "docs/openapi-surface/handwritten/lantern/evidence.toml",
            f"docs/fern-refusals/{REFUSAL_CLASS}/fern-refusal.txt",
            "tools/fern-goldens/generation-seconds.tsv",
        ):
            self.assertIn(regenerated, changed)
        wrapper = next(
            path for path in changed if path.startswith("tests/fixtures/alpha/") and path.endswith("client_wrapper.py")
        )
        self.assertIn(f'"X-Fern-SDK-Version": "{CANDIDATE.generator}"', self.remote_file(branch, wrapper))
        # Its bytes differ from the committed tree's, which published no SDK name
        # or version; crozier's output still matches it.
        self.assertNotIn("X-Fern-SDK-Version", self.remote_file("main", wrapper))
        self.assertIn(
            f"fern_cli_version: {CANDIDATE.cli}",
            self.remote_file(branch, f"docs/fern-refusals/{REFUSAL_CLASS}/fern-refusal.txt"),
        )
        measured = self.remote_file(branch, "tools/fern-goldens/generation-seconds.tsv")
        self.assertRegex(measured, r"(?m)^corpus\talpha\t\d+\.\d$")
        self.assertNotIn("4000.0", measured)

        # The pair's drift check holds over that change set, as crozier's own does.
        merged = self.scratch / "merged"
        subprocess.run(["git", "clone", "-q", "-b", branch, str(self.remote), str(merged)], check=True)
        drift = subprocess.run(
            [sys.executable, str(merged / "tools/fern-goldens/certified_pair.py"), "check", str(merged)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual((0, ""), (drift.returncode, drift.stderr))

        # Once it merges, the pair is the certified one: the next run checks nothing.
        self.git(self.remote, "update-ref", "refs/heads/main", f"refs/heads/{branch}")
        again = self.run_workflow()
        self.assertEqual(0, again.ran("resolve").returncode)
        self.assertIsNone(again.plan)
        self.assertIn("is the certified pair already", again.ran("resolve").stdout)

    def test_a_small_engine_difference_opens_a_diff_pull_request_naming_the_item(self) -> None:
        self.publish_seed()
        self.stand_in(
            {
                "rules": {"probe": self.refusal_rule},
                "tweaks": {
                    "Alpha Lanterns": [
                        ["types/lantern.py", "lit:", "lit_state:"],
                        ["core/force_multipart.py", None, None],
                    ]
                },
            }
        )
        state = self.run_workflow()
        self.assertEqual("diff", state.outcome())
        self.assertEqual(0, state.ran("publish").returncode, state.ran("publish").stderr + self.summary())
        (pull,) = self.pulls()
        self.assertIsNone(pull["autoMergeRequest"], "a diff is never auto-merged")
        self.assertEqual("fern-goldens/update", pull["head"])
        self.assertEqual([{"name": "fern-goldens"}], pull["labels"])
        self.assertIn(CANDIDATE.cli, pull["title"])
        self.assertIn(CANDIDATE.generator, pull["title"])
        failing = pull["body"].split("## Failing items", 1)[1].split("## Inventory", 1)[0]
        self.assertIn("### corpus (1)", failing)
        self.assertIn("- `alpha`", failing)
        self.assertIn("mismatched", failing, "the engine's own report is quoted")
        self.assertIn("types/lantern.py", failing)
        self.assertNotIn("handwritten", failing)
        branch = "fern-goldens/update"
        metadata = json.loads(self.remote_file(branch, "assets/scaffolding/metadata.json"))
        self.assertEqual(CANDIDATE, (metadata["cliVersion"], metadata["generatorVersion"]))
        lantern = next(
            path
            for path in self.git(self.remote, "ls-tree", "-r", "--name-only", branch).splitlines()
            if path.startswith("tests/fixtures/alpha/expected/") and path.endswith("types/lantern.py")
        )
        self.assertIn("lit_state:", self.remote_file(branch, lantern))
        # A file Fern no longer writes is deleted from the tree the pull request carries.
        removed = lantern.replace("types/lantern.py", "core/force_multipart.py")
        self.assertTrue(self.remote_file("main", removed))
        tree = self.git(self.remote, "ls-tree", "-r", "--name-only", branch).splitlines()
        self.assertNotIn(removed, tree)
        self.assertIn("core/force_multipart.py", failing, "crozier still emits it, which the engine reports")
        self.assertEqual(
            "fern_cli_version\tfern_python_sdk_version\tchecked_on\toutcome",
            self.remote_file(branch, "tests/fixtures/fern-pair-checks.tsv"),
            "a diff records no checked pair",
        )

    def test_a_refusal_class_crozier_does_not_refuse_is_a_diff(self) -> None:
        """A regenerated refusal record says Fern refuses a document crozier
        generates from, so crozier's refusal path rejects it."""
        self.add_refused_class()
        self.publish_seed()
        state = self.run_workflow()
        self.assertEqual("diff", state.outcome(), self.summary())
        (pull,) = self.pulls()
        failing = pull["body"].split("## Failing items", 1)[1]
        self.assertIn("### refusals (1)", failing)
        self.assertIn("- `lantern-refused`", failing)
        self.assertNotIn(REFUSAL_CLASS, failing)
        record = self.remote_file("fern-goldens/update", "docs/fern-refusals/lantern-refused/fern-refusal.txt")
        self.assertIn("diagnostic: Lantern 'harbour' cannot be lit", record)

    def test_an_unfetchable_specification_is_named_and_the_rest_still_regenerate(self) -> None:
        self.publish_seed()
        self.stand_in({"rules": {"probe": self.refusal_rule}, "generator_config": {"stand_in_revision": 2}})
        state = self.run_workflow(FAIL_FETCH="beta")
        self.assertEqual([0], [shard.returncode for shard in state.shards], state.shards[0].stderr)
        self.assertEqual(0, state.ran("assemble").returncode, state.ran("assemble").stderr)
        self.assertEqual("diff", state.outcome())
        self.assertEqual({}, state.failing())
        self.assertEqual(["beta"], state.unfetchable())
        self.assertIn("not regenerated: corpus `beta`", self.summary())
        (pull,) = self.pulls()
        self.assertIsNone(pull["autoMergeRequest"])
        section = pull["body"].split("## Not regenerated: upstream specification unavailable", 1)[1]
        self.assertIn("corpus `beta`: spec fetch failed", section)
        changed = self.git(self.remote, "diff", "--name-only", "main...fern-goldens/update").splitlines()
        self.assertIn("tests/fixtures/alpha/expected/.fern/metadata.json", changed)
        self.assertFalse(any(path.startswith("tests/fixtures/beta/") for path in changed))

    def test_a_subset_run_publishes_nothing_and_the_next_full_run_checks_everything(self) -> None:
        self.publish_seed()
        self.stand_in(
            {
                "rules": {"probe": self.refusal_rule},
                "tweaks": {"Harbour Lanterns": [["types/lantern.py", "lit:", "lamp:"]]},
            }
        )
        subset = self.run_workflow("handwritten,corpus:alpha", NO_TOKEN="1")
        self.assertEqual(0, subset.ran("resolve").returncode, subset.ran("resolve").stderr)
        plan = json.loads((subset.artifacts / "plan.json").read_text(encoding="utf-8"))
        self.assertFalse(plan["complete"])
        planned = [(entry["family"], entry["item"]) for shard in plan["shards"] for entry in shard["items"]]
        self.assertEqual([("corpus", "alpha"), ("handwritten", "lantern")], planned)
        self.assertEqual("diff", subset.outcome())
        self.assertIn("lantern", self.summary())
        self.assertIsNone(subset.publish)
        refused = self.publish(subset.artifacts / "bundle", subset.artifacts / "decision")
        self.assertEqual(1, refused.returncode)
        self.assertIn("a diagnostic subset run never publishes", refused.stderr)
        self.assert_untouched()

        self.stand_in({"rules": {"probe": self.refusal_rule}})
        full = self.run_workflow()
        plan = json.loads((full.artifacts / "plan.json").read_text(encoding="utf-8"))
        self.assertTrue(plan["complete"])
        planned = {(entry["family"], entry["item"]) for shard in plan["shards"] for entry in shard["items"]}
        self.assertEqual(
            {("corpus", "alpha"), ("corpus", "beta"), ("handwritten", "lantern"), ("refusals", REFUSAL_CLASS)}, planned
        )
        self.assertEqual("match", full.outcome())
        self.assertEqual(0, full.ran("publish").returncode, full.ran("publish").stderr)

    def test_a_checked_or_certified_pair_ends_green_and_changes_nothing(self) -> None:
        checks = self.seed / "tests/fixtures/fern-pair-checks.tsv"
        checks.write_text(
            checks.read_text(encoding="utf-8") + f"{CANDIDATE.cli}\t{CANDIDATE.generator}\t2026-10-12\tmatch\n",
            encoding="utf-8",
        )
        self.publish_seed()
        state = self.run_workflow()
        self.assertEqual(0, state.ran("resolve").returncode, state.ran("resolve").stderr)
        self.assertIn("was checked on 2026-10-12", state.ran("resolve").stdout)
        self.assertIn("was checked on 2026-10-12", self.summary())
        self.assertIsNone(state.plan)
        self.assert_untouched()

    def test_a_failed_item_generation_is_red_before_anything_is_published(self) -> None:
        self.publish_seed()
        self.stand_in(
            {"rules": {"probe": self.refusal_rule, "Harbour Lanterns": {"generate": [2, "container exited 137"]}}}
        )
        state = self.run_workflow()
        self.assertEqual([1], [shard.returncode for shard in state.shards])
        self.assertEqual(1, state.ran("assemble").returncode)
        self.assertIn("handwritten lantern: generation failed", state.ran("assemble").stderr)
        self.assertIn("**failure**: handwritten lantern: generation failed", self.summary())
        self.assertIsNone(state.decide)
        self.assert_untouched()

    def test_a_missing_or_incomplete_shard_is_red_before_anything_is_published(self) -> None:
        self.publish_seed()
        state = self.run_workflow(stop_after="shards")
        artifacts = state.artifacts
        plan = artifacts / "plan.json"
        result = artifacts / "fern-goldens-shard-0" / "result.json"
        record = json.loads(result.read_text(encoding="utf-8"))
        record["items"] = record["items"][1:]
        result.write_text(json.dumps(record), encoding="utf-8")
        incomplete = self.phase(
            self.clone(), "assemble", "--plan", str(plan), "--shards", str(artifacts), "--output", str(artifacts / "b1")
        )
        self.assertEqual(1, incomplete.returncode)
        self.assertIn("shard 0 does not account for its planned items: missing corpus alpha", incomplete.stderr)
        shutil.rmtree(artifacts / "fern-goldens-shard-0")
        missing = self.phase(
            self.clone(), "assemble", "--plan", str(plan), "--shards", str(artifacts), "--output", str(artifacts / "b2")
        )
        self.assertEqual(1, missing.returncode)
        self.assertIn("shard 0 uploaded no result", missing.stderr)
        self.assertIn("shard 0 uploaded no result", self.summary())
        # A failed assembly can neither be decided nor published.
        refused = self.phase(self.clone(), "apply", "--bundle", str(artifacts / "b2"))
        self.assertEqual(1, refused.returncode)
        self.assertIn("is a failed assembly", refused.stderr)
        self.assert_untouched()

    def test_a_comparison_that_cannot_run_is_red_never_a_pass(self) -> None:
        gates = self.seed / "tools/fern-goldens/decision-gates.tsv"
        gates.write_text(
            gates.read_text(encoding="utf-8").replace(
                "crozier compare {root}/tests", "crozier compare --no-such-flag {root}/tests"
            ),
            encoding="utf-8",
        )
        self.publish_seed()
        state = self.run_workflow()
        self.assertEqual(1, state.ran("decide").returncode)
        self.assertEqual("failure", state.outcome())
        self.assertIn("could not run (exit 2)", state.ran("decide").stderr)
        self.assertIn("**cannot run**", self.summary())
        self.assertIsNone(state.publish)
        self.assert_untouched()

    def test_a_missing_token_is_red_before_any_work_or_remote_step(self) -> None:
        self.publish_seed()
        state = self.run_workflow(NO_TOKEN="1")
        self.assertEqual(1, state.ran("resolve").returncode)
        self.assertIn("RELEASE_PLZ_TOKEN is not set", state.ran("resolve").stderr)
        self.assertIsNone(state.plan)
        decided = self.run_workflow(stop_after="decide")
        artifacts = decided.artifacts
        unauthenticated = self.publish(artifacts / "bundle", artifacts / "decision", GH_TOKEN="<unset>")
        self.assertEqual(1, unauthenticated.returncode)
        self.assertIn("GH_TOKEN (the workflow's RELEASE_PLZ_TOKEN) is not set", unauthenticated.stderr)
        self.assertIn("Steps completed before it:\n- none", self.summary())
        self.assert_untouched()

    def test_a_refused_auto_merge_is_red_and_the_next_run_finishes_it(self) -> None:
        self.publish_seed()
        state = self.run_workflow(stop_after="decide")
        bundle, decision = state.artifacts / "bundle", state.artifacts / "decision"
        refused = self.publish(bundle, decision, GH_FAIL="pr merge")
        self.assertEqual(1, refused.returncode)
        summary = self.summary().split("## Fern goldens: publication failed", 1)[1]
        self.assertIn("enabling auto-merge on #1 failed", summary)
        self.assertIn("- push fern-goldens/update: pushed", summary)
        self.assertIn("- pull request: opened #1", summary)
        self.assertNotIn("auto-merge: enabled", summary)
        self.assertIsNone(self.pulls()[0]["autoMergeRequest"])

        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("already on the remote", finished.stdout)
        self.assertIn("pull request: updated #1", finished.stdout)
        (pull,) = self.pulls()
        self.assertEqual({"mergeMethod": "SQUASH"}, pull["autoMergeRequest"])

    def test_a_lost_response_is_red_and_the_next_run_reuses_what_the_remote_applied(self) -> None:
        self.publish_seed()
        state = self.run_workflow(stop_after="decide")
        bundle, decision = state.artifacts / "bundle", state.artifacts / "decision"
        lost = self.publish(bundle, decision, GH_LOSE="pr create")
        self.assertEqual(1, lost.returncode)
        self.assertIn("opening the pull request failed", self.summary())
        self.assertEqual(1, len(self.pulls()), "the remote applied the create")

        lost_merge = self.publish(bundle, decision, GH_LOSE="pr merge")
        self.assertEqual(1, lost_merge.returncode)
        self.assertIn("pull request: updated #1", lost_merge.stdout)

        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("auto-merge: already enabled", finished.stdout)
        (pull,) = self.pulls()
        self.assertEqual({"mergeMethod": "SQUASH"}, pull["autoMergeRequest"])
        self.assertEqual(["fern-goldens/update", "main"], self.remote_branches())
        merges = [
            call
            for call in json.loads(self.gh_state.read_text(encoding="utf-8"))["calls"]
            if call[:2] == ["pr", "merge"]
        ]
        self.assertEqual(1, len(merges), "an enabled auto-merge is not requested again")

    def test_a_rejected_push_or_label_is_red_and_says_what_completed(self) -> None:
        self.publish_seed()
        state = self.run_workflow(stop_after="decide")
        bundle, decision = state.artifacts / "bundle", state.artifacts / "decision"
        hook = self.remote / "hooks" / "pre-receive"
        write_executable(hook, "#!/bin/sh\necho 'protected by the stand-in remote' >&2\nexit 1\n")
        rejected = self.publish(bundle, decision)
        self.assertEqual(1, rejected.returncode)
        summary = self.summary().split("## Fern goldens: publication failed", 1)[1]
        self.assertIn("pushing fern-goldens/update failed", summary)
        self.assertIn("protected by the stand-in remote", summary)
        self.assertIn("- commit:", summary)
        self.assertNotIn("- push", summary)
        self.assert_untouched()
        hook.unlink()

        unlabelled = self.publish(bundle, decision, GH_FAIL="label create")
        self.assertEqual(1, unlabelled.returncode)
        self.assertIn("could not create the fern-goldens label", unlabelled.stderr)
        self.assertEqual([], self.pulls())
        self.assertEqual(["fern-goldens/update", "main"], self.remote_branches())
        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("label fern-goldens: created", finished.stdout)
        self.assertIn("already on the remote", finished.stdout)
        self.assertEqual(1, len(self.pulls()))

    def test_family_gates_run_a_shared_command_once_and_attribute_its_report(self) -> None:
        """A gate that decides whole families runs once however many rows name
        it; a rejection lists each item its report names, and a report naming
        none is listed whole under its family."""
        compare_all = "{root}/target/release/crozier compare {root}/tests/fixtures/alpha/crozier.yml"
        refuse = "{root}/target/release/crozier --no-config generate --spec {root}/docs/fern-refusals/lantern-refused/probe.yml --output {scratch}/out"
        (self.seed / "tools/fern-goldens/decision-gates.tsv").write_text(
            "family\tscope\tverdict\tcommand\n"
            f"corpus\tfamily\texit:0/3\t{compare_all}\n"
            f"handwritten\tfamily\texit:0/3\t{compare_all}\n"
            f"refusals\tfamily\texit:1/0\t{refuse}\n",
            encoding="utf-8",
        )
        self.add_refused_class()
        self.publish_seed()
        self.stand_in(
            {
                "rules": {
                    "probe": self.refusal_rule,
                    "Refused Lanterns": {"generate": [1, "Lantern 'harbour' cannot be lit"]},
                },
                "tweaks": {"Alpha Lanterns": [["types/lantern.py", "lit:", "lit_state:"]]},
            }
        )
        state = self.run_workflow()
        self.assertEqual("diff", state.outcome(), self.summary())
        self.assertEqual(1, state.gate_commands().count(compare_all), "the shared command ran once")
        self.assertEqual({"corpus": ["alpha"], "refusals": ["(the gate's report names no item)"]}, state.failing())
        (pull,) = self.pulls()
        failing = pull["body"].split("## Failing items", 1)[1].split("## Inventory", 1)[0]
        self.assertIn("tests/fixtures/alpha/crozier.yml", failing)
        self.assertIn("### refusals (1)", failing)
        self.assertIn("generated", failing, "a report naming no item is quoted whole")

    def test_a_concurrent_push_to_the_branch_fails_the_lease_and_the_next_run_reconciles(self) -> None:
        self.publish_seed()
        first = self.run_workflow()
        self.assertEqual(0, first.ran("publish").returncode, first.ran("publish").stderr)
        published = self.git(self.remote, "rev-parse", "refs/heads/fern-goldens/update")
        self.stand_in({"rules": {"probe": self.refusal_rule}, "generator_config": {"stand_in_revision": 3}})
        state = self.run_workflow(stop_after="decide")
        # Another writer lands on the branch between the run's read and its push.
        real_git = shutil.which("git")
        assert real_git is not None
        concurrent = self.git(self.remote, "commit-tree", f"{published}^{{tree}}", "-p", published, "-m", "concurrent")
        racing = self.scratch / "racing-bin"
        write_executable(
            racing / "git",
            f"""#!/bin/sh
            if [ "$3" = push ]; then
              {real_git} --git-dir={self.remote} update-ref refs/heads/fern-goldens/update {concurrent}
            fi
            exec {real_git} "$@"
            """,
        )
        bundle, decision = state.artifacts / "bundle", state.artifacts / "decision"
        raced = self.publish(bundle, decision, PATH=f"{racing}{os.pathsep}{self.bin}{os.pathsep}{os.environ['PATH']}")
        self.assertEqual(1, raced.returncode)
        self.assertIn("pushing fern-goldens/update failed", raced.stderr)
        self.assertIn("stale info", raced.stderr)
        self.assertEqual(concurrent, self.git(self.remote, "rev-parse", "refs/heads/fern-goldens/update"))

        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("push fern-goldens/update: pushed", finished.stdout)
        self.assertIn("pull request: updated #1", finished.stdout)
        self.assertEqual(1, len(self.pulls()))

    def test_a_refused_or_lost_pull_request_update_is_red_and_the_next_run_updates_it(self) -> None:
        self.publish_seed()
        first = self.run_workflow()
        self.assertEqual(0, first.ran("publish").returncode, first.ran("publish").stderr)
        self.stand_in({"rules": {"probe": self.refusal_rule}, "generator_config": {"stand_in_revision": 3}})
        state = self.run_workflow(stop_after="decide")
        bundle, decision = state.artifacts / "bundle", state.artifacts / "decision"
        refused = self.publish(bundle, decision, GH_FAIL="pr edit")
        self.assertEqual(1, refused.returncode)
        summary = self.summary().rsplit("## Fern goldens: publication failed", 1)[1]
        self.assertIn("updating pull request #1 failed", summary)
        self.assertIn("- push fern-goldens/update: pushed", summary)
        self.assertIn("- label fern-goldens: present", summary)
        lost = self.publish(bundle, decision, GH_LOSE="pr edit")
        self.assertEqual(1, lost.returncode)
        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("pull request: updated #1", finished.stdout)
        self.assertIn("auto-merge: already enabled", finished.stdout)
        self.assertEqual(1, len(self.pulls()))

    def test_an_exact_known_upstream_failure_is_carried_through_to_an_adopting_pull_request(self) -> None:
        """A corpus row whose generation reproduces its registered upstream Fern
        failure exactly, at the candidate version, is no failure: the run
        decides and publishes the rest, and the row keeps no golden."""
        manifest = json.loads(KNOWN_FAILURE.read_text(encoding="utf-8"))
        manifest.update(
            {
                "generator_version": CANDIDATE.generator,
                "corpus_spec_name": "gamma",
                "corpus_spec_ref": "1",
                "corpus_spec_url": "https://example.test/gamma/openapi.yaml",
            }
        )
        fixtures = self.seed / "tests/fixtures"
        (fixtures / "gamma").mkdir()
        (fixtures / "gamma/known-fern-failure.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        corpus = fixtures / "CORPUS.md"
        corpus.write_text(
            corpus.read_text(encoding="utf-8")
            + "| 2 | `gamma` | test | https://example.test/gamma/openapi.yaml | `1` | MIT | link-ok | gamma |\n",
            encoding="utf-8",
        )
        self.served["example.test/gamma/"] = DOCUMENT.format(title="Gamma Lanterns")
        compare_corpus = (
            "{root}/target/release/crozier compare {root}/tests/fixtures/alpha/crozier.yml "
            "{root}/tests/fixtures/beta/crozier.yml"
        )
        gates = self.seed / "tools/fern-goldens/decision-gates.tsv"
        gates.write_text(
            "\n".join(
                f"corpus\tfamily\texit:0/3\t{compare_corpus}" if line.startswith("corpus\t") else line
                for line in gates.read_text(encoding="utf-8").splitlines()
            )
            + "\n",
            encoding="utf-8",
        )
        self.publish_seed()
        fingerprint = manifest["fingerprint"]
        blocks = [
            f"fern/output/{entry['path']}:{entry['line']}:{entry['column']}: {entry['message']}\n"
            f"{entry['line']} | {entry['source']}"
            for entry in fingerprint["diagnostics"]
        ]
        payload = "\n\n".join([*blocks, fingerprint["ruff_summary"]]) + "\n"
        failure = f"Failed to run command: {fingerprint['failed_command']}\n{payload.encode('utf-8')!r}"
        self.stand_in(
            {
                "rules": {
                    "probe": self.refusal_rule,
                    "Gamma Lanterns": {"generate": [manifest["exit_code"], failure], "raw": True},
                }
            }
        )
        state = self.run_workflow()
        self.assertEqual([0], [shard.returncode for shard in state.shards], state.shards[0].stderr)
        bundle = json.loads((state.artifacts / "bundle/bundle.json").read_text(encoding="utf-8"))
        statuses = {entry["item"]: entry["status"] for entry in bundle["items"]}
        self.assertEqual("known-upstream-failure", statuses["gamma"])
        self.assertIn("corpus `gamma`: known-upstream-failure", self.summary())
        self.assertEqual("match", state.outcome(), self.summary())
        self.assertEqual(0, state.ran("publish").returncode, state.ran("publish").stderr)
        (pull,) = self.pulls()
        self.assertEqual({"mergeMethod": "SQUASH"}, pull["autoMergeRequest"])
        self.assertIn("| corpus | 3 |", pull["body"])
        tree = self.git(self.remote, "ls-tree", "-r", "--name-only", "fern-goldens/update").splitlines()
        self.assertFalse(any(path.startswith("tests/fixtures/gamma/expected") for path in tree))

    def test_a_diff_after_an_adopting_run_turns_auto_merge_off(self) -> None:
        self.publish_seed()
        matched = self.run_workflow()
        self.assertEqual({"mergeMethod": "SQUASH"}, self.pulls()[0]["autoMergeRequest"], matched.ran("publish").stderr)
        self.stand_in(
            {
                "rules": {"probe": self.refusal_rule},
                "tweaks": {"Alpha Lanterns": [["types/lantern.py", "lit:", "lit_state:"]]},
            }
        )
        # The remote turns auto-merge off, but the response is lost: red, and the
        # next run finds it off and leaves it so.
        differing = self.run_workflow(GH_LOSE="pr merge")
        self.assertEqual(1, differing.ran("publish").returncode)
        self.assertIn("turning off auto-merge on #1 failed", self.summary())
        bundle, decision = differing.artifacts / "bundle", differing.artifacts / "decision"
        finished = self.publish(bundle, decision)
        self.assertEqual(0, finished.returncode, finished.stderr)
        self.assertIn("auto-merge: off: a diff waits for a person", finished.stdout)
        (pull,) = self.pulls()
        self.assertIsNone(pull["autoMergeRequest"])
        self.assertIn("**Diff**", pull["body"])


class ReporterContractTests(unittest.TestCase):
    """The decision reads `report_fixture_diffs`' own report (`just
    fixtures-diff`); these are the lines it reads, as that reporter prints them."""

    def test_the_reporter_still_prints_what_the_decision_reads(self) -> None:
        source = (REPO / "crates/crozier-e2e/tests/e2e.rs").read_text(encoding="utf-8")
        for printed in (
            "comparison generation failure(s) across the reported corpora.",
            "comparison processing failure(s) across the reported corpora.",
            " [REGRESSION — not in `unmatched`]",
            "Comparison setup failed: ",
            'println!("\\n--- {rel}{tag} ---");',
        ):
            self.assertIn(printed, source)
        self.assertIn("differing file(s) across the reported corpora", source)


if __name__ == "__main__":
    unittest.main()
