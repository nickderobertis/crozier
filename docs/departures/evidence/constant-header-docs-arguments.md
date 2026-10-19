# `constant-header-docs-arguments`

**Kind:** `fern-defect`. Fern sends a header whose schema defaults to a string as
that constant and leaves it out of the method, yet its `reference.md` documents
it under the method as an argument.

## The input

[`header-default-constants/openapi.yml`](../../fern-measurements/parameter-lowering/header-default-constants/openapi.yml),
a crozier-authored document whose `GET /beds` declares, beside a required query
parameter, headers with and without defaults: `X-Valve-Mode` (required inline
enum, `default: drip`), `X-Mist-Mode` (optional inline enum, `default: fine`),
`X-Hatch-Mode` (optional nullable enum with a description, `default: down`),
`X-Lamp-Watts` and `X-Fan-Speed` (integer defaults) and `X-Vent-Mode` (a
required enum with none).

## Fern's output

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0; the comment-stripped tree is the document's
`fern-expected/`.

`src/fern/beds/raw_client.py` sends `"X-Valve-Mode": "drip"`, `"X-Mist-Mode":
"fine"` and `"X-Hatch-Mode": "down"` as constants (lines 59–61), and
`list_beds` takes `section`, `lamp_watts`, `vent_mode` and `fan_speed` only.
Yet `reference.md` documents `valve_mode`, `mist_mode` and `hatch_mode` under
the method as `typing.Literal` (lines 68–91).

**Partly fixed at this pair.** At the previous certified pair (Fern CLI 5.67.1,
fern-python-sdk 5.20.0) the worked calls of `README.md` and `reference.md` also
passed `valve_mode="drip"`, `mist_mode="fine"` and `hatch_mode="down"` to
`list_beds`. At 5.41.3 they leave the constants out (`README.md` lines 43–47
and 77–81, `reference.md` lines 24–28), as crozier's do: Fern's `README.md` and
crozier's are identical, and the two `reference.md` files differ only in those
three parameter blocks. The departure, and its rule, now cover only those
blocks.

## Why it is a defect

With a copy of the tree's `src/` on `PYTHONPATH` beside `httpx` 0.28.1 and
`pydantic` 2.14.1 (Python 3.12), passing an argument `reference.md` documents:

```text
$ python -c 'import inspect; from fern import FernApi; print(list(inspect.signature(FernApi().beds.list_beds).parameters))'
['section', 'lamp_watts', 'vent_mode', 'fan_speed', 'request_options']
$ python -c 'from fern import FernApi; from fern.beds import ListBedsRequestXVentMode; FernApi().beds.list_beds(section="section", lamp_watts=1, vent_mode=ListBedsRequestXVentMode.OPEN, valve_mode="drip")'
TypeError: BedsClient.list_beds() got an unexpected keyword argument 'valve_mode'
```

`reference.md` documents arguments the method does not have: docs that
contradict the generated code are a defect under the defect rule. Fern's code —
the constant headers, the method without them — is behaviour, and crozier
matches it.

## crozier's output

crozier writes the same tree but for those lines: its `reference.md` parameter
list leaves the constant headers out. `crozier compare` over the pair matches
and reports this departure once, at the first line of the differing window
(`reference.md:68`); that is the golden's `constant-header-docs-arguments` row
in `tests/fixtures/departures-ledger.tsv`, beside the rows of the corpus goldens
whose operations declare such a header (`letta` `reference.md:21619`, the
`storage_unit` block; `paypal-catalog-products` `reference.md:149`, the
`prefer` block).
`compare_reports_the_parameter_docs_departures_and_fails_on_any_other_difference`
in `crates/crozier-e2e/tests/e2e/compare.rs` drives it, and shows the comparison
failing when one more line of either file differs.
