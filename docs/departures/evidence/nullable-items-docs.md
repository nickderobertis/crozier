# `nullable-items-docs`

**Kind:** `fern-defect`. Fern's signature drops the `Optional` of a query
parameter's nullable array items, while its `reference.md` keeps it and its
worked calls pass `None` items.

## The input

[`query-nullable-30/openapi.yml`](../../fern-measurements/parameter-lowering/query-nullable-30/openapi.yml)
and its OpenAPI 3.1 twin
[`query-nullable-31/openapi.yml`](../../fern-measurements/parameter-lowering/query-nullable-31/openapi.yml),
crozier-authored documents whose `GET /beds` takes array query parameters over
nullable items (`crops`, optional; `rows` and `trays`, required) — `nullable:
true` in the first, `type: [T, "null"]` in the second — beside a `pots` array
over plain integers.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, generated as
[`constant-header-docs-arguments`](constant-header-docs-arguments.md#fern-s-output)
describes, exits 0 on both; the comment-stripped trees are each document's
`fern-expected/`. The signature types `rows` as
`typing.Optional[typing.Union[int, typing.Sequence[int]]]`, and the docstring
example passes `rows=[]`. But `reference.md` documents `crops`, `rows` and
`trays` as `typing.Optional[typing.Union[typing.Optional[int],
typing.Sequence[typing.Optional[int]]]]` (lines 67, 75, 83), and the worked calls
of `README.md` and `reference.md` pass `rows=[None]` and `trays=[None]`, where
`pots`, over plain integers, gets `[1]`.

## Why it is a defect

With the tree's `src/` on `MYPYPATH` (a copy), and `typed_call.py` holding the
README's call:

```text
$ python -c 'import inspect; from fern import FernApi; print(inspect.signature(FernApi().beds.list_beds).parameters["rows"].annotation)'
int | typing.Sequence[int] | None
$ cat typed_call.py
from fern.beds.client import BedsClient


def readme_call(beds: BedsClient) -> None:
    beds.list_beds(soil="soil", rows=[None], trays=[None], shade="shade", pots=[1])
$ mypy --ignore-missing-imports typed_call.py | grep typed_call
typed_call.py:5: error: List item 0 has incompatible type "None"; expected "int"  [list-item]
typed_call.py:5: error: List item 0 has incompatible type "None"; expected "str"  [list-item]
```

`reference.md` documents a type the method does not have, and the documented
call passes values its signature rejects: docs and examples that contradict the
generated code are a defect under the defect rule. The signature, and the
docstring's `[]`, are behaviour, and crozier matches them.

## crozier's output

crozier's `reference.md` documents the signature's own type, and its worked
calls pass the element Fern passes for items without `nullable`
(`rows=[1]`, `trays=["trays"]`). `crozier compare` over each pair matches and
reports this departure once per file, at the first line of the differing window
(`README.md:45`, `reference.md:26`); those are the goldens'
`nullable-items-docs` rows in `tests/fixtures/departures-ledger.tsv`, and
`compare_reports_the_parameter_docs_departures_and_fails_on_any_other_difference`
in `tests/e2e/compare.rs` drives it.
