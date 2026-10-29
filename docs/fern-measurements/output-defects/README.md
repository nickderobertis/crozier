# Generated-output defects, settled against Fern

Each row below is a crozier issue that the last run's follow-up pass filed. Each
was screened for whether it concerns the SDK crozier generates. Each one that
does is settled against the certified pair (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3, declared in
[`assets/scaffolding/metadata.json`](../../../assets/scaffolding/metadata.json)).

The verdicts:

- `parity-gap-repaired`: crozier differed from a non-defective Fern output and
  now matches it.
- `shared-defect-departed`: both generators wrote a defect of a standing kind,
  and crozier departs under a catalogued
  [`assets/departures.yml`](../../../assets/departures.yml) entry.
- `shared-defect-awaiting-ruling`: both share a defect outside the standing
  kinds, and output is unchanged until the user rules.
- `not-generated-output`: the issue concerns crozier's tooling, tests or CLI
  rather than a generated SDK.

The issues stay at Proposal. This index records the decision and closes none.

| issue | generated output | verdict | record | outcome |
|---|---|---|---|---|
| [#598](https://github.com/nickderobertis/crozier/issues/598) | no: `crozier config`'s report panicking on a closed pipe is CLI output, not an SDK | not-generated-output | — | Left to its own repair. |
| [#599](https://github.com/nickderobertis/crozier/issues/599) | no: combination-reach sites are coverage bookkeeping | not-generated-output | — | Left to its own repair. |
| [#600](https://github.com/nickderobertis/crozier/issues/600) | no: the compared-golden inventory is test registration | not-generated-output | — | Left to its own repair. |
| [#601](https://github.com/nickderobertis/crozier/issues/601) | no: a stale binary under the e2e harness is a test-runner concern | not-generated-output | — | Left to its own repair. |
| [#602](https://github.com/nickderobertis/crozier/issues/602) | yes: raw-response parsing in the generated client caught an unbound `ValidationError` | parity-gap-repaired | [`602-validation-error-shadowing/`](602-validation-error-shadowing/README.md) | crozier catches `pydantic_ValidationError` as Fern does, so a response failing validation raises `ParsingError`. |
| [#603](https://github.com/nickderobertis/crozier/issues/603) | no: golden regeneration's source acquisition is reference tooling | not-generated-output | — | Left to its own repair. |
| [#604](https://github.com/nickderobertis/crozier/issues/604) | no: lane concurrency in the refusal tooling's tests | not-generated-output | — | Left to its own repair. |
| [#605](https://github.com/nickderobertis/crozier/issues/605) | no: the departure-ledger refresh is test tooling | not-generated-output | — | Left to its own repair. |
| [#606](https://github.com/nickderobertis/crozier/issues/606) | no: the witness-search response cache is discovery tooling | not-generated-output | — | Left to its own repair. |
| [#607](https://github.com/nickderobertis/crozier/issues/607) | no: an interpreter path in an offline-recovery test | not-generated-output | — | Left to its own repair. |
| [#608](https://github.com/nickderobertis/crozier/issues/608) | no: merging partial ledger recordings is test tooling | not-generated-output | — | Left to its own repair. |
| [#609](https://github.com/nickderobertis/crozier/issues/609) | no: symbolic links in reference imports are reference tooling | not-generated-output | — | Left to its own repair. |
| [#610](https://github.com/nickderobertis/crozier/issues/610) | no: binding a measurement's external-reference bytes concerns reproducibility, not what is emitted | not-generated-output | — | Left to its own repair. |
| [#611](https://github.com/nickderobertis/crozier/issues/611) | no: PATH mutation by the formatter test doubles is test isolation | not-generated-output | — | Left to its own repair. |
| [#612](https://github.com/nickderobertis/crozier/issues/612) | yes: crozier refused to generate an SDK for parameters in different locations sharing a name | parity-gap-repaired | [`612-parameter-location-collision/`](612-parameter-location-collision/README.md) | crozier generates Fern's `{name}_path_param` signature and drops the cookie, each parameter keeping its wire name; the pairs Fern refuses still refuse. |
| [#613](https://github.com/nickderobertis/crozier/issues/613) | yes: worked examples in the generated README, reference and docstrings pass a path parameter's name where its pattern rejects it | shared-defect-departed | [`schema-rejected-name-example`](../../departures/evidence/schema-rejected-name-example.md) in `assets/departures.yml` | crozier writes a value the parameter's own schema accepts, landed by `schema-valid-example-values`. |
| [#614](https://github.com/nickderobertis/crozier/issues/614) | no: workflow lint covers CI configuration | not-generated-output | — | Left to its own repair. |
| [#615](https://github.com/nickderobertis/crozier/issues/615) | yes: an empty composition member beside a reference changes the generated model's identity | parity-gap-repaired | [`615-empty-composition-member-reference/`](615-empty-composition-member-reference/README.md) | crozier types an `allOf` of a reference and an empty `{}` member as the referenced model itself, as Fern does, rather than copying it into a new one. |
| [#616](https://github.com/nickderobertis/crozier/issues/616) | no: the surface census's YAML reader is coverage tooling, not the generator's parser | not-generated-output | — | Left to its own repair. |
| [#617](https://github.com/nickderobertis/crozier/issues/617) | yes: an annotated copy of an inheritance-spelled union generates as a plain object | parity-gap-repaired | [`617-annotated-inherited-union/`](617-annotated-inherited-union/README.md) | crozier copies an annotated reference to an inheritance-spelled union as a discriminated union of its own, as Fern does, so variant payloads parse into their variant classes. |
