# named-type-default: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), with zero
mypy errors. Its unused `ticket` model declares `type` as a string enum with
value and default `ticket`. The generated annotation instead names the
independent `ticket_type` object. The [public model boundary](evaluation-logs/probe.wire.log)
rejects the declared string with a `ValidationError`; the independent object
still parses `id`. No endpoint declares a `ticket` request, so this field has
no HTTP sending journey in the probe; it already fails parsing its declared
value. This class is `refuse` even though the probe's mypy check succeeds.

One representative, [Intercom 2.14,
`1409a459eaaf9cc95b1c87dce2083d4b0c0ff0bd85459cc19fd0b2171b06d5bb`](evaluation-logs/population.log),
imports the package and root client, but mypy reports **four errors in one
file**, exits 2 and stops further checking. Its [ticket journey](evaluation-logs/population.wire.log)
cannot import the ticket subclient: an unrelated enum repeats `_`, raising
`TypeError`. Consequently no request is sent and no response returned. The
public `Ticket` model can be imported separately, but rejects a declared
response `{id: TICKET-1, type: ticket}`: it too annotates `type` as the unrelated
object `TicketType`. These are observed baseline failures, not repaired or
hidden to rescue the class. The population is Intercom versions and mirrors;
one API publisher is represented.

The detector follows declaration order and existing naming functions. It
checks enum/constant field defaults whose imported declaration is replaced by
an object or union. Pinned Fern refuses the [object collision](fern-refusal.txt),
[union collision](evaluation-logs/fern-union-declaration.log) and
[multiple-value collision](evaluation-logs/fern-multiple-values-collision.log).
It accepts [renaming the independent model](evaluation-logs/fern-renamed-model.log),
[removing the default](evaluation-logs/fern-no-default.log),
[a null default](evaluation-logs/fern-null-default.log),
[a string declaration](evaluation-logs/fern-string-declaration.log),
[an enum declaration](evaluation-logs/fern-enum-declaration.log), and
[an explicit string type on the union declaration](evaluation-logs/fern-typed-union-declaration.log).
A [reversed, unused declaration](evaluation-logs/fern-reversed-unused.log)
also succeeds: the later inline enum replaces the earlier object, so the
default no longer belongs to an object declaration.

Defaults attached to ordinary [named strings](evaluation-logs/fern-named-string.log),
[named objects](evaluation-logs/fern-named-object.log),
[named enums](evaluation-logs/fern-named-enum.log),
[inline objects](evaluation-logs/fern-inline-object.log),
[inline unions](evaluation-logs/fern-inline-union.log),
[maps](evaluation-logs/fern-inline-map.log) and
[root objects](evaluation-logs/fern-root-object.log) also generate. The CLI
journey preserves these controls and compares their SDK bytes in both modes;
it also exercises an ignored source schema.

The [population log](evaluation-logs/population-refusals.jsonl) covers all ten
retrievable documents in both modes: exit 1, no files, one line identifying
the class and `ticket/properties/type/default`, with `fern-strict` as the
strict-mode cause. The run uses a preserved build of the finished detector.

The [CLI assertion fails with only the named-default predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 39 files for the probe instead of refusing. This evidence intentionally
records an induced earlier state; the predicate is restored in the finished source.
