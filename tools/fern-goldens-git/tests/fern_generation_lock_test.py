"""Issue #986: every crozier entry point that starts Fern serializes its Fern run
on the host's Fern generation lock itself, and one started inside another's hold
shares it.

Each case runs the REAL entry point — a `justfile` recipe through the real
`just`, or the tool itself — from a scratch checkout holding the real scripts,
with only `fern` doubled: the double does no generation work and appends when
each of its runs starts and ends to an event log. (Two recipes reach Fern below
a build tool, whose double stands in for that tool's compile and then runs the
`fern` double, as the real one would run Fern.) Each case is run twice:

* **waits** — this test holds the lock as an unrelated process would, starts the
  entry point, releases the lock once the entry point reports waiting for it (or
  its Fern starts, which is the failure), and asserts from the event log that
  every Fern run started after the release;
* **shares** — this test holds the lock as an entry point does and starts the
  entry point inside that hold, as a nested one is started, and asserts it runs
  Fern to the end without waiting: taking the lock a second time would deadlock.

The bound on each run only guards against a hang.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from collections.abc import Callable, Generator
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
LOCK_SCRIPT = REPO / "tools" / "fern-goldens" / "fern_generation_lock.py"
# The certified pair, read from its one declaration rather than restated.
PAIR = json.loads((REPO / "assets" / "scaffolding" / "metadata.json").read_text(encoding="utf-8"))
CLI, GENERATOR = PAIR["cliVersion"], PAIR["generatorVersion"]
# Only guards against a hang: a healthy run finishes in a few seconds.
HANG_GUARD_SECONDS = 180
WAITING = "waiting for the host Fern generation lock"


def load_lock():
    spec = importlib.util.spec_from_file_location("fern_generation_lock_under_test", LOCK_SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LOCK = load_lock()

# The scripts every scratch checkout holds, copied from this tree.
MIRRORED = (
    "justfile",
    "scripts/lib.sh",
    "scripts/census-python.sh",
    "assets/scaffolding/metadata.json",
    "tools/fern-goldens/fern_generation_lock.py",
    "tools/fern-goldens/fern-goldens",
    "tools/fern-goldens/fern-references.py",
    "tools/fern-goldens/weekly.py",
    "tools/fern-goldens/generate-fern-fixture.sh",
    "tools/fern-goldens/fern-overlay-goldens.sh",
    "tools/fern-goldens/generate-corpus-fixtures.sh",
    "tools/fern-goldens/golden_overlay.py",
    "tools/fern-goldens/certified_pair.py",
    "tools/fern-goldens/certified_tree.py",
    "tools/fern-refusals/fern-refusals.py",
    "tools/fern-refusals/sdk_evaluation.py",
    "tools/fern-refusals/sdk_evaluation_runtime.py",
    "docs/fern-refusals/unsettled-contract.json",
    "tools/corpus/corpus-lib.sh",
    "tools/corpus/corpus_remote_ref_pins.py",
    "tools/corpus/corpus_sources.py",
    "tools/corpus/fetch-corpus.sh",
    "tests/fixtures/corpus-aliases.tsv",
    "tests/fixtures/corpus-remote-ref-pins.tsv",
    "tools/surface-census/openapi-surface-census.py",
    "tools/surface-census/witness-search-region-keys.py",
    "tools/surface-census/output-insensitive.py",
    "tools/surface-census/output-insensitive-remeasure.py",
    "tools/witness-search/witness_screen.py",
    "tools/witness-search/witness-search-github.py",
    "tools/witness-search/witness-search-github-index.py",
    "tools/witness-search/witness-search-redo.py",
    "tools/witness-search/rate_limit_guard.py",
    "docs/corpus-licensing.md",
)

# The Fern double: no generation work, one event line as each run starts and ends.
FERN_DOUBLE = """\
import json, os, sys, time

def note(event):
    with open(os.environ["CROZIER_FERN_LOCK_EVENTS"], "a", encoding="utf-8") as events:
        events.write(json.dumps({"event": event, "pid": os.getpid(), "argv": sys.argv[1:]}) + "\\n")

note("fern-start")
# Long enough that a run started beside a hold would visibly overlap it.
time.sleep(0.3)
note("fern-end")
"""

# A build tool's double: the compile it stands for is no part of the lock's
# contract, and what the real one runs next is Fern, so it runs the `fern` double.
NX_DOUBLE = """\
import subprocess, sys
# `nx run crozier-e2e:fern-probe-refusal` builds the e2e binary, whose ignored
# test runs `fern check` and then `fern generate`.
for stage in (["check"], ["generate", "--group", "python-sdk", "--local"]):
    subprocess.run(["fern", *stage], check=False)
"""

CARGO_DOUBLE = """\
import sys
# `cargo build --release --locked --bin crozier`: the release binary is already in place.
"""

# A presence the entry point checks but, with Fern doubled, never runs.
ABSENT = """\
import os, sys
with open(os.environ["CROZIER_FERN_LOCK_EVENTS"], "a", encoding="utf-8") as events:
    events.write('{"event": "unexpected", "argv": ' + repr(sys.argv).replace("'", '"') + '}\\n')
sys.exit(97)
"""

# The witness candidate's pinned commit on the loopback raw route.
COMMIT = "c" * 40
DOCUMENT = "openapi: 3.0.3\ninfo: {title: lock probe, version: '1'}\npaths: {}\n"


def write_executable(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"#!{sys.executable}\n" + body, encoding="utf-8", newline="\n")
    path.chmod(0o755)


class RawServer(ThreadingHTTPServer):
    daemon_threads = True


class Raw(BaseHTTPRequestHandler):
    """raw.githubusercontent.com's exact-commit route for the one witness candidate."""

    def log_message(self, format: str, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        body = {
            f"/acme/shop/{COMMIT}/openapi.yaml": DOCUMENT.encode(),
            f"/acme/shop/{COMMIT}/LICENSE": b"MIT License\n\nCopyright (c) acme\n",
        }.get(self.path)
        self.send_response(200 if body is not None else 404)
        self.end_headers()
        self.wfile.write(body or b"")


@dataclass(frozen=True)
class Case:
    """One Fern-running entry point: how a scratch checkout is prepared for it,
    returning the command that starts it there."""

    name: str
    prepare: Callable[[Path], list[str]]
    needs_just: bool = False


def corpus_row(root: Path, decision: str = "committed") -> None:
    """One CORPUS.md row, `alpha`, whose source is committed beside its fixture."""
    fixtures = root / "tests" / "fixtures"
    (fixtures / "alpha").mkdir(parents=True, exist_ok=True)
    (fixtures / "alpha" / "openapi.yml").write_text(DOCUMENT, encoding="utf-8")
    (fixtures / "CORPUS.md").write_text(
        "# Corpus\n\n"
        "| # | name | method | source | pinned ref | license | decision | shapes |\n"
        "|---:|---|---|---|---|---|---|---|\n"
        f"| 1 | `alpha` | test | https://example.test/alpha/openapi.yml | `1` | MIT | {decision} | alpha |\n",
        encoding="utf-8",
    )
    source = fixtures / "corpus-sources" / "alpha" / "openapi.yml"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(DOCUMENT, encoding="utf-8")
    digest = hashlib.sha256(DOCUMENT.encode()).hexdigest()
    (fixtures / "corpus-sources.tsv").write_text(
        "# corpus_name\tpath\tsource_url\tsha256\n"
        f"alpha\ttests/fixtures/corpus-sources/alpha/openapi.yml\thttps://example.test/alpha/openapi.yml\t{digest}\n",
        encoding="utf-8",
    )


def authored_probe(root: Path) -> None:
    case = root / "docs" / "openapi-surface" / "authored-probes" / "lock-probe"
    case.mkdir(parents=True)
    (case / "openapi.yml").write_text(DOCUMENT, encoding="utf-8")


def just(root: Path, *recipe: str) -> list[str]:
    return ["just", "--justfile", str(root / "justfile"), "--working-directory", str(root), *recipe]


def prepare_generate_fern_fixture(root: Path) -> list[str]:
    corpus_row(root)
    script = root / "tools" / "fern-goldens" / "generate-fern-fixture.sh"
    return [str(script), "alpha", GENERATOR, str(root / "tests" / "fixtures" / "alpha" / "openapi.yml")]


def prepare_overlay(root: Path) -> list[str]:
    corpus_row(root)
    for fixture in ("eos.local", "alpha"):
        expected = root / "tests" / "fixtures" / fixture / "expected"
        expected.mkdir(parents=True)
        (expected / ".crozier-fern-golden.json").write_text(
            json.dumps({"fern_python_sdk_version": GENERATOR}), encoding="utf-8"
        )
    return [str(root / "tools" / "fern-goldens" / "fern-overlay-goldens.sh"), "--enum-type", "literals", "alpha"]


def prepare_corpus_fixtures(root: Path) -> list[str]:
    corpus_row(root)
    return [str(root / "tools" / "fern-goldens" / "generate-corpus-fixtures.sh"), "--only", "alpha"]


def prepare_fern_goldens(command: str) -> Callable[[Path], list[str]]:
    def prepare(root: Path) -> list[str]:
        corpus_row(root, decision="link-ok")
        return [
            str(root / "tools" / "fern-goldens" / "fern-goldens"),
            command,
            "--version",
            GENERATOR,
            "--fixture",
            "alpha",
        ]

    return prepare


def prepare_fern_references(root: Path) -> list[str]:
    authored_probe(root)
    return [sys.executable, str(root / "tools" / "fern-goldens" / "fern-references.py"), "generate", "authored-probes"]


REFUSAL_CLASS = "request-property-name-collision"


def refusal_registry(root: Path) -> Path:
    """The registry `fern-refusals.py` reads, holding one class and no finding."""
    registry = root / "docs" / "fern-refusals"
    real = REPO / "docs" / "fern-refusals"
    (registry / REFUSAL_CLASS).mkdir(parents=True)
    shutil.copy2(real / REFUSAL_CLASS / "probe.yml", registry / REFUSAL_CLASS / "probe.yml")
    for table, keep in (("classes.tsv", REFUSAL_CLASS), ("findings.tsv", None)):
        lines = (real / table).read_text(encoding="utf-8").splitlines(keepends=True)
        (registry / table).write_text(
            lines[0] + "".join(line for line in lines[1:] if keep and line.split("\t")[0] == keep), encoding="utf-8"
        )
    (root / "docs" / "openapi-surface" / "fern-refusals").mkdir(parents=True, exist_ok=True)
    return registry


def prepare_fern_refusals(root: Path) -> list[str]:
    refusal_registry(root)
    script = root / "tools" / "fern-refusals" / "fern-refusals.py"
    return [sys.executable, str(script), "probe", REFUSAL_CLASS, "--jobs", "1"]


def prepare_refusal_population(root: Path) -> list[str]:
    """One refused document `measure` takes Fern's verdict on afresh: a screen
    filed it refused, and its crozier verdict is already on record, so of the two
    tools `measure` runs only Fern does."""
    import gzip

    refusal_registry(root)
    surface = root / "docs" / "openapi-surface"
    evidence = surface / "fern-refusals"
    (evidence / "dropped-sources.tsv").write_text(
        "name\tcorpus_line\tsource\tlocator\trevision\tsha256\tevidence\treason\n", encoding="utf-8"
    )
    (root / "tests" / "fixtures").mkdir(parents=True, exist_ok=True)
    (root / "tests" / "fixtures" / "CORPUS.md").write_text("", encoding="utf-8")
    for source in ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees"):
        (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
        with gzip.open(
            surface / "golden-reach-witnesses" / source / "enumeration.tsv.gz", "wt", encoding="utf-8"
        ) as handle:
            handle.write("walk\tdocument\trevision\tsha256\n")
    for source in ("github-code-search", "sourcegraph"):
        (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
        (surface / "golden-reach-witnesses" / source / "candidates.jsonl").write_text("", encoding="utf-8")
    documents = root / "documents"
    documents.mkdir()
    (documents / "refused.yml").write_text(DOCUMENT, encoding="utf-8")
    digest = hashlib.sha256(DOCUMENT.encode()).hexdigest()
    (surface / "scratch").mkdir()
    record = {
        "fern": "failed: `fern check` refused it",
        "source": "scratch",
        "repository": "scratch/apis",
        "commit": "0" * 40,
        "path": "refused.yml",
        "sha256": digest,
    }
    (surface / "scratch" / "screens.jsonl").write_text(json.dumps(record) + "\n", encoding="utf-8")
    strict = evidence / "crozier-logs" / f"{digest}.strict.log"
    strict.parent.mkdir()
    strict.write_text("refused\n", encoding="utf-8")
    row = {
        "key": digest,
        "digest": digest,
        "unretrievable": "",
        "crozier_strict_exit": "1",
        "crozier_strict_log": strict.relative_to(root).as_posix(),
    }
    (evidence / "measurements.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
    return ["--jobs", "1", "--root", str(documents)]


def prepare_refusals_measure(root: Path) -> list[str]:
    script = root / "tools" / "fern-refusals" / "fern-refusals.py"
    return [sys.executable, str(script), "measure", *prepare_refusal_population(root)]


def git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=lock test", "-c", "user.email=lock@test.invalid", *args],
        check=True,
        capture_output=True,
    )


def prepare_weekly_shard(root: Path) -> list[str]:
    """One shard of a plan holding one authored probe, over a committed checkout."""
    authored_probe(root)
    git(root, "init", "-q")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "scratch checkout")
    weekly = load_tool("weekly_under_lock_test", root / "tools" / "fern-goldens" / "weekly.py")
    item = weekly.PlannedItem("authored-probes", "lock-probe", 1.0)
    plan = weekly.Plan(
        complete=False,
        items="authored-probes/lock-probe",
        base=None,
        pair=weekly.Pair(CLI, GENERATOR),
        budget_minutes=weekly.BUDGET_MINUTES,
        shard_limit_minutes=94.5,
        default_seconds=1.0,
        families={"authored-probes": weekly.FamilyTotal(1, 1.0)},
        units=1,
        shards=(weekly.PlannedJob(0, 1.0, 4.02, (item,)),),
        estimate=weekly.wall_clock([1.0]),
    )
    (root.parent / "plan.json").write_text(json.dumps(plan.to_json()), encoding="utf-8")
    script = root / "tools" / "fern-goldens" / "weekly.py"
    return [
        sys.executable,
        str(script),
        "shard",
        "--plan",
        str(root.parent / "plan.json"),
        "--index",
        "0",
        "--output",
        str(root.parent / "shard"),
    ]


def prepare_witness_screen(root: Path) -> list[str]:
    """One legacy witness candidate, served by a loopback raw-GitHub route, whose
    licence and ref screens pass, so its Fern screen runs."""
    metadata = root / "tests" / "fixtures" / "alpha" / "expected" / ".fern" / "metadata.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text(
        json.dumps(
            {
                "cliVersion": CLI,
                "generatorName": "fernapi/fern-python-sdk",
                "generatorVersion": GENERATOR,
                "generatorConfig": {"pydantic_config": {"enum_type": "python_enums"}},
            }
        ),
        encoding="utf-8",
    )
    surface = root.parent / "surface"
    (surface / "witness-search-sourcegraph").mkdir(parents=True)
    (surface / "witness-search-keys.tsv").write_text(
        "key\tselector\tregion\tcensus_status\nsample-shape\tschema:x\tschemas.md\tsupported\n", encoding="utf-8"
    )
    return [
        "screen",
        "--source",
        "sourcegraph",
        "--key",
        "sample-shape",
        "--repository",
        "acme/shop",
        "--commit",
        COMMIT,
        "--path",
        "openapi.yaml",
        "--evidence-root",
        str(surface),
        "--timeout",
        "60",
        "--disposition",
        "witness-found",
    ]


def prepare_witness_screen_tool(root: Path) -> list[str]:
    return [sys.executable, str(root / "tools" / "witness-search" / "witness_screen.py"), *prepare_witness_screen(root)]


def prepare_output_insensitive(root: Path) -> list[str]:
    """One output-insensitive comparison record whose documents sit in its own folder."""
    relative = "docs/openapi-surface/witness-search-unproven-features/lock-probe-attribution"
    folder = root / relative
    folder.mkdir(parents=True)
    for side in ("before", "after"):
        document = {"openapi": "3.0.3", "info": {"title": "lock probe", "version": "1"}, "paths": {}}
        (folder / f"{side}.json").write_text(json.dumps(document), encoding="utf-8")
    (folder / "README.md").write_text("`lock-probe-key`\n", encoding="utf-8")
    for generator in ("fern", "crozier"):
        (folder / f"{generator}-comparison.json").write_text('{"stale": true}\n', encoding="utf-8")
    (root / "docs" / "openapi-surface" / "output-insensitive.tsv").write_text(
        "key\tcontext\tsearch_record\tfern_comparison\tcrozier_comparison\n"
        f"lock-probe-key\t-\t{relative}/README.md\t{relative}/fern-comparison.json\t{relative}/crozier-comparison.json\n",
        encoding="utf-8",
    )
    script = root / "tools" / "surface-census" / "output-insensitive-remeasure.py"
    return [sys.executable, str(script), "--root", str(root), "--only", f"{relative}/fern-comparison.json"]


def prepare_probe_recipe(root: Path) -> list[str]:
    # The recipe's own Nx run, doubled below the lock.
    write_executable(root / "node_modules" / ".bin" / "nx", NX_DOUBLE)
    return just(root, "test-fern-probe-refusal")


def load_tool(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def recipe(name: str, prepare: Callable[[Path], object], *args: str) -> Callable[[Path], list[str]]:
    def run(root: Path) -> list[str]:
        prepare(root)
        return just(root, name, *args)

    return run


CASES = (
    Case("generate-fern-fixture.sh", prepare_generate_fern_fixture),
    Case("fern-overlay-goldens.sh", prepare_overlay),
    Case("generate-corpus-fixtures.sh", prepare_corpus_fixtures),
    Case("fern-goldens generate", prepare_fern_goldens("generate")),
    Case("fern-goldens run", prepare_fern_goldens("run")),
    Case("fern-references.py generate", prepare_fern_references),
    Case("just fern-references", recipe("fern-references", authored_probe, "authored-probes"), needs_just=True),
    Case(
        "just fern-goldens-generate",
        recipe(
            "fern-goldens-generate",
            lambda root: corpus_row(root, "link-ok"),
            "--version",
            GENERATOR,
            "--fixture",
            "alpha",
        ),
        needs_just=True,
    ),
    Case(
        "just fern-goldens",
        recipe("fern-goldens", lambda root: corpus_row(root, "link-ok"), "--version", GENERATOR, "--fixture", "alpha"),
        needs_just=True,
    ),
    Case(
        "just fixtures-generate-corpus",
        recipe("fixtures-generate-corpus", corpus_row, "--only", "alpha"),
        needs_just=True,
    ),
    Case("fern-refusals.py", prepare_fern_refusals),
    Case("fern-refusals.py measure", prepare_refusals_measure),
    Case(
        "just fern-refusals-measure",
        lambda root: just(root, "fern-refusals-measure", *prepare_refusal_population(root)),
        needs_just=True,
    ),
    Case("weekly.py shard", prepare_weekly_shard),
    Case("witness_screen.py", prepare_witness_screen_tool),
    Case(
        "just witness-screen", lambda root: just(root, "witness-screen", *prepare_witness_screen(root)), needs_just=True
    ),
    Case("output-insensitive-remeasure.py", prepare_output_insensitive),
    Case("just test-fern-probe-refusal", prepare_probe_recipe, needs_just=True),
)


@unittest.skipIf(os.name == "nt", "the doubled `fern` is a script with a shebang, and Fern runs on Linux and macOS")
class EveryFernEntryPointHoldsTheHostLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.pristine = tempfile.TemporaryDirectory(prefix="fern-lock-pristine-")
        root = Path(cls.pristine.name) / "repo"
        for relative in MIRRORED:
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, root / relative)
        # Presences the entry points check before Fern but never run with it doubled.
        write_executable(root / "target" / "release" / "crozier", ABSENT)
        cls.raw = RawServer(("127.0.0.1", 0), Raw)
        threading.Thread(target=cls.raw.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.raw.shutdown()
        cls.raw.server_close()
        cls.pristine.cleanup()

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="fern-lock-")
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name)
        self.cache = self.scratch / "cache"
        bin_dir = self.scratch / "bin"
        write_executable(bin_dir / "fern", FERN_DOUBLE)
        write_executable(bin_dir / "docker", ABSENT)
        write_executable(bin_dir / "cargo", CARGO_DOUBLE)
        environment = {key: value for key, value in os.environ.items() if not key.startswith(("CROZIER", "FERN"))}
        environment.update(
            PATH=f"{bin_dir}{os.pathsep}{environment['PATH']}",
            XDG_CACHE_HOME=str(self.cache),
            CROZIER_FERN_NO_DOCKER_SHIM="1",
            FERN_PYTHON_VERSION=GENERATOR,
            CROZIER_RAW_GITHUB_URL=f"http://127.0.0.1:{self.raw.server_port}",
        )
        self.environment = environment
        # The lock this process takes resolves where the entry points' does.
        patched = {"XDG_CACHE_HOME": str(self.cache)}
        saved = {key: os.environ.get(key) for key in (*patched, LOCK.HOLDER_ENV)}
        os.environ.update(patched)
        os.environ.pop(LOCK.HOLDER_ENV, None)

        def restore() -> None:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

        self.addCleanup(restore)

    def checkout(self, case: Case) -> list[str]:
        """A fresh scratch checkout for one run, its event log beside it."""
        run = Path(tempfile.mkdtemp(prefix="run-", dir=self.scratch))
        self.root, self.events = run / "repo", run / "events.jsonl"
        self.environment["CROZIER_FERN_LOCK_EVENTS"] = str(self.events)
        # Where a tool keeps the logs of a dispatch's run: this run's own directory.
        self.environment["ONEPIPELINE_NODE_SCRATCH_DIR"] = str(run)
        shutil.copytree(Path(self.pristine.name) / "repo", self.root, symlinks=True)
        return case.prepare(self.root)

    def recorded(self) -> list[dict[str, object]]:
        if not self.events.exists():
            return []
        return [json.loads(line) for line in self.events.read_text(encoding="utf-8").splitlines()]

    def start(self, argv: list[str], environment: dict[str, str]) -> tuple[subprocess.Popen[bytes], Path]:
        log = self.root.parent / "entry-point.log"
        with log.open("wb") as handle:
            process = subprocess.Popen(argv, cwd=self.root, env=environment, stdout=handle, stderr=subprocess.STDOUT)
        return process, log

    def finish(self, process: subprocess.Popen[bytes], log: Path) -> str:
        try:
            process.wait(timeout=HANG_GUARD_SECONDS)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            self.fail(f"hung past {HANG_GUARD_SECONDS}s:\n{log.read_text(encoding='utf-8', errors='replace')}")
        return log.read_text(encoding="utf-8", errors="replace")

    @contextlib.contextmanager
    def foreign_hold(self) -> Generator[Callable[[], None]]:
        """The lock held as a process outside every entry point holds it: no holder recorded."""
        path = LOCK.lock_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a+", encoding="utf-8") as handle:
            LOCK._lock(handle)
            released = []

            def release() -> None:
                with self.events.open("a", encoding="utf-8") as events:
                    events.write(json.dumps({"event": "released"}) + "\n")
                LOCK._unlock(handle)
                released.append(True)

            try:
                yield release
            finally:
                if not released:
                    LOCK._unlock(handle)

    def assert_ran_fern(self, events: list[dict[str, object]], output: str) -> None:
        kinds = [event["event"] for event in events]
        self.assertIn("fern-start", kinds, f"the entry point never reached Fern:\n{output}")
        self.assertEqual(kinds.count("fern-start"), kinds.count("fern-end"), output)
        self.assertNotIn("unexpected", kinds, f"a tool besides Fern ran:\n{events}\n{output}")

    def waits(self, case: Case) -> None:
        argv = self.checkout(case)
        with self.foreign_hold() as release:
            process, log = self.start(argv, self.environment)
            deadline = time.monotonic() + HANG_GUARD_SECONDS
            while time.monotonic() < deadline and process.poll() is None:
                if WAITING in log.read_text(encoding="utf-8", errors="replace"):
                    break
                if any(event["event"] == "fern-start" for event in self.recorded()):
                    break
                time.sleep(0.05)
            # Still held a moment after it says it waits: it must keep waiting.
            time.sleep(0.3)
            release()
        output = self.finish(process, log)
        events = self.recorded()
        self.assert_ran_fern(events, output)
        kinds = [event["event"] for event in events]
        self.assertLess(
            kinds.index("released"),
            kinds.index("fern-start"),
            f"{case.name} started Fern while another process held the host lock:\n{events}\n{output}",
        )

    def shares(self, case: Case) -> None:
        argv = self.checkout(case)
        with LOCK.hold("fern-generation-lock-test"):
            environment = dict(self.environment, **{LOCK.HOLDER_ENV: os.environ[LOCK.HOLDER_ENV]})
            process, log = self.start(argv, environment)
            output = self.finish(process, log)
        self.assert_ran_fern(self.recorded(), output)
        self.assertNotIn(WAITING, output, f"{case.name} waited on the hold it was started in")

    def test_each_entry_point_waits_for_another_holder_and_shares_its_callers_hold(self) -> None:
        for case in CASES:
            for mode in (self.waits, self.shares):
                with self.subTest(entry_point=case.name, run=mode.__name__):
                    if case.needs_just and shutil.which("just") is None:
                        self.skipTest("`just` is not installed")
                    mode(case)


class NestingIsVerifiedNotTrusted(unittest.TestCase):
    """The holder variable alone never stands in for the lock."""

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="fern-lock-nesting-")
        self.addCleanup(scratch.cleanup)
        self.environment = dict(os.environ, XDG_CACHE_HOME=scratch.name)
        self.environment.pop(LOCK.HOLDER_ENV, None)

    def held(self, **extra: str) -> int:
        return subprocess.run(
            [sys.executable, str(LOCK_SCRIPT), "held"], env=dict(self.environment, **extra), check=False
        ).returncode

    @unittest.skipIf(os.name == "nt", "Windows has no parent lookup, so only the holder itself is a hold there")
    def test_a_variable_naming_no_recorded_holder_or_no_ancestor_is_not_a_hold(self) -> None:
        self.assertEqual(1, self.held())
        self.assertEqual(1, self.held(**{LOCK.HOLDER_ENV: str(os.getpid())}), "no holder recorded")
        holder = Path(self.environment["XDG_CACHE_HOME"]) / "crozier" / "fern-generation.lock.holder"
        holder.parent.mkdir(parents=True)
        # A recorded holder that is no ancestor of the asking process (pid 1 here is
        # every process's ancestor, so a sibling's pid stands in for a stranger).
        stranger = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
        self.addCleanup(stranger.wait)
        self.addCleanup(stranger.kill)
        holder.write_text(f"{stranger.pid}\n", encoding="utf-8")
        self.assertEqual(1, self.held(**{LOCK.HOLDER_ENV: str(stranger.pid)}))
        holder.write_text(f"{os.getpid()}\n", encoding="utf-8")
        self.assertEqual(0, self.held(**{LOCK.HOLDER_ENV: str(os.getpid())}), "this process is the child's parent")

    def lock_is_free(self) -> bool:
        """Whether another process could take the lock now (a fresh process asks, so no hold of this one counts)."""
        probe = (
            "import fcntl, sys\n"
            "with open(sys.argv[1], 'a+') as handle:\n"
            "    try:\n"
            "        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)\n"
            "    except BlockingIOError:\n"
            "        sys.exit(1)\n"
        )
        lock = Path(self.environment["XDG_CACHE_HOME"]) / "crozier" / "fern-generation.lock"
        return subprocess.run([sys.executable, "-c", probe, str(lock)], check=False).returncode == 0

    @unittest.skipIf(os.name == "nt", "SIGTERM and flock are POSIX")
    def test_a_terminated_run_ends_its_command_and_frees_the_lock(self) -> None:
        """`run` hands SIGTERM to its command, exits as the signal asked, and leaves
        neither the lock held nor a holder recorded."""
        scratch = Path(self.environment["XDG_CACHE_HOME"])
        started, ended = scratch / "started", scratch / "ended"
        child = (
            "import pathlib, signal, sys, time\n"
            "def stop(signum, frame):\n"
            f"    pathlib.Path({str(ended)!r}).write_text(str(signum))\n"
            "    sys.exit(128 + signum)\n"
            "signal.signal(signal.SIGTERM, stop)\n"
            f"pathlib.Path({str(started)!r}).write_text('')\n"
            "time.sleep(60)\n"
        )
        wrapper = subprocess.Popen(
            [sys.executable, str(LOCK_SCRIPT), "run", "--label", "probe", "--", sys.executable, "-c", child],
            env=self.environment,
        )
        deadline = time.monotonic() + HANG_GUARD_SECONDS
        while not started.exists() and time.monotonic() < deadline:
            time.sleep(0.05)
        self.assertTrue(started.exists(), "the command never started")
        self.assertFalse(self.lock_is_free(), "the command ran outside the lock")
        wrapper.send_signal(signal.SIGTERM)
        self.assertEqual(128 + signal.SIGTERM, wrapper.wait(timeout=HANG_GUARD_SECONDS))
        self.assertEqual(str(int(signal.SIGTERM)), ended.read_text(), "the command was not handed the signal")
        self.assertTrue(self.lock_is_free())
        self.assertFalse((scratch / "crozier" / "fern-generation.lock.holder").exists())

    @unittest.skipIf(os.name == "nt", "flock is POSIX")
    def test_a_hold_left_by_an_error_restores_its_variable_and_frees_the_lock(self) -> None:
        saved = {key: os.environ.get(key) for key in ("XDG_CACHE_HOME", LOCK.HOLDER_ENV)}
        os.environ["XDG_CACHE_HOME"] = self.environment["XDG_CACHE_HOME"]
        os.environ.pop(LOCK.HOLDER_ENV, None)
        try:
            with self.assertRaises(RuntimeError), LOCK.hold("probe"):
                self.assertEqual(str(os.getpid()), os.environ[LOCK.HOLDER_ENV])
                self.assertFalse(self.lock_is_free())
                raise RuntimeError("an entry point failing mid-generation")
            self.assertNotIn(LOCK.HOLDER_ENV, os.environ)
            self.assertIsNone(LOCK.recorded_holder())
            self.assertTrue(self.lock_is_free())
        finally:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

    def test_run_returns_the_commands_status_and_names_one_it_cannot_start(self) -> None:
        ran = subprocess.run(
            [
                sys.executable,
                str(LOCK_SCRIPT),
                "run",
                "--label",
                "probe",
                "--",
                sys.executable,
                "-c",
                "raise SystemExit(7)",
            ],
            env=self.environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(7, ran.returncode, ran.stderr)
        missing = subprocess.run(
            [
                sys.executable,
                str(LOCK_SCRIPT),
                "run",
                "--label",
                "probe",
                "--",
                str(Path(tempfile.gettempdir()) / "no-such-command-here"),
            ],
            env=self.environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(127, missing.returncode)
        self.assertIn("probe: cannot start", missing.stderr)
        usage = subprocess.run(
            [sys.executable, str(LOCK_SCRIPT), "run", "--label", "probe"],
            env=self.environment,
            capture_output=True,
            check=False,
        )
        self.assertEqual(2, usage.returncode)


if __name__ == "__main__":
    unittest.main()
