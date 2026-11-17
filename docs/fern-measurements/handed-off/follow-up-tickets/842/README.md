# Wire aliases as literal data (#842)

Issue [#842](https://github.com/nickderobertis/crozier/issues/842).
`openapi.yml` was authored from scratch for this measurement. Its `Beacon`
declares three property wire names: `relay\"code` (a backslash, then a quote,
which Fern's unescaped literal accepts), `a" + bearing + "` (a balanced
expression, which its lint accepts because the scaffold ignores `F821`), and
the plain `call-sign` as a control.

Fern CLI 5.200.0 with `fernapi/fern-python-sdk` 5.41.25 generated the complete,
comment-stripped `fern-expected/` through `fern-references.py generate
measurements handed-off/follow-up-tickets/842` (its `cases.tsv` row), under the
shared generation lock. Fern writes each name between quotes unescaped, so the
certified `Beacon` aliases `relay"code` and the expression `"a" + bearing + ""`,
and the model fails to import.

Verdict: **departure-catalogued**, `escaped-field-alias-literal`. crozier writes
each alias as a string literal of the declared name, so its package imports and
the model parses, dumps and writes every field under exactly its declared wire
name. The departure's [evidence note](../../../../departures/evidence/escaped-field-alias-literal.md)
records both runs. The whole tree byte-matches the certified pair with that
departure applied (`follow_up_ticket_matching_outputs_hold_against_the_certified_pair`).
