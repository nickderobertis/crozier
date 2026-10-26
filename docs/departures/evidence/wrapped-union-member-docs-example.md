# Wrapped union member docs example

The independently authored [tide-pool survey document](../../openapi-surface/handwritten/tidepool-survey-log/openapi.yml)
maps `SurveyEntry.entryType=level` to `WaterLevel`, a `oneOf` of a bare
number and an object with no discriminator of its own. Fern CLI 5.163.1 with
fern-python-sdk 5.41.3 holds that union whole in the wrapper's `value` field
(`SurveyEntry_Level(value: WaterLevel, entry_type="level")`), and its
`src/fern/client.py` docstrings construct it as `SurveyEntry_Level(value=1.1)`,
which crozier matches. But the certified `README.md` (twice) and `reference.md`
(once) write the same request as:

```python
    request=SurveyEntry_Level(
        level=,
    ),
```

That is no Python: an empty argument value, under a keyword the constructor
does not have. crozier writes the constructor the docstrings write,
`request=SurveyEntry_Level(value=1.1),`, keeping every other byte of both files.

Run `python3 docs/departures/evidence/wrapped-union-member-docs-example.py`. It
extracts the three examples from the unedited certified tree and compiles each,
then compiles the corrected constructor. With the certified tree installed
(`uv venv .venv && uv pip install --python .venv <fern-expected copy>`), it also
binds the corrected constructor to the certified SDK and shows the certified
keyword rejected. Result with the certified SDK installed (Python 3.12.14,
pydantic 2.14.1), exit 0:

```text
README.md: certified example does not compile: expected argument value expression (line 8)
README.md: certified example does not compile: expected argument value expression (line 12)
reference.md: certified example does not compile: expected argument value expression (line 11)
corrected: {'value': 1.1, 'entryType': 'level'}
certified keyword rejected by the certified SDK: ValidationError
```

The parity rule reads the wrappers off the source document: a mapping target
that is a `oneOf` or `anyOf` of two or more references, with no properties and
no discriminator of its own (one with a discriminator is
[`nested-discriminator-flat-wire`](nested-discriminator-flat-wire.md)'s). In
`README.md` and `reference.md` alone it rewrites each `Wrapper(value=…)` crozier
writes into Fern's `Wrapper(` / `<tag>=,` / `)` and then requires the whole file
to equal Fern's, so any other difference in either file still fails. Its unit
tests in `src/departures.rs` show the rule refusing a neighbouring unexplained
change, another keyword, a target with its own discriminator and a Python file.
