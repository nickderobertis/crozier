# `unquoted-timestamp-parameter-example`

**Kind:** `usefulness`, granted by design-review ruling 3
(`yaml-timestamp-parameter-example`, decided 2026-11-01): crozier keeps the
unquoted ISO timestamp the API's author declared as a parameter's example.

## The input

- [`yaml-timestamp-parameter-example/openapi.yml`](../../fern-measurements/handed-off/example-values/yaml-timestamp-parameter-example/openapi.yml):
  `GET /tides` declares `since` (required, `format: date-time`,
  `example: 2031-04-02T08:15:00Z` unquoted), `until` (optional, the same shape),
  `recordedOn` (required `type: string`, an unquoted timestamp example),
  `loggedAfter` (optional `type: string`, an unquoted timestamp example) and
  `station` (optional, `example: pier-7`).
- [`example-optional-members/openapi.yml`](../../fern-measurements/handed-off/example-values/example-optional-members/openapi.yml):
  the required `observedTo` refers to `Moment`, whose `examples` array's entry
  `2032-06-01T04:30:00Z` is unquoted.

YAML reads each unquoted value as a timestamp. The certified pair (Fern CLI
5.163.1, `fernapi/fern-python-sdk` 5.41.3) then treats it as no example.

## Both outputs and the declared value

`reference.md`, the certified pair's line first and crozier's second:

```text
since=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),   since=datetime.datetime.fromisoformat("2031-04-02T08:15:00+00:00"),   declared 2031-04-02T08:15:00Z
(until left out)                                                        until=datetime.datetime.fromisoformat("2031-04-03T08:15:00+00:00"),   declared 2031-04-03T08:15:00Z
recorded_on="recordedOn",                                                recorded_on="2031-04-01T06:00:00Z",                                    declared 2031-04-01T06:00:00Z
observed_to=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),  observed_to=datetime.datetime.fromisoformat("2032-06-01T04:30:00+00:00")
```

The docstrings wrap each call, so the same values appear on the
`"2031-04-02 08:15:00+00:00",` line of a wrapped `fromisoformat(` call, and
`until`'s three wrapped lines are crozier's alone. `loggedAfter`, an optional
parameter that is not temporal, is left out by both. Both sides bind: each
value is a `datetime.datetime` or `str` the argument accepts.

## The rule

`declared_values::unquoted_timestamp_parameter_example` admits a pair where
Fern writes its date-time placeholder (or the parameter's name) and crozier the
timestamp the document writes unquoted for that same parameter;
`unquoted_timestamp_parameter_line` admits a line only crozier writes for an
*optional* such parameter (one line or a wrapped call's three) and the
`import datetime` those lines need. A required parameter's line is never one it
admits as added.
