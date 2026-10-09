# `empty-namespace-package`

**Kind:** `fern-defect`. Fern groups some operations under an empty namespace
it calls `_`, documents them as `client._.method()`, and then writes that
package's files over the package root, so the tree cannot be imported.

## The input

Two documents carry the construct:

- [`lamp-room-log/openapi.yml`](../../openapi-surface/handwritten/lamp-room-log/openapi.yml),
  a crozier-authored document whose one operation, `GET /lamps`
  (`listLamps`), is tagged only with the empty string and declares no SDK group
  name.
- The registered corpus golden `bungie.net`
  ([`CORPUS.md`](../../../tests/fixtures/CORPUS.md)), a real specification
  whose `GET /GetAvailableLocales/`, `/GlobalAlerts/`, `/Settings/` and
  `/UserSystemOverrides/` are tagged with the empty string and have
  `operationId`s with an empty dotted prefix (`.GetAvailableLocales`).

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0 on `lamp-room-log`; the comment-stripped tree is
its `fern-expected/`. The `bungie.net` golden is
`tests/fixtures/bungie.net/expected`.

In both trees `README.md` imports `from fern import FernApi` and calls
`client._.<method>()`, and `reference.md` titles a `_` section linking
`src/fern/_/client.py`. No `_/` directory exists. Instead the package root holds
the `_` package's files:

- `src/fern/client.py` is `class Client` / `class AsyncClient`, the `_`
  sub-client, importing `from ..core.client_wrapper` and `from .raw_client`;
  its docstring examples call `client..list_lamps()`. No `FernApi` class is
  written anywhere.
- `src/fern/raw_client.py` is the `_` sub-client's `RawClient`.
- `src/fern/__init__.py` is the `_` package's marker: empty for
  `lamp-room-log`, and in `bungie.net` a loader re-exporting only the four
  hoisted response types from `.types`.
- In `bungie.net` those four types, `src/fern/types/get_available_locales_response.py`
  and its three siblings, import `from ...core.pydantic_utilities`, the
  depth of `_/types/`.

## Why it is a defect

Running the documented import over each tree, with Python 3.14.7, `httpx`
0.28.1 and `pydantic` 2.14.0 installed in a fresh virtual environment and the
tree's `src/` as the working directory:

```text
$ python -c 'from fern import FernApi'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from fern import FernApi
ImportError: cannot import name 'FernApi' from 'fern' (./fern/__init__.py)
$ python -c 'import fern.client'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fern.client
  File "./fern/client.py", line 5, in <module>
    from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
ImportError: attempted relative import beyond top-level package
```

Both trees print exactly this. In `bungie.net` the hoisted types fail too:

```text
$ python -c 'import fern.types.get_available_locales_response'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fern.types.get_available_locales_response
  File "./fern/types/get_available_locales_response.py", line 7, in <module>
    from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
ImportError: attempted relative import beyond top-level package
```

The documentation describes a `FernApi` client with a `_` sub-client in
`src/fern/_/client.py`; the generated tree has neither, and the code it does
write cannot be imported. That is a defect under the defect rule. Everything
else — the `_` sub-client's methods, its raw client, its types and their
bytes, `README.md` and `reference.md` — is behaviour, and crozier matches it.

## crozier's output

crozier writes the `_` package where the documentation says it is:
`src/fern/_/client.py`, `_/raw_client.py`, `_/__init__.py` and `_/types/`.
Every one of those files except `_/client.py` and `_/types/__init__.py` is
Fern's root-level copy byte for byte, and `_/client.py` differs only in its
docstring examples, which call `client._.list_lamps()` where Fern writes
`client..list_lamps()`. The root `client.py` is the `FernApi` /
`AsyncFernApi` client with a `_` property returning that sub-client, and the
root `__init__.py` exports it. `README.md` and `reference.md` are Fern's
unchanged, and every other file of `bungie.net` stays byte-compared.

`sdk_env_empty_namespace_package_imports_and_answers_its_documented_call` imports
crozier's generated package and makes the documented `client._.list_lamps()`
call against a local server.

The engine's file rule accepts a file crozier writes under `_/` only after
checking it against Fern's root copy in this way, and accepts Fern's
`raw_client.py` and hoisted `types/` files as moved only then; its region rule
replaces the root `client.py` and `__init__.py` whole. Two gates hold the
departure to its rows in `tests/fixtures/departures-ledger.tsv`:
`handwritten_fixtures_match_fern_goldens` and
`clients_extensions_measurements_match_fern` for `lamp-room-log` in both enum
modes, and `bungie_matches_fern_output` for the four Bungie files the
correction moves away from the root, the root's `raw_client.py`, `client.py`
and `__init__.py`, and the files crozier writes under `_/`. A moved file is
recorded at line 0, standing for the whole file.
