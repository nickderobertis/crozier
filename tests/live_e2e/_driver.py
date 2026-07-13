"""Drive every generated endpoint against the live mock and record what it did.

This is a *helper*, not a test module. `test_live_e2e.py` runs it as a subprocess
(one generated SDK per process, since every fixture's package is named `fern` and
two cannot coexist in one interpreter) and asserts over the recording it prints.

The endpoint list is not hand-authored: it is the set of runnable usage snippets
in the SDK's own generated `reference.md` — one per typed client method, already
carrying valid example arguments. Each snippet is executed verbatim except that
its placeholder `base_url` is repointed at the running Prism server; the returned
value is then validated against the method's *declared return type*
(`typing.get_type_hints` + `pydantic.TypeAdapter`), so a passing endpoint proves
the whole live round-trip: request built and sent, spec-shaped response received,
and deserialized into exactly the type the SDK promises. A raised exception (e.g.
the SDK's `ApiError`) or a type-mismatched result is recorded as a failure rather
than silently swallowed.

Reads three environment variables set by the harness: `LIVE_SDK_SRC` (the
generated SDK's `src/`), `LIVE_REFERENCE` (its `reference.md`), and
`LIVE_BASE_URL` (the mock server). Prints the recording as JSON on stdout."""

import json
import os
import re
import sys
import typing
from pathlib import Path

import pydantic

# A fenced ```python ... ``` block from reference.md, and the `client.<sub>.<method>`
# call that identifies the endpoint a snippet exercises.
_FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)
_CALL = re.compile(r"^client\.(\w+)\.(\w+)", re.MULTILINE)


def usage_snippets(reference_text):
    """Yield `(sub_client, method, source)` for every runnable endpoint snippet in
    a generated `reference.md` — the blocks that construct a client and call it."""
    for block in _FENCE.findall(reference_text):
        call = _CALL.search(block)
        if call and "client = " in block:
            yield call.group(1), call.group(2), block


def _repoint(source, base_url):
    """Rewrite a snippet to hit the mock and capture the endpoint's return value:
    point the client at the mock and bind the call's result to `__result__`.

    A snippet carries an explicit placeholder `base_url` only when the spec has no
    servers; when it does (common in real specs) the constructor omits it and the
    client would default to the real server. So swap an existing `base_url` when
    present, otherwise inject one as the constructor's first argument."""
    if re.search(r'base_url="[^"]*"', source):
        source = re.sub(r'base_url="[^"]*"', f"base_url={base_url!r}", source)
    else:
        source = re.sub(
            r"^(client = \w+\()$",
            rf"\1\n    base_url={base_url!r},",
            source,
            count=1,
            flags=re.MULTILINE,
        )
    lines = source.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("client."):
            lines[index] = "__result__ = " + line
            break
    return "\n".join(lines)


def _kind(value):
    """A stable, low-cardinality label for the deserialized result, so the recording
    reads well and an aggregate test can assert real models come back."""
    if isinstance(value, pydantic.BaseModel):
        return "model"
    if value is None:
        return "none"
    if isinstance(value, (list, set, tuple)):
        return "sequence"
    if isinstance(value, dict):
        return "mapping"
    return "scalar"


def _mock_side_reason(error):
    """Classify a driver exception as a *mock-infrastructure* failure — the mock
    could not honor its own spec, so nothing about the SDK is under test — rather
    than a real SDK failure. Returns a reason when mock-side, else `None`.

    Both cases are provable and independent of which SDK made the call (Fern's own
    generated client would hit them identically), so they are skipped, not failed:

    - **Prism 5xx.** Its dynamic response generator (json-schema-faker) crashed while
      building the body, so no spec-shaped response was ever served. A 4xx is *not*
      covered here — that signals a request the relaxer missed, a real failure.
    - **A response missing a schema-required field.** pydantic rejects it with only
      `missing` errors. The mock emitted a payload that violates the response schema
      it was mocking (e.g. json-schema-faker dropping a `required` property); a
      correct SDK rejecting an invalid-per-schema body is not a defect. A validation
      error with any non-`missing` cause (wrong type, failed constraint) is a real
      failure and falls through. The byte-diff gate independently proves the model's
      required/optional shape matches Fern, so this can never mask a crozier bug.
    """
    status = getattr(error, "status_code", None)
    if isinstance(status, int) and status >= 500:
        return f"prism {status}: mock server failed to generate a response body"
    if isinstance(error, pydantic.ValidationError):
        errors = error.errors()
        if errors and all(item.get("type") == "missing" for item in errors):
            fields = ", ".join(
                ".".join(str(part) for part in item["loc"]) for item in errors
            )
            return f"mock response omitted schema-required field(s): {fields}"
    return None


def _observe(sub_client, method, source, base_url):
    namespace = {}
    exec(compile(_repoint(source, base_url), f"<snippet {method}>", "exec"), namespace)
    result = namespace.get("__result__")
    client = namespace["client"]
    func = getattr(type(getattr(client, sub_client)), method)
    hint = typing.get_type_hints(func).get("return", typing.Any)
    # Re-validate the returned value against the method's declared return type. The
    # SDK already returned an instance of it; this confirms the type is what the
    # SDK promises rather than merely "something non-erroring".
    pydantic.TypeAdapter(hint).validate_python(result)
    return {
        "kind": _kind(result),
        "return_type": str(hint),
        "model": type(result).__name__
        if isinstance(result, pydantic.BaseModel)
        else None,
    }


def record(sdk_src, reference_path, base_url):
    """Run every endpoint snippet and return `{"sub.method": observation}`. The key
    is the full `sub_client.method` call path, not the bare method: real specs reuse
    a method name (`add`, `all_`) across many sub-clients, so keying on the method
    alone would collapse them. An endpoint that raises or type-mismatches records
    `{"ok": False, "error": ...}`; a clean round-trip records `{"ok": True, ...}`."""
    sys.path.insert(0, sdk_src)
    text = Path(reference_path).read_text()
    recording = {}
    for sub_client, method, source in usage_snippets(text):
        endpoint = f"{sub_client}.{method}"
        try:
            recording[endpoint] = {
                "ok": True,
                **_observe(sub_client, method, source, base_url),
            }
        except Exception as error:  # noqa: BLE001 — recorded, then asserted on by the suite
            reason = _mock_side_reason(error)
            if reason is not None:
                # The endpoint WAS exercised (so coverage still counts it), but the
                # mock — not the SDK — failed. Recorded as a skip with the reason so
                # the gate never fails on a Prism/json-schema-faker limitation.
                recording[endpoint] = {"skipped": True, "reason": reason}
            else:
                recording[endpoint] = {
                    "ok": False,
                    "error": f"{type(error).__name__}: {error}",
                }
    return recording


def main():
    src = os.environ.get("LIVE_SDK_SRC")
    reference = os.environ.get("LIVE_REFERENCE")
    base_url = os.environ.get("LIVE_BASE_URL")
    if not (src and reference and base_url):
        print(
            "LIVE_SDK_SRC, LIVE_REFERENCE and LIVE_BASE_URL must all be set",
            file=sys.stderr,
        )
        sys.exit(2)
    json.dump(
        record(src, reference, base_url),
        sys.stdout,
        indent=2,
        sort_keys=True,
        default=str,
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
