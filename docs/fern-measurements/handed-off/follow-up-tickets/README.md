# Generated-output follow-up tickets

All twelve ticket texts concern generated output. The triage is
[`../follow-up-tickets.tsv`](../follow-up-tickets.tsv). Eight tickets reuse a
landed certified measurement and name its clearing commit; #697 reuses the
landed refusal measurement. The remaining three have fresh reductions here.
No ticket was closed, commented on or moved.

Every successful tree in the table byte-matches on the finished tree through
the catalogued departures; the two refusal rows refuse in both CLI modes.
There are no `default-matched` or `ruling-applied:*` rows and no new departures.
No real witness is registered by this node. Existing measurements retain
their original provenance, runtime evidence and enum-mode proofs.

| Ticket | Verdict | Measurement document | SHA-256 |
| --- | --- | --- | --- |
| [#602](https://github.com/nickderobertis/crozier/issues/602) | `already-matching` | [602-validation-error-shadowing](../../output-defects/602-validation-error-shadowing/openapi.yml) | `db97566bc340095e114957665b6519b0f32d506c551df48964066f8b8ecc419d` |
| [#679](https://github.com/nickderobertis/crozier/issues/679) | `refusal-kept` | [679](679/openapi.yml) | `55ecd806e9ab4b21603e24e71d6aa1b68b8847253eb943225baaaa9a69105f59` |
| [#685](https://github.com/nickderobertis/crozier/issues/685) | `already-matching` | [bare-string-parameter-example](../document-acceptance/bare-string-parameter-example/openapi.yml) | `eae65b1eb09203f153eba13ce43f321542638ce3a45e76f75941c08a61afb797` |
| [#694](https://github.com/nickderobertis/crozier/issues/694) | `parity-gap-repaired` | [694](694/openapi.yml) | `90532d775a98997ddb05d2f445e46fe610c7e4702226cac1c2e432703ec22584` |
| [#696](https://github.com/nickderobertis/crozier/issues/696) | `parity-gap-repaired` | [696](696/openapi.yml) | `9cb6d09fe56daa6bb179be467d8d78e77a37a8cf61d859df93466becac076848` |
| [#697](https://github.com/nickderobertis/crozier/issues/697) | `refusal-kept` | [never-compared-request-property-camelcase-collision](../document-acceptance/never-compared-request-property-camelcase-collision/openapi.yml) | `c81a5a3903a46fb20977112fb1ac9aa70736db0e5486c7611b4b12523b8bbff0` |
| [#698](https://github.com/nickderobertis/crozier/issues/698) | `already-matching` | [R2](../client-structure/R2/openapi.yml) | `709828a257ebd5120c5e78ba29f52fc966191a89f090c2e9d071fbab8aa0f94c` |
| [#699](https://github.com/nickderobertis/crozier/issues/699) | `already-matching` | [R9](../union-modelling/R9/openapi.yml) | `e159df09e198171cec5e41e0454ee74aee49df1c453a52e16f82723406eaa64b` |
| [#700](https://github.com/nickderobertis/crozier/issues/700) | `already-matching` | [R10](../client-structure/R10/openapi.yml) | `19562649f8150cc1a19a76fe370d1cefba113571765cb88559d2d83ee06e4bba` |
| [#701](https://github.com/nickderobertis/crozier/issues/701) | `already-matching` | [R13](../union-modelling/R13/openapi.yml) | `6b30bffa91c98da1800f68f40a14a83b8f5d175aa7ffeea30f0434229b600c24` |
| [#702](https://github.com/nickderobertis/crozier/issues/702) | `already-matching` | [R12](../client-structure/R12/openapi.yml) | `aae317cfb1c60c9c5d9ca0884462c284d59f7a57979fef72b03584ce5119c568` |
| [#703](https://github.com/nickderobertis/crozier/issues/703) | `already-matching` | [R14](../document-acceptance/R14/openapi.yml) | `68a66b5edf38b080068b25e0db4b9e26731da597109349115648eb91663cfd89` |

The publisher document behind #697 is api-platform/schema-generator's
`tests/e2e/openapi.yml` at `22635fbacac8011c73cdbbb5c20507c77c02d89d`, SHA-256
`978fbacd3483f78d34c90ff71bdc8429223ef8409e531b4960cb0c78dec31206`, as the
[document-acceptance record](../document-acceptance/README.md) states. A guarded
fetch of that exact revision reproduced crozier's
`request-property-camelcase-collision` refusal for `book` and `book[]`.
The from-scratch shelf reduction already holds the certified refusal and its
runtime evidence; it is reused rather than repaired twice.
