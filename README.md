# crozier

An ultra-fast, memory-efficient OpenAPI-to-SDK code generator written in Rust +
[minijinja](https://github.com/mitsuhiko/minijinja). crozier reproduces
[Fern](https://github.com/fern-api/fern)'s generated SDKs **byte-for-byte** (with
generator-identifying comments aside), driven by nothing but an OpenAPI document
and a couple of naming flags — no per-project config, no generators written in the
target language.

Python is the only target today; more will follow.

> **Status:** early. crozier generates the Python **type layer** (pydantic models,
> enums, unions/aliases) plus `version.py`/`py.typed`, and byte-matches Fern's
> output for those files. See [`docs/matching.md`](docs/matching.md) for exactly
> what is matched and the roadmap.

## Install

**From PyPI (fastest — a prebuilt binary, no Rust toolchain):** crozier ships as
platform wheels that wrap the compiled binary and expose it as a console script,
so any Python installer puts it on your `PATH` in seconds:

```sh
pip install crozier      # or: pipx install crozier
uvx crozier --help       # run once without installing
```

Platforms without a prebuilt wheel fall back to the source distribution, which
builds from Rust (a toolchain is needed there).

**From crates.io:**

```sh
cargo install crozier --locked
```

**From the install script (prebuilt binary from GitHub Releases, verified):**

```sh
curl -fsSL https://raw.githubusercontent.com/nickderobertis/crozier/main/scripts/install.sh | sh
```

It detects your platform, downloads the matching archive, and verifies it against
a trust root independent of where it was downloaded — a Sigstore build-provenance
attestation when a verifier (`cosign`, `pip install sigstore`, or `gh`) is
present, else the canonical SHA-256 checksum. Pin a version or install location
with `sh -s -- --version v0.1.0 --to ~/.local/bin`.

**From source (latest `main`):**

```sh
cargo install --git https://github.com/nickderobertis/crozier --locked
```

**From a release archive (manual):** each release publishes per-platform archives
named `crozier-<tag>-<target>.tar.gz` with a matching `.sha256` and a
`.sigstore.json` provenance bundle, for targets `x86_64`/`aarch64` Linux,
`x86_64`/`aarch64` macOS, and `x86_64` Windows. Download the archive for your
platform from the
[Releases](https://github.com/nickderobertis/crozier/releases) page, verify the
checksum (or the attestation), and put the `crozier` binary on your `PATH`.

## Usage

```sh
crozier generate \
  --spec path/to/openapi.yml \
  --output ./generated \
  --package-name my_api \
  --project-name my-api
```

- `--spec` — the OpenAPI 3.x document (`.yml`, `.yaml`, or `.json`).
- `--output` — directory to write the SDK into.
- `--package-name` — the Python import package (the directory under `src/`).
  Defaults to a `snake_case` of the API title.
- `--project-name` — the distribution name recorded in `version.py`. Defaults to
  the package name.

crozier exits `0` on success (with a one-line summary on stderr) and `1` on any
error, printing the exact problem and a suggested fix.

## Development

The command surface is a small set of `just` recipes:

```sh
just bootstrap   # set up from a clean clone (toolchain + dev tools)
just check       # full gate: fmt, clippy -D warnings, tests + e2e + coverage, deny, machete, doc
just test        # fast tests with coverage enforced (95%)
just test-e2e    # drive the compiled binary and byte-compare against fixtures
just format      # rustfmt in place
just upgrade     # cargo update, then re-run the gate
```

See [`AGENTS.md`](AGENTS.md) for the durable contributor guide and
[`docs/matching.md`](docs/matching.md) for the byte-matching strategy.

## License and attribution

crozier is licensed under [Apache-2.0](LICENSE). It is an independent, clean-room
implementation — it reproduces Fern's generated *output* format (the project's
explicit goal) and does not copy Fern's generator source.

The test fixtures under `tests/fixtures/` are Fern's own output and OpenAPI test
specs, used under Apache-2.0 with attribution and a statement of changes; see
[`NOTICE`](NOTICE) and [`licenses/fern-APACHE-2.0.txt`](licenses/fern-APACHE-2.0.txt).
