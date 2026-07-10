# Changelog

All notable changes to this project are documented here. This file is maintained
by [release-plz](https://github.com/release-plz/release-plz) from Conventional
Commit messages; do not edit released sections by hand.

## [Unreleased]

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
