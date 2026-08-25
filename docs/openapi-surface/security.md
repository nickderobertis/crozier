# OpenAPI surface coverage — Security

Classified entries for the `security` region, against the boundary in
`## Scope` below.

**How this region's feature list was enumerated.** Not by reading the corpus and
writing down what it holds — that would classify only what is already covered.
The list comes off the specification, in five mechanical steps a reader can
repeat against [OAS 3.0.3](https://spec.openapis.org/oas/v3.0.3) and
[OAS 3.1.1](https://spec.openapis.org/oas/v3.1.1):

1. Take the objects this region owns from its `## Scope` row: Security Scheme,
   OAuth Flows, OAuth Flow, Security Requirement, and `components.securitySchemes`.
2. For each object, take **every row of its fixed-field table**, in both
   versions. The two tables are identical field for field, which is why no row
   here reads `3.0` and every field row reads `both`.
3. Where a field's value is drawn from a set the specification enumerates, take
   **one feature per member**, and diff *those* lists across the two versions —
   that diff is the region's only `3.1` row. `type` has 5 members (3.0 names four
   and 3.1 adds `mutualTLS`), `in` has 3, and `scheme`'s members are the [IANA
   HTTP Authentication Scheme
   Registry](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml)
   names, of which `basic`, `bearer` and `digest` get a feature each and the
   remainder (`mutual`, `negotiate`, `hoba`, `scram-sha-256`, …) share one.
4. The Security Requirement Object has **no fixed fields** — its keys are scheme
   names — so its features come from the value shapes its own prose defines (a
   scheme with scopes, a scheme with an empty scope list, the empty requirement
   `{}` that makes authentication optional, an empty `security: []`, several
   requirements as alternatives, several schemes in one requirement as a
   conjunction) crossed with the **two positions** the specification allows the
   list to appear in (the OpenAPI Object's `security`, the Operation Object's
   `security`). Six shapes × two positions = twelve features. The `{}` row is the
   one whose two positions land in different categories, which is exactly why the
   cross is taken rather than assumed.
5. Drop what another region owns, cross-linking instead of duplicating — see
   *Region boundaries* under `## Method notes`.

Steps 2–4 are what makes this a walk rather than a survey: `oauth2-multiple-flows`
and the operation-level `{}` are features no corpus reading would have produced,
because nothing in the corpus declares them.

## Scope

Security Scheme, OAuth Flows, OAuth Flow and Security Requirement objects, and
`components.securitySchemes`.

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
| `securityscheme-type-apikey` | both | `Security Scheme Object.type` = `apiKey` | golden | census `securityScheme.type=apiKey`: 30 golden-bearing sources, 45 sites — `amazonaws.com-cloudformation`, `apideck.com-crm`(3), `appwrite.io-server`(4), `tlon-notes`(2), +26 more |  |  |  |
| `securityscheme-type-http` | both | `Security Scheme Object.type` = `http` | golden | census `securityScheme.type=http`: 35 golden-bearing sources, 42 sites — `airbyte.local-config`, `apache.org`(2), `auth-schemes`(2), `basic-auth`, +31 more |  |  |  |
| `securityscheme-type-oauth2` | both | `Security Scheme Object.type` = `oauth2` | golden | census `securityScheme.type=oauth2`: 10 golden-bearing sources, 11 sites — `auth-schemes`, `bungie.net`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`(2), `reverb.com`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `securityscheme-type-openidconnect` | both | `Security Scheme Object.type` = `openIdConnect` | golden | census `securityScheme.type=openIdConnect`: 4 golden-bearing sources, 4 sites — `apache.org`, `apache.org-airflow`, `khoainats`, `openepcis-dpp-ready` |  |  |  |
| `mutualTLS` | 3.1 | `Security Scheme Object.type` = `mutualTLS` | limitations | `fern-limitations.md` key `mutualTLS`, verdict `discards + supply`; census `securityScheme.type=mutualTLS` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `securityscheme-description` | both | `Security Scheme Object.description` | golden | census `securityScheme.description`: 32 golden-bearing sources, 51 sites — `amazonaws.com-cloudformation`, `apideck.com-crm`(3), `appwrite.io-server`(4), `xero.com-xero-payroll-au`, +28 more |  |  |  |
| `securityscheme-name` | both | `Security Scheme Object.name` (the `apiKey` parameter name) | golden | census `securityScheme.name`: 30 golden-bearing sources, 45 sites — same sources as `securityscheme-type-apikey`, which the specification requires |  |  |  |
| `apikey-header` | both | `Security Scheme Object.in` = `header` | golden | census `securityScheme.in=header`: 30 golden-bearing sources, 44 sites — `amazonaws.com-cloudformation`, `apideck.com-crm`(3), `appwrite.io-server`(4), `tlon-notes`, +26 more. This is the ledger's unnamed *control* row, so it joins no key |  |  |  |
| `apiKey-query` | both | `Security Scheme Object.in` = `query` | limitations | `fern-limitations.md` key `apiKey-query`, verdict `discards + supply`; census `securityScheme.in=query`: 0 golden-bearing sources. Its three registered sources — `bbci.co.uk`, `esgenterprise.com`, `etherpad.local` — are all `CORPUS.md` **DROPPED** rows with no golden |  |  |  |
| `apiKey-cookie` | both | `Security Scheme Object.in` = `cookie` | golden | census `securityScheme.in=cookie`: 1 golden-bearing source, 1 site — `tlon-notes`; `fern-limitations.md` key `apiKey-cookie`, verdict `discards`. `tlon-notes` pairs `eyreCookie` with a header `apiKey`, which is the ledger's *"pair one with a supported scheme"* case, so the golden pins the discard rather than the scheme |  |  |  |
| `http-basic` | both | `Security Scheme Object.scheme` = `basic` | golden | census `securityScheme.scheme=basic`: 15 golden-bearing sources, 15 sites — `apache.org`, `auth-schemes`, `basic-auth`, `openepcis-dpp-ready`, +11 more |  |  |  |
| `http-bearer` | both | `Security Scheme Object.scheme` = `bearer` | golden | census `securityScheme.scheme=bearer`: 25 golden-bearing sources, 25 sites — `airbyte.local-config`, `auth-schemes`, `exhaustive`, `tamoss`, +21 more |  |  |  |
| `http-digest` | both | `Security Scheme Object.scheme` = `digest` | limitations | `fern-limitations.md` key `http-digest`, verdict `discards + licence`; census `securityScheme.scheme=digest` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `http-scheme-other-iana` | both | `Security Scheme Object.scheme` = an IANA-registered scheme other than `basic`, `bearer` or `digest` | golden | census `securityScheme.scheme=negotiate`: 2 golden-bearing sources, 2 sites — `apache.org`, `apache.org-airflow`. `securityScheme.scheme=mutual` is declared once (`conjur.local`), which is **DROPPED**, so `negotiate` alone carries this row |  |  |  |
| `securityscheme-bearerformat` | both | `Security Scheme Object.bearerFormat` | golden | census `securityScheme.bearerFormat`: 5 golden-bearing sources, 5 sites — `airbyte.local-config`, `openepcis-dpp-ready`, `sac-backend`, `tamoss`, `worldcoin-signup-sequencer` |  |  |  |
| `securityscheme-openidconnecturl` | both | `Security Scheme Object.openIdConnectUrl` | golden | census `securityScheme.openIdConnectUrl`: 4 golden-bearing sources, 4 sites — `apache.org`, `apache.org-airflow`, `khoainats`, `openepcis-dpp-ready` |  |  |  |
| `securityscheme-flows` | both | `Security Scheme Object.flows` (the OAuth Flows Object) | golden | census `securityScheme.flows`: 10 golden-bearing sources, 11 sites — the `securityscheme-type-oauth2` sources, every one of which declares the object |  |  |  |
| `oauth2-implicit` | both | `OAuth Flows Object.implicit` | limitations | `fern-limitations.md` key `oauth2-implicit`, verdict `supply` (a qualifier-only cell — see *Two verdict cells* below); census `securityScheme.flows.implicit` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `oauth2-password` | both | `OAuth Flows Object.password` | limitations | `fern-limitations.md` key `oauth2-password`, verdict `supply` (a qualifier-only cell — see *Two verdict cells* below); census `securityScheme.flows.password` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `oauth2-clientcredentials` | both | `OAuth Flows Object.clientCredentials` | golden | census `securityScheme.flows.clientCredentials`: 7 golden-bearing sources, 7 sites — `auth-schemes`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`, `reverb.com` |  |  |  |
| `oauth2-authorizationcode` | both | `OAuth Flows Object.authorizationCode` | golden | census `securityScheme.flows.authorizationCode`: 4 golden-bearing sources, 4 sites — `bungie.net`, `openbanking.org.uk-account-info-openapi`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `oauth2-multiple-flows` | both | `OAuth Flows Object` declaring more than one of its four flows | gap | shape read over the 107 golden-bearing sources: 0 declare it — each of the 11 declared OAuth Flows Objects names exactly one flow (`clientCredentials` 7, `authorizationCode` 4); 0 over all 124 registered sources too. No `fern-limitations.md` row names it: `oauth2-implicit` and `oauth2-password` are about a flow standing alone, not about two standing together | `src/ir.rs` — 1 place: the `authorization_code.or(client_credentials).or(implicit).or(password)` chain in `oauth_scope_enum` (`src/ir.rs:418`) | `src/<pkg>/types/oauth_scope.py`'s `OauthScope` members are read from whichever flow that chain reaches first, so a Fern that prefers a different flow emits a different member set, and `types/__init__.py` and `reference.md` move with it | `FIXTURE` — screen for a redistributable real-world document at an immutable ref whose one `oauth2` scheme declares two flows with *different* `scopes` maps (the flows must differ, or the golden cannot tell the orders apart), register it, and the byte-compare settles the precedence |
| `oauthflow-authorizationurl` | both | `OAuth Flow Object.authorizationUrl` | golden | census `securityScheme.flows.authorizationCode.authorizationUrl`: 4 golden-bearing sources, 4 sites — `bungie.net`, `openbanking.org.uk-account-info-openapi`, `squareup.com`, `xero.com-xero-payroll-au`. The field's other position, `flows.implicit`, is `oauth2-implicit`'s |  |  |  |
| `oauthflow-tokenurl` | both | `OAuth Flow Object.tokenUrl` | golden | census `securityScheme.flows.authorizationCode.tokenUrl` (4 sources) + `securityScheme.flows.clientCredentials.tokenUrl` (7 sources): 10 distinct golden-bearing sources, 11 sites |  |  |  |
| `oauthflow-refreshurl` | both | `OAuth Flow Object.refreshUrl` | golden | census `securityScheme.flows.clientCredentials.refreshUrl`: 1 golden-bearing source, 1 site — `microcks.local`. `…authorizationCode.refreshUrl` is declared once, by `asana.com`, which is **DROPPED** |  |  |  |
| `oauthflow-scopes` | both | `OAuth Flow Object.scopes` | golden | census `securityScheme.flows.authorizationCode.scopes` (4 sources) + `securityScheme.flows.clientCredentials.scopes` (7 sources): 10 distinct golden-bearing sources, 11 sites. Both value shapes are covered — 9 sites carry a non-empty map, and 2 (`auth-schemes`, `oauth-client-credentials`) carry the empty map the specification allows |  |  |  |
| `security-requirement-scopes-document` | both | `OpenAPI Object.security` → `Security Requirement Object`, scheme → non-empty scope list | golden | shape read: 2 golden-bearing sources, 2 sites — `free5gc-namf-communication`, `free5gc-pdu-session` |  |  |  |
| `security-requirement-scopes-operation` | both | `Operation Object.security` → `Security Requirement Object`, scheme → non-empty scope list | golden | shape read: 7 golden-bearing sources, 451 sites — `bungie.net`(57), `khoainats`(1), `microcks.local`(32), `openbanking.org.uk-account-info-openapi`(29), `reverb.com`(108), `squareup.com`(195), `xero.com-xero-payroll-au`(29) |  |  |  |
| `security-requirement-noscopes-document` | both | `OpenAPI Object.security` → `Security Requirement Object`, scheme → `[]` | golden | shape read: 32 golden-bearing sources, 47 sites — `amazonaws.com-cloudformation`, `apideck.com-crm`(3), `openepcis-dpp-ready`(6), `tlon-notes`(2), +28 more |  |  |  |
| `security-requirement-noscopes-operation` | both | `Operation Object.security` → `Security Requirement Object`, scheme → `[]` | golden | shape read: 43 golden-bearing sources, 873 sites — `appwrite.io-server`(229), `appwrite.io-client`(117), `maif.local-otoroshi`(101), `apideck.com-accounting`(53), +39 more |  |  |  |
| `security-optional-requirement-document` | both | `OpenAPI Object.security` containing `{}` (authentication optional) | golden | shape read: 5 golden-bearing sources, 5 sites — `airbyte.local-config`, `free5gc-namf-communication`, `free5gc-pdu-session`, `openepcis-dpp-ready`, `openfigi.com` |  |  |  |
| `security-optional-requirement-operation` | both | `Operation Object.security` containing `{}` (authentication optional for that operation) | gap | shape read over the 107 golden-bearing sources: 0 declare it. The one registered source that does, `atlassian.com-jira` (221 sites), is a `CORPUS.md` **DROPPED** row with no golden, so nothing pins it. No `fern-limitations.md` row names it — `operation-security-alternatives` is about several requirements, not about the empty one | `src/ir.rs` — 3 places: `all_operations_authenticated` (`src/ir.rs:627`), `body_response_same_ref` (`src/ir.rs:2544`) and `operation_uses_basic_auth` (`src/ir.rs:2569`), each folding `op.security` over `doc.security` and testing `!r.is_empty()` | An operation-level `{}` makes that one operation unauthenticated, which flips `all_operations_authenticated` and so decides whether the credential in `client.py`/`core/client_wrapper.py` (and its signature in `reference.md`) is required or `typing.Optional[...] = None` for the **whole** SDK | `FIXTURE` — real-world documents do declare it (`atlassian.com-jira` 221 times), so screen for one Fern can generate, register it, and the byte-compare settles whether Fern reads `{}` as opting the operation out |
| `security-empty-list-document` | both | `OpenAPI Object.security` = `[]` | golden | shape read: 5 golden-bearing sources, 5 sites — `apache.org`, `apache.org-airflow`, `apideck.com-ecosystem`, `apis.guru`, `prometheus-x-edge-computing` |  |  |  |
| `security-empty-list-operation` | both | `Operation Object.security` = `[]` (opting out of the document default) | golden | shape read: 5 golden-bearing sources, 10 sites — `airbyte.local-config`(1), `apideck.com-vault`(3), `exa-gate`(3), `sac-backend`(2), `squareup.com`(1) |  |  |  |
| `security-alternatives-document` | both | `OpenAPI Object.security` holding several Security Requirement Objects (alternatives) | golden | shape read: 7 golden-bearing sources, 7 sites — `exa-gate`, `free5gc-namf-communication`, `free5gc-pdu-session`, `openepcis-dpp-ready`, `openfigi.com`, `tamoss`, `tlon-notes` |  |  |  |
| `operation-security-alternatives` | both | `Operation Object.security` holding several Security Requirement Objects (alternatives) | golden | shape read: 2 golden-bearing sources, 3 sites — `khoainats`(1), `worldcoin-signup-sequencer`(2); `fern-limitations.md` key `operation-security-alternatives`, verdict `ignores + supply` |  |  |  |
| `security-conjunction-document` | both | `OpenAPI Object.security` → one Security Requirement Object naming several schemes (conjunction) | golden | shape read: 6 golden-bearing sources, 6 sites — `apideck.com-crm`, `apideck.com-lead`, `apideck.com-proxy`, `apideck.com-vault`, `openepcis-dpp-ready`, `slurmdb-rest` |  |  |  |
| `security-conjunction-operation` | both | `Operation Object.security` → one Security Requirement Object naming several schemes (conjunction) | golden | shape read: 2 golden-bearing sources, 151 sites — `appwrite.io-client`(56), `appwrite.io-server`(95) |  |  |  |
| `components-securityschemes` | both | `Components Object.securitySchemes` | golden | census `components.securitySchemes`: 69 golden-bearing sources, 69 sites — `airbyte.local-config`, `apache.org`, `auth-schemes`, `xero.com-xero-payroll-au`, +65 more |  |  |  |
| `securityscheme-ref` | both | `Components Object.securitySchemes` holding a Reference Object instead of a Security Scheme Object | gap | shape read: 0 of the 107 golden-bearing sources declare it, and 0 of all 124 registered sources. No `fern-limitations.md` row names it — `pathitem-ref` and `relative-file-ref` are the Reference features that file rules on, and both are [`document-paths.md`](document-paths.md)'s | `none` — `SecurityScheme` (`src/openapi.rs:142`) declares no `$ref` field and `src/refs.rs` resolves references for `components.schemas` only, so the node deserializes to the default scheme and its `type` becomes `SecuritySchemeType::Other` | With no scheme recognised, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token` and `core/client_wrapper.py` sends `Authorization: Bearer` — where a Fern that resolves the reference would emit the referenced scheme's credential (an `api_key` and its own header, say) | `PROBE` — 0 of 124 screened real-world documents declare it, so no corpus row is in reach; a probe declaring one `$ref`-valued scheme beside a supported one, carried through `fern check` and `fern generate`, records in [`../fern-limitations.md`](../fern-limitations.md) whether Fern resolves it |

## Method notes

### What was measured, and with what

Two instruments, and the second is the first one imported rather than a new one.

**The census, for every feature the selector grammar can name.** Run in full once,
and re-run per selector for the absences the `gap` and `limitations` rows cite:

```
just surface-census --json                                    # 407 selectors, 603390 sites, 124 sources
just surface-census --selector securityScheme.type=mutualTLS \
                    --selector securityScheme.scheme=digest \
                    --selector securityScheme.flows.implicit \
                    --selector securityScheme.flows.password
```

That second invocation prints each of the four as `(declared by no registered
source)`, which is the evidence those rows cite — the instrument reports an
absence as an absence rather than as nothing.

**The census imported, for the shapes the grammar cannot name.** A Security
Requirement Object's keys are *scheme names*, so the grammar stops at
`openapi.security` / `operation.security` and emits no selector for what the list
holds: `[]` and `[{}]` and `[{a: []}, {b: []}]` are one selector with one count.
Twelve of this file's rows are about exactly that difference, and two more
(`securityscheme-ref`, `oauth2-multiple-flows`) turn on a shape the grammar
flattens the same way. All fourteen are measured by importing the census script's
own loader and registered-source list and reading the parsed object model — never
by opening a fixture. The whole read is repeatable
from the repository root:

```sh
"$(./scripts/census-python.sh)" - <<'PY'
import collections, importlib.util, sys
from pathlib import Path
root = Path.cwd()
spec = importlib.util.spec_from_file_location("census", root / "scripts/openapi-surface-census.py")
census = importlib.util.module_from_spec(spec); sys.modules["census"] = census
spec.loader.exec_module(census)
fx = root / "tests/fixtures"
aliases = census.corpus_aliases(fx)
sources = census.registered_sources(fx, root / ".local/corpus", False)
golden = {s.fixture for s in sources if (fx / aliases.get(s.fixture, s.fixture) / "expected").is_dir()}
hits = collections.defaultdict(collections.Counter)
METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
FLOWS = ("implicit", "password", "clientCredentials", "authorizationCode")

def requirements(node, where, name):
    if not isinstance(node, list):
        return
    if not node:
        hits[where + ":empty-list"][name] += 1
        return
    if len(node) > 1:
        hits[where + ":alternatives"][name] += 1
    for req in node:
        if not isinstance(req, dict):
            continue
        if not req:
            hits[where + ":optional-empty-object"][name] += 1
            continue
        if len(req) > 1:
            hits[where + ":conjunction"][name] += 1
        for scopes in req.values():
            hits[where + (":with-scopes" if scopes else ":noscopes")][name] += 1

for source in sources:
    if source.path is None or source.fixture not in golden:
        continue
    doc = census.load_document(source.path)
    requirements(doc.get("security"), "document", source.fixture)
    for item in (doc.get("paths") or {}).values():
        if not isinstance(item, dict):
            continue
        for method, op in item.items():
            if method in METHODS and isinstance(op, dict):
                requirements(op.get("security"), "operation", source.fixture)
    for scheme in ((doc.get("components") or {}).get("securitySchemes") or {}).values():
        if not isinstance(scheme, dict):
            continue
        if "$ref" in scheme:
            hits["securityScheme:$ref"][source.fixture] += 1
        flows = scheme.get("flows")
        if isinstance(flows, dict) and len([f for f in FLOWS if f in flows]) > 1:
            hits["oauthFlows:multiple-flows"][source.fixture] += 1
KEYS = [f"{where}:{shape}"
        for where in ("document", "operation")
        for shape in ("with-scopes", "noscopes", "optional-empty-object",
                      "empty-list", "alternatives", "conjunction")]
KEYS += ["securityScheme:$ref", "oauthFlows:multiple-flows"]
for key in KEYS:  # a fixed list, so a shape no source declares prints as 0 rather than vanishing
    counts = hits[key]
    print(f"{key:34} sources={len(counts):3} sites={sum(counts.values()):5}")
PY
```

### A registered source is not always a golden

The census's 124 registered sources are **not** 124 goldens, and rule 1 of the
[category rules](../openapi-surface-coverage.md#the-category-rules) is about *a
registered golden fixture's own source document*. Seventeen registered sources
carry no committed `expected/` tree — sixteen are `CORPUS.md` **DROPPED** rows
(Fern refused or failed on them) and `calorieninjas.com` is the accepted-exception
row `AGENTS.md` names. So every count in this file is filtered to the **107
golden-bearing sources**, `tests/fixtures/<dir>/expected` being the test, with
`corpus-aliases.tsv` mapping manifest names to fixture directories.

The filter is not cosmetic: it moves rows. `apiKey-query` is declared by three
registered sources and by no golden — all three are DROPPED — so it classifies
`limitations`, matching the ledger instead of contradicting it. `http-scheme-other-iana`
loses `conjur.local`'s `mutual` and rests on `apache.org`'s `negotiate`.
`oauthflow-refreshurl` loses `asana.com` and rests on `microcks.local`. Read
unfiltered, two rows change category outright — `apiKey-query` would claim golden
coverage no golden provides, and `security-optional-requirement-operation` would
stop being a gap on the strength of `atlassian.com-jira` — and several more would
cite a source whose Fern output does not exist.

### Two verdict cells that are qualifiers, not verdicts

`oauth2-implicit` and `oauth2-password` carry `supply` in the verdict column of
[`fern-limitations.md`](../fern-limitations.md#what-round-3-did-not-register-and-why)'s
gap table — a *qualifier* under that file's own [*How to read a
verdict*](../fern-limitations.md#how-to-read-a-verdict), which lists `supply`
beside `licence` and `pipeline` as things joined to a verdict rather than as one.
Both rows quote the ledger's cell verbatim rather than inventing the verdict it
omits. What the ledger does measure for both flows is in its auth probe table:
Fern emits `token` → `Authorization: Bearer`, required when every operation is
secured. That is an `implements`-shaped result the gap table's supply cell does
not carry, and only a probe recorded in that file can promote it.

### Region boundaries

Five surfaces touch this region and none is classified here:

- **`OpenAPI Object.security` and `Operation Object.security` as *fields***, i.e.
  whether a document declares them at all, belong to
  [`document-paths.md`](document-paths.md), which owns the OpenAPI and Operation
  objects. This region owns what the *list* holds — the Security Requirement
  Object and its value shapes — which is why its twelve requirement rows all name
  a shape and none of them names the bare field. The census measures the fields as
  `openapi.security` (48 sources) and `operation.security` (58 sources, 1748
  sites) over all 124 registered sources; those two numbers are that region's to
  classify, filter included.
- **`x-` extensions on a Security Scheme Object** belong to
  [`oas31-extensions.md`](oas31-extensions.md). The census finds two:
  `securityScheme.x-amazon-apigateway-authtype` and `securityScheme.x-appwrite`.
- **The Reference Object itself** (`$ref`, `summary`, `description`) is
  [`document-paths.md`](document-paths.md)'s. `securityscheme-ref` above is not
  that object — it is the Security Scheme *position* holding one, which only this
  region can classify.
- **`Security Scheme Object.in`** reuses the Parameter Object's `in` vocabulary
  but is its own field on its own object; `parameter.in` is
  [`parameters.md`](parameters.md)'s.
- **No JSON Schema keyword appears in this region.** OAuth `scopes` is a
  `string → string` map, not a schema, so nothing here belongs to
  [`schemas.md`](schemas.md).

### Deliberate exclusions

Enumeration step 3 takes a feature per member of a value set the specification
enumerates; it does **not** take a feature per *cardinality of a free-keyed map*.
So "a document declaring several security schemes" (24 registered sources do) and
"a document declaring two `oauth2` schemes" (`openbanking.org.uk-account-info-openapi`
does) are not rows here: the keys of `components.securitySchemes` are names, which
is the same rule that keeps them out of the census. `oauth2-multiple-flows` is a
row despite looking similar because the OAuth Flows Object's four flows are
**fixed fields**, not map keys, so declaring two of them is a shape of the object
rather than a count of names.

### One instrument artifact, found while measuring

The census reports `securityRequirement.x-api-key`, 1 site, in
`calorieninjas.com`. It is not an extension: that document names its security
scheme `x-api-key`, and a Security Requirement Object's keys are scheme names. The
walk tests a key for the `x-` prefix before it tests whether the enclosing object
keys its map by name, so a scheme whose name starts with `x-` is recorded as a
vendor extension of the requirement. No row in this file rests on it — the
requirement rows are measured by the shape read above, not by that selector — and
the source is a golden-less accepted-exception row either way. Fixing it belongs
to `scripts/openapi-surface-census.py`, not to this file.

### What this region could not settle

`etherpad.local` and `appng-rest-api` each declare a **sole** `apiKey` scheme in
`query` and `cookie` respectively, with a document-level `security` that secures
every operation — precisely the two rows
[`fern-limitations.md`](../fern-limitations.md#the-importer-drops-four-security-schemes-outright)
measured as `fern check` **exit 1**. Both are DROPPED in `CORPUS.md`, and
`etherpad.local`'s reason is recorded as a *check* failure with five fatal
diagnostics, which is consistent. Whether the sole-scheme refusal is what dropped
them is not settled here: settling it means running Fern, which this pass does
not do.
