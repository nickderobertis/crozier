# Escaped method names in reference headings

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

When an operation's method name would shadow a Python keyword or builtin, Fern's
generated client escapes it with a trailing `_`. Its `reference.md` heading
names the method without the escape. The Apideck ATS golden
(`tests/fixtures/apideck.com-ats/expected`) writes

```text
<details><summary><code>client.applicants.<a href="src/fern/applicants/client.py">all</a>(...) -> GetApplicantsResponse</code></summary>
```

while `src/fern/applicants/client.py` defines `def all_(` (line 55) and no
`all`. The usage example under the same heading calls
`client.applicants.all_(...)`. At this pair Fern anchors every other heading at
its method's lines (`#L<start>-L<end>`); these headings get no anchor, because
the name Fern looks up is not defined in the file.

Calling the documented method on the real generated SDK fails:

```text
$ .venv/bin/python -B docs/departures/evidence/reference-heading-escaped-method-name.py call tests/fixtures/apideck.com-ats/expected/src
client.applicants.all_ resolves: True
client.applicants.all raises AttributeError: 'ApplicantsClient' object has no attribute 'all'
```

The census over every reference tree regenerated at this pair (1233 trees: the
corpus goldens and their overlays, the measurements, and the handwritten,
authored and probe goldens) finds 76 such headings, every one without an
anchor: 62 in `tests/fixtures/` and 14 in `docs/fern-measurements/`. By name:
`all` 58, `import` 3, and `uuid`, `map`, `long`, `int`, `float`, `bool` and
`async` 2 each, `del` 1.

```text
$ python3 docs/departures/evidence/reference-heading-escaped-method-name.py census <every 5.200.0 tree>
…
headings naming a method the client defines only with a trailing `_`: 76
```

crozier names the method the client defines and anchors the link at its lines,
found as for every other heading. The rule admits only a `reference.md` heading
whose method name, less its trailing `_`, is Fern's, where crozier's linked
client defines the escaped name, the link carries a `#L<start>-L<end>` range,
and every other byte of the line is Fern's. Its unit test rejects another
module, a method the client does not define, a name needing no escape, a
missing or malformed range, and any other change on the line; the corpus and
handwritten comparisons apply it over complete trees, and the departures
ledger pins each occurrence.
