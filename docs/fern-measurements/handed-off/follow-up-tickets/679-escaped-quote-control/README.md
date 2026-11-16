# Escaped-quote control for #679

Authored from scratch as the adjacent #679 reduction's control. The wire name
contains a backslash followed by a quote, which forms valid Python when the
certified generator writes the name into an unescaped double-quoted literal.

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated the
complete, comment-stripped `fern-expected/` through
`tools/fern-goldens/fern-references.py::run_fern` and `strip_into`, using the
workspace of `generate-fern-fixture.sh`, under the shared generation lock.
`fern.log` and `exit-code` record success. There are no enums.

Verdict: control generates and byte-matches with the catalogued identity
headers applied. It prevents #679's refusal from rejecting valid emitted
Python. The root ticket keeps its `refusal-kept` verdict for the syntax-breaking
measurement; this control narrows that class, rather than adding a departure.

**Regenerated at the certified pair.** The trees under this record's
`fern-expected/` (and `expected-literals/` or `literals/`, where it has them)
were regenerated at Fern CLI 5.200.0 / `fernapi/fern-python-sdk` 5.41.25, the
certified pair, one Fern run at a time through
`tools/fern-goldens/fern-references.py`'s own `generated_tree` (and
`reduce_overlay` for an overlay), and crozier's comparison holds the record to
them. Statements above that name Fern CLI 5.163.1 / fern-python-sdk 5.41.3
describe the measurement as first taken, at the pair certified then; a digest,
log or exit code they cite is that run's.
