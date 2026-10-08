# `constant-header-docs-arguments`

**Kind:** `fern-defect`. Fern sends a header whose schema defaults to a string as
that constant and leaves it out of the method, yet its `README.md` and
`reference.md` pass it to the method and document it there.

## The input

[`header-default-constants/openapi.yml`](../../fern-measurements/parameter-lowering/header-default-constants/openapi.yml),
a crozier-authored document whose `GET /beds` declares, beside a required query
parameter, headers with and without defaults: `X-Valve-Mode` (required inline
enum, `default: drip`), `X-Mist-Mode` (optional inline enum, `default: fine`),
`X-Hatch-Mode` (optional nullable enum with a description, `default: down`),
`X-Lamp-Watts` and `X-Fan-Speed` (integer defaults) and `X-Vent-Mode` (a
required enum with none).

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0; the comment-stripped tree is the document's
`fern-expected/`.

`src/fern/beds/raw_client.py` sends `"X-Valve-Mode": "drip"`, `"X-Mist-Mode":
"fine"` and `"X-Hatch-Mode": "down"` as constants, and `list_beds` takes
`section`, `lamp_watts`, `vent_mode` and `fan_speed` only. Yet `README.md`
(lines 47–49 and 84–86) and `reference.md` (lines 28–30) pass
`valve_mode="drip"`, `mist_mode="fine"` and `hatch_mode="down"` to `list_beds`,
and `reference.md` documents each under the method as `typing.Literal`
(lines 68–91).

## Why it is a defect

With the tree's `src/` on `PYTHONPATH` beside `httpx` and `pydantic` (a copy):

```text
$ python -c 'import inspect; from fern import FernApi; print(list(inspect.signature(FernApi().beds.list_beds).parameters))'
['section', 'lamp_watts', 'vent_mode', 'fan_speed', 'request_options']
$ python -c 'from fern import FernApi; from fern.beds import ListBedsRequestXVentMode; FernApi().beds.list_beds(section="section", lamp_watts=1, vent_mode=ListBedsRequestXVentMode.OPEN, valve_mode="drip", mist_mode="fine", hatch_mode="down")'
TypeError: BedsClient.list_beds() got an unexpected keyword argument 'valve_mode'
```

The README's call does not match the generated signature and `reference.md`
documents arguments the method does not have: docs and examples that
contradict the generated code are a defect under the defect rule. Fern's code —
the constant headers, the method without them — is behaviour, and crozier
matches it.

## crozier's output

crozier writes the same tree but for those lines: its snippets and parameter
lists leave the constant headers out. `crozier compare` over the pair matches
and reports this departure once per file, at the first line of the differing
window (`README.md:47`, `reference.md:28`); those are the golden's
`constant-header-docs-arguments` rows in `tests/fixtures/departures-ledger.tsv`,
beside the rows of the corpus goldens whose operations declare such a header.
`compare_reports_the_parameter_docs_departures_and_fails_on_any_other_difference`
in `crates/crozier-e2e/tests/e2e/compare.rs` drives it, and shows the comparison failing when one
more line of either file differs.
