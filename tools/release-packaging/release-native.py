#!/usr/bin/env python3
"""Build one wheel executable per target, archive it, and prove both installers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import struct
import subprocess
import sys
import tarfile
import tomllib
import zipfile
from dataclasses import asdict, dataclass
from email.parser import Parser
from enum import Enum
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import NewType

Version = NewType("Version", str)
ReleaseTag = NewType("ReleaseTag", str)
Sha256 = NewType("Sha256", str)


class Target(str, Enum):
    INTEL_MAC = "x86_64-apple-darwin"
    ARM_MAC = "aarch64-apple-darwin"
    INTEL_LINUX = "x86_64-unknown-linux-gnu"
    ARM_LINUX = "aarch64-unknown-linux-gnu"

    @property
    def darwin(self) -> bool:
        return self in (Target.INTEL_MAC, Target.ARM_MAC)

    @property
    def arm(self) -> bool:
        return self in (Target.ARM_MAC, Target.ARM_LINUX)

    @property
    def wheel_arch(self) -> str:
        return "arm64" if self == Target.ARM_MAC else "aarch64" if self.arm else "x86_64"


@dataclass(frozen=True)
class ReleaseIdentity:
    tag: ReleaseTag
    version: Version


@dataclass(frozen=True)
class ReleaseContract:
    schemaVersion: int
    target: Target
    tag: ReleaseTag
    version: Version
    archive: str
    wheel: str
    binarySha256: Sha256
    archiveBinarySha256: Sha256
    wheelBinarySha256: Sha256


@dataclass(frozen=True)
class BuildResult:
    wheel: Path
    version: Version
    contract: ReleaseContract


def run(*args: str, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(args, env=env, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(
            f"{args[0]} failed ({result.returncode}): {result.stdout}{result.stderr}; fix this command and rebuild the staged release"
        )
    return result.stdout


def validate_wheel(wheel: Path, target: Target, version: str) -> bytes:
    with zipfile.ZipFile(wheel) as archive:
        names = [n for n in archive.namelist() if n.endswith(".data/scripts/crozier")]
        if len(names) != 1:
            raise ValueError(f"expected one wheel executable, found {names}; rebuild with maturin bin bindings")
        binary = archive.read(names[0])
        metadata_names = [n for n in archive.namelist() if n.endswith(".dist-info/METADATA")]
        if len(metadata_names) != 1:
            raise ValueError(f"expected one METADATA, found {metadata_names}; rebuild the wheel with maturin")
        metadata = Parser().parsestr(archive.read(metadata_names[0]).decode())
        if metadata["Name"] != "crozier" or metadata["Version"] != version:
            raise ValueError(
                f"wheel metadata {metadata['Name']}/{metadata['Version']} differs from crozier/{version}; rebuild from the matching tag"
            )
        platform_tag = wheel.name[:-4].rsplit("-", 1)[-1]
        if wheel.name != f"crozier-{version}-py3-none-{platform_tag}.whl":
            raise ValueError(
                f"wheel filename {wheel.name} differs from crozier/{version}/py3-none; rebuild with maturin bin bindings"
            )
        platform_pattern = (
            rf"macosx_\d+_\d+_{target.wheel_arch}"
            if target.darwin
            else rf"(?:manylinux_\d+_\d+|manylinux\d{{4}}|linux)_{target.wheel_arch}"
        )
        if not all(re.fullmatch(platform_pattern, tag) for tag in platform_tag.split(".")):
            raise ValueError(f"wheel {wheel.name} has the wrong platform for {target.value}; rebuild with that target")
        if target.darwin:
            expected = 0x0100000C if target.arm else 0x01000007
            valid = (
                len(binary) >= 8
                and binary[:4] == b"\xcf\xfa\xed\xfe"
                and struct.unpack_from("<I", binary, 4)[0] == expected
            )
        else:
            expected = 183 if target.arm else 62
            valid = (
                len(binary) >= 20 and binary[:4] == b"\x7fELF" and struct.unpack_from("<H", binary, 18)[0] == expected
            )
        if not valid:
            raise ValueError(
                f"executable header {binary[:20].hex()} differs from {target.value}; rebuild with that Rust target"
            )
    return binary


def release_identity(tag: str) -> ReleaseIdentity:
    package = tomllib.loads(Path("Cargo.toml").read_text()).get("package")
    if not isinstance(package, dict) or "version" not in package:
        raise ValueError(
            "Cargo.toml must contain a package table and version; restore [package] with a literal version"
        )
    version = package["version"]
    if not isinstance(version, str) or not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+(?:-[A-Za-z0-9.-]+)?(?:\+[A-Za-z0-9.-]+)?", version
    ):
        raise ValueError("unsupported Cargo.toml version; use a literal semantic version without path separators")
    if tag != f"v{version}":
        raise ValueError(f"tag {tag} does not match Cargo.toml version {version}; use v{version}")
    return ReleaseIdentity(ReleaseTag(tag), Version(version))


def pack(target: Target, tag: str, output: Path, wheels: Path) -> BuildResult:
    identity = release_identity(tag)
    tag, version = identity.tag, identity.version
    candidates = list(wheels.glob("*.whl"))
    if len(candidates) != 1:
        raise ValueError(
            f"expected one wheel for {target.value}, found {candidates}; clean the output directory and rebuild"
        )
    wheel = candidates[0]
    binary = validate_wheel(wheel, target, version)
    base = f"crozier-{tag}-{target.value}"
    release = output / tag
    release.mkdir(exist_ok=True)
    packed = release / f"{base}.tar.gz"
    with TemporaryDirectory(prefix=f"stage-{target.value}-", dir=output) as temporary:
        stage = Path(temporary)
        exe = stage / "crozier"
        exe.write_bytes(binary)
        exe.chmod(0o755)
        for name in ["README.md", "LICENSE", "NOTICE", "CHANGELOG.md"]:
            shutil.copyfile(name, stage / name)
        with tarfile.open(packed, "w:gz") as archive:
            for path in sorted(stage.iterdir()):
                archive.add(path, arcname=path.name)
    (release / f"{base}.sha256").write_text(f"{hashlib.sha256(packed.read_bytes()).hexdigest()}  {packed.name}\n")
    with tarfile.open(packed) as archive:
        member = archive.extractfile("crozier")
        if member is None:
            raise ValueError("archive has no executable; fix the archive layout and rebuild")
        archived = member.read()
    if archived != binary:
        raise ValueError("archive and wheel executable differ; inspect staged contents and rebuild")
    digest = Sha256(hashlib.sha256(binary).hexdigest())
    contract = ReleaseContract(
        1, target, tag, version, str(packed), str(wheel), digest, Sha256(hashlib.sha256(archived).hexdigest()), digest
    )
    (output / f"contract-{target.value}.json").write_text(json.dumps(asdict(contract), indent=2) + "\n")
    return BuildResult(wheel, version, contract)


def build(target: Target, tag: str, output: Path) -> BuildResult:
    tag = release_identity(tag).tag
    output.mkdir(parents=True, exist_ok=True)
    wheels = output / f"wheels-{target.value}"
    wheels.mkdir(exist_ok=True)
    run("rustup", "target", "add", target.value)
    run("maturin", "build", "--release", "--locked", "--target", target.value, "--out", str(wheels))
    return pack(target, tag, output, wheels)


def smoke(target: Target, tag: str, output: Path, built: BuildResult) -> None:
    # llmlint: ignore[changed_behavior_has_e2e] Intel-on-ARM execution requires an Apple Silicon/Rosetta runner. Host-native installation and both Darwin artifact contracts are tested locally; the Mac release job installs and runs both architectures.
    prefix = ["arch", "-x86_64"] if target == Target.INTEL_MAC and platform.machine() == "arm64" else []
    installed = output / f"installed-{target.value}"
    # Distinct staged URLs replace forge transport, preserving real installer
    # checksum verification. Rosetta selects Intel uname and executes its CLI.
    checksums = output / "checksum-root"
    checksums.mkdir(exist_ok=True)
    shutil.copytree(output / tag, checksums / tag, dirs_exist_ok=True)
    env = {**os.environ, "CROZIER_RELEASE_BASE_URL": output.as_uri(), "CROZIER_CHECKSUM_BASE_URL": checksums.as_uri()}
    run(*prefix, "sh", "scripts/install.sh", "--version", tag, "--to", str(installed), env=env)
    run(
        *prefix,
        "bash",
        "scripts/smoke.sh",
        built.version,
        env={**os.environ, "CROZIER_BIN": str(installed / "crozier")},
    )
    venv = output / f"venv-{target.value}"
    run("python3", "-m", "venv", str(venv))
    wheel_install = output / f"wheel-installed-{target.value}"
    # py3-none executable wheels need no Intel Python: pip stages the platform
    # explicitly, and Rosetta executes the resulting Intel CLI.
    wheel_platform = built.wheel.name[:-4].rsplit("-", 1)[-1]
    run(
        str(venv / "bin/python"),
        "-m",
        "pip",
        "install",
        "--no-index",
        "--no-deps",
        "--only-binary=:all:",
        "--platform",
        wheel_platform,
        "--target",
        str(wheel_install),
        str(built.wheel),
    )
    run(
        *prefix,
        "bash",
        "scripts/smoke.sh",
        built.version,
        env={**os.environ, "CROZIER_BIN": str(wheel_install / "bin/crozier")},
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Exit statuses: 0 success; 1 operational or validation failure; 2 invalid invocation.",
    )
    parser.add_argument("--target", required=True, choices=[t.value for t in Target])
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--pack-only", action="store_true", help="Validate and pack an existing wheel without compilation or execution"
    )
    args = parser.parse_args()
    target = Target(args.target)
    output = args.out.resolve()
    built = (
        pack(target, args.tag, output, output / f"wheels-{target.value}")
        if args.pack_only
        else build(target, args.tag, output)
    )
    if not args.pack_only:
        smoke(target, args.tag, output, built)
    print(
        f"staged {target.value}: archive/wheel share {built.contract.binarySha256}; "
        + ("validated" if args.pack_only else "both installed and generated a working Python SDK")
    )


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, zipfile.BadZipFile, tarfile.TarError) as error:
        print(
            f"release-native: {error}; clean staging output and rebuild with the intended --target and Cargo.toml version tag",
            file=sys.stderr,
        )
        sys.exit(1)
