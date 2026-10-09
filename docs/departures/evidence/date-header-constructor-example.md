# Date header constructor example

The independently authored [date-header document](../../openapi-surface/handwritten/observatory-client-date/openapi.yml) promotes an optional date header. Its complete certified CLI 5.67.1 / Python SDK 5.20.0 output annotates `sampling_day` as `typing.Optional[dt.date]`, but supplies `"YOUR_SAMPLING_DAY"` in constructor examples. That value is invalid for the schema's `format: date`.

Run `python3 docs/departures/evidence/date-header-constructor-example.py`: the script extracts the placeholder from the unedited certified output and proves it fails date validation. The replacement passes. Its form and default value come from the certified [observation-date output](../../openapi-surface/handwritten/skyglass-observation-date/fern-expected/src/fern/client.py), which renders `datetime.date.fromisoformat("2023-01-15")`.

## Type-checking the certified example against the certified SDK

The certified SDK pins `mypy==1.13.0` in its own `pyproject.toml`. Install the
unedited certified tree (a copy of `fern-expected/` as `sdk/`) into a fresh
venv beside that mypy, so its `py.typed` package is checked as a dependency and
only the example call is reported. `certified_call.py` is the constructor
example exactly as the certified docstrings and README emit it;
`crozier_call.py` is the same call with crozier's replacement value:

```text
$ uv venv .venv && uv pip install --python .venv ./sdk mypy==1.13.0
$ cat certified_call.py
from fern import FernApi

client = FernApi(
    sampling_day="YOUR_SAMPLING_DAY",
)
$ cat crozier_call.py
import datetime

from fern import FernApi

client = FernApi(
    sampling_day=datetime.date.fromisoformat("2023-01-15"),
)
$ .venv/bin/mypy certified_call.py; echo "exit $?"
certified_call.py:4: error: Argument "sampling_day" to "FernApi" has incompatible type "str"; expected "date | None"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
exit 1
$ .venv/bin/mypy crozier_call.py; echo "exit $?"
Success: no issues found in 1 source file
exit 0
```

(Python 3.14.7, mypy 1.13.0.) The certified example does not type-check against
the certified SDK's own `FernApi.__init__` annotation; the replacement does.

The parity rule applies only to Python constructor examples whose parameter is annotated as an optional date. String-header placeholders and unrelated differences are not normalized; a neighboring unexplained change still fails the regression test.
