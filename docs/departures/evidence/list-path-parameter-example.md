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

**Historical.** This record was measured at Fern CLI 5.200.0 /
`fernapi/fern-python-sdk` 5.41.25, the pair certified when it was taken; where it
says "the certified pair" it means that pair. It has not been re-measured at
the current certified pair, Fern CLI 5.216.0 / fern-python-sdk 5.42.0. There
the goldens it cites were regenerated and differ from 5.41.25's only in each
README's Retries section and `.fern/metadata.json`, and the departure's rows in
`tests/fixtures/departures-ledger.tsv` recur on the same lines of Fern's output
(a README row after the Retries section ten lines earlier), so the defective
lines the record shows failing are Fern's at that pair too.

## Aliased lists, maps and unions (#945, #947)

The same defect reaches three more path-parameter shapes, measured on the
registered witness candidate tonik
(`t-unit/tonik/integration_test/simple_encoding/openapi.yaml`, sha256
`30d1f6be…`) and the from-scratch
[`composite-path-parameters`](../../fern-measurements/worked-examples/composite-path-parameters/openapi.yml)
document (tonik measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25;
re-measure both at the certified pair before landing):

- a `$ref` to an array (`string_list: StringList`, `StringList =
  typing.List[str]`) and an inline map (`values: typing.Dict[str, str]`,
  `Dict[str, int]`, `Dict[str, datetime]`): Fern's Markdown calls leave the
  argument out (`client.simple_encoding.test_list_in_path()`), and its
  docstrings pass the string placeholder (`string_list="stringList"`,
  `values="values"`), which neither a `typing.List` nor a map admits;
- a union of object components (`dynamic_value: DynamicCompositeValue`, an
  `anyOf` of three `$ref`s): Fern writes no docstring `Examples` section and
  the Markdown placeholder `client.simple_encoding.test_any_of_composite_in_path(...)`,
  which passes an `Ellipsis` for the required argument.

pyright 1.1.408 (basic mode) over every worked example of Fern's tree,
each against the tree's own `src/`:

```text
s0041_reference.py:8:1 - error: Argument missing for parameter "string_list" (reportCallIssue)
s0045_reference.py:8:1 - error: Argument missing for parameter "values" (reportCallIssue)
s0088_doc.py:5:17 - error: Argument of type "Literal['stringList']" cannot be assigned to parameter "string_list" of type "StringList" in function "test_list_in_path"
s0092_doc.py:5:12 - error: Argument of type "Literal['values']" cannot be assigned to parameter "values" of type "Dict[str, str]" in function "test_map_string_in_path"
s0094_doc.py:5:12 - error: Argument of type "Literal['values']" cannot be assigned to parameter "values" of type "Dict[str, datetime]" in function "test_map_date_time_in_path"
```

crozier passes `string_list=["stringList"]`, `values={"key": "value"}` (with
`import datetime` for the date-time map) and
`dynamic_value=EntityType_Person(first_name="first_name")`, none of which the
same check reports. The region rule admits a docstring's multi-line container
argument only where Fern passes its one-line placeholder at that place, and an
`import datetime` only where the removed value was its snippet's one use; it
admits a union example only where Fern's Markdown snippet is the bare
`client.<path>.<method>(...)` and its docstring for the same method ends at
`Returns`. Unit tests in `src/departures.rs` hold each.
