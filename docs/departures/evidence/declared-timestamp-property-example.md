# `declared-timestamp-property-example`

**Kind:** `usefulness`. It applies the principle of design-review ruling 3
(`yaml-timestamp-parameter-example`, decided 2026-11-01), which keeps the
unquoted ISO timestamp the API's author declared. The planner's ruling of
2026-11-02 extends that principle from a parameter's example to a `date-time`
property's value in a schema-level object example. The case is recorded as a
sub-case of the `yaml-timestamp-parameter-example` triage row.

## The input

[`yaml-timestamp-parameter-example/openapi.yml`](../../fern-measurements/handed-off/example-values/yaml-timestamp-parameter-example/openapi.yml)
posts `TideReading` as a single body (`logReading`) and as an array body
(`logReadings`). The schema-level example gives:

- `highWaterAt` (required, `format: date-time`): `2031-04-02T08:15:00Z`, unquoted;
- `lowWaterAt` (optional, `format: date-time`): `2031-04-02T14:27:00Z`, unquoted;
- `calibratedAt` (optional, `format: date-time`): the `2000-01-23T04:56:07.000+00:00` sentinel.

YAML reads every unquoted value as a timestamp. The certified pair (Fern CLI
5.163.1, `fernapi/fern-python-sdk` 5.41.3) then treats each one as no example.
The same shape was found on confluent's schema registry
(`confluentinc/schema-registry-sdk-go@77f22d67`), where every such value is the
sentinel.

## Both outputs and the declared value

Each row shows the certified pair's line, crozier's line, and the declared
value. The lines are from `reference.md` and repeat on both calls:

```text
high_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),   high_water_at=datetime.datetime.fromisoformat("2031-04-02T08:15:00+00:00"),   declared 2031-04-02T08:15:00Z
low_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),    low_water_at=datetime.datetime.fromisoformat("2031-04-02T14:27:00+00:00"),    declared 2031-04-02T14:27:00Z
calibrated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),   (the same)                                                                       declared sentinel, dropped by both
```

The docstrings in `tides/client.py` wrap the longer calls. The same values
then appear on a `"2031-04-02 14:27:00+00:00",` string line inside a wrapped
`fromisoformat(` call.

The measurement's
[`runtime.txt`](../../fern-measurements/handed-off/example-values/yaml-timestamp-parameter-example/runtime.txt)
runs both sides' worked calls against an `httpx` mock transport. Both validate
and send their bodies. The certified pair sends `"highWaterAt":"2024-01-15T09:30:00Z"`.
crozier sends the declared `"highWaterAt":"2031-04-02T08:15:00Z"` and
`"lowWaterAt":"2031-04-02T14:27:00Z"`.

## The rule

`declared_values::declared_timestamp_property_example` admits a line pair under
two conditions. First, Fern writes its date-time placeholder for a keyword, or
the string line of a wrapped call. Second, crozier writes, for the same
keyword, the instant that a schema-level object example declares unquoted for a
`date-time` property of that wire name. The sentinel is excluded, because both
sides drop it. The rule adds and removes no lines.
`departures::declared_values::tests::a_declared_timestamp_property_is_admitted_only_with_its_declaration`
shows that a different instant, a non-date-time property, a quoted value and
the sentinel still fail.
