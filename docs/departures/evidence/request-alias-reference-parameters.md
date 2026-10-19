# Alias request reference contradicts the generated method

The independent [Manifest Cabinet source](../../openapi-surface/handwritten/request-alias/openapi.yml)
uses a pure component alias of an object with required `ticket` and optional,
documented `caption`. It recreates the alias body shape without other inputs.
The committed renewed [search](../../openapi-surface/witness-search-request-alias/README.md)
finds no complete witness in its bounded source walk; it claims no real witness.

Both complete certified trees use Fern CLI 5.163.1 and
`fernapi/fern-python-sdk` 5.41.3, package `fern`, project
`default_package_name`, with `python-enums` and `literals` respectively. Their
pins and canonical digests live beside the trees. No golden is edited.

The generated sync and async method signatures take `ticket`, `caption` and
`request_options`. The certified reference instead advertises `request:
TitleAlias` (`reference.md` line 39 of both trees). The [executed proof](request-alias-reference-parameters.py)
imports each actual SDK and binds that advertised keyword using `bind_partial`,
isolating the absent keyword from the separately required ticket. Re-run over
both trees at the new pair, each exits 0 and both classes report:

```text
got an unexpected keyword argument 'request'
```

The actual sync and async methods accept flattened arguments and transmit
`{"caption": "compass", "ticket": 7}` through the local HTTP transport. An
unexpected `request` call fails before the handler; the subsequent valid call
recovers. Generated usage examples already use the accepted arguments and stay
matched. Only the reference parameter blocks are corrected, retaining the
actual types and property description: crozier's `reference.md` writes, from
line 39, `**ticket:** `int`` and `**caption:** `typing.Optional[str]` — Shown
on cabinet labels.` in place of Fern's one `request` block; over crozier's
trees in both modes the proof exits 0 with `corrected caption binds` for both
classes.

Reproduce either certified mode (substitute its tree path for SDK):

```sh
python docs/departures/evidence/request-alias-reference-parameters.py SDK/src --reference SDK/reference.md --expected invalid
```

The generated crozier tree runs the same proof with `--expected valid` in
`sdk_env_alias_body_reference_matches_the_actual_flattened_signature`.
The departure rule requires an actual object alias, a flattened JSON request,
the actual signature, and matching parameter descriptions read from the raw
method. It uses the emitter's reference formatting helpers. An unexplained
type, description, extra parameter or unrelated file change still fails.
