# `declared-examples-array-parameter-value`

**Kind:** `usefulness`, granted by design-review ruling 5
(`declared-examples-array`, decided 2026-11-01, causes
`schema-examples-array-parameter-value` and `R4`): crozier works a parameter's
value from its schema's `examples` array or its own `examples` map rather than
the certified pair's placeholder.

## The input

- [`schema-examples-array-parameter-value/openapi.yml`](../../fern-measurements/handed-off/example-values/schema-examples-array-parameter-value/openapi.yml):
  `PATCH /lamps/{lampId}/settings` takes a path parameter whose schema declares
  `examples: [lmp_8f2kq]` beside a body shaped like vercel's
  `update_record` (a `properties` map holding a literal `additionalProperties:
  false` entry). The certified pair writes the name there; on the document's
  other two operations it writes the array's entry, as crozier does.
- [`R4/openapi.yml`](../../fern-measurements/handed-off/example-values/R4/openapi.yml): `keeperId` declares a schema
  `example` (`KPR-from-schema`) and an `examples` map (`KPR-from-map`).

## Both outputs and the declared value

```text
lamp_id="lampId",            lamp_id="lmp_8f2kq",        declared examples: [lmp_8f2kq]
keeper_id="KPR-from-schema", keeper_id="KPR-from-map",   declared examples: {first: {value: KPR-from-map}}
```

The certified pair's line is first, crozier's second, in `reference.md`, `README.md` and
both docstrings. Both bind: each is a `str`.

## The rule

`declared_values::declared_examples_array_parameter_value` admits a pair only
where crozier writes the first `examples` entry of the parameter's (referenced)
schema that declares no `example`, or the first value of the parameter's own
`examples` map, and Fern writes the parameter's name, a numeric placeholder or
the schema's `example`.
