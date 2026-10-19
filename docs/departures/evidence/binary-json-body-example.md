# A binary JSON example has the wrong argument type

The independently authored [request shapes](../../openapi-surface/handwritten/json-request-shapes/openapi.yml)
include tagged `PUT /vault`, without parameters. The independent
[path-parameter source](../../openapi-surface/handwritten/json-binary-path/openapi.yml)
uses tagged `POST /depository/{locker}` beside a required string path parameter.
Both certified pairs declare `request: bytes` and send `json=request` with the
JSON content-type header. Their unedited complete output sits beside each source.
The literals counterparts live under `docs/fern-measurements/bodies-responses/`.

Both use Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3, packaged
preview, organization/package `fern`, project `default_package_name`, no
audience filter. The handwritten pairs set `pydantic_config.enum_type:
python_enums`; the literals pairs leave it unset. These measurements establish
bytes for both trigger variants; no string-annotated method is claimed.

The sync and async client docstrings and `reference.md`, plus the path variant's
README, pass `request="string"`: `json-request-shapes/fern-expected` at
`src/fern/vault/client.py` lines 73 and 153 and `reference.md` line 490;
`json-binary-path/fern-expected` at `src/fern/depository/client.py` lines 54 and
131, `README.md` lines 45 and 66 and `reference.md` line 24. The actual generated
annotation is bytes. Crozier passes `request=b"string"` on those lines.

**Partly fixed at this pair.** At the previous certified pair (Fern CLI 5.67.1,
fern-python-sdk 5.20.0) `reference.md` also documented the parameter as `str`.
fern-python-sdk 5.41.3 documents it as `bytes` (`json-request-shapes`
`reference.md` line 507, `json-binary-path` `reference.md` line 49), as crozier
does, so that half of the departure is retired. Only the example value remains.

The committed [proof script](binary-json-body-example.py) imports each actual
SDK, extracts the example with Python's AST, obtains the actual method's
annotation with `typing.get_type_hints`, and checks its value using Pydantic's
strict type validator. The plain string fails; `b"string"` passes. It also
parses the actual reference example's value and asserts that both sides'
`reference.md` documents `**request:** `bytes``. No SDK or emitted method is
mocked. The README's standard `(...)` scaffolds are deliberate pseudocode,
preserved unchanged; the proof selects concrete worked usage calls and excludes
those placeholders.

Run from the repository root with HTTPX and Pydantic installed (re-run at this
pair with Python 3.12, httpx 0.28.1 and pydantic 2.14.1); each exits 0:

```sh
python docs/departures/evidence/binary-json-body-example.py \
  docs/openapi-surface/handwritten/json-request-shapes/fern-expected/src \
  vault deposit_bundle --examples invalid
python docs/departures/evidence/binary-json-body-example.py \
  docs/openapi-surface/handwritten/json-binary-path/fern-expected/src \
  depository deposit_parcel --examples invalid
```

```text
{"examples": {"AsyncVaultClient": "plain string rejected by actual bytes annotation", "VaultClient": "plain string rejected by actual bytes annotation"}, "wire": "sync/async bytes encoded as a base64 JSON string"}
{"examples": {"AsyncDepositoryClient": "plain string rejected by actual bytes annotation", "DepositoryClient": "plain string rejected by actual bytes annotation"}, "wire": "sync/async bytes encoded as a base64 JSON string"}
```

With `--examples valid` both Fern trees exit 1. Over crozier's SDKs, generated
from each source in both enum modes, `--examples valid` exits 0 with `bytes
example has its declared type` for every sync and async client.

The proof also invokes both actual sync and async methods with the corrected
bytes value through local HTTP transports. The matched SDK wrapper encodes
`b"string"` as the base64 JSON string `"c3RyaW5n"`; those requests succeed.
A missing required request fails before transport, and the subsequent valid
call recovers. Thus there is no runtime serialization defect. The correction
changes only the default example value's type; annotations, signatures, the
reference parameter type, request encoding and all other output match the
certified pair. The real-binary journey
(`sdk_env_binary_json_examples_have_their_actual_argument_type_and_encode`)
runs the same proof with `--examples valid` over crozier's generated SDK.

The parity rule requires the actual raw method's bytes argument, `json=request`
and JSON header, and takes only that method's exact default example value in
client docstrings, the README call or the corresponding reference section.
Adjacent unexplained changes, including a reference parameter type that differs,
remain mismatches. Exact line ledger entries come from `src/parity.rs`.
