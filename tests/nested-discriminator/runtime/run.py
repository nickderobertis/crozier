"""Generate the nested-discriminator SDK and exercise each Pydantic major.

Exit status: 0 when every document, mode and Pydantic major passes; 1 when a
generation, install or wire check fails, or the fixture drifts from the
derivation (the failing command's output is printed); 2 on a usage error or a
missing prerequisite (the crozier binary or uv).
"""

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(command: list[str], environment: dict[str, str]) -> None:
    result = subprocess.run(command, env=environment, capture_output=True, text=True, check=False)
    if result.returncode:
        raise SystemExit(
            f"{subprocess.list2cmdline(command)} failed ({result.returncode}):\n{result.stdout}{result.stderr}"
        )


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--binary", type=Path, default=root / "target" / "debug" / ("crozier.exe" if os.name == "nt" else "crozier")
    )
    args = parser.parse_args()
    if not args.binary.is_file():
        parser.error("crozier binary missing: run just nx run nested-discriminator-runtime:test")
    uv = shutil.which("uv")
    if uv is None:
        parser.error("uv missing: install uv to provide the pinned Python 3.11 SDK environments")
    environment = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_")}
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    source = root / "docs/fern-measurements/examples/nested-discriminator-wire/openapi.yml"
    script = Path(__file__).with_name("wire.py")
    with tempfile.TemporaryDirectory(prefix="crozier-nested-discriminator-") as temporary:
        directory = Path(temporary)
        value_source = directory / "value-discriminator.yml"
        derived = source.read_text()
        for before, after, count in [
            ("propertyName: crust", "propertyName: value", 1),
            ("[kind, crust,", "[kind, value,", 2),
            ("\n        crust:", "\n        value:", 2),
        ]:
            if derived.count(before) != count or after in derived:
                raise SystemExit(
                    f"fixture drift: expected {count} occurrences of {before!r}; review the value-discriminator derivation"
                )
            derived = derived.replace(before, after)
        value_source.write_text(derived)
        for index, spec in enumerate([source, value_source]):
            for strict in [False, True]:
                sdk = directory / f"sdk-{index}-{strict}"
                command = [
                    str(args.binary),
                    "--no-config",
                    "generate",
                    "python",
                    "--spec",
                    str(spec),
                    "--output",
                    str(sdk),
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                ]
                if strict:
                    command.append("--fern-strict")
                run(command, environment)
                for major in ["1.10.26", "2.14.1"]:
                    command = [uv, "run", "--no-project", "--python", "3.11"]
                    for dependency in [
                        f"pydantic=={major}",
                        "httpx==0.28.1",
                        "typing_extensions==4.16.0",
                        "jsonschema==4.26.0",
                        "PyYAML==6.0.3",
                    ]:
                        command.extend(["--with", dependency])
                    command.extend([str(script), str(sdk), str(spec), "crust" if index == 0 else "value"])
                    run(command, environment)
    print("nested discriminator runtime: both documents, modes and Pydantic majors passed")


if __name__ == "__main__":
    main()
