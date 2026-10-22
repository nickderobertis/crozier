"""Inspect the actual wheel installation and import it with its own interpreter."""

from __future__ import annotations

import argparse
import importlib
import importlib.metadata
import json
import pkgutil
import sys
from pathlib import Path

from sdk_evaluation import (
    DISTRIBUTION,
    PACKAGE,
    Distribution,
    Environment,
    ImportSnapshot,
    RuntimeSnapshot,
    Sha256,
    canonical_digest,
    file_digest,
    files_digest,
    normalized_distribution,
)


def distribution_digest(distribution: importlib.metadata.Distribution) -> Sha256:
    files = distribution.files
    if not files:
        raise ValueError(f"distribution {distribution.name} has no installed-file record")
    entries = []
    for entry in sorted(files, key=str):
        if entry.suffix == ".pyc" or "__pycache__" in entry.parts:
            continue
        path = distribution.locate_file(entry)
        if not isinstance(path, Path):
            raise ValueError(f"installed distribution is not on the filesystem: {distribution.name}")
        if not path.is_file():
            raise ValueError(f"installed distribution file missing: {path}")
        entries.append((str(entry), path))
    return files_digest(entries)


def snapshot(distribution_name: str) -> RuntimeSnapshot:
    distributions: list[Distribution] = []
    for distribution in importlib.metadata.distributions():
        distributions.append(
            {
                "name": normalized_distribution(distribution.name),
                "version": distribution.version,
                "sha256": distribution_digest(distribution),
            }
        )
    distributions.sort(key=lambda entry: entry["name"])
    environment: Environment = {
        "executable": sys.executable,
        "executable_sha256": file_digest(Path(sys.executable)),
        "prefix": sys.prefix,
        "base_prefix": sys.base_prefix,
        "python_version": sys.version,
        "configuration_sha256": file_digest(Path(sys.prefix) / "pyvenv.cfg"),
        "distributions": distributions,
    }
    selected = [entry for entry in distributions if entry["name"] == distribution_name]
    if len(selected) != 1:
        raise ValueError(f"expected one installed {distribution_name} distribution")
    return {
        "distribution_sha256": selected[0]["sha256"],
        "environment": environment,
        "environment_sha256": canonical_digest(environment),
    }


def failed_package(name: str) -> None:
    raise ValueError(f"could not discover SDK package {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect", "imports"))
    parser.add_argument("distribution", choices=(DISTRIBUTION,))
    parser.add_argument("package", choices=(PACKAGE,))
    args = parser.parse_args()
    try:
        before = snapshot(args.distribution)
        if args.mode == "inspect":
            result: RuntimeSnapshot | ImportSnapshot = before
        else:
            package = importlib.import_module(args.package)
            if package.__file__ is None or not Path(package.__file__).resolve().is_relative_to(
                Path(sys.prefix).resolve()
            ):
                raise ValueError("SDK import did not come from the fresh installation environment")
            modules = sorted(
                {
                    args.package,
                    *(
                        entry.name
                        for entry in pkgutil.walk_packages(package.__path__, args.package + ".", onerror=failed_package)
                    ),
                }
            )
            for name in modules:
                importlib.import_module(name)
            after = snapshot(args.distribution)
            if before != after:
                raise ValueError("SDK imports changed the installed distribution or environment")
            result = {**after, "modules": modules, "modules_sha256": canonical_digest(modules)}
        json.dump(result, sys.stdout, sort_keys=True)
        sys.stdout.write("\n")
        return 0
    except (OSError, ValueError, ImportError) as error:
        print(f"SDK runtime inspection: {error}; repair the installation and rerun evaluate-sdk", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
