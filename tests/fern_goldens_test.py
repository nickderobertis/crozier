from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
TOOL = REPO / "scripts" / "fern-goldens"
STATE = ".crozier-fern-golden.json"


class FernGoldensBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        (self.root / "scripts").mkdir(parents=True)
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        (self.root / "fake-bin").mkdir()
        shutil.copy2(TOOL, self.root / "scripts" / "fern-goldens")
        (self.root / "justfile").write_text("default:\n    @true\n", encoding="utf-8")
        (self.root / ".gitignore").write_text("/.local\n", encoding="utf-8")
        self.write_manifest()
        self.write_executable(
            self.root / "scripts" / "generate-fern-fixture.sh",
            r"""
            #!/usr/bin/env python3
            import os
            import pathlib
            import sys

            fixture, version, spec, destination = sys.argv[1:]
            root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
            with (root / ".generator-calls").open("a", encoding="utf-8") as calls:
                calls.write(f"{fixture} {version} {spec} {destination}\n")
            output = pathlib.Path(destination)
            (output / "src" / "fern").mkdir(parents=True)
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
            if "-o" not in args:
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
            destination.write_text('{"openapi":"3.0.3"}\n', encoding="utf-8")
            """,
        )
        self.write_executable(
            self.root / "fake-bin" / "just",
            r"""
            #!/usr/bin/env python3
            import os
            import pathlib
            import sys

            args = sys.argv[1:]
            if "fetch-corpus" in args:
                fixture = args[args.index("--fixture") + 1]
                root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
                destination = root / ".local" / "corpus" / fixture / "openapi.json"
                with (root / ".fetch-calls").open("a", encoding="utf-8") as calls:
                    calls.write(" ".join(args[args.index("fetch-corpus"):]) + "\n")
                if fixture in os.environ.get("FAIL_FETCH", "").split(","):
                    print("synthetic fetch failure", file=sys.stderr)
                    raise SystemExit(22)
                if "--if-missing" not in args or not destination.is_file():
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_text('{"openapi":"3.0.3"}\n', encoding="utf-8")
                print(destination)
                raise SystemExit(0)

            root = pathlib.Path(os.environ["CROZIER_FERN_GOLDENS_ROOT"])
            managed = os.environ.get("CROZIER_DIFF_CORPORA", "").split(",")
            expected_managed = sorted(
                path.name
                for path in (root / "tests" / "fixtures").iterdir()
                if (path / "expected").is_dir()
            )
            if managed != expected_managed:
                print(f"exact managed-corpus filter was not set: {managed}")
                raise SystemExit(8)
            (root / ".compare-scope").write_text(",".join(managed), encoding="utf-8")
            mode = os.environ.get("COMPARE_MODE", "green")
            if mode == "infrastructure":
                print("comparison crashed")
                raise SystemExit(7)
            if mode == "diff":
                print("=== alpha ===\n--- src/fern/a.py ---\n- Fern\n+ Crozier")
                print("=== beta ===\n--- src/fern/b.py ---\n- Fern\n+ Crozier")
                print("0 comparison generation failure(s) across the reported corpora.")
                print("0 comparison processing failure(s) across the reported corpora.")
                print("2 differing file(s) across the reported corpora.")
            elif mode == "generation-failure":
                print("=== alpha ===\n  Crozier generation failed: synthetic")
                print("1 comparison generation failure(s) across the reported corpora.")
                print("0 comparison processing failure(s) across the reported corpora.")
                print("0 differing file(s) across the reported corpora.")
            elif mode == "processing-failure":
                print("=== new-fixture ===\n  Comparison setup failed: not registered")
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
            self.script_command(self.root / "scripts" / "fern-goldens", *args),
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

    def state(self, fixture: str) -> dict[str, str]:
        path = self.root / "tests" / "fixtures" / fixture / "expected" / STATE
        return json.loads(path.read_text(encoding="utf-8"))

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
            (self.root / ".local" / "corpus" / "alpha" / "openapi.json").is_file()
        )
        self.assertTrue(all("fetch-corpus --fixture alpha" in call for call in self.fetch_calls()))

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

    def test_shared_fetch_command_uses_canonical_cache_and_reuses_it(self) -> None:
        destination = Path(self.temporary.name) / "corpus-cache"
        command = self.script_command(
            REPO / "scripts" / "fetch-corpus.sh",
            "--fixture",
            "apideck.com-crm",
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
        canonical = destination / "apideck.com-crm" / "openapi.json"
        self.assertEqual(first.stdout, f"{canonical}\n")
        self.assertTrue(canonical.is_file())

        second = subprocess.run(
            [*command[:-1], "--if-missing", command[-1]],
            cwd=REPO,
            env=self.environment(FAIL_FETCH="api.apis.guru"),
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

    def test_compare_aggregates_differences_and_generation_failures(self) -> None:
        green = self.run_tool("compare")
        self.assertEqual(green.returncode, 0)
        self.assertNotIn("comparison generation failure(s)", green.stdout)
        self.assertEqual(green.stdout.count("Fern comparison summary:"), 1)

        differing = self.run_tool("compare", COMPARE_MODE="diff")
        self.assertEqual(differing.returncode, 1)
        self.assertIn("=== alpha ===", differing.stdout)
        self.assertIn("=== beta ===", differing.stdout)
        self.assertIn("2 differing files", differing.stdout)

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
            (self.root / ".compare-scope").read_text(encoding="utf-8"),
            "alpha,beta,new-fixture",
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
        comparison = self.run_tool("compare", COMPARE_MODE="diff")
        self.assertEqual(comparison.returncode, 1)
        self.run_tool("publish", "--branch", "goldens/test", check=True)
        remote_subject = subprocess.run(
            ["git", f"--git-dir={remote}", "log", "-1", "--format=%s", "goldens/test"],
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()
        self.assertEqual(remote_subject, "test(fixtures): refresh Fern goldens at 4.9.0")
        red = self.run_tool(
            "result",
            "--generation",
            "success",
            "--comparison",
            "failure",
            "--publication",
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
            "--comparison",
            "success",
            "--publication",
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
        self.run_tool("compare", COMPARE_MODE="green", check=True)
        self.run_tool("publish", "--branch", "goldens/test", check=True)

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
            "--comparison",
            "success",
            "--publication",
            "success",
        )
        self.assertEqual(final.returncode, 1)

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
        shutil.copy2(REPO / "scripts" / "generate-fern-fixture.sh", scripts)
        shutil.copy2(REPO / "scripts" / "lib.sh", scripts)
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
            import sys

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
            scripts / "generate-fern-fixture.sh",
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

        succeeded = subprocess.run(
            command,
            cwd=root,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(succeeded.returncode, 0, succeeded.stderr)
        self.assertEqual(
            (expected / "src" / "fern" / "version.py").read_text(encoding="utf-8"),
            "complete-fern-output\n",
        )
        self.assertFalse((expected / STATE).exists())
        self.assertFalse(list(fixture.glob(".fern-output.*")))
        self.assertFalse(list(fixture.glob(".expected.backup.*")))

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
                REPO / "scripts" / "fetch-corpus.sh", "--fixture", "../unsafe"
            ),
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(invalid_fetch.returncode, 0)
        self.assertIn("invalid fixture name", invalid_fetch.stderr)

        generator_source = (REPO / "scripts" / "generate-fern-fixture.sh").read_text(
            encoding="utf-8"
        )
        self.assertIn('"$repo_root/scripts/fern-goldens" latest-version', generator_source)
        self.assertNotIn('${2:-4.35.0}', generator_source)

        outside = Path(self.temporary.name) / "outside"
        outside.mkdir()
        generator = subprocess.run(
            self.script_command(
                REPO / "scripts" / "generate-fern-fixture.sh",
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


if __name__ == "__main__":
    unittest.main()
