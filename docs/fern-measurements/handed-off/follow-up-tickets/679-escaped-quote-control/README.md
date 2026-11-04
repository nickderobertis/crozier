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
