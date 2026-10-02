# undefined-component-reference: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe log](evaluation-logs/probe.log) shows successful package/client
imports and **zero mypy errors**. It declares `GET /carts/{id}` with missing
`CartIdParam` and valid `LocaleParam`. The [public client attempt](evaluation-logs/probe.wire.log)
raises `AttributeError` because `get_cart` is absent. No request is sent,
`locale` cannot be supplied and the declared empty 204 cannot be parsed:
crozier drops the entire endpoint, rather than faithfully representing the
unresolved required parameter. This fails the no-dropped-field/operation rule.

One population representative, [Jentic's Jumpseller description,
`f368e886888436f308b9adb3ecd198c0e47f098db700ace8e646155d70582608`](evaluation-logs/population.log),
imports its package and root client but has **234 mypy errors**. Its Cart
endpoint `GET /carts/{id}.json` names missing `CartIDParam`; the [wire
attempt](evaluation-logs/population.wire.log) finds the entire `cart` subclient
absent, sends no request and parses no response. The baseline log records
its immutable source URL, digest and complete mypy report. Both the typing
errors and the dropped endpoint disqualify it. Further representatives cannot
qualify the class under the dispatch's conjunction rule.

The class is `refuse` in both modes. The structural check finds a parameter
Reference Object naming an absent `components.parameters` target before
normalization can erase its endpoint. Other invalid Reference Object kinds
retain the separately measured `unresolved-reference` classification. It does
not read Fern's source or repair missing declarations.

The CLI journey [was observed failing before this detector](evaluation-logs/refusal-e2e-red.log):
the probe generated 35 files instead of refusing. Adding the missing parameter
component restores generation with byte-identical SDKs in both modes.
[All three population documents](evaluation-logs/population-refusals.jsonl)
were retrieved at their digests and refused in both modes with exit 1, no
files, one class/element line and the strict cause when applicable.

The third population member, Paychex
`cdf32573a9a65a8ed9007c222224b1b07b382365d44fe1764566ee0b776bca17`,
carries a named Example Reference Object pointing into
`#/components/examples/JSONEXAMPLES/value/COMPANIES_GET`. This JSON Pointer
exists, but Fern fails to import it with the same `is undefined` diagnostic.
The manager authorized this component-reference case after the initial
parameter-only detector missed it; Reference Object checks precede subsequent
parameter-use checks so its class is not masked.

A [hand-written isolated probe](named-example-probe.yml) and its
[direct-example control](named-example-control.yml) establish the boundary.
The [pinned Fern check/generation log](evaluation-logs/fern-named-example.log)
prints the undefined diagnostic and writes a false-success empty SDK for the
probe; the control passes and writes 31 Python files. Its extra
[Contract A record](named-example-fern-refusal.txt) records that measured result.

Crozier's [baseline output on the extra probe](evaluation-logs/named-example-baseline.log)
imports and has **zero mypy errors**. Its [wire journey](evaluation-logs/named-example-baseline.wire.log)
sends `GET /companies` and parses `companies: [ACME]` faithfully. That extra
probe alone is valid output; the original missing-parameter probe and the
Jumpseller population still disqualify the class as a whole under the task's
rule, so its status remains `refuse` with no SDK repairs.

The additional CLI journey refuses the nested Example Reference Object in
both modes and restores byte-identical output with the direct-example control.
It also generates when `$ref` is ordinary data inside an example's `value`,
which is never traversed as a Reference Object. Its refusal assertion was
[observed failing with this detector disabled](evaluation-logs/named-example-e2e-induced-red.log)
before the mutation was reverted.

The strict corpus identified api.video's accepted SDK as a control for unused
parameter definitions: `components.parameters.filterBy` points to absent
`filterBy_2`, but no operation binds that alias. The detector now checks bound
parameter Reference Objects rather than every unused parameter component.
An added CLI recovery assertion [failed before that restriction](evaluation-logs/unused-parameter-alias-e2e-red.log);
adding an unused dangling alias now preserves generation. Unused component
examples are likewise not traversed; actual named Example Reference Objects
on operations supply the measured boundary.

A missing top-level named example component follows the same measured
undefined-component diagnostic: [Fern check](evaluation-logs/fern-missing-example.log)
prints `#/components/examples/AbsentExample is undefined`, despite exit zero.
The CLI journey now covers that missing target as well as the nested target;
[disabling only the missing-target branch made it fail](evaluation-logs/missing-example-e2e-induced-red.log)
with 38 generated files. Restoring the branch refuses both modes, and the
existing direct-example control proves recovery.
