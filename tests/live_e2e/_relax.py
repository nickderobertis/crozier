"""Produce a request-relaxed copy of an OpenAPI document for the live mock.

The live e2e proves the generated SDK's *response* handling: it drives every
endpoint against a real Prism mock and asserts the reply deserializes into the
method's declared return type. Prism, however, also validates the *request* and
returns a 422 (never reaching a response) when a body is absent or a scalar does
not satisfy a `format`/`pattern` — and Fern's own generated example snippets do
exactly that (they omit all-optional bodies and pass placeholder strings for
`uuid`/`byte` fields). Request construction is already covered exactly by the
differential wire tests (`tests/runtime/`), so here we loosen only the request
side and leave every response schema — the thing under test — untouched:

- each operation's `requestBody.required` becomes `false`;
- inside request-body schemas, `format`/`pattern` and object `required` lists are
  dropped.

Nothing under `responses` is modified, so the mock still serves spec-shaped
bodies that the SDK must parse. Importable (`relax`) and runnable
(`python _relax.py <in> <out>`)."""

import sys

import yaml


def _strip_request_constraints(node):
    """Recursively drop request-side validation keywords Prism would enforce on
    the way in (`format`, `pattern`, and an object schema's `required` list),
    leaving response schemas — reached separately — pristine."""
    if isinstance(node, dict):
        node.pop("format", None)
        node.pop("pattern", None)
        if node.get("type") == "object":
            node.pop("required", None)
        for value in node.values():
            _strip_request_constraints(value)
    elif isinstance(node, list):
        for value in node:
            _strip_request_constraints(value)


def relax(doc):
    """Return `doc` (mutated in place) with request-body validation loosened."""
    for operations in (doc.get("paths") or {}).values():
        if not isinstance(operations, dict):
            continue
        for operation in operations.values():
            if not isinstance(operation, dict):
                continue
            request_body = operation.get("requestBody")
            if not isinstance(request_body, dict):
                continue
            request_body["required"] = False
            for media_type in (request_body.get("content") or {}).values():
                if isinstance(media_type, dict) and "schema" in media_type:
                    _strip_request_constraints(media_type["schema"])
    return doc


def main():
    if len(sys.argv) != 3:
        print("usage: python _relax.py <spec-in> <spec-out>", file=sys.stderr)
        sys.exit(2)
    with open(sys.argv[1]) as handle:
        doc = yaml.safe_load(handle)
    with open(sys.argv[2], "w") as handle:
        yaml.safe_dump(relax(doc), handle, sort_keys=False)


if __name__ == "__main__":
    main()
