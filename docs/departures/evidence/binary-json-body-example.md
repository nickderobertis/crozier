# A binary JSON example has the wrong argument type

The independently authored [request shapes](../../openapi-surface/handwritten/json-request-shapes/openapi.yml)
include tagged `PUT /vault`, without parameters. The independent
[path-parameter source](../../openapi-surface/handwritten/json-binary-path/openapi.yml)
uses tagged `POST /depository/{locker}` beside a required string path parameter.
Both certified pairs declare `request: bytes` and send `json=request` with the
JSON content-type header. Their unedited complete output sits beside each source.
The literals counterparts live under `docs/fern-measurements/bodies-responses/`.

Both use CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0, packaged preview,
organization/package `fern`, project `default_package_name`, no audience filter.
The handwritten pairs set `pydantic_config.enum_type: python_enums`; the literals
pairs leave it unset. These fresh measurements establish bytes for both trigger
variants; no string-annotated method is claimed.

The sync and async client docstrings and `reference.md`, plus the path variant's
README, pass `request="string"`.
The actual generated annotation is bytes, while the reference parameter block
incorrectly documents that parameter as `str`. Crozier documents bytes there. The committed
[proof script](binary-json-body-example.py) imports each actual SDK, extracts the
example with Python's AST, obtains the actual method's annotation with
`typing.get_type_hints`, and checks its value using Pydantic's strict type
validator. The plain string fails; `b"string"` passes. It also parses the actual
reference example's value. No SDK or emitted method is mocked. The README's standard `(...)` scaffolds
are deliberate pseudocode, preserved unchanged; the proof selects concrete
worked usage calls and excludes those placeholders.

Run from the repository root with HTTPX and Pydantic installed:

```sh
python docs/departures/evidence/binary-json-body-example.py \
  docs/openapi-surface/handwritten/json-request-shapes/fern-expected/src \
  vault deposit_bundle --examples invalid
python docs/departures/evidence/binary-json-body-example.py \
  docs/openapi-surface/handwritten/json-binary-path/fern-expected/src \
  depository deposit_parcel --examples invalid
```

The proof also invokes both actual sync and async methods with the corrected
bytes value through local HTTP transports. The matched SDK wrapper encodes
`b"string"` as the base64 JSON string `"c3RyaW5n"`; those requests succeed.
A missing required request fails before transport, and the subsequent valid
call recovers. Thus there is no runtime serialization defect. The correction
changes only the default example value's type; annotations, signatures, request
encoding and all other output match the certified pair. The real-binary journey
runs the same proof with `--examples valid` over crozier's generated SDK.

The parity rule requires the actual raw method's bytes argument, `json=request`
and JSON header, and takes only that method's exact default example value and its contradictory
reference parameter type in
client docstrings, the README call or the corresponding reference section. Adjacent unexplained
changes remain mismatches. Exact line ledger entries come from `src/parity.rs`.
