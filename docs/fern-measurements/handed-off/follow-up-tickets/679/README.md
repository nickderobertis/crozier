# Quoted and multiline wire names

Issue [#679](https://github.com/nickderobertis/crozier/issues/679).
`openapi.yml` was authored from scratch for this measurement. It declares
property wire names containing a quote, a backslash and a line break.

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 was run through
`tools/fern-goldens/fern-references.py::run_fern`, using the workspace of
`generate-fern-fixture.sh`, under the shared generation lock. `fern.log` and
`exit-code` preserve its fresh refusal: exit 1, with an unescaped
`FieldMetadata(alias="probe"code")` failing the generator's own ruff check.
There is no successful reference tree.

Verdict: **refusal-kept**, class `generator-lint-failure`. The refusal rule
requires both default and `fern-strict` generation to refuse this shape.
crozier previously reached its own formatter with invalid Python. It now
reports the class and offending type/property before writing files. For names containing a quote, backslash or line break, the boundary checks
the unescaped literal with the existing ruff dependency's isolated default
lint rules. This catches malformed escapes and trailing backslashes too,
without refusing a backslash that makes a quote valid. Tool-launch and I/O
errors remain actionable formatter errors, rather than refusal classifications.

The unit test `a_field_alias_that_breaks_a_python_literal_is_a_lint_failure`
checks quote, LF and CR independently and a safe alias as control. The real CLI
journeys in `follow_up_tickets.rs` require both refusals and successful
recovery after replacing the unsafe names with `probe-code`.

[`../679-escaped-quote-control/openapi.yml`](../679-escaped-quote-control/openapi.yml) was authored from scratch by retaining one
property whose backslash escapes its quote. Its complete `fern-expected/`,
`fern.log` and `exit-code` are a second fresh generation under the same pair,
workspace and lock; Fern generates successfully. The real CLI test
`follow_up_ticket_escaped_quote_alias_still_matches_the_certified_pair` holds
crozier's whole tree against it. The separate real CLI invalid-alias test
checks raw quote, LF, CR, malformed hexadecimal escape and trailing backslash,
each in default and strict modes.
