# Operation combination bounded search

This search reads registered source bytes, the pinned APIs.guru archive,
exact-byte documents recovered from the retained response cache, and the
handed-off population. A positive selector is a candidate, never branch proof.
No live code search was used. Missing earlier acquired documents and unfinished
arm-specific comparisons remain outstanding, so no fallback is exhausted.

The archive revision is `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`.
Its downloaded archive digest is
`7a0bdff93afc94d373c7e596d24739cc8aff7d93c4e8b75a82e9c0cf7e0606a1`;
all 4,138 source digests match the existing acquisition manifest. The shared
cache publishes it atomically under the archive lock. The archive format
differs from the earlier acquisition record; document digests are the authority.

The three JSONL files preserve every fresh source census result (including
zero declarations), with source SHA-256 and per-combination selector counts.
The population index retains all 9,024 recorded identities. The candidate
ledger names every unresolved candidate and all handed-off documents per
combination; other negative declarations are checkable in the exact-byte
JSONL source census, joined by SHA-256 to population.tsv. Anonymous bytes are explicitly ineligible for corpus
registration. Each newly admitted and registered handed-off document is named
individually, including a negative selector verdict for each former handwritten
combination. Neither missing documents nor declarations count as matches.

The search bound was one pinned archive acquisition, retained local exact-byte
recovery, and the recorded instrumented control experiments. A candidate with
source bytes but no completed arm-specific certified comparison remains open.
The retained raw JSONL files were produced with the existing
`tools/witness-search/witness-search-local-census.py`, one worker, using the
selectors in `contract.tsv`; all recovered bytes were SHA-256 verified first.

## Populations measured

| Census | Documents read |
|---|---:|
| `census.jsonl` | 4474 |
| `earlier-census.jsonl` | 552 |
| `handed-off-census.jsonl` | 25 |

## Verdicts

The interaction row retains its search history here; its proof is its exclusive
region and the registered Adyen golden run. Every other row is search-incomplete.
The complete outstanding list for each row is in
[outstanding-candidates.tsv](outstanding-candidates.tsv), with every affected combination explicitly listed and one reason per
candidate. It is also the open-row list for the completion report.

| Combination | State | Candidates | Outstanding |
|---|---|---:|---:|
| `combo-basic-auth-document-requirement` | `search-incomplete` | 3041 | 2938 |
| `combo-basic-auth-operation-requirement` | `search-incomplete` | 3244 | 3138 |
| `combo-body-property-named-as-header-param` | `search-incomplete` | 2960 | 2847 |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 3535 | 3438 |
| `combo-document-operation-security` | `search-incomplete` | 3165 | 3069 |
| `combo-document-security-security-empty` | `search-incomplete` | 3059 | 2957 |
| `combo-echo-body-effective-anonymous` | `search-incomplete` | 3123 | 3013 |
| `combo-echo-body-effective-non-oauth-required` | `search-incomplete` | 3094 | 2990 |
| `combo-echo-body-effective-oauth2` | `search-incomplete` | 3248 | 3137 |
| `combo-error-multiple-media` | `search-incomplete` | 3084 | 2979 |
| `combo-error-object` | `search-incomplete` | 3344 | 3256 |
| `combo-errors-shared-ref` | `search-incomplete` | 3568 | 3499 |
| `combo-form-urlencoded-beside-json-body` | `search-incomplete` | 3004 | 2894 |
| `combo-form-urlencoded-body-with-params` | `search-incomplete` | 3129 | 3024 |
| `combo-form-urlencoded-union-body` | `search-incomplete` | 2973 | 2860 |
| `combo-header-param-ref-string-enum` | `search-incomplete` | 2975 | 2864 |
| `combo-inline-body-read-only-property` | `search-incomplete` | 2990 | 2882 |
| `combo-multipart-beside-json-body` | `search-incomplete` | 2993 | 2885 |
| `combo-multipart-body-with-params` | `search-incomplete` | 3186 | 3096 |
| `combo-oas31-grouped-response` | `search-incomplete` | 3288 | 3217 |
| `combo-oas31-root-response` | `search-incomplete` | 3030 | 2927 |
| `combo-octet-stream-body-header-param` | `search-incomplete` | 2977 | 2867 |
| `combo-optional-ref-map-body` | `search-incomplete` | 3019 | 2912 |
| `combo-optional-ref-union-body` | `search-incomplete` | 2979 | 2868 |
| `combo-paginated-grouped-operation` | `search-incomplete` | 2974 | 2863 |
| `combo-params-beside-inline-anyof-body` | `search-incomplete` | 3041 | 2933 |
| `combo-params-beside-inline-oneof-body` | `search-incomplete` | 3058 | 2954 |
| `combo-path-param-ref-string-enum` | `search-incomplete` | 3010 | 2903 |
| `combo-query-param-anyof` | `search-incomplete` | 3050 | 2946 |
| `combo-query-param-array-inline-enum-items` | `search-incomplete` | 3171 | 3070 |
| `combo-query-param-array-ref-enum-items` | `search-incomplete` | 3066 | 2957 |
| `combo-query-param-inline-object` | `search-incomplete` | 3007 | 2897 |
| `combo-query-param-oneof` | `search-incomplete` | 3007 | 2902 |
| `combo-query-param-ref-date-time` | `search-incomplete` | 2965 | 2853 |
| `combo-query-param-ref-object` | `search-incomplete` | 3009 | 2901 |
| `combo-query-param-ref-string-enum` | `search-incomplete` | 3189 | 3091 |
| `combo-streaming-method-name` | `search-incomplete` | 2984 | 2873 |
| `combo-success-anyof-nullable` | `search-incomplete` | 2979 | 2868 |
| `combo-success-json-beside-binary-schema` | `search-incomplete` | 3009 | 2908 |
| `combo-success-json-beside-download` | `search-incomplete` | 2998 | 2891 |
| `combo-success-oneof-nullable` | `search-incomplete` | 2963 | 2851 |
| `combo-success-statuses-mixed-media` | `search-incomplete` | 3139 | 3037 |
| `combo-success-text-beside-download` | `search-incomplete` | 2969 | 2861 |

## Census encoding

`census.tsv.gz` retains the fixture-only search census columns, sorted by all
column values, with UTF-8 and LF records. It uses gzip level 9, timestamp 0,
and an empty original filename. The census suite decodes, sorts, serializes
and recompresses this committed file and requires identical bytes. The plain
[outstanding index](outstanding-candidates.tsv) lists every affected combination
for each candidate and the reason its screening is unfinished.

## Interaction-region review

[interaction-region-review.tsv](interaction-region-review.tsv) lists every open
row, its current site declaration, and every registered golden declarer selected
from the fresh source census. A declaration alone is not an interaction witness.
The refreshed reach store contains all 319 registered golden tests. The
[path/body-name arm screen](registered-arm-screen.tsv) checks all 30 registered
declarers against that store; none executes its exclusive arm. The store records
commit `daa26ba3013e2c6158e22a63a857ed65d0c8871e`. The refresh started from
the complete saved base, but the tool selected full measurement because its
change attribution considered the new `Document::tree` test helper reachable
from golden tests. No declaration was promoted from a pooled hit.
The nullable-response declarations pool the two union keywords;
the inline-readOnly predicate pools writable fields. Its pruning helper also
pools dropped and kept fields in one closure. The historical co-occurrence
audit identifies the pooled operands or absence of a conjunctive condition for
each other row. These stay open until an exclusive arm and a matching real
witness settle them.

Ten completed, from-scratch control experiments are in `controls/`, each with
three documents and a version-1 region report naming all handlers and both
directions of the failed union. Their real-generator replay asserts the
inequality and the exact report; it does not relax the independent-row union
assertion. Regenerate those reports from the current source with:

```sh
CROZIER_UPDATE_COMBINATION_CONTROLS=1 \
flock "${XDG_CACHE_HOME:-$HOME/.cache}/crozier/instrumented-measurement.lock" \
just nx run surface-reach:test-handwritten-reach --skipNxCache \
  --args="-q -k test_open_control_union_reports"
```

The enum-array experiment first encountered a refused header control, including
a retry with an explicit array example. That initial batch did not run the
combined document. The later cookie-location experiment did run all three
documents and found 44 both-only and 22 single-union-only regions. The certified
pair also refused the header document, so that screen establishes no refusal
parity gap. Its document and Contract A result are in
[the measurement](../../fern-measurements/operation-independence/header-array-enum-second/README.md).

## Adyen interaction proof

`combo-query-param-ref-string-enum` uses the dedicated true-return region in
`src/ir.rs::build_endpoint` after resolving the query parameter's reference and
testing the target's string enum. The controls exclude an ordinary referenced
query, an enum reference in a header, and an inline query enum. The registered
Adyen source also executes the region. Its corpus journey compares both
`python_enums` and the newly generated `expected-literals/` overlay.

The default golden and literals overlay were freshly generated through the
standard corpus recipes at the certified pair. The default-mode shared cache
entry was additionally checked against the exact source SHA-256, its successful
exit record, and a real `crozier compare`;
[adyen-capital-comparison.json](adyen-capital-comparison.json) records that
comparison. Its source is
`03969223d168d12c64c77dae327ea08a0c914a3104a77caf3ccb968ee61af0d7`.
The reference tree is reused unchanged; no raw cache tree was reconstructed
from normalized goldens or overlays.
