# Nested discriminator flat wire

The independently authored [patisserie document](../../fern-measurements/examples/nested-discriminator-wire/openapi.yml)
maps `Pastry.kind=tart` to `TartOrder`, itself discriminated by `crust`.
Fern CLI 5.163.1 with fern-python-sdk 5.41.3 emits `Pastry_Tart(value:
TartOrder, kind="tart")`. Those public names, fields and constructors remain
unchanged in crozier.

The [certified reference and reproduction](../../fern-measurements/examples/nested-discriminator-wire/README.md)
show Fern emitting `{"kind":"tart","value":{"kind":"tart","crust":"shortcrust","fruit":"pear"}}`.
That fails the document's schema: the outer union requires the inner object's
properties at the same level. Fern rejects the valid provider payload
`{"kind":"tart","crust":"shortcrust","fruit":"pear"}` because `value` is
missing. Its README and reference examples contain the invalid Python `tart=,`.
Both wire failures also reproduce with Pydantic 1.10.26 (whose default JSON
output additionally omits the unset outer tag); the original committed
runtime measurement uses Pydantic 2.14.1.

Crozier preserves the wrapper's Python interface, validates a flat input through
its inner union, and serializes its inner fields alongside the outer tag. The
outer tag wins when the inner model also declares that property. Explicit
`value=` construction and wrapped inputs remain accepted. Other union shapes
receive no adapters. The README and reference construct the inner variant using
`value=TartOrder_Shortcrust(...)`.

Run the generated SDK journey with:

```sh
just nx run nested-discriminator-runtime:test
```

The journey generates from the canonical document in normal and `--fern-strict`
modes and runs the real SDK under Pydantic 1.10.26 and 2.14.1 on Python 3.11.
It checks both inner variants, an open inner payload with its own `value` key,
and a derived document whose inner discriminator itself is named `value`, the public fields and constructor parameters,
model dict/JSON output, schema validation, flat parsing, malformed-input
rejection, sync and async HTTP request/response handling against a real loopback server with malformed-response
recovery, and compilation and construction of both README examples. Its
[script](../../../tests/nested-discriminator/runtime/wire.py)
also fails against the certified reference at the flat serialization assertion;
this was checked with both majors before accepting the repaired output.

The offline golden journey compares this fixture through the shared departure
engine and ledger. The rule admits only the added wrapper adapters and the
repaired example constructs and imports; all other text must match Fern.
