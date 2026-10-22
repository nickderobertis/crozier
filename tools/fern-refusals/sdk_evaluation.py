"""Produce and validate a versioned, linked SDK evaluation without invoking Fern."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from pathlib import Path
from typing import (
    Literal,
    NewType,
    Protocol,
    TypedDict,
    cast,
    get_args,
    get_origin,
    get_type_hints,
    is_typeddict,
    overload,
)

Sha256 = NewType("Sha256", str)
PACKAGE = "limitation_sdk"
DISTRIBUTION = "limitation-sdk"


class Distribution(TypedDict):
    name: str
    version: str
    sha256: Sha256


class Environment(TypedDict):
    executable: str
    executable_sha256: Sha256
    prefix: str
    base_prefix: str
    python_version: str
    configuration_sha256: Sha256
    distributions: list[Distribution]


class RuntimeSnapshot(TypedDict):
    distribution_sha256: Sha256
    environment: Environment
    environment_sha256: Sha256


class ImportSnapshot(RuntimeSnapshot):
    modules: list[str]
    modules_sha256: Sha256


class LinkedStage(TypedDict):
    command: list[str]
    exit: Literal[0]
    output: str
    input_sha256: Sha256
    output_sha256: Sha256


class EnvironmentStage(LinkedStage):
    environment: Environment
    environment_sha256: Sha256


class ImportStage(EnvironmentStage):
    modules: list[str]


class SdkEvaluation(TypedDict):
    schema_version: Literal[2]
    document_sha256: Sha256
    fern_cli: str
    fern_python_sdk: str
    crozier_commit: str
    crozier_binary_sha256: Sha256
    sdk_sha256: Sha256
    package_name: str
    validation: LinkedStage
    default_generation: LinkedStage
    strict_generation: LinkedStage
    build: LinkedStage
    installation: EnvironmentStage
    imports: ImportStage


class Schema(TypedDict, total=False):
    type: Literal["object", "array", "string", "integer"]
    enum: list[object]
    properties: dict[str, Schema]
    required: list[str]
    additionalProperties: Literal[False]
    items: Schema
    pattern: str


class TypedRecord(Protocol):
    @property
    def __required_keys__(self) -> frozenset[str]: ...


def schema_for(annotation: object) -> Schema:
    """Derive the closed JSON contract from the models used after validation."""
    if annotation is Sha256:
        return {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    if annotation is str:
        return {"type": "string"}
    if annotation is int:
        return {"type": "integer"}
    if get_origin(annotation) is Literal:
        values = list(get_args(annotation))
        return {"type": "integer" if type(values[0]) is int else "string", "enum": values}
    if get_origin(annotation) is list:
        return {"type": "array", "items": schema_for(get_args(annotation)[0])}
    if is_typeddict(annotation):
        # is_typeddict verifies this runtime descriptor; the typing stubs do
        # not narrow its metaclass to the required-keys interface.
        record = cast(TypedRecord, annotation)
        return {
            "type": "object",
            "properties": {key: schema_for(value) for key, value in get_type_hints(annotation).items()},
            "required": sorted(record.__required_keys__),
            "additionalProperties": False,
        }
    raise ValueError(f"unsupported SDK evidence annotation: {annotation!r}")


def structural_errors(value: object, schema: Schema, where: str = "SDK evidence") -> list[str]:
    kind = schema["type"]
    if kind == "object":
        if not isinstance(value, dict):
            return [f"{where}: expected an object"]
        properties = schema["properties"]
        missing = set(schema["required"]) - value.keys()
        extra = value.keys() - properties.keys()
        if missing or extra:
            return [f"{where}: missing fields {sorted(missing)}; unexpected fields {sorted(map(str, extra))}"]
        return [
            error
            for key, child in properties.items()
            for error in structural_errors(value[key], child, f"{where}.{key}")
        ]
    if kind == "array":
        if not isinstance(value, list):
            return [f"{where}: expected an array"]
        return [
            error
            for index, item in enumerate(value)
            for error in structural_errors(item, schema["items"], f"{where}[{index}]")
        ]
    if (kind == "integer" and type(value) is not int) or (kind == "string" and not isinstance(value, str)):
        return [f"{where}: expected {kind}"]
    if "enum" in schema and value not in schema["enum"]:
        return [f"{where}: expected one of {schema['enum']}"]
    if "pattern" in schema and (not isinstance(value, str) or re.fullmatch(schema["pattern"], value) is None):
        return [f"{where}: invalid SHA-256"]
    return []


def canonical_digest(value: object) -> Sha256:
    return Sha256(
        hashlib.sha256(
            json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        ).hexdigest()
    )


def file_digest(path: Path) -> Sha256:
    return Sha256(hashlib.sha256(path.read_bytes()).hexdigest())


def files_digest(entries: Iterable[tuple[str, Path]]) -> Sha256:
    """Hash a framed manifest of file names and raw-byte hashes, including binary files."""
    manifest = sorted((name, file_digest(path)) for name, path in entries)
    if not manifest or len({name for name, _digest in manifest}) != len(manifest):
        raise ValueError("artifact file manifest must be nonempty with unique names")
    return canonical_digest(manifest)


def tree_digest(root: Path) -> Sha256:
    files = [
        path for path in root.rglob("*") if path.is_file() and path.suffix != ".pyc" and "__pycache__" not in path.parts
    ]
    if any(path.is_symlink() for path in files):
        raise ValueError(f"generated SDK contains a symlink under {root}")
    return files_digest((path.relative_to(root).as_posix(), path) for path in files)


def normalized_distribution(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def validate_evaluation(value: object, digest: str, cli: str, sdk: str) -> list[str]:
    errors = structural_errors(value, schema_for(SdkEvaluation))
    if errors:
        return errors
    # The complete shape and every nested value were checked against the schema
    # derived from this TypedDict, rather than a second handwritten contract.
    data = cast(SdkEvaluation, value)
    if data["document_sha256"] != digest or (data["fern_cli"], data["fern_python_sdk"]) != (cli, sdk):
        errors.append("SDK evidence has the wrong document or certified pair")
    if re.fullmatch(r"[0-9a-f]{40}", data["crozier_commit"]) is None:
        errors.append("SDK evidence has an invalid crozier commit")
    if data["package_name"] != PACKAGE:
        errors.append("SDK evidence names a package the native evaluator does not generate")
    validation = data["validation"]
    default = data["default_generation"]
    strict = data["strict_generation"]
    build = data["build"]
    installation = data["installation"]
    imports = data["imports"]
    links = [
        ("validation input", validation["input_sha256"], digest),
        ("validation output", validation["output_sha256"], digest),
        ("default generation input", default["input_sha256"], validation["output_sha256"]),
        ("strict generation input", strict["input_sha256"], validation["output_sha256"]),
        ("default/strict generated tree", default["output_sha256"], strict["output_sha256"]),
        ("generated tree", data["sdk_sha256"], strict["output_sha256"]),
        ("build input", build["input_sha256"], strict["output_sha256"]),
        ("installation input", installation["input_sha256"], build["output_sha256"]),
        ("imports input", imports["input_sha256"], installation["output_sha256"]),
        ("import environment", imports["environment_sha256"], installation["environment_sha256"]),
        ("imported module list", imports["output_sha256"], canonical_digest(imports["modules"])),
    ]
    for label, actual, expected in links:
        if actual != expected:
            errors.append(f"SDK evidence {label} digest does not match its preceding artifact")
    for label, stage in (("installation", installation), ("imports", imports)):
        environment = stage["environment"]
        if canonical_digest(environment) != stage["environment_sha256"]:
            errors.append(f"SDK evidence {label} environment digest does not match its manifest")
        names = [entry["name"] for entry in environment["distributions"]]
        if names != sorted(set(names)):
            errors.append(f"SDK evidence {label} distribution manifest is not unique and sorted")
        installed = [entry for entry in environment["distributions"] if entry["name"] == DISTRIBUTION]
        if len(installed) != 1 or installed[0]["sha256"] != installation["output_sha256"]:
            errors.append(f"SDK evidence {label} does not identify the installed SDK distribution")
        if not all(environment[key] for key in ("executable", "prefix", "base_prefix", "python_version")):
            errors.append(f"SDK evidence {label} omits its interpreter or environment")
    if (
        imports["modules"] != sorted(set(imports["modules"]))
        or PACKAGE not in imports["modules"]
        or any(name != PACKAGE and not name.startswith(PACKAGE + ".") for name in imports["modules"])
    ):
        errors.append("SDK evidence must import every discovered module of its generated package")
    for label, stage in (
        ("validation", validation),
        ("default_generation", default),
        ("strict_generation", strict),
        ("build", build),
        ("installation", installation),
        ("imports", imports),
    ):
        if not stage["command"] or any(not argument for argument in stage["command"]):
            errors.append(f"SDK evidence {label} has no recorded command")
    return errors


def _run(
    command: list[str], work: Path, label: str, timeout: int, env: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            command,
            cwd=work,
            env=env,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ValueError(
            f"{label} could not run: {error}; repair the executable or timeout and retry in a fresh work directory"
        ) from error
    (work / f"{label}.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise ValueError(
            f"{label} failed with exit {result.returncode}:\n{result.stdout}{result.stderr}\nFix the reported error and retry in a fresh work directory"
        )
    return result


def _stage(
    command: list[str], result: subprocess.CompletedProcess[str], input_digest: Sha256, output_digest: Sha256
) -> LinkedStage:
    return {
        "command": command,
        "exit": 0,
        "output": result.stdout + result.stderr,
        "input_sha256": input_digest,
        "output_sha256": output_digest,
    }


def _python(environment: Path) -> Path:
    return environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


@overload
def _snapshot(result: subprocess.CompletedProcess[str], imports: Literal[True]) -> ImportSnapshot: ...


@overload
def _snapshot(result: subprocess.CompletedProcess[str], imports: Literal[False] = False) -> RuntimeSnapshot: ...


def _snapshot(result: subprocess.CompletedProcess[str], imports: bool = False) -> RuntimeSnapshot | ImportSnapshot:
    try:
        value: object = json.loads(result.stdout)
    except ValueError as error:
        raise ValueError("runtime inspection did not produce JSON; inspect its log and repair the SDK") from error
    errors = structural_errors(value, schema_for(ImportSnapshot if imports else RuntimeSnapshot))
    if errors:
        raise ValueError("; ".join(errors))
    # The native inspector's closed payload is validated by its own model.
    return cast(ImportSnapshot, value) if imports else cast(RuntimeSnapshot, value)


def produce(
    document: Path, crozier: Path, work: Path, output: Path, repo: Path, cli: str, sdk: str, timeout: int
) -> None:
    document = document.resolve()
    crozier = crozier.resolve()
    work = work.resolve()
    output = output.resolve()
    if not document.is_file():
        raise ValueError(f"source file missing: {document}; supply an OpenAPI file")
    if not crozier.is_file():
        raise ValueError(f"crozier executable missing: {crozier}; build crozier first")
    if output in {document, crozier}:
        raise ValueError("evidence output would overwrite an input; choose a separate JSON file")
    if work.exists():
        raise ValueError(f"evaluation work directory already exists: {work}; choose a fresh directory")
    uv = shutil.which("uv")
    if uv is None:
        raise ValueError("uv is missing from PATH; install uv and retry")
    source_digest = file_digest(document)
    binary_digest = file_digest(crozier)
    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    work.mkdir(parents=True)
    env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_")}
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    env.update(PYTHONNOUSERSITE="1", UV_NO_PROGRESS="1")
    build_environment = work / "build-environment"
    runtime_environment = work / "runtime-environment"
    for label, environment in (("build", build_environment), ("runtime", runtime_environment)):
        _run([uv, "venv", "--python", sys.executable, str(environment)], work, f"prepare-{label}", timeout, env)
    build_python = _python(build_environment)
    runtime_python = _python(runtime_environment)
    ruff = (repo / ".ruff-version").read_text(encoding="utf-8").strip()
    _run(
        [
            uv,
            "pip",
            "install",
            "--python",
            str(build_python),
            "build==1.6.1",
            "poetry-core==2.5.0",
            "openapi-spec-validator==0.9.0",
            f"ruff=={ruff}",
        ],
        work,
        "prepare-dependencies",
        timeout,
        env,
    )
    env["PATH"] = str(build_python.parent) + os.pathsep + env.get("PATH", "")
    validation_command = [str(build_python), "-m", "openapi_spec_validator", str(document)]
    validation_result = _run(validation_command, work, "validation", timeout, env)
    validation = _stage(validation_command, validation_result, source_digest, file_digest(document))
    generations: dict[str, LinkedStage] = {}
    for label, strict in (("default_generation", False), ("strict_generation", True)):
        target = work / label
        command = [
            str(crozier),
            "generate",
            "python",
            "--no-config",
            "--spec",
            str(document),
            "--output",
            str(target),
            "--package-name",
            PACKAGE,
            "--project-name",
            DISTRIBUTION,
        ]
        if strict:
            command.append("--fern-strict")
        input_digest = file_digest(document)
        result = _run(command, work, label, timeout, env)
        generations[label] = _stage(command, result, input_digest, tree_digest(target))
    generated = work / "strict_generation"
    dist = work / "dist"
    build_command = [
        str(build_python),
        "-m",
        "build",
        "--wheel",
        "--no-isolation",
        str(generated),
        "--outdir",
        str(dist),
    ]
    input_tree_digest = tree_digest(generated)
    build_result = _run(build_command, work, "build", timeout, env)
    if tree_digest(generated) != input_tree_digest:
        raise ValueError("building mutated the generated SDK; inspect the build log before retrying")
    wheels = list(dist.glob("*.whl"))
    if len(wheels) != 1:
        raise ValueError("build did not produce exactly one wheel; inspect build.log")
    wheel = wheels[0]
    build = _stage(build_command, build_result, input_tree_digest, file_digest(wheel))
    installation_command = [uv, "pip", "install", "--python", str(runtime_python), "pydantic==2.14.1", str(wheel)]
    wheel_input_digest = file_digest(wheel)
    installation_result = _run(installation_command, work, "installation", timeout, env)
    inspector = Path(__file__).with_name("sdk_evaluation_runtime.py")
    inspect_command = [str(runtime_python), str(inspector), "inspect", DISTRIBUTION, PACKAGE]
    installed = _snapshot(_run(inspect_command, work, "installed-environment", timeout, env))
    installation: EnvironmentStage = {
        **_stage(installation_command, installation_result, wheel_input_digest, installed["distribution_sha256"]),
        "environment": installed["environment"],
        "environment_sha256": installed["environment_sha256"],
    }
    import_command = [str(runtime_python), str(inspector), "imports", DISTRIBUTION, PACKAGE]
    imported_raw = _run(import_command, work, "imports", timeout, env)
    imported = _snapshot(imported_raw, imports=True)
    imports: ImportStage = {
        **_stage(import_command, imported_raw, imported["distribution_sha256"], imported["modules_sha256"]),
        "environment": imported["environment"],
        "environment_sha256": imported["environment_sha256"],
        "modules": imported["modules"],
    }
    evidence: SdkEvaluation = {
        "schema_version": 2,
        "document_sha256": source_digest,
        "fern_cli": cli,
        "fern_python_sdk": sdk,
        "crozier_commit": commit,
        "crozier_binary_sha256": binary_digest,
        "sdk_sha256": generations["strict_generation"]["output_sha256"],
        "package_name": PACKAGE,
        "validation": validation,
        "default_generation": generations["default_generation"],
        "strict_generation": generations["strict_generation"],
        "build": build,
        "installation": installation,
        "imports": imports,
    }
    errors = validate_evaluation(evidence, source_digest, cli, sdk)
    if errors:
        raise ValueError("; ".join(errors))
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output.parent, prefix=".sdk-evaluation-", newline="\n", delete=False
        ) as handle:
            temporary = Path(handle.name)
            json.dump(evidence, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def evaluate(args: argparse.Namespace, repo: Path, cli: str, sdk: str) -> int:
    try:
        if not args.document.is_file():
            raise ValueError(f"source file missing: {args.document}; supply an OpenAPI file")
        digest = file_digest(args.document)
        output = args.output or repo / "docs/openapi-surface/fern-refusals/limitations" / f"{digest}.json"
        produce(args.document, args.crozier, args.work_dir, output, repo, cli, sdk, args.timeout)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"SDK evaluation: {error}; repair the reported input and rerun evaluate-sdk", file=sys.stderr)
        return 1
    print(f"SDK evaluation: wrote {output}")
    return 0


def verify(args: argparse.Namespace, cli: str, sdk: str) -> int:
    try:
        digest = file_digest(args.document)
        value: object = json.loads(args.evidence.read_text(encoding="utf-8"))
        errors = validate_evaluation(value, digest, cli, sdk)
    except (OSError, ValueError) as error:
        errors = [str(error)]
    for error in errors:
        print(f"SDK evaluation: {error}; regenerate with evaluate-sdk", file=sys.stderr)
    return 1 if errors else 0
