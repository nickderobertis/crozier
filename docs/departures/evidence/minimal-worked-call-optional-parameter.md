# `minimal-worked-call-optional-parameter`

**Kind:** `usefulness`, granted by design-review ruling 4 (`minimal-worked-call`,
decided 2026-11-01): a worked call is a minimal call carrying the required
parameters only, so crozier leaves every optional parameter out of it, even one
with a declared example.

The ruling's sentence also says "match the certified pair", and on these two
shapes the certified output contradicts its minimal call: it passes the optional
argument. The standing rule is that contradictory evidence is recorded and the
ruling followed, so crozier keeps the minimal call and this departure records the
difference.

## The value the API's author declared

| Document | Parameter | Shape | Declared |
|---|---|---|---|
| `Kong/developer.konghq.com` analytics-dashboards v2 (`d58ac8e1`) | `sort`, optional query | `allOf: [$ref SortQuery, {description}]` | `SortQuery.example: created_at desc` |
| `crate-works/ro-crate-api` (`f2457da3`) | `entityType`, optional query | `{type: array, items: {$ref EntityType}}` | parameter `example: ["http://pcdm.org/models#Collection"]` |

## Both outputs

The certified pair, Fern CLI 5.163.1 with fern-python-sdk 5.41.3, in both enum modes:

```python
client.dashboards.list(
    page_size=10,
    page_number=1,
    sort="created_at desc",
)
client.entities.list_entities(
    member_of="https://catalog.paradisec.org.au/repository/NT1",
    entity_type=["http://pcdm.org/models#Collection"],
)
```

crozier:

```python
client.dashboards.list(
    page_size=10,
    page_number=1,
)
client.entities.list_entities(
    member_of="https://catalog.paradisec.org.au/repository/NT1",
)
```

The `page_size` and `page_number` examples on the first call are the existing R11
behaviour for an optional scalar with a plain example, which this departure does
not change. Those lines match the certified pair, so the call is minimal for
these two shapes only.

## Running it

`python3 docs/departures/evidence/minimal-worked-call-optional-parameter.py` reads
each committed document and certified golden, generates with crozier, and checks
that the certified docstring passes the argument, crozier's does not, and both
signatures give the argument a default, so the minimal call binds:

```text
registered-literals-kong-developer-konghq-com-d58ac8e1: certified passes sort="created_at desc", crozier leaves sort out; both calls bind
registered-literals-crate-works-ro-crate-api-f2457da3: certified passes entity_type=["http://pcdm.org/models#Collection"], crozier leaves entity_type out; both calls bind
```

## What stays unexplained

`a_minimal_call_excuses_only_the_declared_omitted_arguments` in
`src/departures/declared_values.rs` holds the rule to the declared value and these
shapes: another value, another argument, an array with inline items, a required
parameter, and an unexplained argument beside an excused one all still fail.
