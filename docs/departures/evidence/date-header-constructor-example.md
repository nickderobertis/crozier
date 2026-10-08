# Date header constructor example

The independently authored [date-header document](../../openapi-surface/handwritten/observatory-client-date/openapi.yml) promotes an optional date header. Its complete certified CLI 5.67.1 / Python SDK 5.20.0 output annotates `sampling_day` as `typing.Optional[dt.date]`, but supplies `"YOUR_SAMPLING_DAY"` in constructor examples. That value is invalid for the schema's `format: date`.

Run `python3 docs/departures/evidence/date-header-constructor-example.py`: the script extracts the placeholder from the unedited certified output and proves it fails date validation. The replacement passes. Its form and default value come from the certified [observation-date output](../../openapi-surface/handwritten/skyglass-observation-date/fern-expected/src/fern/client.py), which renders `datetime.date.fromisoformat("2023-01-15")`.

The parity rule applies only to Python constructor examples whose parameter is annotated as an optional date. String-header placeholders and unrelated differences are not normalized; a neighboring unexplained change still fails the regression test.
