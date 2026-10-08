# Nullable multipart and array body search

## Witness search

Only corpus sources and committed remote-tree fragments are recorded here;
local test inputs are excluded from real-witness evidence.

At `54fb1adf2`, a renewed offline walk parsed all 283 acquired source records
and previously enumerated committed remote-tree fragments. [sources.tsv](sources.tsv)
records hashes computed from the committed bytes and each detected declaration.
No parse errors occurred. Multipart screens found no array property lacking its
own description while its binary items carry one, and no 3.1 binary-string/null
anyOf property. They inspect directly declared properties after local reference
resolution; inherited declarations and cross-document references remain unsearched.

The 3.1 PUT array-of-references screen found two partial candidates:

| registered source | declaration | missing recorded behavior |
|---|---|---|
| `letta` | `PUT /v1/identities/{identity_id}/properties` | Its certified `identities/raw_client.py::upsert_properties_for_identity` request includes a JSON content-type header; it also has a path argument and a titled body |
| `deepsearch-ds-v2` | `PUT /system/admin/save_flavours_default_quota` | Its certified `system_quotas/raw_client.py::save_flavours_default_quotas` request includes a JSON content-type header; it has a titled body and security |

Their existing publisher provenance, pinned revisions, source bytes, accepted
complete goldens and gate wiring remain registered. They establish the array
family but do not substitute for the root, untitled, header-free conjunction
measured in the fresh fixture. No complete real witness is claimed for that
conjunction. Publisher searches remain incomplete; no network acquisition was
performed and no exhaustive public absence is claimed.

| key | verdict | why |
|---|---|---|
| `format-binary` | `search-incomplete` | No exact nullable binary multipart declaration |
| `description` | `search-incomplete` | No exact inherited items description on a multipart file array |
| `request-body-content` | `search-incomplete` | Two array-family candidates do not exhibit the recorded header-free call |

Handling sites:

- `src/ir.rs::hoist_form_object[let nullable_binary = multipart]`
- `src/ir.rs::hoist_form_object[\(multipart && is_file\)]`
- `src/emit.rs::build_example_inner[&& matches!\(f\.type_ref, TypeRef::Optional\(_\)\)]`

## Renewed search

| key | result | scope |
|---|---|---|
| `format-binary` | `none-registrable` | Exact nullable binary conjunction over committed source records |
| `description` | `none-registrable` | Direct multipart item-description conjunction |
| `request-body-content` | `none-registrable` | Recorded header-free root array-body conjunction |
