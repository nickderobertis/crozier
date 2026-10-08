# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo CLI driven by just, with no Nx workspace; this documentary evidence script belongs to the linked departure or refusal evaluation and is run explicitly against the committed certified output or an identified generated SDK.
"""Bind the certified output signatures without importing optional dependencies."""
import ast
import inspect
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "openapi-surface" / "handwritten" / "observatory-client-variable" / "fern-expected"
client = ast.parse((ROOT / "src/fern/client.py").read_text(encoding="utf-8"))
cls = next(node for node in client.body if isinstance(node, ast.ClassDef) and node.name == "FernApi")
namespace = {}
for name in ("__init__", "list_signals"):
    method = next(node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == name)
    method.decorator_list = []
    method.returns = None
    for argument in [*method.args.posonlyargs, *method.args.args, *method.args.kwonlyargs]:
        argument.annotation = None
    method.args.defaults = [ast.Constant(None) for _ in method.args.defaults]
    method.args.kw_defaults = [None if value is None else ast.Constant(None) for value in method.args.kw_defaults]
    method.body = [ast.Pass()]
    exec(compile(ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[])), "<certified-signature>", "exec"), namespace)

for name, positional, keywords in (
    ("__init__", (object(),), {"base_url": "https://signals.example.net"}),
    ("list_signals", (object(), object()), {}),
):
    signature = inspect.signature(namespace[name])
    try:
        signature.bind(*positional, **keywords)
    except TypeError as error:
        print(f"{name}: {error}")
    else:
        raise AssertionError(f"{name}: the defective example unexpectedly binds")
print("certified signatures reject both defective calls")
