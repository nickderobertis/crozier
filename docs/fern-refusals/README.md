# Fern refusal registry

The classes of input Fern (CLI 5.67.1, `fernapi/fern-python-sdk` 5.20.0)
refuses, crashes on, or falsely reports success over, and what crozier does with
each. crozier's default is to generate wherever its output is valid and useful;
[`fern-strict`](../configuration.md#strict-fern-compatibility) refuses as Fern
does. This directory is the one statement of which inputs that covers. The gate
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
  release build, default mode), `crozier_strict_exit` (`—` until the class is
  evaluated).
- [`unretrievable.tsv`](unretrievable.tsv) — a selected document whose bytes
  could not be read again, with its revision and the reason.
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
checked for its files only.

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
`dropped-sources.tsv` names for it.

`scripts/fern-refusals.py` builds the tables:

```sh
scripts/fern-refusals.py select            # the population, offline
cargo build --release --locked
scripts/fern-refusals.py measure           # fetch, run Fern and crozier (network, Docker)
scripts/fern-refusals.py build             # rewrite documents.tsv, unretrievable.tsv, classes.tsv counts
scripts/fern-refusals.py check             # offline drift check; tests/fern_refusals_test.py runs it
```

`measure` fetches through `scripts/rate_limit_guard.py`'s paced raw lane,
reuses a committed screen log where it holds the failing stage's complete list,
and otherwise runs `fern check` (then `fern generate` where the check exits 0
cleanly) in a scratch workspace outside any checkout, writing the log to
[`../openapi-surface/fern-refusals/logs/`](../openapi-surface/fern-refusals/logs/)
and the result to `measurements.jsonl` beside it. `build` finds each document's
classes by matching every diagnostic in its log against `classes.tsv`'s
`diagnostic` templates; a diagnostic no template matches fails the build, so a
new phrase becomes a class on purpose.
