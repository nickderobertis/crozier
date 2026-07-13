"""Produce a request-relaxed copy of an OpenAPI document for the live mock.

The live e2e proves the generated SDK's *response* handling: it drives every
endpoint against a real Prism mock and asserts the reply deserializes into the
method's declared return type. Prism, however, also validates the *request* and
serves a defined 4xx (or a generated 422) — never reaching the success response —
when the body is absent, a scalar fails a `format`/`pattern`, a required field is
missing, or a security requirement is unmet. The generated example snippets trip
all of these (they omit all-optional bodies, pass placeholder `uuid`/`byte`
strings, never fill a `$ref`-ed request body, and carry only a placeholder token).
Request construction — auth included — is already covered exactly by the wire
tests (`tests/runtime/`), so here we neutralize request-side validation while
leaving every response schema — the thing under test — untouched:

- drop `security` (document-wide and per operation) so the mock never 401s;
- set each operation's `requestBody.required` to `false`;
- replace each request-body media type's `schema` with `{}` (match-anything).

Replacing the request schema (rather than editing it in place) is what makes this
correct for real specs: a request body is usually a `$ref` into
`components.schemas`, and those component schemas are *shared with responses* —
mutating them would weaken the very validation the test relies on. Swapping the
request's own schema pointer for `{}` leaves the shared component, and every
`responses` schema, pristine. Importable (`relax`) and runnable
(`python _relax.py <in> <out>`)."""

import sys

import yaml


def relax(doc):
    """Return `doc` (mutated in place) with request-side validation neutralized."""
    doc.pop("security", None)
    for operations in (doc.get("paths") or {}).values():
        if not isinstance(operations, dict):
            continue
        for operation in operations.values():
            if not isinstance(operation, dict):
                continue
            operation.pop("security", None)
            request_body = operation.get("requestBody")
            if not isinstance(request_body, dict):
                continue
            request_body["required"] = False
            for media_type in (request_body.get("content") or {}).values():
                if isinstance(media_type, dict) and "schema" in media_type:
                    # Match-anything: the mock accepts any body, and the shared
                    # component this used to $ref stays untouched for responses.
                    media_type["schema"] = {}
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
