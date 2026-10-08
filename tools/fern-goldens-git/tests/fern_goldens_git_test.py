"""The Fern goldens tooling's journeys that drive the real `git`: the
lifecycle's checkout, publication and state handling over a synthetic root with
a bare local remote, `fixtures-refresh.sh`'s sparse fetch from a local stand-in
for Fern's repository, and `generate-corpus-fixtures.sh` over a local upstream.
The offline suites, and the helpers both share, are
`tools/fern-goldens/tests/fern_goldens_test.py`'s. No case reaches the network.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import textwrap
import unittest
import unittest.mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "fern-goldens" / "tests"))

from fern_goldens_test import (  # noqa: E402 - the shared helpers' directory must be on sys.path first
    ALIASES,
    KNOWN_FAILURE,
    PIN_MANIFEST,
    REPO,
    STATE,
    TOOL,
    mirror,
)


@unittest.skipIf(os.name == "nt", "Fern golden workflow scripts run on Linux")
class FernGoldensBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        # Newer git detaches the auto-maintenance that `commit` and `fetch` start
        # (`maintenance.auto`) and the auto-gc a bare remote's `receive-pack`
        # starts (`receive.autoGc`), so either can still be writing under a temp
        # repo's `.git/` while `tearDown` removes it ("Directory not empty"). A
        # global config file, unlike `GIT_CONFIG_COUNT`, also reaches the
        # `receive-pack` a local push spawns. Every git these tests run inherits it.
        git_config = Path(self.temporary.name) / "gitconfig"
        git_config.write_text(
            "[maintenance]\n\tauto = false\n[receive]\n\tautoGc = false\n", encoding="utf-8"
        )
        environment = unittest.mock.patch.dict(os.environ, {"GIT_CONFIG_GLOBAL": str(git_config)})
        environment.start()
        self.addCleanup(environment.stop)
        self.root = Path(self.temporary.name) / "repo"
        (self.root / "scripts").mkdir(parents=True)
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        (self.root / "fake-bin").mkdir()
        mirror(
            self.root,
            "tools/fern-goldens/fern-goldens",
            "tools/corpus/corpus-lib.sh",
            "tools/corpus/corpus_remote_ref_pins.py",
            "tools/corpus/fetch-corpus.sh",
            "scripts/lib.sh",
            "tools/surface-census/openapi-surface-census.py",
        )
        shutil.copy2(ALIASES, self.root / "tests" / "fixtures" / ALIASES.name)
        shutil.copy2(PIN_MANIFEST, self.root / "tests" / "fixtures" / PIN_MANIFEST.name)
        (self.root / "justfile").write_text("default:\n    @true\n", encoding="utf-8")
        (self.root / ".gitignore").write_text("/.local\n", encoding="utf-8")
        self.write_manifest()
        self.write_executable(
            self.root / "tools" / "fern-goldens" / "generate-fern-fixture.sh",
            r"""
            #!/usr/bin/env python3
            import os
            import json
            import pathlib
            import sys

            arguments = sys.argv[1:]
            layout = "packaged"
            if arguments[:1] == ["--layout"]:
                layout = arguments[1]
                arguments = arguments[2:]
            fixture, version, spec, destination = arguments
            root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
            with (root / ".generator-calls").open("a", encoding="utf-8") as calls:
                prefix = "--layout flat " if layout == "flat" else ""
                calls.write(f"{prefix}{fixture} {version} {spec} {destination}\n")
            output = pathlib.Path(destination)
            if layout == "flat":
                output.mkdir(parents=True)
                if fixture in os.environ.get("FAIL_FLAT_FIXTURES", "").split(","):
                    (output / "partial.py").write_text("partial\n")
                    raise SystemExit(21)
                if fixture in os.environ.get("PACKAGED_SHAPE_FLAT_FIXTURES", "").split(","):
                    (output / "src" / "fern").mkdir(parents=True)
                    (output / "src" / "fern" / "__init__.py").write_text("wrong shape\n")
                    raise SystemExit(0)
                (output / "__init__.py").write_text(f"flat {fixture}:{version}\n", encoding="utf-8")
                raise SystemExit(0)
            (output / "src" / "fern").mkdir(parents=True)
            if fixture in os.environ.get("KNOWN_FAILURE_FIXTURES", "").split(","):
                manifest = json.loads(
                    (root / "tests" / "fixtures" / fixture / "known-fern-failure.json")
                    .read_text(encoding="utf-8")
                )
                fingerprint = manifest["fingerprint"]
                blocks = []
                for diagnostic in fingerprint["diagnostics"]:
                    blocks.append(
                        f"fern/output/{diagnostic['path']}:{diagnostic['line']}:"
                        f"{diagnostic['column']}: {diagnostic['message']}\n"
                        f"{diagnostic['line']} | {diagnostic['source']}"
                    )
                summary = fingerprint["ruff_summary"]
                if os.environ.get("MUTATE_KNOWN_FAILURE") == "1":
                    summary = "Found 12 errors (5 fixed, 7 remaining)."
                payload = "\n\n".join([*blocks, summary]) + "\n"
                print(f"Failed to run command: {fingerprint['failed_command']}")
                print(repr(payload.encode()))
                raise SystemExit(int(os.environ.get("KNOWN_FAILURE_EXIT_CODE", "1")))
            if fixture in os.environ.get("FAIL_FIXTURES", "").split(","):
                (output / "src" / "fern" / "partial.py").write_text("partial\n")
                raise SystemExit(19)
            (output / "src" / "fern" / "version.py").write_text(
                f"{fixture}:{version}\n", encoding="utf-8"
            )
            """,
        )
        self.write_executable(
            self.root / "fake-bin" / "curl",
            r"""
            #!/usr/bin/env python3
            import json
            import os
            import pathlib
            import sys

            args = sys.argv[1:]
            served = json.loads(os.environ.get("SERVED_DOCUMENTS", "{}"))
            if "--output" in args:
                destination = pathlib.Path(args[args.index("--output") + 1])
                headers = pathlib.Path(args[args.index("--dump-header") + 1])
                url = next(arg for arg in args if arg.startswith("https://"))
                body = next((body for fragment, body in served.items() if fragment in url), '{"openapi":"3.0.3"}\n')
                destination.write_text(body, encoding="utf-8")
                headers.write_text("HTTP/1.1 200 OK\n", encoding="utf-8")
                sys.stdout.write("200")
                raise SystemExit(0)
            if "-o" not in args:
                url = next((arg for arg in args if arg.startswith("https://")), "")
                for fragment, body in served.items():
                    if fragment in url:
                        sys.stdout.write(body)
                        raise SystemExit(0)
                print(json.dumps({"results": [
                    {"name": "4.9.0"}, {"name": "4.10.0"},
                    {"name": "4.11.0-rc.1"}, {"name": "latest"}
                ], "next": None}))
                raise SystemExit(0)
            destination = pathlib.Path(args[args.index("-o") + 1])
            url = next(arg for arg in args if arg.startswith("https://"))
            if any(name and name in url for name in os.environ.get("FAIL_FETCH", "").split(",")):
                print("synthetic fetch failure", file=sys.stderr)
                raise SystemExit(22)
            for fragment, body in served.items():
                if fragment in url:
                    destination.write_text(body, encoding="utf-8")
                    raise SystemExit(0)
            destination.write_text('{"openapi":"3.0.3"}\n', encoding="utf-8")
            """,
        )
        self.write_executable(
            self.root / "fake-bin" / "just",
            r"""
            #!/usr/bin/env python3
            import json
            import os
            import pathlib
            import signal
            import subprocess
            import sys

            args = sys.argv[1:]
            if "fetch-corpus" in args:
                fixture = args[args.index("--fixture") + 1]
                root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
                with (root / ".fetch-calls").open("a", encoding="utf-8") as calls:
                    calls.write(" ".join(args[args.index("fetch-corpus"):]) + "\n")
                command = [
                    root / "tools" / "corpus" / "fetch-corpus.sh",
                    *args[args.index("fetch-corpus") + 1:],
                ]
                result = subprocess.run(
                    command,
                    cwd=root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                stdout = result.stdout
                reported_name = os.environ.get("FETCH_REPORTED_NAME")
                if result.returncode == 0 and reported_name:
                    fetched = pathlib.Path(stdout.strip())
                    reported = fetched.with_name(reported_name)
                    fetched.replace(reported)
                    stdout = f"{reported}\n"
                sys.stdout.write(stdout)
                sys.stderr.write(result.stderr)
                raise SystemExit(result.returncode)

            root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
            fixture = os.environ.get("CROZIER_DIFF_CORPUS", "")
            expected_managed = sorted(
                path.name
                for path in (root / "tests" / "fixtures").iterdir()
                if (path / "expected").is_dir()
            )
            if fixture not in expected_managed:
                print(f"exact per-corpus filter was not set: {fixture!r}")
                raise SystemExit(8)
            if os.environ.get("CROZIER_DIFF_SUMMARY_ONLY") != "1":
                print("comparison did not request bounded summary mode")
                raise SystemExit(9)
            with (root / ".compare-calls").open("a", encoding="utf-8") as calls:
                calls.write(fixture + "\n")
            known_failure = (
                root / "tests" / "fixtures" / fixture / "known-fern-failure.json"
            )
            if known_failure.is_file():
                manifest = json.loads(known_failure.read_text(encoding="utf-8"))
                print(
                    f"KNOWN UPSTREAM FERN FAILURE: {fixture} at "
                    f"{manifest['generator']}:{manifest['generator_version']}; "
                    "Crozier generation succeeded."
                )
            mode = os.environ.get("COMPARE_MODE", "green")
            if mode == "terminated" and fixture == "alpha":
                os.kill(os.getpid(), signal.SIGTERM)
            if mode == "infrastructure" and fixture == "alpha":
                print("comparison crashed")
                raise SystemExit(7)
            if mode == "diff":
                print(f"=== {fixture} ===\n--- src/fern/{fixture}.py ---")
                print("  Normalized text differs; unified diff omitted in summary mode.")
                print("0 comparison generation failure(s) across the reported corpora.")
                print("0 comparison processing failure(s) across the reported corpora.")
                print("1 differing file(s) across the reported corpora.")
            elif mode == "generation-failure" and fixture == "alpha":
                print(f"=== {fixture} ===\n  Crozier generation failed: synthetic")
                print("1 comparison generation failure(s) across the reported corpora.")
                print("0 comparison processing failure(s) across the reported corpora.")
                print("0 differing file(s) across the reported corpora.")
            elif mode == "processing-failure" and fixture == "new-fixture":
                print(f"=== {fixture} ===\n  Comparison setup failed: not registered")
                print("0 comparison generation failure(s) across the reported corpora.")
                print("1 comparison processing failure(s) across the reported corpora.")
                print("0 differing file(s) across the reported corpora.")
            else:
                print("0 comparison generation failure(s) across the reported corpora.")
                print("0 comparison processing failure(s) across the reported corpora.")
                print("0 differing file(s) across the reported corpora.")
            """,
        )
        for fixture in ("alpha", "beta"):
            expected = self.root / "tests" / "fixtures" / fixture / "expected"
            (expected / "src" / "fern").mkdir(parents=True)
            (expected / "src" / "fern" / "version.py").write_text(
                f"prior-{fixture}\n", encoding="utf-8"
            )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_manifest(
        self,
        *,
        alpha_ref: str = "1",
        alpha_url: str = "https://example.test/alpha/openapi.json",
    ) -> None:
        manifest = f"""\
        # Corpus

        | # | name | method | source | pinned ref | license | decision | shapes |
        |---:|---|---|---|---|---|---|---|
        | 1 | `alpha` | test | {alpha_url} | `{alpha_ref}` | MIT | link-ok | alpha |
        | 2 | `beta` | test | https://example.test/beta/openapi.json | `1` | MIT | link-ok | beta |
        | 3 | `new-fixture` | test | https://example.test/new-fixture/openapi.json | `1` | MIT | link-ok | new |

        | name | status |
        |---|---|
        | `not-a-row` | documentation only |
        """
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            textwrap.dedent(manifest), encoding="utf-8"
        )

    def write_known_failure(self, fixture: str = "alpha", version: str = "5.20.0") -> Path:
        payload = json.loads(KNOWN_FAILURE.read_text(encoding="utf-8"))
        identities = {
            "alpha": ("1", "https://example.test/alpha/openapi.json"),
            "beta": ("1", "https://example.test/beta/openapi.json"),
            "new-fixture": ("1", "https://example.test/new-fixture/openapi.json"),
        }
        ref, url = identities[fixture]
        payload.update(
            {
                "generator_version": version,
                "corpus_spec_name": fixture,
                "corpus_spec_ref": ref,
                "corpus_spec_url": url,
            }
        )
        path = self.root / "tests" / "fixtures" / fixture / "known-fern-failure.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return path

    def write_pin_manifest(self, *records: tuple[str, str, str, str]) -> None:
        (self.root / "tests" / "fixtures" / PIN_MANIFEST.name).write_text(
            "# Synthetic pin manifest.\n"
            + "".join("\t".join(record) + "\n" for record in sorted(records)),
            encoding="utf-8",
        )

    @staticmethod
    def write_executable(path: Path, source: str) -> None:
        path.write_text(textwrap.dedent(source).lstrip(), encoding="utf-8")
        path.chmod(0o755)

    def environment(self, **updates: str) -> dict[str, str]:
        env = os.environ.copy()
        env.update(
            {
                "CROZIER_FERN_GOLDENS_ROOT": str(self.root),
                "PATH": f"{self.root / 'fake-bin'}{os.pathsep}{env['PATH']}",
            }
        )
        env.update(updates)
        return env

    def script_command(self, script: Path, *args: str) -> list[str]:
        command = [script.as_posix(), *args]
        if os.name != "nt":
            return command
        bash = shutil.which("bash")
        self.assertIsNotNone(bash, "Git Bash is required to exercise workflow scripts on Windows")
        return [str(bash), *command]

    def run_tool(self, *args: str, check: bool = False, **env: str) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            self.script_command(self.root / "tools" / "fern-goldens" / "fern-goldens", *args),
            cwd=self.root,
            env=self.environment(**env),
            text=True,
            capture_output=True,
            check=False,
        )
        if check and result.returncode != 0:
            self.fail(f"command failed ({result.returncode}):\n{result.stdout}\n{result.stderr}")
        return result

    def calls(self) -> list[str]:
        path = self.root / ".generator-calls"
        return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

    def fetch_calls(self) -> list[str]:
        path = self.root / ".fetch-calls"
        return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

    def compare_calls(self) -> list[str]:
        path = self.root / ".compare-calls"
        return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

    def state(self, fixture: str, golden: str = "expected") -> dict[str, str]:
        path = self.root / "tests" / "fixtures" / fixture / golden / STATE
        return json.loads(path.read_text(encoding="utf-8"))

    def write_flat_goldens(self, *rows: str) -> None:
        (self.root / "tests" / "fixtures" / "flat-goldens.txt").write_text(
            "# fixture|spec\n" + "".join(f"{row}\n" for row in rows), encoding="utf-8"
        )

    def tree(self, directory: Path) -> dict[str, bytes]:
        return {
            path.relative_to(directory).as_posix(): path.read_bytes()
            for path in directory.rglob("*")
            if path.is_file()
        }

    def test_a_declared_flat_golden_refreshes_beside_its_packaged_golden(self) -> None:
        self.write_flat_goldens("alpha|")
        flat = self.root / "tests" / "fixtures" / "alpha" / "expected-flat"

        first = self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        self.assertIn("generated alpha at", first.stdout)
        self.assertIn("generated alpha (flat) at", first.stdout)
        self.assertIn("1 generated, 0 current, 0 failed", first.stdout)
        packaged_call, flat_call = self.calls()
        self.assertTrue(packaged_call.startswith("alpha 4.9.0 "), packaged_call)
        self.assertTrue(packaged_call.endswith("/expected"), packaged_call)
        self.assertTrue(flat_call.startswith("--layout flat alpha 4.9.0 "), flat_call)
        self.assertTrue(flat_call.endswith("/expected-flat"), flat_call)
        self.assertEqual((flat / "__init__.py").read_text(encoding="utf-8"), "flat alpha:4.9.0\n")
        # The flat record is the packaged record plus its layout; the packaged
        # record keeps exactly the form it always had.
        packaged_state = self.state("alpha")
        flat_state = self.state("alpha", "expected-flat")
        self.assertNotIn("layout", packaged_state)
        self.assertEqual(flat_state, {**packaged_state, "layout": "flat"})
        with tarfile.open(self.root / ".local" / "fern-goldens" / "generated-goldens.tar.gz") as archive:
            names = archive.getnames()
        self.assertIn("tests/fixtures/alpha/expected-flat/__init__.py", names)
        self.assertIn("tests/fixtures/alpha/expected/src/fern/version.py", names)

        # Both current: nothing regenerates.
        rerun = self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        self.assertIn("0 generated, 1 current", rerun.stdout)
        self.assertEqual(len(self.calls()), 2)

        # Only the flat golden stale: only it regenerates, and the fixture counts
        # as generated so publication picks it up.
        (flat / STATE).unlink()
        flat_only = self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        self.assertIn("1 generated, 0 current", flat_only.stdout)
        self.assertEqual(len(self.calls()), 3)
        self.assertTrue(self.calls()[-1].startswith("--layout flat alpha 4.9.0 "))
        self.assertEqual(
            (self.root / ".local" / "fern-goldens" / "generated.txt").read_text(), "alpha\n"
        )

    def test_a_failed_flat_refresh_keeps_the_prior_flat_golden_and_the_new_packaged_one(self) -> None:
        self.write_flat_goldens("alpha|")
        self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        flat = self.root / "tests" / "fixtures" / "alpha" / "expected-flat"
        before = self.tree(flat)

        for variables, message in (
            ({"FAIL_FLAT_FIXTURES": "alpha"}, "flat generator exited 21"),
            (
                {"PACKAGED_SHAPE_FLAT_FIXTURES": "alpha"},
                "generator returned success without a flat module tree",
            ),
        ):
            failed = self.run_tool(
                "generate", "--version", "4.10.0", "--fixture", "alpha", **variables
            )
            self.assertEqual(failed.returncode, 1, failed.stdout)
            self.assertIn(f"alpha: {message}", failed.stderr)
            self.assertEqual(self.tree(flat), before)
            self.assertFalse(list(flat.parent.glob(".fern-goldens-stage.*")))
            # The packaged golden that did succeed is installed and reported.
            self.assertEqual(self.state("alpha")["fern_python_sdk_version"], "4.10.0")
            self.assertEqual(
                (self.root / ".local" / "fern-goldens" / "generated.txt").read_text(), "alpha\n"
            )
            (self.root / "tests" / "fixtures" / "alpha" / "expected" / STATE).unlink()

    def test_publish_commits_a_current_flat_golden_and_skips_a_stale_one(self) -> None:
        self.write_flat_goldens("alpha|")
        remote, _ = self.initialize_remote()

        def published_paths() -> list[str]:
            return subprocess.run(
                ["git", f"--git-dir={remote}", "show", "--name-only", "--format=", "goldens/test"],
                text=True,
                capture_output=True,
                check=True,
            ).stdout.split()

        self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        self.run_tool("publish", "--branch", "goldens/test", check=True)
        paths = published_paths()
        self.assertIn("tests/fixtures/alpha/expected-flat/__init__.py", paths)
        self.assertIn(f"tests/fixtures/alpha/expected-flat/{STATE}", paths)
        self.assertIn("tests/fixtures/alpha/expected/src/fern/version.py", paths)

        # A later run whose flat refresh fails publishes the packaged golden alone.
        failed = self.run_tool(
            "generate", "--version", "4.10.0", "--fixture", "alpha", FAIL_FLAT_FIXTURES="alpha"
        )
        self.assertEqual(failed.returncode, 1)
        self.run_tool("publish", "--branch", "goldens/test", check=True)
        paths = published_paths()
        self.assertIn("tests/fixtures/alpha/expected/src/fern/version.py", paths)
        self.assertFalse([path for path in paths if "expected-flat" in path], paths)

    def test_the_flat_goldens_table_is_validated_and_hand_authored_rows_are_skipped(self) -> None:
        # A row naming another fixture's spec is a hand-authored golden this tool
        # never generates, even when the row's name is a corpus fixture.
        self.write_flat_goldens("alpha|beta")
        self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        self.assertEqual(len(self.calls()), 1)
        self.assertFalse((self.root / "tests" / "fixtures" / "alpha" / "expected-flat").exists())

        for rows, message in (
            (("alpha",), "expected fixture and spec separated by one |"),
            (("alpha|", "alpha|"), "duplicate flat golden 'alpha'"),
            (("../alpha|",), "invalid fixture name"),
            (("alpha|..",), "invalid fixture name"),
        ):
            self.write_flat_goldens(*rows)
            result = self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha")
            self.assertEqual(result.returncode, 2, rows)
            self.assertIn(message, result.stderr)
        self.assertEqual(len(self.calls()), 1)

    def fixture_aliases(self) -> list[tuple[str, str]]:
        return [
            tuple(line.split("\t"))
            for line in (self.root / "tests" / "fixtures" / ALIASES.name)
            .read_text(encoding="utf-8")
            .splitlines()
            if line and not line.startswith("#")
        ]

    def initialize_remote(self) -> tuple[Path, str]:
        remote = Path(self.temporary.name) / "remote.git"
        subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
        subprocess.run(
            ["git", "init", "-b", "goldens/test"],
            cwd=self.root,
            check=True,
            capture_output=True,
        )
        for key, value in (("user.name", "Test"), ("user.email", "test@example.test")):
            subprocess.run(["git", "config", key, value], cwd=self.root, check=True)
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(
            ["git", "commit", "-m", "test: baseline"],
            cwd=self.root,
            check=True,
            capture_output=True,
        )
        baseline = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()
        subprocess.run(["git", "remote", "add", "origin", str(remote)], cwd=self.root, check=True)
        subprocess.run(
            ["git", "push", "-u", "origin", "goldens/test"],
            cwd=self.root,
            check=True,
            capture_output=True,
        )
        return remote, baseline

    def test_explicit_state_current_new_upgrade_and_no_op(self) -> None:
        first = self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        self.assertIn("1 generated, 0 current, 0 failed", first.stdout)
        self.assertEqual(self.state("alpha")["fern_python_sdk_version"], "4.9.0")
        self.assertEqual(self.state("alpha")["corpus_spec_name"], "alpha")
        self.assertEqual(self.state("alpha")["corpus_spec_ref"], "1")
        self.assertEqual(
            self.state("alpha")["corpus_spec_url"],
            "https://example.test/alpha/openapi.json",
        )

        current = self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        self.assertEqual(current.stdout.count("Fern generation summary:"), 1)
        self.assertNotIn("generation skipped", current.stdout)
        self.assertEqual(len(self.calls()), 1)

        self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "new-fixture", check=True
        )
        self.assertEqual(self.state("new-fixture")["fern_python_sdk_version"], "4.9.0")
        self.assertEqual(len(self.calls()), 2)

        self.run_tool(
            "generate", "--version", "4.10.0", "--fixture", "alpha", check=True
        )
        self.assertEqual(self.state("alpha")["fern_python_sdk_version"], "4.10.0")
        self.assertEqual(len(self.calls()), 3)

        # Default selection includes every existing corpus golden. Alpha is
        # exact and skips; beta has no state and new-fixture is stale, so both
        # generate at the requested upgrade.
        self.run_tool("generate", "--version", "4.10.0", check=True)
        self.assertEqual(len(self.calls()), 5)
        no_op = self.run_tool("generate", "--version", "4.10.0", check=True)
        self.assertIn("0 generated, 3 current, 0 failed", no_op.stdout)
        self.assertEqual(no_op.stdout.count("Fern generation summary:"), 1)
        self.assertEqual(len(self.calls()), 5)
        self.assertFalse(
            (self.root / ".local" / "fern-goldens" / "generated-goldens.tar.gz").exists()
        )

    def test_a_row_with_pin_records_records_them_and_restages_when_one_moves(self) -> None:
        """The pins land in the state file, and moving one makes the row stale."""
        schema = "base:\n  type: string\n"
        digest = hashlib.sha256(schema.encode()).hexdigest()
        mutable = "https://example.test/schemas/base.yaml"
        first = "https://raw.githubusercontent.com/e/a/" + "a" * 40 + "/src/base.yaml"
        second = "https://raw.githubusercontent.com/e/a/" + "b" * 40 + "/src/base.yaml"
        spec = json.dumps(
            {
                "openapi": "3.0.3",
                "components": {"schemas": {"Base": {"$ref": f"{mutable}#/base"}}},
            }
        )
        served = json.dumps(
            {"alpha/openapi.json": spec, "a" * 40: schema, "b" * 40: schema}
        )

        self.write_pin_manifest(("alpha", mutable, first, digest))
        generated = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            check=True,
            SERVED_DOCUMENTS=served,
        )
        self.assertIn("1 generated, 0 current, 0 failed", generated.stdout)
        self.assertEqual(
            self.state("alpha")["corpus_remote_ref_pins"],
            [{"url": mutable, "pinned_url": first, "sha256": digest}],
        )
        # The fetched document is upstream's bytes plus exactly that substitution.
        fetched = (self.root / ".local" / "corpus" / "alpha" / "openapi.json").read_text(
            encoding="utf-8"
        )
        self.assertEqual(fetched, spec.replace(mutable, first))

        unchanged = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            check=True,
            SERVED_DOCUMENTS=served,
        )
        self.assertIn("0 generated, 1 current, 0 failed", unchanged.stdout)

        self.write_pin_manifest(("alpha", mutable, second, digest))
        moved = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            check=True,
            SERVED_DOCUMENTS=served,
        )
        self.assertIn("1 generated, 0 current, 0 failed", moved.stdout)
        self.assertEqual(
            self.state("alpha")["corpus_remote_ref_pins"],
            [{"url": mutable, "pinned_url": second, "sha256": digest}],
        )

    def test_a_row_without_pin_records_writes_the_state_it_always_wrote(self) -> None:
        """Conditional emission: no pin key, so no other golden goes stale."""
        self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha", check=True)
        path = self.root / "tests" / "fixtures" / "alpha" / "expected" / STATE
        self.assertEqual(
            path.read_bytes(),
            (
                json.dumps(
                    {
                        "fern_python_sdk_version": "4.9.0",
                        "corpus_spec_name": "alpha",
                        "corpus_spec_ref": "1",
                        "corpus_spec_url": "https://example.test/alpha/openapi.json",
                    },
                    indent=2,
                )
                + "\n"
            ).encode(),
        )

    def test_authoritative_aliases_drive_python_workflow_and_bash_helper(self) -> None:
        aliases = self.fixture_aliases()
        rows = [
            f"| {number} | `{name}` | test | https://example.test/{name}/openapi.json "
            f"| `1` | MIT | link-ok | alias |"
            for number, (name, _) in enumerate(aliases, start=1)
        ]
        manifest = "\n".join(
            [
                "# Corpus",
                "",
                "| # | name | method | source | pinned ref | license | decision | shapes |",
                "|---:|---|---|---|---|---|---|---|",
                *rows,
                "",
            ]
        )
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            manifest, encoding="utf-8"
        )

        for name, fixture in aliases:
            with self.subTest(consumer="python", name=name):
                generated = self.run_tool(
                    "generate", "--version", "4.9.0", "--fixture", name, check=True
                )
                self.assertIn(f"generated {fixture}", generated.stdout)
                self.assertEqual(self.state(fixture)["corpus_spec_name"], name)
                current = self.run_tool(
                    "generate", "--version", "4.9.0", "--fixture", fixture, check=True
                )
                self.assertIn("0 generated, 1 current", current.stdout)

            with self.subTest(consumer="bash", name=name):
                resolved = subprocess.run(
                    [
                        self.root / "tools" / "corpus" / "fetch-corpus.sh",
                        "--dry-run",
                        "--fixture",
                        fixture,
                    ],
                    cwd=self.root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(resolved.returncode, 0, resolved.stderr)
                self.assertTrue(resolved.stdout.startswith(f"{name}\t"), resolved.stdout)

    def test_latest_tag_and_every_spec_identity_change_regenerate(self) -> None:
        latest = self.run_tool("latest-version", check=True)
        self.assertEqual(latest.stdout, "4.10.0\n")
        self.run_tool("generate", "--fixture", "alpha", check=True)
        self.assertEqual(self.state("alpha")["fern_python_sdk_version"], "4.10.0")
        self.write_manifest(alpha_url="https://example.test/alpha/replacement.yaml")
        self.run_tool("generate", "--fixture", "alpha", check=True)
        self.assertEqual(len(self.calls()), 2)
        self.assertEqual(
            self.state("alpha")["corpus_spec_url"],
            "https://example.test/alpha/replacement.yaml",
        )
        self.write_manifest(
            alpha_ref="2",
            alpha_url="https://example.test/alpha/replacement.yaml",
        )
        self.run_tool("generate", "--fixture", "alpha", check=True)
        self.assertEqual(len(self.calls()), 3)
        self.assertEqual(self.state("alpha")["corpus_spec_ref"], "2")
        self.assertTrue(
            (self.root / ".local" / "corpus" / "alpha" / "openapi.yaml").is_file()
        )
        self.assertTrue(all("fetch-corpus --fixture alpha" in call for call in self.fetch_calls()))

    def test_generation_uses_the_path_reported_by_fetch_corpus(self) -> None:
        self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            check=True,
            FETCH_REPORTED_NAME="authoritative-spec.yaml",
        )

        reported = (
            self.root
            / ".local"
            / "corpus"
            / "alpha"
            / "authoritative-spec.yaml"
        )
        self.assertTrue(reported.is_file())
        self.assertIn(str(reported), self.calls()[0])

    def test_incomplete_exact_state_is_not_treated_as_current(self) -> None:
        self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        generated = (
            self.root
            / "tests"
            / "fixtures"
            / "alpha"
            / "expected"
            / "src"
            / "fern"
            / "version.py"
        )
        generated.unlink()

        repaired = self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        self.assertIn("1 generated, 0 current", repaired.stdout)
        self.assertEqual(len(self.calls()), 2)
        self.assertTrue(generated.is_file())

    def test_shared_fetch_command_preserves_source_suffix_and_reuses_cache(self) -> None:
        destination = Path(self.temporary.name) / "corpus-cache"
        cases = (
            ("apideck.com-crm", "openapi.json", "api.apis.guru"),
            ("redocly.com-museum", "openapi.yaml", "raw.githubusercontent.com"),
        )
        for fixture, filename, failed_host in cases:
            with self.subTest(fixture=fixture):
                command = self.script_command(
                    REPO / "tools" / "corpus" / "fetch-corpus.sh",
                    "--fixture",
                    fixture,
                    str(destination),
                )
                first = subprocess.run(
                    command,
                    cwd=REPO,
                    env=self.environment(),
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(first.returncode, 0, first.stderr)
                canonical = destination / fixture / filename
                self.assertEqual(first.stdout, f"{canonical}\n")
                self.assertTrue(canonical.is_file())

                second = subprocess.run(
                    [*command[:-1], "--if-missing", command[-1]],
                    cwd=REPO,
                    env=self.environment(FAIL_FETCH=failed_host),
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(second.returncode, 0, second.stderr)
                self.assertEqual(second.stdout, f"{canonical}\n")

    def test_partial_failures_preserve_prior_goldens_and_state(self) -> None:
        self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        alpha = self.root / "tests" / "fixtures" / "alpha" / "expected"
        before = {
            path.relative_to(alpha).as_posix(): path.read_bytes()
            for path in alpha.rglob("*")
            if path.is_file()
        }
        failed = self.run_tool(
            "generate",
            "--version",
            "4.10.0",
            "--fixture",
            "alpha",
            "--fixture",
            "beta",
            FAIL_FIXTURES="alpha,beta",
        )
        self.assertEqual(failed.returncode, 1)
        self.assertIn("alpha:", failed.stderr)
        self.assertIn("beta:", failed.stderr)
        after = {
            path.relative_to(alpha).as_posix(): path.read_bytes()
            for path in alpha.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)
        self.assertEqual(
            (self.root / "tests" / "fixtures" / "beta" / "expected" / "src" / "fern" / "version.py").read_text(),
            "prior-beta\n",
        )
        self.assertFalse(
            (self.root / "tests" / "fixtures" / "beta" / "expected" / STATE).exists()
        )
        self.assertFalse(list((self.root / "tests" / "fixtures" / "alpha").glob(".fern-goldens-stage.*")))

    def test_exact_known_upstream_failure_is_revalidated_and_retry_is_deterministic(self) -> None:
        self.write_known_failure()
        expected = self.root / "tests" / "fixtures" / "alpha" / "expected"
        before = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }

        reports = []
        for _ in range(2):
            result = self.run_tool(
                "generate",
                "--version",
                "5.20.0",
                "--fixture",
                "alpha",
                KNOWN_FAILURE_FIXTURES="alpha",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("exact known upstream Fern failure reproduced", result.stdout)
            self.assertIn(
                "0 generated, 0 current, 0 failed, 1 exact known upstream Fern failure(s)",
                result.stdout,
            )
            report = self.root / ".local" / "fern-goldens"
            reports.append(
                (
                    (report / "generation-summary.txt").read_bytes(),
                    (report / "generated.txt").read_bytes(),
                    (report / "current.txt").read_bytes(),
                    (report / "generation-failures.txt").read_bytes(),
                    (report / "known-upstream-failures.txt").read_bytes(),
                )
            )

        self.assertEqual(reports[0], reports[1])
        self.assertEqual(reports[0][-1], b"alpha\n")
        self.assertEqual(len(self.calls()), 2, "known failures must be retried every run")
        after = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)
        self.assertFalse(list(expected.parent.glob(".fern-goldens-stage.*")))

        comparison = self.run_tool("compare")
        self.assertEqual(comparison.returncode, 0, comparison.stderr)
        self.assertIn("1 exact known upstream Fern failure(s)", comparison.stdout)
        known_report = (
            self.root
            / ".local"
            / "fern-goldens"
            / "comparison-known-upstream-failures.txt"
        )
        self.assertEqual(known_report.read_text(encoding="utf-8"), "alpha\n")

    def test_changed_known_failure_and_unexpected_success_remain_fatal(self) -> None:
        self.write_known_failure()
        expected = self.root / "tests" / "fixtures" / "alpha" / "expected"
        before = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }

        changed = self.run_tool(
            "generate",
            "--version",
            "5.20.0",
            "--fixture",
            "alpha",
            KNOWN_FAILURE_FIXTURES="alpha",
            MUTATE_KNOWN_FAILURE="1",
        )
        self.assertEqual(changed.returncode, 1)
        self.assertIn("fingerprint changed", changed.stderr)

        changed_exit = self.run_tool(
            "generate",
            "--version",
            "5.20.0",
            "--fixture",
            "alpha",
            KNOWN_FAILURE_FIXTURES="alpha",
            KNOWN_FAILURE_EXIT_CODE="2",
        )
        self.assertEqual(changed_exit.returncode, 1)
        self.assertIn("exit changed from 1 to 2", changed_exit.stderr)

        succeeded = self.run_tool(
            "generate", "--version", "5.20.0", "--fixture", "alpha"
        )
        self.assertEqual(succeeded.returncode, 1)
        self.assertIn("unexpectedly succeeded", succeeded.stderr)
        after = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)

    def test_compare_aggregates_differences_and_generation_failures(self) -> None:
        green = self.run_tool("compare")
        self.assertEqual(green.returncode, 0)
        self.assertNotIn("comparison generation failure(s)", green.stdout)
        self.assertEqual(green.stdout.count("Fern comparison summary:"), 1)
        self.assertEqual(green.stdout.count("\n"), 1)
        self.assertIn("comparing 1/2 alpha", green.stderr)
        self.assertIn("comparing 2/2 beta", green.stderr)
        self.assertNotIn("compared 2/2 beta", green.stdout + green.stderr)

        differing = self.run_tool("compare", COMPARE_MODE="diff")
        self.assertEqual(differing.returncode, 1)
        self.assertIn("2 differing files", differing.stdout)
        comparison_log = (
            self.root / ".local" / "fern-goldens" / "comparison.log"
        ).read_text(encoding="utf-8")
        self.assertIn("=== alpha ===", comparison_log)
        self.assertIn("=== beta ===", comparison_log)
        self.assertIn("unified diff omitted in summary mode", comparison_log)

        failed = self.run_tool("compare", COMPARE_MODE="generation-failure")
        self.assertEqual(failed.returncode, 1)
        self.assertIn("1 Crozier generation failures", failed.stdout)
        self.assertTrue(
            (self.root / ".local" / "fern-goldens" / "comparison.log").is_file()
        )

    def test_same_version_new_fixture_is_in_exact_comparison_scope(self) -> None:
        self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "new-fixture",
            check=True,
        )
        compared = self.run_tool("compare", COMPARE_MODE="processing-failure")
        self.assertEqual(compared.returncode, 1)
        self.assertIn("1 comparison processing failures", compared.stdout)
        self.assertEqual(
            self.compare_calls()[-3:],
            ["alpha", "beta", "new-fixture"],
        )

    def test_publish_success_before_red_then_fixed_current_rerun_is_green(self) -> None:
        remote, _ = self.initialize_remote()
        generation = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            "--fixture",
            "beta",
        )
        self.assertEqual(generation.returncode, 0)
        self.assertEqual(self.state("alpha")["fern_python_sdk_version"], "4.9.0")
        self.assertEqual(self.state("beta")["fern_python_sdk_version"], "4.9.0")
        report = self.root / ".local" / "fern-goldens"
        self.assertTrue((report / "generation-summary.txt").is_file())
        self.assertTrue((report / "generated-goldens.tar.gz").is_file())
        self.assertEqual(self.compare_calls(), [])
        self.run_tool("publish", "--branch", "goldens/test", check=True)
        remote_subject = subprocess.run(
            ["git", f"--git-dir={remote}", "log", "-1", "--format=%s", "goldens/test"],
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()
        self.assertEqual(remote_subject, "test(fixtures): refresh Fern goldens at 4.9.0")
        comparison = self.run_tool("compare", COMPARE_MODE="diff")
        self.assertEqual(comparison.returncode, 1)
        red = self.run_tool(
            "result",
            "--generation",
            "success",
            "--publication",
            "success",
            "--generation-summary",
            "success",
            "--generation-evidence",
            "success",
            "--comparison",
            "failure",
            "--comparison-summary",
            "success",
            "--comparison-evidence",
            "success",
        )
        self.assertEqual(red.returncode, 1)

        # The Crozier repair changes only comparison behavior. Exact Fern state
        # skips costly generation, publication is a no-op, and the rerun is green.
        rerun = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            "--fixture",
            "beta",
            check=True,
        )
        self.assertIn("0 generated, 2 current", rerun.stdout)
        self.assertEqual(len(self.calls()), 2)
        self.run_tool("compare", COMPARE_MODE="green", check=True)
        published = self.run_tool("publish", "--branch", "goldens/test", check=True)
        self.assertIn("no-op", published.stdout)
        green = self.run_tool(
            "result",
            "--generation",
            "success",
            "--publication",
            "success",
            "--generation-summary",
            "success",
            "--generation-evidence",
            "success",
            "--comparison",
            "success",
            "--comparison-summary",
            "success",
            "--comparison-evidence",
            "success",
        )
        self.assertEqual(green.returncode, 0)

    def test_successful_sibling_publishes_before_generation_failure_status(self) -> None:
        remote, _ = self.initialize_remote()
        generation = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            "--fixture",
            "beta",
            FAIL_FIXTURES="beta",
        )
        self.assertEqual(generation.returncode, 1)
        self.run_tool("publish", "--branch", "goldens/test", check=True)
        self.run_tool("compare", COMPARE_MODE="green", check=True)

        alpha_state = subprocess.run(
            [
                "git",
                f"--git-dir={remote}",
                "show",
                f"goldens/test:tests/fixtures/alpha/expected/{STATE}",
            ],
            text=True,
            capture_output=True,
            check=True,
        ).stdout
        self.assertEqual(json.loads(alpha_state)["fern_python_sdk_version"], "4.9.0")
        beta_state = subprocess.run(
            [
                "git",
                f"--git-dir={remote}",
                "cat-file",
                "-e",
                f"goldens/test:tests/fixtures/beta/expected/{STATE}",
            ],
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(beta_state.returncode, 0)
        final = self.run_tool(
            "result",
            "--generation",
            "failure",
            "--publication",
            "success",
            "--generation-summary",
            "success",
            "--generation-evidence",
            "success",
            "--comparison",
            "success",
            "--comparison-summary",
            "success",
            "--comparison-evidence",
            "success",
        )
        self.assertEqual(final.returncode, 1)

    def test_published_outputs_survive_terminated_comparison_process(self) -> None:
        remote, _ = self.initialize_remote()
        generation = self.run_tool(
            "generate",
            "--version",
            "4.9.0",
            "--fixture",
            "alpha",
            "--fixture",
            "beta",
            check=True,
        )
        self.assertIn("2 generated", generation.stdout)
        report = self.root / ".local" / "fern-goldens"
        self.assertTrue((report / "generation-summary.txt").is_file())
        self.assertTrue((report / "generated-goldens.tar.gz").is_file())
        self.assertEqual(self.compare_calls(), [])

        self.run_tool("publish", "--branch", "goldens/test", check=True)
        published_alpha = subprocess.run(
            [
                "git",
                f"--git-dir={remote}",
                "show",
                f"goldens/test:tests/fixtures/alpha/expected/{STATE}",
            ],
            text=True,
            capture_output=True,
            check=True,
        ).stdout
        self.assertEqual(json.loads(published_alpha)["fern_python_sdk_version"], "4.9.0")

        comparison = self.run_tool("compare", COMPARE_MODE="terminated")
        self.assertEqual(comparison.returncode, 1)
        self.assertIn("1 comparison processing failures", comparison.stdout)
        self.assertIn("terminated by signal 15", comparison.stderr)
        self.assertEqual(self.compare_calls(), ["alpha", "beta"])
        still_published = subprocess.run(
            [
                "git",
                f"--git-dir={remote}",
                "show",
                f"goldens/test:tests/fixtures/alpha/expected/{STATE}",
            ],
            text=True,
            capture_output=True,
            check=True,
        ).stdout
        self.assertEqual(still_published, published_alpha)

    def test_publish_refuses_remote_advance_without_commit_or_force(self) -> None:
        remote, baseline = self.initialize_remote()
        self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        writer = Path(self.temporary.name) / "remote-writer"
        subprocess.run(
            ["git", "clone", "--branch", "goldens/test", str(remote), str(writer)],
            check=True,
            capture_output=True,
        )
        for key, value in (("user.name", "Writer"), ("user.email", "writer@example.test")):
            subprocess.run(["git", "config", key, value], cwd=writer, check=True)
        (writer / "remote-advance.txt").write_text("advance\n", encoding="utf-8")
        subprocess.run(["git", "add", "remote-advance.txt"], cwd=writer, check=True)
        subprocess.run(
            ["git", "commit", "-m", "test: advance remote"],
            cwd=writer,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "push", "origin", "goldens/test"],
            cwd=writer,
            check=True,
            capture_output=True,
        )

        publication = self.run_tool("publish", "--branch", "goldens/test")
        self.assertEqual(publication.returncode, 2)
        self.assertIn("advanced during generation", publication.stderr)
        local_head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()
        self.assertEqual(local_head, baseline)
        staged = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=True,
        ).stdout
        self.assertEqual(staged, "")

    def test_real_generator_script_installs_atomically_across_spaced_paths(self) -> None:
        root = Path(self.temporary.name) / "generator repo with spaces"
        scripts = root / "scripts"
        fixture = root / "tests" / "fixtures" / "alpha"
        expected = fixture / "expected"
        fake_bin = root / "fake bin"
        target = root / "target" / "release"
        for directory in (scripts, expected / "src" / "fern", fake_bin, target):
            directory.mkdir(parents=True, exist_ok=True)
        mirror(root, "tools/fern-goldens/generate-fern-fixture.sh", "scripts/lib.sh",
               "tools/corpus/corpus_remote_ref_pins.py", "tools/surface-census/openapi-surface-census.py")
        spec_dir = root / "source specs"
        spec_dir.mkdir()
        spec = spec_dir / "open api.json"
        spec.write_text('{"openapi":"3.0.3"}\n', encoding="utf-8")
        (expected / "src" / "fern" / "version.py").write_text(
            "prior-valid-golden\n", encoding="utf-8"
        )
        (expected / STATE).write_text("prior-valid-state\n", encoding="utf-8")
        before = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }

        self.write_executable(
            fake_bin / "fern",
            r"""
            #!/usr/bin/env python3
            import pathlib
            import os
            import sys

            if os.environ.get("EXPECT_TREE") == "1":
                assert "path: openapi/spec/openapi.yaml" in pathlib.Path("generators.yml").read_text()
                assert pathlib.Path("openapi/spec/openapi.yaml").is_file()
                assert pathlib.Path("openapi/spec/schemas/item.yaml").read_text() == "type: string\n"
            arguments = sys.argv[1:]
            output = pathlib.Path(arguments[arguments.index("--output") + 1])
            generated = output / "fern-python-sdk" / "src" / "fern"
            generated.mkdir(parents=True)
            (generated / "version.py").write_text("complete-fern-output\n", encoding="utf-8")
            """,
        )
        self.write_executable(fake_bin / "docker", "#!/usr/bin/env bash\nexit 0\n")
        self.write_executable(
            target / "crozier",
            r"""
            #!/usr/bin/env python3
            import os
            import pathlib
            import sys

            if os.environ.get("FAIL_STRIP") == "1":
                print("partial-strip")
                raise SystemExit(23)
            sys.stdout.buffer.write(pathlib.Path(sys.argv[2]).read_bytes())
            """,
        )
        command = self.script_command(
            root / "tools/fern-goldens/generate-fern-fixture.sh",
            "alpha",
            "4.35.0",
            str(spec),
        )
        environment = self.environment(
            CROZIER_FERN_NO_DOCKER_SHIM="1",
            PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
        )
        failed = subprocess.run(
            command,
            cwd=root,
            env={**environment, "FAIL_STRIP": "1"},
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(failed.returncode, 23, failed.stderr)
        after_failure = {
            path.relative_to(expected).as_posix(): path.read_bytes()
            for path in expected.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after_failure, before)
        self.assertFalse(list(fixture.glob(".fern-output.*")))
        self.assertFalse(list(fixture.glob(".expected.backup.*")))

        # The real scaffold must put a referenced sibling at the same relative
        # location Fern reads from its configured root document.
        tree = root / ".local" / "corpus" / "alpha" / "spec"
        (tree / "schemas").mkdir(parents=True)
        root_bytes = (
            b"openapi: 3.0.3\ninfo: {title: Tree, version: '1'}\npaths: {}\n"
            b"components:\n  schemas:\n    Item:\n      $ref: './schemas/item.yaml'\n"
        )
        sibling_bytes = b"type: string\n"
        (tree / "openapi.yaml").write_bytes(root_bytes)
        (tree / "schemas" / "item.yaml").write_bytes(sibling_bytes)
        revision = "a" * 40
        base = f"https://raw.githubusercontent.com/example/api/{revision}/spec"
        (root / "tests" / "fixtures" / "CORPUS.md").write_text(
            f"| 1 | `alpha` | github-raw | {base}/openapi.yaml | `{revision}` | MIT | link-ok | sibling |\n"
        )
        (root / "tests" / "fixtures" / PIN_MANIFEST.name).write_text(
            "kind\tcorpus_name\tpath\tpinned_url\tsha256\n"
            + f"tree\talpha\tspec/openapi.yaml\t{base}/openapi.yaml\t{hashlib.sha256(root_bytes).hexdigest()}\n"
            + f"tree\talpha\tspec/schemas/item.yaml\t{base}/schemas/item.yaml\t{hashlib.sha256(sibling_bytes).hexdigest()}\n"
        )
        tree_result = subprocess.run(
            self.script_command(root / "tools/fern-goldens/generate-fern-fixture.sh", "alpha", "4.35.0", str(tree / "openapi.yaml")),
            cwd=root,
            env={**environment, "EXPECT_TREE": "1"},
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(tree_result.returncode, 0, tree_result.stderr)
        wrong_root = subprocess.run(
            self.script_command(
                root / "tools/fern-goldens/generate-fern-fixture.sh", "alpha", "4.35.0",
                str(tree / "schemas" / "item.yaml"),
            ),
            cwd=root,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(wrong_root.returncode, 0)
        self.assertIn("not the pinned tree root", wrong_root.stderr)

        self.assertEqual(
            (expected / "src" / "fern" / "version.py").read_text(encoding="utf-8"),
            "complete-fern-output\n",
        )
        self.assertFalse((expected / STATE).exists())
        self.assertFalse(list(fixture.glob(".fern-output.*")))
        self.assertFalse(list(fixture.glob(".expected.backup.*")))

    def test_vendored_generation_records_provenance_and_ci_invocation(self) -> None:
        root = Path(self.temporary.name) / "vendored repo"
        scripts = root / "scripts"
        fixture = root / "tests" / "fixtures" / "beta"
        fake_bin = root / "fake bin"
        target = root / "target" / "release"
        for directory in (scripts, fixture, fake_bin, target):
            directory.mkdir(parents=True, exist_ok=True)
        mirror(root, "tools/fern-goldens/generate-fern-fixture.sh", "scripts/lib.sh")
        (fixture / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        (root / "tests" / "fixtures" / "fern-generator-config.txt").write_text(
            "beta|public|true|AcmeClient|ignore\n", encoding="utf-8"
        )

        self.write_executable(
            fake_bin / "fern",
            r"""
            #!/usr/bin/env python3
            import json
            import os
            import pathlib
            import shutil
            import sys

            arguments = sys.argv[1:]
            output = pathlib.Path(arguments[arguments.index("--output") + 1])
            generated = output / "fern-python-sdk" / "src" / "fern"
            generated.mkdir(parents=True)
            (generated / "version.py").write_text("complete-fern-output\n", encoding="utf-8")
            shutil.copy2("generators.yml", os.environ["GENERATOR_CONFIG_RECORD"])
            pathlib.Path(os.environ["INVOCATION_RECORD"]).write_text(
                json.dumps({key: os.environ.get(key) for key in ("CI", "GITHUB_ACTIONS")}),
                encoding="utf-8",
            )
            """,
        )
        self.write_executable(fake_bin / "docker", "#!/usr/bin/env bash\nexit 0\n")
        self.write_executable(
            target / "crozier",
            r"""
            #!/usr/bin/env python3
            import pathlib
            import sys

            sys.stdout.buffer.write(pathlib.Path(sys.argv[2]).read_bytes())
            """,
        )

        invocation_record = root / "invocation.json"
        generator_config_record = root / "generators.yml"
        result = subprocess.run(
            self.script_command(root / "tools/fern-goldens/generate-fern-fixture.sh", "beta", "5.20.0"),
            cwd=root,
            env=self.environment(
                CROZIER_FERN_NO_DOCKER_SHIM="1",
                PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
                INVOCATION_RECORD=str(invocation_record),
                GENERATOR_CONFIG_RECORD=str(generator_config_record),
            ),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

        # The vendored path is not a CORPUS.md row, so `fern-goldens` never
        # records its generator; the script owns the provenance there.
        provenance = json.loads(
            (fixture / "expected" / STATE).read_text(encoding="utf-8")
        )
        self.assertEqual(provenance["fern_python_sdk_version"], "5.20.0")
        self.assertEqual(provenance["vendored_spec_path"], "tests/fixtures/beta/openapi.yml")
        self.assertEqual(provenance["audiences"], "public")
        self.assertEqual(provenance["audience_strict"], "true")
        self.assertEqual(provenance["client_class_name"], "AcmeClient")
        self.assertEqual(provenance["extra_fields"], "ignore")
        self.assertTrue(provenance["fern_cli_version"])
        rendered = generator_config_record.read_text(encoding="utf-8")
        self.assertIn("    audiences:\n      - public\n", rendered)
        self.assertIn("          client_class_name: AcmeClient\n", rendered)
        self.assertIn("            extra_fields: ignore\n", rendered)

        # Fern stamps `.fern/metadata.json`'s `invokedBy` from the environment,
        # and every published golden comes from the workflow's Actions runner.
        self.assertEqual(
            json.loads(invocation_record.read_text(encoding="utf-8")),
            {"CI": "true", "GITHUB_ACTIONS": "true"},
        )

    def test_real_generator_script_flat_mode_installs_the_local_file_system_tree(self) -> None:
        root = Path(self.temporary.name) / "flat repo"
        scripts = root / "scripts"
        fixtures = root / "tests" / "fixtures"
        fake_bin = root / "fake bin"
        target = root / "target" / "release"
        for directory in (
            scripts,
            fixtures / "beta",
            fixtures / "gamma",
            fixtures / "delta",
            fixtures / "epsilon",
            fixtures / "corpus-sources" / "zeta",
            fake_bin,
            target,
        ):
            directory.mkdir(parents=True, exist_ok=True)
        (fixtures / "corpus-sources" / "zeta" / "openapi.yaml").write_text(
            "openapi: 3.0.3 # zeta\n", encoding="utf-8"
        )
        mirror(root, "tools/fern-goldens/generate-fern-fixture.sh", "scripts/lib.sh")
        for fixture in ("beta", "delta"):
            (fixtures / fixture / "openapi.yml").write_text(f"openapi: 3.0.3 # {fixture}\n", encoding="utf-8")
        (fixtures / "fern-generator-config.txt").write_text(
            "beta||false|||acme\ngamma||false|AcmeClient||\nepsilon||false|||PetStore\n", encoding="utf-8"
        )
        # `gamma` has no spec of its own and borrows `beta`'s; `epsilon` borrows
        # the committed corpus source of the row `zeta`; `delta` is undeclared.
        (fixtures / "flat-goldens.txt").write_text(
            "# fixture|spec\nbeta|\ngamma|beta\nepsilon|zeta\n", encoding="utf-8"
        )
        record = root / "fern-invocation.json"
        self.write_executable(
            fake_bin / "fern",
            r"""
            #!/usr/bin/env python3
            import json
            import os
            import pathlib
            import sys

            arguments = sys.argv[1:]
            pathlib.Path(os.environ["FERN_RECORD"]).write_text(json.dumps({
                "arguments": arguments,
                "token": os.environ.get("FERN_TOKEN"),
                "config": json.loads(pathlib.Path("fern.config.json").read_text()),
                "generators": pathlib.Path("generators.yml").read_text(),
                "spec": pathlib.Path("openapi/openapi.yml").read_text(),
            }))
            if "--preview" in arguments:
                output = pathlib.Path(arguments[arguments.index("--output") + 1])
                generated = output / "fern-python-sdk" / "src" / "fern"
                generated.mkdir(parents=True)
                (generated / "__init__.py").write_text("packaged\n", encoding="utf-8")
                raise SystemExit(0)
            # The local-file-system path generators.yml names, relative to fern/.
            flat = pathlib.Path("..") / "generated" / "python"
            if os.environ.get("FLAT_WRITES_SRC") == "1":
                (flat / "src").mkdir(parents=True)
            flat.mkdir(parents=True, exist_ok=True)
            (flat / "__init__.py").write_text("flat-module-tree\n", encoding="utf-8")
            (flat / ".fern").mkdir()
            (flat / ".fern" / "metadata.json").write_text("{}\n", encoding="utf-8")
            """,
        )
        self.write_executable(fake_bin / "docker", "#!/usr/bin/env bash\nexit 0\n")
        self.write_executable(
            target / "crozier",
            r"""
            #!/usr/bin/env python3
            import pathlib
            import sys

            sys.stdout.buffer.write(pathlib.Path(sys.argv[2]).read_bytes())
            """,
        )
        environment = self.environment(
            CROZIER_FERN_NO_DOCKER_SHIM="1",
            PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            FERN_RECORD=str(record),
            FERN_TOKEN="a-real-looking-token",
        )

        def run(*arguments: str, **extra: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                self.script_command(root / "tools/fern-goldens/generate-fern-fixture.sh", *arguments),
                cwd=root,
                env={**environment, **extra},
                text=True,
                capture_output=True,
                check=False,
            )

        result = run("--layout", "flat", "beta", "5.20.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        invocation = json.loads(record.read_text(encoding="utf-8"))
        # `fern generate --local` into the local-file-system path: no --preview,
        # no --output, and no token, even one the caller exported.
        self.assertEqual(invocation["arguments"], ["generate", "--group", "python-sdk", "--local", "--force"])
        self.assertIsNone(invocation["token"])
        self.assertEqual(invocation["config"]["organization"], "acme")
        self.assertIn("location: local-file-system", invocation["generators"])
        flat = fixtures / "beta" / "expected-flat"
        self.assertEqual((flat / "__init__.py").read_text(encoding="utf-8"), "flat-module-tree\n")
        self.assertTrue((flat / ".fern" / "metadata.json").is_file())
        self.assertFalse((fixtures / "beta" / "expected").exists())
        provenance = json.loads((flat / STATE).read_text(encoding="utf-8"))
        self.assertEqual(provenance["layout"], "flat")
        self.assertEqual(provenance["organization"], "acme")
        self.assertEqual(provenance["fern_python_sdk_version"], "5.20.0")
        self.assertEqual(provenance["vendored_spec_path"], "tests/fixtures/beta/openapi.yml")

        # A golden without a spec generates from the one its row names.
        result = run("--layout", "flat", "gamma", "5.20.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        invocation = json.loads(record.read_text(encoding="utf-8"))
        self.assertEqual(invocation["spec"], "openapi: 3.0.3 # beta\n")
        self.assertEqual(invocation["config"]["organization"], "fern")
        self.assertIn("client_class_name: AcmeClient", invocation["generators"])
        provenance = json.loads((fixtures / "gamma" / "expected-flat" / STATE).read_text(encoding="utf-8"))
        self.assertEqual(provenance["vendored_spec_path"], "tests/fixtures/beta/openapi.yml")
        self.assertEqual(provenance["client_class_name"], "AcmeClient")

        # A mixed-case organization over a committed corpus source.
        result = run("--layout", "flat", "epsilon", "5.20.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        invocation = json.loads(record.read_text(encoding="utf-8"))
        self.assertEqual(invocation["spec"], "openapi: 3.0.3 # zeta\n")
        self.assertEqual(invocation["config"]["organization"], "PetStore")
        provenance = json.loads((fixtures / "epsilon" / "expected-flat" / STATE).read_text(encoding="utf-8"))
        self.assertEqual(
            provenance["vendored_spec_path"], "tests/fixtures/corpus-sources/zeta/openapi.yaml"
        )
        self.assertEqual(provenance["organization"], "PetStore")

        # The default mode is still the packaged run, and its record has no layout.
        result = run("beta", "5.20.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        invocation = json.loads(record.read_text(encoding="utf-8"))
        self.assertIn("--preview", invocation["arguments"])
        self.assertEqual(invocation["token"], "a-real-looking-token")
        packaged = json.loads((fixtures / "beta" / "expected" / STATE).read_text(encoding="utf-8"))
        self.assertNotIn("layout", packaged)

        before = self.tree(flat)
        for arguments, extra, message in (
            (("--layout", "flat", "delta", "5.20.0"), {}, "not a declared flat golden"),
            (("--layout", "sideways", "beta", "5.20.0"), {}, "invalid layout 'sideways'"),
            (("--layout",), {}, "--layout needs a value"),
            (
                ("--layout", "flat", "beta", "5.20.0", "", str(fixtures / "beta" / "expected")),
                {},
                "final path segment must be expected-flat",
            ),
            (("--layout", "flat", "beta", "5.20.0"), {"ORGANIZATION": "Acme Corp"}, "invalid organization"),
            (("--layout", "flat", "beta", "5.20.0"), {"ORGANIZATION": "9Lives"}, "invalid organization"),
            (("--layout", "flat", "beta", "5.20.0"), {"FLAT_WRITES_SRC": "1"}, "no flat module tree"),
        ):
            refused = run(*arguments, **extra)
            self.assertNotEqual(refused.returncode, 0, arguments)
            self.assertIn(message, refused.stderr)
        self.assertEqual(self.tree(flat), before)
        self.assertFalse((fixtures / "delta" / "expected-flat").exists())
        self.assertFalse(list((fixtures / "beta").glob(".fern-output.*")))

    def generator_repo(self, name: str) -> tuple[Path, Path, dict[str, str]]:
        """A synthetic root around the REAL generate-fern-fixture.sh: stub `fern`,
        `docker` and release `crozier` on PATH, the fixture `beta` with a spec."""
        root = Path(self.temporary.name) / name
        fixtures = root / "tests" / "fixtures"
        fake_bin = root / "fake bin"
        target = root / "target" / "release"
        for directory in (root / "scripts", fixtures / "beta", fake_bin, target):
            directory.mkdir(parents=True, exist_ok=True)
        mirror(root, "tools/fern-goldens/generate-fern-fixture.sh", "scripts/lib.sh")
        (fixtures / "beta" / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        self.write_executable(
            fake_bin / "fern",
            r"""
            #!/usr/bin/env python3
            import os
            import pathlib
            import sys

            arguments = sys.argv[1:]
            status = int(os.environ.get("FERN_EXIT", "0"))
            if status:
                print("fern: simulated generator failure", file=sys.stderr)
                raise SystemExit(status)
            if os.environ.get("FERN_NO_OUTPUT") == "1":
                raise SystemExit(0)
            if "--preview" in arguments:
                output = pathlib.Path(arguments[arguments.index("--output") + 1])
                generated = output / "fern-python-sdk" / "src" / "fern"
                generated.mkdir(parents=True)
                (generated / "version.py").write_text("generated\n", encoding="utf-8")
                raise SystemExit(0)
            flat = pathlib.Path("..") / "generated" / "python"
            flat.mkdir(parents=True)
            (flat / "__init__.py").write_text("flat\n", encoding="utf-8")
            """,
        )
        self.write_executable(fake_bin / "docker", "#!/usr/bin/env bash\nexit 0\n")
        self.write_executable(
            target / "crozier",
            r"""
            #!/usr/bin/env python3
            import pathlib
            import sys

            sys.stdout.buffer.write(pathlib.Path(sys.argv[2]).read_bytes())
            """,
        )
        environment = self.environment(
            PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            CROZIER_FERN_NO_DOCKER_SHIM="1",
        )
        return root, root / "tools/fern-goldens/generate-fern-fixture.sh", environment

    def test_real_generator_script_success_is_one_summary_line(self) -> None:
        root, script, environment = self.generator_repo("quiet repo")
        # A sandbox proxy with no CA bundle used to add two more lines of its own.
        environment.pop("CROZIER_FERN_NO_DOCKER_SHIM")
        environment.update(
            HTTPS_PROXY="http://127.0.0.1:9",
            CROZIER_FERN_DOCKER_CA=str(root / "no-such-ca.pem"),
        )
        result = subprocess.run(
            self.script_command(script, "beta", "5.20.0"),
            cwd=root, env=environment, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        lines = result.stderr.splitlines()
        self.assertEqual(len(lines), 1, result.stderr)
        self.assertIn("wrote 2 files to", lines[0])
        self.assertIn("(python-sdk@5.20.0, packaged)", lines[0])
        self.assertIn("review, then wire them into the e2e manifest", lines[0])

        # What the quiet run withheld is reported when Fern fails, with Fern's
        # own exit status (fern-goldens matches a known failure on it).
        failed = subprocess.run(
            self.script_command(script, "beta", "5.20.0"),
            cwd=root, env={**environment, "FERN_EXIT": "7"},
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(failed.returncode, 7, failed.stderr)
        self.assertIn("simulated generator failure", failed.stderr)
        self.assertIn("fern generate (python-sdk@5.20.0, packaged) exited 7", failed.stderr)
        self.assertIn("fix the cause Fern printed above, then re-run", failed.stderr)
        self.assertIn("CROZIER_FERN_NO_DOCKER_SHIM=1", failed.stderr)
        self.assertIn("set CROZIER_FERN_DOCKER_CA to the bundle", failed.stderr)

    def test_every_committed_audience_and_client_class_row_renders_its_generators_yml(self) -> None:
        root, script, environment = self.generator_repo("committed config repo")
        fixtures = root / "tests" / "fixtures"
        shutil.copy2(REPO / "tests" / "fixtures" / "fern-generator-config.txt", fixtures)
        self.write_executable(
            root / "fake bin" / "fern",
            r"""
            #!/usr/bin/env python3
            import os
            import pathlib
            import shutil
            import sys

            arguments = sys.argv[1:]
            shutil.copy2("generators.yml", os.environ["GENERATOR_CONFIG_RECORD"])
            output = pathlib.Path(arguments[arguments.index("--output") + 1])
            generated = output / "fern-python-sdk" / "src" / "fern"
            generated.mkdir(parents=True)
            (generated / "version.py").write_text("generated\n", encoding="utf-8")
            """,
        )
        rows = [
            line.split("|")
            for line in (fixtures / "fern-generator-config.txt").read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("#")
        ]
        rows = [row for row in rows if row[1] or row[3]]
        self.assertGreaterEqual(len(rows), 4, "the committed table should set audiences and client names")
        for fixture, audiences, _, client_class_name, extra_fields, *_ in rows:
            with self.subTest(fixture=fixture):
                (fixtures / fixture).mkdir(exist_ok=True)
                (fixtures / fixture / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
                record = root / f"{fixture}.generators.yml"
                result = subprocess.run(
                    self.script_command(script, fixture, "5.20.0"),
                    cwd=root,
                    env={**environment, "GENERATOR_CONFIG_RECORD": str(record)},
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                audience_lines = "".join(f"      - {label}\n" for label in audiences.split(",") if label)
                self.assertEqual(
                    record.read_text(encoding="utf-8"),
                    "api:\n"
                    "  path: openapi/openapi.yml\n"
                    "groups:\n"
                    "  python-sdk:\n"
                    + ("    audiences:\n" + audience_lines if audiences else "")
                    + "    generators:\n"
                    "      - name: fernapi/fern-python-sdk\n"
                    "        version: 5.20.0\n"
                    "        config:\n"
                    + (f"          client_class_name: {client_class_name}\n" if client_class_name else "")
                    + "          pydantic_config:\n"
                    "            enum_type: python_enums\n"
                    + (f"            extra_fields: {extra_fields}\n" if extra_fields else "")
                    + "        output:\n"
                    "          location: local-file-system\n"
                    "          path: ../generated/python\n",
                )

    def test_real_generator_script_names_a_next_action_for_every_refusal(self) -> None:
        root, script, environment = self.generator_repo("refusing repo")
        fixtures = root / "tests" / "fixtures"
        config = fixtures / "fern-generator-config.txt"
        (fixtures / "gamma").mkdir()  # a fixture without its spec
        (fixtures / "flat-goldens.txt").write_text("beta|\n", encoding="utf-8")

        def run(*arguments: str, **extra: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                self.script_command(script, *arguments),
                cwd=root, env={**environment, **extra},
                text=True, capture_output=True, check=False,
            )

        cases = [
            (("nosuch", "5.20.0"), {}, "scaffold it with tools/fern-goldens/fixture-new.sh nosuch"),
            (
                ("beta", "5.20.0", "", str(fixtures / "beta" / "missing" / "expected")),
                {},
                "create it with mkdir -p, or omit DEST_PATH",
            ),
            (("beta", "5.20.0"), {"AUDIENCE_STRICT": "maybe"}, "use true, false, or leave it empty"),
            (("beta", "5.20.0"), {"EXTRA_FIELDS": "sometimes"}, "use allow, ignore, forbid, or leave it empty"),
            (("beta", "5.20.0"), {"FERN_AUDIENCES": "public: [x]"}, "invalid audiences 'public: [x]'"),
            (("beta", "5.20.0"), {"FERN_AUDIENCES": "public,,internal"}, "use comma-separated labels"),
            # Only the first line would reach `read`; the rest would reach the provenance.
            (("beta", "5.20.0"), {"FERN_AUDIENCES": "public\nbad: [x]"}, "use comma-separated labels"),
            (("beta", "5.20.0"), {"FERN_AUDIENCES": "public,"}, "each starting with a letter"),
            (("beta", "5.20.0"), {"FERN_AUDIENCES": "Off"}, "not true/false/yes/no/on/off/y/n/null"),
            (("beta", "5.20.0"), {"CLIENT_CLASS_NAME": "Acme\n          timeout: 1"}, "invalid client_class_name"),
            (("beta", "5.20.0"), {"CLIENT_CLASS_NAME": "9Client"}, "use a Python class name"),
            (("beta", "5.20.0"), {"CLIENT_CLASS_NAME": "null"}, "CLIENT_CLASS_NAME or its"),
            (("beta", "5.20.0"), {"FERN_CLI_VERSION": "latest; touch pwned"}, "invalid FERN_CLI_VERSION"),
            (("gamma", "5.20.0"), {}, "or pass the document as SPEC_PATH"),
            (("beta", "5.20.0"), {"FERN_NO_OUTPUT": "1"}, "no packaged SDK"),
            (("--layout", "flat", "beta", "5.20.0"), {"FERN_NO_OUTPUT": "1"}, "without an __init__.py"),
        ]
        for arguments, extra, message in cases:
            with self.subTest(arguments=arguments, extra=extra):
                refused = run(*arguments, **extra)
                self.assertNotEqual(refused.returncode, 0, refused.stderr)
                self.assertIn(message, refused.stderr)
        with self.subTest("missing fixture names its path"):
            self.assertIn(str(fixtures / "nosuch"), run("nosuch", "5.20.0").stderr)
        with self.subTest("no packaged SDK"):
            self.assertIn("fix the spec, then re-run", run("beta", "5.20.0", FERN_NO_OUTPUT="1").stderr)

        with self.subTest("duplicate configuration"):
            config.write_text("beta||true|||\nbeta||false|||\n", encoding="utf-8")
            duplicate = run("beta", "5.20.0")
            config.unlink()
            self.assertNotEqual(duplicate.returncode, 0)
            self.assertIn("delete all but one 'beta|…' row, then re-run", duplicate.stderr)

        expected = fixtures / "beta" / "expected"
        self.assertEqual(run("beta", "5.20.0").returncode, 0)
        before = self.tree(expected)
        with self.subTest("stale backup"):
            # A stale backup at this process's own backup path blocks the
            # install; `exec` keeps the PID the script names its backup after.
            stale = subprocess.run(
                ["bash", "-c", 'mkdir "$0/.expected.backup.$$" && exec "$1" beta 5.20.0',
                 str(fixtures / "beta"), str(script)],
                cwd=root, env=environment, text=True, capture_output=True, check=False,
            )
            for leftover in (fixtures / "beta").glob(".expected.backup.*"):
                leftover.rmdir()
            self.assertNotEqual(stale.returncode, 0)
            self.assertIn("stale backup blocks the install", stale.stderr)
            self.assertIn("diff -r", stale.stderr)
            self.assertIn("otherwise remove it (rm -rf), then re-run", stale.stderr)
            self.assertEqual(self.tree(expected), before)

        with self.subTest("failed install"):
            # The final rename fails: the prior golden comes back, and the caller
            # is told what to check before retrying.
            real_mv = shutil.which("mv")
            self.assertIsNotNone(real_mv)
            failing_bin = root / "failing mv"
            failing_bin.mkdir()
            self.write_executable(
                failing_bin / "mv",
                "#!/usr/bin/env bash\n"
                'case "${1:-}" in */.fern-output.*/expected) echo "mv: simulated failure" >&2; exit 1 ;; esac\n'
                f'exec "{real_mv}" "$@"\n',
            )
            install = run("beta", "5.20.0", PATH=f"{failing_bin}{os.pathsep}{environment['PATH']}")
            self.assertNotEqual(install.returncode, 0)
            self.assertIn("could not install the staged golden", install.stderr)
            self.assertIn("is writable and has free space, then re-run", install.stderr)
            self.assertEqual(self.tree(expected), before)

        with self.subTest("failed install whose rollback fails too"):
            # Both renames fail: the prior golden stays under its backup path,
            # and the diagnostic names that path and the move that restores it.
            self.write_executable(
                failing_bin / "mv",
                "#!/usr/bin/env bash\n"
                'case "${1:-}" in */.fern-output.*/expected|*/.expected.backup.*)'
                ' echo "mv: simulated failure" >&2; exit 1 ;; esac\n'
                f'exec "{real_mv}" "$@"\n',
            )
            stranded = run("beta", "5.20.0", PATH=f"{failing_bin}{os.pathsep}{environment['PATH']}")
            self.assertEqual(stranded.returncode, 1, stranded.stderr)
            backups = list((fixtures / "beta").glob(".expected.backup.*"))
            self.assertEqual(len(backups), 1, stranded.stderr)
            self.assertFalse(expected.exists())
            self.assertIn(f"nor restore the prior golden from {backups[0]}", stranded.stderr)
            self.assertIn(f"(mv {backups[0]} {expected})", stranded.stderr)
            backups[0].rename(expected)
            self.assertEqual(self.tree(expected), before)

        with self.subTest("symlinked destination"):
            shutil.rmtree(expected)
            elsewhere = root / "elsewhere"
            elsewhere.mkdir()
            expected.symlink_to(elsewhere, target_is_directory=True)
            symlinked = run("beta", "5.20.0")
            self.assertNotEqual(symlinked.returncode, 0)
            self.assertIn("refusing to replace symlinked destination", symlinked.stderr)
            self.assertIn("pass a real directory path as DEST_PATH", symlinked.stderr)
            self.assertTrue(expected.is_symlink())

        with self.subTest("an invalid latest version names the override"):
            self.write_executable(root / "tools" / "fern-goldens" / "fern-goldens",
                                  "#!/usr/bin/env bash\necho latest\n")
            invalid = run("beta", "")
            self.assertNotEqual(invalid.returncode, 0, invalid.stderr)
            self.assertIn("latest-version returned invalid Fern version 'latest'", invalid.stderr)
            self.assertIn("pass the version to generate at as FERN_PYTHON_VERSION", invalid.stderr)

        with self.subTest("an unwritable fixture directory names the failed step and the fix"):
            if os.geteuid() == 0:
                self.skipTest("root writes through a read-only directory")
            expected = fixtures / "beta" / "expected"
            before = self.tree(expected) if expected.exists() else None
            (fixtures / "beta").chmod(0o555)
            try:
                blocked = run("beta", "5.20.0")
            finally:
                (fixtures / "beta").chmod(0o755)
            self.assertNotEqual(blocked.returncode, 0, blocked.stderr)
            self.assertRegex(blocked.stderr, r"generate-fern-fixture: line \d+: 'mktemp -d [^']*' failed \(exit 1\)")
            self.assertIn("are writable on a disk with free space, then re-run", blocked.stderr)
            if before is not None:
                self.assertEqual(before, self.tree(expected))

    def test_numbered_status_rows_below_the_manifest_are_skipped(self) -> None:
        """CORPUS.md's per-batch STATUS tables are numbered too, and are not rows.

        The real manifest ends with `| 130 | `komga` | `media-type-range` | ⚠️ … |`
        and a dozen like it: four cells, a leading number, and no part of the
        canonical table. Reading one as a malformed manifest row made every
        `fern-goldens` subcommand exit before it fetched anything.
        """
        manifest = "\n".join(
            [
                "# Corpus",
                "",
                "| # | name | method | source | pinned ref | license | decision | shapes |",
                "|---:|---|---|---|---|---|---|---|",
                "| 1 | `alpha` | test | https://example.test/alpha/openapi.json | `1` | MIT | link-ok | alpha |",
                "",
                "## Batch 2 — status",
                "",
                "| # | name | settles | state |",
                "|---:|---|---|---|",
                "| 1 | `alpha` | some-shape | ✅ byte-matched |",
                "",
            ]
        )
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            manifest, encoding="utf-8"
        )
        generated = self.run_tool(
            "generate", "--version", "4.9.0", "--fixture", "alpha", check=True
        )
        self.assertIn("generated alpha", generated.stdout)
        self.assertEqual([call.split()[0] for call in self.calls()], ["alpha"])

    def test_the_manifest_header_anchor_is_the_one_corpus_md_writes(self) -> None:
        """The tool anchors the whole walk on that header; drift would read zero rows."""
        header = next(
            line
            for line in (REPO / "tests" / "fixtures" / "CORPUS.md")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.startswith("| # |")
        )
        cells = [cell.strip() for cell in header.strip().strip("|").split("|")]
        declared = TOOL.read_text(encoding="utf-8").split("MANIFEST_HEADER = [", 1)[1]
        declared = declared.split("]", 1)[0]
        self.assertEqual(
            cells,
            [value.strip().strip('"') for value in declared.split(",") if value.strip()],
            "tools/fern-goldens/fern-goldens no longer anchors on tests/fixtures/CORPUS.md's header",
        )

    def test_invalid_inputs_fail_before_generation_or_publication(self) -> None:
        cases = [
            ("generate", "--version", "latest", "--fixture", "alpha"),
            ("generate", "--version", "4.9.0; touch nope", "--fixture", "alpha"),
            ("generate", "--version", "4.9.0", "--fixture", "../alpha"),
            ("generate", "--version", "4.9.0", "--fixture", "missing"),
        ]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(self.run_tool(*args).returncode, 2)
        self.assertEqual(self.calls(), [])

        self.write_manifest(alpha_url="http://example.test/alpha/openapi.json")
        self.assertEqual(
            self.run_tool("generate", "--version", "4.9.0", "--fixture", "alpha").returncode,
            2,
        )
        self.assertEqual(
            self.run_tool("publish", "--branch", "-unsafe").returncode,
            2,
        )

        invalid_fetch = subprocess.run(
            self.script_command(
                REPO / "tools" / "corpus" / "fetch-corpus.sh", "--fixture", "../unsafe"
            ),
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(invalid_fetch.returncode, 0)
        self.assertIn("invalid fixture name", invalid_fetch.stderr)

        generator_source = (REPO / "tools" / "fern-goldens" / "generate-fern-fixture.sh").read_text(
            encoding="utf-8"
        )
        self.assertIn('"$repo_root/tools/fern-goldens/fern-goldens" latest-version', generator_source)
        self.assertNotIn('${2:-4.35.0}', generator_source)

        outside = Path(self.temporary.name) / "outside"
        outside.mkdir()
        generator = subprocess.run(
            self.script_command(
                REPO / "tools" / "fern-goldens" / "generate-fern-fixture.sh",
                "exhaustive",
                "4.35.0",
                str(REPO / "tests" / "fixtures" / "exhaustive" / "openapi.yml"),
                str(outside / "expected"),
            ),
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(generator.returncode, 0)
        self.assertIn("it must stay below", generator.stderr)

    def test_just_recipes_preserve_untrusted_arguments_without_shell_evaluation(self) -> None:
        just = shutil.which("just", path=os.environ.get("PATH"))
        self.assertIsNotNone(just)
        marker = Path(self.temporary.name) / "dispatch-injection"
        injected_version = f"latest; : > {marker}; #"
        generation = subprocess.run(
            [
                just,
                "--justfile",
                str(REPO / "justfile"),
                "fern-goldens-generate",
                "--version",
                injected_version,
                "--fixture",
                "alpha",
            ],
            cwd=REPO,
            env=self.environment(),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(generation.returncode, 0)
        self.assertIn(
            "invalid Fern version", generation.stdout + generation.stderr
        )
        self.assertFalse(marker.exists())

        branch_marker = Path(self.temporary.name) / "branch-injection"
        publication = subprocess.run(
            [
                just,
                "--justfile",
                str(REPO / "justfile"),
                "fern-goldens-publish",
                f"$(touch {branch_marker})",
            ],
            cwd=REPO,
            env=self.environment(),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(publication.returncode, 0)
        self.assertIn(
            "invalid branch name", publication.stdout + publication.stderr
        )
        self.assertFalse(branch_marker.exists())


@unittest.skipIf(os.name == "nt", "Fern golden workflow scripts run on Linux")
class FixturesRefreshTests(unittest.TestCase):
    """`tools/fern-goldens/fixtures-refresh.sh` over a synthetic root with real git:
    a `git` wrapper on PATH serves the pinned-commit fetch from a local stand-in
    for Fern's repository (no network), and can refuse `sparse-checkout`."""

    SPEC = "test-definitions/fern/apis/query-parameters-openapi/openapi.yml"
    SEED = "seed/python-sdk/query-parameters-openapi/no-custom-config"

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        git_config = base / "gitconfig"
        git_config.write_text("[maintenance]\n\tauto = false\n", encoding="utf-8")
        self.root = base / "repo"
        mirror(self.root, "tools/fern-goldens/fixtures-refresh.sh")
        target = self.root / "target" / "release"
        target.mkdir(parents=True)
        (target / "crozier").write_text(
            "#!/usr/bin/env bash\n"
            # A scratch directory the refresh cannot remove afterwards.
            '[ -z "${LOCK_SCRATCH:-}" ] || chmod a-w "$(dirname "$2")"\n'
            '[ -z "${FAIL_STRIP:-}" ] || { echo "crozier: simulated strip failure" >&2; exit 3; }\n'
            'cat "$2"\n',
            encoding="utf-8",
        )
        (target / "crozier").chmod(0o755)

        fern = base / "fern"
        (fern / Path(self.SPEC).parent).mkdir(parents=True)
        (fern / self.SPEC).write_text("openapi: 3.0.3\n", encoding="utf-8")
        (fern / self.SEED / "src").mkdir(parents=True)
        (fern / self.SEED / "src" / "client.py").write_text("client = 1\n", encoding="utf-8")
        (fern / "elsewhere").mkdir()
        (fern / "elsewhere" / "unrelated.txt").write_text("outside the cone\n", encoding="utf-8")
        environment = {**os.environ, "GIT_CONFIG_GLOBAL": str(git_config)}
        for command in (
            ["init", "-q"],
            ["add", "-A"],
            ["-c", "user.name=t", "-c", "user.email=t@example.test", "commit", "-qm", "fern"],
        ):
            subprocess.run(["git", "-C", str(fern), *command], env=environment, check=True)

        real_git = shutil.which("git")
        self.assertIsNotNone(real_git)
        fake_bin = base / "fake bin"
        fake_bin.mkdir()
        (fake_bin / "git").write_text(
            textwrap.dedent(
                f"""\
                #!/usr/bin/env bash
                set -euo pipefail
                case " $* " in
                  *" sparse-checkout ${{FAIL_SPARSE:-unset}} "*)
                    echo "git: 'sparse-checkout' is not a git command. See 'git --help'." >&2
                    exit 1 ;;
                  *" fetch "*) exec "{real_git}" -C "$2" fetch -q "{fern}" HEAD ;;
                esac
                exec "{real_git}" "$@"
                """
            ),
            encoding="utf-8",
        )
        (fake_bin / "git").chmod(0o755)
        self.environment = {**environment, "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}"}
        self.fixture = self.root / "tests" / "fixtures" / "query-parameters-openapi"

    def refresh(self, *arguments: str, **extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(self.root / "tools" / "fern-goldens" / "fixtures-refresh.sh"), *arguments],
            cwd=self.root,
            env={**self.environment, **extra},
            capture_output=True,
            text=True,
            check=False,
        )

    def test_a_scratch_directory_that_cannot_be_made_names_the_fix(self) -> None:
        refused = self.refresh(TMPDIR=str(self.root / "no-such-tmp"))
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn("fixtures-refresh: could not create a scratch directory — point TMPDIR at a writable",
                      refused.stderr)

    def test_a_successful_refresh_prints_one_summary_line(self) -> None:
        result = self.refresh()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(
            result.stderr.splitlines(),
            [
                "fixtures-refresh: refreshed 1 fixture(s) from Fern @ 4d07e6aee — review the diff;"
                " update the e2e manifest for any new matched files."
            ],
        )
        self.assertEqual((self.fixture / "openapi.yml").read_text(encoding="utf-8"), "openapi: 3.0.3\n")
        self.assertEqual(
            (self.fixture / "expected" / "src" / "client.py").read_text(encoding="utf-8"), "client = 1\n"
        )

    def test_a_failed_sparse_checkout_setup_stops_with_its_cause_and_fix(self) -> None:
        for subcommand in ("init", "add"):
            with self.subTest(subcommand=subcommand):
                result = self.refresh(FAIL_SPARSE=subcommand)
                self.assertNotEqual(result.returncode, 0, result.stderr)
                self.assertIn(
                    f"fixtures-refresh: git sparse-checkout {subcommand} failed: git: 'sparse-checkout'"
                    " is not a git command",
                    result.stderr,
                )
                self.assertIn("git 2.26 or newer (git --version); upgrade git, then re-run", result.stderr)
                self.assertEqual(len(result.stderr.splitlines()), 1, result.stderr)
                self.assertFalse(self.fixture.exists())

    def stand_in_generator(self) -> None:
        """A `generate-fern-fixture.sh` that prints its own summary, or fails as FAIL_GENERATE says."""
        generator = self.root / "tools" / "fern-goldens" / "generate-fern-fixture.sh"
        generator.write_text(
            "#!/usr/bin/env bash\n"
            '[ -z "${FAIL_GENERATE:-}" ] || { echo "generate-fern-fixture: docker is not running" >&2; exit 4; }\n'
            'echo "generate-fern-fixture: wrote 9 files to tests/fixtures/exhaustive/expected" >&2\n',
            encoding="utf-8")
        generator.chmod(0o755)

    def test_an_exhaustive_refresh_prints_one_summary_line_for_both(self) -> None:
        self.stand_in_generator()
        result = self.refresh("exhaustive")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr.splitlines(), [
            "fixtures-refresh: refreshed 1 fixture(s) from Fern @ 4d07e6aee and exhaustive — review the diff;"
            " update the e2e manifest for any new matched files."])

    def test_a_failed_exhaustive_generation_shows_its_output_and_the_step(self) -> None:
        self.stand_in_generator()
        result = self.refresh("exhaustive", FAIL_GENERATE="1")
        self.assertEqual(result.returncode, 4, result.stderr)
        self.assertIn("generate-fern-fixture: docker is not running", result.stderr)
        self.assertIn("fixtures-refresh: stopped while regenerating tests/fixtures/exhaustive with Fern's "
                      "container generator (exit 4)", result.stderr)

    @unittest.skipIf(os.geteuid() == 0, "root removes a read-only directory's entries")
    def test_a_scratch_directory_it_cannot_remove_is_named_without_hiding_the_result(self) -> None:
        scratch = self.root.parent / "tmp"
        scratch.mkdir()
        self.addCleanup(lambda: [path.chmod(0o755) for path in scratch.rglob("*") if path.is_dir()])
        result = self.refresh(LOCK_SCRATCH="1", TMPDIR=str(scratch))
        self.assertEqual(result.returncode, 0, result.stderr)
        [workdir] = list(scratch.iterdir())
        self.assertIn(f"fixtures-refresh: could not remove the scratch directory {workdir} — delete it "
                      f"(rm -rf {workdir})", result.stderr)
        self.assertIn("fixtures-refresh: refreshed 1 fixture(s)", result.stderr)
        # A failed run keeps its own status and step behind the same note.
        failed = self.refresh(LOCK_SCRATCH="1", FAIL_STRIP="1", TMPDIR=str(scratch))
        self.assertEqual(failed.returncode, 3, failed.stderr)
        self.assertIn("could not remove the scratch directory", failed.stderr)
        self.assertIn("fixtures-refresh: stopped while refreshing tests/fixtures/query-parameters-openapi (exit 3)",
                      failed.stderr)

    def test_a_failed_step_is_named_on_exit(self) -> None:
        result = self.refresh(FAIL_STRIP="1")
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertIn("crozier: simulated strip failure", result.stderr)
        self.assertIn(
            "fixtures-refresh: stopped while refreshing tests/fixtures/query-parameters-openapi (exit 3)",
            result.stderr,
        )
        self.assertIn("git checkout -- tests/fixtures/", result.stderr)


@unittest.skipIf(os.name == "nt", "Fern golden workflow scripts run on Linux")
class GenerateCorpusFixturesTests(unittest.TestCase):
    """`tools/fern-goldens/generate-corpus-fixtures.sh` and the real corpus-lib over
    a synthetic root: a stand-in generator, and a real local git repository as a
    repository-source row's upstream (no network)."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "repo"
        mirror(
            self.root,
            "tools/fern-goldens/generate-corpus-fixtures.sh",
            "tools/corpus/corpus-lib.sh",
            "tools/corpus/corpus_remote_ref_pins.py",
            "tools/surface-census/openapi-surface-census.py",
        )
        fixtures = self.root / "tests" / "fixtures"
        (fixtures / "alpha").mkdir(parents=True)
        shutil.copy2(ALIASES, fixtures / ALIASES.name)
        shutil.copy2(PIN_MANIFEST, fixtures / PIN_MANIFEST.name)
        (fixtures / "alpha" / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        generator = self.root / "tools" / "fern-goldens" / "generate-fern-fixture.sh"
        generator.write_text(
            "#!/usr/bin/env bash\n"
            '[ -z "${GENERATOR_CALLS:-}" ] || printf \'%s\\n\' "$*" >> "$GENERATOR_CALLS"\n'
            '[ -z "${FAIL_GENERATE:-}" ] || { echo "generate-fern-fixture: simulated failure" >&2; exit 9; }\n'
            'echo "generate-fern-fixture: wrote 1 files to tests/fixtures/$1/expected" >&2\n'
            # A log of its output the caller can no longer read.
            '[ -z "${HIDE_LOG:-}" ] || chmod 0 "$(readlink /proc/$$/fd/2)"\n',
            encoding="utf-8",
        )
        generator.chmod(0o755)

        # A repository-source row whose upstream holds no OpenAPI document.
        upstream = self.base / "upstream"
        upstream.mkdir()
        (upstream / "README.md").write_text("no spec here\n", encoding="utf-8")
        # A YAML file that is no OpenAPI document, so discovery reads one file.
        (upstream / "settings.yml").write_text("theme: dark\n", encoding="utf-8")
        environment = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull}
        for command in (
            ["init", "-q"],
            ["add", "-A"],
            ["-c", "user.name=t", "-c", "user.email=t@example.test", "commit", "-qm", "upstream"],
        ):
            subprocess.run(["git", "-C", str(upstream), *command], env=environment, check=True)
        (fixtures / "CORPUS.md").write_text(
            "| # | name | method | source | pinned ref | license | decision | shapes |\n"
            "|---:|---|---|---|---|---|---|---|\n"
            "| 1 | `alpha` | test | https://example.test/alpha/openapi.yml | `1` | MIT | committed | a |\n"
            "| 2 | `beta` | test | https://example.test/beta/openapi.yml | `1` | MIT | committed | b |\n"
            f"| 3 | `gamma` | git | {upstream} | `HEAD` | MIT | link-ok | c |\n",
            encoding="utf-8",
        )

    def upstream_row(self, name: str, files: dict[str, str]) -> Path:
        """A local git repository holding `files`, registered as the link-ok row `name`."""
        upstream = self.base / f"upstream-{name}"
        for relative, text in files.items():
            (upstream / relative).parent.mkdir(parents=True, exist_ok=True)
            (upstream / relative).write_text(text, encoding="utf-8")
        environment = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull}
        for command in (["init", "-q"], ["add", "-A"],
                        ["-c", "user.name=t", "-c", "user.email=t@example.test", "commit", "-qm", "upstream"]):
            subprocess.run(["git", "-C", str(upstream), *command], env=environment, check=True)
        with (self.root / "tests" / "fixtures" / "CORPUS.md").open("a", encoding="utf-8") as handle:
            handle.write(f"| 9 | `{name}` | git | {upstream} | `HEAD` | MIT | link-ok | d |\n")
        return upstream

    def test_a_fetched_repositorys_one_openapi_document_is_what_the_generator_reads(self) -> None:
        self.upstream_row("delta", {"README.md": "docs\n", "settings.yml": "theme: dark\n",
                                    "spec/api/openapi.yaml": "openapi: 3.0.3\ninfo: {title: d, version: '1'}\n"})
        calls = self.base / "calls"
        result = self.run_script("--only", "delta", "--fetch-root", str(self.base / "cache"),
                                 GENERATOR_CALLS=str(calls))
        self.assertEqual(result.returncode, 0, result.stderr)
        [call] = calls.read_text(encoding="utf-8").splitlines()
        self.assertEqual(call.split(" ")[0], "delta")
        self.assertTrue(call.endswith("/delta/spec/api/openapi.yaml"), call)
        # (git's own note that a local clone ignores --filter precedes it.)
        self.assertEqual(result.stderr.splitlines()[-1], "generate-fern-fixture: wrote 1 files to tests/fixtures/delta/expected")

    def test_a_fetched_repository_with_several_openapi_documents_generates_nothing(self) -> None:
        self.upstream_row("epsilon", {"v1/openapi.yml": "openapi: 3.0.3\n", "v2/openapi.json": '{"openapi": "3.1.0"}\n'})
        calls = self.base / "calls"
        result = self.run_script("--only", "epsilon", "--fetch-root", str(self.base / "cache"),
                                 GENERATOR_CALLS=str(calls))
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn("found multiple OpenAPI candidates under", result.stderr)
        self.assertIn("/epsilon/v1/openapi.yml", result.stderr)
        self.assertIn("/epsilon/v2/openapi.json", result.stderr)
        self.assertIn("could not discover exactly one OpenAPI spec for epsilon", result.stderr)
        self.assertFalse(calls.exists(), "the generator ran over an ambiguous repository")

    def run_script(self, *arguments: str, **extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(self.root / "tools" / "fern-goldens" / "generate-corpus-fixtures.sh"), *arguments],
            cwd=self.root,
            env={**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, **extra},
            capture_output=True,
            text=True,
            check=False,
        )

    def test_each_fixture_reports_only_the_generators_own_line(self) -> None:
        result = self.run_script("--only", "alpha")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stderr.splitlines(),
            ["generate-fern-fixture: wrote 1 files to tests/fixtures/alpha/expected"],
        )
        failed = self.run_script("--only", "alpha", FAIL_GENERATE="1")
        self.assertEqual(failed.returncode, 9, failed.stderr)
        self.assertIn(
            f"generate-corpus-fixtures: generating alpha (spec source: "
            f"{self.root / 'tests' / 'fixtures' / 'alpha' / 'openapi.yml'}) exited 9",
            failed.stderr,
        )
        self.assertIn("then re-run with --only alpha", failed.stderr)
        # The failing generator's own output is shown before the fix.
        self.assertIn("generate-fern-fixture: simulated failure\n", failed.stderr)

    @unittest.skipIf(not Path("/proc/self/fd").is_dir() or os.geteuid() == 0,
                     "the stand-in hides its log through /proc, from a reader file modes deny")
    def test_a_summary_it_cannot_read_names_the_log_and_what_to_review(self) -> None:
        result = self.run_script("--only", "alpha", HIDE_LOG="1")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("generate-corpus-fixtures: generated alpha, but could not read the generator's summary "
                      "from ", result.stderr)
        self.assertIn("review tests/fixtures/alpha/expected, then wire it into the e2e manifest", result.stderr)

    def test_a_batch_reports_one_line_for_every_fixture_it_generated(self) -> None:
        beta = self.root / "tests" / "fixtures" / "beta"
        beta.mkdir()
        (beta / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        result = self.run_script("--committed")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr.splitlines(), [
            "generate-corpus-fixtures: generated 2 fixtures (alpha beta) — review, then wire them into the "
            "e2e manifest (see docs/matching.md)"])

    @unittest.skipIf(os.name == "nt" or os.geteuid() == 0, "file modes do not deny this reader")
    def test_an_unreadable_manifest_generates_nothing(self) -> None:
        manifest = self.root / "tests" / "fixtures" / "CORPUS.md"
        manifest.chmod(0)
        self.addCleanup(manifest.chmod, 0o644)
        result = self.run_script("--all")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(f"could not read the numbered rows of {manifest}", result.stderr)
        self.assertIn("git checkout -- tests/fixtures/CORPUS.md", result.stderr)
        self.assertNotIn("generate-fern-fixture:", result.stderr)

    def test_a_discovery_search_that_cannot_read_a_file_stops_naming_it(self) -> None:
        stubs = self.base / "failing-rg"
        stubs.mkdir()
        (stubs / "rg").write_text("#!/bin/sh\necho 'rg: Permission denied' >&2\nexit 2\n", encoding="utf-8")
        (stubs / "rg").chmod(0o755)
        result = self.run_script("--only", "gamma", "--fetch-root", str(self.base / "cache"),
                                 PATH=f"{stubs}{os.pathsep}{os.environ['PATH']}")
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn("settings.yml while looking for the OpenAPI document (rg exit 2)", result.stderr)
        self.assertIn("the search for the OpenAPI document under", result.stderr)
        self.assertNotIn("generate-fern-fixture:", result.stderr)

    def test_each_refusal_names_how_to_supply_what_is_missing(self) -> None:
        fixtures = self.root / "tests" / "fixtures"
        with self.subTest("committed row without its spec"):
            result = self.run_script("--only", "beta")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("git checkout -- tests/fixtures/beta/openapi.yml", result.stderr)
            self.assertIn("tools/corpus/fetch-corpus.sh --fixture beta", result.stderr)
        with self.subTest("no discoverable spec"):
            result = self.run_script("--only", "gamma", "--fetch-root", str(self.base / "cache"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("could not discover exactly one OpenAPI spec for gamma", result.stderr)
            self.assertIn(f"to {fixtures / 'gamma' / 'openapi.yml'}", result.stderr)
            self.assertIn("then re-run", result.stderr)
        with self.subTest("uncreatable fetch root"):
            blocking = self.base / "a-file"
            blocking.write_text("in the way\n", encoding="utf-8")
            result = self.run_script("--only", "gamma", "--fetch-root", str(blocking / "cache"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(f"cannot create the fetch root {blocking / 'cache'} for gamma", result.stderr)
            self.assertNotIn("could not discover", result.stderr)
        with self.subTest("an --only matching no row"):
            result = self.run_script("--only", "delta", "--dry-run")
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(result.stdout, "")
            self.assertIn("no corpus rows selected — --only 'delta' names no", result.stderr)
            self.assertIn("pass one of its row names or fixture directories", result.stderr)
            self.assertIn("--dry-run without --only lists them", result.stderr)
        with self.subTest("no committed row"):
            corpus = fixtures / "CORPUS.md"
            original = corpus.read_text(encoding="utf-8")
            corpus.write_text(original.replace("| committed |", "| link-ok |"), encoding="utf-8")
            result = self.run_script("--committed", "--dry-run")
            corpus.write_text(original, encoding="utf-8")
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("no numbered row that committed mode selects", result.stderr)
            self.assertIn("use --all when none is marked committed", result.stderr)
        with self.subTest("missing manifest"):
            (fixtures / "CORPUS.md").unlink()
            result = self.run_script()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("restore it with git checkout -- tests/fixtures/CORPUS.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
