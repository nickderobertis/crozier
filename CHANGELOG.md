# Changelog

All notable changes to this project are documented here. This file is maintained
by [release-plz](https://github.com/release-plz/release-plz) from Conventional
Commit messages; do not edit released sections by hand.

## [Unreleased]

## [0.0.7](https://github.com/nickderobertis/crozier/compare/v0.0.6...v0.0.7) - 2026-07-11

### Added

- byte-match generation for auth, discriminated unions, integer enums, schema constraints, and form bodies ([#31](https://github.com/nickderobertis/crozier/pull/31))

## [0.0.6](https://github.com/nickderobertis/crozier/compare/v0.0.5...v0.0.6) - 2026-07-10

### Fixed

- stop emitting an empty errors import and prune stale modules on regeneration ([#28](https://github.com/nickderobertis/crozier/pull/28))

## [0.0.5](https://github.com/nickderobertis/crozier/compare/v0.0.4...v0.0.5) - 2026-07-10

### Added

- complete the client layer, aggregators, and docs (exhaustive fully matches Fern) ([#25](https://github.com/nickderobertis/crozier/pull/25))

## [0.0.4](https://github.com/nickderobertis/crozier/compare/v0.0.3...v0.0.4) - 2026-07-10

### Added

- complete the raw-client endpoint layer, errors, and scaffolding ([#23](https://github.com/nickderobertis/crozier/pull/23))

## [0.0.3](https://github.com/nickderobertis/crozier/compare/v0.0.2...v0.0.3) - 2026-07-10

### Added

- widen raw_client.py to query/header params and scalar/enum/union bodies ([#21](https://github.com/nickderobertis/crozier/pull/21))

## [0.0.2](https://github.com/nickderobertis/crozier/compare/v0.0.1...v0.0.2) - 2026-07-10

### Added

- emit per-tag raw_client.py for no-request-body endpoints ([#18](https://github.com/nickderobertis/crozier/pull/18))

## [0.0.1](https://github.com/nickderobertis/crozier/compare/v0.0.0...v0.0.1) - 2026-07-10

### Fixed

- ship assets/ in the published crate so cargo publish builds ([#15](https://github.com/nickderobertis/crozier/pull/15))

## [0.0.0](https://github.com/nickderobertis/crozier/releases/tag/v0.0.0) - 2026-07-10

### Added

- parse paths and emit endpoint package markers ([#11](https://github.com/nickderobertis/crozier/pull/11))
- vendor and emit Fern's core/ SDK runtime ([#10](https://github.com/nickderobertis/crozier/pull/10))
- publish to crates.io and PyPI (maturin wheels) on release ([#6](https://github.com/nickderobertis/crozier/pull/6))
- hoist inline oneOf/allOf schemas to complete the type layer ([#8](https://github.com/nickderobertis/crozier/pull/8))
- reproduce ruff's line wrapping to match Fern's wide lines ([#7](https://github.com/nickderobertis/crozier/pull/7))
- match Fern's OpenAPI type conventions across the type layer ([#5](https://github.com/nickderobertis/crozier/pull/5))
- Python type-layer generation, CLI, gate, CI, and releasing

### Fixed

- separator-agnostic coverage exclude and cover uniqueItems/anyOf/json paths

### Other

- commit exhaustive Fern fixture and byte-match 8 files ([#3](https://github.com/nickderobertis/crozier/pull/3))
- vendor exhaustive openapi.yml and add fixtures provenance README
- add aggregation gate job and simplify llmlint context
- scaffold crozier repo, pipeline, and first byte-exact fixture match
