# Changelog

All notable changes to this project are documented here. This file is maintained
by [release-plz](https://github.com/release-plz/release-plz) from Conventional
Commit messages; do not edit released sections by hand.

## [Unreleased]

## [0.0.38](https://github.com/nickderobertis/crozier/compare/v0.0.37...v0.0.38) - 2026-07-19

### Other

- *(fixtures)* byte-match 3 composition corpora + drop appng dud (full parity) ([#124](https://github.com/nickderobertis/crozier/pull/124))

## [0.0.37](https://github.com/nickderobertis/crozier/compare/v0.0.36...v0.0.37) - 2026-07-19

### Other

- *(fixtures)* byte-match 7 batch-4 corpora to Fern goldens (full parity) ([#121](https://github.com/nickderobertis/crozier/pull/121))

## [0.0.36](https://github.com/nickderobertis/crozier/compare/v0.0.35...v0.0.36) - 2026-07-19

### Fixed

- legalize digit-leading schema names; add parameter serialization c… ([#119](https://github.com/nickderobertis/crozier/pull/119))

## [0.0.35](https://github.com/nickderobertis/crozier/compare/v0.0.34...v0.0.35) - 2026-07-18

### Other

- *(dev)* warm new worktrees via post-checkout sccache ([#115](https://github.com/nickderobertis/crozier/pull/115))

## [0.0.34](https://github.com/nickderobertis/crozier/compare/v0.0.33...v0.0.34) - 2026-07-18

### Other

- register HTTP Toolkit corpus fixture; Add ONE new real-world Open… ([#113](https://github.com/nickderobertis/crozier/pull/113))

## [0.0.33](https://github.com/nickderobertis/crozier/compare/v0.0.32...v0.0.33) - 2026-07-17

### Other

- dogfood Redocly Museum Fern fixture ([#110](https://github.com/nickderobertis/crozier/pull/110))

## [0.0.32](https://github.com/nickderobertis/crozier/compare/v0.0.31...v0.0.32) - 2026-07-16

### Added

- byte-match Batch 5 OpenAPI corpora ([#107](https://github.com/nickderobertis/crozier/pull/107))

## [0.0.31](https://github.com/nickderobertis/crozier/compare/v0.0.30...v0.0.31) - 2026-07-16

### Added

- register Batch 4 OpenAPI corpora ([#106](https://github.com/nickderobertis/crozier/pull/106))
- byte-match Batch 3 OpenAPI corpora ([#104](https://github.com/nickderobertis/crozier/pull/104))

## [0.0.30](https://github.com/nickderobertis/crozier/compare/v0.0.29...v0.0.30) - 2026-07-15

### Other

- *(e2e)* add 8 batch-2 byte-match corpora (2 dropped: Fern can't generate) ([#101](https://github.com/nickderobertis/crozier/pull/101))

## [0.0.29](https://github.com/nickderobertis/crozier/compare/v0.0.28...v0.0.29) - 2026-07-14

### Other

- *(e2e)* add five more real-world corpora (issue #77), all byte-matched ([#99](https://github.com/nickderobertis/crozier/pull/99))

## [0.0.28](https://github.com/nickderobertis/crozier/compare/v0.0.27...v0.0.28) - 2026-07-13

### Added

- add bungie.net as the third real-world corpus, fully byte-matched (1082/1082) ([#97](https://github.com/nickderobertis/crozier/pull/97))

## [0.0.27](https://github.com/nickderobertis/crozier/compare/v0.0.26...v0.0.27) - 2026-07-13

### Added

- fully byte-match the bunq.com real-world corpus ([#95](https://github.com/nickderobertis/crozier/pull/95))

## [0.0.26](https://github.com/nickderobertis/crozier/compare/v0.0.25...v0.0.26) - 2026-07-13

### Added

- spec-driven live-e2e mock-server suite and enforced real-world byte-match (apideck) ([#92](https://github.com/nickderobertis/crozier/pull/92))

## [0.0.25](https://github.com/nickderobertis/crozier/compare/v0.0.24...v0.0.25) - 2026-07-12

### Fixed

- handle recursive schemas, nested-type core import depth, and malformed property nodes ([#88](https://github.com/nickderobertis/crozier/pull/88))

## [0.0.24](https://github.com/nickderobertis/crozier/compare/v0.0.23...v0.0.24) - 2026-07-12

### Other

- generate issue 77 fixtures from source links

## [0.0.23](https://github.com/nickderobertis/crozier/compare/v0.0.22...v0.0.23) - 2026-07-12

### Added

- honor x-crozier-ignore/x-fern-ignore and accept both extension spellings ([#80](https://github.com/nickderobertis/crozier/pull/80))

## [0.0.22](https://github.com/nickderobertis/crozier/compare/v0.0.21...v0.0.22) - 2026-07-12

### Fixed

- sanitize non-identifier request-body/query property names ([#75](https://github.com/nickderobertis/crozier/pull/75))

## [0.0.21](https://github.com/nickderobertis/crozier/compare/v0.0.20...v0.0.21) - 2026-07-12

### Other

- showcase the CLI with screencomp-gated terminal screenshots ([#72](https://github.com/nickderobertis/crozier/pull/72))

## [0.0.20](https://github.com/nickderobertis/crozier/compare/v0.0.19...v0.0.20) - 2026-07-12

### Added

- add --extra-fields for pydantic extra behavior ([#70](https://github.com/nickderobertis/crozier/pull/70))

## [0.0.19](https://github.com/nickderobertis/crozier/compare/v0.0.18...v0.0.19) - 2026-07-12

### Added

- layered config with named generators, JSON Schema, and init/config/schema commands ([#68](https://github.com/nickderobertis/crozier/pull/68))

## [0.0.18](https://github.com/nickderobertis/crozier/compare/v0.0.17...v0.0.18) - 2026-07-12

### Added

- add --client-class-name to override the root client class ([#65](https://github.com/nickderobertis/crozier/pull/65))

## [0.0.17](https://github.com/nickderobertis/crozier/compare/v0.0.16...v0.0.17) - 2026-07-12

### Added

- add --audience-strict for exclusive audience subsetting ([#64](https://github.com/nickderobertis/crozier/pull/64))

## [0.0.16](https://github.com/nickderobertis/crozier/compare/v0.0.15...v0.0.16) - 2026-07-12

### Fixed

- escape enum visit() param colliding with self receiver ([#57](https://github.com/nickderobertis/crozier/pull/57)) ([#58](https://github.com/nickderobertis/crozier/pull/58))

## [0.0.15](https://github.com/nickderobertis/crozier/compare/v0.0.14...v0.0.15) - 2026-07-12

### Fixed

- emit Annotated discriminated-union alias; bump corpus to Fern 4.35.0 (issue #50) ([#55](https://github.com/nickderobertis/crozier/pull/55))

## [0.0.14](https://github.com/nickderobertis/crozier/compare/v0.0.13...v0.0.14) - 2026-07-11

### Fixed

- sanitize enum member and visit() names (issue #50) ([#53](https://github.com/nickderobertis/crozier/pull/53))

## [0.0.13](https://github.com/nickderobertis/crozier/compare/v0.0.12...v0.0.13) - 2026-07-11

### Added

- close Fern-python parity gaps from #41 (tag grouping, real enums, audience filtering) ([#47](https://github.com/nickderobertis/crozier/pull/47))

## [0.0.12](https://github.com/nickderobertis/crozier/compare/v0.0.11...v0.0.12) - 2026-07-11

### Added

- close issue #43 gaps — error responses and SSE streaming ([#45](https://github.com/nickderobertis/crozier/pull/45))

## [0.0.11](https://github.com/nickderobertis/crozier/compare/v0.0.10...v0.0.11) - 2026-07-11

### Added

- generate valid clients for real-world specs (issue #40) ([#42](https://github.com/nickderobertis/crozier/pull/42))

## [0.0.10](https://github.com/nickderobertis/crozier/compare/v0.0.9...v0.0.10) - 2026-07-11

### Added

- close the four remaining Fern parity gaps (basic auth, oauth, inline-array bodies, writeOnly ordering) ([#37](https://github.com/nickderobertis/crozier/pull/37))

## [0.0.9](https://github.com/nickderobertis/crozier/compare/v0.0.8...v0.0.9) - 2026-07-11

### Added

- close remaining Fern parity gaps (inline hoisting, cookie params, environments) ([#35](https://github.com/nickderobertis/crozier/pull/35))

## [0.0.8](https://github.com/nickderobertis/crozier/compare/v0.0.7...v0.0.8) - 2026-07-11

### Other

- delegate formatting to ruff and move presentational rendering to templates ([#33](https://github.com/nickderobertis/crozier/pull/33))

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
