# `repeated-credential-example-keyword`

**Kind:** `fern-defect`. When two credentials resolve to one constructor
parameter, Fern declares the parameter once but passes it twice in every
client constructor example.

## The input

Two crozier-authored documents:

- [`twin-key-relay/openapi.yml`](../../openapi-surface/handwritten/twin-key-relay/openapi.yml)
  declares two header `apiKey` schemes, `issuerA` and `issuerB`, both naming
  `X-Api-Key`, and offers both in the document's `security`.
- [`grid-valve-console/openapi.yml`](../../openapi-surface/handwritten/grid-valve-console/openapi.yml)
  declares an http `bearer` scheme with `x-fern-token-variable-name: apiKey`
  beside a header `apiKey` scheme naming `X-Api-Key`, with no `security`.

The registered corpus golden `openepcis-dpp-ready` (corpus row 93 in
[`CORPUS.md`](../../../tests/fixtures/CORPUS.md)) carries the same construct
from a real specification: its `X-API-KEY` and `API-KEY` header schemes both
become the client's `api_key`. The measurement case
[`relay-station-shared-name`](../../fern-measurements/clients-extensions/relay-station-shared-name/openapi.yml)
reaches it through the header extension: two header schemes at distinct
headers, both named `token` by `x-fern-header`, and Fern's examples pass
`token` twice; `clients_extensions_measurements_match_fern` holds its rows.

## Fern's output

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0 on both; each comment-stripped tree is the
document's `fern-expected/`.

In `twin-key-relay`, `src/fern/client.py`'s `FernApi.__init__` and
`AsyncFernApi.__init__` each declare one `api_key: str` (lines 76 and 234), and
`core/client_wrapper.py` writes the `X-Api-Key` header from it twice (lines
44–45). Yet every constructor example passes `api_key` twice: `README.md` lines
41–42 and 74–75 (`api_key="<value>"` then `api_key="<X-Api-Key>"`),
`reference.md` lines 19–20, and `src/fern/client.py` lines 66–67, 145–146,
224–225 and 303–304 (`api_key="YOUR_API_KEY"` twice). `grid-valve-console`'s
`README.md` (lines 41–42, `api_key="<token>"` then `api_key="<X-Api-Key>"`),
`reference.md` (lines 19–20) and `src/fern/client.py` (lines 63–64, 130–131,
209–210 and 278–279) do the same.

## Why it is a defect

A call that repeats a keyword argument does not bind. Compiling the `README.md`
snippet of `twin-key-relay`'s tree (lines 38–48), with no dependency needed,
re-run at the new pair on 2026-10-18 under Python 3.14.7:

```text
$ python3 -c 'import sys; compile(open(sys.argv[1]).read(), "README.md", "exec")' readme-snippet.py
  File "README.md", line 5
SyntaxError: keyword argument repeated: api_key
```

The client docstring's example (`src/fern/client.py` lines 64–68, dedented)
fails the same way, and so do `grid-valve-console`'s `README.md` snippet (lines
38–44) and `openepcis-dpp-ready`'s (`tests/fixtures/openepcis-dpp-ready/expected/README.md`
lines 38–51, `api_key="<X-API-KEY>"` then `api_key="<API-KEY>"` at lines
42–43):
`SyntaxError: keyword argument repeated: api_key`. The examples contradict the
generated constructor, which takes the keyword once; that is a defect under the
defect rule. Fern's code — the one parameter, the header written twice, the
bearer reading the shared field — is behaviour, and crozier matches it.

## crozier's output

crozier writes the same trees but for those lines: each constructor example
passes the shared keyword once, keeping the first. Its `README.md` snippet for
`twin-key-relay` compiles and runs, with `httpx` and `pydantic` installed beside
the generated `src/`:

```text
$ python -c 'import inspect; from fern import FernApi; print(list(inspect.signature(FernApi).parameters)[:3]); client = FernApi(api_key="<value>", base_url="https://relay.keys.test"); print(client._client_wrapper.get_headers()["X-Api-Key"])'
['base_url', 'environment', 'api_key']
<value>
```

`handwritten_fixtures_match_fern_goldens` compares both fixtures and holds the
departure to each golden's `repeated-credential-example-keyword` rows in
`tests/fixtures/departures-ledger.tsv`, one per file at the first line of its
differing window; `clients_extensions_measurements_match_fern` does the same
for their literals-mode trees and `relay-station-shared-name`, and
`openepcis_dpp_ready_matches_fern_output` for that golden's `README.md`,
`reference.md` and four `client.py` files. At the new pair the departure
applies at `README.md:42`, `reference.md:20` and `src/fern/client.py:67`
(`twin-key-relay`) or `:64` (`grid-valve-console`).
