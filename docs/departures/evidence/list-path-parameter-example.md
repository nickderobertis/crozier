# List-typed path parameters in worked calls

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

A path parameter whose schema is an array becomes a required method parameter
typed `typing.Sequence[...]`. Across the 1308 trees the golden comparisons
read, 21 methods in 5 trees take one: `daniweb-connect` (15, `Sequence[int]`),
`gambitcomm.local-mimic` (1 `Sequence[str]`, 2 `Sequence[Sequence[str]]`),
`braintrust-dev` (1) and the `matrix-array` and `label-array-or-object` probes
(1 each, `Sequence[str]`).

**Markdown.** Fern's `README.md` and `reference.md` calls leave the argument
out. The `matrix-array` probe's golden writes `client.probe()` (`README.md`
line 42, `reference.md` line 22) for `def probe(self, probe_param:
typing.Sequence[str], ...)`. On the golden's own SDK:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'docs/openapi-surface/probe-expected/matrix-array/src')
from fern import FernApi
FernApi().probe()"
TypeError: FernApi.probe() missing 1 required positional argument: 'probe_param'
```

**Docstrings.** Fern's docstring passes the parameter's string placeholder.
For a list of strings that is a `typing.Sequence[str]`, and stays. For
`daniweb-connect`'s `id: typing.Sequence[int]` it writes `id="ID"`
(`src/fern/users/client.py` line 470), which the SDK's own validation library
refuses for that type:

```text
$ python -B -c "
import typing, pydantic
pydantic.TypeAdapter(typing.Sequence[int]).validate_python('ID')"
pydantic_core._pydantic_core.ValidationError: 1 validation error ...
  'str' instances are not allowed as a Sequence value [type=sequence_str, input_value='ID', input_type=str]
```

crozier passes the argument in every call: Fern's string placeholder where the
items are strings (`probe_param="probeParam"`, as Fern's docstring does), else
a one-item list of the item's example (`id=[1]`). The region rule admits a
Markdown call only where crozier's call without that one argument's lines (and
closed on its opening line when nothing else is left) is Fern's call, the
argument being a list-typed positional parameter crozier's client declares; the
line rule admits a docstring line only where Fern passes a string and crozier a
list for such a parameter whose items are not strings. The unit test rejects
another parameter, an extra change, a non-client call and a list of strings;
the departures ledger pins every occurrence.
