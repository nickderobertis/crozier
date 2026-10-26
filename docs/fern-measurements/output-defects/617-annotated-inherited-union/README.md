# Annotated reference to an inheritance-spelled union

**Verdict: `parity-gap-repaired`.** Compared against the certified pair, Fern
copies an annotated `$ref` to a union spelled through inheritance as a
discriminated union of its own, with one variant wrapper per mapping entry.
crozier flattened the base into an ordinary model (`PotOuterCoat` with
`finish: str`), so variant payloads no longer parsed into variant classes.
crozier now copies such a union complete, and its SDK for this document
byte-matches `fern-expected/`.

Proposal: [#617](https://github.com/nickderobertis/crozier/issues/617).

`openapi.yml` was written from scratch for this measurement. `fern-expected/` is
the complete, comment-stripped output that Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3 generated from it under `python_enums`. It was
produced by `just fern-references measurements
output-defects/617-annotated-inherited-union`, the case `cases.tsv` registers.
Its tree digest (Contract A) is
`ac8d97b3a72a5cbaf97042b43b631c5464145dce1de711c9d4f38b347ecfb14a`.

## The comparison

`Coat` is the base: a `discriminator` on `finish` whose `mapping` names
`MatteCoat` and `GlossCoat`, each of which is `allOf: [$ref Coat, {…}]`. `Coat`
writes no `oneOf`. This is the shape of the committed Palo Alto Prisma Cloud
`TimeRangeConfigModel` once its `oneOf` is removed, the removal control the
proposal records.

| Site | Spelling | Fern | crozier at `80331e4bb` |
|---|---|---|---|
| `Pot.outerCoat` | `allOf: [$ref Coat, {description}]` | `PotOuterCoat = Union[PotOuterCoat_Matte, PotOuterCoat_Gloss]` on `finish` | `class PotOuterCoat` with `finish: str` |
| `recoatPot`'s inline body `coat` | the same | `RecoatPotRequestCoat_Matte` / `_Gloss` union, argument documented | `class RecoatPotRequestCoat`, argument undocumented |
| `Pot.innerCoat`, body `previousCoat` | plain `$ref Coat` | `Coat` | same |

Every variant wrapper of a copy carries the annotation's description as its
docstring, where `Coat_Matte` carries `Coat`'s own.

## The outcome

- `src/ir.rs`: `Builder::use_site_copy`, which copies a component property's
  annotated reference, and `InlineHoister::prop_type_ref`, which copies an
  inline body's, both read an inheritance union base (`is_inheritance_union_base`)
  as a union. Each copies it through the same union builder as the original
  declaration, documented by the annotation.
- `src/ir.rs`: the body argument is documented by its `allOf` member's
  description (`hoist_inline_object`), as a model field already was.

`crates/crozier-e2e/tests/e2e/output_defects.rs` holds crozier's whole SDK to
`fern-expected/`. It also shows that crozier's former flattened `PotOuterCoat`
fails the comparison. Its `sdk_env_*` journey runs the SDK as `runtime.txt`
records.

## Runtime

The verdict rests on behaviour, so `runtime.txt` records an actual run of the
certified SDK with Pydantic 2.14.1, and the same run over crozier's pre-repair
SDK as a control. The journey
(`crates/crozier-e2e/tests/e2e/output_defects_runtime.py 617`) drives the
generated client over an `httpx.MockTransport`. For each of `matte` and `gloss`:

- a payload parsed through the annotated copy yields that variant's class with
  its `finish` value, both as `Pot.outer_coat` and through `parse_obj_as`;
- each variant constructed and passed to `record_pot` and `recoat_pot` is sent
  in the shape the source schema validates.

The script checks that shape with a small validator that follows the
discriminator mapping. `runtime.txt` adds an independent `jsonschema` 4.26.0
check of the same payloads against `MatteCoat` and `GlossCoat`. Over the
pre-repair SDK, the first parse yields `PotOuterCoat` itself.

To reproduce, install `httpx`, `pydantic` and `jsonschema==4.26.0` in a
disposable environment, convert `openapi.yml` to `openapi.json` (any YAML
loader), and run:

```sh
python crates/crozier-e2e/tests/e2e/output_defects_runtime.py 617 \
  docs/fern-measurements/output-defects/617-annotated-inherited-union/fern-expected/src \
  openapi.json
python - openapi.json <<'PY'
import importlib.metadata
import json
import sys

import jsonschema

doc = json.load(open(sys.argv[1]))
for name, payload in [
    ("MatteCoat", {"finish": "matte", "layers": 2, "tooth": 3}),
    ("GlossCoat", {"finish": "gloss", "layers": 1, "sheen": 0.8}),
]:
    schema = {"$ref": f"#/components/schemas/{name}", "components": doc["components"]}
    jsonschema.Draft202012Validator(schema).validate(payload)
    version = importlib.metadata.version("jsonschema")
    print(f"jsonschema {version}: {json.dumps(payload, sort_keys=True)} is valid against {name}")
PY
```
