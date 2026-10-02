# Fern refusal registry

The classes of input Fern (CLI 5.67.1, `fernapi/fern-python-sdk` 5.20.0)
refuses, crashes on, or falsely reports success over, and what crozier does with
each. crozier's default is to generate wherever its output is valid and useful;
`fern-strict` refuses as Fern does. This directory is the one statement of which inputs that covers. The gate
(`tests/e2e.rs::fern_refusal_classes_hold`, in `just check`) reads it, and
nothing but the steps below writes it.

## The contract

**The setting.** `fern-strict` (default `false`) layers like `audience-strict`:
`--fern-strict` on `crozier generate`, `CROZIER_FERN_STRICT`, and `fern-strict`
at the config's top level or under `generators.<name>`. Strict mode only ever
decides whether an SDK is written, never a byte of one that is.

**A refusal**, in either mode, exits 1, writes nothing to the output directory,
and prints one stderr line naming the class id, the offending element (its
method and route, and the parameter, property, schema, enum value or scheme
name, or its JSON pointer) and, for a strict-mode refusal, that `fern-strict`
caused it.

**The files.**

- [`classes.tsv`](classes.tsv) — one row per class, sorted by `class`:
  `class` (kebab-case id), `family` (`names` for a diagnostic about a name Fern
  cannot form or that collides with another; `documents` for every other),
  `fern_stage` (`check` or `generate`), `fern_exit`, `diagnostic` (Fern's phrase
  verbatim, document-specific parts written `<…>`), `documents` (how many
  `documents.tsv` rows carry it), `status` (`unevaluated`, `generate` or
  `refuse`), `crozier_diagnostic` (the literal substring crozier's refusal line
  must contain; `—` while `unevaluated`), `population_strict`
  (`<refused>/<total>` over the retrievable documents carrying the class; `—`
  while `unevaluated`).
- [`documents.tsv`](documents.tsv) — one row per distinct refused document,
  sorted by `digest` (lower-hex SHA-256 of its exact bytes): `source`,
  `locator`, `revision` (immutable), `recorded_by` (the committed records naming
  the refusal, `;`-separated), `fern_stage`, `fern_exit`, `fern_log` (the
  committed log holding Fern's complete diagnostic list), `classes`
  (`,`-separated, never empty), `crozier_exit`, `crozier_files` (crozier's
  release build, default mode), `crozier_strict_exit` (the same build under
  `--fern-strict`; `—` until one of the document's classes is evaluated). All
  three come from `measurements.jsonl`, which `just fern-refusals-measure`
  fills, so `build` reproduces them.
- [`unretrievable.tsv`](unretrievable.tsv) — a selected document whose bytes
  could not be read again, with its revision and the reason.
- [`generated.tsv`](generated.tsv) — a selected document whose `fern check`
  failed but whose `fern generate` at the pin still writes an SDK, with its log
  and the check-only phrases it printed. Fern produces output for these, so
  crozier is expected to byte-match them, not refuse them: this is a candidate
  list the witness-registration work may screen, and nothing here registers one.
- [`findings.tsv`](findings.tsv) — shapes measured and found **not** to be
  refusals, each with its probe under
  [`../openapi-surface/fern-refusals/findings/`](../openapi-surface/fern-refusals/findings/):
  `check-only` phrases `fern check` refuses while `fern generate` writes an SDK
  past them, and `generates` shapes neither stage objects to. A `generates`
  finding whose naming crozier is held to keeps Fern's comment-stripped tree
  under [`../openapi-surface/fern-refusals/finding-trees/<finding>/`](../openapi-surface/fern-refusals/finding-trees/),
  built the way [the probes'](../openapi-surface/probes/AGENTS.md#re-running-one)
  are. `tests/e2e.rs::generates_findings_byte_match_their_fern_trees` (in
  `just check`) byte-compares crozier against it over the finding's probe in
  both modes. These trees are probe evidence, never a real-specification match.
- `<class>/probe.yml` — a minimal hand-written document isolating the class.
- `<class>/fern-refusal.txt` — Fern's measured outcome on the probe in Contract
  A's five fields (`fern_cli_version`, `fern_python_sdk_version`,
  `generate_exit`, `diagnostic`, `output_tree`). A false success records
  `generate_exit: 0` with the stderr phrase. A shape Fern turns out to generate
  from is no refusal class and is not recorded here.
- `<class>/evaluation.md` — once evaluated: whether crozier's default output
  imports, its `mypy` error count under the generated `pyproject.toml`'s own
  configuration, and what it sends and parses at the offending element against
  what the document declares, each linked to a committed log.
- `<class>/wire_test.py` — exactly when `status` is `generate`: a pytest module
  run against crozier's default SDK for the probe. The gate generates that SDK
  with `--package-name fern`, installs what its `pyproject.toml` declares (the
  pinned `mypy` among it), and runs the module with `CROZIER_SDK_DIR` (the SDK
  root), `CROZIER_SDK_SRC` (its `src/`) and `CROZIER_PROBE` set. It asserts that
  the package imports, that `mypy .` in the SDK root reports zero errors, and,
  through an injected `httpx.MockTransport` as `tests/runtime/` does, that the
  request at the offending element carries exactly the wire names and values the
  probe declares and that a declared response parses into its declared model.

**The gate** fails when a row's `probe.yml` or `fern-refusal.txt` is missing,
the record's versions differ from the pin or its `diagnostic` is empty; when a
`refuse` class's probe is not refused (as above) with and without
`--fern-strict`, or its line lacks `crozier_diagnostic`; when a `generate`
class's probe does not generate by default, its `wire_test.py` fails, or it is
not refused under `--fern-strict` with such a line; and when a `documents.tsv`
class id or a directory here is no `classes.tsv` row. An `unevaluated` row is
checked for its files only. `fern_refusal_classes_hold` checks every condition
but the `wire_test.py` run in the offline `just check`; that one builds the
SDK's environment from PyPI, so `sdk_env_fern_refusal_wire_tests_hold` runs the
whole gate in `just test-sdk-env` (CI's `sdk-env` job, required by `gate`).

**No false refusals.** `just test-corpus-match-strict` runs the corpus
byte-match with `CROZIER_FERN_STRICT=true`, so a class that refuses a document
Fern generates from fails it.

## The population

Every document crozier's committed records name as refused, crashed on or
falsely reported successful by Fern: the `DROPPED` rows of
`tests/fixtures/CORPUS.md` whose reason names Fern (located by
[`dropped-sources.tsv`](../openapi-surface/fern-refusals/dropped-sources.tsv)),
and every `docs/openapi-surface/**/screens.jsonl` record whose `fern` verdict is
`failed:` or `refused:`. Deduplicated by digest. A served APIs.guru document no
immutable commit holds is pinned by its recorded digest (`revision` is
`sha256:<digest>`). `fern-docs-fai`'s row drops every revision of one document
by a rule rather than a list, so the population carries the revision
`dropped-sources.tsv` names for it. Fourteen `DROPPED` rows name a document
without ever recording the ref that was screened; they are in
`unretrievable.tsv` with what later searches did record, and the ref the
`letta` row names answers 404.

A document is **refused** when its `fern generate` exits non-zero, writes
nothing, or reports a refusal class over a document it did not parse (a false
success). Its classes are the ones its `fern check` names when the check names
any (`fern_stage` `check`), else the ones its generation names (`generate`).
A document's generate outcome is **derived from its classes**, not measured
document by document: each class's probe shows whether its phrase stops
`fern generate` (a phrase that does not is a `check-only` finding), so a
document whose check names a class is refused, and one whose check names only
check-only findings goes to `generated.tsv`. `fern generate` was run on a
document only where its check named no class (a check that passed, or one that
reported a document it could not parse); those per-document results are kept in
`measurements.jsonl`. The derivation is confirmed on the population: `confirm`
runs `fern generate` on up to three real documents per class — documents
carrying only that class first, from different publishers where they exist —
into
[`confirmations.tsv`](../openapi-surface/fern-refusals/confirmations.tsv), and
`check` fails if any of them generates where its class says Fern refuses.

`scripts/fern-refusals.py` builds the tables:

```sh
scripts/fern-refusals.py select            # the population, offline
just fern-refusals-measure                 # rebuild the release binary, then measure: fetch, run Fern and crozier (network, Docker)
scripts/fern-refusals.py build             # rewrite documents.tsv, generated.tsv, unretrievable.tsv, class counts
scripts/fern-refusals.py confirm           # sample each class's real documents through fern generate
scripts/fern-refusals.py check             # offline drift check; tests/fern_refusals_test.py runs it
```

`measure` fetches through `scripts/rate_limit_guard.py`'s paced raw lane,
reuses a committed screen's `fern check` log where its record states the exit,
and otherwise runs `fern check` — then `fern generate` unless the check named a
class — in a scratch workspace outside any checkout, writing each log to
[`../openapi-surface/fern-refusals/logs/`](../openapi-surface/fern-refusals/logs/)
and the result to `measurements.jsonl` beside it. Fern runs with a 16 GB Node
heap: at the default 4 GB the largest documents (the GitHub REST descriptions)
report the host's memory rather than Fern's diagnostics. Every
`documents.tsv` row's `crozier_exit` and `crozier_files` were last re-measured
by the release build after `main`'s `layout` setting merged, each run bounded at
45 minutes and none reaching it: [`crozier-timings.tsv`](../openapi-surface/fern-refusals/crozier-timings.tsv)
keeps each document's size, outcome and wall-clock seconds from that run, taken
with up to eighteen measurement runs at once on a shared, loaded host. `build` classifies
every diagnostic in a document's logs against `classes.tsv`'s and
`findings.tsv`'s templates; one that matches no single template fails the
build, so a new phrase becomes a class or a finding on purpose.

`probe <class>…` measures Fern on a class's probe (`fern check`, then
`fern generate` whatever the check said) and writes its `fern-refusal.txt` and
the class's `fern_stage`/`fern_exit`, refusing to record a probe Fern generates
from; `finding <name>…` does the same for `findings.tsv`, refusing a probe Fern
refuses. Both keep Fern's logs under
[`../openapi-surface/fern-refusals/probe-logs/`](../openapi-surface/fern-refusals/probe-logs/).

## What the measurement settled

- **GitHub's duplicate request names** are `request-property-name-collision`:
  a path parameter and a body property both called `name`.
- **`appng-rest-api`** does not fail after a passing check at the pin: its
  `fern check` exits 1 with `Service requires auth, but no auth is defined.`,
  because its only security scheme is an `apiKey` in a cookie, which Fern does
  not import (`service-auth-undefined`). `CORPUS.md`'s reason predates the pin.
- **Enum members led by a digit** (`1st` → `ONE_ST`) **or a zero-led digit run**
  (`007` → `SEVEN`) are generated by Fern, and crozier emits the same members:
  both are `generates` findings. What Fern refuses is a member it can name no
  way (`enum-value-unnameable`, e.g. `10080`) or names with a leading digit
  (`enum-name-unsuitable`, e.g. `#0094FF` → `0094Ff`).
- **A component's declared type name, a `construct` property and an
  operationId that only repeats its tag** (`Search_` under `Search`) are
  generated by Fern, so they are `generates` findings with committed trees, not
  refusals. Fern names the component by its declaration, renames the field
  `construct_` under an alias, and hoists `search` to the root client
  ([`../matching.md`](../matching.md#three-naming-shapes-measured-on-probes-not-real-specifications)).
- **A security scheme `$ref` into another document** is `unresolved-reference`,
  a false success: `fern check` and `fern generate` exit 0 over a document Fern
  never parsed. With the referenced document placed beside the probe,
  `fern check` resolves it and passes, so the class is a reference Fern cannot
  follow, not the scheme.
- **The generator's own crashes** are classes too, measured in `fern generate`
  after a clean check: `generator-lint-failure` (the generated package fails
  `ruff check`, e.g. two union variants or a method and a sub-client given one
  Python name), `generator-missing-type` (a `KeyError` over a type Fern named
  but never emitted, e.g. an inline enum header), and
  `generated-file-name-too-long`. The `Failed to format …` lines printed before
  a lint failure only say which snippet did not parse; they were never seen
  without the failure they precede. `heap-exhausted` is Fern's check running
  out of a 16 GB heap on a document a few hundred kilobytes long.
- **Contract A's refusal rows** (`header-array`, `header-object`,
  `nonascii-operationId`, `ref-pointer-unnamed-segment` in
  [`../openapi-surface/probe-expected/MANIFEST.tsv`](../openapi-surface/probe-expected/MANIFEST.tsv))
  stay there. Where a phrase class would share one's shape, its probe isolates
  the phrase another way: `type-name-not-letter-led` names a schema `123456`
  rather than `$ref`ing an unnamed pointer segment, and `example-type-mismatch`
  is probed with a date rather than a header list.
