# llmlint: ignore[new_code_lands_in_a_project] This Cargo/just repository has no Nx graph. The real sdk_env_pattern_narrowed_evidence_validates_certified_examples_and_recovers journey runs this checker through the existing just test-sdk-env tier.
"""Validate the certified pattern-narrowing example fault without sending requests."""

import argparse
import ast
import importlib
from pathlib import Path
import re
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk", type=Path, help="complete certified SDK directory")
    parser.add_argument("source", type=Path, help="measurement-phase OpenAPI document")
    args = parser.parse_args()
    if not (args.sdk / "src/fern/__init__.py").is_file():
        parser.error(f"{args.sdk}: no certified src/fern/__init__.py; supply the complete SDK")
    if not args.source.is_file():
        parser.error(f"{args.source}: source file missing; supply measurement-phase/openapi.yml")

    try:
        import jsonschema
        import yaml
    except ImportError as error:
        parser.error(f"{error}; install the certified SDK requirements, jsonschema==4.26.0 and PyYAML==6.0.3, then rerun")

    try:
        source = yaml.safe_load(args.source.read_text(encoding="utf-8"))
        schemas = source["components"]["schemas"]
        prop = schemas["Measurement"]["properties"]["phase"]
        members = prop["allOf"]
        if not isinstance(members, list) or len(members) != 2:
            raise ValueError("phase must have exactly two allOf members")
        if members[0].get("$ref") != "#/components/schemas/Phase":
            raise ValueError("phase's first member must reference Phase")
        constraint = {"allOf": [schemas["Phase"], members[1]]}
        jsonschema.Draft202012Validator.check_schema(constraint)
        validator = jsonschema.Draft202012Validator(constraint)
    except (OSError, KeyError, TypeError, AttributeError, ValueError, yaml.YAMLError, jsonschema.SchemaError) as error:
        parser.error(f"{args.source}: invalid narrowing proof source: {error}; restore the certified source")

    sys.dont_write_bytecode = True
    sys.path.insert(0, str(args.sdk / "src"))
    try:
        package = importlib.import_module("fern")
    except (ImportError, SyntaxError, NameError, AttributeError) as error:
        parser.error(f"{args.sdk}: certified entry point failed to import: {error}; verify the complete tree and install its declared dependencies")
    count = 0
    for name in ["README.md", "reference.md", "src/fern/client.py"]:
        try:
            text = (args.sdk / name).read_text(encoding="utf-8")
            if name.endswith(".py"):
                snippets = []
                for function in ast.walk(ast.parse(text)):
                    if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    doc = ast.get_docstring(function) or ""
                    if "Examples\n" in doc:
                        snippets.append(doc.split("Examples\n", 1)[1].lstrip("-\n"))
            else:
                snippets = re.findall(r"```python\s*\n(.*?)```", text, re.S)
            for snippet in snippets:
                for node in ast.walk(ast.parse(snippet)):
                    if not isinstance(node, ast.keyword) or node.arg != "phase":
                        continue
                    value_node = node.value
                    if isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                        value = value_node.value
                    elif isinstance(value_node, ast.Attribute) and isinstance(value_node.value, ast.Name):
                        value = getattr(getattr(package, value_node.value.id), value_node.attr).value
                    else:
                        raise ValueError(f"unsupported phase expression: {ast.unparse(value_node)}")
                    if value != "preparation" or not list(validator.iter_errors(value)):
                        raise ValueError(f"phase={value!r} does not demonstrate the certified invalid default")
                    count += 1
        except (OSError, SyntaxError, AttributeError, ValueError) as error:
            parser.error(f"{args.sdk / name}: invalid certified example evidence: {error}; regenerate the complete certified tree")
    if count != 8:
        parser.error(f"{args.sdk}: expected 8 invalid phase arguments, found {count}; regenerate the complete certified tree")
    try:
        validator.validate("recording")
    except jsonschema.ValidationError as error:
        parser.error(f"{args.source}: replacement recording is invalid: {error.message}; restore the certified source")
    print(f"{args.sdk.name}: imported certified entry point; {count} generated phase arguments rejected; recording accepted")


if __name__ == "__main__":
    main()
