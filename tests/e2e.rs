//! End-to-end tests: drive the compiled `crozier` binary the way a user does —
//! as a subprocess over real files in a real temp directory — and byte-compare
//! its (comment-stripped) output against the committed Fern fixtures.
//!
//! This is the product's only faithful QA loop, so it never mocks the generator,
//! the filesystem, or the process boundary. The `just check` gate runs it.

use std::path::{Path, PathBuf};

use assert_cmd::Command;
use predicates::prelude::*;

/// A vendored Fern corpus: the spec at `tests/fixtures/<api>/openapi.yml`, the
/// naming flags crozier is driven with, and the generated files it reproduces
/// byte-for-byte today (paths relative to the output root). Each `matched` list
/// is the source of truth for what that corpus matches; it grows as generation
/// lands. See docs/matching.md.
struct Corpus {
    api: &'static str,
    package_name: &'static str,
    project_name: &'static str,
    /// `--audience` filters to drive crozier with (`x-crozier-audiences`);
    /// empty means the whole API is generated, matching most corpora.
    audiences: &'static [&'static str],
    /// Whether to pass `--audience-strict` (exclude un-annotated operations,
    /// matching Fern's exclusive filtering). Only meaningful with `audiences`.
    audience_strict: bool,
    /// `--client-class-name` to drive crozier with (Fern's `client_class_name`);
    /// `None` lets crozier derive the root client class from the package name, as
    /// every corpus but `client-class-name` does.
    client_class_name: Option<&'static str>,
    /// `--extra-fields` to drive crozier with (Fern's `pydantic_config.extra_fields`);
    /// `None` uses the default `allow`, as every corpus but `pydantic-extra-fields`
    /// does.
    extra_fields: Option<&'static str>,
    matched: &'static [&'static str],
}

/// Fern's OpenAPI-sourced `query-parameters-openapi` seed (offline corpus).
const QUERY_PARAMETERS: Corpus = Corpus {
    api: "query-parameters-openapi",
    package_name: "seed",
    project_name: "fern_query-parameters-openapi",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        "src/seed/version.py",
        "src/seed/py.typed",
        "src/seed/types/user.py",
        "src/seed/types/nested_user.py",
        // Static `core/` runtime assets that reproduce across both Fern corpora
        // (this seed pins a different Fern version than `exhaustive`, so only the
        // assets that are byte-identical between the two versions are matched
        // here — locking in that the vendored assets track upstream).
        "src/seed/core/api_error.py",
        "src/seed/core/file.py",
        "src/seed/core/force_multipart.py",
        "src/seed/core/http_sse/__init__.py",
        "src/seed/core/http_sse/_exceptions.py",
        "src/seed/core/http_sse/_models.py",
        "src/seed/core/query_encoder.py",
        "src/seed/core/remove_none_from_dict.py",
    ],
};

/// The broad legacy `exhaustive` target: Fern 4.35 output over the vendored
/// OpenAPI document (see scripts/generate-fern-fixture.sh). Its `matched` list
/// retains only paths unchanged by the Fern 5.20 upgrade; current managed corpus
/// fixtures gate the newer runtime, endpoint parsing, types, docs, and scaffolding.
/// See docs/matching.md.
const EXHAUSTIVE: Corpus = Corpus {
    api: "exhaustive",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        "src/fern/version.py",
        "src/fern/py.typed",
        // Static core assets that did not change between Fern 4.35 and 5.20.
        "src/fern/core/api_error.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/types/bad_object_request_info.py",
        "src/fern/types/endpoints_error.py",
        "src/fern/types/endpoints_paginated_response.py",
        "src/fern/types/endpoints_put_response.py",
        "src/fern/types/types_animal.py",
        "src/fern/types/types_animal_one.py",
        "src/fern/types/types_animal_zero.py",
        "src/fern/types/types_mixed_type.py",
        "src/fern/types/types_object_with_docs.py",
        "src/fern/types/types_object_with_required_field.py",
        "src/fern/types/types_optional_alias.py",
        // Endpoint client package markers (one per operation group).
        "src/fern/endpoints_container/__init__.py",
        "src/fern/endpoints_content_type/__init__.py",
        "src/fern/endpoints_enum/__init__.py",
        "src/fern/endpoints_http_methods/__init__.py",
        "src/fern/endpoints_object/__init__.py",
        "src/fern/endpoints_pagination/__init__.py",
        "src/fern/endpoints_params/__init__.py",
        "src/fern/endpoints_primitive/__init__.py",
        "src/fern/endpoints_put/__init__.py",
        "src/fern/endpoints_union/__init__.py",
        "src/fern/endpoints_urls/__init__.py",
        "src/fern/inlinedrequests/__init__.py",
        "src/fern/noauth/__init__.py",
        "src/fern/noreqbody/__init__.py",
        "src/fern/reqwithheaders/__init__.py",
        // The typed error package itself is unchanged; Fern 5.20 raw clients add
        // ParsingError handling and are gated by current managed fixtures.
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/__init__.py",
        // Per-tag high-level `client.py`: the sync+async wrappers that return
        // `_response.data`, each with a worked `Examples` docstring synthesized by
        // the example-value generator (objects with required fields, unions, maps,
        // containers, enums, datetimes, the `long` placeholder, ...).
        "src/fern/endpoints_container/client.py",
        "src/fern/endpoints_content_type/client.py",
        "src/fern/endpoints_enum/client.py",
        "src/fern/endpoints_http_methods/client.py",
        "src/fern/endpoints_pagination/client.py",
        "src/fern/endpoints_params/client.py",
        "src/fern/endpoints_primitive/client.py",
        "src/fern/endpoints_put/client.py",
        "src/fern/endpoints_union/client.py",
        "src/fern/endpoints_urls/client.py",
        "src/fern/inlinedrequests/client.py",
        "src/fern/noauth/client.py",
        "src/fern/noreqbody/client.py",
        "src/fern/reqwithheaders/client.py",
        // The type aggregator remains stable; the package root changed with 5.20.
        "src/fern/types/__init__.py",
    ],
};

/// Feature-coverage target specs: hand-authored OpenAPI documents that exercise
/// shapes crozier does not fully generate yet (the gaps in docs/matching.md) —
/// auth schemes beyond bearer, inline request/response hoisting, cookie params,
/// form bodies, discriminated unions, schema constraints, integer enums, and
/// document-level servers/webhooks/callbacks.
///
/// Their Fern `expected/` trees were produced by running Fern's container
/// generator with the scaffold defaults (`--package-name fern`,
/// `--project-name default_package_name`; see scripts/generate-fern-fixture.sh),
/// so the corpora drive crozier with the same naming. Each `matched` list grows
/// as generation lands; the smoke test asserts crozier consumes every spec
/// without panicking regardless of how much is matched yet.
const FEATURE_TARGETS: &[Corpus] = &[
    Corpus {
        api: "auth-schemes",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/apikeyauth/__init__.py",
            "src/fern/apikeyauth/client.py",
            "src/fern/basicauth/__init__.py",
            "src/fern/basicauth/client.py",
            "src/fern/bearerauth/__init__.py",
            "src/fern/bearerauth/client.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/oauth/__init__.py",
            "src/fern/oauth/client.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/token_response.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "inline-request-response",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/inlined/__init__.py",
            "src/fern/inlined/client.py",
            "src/fern/inlined/types/__init__.py",
            "src/fern/inlined/types/inlined_index_response.py",
            "src/fern/inlined/types/inlined_search_request_filter.py",
            "src/fern/inlined/types/inlined_search_response.py",
            "src/fern/inlined/types/inlined_search_response_neighbor.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/search_result.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "cookie-parameters",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/cookies/__init__.py",
            "src/fern/cookies/client.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/session.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "form-bodies",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/forms/__init__.py",
            "src/fern/forms/client.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/file_metadata.py",
            "src/fern/types/upload_response.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "discriminated-unions",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/shapes/__init__.py",
            "src/fern/shapes/client.py",
            "src/fern/types/__init__.py",
            "src/fern/types/circle.py",
            "src/fern/types/shape.py",
            "src/fern/types/square.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "schema-constraints",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/accounts/__init__.py",
            "src/fern/accounts/client.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/account.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "integer-enums",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/enums/__init__.py",
            "src/fern/enums/client.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/http_status.py",
            "src/fern/types/priority.py",
            "src/fern/types/ticket.py",
            "src/fern/version.py",
        ],
    },
    Corpus {
        api: "servers-webhooks",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/environment.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/subscriptions/__init__.py",
            "src/fern/subscriptions/client.py",
            "src/fern/types/__init__.py",
            "src/fern/version.py",
        ],
    },
    // Gap-exercising targets: previously unproven OpenAPI shapes, each now with its
    // golden Fern `expected/` tree generated (via scripts/generate-fern-fixture.sh)
    // and byte-matched in full. The comment on each records the shape it pins.
    //
    // basic-auth: HTTP `basic` as the sole/primary security scheme. crozier's auth
    // model reproduces it as Fern's `username`/`password` client wrapper (each a
    // `str` or callable), threaded through the root/per-tag clients, docs, and the
    // `httpx.BasicAuth(...)._auth_header` header wiring. Matches in full.
    Corpus {
        api: "basic-auth",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/user/__init__.py",
            "src/fern/user/client.py",
            "src/fern/version.py",
        ],
    },
    // oauth-client-credentials: OAuth2 `clientCredentials` as the primary scheme,
    // with the token endpoint declared as an operation. Fern's plain-OpenAPI oauth2
    // output equals crozier's optional-bearer fallback (no `x-fern-*` extensions to
    // wire a token provider), so this matches in full and pins that equivalence.
    Corpus {
        api: "oauth-client-credentials",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/auth/__init__.py",
            "src/fern/auth/client.py",
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/token_response.py",
            "src/fern/types/user.py",
            "src/fern/users/__init__.py",
            "src/fern/users/client.py",
            "src/fern/version.py",
        ],
    },
    // inline-array-request: a request body that is an array of *inline* objects
    // (not a `$ref`). The element hoists into the tag's `types/` as
    // `{Tag}{Method}RequestItem` (`ItemsCreateBatchRequestItem`), the body serializes
    // through the convert wrapper as `Sequence[..]`, and the worked example
    // constructs the element and imports it from its tag package. Matches in full.
    Corpus {
        api: "inline-array-request",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/items/__init__.py",
            "src/fern/items/client.py",
            "src/fern/items/types/__init__.py",
            "src/fern/items/types/items_create_batch_request_item.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/item.py",
            "src/fern/version.py",
        ],
    },
    // writeonly-fields: one schema used as *both* request body and response, with a
    // required `readOnly` field (server-populated) and a required `writeOnly` field
    // (client-only). Fern orders the inlined request signature/docstring
    // required-first (optional `= OMIT` args last) while the `json={...}` dict keeps
    // schema order — so the `readOnly`/`writeOnly` fields land after the required
    // ones. Also carries a required `date` field. Matches in full.
    Corpus {
        api: "writeonly-fields",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/user.py",
            "src/fern/users/__init__.py",
            "src/fern/users/client.py",
            "src/fern/version.py",
        ],
    },
    // Real-world-spec robustness targets (issue #40). These minimal specs used to
    // make crozier emit invalid Python or hard-error; each now matches Fern across
    // the whole generated SDK — types, the tag-grouped raw/high-level clients, the
    // root client, and the package aggregators — with no auth (no bearer token).
    //
    // Two files per fixture stay unmatched, for reasons orthogonal to #40: (1)
    // `core/client_wrapper.py` — Fern's `X-Fern-SDK-*` identity headers and the
    // `pyproject.toml`/`version.py` scaffolding come from Fern's *packaged* output
    // mode, which needs publishing credentials; the vendored golden trees are Fern's
    // credential-free local (`downloadFiles`) output, which omits them. crozier's
    // packaged wrapper is already byte-validated by the auth'd corpora above. (2)
    // For digit-leading-property only, the client layer — its `getThing` operation
    // is untagged and groupless, so Fern emits a root-level method while crozier
    // still nests it under a single-endpoint client (a separate root-client gap);
    // the fix under test, the `f_2fa_enabled` model, matches in full.
    Corpus {
        api: "digit-leading-property",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/types/__init__.py",
        ],
    },
    // operation-id-non-identifier: a hyphen/space in the `operationId`
    // (`get-all-widgets`, `verify code`) once produced unparseable Python. Both
    // operations are groupless, so Fern groups them by their `widgets` tag and
    // snake-cases the method names (`get_all_widgets`, `verify_code`); the inline
    // response hoists to `VerifyCodeResponse`.
    Corpus {
        api: "operation-id-non-identifier",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            "src/fern/widgets/types/verify_code_response.py",
        ],
    },
    // bracketed-property-names: JSON:API / Rails / Stripe bracketed query and
    // form-body property names (`page[size]`, `filter[name]`) aren't valid Python
    // identifiers. crozier once emitted them verbatim as function parameters,
    // producing source `ruff format` refuses to parse (issue #74). It now folds
    // the identifier to snake_case (`filter[name]` → `filter_name`) while keeping
    // the raw bracketed name as the wire key, matching Fern's tag client, its raw
    // client, and the hoisted `SearchWidgetsResponse`.
    Corpus {
        api: "bracketed-property-names",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            "src/fern/widgets/types/search_widgets_response.py",
        ],
    },
    // missing-operation-id: an operation with no `operationId` (valid OpenAPI) once
    // hard-errored. crozier groups it by its `widgets` tag and synthesizes the
    // method name from the route (`GET /widgets` → `list_widgets`), matching Fern's
    // tag client and its `__init__`.
    Corpus {
        api: "missing-operation-id",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // error-responses (issue #43, gap #1): an operation that declares any non-2xx
    // response used to be silently dropped — crozier emitted its response type but no
    // client method, reporting a successful generation of an uncallable SDK. Now an
    // error response never suppresses method generation: each declared status maps to
    // Fern's typed exception (`404` → `NotFoundError`, `500` → `InternalServerError`,
    // `400` → `BadRequestError`, `422` → `UnprocessableEntityError`, `503` →
    // `ServiceUnavailableError`) raised over the generic `ApiError` fallback, with the
    // body parsed per declared shape — a `$ref` (`Error`), a container
    // (`typing.List[str]`), or `typing.Optional[typing.Any]` for a content-less error.
    // Matches Fern's whole raw/high-level client, error package, and types. Only the
    // package-root `__init__.py` stays unmatched (the `version.py` packaging
    // difference the local golden trees carry).
    Corpus {
        api: "error-responses",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/errors/__init__.py",
            "src/fern/errors/bad_request_error.py",
            "src/fern/errors/internal_server_error.py",
            "src/fern/errors/service_unavailable_error.py",
            "src/fern/errors/unprocessable_entity_error.py",
            "src/fern/types/__init__.py",
            "src/fern/types/error.py",
            "src/fern/types/widget.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // tag-based-grouping (issue #41 gap 1): plain (no `group_method`) operationIds
    // `listWidgets`/`createWidget` under tags `widgets`, `gadgets`/`createGadget`
    // under `gadgets`. Fern groups by first tag into one sub-client per tag with
    // snake_cased methods, orders the sub-clients in path-declaration order
    // (`widgets` before `gadgets`), and hoists each inline response to
    // `{Method}Response` in that tag's own `types/`.
    Corpus {
        api: "tag-based-grouping",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/gadgets/__init__.py",
            "src/fern/gadgets/client.py",
            "src/fern/gadgets/types/__init__.py",
            "src/fern/gadgets/types/create_gadget_response.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            "src/fern/widgets/types/create_widget_response.py",
        ],
    },
    // enum-query-param (issue #41 gap 2a): an inline `type: string` enum on a query
    // parameter. Fern hoists it to a named extensible-enum alias
    // `{Method}Request{Prop}` (`ListWidgetsRequestLevel`) in the tag's `types/`
    // package and references it by name in the client/raw client, rather than
    // inlining the `Union[Literal[..], Any]` at every use site.
    Corpus {
        api: "enum-query-param",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            "src/fern/widgets/types/list_widgets_response.py",
        ],
    },
    // audience-filter (issue #41 gap 3): `x-crozier-audiences` on the operations
    // (`listWidgets`→public, `getStats`→internal; the spec also carries Fern's
    // `x-fern-audiences` so Fern produces the golden). Driven with `--audience public`,
    // crozier prunes to the public operation and the transitive schema closure it
    // references (`Widget`→`WidgetDetail`), dropping the internal `admin` client and
    // the internal-only `Stats` type — byte-matching Fern's audience-filtered SDK.
    Corpus {
        api: "audience-filter",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &["public"],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/types/widget_detail.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // audience-filter-strict (issue #62): the `audience-filter` spec plus an
    // *un-annotated* operation (`/health`, no audiences). Fern's audience filter is
    // exclusive, so `audiences: [public]` drops both the internal `getStats` op AND
    // the un-annotated `healthCheck` op — the golden here is that strict subset.
    // crozier reproduces it only under `--audience-strict`; the permissive default
    // would keep `healthCheck`. The surviving tree is therefore identical to
    // `audience-filter`'s (public op + `Widget`→`WidgetDetail`), proving that strict
    // mode excludes the un-annotated op exactly as Fern does.
    Corpus {
        api: "audience-filter-strict",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &["public"],
        audience_strict: true,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/types/widget_detail.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // sse-streaming (issue #43, gap #3): a `text/event-stream` (SSE) response used to
    // collapse to a `-> None` method that discarded the stream. crozier now emits
    // Fern's context-managed streaming shape: the raw client is a
    // `@contextlib.(async)contextmanager` over `httpx_client.stream(...)` that decodes
    // events through the `core/http_sse` runtime (`EventSource.iter_sse`/`aiter_sse`)
    // into `typing.(Async)Iterator[typing.Optional[typing.Any]]` chunks (Fern's OpenAPI
    // importer does not resolve the `x-fern-streaming` `chunk-schema-ref`, so the chunk
    // stays `Optional[Any]`), and the high-level client yields each chunk with a worked
    // streaming `Examples` block. Matches Fern's whole client layer; only the
    // package-root `__init__.py` stays unmatched (the `version.py` packaging difference).
    Corpus {
        api: "sse-streaming",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/messages/__init__.py",
            "src/fern/messages/client.py",
            "src/fern/types/__init__.py",
            "src/fern/types/stream_chunk.py",
        ],
    },
    // issue #50: enum member / `visit()` parameter names are sanitized into legal
    // Python identifiers instead of crashing the final `ruff format`. `global` (a
    // keyword) → `GLOBAL`/`global_`, `0: Active` (leading digit + punctuation) →
    // `ZERO_ACTIVE`/`zero_active`, and a `type: string` enum whose values are all
    // integers (`size`) drops its members and falls back to `str`. The
    // digit-leading `_01_00_AM` shape Fern itself rejects is covered by the
    // compile-only `enum_sanitization_generates_valid_python` test below, not here.
    Corpus {
        api: "enum-name-sanitization",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // issue #57: an enum value that sanitizes to the `visit(self, …)` receiver
    // name `self` must escape its `visit()` parameter (`self` → `self_`), or the
    // method emits a duplicate `self` argument — valid enough to pass the final
    // `ruff format` but a SyntaxError at import. Fern escapes `self` and leaves
    // `cls` alone (an ordinary parameter on an instance method never shadows the
    // receiver), so `WidgetOwner` pins the escape and `WidgetBinding` pins the
    // deliberate non-escape.
    Corpus {
        api: "enum-receiver-collision",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // Issue #61: `--client-class-name` overrides the generated root client class
    // name (Fern's `client_class_name`), so `AcmeClient`/`AsyncAcmeClient` replace
    // the package-derived `FernApi`. Driven with `--client-class-name AcmeClient`;
    // the whole 33-file tree byte-matches Fern's, threading the name through the
    // root `client.py`, the package `__init__.py` re-exports, the per-tag client's
    // worked examples, and the README/reference snippets.
    Corpus {
        api: "client-class-name",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: Some("AcmeClient"),
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // Issue #63: `--extra-fields` sets Fern's `pydantic_config.extra_fields`, which
    // drives every generated model's `extra` config. Driven with
    // `--extra-fields ignore`; Fern omits the v2 `extra=` kwarg for `ignore` (v2's
    // own default) but keeps the explicit v1 `pydantic.Extra.ignore` member, so
    // `Widget`'s model matches only when crozier reproduces that asymmetry.
    Corpus {
        api: "pydantic-extra-fields",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: Some("ignore"),
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
        ],
    },
    // Recursive schemas (issue #84): a self-referential model (`TreeNode`) and a
    // recursive discriminated union (`Node` → `AndNode.children: List[Node]`).
    // Both render with `from __future__ import annotations`, string forward
    // references, and `update_forward_refs`, and no self-import — where crozier
    // previously emitted a circular self-import and stack-overflowed the generator.
    Corpus {
        api: "recursive-types",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/pred/__init__.py",
            "src/fern/py.typed",
            "src/fern/tree/__init__.py",
            "src/fern/tree/client.py",
            "src/fern/types/__init__.py",
            // The recursion payoff: a self-referential model and a recursive
            // discriminated union, each with forward refs + `update_forward_refs`.
            "src/fern/types/leaf_node.py",
            "src/fern/types/tree_node.py",
            "src/fern/version.py",
        ],
    },
    // Per-operation nested types importing `core` at the correct relative depth
    // (issue #85): an inline request-body object hoisted to `widgets/types/…`
    // reaches `core.serialization` with `...core`, not the depth-wrong `..core`.
    Corpus {
        api: "nested-core-imports",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            // The fix's payoff: a nested per-operation type reaching `core` at the
            // right relative depth (`...core.serialization`, not `..core`).
        ],
    },
    // A property whose schema node is a JSON array (issue #86): a misplaced
    // `required` list inside `properties` degrades to `Optional[Any]` instead of
    // synthesizing a bogus type name and a dangling import.
    Corpus {
        api: "malformed-property-schema",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        matched: &[
            "src/fern/core/api_error.py",
            "src/fern/core/file.py",
            "src/fern/core/force_multipart.py",
            "src/fern/core/http_sse/__init__.py",
            "src/fern/core/http_sse/_exceptions.py",
            "src/fern/core/http_sse/_models.py",
            "src/fern/core/query_encoder.py",
            "src/fern/core/remove_none_from_dict.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/types/__init__.py",
            // The fix's payoff: the malformed `required` node degrades to
            // `Optional[Any]` rather than emitting a dangling type import.
            "src/fern/widgets/types/search_widgets_response.py",
        ],
    },
];

/// Path to a fixture directory under `tests/fixtures/`.
fn fixture_dir(api: &str) -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures")
        .join(api)
}

const KNOWN_FERN_FAILURE_FILE: &str = "known-fern-failure.json";

struct KnownFernFailure {
    generator: String,
    generator_version: String,
}

/// Validate a deliberately narrow upstream Fern failure registration. The
/// generation workflow verifies the full diagnostic fingerprint against Fern;
/// the Rust boundary consumes the same checked-in identity before substituting a
/// real successful Crozier generation for an impossible Fern byte comparison.
fn known_fern_failure(c: &Corpus) -> Result<Option<KnownFernFailure>, String> {
    let path = fixture_dir(c.api).join(KNOWN_FERN_FAILURE_FILE);
    if !path.exists() {
        return Ok(None);
    }
    let bytes = std::fs::read(&path)
        .map_err(|error| format!("could not read {}: {error}", path.display()))?;
    let payload: serde_json::Value = serde_json::from_slice(&bytes)
        .map_err(|error| format!("invalid {}: {error}", path.display()))?;
    let object = payload
        .as_object()
        .ok_or_else(|| format!("{} must contain a JSON object", path.display()))?;
    let expected_keys = [
        "schema_version",
        "generator",
        "generator_version",
        "corpus_spec_name",
        "corpus_spec_ref",
        "corpus_spec_url",
        "exit_code",
        "fingerprint",
    ];
    if object.len() != expected_keys.len()
        || expected_keys.iter().any(|key| !object.contains_key(*key))
    {
        return Err(format!(
            "{} does not have the exact known-failure contract keys",
            path.display()
        ));
    }
    let exact_values = [
        ("schema_version", serde_json::json!(1)),
        ("generator", serde_json::json!("fernapi/fern-python-sdk")),
        ("generator_version", serde_json::json!("5.20.0")),
        ("corpus_spec_name", serde_json::json!(c.api)),
        ("corpus_spec_ref", serde_json::json!("1.0.0")),
        (
            "corpus_spec_url",
            serde_json::json!(
                "https://api.apis.guru/v2/specs/calorieninjas.com/1.0.0/openapi.json"
            ),
        ),
        ("exit_code", serde_json::json!(1)),
    ];
    for (key, expected) in exact_values {
        if object.get(key) != Some(&expected) {
            return Err(format!(
                "{} has stale {key}: expected {expected}",
                path.display()
            ));
        }
    }
    let fingerprint = object["fingerprint"]
        .as_object()
        .ok_or_else(|| format!("{} has no fingerprint object", path.display()))?;
    if fingerprint.get("failed_command")
        != Some(&serde_json::json!(
            "ruff check --fix --no-cache --ignore E741 /fern/output"
        ))
        || fingerprint.get("ruff_summary")
            != Some(&serde_json::json!(
                "Found 11 errors (5 fixed, 6 remaining)."
            ))
    {
        return Err(format!("{} has stale Ruff failure markers", path.display()));
    }
    let diagnostics = fingerprint
        .get("diagnostics")
        .and_then(serde_json::Value::as_array)
        .ok_or_else(|| format!("{} has no diagnostic list", path.display()))?;
    if diagnostics.len() != 6
        || diagnostics.iter().any(|diagnostic| {
            diagnostic.get("message")
                != Some(&serde_json::json!("SyntaxError: Expected an identifier"))
        })
    {
        return Err(format!(
            "{} must fingerprint exactly six identifier syntax errors",
            path.display()
        ));
    }
    if fixture_dir(c.api)
        .join("expected/.crozier-fern-golden.json")
        .exists()
    {
        return Err(format!(
            "{} is stale because a provenance-current golden exists",
            path.display()
        ));
    }
    Ok(Some(KnownFernFailure {
        generator: object["generator"].as_str().unwrap().to_owned(),
        generator_version: object["generator_version"].as_str().unwrap().to_owned(),
    }))
}

fn known_fern_failure_marker(c: &Corpus, known: &KnownFernFailure) -> String {
    format!(
        "KNOWN UPSTREAM FERN FAILURE: {} at {}:{}; Crozier generation succeeded.",
        c.api, known.generator, known.generator_version
    )
}

/// The OpenAPI spec a corpus generates from. A vendored corpus ships its
/// `openapi.yml`; a `link-ok` corpus (`tests/fixtures/CORPUS.md`, spec not
/// redistributed) is fetched into `.local/corpus/<api>/openapi.<source suffix>`
/// by `scripts/fetch-corpus.sh` — `None` when that fetch has not run.
fn corpus_spec(api: &str) -> Option<PathBuf> {
    let vendored = fixture_dir(api).join("openapi.yml");
    if vendored.exists() {
        return Some(vendored);
    }
    let fetched = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(".local/corpus")
        .join(api);
    ["openapi.json", "openapi.yaml", "openapi.yml"]
        .into_iter()
        .map(|name| fetched.join(name))
        .find(|path| path.exists())
}

/// Fresh `crozier` command bound to the built binary.
fn crozier() -> Command {
    Command::cargo_bin("crozier").expect("crozier binary is built for tests")
}

/// Normalize the SDK-identity headers out of the comparison. crozier brands its
/// own `X-Crozier-*` headers rather than impersonating Fern, and — because it
/// reproduces Fern's *packaged* wrapper — always emits the `SDK-Name`/`SDK-Version`
/// headers that Fern's publishing metadata supplies, which the credential-free
/// local golden trees omit. Both are deliberate, non-behavioral differences in tool
/// branding/packaging, so drop the `SDK-Name`/`SDK-Version` lines and canonicalize
/// the remaining `X-Crozier-` prefix (the `Language` header) to `X-Fern-`. Applied
/// to both sides; a no-op on lines the fixtures don't contain.
fn normalize_sdk_headers(content: &str) -> String {
    let is_sdk_identity_line = |line: &str| {
        let t = line.trim_start();
        [
            "X-Fern-SDK-Name",
            "X-Crozier-SDK-Name",
            "X-Fern-SDK-Version",
            "X-Crozier-SDK-Version",
        ]
        .iter()
        .any(|h| t.starts_with(&format!("\"{h}\"")))
    };
    content
        .split_inclusive('\n')
        .filter(|line| !is_sdk_identity_line(line))
        .collect::<String>()
        .replace("X-Crozier-", "X-Fern-")
}

/// Normalize a lazy-loader `__init__.py` for comparison: drop leading blank lines
/// (a comment-strip artifact) and canonicalize the import order with `ruff` isort,
/// so the semantically-irrelevant `TYPE_CHECKING` ordering does not gate the match.
fn try_normalize_init(content: &str) -> Result<String, String> {
    let trimmed: String = content
        .split_inclusive('\n')
        .skip_while(|line| line.trim().is_empty())
        .collect();
    try_ruff_isort(&trimmed)
}

/// Drop Fern's `generatorConfig` block from `.fern/metadata.json`. Because the
/// whole corpus is generated with `pydantic_config.enum_type: python_enums` (so
/// enums render as real classes — see docs/matching.md), Fern records that config
/// in its provenance file. crozier renders python_enums unconditionally and carries
/// no such config, so — like the SDK-identity headers — this Fern-only provenance is
/// normalized out of both sides rather than faked by crozier. Applied only to
/// `metadata.json`; a no-op on content without the block. The block is the object's
/// last key, so removing it plus the preceding comma restores the shorter form.
fn normalize_metadata(content: &str) -> String {
    let Some(start) = content.find("\"generatorConfig\"") else {
        return content.to_string();
    };
    let before = content[..start].trim_end();
    let before = before.strip_suffix(',').unwrap_or(before);
    // Skip past the balanced `{ ... }` value that follows `"generatorConfig":`.
    let rest = &content[start..];
    let (mut depth, mut started, mut end) = (0i32, false, rest.len());
    for (i, ch) in rest.char_indices() {
        match ch {
            '{' => {
                depth += 1;
                started = true;
            }
            '}' if started => {
                depth -= 1;
                if depth == 0 {
                    end = i + 1;
                    break;
                }
            }
            _ => {}
        }
    }
    format!("{before}{}", &rest[end..])
}

/// Run `ruff check --select I --fix` over a source string, returning the
/// import-sorted result. Uses the same `ruff` the generator depends on.
fn try_ruff_isort(source: &str) -> Result<String, String> {
    use std::io::Write;
    use std::process::{Command as PCommand, Stdio};
    let mut child = PCommand::new("ruff")
        .args([
            "check",
            "--select",
            "I",
            "--fix",
            "--stdin-filename",
            "x.py",
            "-",
        ])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|error| format!("could not run ruff (see docs/matching.md): {error}"))?;
    child
        .stdin
        .take()
        .ok_or_else(|| "ruff stdin was not piped".to_string())?
        .write_all(source.as_bytes())
        .map_err(|error| format!("could not write to ruff: {error}"))?;
    let out = child
        .wait_with_output()
        .map_err(|error| format!("could not wait for ruff: {error}"))?;
    // Trust ruff's stdout only when it exited cleanly — a non-zero exit (e.g. a
    // syntax error in the input) must surface, not silently yield wrong text.
    if !out.status.success() {
        return Err(format!(
            "ruff isort failed ({}): {}",
            out.status,
            String::from_utf8_lossy(&out.stderr).trim()
        ));
    }
    String::from_utf8(out.stdout).map_err(|error| format!("ruff output is not UTF-8: {error}"))
}

/// Drive the compiled binary over a corpus's spec and require every file in its
/// `matched` list to equal the committed fixture once comments are stripped.
fn assert_corpus_matches(c: &Corpus) {
    let fixtures = fixture_dir(c.api);
    let out = generate_corpus(c);

    for rel in c.matched {
        let generated = std::fs::read_to_string(out.path().join(rel))
            .unwrap_or_else(|e| panic!("crozier did not write {rel}: {e}"));
        let expected = std::fs::read_to_string(fixtures.join("expected").join(rel))
            .unwrap_or_else(|e| panic!("missing fixture {rel}: {e}"));
        if !generated_matches_fixture(rel, &generated, &expected) {
            // Show the exact gate-relevant diff inline instead of a bare "does not
            // match" — the normalized bytes the comparison actually decides on, so a
            // regression is diagnosable straight from the test output (no second
            // generate-and-diff pass). `just fixtures-diff` prints the same thing on
            // demand for a file not (yet) in `matched`.
            let (actual, expected) = normalized_pair(rel, &generated, &expected);
            let diff = unified_diff(&expected, &actual).unwrap_or_default();
            panic!(
                "generated {rel} does not match the Fern fixture \
                 (normalized diff; `-` = Fern golden, `+` = crozier). \
                 Reproduce with `just fixtures-diff {} {rel}`; fix the generator, \
                 never the fixture.\n{diff}",
                c.api
            );
        }
    }
}

/// Generate a corpus's SDK into a fresh tempdir with that corpus's naming, and
/// return the dir (the caller keeps it alive). Fails the test if crozier errors —
/// shared by the gate and the candidate reporter so both drive the binary
/// identically.
fn generate_corpus(c: &Corpus) -> tempfile::TempDir {
    let out = tempfile::tempdir().expect("tempdir");
    corpus_command(c, out.path())
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    out
}

/// The exact public CLI invocation used for a corpus. Reporters call the same
/// command without assert_cmd's fail-fast assertion so one broken corpus cannot
/// hide differences in its siblings.
fn corpus_command(c: &Corpus, output: &Path) -> Command {
    let mut command = crozier();
    command
        .args(["generate", "--spec"])
        .arg(corpus_spec(c.api).unwrap_or_else(|| fixture_dir(c.api).join("openapi.yml")))
        .arg("--output")
        .arg(output)
        .args([
            "--package-name",
            c.package_name,
            "--project-name",
            c.project_name,
        ])
        .args(c.audiences.iter().flat_map(|a| ["--audience", a]))
        .args(c.audience_strict.then_some("--audience-strict"))
        .args(
            c.client_class_name
                .iter()
                .flat_map(|n| ["--client-class-name", n]),
        )
        .args(c.extra_fields.iter().flat_map(|e| ["--extra-fields", e]));
    command
}

fn try_generate_corpus(c: &Corpus) -> Result<tempfile::TempDir, String> {
    let out = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let result = corpus_command(c, out.path())
        .output()
        .map_err(|error| format!("could not run crozier: {error}"))?;
    let stderr = String::from_utf8_lossy(&result.stderr);
    if !result.status.success() || !stderr.contains("generated") {
        return Err(format!(
            "crozier exited {}: {}",
            result
                .status
                .code()
                .map_or_else(|| "without a status".to_string(), |code| code.to_string()),
            stderr.trim()
        ));
    }
    Ok(out)
}

/// Whether crozier's `generated` output for `rel` equals the committed fixture
/// under the gate's normalization — the single definition of "matches", used by
/// both `assert_corpus_matches` and the candidate reporter so they never drift.
///
/// Python files are compared with comments stripped (the same normalization that
/// produced the fixtures); non-Python scaffolding (pyproject.toml, requirements.txt,
/// JSON) is Fern's verbatim output and compared as-is.
///
/// The lazy-loader `__init__.py` aggregators are normalized on both sides first:
/// leading blank lines (a comment-strip artifact of Fern's multi-line header) are
/// trimmed, and the `TYPE_CHECKING` import block is canonicalized with `ruff` isort.
/// That block is never executed, so its order carries no meaning — normalizing it
/// lets crozier sort imports straightforwardly instead of reproducing Fern's
/// traversal order.
///
/// The SDK-identity headers are also normalized out of both sides (see
/// [`normalize_sdk_headers`]): crozier's `X-Crozier-*` rebrand and the
/// packaging-only `SDK-Name`/`SDK-Version` lines are deliberate, non-behavioral
/// differences in tool branding/packaging.
fn generated_matches_fixture(rel: &str, generated: &str, expected: &str) -> bool {
    let (actual, expected) = normalized_pair(rel, generated, expected);
    actual == expected
}

/// The exact `(actual, expected)` strings the gate compares for `rel`, after the
/// per-file normalization described on [`generated_matches_fixture`]. Factored out
/// so the match check and the diff reporters share one definition of "the bytes
/// that decide the match" — a printed diff is then precisely what the gate sees,
/// never a raw diff polluted by comments, SDK-identity headers, or `__init__.py`
/// import order that the gate already normalizes away.
fn normalized_pair(rel: &str, generated: &str, expected: &str) -> (String, String) {
    try_normalized_pair(rel, generated, expected).unwrap_or_else(|error| panic!("{error}"))
}

fn try_normalized_pair(
    rel: &str,
    generated: &str,
    expected: &str,
) -> Result<(String, String), String> {
    let generated = normalize_sdk_headers(generated);
    let expected = normalize_sdk_headers(expected);
    if rel.ends_with("__init__.py") {
        Ok((
            try_normalize_init(&crozier::strip_python_comments(&generated))?,
            try_normalize_init(&expected)?,
        ))
    } else if rel.ends_with(".py") {
        Ok((crozier::strip_python_comments(&generated), expected))
    } else if rel.ends_with("metadata.json") {
        Ok((
            normalize_metadata(&generated),
            normalize_metadata(&expected),
        ))
    } else {
        Ok((generated, expected))
    }
}

/// A minimal unified-style line diff of two already-normalized texts, dependency-free
/// (the suite avoids a diff crate for one use, as [`walk_files`] avoids `walkdir`).
/// Lines only in `expected` are prefixed `-`, only in `actual` `+`, shared lines a
/// space; runs of unchanged lines beyond `CONTEXT` around each change collapse to a
/// `⋮ (N unchanged line(s))` marker so a one-line drift in a large file prints a few
/// lines, not the whole file. Returns `None` when the two are byte-identical.
fn unified_diff(expected: &str, actual: &str) -> Option<String> {
    if expected == actual {
        return None;
    }
    const CONTEXT: usize = 3;
    let a: Vec<&str> = expected.lines().collect();
    let b: Vec<&str> = actual.lines().collect();
    let (n, m) = (a.len(), b.len());

    // Longest-common-subsequence lengths, filled from the bottom-right.
    let mut lcs = vec![vec![0u32; m + 1]; n + 1];
    for i in (0..n).rev() {
        for j in (0..m).rev() {
            lcs[i][j] = if a[i] == b[j] {
                lcs[i + 1][j + 1] + 1
            } else {
                lcs[i + 1][j].max(lcs[i][j + 1])
            };
        }
    }

    // Backtrack into an edit script of (sign, line) ops.
    let mut ops: Vec<(char, &str)> = Vec::new();
    let (mut i, mut j) = (0usize, 0usize);
    while i < n && j < m {
        if a[i] == b[j] {
            ops.push((' ', a[i]));
            i += 1;
            j += 1;
        } else if lcs[i + 1][j] >= lcs[i][j + 1] {
            ops.push(('-', a[i]));
            i += 1;
        } else {
            ops.push(('+', b[j]));
            j += 1;
        }
    }
    while i < n {
        ops.push(('-', a[i]));
        i += 1;
    }
    while j < m {
        ops.push(('+', b[j]));
        j += 1;
    }

    // Keep every change, plus CONTEXT unchanged lines on each side; collapse the rest.
    let keep: Vec<bool> = (0..ops.len())
        .map(|k| {
            let lo = k.saturating_sub(CONTEXT);
            let hi = (k + CONTEXT).min(ops.len() - 1);
            (lo..=hi).any(|x| ops[x].0 != ' ')
        })
        .collect();

    let mut out = String::new();
    let mut elided = 0usize;
    for (k, (sign, line)) in ops.iter().enumerate() {
        if keep[k] {
            if elided > 0 {
                out.push_str(&format!("      ⋮ ({elided} unchanged line(s))\n"));
                elided = 0;
            }
            out.push(*sign);
            out.push(' ');
            out.push_str(line);
            out.push('\n');
        } else {
            elided += 1;
        }
    }
    if elided > 0 {
        out.push_str(&format!("      ⋮ ({elided} unchanged line(s))\n"));
    }
    Some(out)
}

#[test]
fn query_parameters_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&QUERY_PARAMETERS);
}

#[test]
fn exhaustive_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&EXHAUSTIVE);
}

/// Reporter-approved paths for the MAIF Otoroshi corpus are kept separately from
/// its `Corpus` declaration only to keep the existing corpus registry readable.
const MAIF_OTOROSHI_MATCHED: &[&str] = &[
    ".fern/metadata.json",
    "pyproject.toml",
    "README.md",
    "reference.md",
    "requirements.txt",
    "src/fern/__init__.py",
    "src/fern/apikeys/__init__.py",
    "src/fern/apikeys/client.py",
    "src/fern/apikeys/raw_client.py",
    "src/fern/auth_config/types/create_global_auth_module_response.py",
    "src/fern/auth_config/__init__.py",
    "src/fern/auth_config/client.py",
    "src/fern/auth_config/raw_client.py",
    "src/fern/auth_config/types/__init__.py",
    "src/fern/auth_config/types/create_global_auth_module_request.py",
    "src/fern/auth_config/types/find_all_global_auth_modules_response_item.py",
    "src/fern/auth_config/types/find_global_auth_module_by_id_response.py",
    "src/fern/auth_config/types/patch_global_auth_module_response.py",
    "src/fern/auth_config/types/update_global_auth_module_request_body.py",
    "src/fern/auth_config/types/update_global_auth_module_response.py",
    "src/fern/certificates/__init__.py",
    "src/fern/certificates/client.py",
    "src/fern/certificates/raw_client.py",
    "src/fern/client.py",
    "src/fern/configuration/__init__.py",
    "src/fern/configuration/client.py",
    "src/fern/configuration/raw_client.py",
    "src/fern/core/__init__.py",
    "src/fern/core/api_error.py",
    "src/fern/core/client_wrapper.py",
    "src/fern/core/datetime_utils.py",
    "src/fern/core/file.py",
    "src/fern/core/force_multipart.py",
    "src/fern/core/http_client.py",
    "src/fern/core/http_response.py",
    "src/fern/core/http_sse/__init__.py",
    "src/fern/core/http_sse/_api.py",
    "src/fern/core/http_sse/_decoders.py",
    "src/fern/core/http_sse/_exceptions.py",
    "src/fern/core/http_sse/_models.py",
    "src/fern/core/jsonable_encoder.py",
    "src/fern/core/pydantic_utilities.py",
    "src/fern/core/query_encoder.py",
    "src/fern/core/remove_none_from_dict.py",
    "src/fern/core/request_options.py",
    "src/fern/core/serialization.py",
    "src/fern/data_exporter_configs/__init__.py",
    "src/fern/data_exporter_configs/client.py",
    "src/fern/data_exporter_configs/raw_client.py",
    "src/fern/data_exporter_configs/types/__init__.py",
    "src/fern/data_exporter_configs/types/create_bulk_data_exporter_configs_response_item.py",
    "src/fern/data_exporter_configs/types/create_bulk_data_exporter_configs_response_item_status.py",
    "src/fern/data_exporter_configs/types/deletebulk_data_exporter_config_response_item.py",
    "src/fern/data_exporter_configs/types/deletebulk_data_exporter_config_response_item_status.py",
    "src/fern/data_exporter_configs/types/patch_bulk_data_exporter_config_response_item.py",
    "src/fern/data_exporter_configs/types/patch_bulk_data_exporter_config_response_item_status.py",
    "src/fern/data_exporter_configs/types/update_bulk_data_exporter_config_response_item.py",
    "src/fern/data_exporter_configs/types/update_bulk_data_exporter_config_response_item_status.py",
    "src/fern/environment.py",
    "src/fern/environments/__init__.py",
    "src/fern/environments/client.py",
    "src/fern/environments/raw_client.py",
    "src/fern/errors/__init__.py",
    "src/fern/errors/bad_request_error.py",
    "src/fern/errors/not_found_error.py",
    "src/fern/errors/unauthorized_error.py",
    "src/fern/groups/__init__.py",
    "src/fern/groups/client.py",
    "src/fern/groups/raw_client.py",
    "src/fern/import_/__init__.py",
    "src/fern/import_/client.py",
    "src/fern/import_/raw_client.py",
    "src/fern/jwt_verifiers/__init__.py",
    "src/fern/jwt_verifiers/client.py",
    "src/fern/jwt_verifiers/raw_client.py",
    "src/fern/py.typed",
    "src/fern/raw_client.py",
    "src/fern/scripts/__init__.py",
    "src/fern/scripts/client.py",
    "src/fern/scripts/raw_client.py",
    "src/fern/services/__init__.py",
    "src/fern/services/client.py",
    "src/fern/services/raw_client.py",
    "src/fern/snowmonkey/__init__.py",
    "src/fern/snowmonkey/client.py",
    "src/fern/snowmonkey/raw_client.py",
    "src/fern/stats/__init__.py",
    "src/fern/stats/client.py",
    "src/fern/stats/raw_client.py",
    "src/fern/templates/__init__.py",
    "src/fern/templates/client.py",
    "src/fern/templates/raw_client.py",
    "src/fern/types/__init__.py",
    "src/fern/types/api_key.py",
    "src/fern/types/auth0config.py",
    "src/fern/types/bad_response.py",
    "src/fern/types/bad_responses_fault_config.py",
    "src/fern/types/canary.py",
    "src/fern/types/certificate.py",
    "src/fern/types/chaos_config.py",
    "src/fern/types/clever_settings.py",
    "src/fern/types/client_config.py",
    "src/fern/types/console_data_exporter_config.py",
    "src/fern/types/cors_settings.py",
    "src/fern/types/custom_data_exporter_config.py",
    "src/fern/types/data_exporter_config.py",
    "src/fern/types/data_exporter_config_config.py",
    "src/fern/types/data_exporter_config_typ.py",
    "src/fern/types/deleted.py",
    "src/fern/types/done.py",
    "src/fern/types/elastic_config.py",
    "src/fern/types/environment.py",
    "src/fern/types/error_template.py",
    "src/fern/types/es_algo_settings.py",
    "src/fern/types/exposed_api.py",
    "src/fern/types/file_data_exporter_config.py",
    "src/fern/types/filtering.py",
    "src/fern/types/generic_oauth2module_config.py",
    "src/fern/types/generic_oauth2module_config_jwt_verifier.py",
    "src/fern/types/global_config.py",
    "src/fern/types/global_jwt_verifier.py",
    "src/fern/types/global_jwt_verifier_algo_settings.py",
    "src/fern/types/global_jwt_verifier_source.py",
    "src/fern/types/global_jwt_verifier_strategy.py",
    "src/fern/types/group.py",
    "src/fern/types/gzip.py",
    "src/fern/types/health_check.py",
    "src/fern/types/hs_algo_settings.py",
    "src/fern/types/import_export.py",
    "src/fern/types/import_export_admins_item.py",
    "src/fern/types/import_export_api_keys_item.py",
    "src/fern/types/import_export_error_templates_item.py",
    "src/fern/types/import_export_service_descriptors_item.py",
    "src/fern/types/import_export_service_descriptors_item_jwt_verifier.py",
    "src/fern/types/import_export_service_descriptors_item_sec_com_settings.py",
    "src/fern/types/import_export_service_groups_item.py",
    "src/fern/types/import_export_simple_admins_item.py",
    "src/fern/types/import_export_stats.py",
    "src/fern/types/in_cookie.py",
    "src/fern/types/in_header.py",
    "src/fern/types/in_memory_auth_module_config.py",
    "src/fern/types/in_memory_user.py",
    "src/fern/types/in_query_param.py",
    "src/fern/types/ip_filtering.py",
    "src/fern/types/jwks_algo_settings.py",
    "src/fern/types/kafka_config.py",
    "src/fern/types/large_request_fault_config.py",
    "src/fern/types/large_response_fault_config.py",
    "src/fern/types/latency_injection_fault_config.py",
    "src/fern/types/ldap_auth_module_config.py",
    "src/fern/types/ldap_user.py",
    "src/fern/types/local_jwt_verifier.py",
    "src/fern/types/local_jwt_verifier_algo_settings.py",
    "src/fern/types/local_jwt_verifier_source.py",
    "src/fern/types/local_jwt_verifier_strategy.py",
    "src/fern/types/location.py",
    "src/fern/types/mailer_console_exporter_config.py",
    "src/fern/types/mailer_console_exporter_config_type.py",
    "src/fern/types/mailer_generic_exporter_config.py",
    "src/fern/types/mailer_generic_exporter_config_type.py",
    "src/fern/types/mailer_mailgun_exporter_config.py",
    "src/fern/types/mailer_mailgun_exporter_config_type.py",
    "src/fern/types/mailer_mailjet_exporter_config.py",
    "src/fern/types/mailer_mailjet_exporter_config_type.py",
    "src/fern/types/mailer_sendgrid_exporter_config.py",
    "src/fern/types/mailer_sendgrid_exporter_config_type.py",
    "src/fern/types/mailer_settings.py",
    "src/fern/types/mapping_settings.py",
    "src/fern/types/otoroshi_health.py",
    "src/fern/types/otoroshi_health_datastore.py",
    "src/fern/types/otoroshi_health_otoroshi.py",
    "src/fern/types/outage.py",
    "src/fern/types/outage_strategy.py",
    "src/fern/types/pass_through.py",
    "src/fern/types/patch.py",
    "src/fern/types/patch_item.py",
    "src/fern/types/patch_item_op.py",
    "src/fern/types/pulsar_data_exporter_config.py",
    "src/fern/types/quotas.py",
    "src/fern/types/redirection_settings.py",
    "src/fern/types/ref_jwt_verifier.py",
    "src/fern/types/rs_algo_settings.py",
    "src/fern/types/script.py",
    "src/fern/types/script_compilation_error.py",
    "src/fern/types/script_compilation_result.py",
    "src/fern/types/service.py",
    "src/fern/types/service_jwt_verifier.py",
    "src/fern/types/service_sec_com_settings.py",
    "src/fern/types/sign.py",
    "src/fern/types/sign_algo_settings.py",
    "src/fern/types/simple_admin.py",
    "src/fern/types/snow_monkey_config.py",
    "src/fern/types/stats.py",
    "src/fern/types/statsd_config.py",
    "src/fern/types/target.py",
    "src/fern/types/transform.py",
    "src/fern/types/transform_algo_settings.py",
    "src/fern/types/transform_settings.py",
    "src/fern/types/transform_settings_location.py",
    "src/fern/types/u2f_admin.py",
    "src/fern/types/validation_authority.py",
    "src/fern/types/verification_settings.py",
    "src/fern/types/webhook.py",
    "src/fern/types/whebhook_config.py",
    "src/fern/validation_authorities/__init__.py",
    "src/fern/validation_authorities/client.py",
    "src/fern/validation_authorities/raw_client.py",
    "src/fern/version.py",
];

/// `apideck.com-crm`: a real-world `link-ok` corpus API (issue #77). Its OpenAPI
/// spec is fetched, not vendored (`corpus_spec`); its full Fern golden is
/// committed. crozier reproduces it byte-for-byte except [`APIDECK_CRM_GAPS`].
const APIDECK_CRM: Corpus = Corpus {
    api: "apideck.com-crm",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[],
};

const APIDECK_HRIS: Corpus = Corpus {
    api: "apideck.com-hris",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/_default_clients.py",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/companies/__init__.py",
        "src/fern/companies/client.py",
        "src/fern/companies/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/departments/__init__.py",
        "src/fern/departments/client.py",
        "src/fern/departments/raw_client.py",
        "src/fern/employee_payrolls/__init__.py",
        "src/fern/employee_payrolls/client.py",
        "src/fern/employee_payrolls/raw_client.py",
        "src/fern/employee_schedules/__init__.py",
        "src/fern/employee_schedules/client.py",
        "src/fern/employee_schedules/raw_client.py",
        "src/fern/employees/__init__.py",
        "src/fern/employees/client.py",
        "src/fern/employees/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/jobs/__init__.py",
        "src/fern/jobs/client.py",
        "src/fern/jobs/raw_client.py",
        "src/fern/payrolls/__init__.py",
        "src/fern/payrolls/client.py",
        "src/fern/payrolls/raw_client.py",
        "src/fern/py.typed",
        "src/fern/time_off_requests/__init__.py",
        "src/fern/time_off_requests/client.py",
        "src/fern/time_off_requests/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/benefit.py",
        "src/fern/types/company_id.py",
        "src/fern/types/company_name.py",
        "src/fern/types/compensation.py",
        "src/fern/types/create_department_response.py",
        "src/fern/types/create_employee_response.py",
        "src/fern/types/create_hris_company_response.py",
        "src/fern/types/create_time_off_request_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/created_by.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/deduction.py",
        "src/fern/types/delete_department_response.py",
        "src/fern/types/delete_employee_response.py",
        "src/fern/types/delete_hris_company_response.py",
        "src/fern/types/delete_time_off_request_response.py",
        "src/fern/types/department.py",
        "src/fern/types/description.py",
        "src/fern/types/division.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/employee.py",
        "src/fern/types/employee_compensations_item.py",
        "src/fern/types/employee_compensations_item_flsa_status.py",
        "src/fern/types/employee_employment_role.py",
        "src/fern/types/employee_employment_role_sub_type.py",
        "src/fern/types/employee_employment_role_type.py",
        "src/fern/types/employee_jobs_item.py",
        "src/fern/types/employee_leaving_reason.py",
        "src/fern/types/employee_manager.py",
        "src/fern/types/employee_number.py",
        "src/fern/types/employee_partner.py",
        "src/fern/types/employee_payroll.py",
        "src/fern/types/employee_payrolls.py",
        "src/fern/types/employee_schedules.py",
        "src/fern/types/employee_social_links_item.py",
        "src/fern/types/employee_team.py",
        "src/fern/types/employees_filter.py",
        "src/fern/types/employees_filter_employment_status.py",
        "src/fern/types/employees_sort.py",
        "src/fern/types/employees_sort_by.py",
        "src/fern/types/employment_status.py",
        "src/fern/types/first_name.py",
        "src/fern/types/gender.py",
        "src/fern/types/get_department_response.py",
        "src/fern/types/get_departments_response.py",
        "src/fern/types/get_employee_payroll_response.py",
        "src/fern/types/get_employee_payrolls_response.py",
        "src/fern/types/get_employee_response.py",
        "src/fern/types/get_employee_schedules_response.py",
        "src/fern/types/get_employees_response.py",
        "src/fern/types/get_hris_companies_response.py",
        "src/fern/types/get_hris_company_response.py",
        "src/fern/types/get_hris_job_response.py",
        "src/fern/types/get_hris_jobs_response.py",
        "src/fern/types/get_payroll_response.py",
        "src/fern/types/get_payrolls_response.py",
        "src/fern/types/get_time_off_request_response.py",
        "src/fern/types/get_time_off_requests_response.py",
        "src/fern/types/hris_company.py",
        "src/fern/types/hris_company_status.py",
        "src/fern/types/hris_event_type.py",
        "src/fern/types/hris_job.py",
        "src/fern/types/hris_job_location.py",
        "src/fern/types/hris_jobs.py",
        "src/fern/types/id.py",
        "src/fern/types/language.py",
        "src/fern/types/last_name.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/middle_name.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/payment_unit.py",
        "src/fern/types/payroll.py",
        "src/fern/types/payroll_totals.py",
        "src/fern/types/payrolls_filter.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/photo_url.py",
        "src/fern/types/row_version.py",
        "src/fern/types/schedule.py",
        "src/fern/types/schedule_work_pattern.py",
        "src/fern/types/schedule_work_pattern_even_weeks.py",
        "src/fern/types/schedule_work_pattern_odd_weeks.py",
        "src/fern/types/sort_direction.py",
        "src/fern/types/tax.py",
        "src/fern/types/time_off_request.py",
        "src/fern/types/time_off_request_notes.py",
        "src/fern/types/time_off_request_request_type.py",
        "src/fern/types/time_off_request_status.py",
        "src/fern/types/time_off_request_units.py",
        "src/fern/types/time_off_requests_filter.py",
        "src/fern/types/time_off_requests_filter_time_off_request_status.py",
        "src/fern/types/title.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_department_response.py",
        "src/fern/types/update_employee_response.py",
        "src/fern/types/update_hris_company_response.py",
        "src/fern/types/update_time_off_request_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/updated_by.py",
        "src/fern/types/webhook_event.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/version.py",
    ],
};

/// Files crozier does not yet reproduce for `apideck.com-crm`. Now **empty** —
/// crozier matches the whole golden byte-for-byte. Kept (with its guard) so a
/// future regression that can only be quarantined lands here explicitly rather than
/// weakening the assertion; the test fails if an entry here already matches.
const APIDECK_CRM_GAPS: &[&str] = &[];

/// Enforce the real-world apideck byte-match. The spec is `link-ok` (fetched by
/// `scripts/fetch-corpus.sh` into `.local/corpus`, not vendored), so this **skips**
/// when the spec is absent — including the offline `check` gate, which never
/// fetches — and **fails** when `CROZIER_REQUIRE_CORPUS` is set (the CI corpus leg
/// fetches the spec, then sets it), so the enforced leg can never silently no-op.
#[test]
fn apideck_crm_matches_fern_output() {
    if corpus_spec(APIDECK_CRM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apideck corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping apideck byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    let out = generate_corpus(&APIDECK_CRM);
    let expected_root = fixture_dir(APIDECK_CRM.api).join("expected");
    let mut diverged = Vec::new();
    for rel in walk_files(&expected_root) {
        if APIDECK_CRM_GAPS.contains(&rel.as_str()) {
            continue;
        }
        let generated = std::fs::read_to_string(out.path().join(&rel))
            .unwrap_or_else(|e| panic!("crozier did not write {rel}: {e}"));
        let expected = std::fs::read_to_string(expected_root.join(&rel))
            .unwrap_or_else(|e| panic!("missing fixture {rel}: {e}"));
        if !generated_matches_fixture(&rel, &generated, &expected) {
            diverged.push(rel);
        }
    }
    assert!(
        diverged.is_empty(),
        "apideck diverged from Fern (fix the generator, or add to APIDECK_CRM_GAPS):\n{diverged:#?}"
    );
    // Every declared gap must still differ, so a closed one is removed from the list.
    for gap in APIDECK_CRM_GAPS {
        let generated = std::fs::read_to_string(out.path().join(gap)).unwrap_or_default();
        let expected = std::fs::read_to_string(expected_root.join(gap)).unwrap_or_default();
        assert!(
            !generated_matches_fixture(gap, &generated, &expected),
            "apideck gap `{gap}` now matches Fern — remove it from APIDECK_CRM_GAPS"
        );
    }
}

/// Files crozier reproduces byte-for-byte for `bunq.com`, kept in its own const so
/// the large list stays regenerable in one place. Grown mechanically by `just
/// fixtures-candidates` (never hand-edited): every entry is proven byte-identical by
/// the gate, and the reporter's positive control re-confirms them. The gap — files
/// Fern emits that crozier lays out differently — is categorized in docs/matching.md.
const BUNQ_MATCHED: &[&str] = &[
    ".fern/metadata.json",
    "README.md",
    "pyproject.toml",
    "reference.md",
    "requirements.txt",
    "src/fern/__init__.py",
    "src/fern/attachment/__init__.py",
    "src/fern/attachment/client.py",
    "src/fern/attachment/raw_client.py",
    "src/fern/attachment_public/__init__.py",
    "src/fern/attachment_public/client.py",
    "src/fern/attachment_public/raw_client.py",
    "src/fern/avatar/__init__.py",
    "src/fern/avatar/client.py",
    "src/fern/avatar/raw_client.py",
    "src/fern/billing_contract_subscription/__init__.py",
    "src/fern/billing_contract_subscription/client.py",
    "src/fern/billing_contract_subscription/raw_client.py",
    "src/fern/bunqme_fundraiser_profile/__init__.py",
    "src/fern/bunqme_fundraiser_profile/client.py",
    "src/fern/bunqme_fundraiser_profile/raw_client.py",
    "src/fern/bunqme_fundraiser_result/__init__.py",
    "src/fern/bunqme_fundraiser_result/client.py",
    "src/fern/bunqme_fundraiser_result/raw_client.py",
    "src/fern/bunqme_tab/__init__.py",
    "src/fern/bunqme_tab/client.py",
    "src/fern/bunqme_tab/raw_client.py",
    "src/fern/bunqme_tab_result_response/__init__.py",
    "src/fern/bunqme_tab_result_response/client.py",
    "src/fern/bunqme_tab_result_response/raw_client.py",
    "src/fern/callback_url/__init__.py",
    "src/fern/callback_url/client.py",
    "src/fern/callback_url/raw_client.py",
    "src/fern/card/__init__.py",
    "src/fern/card/client.py",
    "src/fern/card/raw_client.py",
    "src/fern/card_batch/__init__.py",
    "src/fern/card_batch/client.py",
    "src/fern/card_batch/raw_client.py",
    "src/fern/card_batch_replace/__init__.py",
    "src/fern/card_batch_replace/client.py",
    "src/fern/card_batch_replace/raw_client.py",
    "src/fern/card_credit/__init__.py",
    "src/fern/card_credit/client.py",
    "src/fern/card_credit/raw_client.py",
    "src/fern/card_debit/__init__.py",
    "src/fern/card_debit/client.py",
    "src/fern/card_debit/raw_client.py",
    "src/fern/card_name/__init__.py",
    "src/fern/card_name/client.py",
    "src/fern/card_name/raw_client.py",
    "src/fern/certificate_pinned/__init__.py",
    "src/fern/certificate_pinned/client.py",
    "src/fern/certificate_pinned/raw_client.py",
    "src/fern/challenge_request/__init__.py",
    "src/fern/challenge_request/client.py",
    "src/fern/challenge_request/raw_client.py",
    "src/fern/client.py",
    "src/fern/company/__init__.py",
    "src/fern/company/client.py",
    "src/fern/company/raw_client.py",
    "src/fern/confirmation_of_funds/__init__.py",
    "src/fern/confirmation_of_funds/client.py",
    "src/fern/confirmation_of_funds/raw_client.py",
    "src/fern/content/__init__.py",
    "src/fern/content/client.py",
    "src/fern/content/raw_client.py",
    "src/fern/core/__init__.py",
    "src/fern/core/api_error.py",
    "src/fern/core/client_wrapper.py",
    "src/fern/core/datetime_utils.py",
    "src/fern/core/file.py",
    "src/fern/core/force_multipart.py",
    "src/fern/core/http_client.py",
    "src/fern/core/http_response.py",
    "src/fern/core/http_sse/__init__.py",
    "src/fern/core/http_sse/_api.py",
    "src/fern/core/http_sse/_decoders.py",
    "src/fern/core/http_sse/_exceptions.py",
    "src/fern/core/http_sse/_models.py",
    "src/fern/core/jsonable_encoder.py",
    "src/fern/core/pydantic_utilities.py",
    "src/fern/core/query_encoder.py",
    "src/fern/core/remove_none_from_dict.py",
    "src/fern/core/request_options.py",
    "src/fern/core/serialization.py",
    "src/fern/credential_password_ip/__init__.py",
    "src/fern/credential_password_ip/client.py",
    "src/fern/credential_password_ip/raw_client.py",
    "src/fern/currency_cloud_beneficiary/__init__.py",
    "src/fern/currency_cloud_beneficiary/client.py",
    "src/fern/currency_cloud_beneficiary/raw_client.py",
    "src/fern/currency_cloud_beneficiary_requirement/__init__.py",
    "src/fern/currency_cloud_beneficiary_requirement/client.py",
    "src/fern/currency_cloud_beneficiary_requirement/raw_client.py",
    "src/fern/currency_cloud_payment_quote/__init__.py",
    "src/fern/currency_cloud_payment_quote/client.py",
    "src/fern/currency_cloud_payment_quote/raw_client.py",
    "src/fern/currency_conversion/__init__.py",
    "src/fern/currency_conversion/client.py",
    "src/fern/currency_conversion/raw_client.py",
    "src/fern/currency_conversion_quote/__init__.py",
    "src/fern/currency_conversion_quote/client.py",
    "src/fern/currency_conversion_quote/raw_client.py",
    "src/fern/customer_statement/__init__.py",
    "src/fern/customer_statement/client.py",
    "src/fern/customer_statement/raw_client.py",
    "src/fern/definition/__init__.py",
    "src/fern/definition/client.py",
    "src/fern/definition/raw_client.py",
    "src/fern/device/__init__.py",
    "src/fern/device/client.py",
    "src/fern/device/raw_client.py",
    "src/fern/device_server/__init__.py",
    "src/fern/device_server/client.py",
    "src/fern/device_server/raw_client.py",
    "src/fern/draft_payment/__init__.py",
    "src/fern/draft_payment/client.py",
    "src/fern/draft_payment/raw_client.py",
    "src/fern/environment.py",
    "src/fern/errors/__init__.py",
    "src/fern/errors/bad_request_error.py",
    "src/fern/event/__init__.py",
    "src/fern/event/client.py",
    "src/fern/event/raw_client.py",
    "src/fern/export_annual_overview/__init__.py",
    "src/fern/export_annual_overview/client.py",
    "src/fern/export_annual_overview/raw_client.py",
    "src/fern/export_rib/__init__.py",
    "src/fern/export_rib/client.py",
    "src/fern/export_rib/raw_client.py",
    "src/fern/export_statement_card/__init__.py",
    "src/fern/export_statement_card/client.py",
    "src/fern/export_statement_card/raw_client.py",
    "src/fern/export_statement_card_csv/__init__.py",
    "src/fern/export_statement_card_csv/client.py",
    "src/fern/export_statement_card_csv/raw_client.py",
    "src/fern/export_statement_card_pdf/__init__.py",
    "src/fern/export_statement_card_pdf/client.py",
    "src/fern/export_statement_card_pdf/raw_client.py",
    "src/fern/feature_announcement/__init__.py",
    "src/fern/feature_announcement/client.py",
    "src/fern/feature_announcement/raw_client.py",
    "src/fern/generated_cvc2/__init__.py",
    "src/fern/generated_cvc2/client.py",
    "src/fern/generated_cvc2/raw_client.py",
    "src/fern/ideal_merchant_transaction/__init__.py",
    "src/fern/ideal_merchant_transaction/client.py",
    "src/fern/ideal_merchant_transaction/raw_client.py",
    "src/fern/insight_preference_date/__init__.py",
    "src/fern/insight_preference_date/client.py",
    "src/fern/insight_preference_date/raw_client.py",
    "src/fern/insights/__init__.py",
    "src/fern/insights/client.py",
    "src/fern/insights/raw_client.py",
    "src/fern/insights_search/__init__.py",
    "src/fern/insights_search/client.py",
    "src/fern/insights_search/raw_client.py",
    "src/fern/installation/__init__.py",
    "src/fern/installation/client.py",
    "src/fern/installation/raw_client.py",
    "src/fern/instance/__init__.py",
    "src/fern/instance/client.py",
    "src/fern/instance/raw_client.py",
    "src/fern/invoice/__init__.py",
    "src/fern/invoice/client.py",
    "src/fern/invoice/raw_client.py",
    "src/fern/ip/__init__.py",
    "src/fern/ip/client.py",
    "src/fern/ip/raw_client.py",
    "src/fern/legal_name/__init__.py",
    "src/fern/legal_name/client.py",
    "src/fern/legal_name/raw_client.py",
    "src/fern/limit/__init__.py",
    "src/fern/limit/client.py",
    "src/fern/limit/raw_client.py",
    "src/fern/mastercard_action/__init__.py",
    "src/fern/mastercard_action/client.py",
    "src/fern/mastercard_action/raw_client.py",
    "src/fern/monetary_account/__init__.py",
    "src/fern/monetary_account/client.py",
    "src/fern/monetary_account/raw_client.py",
    "src/fern/monetary_account_bank/__init__.py",
    "src/fern/monetary_account_bank/client.py",
    "src/fern/monetary_account_bank/raw_client.py",
    "src/fern/monetary_account_external/__init__.py",
    "src/fern/monetary_account_external/client.py",
    "src/fern/monetary_account_external/raw_client.py",
    "src/fern/monetary_account_joint/__init__.py",
    "src/fern/monetary_account_joint/client.py",
    "src/fern/monetary_account_joint/raw_client.py",
    "src/fern/monetary_account_savings/__init__.py",
    "src/fern/monetary_account_savings/client.py",
    "src/fern/monetary_account_savings/raw_client.py",
    "src/fern/name/__init__.py",
    "src/fern/name/client.py",
    "src/fern/name/raw_client.py",
    "src/fern/note_attachment/__init__.py",
    "src/fern/note_attachment/client.py",
    "src/fern/note_attachment/raw_client.py",
    "src/fern/note_text/__init__.py",
    "src/fern/note_text/client.py",
    "src/fern/note_text/raw_client.py",
    "src/fern/notification_filter_email/__init__.py",
    "src/fern/notification_filter_email/client.py",
    "src/fern/notification_filter_email/raw_client.py",
    "src/fern/notification_filter_push/__init__.py",
    "src/fern/notification_filter_push/client.py",
    "src/fern/notification_filter_push/raw_client.py",
    "src/fern/notification_filter_url/__init__.py",
    "src/fern/notification_filter_url/client.py",
    "src/fern/notification_filter_url/raw_client.py",
    "src/fern/oauth_client/__init__.py",
    "src/fern/oauth_client/client.py",
    "src/fern/oauth_client/raw_client.py",
    "src/fern/payment/__init__.py",
    "src/fern/payment/client.py",
    "src/fern/payment/raw_client.py",
    "src/fern/payment_auto_allocate/__init__.py",
    "src/fern/payment_auto_allocate/client.py",
    "src/fern/payment_auto_allocate/raw_client.py",
    "src/fern/payment_batch/__init__.py",
    "src/fern/payment_batch/client.py",
    "src/fern/payment_batch/raw_client.py",
    "src/fern/payment_service_provider_credential/__init__.py",
    "src/fern/payment_service_provider_credential/client.py",
    "src/fern/payment_service_provider_credential/raw_client.py",
    "src/fern/payment_service_provider_draft_payment/__init__.py",
    "src/fern/payment_service_provider_draft_payment/client.py",
    "src/fern/payment_service_provider_draft_payment/raw_client.py",
    "src/fern/pdf_content/__init__.py",
    "src/fern/pdf_content/client.py",
    "src/fern/pdf_content/raw_client.py",
    "src/fern/py.typed",
    "src/fern/registry_settlement/__init__.py",
    "src/fern/registry_settlement/client.py",
    "src/fern/registry_settlement/raw_client.py",
    "src/fern/replace/__init__.py",
    "src/fern/replace/client.py",
    "src/fern/replace/raw_client.py",
    "src/fern/request_inquiry/__init__.py",
    "src/fern/request_inquiry/client.py",
    "src/fern/request_inquiry/raw_client.py",
    "src/fern/request_inquiry_batch/__init__.py",
    "src/fern/request_inquiry_batch/client.py",
    "src/fern/request_inquiry_batch/raw_client.py",
    "src/fern/request_response/__init__.py",
    "src/fern/request_response/client.py",
    "src/fern/request_response/raw_client.py",
    "src/fern/reward/__init__.py",
    "src/fern/reward/client.py",
    "src/fern/reward/raw_client.py",
    "src/fern/reward_recipient/__init__.py",
    "src/fern/reward_recipient/client.py",
    "src/fern/reward_recipient/raw_client.py",
    "src/fern/reward_sender/__init__.py",
    "src/fern/reward_sender/client.py",
    "src/fern/reward_sender/raw_client.py",
    "src/fern/sandbox_user_company/__init__.py",
    "src/fern/sandbox_user_company/client.py",
    "src/fern/sandbox_user_company/raw_client.py",
    "src/fern/sandbox_user_person/__init__.py",
    "src/fern/sandbox_user_person/client.py",
    "src/fern/sandbox_user_person/raw_client.py",
    "src/fern/schedule/__init__.py",
    "src/fern/schedule/client.py",
    "src/fern/schedule/raw_client.py",
    "src/fern/schedule_instance/__init__.py",
    "src/fern/schedule_instance/client.py",
    "src/fern/schedule_instance/raw_client.py",
    "src/fern/schedule_payment/__init__.py",
    "src/fern/schedule_payment/client.py",
    "src/fern/schedule_payment/raw_client.py",
    "src/fern/schedule_payment_batch/__init__.py",
    "src/fern/schedule_payment_batch/client.py",
    "src/fern/schedule_payment_batch/raw_client.py",
    "src/fern/server_error/__init__.py",
    "src/fern/server_error/client.py",
    "src/fern/server_error/raw_client.py",
    "src/fern/server_public_key/__init__.py",
    "src/fern/server_public_key/client.py",
    "src/fern/server_public_key/raw_client.py",
    "src/fern/session/__init__.py",
    "src/fern/session/client.py",
    "src/fern/session/raw_client.py",
    "src/fern/session_server/__init__.py",
    "src/fern/session_server/client.py",
    "src/fern/session_server/raw_client.py",
    "src/fern/share_invite_monetary_account_inquiry/__init__.py",
    "src/fern/share_invite_monetary_account_inquiry/client.py",
    "src/fern/share_invite_monetary_account_inquiry/raw_client.py",
    "src/fern/share_invite_monetary_account_response/__init__.py",
    "src/fern/share_invite_monetary_account_response/client.py",
    "src/fern/share_invite_monetary_account_response/raw_client.py",
    "src/fern/sofort_merchant_transaction/__init__.py",
    "src/fern/sofort_merchant_transaction/client.py",
    "src/fern/sofort_merchant_transaction/raw_client.py",
    "src/fern/statement/__init__.py",
    "src/fern/statement/client.py",
    "src/fern/statement/raw_client.py",
    "src/fern/switch_service_payment/__init__.py",
    "src/fern/switch_service_payment/client.py",
    "src/fern/switch_service_payment/raw_client.py",
    "src/fern/token_qr_request_ideal/__init__.py",
    "src/fern/token_qr_request_ideal/client.py",
    "src/fern/token_qr_request_ideal/raw_client.py",
    "src/fern/token_qr_request_sofort/__init__.py",
    "src/fern/token_qr_request_sofort/client.py",
    "src/fern/token_qr_request_sofort/raw_client.py",
    "src/fern/transferwise_currency/__init__.py",
    "src/fern/transferwise_currency/client.py",
    "src/fern/transferwise_currency/raw_client.py",
    "src/fern/transferwise_quote/__init__.py",
    "src/fern/transferwise_quote/client.py",
    "src/fern/transferwise_quote/raw_client.py",
    "src/fern/transferwise_quote_temporary/__init__.py",
    "src/fern/transferwise_quote_temporary/client.py",
    "src/fern/transferwise_quote_temporary/raw_client.py",
    "src/fern/transferwise_recipient/__init__.py",
    "src/fern/transferwise_recipient/client.py",
    "src/fern/transferwise_recipient/raw_client.py",
    "src/fern/transferwise_recipient_requirement/__init__.py",
    "src/fern/transferwise_recipient_requirement/client.py",
    "src/fern/transferwise_recipient_requirement/raw_client.py",
    "src/fern/transferwise_transfer/__init__.py",
    "src/fern/transferwise_transfer/client.py",
    "src/fern/transferwise_transfer/raw_client.py",
    "src/fern/transferwise_transfer_requirement/__init__.py",
    "src/fern/transferwise_transfer_requirement/client.py",
    "src/fern/transferwise_transfer_requirement/raw_client.py",
    "src/fern/transferwise_user/__init__.py",
    "src/fern/transferwise_user/client.py",
    "src/fern/transferwise_user/raw_client.py",
    "src/fern/translink_transaction/__init__.py",
    "src/fern/translink_transaction/client.py",
    "src/fern/translink_transaction/raw_client.py",
    "src/fern/tree_progress/__init__.py",
    "src/fern/tree_progress/client.py",
    "src/fern/tree_progress/raw_client.py",
    "src/fern/types/__init__.py",
    "src/fern/types/additional_information.py",
    "src/fern/types/address.py",
    "src/fern/types/amount.py",
    "src/fern/types/attachment.py",
    "src/fern/types/attachment_conversation_content_listing.py",
    "src/fern/types/attachment_master_card_action_refund.py",
    "src/fern/types/attachment_monetary_account.py",
    "src/fern/types/attachment_monetary_account_content_listing.py",
    "src/fern/types/attachment_monetary_account_create.py",
    "src/fern/types/attachment_monetary_account_payment.py",
    "src/fern/types/attachment_public.py",
    "src/fern/types/attachment_public_content_listing.py",
    "src/fern/types/attachment_public_create.py",
    "src/fern/types/attachment_public_read.py",
    "src/fern/types/attachment_url.py",
    "src/fern/types/attachment_user_content_listing.py",
    "src/fern/types/attachment_user_read.py",
    "src/fern/types/avatar.py",
    "src/fern/types/avatar_create.py",
    "src/fern/types/avatar_read.py",
    "src/fern/types/bad_request_error_body.py",
    "src/fern/types/bank_switch_service_netherlands_incoming.py",
    "src/fern/types/bank_switch_service_netherlands_incoming_payment.py",
    "src/fern/types/bank_switch_service_netherlands_incoming_payment_read.py",
    "src/fern/types/billing_contract_subscription.py",
    "src/fern/types/billing_contract_subscription_listing.py",
    "src/fern/types/birdee_investment_portfolio.py",
    "src/fern/types/birdee_investment_portfolio_balance.py",
    "src/fern/types/birdee_investment_portfolio_goal.py",
    "src/fern/types/birdee_portfolio_allocation.py",
    "src/fern/types/bunq_id.py",
    "src/fern/types/bunq_me_fundraiser_profile.py",
    "src/fern/types/bunq_me_fundraiser_profile_user_listing.py",
    "src/fern/types/bunq_me_fundraiser_profile_user_read.py",
    "src/fern/types/bunq_me_fundraiser_result.py",
    "src/fern/types/bunq_me_fundraiser_result_read.py",
    "src/fern/types/bunq_me_merchant_available.py",
    "src/fern/types/bunq_me_tab.py",
    "src/fern/types/bunq_me_tab_create.py",
    "src/fern/types/bunq_me_tab_entry.py",
    "src/fern/types/bunq_me_tab_listing.py",
    "src/fern/types/bunq_me_tab_read.py",
    "src/fern/types/bunq_me_tab_result_inquiry.py",
    "src/fern/types/bunq_me_tab_result_response.py",
    "src/fern/types/bunq_me_tab_result_response_read.py",
    "src/fern/types/bunq_me_tab_update.py",
    "src/fern/types/card.py",
    "src/fern/types/card_batch_create.py",
    "src/fern/types/card_batch_entry.py",
    "src/fern/types/card_batch_replace_create.py",
    "src/fern/types/card_batch_replace_entry.py",
    "src/fern/types/card_country_permission.py",
    "src/fern/types/card_credit_create.py",
    "src/fern/types/card_debit.py",
    "src/fern/types/card_debit_create.py",
    "src/fern/types/card_generated_cvc2.py",
    "src/fern/types/card_generated_cvc2create.py",
    "src/fern/types/card_generated_cvc2listing.py",
    "src/fern/types/card_generated_cvc2read.py",
    "src/fern/types/card_generated_cvc2update.py",
    "src/fern/types/card_listing.py",
    "src/fern/types/card_name_listing.py",
    "src/fern/types/card_pin_assignment.py",
    "src/fern/types/card_primary_account_number.py",
    "src/fern/types/card_read.py",
    "src/fern/types/card_replace_create.py",
    "src/fern/types/card_update.py",
    "src/fern/types/certificate.py",
    "src/fern/types/certificate_pinned_create.py",
    "src/fern/types/certificate_pinned_delete.py",
    "src/fern/types/certificate_pinned_listing.py",
    "src/fern/types/certificate_pinned_read.py",
    "src/fern/types/co_owner.py",
    "src/fern/types/company.py",
    "src/fern/types/company_create.py",
    "src/fern/types/company_listing.py",
    "src/fern/types/company_read.py",
    "src/fern/types/company_update.py",
    "src/fern/types/company_vat_number.py",
    "src/fern/types/confirmation_of_funds_create.py",
    "src/fern/types/currency_cloud_beneficiary_create.py",
    "src/fern/types/currency_cloud_beneficiary_listing.py",
    "src/fern/types/currency_cloud_beneficiary_read.py",
    "src/fern/types/currency_cloud_beneficiary_requirement_field.py",
    "src/fern/types/currency_cloud_beneficiary_requirement_listing.py",
    "src/fern/types/currency_cloud_payment_quote_create.py",
    "src/fern/types/currency_conversion_listing.py",
    "src/fern/types/currency_conversion_quote.py",
    "src/fern/types/currency_conversion_quote_create.py",
    "src/fern/types/currency_conversion_quote_read.py",
    "src/fern/types/currency_conversion_quote_update.py",
    "src/fern/types/currency_conversion_read.py",
    "src/fern/types/customer.py",
    "src/fern/types/customer_limit.py",
    "src/fern/types/customer_limit_listing.py",
    "src/fern/types/device_listing.py",
    "src/fern/types/device_read.py",
    "src/fern/types/device_server.py",
    "src/fern/types/device_server_create.py",
    "src/fern/types/device_server_listing.py",
    "src/fern/types/device_server_read.py",
    "src/fern/types/draft_payment.py",
    "src/fern/types/draft_payment_anchor_object.py",
    "src/fern/types/draft_payment_create.py",
    "src/fern/types/draft_payment_entry.py",
    "src/fern/types/draft_payment_listing.py",
    "src/fern/types/draft_payment_read.py",
    "src/fern/types/draft_payment_response.py",
    "src/fern/types/draft_payment_update.py",
    "src/fern/types/error.py",
    "src/fern/types/error_item.py",
    "src/fern/types/event_listing.py",
    "src/fern/types/event_object.py",
    "src/fern/types/event_read.py",
    "src/fern/types/export_annual_overview_content_listing.py",
    "src/fern/types/export_annual_overview_create.py",
    "src/fern/types/export_annual_overview_delete.py",
    "src/fern/types/export_annual_overview_listing.py",
    "src/fern/types/export_annual_overview_read.py",
    "src/fern/types/export_rib.py",
    "src/fern/types/export_rib_content_listing.py",
    "src/fern/types/export_rib_create.py",
    "src/fern/types/export_rib_delete.py",
    "src/fern/types/export_rib_listing.py",
    "src/fern/types/export_rib_read.py",
    "src/fern/types/export_statement_card_content_listing.py",
    "src/fern/types/export_statement_card_csv_create.py",
    "src/fern/types/export_statement_card_csv_delete.py",
    "src/fern/types/export_statement_card_csv_listing.py",
    "src/fern/types/export_statement_card_csv_read.py",
    "src/fern/types/export_statement_card_listing.py",
    "src/fern/types/export_statement_card_pdf_create.py",
    "src/fern/types/export_statement_card_pdf_delete.py",
    "src/fern/types/export_statement_card_pdf_listing.py",
    "src/fern/types/export_statement_card_pdf_read.py",
    "src/fern/types/export_statement_card_read.py",
    "src/fern/types/export_statement_content_listing.py",
    "src/fern/types/export_statement_create.py",
    "src/fern/types/export_statement_delete.py",
    "src/fern/types/export_statement_listing.py",
    "src/fern/types/export_statement_payment.py",
    "src/fern/types/export_statement_payment_content_listing.py",
    "src/fern/types/export_statement_payment_create.py",
    "src/fern/types/export_statement_payment_read.py",
    "src/fern/types/export_statement_read.py",
    "src/fern/types/feature_announcement.py",
    "src/fern/types/feature_announcement_read.py",
    "src/fern/types/geolocation.py",
    "src/fern/types/ideal_merchant_transaction.py",
    "src/fern/types/ideal_merchant_transaction_create.py",
    "src/fern/types/ideal_merchant_transaction_listing.py",
    "src/fern/types/ideal_merchant_transaction_read.py",
    "src/fern/types/image.py",
    "src/fern/types/insight_event_listing.py",
    "src/fern/types/insight_listing.py",
    "src/fern/types/insight_preference_date_listing.py",
    "src/fern/types/installation_create.py",
    "src/fern/types/installation_listing.py",
    "src/fern/types/installation_read.py",
    "src/fern/types/installation_server_public_key.py",
    "src/fern/types/installation_server_public_key_listing.py",
    "src/fern/types/installation_token.py",
    "src/fern/types/invoice.py",
    "src/fern/types/invoice_by_user_listing.py",
    "src/fern/types/invoice_by_user_read.py",
    "src/fern/types/invoice_export_pdf_content_listing.py",
    "src/fern/types/invoice_item.py",
    "src/fern/types/invoice_item_group.py",
    "src/fern/types/invoice_listing.py",
    "src/fern/types/invoice_read.py",
    "src/fern/types/issuer.py",
    "src/fern/types/label_card.py",
    "src/fern/types/label_monetary_account.py",
    "src/fern/types/label_user.py",
    "src/fern/types/master_card_action.py",
    "src/fern/types/master_card_action_listing.py",
    "src/fern/types/master_card_action_read.py",
    "src/fern/types/master_card_action_reference.py",
    "src/fern/types/master_card_action_refund.py",
    "src/fern/types/master_card_identity_check_challenge_request_user_read.py",
    "src/fern/types/master_card_identity_check_challenge_request_user_update.py",
    "src/fern/types/master_card_payment_listing.py",
    "src/fern/types/monetary_account_bank.py",
    "src/fern/types/monetary_account_bank_create.py",
    "src/fern/types/monetary_account_bank_listing.py",
    "src/fern/types/monetary_account_bank_read.py",
    "src/fern/types/monetary_account_bank_update.py",
    "src/fern/types/monetary_account_external.py",
    "src/fern/types/monetary_account_external_listing.py",
    "src/fern/types/monetary_account_external_read.py",
    "src/fern/types/monetary_account_investment.py",
    "src/fern/types/monetary_account_joint.py",
    "src/fern/types/monetary_account_joint_create.py",
    "src/fern/types/monetary_account_joint_listing.py",
    "src/fern/types/monetary_account_joint_read.py",
    "src/fern/types/monetary_account_joint_update.py",
    "src/fern/types/monetary_account_light.py",
    "src/fern/types/monetary_account_listing.py",
    "src/fern/types/monetary_account_profile.py",
    "src/fern/types/monetary_account_profile_drain.py",
    "src/fern/types/monetary_account_profile_fill.py",
    "src/fern/types/monetary_account_read.py",
    "src/fern/types/monetary_account_savings.py",
    "src/fern/types/monetary_account_savings_create.py",
    "src/fern/types/monetary_account_savings_listing.py",
    "src/fern/types/monetary_account_savings_read.py",
    "src/fern/types/monetary_account_savings_update.py",
    "src/fern/types/monetary_account_setting.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment_create.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment_delete.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment_listing.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment_read.py",
    "src/fern/types/note_attachment_bank_switch_service_netherlands_incoming_payment_update.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result_create.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result_delete.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result_listing.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result_read.py",
    "src/fern/types/note_attachment_bunq_me_fundraiser_result_update.py",
    "src/fern/types/note_attachment_draft_payment.py",
    "src/fern/types/note_attachment_draft_payment_create.py",
    "src/fern/types/note_attachment_draft_payment_delete.py",
    "src/fern/types/note_attachment_draft_payment_listing.py",
    "src/fern/types/note_attachment_draft_payment_read.py",
    "src/fern/types/note_attachment_draft_payment_update.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction_create.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction_delete.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction_listing.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction_read.py",
    "src/fern/types/note_attachment_ideal_merchant_transaction_update.py",
    "src/fern/types/note_attachment_master_card_action.py",
    "src/fern/types/note_attachment_master_card_action_create.py",
    "src/fern/types/note_attachment_master_card_action_delete.py",
    "src/fern/types/note_attachment_master_card_action_listing.py",
    "src/fern/types/note_attachment_master_card_action_read.py",
    "src/fern/types/note_attachment_master_card_action_update.py",
    "src/fern/types/note_attachment_payment.py",
    "src/fern/types/note_attachment_payment_batch.py",
    "src/fern/types/note_attachment_payment_batch_create.py",
    "src/fern/types/note_attachment_payment_batch_delete.py",
    "src/fern/types/note_attachment_payment_batch_listing.py",
    "src/fern/types/note_attachment_payment_batch_read.py",
    "src/fern/types/note_attachment_payment_batch_update.py",
    "src/fern/types/note_attachment_payment_create.py",
    "src/fern/types/note_attachment_payment_delete.py",
    "src/fern/types/note_attachment_payment_listing.py",
    "src/fern/types/note_attachment_payment_read.py",
    "src/fern/types/note_attachment_payment_update.py",
    "src/fern/types/note_attachment_request_inquiry.py",
    "src/fern/types/note_attachment_request_inquiry_batch.py",
    "src/fern/types/note_attachment_request_inquiry_batch_create.py",
    "src/fern/types/note_attachment_request_inquiry_batch_delete.py",
    "src/fern/types/note_attachment_request_inquiry_batch_listing.py",
    "src/fern/types/note_attachment_request_inquiry_batch_read.py",
    "src/fern/types/note_attachment_request_inquiry_batch_update.py",
    "src/fern/types/note_attachment_request_inquiry_create.py",
    "src/fern/types/note_attachment_request_inquiry_delete.py",
    "src/fern/types/note_attachment_request_inquiry_listing.py",
    "src/fern/types/note_attachment_request_inquiry_read.py",
    "src/fern/types/note_attachment_request_inquiry_update.py",
    "src/fern/types/note_attachment_request_response.py",
    "src/fern/types/note_attachment_request_response_create.py",
    "src/fern/types/note_attachment_request_response_delete.py",
    "src/fern/types/note_attachment_request_response_listing.py",
    "src/fern/types/note_attachment_request_response_read.py",
    "src/fern/types/note_attachment_request_response_update.py",
    "src/fern/types/note_attachment_schedule_instance.py",
    "src/fern/types/note_attachment_schedule_instance_create.py",
    "src/fern/types/note_attachment_schedule_instance_delete.py",
    "src/fern/types/note_attachment_schedule_instance_listing.py",
    "src/fern/types/note_attachment_schedule_instance_read.py",
    "src/fern/types/note_attachment_schedule_instance_update.py",
    "src/fern/types/note_attachment_schedule_payment.py",
    "src/fern/types/note_attachment_schedule_payment_batch.py",
    "src/fern/types/note_attachment_schedule_payment_batch_create.py",
    "src/fern/types/note_attachment_schedule_payment_batch_delete.py",
    "src/fern/types/note_attachment_schedule_payment_batch_listing.py",
    "src/fern/types/note_attachment_schedule_payment_batch_read.py",
    "src/fern/types/note_attachment_schedule_payment_batch_update.py",
    "src/fern/types/note_attachment_schedule_payment_create.py",
    "src/fern/types/note_attachment_schedule_payment_delete.py",
    "src/fern/types/note_attachment_schedule_payment_listing.py",
    "src/fern/types/note_attachment_schedule_payment_read.py",
    "src/fern/types/note_attachment_schedule_payment_update.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction_create.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction_delete.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction_listing.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction_read.py",
    "src/fern/types/note_attachment_sofort_merchant_transaction_update.py",
    "src/fern/types/note_attachment_whitelist_result.py",
    "src/fern/types/note_attachment_whitelist_result_create.py",
    "src/fern/types/note_attachment_whitelist_result_delete.py",
    "src/fern/types/note_attachment_whitelist_result_listing.py",
    "src/fern/types/note_attachment_whitelist_result_read.py",
    "src/fern/types/note_attachment_whitelist_result_update.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment_create.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment_delete.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment_listing.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment_read.py",
    "src/fern/types/note_text_bank_switch_service_netherlands_incoming_payment_update.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result_create.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result_delete.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result_listing.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result_read.py",
    "src/fern/types/note_text_bunq_me_fundraiser_result_update.py",
    "src/fern/types/note_text_draft_payment.py",
    "src/fern/types/note_text_draft_payment_create.py",
    "src/fern/types/note_text_draft_payment_delete.py",
    "src/fern/types/note_text_draft_payment_listing.py",
    "src/fern/types/note_text_draft_payment_read.py",
    "src/fern/types/note_text_draft_payment_update.py",
    "src/fern/types/note_text_ideal_merchant_transaction.py",
    "src/fern/types/note_text_ideal_merchant_transaction_create.py",
    "src/fern/types/note_text_ideal_merchant_transaction_delete.py",
    "src/fern/types/note_text_ideal_merchant_transaction_listing.py",
    "src/fern/types/note_text_ideal_merchant_transaction_read.py",
    "src/fern/types/note_text_ideal_merchant_transaction_update.py",
    "src/fern/types/note_text_master_card_action.py",
    "src/fern/types/note_text_master_card_action_create.py",
    "src/fern/types/note_text_master_card_action_delete.py",
    "src/fern/types/note_text_master_card_action_listing.py",
    "src/fern/types/note_text_master_card_action_read.py",
    "src/fern/types/note_text_master_card_action_update.py",
    "src/fern/types/note_text_payment.py",
    "src/fern/types/note_text_payment_batch.py",
    "src/fern/types/note_text_payment_batch_create.py",
    "src/fern/types/note_text_payment_batch_delete.py",
    "src/fern/types/note_text_payment_batch_listing.py",
    "src/fern/types/note_text_payment_batch_read.py",
    "src/fern/types/note_text_payment_batch_update.py",
    "src/fern/types/note_text_payment_create.py",
    "src/fern/types/note_text_payment_delete.py",
    "src/fern/types/note_text_payment_listing.py",
    "src/fern/types/note_text_payment_read.py",
    "src/fern/types/note_text_payment_update.py",
    "src/fern/types/note_text_request_inquiry.py",
    "src/fern/types/note_text_request_inquiry_batch.py",
    "src/fern/types/note_text_request_inquiry_batch_create.py",
    "src/fern/types/note_text_request_inquiry_batch_delete.py",
    "src/fern/types/note_text_request_inquiry_batch_listing.py",
    "src/fern/types/note_text_request_inquiry_batch_read.py",
    "src/fern/types/note_text_request_inquiry_batch_update.py",
    "src/fern/types/note_text_request_inquiry_create.py",
    "src/fern/types/note_text_request_inquiry_delete.py",
    "src/fern/types/note_text_request_inquiry_listing.py",
    "src/fern/types/note_text_request_inquiry_read.py",
    "src/fern/types/note_text_request_inquiry_update.py",
    "src/fern/types/note_text_request_response.py",
    "src/fern/types/note_text_request_response_create.py",
    "src/fern/types/note_text_request_response_delete.py",
    "src/fern/types/note_text_request_response_listing.py",
    "src/fern/types/note_text_request_response_read.py",
    "src/fern/types/note_text_request_response_update.py",
    "src/fern/types/note_text_schedule_instance.py",
    "src/fern/types/note_text_schedule_instance_create.py",
    "src/fern/types/note_text_schedule_instance_delete.py",
    "src/fern/types/note_text_schedule_instance_listing.py",
    "src/fern/types/note_text_schedule_instance_read.py",
    "src/fern/types/note_text_schedule_instance_update.py",
    "src/fern/types/note_text_schedule_payment.py",
    "src/fern/types/note_text_schedule_payment_batch.py",
    "src/fern/types/note_text_schedule_payment_batch_create.py",
    "src/fern/types/note_text_schedule_payment_batch_delete.py",
    "src/fern/types/note_text_schedule_payment_batch_listing.py",
    "src/fern/types/note_text_schedule_payment_batch_read.py",
    "src/fern/types/note_text_schedule_payment_batch_update.py",
    "src/fern/types/note_text_schedule_payment_create.py",
    "src/fern/types/note_text_schedule_payment_delete.py",
    "src/fern/types/note_text_schedule_payment_listing.py",
    "src/fern/types/note_text_schedule_payment_read.py",
    "src/fern/types/note_text_schedule_payment_update.py",
    "src/fern/types/note_text_sofort_merchant_transaction.py",
    "src/fern/types/note_text_sofort_merchant_transaction_create.py",
    "src/fern/types/note_text_sofort_merchant_transaction_delete.py",
    "src/fern/types/note_text_sofort_merchant_transaction_listing.py",
    "src/fern/types/note_text_sofort_merchant_transaction_read.py",
    "src/fern/types/note_text_sofort_merchant_transaction_update.py",
    "src/fern/types/note_text_whitelist_result.py",
    "src/fern/types/note_text_whitelist_result_create.py",
    "src/fern/types/note_text_whitelist_result_delete.py",
    "src/fern/types/note_text_whitelist_result_listing.py",
    "src/fern/types/note_text_whitelist_result_read.py",
    "src/fern/types/note_text_whitelist_result_update.py",
    "src/fern/types/notification_filter.py",
    "src/fern/types/notification_filter_email.py",
    "src/fern/types/notification_filter_email_create.py",
    "src/fern/types/notification_filter_email_listing.py",
    "src/fern/types/notification_filter_push.py",
    "src/fern/types/notification_filter_push_create.py",
    "src/fern/types/notification_filter_push_listing.py",
    "src/fern/types/notification_filter_url.py",
    "src/fern/types/notification_filter_url_create.py",
    "src/fern/types/notification_filter_url_listing.py",
    "src/fern/types/notification_filter_url_monetary_account_create.py",
    "src/fern/types/notification_filter_url_monetary_account_listing.py",
    "src/fern/types/oauth_callback_url.py",
    "src/fern/types/oauth_callback_url_create.py",
    "src/fern/types/oauth_callback_url_delete.py",
    "src/fern/types/oauth_callback_url_listing.py",
    "src/fern/types/oauth_callback_url_read.py",
    "src/fern/types/oauth_callback_url_update.py",
    "src/fern/types/oauth_client.py",
    "src/fern/types/oauth_client_create.py",
    "src/fern/types/oauth_client_listing.py",
    "src/fern/types/oauth_client_read.py",
    "src/fern/types/oauth_client_update.py",
    "src/fern/types/payment.py",
    "src/fern/types/payment_auto_allocate.py",
    "src/fern/types/payment_auto_allocate_create.py",
    "src/fern/types/payment_auto_allocate_definition.py",
    "src/fern/types/payment_auto_allocate_definition_listing.py",
    "src/fern/types/payment_auto_allocate_delete.py",
    "src/fern/types/payment_auto_allocate_instance.py",
    "src/fern/types/payment_auto_allocate_instance_listing.py",
    "src/fern/types/payment_auto_allocate_instance_read.py",
    "src/fern/types/payment_auto_allocate_listing.py",
    "src/fern/types/payment_auto_allocate_read.py",
    "src/fern/types/payment_auto_allocate_update.py",
    "src/fern/types/payment_auto_allocate_user_listing.py",
    "src/fern/types/payment_batch.py",
    "src/fern/types/payment_batch_anchored_payment.py",
    "src/fern/types/payment_batch_create.py",
    "src/fern/types/payment_batch_listing.py",
    "src/fern/types/payment_batch_read.py",
    "src/fern/types/payment_batch_update.py",
    "src/fern/types/payment_create.py",
    "src/fern/types/payment_listing.py",
    "src/fern/types/payment_read.py",
    "src/fern/types/payment_service_provider_credential_create.py",
    "src/fern/types/payment_service_provider_credential_read.py",
    "src/fern/types/payment_service_provider_draft_payment.py",
    "src/fern/types/payment_service_provider_draft_payment_create.py",
    "src/fern/types/payment_service_provider_draft_payment_listing.py",
    "src/fern/types/payment_service_provider_draft_payment_read.py",
    "src/fern/types/payment_service_provider_draft_payment_update.py",
    "src/fern/types/permitted_device.py",
    "src/fern/types/permitted_ip.py",
    "src/fern/types/permitted_ip_create.py",
    "src/fern/types/permitted_ip_listing.py",
    "src/fern/types/permitted_ip_read.py",
    "src/fern/types/permitted_ip_update.py",
    "src/fern/types/place_photo_lookup_content_listing.py",
    "src/fern/types/pointer.py",
    "src/fern/types/registry_membership.py",
    "src/fern/types/registry_settlement.py",
    "src/fern/types/registry_settlement_create.py",
    "src/fern/types/registry_settlement_item.py",
    "src/fern/types/registry_settlement_listing.py",
    "src/fern/types/registry_settlement_read.py",
    "src/fern/types/relation_user.py",
    "src/fern/types/request_inquiry.py",
    "src/fern/types/request_inquiry_batch.py",
    "src/fern/types/request_inquiry_batch_create.py",
    "src/fern/types/request_inquiry_batch_listing.py",
    "src/fern/types/request_inquiry_batch_read.py",
    "src/fern/types/request_inquiry_batch_update.py",
    "src/fern/types/request_inquiry_create.py",
    "src/fern/types/request_inquiry_listing.py",
    "src/fern/types/request_inquiry_read.py",
    "src/fern/types/request_inquiry_reference.py",
    "src/fern/types/request_inquiry_update.py",
    "src/fern/types/request_reference_split_the_bill_anchor_object.py",
    "src/fern/types/request_response.py",
    "src/fern/types/request_response_listing.py",
    "src/fern/types/request_response_read.py",
    "src/fern/types/request_response_update.py",
    "src/fern/types/reward_listing.py",
    "src/fern/types/reward_read.py",
    "src/fern/types/reward_recipient.py",
    "src/fern/types/reward_recipient_listing.py",
    "src/fern/types/reward_recipient_read.py",
    "src/fern/types/reward_sender.py",
    "src/fern/types/reward_sender_listing.py",
    "src/fern/types/reward_sender_read.py",
    "src/fern/types/sandbox_user_company.py",
    "src/fern/types/sandbox_user_company_create.py",
    "src/fern/types/sandbox_user_person.py",
    "src/fern/types/sandbox_user_person_create.py",
    "src/fern/types/schedule.py",
    "src/fern/types/schedule_anchor_object.py",
    "src/fern/types/schedule_instance.py",
    "src/fern/types/schedule_instance_anchor_object.py",
    "src/fern/types/schedule_instance_listing.py",
    "src/fern/types/schedule_instance_read.py",
    "src/fern/types/schedule_instance_update.py",
    "src/fern/types/schedule_listing.py",
    "src/fern/types/schedule_payment.py",
    "src/fern/types/schedule_payment_batch.py",
    "src/fern/types/schedule_payment_batch_create.py",
    "src/fern/types/schedule_payment_batch_delete.py",
    "src/fern/types/schedule_payment_batch_read.py",
    "src/fern/types/schedule_payment_batch_update.py",
    "src/fern/types/schedule_payment_create.py",
    "src/fern/types/schedule_payment_delete.py",
    "src/fern/types/schedule_payment_entry.py",
    "src/fern/types/schedule_payment_listing.py",
    "src/fern/types/schedule_payment_read.py",
    "src/fern/types/schedule_payment_update.py",
    "src/fern/types/schedule_read.py",
    "src/fern/types/schedule_user_listing.py",
    "src/fern/types/server_error.py",
    "src/fern/types/server_error_create.py",
    "src/fern/types/session_delete.py",
    "src/fern/types/session_server_create.py",
    "src/fern/types/session_server_token.py",
    "src/fern/types/share_detail.py",
    "src/fern/types/share_detail_draft_payment.py",
    "src/fern/types/share_detail_payment.py",
    "src/fern/types/share_detail_read_only.py",
    "src/fern/types/share_invite_monetary_account_inquiry.py",
    "src/fern/types/share_invite_monetary_account_inquiry_create.py",
    "src/fern/types/share_invite_monetary_account_inquiry_listing.py",
    "src/fern/types/share_invite_monetary_account_inquiry_read.py",
    "src/fern/types/share_invite_monetary_account_inquiry_update.py",
    "src/fern/types/share_invite_monetary_account_response.py",
    "src/fern/types/share_invite_monetary_account_response_listing.py",
    "src/fern/types/share_invite_monetary_account_response_read.py",
    "src/fern/types/share_invite_monetary_account_response_update.py",
    "src/fern/types/sofort_merchant_transaction.py",
    "src/fern/types/sofort_merchant_transaction_listing.py",
    "src/fern/types/sofort_merchant_transaction_read.py",
    "src/fern/types/tax_resident.py",
    "src/fern/types/token_qr_request_ideal_create.py",
    "src/fern/types/token_qr_request_sofort_create.py",
    "src/fern/types/transferwise_account_quote_create.py",
    "src/fern/types/transferwise_account_quote_delete.py",
    "src/fern/types/transferwise_account_quote_listing.py",
    "src/fern/types/transferwise_account_quote_read.py",
    "src/fern/types/transferwise_account_requirement_create.py",
    "src/fern/types/transferwise_account_requirement_listing.py",
    "src/fern/types/transferwise_currency_listing.py",
    "src/fern/types/transferwise_quote.py",
    "src/fern/types/transferwise_quote_create.py",
    "src/fern/types/transferwise_quote_read.py",
    "src/fern/types/transferwise_quote_temporary_create.py",
    "src/fern/types/transferwise_quote_temporary_read.py",
    "src/fern/types/transferwise_requirement_field.py",
    "src/fern/types/transferwise_requirement_field_group.py",
    "src/fern/types/transferwise_requirement_field_group_validation_async.py",
    "src/fern/types/transferwise_requirement_field_group_validation_async_params.py",
    "src/fern/types/transferwise_requirement_field_group_values_allowed.py",
    "src/fern/types/transferwise_transfer.py",
    "src/fern/types/transferwise_transfer_create.py",
    "src/fern/types/transferwise_transfer_listing.py",
    "src/fern/types/transferwise_transfer_read.py",
    "src/fern/types/transferwise_transfer_requirement_create.py",
    "src/fern/types/transferwise_user_create.py",
    "src/fern/types/transferwise_user_listing.py",
    "src/fern/types/translink_transaction_create.py",
    "src/fern/types/translink_transaction_entry.py",
    "src/fern/types/translink_transaction_listing.py",
    "src/fern/types/translink_transaction_read.py",
    "src/fern/types/tree_progress_listing.py",
    "src/fern/types/ubo.py",
    "src/fern/types/user_api_key.py",
    "src/fern/types/user_api_key_anchored_user.py",
    "src/fern/types/user_company.py",
    "src/fern/types/user_company_name_listing.py",
    "src/fern/types/user_company_read.py",
    "src/fern/types/user_company_update.py",
    "src/fern/types/user_credential_password_ip_listing.py",
    "src/fern/types/user_credential_password_ip_read.py",
    "src/fern/types/user_legal_name_listing.py",
    "src/fern/types/user_listing.py",
    "src/fern/types/user_payment_service_provider.py",
    "src/fern/types/user_payment_service_provider_read.py",
    "src/fern/types/user_person.py",
    "src/fern/types/user_person_read.py",
    "src/fern/types/user_person_update.py",
    "src/fern/types/user_read.py",
    "src/fern/types/whitelist.py",
    "src/fern/types/whitelist_result.py",
    "src/fern/types/whitelist_result_view_anchored_object.py",
    "src/fern/types/whitelist_sdd_listing.py",
    "src/fern/types/whitelist_sdd_monetary_account_paying_listing.py",
    "src/fern/types/whitelist_sdd_monetary_account_paying_read.py",
    "src/fern/types/whitelist_sdd_one_off.py",
    "src/fern/types/whitelist_sdd_one_off_create.py",
    "src/fern/types/whitelist_sdd_one_off_delete.py",
    "src/fern/types/whitelist_sdd_one_off_listing.py",
    "src/fern/types/whitelist_sdd_one_off_read.py",
    "src/fern/types/whitelist_sdd_one_off_update.py",
    "src/fern/types/whitelist_sdd_read.py",
    "src/fern/types/whitelist_sdd_recurring.py",
    "src/fern/types/whitelist_sdd_recurring_create.py",
    "src/fern/types/whitelist_sdd_recurring_delete.py",
    "src/fern/types/whitelist_sdd_recurring_listing.py",
    "src/fern/types/whitelist_sdd_recurring_read.py",
    "src/fern/types/whitelist_sdd_recurring_update.py",
    "src/fern/user/__init__.py",
    "src/fern/user/client.py",
    "src/fern/user/raw_client.py",
    "src/fern/user_company/__init__.py",
    "src/fern/user_company/client.py",
    "src/fern/user_company/raw_client.py",
    "src/fern/user_payment_service_provider/__init__.py",
    "src/fern/user_payment_service_provider/client.py",
    "src/fern/user_payment_service_provider/raw_client.py",
    "src/fern/user_person/__init__.py",
    "src/fern/user_person/client.py",
    "src/fern/user_person/raw_client.py",
    "src/fern/version.py",
    "src/fern/whitelist_sdd/__init__.py",
    "src/fern/whitelist_sdd/client.py",
    "src/fern/whitelist_sdd/raw_client.py",
    "src/fern/whitelist_sdd_one_off/__init__.py",
    "src/fern/whitelist_sdd_one_off/client.py",
    "src/fern/whitelist_sdd_one_off/raw_client.py",
    "src/fern/whitelist_sdd_recurring/__init__.py",
    "src/fern/whitelist_sdd_recurring/client.py",
    "src/fern/whitelist_sdd_recurring/raw_client.py",
];

/// `bunq.com`: a large real-world `link-ok` corpus API (issue #77) — 421 endpoints
/// across 118 sub-clients (~10× apideck), the pipeline's at-scale stress target. Its
/// OpenAPI spec is fetched, not vendored (`corpus_spec`); its full Fern golden is
/// committed. crozier reproduces the files in [`BUNQ.matched`] byte-for-byte; the
/// structural remainder (types Fern splits that crozier lays out differently) is the
/// documented gap to full byte-match — see docs/matching.md.
const BUNQ: Corpus = Corpus {
    api: "bunq.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    // Grown by `just fixtures-candidates`; see docs/matching.md for the open gap.
    matched: BUNQ_MATCHED,
};

/// Files crozier reproduces byte-for-byte for `bungie.net`. Grown mechanically by
/// `just fixtures-candidates`; keep entries reporter-approved, not hand-curated.
const BUNGIE_MATCHED: &[&str] = &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/app/__init__.py",
        "src/fern/app/client.py",
        "src/fern/app/raw_client.py",
        "src/fern/app/types/__init__.py",
        "src/fern/app/types/app_get_application_api_usage_response.py",
        "src/fern/app/types/app_get_bungie_applications_response.py",
        "src/fern/client.py",
        "src/fern/communitycontent/__init__.py",
        "src/fern/communitycontent/client.py",
        "src/fern/communitycontent/raw_client.py",
        "src/fern/communitycontent/types/__init__.py",
        "src/fern/communitycontent/types/community_content_get_community_content_response.py",
        "src/fern/content/__init__.py",
        "src/fern/content/client.py",
        "src/fern/content/raw_client.py",
        "src/fern/content/types/__init__.py",
        "src/fern/content/types/content_get_content_by_id_response.py",
        "src/fern/content/types/content_get_content_by_tag_and_type_response.py",
        "src/fern/content/types/content_get_content_type_response.py",
        "src/fern/content/types/content_rss_news_articles_response.py",
        "src/fern/content/types/content_search_content_by_tag_and_type_response.py",
        "src/fern/content/types/content_search_content_with_text_response.py",
        "src/fern/content/types/content_search_help_articles_response.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/destiny2/__init__.py",
        "src/fern/destiny2/client.py",
        "src/fern/destiny2/raw_client.py",
        "src/fern/destiny2/types/__init__.py",
        "src/fern/destiny2/types/destiny2awa_get_action_token_response.py",
        "src/fern/destiny2/types/destiny2awa_initialize_request_response.py",
        "src/fern/destiny2/types/destiny2awa_provide_authorization_result_response.py",
        "src/fern/destiny2/types/destiny2clear_loadout_response.py",
        "src/fern/destiny2/types/destiny2equip_item_response.py",
        "src/fern/destiny2/types/destiny2equip_items_response.py",
        "src/fern/destiny2/types/destiny2equip_loadout_response.py",
        "src/fern/destiny2/types/destiny2get_activity_history_response.py",
        "src/fern/destiny2/types/destiny2get_character_response.py",
        "src/fern/destiny2/types/destiny2get_clan_aggregate_stats_response.py",
        "src/fern/destiny2/types/destiny2get_clan_banner_source_response.py",
        "src/fern/destiny2/types/destiny2get_clan_leaderboards_response.py",
        "src/fern/destiny2/types/destiny2get_clan_weekly_reward_state_response.py",
        "src/fern/destiny2/types/destiny2get_collectible_node_details_response.py",
        "src/fern/destiny2/types/destiny2get_destiny_aggregate_activity_stats_response.py",
        "src/fern/destiny2/types/destiny2get_destiny_entity_definition_response.py",
        "src/fern/destiny2/types/destiny2get_destiny_manifest_response.py",
        "src/fern/destiny2/types/destiny2get_historical_stats_definition_response.py",
        "src/fern/destiny2/types/destiny2get_historical_stats_for_account_response.py",
        "src/fern/destiny2/types/destiny2get_historical_stats_response.py",
        "src/fern/destiny2/types/destiny2get_item_response.py",
        "src/fern/destiny2/types/destiny2get_leaderboards_for_character_response.py",
        "src/fern/destiny2/types/destiny2get_leaderboards_response.py",
        "src/fern/destiny2/types/destiny2get_linked_profiles_response.py",
        "src/fern/destiny2/types/destiny2get_post_game_carnage_report_response.py",
        "src/fern/destiny2/types/destiny2get_profile_response.py",
        "src/fern/destiny2/types/destiny2get_public_milestone_content_response.py",
        "src/fern/destiny2/types/destiny2get_public_milestones_response.py",
        "src/fern/destiny2/types/destiny2get_public_vendors_response.py",
        "src/fern/destiny2/types/destiny2get_unique_weapon_history_response.py",
        "src/fern/destiny2/types/destiny2get_vendor_response.py",
        "src/fern/destiny2/types/destiny2get_vendors_response.py",
        "src/fern/destiny2/types/destiny2insert_socket_plug_free_response.py",
        "src/fern/destiny2/types/destiny2insert_socket_plug_response.py",
        "src/fern/destiny2/types/destiny2pull_from_postmaster_response.py",
        "src/fern/destiny2/types/destiny2report_offensive_post_game_carnage_report_player_response.py",
        "src/fern/destiny2/types/destiny2search_destiny_entities_response.py",
        "src/fern/destiny2/types/destiny2search_destiny_player_by_bungie_name_response.py",
        "src/fern/destiny2/types/destiny2set_item_lock_state_response.py",
        "src/fern/destiny2/types/destiny2set_quest_tracked_state_response.py",
        "src/fern/destiny2/types/destiny2snapshot_loadout_response.py",
        "src/fern/destiny2/types/destiny2transfer_item_response.py",
        "src/fern/destiny2/types/destiny2update_loadout_identifiers_response.py",
        "src/fern/environment.py",
        "src/fern/fireteam/__init__.py",
        "src/fern/fireteam/client.py",
        "src/fern/fireteam/raw_client.py",
        "src/fern/fireteam/types/__init__.py",
        "src/fern/fireteam/types/fireteam_get_active_private_clan_fireteam_count_response.py",
        "src/fern/fireteam/types/fireteam_get_available_clan_fireteams_response.py",
        "src/fern/fireteam/types/fireteam_get_clan_fireteam_response.py",
        "src/fern/fireteam/types/fireteam_get_my_clan_fireteams_response.py",
        "src/fern/fireteam/types/fireteam_search_public_available_clan_fireteams_response.py",
        "src/fern/forum/__init__.py",
        "src/fern/forum/client.py",
        "src/fern/forum/raw_client.py",
        "src/fern/forum/types/__init__.py",
        "src/fern/forum/types/forum_get_core_topics_paged_response.py",
        "src/fern/forum/types/forum_get_forum_tag_suggestions_response.py",
        "src/fern/forum/types/forum_get_poll_response.py",
        "src/fern/forum/types/forum_get_post_and_parent_awaiting_approval_response.py",
        "src/fern/forum/types/forum_get_post_and_parent_response.py",
        "src/fern/forum/types/forum_get_posts_threaded_paged_from_child_response.py",
        "src/fern/forum/types/forum_get_posts_threaded_paged_response.py",
        "src/fern/forum/types/forum_get_recruitment_thread_summaries_response.py",
        "src/fern/forum/types/forum_get_topic_for_content_response.py",
        "src/fern/forum/types/forum_get_topics_paged_response.py",
        "src/fern/groupv2/__init__.py",
        "src/fern/groupv2/client.py",
        "src/fern/groupv2/raw_client.py",
        "src/fern/groupv2/types/__init__.py",
        "src/fern/groupv2/types/group_v2abdicate_foundership_response.py",
        "src/fern/groupv2/types/group_v2add_optional_conversation_response.py",
        "src/fern/groupv2/types/group_v2approve_all_pending_response.py",
        "src/fern/groupv2/types/group_v2approve_pending_for_list_response.py",
        "src/fern/groupv2/types/group_v2approve_pending_response.py",
        "src/fern/groupv2/types/group_v2ban_member_response.py",
        "src/fern/groupv2/types/group_v2deny_all_pending_response.py",
        "src/fern/groupv2/types/group_v2deny_pending_for_list_response.py",
        "src/fern/groupv2/types/group_v2edit_clan_banner_response.py",
        "src/fern/groupv2/types/group_v2edit_founder_options_response.py",
        "src/fern/groupv2/types/group_v2edit_group_membership_response.py",
        "src/fern/groupv2/types/group_v2edit_group_response.py",
        "src/fern/groupv2/types/group_v2edit_optional_conversation_response.py",
        "src/fern/groupv2/types/group_v2get_admins_and_founder_of_group_response.py",
        "src/fern/groupv2/types/group_v2get_available_avatars_response.py",
        "src/fern/groupv2/types/group_v2get_available_themes_response.py",
        "src/fern/groupv2/types/group_v2get_banned_members_of_group_response.py",
        "src/fern/groupv2/types/group_v2get_group_by_name_response.py",
        "src/fern/groupv2/types/group_v2get_group_by_name_v2response.py",
        "src/fern/groupv2/types/group_v2get_group_optional_conversations_response.py",
        "src/fern/groupv2/types/group_v2get_group_response.py",
        "src/fern/groupv2/types/group_v2get_groups_for_member_response.py",
        "src/fern/groupv2/types/group_v2get_invited_individuals_response.py",
        "src/fern/groupv2/types/group_v2get_members_of_group_response.py",
        "src/fern/groupv2/types/group_v2get_pending_memberships_response.py",
        "src/fern/groupv2/types/group_v2get_potential_groups_for_member_response.py",
        "src/fern/groupv2/types/group_v2get_recommended_groups_response.py",
        "src/fern/groupv2/types/group_v2get_user_clan_invite_setting_response.py",
        "src/fern/groupv2/types/group_v2group_search_response.py",
        "src/fern/groupv2/types/group_v2individual_group_invite_cancel_response.py",
        "src/fern/groupv2/types/group_v2individual_group_invite_response.py",
        "src/fern/groupv2/types/group_v2kick_member_response.py",
        "src/fern/groupv2/types/group_v2recover_group_for_founder_response.py",
        "src/fern/groupv2/types/group_v2unban_member_response.py",
        "src/fern/py.typed",
        "src/fern/social/__init__.py",
        "src/fern/social/client.py",
        "src/fern/social/raw_client.py",
        "src/fern/social/types/__init__.py",
        "src/fern/social/types/social_accept_friend_request_response.py",
        "src/fern/social/types/social_decline_friend_request_response.py",
        "src/fern/social/types/social_get_friend_list_response.py",
        "src/fern/social/types/social_get_friend_request_list_response.py",
        "src/fern/social/types/social_get_platform_friend_list_response.py",
        "src/fern/social/types/social_issue_friend_request_response.py",
        "src/fern/social/types/social_remove_friend_request_response.py",
        "src/fern/social/types/social_remove_friend_response.py",
        "src/fern/tokens/__init__.py",
        "src/fern/tokens/client.py",
        "src/fern/tokens/raw_client.py",
        "src/fern/tokens/types/__init__.py",
        "src/fern/tokens/types/tokens_apply_missing_partner_offers_without_claim_response.py",
        "src/fern/tokens/types/tokens_claim_partner_offer_response.py",
        "src/fern/tokens/types/tokens_force_drops_repair_response.py",
        "src/fern/tokens/types/tokens_get_bungie_rewards_for_platform_user_response.py",
        "src/fern/tokens/types/tokens_get_bungie_rewards_for_user_response.py",
        "src/fern/tokens/types/tokens_get_bungie_rewards_list_response.py",
        "src/fern/tokens/types/tokens_get_partner_offer_sku_history_response.py",
        "src/fern/tokens/types/tokens_get_partner_reward_history_response.py",
        "src/fern/trending/__init__.py",
        "src/fern/trending/client.py",
        "src/fern/trending/raw_client.py",
        "src/fern/trending/types/__init__.py",
        "src/fern/trending/types/trending_get_trending_categories_response.py",
        "src/fern/trending/types/trending_get_trending_category_response.py",
        "src/fern/trending/types/trending_get_trending_entry_detail_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/applications_api_usage.py",
        "src/fern/types/applications_application.py",
        "src/fern/types/applications_application_developer.py",
        "src/fern/types/applications_application_scopes.py",
        "src/fern/types/applications_application_status.py",
        "src/fern/types/applications_datapoint.py",
        "src/fern/types/applications_developer_role.py",
        "src/fern/types/applications_series.py",
        "src/fern/types/bungie_credential_type.py",
        "src/fern/types/bungie_membership_type.py",
        "src/fern/types/bungie_membership_type_array.py",
        "src/fern/types/common_models_core_setting.py",
        "src/fern/types/common_models_core_settings_configuration.py",
        "src/fern/types/common_models_core_system.py",
        "src/fern/types/common_models_destiny2core_settings.py",
        "src/fern/types/components_component_privacy_setting.py",
        "src/fern/types/components_component_response.py",
        "src/fern/types/config_clan_banner_clan_banner_decal.py",
        "src/fern/types/config_clan_banner_clan_banner_source.py",
        "src/fern/types/config_group_theme.py",
        "src/fern/types/config_user_theme.py",
        "src/fern/types/content_comment_summary.py",
        "src/fern/types/content_content_item_public_contract.py",
        "src/fern/types/content_content_representation.py",
        "src/fern/types/content_models_content_preview.py",
        "src/fern/types/content_models_content_property_data_type_enum.py",
        "src/fern/types/content_models_content_type_default_value.py",
        "src/fern/types/content_models_content_type_description.py",
        "src/fern/types/content_models_content_type_property.py",
        "src/fern/types/content_models_content_type_property_section.py",
        "src/fern/types/content_models_tag_metadata_definition.py",
        "src/fern/types/content_models_tag_metadata_item.py",
        "src/fern/types/content_news_article_rss_item.py",
        "src/fern/types/content_news_article_rss_response.py",
        "src/fern/types/dates_date_range.py",
        "src/fern/types/destiny_activities_destiny_public_activity_status.py",
        "src/fern/types/destiny_activity_graph_node_highlight_type.py",
        "src/fern/types/destiny_advanced_awa_authorization_result.py",
        "src/fern/types/destiny_advanced_awa_initialize_response.py",
        "src/fern/types/destiny_advanced_awa_permission_requested.py",
        "src/fern/types/destiny_advanced_awa_response_reason.py",
        "src/fern/types/destiny_advanced_awa_type.py",
        "src/fern/types/destiny_advanced_awa_user_response.py",
        "src/fern/types/destiny_advanced_awa_user_selection.py",
        "src/fern/types/destiny_artifacts_destiny_artifact_character_scoped.py",
        "src/fern/types/destiny_artifacts_destiny_artifact_profile_scoped.py",
        "src/fern/types/destiny_artifacts_destiny_artifact_tier.py",
        "src/fern/types/destiny_artifacts_destiny_artifact_tier_item.py",
        "src/fern/types/destiny_base_item_component_set_ofint32.py",
        "src/fern/types/destiny_base_item_component_set_ofint64.py",
        "src/fern/types/destiny_base_item_component_set_ofuint32.py",
        "src/fern/types/destiny_bucket_category.py",
        "src/fern/types/destiny_bucket_scope.py",
        "src/fern/types/destiny_challenges_destiny_challenge_status.py",
        "src/fern/types/destiny_character_destiny_character_customization.py",
        "src/fern/types/destiny_character_destiny_character_peer_view.py",
        "src/fern/types/destiny_character_destiny_item_peer_view.py",
        "src/fern/types/destiny_components_collectibles_destiny_collectible_component.py",
        "src/fern/types/destiny_components_collectibles_destiny_collectibles_component.py",
        "src/fern/types/destiny_components_collectibles_destiny_profile_collectibles_component.py",
        "src/fern/types/destiny_components_craftables_destiny_craftable_component.py",
        "src/fern/types/destiny_components_craftables_destiny_craftable_socket_component.py",
        "src/fern/types/destiny_components_craftables_destiny_craftable_socket_plug_component.py",
        "src/fern/types/destiny_components_craftables_destiny_craftables_component.py",
        "src/fern/types/destiny_components_inventory_destiny_currencies_component.py",
        "src/fern/types/destiny_components_inventory_destiny_platform_silver_component.py",
        "src/fern/types/destiny_components_items_destiny_item_plug_component.py",
        "src/fern/types/destiny_components_items_destiny_item_plug_objectives_component.py",
        "src/fern/types/destiny_components_items_destiny_item_reusable_plugs_component.py",
        "src/fern/types/destiny_components_kiosks_destiny_kiosk_item.py",
        "src/fern/types/destiny_components_kiosks_destiny_kiosks_component.py",
        "src/fern/types/destiny_components_loadouts_destiny_loadout_component.py",
        "src/fern/types/destiny_components_loadouts_destiny_loadout_item_component.py",
        "src/fern/types/destiny_components_loadouts_destiny_loadouts_component.py",
        "src/fern/types/destiny_components_metrics_destiny_metric_component.py",
        "src/fern/types/destiny_components_metrics_destiny_metrics_component.py",
        "src/fern/types/destiny_components_plug_sets_destiny_plug_sets_component.py",
        "src/fern/types/destiny_components_presentation_destiny_presentation_node_component.py",
        "src/fern/types/destiny_components_presentation_destiny_presentation_nodes_component.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_progression_component.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_transitory_component.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_transitory_current_activity.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_transitory_joinability.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_transitory_party_member.py",
        "src/fern/types/destiny_components_profiles_destiny_profile_transitory_tracking_entry.py",
        "src/fern/types/destiny_components_records_destiny_character_records_component.py",
        "src/fern/types/destiny_components_records_destiny_profile_records_component.py",
        "src/fern/types/destiny_components_records_destiny_record_component.py",
        "src/fern/types/destiny_components_records_destiny_records_component.py",
        "src/fern/types/destiny_components_social_destiny_social_commendations_component.py",
        "src/fern/types/destiny_components_string_variables_destiny_string_variables_component.py",
        "src/fern/types/destiny_components_vendors_destiny_public_vendor_component.py",
        "src/fern/types/destiny_components_vendors_destiny_public_vendor_sale_item_component.py",
        "src/fern/types/destiny_components_vendors_destiny_vendor_base_component.py",
        "src/fern/types/destiny_components_vendors_destiny_vendor_group.py",
        "src/fern/types/destiny_components_vendors_destiny_vendor_group_component.py",
        "src/fern/types/destiny_components_vendors_destiny_vendor_sale_item_base_component.py",
        "src/fern/types/destiny_config_destiny_manifest.py",
        "src/fern/types/destiny_config_gear_asset_data_base_definition.py",
        "src/fern/types/destiny_config_image_pyramid_entry.py",
        "src/fern/types/destiny_constants_destiny_environment_location_mapping.py",
        "src/fern/types/destiny_damage_type.py",
        "src/fern/types/destiny_definitions_activity_modifiers_destiny_activity_modifier_definition.py",
        "src/fern/types/destiny_definitions_animations_destiny_animation_reference.py",
        "src/fern/types/destiny_definitions_artifacts_destiny_artifact_definition.py",
        "src/fern/types/destiny_definitions_artifacts_destiny_artifact_tier_definition.py",
        "src/fern/types/destiny_definitions_artifacts_destiny_artifact_tier_item_definition.py",
        "src/fern/types/destiny_definitions_breaker_types_destiny_breaker_type_definition.py",
        "src/fern/types/destiny_definitions_checklists_destiny_checklist_definition.py",
        "src/fern/types/destiny_definitions_checklists_destiny_checklist_entry_definition.py",
        "src/fern/types/destiny_definitions_collectibles_destiny_collectible_acquisition_block.py",
        "src/fern/types/destiny_definitions_collectibles_destiny_collectible_definition.py",
        "src/fern/types/destiny_definitions_collectibles_destiny_collectible_state_block.py",
        "src/fern/types/destiny_definitions_common_destiny_display_properties_definition.py",
        "src/fern/types/destiny_definitions_common_destiny_icon_sequence_definition.py",
        "src/fern/types/destiny_definitions_common_destiny_position_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_challenge_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_graph_list_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_guided_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_insertion_point_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_loadout_requirement.py",
        "src/fern/types/destiny_definitions_destiny_activity_loadout_requirement_set.py",
        "src/fern/types/destiny_definitions_destiny_activity_matchmaking_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_mode_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_modifier_reference_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_playlist_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_reward_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_type_definition.py",
        "src/fern/types/destiny_definitions_destiny_activity_unlock_string_definition.py",
        "src/fern/types/destiny_definitions_destiny_arrangement_region_filter_definition.py",
        "src/fern/types/destiny_definitions_destiny_art_dye_reference.py",
        "src/fern/types/destiny_definitions_destiny_bubble_definition.py",
        "src/fern/types/destiny_definitions_destiny_class_definition.py",
        "src/fern/types/destiny_definitions_destiny_damage_type_definition.py",
        "src/fern/types/destiny_definitions_destiny_definition.py",
        "src/fern/types/destiny_definitions_destiny_destination_bubble_setting_definition.py",
        "src/fern/types/destiny_definitions_destiny_destination_definition.py",
        "src/fern/types/destiny_definitions_destiny_display_category_definition.py",
        "src/fern/types/destiny_definitions_destiny_entity_search_result.py",
        "src/fern/types/destiny_definitions_destiny_entity_search_result_item.py",
        "src/fern/types/destiny_definitions_destiny_equipment_slot_definition.py",
        "src/fern/types/destiny_definitions_destiny_equipping_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_faction_definition.py",
        "src/fern/types/destiny_definitions_destiny_faction_vendor_definition.py",
        "src/fern/types/destiny_definitions_destiny_gear_art_arrangement_reference.py",
        "src/fern/types/destiny_definitions_destiny_gender_definition.py",
        "src/fern/types/destiny_definitions_destiny_inventory_bucket_definition.py",
        "src/fern/types/destiny_definitions_destiny_inventory_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_inventory_item_stat_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_action_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_action_required_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_category_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_crafting_block_bonus_plug_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_crafting_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_creation_entry_level_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_gearset_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_intrinsic_socket_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_inventory_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_investment_stat_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_metric_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_objective_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_perk_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_preview_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_quality_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_sack_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_set_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_set_block_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_socket_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_socket_category_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_socket_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_socket_entry_plug_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_socket_entry_plug_item_randomized_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_source_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_stat_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_summary_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_talent_grid_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_tooltip_notification.py",
        "src/fern/types/destiny_definitions_destiny_item_translation_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_value_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_item_vendor_source_reference.py",
        "src/fern/types/destiny_definitions_destiny_item_version_definition.py",
        "src/fern/types/destiny_definitions_destiny_location_definition.py",
        "src/fern/types/destiny_definitions_destiny_location_release_definition.py",
        "src/fern/types/destiny_definitions_destiny_material_requirement.py",
        "src/fern/types/destiny_definitions_destiny_material_requirement_set_definition.py",
        "src/fern/types/destiny_definitions_destiny_medal_tier_definition.py",
        "src/fern/types/destiny_definitions_destiny_node_activation_requirement.py",
        "src/fern/types/destiny_definitions_destiny_node_socket_replace_response.py",
        "src/fern/types/destiny_definitions_destiny_node_step_definition.py",
        "src/fern/types/destiny_definitions_destiny_objective_definition.py",
        "src/fern/types/destiny_definitions_destiny_objective_display_properties.py",
        "src/fern/types/destiny_definitions_destiny_objective_perk_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_objective_stat_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_place_definition.py",
        "src/fern/types/destiny_definitions_destiny_plug_item_crafting_requirements.py",
        "src/fern/types/destiny_definitions_destiny_plug_item_crafting_unlock_requirement.py",
        "src/fern/types/destiny_definitions_destiny_progression_definition.py",
        "src/fern/types/destiny_definitions_destiny_progression_display_properties_definition.py",
        "src/fern/types/destiny_definitions_destiny_progression_mapping_definition.py",
        "src/fern/types/destiny_definitions_destiny_progression_reward_definition.py",
        "src/fern/types/destiny_definitions_destiny_progression_reward_item_quantity.py",
        "src/fern/types/destiny_definitions_destiny_progression_step_definition.py",
        "src/fern/types/destiny_definitions_destiny_race_definition.py",
        "src/fern/types/destiny_definitions_destiny_reward_source_category.py",
        "src/fern/types/destiny_definitions_destiny_reward_source_definition.py",
        "src/fern/types/destiny_definitions_destiny_sandbox_pattern_definition.py",
        "src/fern/types/destiny_definitions_destiny_sandbox_perk_definition.py",
        "src/fern/types/destiny_definitions_destiny_stat_definition.py",
        "src/fern/types/destiny_definitions_destiny_stat_display_definition.py",
        "src/fern/types/destiny_definitions_destiny_stat_group_definition.py",
        "src/fern/types/destiny_definitions_destiny_stat_override_definition.py",
        "src/fern/types/destiny_definitions_destiny_talent_exclusive_group.py",
        "src/fern/types/destiny_definitions_destiny_talent_grid_definition.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_category.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_definition.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_exclusive_set_definition.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_damage_types.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_groups.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_guardian_attributes.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_impact_effects.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_light_abilities.py",
        "src/fern/types/destiny_definitions_destiny_talent_node_step_weapon_performances.py",
        "src/fern/types/destiny_definitions_destiny_unlock_definition.py",
        "src/fern/types/destiny_definitions_destiny_unlock_expression_definition.py",
        "src/fern/types/destiny_definitions_destiny_unlock_value_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_accepted_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_action_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_category_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_category_overlay_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_display_properties_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_group_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_group_reference.py",
        "src/fern/types/destiny_definitions_destiny_vendor_interaction_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_interaction_reply_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_interaction_sack_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_inventory_flyout_bucket_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_inventory_flyout_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_item_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_item_quantity.py",
        "src/fern/types/destiny_definitions_destiny_vendor_item_socket_override.py",
        "src/fern/types/destiny_definitions_destiny_vendor_requirement_display_entry_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_sale_item_action_block_definition.py",
        "src/fern/types/destiny_definitions_destiny_vendor_service_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_art_element_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_connection_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_display_objective_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_display_progression_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_node_activity_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_node_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_node_featuring_state_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_activity_graph_node_state_entry.py",
        "src/fern/types/destiny_definitions_director_destiny_linked_graph_definition.py",
        "src/fern/types/destiny_definitions_director_destiny_linked_graph_entry_definition.py",
        "src/fern/types/destiny_definitions_energy_types_destiny_energy_type_definition.py",
        "src/fern/types/destiny_definitions_guardian_ranks_destiny_guardian_rank_constants_definition.py",
        "src/fern/types/destiny_definitions_guardian_ranks_destiny_guardian_rank_definition.py",
        "src/fern/types/destiny_definitions_guardian_ranks_destiny_guardian_rank_icon_backgrounds_definition.py",
        "src/fern/types/destiny_definitions_items_destiny_derived_item_category_definition.py",
        "src/fern/types/destiny_definitions_items_destiny_derived_item_definition.py",
        "src/fern/types/destiny_definitions_items_destiny_energy_capacity_entry.py",
        "src/fern/types/destiny_definitions_items_destiny_energy_cost_entry.py",
        "src/fern/types/destiny_definitions_items_destiny_item_plug_definition.py",
        "src/fern/types/destiny_definitions_items_destiny_item_tier_type_definition.py",
        "src/fern/types/destiny_definitions_items_destiny_item_tier_type_infusion_block.py",
        "src/fern/types/destiny_definitions_items_destiny_parent_item_override.py",
        "src/fern/types/destiny_definitions_items_destiny_plug_rule_definition.py",
        "src/fern/types/destiny_definitions_loadouts_destiny_loadout_color_definition.py",
        "src/fern/types/destiny_definitions_loadouts_destiny_loadout_constants_definition.py",
        "src/fern/types/destiny_definitions_loadouts_destiny_loadout_icon_definition.py",
        "src/fern/types/destiny_definitions_loadouts_destiny_loadout_name_definition.py",
        "src/fern/types/destiny_definitions_lore_destiny_lore_definition.py",
        "src/fern/types/destiny_definitions_metrics_destiny_metric_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_activity_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_activity_variant_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_challenge_activity_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_challenge_activity_graph_node_entry.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_challenge_activity_phase.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_challenge_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_display_preference.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_quest_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_quest_reward_item.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_quest_rewards_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_reward_category_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_reward_entry_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_type.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_value_definition.py",
        "src/fern/types/destiny_definitions_milestones_destiny_milestone_vendor_definition.py",
        "src/fern/types/destiny_definitions_power_caps_destiny_power_cap_definition.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_child_block.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_base_definition.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_child_entry.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_child_entry_base.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_children_block.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_collectible_child_entry.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_craftable_child_entry.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_definition.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_metric_child_entry.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_record_child_entry.py",
        "src/fern/types/destiny_definitions_presentation_destiny_presentation_node_requirements_block.py",
        "src/fern/types/destiny_definitions_presentation_destiny_scored_presentation_node_base_definition.py",
        "src/fern/types/destiny_definitions_progression_destiny_progression_level_requirement_definition.py",
        "src/fern/types/destiny_definitions_records_destiny_record_completion_block.py",
        "src/fern/types/destiny_definitions_records_destiny_record_definition.py",
        "src/fern/types/destiny_definitions_records_destiny_record_expiration_block.py",
        "src/fern/types/destiny_definitions_records_destiny_record_interval_block.py",
        "src/fern/types/destiny_definitions_records_destiny_record_interval_objective.py",
        "src/fern/types/destiny_definitions_records_destiny_record_interval_rewards.py",
        "src/fern/types/destiny_definitions_records_destiny_record_title_block.py",
        "src/fern/types/destiny_definitions_records_schema_record_state_block.py",
        "src/fern/types/destiny_definitions_reporting_destiny_report_reason_category_definition.py",
        "src/fern/types/destiny_definitions_reporting_destiny_report_reason_definition.py",
        "src/fern/types/destiny_definitions_seasons_destiny_event_card_definition.py",
        "src/fern/types/destiny_definitions_seasons_destiny_event_card_images.py",
        "src/fern/types/destiny_definitions_seasons_destiny_season_definition.py",
        "src/fern/types/destiny_definitions_seasons_destiny_season_pass_definition.py",
        "src/fern/types/destiny_definitions_seasons_destiny_season_preview_definition.py",
        "src/fern/types/destiny_definitions_seasons_destiny_season_preview_image_definition.py",
        "src/fern/types/destiny_definitions_social_destiny_social_commendation_definition.py",
        "src/fern/types/destiny_definitions_social_destiny_social_commendation_node_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_insert_plug_action_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_plug_set_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_plug_whitelist_entry_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_socket_category_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_socket_type_definition.py",
        "src/fern/types/destiny_definitions_sockets_destiny_socket_type_scalar_material_requirement_entry.py",
        "src/fern/types/destiny_definitions_sources_destiny_item_source_definition.py",
        "src/fern/types/destiny_definitions_traits_destiny_trait_definition.py",
        "src/fern/types/destiny_definitions_vendors_destiny_vendor_location_definition.py",
        "src/fern/types/destiny_destiny_activity.py",
        "src/fern/types/destiny_destiny_activity_difficulty_tier.py",
        "src/fern/types/destiny_destiny_activity_mode_category.py",
        "src/fern/types/destiny_destiny_activity_nav_point_type.py",
        "src/fern/types/destiny_destiny_ammunition_type.py",
        "src/fern/types/destiny_destiny_breaker_type.py",
        "src/fern/types/destiny_destiny_class.py",
        "src/fern/types/destiny_destiny_collectible_state.py",
        "src/fern/types/destiny_destiny_component_type.py",
        "src/fern/types/destiny_destiny_energy_type.py",
        "src/fern/types/destiny_destiny_equip_item_result.py",
        "src/fern/types/destiny_destiny_equip_item_results.py",
        "src/fern/types/destiny_destiny_game_privacy_setting.py",
        "src/fern/types/destiny_destiny_game_versions.py",
        "src/fern/types/destiny_destiny_gating_scope.py",
        "src/fern/types/destiny_destiny_gender.py",
        "src/fern/types/destiny_destiny_graph_node_state.py",
        "src/fern/types/destiny_destiny_item_quantity.py",
        "src/fern/types/destiny_destiny_item_sort_type.py",
        "src/fern/types/destiny_destiny_item_sub_type.py",
        "src/fern/types/destiny_destiny_item_type.py",
        "src/fern/types/destiny_destiny_join_closed_reasons.py",
        "src/fern/types/destiny_destiny_objective_grant_style.py",
        "src/fern/types/destiny_destiny_objective_ui_style.py",
        "src/fern/types/destiny_destiny_party_member_states.py",
        "src/fern/types/destiny_destiny_presentation_display_style.py",
        "src/fern/types/destiny_destiny_presentation_node_state.py",
        "src/fern/types/destiny_destiny_presentation_node_type.py",
        "src/fern/types/destiny_destiny_presentation_screen_style.py",
        "src/fern/types/destiny_destiny_progression.py",
        "src/fern/types/destiny_destiny_progression_reset_entry.py",
        "src/fern/types/destiny_destiny_progression_reward_item_acquisition_behavior.py",
        "src/fern/types/destiny_destiny_progression_reward_item_state.py",
        "src/fern/types/destiny_destiny_progression_scope.py",
        "src/fern/types/destiny_destiny_progression_step_display_effect.py",
        "src/fern/types/destiny_destiny_race.py",
        "src/fern/types/destiny_destiny_record_state.py",
        "src/fern/types/destiny_destiny_record_toast_style.py",
        "src/fern/types/destiny_destiny_record_value_style.py",
        "src/fern/types/destiny_destiny_scope.py",
        "src/fern/types/destiny_destiny_socket_category_style.py",
        "src/fern/types/destiny_destiny_socket_visibility.py",
        "src/fern/types/destiny_destiny_stat.py",
        "src/fern/types/destiny_destiny_stat_aggregation_type.py",
        "src/fern/types/destiny_destiny_stat_category.py",
        "src/fern/types/destiny_destiny_talent_node.py",
        "src/fern/types/destiny_destiny_talent_node_stat_block.py",
        "src/fern/types/destiny_destiny_talent_node_state.py",
        "src/fern/types/destiny_destiny_unlock_status.py",
        "src/fern/types/destiny_destiny_unlock_value_ui_style.py",
        "src/fern/types/destiny_destiny_vendor_filter.py",
        "src/fern/types/destiny_destiny_vendor_interaction_reward_selection.py",
        "src/fern/types/destiny_destiny_vendor_item_refund_policy.py",
        "src/fern/types/destiny_destiny_vendor_item_state.py",
        "src/fern/types/destiny_destiny_vendor_progression_type.py",
        "src/fern/types/destiny_destiny_vendor_reply_type.py",
        "src/fern/types/destiny_dye_reference.py",
        "src/fern/types/destiny_entities_characters_destiny_character_activities_component.py",
        "src/fern/types/destiny_entities_characters_destiny_character_component.py",
        "src/fern/types/destiny_entities_characters_destiny_character_progression_component.py",
        "src/fern/types/destiny_entities_characters_destiny_character_render_component.py",
        "src/fern/types/destiny_entities_inventory_destiny_inventory_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_instance_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_instance_energy.py",
        "src/fern/types/destiny_entities_items_destiny_item_objectives_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_perks_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_render_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_socket_state.py",
        "src/fern/types/destiny_entities_items_destiny_item_sockets_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_stats_component.py",
        "src/fern/types/destiny_entities_items_destiny_item_talent_grid_component.py",
        "src/fern/types/destiny_entities_profiles_destiny_profile_component.py",
        "src/fern/types/destiny_entities_profiles_destiny_vendor_receipts_component.py",
        "src/fern/types/destiny_entities_vendors_destiny_vendor_categories_component.py",
        "src/fern/types/destiny_entities_vendors_destiny_vendor_category.py",
        "src/fern/types/destiny_entities_vendors_destiny_vendor_component.py",
        "src/fern/types/destiny_entities_vendors_destiny_vendor_sale_item_component.py",
        "src/fern/types/destiny_equip_failure_reason.py",
        "src/fern/types/destiny_equipping_item_block_attributes.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_activity_mode_type.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_activity_mode_type_array.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_historical_stats_definition.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_stats_category_type.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_stats_group_type.py",
        "src/fern/types/destiny_historical_stats_definitions_destiny_stats_merge_method.py",
        "src/fern/types/destiny_historical_stats_definitions_period_type.py",
        "src/fern/types/destiny_historical_stats_definitions_period_type_array.py",
        "src/fern/types/destiny_historical_stats_definitions_unit_type.py",
        "src/fern/types/destiny_historical_stats_destiny_activity_history_results.py",
        "src/fern/types/destiny_historical_stats_destiny_aggregate_activity_results.py",
        "src/fern/types/destiny_historical_stats_destiny_aggregate_activity_stats.py",
        "src/fern/types/destiny_historical_stats_destiny_clan_aggregate_stat.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_account_result.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_activity.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_by_period.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_per_character.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_period_group.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_results.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_value.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_value_pair.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_stats_with_merged.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_weapon_stats.py",
        "src/fern/types/destiny_historical_stats_destiny_historical_weapon_stats_data.py",
        "src/fern/types/destiny_historical_stats_destiny_leaderboard.py",
        "src/fern/types/destiny_historical_stats_destiny_leaderboard_entry.py",
        "src/fern/types/destiny_historical_stats_destiny_leaderboard_results.py",
        "src/fern/types/destiny_historical_stats_destiny_player.py",
        "src/fern/types/destiny_historical_stats_destiny_post_game_carnage_report_data.py",
        "src/fern/types/destiny_historical_stats_destiny_post_game_carnage_report_entry.py",
        "src/fern/types/destiny_historical_stats_destiny_post_game_carnage_report_extended_data.py",
        "src/fern/types/destiny_historical_stats_destiny_post_game_carnage_report_team_entry.py",
        "src/fern/types/destiny_item_bind_status.py",
        "src/fern/types/destiny_item_component_set_ofint32.py",
        "src/fern/types/destiny_item_component_set_ofint64.py",
        "src/fern/types/destiny_item_component_set_ofuint32.py",
        "src/fern/types/destiny_item_location.py",
        "src/fern/types/destiny_item_perk_visibility.py",
        "src/fern/types/destiny_item_state.py",
        "src/fern/types/destiny_milestones_destiny_milestone.py",
        "src/fern/types/destiny_milestones_destiny_milestone_activity.py",
        "src/fern/types/destiny_milestones_destiny_milestone_activity_completion_status.py",
        "src/fern/types/destiny_milestones_destiny_milestone_activity_phase.py",
        "src/fern/types/destiny_milestones_destiny_milestone_activity_variant.py",
        "src/fern/types/destiny_milestones_destiny_milestone_challenge_activity.py",
        "src/fern/types/destiny_milestones_destiny_milestone_content.py",
        "src/fern/types/destiny_milestones_destiny_milestone_content_item_category.py",
        "src/fern/types/destiny_milestones_destiny_milestone_quest.py",
        "src/fern/types/destiny_milestones_destiny_milestone_reward_category.py",
        "src/fern/types/destiny_milestones_destiny_milestone_reward_entry.py",
        "src/fern/types/destiny_milestones_destiny_milestone_vendor.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_activity.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_activity_variant.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_challenge.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_challenge_activity.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_quest.py",
        "src/fern/types/destiny_milestones_destiny_public_milestone_vendor.py",
        "src/fern/types/destiny_misc_destiny_color.py",
        "src/fern/types/destiny_perks_destiny_perk_reference.py",
        "src/fern/types/destiny_plug_availability_mode.py",
        "src/fern/types/destiny_plug_ui_styles.py",
        "src/fern/types/destiny_progression_destiny_faction_progression.py",
        "src/fern/types/destiny_quests_destiny_objective_progress.py",
        "src/fern/types/destiny_quests_destiny_quest_status.py",
        "src/fern/types/destiny_reporting_requests_destiny_report_offense_pgcr_request.py",
        "src/fern/types/destiny_requests_actions_destiny_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_character_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_insert_plugs_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_insert_plugs_free_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_insert_plugs_request_entry.py",
        "src/fern/types/destiny_requests_actions_destiny_item_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_item_set_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_item_state_request.py",
        "src/fern/types/destiny_requests_actions_destiny_loadout_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_loadout_update_action_request.py",
        "src/fern/types/destiny_requests_actions_destiny_postmaster_transfer_request.py",
        "src/fern/types/destiny_requests_actions_destiny_socket_array_type.py",
        "src/fern/types/destiny_requests_destiny_item_transfer_request.py",
        "src/fern/types/destiny_responses_destiny_character_response.py",
        "src/fern/types/destiny_responses_destiny_collectible_node_detail_response.py",
        "src/fern/types/destiny_responses_destiny_error_profile.py",
        "src/fern/types/destiny_responses_destiny_item_change_response.py",
        "src/fern/types/destiny_responses_destiny_item_response.py",
        "src/fern/types/destiny_responses_destiny_linked_profiles_response.py",
        "src/fern/types/destiny_responses_destiny_profile_response.py",
        "src/fern/types/destiny_responses_destiny_profile_user_info_card.py",
        "src/fern/types/destiny_responses_destiny_public_vendors_response.py",
        "src/fern/types/destiny_responses_destiny_vendor_response.py",
        "src/fern/types/destiny_responses_destiny_vendors_response.py",
        "src/fern/types/destiny_responses_inventory_changed_response.py",
        "src/fern/types/destiny_responses_personal_destiny_vendor_sale_item_set_component.py",
        "src/fern/types/destiny_responses_public_destiny_vendor_sale_item_set_component.py",
        "src/fern/types/destiny_socket_plug_sources.py",
        "src/fern/types/destiny_socket_type_action_type.py",
        "src/fern/types/destiny_sockets_destiny_item_plug.py",
        "src/fern/types/destiny_sockets_destiny_item_plug_base.py",
        "src/fern/types/destiny_special_item_type.py",
        "src/fern/types/destiny_tier_type.py",
        "src/fern/types/destiny_transfer_statuses.py",
        "src/fern/types/destiny_vendor_display_category_sort_order.py",
        "src/fern/types/destiny_vendor_interaction_type.py",
        "src/fern/types/destiny_vendor_item_status.py",
        "src/fern/types/destiny_vendor_sale_item_set_component_of_destiny_public_vendor_sale_item_component.py",
        "src/fern/types/destiny_vendor_sale_item_set_component_of_destiny_vendor_sale_item_component.py",
        "src/fern/types/destiny_vendors_destiny_vendor_receipt.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_instance_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_perks_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_plug_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_render_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_reusable_plugs_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_sockets_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_stats_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_item_talent_grid_component.py",
        "src/fern/types/dictionary_component_response_ofint32and_destiny_vendor_sale_item_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_character_activities_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_character_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_character_progression_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_character_records_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_character_render_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_collectibles_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_craftables_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_currencies_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_inventory_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_instance_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_perks_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_plug_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_render_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_reusable_plugs_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_sockets_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_stats_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_item_talent_grid_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_kiosks_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_loadouts_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_plug_sets_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_presentation_nodes_component.py",
        "src/fern/types/dictionary_component_response_ofint64and_destiny_string_variables_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_instance_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_perks_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_plug_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_plug_objectives_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_render_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_reusable_plugs_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_sockets_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_stats_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_item_talent_grid_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_public_vendor_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_vendor_categories_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_destiny_vendor_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_personal_destiny_vendor_sale_item_set_component.py",
        "src/fern/types/dictionary_component_response_ofuint32and_public_destiny_vendor_sale_item_set_component.py",
        "src/fern/types/entities_entity_action_result.py",
        "src/fern/types/exceptions_platform_error_codes.py",
        "src/fern/types/fireteam_fireteam_date_range.py",
        "src/fern/types/fireteam_fireteam_member.py",
        "src/fern/types/fireteam_fireteam_platform.py",
        "src/fern/types/fireteam_fireteam_platform_invite_result.py",
        "src/fern/types/fireteam_fireteam_public_search_option.py",
        "src/fern/types/fireteam_fireteam_response.py",
        "src/fern/types/fireteam_fireteam_slot_search.py",
        "src/fern/types/fireteam_fireteam_summary.py",
        "src/fern/types/fireteam_fireteam_user_info_card.py",
        "src/fern/types/forum_community_content_sort_mode.py",
        "src/fern/types/forum_forum_media_type.py",
        "src/fern/types/forum_forum_post_popularity.py",
        "src/fern/types/forum_forum_post_sort_enum.py",
        "src/fern/types/forum_forum_recruitment_detail.py",
        "src/fern/types/forum_forum_recruitment_intensity_label.py",
        "src/fern/types/forum_forum_recruitment_tone_label.py",
        "src/fern/types/forum_forum_topics_category_filters_enum.py",
        "src/fern/types/forum_forum_topics_quick_date_enum.py",
        "src/fern/types/forum_forum_topics_sort_enum.py",
        "src/fern/types/forum_poll_response.py",
        "src/fern/types/forum_poll_result.py",
        "src/fern/types/forum_post_response.py",
        "src/fern/types/forum_post_search_response.py",
        "src/fern/types/forums_forum_flags_enum.py",
        "src/fern/types/forums_forum_post_category_enums.py",
        "src/fern/types/global_alert.py",
        "src/fern/types/global_alert_level.py",
        "src/fern/types/global_alert_type.py",
        "src/fern/types/groups_v2capabilities.py",
        "src/fern/types/groups_v2chat_security_setting.py",
        "src/fern/types/groups_v2clan_banner.py",
        "src/fern/types/groups_v2get_groups_for_member_response.py",
        "src/fern/types/groups_v2group_alliance_status.py",
        "src/fern/types/groups_v2group_application_list_request.py",
        "src/fern/types/groups_v2group_application_request.py",
        "src/fern/types/groups_v2group_application_resolve_state.py",
        "src/fern/types/groups_v2group_application_response.py",
        "src/fern/types/groups_v2group_ban.py",
        "src/fern/types/groups_v2group_ban_request.py",
        "src/fern/types/groups_v2group_date_range.py",
        "src/fern/types/groups_v2group_edit_action.py",
        "src/fern/types/groups_v2group_features.py",
        "src/fern/types/groups_v2group_homepage.py",
        "src/fern/types/groups_v2group_member.py",
        "src/fern/types/groups_v2group_member_application.py",
        "src/fern/types/groups_v2group_member_count_filter.py",
        "src/fern/types/groups_v2group_member_leave_result.py",
        "src/fern/types/groups_v2group_membership.py",
        "src/fern/types/groups_v2group_membership_base.py",
        "src/fern/types/groups_v2group_membership_search_response.py",
        "src/fern/types/groups_v2group_name_search_request.py",
        "src/fern/types/groups_v2group_optional_conversation.py",
        "src/fern/types/groups_v2group_optional_conversation_add_request.py",
        "src/fern/types/groups_v2group_optional_conversation_edit_request.py",
        "src/fern/types/groups_v2group_options_edit_action.py",
        "src/fern/types/groups_v2group_post_publicity.py",
        "src/fern/types/groups_v2group_potential_member.py",
        "src/fern/types/groups_v2group_potential_member_status.py",
        "src/fern/types/groups_v2group_potential_membership.py",
        "src/fern/types/groups_v2group_potential_membership_search_response.py",
        "src/fern/types/groups_v2group_query.py",
        "src/fern/types/groups_v2group_response.py",
        "src/fern/types/groups_v2group_search_response.py",
        "src/fern/types/groups_v2group_sort_by.py",
        "src/fern/types/groups_v2group_type.py",
        "src/fern/types/groups_v2group_user_base.py",
        "src/fern/types/groups_v2group_user_info_card.py",
        "src/fern/types/groups_v2group_v2.py",
        "src/fern/types/groups_v2group_v2card.py",
        "src/fern/types/groups_v2group_v2clan_info.py",
        "src/fern/types/groups_v2group_v2clan_info_and_investment.py",
        "src/fern/types/groups_v2groups_for_member_filter.py",
        "src/fern/types/groups_v2host_guided_games_permission_level.py",
        "src/fern/types/groups_v2membership_option.py",
        "src/fern/types/groups_v2runtime_group_member_type.py",
        "src/fern/types/ignores_ignore_length.py",
        "src/fern/types/ignores_ignore_response.py",
        "src/fern/types/ignores_ignore_status.py",
        "src/fern/types/interpolation_interpolation_point.py",
        "src/fern/types/interpolation_interpolation_point_float.py",
        "src/fern/types/links_hyperlink_reference.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/queries_paged_query.py",
        "src/fern/types/queries_search_result.py",
        "src/fern/types/schema1.py",
        "src/fern/types/schema10.py",
        "src/fern/types/schema100.py",
        "src/fern/types/schema101.py",
        "src/fern/types/schema102.py",
        "src/fern/types/schema103.py",
        "src/fern/types/schema104.py",
        "src/fern/types/schema105.py",
        "src/fern/types/schema106.py",
        "src/fern/types/schema107.py",
        "src/fern/types/schema108.py",
        "src/fern/types/schema109.py",
        "src/fern/types/schema11.py",
        "src/fern/types/schema110.py",
        "src/fern/types/schema111.py",
        "src/fern/types/schema112.py",
        "src/fern/types/schema113.py",
        "src/fern/types/schema114.py",
        "src/fern/types/schema115.py",
        "src/fern/types/schema116.py",
        "src/fern/types/schema117.py",
        "src/fern/types/schema118.py",
        "src/fern/types/schema12.py",
        "src/fern/types/schema13.py",
        "src/fern/types/schema14.py",
        "src/fern/types/schema15.py",
        "src/fern/types/schema16.py",
        "src/fern/types/schema17.py",
        "src/fern/types/schema18.py",
        "src/fern/types/schema19.py",
        "src/fern/types/schema2.py",
        "src/fern/types/schema20.py",
        "src/fern/types/schema21.py",
        "src/fern/types/schema22.py",
        "src/fern/types/schema23.py",
        "src/fern/types/schema24.py",
        "src/fern/types/schema25.py",
        "src/fern/types/schema26.py",
        "src/fern/types/schema27.py",
        "src/fern/types/schema28.py",
        "src/fern/types/schema29.py",
        "src/fern/types/schema3.py",
        "src/fern/types/schema30.py",
        "src/fern/types/schema31.py",
        "src/fern/types/schema32.py",
        "src/fern/types/schema33.py",
        "src/fern/types/schema34.py",
        "src/fern/types/schema35.py",
        "src/fern/types/schema36.py",
        "src/fern/types/schema37.py",
        "src/fern/types/schema38.py",
        "src/fern/types/schema39.py",
        "src/fern/types/schema4.py",
        "src/fern/types/schema40.py",
        "src/fern/types/schema41.py",
        "src/fern/types/schema42.py",
        "src/fern/types/schema43.py",
        "src/fern/types/schema44.py",
        "src/fern/types/schema45.py",
        "src/fern/types/schema46.py",
        "src/fern/types/schema47.py",
        "src/fern/types/schema48.py",
        "src/fern/types/schema49.py",
        "src/fern/types/schema5.py",
        "src/fern/types/schema50.py",
        "src/fern/types/schema51.py",
        "src/fern/types/schema52.py",
        "src/fern/types/schema53.py",
        "src/fern/types/schema54.py",
        "src/fern/types/schema55.py",
        "src/fern/types/schema56.py",
        "src/fern/types/schema57.py",
        "src/fern/types/schema58.py",
        "src/fern/types/schema59.py",
        "src/fern/types/schema6.py",
        "src/fern/types/schema60.py",
        "src/fern/types/schema61.py",
        "src/fern/types/schema62.py",
        "src/fern/types/schema63.py",
        "src/fern/types/schema64.py",
        "src/fern/types/schema65.py",
        "src/fern/types/schema66.py",
        "src/fern/types/schema67.py",
        "src/fern/types/schema68.py",
        "src/fern/types/schema69.py",
        "src/fern/types/schema7.py",
        "src/fern/types/schema70.py",
        "src/fern/types/schema71.py",
        "src/fern/types/schema72.py",
        "src/fern/types/schema73.py",
        "src/fern/types/schema74.py",
        "src/fern/types/schema75.py",
        "src/fern/types/schema76.py",
        "src/fern/types/schema77.py",
        "src/fern/types/schema78.py",
        "src/fern/types/schema79.py",
        "src/fern/types/schema8.py",
        "src/fern/types/schema80.py",
        "src/fern/types/schema81.py",
        "src/fern/types/schema82.py",
        "src/fern/types/schema83.py",
        "src/fern/types/schema84.py",
        "src/fern/types/schema85.py",
        "src/fern/types/schema86.py",
        "src/fern/types/schema87.py",
        "src/fern/types/schema88.py",
        "src/fern/types/schema89.py",
        "src/fern/types/schema9.py",
        "src/fern/types/schema90.py",
        "src/fern/types/schema91.py",
        "src/fern/types/schema92.py",
        "src/fern/types/schema93.py",
        "src/fern/types/schema94.py",
        "src/fern/types/schema95.py",
        "src/fern/types/schema96.py",
        "src/fern/types/schema97.py",
        "src/fern/types/schema98.py",
        "src/fern/types/schema99.py",
        "src/fern/types/search_result_of_content_item_public_contract.py",
        "src/fern/types/search_result_of_destiny_entity_search_result_item.py",
        "src/fern/types/search_result_of_fireteam_response.py",
        "src/fern/types/search_result_of_fireteam_summary.py",
        "src/fern/types/search_result_of_group_ban.py",
        "src/fern/types/search_result_of_group_member.py",
        "src/fern/types/search_result_of_group_member_application.py",
        "src/fern/types/search_result_of_group_membership.py",
        "src/fern/types/search_result_of_group_potential_membership.py",
        "src/fern/types/search_result_of_group_v2card.py",
        "src/fern/types/search_result_of_post_response.py",
        "src/fern/types/search_result_of_trending_entry.py",
        "src/fern/types/single_component_response_of_destiny_character_activities_component.py",
        "src/fern/types/single_component_response_of_destiny_character_component.py",
        "src/fern/types/single_component_response_of_destiny_character_progression_component.py",
        "src/fern/types/single_component_response_of_destiny_character_records_component.py",
        "src/fern/types/single_component_response_of_destiny_character_render_component.py",
        "src/fern/types/single_component_response_of_destiny_collectibles_component.py",
        "src/fern/types/single_component_response_of_destiny_currencies_component.py",
        "src/fern/types/single_component_response_of_destiny_inventory_component.py",
        "src/fern/types/single_component_response_of_destiny_item_component.py",
        "src/fern/types/single_component_response_of_destiny_item_instance_component.py",
        "src/fern/types/single_component_response_of_destiny_item_objectives_component.py",
        "src/fern/types/single_component_response_of_destiny_item_perks_component.py",
        "src/fern/types/single_component_response_of_destiny_item_plug_objectives_component.py",
        "src/fern/types/single_component_response_of_destiny_item_render_component.py",
        "src/fern/types/single_component_response_of_destiny_item_reusable_plugs_component.py",
        "src/fern/types/single_component_response_of_destiny_item_sockets_component.py",
        "src/fern/types/single_component_response_of_destiny_item_stats_component.py",
        "src/fern/types/single_component_response_of_destiny_item_talent_grid_component.py",
        "src/fern/types/single_component_response_of_destiny_kiosks_component.py",
        "src/fern/types/single_component_response_of_destiny_loadouts_component.py",
        "src/fern/types/single_component_response_of_destiny_metrics_component.py",
        "src/fern/types/single_component_response_of_destiny_platform_silver_component.py",
        "src/fern/types/single_component_response_of_destiny_plug_sets_component.py",
        "src/fern/types/single_component_response_of_destiny_presentation_nodes_component.py",
        "src/fern/types/single_component_response_of_destiny_profile_collectibles_component.py",
        "src/fern/types/single_component_response_of_destiny_profile_component.py",
        "src/fern/types/single_component_response_of_destiny_profile_progression_component.py",
        "src/fern/types/single_component_response_of_destiny_profile_records_component.py",
        "src/fern/types/single_component_response_of_destiny_profile_transitory_component.py",
        "src/fern/types/single_component_response_of_destiny_social_commendations_component.py",
        "src/fern/types/single_component_response_of_destiny_string_variables_component.py",
        "src/fern/types/single_component_response_of_destiny_vendor_categories_component.py",
        "src/fern/types/single_component_response_of_destiny_vendor_component.py",
        "src/fern/types/single_component_response_of_destiny_vendor_group_component.py",
        "src/fern/types/single_component_response_of_destiny_vendor_receipts_component.py",
        "src/fern/types/social_friends_bungie_friend.py",
        "src/fern/types/social_friends_bungie_friend_list_response.py",
        "src/fern/types/social_friends_bungie_friend_request_list_response.py",
        "src/fern/types/social_friends_friend_relationship_state.py",
        "src/fern/types/social_friends_platform_friend.py",
        "src/fern/types/social_friends_platform_friend_response.py",
        "src/fern/types/social_friends_platform_friend_type.py",
        "src/fern/types/social_friends_presence_online_state_flags.py",
        "src/fern/types/social_friends_presence_status.py",
        "src/fern/types/stream_info.py",
        "src/fern/types/streaming_drop_state_enum.py",
        "src/fern/types/tags_models_contracts_tag_response.py",
        "src/fern/types/tokens_bungie_reward_display.py",
        "src/fern/types/tokens_collectible_definitions.py",
        "src/fern/types/tokens_partner_offer_claim_request.py",
        "src/fern/types/tokens_partner_offer_history_response.py",
        "src/fern/types/tokens_partner_offer_sku_history_response.py",
        "src/fern/types/tokens_partner_reward_history_response.py",
        "src/fern/types/tokens_reward_availability_model.py",
        "src/fern/types/tokens_reward_display_properties.py",
        "src/fern/types/tokens_twitch_drop_history_response.py",
        "src/fern/types/tokens_user_reward_availability_model.py",
        "src/fern/types/trending_trending_categories.py",
        "src/fern/types/trending_trending_category.py",
        "src/fern/types/trending_trending_detail.py",
        "src/fern/types/trending_trending_entry.py",
        "src/fern/types/trending_trending_entry_community_creation.py",
        "src/fern/types/trending_trending_entry_destiny_activity.py",
        "src/fern/types/trending_trending_entry_destiny_item.py",
        "src/fern/types/trending_trending_entry_destiny_ritual.py",
        "src/fern/types/trending_trending_entry_news.py",
        "src/fern/types/trending_trending_entry_support_article.py",
        "src/fern/types/trending_trending_entry_type.py",
        "src/fern/types/user_cross_save_user_membership.py",
        "src/fern/types/user_e_mail_setting_localization.py",
        "src/fern/types/user_e_mail_setting_subscription_localization.py",
        "src/fern/types/user_email_opt_in_definition.py",
        "src/fern/types/user_email_settings.py",
        "src/fern/types/user_email_subscription_definition.py",
        "src/fern/types/user_email_view_definition.py",
        "src/fern/types/user_email_view_definition_setting.py",
        "src/fern/types/user_exact_search_request.py",
        "src/fern/types/user_general_user.py",
        "src/fern/types/user_hard_linked_user_membership.py",
        "src/fern/types/user_models_get_credential_types_for_account_response.py",
        "src/fern/types/user_opt_in_flags.py",
        "src/fern/types/user_user_info_card.py",
        "src/fern/types/user_user_membership.py",
        "src/fern/types/user_user_membership_data.py",
        "src/fern/types/user_user_search_prefix_request.py",
        "src/fern/types/user_user_search_response.py",
        "src/fern/types/user_user_search_response_detail.py",
        "src/fern/types/user_user_to_user_context.py",
        "src/fern/user/__init__.py",
        "src/fern/user/client.py",
        "src/fern/user/raw_client.py",
        "src/fern/user/types/__init__.py",
        "src/fern/user/types/user_get_available_themes_response.py",
        "src/fern/user/types/user_get_bungie_net_user_by_id_response.py",
        "src/fern/user/types/user_get_credential_types_for_target_account_response.py",
        "src/fern/user/types/user_get_membership_data_by_id_response.py",
        "src/fern/user/types/user_get_membership_data_for_current_user_response.py",
        "src/fern/user/types/user_get_membership_from_hard_linked_credential_response.py",
        "src/fern/user/types/user_get_sanitized_platform_display_names_response.py",
        "src/fern/user/types/user_search_by_global_name_post_response.py",
        "src/fern/user/types/user_search_by_global_name_prefix_response.py",
        "src/fern/version.py",
];

/// `bungie.net`: a real-world `link-ok` corpus API (issue #77) chosen as the
/// schema-heavy counterpart to endpoint-heavy bunq — 869 component schemas across
/// only 13 tags. Fern accepts the raw spec cleanly and crozier consumes it without
/// error; its OpenAPI spec is fetched, not vendored (`corpus_spec`), and crozier
/// now reproduces the committed Fern golden byte-for-byte.
const BUNGIE: Corpus = Corpus {
    api: "bungie.net",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: BUNGIE_MATCHED,
};

// ---------------------------------------------------------------------------
// Five additional real-world `link-ok` corpora (issue #77), added together as a
// batch of harder, feature-diverse targets. Each passes `fern check` cleanly (the
// prerequisite — Fern must accept the raw spec first); their Fern golden `expected/`
// trees are generated with Docker (`just fixtures-generate-corpus --only <name>`)
// and land in the same PR before byte-matching begins. Every `matched` list starts
// empty: the corpus test then only asserts crozier consumes the fetched spec, and
// the list grows (via `just fixtures-candidates`) as the generator is brought to a
// byte-match. Where crozier does not yet consume the spec cleanly, the gap is named
// on the const so the byte-match pass knows the work; the offline `check` gate skips
// every one of these (their specs are fetched, not vendored).
// ---------------------------------------------------------------------------

/// `anchore.io`: the Anchore Engine API server — the largest clean component-schema
/// surface of this batch (149 schemas, heavy `allOf` + enums).
const ANCHORE: Corpus = Corpus {
    api: "anchore.io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/archives/__init__.py",
        "src/fern/archives/client.py",
        "src/fern/archives/raw_client.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/events/__init__.py",
        "src/fern/events/client.py",
        "src/fern/events/raw_client.py",
        "src/fern/identity/__init__.py",
        "src/fern/identity/client.py",
        "src/fern/identity/raw_client.py",
        "src/fern/images/__init__.py",
        "src/fern/images/client.py",
        "src/fern/images/raw_client.py",
        "src/fern/images/types/__init__.py",
        "src/fern/images/types/get_image_vulnerability_types_by_image_id_response_item.py",
        "src/fern/images/types/get_image_vulnerability_types_response_item.py",
        "src/fern/images/types/list_images_request_analysis_status.py",
        "src/fern/images/types/list_images_request_image_status.py",
        "src/fern/import_/__init__.py",
        "src/fern/import_/client.py",
        "src/fern/import_/raw_client.py",
        "src/fern/imports/__init__.py",
        "src/fern/imports/client.py",
        "src/fern/imports/raw_client.py",
        "src/fern/policies/__init__.py",
        "src/fern/policies/client.py",
        "src/fern/policies/raw_client.py",
        "src/fern/py.typed",
        "src/fern/query/__init__.py",
        "src/fern/query/client.py",
        "src/fern/query/raw_client.py",
        "src/fern/query/types/__init__.py",
        "src/fern/query/types/query_images_by_vulnerability_request_severity.py",
        "src/fern/raw_client.py",
        "src/fern/registries/__init__.py",
        "src/fern/registries/client.py",
        "src/fern/registries/raw_client.py",
        "src/fern/repository_credentials/__init__.py",
        "src/fern/repository_credentials/client.py",
        "src/fern/repository_credentials/raw_client.py",
        "src/fern/subscriptions/__init__.py",
        "src/fern/subscriptions/client.py",
        "src/fern/subscriptions/raw_client.py",
        "src/fern/summaries/__init__.py",
        "src/fern/summaries/client.py",
        "src/fern/summaries/raw_client.py",
        "src/fern/summaries/types/__init__.py",
        "src/fern/summaries/types/list_imagetags_request_image_status_item.py",
        "src/fern/system/__init__.py",
        "src/fern/system/client.py",
        "src/fern/system/raw_client.py",
        "src/fern/system/types/__init__.py",
        "src/fern/system/types/test_webhook_request_notification_type.py",
        "src/fern/types/__init__.py",
        "src/fern/types/access_credential.py",
        "src/fern/types/access_credential_type.py",
        "src/fern/types/account.py",
        "src/fern/types/account_list.py",
        "src/fern/types/account_state.py",
        "src/fern/types/account_status.py",
        "src/fern/types/account_status_state.py",
        "src/fern/types/account_type.py",
        "src/fern/types/add_analysis_archive_result.py",
        "src/fern/types/analysis_archive_add_result.py",
        "src/fern/types/analysis_archive_add_result_status.py",
        "src/fern/types/analysis_archive_rules.py",
        "src/fern/types/analysis_archive_rules_summary.py",
        "src/fern/types/analysis_archive_source.py",
        "src/fern/types/analysis_archive_summary.py",
        "src/fern/types/analysis_archive_transition_history.py",
        "src/fern/types/analysis_archive_transition_history_transition.py",
        "src/fern/types/analysis_archive_transition_rule.py",
        "src/fern/types/analysis_archive_transition_rule_exclude.py",
        "src/fern/types/analysis_archive_transition_rule_transition.py",
        "src/fern/types/analysis_update_eval.py",
        "src/fern/types/analysis_update_notification.py",
        "src/fern/types/analysis_update_notification_data.py",
        "src/fern/types/analysis_update_notification_payload.py",
        "src/fern/types/anchore_error_code.py",
        "src/fern/types/anchore_image.py",
        "src/fern/types/anchore_image_analysis_status.py",
        "src/fern/types/anchore_image_image_status.py",
        "src/fern/types/anchore_image_list.py",
        "src/fern/types/anchore_image_tag_summary.py",
        "src/fern/types/anchore_image_tag_summary_list.py",
        "src/fern/types/annotations.py",
        "src/fern/types/api_error_response.py",
        "src/fern/types/archive_summary.py",
        "src/fern/types/archived_analyses.py",
        "src/fern/types/archived_analysis.py",
        "src/fern/types/archived_analysis_status.py",
        "src/fern/types/base_notification_data.py",
        "src/fern/types/content_files_response.py",
        "src/fern/types/content_files_response_content_item.py",
        "src/fern/types/content_java_package_response.py",
        "src/fern/types/content_java_package_response_content_item.py",
        "src/fern/types/content_malware_response.py",
        "src/fern/types/content_package_response.py",
        "src/fern/types/content_package_response_content_item.py",
        "src/fern/types/content_response.py",
        "src/fern/types/credential_list.py",
        "src/fern/types/cvssv2scores.py",
        "src/fern/types/cvssv3scores.py",
        "src/fern/types/delete_image_response.py",
        "src/fern/types/delete_image_response_list.py",
        "src/fern/types/delete_image_response_status.py",
        "src/fern/types/event_category.py",
        "src/fern/types/event_description.py",
        "src/fern/types/event_response.py",
        "src/fern/types/event_response_event.py",
        "src/fern/types/event_response_event_resource.py",
        "src/fern/types/event_response_event_source.py",
        "src/fern/types/event_subcategory.py",
        "src/fern/types/event_types_list.py",
        "src/fern/types/events_list.py",
        "src/fern/types/feed_group_metadata.py",
        "src/fern/types/feed_metadata.py",
        "src/fern/types/feed_sync_result.py",
        "src/fern/types/feed_sync_result_status.py",
        "src/fern/types/feed_sync_results.py",
        "src/fern/types/file_content_search_list.py",
        "src/fern/types/file_content_search_result.py",
        "src/fern/types/gate_spec.py",
        "src/fern/types/gate_spec_state.py",
        "src/fern/types/generic_notification_payload.py",
        "src/fern/types/group_sync_result.py",
        "src/fern/types/group_sync_result_status.py",
        "src/fern/types/image_analysis_references.py",
        "src/fern/types/image_analysis_report.py",
        "src/fern/types/image_content.py",
        "src/fern/types/image_content_delete_response.py",
        "src/fern/types/image_detail.py",
        "src/fern/types/image_filter.py",
        "src/fern/types/image_import_content_response.py",
        "src/fern/types/image_import_manifest.py",
        "src/fern/types/image_import_operation.py",
        "src/fern/types/image_import_operation_status.py",
        "src/fern/types/image_imports.py",
        "src/fern/types/image_ref.py",
        "src/fern/types/image_ref_type.py",
        "src/fern/types/image_reference.py",
        "src/fern/types/image_selection_rule.py",
        "src/fern/types/image_selector.py",
        "src/fern/types/image_source.py",
        "src/fern/types/image_with_packages.py",
        "src/fern/types/import_content_digest_list.py",
        "src/fern/types/import_content_digests.py",
        "src/fern/types/import_descriptor.py",
        "src/fern/types/import_distribution.py",
        "src/fern/types/import_package.py",
        "src/fern/types/import_package_location.py",
        "src/fern/types/import_package_relationship.py",
        "src/fern/types/import_schema.py",
        "src/fern/types/import_source.py",
        "src/fern/types/local_analysis_source.py",
        "src/fern/types/malware_scan.py",
        "src/fern/types/malware_scan_findings_item.py",
        "src/fern/types/mapping_rule.py",
        "src/fern/types/metadata_response.py",
        "src/fern/types/native_sbom.py",
        "src/fern/types/notification_base.py",
        "src/fern/types/nvd_data_list.py",
        "src/fern/types/nvd_data_object.py",
        "src/fern/types/package_reference.py",
        "src/fern/types/paginated_image_list.py",
        "src/fern/types/paginated_vulnerability_list.py",
        "src/fern/types/paginated_vulnerable_image_list.py",
        "src/fern/types/pagination_properties.py",
        "src/fern/types/policy.py",
        "src/fern/types/policy_bundle.py",
        "src/fern/types/policy_bundle_list.py",
        "src/fern/types/policy_bundle_record.py",
        "src/fern/types/policy_eval_notification.py",
        "src/fern/types/policy_eval_notification_data.py",
        "src/fern/types/policy_eval_notification_payload.py",
        "src/fern/types/policy_evaluation.py",
        "src/fern/types/policy_evaluation_list.py",
        "src/fern/types/policy_rule.py",
        "src/fern/types/policy_rule_action.py",
        "src/fern/types/policy_rule_params_item.py",
        "src/fern/types/regex_content_match.py",
        "src/fern/types/registry_configuration.py",
        "src/fern/types/registry_configuration_list.py",
        "src/fern/types/registry_configuration_request.py",
        "src/fern/types/registry_digest_source.py",
        "src/fern/types/registry_tag_source.py",
        "src/fern/types/repository_tag_list.py",
        "src/fern/types/retrieved_file.py",
        "src/fern/types/retrieved_file_list.py",
        "src/fern/types/secret_search_list.py",
        "src/fern/types/secret_search_result.py",
        "src/fern/types/service.py",
        "src/fern/types/service_list.py",
        "src/fern/types/service_version.py",
        "src/fern/types/service_version_api.py",
        "src/fern/types/service_version_db.py",
        "src/fern/types/service_version_service.py",
        "src/fern/types/standalone_vulnerability.py",
        "src/fern/types/standalone_vulnerability_severity.py",
        "src/fern/types/status_response.py",
        "src/fern/types/subscription.py",
        "src/fern/types/subscription_list.py",
        "src/fern/types/system_status_response.py",
        "src/fern/types/tag_entry.py",
        "src/fern/types/tag_update_notification.py",
        "src/fern/types/tag_update_notification_data.py",
        "src/fern/types/tag_update_notification_payload.py",
        "src/fern/types/token_response.py",
        "src/fern/types/trigger_param_spec.py",
        "src/fern/types/trigger_param_spec_state.py",
        "src/fern/types/trigger_spec.py",
        "src/fern/types/trigger_spec_state.py",
        "src/fern/types/user.py",
        "src/fern/types/user_list.py",
        "src/fern/types/user_type.py",
        "src/fern/types/vendor_data_list.py",
        "src/fern/types/vendor_data_object.py",
        "src/fern/types/vuln_diff_result.py",
        "src/fern/types/vuln_update_notification.py",
        "src/fern/types/vuln_update_notification_data.py",
        "src/fern/types/vuln_update_notification_payload.py",
        "src/fern/types/vulnerability.py",
        "src/fern/types/vulnerability_list.py",
        "src/fern/types/vulnerability_reference.py",
        "src/fern/types/vulnerability_response.py",
        "src/fern/types/vulnerable_image.py",
        "src/fern/types/vulnerable_package_reference.py",
        "src/fern/types/whitelist.py",
        "src/fern/types/whitelist_item.py",
        "src/fern/user_management/__init__.py",
        "src/fern/user_management/client.py",
        "src/fern/user_management/raw_client.py",
        "src/fern/user_management/types/__init__.py",
        "src/fern/user_management/types/delete_user_credential_request_credential_type.py",
        "src/fern/user_management/types/list_accounts_request_state.py",
        "src/fern/version.py",
    ],
};

/// `apache.org`: the Airflow (Stable) REST API — the heaviest composition of this
/// batch (`allOf`×22 plus the only discriminated union) across 18 tags, so the
/// deepest sub-client fan-out. Fully matched: all 182 files reproduce Fern
/// byte-for-byte.
const APACHE_AIRFLOW: Corpus = Corpus {
    api: "apache.org",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/config/__init__.py",
        "src/fern/config/client.py",
        "src/fern/config/raw_client.py",
        "src/fern/connection/__init__.py",
        "src/fern/connection/client.py",
        "src/fern/connection/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/dag/__init__.py",
        "src/fern/dag/client.py",
        "src/fern/dag/raw_client.py",
        "src/fern/dag/types/__init__.py",
        "src/fern/dag/types/get_dag_source_response.py",
        "src/fern/dag/types/update_task_instances_state_new_state.py",
        "src/fern/dag_run/__init__.py",
        "src/fern/dag_run/client.py",
        "src/fern/dag_run/raw_client.py",
        "src/fern/dag_run/types/__init__.py",
        "src/fern/dag_run/types/update_dag_run_state_state.py",
        "src/fern/dag_warning/__init__.py",
        "src/fern/dag_warning/client.py",
        "src/fern/dag_warning/raw_client.py",
        "src/fern/dataset/__init__.py",
        "src/fern/dataset/client.py",
        "src/fern/dataset/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/not_acceptable_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/event_log/__init__.py",
        "src/fern/event_log/client.py",
        "src/fern/event_log/raw_client.py",
        "src/fern/import_error/__init__.py",
        "src/fern/import_error/client.py",
        "src/fern/import_error/raw_client.py",
        "src/fern/monitoring/__init__.py",
        "src/fern/monitoring/client.py",
        "src/fern/monitoring/raw_client.py",
        "src/fern/permission/__init__.py",
        "src/fern/permission/client.py",
        "src/fern/permission/raw_client.py",
        "src/fern/plugin/__init__.py",
        "src/fern/plugin/client.py",
        "src/fern/plugin/raw_client.py",
        "src/fern/pool/__init__.py",
        "src/fern/pool/client.py",
        "src/fern/pool/raw_client.py",
        "src/fern/provider/__init__.py",
        "src/fern/provider/client.py",
        "src/fern/provider/raw_client.py",
        "src/fern/provider/types/__init__.py",
        "src/fern/provider/types/get_providers_response.py",
        "src/fern/py.typed",
        "src/fern/role/__init__.py",
        "src/fern/role/client.py",
        "src/fern/role/raw_client.py",
        "src/fern/task_instance/__init__.py",
        "src/fern/task_instance/client.py",
        "src/fern/task_instance/raw_client.py",
        "src/fern/task_instance/types/__init__.py",
        "src/fern/task_instance/types/get_log_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/action.py",
        "src/fern/types/action_collection.py",
        "src/fern/types/action_resource.py",
        "src/fern/types/basic_dag_run.py",
        "src/fern/types/class_reference.py",
        "src/fern/types/collection_info.py",
        "src/fern/types/color.py",
        "src/fern/types/config.py",
        "src/fern/types/config_option.py",
        "src/fern/types/config_section.py",
        "src/fern/types/connection.py",
        "src/fern/types/connection_collection.py",
        "src/fern/types/connection_collection_item.py",
        "src/fern/types/connection_test.py",
        "src/fern/types/cron_expression.py",
        "src/fern/types/dag.py",
        "src/fern/types/dag_collection.py",
        "src/fern/types/dag_detail.py",
        "src/fern/types/dag_run.py",
        "src/fern/types/dag_run_collection.py",
        "src/fern/types/dag_run_run_type.py",
        "src/fern/types/dag_schedule_dataset_reference.py",
        "src/fern/types/dag_state.py",
        "src/fern/types/dag_warning.py",
        "src/fern/types/dag_warning_collection.py",
        "src/fern/types/dataset.py",
        "src/fern/types/dataset_collection.py",
        "src/fern/types/dataset_event.py",
        "src/fern/types/dataset_event_collection.py",
        "src/fern/types/error.py",
        "src/fern/types/event_log.py",
        "src/fern/types/event_log_collection.py",
        "src/fern/types/extra_link.py",
        "src/fern/types/extra_link_collection.py",
        "src/fern/types/health_info.py",
        "src/fern/types/health_status.py",
        "src/fern/types/import_error.py",
        "src/fern/types/import_error_collection.py",
        "src/fern/types/job.py",
        "src/fern/types/metadatabase_status.py",
        "src/fern/types/plugin_collection.py",
        "src/fern/types/plugin_collection_item.py",
        "src/fern/types/pool.py",
        "src/fern/types/pool_collection.py",
        "src/fern/types/provider.py",
        "src/fern/types/provider_collection.py",
        "src/fern/types/relative_delta.py",
        "src/fern/types/resource.py",
        "src/fern/types/role.py",
        "src/fern/types/role_collection.py",
        "src/fern/types/schedule_interval.py",
        "src/fern/types/scheduler_status.py",
        "src/fern/types/set_task_instance_note.py",
        "src/fern/types/sla_miss.py",
        "src/fern/types/tag.py",
        "src/fern/types/task.py",
        "src/fern/types/task_collection.py",
        "src/fern/types/task_extra_links_item.py",
        "src/fern/types/task_instance.py",
        "src/fern/types/task_instance_collection.py",
        "src/fern/types/task_instance_reference.py",
        "src/fern/types/task_instance_reference_collection.py",
        "src/fern/types/task_outlet_dataset_reference.py",
        "src/fern/types/task_state.py",
        "src/fern/types/time_delta.py",
        "src/fern/types/timezone.py",
        "src/fern/types/trigger.py",
        "src/fern/types/trigger_rule.py",
        "src/fern/types/update_task_instance.py",
        "src/fern/types/update_task_instance_new_state.py",
        "src/fern/types/user.py",
        "src/fern/types/user_collection.py",
        "src/fern/types/user_collection_item.py",
        "src/fern/types/user_collection_item_roles_item.py",
        "src/fern/types/variable.py",
        "src/fern/types/variable_collection.py",
        "src/fern/types/variable_collection_item.py",
        "src/fern/types/version_info.py",
        "src/fern/types/weight_rule.py",
        "src/fern/types/x_com.py",
        "src/fern/types/x_com_collection.py",
        "src/fern/types/x_com_collection_item.py",
        "src/fern/user/__init__.py",
        "src/fern/user/client.py",
        "src/fern/user/raw_client.py",
        "src/fern/variable/__init__.py",
        "src/fern/variable/client.py",
        "src/fern/variable/raw_client.py",
        "src/fern/version.py",
        "src/fern/x_com/__init__.py",
        "src/fern/x_com/client.py",
        "src/fern/x_com/raw_client.py",
    ],
};

/// `discourse.local`: the Discourse API — an all-inline shape (0 named component
/// schemas; ~113 inline request/response objects Fern must coin names for), unlike
/// any matched corpus. Fully matched: all 328 files reproduce Fern byte-for-byte.
const DISCOURSE: Corpus = Corpus {
    api: "discourse.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/backups/__init__.py",
        "src/fern/backups/client.py",
        "src/fern/backups/raw_client.py",
        "src/fern/backups/types/__init__.py",
        "src/fern/backups/types/create_backup_response.py",
        "src/fern/backups/types/get_backups_response_item.py",
        "src/fern/badges/__init__.py",
        "src/fern/badges/client.py",
        "src/fern/badges/raw_client.py",
        "src/fern/badges/types/__init__.py",
        "src/fern/badges/types/admin_list_badges_response.py",
        "src/fern/badges/types/admin_list_badges_response_admin_badges.py",
        "src/fern/badges/types/admin_list_badges_response_admin_badges_triggers.py",
        "src/fern/badges/types/admin_list_badges_response_badge_groupings_item.py",
        "src/fern/badges/types/admin_list_badges_response_badge_types_item.py",
        "src/fern/badges/types/admin_list_badges_response_badges_item.py",
        "src/fern/badges/types/create_badge_response.py",
        "src/fern/badges/types/create_badge_response_badge.py",
        "src/fern/badges/types/create_badge_response_badge_types_item.py",
        "src/fern/badges/types/list_user_badges_response.py",
        "src/fern/badges/types/list_user_badges_response_badge_types_item.py",
        "src/fern/badges/types/list_user_badges_response_badges_item.py",
        "src/fern/badges/types/list_user_badges_response_granted_bies_item.py",
        "src/fern/badges/types/list_user_badges_response_user_badges_item.py",
        "src/fern/badges/types/update_badge_response.py",
        "src/fern/badges/types/update_badge_response_badge.py",
        "src/fern/badges/types/update_badge_response_badge_types_item.py",
        "src/fern/categories/__init__.py",
        "src/fern/categories/client.py",
        "src/fern/categories/raw_client.py",
        "src/fern/categories/types/__init__.py",
        "src/fern/categories/types/create_category_request_permissions.py",
        "src/fern/categories/types/create_category_response.py",
        "src/fern/categories/types/create_category_response_category.py",
        "src/fern/categories/types/create_category_response_category_custom_fields.py",
        "src/fern/categories/types/create_category_response_category_group_permissions_item.py",
        "src/fern/categories/types/create_category_response_category_required_tag_groups_item.py",
        "src/fern/categories/types/get_category_response.py",
        "src/fern/categories/types/get_category_response_category.py",
        "src/fern/categories/types/get_category_response_category_custom_fields.py",
        "src/fern/categories/types/get_category_response_category_group_permissions_item.py",
        "src/fern/categories/types/get_category_response_category_required_tag_groups_item.py",
        "src/fern/categories/types/list_categories_response.py",
        "src/fern/categories/types/list_categories_response_category_list.py",
        "src/fern/categories/types/list_categories_response_category_list_categories_item.py",
        "src/fern/categories/types/list_category_topics_response.py",
        "src/fern/categories/types/list_category_topics_response_topic_list.py",
        "src/fern/categories/types/list_category_topics_response_topic_list_topics_item.py",
        "src/fern/categories/types/list_category_topics_response_topic_list_topics_item_posters_item.py",
        "src/fern/categories/types/list_category_topics_response_users_item.py",
        "src/fern/categories/types/update_category_request_permissions.py",
        "src/fern/categories/types/update_category_response.py",
        "src/fern/categories/types/update_category_response_category.py",
        "src/fern/categories/types/update_category_response_category_custom_fields.py",
        "src/fern/categories/types/update_category_response_category_group_permissions_item.py",
        "src/fern/categories/types/update_category_response_category_required_tag_groups_item.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/groups/__init__.py",
        "src/fern/groups/client.py",
        "src/fern/groups/raw_client.py",
        "src/fern/groups/types/__init__.py",
        "src/fern/groups/types/add_group_members_response.py",
        "src/fern/groups/types/create_group_request_group.py",
        "src/fern/groups/types/create_group_response.py",
        "src/fern/groups/types/create_group_response_basic_group.py",
        "src/fern/groups/types/delete_group_response.py",
        "src/fern/groups/types/get_group_response.py",
        "src/fern/groups/types/get_group_response_extras.py",
        "src/fern/groups/types/get_group_response_group.py",
        "src/fern/groups/types/list_group_members_response.py",
        "src/fern/groups/types/list_group_members_response_members_item.py",
        "src/fern/groups/types/list_group_members_response_meta.py",
        "src/fern/groups/types/list_group_members_response_owners_item.py",
        "src/fern/groups/types/list_groups_response.py",
        "src/fern/groups/types/list_groups_response_extras.py",
        "src/fern/groups/types/list_groups_response_groups_item.py",
        "src/fern/groups/types/remove_group_members_response.py",
        "src/fern/groups/types/update_group_request_group.py",
        "src/fern/groups/types/update_group_response.py",
        "src/fern/invites/__init__.py",
        "src/fern/invites/client.py",
        "src/fern/invites/raw_client.py",
        "src/fern/invites/types/__init__.py",
        "src/fern/invites/types/create_invite_response.py",
        "src/fern/notifications/__init__.py",
        "src/fern/notifications/client.py",
        "src/fern/notifications/raw_client.py",
        "src/fern/notifications/types/__init__.py",
        "src/fern/notifications/types/get_notifications_response.py",
        "src/fern/notifications/types/get_notifications_response_notifications_item.py",
        "src/fern/notifications/types/get_notifications_response_notifications_item_data.py",
        "src/fern/notifications/types/mark_notifications_as_read_response.py",
        "src/fern/posts/__init__.py",
        "src/fern/posts/client.py",
        "src/fern/posts/raw_client.py",
        "src/fern/posts/types/__init__.py",
        "src/fern/posts/types/create_topic_post_pm_response.py",
        "src/fern/posts/types/create_topic_post_pm_response_actions_summary_item.py",
        "src/fern/posts/types/get_post_response.py",
        "src/fern/posts/types/get_post_response_actions_summary_item.py",
        "src/fern/posts/types/list_posts_response.py",
        "src/fern/posts/types/list_posts_response_latest_posts_item.py",
        "src/fern/posts/types/list_posts_response_latest_posts_item_actions_summary_item.py",
        "src/fern/posts/types/lock_post_response.py",
        "src/fern/posts/types/perform_post_action_response.py",
        "src/fern/posts/types/perform_post_action_response_actions_summary_item.py",
        "src/fern/posts/types/post_replies_response_item.py",
        "src/fern/posts/types/post_replies_response_item_actions_summary_item.py",
        "src/fern/posts/types/post_replies_response_item_reply_to_user.py",
        "src/fern/posts/types/update_post_request_post.py",
        "src/fern/posts/types/update_post_response.py",
        "src/fern/posts/types/update_post_response_post.py",
        "src/fern/posts/types/update_post_response_post_actions_summary_item.py",
        "src/fern/private_messages/__init__.py",
        "src/fern/private_messages/client.py",
        "src/fern/private_messages/raw_client.py",
        "src/fern/private_messages/types/__init__.py",
        "src/fern/private_messages/types/get_user_sent_private_messages_response.py",
        "src/fern/private_messages/types/get_user_sent_private_messages_response_topic_list.py",
        "src/fern/private_messages/types/get_user_sent_private_messages_response_topic_list_topics_item.py",
        "src/fern/private_messages/types/get_user_sent_private_messages_response_topic_list_topics_item_posters_item.py",
        "src/fern/private_messages/types/get_user_sent_private_messages_response_users_item.py",
        "src/fern/private_messages/types/list_user_private_messages_response.py",
        "src/fern/private_messages/types/list_user_private_messages_response_topic_list.py",
        "src/fern/private_messages/types/list_user_private_messages_response_topic_list_topics_item.py",
        "src/fern/private_messages/types/list_user_private_messages_response_topic_list_topics_item_participants_item.py",
        "src/fern/private_messages/types/list_user_private_messages_response_topic_list_topics_item_posters_item.py",
        "src/fern/private_messages/types/list_user_private_messages_response_users_item.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/site/__init__.py",
        "src/fern/site/client.py",
        "src/fern/site/raw_client.py",
        "src/fern/site/types/__init__.py",
        "src/fern/site/types/get_site_response.py",
        "src/fern/site/types/get_site_response_archetypes_item.py",
        "src/fern/site/types/get_site_response_categories_item.py",
        "src/fern/site/types/get_site_response_categories_item_required_tag_groups_item.py",
        "src/fern/site/types/get_site_response_custom_emoji_translation.py",
        "src/fern/site/types/get_site_response_groups_item.py",
        "src/fern/site/types/get_site_response_notification_types.py",
        "src/fern/site/types/get_site_response_post_action_types_item.py",
        "src/fern/site/types/get_site_response_post_types.py",
        "src/fern/site/types/get_site_response_topic_flag_types_item.py",
        "src/fern/site/types/get_site_response_trust_levels.py",
        "src/fern/site/types/get_site_response_user_color_schemes_item.py",
        "src/fern/site/types/get_site_response_user_themes_item.py",
        "src/fern/tags/__init__.py",
        "src/fern/tags/client.py",
        "src/fern/tags/raw_client.py",
        "src/fern/tags/types/__init__.py",
        "src/fern/tags/types/create_tag_group_response.py",
        "src/fern/tags/types/create_tag_group_response_tag_group.py",
        "src/fern/tags/types/get_tag_group_response.py",
        "src/fern/tags/types/get_tag_group_response_tag_group.py",
        "src/fern/tags/types/get_tag_group_response_tag_group_permissions.py",
        "src/fern/tags/types/get_tag_response.py",
        "src/fern/tags/types/get_tag_response_topic_list.py",
        "src/fern/tags/types/get_tag_response_topic_list_tags_item.py",
        "src/fern/tags/types/get_tag_response_topic_list_topics_item.py",
        "src/fern/tags/types/get_tag_response_topic_list_topics_item_posters_item.py",
        "src/fern/tags/types/get_tag_response_users_item.py",
        "src/fern/tags/types/list_tag_groups_response.py",
        "src/fern/tags/types/list_tag_groups_response_tag_groups_item.py",
        "src/fern/tags/types/list_tag_groups_response_tag_groups_item_permissions.py",
        "src/fern/tags/types/list_tags_response.py",
        "src/fern/tags/types/list_tags_response_extras.py",
        "src/fern/tags/types/list_tags_response_tags_item.py",
        "src/fern/tags/types/update_tag_group_response.py",
        "src/fern/tags/types/update_tag_group_response_tag_group.py",
        "src/fern/tags/types/update_tag_group_response_tag_group_permissions.py",
        "src/fern/topics/__init__.py",
        "src/fern/topics/client.py",
        "src/fern/topics/raw_client.py",
        "src/fern/topics/types/__init__.py",
        "src/fern/topics/types/create_topic_timer_response.py",
        "src/fern/topics/types/get_specific_posts_from_topic_response.py",
        "src/fern/topics/types/get_specific_posts_from_topic_response_post_stream.py",
        "src/fern/topics/types/get_specific_posts_from_topic_response_post_stream_posts_item.py",
        "src/fern/topics/types/get_specific_posts_from_topic_response_post_stream_posts_item_actions_summary_item.py",
        "src/fern/topics/types/get_topic_response.py",
        "src/fern/topics/types/get_topic_response_actions_summary_item.py",
        "src/fern/topics/types/get_topic_response_details.py",
        "src/fern/topics/types/get_topic_response_details_created_by.py",
        "src/fern/topics/types/get_topic_response_details_last_poster.py",
        "src/fern/topics/types/get_topic_response_details_participants_item.py",
        "src/fern/topics/types/get_topic_response_post_stream.py",
        "src/fern/topics/types/get_topic_response_post_stream_posts_item.py",
        "src/fern/topics/types/get_topic_response_post_stream_posts_item_actions_summary_item.py",
        "src/fern/topics/types/get_topic_response_post_stream_posts_item_link_counts_item.py",
        "src/fern/topics/types/get_topic_response_suggested_topics_item.py",
        "src/fern/topics/types/get_topic_response_suggested_topics_item_posters_item.py",
        "src/fern/topics/types/get_topic_response_suggested_topics_item_posters_item_user.py",
        "src/fern/topics/types/get_topic_response_suggested_topics_item_tags_descriptions.py",
        "src/fern/topics/types/get_topic_response_tags_descriptions.py",
        "src/fern/topics/types/invite_to_topic_response.py",
        "src/fern/topics/types/invite_to_topic_response_user.py",
        "src/fern/topics/types/list_latest_topics_response.py",
        "src/fern/topics/types/list_latest_topics_response_topic_list.py",
        "src/fern/topics/types/list_latest_topics_response_topic_list_topics_item.py",
        "src/fern/topics/types/list_latest_topics_response_topic_list_topics_item_posters_item.py",
        "src/fern/topics/types/list_latest_topics_response_users_item.py",
        "src/fern/topics/types/list_top_topics_response.py",
        "src/fern/topics/types/list_top_topics_response_topic_list.py",
        "src/fern/topics/types/list_top_topics_response_topic_list_topics_item.py",
        "src/fern/topics/types/list_top_topics_response_topic_list_topics_item_posters_item.py",
        "src/fern/topics/types/list_top_topics_response_users_item.py",
        "src/fern/topics/types/set_notification_level_request_notification_level.py",
        "src/fern/topics/types/set_notification_level_response.py",
        "src/fern/topics/types/update_topic_request_topic.py",
        "src/fern/topics/types/update_topic_response.py",
        "src/fern/topics/types/update_topic_response_basic_topic.py",
        "src/fern/topics/types/update_topic_status_request_enabled.py",
        "src/fern/topics/types/update_topic_status_request_status.py",
        "src/fern/topics/types/update_topic_status_response.py",
        "src/fern/topics/types/update_topic_timestamp_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/search_response.py",
        "src/fern/types/search_response_grouped_search_result.py",
        "src/fern/uploads/__init__.py",
        "src/fern/uploads/client.py",
        "src/fern/uploads/raw_client.py",
        "src/fern/uploads/types/__init__.py",
        "src/fern/uploads/types/abort_multipart_response.py",
        "src/fern/uploads/types/batch_presign_multipart_parts_response.py",
        "src/fern/uploads/types/complete_external_upload_response.py",
        "src/fern/uploads/types/complete_multipart_response.py",
        "src/fern/uploads/types/create_multipart_upload_request_metadata.py",
        "src/fern/uploads/types/create_multipart_upload_request_upload_type.py",
        "src/fern/uploads/types/create_multipart_upload_response.py",
        "src/fern/uploads/types/create_upload_request_type.py",
        "src/fern/uploads/types/create_upload_response.py",
        "src/fern/uploads/types/generate_presigned_put_request_metadata.py",
        "src/fern/uploads/types/generate_presigned_put_request_type.py",
        "src/fern/uploads/types/generate_presigned_put_response.py",
        "src/fern/users/__init__.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/users/types/__init__.py",
        "src/fern/users/types/admin_get_user_response.py",
        "src/fern/users/types/admin_get_user_response_approved_by.py",
        "src/fern/users/types/admin_get_user_response_groups_item.py",
        "src/fern/users/types/admin_get_user_response_penalty_counts.py",
        "src/fern/users/types/admin_get_user_response_tl3requirements.py",
        "src/fern/users/types/admin_get_user_response_tl3requirements_penalty_counts.py",
        "src/fern/users/types/admin_list_users_request_asc.py",
        "src/fern/users/types/admin_list_users_request_flag.py",
        "src/fern/users/types/admin_list_users_request_order.py",
        "src/fern/users/types/admin_list_users_response_item.py",
        "src/fern/users/types/anonymize_user_response.py",
        "src/fern/users/types/create_user_response.py",
        "src/fern/users/types/delete_user_response.py",
        "src/fern/users/types/get_user_emails_response.py",
        "src/fern/users/types/get_user_external_id_response.py",
        "src/fern/users/types/get_user_external_id_response_user.py",
        "src/fern/users/types/get_user_external_id_response_user_custom_fields.py",
        "src/fern/users/types/get_user_external_id_response_user_group_users_item.py",
        "src/fern/users/types/get_user_external_id_response_user_groups_item.py",
        "src/fern/users/types/get_user_external_id_response_user_user_auth_tokens_item.py",
        "src/fern/users/types/get_user_external_id_response_user_user_fields.py",
        "src/fern/users/types/get_user_external_id_response_user_user_notification_schedule.py",
        "src/fern/users/types/get_user_external_id_response_user_user_option.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_custom_fields.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_group_users_item.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_groups_item.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_user_auth_tokens_item.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_user_fields.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_user_notification_schedule.py",
        "src/fern/users/types/get_user_identiy_provider_external_id_response_user_user_option.py",
        "src/fern/users/types/get_user_response.py",
        "src/fern/users/types/get_user_response_user.py",
        "src/fern/users/types/get_user_response_user_custom_fields.py",
        "src/fern/users/types/get_user_response_user_group_users_item.py",
        "src/fern/users/types/get_user_response_user_groups_item.py",
        "src/fern/users/types/get_user_response_user_user_auth_tokens_item.py",
        "src/fern/users/types/get_user_response_user_user_fields.py",
        "src/fern/users/types/get_user_response_user_user_notification_schedule.py",
        "src/fern/users/types/get_user_response_user_user_option.py",
        "src/fern/users/types/list_user_actions_response.py",
        "src/fern/users/types/list_user_actions_response_user_actions_item.py",
        "src/fern/users/types/list_users_public_request_asc.py",
        "src/fern/users/types/list_users_public_request_order.py",
        "src/fern/users/types/list_users_public_request_period.py",
        "src/fern/users/types/list_users_public_response.py",
        "src/fern/users/types/list_users_public_response_directory_items_item.py",
        "src/fern/users/types/list_users_public_response_directory_items_item_user.py",
        "src/fern/users/types/list_users_public_response_meta.py",
        "src/fern/users/types/log_out_user_response.py",
        "src/fern/users/types/refresh_gravatar_response.py",
        "src/fern/users/types/send_password_reset_email_response.py",
        "src/fern/users/types/silence_user_response.py",
        "src/fern/users/types/silence_user_response_silence.py",
        "src/fern/users/types/silence_user_response_silence_silenced_by.py",
        "src/fern/users/types/suspend_user_response.py",
        "src/fern/users/types/suspend_user_response_suspension.py",
        "src/fern/users/types/suspend_user_response_suspension_suspended_by.py",
        "src/fern/users/types/update_avatar_request_type.py",
        "src/fern/users/types/update_avatar_response.py",
        "src/fern/users/types/update_user_response.py",
        "src/fern/version.py",
    ],
};

/// `appwrite.io-server`: the Appwrite server API — the widest operation surface of
/// this batch (95 operations) with `url`-format fields. Fully matched: all 97
/// files reproduce Fern byte-for-byte.
const APPWRITE_SERVER: Corpus = Corpus {
    api: "appwrite.io-server",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/account/__init__.py",
        "src/fern/account/client.py",
        "src/fern/account/raw_client.py",
        "src/fern/avatars/__init__.py",
        "src/fern/avatars/client.py",
        "src/fern/avatars/raw_client.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/database/__init__.py",
        "src/fern/database/client.py",
        "src/fern/database/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/functions/__init__.py",
        "src/fern/functions/client.py",
        "src/fern/functions/raw_client.py",
        "src/fern/health/__init__.py",
        "src/fern/health/client.py",
        "src/fern/health/raw_client.py",
        "src/fern/locale/__init__.py",
        "src/fern/locale/client.py",
        "src/fern/locale/raw_client.py",
        "src/fern/py.typed",
        "src/fern/storage/__init__.py",
        "src/fern/storage/client.py",
        "src/fern/storage/raw_client.py",
        "src/fern/teams/__init__.py",
        "src/fern/teams/client.py",
        "src/fern/teams/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/collection.py",
        "src/fern/types/collection_list.py",
        "src/fern/types/continent.py",
        "src/fern/types/continent_list.py",
        "src/fern/types/country.py",
        "src/fern/types/country_list.py",
        "src/fern/types/currency.py",
        "src/fern/types/currency_list.py",
        "src/fern/types/document.py",
        "src/fern/types/document_list.py",
        "src/fern/types/error.py",
        "src/fern/types/execution.py",
        "src/fern/types/execution_list.py",
        "src/fern/types/file.py",
        "src/fern/types/file_list.py",
        "src/fern/types/function.py",
        "src/fern/types/function_list.py",
        "src/fern/types/language.py",
        "src/fern/types/language_list.py",
        "src/fern/types/locale.py",
        "src/fern/types/log.py",
        "src/fern/types/log_list.py",
        "src/fern/types/membership.py",
        "src/fern/types/membership_list.py",
        "src/fern/types/permissions.py",
        "src/fern/types/phone.py",
        "src/fern/types/phone_list.py",
        "src/fern/types/preferences.py",
        "src/fern/types/rule.py",
        "src/fern/types/session.py",
        "src/fern/types/session_list.py",
        "src/fern/types/tag.py",
        "src/fern/types/tag_list.py",
        "src/fern/types/team.py",
        "src/fern/types/team_list.py",
        "src/fern/types/token.py",
        "src/fern/types/user.py",
        "src/fern/types/user_list.py",
        "src/fern/users/__init__.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/version.py",
    ],
};

/// `apicurio.local-registry`: the Apicurio Registry API — the only `int64`-format
/// corpus of this batch. All committed Fern output is byte-matched.
const APICURIO: Corpus = Corpus {
    api: "apicurio.local-registry",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/admin/__init__.py",
        "src/fern/admin/client.py",
        "src/fern/admin/raw_client.py",
        "src/fern/artifact_rules/__init__.py",
        "src/fern/artifact_rules/client.py",
        "src/fern/artifact_rules/raw_client.py",
        "src/fern/artifact_rules/types/__init__.py",
        "src/fern/artifact_rules/types/delete_artifact_rule_request_rule.py",
        "src/fern/artifact_rules/types/get_artifact_rule_config_request_rule.py",
        "src/fern/artifact_rules/types/update_artifact_rule_config_request_rule.py",
        "src/fern/artifact_type/__init__.py",
        "src/fern/artifact_type/client.py",
        "src/fern/artifact_type/raw_client.py",
        "src/fern/artifacts/__init__.py",
        "src/fern/artifacts/client.py",
        "src/fern/artifacts/raw_client.py",
        "src/fern/artifacts/types/__init__.py",
        "src/fern/artifacts/types/create_artifact_request_x_registry_hash_algorithm.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/global_rules/__init__.py",
        "src/fern/global_rules/client.py",
        "src/fern/global_rules/raw_client.py",
        "src/fern/groups/__init__.py",
        "src/fern/groups/client.py",
        "src/fern/groups/raw_client.py",
        "src/fern/metadata/__init__.py",
        "src/fern/metadata/client.py",
        "src/fern/metadata/raw_client.py",
        "src/fern/py.typed",
        "src/fern/search/__init__.py",
        "src/fern/search/client.py",
        "src/fern/search/raw_client.py",
        "src/fern/search/types/__init__.py",
        "src/fern/search/types/search_artifacts_by_content_request_order.py",
        "src/fern/search/types/search_artifacts_by_content_request_orderby.py",
        "src/fern/system/__init__.py",
        "src/fern/system/client.py",
        "src/fern/system/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/artifact_description.py",
        "src/fern/types/artifact_id.py",
        "src/fern/types/artifact_meta_data.py",
        "src/fern/types/artifact_name.py",
        "src/fern/types/artifact_owner.py",
        "src/fern/types/artifact_reference.py",
        "src/fern/types/artifact_search_results.py",
        "src/fern/types/artifact_state.py",
        "src/fern/types/artifact_type.py",
        "src/fern/types/artifact_type_info.py",
        "src/fern/types/configuration_property.py",
        "src/fern/types/content_create_request.py",
        "src/fern/types/download_ref.py",
        "src/fern/types/editable_meta_data.py",
        "src/fern/types/encoded_artifact_description.py",
        "src/fern/types/encoded_artifact_name.py",
        "src/fern/types/error.py",
        "src/fern/types/file_content.py",
        "src/fern/types/group_id.py",
        "src/fern/types/group_meta_data.py",
        "src/fern/types/group_search_results.py",
        "src/fern/types/if_exists.py",
        "src/fern/types/limits.py",
        "src/fern/types/log_configuration.py",
        "src/fern/types/log_level.py",
        "src/fern/types/named_log_configuration.py",
        "src/fern/types/properties.py",
        "src/fern/types/role_mapping.py",
        "src/fern/types/role_type.py",
        "src/fern/types/rule.py",
        "src/fern/types/rule_type.py",
        "src/fern/types/rule_violation_cause.py",
        "src/fern/types/rule_violation_error.py",
        "src/fern/types/searched_artifact.py",
        "src/fern/types/searched_group.py",
        "src/fern/types/searched_version.py",
        "src/fern/types/sort_by.py",
        "src/fern/types/sort_order.py",
        "src/fern/types/system_info.py",
        "src/fern/types/update_state.py",
        "src/fern/types/user_info.py",
        "src/fern/types/version.py",
        "src/fern/types/version_meta_data.py",
        "src/fern/types/version_search_results.py",
        "src/fern/users/__init__.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/version.py",
        "src/fern/versions/__init__.py",
        "src/fern/versions/client.py",
        "src/fern/versions/raw_client.py",
    ],
};

/// `gambitcomm.local-mimic`: the Gambit Communications MIMIC REST API. Its large
/// operation surface exercises keyword-safe method naming and free-form maps.
const GAMBITCOMM_MIMIC: Corpus = Corpus {
    api: "gambitcomm.local-mimic",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/access/__init__.py",
        "src/fern/access/client.py",
        "src/fern/access/raw_client.py",
        "src/fern/agent/__init__.py",
        "src/fern/agent/client.py",
        "src/fern/agent/raw_client.py",
        "src/fern/client.py",
        "src/fern/coap/__init__.py",
        "src/fern/coap/client.py",
        "src/fern/coap/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/daemon/__init__.py",
        "src/fern/daemon/client.py",
        "src/fern/daemon/raw_client.py",
        "src/fern/dhcp/__init__.py",
        "src/fern/dhcp/client.py",
        "src/fern/dhcp/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/ipmi/__init__.py",
        "src/fern/ipmi/client.py",
        "src/fern/ipmi/raw_client.py",
        "src/fern/mqtt/__init__.py",
        "src/fern/mqtt/client.py",
        "src/fern/mqtt/raw_client.py",
        "src/fern/netflow/__init__.py",
        "src/fern/netflow/client.py",
        "src/fern/netflow/raw_client.py",
        "src/fern/proxy/__init__.py",
        "src/fern/proxy/client.py",
        "src/fern/proxy/raw_client.py",
        "src/fern/py.typed",
        "src/fern/sflow/__init__.py",
        "src/fern/sflow/client.py",
        "src/fern/sflow/raw_client.py",
        "src/fern/snm_pv3/__init__.py",
        "src/fern/snm_pv3/client.py",
        "src/fern/snm_pv3/raw_client.py",
        "src/fern/snmptcp/__init__.py",
        "src/fern/snmptcp/client.py",
        "src/fern/snmptcp/raw_client.py",
        "src/fern/ssh/__init__.py",
        "src/fern/ssh/client.py",
        "src/fern/ssh/raw_client.py",
        "src/fern/syslog/__init__.py",
        "src/fern/syslog/client.py",
        "src/fern/syslog/raw_client.py",
        "src/fern/telnet/__init__.py",
        "src/fern/telnet/client.py",
        "src/fern/telnet/raw_client.py",
        "src/fern/tftp/__init__.py",
        "src/fern/tftp/client.py",
        "src/fern/tftp/raw_client.py",
        "src/fern/tod/__init__.py",
        "src/fern/tod/client.py",
        "src/fern/tod/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/access_entry.py",
        "src/fern/types/agent_state.py",
        "src/fern/types/config_coap.py",
        "src/fern/types/config_dhcp.py",
        "src/fern/types/config_ipmi.py",
        "src/fern/types/config_mqtt.py",
        "src/fern/types/config_netflow.py",
        "src/fern/types/config_proxy.py",
        "src/fern/types/config_sflow.py",
        "src/fern/types/config_snm_pv3.py",
        "src/fern/types/config_snmptcp.py",
        "src/fern/types/config_ssh.py",
        "src/fern/types/config_syslog.py",
        "src/fern/types/config_telnet.py",
        "src/fern/types/config_tftp.py",
        "src/fern/types/config_tod.py",
        "src/fern/types/config_web.py",
        "src/fern/types/ip_alias.py",
        "src/fern/types/ip_source.py",
        "src/fern/types/telnet_user.py",
        "src/fern/types/timer_script.py",
        "src/fern/types/trap_dest.py",
        "src/fern/types/triplet.py",
        "src/fern/valuespace/__init__.py",
        "src/fern/valuespace/client.py",
        "src/fern/valuespace/raw_client.py",
        "src/fern/version.py",
        "src/fern/web/__init__.py",
        "src/fern/web/client.py",
        "src/fern/web/raw_client.py",
    ],
};

const DND5EAPI: Corpus = Corpus {
    api: "dnd5eapi.co",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/character_data/__init__.py",
        "src/fern/character_data/client.py",
        "src/fern/character_data/raw_client.py",
        "src/fern/character_data/types/__init__.py",
        "src/fern/character_data/types/get_api_ability_scores_index_request_index.py",
        "src/fern/character_data/types/get_api_alignments_index_request_index.py",
        "src/fern/character_data/types/get_api_backgrounds_index_request_index.py",
        "src/fern/character_data/types/get_api_languages_index_request_index.py",
        "src/fern/character_data/types/get_api_skills_index_request_index.py",
        "src/fern/class_/__init__.py",
        "src/fern/class_/client.py",
        "src/fern/class_/raw_client.py",
        "src/fern/class_/types/__init__.py",
        "src/fern/class_/types/get_api_classes_index_multi_classing_request_index.py",
        "src/fern/class_/types/get_api_classes_index_request_index.py",
        "src/fern/class_/types/get_api_classes_index_spellcasting_request_index.py",
        "src/fern/class_levels/__init__.py",
        "src/fern/class_levels/client.py",
        "src/fern/class_levels/raw_client.py",
        "src/fern/class_levels/types/__init__.py",
        "src/fern/class_levels/types/get_api_classes_index_levels_class_level_features_request_index.py",
        "src/fern/class_levels/types/get_api_classes_index_levels_class_level_request_index.py",
        "src/fern/class_levels/types/get_api_classes_index_levels_request_index.py",
        "src/fern/class_levels/types/get_api_classes_index_levels_spell_level_spells_request_index.py",
        "src/fern/class_resource_lists/__init__.py",
        "src/fern/class_resource_lists/client.py",
        "src/fern/class_resource_lists/raw_client.py",
        "src/fern/class_resource_lists/types/__init__.py",
        "src/fern/class_resource_lists/types/get_api_classes_index_features_request_index.py",
        "src/fern/class_resource_lists/types/get_api_classes_index_proficiencies_request_index.py",
        "src/fern/class_resource_lists/types/get_api_classes_index_spells_request_index.py",
        "src/fern/class_resource_lists/types/get_api_classes_index_subclasses_request_index.py",
        "src/fern/client.py",
        "src/fern/common/__init__.py",
        "src/fern/common/client.py",
        "src/fern/common/raw_client.py",
        "src/fern/common/types/__init__.py",
        "src/fern/common/types/get_api_endpoint_request_endpoint.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/equipment/__init__.py",
        "src/fern/equipment/client.py",
        "src/fern/equipment/raw_client.py",
        "src/fern/equipment/types/__init__.py",
        "src/fern/equipment/types/get_api_weapon_properties_index_request_index.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/feats/__init__.py",
        "src/fern/feats/client.py",
        "src/fern/feats/raw_client.py",
        "src/fern/feats/types/__init__.py",
        "src/fern/feats/types/get_api_feats_index_request_index.py",
        "src/fern/features/__init__.py",
        "src/fern/features/client.py",
        "src/fern/features/raw_client.py",
        "src/fern/game_mechanics/__init__.py",
        "src/fern/game_mechanics/client.py",
        "src/fern/game_mechanics/raw_client.py",
        "src/fern/game_mechanics/types/__init__.py",
        "src/fern/game_mechanics/types/get_api_conditions_index_request_index.py",
        "src/fern/game_mechanics/types/get_api_damage_types_index_request_index.py",
        "src/fern/game_mechanics/types/get_api_magic_schools_index_request_index.py",
        "src/fern/monsters/__init__.py",
        "src/fern/monsters/client.py",
        "src/fern/monsters/raw_client.py",
        "src/fern/py.typed",
        "src/fern/races/__init__.py",
        "src/fern/races/client.py",
        "src/fern/races/raw_client.py",
        "src/fern/races/types/__init__.py",
        "src/fern/races/types/get_api_races_index_proficiencies_request_index.py",
        "src/fern/races/types/get_api_races_index_request_index.py",
        "src/fern/races/types/get_api_races_index_subraces_request_index.py",
        "src/fern/races/types/get_api_races_index_traits_request_index.py",
        "src/fern/rules/__init__.py",
        "src/fern/rules/client.py",
        "src/fern/rules/raw_client.py",
        "src/fern/rules/types/__init__.py",
        "src/fern/rules/types/get_api_rule_sections_index_request_index.py",
        "src/fern/rules/types/get_api_rules_index_request_index.py",
        "src/fern/spells/__init__.py",
        "src/fern/spells/client.py",
        "src/fern/spells/raw_client.py",
        "src/fern/subclasses/__init__.py",
        "src/fern/subclasses/client.py",
        "src/fern/subclasses/raw_client.py",
        "src/fern/subclasses/types/__init__.py",
        "src/fern/subclasses/types/get_api_subclasses_index_features_request_index.py",
        "src/fern/subclasses/types/get_api_subclasses_index_levels_request_index.py",
        "src/fern/subclasses/types/get_api_subclasses_index_levels_subclass_level_features_request_index.py",
        "src/fern/subclasses/types/get_api_subclasses_index_levels_subclass_level_request_index.py",
        "src/fern/subclasses/types/get_api_subclasses_index_request_index.py",
        "src/fern/subraces/__init__.py",
        "src/fern/subraces/client.py",
        "src/fern/subraces/raw_client.py",
        "src/fern/subraces/types/__init__.py",
        "src/fern/subraces/types/get_api_subraces_index_proficiencies_request_index.py",
        "src/fern/subraces/types/get_api_subraces_index_request_index.py",
        "src/fern/subraces/types/get_api_subraces_index_traits_request_index.py",
        "src/fern/traits/__init__.py",
        "src/fern/traits/client.py",
        "src/fern/traits/raw_client.py",
        "src/fern/traits/types/__init__.py",
        "src/fern/traits/types/get_api_traits_index_request_index.py",
        "src/fern/types/__init__.py",
        "src/fern/types/ability_bonus.py",
        "src/fern/types/ability_score.py",
        "src/fern/types/alignment.py",
        "src/fern/types/api_reference.py",
        "src/fern/types/api_reference_list.py",
        "src/fern/types/area_of_effect.py",
        "src/fern/types/area_of_effect_type.py",
        "src/fern/types/armor.py",
        "src/fern/types/background.py",
        "src/fern/types/background_feature.py",
        "src/fern/types/choice.py",
        "src/fern/types/class_.py",
        "src/fern/types/class_level.py",
        "src/fern/types/class_level_class_specific.py",
        "src/fern/types/class_level_class_specific_action_surges.py",
        "src/fern/types/class_level_class_specific_arcane_recover_levels.py",
        "src/fern/types/class_level_class_specific_aura_range.py",
        "src/fern/types/class_level_class_specific_bardic_inspiration_dice.py",
        "src/fern/types/class_level_class_specific_brutal_critical_dice.py",
        "src/fern/types/class_level_class_specific_channel_divinity_charges.py",
        "src/fern/types/class_level_class_specific_creating_spell_slots.py",
        "src/fern/types/class_level_class_specific_creating_spell_slots_creating_spell_slots_item.py",
        "src/fern/types/class_level_class_specific_favored_enemies.py",
        "src/fern/types/class_level_class_specific_invocations_known.py",
        "src/fern/types/class_level_class_specific_ki_points.py",
        "src/fern/types/class_level_class_specific_ki_points_martial_arts.py",
        "src/fern/types/class_level_class_specific_sneak_attack.py",
        "src/fern/types/class_level_class_specific_sneak_attack_sneak_attack.py",
        "src/fern/types/class_level_class_specific_wild_shape_fly.py",
        "src/fern/types/class_level_spellcasting.py",
        "src/fern/types/class_starting_equipment_item.py",
        "src/fern/types/condition.py",
        "src/fern/types/cost.py",
        "src/fern/types/damage.py",
        "src/fern/types/damage_at_character_level.py",
        "src/fern/types/damage_at_slot_level.py",
        "src/fern/types/damage_type.py",
        "src/fern/types/dc.py",
        "src/fern/types/equipment.py",
        "src/fern/types/equipment_category.py",
        "src/fern/types/equipment_pack.py",
        "src/fern/types/error_response.py",
        "src/fern/types/feat.py",
        "src/fern/types/feature.py",
        "src/fern/types/feature_prerequisites_item.py",
        "src/fern/types/feature_prerequisites_item_feature.py",
        "src/fern/types/feature_prerequisites_item_level.py",
        "src/fern/types/feature_prerequisites_item_spell.py",
        "src/fern/types/gear.py",
        "src/fern/types/language.py",
        "src/fern/types/language_type.py",
        "src/fern/types/magic_item.py",
        "src/fern/types/magic_item_rarity.py",
        "src/fern/types/magic_item_rarity_name.py",
        "src/fern/types/magic_school.py",
        "src/fern/types/monster.py",
        "src/fern/types/monster_actions_item.py",
        "src/fern/types/monster_actions_item_actions_item.py",
        "src/fern/types/monster_actions_item_actions_item_type.py",
        "src/fern/types/monster_actions_item_attacks_item.py",
        "src/fern/types/monster_actions_item_damage_item.py",
        "src/fern/types/monster_alignments.py",
        "src/fern/types/monster_armor_class_item.py",
        "src/fern/types/monster_armor_class_item_armor.py",
        "src/fern/types/monster_armor_class_item_condition.py",
        "src/fern/types/monster_armor_class_item_dex.py",
        "src/fern/types/monster_armor_class_item_natural.py",
        "src/fern/types/monster_armor_class_item_spell.py",
        "src/fern/types/monster_legendary_actions_item.py",
        "src/fern/types/monster_legendary_actions_item_actions_item.py",
        "src/fern/types/monster_legendary_actions_item_actions_item_type.py",
        "src/fern/types/monster_legendary_actions_item_attacks_item.py",
        "src/fern/types/monster_legendary_actions_item_damage_item.py",
        "src/fern/types/monster_proficiencies_item.py",
        "src/fern/types/monster_reactions_item.py",
        "src/fern/types/monster_reactions_item_actions_item.py",
        "src/fern/types/monster_reactions_item_actions_item_type.py",
        "src/fern/types/monster_reactions_item_attacks_item.py",
        "src/fern/types/monster_reactions_item_damage_item.py",
        "src/fern/types/monster_senses.py",
        "src/fern/types/monster_size.py",
        "src/fern/types/monster_special_abilities_item.py",
        "src/fern/types/monster_special_abilities_item_spellcasting.py",
        "src/fern/types/monster_special_abilities_item_spellcasting_spells_item.py",
        "src/fern/types/monster_special_abilities_item_usage.py",
        "src/fern/types/monster_special_abilities_item_usage_type.py",
        "src/fern/types/monster_speed.py",
        "src/fern/types/multiclassing.py",
        "src/fern/types/option.py",
        "src/fern/types/option_action_name.py",
        "src/fern/types/option_action_name_type.py",
        "src/fern/types/option_alignments.py",
        "src/fern/types/option_bonus.py",
        "src/fern/types/option_choice.py",
        "src/fern/types/option_damage.py",
        "src/fern/types/option_damage_dice.py",
        "src/fern/types/option_item.py",
        "src/fern/types/option_items.py",
        "src/fern/types/option_minimum_score.py",
        "src/fern/types/option_of.py",
        "src/fern/types/option_set.py",
        "src/fern/types/option_set_equipment_category.py",
        "src/fern/types/option_set_option_set_type.py",
        "src/fern/types/option_set_options_array.py",
        "src/fern/types/option_string.py",
        "src/fern/types/prerequisite.py",
        "src/fern/types/proficiency.py",
        "src/fern/types/race.py",
        "src/fern/types/resource_description.py",
        "src/fern/types/rule.py",
        "src/fern/types/rule_section.py",
        "src/fern/types/skill.py",
        "src/fern/types/spell.py",
        "src/fern/types/spell_components_item.py",
        "src/fern/types/spell_damage.py",
        "src/fern/types/spell_prerequisite.py",
        "src/fern/types/spellcasting.py",
        "src/fern/types/spellcasting_info_item.py",
        "src/fern/types/subclass.py",
        "src/fern/types/subclass_level.py",
        "src/fern/types/subclass_level_resource.py",
        "src/fern/types/subclass_level_spellcasting.py",
        "src/fern/types/subclass_spells_item.py",
        "src/fern/types/subrace.py",
        "src/fern/types/trait.py",
        "src/fern/types/trait_trait_specific.py",
        "src/fern/types/trait_trait_specific_breath_weapon.py",
        "src/fern/types/trait_trait_specific_breath_weapon_breath_weapon.py",
        "src/fern/types/trait_trait_specific_breath_weapon_breath_weapon_damage.py",
        "src/fern/types/trait_trait_specific_breath_weapon_breath_weapon_usage.py",
        "src/fern/types/weapon.py",
        "src/fern/types/weapon_property.py",
        "src/fern/types/weapon_range.py",
        "src/fern/version.py",
    ],
};

const APACHE_QAKKA: Corpus = Corpus {
    api: "apache.org-qakka",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/py.typed",
        "src/fern/queues/__init__.py",
        "src/fern/queues/client.py",
        "src/fern/queues/raw_client.py",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/api_response.py",
        "src/fern/types/queue.py",
        "src/fern/types/queue_message.py",
        "src/fern/version.py",
    ],
};

const AUTHENTIQIO: Corpus = Corpus {
    api: "6-dot-authentiqio.appspot.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/gone_error.py",
        "src/fern/errors/method_not_allowed_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/key/__init__.py",
        "src/fern/key/client.py",
        "src/fern/key/raw_client.py",
        "src/fern/key/types/__init__.py",
        "src/fern/key/types/key_bind_response.py",
        "src/fern/key/types/key_register_response.py",
        "src/fern/key/types/key_retrieve_response.py",
        "src/fern/key/types/key_revoke_nosecret_response.py",
        "src/fern/key/types/key_revoke_response.py",
        "src/fern/key/types/key_update_response.py",
        "src/fern/login/__init__.py",
        "src/fern/login/client.py",
        "src/fern/login/raw_client.py",
        "src/fern/login/types/__init__.py",
        "src/fern/login/types/push_login_request_response.py",
        "src/fern/py.typed",
        "src/fern/scope/__init__.py",
        "src/fern/scope/client.py",
        "src/fern/scope/raw_client.py",
        "src/fern/scope/types/__init__.py",
        "src/fern/scope/types/sign_confirm_response.py",
        "src/fern/scope/types/sign_delete_response.py",
        "src/fern/scope/types/sign_request_response.py",
        "src/fern/scope/types/sign_retrieve_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/authentiq_id.py",
        "src/fern/types/claims.py",
        "src/fern/types/error.py",
        "src/fern/types/push_token.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

const ETSI_MEC010_2: Corpus = Corpus {
    api: "etsi.local-mec010-2_apppkgmgmt",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/app_pkgm/__init__.py",
        "src/fern/app_pkgm/client.py",
        "src/fern/app_pkgm/raw_client.py",
        "src/fern/app_pkgm_notifications/__init__.py",
        "src/fern/app_pkgm_notifications/client.py",
        "src/fern/app_pkgm_notifications/raw_client.py",
        "src/fern/app_pkgm_notifications/types/__init__.py",
        "src/fern/app_pkgm_notifications/types/app_pkg_notification_operational_state.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/not_acceptable_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/range_not_satisfiable_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/action.py",
        "src/fern/types/algorithm.py",
        "src/fern/types/app_d.py",
        "src/fern/types/app_d_id.py",
        "src/fern/types/app_d_version.py",
        "src/fern/types/app_external_cpd.py",
        "src/fern/types/app_name.py",
        "src/fern/types/app_pkg_artifact_info.py",
        "src/fern/types/app_pkg_filter.py",
        "src/fern/types/app_pkg_id.py",
        "src/fern/types/app_pkg_info.py",
        "src/fern/types/app_pkg_info_links.py",
        "src/fern/types/app_pkg_info_modifications.py",
        "src/fern/types/app_pkg_info_modifications_operation_state.py",
        "src/fern/types/app_pkg_notification_id.py",
        "src/fern/types/app_pkg_notification_links.py",
        "src/fern/types/app_pkg_notification_type.py",
        "src/fern/types/app_pkg_operational_state.py",
        "src/fern/types/app_pkg_subscription_info.py",
        "src/fern/types/app_pkg_subscription_info_id.py",
        "src/fern/types/app_pkg_subscription_info_links.py",
        "src/fern/types/app_pkg_subscription_link_list.py",
        "src/fern/types/app_pkg_subscription_link_list_links.py",
        "src/fern/types/app_pkg_subscription_type.py",
        "src/fern/types/app_pkg_sw_image_info.py",
        "src/fern/types/app_provider.py",
        "src/fern/types/app_software_version.py",
        "src/fern/types/callback_uri.py",
        "src/fern/types/category_ref.py",
        "src/fern/types/change_app_instance_state_op_config.py",
        "src/fern/types/checksum.py",
        "src/fern/types/dns_rule_descriptor.py",
        "src/fern/types/feature_dependency.py",
        "src/fern/types/filter_type.py",
        "src/fern/types/hash.py",
        "src/fern/types/href.py",
        "src/fern/types/interface_descriptor.py",
        "src/fern/types/interface_type.py",
        "src/fern/types/ip_address_type.py",
        "src/fern/types/key_value_pairs.py",
        "src/fern/types/latency_descriptor.py",
        "src/fern/types/link_type.py",
        "src/fern/types/not_specified.py",
        "src/fern/types/onboarding_state.py",
        "src/fern/types/problem_details.py",
        "src/fern/types/security_info.py",
        "src/fern/types/ser_name.py",
        "src/fern/types/ser_version.py",
        "src/fern/types/serializer_types.py",
        "src/fern/types/serializers.py",
        "src/fern/types/service_dependency.py",
        "src/fern/types/service_descriptor.py",
        "src/fern/types/subscription_id.py",
        "src/fern/types/subscriptions_app_pkg_subscription.py",
        "src/fern/types/subsctiption_type_app_pkg.py",
        "src/fern/types/sw_image_descriptor.py",
        "src/fern/types/terminate_app_instance_op_config.py",
        "src/fern/types/time_stamp.py",
        "src/fern/types/traffic_filter.py",
        "src/fern/types/traffic_rule_descriptor.py",
        "src/fern/types/transport_dependency.py",
        "src/fern/types/transport_descriptor.py",
        "src/fern/types/transport_types.py",
        "src/fern/types/transports_supported.py",
        "src/fern/types/tunnel_info.py",
        "src/fern/types/tunnel_type.py",
        "src/fern/types/uri.py",
        "src/fern/types/usage_state.py",
        "src/fern/types/virtual_compute_description.py",
        "src/fern/types/virtual_network_interface_requirements.py",
        "src/fern/types/virtual_storage_descriptor.py",
        "src/fern/version.py",
    ],
};

const APIDECK_WEBHOOK: Corpus = Corpus {
    api: "apideck.com-webhook",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/application_id.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/consumer_id.py",
        "src/fern/types/create_webhook_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/delete_webhook_response.py",
        "src/fern/types/delivery_url.py",
        "src/fern/types/description.py",
        "src/fern/types/execute_base_url.py",
        "src/fern/types/execute_webhook_event_request.py",
        "src/fern/types/execute_webhook_events_request.py",
        "src/fern/types/execute_webhook_response.py",
        "src/fern/types/get_webhook_event_logs_response.py",
        "src/fern/types/get_webhook_response.py",
        "src/fern/types/get_webhooks_response.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/resolve_webhook_event_request.py",
        "src/fern/types/resolve_webhook_events_request.py",
        "src/fern/types/resolve_webhook_response.py",
        "src/fern/types/service_id.py",
        "src/fern/types/status.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_api_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_webhook_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/webhook.py",
        "src/fern/types/webhook_disabled_reason.py",
        "src/fern/types/webhook_event.py",
        "src/fern/types/webhook_event_log.py",
        "src/fern/types/webhook_event_log_attempts_item.py",
        "src/fern/types/webhook_event_log_service.py",
        "src/fern/types/webhook_event_logs_filter.py",
        "src/fern/types/webhook_event_logs_filter_service.py",
        "src/fern/types/webhook_event_type.py",
        "src/fern/version.py",
        "src/fern/webhooks/__init__.py",
        "src/fern/webhooks/client.py",
        "src/fern/webhooks/raw_client.py",
        "src/fern/webhooks/types/__init__.py",
        "src/fern/webhooks/types/webhooks_execute_request_body.py",
        "src/fern/webhooks/types/webhooks_resolve_request_body.py",
        "src/fern/webhooks/types/webhooks_short_execute_request_body.py",
    ],
};

const APIDECK_VAULT: Corpus = Corpus {
    api: "apideck.com-vault",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/connections/__init__.py",
        "src/fern/connections/client.py",
        "src/fern/connections/raw_client.py",
        "src/fern/connections/types/__init__.py",
        "src/fern/connections/types/connection_import_data_credentials.py",
        "src/fern/consumers/__init__.py",
        "src/fern/consumers/client.py",
        "src/fern/consumers/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/logs/__init__.py",
        "src/fern/logs/client.py",
        "src/fern/logs/raw_client.py",
        "src/fern/py.typed",
        "src/fern/sessions/__init__.py",
        "src/fern/sessions/client.py",
        "src/fern/sessions/raw_client.py",
        "src/fern/sessions/types/__init__.py",
        "src/fern/sessions/types/session_settings.py",
        "src/fern/sessions/types/session_settings_allow_actions_item.py",
        "src/fern/sessions/types/session_theme.py",
        "src/fern/types/__init__.py",
        "src/fern/types/application_id.py",
        "src/fern/types/auth_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/connection.py",
        "src/fern/types/connection_configuration_item.py",
        "src/fern/types/connection_configuration_item_defaults_item.py",
        "src/fern/types/connection_configuration_item_defaults_item_target.py",
        "src/fern/types/connection_configuration_item_defaults_item_value.py",
        "src/fern/types/connection_configuration_item_defaults_item_value_four_item.py",
        "src/fern/types/connection_event.py",
        "src/fern/types/connection_metadata.py",
        "src/fern/types/connection_state.py",
        "src/fern/types/connection_status.py",
        "src/fern/types/connection_webhook.py",
        "src/fern/types/connection_webhook_disabled_reason.py",
        "src/fern/types/connection_webhook_events_item.py",
        "src/fern/types/connection_webhook_status.py",
        "src/fern/types/consumer.py",
        "src/fern/types/consumer_connection.py",
        "src/fern/types/consumer_connection_state.py",
        "src/fern/types/consumer_id.py",
        "src/fern/types/consumer_metadata.py",
        "src/fern/types/consumer_request_counts_in_date_range_response.py",
        "src/fern/types/consumer_request_counts_in_date_range_response_data.py",
        "src/fern/types/create_connection_response.py",
        "src/fern/types/create_consumer_response.py",
        "src/fern/types/create_session_response.py",
        "src/fern/types/create_session_response_data.py",
        "src/fern/types/delete_consumer_response.py",
        "src/fern/types/delete_consumer_response_data.py",
        "src/fern/types/form_field.py",
        "src/fern/types/form_field_option.py",
        "src/fern/types/form_field_option_group.py",
        "src/fern/types/form_field_type.py",
        "src/fern/types/get_connection_response.py",
        "src/fern/types/get_connections_response.py",
        "src/fern/types/get_consumer_response.py",
        "src/fern/types/get_consumers_response.py",
        "src/fern/types/get_consumers_response_data_item.py",
        "src/fern/types/get_logs_response.py",
        "src/fern/types/integration_state.py",
        "src/fern/types/links.py",
        "src/fern/types/log.py",
        "src/fern/types/log_operation.py",
        "src/fern/types/log_service.py",
        "src/fern/types/log_unified_api.py",
        "src/fern/types/logs_filter.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/o_auth_grant_type.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/proxy_request.py",
        "src/fern/types/request_count_allocation.py",
        "src/fern/types/simple_form_field_option.py",
        "src/fern/types/simple_form_field_option_value.py",
        "src/fern/types/simple_form_field_option_value_four_item.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_api_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_connection_response.py",
        "src/fern/types/update_consumer_response.py",
        "src/fern/types/vault_event_type.py",
        "src/fern/types/webhook_subscription.py",
        "src/fern/version.py",
    ],
};

const AIRBYTE_CONFIG: Corpus = Corpus {
    api: "airbyte.local-config",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/attempt/__init__.py",
        "src/fern/attempt/client.py",
        "src/fern/attempt/raw_client.py",
        "src/fern/client.py",
        "src/fern/connection/__init__.py",
        "src/fern/connection/client.py",
        "src/fern/connection/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/destination/__init__.py",
        "src/fern/destination/client.py",
        "src/fern/destination/raw_client.py",
        "src/fern/destination_definition/__init__.py",
        "src/fern/destination_definition/client.py",
        "src/fern/destination_definition/raw_client.py",
        "src/fern/destination_definition_specification/__init__.py",
        "src/fern/destination_definition_specification/client.py",
        "src/fern/destination_definition_specification/raw_client.py",
        "src/fern/destination_oauth/__init__.py",
        "src/fern/destination_oauth/client.py",
        "src/fern/destination_oauth/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/health/__init__.py",
        "src/fern/health/client.py",
        "src/fern/health/raw_client.py",
        "src/fern/jobs/__init__.py",
        "src/fern/jobs/client.py",
        "src/fern/jobs/raw_client.py",
        "src/fern/logs/__init__.py",
        "src/fern/logs/client.py",
        "src/fern/logs/raw_client.py",
        "src/fern/notifications/__init__.py",
        "src/fern/notifications/client.py",
        "src/fern/notifications/raw_client.py",
        "src/fern/openapi/__init__.py",
        "src/fern/openapi/client.py",
        "src/fern/openapi/raw_client.py",
        "src/fern/operation/__init__.py",
        "src/fern/operation/client.py",
        "src/fern/operation/raw_client.py",
        "src/fern/py.typed",
        "src/fern/scheduler/__init__.py",
        "src/fern/scheduler/client.py",
        "src/fern/scheduler/raw_client.py",
        "src/fern/source/__init__.py",
        "src/fern/source/client.py",
        "src/fern/source/raw_client.py",
        "src/fern/source_definition/__init__.py",
        "src/fern/source_definition/client.py",
        "src/fern/source_definition/raw_client.py",
        "src/fern/source_definition_specification/__init__.py",
        "src/fern/source_definition_specification/client.py",
        "src/fern/source_definition_specification/raw_client.py",
        "src/fern/source_oauth/__init__.py",
        "src/fern/source_oauth/client.py",
        "src/fern/source_oauth/raw_client.py",
        "src/fern/state/__init__.py",
        "src/fern/state/client.py",
        "src/fern/state/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/actor_catalog_with_updated_at.py",
        "src/fern/types/actor_definition_resource_requirements.py",
        "src/fern/types/advanced_auth.py",
        "src/fern/types/advanced_auth_auth_flow_type.py",
        "src/fern/types/airbyte_archive.py",
        "src/fern/types/airbyte_catalog.py",
        "src/fern/types/airbyte_stream.py",
        "src/fern/types/airbyte_stream_and_configuration.py",
        "src/fern/types/airbyte_stream_configuration.py",
        "src/fern/types/attempt_failure_origin.py",
        "src/fern/types/attempt_failure_reason.py",
        "src/fern/types/attempt_failure_summary.py",
        "src/fern/types/attempt_failure_type.py",
        "src/fern/types/attempt_info_read.py",
        "src/fern/types/attempt_normalization_status_read.py",
        "src/fern/types/attempt_normalization_status_read_list.py",
        "src/fern/types/attempt_number.py",
        "src/fern/types/attempt_read.py",
        "src/fern/types/attempt_stats.py",
        "src/fern/types/attempt_status.py",
        "src/fern/types/attempt_stream_stats.py",
        "src/fern/types/attempt_sync_config.py",
        "src/fern/types/auth_specification.py",
        "src/fern/types/auth_specification_auth_type.py",
        "src/fern/types/catalog_diff.py",
        "src/fern/types/check_connection_read.py",
        "src/fern/types/check_connection_read_status.py",
        "src/fern/types/check_operation_read.py",
        "src/fern/types/check_operation_read_status.py",
        "src/fern/types/complete_o_auth_response.py",
        "src/fern/types/connection_id.py",
        "src/fern/types/connection_id_request_body.py",
        "src/fern/types/connection_read.py",
        "src/fern/types/connection_read_list.py",
        "src/fern/types/connection_schedule.py",
        "src/fern/types/connection_schedule_data.py",
        "src/fern/types/connection_schedule_data_basic_schedule.py",
        "src/fern/types/connection_schedule_data_basic_schedule_time_unit.py",
        "src/fern/types/connection_schedule_data_cron.py",
        "src/fern/types/connection_schedule_time_unit.py",
        "src/fern/types/connection_schedule_type.py",
        "src/fern/types/connection_state.py",
        "src/fern/types/connection_state_type.py",
        "src/fern/types/connection_status.py",
        "src/fern/types/customer_id.py",
        "src/fern/types/customerio_notification_configuration.py",
        "src/fern/types/data_type.py",
        "src/fern/types/db_migration_execution_read.py",
        "src/fern/types/db_migration_read.py",
        "src/fern/types/db_migration_read_list.py",
        "src/fern/types/db_migration_request_body.py",
        "src/fern/types/db_migration_state.py",
        "src/fern/types/destination_auth_specification.py",
        "src/fern/types/destination_clone_configuration.py",
        "src/fern/types/destination_configuration.py",
        "src/fern/types/destination_definition_create.py",
        "src/fern/types/destination_definition_id.py",
        "src/fern/types/destination_definition_id_request_body.py",
        "src/fern/types/destination_definition_id_with_workspace_id.py",
        "src/fern/types/destination_definition_read.py",
        "src/fern/types/destination_definition_read_list.py",
        "src/fern/types/destination_definition_specification.py",
        "src/fern/types/destination_definition_specification_read.py",
        "src/fern/types/destination_id.py",
        "src/fern/types/destination_id_request_body.py",
        "src/fern/types/destination_read.py",
        "src/fern/types/destination_read_list.py",
        "src/fern/types/destination_search.py",
        "src/fern/types/destination_snippet_read.py",
        "src/fern/types/destination_sync_mode.py",
        "src/fern/types/destination_update.py",
        "src/fern/types/discover_catalog_result.py",
        "src/fern/types/field_add.py",
        "src/fern/types/field_name.py",
        "src/fern/types/field_remove.py",
        "src/fern/types/field_schema.py",
        "src/fern/types/field_schema_update.py",
        "src/fern/types/field_transform.py",
        "src/fern/types/field_transform_transform_type.py",
        "src/fern/types/geography.py",
        "src/fern/types/global_state.py",
        "src/fern/types/health_check_read.py",
        "src/fern/types/import_read.py",
        "src/fern/types/import_read_status.py",
        "src/fern/types/import_request_body.py",
        "src/fern/types/internal_operation_result.py",
        "src/fern/types/invalid_input_exception_info.py",
        "src/fern/types/invalid_input_property.py",
        "src/fern/types/job_config_type.py",
        "src/fern/types/job_created_at.py",
        "src/fern/types/job_debug_info_read.py",
        "src/fern/types/job_debug_read.py",
        "src/fern/types/job_id.py",
        "src/fern/types/job_id_request_body.py",
        "src/fern/types/job_info_light_read.py",
        "src/fern/types/job_info_read.py",
        "src/fern/types/job_optional_read.py",
        "src/fern/types/job_read.py",
        "src/fern/types/job_read_list.py",
        "src/fern/types/job_status.py",
        "src/fern/types/job_type.py",
        "src/fern/types/job_type_resource_limit.py",
        "src/fern/types/job_with_attempts_read.py",
        "src/fern/types/known_exception_info.py",
        "src/fern/types/log_read.py",
        "src/fern/types/log_type.py",
        "src/fern/types/namespace_definition_type.py",
        "src/fern/types/non_breaking_changes_preference.py",
        "src/fern/types/normalization_destination_definition_config.py",
        "src/fern/types/not_found_known_exception_info.py",
        "src/fern/types/notification.py",
        "src/fern/types/notification_read.py",
        "src/fern/types/notification_read_status.py",
        "src/fern/types/notification_type.py",
        "src/fern/types/o_auth2specification.py",
        "src/fern/types/o_auth_config_specification.py",
        "src/fern/types/o_auth_configuration.py",
        "src/fern/types/o_auth_consent_read.py",
        "src/fern/types/o_auth_input_configuration.py",
        "src/fern/types/operation_create.py",
        "src/fern/types/operation_id.py",
        "src/fern/types/operation_id_request_body.py",
        "src/fern/types/operation_read.py",
        "src/fern/types/operation_read_list.py",
        "src/fern/types/operator_configuration.py",
        "src/fern/types/operator_dbt.py",
        "src/fern/types/operator_normalization.py",
        "src/fern/types/operator_normalization_option.py",
        "src/fern/types/operator_type.py",
        "src/fern/types/operator_webhook.py",
        "src/fern/types/operator_webhook_dbt_cloud.py",
        "src/fern/types/operator_webhook_webhook_type.py",
        "src/fern/types/pagination.py",
        "src/fern/types/private_destination_definition_read.py",
        "src/fern/types/private_destination_definition_read_list.py",
        "src/fern/types/private_source_definition_read.py",
        "src/fern/types/private_source_definition_read_list.py",
        "src/fern/types/release_stage.py",
        "src/fern/types/reset_config.py",
        "src/fern/types/resource_id.py",
        "src/fern/types/resource_requirements.py",
        "src/fern/types/schema_change.py",
        "src/fern/types/selected_field_info.py",
        "src/fern/types/slack_notification_configuration.py",
        "src/fern/types/source_auth_specification.py",
        "src/fern/types/source_clone_configuration.py",
        "src/fern/types/source_configuration.py",
        "src/fern/types/source_core_config.py",
        "src/fern/types/source_definition_create.py",
        "src/fern/types/source_definition_id.py",
        "src/fern/types/source_definition_id_request_body.py",
        "src/fern/types/source_definition_id_with_workspace_id.py",
        "src/fern/types/source_definition_read.py",
        "src/fern/types/source_definition_read_list.py",
        "src/fern/types/source_definition_read_source_type.py",
        "src/fern/types/source_definition_specification.py",
        "src/fern/types/source_definition_specification_read.py",
        "src/fern/types/source_discover_schema_read.py",
        "src/fern/types/source_id.py",
        "src/fern/types/source_id_request_body.py",
        "src/fern/types/source_read.py",
        "src/fern/types/source_read_list.py",
        "src/fern/types/source_search.py",
        "src/fern/types/source_snippet_read.py",
        "src/fern/types/source_update.py",
        "src/fern/types/state_blob.py",
        "src/fern/types/stream_descriptor.py",
        "src/fern/types/stream_json_schema.py",
        "src/fern/types/stream_state.py",
        "src/fern/types/stream_transform.py",
        "src/fern/types/stream_transform_transform_type.py",
        "src/fern/types/sync_mode.py",
        "src/fern/types/synchronous_job_read.py",
        "src/fern/types/upload_read.py",
        "src/fern/types/upload_read_status.py",
        "src/fern/types/web_backend_check_updates_read.py",
        "src/fern/types/web_backend_connection_list_item.py",
        "src/fern/types/web_backend_connection_read.py",
        "src/fern/types/web_backend_connection_read_list.py",
        "src/fern/types/web_backend_geographies_list_result.py",
        "src/fern/types/web_backend_operation_create_or_update.py",
        "src/fern/types/web_backend_workspace_state_result.py",
        "src/fern/types/webhook_config_read.py",
        "src/fern/types/webhook_config_write.py",
        "src/fern/types/workflow_id.py",
        "src/fern/types/workflow_state_read.py",
        "src/fern/types/workspace_id.py",
        "src/fern/types/workspace_id_request_body.py",
        "src/fern/types/workspace_read.py",
        "src/fern/types/workspace_read_list.py",
        "src/fern/version.py",
        "src/fern/web_backend/__init__.py",
        "src/fern/web_backend/client.py",
        "src/fern/web_backend/raw_client.py",
        "src/fern/workspace/__init__.py",
        "src/fern/workspace/client.py",
        "src/fern/workspace/raw_client.py",
    ],
};

const BINTABLE: Corpus = Corpus {
    api: "bintable.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/balance/__init__.py",
        "src/fern/balance/client.py",
        "src/fern/balance/raw_client.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/lookup/__init__.py",
        "src/fern/lookup/client.py",
        "src/fern/lookup/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/response_item.py",
        "src/fern/version.py",
    ],
};

const APIS_GURU: Corpus = Corpus {
    api: "apis.guru",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/ap_is/__init__.py",
        "src/fern/ap_is/client.py",
        "src/fern/ap_is/raw_client.py",
        "src/fern/ap_is/types/__init__.py",
        "src/fern/ap_is/types/get_providers_response.py",
        "src/fern/ap_is/types/get_services_response.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/ap_is.py",
        "src/fern/types/api.py",
        "src/fern/types/api_version.py",
        "src/fern/types/metrics.py",
        "src/fern/types/metrics_this_week.py",
        "src/fern/version.py",
    ],
};

const COLOR_PIZZA: Corpus = Corpus {
    api: "color.pizza",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/color.py",
        "src/fern/types/color_base.py",
        "src/fern/types/color_base_hsl.py",
        "src/fern/types/color_base_lab.py",
        "src/fern/types/color_base_rgb.py",
        "src/fern/types/color_base_swatch_img.py",
        "src/fern/types/color_hsl.py",
        "src/fern/types/color_lab.py",
        "src/fern/types/color_rgb.py",
        "src/fern/types/error.py",
        "src/fern/types/get_lists_response.py",
        "src/fern/types/get_lists_response_list_descriptions.py",
        "src/fern/types/get_names_response.py",
        "src/fern/types/get_response.py",
        "src/fern/types/list_description.py",
        "src/fern/types/possible_lists.py",
        "src/fern/version.py",
    ],
};

const BYAUTOMATA_IO: Corpus = Corpus {
    api: "byautomata.io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/contentpro_search/__init__.py",
        "src/fern/contentpro_search/client.py",
        "src/fern/contentpro_search/raw_client.py",
        "src/fern/contentpro_search/types/__init__.py",
        "src/fern/contentpro_search/types/get_contentpro_search_response.py",
        "src/fern/contentpro_search/types/get_contentpro_search_response_data_item.py",
        "src/fern/contentpro_similar_text/__init__.py",
        "src/fern/contentpro_similar_text/client.py",
        "src/fern/contentpro_similar_text/raw_client.py",
        "src/fern/contentpro_similar_text/types/__init__.py",
        "src/fern/contentpro_similar_text/types/post_contentpro_similar_text_response.py",
        "src/fern/contentpro_similar_text/types/post_contentpro_similar_text_response_data_item.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/not_implemented_error.py",
        "src/fern/py.typed",
        "src/fern/search/__init__.py",
        "src/fern/search/client.py",
        "src/fern/search/raw_client.py",
        "src/fern/search/types/__init__.py",
        "src/fern/search/types/get_search_response.py",
        "src/fern/similar/__init__.py",
        "src/fern/similar/client.py",
        "src/fern/similar/raw_client.py",
        "src/fern/similar/types/__init__.py",
        "src/fern/similar/types/get_similar_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/article.py",
        "src/fern/types/content_pro_company.py",
        "src/fern/types/content_pro_snippets.py",
        "src/fern/types/input_company.py",
        "src/fern/types/similar_company.py",
        "src/fern/types/similar_company_search.py",
        "src/fern/types/snippet.py",
        "src/fern/version.py",
    ],
};

const APIDECK_PROXY: Corpus = Corpus {
    api: "apideck.com-proxy",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/execute/__init__.py",
        "src/fern/execute/client.py",
        "src/fern/execute/raw_client.py",
        "src/fern/execute/types/__init__.py",
        "src/fern/execute/types/patch_proxy_request_body.py",
        "src/fern/execute/types/patch_proxy_request_body_zero.py",
        "src/fern/execute/types/post_proxy_request_body.py",
        "src/fern/execute/types/post_proxy_request_body_zero.py",
        "src/fern/execute/types/put_proxy_request_body.py",
        "src/fern/execute/types/put_proxy_request_body_zero.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/unauthorized_error_body.py",
        "src/fern/version.py",
    ],
};

const APIDECK_CONNECTOR: Corpus = Corpus {
    api: "apideck.com-connector",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/api_resources/__init__.py",
        "src/fern/api_resources/client.py",
        "src/fern/api_resources/raw_client.py",
        "src/fern/apis/__init__.py",
        "src/fern/apis/client.py",
        "src/fern/apis/raw_client.py",
        "src/fern/client.py",
        "src/fern/connector_docs/__init__.py",
        "src/fern/connector_docs/client.py",
        "src/fern/connector_docs/raw_client.py",
        "src/fern/connector_resources/__init__.py",
        "src/fern/connector_resources/client.py",
        "src/fern/connector_resources/raw_client.py",
        "src/fern/connectors/__init__.py",
        "src/fern/connectors/client.py",
        "src/fern/connectors/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/api.py",
        "src/fern/types/api_resource.py",
        "src/fern/types/api_resource_coverage.py",
        "src/fern/types/api_resource_coverage_coverage_item.py",
        "src/fern/types/api_resource_linked_resources_item.py",
        "src/fern/types/api_resources_item.py",
        "src/fern/types/api_status.py",
        "src/fern/types/api_type.py",
        "src/fern/types/apis_filter.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/connector.py",
        "src/fern/types/connector_auth_type.py",
        "src/fern/types/connector_doc.py",
        "src/fern/types/connector_doc_audience.py",
        "src/fern/types/connector_doc_format.py",
        "src/fern/types/connector_event.py",
        "src/fern/types/connector_event_event_source.py",
        "src/fern/types/connector_oauth_credentials_source.py",
        "src/fern/types/connector_oauth_grant_type.py",
        "src/fern/types/connector_oauth_scopes_item.py",
        "src/fern/types/connector_resource.py",
        "src/fern/types/connector_setting.py",
        "src/fern/types/connector_setting_type.py",
        "src/fern/types/connector_status.py",
        "src/fern/types/connector_tls_support.py",
        "src/fern/types/connector_unified_apis_item.py",
        "src/fern/types/connector_unified_apis_item_oauth_scopes_item.py",
        "src/fern/types/connectors_filter.py",
        "src/fern/types/get_api_resource_coverage_response.py",
        "src/fern/types/get_api_resource_response.py",
        "src/fern/types/get_api_response.py",
        "src/fern/types/get_apis_response.py",
        "src/fern/types/get_connector_resource_response.py",
        "src/fern/types/get_connector_response.py",
        "src/fern/types/get_connectors_response.py",
        "src/fern/types/id.py",
        "src/fern/types/linked_connector_resource.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/pagination_coverage.py",
        "src/fern/types/pagination_coverage_mode.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/resource_id.py",
        "src/fern/types/resource_status.py",
        "src/fern/types/supported_property.py",
        "src/fern/types/supported_property_child_properties_item.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_api_id.py",
        "src/fern/types/unified_property.py",
        "src/fern/types/webhook_support.py",
        "src/fern/types/webhook_support_managed_via.py",
        "src/fern/types/webhook_support_mode.py",
        "src/fern/types/webhook_support_subscription_level.py",
        "src/fern/types/webhook_support_virtual_webhooks.py",
        "src/fern/types/webhook_support_virtual_webhooks_request_rate.py",
        "src/fern/types/webhook_support_virtual_webhooks_request_rate_unit.py",
        "src/fern/version.py",
    ],
};

const APIDECK_ECOMMERCE: Corpus = Corpus {
    api: "apideck.com-ecommerce",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/customers/__init__.py",
        "src/fern/customers/client.py",
        "src/fern/customers/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/orders/__init__.py",
        "src/fern/orders/client.py",
        "src/fern/orders/raw_client.py",
        "src/fern/products/__init__.py",
        "src/fern/products/client.py",
        "src/fern/products/raw_client.py",
        "src/fern/py.typed",
        "src/fern/stores/__init__.py",
        "src/fern/stores/client.py",
        "src/fern/stores/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/create_ecommerce_customer_response.py",
        "src/fern/types/create_ecommerce_order_response.py",
        "src/fern/types/create_product_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/created_by.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/delete_ecommerce_customer_response.py",
        "src/fern/types/delete_ecommerce_order_response.py",
        "src/fern/types/delete_product_response.py",
        "src/fern/types/department.py",
        "src/fern/types/description.py",
        "src/fern/types/division.py",
        "src/fern/types/ecommerce_address.py",
        "src/fern/types/ecommerce_customer.py",
        "src/fern/types/ecommerce_customer_addresses_item.py",
        "src/fern/types/ecommerce_customer_addresses_item_type.py",
        "src/fern/types/ecommerce_customer_status.py",
        "src/fern/types/ecommerce_customers_filter.py",
        "src/fern/types/ecommerce_discount.py",
        "src/fern/types/ecommerce_order.py",
        "src/fern/types/ecommerce_order_fulfillment_status.py",
        "src/fern/types/ecommerce_order_line_item.py",
        "src/fern/types/ecommerce_order_line_item_options_item.py",
        "src/fern/types/ecommerce_order_payment_status.py",
        "src/fern/types/ecommerce_order_status.py",
        "src/fern/types/ecommerce_orders_filter.py",
        "src/fern/types/ecommerce_product.py",
        "src/fern/types/ecommerce_product_categories_item.py",
        "src/fern/types/ecommerce_product_images_item.py",
        "src/fern/types/ecommerce_product_options_item.py",
        "src/fern/types/ecommerce_product_status.py",
        "src/fern/types/ecommerce_product_variants_item.py",
        "src/fern/types/ecommerce_product_variants_item_images_item.py",
        "src/fern/types/ecommerce_product_variants_item_options_item.py",
        "src/fern/types/ecommerce_store.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/first_name.py",
        "src/fern/types/gender.py",
        "src/fern/types/get_ecommerce_customer_response.py",
        "src/fern/types/get_ecommerce_customers_response.py",
        "src/fern/types/get_ecommerce_order_response.py",
        "src/fern/types/get_ecommerce_orders_response.py",
        "src/fern/types/get_product_response.py",
        "src/fern/types/get_products_response.py",
        "src/fern/types/get_store_response.py",
        "src/fern/types/get_stores_response.py",
        "src/fern/types/id.py",
        "src/fern/types/language.py",
        "src/fern/types/last_name.py",
        "src/fern/types/linked_ecommerce_customer.py",
        "src/fern/types/linked_ecommerce_order.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/middle_name.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/payment_unit.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/photo_url.py",
        "src/fern/types/row_version.py",
        "src/fern/types/title.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/tracking_item.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_ecommerce_customer_response.py",
        "src/fern/types/update_ecommerce_order_response.py",
        "src/fern/types/update_product_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/updated_by.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/version.py",
    ],
};

const APIDECK_ISSUE_TRACKING: Corpus = Corpus {
    api: "apideck.com-issue-tracking",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/collections/__init__.py",
        "src/fern/collections/client.py",
        "src/fern/collections/raw_client.py",
        "src/fern/comments/__init__.py",
        "src/fern/comments/client.py",
        "src/fern/comments/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/py.typed",
        "src/fern/tags/__init__.py",
        "src/fern/tags/client.py",
        "src/fern/tags/raw_client.py",
        "src/fern/tickets/__init__.py",
        "src/fern/tickets/client.py",
        "src/fern/tickets/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/assignee.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/collection.py",
        "src/fern/types/collection_tag.py",
        "src/fern/types/collection_ticket_comment.py",
        "src/fern/types/collection_user.py",
        "src/fern/types/collections_sort.py",
        "src/fern/types/collections_sort_by.py",
        "src/fern/types/comments_sort.py",
        "src/fern/types/comments_sort_by.py",
        "src/fern/types/company_id.py",
        "src/fern/types/company_name.py",
        "src/fern/types/create_comment_response.py",
        "src/fern/types/create_ticket_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/created_by.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/delete_comment_response.py",
        "src/fern/types/delete_ticket_response.py",
        "src/fern/types/department.py",
        "src/fern/types/description.py",
        "src/fern/types/division.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/first_name.py",
        "src/fern/types/gender.py",
        "src/fern/types/get_collection_response.py",
        "src/fern/types/get_collection_tags_response.py",
        "src/fern/types/get_collection_user_response.py",
        "src/fern/types/get_collection_users_response.py",
        "src/fern/types/get_collections_response.py",
        "src/fern/types/get_comment_response.py",
        "src/fern/types/get_comments_response.py",
        "src/fern/types/get_ticket_response.py",
        "src/fern/types/get_tickets_response.py",
        "src/fern/types/id.py",
        "src/fern/types/issue_tracking_event_type.py",
        "src/fern/types/issue_tracking_webhook_event.py",
        "src/fern/types/issues_filter.py",
        "src/fern/types/language.py",
        "src/fern/types/last_name.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/middle_name.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/pass_through_query.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/payment_unit.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/photo_url.py",
        "src/fern/types/row_version.py",
        "src/fern/types/sort_direction.py",
        "src/fern/types/ticket.py",
        "src/fern/types/ticket_priority.py",
        "src/fern/types/tickets_sort.py",
        "src/fern/types/tickets_sort_by.py",
        "src/fern/types/title.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_comment_response.py",
        "src/fern/types/update_ticket_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/updated_by.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/users/__init__.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/version.py",
    ],
};

const APPWRITE_CLIENT: Corpus = Corpus {
    api: "appwrite.io-client",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/account/__init__.py",
        "src/fern/account/client.py",
        "src/fern/account/raw_client.py",
        "src/fern/avatars/__init__.py",
        "src/fern/avatars/client.py",
        "src/fern/avatars/raw_client.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/database/__init__.py",
        "src/fern/database/client.py",
        "src/fern/database/raw_client.py",
        "src/fern/environment.py",
        "src/fern/functions/__init__.py",
        "src/fern/functions/client.py",
        "src/fern/functions/raw_client.py",
        "src/fern/locale/__init__.py",
        "src/fern/locale/client.py",
        "src/fern/locale/raw_client.py",
        "src/fern/py.typed",
        "src/fern/storage/__init__.py",
        "src/fern/storage/client.py",
        "src/fern/storage/raw_client.py",
        "src/fern/teams/__init__.py",
        "src/fern/teams/client.py",
        "src/fern/teams/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/collection.py",
        "src/fern/types/continent.py",
        "src/fern/types/continent_list.py",
        "src/fern/types/country.py",
        "src/fern/types/country_list.py",
        "src/fern/types/currency.py",
        "src/fern/types/currency_list.py",
        "src/fern/types/document.py",
        "src/fern/types/document_list.py",
        "src/fern/types/error.py",
        "src/fern/types/execution.py",
        "src/fern/types/execution_list.py",
        "src/fern/types/file.py",
        "src/fern/types/file_list.py",
        "src/fern/types/function.py",
        "src/fern/types/jwt.py",
        "src/fern/types/language.py",
        "src/fern/types/language_list.py",
        "src/fern/types/locale.py",
        "src/fern/types/log.py",
        "src/fern/types/log_list.py",
        "src/fern/types/membership.py",
        "src/fern/types/membership_list.py",
        "src/fern/types/permissions.py",
        "src/fern/types/phone.py",
        "src/fern/types/phone_list.py",
        "src/fern/types/preferences.py",
        "src/fern/types/rule.py",
        "src/fern/types/session.py",
        "src/fern/types/session_list.py",
        "src/fern/types/tag.py",
        "src/fern/types/team.py",
        "src/fern/types/team_list.py",
        "src/fern/types/token.py",
        "src/fern/types/user.py",
        "src/fern/version.py",
    ],
};

const APIDECK_FILE_STORAGE: Corpus = Corpus {
    api: "apideck.com-file-storage",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/drive_groups/__init__.py",
        "src/fern/drive_groups/client.py",
        "src/fern/drive_groups/raw_client.py",
        "src/fern/drives/__init__.py",
        "src/fern/drives/client.py",
        "src/fern/drives/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/files/__init__.py",
        "src/fern/files/client.py",
        "src/fern/files/raw_client.py",
        "src/fern/folders/__init__.py",
        "src/fern/folders/client.py",
        "src/fern/folders/raw_client.py",
        "src/fern/py.typed",
        "src/fern/shared_links/__init__.py",
        "src/fern/shared_links/client.py",
        "src/fern/shared_links/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/create_drive_group_response.py",
        "src/fern/types/create_drive_response.py",
        "src/fern/types/create_file_request.py",
        "src/fern/types/create_file_response.py",
        "src/fern/types/create_folder_response.py",
        "src/fern/types/create_shared_link_response.py",
        "src/fern/types/create_upload_session_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/created_by.py",
        "src/fern/types/delete_drive_group_response.py",
        "src/fern/types/delete_drive_response.py",
        "src/fern/types/delete_file_response.py",
        "src/fern/types/delete_folder_response.py",
        "src/fern/types/delete_shared_link_response.py",
        "src/fern/types/delete_upload_session_response.py",
        "src/fern/types/description.py",
        "src/fern/types/downstream_id.py",
        "src/fern/types/drive.py",
        "src/fern/types/drive_group.py",
        "src/fern/types/drive_groups_filter.py",
        "src/fern/types/drives_filter.py",
        "src/fern/types/expires_at.py",
        "src/fern/types/file_size.py",
        "src/fern/types/file_storage_event_type.py",
        "src/fern/types/file_type.py",
        "src/fern/types/files_filter.py",
        "src/fern/types/files_sort.py",
        "src/fern/types/files_sort_by.py",
        "src/fern/types/folder.py",
        "src/fern/types/get_drive_group_response.py",
        "src/fern/types/get_drive_groups_response.py",
        "src/fern/types/get_drive_response.py",
        "src/fern/types/get_drives_response.py",
        "src/fern/types/get_file_response.py",
        "src/fern/types/get_files_response.py",
        "src/fern/types/get_folder_response.py",
        "src/fern/types/get_folders_response.py",
        "src/fern/types/get_shared_link_response.py",
        "src/fern/types/get_shared_links_response.py",
        "src/fern/types/get_upload_session_response.py",
        "src/fern/types/id.py",
        "src/fern/types/linked_folder.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/owner.py",
        "src/fern/types/parent_folder_id.py",
        "src/fern/types/pass_through_query.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/shared_link.py",
        "src/fern/types/shared_link_scope.py",
        "src/fern/types/shared_link_target.py",
        "src/fern/types/sort_direction.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_file.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_drive_group_response.py",
        "src/fern/types/update_drive_response.py",
        "src/fern/types/update_file_response.py",
        "src/fern/types/update_folder_response.py",
        "src/fern/types/update_shared_link_response.py",
        "src/fern/types/update_upload_session_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/updated_by.py",
        "src/fern/types/upload_session.py",
        "src/fern/types/webhook_event.py",
        "src/fern/upload_sessions/__init__.py",
        "src/fern/upload_sessions/client.py",
        "src/fern/upload_sessions/raw_client.py",
        "src/fern/version.py",
    ],
};

const APIDECK_ACCOUNTING: Corpus = Corpus {
    api: "apideck.com-accounting",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/balance_sheet/__init__.py",
        "src/fern/balance_sheet/client.py",
        "src/fern/balance_sheet/raw_client.py",
        "src/fern/bills/__init__.py",
        "src/fern/bills/client.py",
        "src/fern/bills/raw_client.py",
        "src/fern/client.py",
        "src/fern/company_info/__init__.py",
        "src/fern/company_info/client.py",
        "src/fern/company_info/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/credit_notes/__init__.py",
        "src/fern/credit_notes/client.py",
        "src/fern/credit_notes/raw_client.py",
        "src/fern/customers/__init__.py",
        "src/fern/customers/client.py",
        "src/fern/customers/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/invoice_items/__init__.py",
        "src/fern/invoice_items/client.py",
        "src/fern/invoice_items/raw_client.py",
        "src/fern/invoices/__init__.py",
        "src/fern/invoices/client.py",
        "src/fern/invoices/raw_client.py",
        "src/fern/journal_entries/__init__.py",
        "src/fern/journal_entries/client.py",
        "src/fern/journal_entries/raw_client.py",
        "src/fern/ledger_accounts/__init__.py",
        "src/fern/ledger_accounts/client.py",
        "src/fern/ledger_accounts/raw_client.py",
        "src/fern/payments/__init__.py",
        "src/fern/payments/client.py",
        "src/fern/payments/raw_client.py",
        "src/fern/profit_and_loss/__init__.py",
        "src/fern/profit_and_loss/client.py",
        "src/fern/profit_and_loss/raw_client.py",
        "src/fern/py.typed",
        "src/fern/suppliers/__init__.py",
        "src/fern/suppliers/client.py",
        "src/fern/suppliers/raw_client.py",
        "src/fern/tax_rates/__init__.py",
        "src/fern/tax_rates/client.py",
        "src/fern/tax_rates/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/accounting_customer.py",
        "src/fern/types/accounting_customer_status.py",
        "src/fern/types/accounting_event_type.py",
        "src/fern/types/accounting_webhook_event.py",
        "src/fern/types/active.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/balance_sheet.py",
        "src/fern/types/balance_sheet_assets.py",
        "src/fern/types/balance_sheet_assets_current_assets.py",
        "src/fern/types/balance_sheet_assets_current_assets_accounts_item.py",
        "src/fern/types/balance_sheet_assets_fixed_assets.py",
        "src/fern/types/balance_sheet_assets_fixed_assets_accounts_item.py",
        "src/fern/types/balance_sheet_equity.py",
        "src/fern/types/balance_sheet_equity_items_item.py",
        "src/fern/types/balance_sheet_filter.py",
        "src/fern/types/balance_sheet_liabilities.py",
        "src/fern/types/balance_sheet_liabilities_accounts_item.py",
        "src/fern/types/bank_account.py",
        "src/fern/types/bank_account_account_type.py",
        "src/fern/types/bill.py",
        "src/fern/types/bill_line_item.py",
        "src/fern/types/bill_line_item_type.py",
        "src/fern/types/bill_status.py",
        "src/fern/types/bills_sort.py",
        "src/fern/types/bills_sort_by.py",
        "src/fern/types/company.py",
        "src/fern/types/company_info.py",
        "src/fern/types/company_info_fiscal_year_start_month.py",
        "src/fern/types/company_info_status.py",
        "src/fern/types/company_name.py",
        "src/fern/types/company_row_type.py",
        "src/fern/types/contact.py",
        "src/fern/types/contact_gender.py",
        "src/fern/types/contact_type.py",
        "src/fern/types/create_bill_response.py",
        "src/fern/types/create_credit_note_response.py",
        "src/fern/types/create_customer_response.py",
        "src/fern/types/create_invoice_item_response.py",
        "src/fern/types/create_invoice_response.py",
        "src/fern/types/create_journal_entry_response.py",
        "src/fern/types/create_ledger_account_response.py",
        "src/fern/types/create_payment_response.py",
        "src/fern/types/create_supplier_response.py",
        "src/fern/types/create_tax_rate_response.py",
        "src/fern/types/created_at.py",
        "src/fern/types/created_by.py",
        "src/fern/types/credit_note.py",
        "src/fern/types/credit_note_allocations_item.py",
        "src/fern/types/credit_note_allocations_item_type.py",
        "src/fern/types/credit_note_status.py",
        "src/fern/types/credit_note_type.py",
        "src/fern/types/currency.py",
        "src/fern/types/currency_rate.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/customers_filter.py",
        "src/fern/types/delete_bill_response.py",
        "src/fern/types/delete_credit_note_response.py",
        "src/fern/types/delete_customer_response.py",
        "src/fern/types/delete_invoice_item_response.py",
        "src/fern/types/delete_invoice_response.py",
        "src/fern/types/delete_journal_entry_response.py",
        "src/fern/types/delete_ledger_account_response.py",
        "src/fern/types/delete_payment_response.py",
        "src/fern/types/delete_supplier_response.py",
        "src/fern/types/delete_tax_rate_response.py",
        "src/fern/types/downstream_id.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/first_name.py",
        "src/fern/types/get_balance_sheet_response.py",
        "src/fern/types/get_bill_response.py",
        "src/fern/types/get_bills_response.py",
        "src/fern/types/get_company_info_response.py",
        "src/fern/types/get_credit_note_response.py",
        "src/fern/types/get_credit_notes_response.py",
        "src/fern/types/get_customer_response.py",
        "src/fern/types/get_customers_response.py",
        "src/fern/types/get_invoice_item_response.py",
        "src/fern/types/get_invoice_items_response.py",
        "src/fern/types/get_invoice_response.py",
        "src/fern/types/get_invoices_response.py",
        "src/fern/types/get_journal_entries_response.py",
        "src/fern/types/get_journal_entry_response.py",
        "src/fern/types/get_ledger_account_response.py",
        "src/fern/types/get_ledger_accounts_response.py",
        "src/fern/types/get_payment_response.py",
        "src/fern/types/get_payments_response.py",
        "src/fern/types/get_profit_and_loss_response.py",
        "src/fern/types/get_supplier_response.py",
        "src/fern/types/get_suppliers_response.py",
        "src/fern/types/get_tax_rate_response.py",
        "src/fern/types/get_tax_rates_response.py",
        "src/fern/types/id.py",
        "src/fern/types/invoice.py",
        "src/fern/types/invoice_item.py",
        "src/fern/types/invoice_item_asset_account.py",
        "src/fern/types/invoice_item_expense_account.py",
        "src/fern/types/invoice_item_income_account.py",
        "src/fern/types/invoice_item_purchase_details.py",
        "src/fern/types/invoice_item_sales_details.py",
        "src/fern/types/invoice_item_type.py",
        "src/fern/types/invoice_items_filter.py",
        "src/fern/types/invoice_line_item.py",
        "src/fern/types/invoice_line_item_type.py",
        "src/fern/types/invoice_response.py",
        "src/fern/types/invoice_status.py",
        "src/fern/types/invoice_type.py",
        "src/fern/types/invoices_sort.py",
        "src/fern/types/invoices_sort_by.py",
        "src/fern/types/journal_entry.py",
        "src/fern/types/journal_entry_line_item.py",
        "src/fern/types/journal_entry_line_item_type.py",
        "src/fern/types/language.py",
        "src/fern/types/last_name.py",
        "src/fern/types/ledger_account.py",
        "src/fern/types/ledger_account_categories_item.py",
        "src/fern/types/ledger_account_classification.py",
        "src/fern/types/ledger_account_parent_account.py",
        "src/fern/types/ledger_account_status.py",
        "src/fern/types/ledger_account_sub_accounts_item.py",
        "src/fern/types/ledger_account_type.py",
        "src/fern/types/ledger_accounts.py",
        "src/fern/types/linked_customer.py",
        "src/fern/types/linked_invoice_item.py",
        "src/fern/types/linked_ledger_account.py",
        "src/fern/types/linked_parent_customer.py",
        "src/fern/types/linked_supplier.py",
        "src/fern/types/linked_tax_rate.py",
        "src/fern/types/linked_tracking_category.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/middle_name.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/pass_through_query.py",
        "src/fern/types/payment.py",
        "src/fern/types/payment_allocations_item.py",
        "src/fern/types/payment_allocations_item_type.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/payment_status.py",
        "src/fern/types/payment_type.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/profit_and_loss.py",
        "src/fern/types/profit_and_loss_expenses.py",
        "src/fern/types/profit_and_loss_filter.py",
        "src/fern/types/profit_and_loss_gross_profit.py",
        "src/fern/types/profit_and_loss_income.py",
        "src/fern/types/profit_and_loss_net_income.py",
        "src/fern/types/profit_and_loss_net_operating_income.py",
        "src/fern/types/profit_and_loss_record.py",
        "src/fern/types/profit_and_loss_records.py",
        "src/fern/types/profit_and_loss_records_item.py",
        "src/fern/types/profit_and_loss_section.py",
        "src/fern/types/quantity.py",
        "src/fern/types/row_version.py",
        "src/fern/types/sales_tax_number.py",
        "src/fern/types/social_link.py",
        "src/fern/types/sort_direction.py",
        "src/fern/types/suffix.py",
        "src/fern/types/supplier.py",
        "src/fern/types/supplier_status.py",
        "src/fern/types/suppliers_filter.py",
        "src/fern/types/tags.py",
        "src/fern/types/tax_inclusive.py",
        "src/fern/types/tax_number.py",
        "src/fern/types/tax_rate.py",
        "src/fern/types/tax_rate_components_item.py",
        "src/fern/types/tax_rate_status.py",
        "src/fern/types/tax_rates_filter.py",
        "src/fern/types/title.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unit_of_measure.py",
        "src/fern/types/unit_price.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_bill_response.py",
        "src/fern/types/update_credit_note_response.py",
        "src/fern/types/update_customer_response.py",
        "src/fern/types/update_invoice_items_response.py",
        "src/fern/types/update_invoice_response.py",
        "src/fern/types/update_journal_entry_response.py",
        "src/fern/types/update_ledger_account_response.py",
        "src/fern/types/update_payment_response.py",
        "src/fern/types/update_supplier_response.py",
        "src/fern/types/update_tax_rate_response.py",
        "src/fern/types/updated_at.py",
        "src/fern/types/updated_by.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/version.py",
    ],
};

const CALORIENINJAS: Corpus = Corpus {
    api: "calorieninjas.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    // Fern 5.20 cannot produce a valid tree for this spec. Its exact registered
    // upstream failure is covered at the process boundary instead of comparing
    // against the preserved, non-authoritative 4.35 output.
    matched: &[],
};

const EOS: Corpus = Corpus {
    api: "eos.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/connections_response_item.py",
        "src/fern/types/connections_response_item_last_handshake.py",
        "src/fern/types/status_response.py",
        "src/fern/types/status_response_last_handshake.py",
        "src/fern/version.py",
    ],
};

const APIDECK_SMS: Corpus = Corpus {
    api: "apideck.com-sms",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/messages/__init__.py",
        "src/fern/messages/client.py",
        "src/fern/messages/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/create_message_response.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/delete_message_response.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/get_message_response.py",
        "src/fern/types/get_messages_response.py",
        "src/fern/types/links.py",
        "src/fern/types/message.py",
        "src/fern/types/message_direction.py",
        "src/fern/types/message_error.py",
        "src/fern/types/message_price.py",
        "src/fern/types/message_status.py",
        "src/fern/types/message_type.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/tags.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_message_response.py",
        "src/fern/version.py",
    ],
};

const APIDECK_ECOSYSTEM: Corpus = Corpus {
    api: "apideck.com-ecosystem",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/category/__init__.py",
        "src/fern/category/client.py",
        "src/fern/category/raw_client.py",
        "src/fern/client.py",
        "src/fern/collection/__init__.py",
        "src/fern/collection/client.py",
        "src/fern/collection/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/ecosystem/__init__.py",
        "src/fern/ecosystem/client.py",
        "src/fern/ecosystem/raw_client.py",
        "src/fern/environment.py",
        "src/fern/listing/__init__.py",
        "src/fern/listing/client.py",
        "src/fern/listing/raw_client.py",
        "src/fern/product/__init__.py",
        "src/fern/product/client.py",
        "src/fern/product/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/card_settings.py",
        "src/fern/types/category.py",
        "src/fern/types/collection.py",
        "src/fern/types/contact.py",
        "src/fern/types/cta_settings.py",
        "src/fern/types/custom_settings.py",
        "src/fern/types/ecosystem.py",
        "src/fern/types/ecosystem_menu_position.py",
        "src/fern/types/ecosystem_menu_style.py",
        "src/fern/types/ecosystem_navigation_mobile_menu_type.py",
        "src/fern/types/file.py",
        "src/fern/types/file_type.py",
        "src/fern/types/get_categories_response.py",
        "src/fern/types/get_category_response.py",
        "src/fern/types/get_collection_response.py",
        "src/fern/types/get_collections_response.py",
        "src/fern/types/get_ecosystem_response.py",
        "src/fern/types/get_listing_response.py",
        "src/fern/types/get_listings_response.py",
        "src/fern/types/get_product_response.py",
        "src/fern/types/get_products_response.py",
        "src/fern/types/integration_settings.py",
        "src/fern/types/lead_form_settings.py",
        "src/fern/types/links.py",
        "src/fern/types/listing.py",
        "src/fern/types/listing_settings.py",
        "src/fern/types/listing_settings_naming.py",
        "src/fern/types/listing_settings_sidebar_position.py",
        "src/fern/types/logo.py",
        "src/fern/types/logo_type.py",
        "src/fern/types/masthead_settings.py",
        "src/fern/types/media.py",
        "src/fern/types/media_type.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/meta_tag_settings.py",
        "src/fern/types/partner.py",
        "src/fern/types/product.py",
        "src/fern/types/screenshot.py",
        "src/fern/types/translation.py",
        "src/fern/types/translations.py",
        "src/fern/version.py",
    ],
};

const APIDECK_CUSTOMER_SUPPORT: Corpus = Corpus {
    api: "apideck.com-customer-support",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/customers/__init__.py",
        "src/fern/customers/client.py",
        "src/fern/customers/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/bank_account.py",
        "src/fern/types/bank_account_account_type.py",
        "src/fern/types/company.py",
        "src/fern/types/company_name.py",
        "src/fern/types/company_row_type.py",
        "src/fern/types/contact.py",
        "src/fern/types/contact_gender.py",
        "src/fern/types/contact_type.py",
        "src/fern/types/create_customer_support_customer_response.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/customer_support_customer.py",
        "src/fern/types/customer_support_customer_status.py",
        "src/fern/types/delete_customer_support_customer_response.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/first_name.py",
        "src/fern/types/get_customer_support_customer_response.py",
        "src/fern/types/get_customer_support_customers_response.py",
        "src/fern/types/last_name.py",
        "src/fern/types/lead.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/opportunity.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/row_version.py",
        "src/fern/types/social_link.py",
        "src/fern/types/tags.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_customer_support_customer_response.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/version.py",
    ],
};

const APIDECK_LEAD: Corpus = Corpus {
    api: "apideck.com-lead",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/leads/__init__.py",
        "src/fern/leads/client.py",
        "src/fern/leads/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/address.py",
        "src/fern/types/address_type.py",
        "src/fern/types/bad_request_response.py",
        "src/fern/types/bad_request_response_detail.py",
        "src/fern/types/bank_account.py",
        "src/fern/types/bank_account_account_type.py",
        "src/fern/types/create_lead_response.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_field_value.py",
        "src/fern/types/delete_lead_response.py",
        "src/fern/types/email.py",
        "src/fern/types/email_type.py",
        "src/fern/types/get_lead_response.py",
        "src/fern/types/get_leads_response.py",
        "src/fern/types/lead.py",
        "src/fern/types/lead_event_type.py",
        "src/fern/types/lead_webhook_event.py",
        "src/fern/types/leads_filter.py",
        "src/fern/types/leads_sort.py",
        "src/fern/types/leads_sort_by.py",
        "src/fern/types/links.py",
        "src/fern/types/meta.py",
        "src/fern/types/meta_cursors.py",
        "src/fern/types/not_found_response.py",
        "src/fern/types/not_found_response_detail.py",
        "src/fern/types/not_implemented_response.py",
        "src/fern/types/not_implemented_response_detail.py",
        "src/fern/types/payment_required_response.py",
        "src/fern/types/phone_number.py",
        "src/fern/types/phone_number_type.py",
        "src/fern/types/row_version.py",
        "src/fern/types/social_link.py",
        "src/fern/types/sort_direction.py",
        "src/fern/types/tags.py",
        "src/fern/types/too_many_requests_response.py",
        "src/fern/types/too_many_requests_response_detail.py",
        "src/fern/types/unauthorized_response.py",
        "src/fern/types/unexpected_error_response.py",
        "src/fern/types/unexpected_error_response_detail.py",
        "src/fern/types/unified_id.py",
        "src/fern/types/unprocessable_response.py",
        "src/fern/types/update_lead_response.py",
        "src/fern/types/website.py",
        "src/fern/types/website_type.py",
        "src/fern/version.py",
    ],
};

const APACHE_ORG_AIRFLOW: Corpus = Corpus {
    api: "apache.org-airflow",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/config/__init__.py",
        "src/fern/config/client.py",
        "src/fern/config/raw_client.py",
        "src/fern/connection/__init__.py",
        "src/fern/connection/client.py",
        "src/fern/connection/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/dag/__init__.py",
        "src/fern/dag/client.py",
        "src/fern/dag/raw_client.py",
        "src/fern/dag/types/__init__.py",
        "src/fern/dag/types/get_dag_source_response.py",
        "src/fern/dag/types/update_task_instances_state_new_state.py",
        "src/fern/dag_run/__init__.py",
        "src/fern/dag_run/client.py",
        "src/fern/dag_run/raw_client.py",
        "src/fern/dag_run/types/__init__.py",
        "src/fern/dag_run/types/update_dag_run_state_state.py",
        "src/fern/dag_warning/__init__.py",
        "src/fern/dag_warning/client.py",
        "src/fern/dag_warning/raw_client.py",
        "src/fern/dataset/__init__.py",
        "src/fern/dataset/client.py",
        "src/fern/dataset/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/not_acceptable_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/event_log/__init__.py",
        "src/fern/event_log/client.py",
        "src/fern/event_log/raw_client.py",
        "src/fern/import_error/__init__.py",
        "src/fern/import_error/client.py",
        "src/fern/import_error/raw_client.py",
        "src/fern/monitoring/__init__.py",
        "src/fern/monitoring/client.py",
        "src/fern/monitoring/raw_client.py",
        "src/fern/permission/__init__.py",
        "src/fern/permission/client.py",
        "src/fern/permission/raw_client.py",
        "src/fern/plugin/__init__.py",
        "src/fern/plugin/client.py",
        "src/fern/plugin/raw_client.py",
        "src/fern/pool/__init__.py",
        "src/fern/pool/client.py",
        "src/fern/pool/raw_client.py",
        "src/fern/provider/__init__.py",
        "src/fern/provider/client.py",
        "src/fern/provider/raw_client.py",
        "src/fern/provider/types/__init__.py",
        "src/fern/provider/types/get_providers_response.py",
        "src/fern/py.typed",
        "src/fern/role/__init__.py",
        "src/fern/role/client.py",
        "src/fern/role/raw_client.py",
        "src/fern/task_instance/__init__.py",
        "src/fern/task_instance/client.py",
        "src/fern/task_instance/raw_client.py",
        "src/fern/task_instance/types/__init__.py",
        "src/fern/task_instance/types/get_log_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/action.py",
        "src/fern/types/action_collection.py",
        "src/fern/types/action_resource.py",
        "src/fern/types/basic_dag_run.py",
        "src/fern/types/class_reference.py",
        "src/fern/types/collection_info.py",
        "src/fern/types/color.py",
        "src/fern/types/config.py",
        "src/fern/types/config_option.py",
        "src/fern/types/config_section.py",
        "src/fern/types/connection.py",
        "src/fern/types/connection_collection.py",
        "src/fern/types/connection_collection_item.py",
        "src/fern/types/connection_test.py",
        "src/fern/types/cron_expression.py",
        "src/fern/types/dag.py",
        "src/fern/types/dag_collection.py",
        "src/fern/types/dag_detail.py",
        "src/fern/types/dag_run.py",
        "src/fern/types/dag_run_collection.py",
        "src/fern/types/dag_run_run_type.py",
        "src/fern/types/dag_schedule_dataset_reference.py",
        "src/fern/types/dag_state.py",
        "src/fern/types/dag_warning.py",
        "src/fern/types/dag_warning_collection.py",
        "src/fern/types/dataset.py",
        "src/fern/types/dataset_collection.py",
        "src/fern/types/dataset_event.py",
        "src/fern/types/dataset_event_collection.py",
        "src/fern/types/error.py",
        "src/fern/types/event_log.py",
        "src/fern/types/event_log_collection.py",
        "src/fern/types/extra_link.py",
        "src/fern/types/extra_link_collection.py",
        "src/fern/types/health_info.py",
        "src/fern/types/health_status.py",
        "src/fern/types/import_error.py",
        "src/fern/types/import_error_collection.py",
        "src/fern/types/job.py",
        "src/fern/types/metadatabase_status.py",
        "src/fern/types/plugin_collection.py",
        "src/fern/types/plugin_collection_item.py",
        "src/fern/types/pool.py",
        "src/fern/types/pool_collection.py",
        "src/fern/types/provider.py",
        "src/fern/types/provider_collection.py",
        "src/fern/types/relative_delta.py",
        "src/fern/types/resource.py",
        "src/fern/types/role.py",
        "src/fern/types/role_collection.py",
        "src/fern/types/schedule_interval.py",
        "src/fern/types/scheduler_status.py",
        "src/fern/types/set_task_instance_note.py",
        "src/fern/types/sla_miss.py",
        "src/fern/types/tag.py",
        "src/fern/types/task.py",
        "src/fern/types/task_collection.py",
        "src/fern/types/task_extra_links_item.py",
        "src/fern/types/task_instance.py",
        "src/fern/types/task_instance_collection.py",
        "src/fern/types/task_instance_reference.py",
        "src/fern/types/task_instance_reference_collection.py",
        "src/fern/types/task_outlet_dataset_reference.py",
        "src/fern/types/task_state.py",
        "src/fern/types/time_delta.py",
        "src/fern/types/timezone.py",
        "src/fern/types/trigger.py",
        "src/fern/types/trigger_rule.py",
        "src/fern/types/update_task_instance.py",
        "src/fern/types/update_task_instance_new_state.py",
        "src/fern/types/user.py",
        "src/fern/types/user_collection.py",
        "src/fern/types/user_collection_item.py",
        "src/fern/types/user_collection_item_roles_item.py",
        "src/fern/types/variable.py",
        "src/fern/types/variable_collection.py",
        "src/fern/types/variable_collection_item.py",
        "src/fern/types/version_info.py",
        "src/fern/types/weight_rule.py",
        "src/fern/types/x_com.py",
        "src/fern/types/x_com_collection.py",
        "src/fern/types/x_com_collection_item.py",
        "src/fern/user/__init__.py",
        "src/fern/user/client.py",
        "src/fern/user/raw_client.py",
        "src/fern/variable/__init__.py",
        "src/fern/variable/client.py",
        "src/fern/variable/raw_client.py",
        "src/fern/version.py",
        "src/fern/x_com/__init__.py",
        "src/fern/x_com/client.py",
        "src/fern/x_com/raw_client.py",
    ],
};

const OPENFIGI: Corpus = Corpus {
    api: "openfigi.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/content_too_large_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/not_acceptable_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/bulk_mapping_job.py",
        "src/fern/types/bulk_mapping_job_result.py",
        "src/fern/types/figi_result.py",
        "src/fern/types/get_mapping_values_key_request_key.py",
        "src/fern/types/get_mapping_values_key_response.py",
        "src/fern/types/mapping_job.py",
        "src/fern/types/mapping_job_id_type.py",
        "src/fern/types/mapping_job_id_value.py",
        "src/fern/types/mapping_job_option_type.py",
        "src/fern/types/mapping_job_result.py",
        "src/fern/types/mapping_job_result_figi_list.py",
        "src/fern/types/mapping_job_result_figi_not_found.py",
        "src/fern/types/mapping_job_state_code.py",
        "src/fern/types/nullable_date_interval.py",
        "src/fern/types/nullable_number_interval.py",
        "src/fern/version.py",
    ],
};

const TWILIO_VOICE_V1: Corpus = Corpus {
    api: "twilio.com-twilio_voice_v1",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/create_byoc_trunk_request_status_callback_method.py",
        "src/fern/types/create_byoc_trunk_request_voice_fallback_method.py",
        "src/fern/types/create_byoc_trunk_request_voice_method.py",
        "src/fern/types/list_byoc_trunk_response.py",
        "src/fern/types/list_byoc_trunk_response_meta.py",
        "src/fern/types/list_connection_policy_response.py",
        "src/fern/types/list_connection_policy_response_meta.py",
        "src/fern/types/list_connection_policy_target_response.py",
        "src/fern/types/list_connection_policy_target_response_meta.py",
        "src/fern/types/list_dialing_permissions_country_response.py",
        "src/fern/types/list_dialing_permissions_country_response_meta.py",
        "src/fern/types/list_dialing_permissions_hrs_prefixes_response.py",
        "src/fern/types/list_dialing_permissions_hrs_prefixes_response_meta.py",
        "src/fern/types/list_ip_record_response.py",
        "src/fern/types/list_ip_record_response_meta.py",
        "src/fern/types/list_source_ip_mapping_response.py",
        "src/fern/types/list_source_ip_mapping_response_meta.py",
        "src/fern/types/update_byoc_trunk_request_status_callback_method.py",
        "src/fern/types/update_byoc_trunk_request_voice_fallback_method.py",
        "src/fern/types/update_byoc_trunk_request_voice_method.py",
        "src/fern/types/voice_v1archived_call.py",
        "src/fern/types/voice_v1byoc_trunk.py",
        "src/fern/types/voice_v1byoc_trunk_status_callback_method.py",
        "src/fern/types/voice_v1byoc_trunk_voice_fallback_method.py",
        "src/fern/types/voice_v1byoc_trunk_voice_method.py",
        "src/fern/types/voice_v1connection_policy.py",
        "src/fern/types/voice_v1connection_policy_connection_policy_target.py",
        "src/fern/types/voice_v1dialing_permissions.py",
        "src/fern/types/voice_v1dialing_permissions_dialing_permissions_country.py",
        "src/fern/types/voice_v1dialing_permissions_dialing_permissions_country_bulk_update.py",
        "src/fern/types/voice_v1dialing_permissions_dialing_permissions_country_dialing_permissions_hrs_prefixes.py",
        "src/fern/types/voice_v1dialing_permissions_dialing_permissions_country_instance.py",
        "src/fern/types/voice_v1dialing_permissions_dialing_permissions_settings.py",
        "src/fern/types/voice_v1ip_record.py",
        "src/fern/types/voice_v1source_ip_mapping.py",
        "src/fern/version.py",
    ],
};

const MICROCKS_LOCAL: Corpus = Corpus {
    api: "microcks.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/config/__init__.py",
        "src/fern/config/client.py",
        "src/fern/config/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/job/__init__.py",
        "src/fern/job/client.py",
        "src/fern/job/raw_client.py",
        "src/fern/metrics/__init__.py",
        "src/fern/metrics/client.py",
        "src/fern/metrics/raw_client.py",
        "src/fern/mock/__init__.py",
        "src/fern/mock/client.py",
        "src/fern/mock/raw_client.py",
        "src/fern/mock/types/__init__.py",
        "src/fern/mock/types/get_service_response.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/test/__init__.py",
        "src/fern/test/client.py",
        "src/fern/test/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/abstract_exchange.py",
        "src/fern/types/abstract_exchange_type.py",
        "src/fern/types/binding.py",
        "src/fern/types/binding_type.py",
        "src/fern/types/counter.py",
        "src/fern/types/counter_map.py",
        "src/fern/types/daily_invocation_statistic.py",
        "src/fern/types/event_message.py",
        "src/fern/types/exchange.py",
        "src/fern/types/features_config.py",
        "src/fern/types/features_config_async_api.py",
        "src/fern/types/features_config_microcks_hub.py",
        "src/fern/types/features_config_repository_filter.py",
        "src/fern/types/features_config_repository_tenancy.py",
        "src/fern/types/header.py",
        "src/fern/types/header_dto.py",
        "src/fern/types/import_job.py",
        "src/fern/types/keycloak_config.py",
        "src/fern/types/keycloak_config_ssl_required.py",
        "src/fern/types/labels_map.py",
        "src/fern/types/message_array.py",
        "src/fern/types/metadata.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/operation.py",
        "src/fern/types/operation_headers.py",
        "src/fern/types/parameter_constraint.py",
        "src/fern/types/parameter_constraint_in.py",
        "src/fern/types/request.py",
        "src/fern/types/request_response_pair.py",
        "src/fern/types/resource.py",
        "src/fern/types/resource_type.py",
        "src/fern/types/response.py",
        "src/fern/types/secret.py",
        "src/fern/types/secret_ref.py",
        "src/fern/types/service.py",
        "src/fern/types/service_ref.py",
        "src/fern/types/service_type.py",
        "src/fern/types/service_view.py",
        "src/fern/types/string_array.py",
        "src/fern/types/test_case_result.py",
        "src/fern/types/test_conformance_metric.py",
        "src/fern/types/test_result.py",
        "src/fern/types/test_result_summary.py",
        "src/fern/types/test_return.py",
        "src/fern/types/test_runner_type.py",
        "src/fern/types/test_step_result.py",
        "src/fern/types/trend.py",
        "src/fern/types/unidirectional_event.py",
        "src/fern/types/weighted_metric_value.py",
        "src/fern/version.py",
    ],
};

const REDHAT_CATALOG_INVENTORY: Corpus = Corpus {
    api: "redhat.com-catalog_inventory",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/service_credential/__init__.py",
        "src/fern/service_credential/client.py",
        "src/fern/service_credential/raw_client.py",
        "src/fern/service_credential_type/__init__.py",
        "src/fern/service_credential_type/client.py",
        "src/fern/service_credential_type/raw_client.py",
        "src/fern/service_instance/__init__.py",
        "src/fern/service_instance/client.py",
        "src/fern/service_instance/raw_client.py",
        "src/fern/service_inventory/__init__.py",
        "src/fern/service_inventory/client.py",
        "src/fern/service_inventory/raw_client.py",
        "src/fern/service_offering/__init__.py",
        "src/fern/service_offering/client.py",
        "src/fern/service_offering/raw_client.py",
        "src/fern/service_offering/types/__init__.py",
        "src/fern/service_offering/types/order_service_offering_response.py",
        "src/fern/service_offering_node/__init__.py",
        "src/fern/service_offering_node/client.py",
        "src/fern/service_offering_node/raw_client.py",
        "src/fern/service_plan/__init__.py",
        "src/fern/service_plan/client.py",
        "src/fern/service_plan/raw_client.py",
        "src/fern/source/__init__.py",
        "src/fern/source/client.py",
        "src/fern/source/raw_client.py",
        "src/fern/tags/__init__.py",
        "src/fern/tags/client.py",
        "src/fern/tags/raw_client.py",
        "src/fern/task/__init__.py",
        "src/fern/task/client.py",
        "src/fern/task/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/check_availability_task.py",
        "src/fern/types/collection_links.py",
        "src/fern/types/collection_metadata.py",
        "src/fern/types/error_not_found.py",
        "src/fern/types/error_not_found_errors_item.py",
        "src/fern/types/full_refresh_persister_task.py",
        "src/fern/types/full_refresh_upload_task.py",
        "src/fern/types/graph_ql_response.py",
        "src/fern/types/id.py",
        "src/fern/types/incremental_refresh_upload_task.py",
        "src/fern/types/launch_job_task.py",
        "src/fern/types/order_parameters_service_plan.py",
        "src/fern/types/service_credential.py",
        "src/fern/types/service_credential_type.py",
        "src/fern/types/service_credential_types_collection.py",
        "src/fern/types/service_credentials_collection.py",
        "src/fern/types/service_instance.py",
        "src/fern/types/service_instance_node.py",
        "src/fern/types/service_instance_nodes_collection.py",
        "src/fern/types/service_instances_collection.py",
        "src/fern/types/service_inventories_collection.py",
        "src/fern/types/service_inventory.py",
        "src/fern/types/service_offering.py",
        "src/fern/types/service_offering_icon.py",
        "src/fern/types/service_offering_icons_collection.py",
        "src/fern/types/service_offering_node.py",
        "src/fern/types/service_offering_nodes_collection.py",
        "src/fern/types/service_offerings_collection.py",
        "src/fern/types/service_plan.py",
        "src/fern/types/service_plans_collection.py",
        "src/fern/types/source.py",
        "src/fern/types/sources_collection.py",
        "src/fern/types/tag.py",
        "src/fern/types/tags_collection.py",
        "src/fern/types/task.py",
        "src/fern/types/task_state.py",
        "src/fern/types/task_status.py",
        "src/fern/types/tasks_collection.py",
        "src/fern/types/tenant.py",
        "src/fern/types/towing_task.py",
        "src/fern/types/uuid_.py",
        "src/fern/version.py",
    ],
};

const XERO_PAYROLL_AU: Corpus = Corpus {
    api: "xero.com-xero-payroll-au",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/payroll_au/__init__.py",
        "src/fern/payroll_au/client.py",
        "src/fern/payroll_au/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/account.py",
        "src/fern/types/account_type.py",
        "src/fern/types/allowance_type.py",
        "src/fern/types/api_exception.py",
        "src/fern/types/bank_account.py",
        "src/fern/types/calendar_type.py",
        "src/fern/types/deduction_line.py",
        "src/fern/types/deduction_type.py",
        "src/fern/types/deduction_type_calculation_type.py",
        "src/fern/types/deduction_type_deduction_category.py",
        "src/fern/types/earnings_line.py",
        "src/fern/types/earnings_rate.py",
        "src/fern/types/earnings_rate_calculation_type.py",
        "src/fern/types/earnings_type.py",
        "src/fern/types/employee.py",
        "src/fern/types/employee_gender.py",
        "src/fern/types/employee_status.py",
        "src/fern/types/employees.py",
        "src/fern/types/employment_basis.py",
        "src/fern/types/employment_termination_payment_type.py",
        "src/fern/types/entitlement_final_pay_payout_type.py",
        "src/fern/types/home_address.py",
        "src/fern/types/leave_accrual_line.py",
        "src/fern/types/leave_application.py",
        "src/fern/types/leave_applications.py",
        "src/fern/types/leave_balance.py",
        "src/fern/types/leave_earnings_line.py",
        "src/fern/types/leave_line.py",
        "src/fern/types/leave_line_calculation_type.py",
        "src/fern/types/leave_lines.py",
        "src/fern/types/leave_period.py",
        "src/fern/types/leave_period_status.py",
        "src/fern/types/leave_type.py",
        "src/fern/types/leave_type_contribution_type.py",
        "src/fern/types/manual_tax_type.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/opening_balances.py",
        "src/fern/types/pay_item.py",
        "src/fern/types/pay_items.py",
        "src/fern/types/pay_run.py",
        "src/fern/types/pay_run_status.py",
        "src/fern/types/pay_runs.py",
        "src/fern/types/pay_template.py",
        "src/fern/types/payment_frequency_type.py",
        "src/fern/types/payroll_calendar.py",
        "src/fern/types/payroll_calendars.py",
        "src/fern/types/payslip.py",
        "src/fern/types/payslip_lines.py",
        "src/fern/types/payslip_object.py",
        "src/fern/types/payslip_summary.py",
        "src/fern/types/payslips.py",
        "src/fern/types/rate_type.py",
        "src/fern/types/reimbursement_line.py",
        "src/fern/types/reimbursement_lines.py",
        "src/fern/types/reimbursement_type.py",
        "src/fern/types/residency_status.py",
        "src/fern/types/settings.py",
        "src/fern/types/settings_object.py",
        "src/fern/types/settings_tracking_categories.py",
        "src/fern/types/settings_tracking_categories_employee_groups.py",
        "src/fern/types/settings_tracking_categories_timesheet_categories.py",
        "src/fern/types/state.py",
        "src/fern/types/super_fund.py",
        "src/fern/types/super_fund_product.py",
        "src/fern/types/super_fund_products.py",
        "src/fern/types/super_fund_type.py",
        "src/fern/types/super_funds.py",
        "src/fern/types/super_line.py",
        "src/fern/types/super_membership.py",
        "src/fern/types/superannuation_calculation_type.py",
        "src/fern/types/superannuation_contribution_type.py",
        "src/fern/types/superannuation_line.py",
        "src/fern/types/tax_declaration.py",
        "src/fern/types/tax_line.py",
        "src/fern/types/tfn_exemption_type.py",
        "src/fern/types/timesheet.py",
        "src/fern/types/timesheet_line.py",
        "src/fern/types/timesheet_lines.py",
        "src/fern/types/timesheet_object.py",
        "src/fern/types/timesheet_status.py",
        "src/fern/types/timesheets.py",
        "src/fern/types/validation_error.py",
        "src/fern/version.py",
    ],
};

const TRACCAR: Corpus = Corpus {
    api: "traccar.org",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "README.md",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/attributes/__init__.py",
        "src/fern/attributes/client.py",
        "src/fern/attributes/raw_client.py",
        "src/fern/calendars/__init__.py",
        "src/fern/calendars/client.py",
        "src/fern/calendars/raw_client.py",
        "src/fern/client.py",
        "src/fern/commands/__init__.py",
        "src/fern/commands/client.py",
        "src/fern/commands/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/devices/__init__.py",
        "src/fern/devices/client.py",
        "src/fern/devices/raw_client.py",
        "src/fern/drivers/__init__.py",
        "src/fern/drivers/client.py",
        "src/fern/drivers/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/events/__init__.py",
        "src/fern/events/client.py",
        "src/fern/events/raw_client.py",
        "src/fern/geofences/__init__.py",
        "src/fern/geofences/client.py",
        "src/fern/geofences/raw_client.py",
        "src/fern/groups/__init__.py",
        "src/fern/groups/client.py",
        "src/fern/groups/raw_client.py",
        "src/fern/maintenance/__init__.py",
        "src/fern/maintenance/client.py",
        "src/fern/maintenance/raw_client.py",
        "src/fern/notifications/__init__.py",
        "src/fern/notifications/client.py",
        "src/fern/notifications/raw_client.py",
        "src/fern/permissions/__init__.py",
        "src/fern/permissions/client.py",
        "src/fern/permissions/raw_client.py",
        "src/fern/positions/__init__.py",
        "src/fern/positions/client.py",
        "src/fern/positions/raw_client.py",
        "src/fern/py.typed",
        "src/fern/reports/__init__.py",
        "src/fern/reports/client.py",
        "src/fern/reports/raw_client.py",
        "src/fern/server/__init__.py",
        "src/fern/server/client.py",
        "src/fern/server/raw_client.py",
        "src/fern/session/__init__.py",
        "src/fern/session/client.py",
        "src/fern/session/raw_client.py",
        "src/fern/statistics/__init__.py",
        "src/fern/statistics/client.py",
        "src/fern/statistics/raw_client.py",
        "src/fern/types/attribute.py",
        "src/fern/types/calendar.py",
        "src/fern/types/calendar_attributes.py",
        "src/fern/types/command.py",
        "src/fern/types/command_attributes.py",
        "src/fern/types/command_type.py",
        "src/fern/types/device.py",
        "src/fern/types/device_attributes.py",
        "src/fern/types/driver.py",
        "src/fern/types/driver_attributes.py",
        "src/fern/types/event.py",
        "src/fern/types/event_attributes.py",
        "src/fern/types/geofence.py",
        "src/fern/types/geofence_attributes.py",
        "src/fern/types/group.py",
        "src/fern/types/group_attributes.py",
        "src/fern/types/__init__.py",
        "src/fern/types/maintenance.py",
        "src/fern/types/maintenance_attributes.py",
        "src/fern/types/notification.py",
        "src/fern/types/notification_attributes.py",
        "src/fern/types/notification_type.py",
        "src/fern/types/permission.py",
        "src/fern/types/position.py",
        "src/fern/types/position_attributes.py",
        "src/fern/types/position_network.py",
        "src/fern/types/report_stops.py",
        "src/fern/types/report_summary.py",
        "src/fern/types/report_trips.py",
        "src/fern/types/server.py",
        "src/fern/types/server_attributes.py",
        "src/fern/types/statistics.py",
        "src/fern/types/user.py",
        "src/fern/types/user_attributes.py",
        "src/fern/users/__init__.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/version.py",
    ],
};

const REVERB_COM: Corpus = Corpus {
    api: "reverb.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "README.md",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/articles/__init__.py",
        "src/fern/articles/client.py",
        "src/fern/articles/raw_client.py",
        "src/fern/categories/__init__.py",
        "src/fern/categories/client.py",
        "src/fern/categories/raw_client.py",
        "src/fern/client.py",
        "src/fern/comparison_shopping_pages/__init__.py",
        "src/fern/comparison_shopping_pages/client.py",
        "src/fern/comparison_shopping_pages/raw_client.py",
        "src/fern/conversations/__init__.py",
        "src/fern/conversations/client.py",
        "src/fern/conversations/raw_client.py",
        "src/fern/conversations/types/__init__.py",
        "src/fern/conversations/types/post_conversations_conversation_id_offer_request_offer_items_item.py",
        "src/fern/conversations/types/post_conversations_conversation_id_offer_request_price.py",
        "src/fern/conversations/types/post_conversations_conversation_id_offer_request_price_currency.py",
        "src/fern/conversations/types/post_conversations_conversation_id_offer_request_shipping_price.py",
        "src/fern/conversations/types/post_conversations_conversation_id_offer_request_shipping_price_currency.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/countries/__init__.py",
        "src/fern/countries/client.py",
        "src/fern/countries/raw_client.py",
        "src/fern/csps/__init__.py",
        "src/fern/csps/client.py",
        "src/fern/csps/raw_client.py",
        "src/fern/curated_sets/__init__.py",
        "src/fern/curated_sets/client.py",
        "src/fern/curated_sets/raw_client.py",
        "src/fern/currencies/__init__.py",
        "src/fern/currencies/client.py",
        "src/fern/currencies/raw_client.py",
        "src/fern/environment.py",
        "src/fern/feedback/__init__.py",
        "src/fern/feedback/client.py",
        "src/fern/feedback/raw_client.py",
        "src/fern/handpicked/__init__.py",
        "src/fern/handpicked/client.py",
        "src/fern/handpicked/raw_client.py",
        "src/fern/listing_conditions/__init__.py",
        "src/fern/listing_conditions/client.py",
        "src/fern/listing_conditions/raw_client.py",
        "src/fern/listings/__init__.py",
        "src/fern/listings/client.py",
        "src/fern/listings/raw_client.py",
        "src/fern/listings/types/__init__.py",
        "src/fern/listings/types/post_listings_request_categories_item.py",
        "src/fern/listings/types/post_listings_request_condition.py",
        "src/fern/listings/types/post_listings_request_condition_uuid.py",
        "src/fern/listings/types/post_listings_request_exclusive_channel.py",
        "src/fern/listings/types/post_listings_request_location.py",
        "src/fern/listings/types/post_listings_request_preorder_info.py",
        "src/fern/listings/types/post_listings_request_preorder_info_lead_time_unit.py",
        "src/fern/listings/types/post_listings_request_price.py",
        "src/fern/listings/types/post_listings_request_price_currency.py",
        "src/fern/listings/types/post_listings_request_seller.py",
        "src/fern/listings/types/post_listings_request_shipping.py",
        "src/fern/listings/types/post_listings_request_shipping_rates_item.py",
        "src/fern/listings/types/post_listings_request_shipping_rates_item_rate.py",
        "src/fern/listings/types/post_listings_request_shipping_rates_item_rate_currency.py",
        "src/fern/listings/types/post_listings_request_videos_item.py",
        "src/fern/listings/types/put_listings_slug_request_categories_item.py",
        "src/fern/listings/types/put_listings_slug_request_condition.py",
        "src/fern/listings/types/put_listings_slug_request_condition_uuid.py",
        "src/fern/listings/types/put_listings_slug_request_exclusive_channel.py",
        "src/fern/listings/types/put_listings_slug_request_location.py",
        "src/fern/listings/types/put_listings_slug_request_preorder_info.py",
        "src/fern/listings/types/put_listings_slug_request_preorder_info_lead_time_unit.py",
        "src/fern/listings/types/put_listings_slug_request_price.py",
        "src/fern/listings/types/put_listings_slug_request_price_currency.py",
        "src/fern/listings/types/put_listings_slug_request_seller.py",
        "src/fern/listings/types/put_listings_slug_request_shipping.py",
        "src/fern/listings/types/put_listings_slug_request_shipping_rates_item.py",
        "src/fern/listings/types/put_listings_slug_request_shipping_rates_item_rate.py",
        "src/fern/listings/types/put_listings_slug_request_shipping_rates_item_rate_currency.py",
        "src/fern/listings/types/put_listings_slug_request_videos_item.py",
        "src/fern/my/__init__.py",
        "src/fern/my/client.py",
        "src/fern/my/raw_client.py",
        "src/fern/my/types/__init__.py",
        "src/fern/my/types/post_my_follows_search_request_currency.py",
        "src/fern/my/types/post_my_follows_search_request_listing_type.py",
        "src/fern/my/types/post_my_negotiations_id_counter_request_offer_items_item.py",
        "src/fern/my/types/post_my_negotiations_id_counter_request_price.py",
        "src/fern/my/types/post_my_negotiations_id_counter_request_price_currency.py",
        "src/fern/my/types/post_my_negotiations_id_counter_request_shipping_price.py",
        "src/fern/my/types/post_my_negotiations_id_counter_request_shipping_price_currency.py",
        "src/fern/my/types/put_my_listings_slug_state_end_request_reason.py",
        "src/fern/orders/__init__.py",
        "src/fern/orders/client.py",
        "src/fern/orders/raw_client.py",
        "src/fern/payment_methods/__init__.py",
        "src/fern/payment_methods/client.py",
        "src/fern/payment_methods/raw_client.py",
        "src/fern/priceguide/__init__.py",
        "src/fern/priceguide/client.py",
        "src/fern/priceguide/raw_client.py",
        "src/fern/products/__init__.py",
        "src/fern/products/client.py",
        "src/fern/products/raw_client.py",
        "src/fern/py.typed",
        "src/fern/sales/__init__.py",
        "src/fern/sales/client.py",
        "src/fern/sales/raw_client.py",
        "src/fern/shipping/__init__.py",
        "src/fern/shipping/client.py",
        "src/fern/shipping/raw_client.py",
        "src/fern/shop/__init__.py",
        "src/fern/shop/client.py",
        "src/fern/shop/raw_client.py",
        "src/fern/shop/types/__init__.py",
        "src/fern/shop/types/put_shop_request_address.py",
        "src/fern/shop/types/put_shop_request_currency.py",
        "src/fern/shop/types/put_shop_request_legal_country_code.py",
        "src/fern/shop/types/put_shop_request_shop_type.py",
        "src/fern/shops/__init__.py",
        "src/fern/shops/client.py",
        "src/fern/shops/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/version.py",
        "src/fern/wants/__init__.py",
        "src/fern/wants/client.py",
        "src/fern/wants/raw_client.py",
        "src/fern/webhooks/__init__.py",
        "src/fern/webhooks/client.py",
        "src/fern/webhooks/raw_client.py",
        "src/fern/webhooks/types/__init__.py",
        "src/fern/webhooks/types/post_webhooks_registrations_request_topic.py",
    ],
};

const MAIF_OTOROSHI: Corpus = Corpus {
    api: "maif.local-otoroshi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: MAIF_OTOROSHI_MATCHED,
};

const PORTFOLIOOPTIMIZER_IO: Corpus = Corpus {
    api: "portfoliooptimizer.io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/factors/__init__.py",
        "src/fern/factors/types/__init__.py",
        "src/fern/factors/types/post_factors_residualization_request_factors_item.py",
        "src/fern/factors/types/post_factors_residualization_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_request_risk_free_rate.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_request_risk_free_rate_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_request_risk_free_returns.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_request_risk_free_returns_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_alpha_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_request_risk_free_rate.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_request_risk_free_rate_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_request_risk_free_returns.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_request_risk_free_returns_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_beta_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_conditional_value_at_risk_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_conditional_value_at_risk_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_conditional_value_at_risk_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_return_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_return_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_return_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_risk_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_risk_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_contributions_risk_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_drawdowns_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_drawdowns_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_drawdowns_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_drawdowns_response_portfolios_item_portfolio_worst_drawdowns_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_effective_number_of_bets_request_factors_extraction_method.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_effective_number_of_bets_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_effective_number_of_bets_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_effective_number_of_bets_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_factors_exposures_request_factors_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_factors_exposures_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_factors_exposures_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_factors_exposures_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_efficient_frontier_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_efficient_frontier_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_minimum_variance_frontier_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_minimum_variance_frontier_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_request_assets.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_request_assets_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_returns_average_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_returns_average_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_returns_average_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_tracking_error_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_tracking_error_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_tracking_error_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_index_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_index_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_index_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_performance_index_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_performance_index_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_ulcer_performance_index_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_value_at_risk_request_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_value_at_risk_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_value_at_risk_response_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_request_assets.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_request_assets_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_response.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_response_portfolios_item.py",
        "src/fern/portfolio_construction/__init__.py",
        "src/fern/portfolio_construction/types/__init__.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_investable_response.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_mimicking_request_assets_item.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_mimicking_response.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_random_request_constraints.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_random_response.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_random_response_portfolios_item.py",
        "src/fern/portfolio_optimization/__init__.py",
        "src/fern/portfolio_optimization/types/__init__.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_equal_risk_contributions_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_equal_risk_contributions_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_equal_sharpe_ratio_contributions_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_equal_volatility_weighted_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_equal_weighted_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_across_cluster_allocation_method.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_method.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_ordering.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_within_cluster_allocation_method.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_clustering_based_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_request_clustering_method.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_request_clustering_ordering.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_hierarchical_risk_parity_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_inverse_variance_weighted_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_inverse_volatility_weighted_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_market_capitalization_weighted_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_maximum_decorrelation_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_maximum_ulcer_performance_index_request_assets_item.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_maximum_ulcer_performance_index_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_minimum_correlation_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_minimum_ulcer_index_request_assets_item.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_minimum_ulcer_index_response.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_most_diversified_response.py",
        "src/fern/portfolio_simulation/__init__.py",
        "src/fern/portfolio_simulation/types/__init__.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_drift_weight_request_assets_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_drift_weight_request_portfolios_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_drift_weight_response.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_drift_weight_response_portfolios_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_fixed_weight_request_assets_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_fixed_weight_request_portfolios_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_fixed_weight_response.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_fixed_weight_response_portfolios_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_random_weight_request_assets_item.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_random_weight_response.py",
        "src/fern/portfolio_simulation/types/post_portfolio_simulation_rebalancing_random_weight_response_portfolios_item.py",
        "src/fern/py.typed",
        "src/fern/version.py",
        "src/fern/assets_analysis/__init__.py",
        "src/fern/assets_analysis/types/__init__.py",
        "src/fern/assets_analysis/types/post_assets_analysis_absorption_ratio_request_assets_covariance_matrix_eigenvectors.py",
        "src/fern/assets_analysis/types/post_assets_analysis_absorption_ratio_response.py",
        "src/fern/assets_analysis/types/post_assets_analysis_turbulence_index_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_bounds_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_denoised_request_denoising_method.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_denoised_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_distance_request_distance_metric.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_distance_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_effective_rank_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_informativeness_request_distance_metric.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_informativeness_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_nearest_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_random_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_request_assets_covariance_matrix.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_shrinkage_request.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_shrinkage_request_target_correlation_matrix.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix_target_equicorrelation_matrix.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_shrinkage_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_theory_implied_request_clustering_method.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_theory_implied_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_validation_response.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_validation_response_message.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_effective_rank_response.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_exponentially_weighted_request_assets_item.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_exponentially_weighted_response.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_request_assets_variances.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_response.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_validation_response.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_validation_response_message.py",
        "src/fern/assets_kurtosis/__init__.py",
        "src/fern/assets_kurtosis/types/__init__.py",
        "src/fern/assets_kurtosis/types/post_assets_kurtosis_request_assets_item.py",
        "src/fern/assets_kurtosis/types/post_assets_kurtosis_response.py",
        "src/fern/assets_kurtosis/types/post_assets_kurtosis_response_assets_item.py",
        "src/fern/assets_prices/__init__.py",
        "src/fern/assets_prices/types/__init__.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_request_assets_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_request_assets_item_asset_dividends_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_request_assets_item_asset_prices_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_request_assets_item_asset_splits_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_response.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_response_assets_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_forward_response_assets_item_asset_adjusted_prices_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_request_assets_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_request_assets_item_asset_dividends_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_request_assets_item_asset_prices_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_request_assets_item_asset_splits_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_response.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_response_assets_item.py",
        "src/fern/assets_prices/types/post_assets_prices_adjusted_response_assets_item_asset_adjusted_prices_item.py",
        "src/fern/assets_returns/__init__.py",
        "src/fern/assets_returns/types/__init__.py",
        "src/fern/assets_returns/types/post_assets_returns_average_request_assets_item.py",
        "src/fern/assets_returns/types/post_assets_returns_average_response.py",
        "src/fern/assets_returns/types/post_assets_returns_average_response_assets_item.py",
        "src/fern/assets_returns/types/post_assets_returns_request_assets_item.py",
        "src/fern/assets_returns/types/post_assets_returns_response.py",
        "src/fern/assets_returns/types/post_assets_returns_response_assets_item.py",
        "src/fern/assets_returns_simulation/__init__.py",
        "src/fern/assets_returns_simulation/types/__init__.py",
        "src/fern/assets_returns_simulation/types/post_assets_returns_simulation_bootstrap_request_assets_item.py",
        "src/fern/assets_returns_simulation/types/post_assets_returns_simulation_bootstrap_request_bootstrap_method.py",
        "src/fern/assets_returns_simulation/types/post_assets_returns_simulation_bootstrap_response.py",
        "src/fern/assets_returns_simulation/types/post_assets_returns_simulation_bootstrap_response_simulations_item.py",
        "src/fern/assets_returns_simulation/types/post_assets_returns_simulation_bootstrap_response_simulations_item_assets_item.py",
        "src/fern/assets_skewness/__init__.py",
        "src/fern/assets_skewness/types/__init__.py",
        "src/fern/assets_skewness/types/post_assets_skewness_request_assets_item.py",
        "src/fern/assets_skewness/types/post_assets_skewness_response.py",
        "src/fern/assets_skewness/types/post_assets_skewness_response_assets_item.py",
        "src/fern/assets_variance/raw_client.py",
        "src/fern/assets_variance/types/post_assets_variance_request_assets.py",
        "src/fern/assets_variance/types/post_assets_variance_request_assets_assets_item.py",
        "src/fern/assets_variance/types/post_assets_variance_request_assets_covariance_matrix.py",
        "src/fern/assets_variance/types/post_assets_variance_response.py",
        "src/fern/assets_variance/types/post_assets_variance_response_assets_item.py",
        "src/fern/assets_volatility/raw_client.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request_assets.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request_assets_assets_item.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request_assets_covariance_matrix.py",
        "src/fern/assets_volatility/types/post_assets_volatility_response.py",
        "src/fern/assets_volatility/types/post_assets_volatility_response_assets_item.py",
        "src/fern/client.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_efficient_frontier_request_constraints.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_mean_variance_minimum_variance_frontier_request_constraints.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_bias_adjusted_request_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_bias_adjusted_response.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_bias_adjusted_response_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_confidence_interval_request_confidence_interval_type.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_confidence_interval_request_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_confidence_interval_response.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_confidence_interval_response_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_request.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_response.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_probabilistic_response_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_request_assets.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_request_assets_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_response.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_response_portfolios_item.py",
        "src/fern/portfolio_construction/types/post_portfolio_construction_mimicking_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_maximum_decorrelation_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_maximum_ulcer_performance_index_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_minimum_ulcer_index_request_constraints.py",
        "src/fern/portfolio_optimization/types/post_portfolio_optimization_most_diversified_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/__init__.py",
        "src/fern/portfolio_optimization_mean_variance/types/__init__.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_diversified_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_diversified_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_subset_resampling_based_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_aggregation_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_enumeration_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_return_subset_resampling_based_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_diversified_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_diversified_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_aggregation_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_enumeration_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_diversified_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_diversified_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_aggregation_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_enumeration_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_diversified_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_diversified_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_response.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_subset_resampling_based_request_constraints.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_aggregation_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_enumeration_method.py",
        "src/fern/portfolio_optimization_mean_variance/types/post_portfolio_optimization_minimum_variance_subset_resampling_based_response.py",
        "README.md",
        "src/fern/assets_analysis/client.py",
        "src/fern/assets_analysis/raw_client.py",
        "src/fern/assets_correlation_matrix/raw_client.py",
        "src/fern/assets_covariance_matrix/raw_client.py",
        "src/fern/assets_kurtosis/raw_client.py",
        "src/fern/assets_prices/raw_client.py",
        "src/fern/assets_returns/client.py",
        "src/fern/assets_returns/raw_client.py",
        "src/fern/assets_returns_simulation/client.py",
        "src/fern/assets_returns_simulation/raw_client.py",
        "src/fern/assets_skewness/raw_client.py",
        "src/fern/factors/client.py",
        "src/fern/factors/raw_client.py",
        "src/fern/portfolio_analysis/raw_client.py",
        "src/fern/portfolio_analysis_sharpe_ratio/raw_client.py",
        "src/fern/portfolio_construction/raw_client.py",
        "src/fern/portfolio_optimization/raw_client.py",
        "src/fern/portfolio_optimization_mean_variance/raw_client.py",
        "src/fern/portfolio_simulation/client.py",
        "src/fern/portfolio_simulation/raw_client.py",
        "src/fern/assets_kurtosis/client.py",
        "src/fern/assets_prices/client.py",
        "src/fern/assets_skewness/client.py",
        "src/fern/portfolio_analysis_sharpe_ratio/client.py",
        "src/fern/portfolio_construction/client.py",
        "src/fern/portfolio_analysis/client.py",
        "src/fern/portfolio_optimization/client.py",
        "src/fern/assets_correlation_matrix/client.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_request.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_request_zero.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_request_zero_assets_item.py",
        "src/fern/assets_covariance_matrix/__init__.py",
        "src/fern/assets_covariance_matrix/client.py",
        "src/fern/assets_covariance_matrix/types/__init__.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_request.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_request_assets.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_request_zero.py",
        "src/fern/assets_covariance_matrix/types/post_assets_covariance_matrix_request_zero_assets_item.py",
        "src/fern/assets_variance/__init__.py",
        "src/fern/assets_variance/client.py",
        "src/fern/assets_variance/types/__init__.py",
        "src/fern/assets_variance/types/post_assets_variance_request.py",
        "src/fern/assets_variance/types/post_assets_variance_request_zero.py",
        "src/fern/assets_variance/types/post_assets_variance_request_zero_assets_item.py",
        "src/fern/assets_volatility/__init__.py",
        "src/fern/assets_volatility/client.py",
        "src/fern/assets_volatility/types/__init__.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request_zero.py",
        "src/fern/assets_volatility/types/post_assets_volatility_request_zero_assets_item.py",
        "src/fern/portfolio_analysis/__init__.py",
        "src/fern/portfolio_analysis/types/__init__.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request_one.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request_one_assets_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_correlation_spectrum_request_one_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request_one.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request_one_assets_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_diversification_ratio_request_one_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_request_one.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_return_request_one_portfolios_item.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_request.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_request_one.py",
        "src/fern/portfolio_analysis/types/post_portfolio_analysis_volatility_request_one_portfolios_item.py",
        "src/fern/portfolio_analysis_sharpe_ratio/__init__.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/__init__.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_request.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_request_one.py",
        "src/fern/portfolio_analysis_sharpe_ratio/types/post_portfolio_analysis_sharpe_ratio_request_one_portfolios_item.py",
        "src/fern/portfolio_optimization_mean_variance/client.py",
        "src/fern/__init__.py",
        "src/fern/assets_correlation_matrix/__init__.py",
        "src/fern/assets_correlation_matrix/types/__init__.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_theory_implied_request_assets_item.py",
        "src/fern/assets_correlation_matrix/types/post_assets_correlation_matrix_theory_implied_request_assets_item_asset_hierarchical_classification_item.py",
        "reference.md",
    ],
};

const OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI: Corpus = Corpus {
    api: "openbanking.org.uk-account-info-openapi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/account_access/__init__.py",
        "src/fern/account_access/raw_client.py",
        "src/fern/account_access/types/__init__.py",
        "src/fern/account_access/types/ob_read_consent1data.py",
        "src/fern/account_access/types/ob_read_consent1data_permissions_item.py",
        "src/fern/accounts/__init__.py",
        "src/fern/accounts/raw_client.py",
        "src/fern/balances/__init__.py",
        "src/fern/balances/raw_client.py",
        "src/fern/beneficiaries/__init__.py",
        "src/fern/beneficiaries/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/direct_debits/__init__.py",
        "src/fern/direct_debits/raw_client.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/method_not_allowed_error.py",
        "src/fern/errors/not_acceptable_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/errors/unsupported_media_type_error.py",
        "src/fern/offers/__init__.py",
        "src/fern/offers/raw_client.py",
        "src/fern/parties/__init__.py",
        "src/fern/parties/raw_client.py",
        "src/fern/products/__init__.py",
        "src/fern/products/raw_client.py",
        "src/fern/py.typed",
        "src/fern/scheduled_payments/__init__.py",
        "src/fern/scheduled_payments/raw_client.py",
        "src/fern/standing_orders/__init__.py",
        "src/fern/standing_orders/raw_client.py",
        "src/fern/statements/__init__.py",
        "src/fern/statements/raw_client.py",
        "src/fern/transactions/__init__.py",
        "src/fern/transactions/raw_client.py",
        "src/fern/types/account_id.py",
        "src/fern/types/active_or_historic_currency_code0.py",
        "src/fern/types/active_or_historic_currency_code1.py",
        "src/fern/types/address_line.py",
        "src/fern/types/beneficiary_id.py",
        "src/fern/types/booking_date_time.py",
        "src/fern/types/building_number.py",
        "src/fern/types/country_code.py",
        "src/fern/types/country_sub_division.py",
        "src/fern/types/creation_date_time.py",
        "src/fern/types/date_time.py",
        "src/fern/types/debtor_reference.py",
        "src/fern/types/description0.py",
        "src/fern/types/description1.py",
        "src/fern/types/description2.py",
        "src/fern/types/description3.py",
        "src/fern/types/direct_debit_id.py",
        "src/fern/types/email_address.py",
        "src/fern/types/end_date_time.py",
        "src/fern/types/file.py",
        "src/fern/types/final_payment_date_time.py",
        "src/fern/types/first_payment_date_time.py",
        "src/fern/types/frequency0.py",
        "src/fern/types/frequency1.py",
        "src/fern/types/full_legal_name.py",
        "src/fern/types/identification0.py",
        "src/fern/types/identification1.py",
        "src/fern/types/identification2.py",
        "src/fern/types/iso_date_time.py",
        "src/fern/types/last_payment_date_time.py",
        "src/fern/types/links.py",
        "src/fern/types/mandate_identification.py",
        "src/fern/types/maturity_date.py",
        "src/fern/types/meta.py",
        "src/fern/types/model.py",
        "src/fern/types/name0.py",
        "src/fern/types/name1.py",
        "src/fern/types/name2.py",
        "src/fern/types/name3.py",
        "src/fern/types/name4.py",
        "src/fern/types/next_payment_date_time.py",
        "src/fern/types/nickname.py",
        "src/fern/types/number0.py",
        "src/fern/types/number1.py",
        "src/fern/types/number_of_payments.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/ob_account4.py",
        "src/fern/types/ob_account4account_item.py",
        "src/fern/types/ob_account4basic.py",
        "src/fern/types/ob_account4detail.py",
        "src/fern/types/ob_account4detail_account_item.py",
        "src/fern/types/ob_account6.py",
        "src/fern/types/ob_account6account_item.py",
        "src/fern/types/ob_account6basic.py",
        "src/fern/types/ob_account6detail.py",
        "src/fern/types/ob_account6detail_account_item.py",
        "src/fern/types/ob_account_status1code.py",
        "src/fern/types/ob_active_currency_and_amount_simple_type.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount0.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount1.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount10.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount11.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount2.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount3.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount4.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount5.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount6.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount7.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount8.py",
        "src/fern/types/ob_active_or_historic_currency_and_amount9.py",
        "src/fern/types/ob_address_type_code.py",
        "src/fern/types/ob_amount10.py",
        "src/fern/types/ob_amount11.py",
        "src/fern/types/ob_amount12.py",
        "src/fern/types/ob_amount13.py",
        "src/fern/types/ob_amount14.py",
        "src/fern/types/ob_balance_type1code.py",
        "src/fern/types/ob_bank_transaction_code_structure1.py",
        "src/fern/types/ob_beneficiary5.py",
        "src/fern/types/ob_beneficiary5basic.py",
        "src/fern/types/ob_beneficiary5detail.py",
        "src/fern/types/ob_beneficiary_type1code.py",
        "src/fern/types/ob_branch_and_financial_institution_identification50.py",
        "src/fern/types/ob_branch_and_financial_institution_identification51.py",
        "src/fern/types/ob_branch_and_financial_institution_identification60.py",
        "src/fern/types/ob_branch_and_financial_institution_identification61.py",
        "src/fern/types/ob_branch_and_financial_institution_identification62.py",
        "src/fern/types/ob_cash_account50.py",
        "src/fern/types/ob_cash_account51.py",
        "src/fern/types/ob_cash_account60.py",
        "src/fern/types/ob_cash_account61.py",
        "src/fern/types/ob_code_mnemonic.py",
        "src/fern/types/ob_credit_debit_code0.py",
        "src/fern/types/ob_credit_debit_code1.py",
        "src/fern/types/ob_credit_debit_code2.py",
        "src/fern/types/ob_currency_exchange5.py",
        "src/fern/types/ob_currency_exchange5instructed_amount.py",
        "src/fern/types/ob_entry_status1code.py",
        "src/fern/types/ob_error1.py",
        "src/fern/types/ob_error_response1.py",
        "src/fern/types/ob_external_account_identification4code.py",
        "src/fern/types/ob_external_account_role1code.py",
        "src/fern/types/ob_external_account_sub_type1code.py",
        "src/fern/types/ob_external_account_type1code.py",
        "src/fern/types/ob_external_direct_debit_status1code.py",
        "src/fern/types/ob_external_financial_institution_identification4code.py",
        "src/fern/types/ob_external_legal_structure_type1code.py",
        "src/fern/types/ob_external_party_type1code.py",
        "src/fern/types/ob_external_schedule_type1code.py",
        "src/fern/types/ob_external_standing_order_status1code.py",
        "src/fern/types/ob_external_statement_amount_type1code.py",
        "src/fern/types/ob_external_statement_benefit_type1code.py",
        "src/fern/types/ob_external_statement_date_time_type1code.py",
        "src/fern/types/ob_external_statement_fee_frequency1code.py",
        "src/fern/types/ob_external_statement_fee_rate_type1code.py",
        "src/fern/types/ob_external_statement_fee_type1code.py",
        "src/fern/types/ob_external_statement_interest_frequency1code.py",
        "src/fern/types/ob_external_statement_interest_rate_type1code.py",
        "src/fern/types/ob_external_statement_interest_type1code.py",
        "src/fern/types/ob_external_statement_rate_type1code.py",
        "src/fern/types/ob_external_statement_type1code.py",
        "src/fern/types/ob_external_statement_value_type1code.py",
        "src/fern/types/ob_external_switch_status_code.py",
        "src/fern/types/ob_fee_category1code.py",
        "src/fern/types/ob_fee_frequency1code0.py",
        "src/fern/types/ob_fee_frequency1code1.py",
        "src/fern/types/ob_fee_frequency1code2.py",
        "src/fern/types/ob_fee_frequency1code3.py",
        "src/fern/types/ob_fee_frequency1code4.py",
        "src/fern/types/ob_fee_type1code.py",
        "src/fern/types/ob_interest_calculation_method1code.py",
        "src/fern/types/ob_interest_fixed_variable_type1code.py",
        "src/fern/types/ob_interest_rate_type1code0.py",
        "src/fern/types/ob_interest_rate_type1code1.py",
        "src/fern/types/ob_merchant_details1.py",
        "src/fern/types/ob_min_max_type1code.py",
        "src/fern/types/ob_other_code_type10.py",
        "src/fern/types/ob_other_code_type11.py",
        "src/fern/types/ob_other_code_type12.py",
        "src/fern/types/ob_other_code_type13.py",
        "src/fern/types/ob_other_code_type14.py",
        "src/fern/types/ob_other_code_type15.py",
        "src/fern/types/ob_other_code_type16.py",
        "src/fern/types/ob_other_code_type17.py",
        "src/fern/types/ob_other_code_type18.py",
        "src/fern/types/ob_other_fee_charge_detail_type.py",
        "src/fern/types/ob_overdraft_fee_type1code.py",
        "src/fern/types/ob_party2.py",
        "src/fern/types/ob_party2address_item.py",
        "src/fern/types/ob_party_relationships1.py",
        "src/fern/types/ob_party_relationships1account.py",
        "src/fern/types/ob_period1code.py",
        "src/fern/types/ob_postal_address6.py",
        "src/fern/types/ob_rate10.py",
        "src/fern/types/ob_rate11.py",
        "src/fern/types/ob_read_account6.py",
        "src/fern/types/ob_read_account6data.py",
        "src/fern/types/ob_read_balance1.py",
        "src/fern/types/ob_read_balance1data.py",
        "src/fern/types/ob_read_balance1data_balance_item.py",
        "src/fern/types/ob_read_balance1data_balance_item_amount.py",
        "src/fern/types/ob_read_balance1data_balance_item_credit_line_item.py",
        "src/fern/types/ob_read_balance1data_balance_item_credit_line_item_amount.py",
        "src/fern/types/ob_read_balance1data_balance_item_credit_line_item_type.py",
        "src/fern/types/ob_read_beneficiary5.py",
        "src/fern/types/ob_read_beneficiary5data.py",
        "src/fern/types/ob_read_consent_response1.py",
        "src/fern/types/ob_read_consent_response1data.py",
        "src/fern/types/ob_read_consent_response1data_permissions_item.py",
        "src/fern/types/ob_read_consent_response1data_status.py",
        "src/fern/types/ob_read_data_statement2.py",
        "src/fern/types/ob_read_data_transaction6.py",
        "src/fern/types/ob_read_direct_debit2.py",
        "src/fern/types/ob_read_direct_debit2data.py",
        "src/fern/types/ob_read_direct_debit2data_direct_debit_item.py",
        "src/fern/types/ob_read_offer1.py",
        "src/fern/types/ob_read_offer1data.py",
        "src/fern/types/ob_read_offer1data_offer_item.py",
        "src/fern/types/ob_read_offer1data_offer_item_amount.py",
        "src/fern/types/ob_read_offer1data_offer_item_fee.py",
        "src/fern/types/ob_read_offer1data_offer_item_offer_type.py",
        "src/fern/types/ob_read_party2.py",
        "src/fern/types/ob_read_party2data.py",
        "src/fern/types/ob_read_party3.py",
        "src/fern/types/ob_read_party3data.py",
        "src/fern/types/ob_read_product2.py",
        "src/fern/types/ob_read_product2data.py",
        "src/fern/types/ob_read_product2data_product_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_destination.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_application_frequency.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_calculation_frequency.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_method.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_provider_interest_rate_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_max_term_period.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_min_term_period.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_tier_band_method.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_other_tariff_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_other_fees_charges_item_tariff_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_tier_band_method.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_product_details.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_product_details_fee_free_length_period.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_product_details_segment_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_amount_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_other_amount_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_other_repayment_frequency.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_other_repayment_type.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_frequency.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item_max_holiday_period.py",
        "src/fern/types/ob_read_product2data_product_item_other_product_type_repayment_repayment_type.py",
        "src/fern/types/ob_read_product2data_product_item_product_type.py",
        "src/fern/types/ob_read_scheduled_payment3.py",
        "src/fern/types/ob_read_scheduled_payment3data.py",
        "src/fern/types/ob_read_standing_order6.py",
        "src/fern/types/ob_read_standing_order6data.py",
        "src/fern/types/ob_read_statement2.py",
        "src/fern/types/ob_read_transaction6.py",
        "src/fern/types/ob_risk2.py",
        "src/fern/types/ob_scheduled_payment3.py",
        "src/fern/types/ob_scheduled_payment3basic.py",
        "src/fern/types/ob_scheduled_payment3detail.py",
        "src/fern/types/ob_statement2.py",
        "src/fern/types/ob_statement2basic.py",
        "src/fern/types/ob_statement2basic_statement_benefit_item.py",
        "src/fern/types/ob_statement2basic_statement_date_time_item.py",
        "src/fern/types/ob_statement2basic_statement_fee_item.py",
        "src/fern/types/ob_statement2basic_statement_interest_item.py",
        "src/fern/types/ob_statement2basic_statement_rate_item.py",
        "src/fern/types/ob_statement2basic_statement_value_item.py",
        "src/fern/types/ob_statement2detail.py",
        "src/fern/types/ob_statement2detail_statement_amount_item.py",
        "src/fern/types/ob_statement2detail_statement_benefit_item.py",
        "src/fern/types/ob_statement2detail_statement_date_time_item.py",
        "src/fern/types/ob_statement2detail_statement_fee_item.py",
        "src/fern/types/ob_statement2detail_statement_interest_item.py",
        "src/fern/types/ob_statement2detail_statement_rate_item.py",
        "src/fern/types/ob_statement2detail_statement_value_item.py",
        "src/fern/types/ob_statement2statement_amount_item.py",
        "src/fern/types/ob_statement2statement_benefit_item.py",
        "src/fern/types/ob_statement2statement_date_time_item.py",
        "src/fern/types/ob_statement2statement_fee_item.py",
        "src/fern/types/ob_statement2statement_interest_item.py",
        "src/fern/types/ob_statement2statement_rate_item.py",
        "src/fern/types/ob_statement2statement_value_item.py",
        "src/fern/types/ob_supplementary_data1.py",
        "src/fern/types/ob_transaction_card_instrument1.py",
        "src/fern/types/ob_transaction_card_instrument1authorisation_type.py",
        "src/fern/types/ob_transaction_card_instrument1card_scheme_name.py",
        "src/fern/types/ob_transaction_cash_balance.py",
        "src/fern/types/ob_transaction_cash_balance_amount.py",
        "src/fern/types/ob_transaction_mutability1code.py",
        "src/fern/types/obbca_data1.py",
        "src/fern/types/obbca_data1credit_interest.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_calculation_method.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_destination.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency.py",
        "src/fern/types/obbca_data1credit_interest_tier_band_set_item_tier_band_method.py",
        "src/fern/types/obbca_data1other_fees_charges_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_applicable_range.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_category.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_category_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type_fee_category.py",
        "src/fern/types/obbca_data1other_fees_charges_item_other_tariff_type.py",
        "src/fern/types/obbca_data1other_fees_charges_item_tariff_type.py",
        "src/fern/types/obbca_data1overdraft.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_type.py",
        "src/fern/types/obbca_data1overdraft_overdraft_tier_band_set_item_tier_band_method.py",
        "src/fern/types/obbca_data1product_details.py",
        "src/fern/types/obbca_data1product_details_fee_free_length_period.py",
        "src/fern/types/obbca_data1product_details_segment_item.py",
        "src/fern/types/obpca_data1.py",
        "src/fern/types/obpca_data1credit_interest.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_calculation_method.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_destination.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency.py",
        "src/fern/types/obpca_data1credit_interest_tier_band_set_item_tier_band_method.py",
        "src/fern/types/obpca_data1other_fees_charges.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_cap_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_applicable_range.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_category.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_category_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obpca_data1other_fees_charges_fee_charge_detail_item_other_fee_type_fee_category.py",
        "src/fern/types/obpca_data1overdraft.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_type.py",
        "src/fern/types/obpca_data1overdraft_overdraft_tier_band_set_item_tier_band_method.py",
        "src/fern/types/obpca_data1product_details.py",
        "src/fern/types/obpca_data1product_details_segment_item.py",
        "src/fern/types/opening_date.py",
        "src/fern/types/party_id.py",
        "src/fern/types/party_number.py",
        "src/fern/types/phone_number0.py",
        "src/fern/types/phone_number1.py",
        "src/fern/types/post_code.py",
        "src/fern/types/previous_payment_date_time.py",
        "src/fern/types/proprietary_bank_transaction_code_structure1.py",
        "src/fern/types/rate.py",
        "src/fern/types/reference.py",
        "src/fern/types/scheduled_payment_date_time.py",
        "src/fern/types/scheduled_payment_id.py",
        "src/fern/types/secondary_identification.py",
        "src/fern/types/standing_order_id.py",
        "src/fern/types/start_date_time.py",
        "src/fern/types/statement_id.py",
        "src/fern/types/statement_reference.py",
        "src/fern/types/status_update_date_time.py",
        "src/fern/types/street_name.py",
        "src/fern/types/town_name.py",
        "src/fern/types/transaction_id.py",
        "src/fern/types/transaction_information.py",
        "src/fern/types/transaction_reference.py",
        "src/fern/types/value.py",
        "src/fern/types/value_date_time.py",
        "src/fern/version.py",
        "README.md",
        "reference.md",
        "src/fern/__init__.py",
        "src/fern/account_access/client.py",
        "src/fern/accounts/client.py",
        "src/fern/balances/client.py",
        "src/fern/beneficiaries/client.py",
        "src/fern/client.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/direct_debits/client.py",
        "src/fern/offers/client.py",
        "src/fern/parties/client.py",
        "src/fern/products/client.py",
        "src/fern/scheduled_payments/client.py",
        "src/fern/standing_orders/client.py",
        "src/fern/statements/client.py",
        "src/fern/transactions/client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/ob_standing_order6.py",
        "src/fern/types/ob_standing_order6basic.py",
        "src/fern/types/ob_standing_order6detail.py",
        "src/fern/types/ob_transaction6.py",
        "src/fern/types/ob_transaction6basic.py",
        "src/fern/types/ob_transaction6detail.py",
    ],
};

const NETBOX_DEV: Corpus = Corpus {
    api: "netbox.dev",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/circuits/__init__.py",
        "src/fern/circuits/types/__init__.py",
        "src/fern/circuits/types/circuits_circuit_terminations_list_response.py",
        "src/fern/circuits/types/circuits_circuit_types_list_response.py",
        "src/fern/circuits/types/circuits_circuits_list_response.py",
        "src/fern/circuits/types/circuits_provider_networks_list_response.py",
        "src/fern/circuits/types/circuits_providers_list_response.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/dcim/__init__.py",
        "src/fern/dcim/types/__init__.py",
        "src/fern/dcim/types/dcim_cable_terminations_list_response.py",
        "src/fern/dcim/types/dcim_cables_list_response.py",
        "src/fern/dcim/types/dcim_console_port_templates_list_response.py",
        "src/fern/dcim/types/dcim_console_ports_list_response.py",
        "src/fern/dcim/types/dcim_console_server_port_templates_list_response.py",
        "src/fern/dcim/types/dcim_console_server_ports_list_response.py",
        "src/fern/dcim/types/dcim_device_bay_templates_list_response.py",
        "src/fern/dcim/types/dcim_device_bays_list_response.py",
        "src/fern/dcim/types/dcim_device_roles_list_response.py",
        "src/fern/dcim/types/dcim_device_types_list_response.py",
        "src/fern/dcim/types/dcim_devices_list_response.py",
        "src/fern/dcim/types/dcim_front_port_templates_list_response.py",
        "src/fern/dcim/types/dcim_front_ports_list_response.py",
        "src/fern/dcim/types/dcim_interface_templates_list_response.py",
        "src/fern/dcim/types/dcim_interfaces_list_response.py",
        "src/fern/dcim/types/dcim_inventory_item_roles_list_response.py",
        "src/fern/dcim/types/dcim_inventory_item_templates_list_response.py",
        "src/fern/dcim/types/dcim_inventory_items_list_response.py",
        "src/fern/dcim/types/dcim_locations_list_response.py",
        "src/fern/dcim/types/dcim_manufacturers_list_response.py",
        "src/fern/dcim/types/dcim_module_bay_templates_list_response.py",
        "src/fern/dcim/types/dcim_module_bays_list_response.py",
        "src/fern/dcim/types/dcim_module_types_list_response.py",
        "src/fern/dcim/types/dcim_modules_list_response.py",
        "src/fern/dcim/types/dcim_platforms_list_response.py",
        "src/fern/dcim/types/dcim_power_feeds_list_response.py",
        "src/fern/dcim/types/dcim_power_outlet_templates_list_response.py",
        "src/fern/dcim/types/dcim_power_outlets_list_response.py",
        "src/fern/dcim/types/dcim_power_panels_list_response.py",
        "src/fern/dcim/types/dcim_power_port_templates_list_response.py",
        "src/fern/dcim/types/dcim_power_ports_list_response.py",
        "src/fern/dcim/types/dcim_rack_reservations_list_response.py",
        "src/fern/dcim/types/dcim_rack_roles_list_response.py",
        "src/fern/dcim/types/dcim_racks_elevation_request_face.py",
        "src/fern/dcim/types/dcim_racks_elevation_request_render.py",
        "src/fern/dcim/types/dcim_racks_list_response.py",
        "src/fern/dcim/types/dcim_rear_port_templates_list_response.py",
        "src/fern/dcim/types/dcim_rear_ports_list_response.py",
        "src/fern/dcim/types/dcim_regions_list_response.py",
        "src/fern/dcim/types/dcim_site_groups_list_response.py",
        "src/fern/dcim/types/dcim_sites_list_response.py",
        "src/fern/dcim/types/dcim_virtual_chassis_list_response.py",
        "src/fern/dcim/types/dcim_virtual_device_contexts_list_response.py",
        "src/fern/environment.py",
        "src/fern/extras/__init__.py",
        "src/fern/extras/types/__init__.py",
        "src/fern/extras/types/extras_config_contexts_list_response.py",
        "src/fern/extras/types/extras_content_types_list_response.py",
        "src/fern/extras/types/extras_custom_fields_list_response.py",
        "src/fern/extras/types/extras_custom_links_list_response.py",
        "src/fern/extras/types/extras_export_templates_list_response.py",
        "src/fern/extras/types/extras_image_attachments_list_response.py",
        "src/fern/extras/types/extras_job_results_list_response.py",
        "src/fern/extras/types/extras_journal_entries_list_response.py",
        "src/fern/extras/types/extras_object_changes_list_response.py",
        "src/fern/extras/types/extras_saved_filters_list_response.py",
        "src/fern/extras/types/extras_tags_list_response.py",
        "src/fern/extras/types/extras_webhooks_list_response.py",
        "src/fern/ipam/types/ipam_aggregates_list_response.py",
        "src/fern/ipam/types/ipam_asns_list_response.py",
        "src/fern/ipam/types/ipam_fhrp_group_assignments_list_response.py",
        "src/fern/ipam/types/ipam_fhrp_groups_list_response.py",
        "src/fern/ipam/types/ipam_ip_addresses_list_response.py",
        "src/fern/ipam/types/ipam_ip_ranges_list_response.py",
        "src/fern/ipam/types/ipam_prefixes_list_response.py",
        "src/fern/ipam/types/ipam_rirs_list_response.py",
        "src/fern/ipam/types/ipam_roles_list_response.py",
        "src/fern/ipam/types/ipam_route_targets_list_response.py",
        "src/fern/ipam/types/ipam_service_templates_list_response.py",
        "src/fern/ipam/types/ipam_services_list_response.py",
        "src/fern/ipam/types/ipam_vlan_groups_list_response.py",
        "src/fern/ipam/types/ipam_vlans_list_response.py",
        "src/fern/ipam/types/ipam_vrfs_list_response.py",
        "src/fern/ipam/types/writable_create_available_vlan_status.py",
        "src/fern/py.typed",
        "src/fern/status/__init__.py",
        "src/fern/status/client.py",
        "src/fern/status/raw_client.py",
        "src/fern/tenancy/__init__.py",
        "src/fern/tenancy/types/__init__.py",
        "src/fern/tenancy/types/tenancy_contact_assignments_list_response.py",
        "src/fern/tenancy/types/tenancy_contact_groups_list_response.py",
        "src/fern/tenancy/types/tenancy_contact_roles_list_response.py",
        "src/fern/tenancy/types/tenancy_contacts_list_response.py",
        "src/fern/tenancy/types/tenancy_tenant_groups_list_response.py",
        "src/fern/tenancy/types/tenancy_tenants_list_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/aggregate.py",
        "src/fern/types/aggregate_family.py",
        "src/fern/types/aggregate_family_label.py",
        "src/fern/types/asn.py",
        "src/fern/types/available_ip.py",
        "src/fern/types/available_prefix.py",
        "src/fern/types/available_vlan.py",
        "src/fern/types/cable.py",
        "src/fern/types/cable_length_unit.py",
        "src/fern/types/cable_length_unit_label.py",
        "src/fern/types/cable_length_unit_value.py",
        "src/fern/types/cable_status.py",
        "src/fern/types/cable_status_label.py",
        "src/fern/types/cable_status_value.py",
        "src/fern/types/cable_termination.py",
        "src/fern/types/cable_termination_cable_end.py",
        "src/fern/types/cable_type.py",
        "src/fern/types/circuit.py",
        "src/fern/types/circuit_circuit_termination.py",
        "src/fern/types/circuit_status.py",
        "src/fern/types/circuit_status_label.py",
        "src/fern/types/circuit_status_value.py",
        "src/fern/types/circuit_termination.py",
        "src/fern/types/circuit_termination_term_side.py",
        "src/fern/types/circuit_type.py",
        "src/fern/types/cluster.py",
        "src/fern/types/cluster_group.py",
        "src/fern/types/cluster_status.py",
        "src/fern/types/cluster_status_label.py",
        "src/fern/types/cluster_status_value.py",
        "src/fern/types/cluster_type.py",
        "src/fern/types/component_nested_module.py",
        "src/fern/types/console_port.py",
        "src/fern/types/console_port_speed.py",
        "src/fern/types/console_port_template.py",
        "src/fern/types/console_port_template_type.py",
        "src/fern/types/console_port_type.py",
        "src/fern/types/console_server_port.py",
        "src/fern/types/console_server_port_speed.py",
        "src/fern/types/console_server_port_template.py",
        "src/fern/types/console_server_port_template_type.py",
        "src/fern/types/console_server_port_type.py",
        "src/fern/types/contact.py",
        "src/fern/types/contact_assignment.py",
        "src/fern/types/contact_assignment_priority.py",
        "src/fern/types/contact_assignment_priority_label.py",
        "src/fern/types/contact_assignment_priority_value.py",
        "src/fern/types/contact_group.py",
        "src/fern/types/contact_role.py",
        "src/fern/types/content_type.py",
        "src/fern/types/custom_field_filter_logic.py",
        "src/fern/types/custom_field_filter_logic_label.py",
        "src/fern/types/custom_field_filter_logic_value.py",
        "src/fern/types/custom_field_type.py",
        "src/fern/types/custom_field_type_label.py",
        "src/fern/types/custom_field_type_value.py",
        "src/fern/types/custom_field_ui_visibility.py",
        "src/fern/types/custom_field_ui_visibility_label.py",
        "src/fern/types/custom_field_ui_visibility_value.py",
        "src/fern/types/custom_link_button_class.py",
        "src/fern/types/device.py",
        "src/fern/types/device_airflow.py",
        "src/fern/types/device_airflow_label.py",
        "src/fern/types/device_airflow_value.py",
        "src/fern/types/device_bay.py",
        "src/fern/types/device_bay_template.py",
        "src/fern/types/device_face.py",
        "src/fern/types/device_face_label.py",
        "src/fern/types/device_face_value.py",
        "src/fern/types/device_napalm.py",
        "src/fern/types/device_role.py",
        "src/fern/types/device_status.py",
        "src/fern/types/device_status_label.py",
        "src/fern/types/device_status_value.py",
        "src/fern/types/device_type.py",
        "src/fern/types/device_type_airflow.py",
        "src/fern/types/device_type_airflow_label.py",
        "src/fern/types/device_type_airflow_value.py",
        "src/fern/types/device_type_subdevice_role.py",
        "src/fern/types/device_type_subdevice_role_label.py",
        "src/fern/types/device_type_subdevice_role_value.py",
        "src/fern/types/device_type_weight_unit.py",
        "src/fern/types/device_type_weight_unit_label.py",
        "src/fern/types/device_type_weight_unit_value.py",
        "src/fern/types/device_with_config_context.py",
        "src/fern/types/device_with_config_context_airflow.py",
        "src/fern/types/device_with_config_context_airflow_label.py",
        "src/fern/types/device_with_config_context_airflow_value.py",
        "src/fern/types/device_with_config_context_face.py",
        "src/fern/types/device_with_config_context_face_label.py",
        "src/fern/types/device_with_config_context_face_value.py",
        "src/fern/types/device_with_config_context_status.py",
        "src/fern/types/device_with_config_context_status_label.py",
        "src/fern/types/device_with_config_context_status_value.py",
        "src/fern/types/fhrp_group.py",
        "src/fern/types/fhrp_group_assignment.py",
        "src/fern/types/fhrp_group_auth_type.py",
        "src/fern/types/fhrp_group_protocol.py",
        "src/fern/types/front_port.py",
        "src/fern/types/front_port_rear_port.py",
        "src/fern/types/front_port_template.py",
        "src/fern/types/front_port_template_type.py",
        "src/fern/types/front_port_type.py",
        "src/fern/types/generic_object.py",
        "src/fern/types/group.py",
        "src/fern/types/image_attachment.py",
        "src/fern/types/interface_duplex.py",
        "src/fern/types/interface_duplex_label.py",
        "src/fern/types/interface_duplex_value.py",
        "src/fern/types/interface_mode.py",
        "src/fern/types/interface_mode_label.py",
        "src/fern/types/interface_mode_value.py",
        "src/fern/types/interface_poe_mode.py",
        "src/fern/types/interface_poe_mode_label.py",
        "src/fern/types/interface_poe_mode_value.py",
        "src/fern/types/interface_poe_type.py",
        "src/fern/types/interface_rf_channel.py",
        "src/fern/types/interface_rf_role.py",
        "src/fern/types/interface_rf_role_label.py",
        "src/fern/types/interface_rf_role_value.py",
        "src/fern/types/interface_template.py",
        "src/fern/types/interface_template_poe_mode.py",
        "src/fern/types/interface_template_poe_mode_label.py",
        "src/fern/types/interface_template_poe_mode_value.py",
        "src/fern/types/interface_template_poe_type.py",
        "src/fern/types/interface_template_type.py",
        "src/fern/types/interface_type.py",
        "src/fern/types/inventory_item.py",
        "src/fern/types/inventory_item_role.py",
        "src/fern/types/inventory_item_template.py",
        "src/fern/types/ip_address.py",
        "src/fern/types/ip_address_family.py",
        "src/fern/types/ip_address_family_label.py",
        "src/fern/types/ip_address_role.py",
        "src/fern/types/ip_address_role_label.py",
        "src/fern/types/ip_address_role_value.py",
        "src/fern/types/ip_address_status.py",
        "src/fern/types/ip_address_status_label.py",
        "src/fern/types/ip_address_status_value.py",
        "src/fern/types/ip_network.py",
        "src/fern/types/ip_range.py",
        "src/fern/types/ip_range_family.py",
        "src/fern/types/ip_range_family_label.py",
        "src/fern/types/ip_range_status.py",
        "src/fern/types/ip_range_status_label.py",
        "src/fern/types/ip_range_status_value.py",
        "src/fern/types/job_result.py",
        "src/fern/types/job_result_status.py",
        "src/fern/types/job_result_status_label.py",
        "src/fern/types/job_result_status_value.py",
        "src/fern/types/journal_entry.py",
        "src/fern/types/journal_entry_kind.py",
        "src/fern/types/journal_entry_kind_label.py",
        "src/fern/types/journal_entry_kind_value.py",
        "src/fern/types/l2vpn_termination.py",
        "src/fern/types/l2vpn_type.py",
        "src/fern/types/l2vpn_type_label.py",
        "src/fern/types/l2vpn_type_value.py",
        "src/fern/types/location.py",
        "src/fern/types/location_status.py",
        "src/fern/types/location_status_label.py",
        "src/fern/types/location_status_value.py",
        "src/fern/types/manufacturer.py",
        "src/fern/types/module.py",
        "src/fern/types/module_bay.py",
        "src/fern/types/module_bay_nested_module.py",
        "src/fern/types/module_bay_template.py",
        "src/fern/types/module_nested_module_bay.py",
        "src/fern/types/module_status.py",
        "src/fern/types/module_status_label.py",
        "src/fern/types/module_status_value.py",
        "src/fern/types/module_type.py",
        "src/fern/types/module_type_weight_unit.py",
        "src/fern/types/module_type_weight_unit_label.py",
        "src/fern/types/module_type_weight_unit_value.py",
        "src/fern/types/nested_asn.py",
        "src/fern/types/nested_cable.py",
        "src/fern/types/nested_circuit.py",
        "src/fern/types/nested_circuit_type.py",
        "src/fern/types/nested_cluster.py",
        "src/fern/types/nested_cluster_group.py",
        "src/fern/types/nested_cluster_type.py",
        "src/fern/types/nested_contact.py",
        "src/fern/types/nested_contact_group.py",
        "src/fern/types/nested_contact_role.py",
        "src/fern/types/nested_device.py",
        "src/fern/types/nested_device_role.py",
        "src/fern/types/nested_device_type.py",
        "src/fern/types/nested_fhrp_group.py",
        "src/fern/types/nested_fhrp_group_protocol.py",
        "src/fern/types/nested_group.py",
        "src/fern/types/nested_interface.py",
        "src/fern/types/nested_inventory_item_role.py",
        "src/fern/types/nested_ip_address.py",
        "src/fern/types/nested_l2vpn.py",
        "src/fern/types/nested_l2vpn_termination.py",
        "src/fern/types/nested_l2vpn_type.py",
        "src/fern/types/nested_location.py",
        "src/fern/types/nested_manufacturer.py",
        "src/fern/types/nested_module.py",
        "src/fern/types/nested_module_bay.py",
        "src/fern/types/nested_module_type.py",
        "src/fern/types/nested_platform.py",
        "src/fern/types/nested_power_panel.py",
        "src/fern/types/nested_power_port.py",
        "src/fern/types/nested_power_port_template.py",
        "src/fern/types/nested_provider.py",
        "src/fern/types/nested_provider_network.py",
        "src/fern/types/nested_rack.py",
        "src/fern/types/nested_rack_role.py",
        "src/fern/types/nested_rear_port_template.py",
        "src/fern/types/nested_region.py",
        "src/fern/types/nested_rir.py",
        "src/fern/types/nested_role.py",
        "src/fern/types/nested_route_target.py",
        "src/fern/types/nested_site.py",
        "src/fern/types/nested_site_group.py",
        "src/fern/types/nested_tag.py",
        "src/fern/types/nested_tenant.py",
        "src/fern/types/nested_tenant_group.py",
        "src/fern/types/nested_user.py",
        "src/fern/types/nested_virtual_chassis.py",
        "src/fern/types/nested_virtual_device_context.py",
        "src/fern/types/nested_virtual_machine.py",
        "src/fern/types/nested_vlan.py",
        "src/fern/types/nested_vlan_group.py",
        "src/fern/types/nested_vm_interface.py",
        "src/fern/types/nested_vrf.py",
        "src/fern/types/nested_wireless_lan.py",
        "src/fern/types/nested_wireless_lan_group.py",
        "src/fern/types/nested_wireless_link.py",
        "src/fern/types/object_change.py",
        "src/fern/types/object_change_action.py",
        "src/fern/types/object_change_action_label.py",
        "src/fern/types/object_change_action_value.py",
        "src/fern/types/platform.py",
        "src/fern/types/power_feed.py",
        "src/fern/types/power_feed_phase.py",
        "src/fern/types/power_feed_phase_label.py",
        "src/fern/types/power_feed_phase_value.py",
        "src/fern/types/power_feed_status.py",
        "src/fern/types/power_feed_status_label.py",
        "src/fern/types/power_feed_status_value.py",
        "src/fern/types/power_feed_supply.py",
        "src/fern/types/power_feed_supply_label.py",
        "src/fern/types/power_feed_supply_value.py",
        "src/fern/types/power_feed_type.py",
        "src/fern/types/power_feed_type_label.py",
        "src/fern/types/power_feed_type_value.py",
        "src/fern/types/power_outlet.py",
        "src/fern/types/power_outlet_feed_leg.py",
        "src/fern/types/power_outlet_feed_leg_label.py",
        "src/fern/types/power_outlet_feed_leg_value.py",
        "src/fern/types/power_outlet_template.py",
        "src/fern/types/power_outlet_template_feed_leg.py",
        "src/fern/types/power_outlet_template_feed_leg_label.py",
        "src/fern/types/power_outlet_template_feed_leg_value.py",
        "src/fern/types/power_outlet_template_type.py",
        "src/fern/types/power_outlet_type.py",
        "src/fern/types/power_panel.py",
        "src/fern/types/power_port.py",
        "src/fern/types/power_port_template.py",
        "src/fern/types/power_port_template_type.py",
        "src/fern/types/power_port_type.py",
        "src/fern/types/prefix.py",
        "src/fern/types/prefix_family.py",
        "src/fern/types/prefix_family_label.py",
        "src/fern/types/prefix_status.py",
        "src/fern/types/prefix_status_label.py",
        "src/fern/types/prefix_status_value.py",
        "src/fern/types/provider_network.py",
        "src/fern/types/rack.py",
        "src/fern/types/rack_outer_unit.py",
        "src/fern/types/rack_outer_unit_label.py",
        "src/fern/types/rack_outer_unit_value.py",
        "src/fern/types/rack_reservation.py",
        "src/fern/types/rack_role.py",
        "src/fern/types/rack_status.py",
        "src/fern/types/rack_status_label.py",
        "src/fern/types/rack_status_value.py",
        "src/fern/types/rack_type.py",
        "src/fern/types/rack_type_label.py",
        "src/fern/types/rack_type_value.py",
        "src/fern/types/rack_unit.py",
        "src/fern/types/rack_unit_face.py",
        "src/fern/types/rack_unit_face_label.py",
        "src/fern/types/rack_unit_face_value.py",
        "src/fern/types/rack_weight_unit.py",
        "src/fern/types/rack_weight_unit_label.py",
        "src/fern/types/rack_weight_unit_value.py",
        "src/fern/types/rack_width.py",
        "src/fern/types/rear_port.py",
        "src/fern/types/rear_port_template.py",
        "src/fern/types/rear_port_template_type.py",
        "src/fern/types/rear_port_type.py",
        "src/fern/types/region.py",
        "src/fern/types/rir.py",
        "src/fern/types/role.py",
        "src/fern/types/route_target.py",
        "src/fern/types/service_protocol.py",
        "src/fern/types/service_protocol_label.py",
        "src/fern/types/service_protocol_value.py",
        "src/fern/types/service_template.py",
        "src/fern/types/service_template_protocol.py",
        "src/fern/types/service_template_protocol_label.py",
        "src/fern/types/service_template_protocol_value.py",
        "src/fern/types/site_group.py",
        "src/fern/types/site_status.py",
        "src/fern/types/site_status_label.py",
        "src/fern/types/site_status_value.py",
        "src/fern/types/tag.py",
        "src/fern/types/tenant.py",
        "src/fern/types/tenant_group.py",
        "src/fern/types/token.py",
        "src/fern/types/virtual_chassis.py",
        "src/fern/types/virtual_device_context.py",
        "src/fern/types/virtual_device_context_status.py",
        "src/fern/types/virtual_machine_with_config_context.py",
        "src/fern/types/virtual_machine_with_config_context_status.py",
        "src/fern/types/virtual_machine_with_config_context_status_label.py",
        "src/fern/types/virtual_machine_with_config_context_status_value.py",
        "src/fern/types/vlan.py",
        "src/fern/types/vlan_group.py",
        "src/fern/types/vlan_status.py",
        "src/fern/types/vlan_status_label.py",
        "src/fern/types/vlan_status_value.py",
        "src/fern/types/vm_interface_mode.py",
        "src/fern/types/vm_interface_mode_label.py",
        "src/fern/types/vm_interface_mode_value.py",
        "src/fern/types/webhook_http_method.py",
        "src/fern/types/wireless_lan.py",
        "src/fern/types/wireless_lan_auth_cipher.py",
        "src/fern/types/wireless_lan_auth_cipher_label.py",
        "src/fern/types/wireless_lan_auth_cipher_value.py",
        "src/fern/types/wireless_lan_auth_type.py",
        "src/fern/types/wireless_lan_auth_type_label.py",
        "src/fern/types/wireless_lan_auth_type_value.py",
        "src/fern/types/wireless_lan_group.py",
        "src/fern/types/wireless_lan_status.py",
        "src/fern/types/wireless_lan_status_label.py",
        "src/fern/types/wireless_lan_status_value.py",
        "src/fern/types/wireless_link.py",
        "src/fern/types/wireless_link_auth_cipher.py",
        "src/fern/types/wireless_link_auth_cipher_label.py",
        "src/fern/types/wireless_link_auth_cipher_value.py",
        "src/fern/types/wireless_link_auth_type.py",
        "src/fern/types/wireless_link_auth_type_label.py",
        "src/fern/types/wireless_link_auth_type_value.py",
        "src/fern/types/wireless_link_status.py",
        "src/fern/types/wireless_link_status_label.py",
        "src/fern/types/wireless_link_status_value.py",
        "src/fern/types/writable_aggregate.py",
        "src/fern/types/writable_asn.py",
        "src/fern/types/writable_available_ip.py",
        "src/fern/types/writable_cable.py",
        "src/fern/types/writable_cable_length_unit.py",
        "src/fern/types/writable_cable_status.py",
        "src/fern/types/writable_cable_type.py",
        "src/fern/types/writable_circuit.py",
        "src/fern/types/writable_circuit_status.py",
        "src/fern/types/writable_circuit_termination.py",
        "src/fern/types/writable_circuit_termination_term_side.py",
        "src/fern/types/writable_cluster.py",
        "src/fern/types/writable_cluster_status.py",
        "src/fern/types/writable_console_port.py",
        "src/fern/types/writable_console_port_template.py",
        "src/fern/types/writable_console_server_port.py",
        "src/fern/types/writable_console_server_port_template.py",
        "src/fern/types/writable_contact.py",
        "src/fern/types/writable_contact_assignment.py",
        "src/fern/types/writable_contact_assignment_priority.py",
        "src/fern/types/writable_contact_group.py",
        "src/fern/types/writable_custom_field_filter_logic.py",
        "src/fern/types/writable_custom_field_type.py",
        "src/fern/types/writable_custom_field_ui_visibility.py",
        "src/fern/types/writable_device_bay.py",
        "src/fern/types/writable_device_bay_template.py",
        "src/fern/types/writable_device_type.py",
        "src/fern/types/writable_device_type_airflow.py",
        "src/fern/types/writable_device_type_subdevice_role.py",
        "src/fern/types/writable_device_type_weight_unit.py",
        "src/fern/types/writable_device_with_config_context.py",
        "src/fern/types/writable_device_with_config_context_airflow.py",
        "src/fern/types/writable_device_with_config_context_face.py",
        "src/fern/types/writable_device_with_config_context_status.py",
        "src/fern/types/writable_fhrp_group_assignment.py",
        "src/fern/types/writable_front_port.py",
        "src/fern/types/writable_front_port_template.py",
        "src/fern/types/writable_interface_duplex.py",
        "src/fern/types/writable_interface_mode.py",
        "src/fern/types/writable_interface_poe_mode.py",
        "src/fern/types/writable_interface_rf_role.py",
        "src/fern/types/writable_interface_template.py",
        "src/fern/types/writable_interface_template_poe_mode.py",
        "src/fern/types/writable_inventory_item.py",
        "src/fern/types/writable_inventory_item_template.py",
        "src/fern/types/writable_ip_address.py",
        "src/fern/types/writable_ip_address_role.py",
        "src/fern/types/writable_ip_address_status.py",
        "src/fern/types/writable_ip_range.py",
        "src/fern/types/writable_ip_range_status.py",
        "src/fern/types/writable_journal_entry.py",
        "src/fern/types/writable_journal_entry_kind.py",
        "src/fern/types/writable_l2vpn_termination.py",
        "src/fern/types/writable_l2vpn_type.py",
        "src/fern/types/writable_location.py",
        "src/fern/types/writable_location_status.py",
        "src/fern/types/writable_module.py",
        "src/fern/types/writable_module_bay.py",
        "src/fern/types/writable_module_bay_template.py",
        "src/fern/types/writable_module_status.py",
        "src/fern/types/writable_module_type.py",
        "src/fern/types/writable_module_type_weight_unit.py",
        "src/fern/types/writable_platform.py",
        "src/fern/types/writable_power_feed.py",
        "src/fern/types/writable_power_feed_phase.py",
        "src/fern/types/writable_power_feed_status.py",
        "src/fern/types/writable_power_feed_supply.py",
        "src/fern/types/writable_power_feed_type.py",
        "src/fern/types/writable_power_outlet.py",
        "src/fern/types/writable_power_outlet_feed_leg.py",
        "src/fern/types/writable_power_outlet_template.py",
        "src/fern/types/writable_power_outlet_template_feed_leg.py",
        "src/fern/types/writable_power_panel.py",
        "src/fern/types/writable_power_port.py",
        "src/fern/types/writable_power_port_template.py",
        "src/fern/types/writable_prefix.py",
        "src/fern/types/writable_prefix_status.py",
        "src/fern/types/writable_provider_network.py",
        "src/fern/types/writable_rack.py",
        "src/fern/types/writable_rack_outer_unit.py",
        "src/fern/types/writable_rack_reservation.py",
        "src/fern/types/writable_rack_status.py",
        "src/fern/types/writable_rack_type.py",
        "src/fern/types/writable_rack_weight_unit.py",
        "src/fern/types/writable_rear_port.py",
        "src/fern/types/writable_rear_port_template.py",
        "src/fern/types/writable_region.py",
        "src/fern/types/writable_route_target.py",
        "src/fern/types/writable_service_protocol.py",
        "src/fern/types/writable_service_template.py",
        "src/fern/types/writable_service_template_protocol.py",
        "src/fern/types/writable_site_group.py",
        "src/fern/types/writable_site_status.py",
        "src/fern/types/writable_tenant.py",
        "src/fern/types/writable_tenant_group.py",
        "src/fern/types/writable_token.py",
        "src/fern/types/writable_virtual_chassis.py",
        "src/fern/types/writable_virtual_device_context.py",
        "src/fern/types/writable_virtual_device_context_status.py",
        "src/fern/types/writable_virtual_machine_with_config_context.py",
        "src/fern/types/writable_virtual_machine_with_config_context_status.py",
        "src/fern/types/writable_vlan.py",
        "src/fern/types/writable_vlan_status.py",
        "src/fern/types/writable_vm_interface_mode.py",
        "src/fern/types/writable_wireless_lan.py",
        "src/fern/types/writable_wireless_lan_auth_cipher.py",
        "src/fern/types/writable_wireless_lan_auth_type.py",
        "src/fern/types/writable_wireless_lan_group.py",
        "src/fern/types/writable_wireless_lan_status.py",
        "src/fern/types/writable_wireless_link.py",
        "src/fern/types/writable_wireless_link_auth_cipher.py",
        "src/fern/types/writable_wireless_link_auth_type.py",
        "src/fern/types/writable_wireless_link_status.py",
        "src/fern/users/__init__.py",
        "src/fern/users/types/__init__.py",
        "src/fern/users/types/users_groups_list_response.py",
        "src/fern/users/types/users_permissions_list_response.py",
        "src/fern/users/types/users_tokens_list_response.py",
        "src/fern/users/types/users_users_list_response.py",
        "src/fern/version.py",
        "src/fern/virtualization/__init__.py",
        "src/fern/virtualization/types/__init__.py",
        "src/fern/virtualization/types/virtualization_cluster_groups_list_response.py",
        "src/fern/virtualization/types/virtualization_cluster_types_list_response.py",
        "src/fern/virtualization/types/virtualization_clusters_list_response.py",
        "src/fern/virtualization/types/virtualization_interfaces_list_response.py",
        "src/fern/virtualization/types/virtualization_virtual_machines_list_response.py",
        "src/fern/wireless/__init__.py",
        "src/fern/wireless/types/__init__.py",
        "src/fern/wireless/types/wireless_wireless_lan_groups_list_response.py",
        "src/fern/wireless/types/wireless_wireless_lans_list_response.py",
        "src/fern/wireless/types/wireless_wireless_links_list_response.py",
        // Reporter-approved after enum numeric smart-casing and declared-empty
        // parameter descriptions were matched to Fern.
        "src/fern/circuits/client.py",
        "src/fern/circuits/raw_client.py",
        "src/fern/dcim/raw_client.py",
        "src/fern/extras/client.py",
        "src/fern/extras/raw_client.py",
        "src/fern/tenancy/client.py",
        "src/fern/tenancy/raw_client.py",
        "src/fern/types/console_port_speed_label.py",
        "src/fern/types/console_port_template_type_label.py",
        "src/fern/types/console_port_template_type_value.py",
        "src/fern/types/console_port_type_label.py",
        "src/fern/types/console_port_type_value.py",
        "src/fern/types/console_server_port_speed_label.py",
        "src/fern/types/console_server_port_template_type_label.py",
        "src/fern/types/console_server_port_template_type_value.py",
        "src/fern/types/console_server_port_type_label.py",
        "src/fern/types/console_server_port_type_value.py",
        "src/fern/types/front_port_template_type_label.py",
        "src/fern/types/front_port_type_label.py",
        "src/fern/types/interface_poe_type_label.py",
        "src/fern/types/interface_poe_type_value.py",
        "src/fern/types/interface_rf_channel_label.py",
        "src/fern/types/interface_template_poe_type_label.py",
        "src/fern/types/interface_template_poe_type_value.py",
        "src/fern/types/rack_width_label.py",
        "src/fern/types/rear_port_template_type_label.py",
        "src/fern/types/rear_port_type_label.py",
        "src/fern/types/writable_console_port_template_type.py",
        "src/fern/types/writable_console_port_type.py",
        "src/fern/types/writable_console_server_port_template_type.py",
        "src/fern/types/writable_console_server_port_type.py",
        "src/fern/types/writable_interface_poe_type.py",
        "src/fern/types/writable_interface_template_poe_type.py",
        "src/fern/users/client.py",
        "src/fern/users/raw_client.py",
        "src/fern/virtualization/client.py",
        "src/fern/virtualization/raw_client.py",
        "src/fern/wireless/client.py",
        "src/fern/wireless/raw_client.py",
        // Reporter-approved after numeric-prefix enum names were matched.
        "src/fern/dcim/client.py",
        "src/fern/types/front_port_template_type_value.py",
        "src/fern/types/front_port_type_value.py",
        "src/fern/types/interface_rf_channel_value.py",
        "src/fern/types/rear_port_template_type_value.py",
        "src/fern/types/rear_port_type_value.py",
        "src/fern/types/writable_front_port_template_type.py",
        "src/fern/types/writable_front_port_type.py",
        "src/fern/types/writable_interface_rf_channel.py",
        "src/fern/types/writable_rear_port_template_type.py",
        "src/fern/types/writable_rear_port_type.py",
        // Reporter-approved after single-letter enum fragments were matched.
        "src/fern/types/interface_template_type_label.py",
        "src/fern/types/interface_type_label.py",
        // Reporter-approved after unique-items list semantics were matched.
        "src/fern/types/config_context.py",
        "src/fern/types/custom_field.py",
        "src/fern/types/custom_link.py",
        "src/fern/types/export_template.py",
        "src/fern/types/interface.py",
        "src/fern/types/interface_template_type_value.py",
        "src/fern/types/interface_type_value.py",
        "src/fern/types/l2vpn.py",
        "src/fern/types/object_permission.py",
        "src/fern/types/provider.py",
        "src/fern/types/saved_filter.py",
        "src/fern/types/service.py",
        "src/fern/types/site.py",
        "src/fern/types/user.py",
        "src/fern/types/vm_interface.py",
        "src/fern/types/vrf.py",
        "src/fern/types/webhook.py",
        "src/fern/types/writable_config_context.py",
        "src/fern/types/writable_custom_field.py",
        "src/fern/types/writable_interface.py",
        "src/fern/types/writable_interface_template_type.py",
        "src/fern/types/writable_interface_type.py",
        "src/fern/types/writable_l2vpn.py",
        "src/fern/types/writable_object_permission.py",
        "src/fern/types/writable_provider.py",
        "src/fern/types/writable_service.py",
        "src/fern/types/writable_site.py",
        "src/fern/types/writable_user.py",
        "src/fern/types/writable_vm_interface.py",
        "src/fern/types/writable_vrf.py",
        // Reporter-approved after single-letter enum runs were matched.
        "src/fern/types/power_outlet_template_type_label.py",
        "src/fern/types/power_outlet_type_label.py",
        "src/fern/types/power_port_template_type_label.py",
        "src/fern/types/power_port_type_label.py",
        // Reporter-approved after numeric single-letter enum runs were matched.
        "src/fern/types/power_outlet_template_type_value.py",
        "src/fern/types/power_outlet_type_value.py",
        "src/fern/types/power_port_template_type_value.py",
        "src/fern/types/power_port_type_value.py",
        "src/fern/types/writable_power_outlet_template_type.py",
        "src/fern/types/writable_power_outlet_type.py",
        "src/fern/types/writable_power_port_template_type.py",
        "src/fern/types/writable_power_port_type.py",
        // Reporter-approved after digit-boundary Pascal casing was matched.
        "src/fern/__init__.py",
        "src/fern/ipam/__init__.py",
        "src/fern/ipam/client.py",
        "src/fern/ipam/raw_client.py",
        "src/fern/ipam/types/__init__.py",
        "src/fern/ipam/types/ipam_l2vpn_terminations_list_response.py",
        "src/fern/ipam/types/ipam_l2vpns_list_response.py",
        // Reporter-approved after reference parameter descriptions were matched.
        "reference.md",
    ],
};

const CORPORA: &[&Corpus] = &[
    &QUERY_PARAMETERS,
    &EXHAUSTIVE,
    &APIDECK_CRM,
    &BUNQ,
    &BUNGIE,
    &ANCHORE,
    &APACHE_AIRFLOW,
    &DISCOURSE,
    &APPWRITE_SERVER,
    &APICURIO,
    &GAMBITCOMM_MIMIC,
    &DND5EAPI,
    &APACHE_QAKKA,
    &AUTHENTIQIO,
    &ETSI_MEC010_2,
    &APIDECK_WEBHOOK,
    &APIDECK_VAULT,
    &AIRBYTE_CONFIG,
    &BINTABLE,
    &APIS_GURU,
    &COLOR_PIZZA,
    &BYAUTOMATA_IO,
    &APIDECK_PROXY,
    &APIDECK_CONNECTOR,
    &APIDECK_ECOMMERCE,
    &APIDECK_ISSUE_TRACKING,
    &APPWRITE_CLIENT,
    &APIDECK_FILE_STORAGE,
    &APIDECK_HRIS,
    &APIDECK_ACCOUNTING,
    &CALORIENINJAS,
    &EOS,
    &APIDECK_SMS,
    &APIDECK_ECOSYSTEM,
    &APIDECK_CUSTOMER_SUPPORT,
    &APIDECK_LEAD,
    &APACHE_ORG_AIRFLOW,
    &OPENFIGI,
    &TWILIO_VOICE_V1,
    &MICROCKS_LOCAL,
    &REDHAT_CATALOG_INVENTORY,
    &XERO_PAYROLL_AU,
    &TRACCAR,
    &REVERB_COM,
    &MAIF_OTOROSHI,
    &PORTFOLIOOPTIMIZER_IO,
    &OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI,
    &NETBOX_DEV,
    &SQUAREUP_COM,
    &AMAZONAWS_COM_CLOUDFORMATION,
    &REDOCLY_COM_MUSEUM,
    &HTTP_TOOLKIT,
    &FRANKFURTER,
    &WORLDCOIN_SIGNUP_SEQUENCER,
    &ELECTRIC_SQL,
    &TAMOSS,
    &SLURMDB_REST,
    &NIMISAMPO,
    &FREE5GC_PDU_SESSION,
    &SIGSTORE_REKOR,
    &LETTA,
    &FREE5GC_NAMF_COMMUNICATION,
];

#[test]
fn every_matched_entry_exists_in_its_own_golden() {
    // Single source of truth: iterate the CORPORA registry directly and identify each
    // corpus by its unique `api` (which maps 1:1 to a `const _: Corpus`), so there is no
    // parallel name array to drift out of sync with it.
    let mut violations = Vec::new();
    for corpus in CORPORA {
        let expected = fixture_dir(corpus.api).join("expected");
        for relative in corpus.matched {
            if !expected.join(relative).is_file() {
                violations.push(format!("{} -> {relative}", corpus.api));
            }
        }
    }
    assert!(
        violations.is_empty(),
        "matched entries missing from their corpus golden:\n{}",
        violations.join("\n")
    );
}

#[test]
fn bunq_matches_fern_output() {
    // `link-ok` like apideck: the spec is fetched (not vendored), so this **skips**
    // when it is absent — including the offline `check` gate — and **fails** when
    // `CROZIER_REQUIRE_CORPUS` is set (the CI corpus leg fetches first, then sets
    // it), so the enforced leg can never silently no-op. Unlike apideck, bunq is not
    // yet fully matched, so this byte-compares only `BUNQ.matched` (via
    // `assert_corpus_matches`) rather than walking the whole golden tree.
    if corpus_spec(BUNQ.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the bunq corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping bunq byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&BUNQ);
}

#[test]
fn bungie_matches_fern_output() {
    // `link-ok` like apideck and bunq: the spec is fetched (not vendored), so this
    // **skips** when it is absent — including the offline `check` gate — and
    // **fails** when `CROZIER_REQUIRE_CORPUS` is set (the CI corpus leg fetches
    // first, then sets it), so the enforced leg can never silently no-op.
    // `BUNGIE_MATCHED` covers the full committed golden, so this enforces the
    // schema-heavy corpus as a byte-match gate once the spec has been fetched.
    if corpus_spec(BUNGIE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the bungie corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping bungie byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&BUNGIE);
}

// The five batch corpora below share the bunq/bungie test shape: `link-ok` (spec
// fetched, not vendored) so each **skips** offline — including the `check` gate — and
// **fails** when `CROZIER_REQUIRE_CORPUS` is set without a fetched spec, so an
// enforced leg can never silently no-op. Each `matched` list is empty until its Fern
// golden is generated and the byte-match pass grows it, so today they assert only
// that crozier consumes the fetched spec and writes a tree without panicking. The
// three with a named generator gap on their const (anchore, apache, apicurio) reach
// that bar once the byte-match pass closes the gap; discourse and appwrite already do.

#[test]
fn anchore_matches_fern_output() {
    if corpus_spec(ANCHORE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the anchore corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping anchore byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&ANCHORE);
}

#[test]
fn apache_airflow_matches_fern_output() {
    if corpus_spec(APACHE_AIRFLOW.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apache corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping apache byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&APACHE_AIRFLOW);
}

#[test]
fn discourse_matches_fern_output() {
    if corpus_spec(DISCOURSE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the discourse corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping discourse byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&DISCOURSE);
}

#[test]
fn appwrite_server_matches_fern_output() {
    if corpus_spec(APPWRITE_SERVER.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the appwrite corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping appwrite byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&APPWRITE_SERVER);
}

#[test]
fn apicurio_matches_fern_output() {
    if corpus_spec(APICURIO.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apicurio corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping apicurio byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&APICURIO);
}

#[test]
fn gambitcomm_mimic_matches_fern_output() {
    if corpus_spec(GAMBITCOMM_MIMIC.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the gambitcomm corpus spec is not fetched; \
             run scripts/fetch-corpus.sh first"
        );
        eprintln!("skipping gambitcomm byte-match: spec not fetched (run scripts/fetch-corpus.sh)");
        return;
    }
    assert_corpus_matches(&GAMBITCOMM_MIMIC);
}

#[test]
fn dnd5eapi_matches_fern_output() {
    if corpus_spec(DND5EAPI.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the dnd5eapi corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&DND5EAPI);
}

#[test]
fn apache_qakka_matches_fern_output() {
    if corpus_spec(APACHE_QAKKA.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apache-qakka corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APACHE_QAKKA);
}

#[test]
fn authentiqio_matches_fern_output() {
    if corpus_spec(AUTHENTIQIO.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the authentiqio corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&AUTHENTIQIO);
}

#[test]
fn etsi_mec010_2_matches_fern_output() {
    if corpus_spec(ETSI_MEC010_2.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the ETSI MEC 010-2 corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&ETSI_MEC010_2);
}

#[test]
fn apideck_webhook_matches_fern_output() {
    if corpus_spec(APIDECK_WEBHOOK.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Webhook corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_WEBHOOK);
}

#[test]
fn apideck_vault_matches_fern_output() {
    if corpus_spec(APIDECK_VAULT.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Vault corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_VAULT);
}

#[test]
fn airbyte_config_matches_fern_output() {
    if corpus_spec(AIRBYTE_CONFIG.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Airbyte Config corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&AIRBYTE_CONFIG);
}

#[test]
fn bintable_matches_fern_output() {
    if corpus_spec(BINTABLE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Bintable corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&BINTABLE);
}

#[test]
fn apis_guru_matches_fern_output() {
    if corpus_spec(APIS_GURU.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the APIs.guru corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIS_GURU);
}

#[test]
fn color_pizza_matches_fern_output() {
    if corpus_spec(COLOR_PIZZA.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Color Pizza corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&COLOR_PIZZA);
}

#[test]
fn byautomata_io_matches_fern_output() {
    if corpus_spec(BYAUTOMATA_IO.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the By Automata corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&BYAUTOMATA_IO);
}

#[test]
fn apideck_proxy_matches_fern_output() {
    if corpus_spec(APIDECK_PROXY.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Proxy corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_PROXY);
}

#[test]
fn apideck_connector_matches_fern_output() {
    if corpus_spec(APIDECK_CONNECTOR.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Connector corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_CONNECTOR);
}

#[test]
fn apideck_ecommerce_matches_fern_output() {
    if corpus_spec(APIDECK_ECOMMERCE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Ecommerce corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_ECOMMERCE);
}

#[test]
fn apideck_issue_tracking_matches_fern_output() {
    if corpus_spec(APIDECK_ISSUE_TRACKING.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Issue Tracking corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_ISSUE_TRACKING);
}

#[test]
fn appwrite_client_matches_fern_output() {
    if corpus_spec(APPWRITE_CLIENT.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Appwrite Client corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APPWRITE_CLIENT);
}

#[test]
fn apideck_file_storage_matches_fern_output() {
    if corpus_spec(APIDECK_FILE_STORAGE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck File Storage corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_FILE_STORAGE);
}

#[test]
fn apideck_hris_matches_fern_output() {
    if corpus_spec(APIDECK_HRIS.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck HRIS corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_HRIS);
}

#[test]
fn apideck_accounting_matches_fern_output() {
    if corpus_spec(APIDECK_ACCOUNTING.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Accounting corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_ACCOUNTING);
}

#[test]
fn calorieninjas_reproduces_the_exact_known_fern_failure_boundary() {
    if corpus_spec(CALORIENINJAS.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the CalorieNinjas corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    let known = known_fern_failure(&CALORIENINJAS)
        .expect("known Fern failure contract must be valid")
        .expect("CalorieNinjas must register its Fern 5.20 failure");
    let out = generate_corpus(&CALORIENINJAS);
    let client = std::fs::read_to_string(out.path().join("src/fern/client.py"))
        .expect("Crozier generated a valid CalorieNinjas client");
    let raw_client = std::fs::read_to_string(out.path().join("src/fern/raw_client.py"))
        .expect("Crozier generated a valid CalorieNinjas raw client");
    assert!(!client.contains("def ("), "Crozier must name the operation");
    assert!(
        !raw_client.contains("def ("),
        "Crozier must name the operation"
    );
    assert_eq!(
        known_fern_failure_marker(&CALORIENINJAS, &known),
        "KNOWN UPSTREAM FERN FAILURE: calorieninjas.com at fernapi/fern-python-sdk:5.20.0; Crozier generation succeeded."
    );
}

#[test]
fn eos_matches_fern_output() {
    if corpus_spec(EOS.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the EOS corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&EOS);
}

#[test]
fn apideck_sms_matches_fern_output() {
    if corpus_spec(APIDECK_SMS.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck SMS corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_SMS);
}

#[test]
fn apideck_ecosystem_matches_fern_output() {
    if corpus_spec(APIDECK_ECOSYSTEM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Ecosystem corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_ECOSYSTEM);
}

#[test]
fn apideck_customer_support_matches_fern_output() {
    if corpus_spec(APIDECK_CUSTOMER_SUPPORT.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Customer Support corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_CUSTOMER_SUPPORT);
}

#[test]
fn apideck_lead_matches_fern_output() {
    if corpus_spec(APIDECK_LEAD.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Lead corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_LEAD);
}

#[test]
fn apache_org_airflow_matches_fern_output() {
    if corpus_spec(APACHE_ORG_AIRFLOW.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apache Airflow corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&APACHE_ORG_AIRFLOW);
}

#[test]
fn openfigi_com_matches_fern_output() {
    if corpus_spec(OPENFIGI.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the OpenFIGI corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&OPENFIGI);
}

#[test]
fn twilio_voice_v1_matches_fern_output() {
    if corpus_spec(TWILIO_VOICE_V1.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Twilio Voice v1 corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&TWILIO_VOICE_V1);
}

#[test]
fn microcks_local_matches_fern_output() {
    if corpus_spec(MICROCKS_LOCAL.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Microcks corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&MICROCKS_LOCAL);
}

#[test]
fn redhat_catalog_inventory_matches_fern_output() {
    if corpus_spec(REDHAT_CATALOG_INVENTORY.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Red Hat Catalog Inventory corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&REDHAT_CATALOG_INVENTORY);
}

#[test]
fn xero_payroll_au_matches_fern_output() {
    if corpus_spec(XERO_PAYROLL_AU.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Xero Payroll AU corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&XERO_PAYROLL_AU);
}

#[test]
fn traccar_matches_fern_output() {
    if corpus_spec(TRACCAR.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Traccar corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&TRACCAR);
}

#[test]
fn reverb_com_matches_fern_output() {
    if corpus_spec(REVERB_COM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Reverb corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&REVERB_COM);
}

#[test]
fn maif_otoroshi_matches_fern_output() {
    if corpus_spec(MAIF_OTOROSHI.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the MAIF Otoroshi corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&MAIF_OTOROSHI);
}

#[test]
fn portfoliooptimizer_io_matches_fern_output() {
    if corpus_spec(PORTFOLIOOPTIMIZER_IO.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Portfolio Optimizer corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&PORTFOLIOOPTIMIZER_IO);
}

#[test]
fn openbanking_org_uk_account_info_openapi_matches_fern_output() {
    if corpus_spec(OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Open Banking account info corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI);
}

#[test]
fn netbox_dev_matches_fern_output() {
    if corpus_spec(NETBOX_DEV.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the NetBox corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&NETBOX_DEV);
}

const SQUAREUP_COM: Corpus = Corpus {
    api: "squareup.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/apple_pay/__init__.py",
        "src/fern/apple_pay/raw_client.py",
        "src/fern/bank_accounts/__init__.py",
        "src/fern/bank_accounts/raw_client.py",
        "src/fern/bookings/__init__.py",
        "src/fern/bookings/raw_client.py",
        "src/fern/cards/__init__.py",
        "src/fern/cash_drawers/__init__.py",
        "src/fern/cash_drawers/raw_client.py",
        "src/fern/catalog/__init__.py",
        "src/fern/checkout/__init__.py",
        "src/fern/checkout/raw_client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/customer_groups/__init__.py",
        "src/fern/customer_segments/__init__.py",
        "src/fern/customer_segments/raw_client.py",
        "src/fern/customers/__init__.py",
        "src/fern/devices/__init__.py",
        "src/fern/devices/raw_client.py",
        "src/fern/disputes/__init__.py",
        "src/fern/disputes/raw_client.py",
        "src/fern/employees/__init__.py",
        "src/fern/employees/raw_client.py",
        "src/fern/environment.py",
        "src/fern/gift_card_activities/__init__.py",
        "src/fern/gift_card_activities/raw_client.py",
        "src/fern/gift_cards/__init__.py",
        "src/fern/gift_cards/raw_client.py",
        "src/fern/inventory/__init__.py",
        "src/fern/inventory/raw_client.py",
        "src/fern/invoices/__init__.py",
        "src/fern/labor/__init__.py",
        "src/fern/locations/__init__.py",
        "src/fern/loyalty/__init__.py",
        "src/fern/merchants/__init__.py",
        "src/fern/merchants/raw_client.py",
        "src/fern/mobile_authorization/__init__.py",
        "src/fern/o_auth/__init__.py",
        "src/fern/o_auth/raw_client.py",
        "src/fern/orders/__init__.py",
        "src/fern/payments/__init__.py",
        "src/fern/py.typed",
        "src/fern/refunds/__init__.py",
        "src/fern/sites/__init__.py",
        "src/fern/sites/raw_client.py",
        "src/fern/snippets/__init__.py",
        "src/fern/snippets/raw_client.py",
        "src/fern/subscriptions/__init__.py",
        "src/fern/team/__init__.py",
        "src/fern/terminal/__init__.py",
        "src/fern/terminal/raw_client.py",
        "src/fern/transactions/__init__.py",
        "src/fern/transactions/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/accept_dispute_request.py",
        "src/fern/types/accept_dispute_response.py",
        "src/fern/types/accumulate_loyalty_points_response.py",
        "src/fern/types/ach_details.py",
        "src/fern/types/action_cancel_reason.py",
        "src/fern/types/add_group_to_customer_request.py",
        "src/fern/types/add_group_to_customer_response.py",
        "src/fern/types/additional_recipient.py",
        "src/fern/types/address.py",
        "src/fern/types/adjust_loyalty_points_response.py",
        "src/fern/types/appointment_segment.py",
        "src/fern/types/availability.py",
        "src/fern/types/bank_account.py",
        "src/fern/types/bank_account_payment_details.py",
        "src/fern/types/bank_account_status.py",
        "src/fern/types/bank_account_type.py",
        "src/fern/types/batch_change_inventory_request.py",
        "src/fern/types/batch_change_inventory_response.py",
        "src/fern/types/batch_delete_catalog_objects_response.py",
        "src/fern/types/batch_retrieve_catalog_objects_response.py",
        "src/fern/types/batch_retrieve_inventory_changes_request.py",
        "src/fern/types/batch_retrieve_inventory_changes_response.py",
        "src/fern/types/batch_retrieve_inventory_counts_request.py",
        "src/fern/types/batch_retrieve_inventory_counts_response.py",
        "src/fern/types/batch_retrieve_orders_response.py",
        "src/fern/types/batch_upsert_catalog_objects_response.py",
        "src/fern/types/booking.py",
        "src/fern/types/booking_status.py",
        "src/fern/types/break_.py",
        "src/fern/types/break_type.py",
        "src/fern/types/bulk_create_team_members_response.py",
        "src/fern/types/bulk_update_team_members_response.py",
        "src/fern/types/business_appointment_settings.py",
        "src/fern/types/business_appointment_settings_alignment_time.py",
        "src/fern/types/business_appointment_settings_booking_location_type.py",
        "src/fern/types/business_appointment_settings_cancellation_policy.py",
        "src/fern/types/business_appointment_settings_max_appointments_per_day_limit_type.py",
        "src/fern/types/business_booking_profile.py",
        "src/fern/types/business_booking_profile_booking_policy.py",
        "src/fern/types/business_booking_profile_customer_timezone_choice.py",
        "src/fern/types/business_hours.py",
        "src/fern/types/business_hours_period.py",
        "src/fern/types/calculate_loyalty_points_response.py",
        "src/fern/types/calculate_order_response.py",
        "src/fern/types/cancel_booking_response.py",
        "src/fern/types/cancel_invoice_response.py",
        "src/fern/types/cancel_payment_by_idempotency_key_response.py",
        "src/fern/types/cancel_payment_request.py",
        "src/fern/types/cancel_payment_response.py",
        "src/fern/types/cancel_subscription_request.py",
        "src/fern/types/cancel_subscription_response.py",
        "src/fern/types/cancel_terminal_checkout_request.py",
        "src/fern/types/cancel_terminal_checkout_response.py",
        "src/fern/types/cancel_terminal_refund_request.py",
        "src/fern/types/cancel_terminal_refund_response.py",
        "src/fern/types/capture_transaction_request.py",
        "src/fern/types/capture_transaction_response.py",
        "src/fern/types/card.py",
        "src/fern/types/card_brand.py",
        "src/fern/types/card_payment_details.py",
        "src/fern/types/card_payment_timeline.py",
        "src/fern/types/card_prepaid_type.py",
        "src/fern/types/card_square_product.py",
        "src/fern/types/card_type.py",
        "src/fern/types/cash_drawer_device.py",
        "src/fern/types/cash_drawer_event_type.py",
        "src/fern/types/cash_drawer_shift.py",
        "src/fern/types/cash_drawer_shift_event.py",
        "src/fern/types/cash_drawer_shift_state.py",
        "src/fern/types/cash_drawer_shift_summary.py",
        "src/fern/types/cash_payment_details.py",
        "src/fern/types/catalog_category.py",
        "src/fern/types/catalog_custom_attribute_definition.py",
        "src/fern/types/catalog_custom_attribute_definition_app_visibility.py",
        "src/fern/types/catalog_custom_attribute_definition_number_config.py",
        "src/fern/types/catalog_custom_attribute_definition_selection_config.py",
        "src/fern/types/catalog_custom_attribute_definition_selection_config_custom_attribute_selection.py",
        "src/fern/types/catalog_custom_attribute_definition_seller_visibility.py",
        "src/fern/types/catalog_custom_attribute_definition_string_config.py",
        "src/fern/types/catalog_custom_attribute_definition_type.py",
        "src/fern/types/catalog_custom_attribute_value.py",
        "src/fern/types/catalog_discount.py",
        "src/fern/types/catalog_discount_modify_tax_basis.py",
        "src/fern/types/catalog_discount_type.py",
        "src/fern/types/catalog_id_mapping.py",
        "src/fern/types/catalog_image.py",
        "src/fern/types/catalog_info_request.py",
        "src/fern/types/catalog_info_response.py",
        "src/fern/types/catalog_info_response_limits.py",
        "src/fern/types/catalog_item.py",
        "src/fern/types/catalog_item_modifier_list_info.py",
        "src/fern/types/catalog_item_option.py",
        "src/fern/types/catalog_item_option_value.py",
        "src/fern/types/catalog_item_option_value_for_item_variation.py",
        "src/fern/types/catalog_item_product_type.py",
        "src/fern/types/catalog_item_variation.py",
        "src/fern/types/catalog_measurement_unit.py",
        "src/fern/types/catalog_modifier.py",
        "src/fern/types/catalog_modifier_list.py",
        "src/fern/types/catalog_modifier_list_selection_type.py",
        "src/fern/types/catalog_modifier_override.py",
        "src/fern/types/catalog_object.py",
        "src/fern/types/catalog_object_batch.py",
        "src/fern/types/catalog_object_reference.py",
        "src/fern/types/catalog_object_type.py",
        "src/fern/types/catalog_pricing_rule.py",
        "src/fern/types/catalog_pricing_type.py",
        "src/fern/types/catalog_product_set.py",
        "src/fern/types/catalog_query.py",
        "src/fern/types/catalog_query_exact.py",
        "src/fern/types/catalog_query_item_variations_for_item_option_values.py",
        "src/fern/types/catalog_query_items_for_item_options.py",
        "src/fern/types/catalog_query_items_for_modifier_list.py",
        "src/fern/types/catalog_query_items_for_tax.py",
        "src/fern/types/catalog_query_prefix.py",
        "src/fern/types/catalog_query_range.py",
        "src/fern/types/catalog_query_set.py",
        "src/fern/types/catalog_query_sorted_attribute.py",
        "src/fern/types/catalog_query_text.py",
        "src/fern/types/catalog_quick_amount.py",
        "src/fern/types/catalog_quick_amount_type.py",
        "src/fern/types/catalog_quick_amounts_settings.py",
        "src/fern/types/catalog_quick_amounts_settings_option.py",
        "src/fern/types/catalog_stock_conversion.py",
        "src/fern/types/catalog_subscription_plan.py",
        "src/fern/types/catalog_tax.py",
        "src/fern/types/catalog_time_period.py",
        "src/fern/types/catalog_v1id.py",
        "src/fern/types/charge_request_additional_recipient.py",
        "src/fern/types/charge_response.py",
        "src/fern/types/check_appointments_onboarded_request.py",
        "src/fern/types/checkout.py",
        "src/fern/types/checkout_options_payment_type.py",
        "src/fern/types/complete_payment_request.py",
        "src/fern/types/complete_payment_response.py",
        "src/fern/types/coordinates.py",
        "src/fern/types/country.py",
        "src/fern/types/create_booking_response.py",
        "src/fern/types/create_break_type_response.py",
        "src/fern/types/create_card_response.py",
        "src/fern/types/create_checkout_response.py",
        "src/fern/types/create_customer_card_response.py",
        "src/fern/types/create_customer_group_response.py",
        "src/fern/types/create_customer_response.py",
        "src/fern/types/create_device_code_response.py",
        "src/fern/types/create_dispute_evidence_text_response.py",
        "src/fern/types/create_gift_card_activity_response.py",
        "src/fern/types/create_gift_card_response.py",
        "src/fern/types/create_invoice_response.py",
        "src/fern/types/create_location_response.py",
        "src/fern/types/create_loyalty_account_response.py",
        "src/fern/types/create_loyalty_reward_response.py",
        "src/fern/types/create_mobile_authorization_code_response.py",
        "src/fern/types/create_order_request.py",
        "src/fern/types/create_order_response.py",
        "src/fern/types/create_payment_response.py",
        "src/fern/types/create_refund_response.py",
        "src/fern/types/create_shift_response.py",
        "src/fern/types/create_subscription_response.py",
        "src/fern/types/create_team_member_request.py",
        "src/fern/types/create_team_member_response.py",
        "src/fern/types/create_terminal_checkout_response.py",
        "src/fern/types/create_terminal_refund_response.py",
        "src/fern/types/currency.py",
        "src/fern/types/custom_attribute_filter.py",
        "src/fern/types/customer.py",
        "src/fern/types/customer_creation_source.py",
        "src/fern/types/customer_creation_source_filter.py",
        "src/fern/types/customer_filter.py",
        "src/fern/types/customer_group.py",
        "src/fern/types/customer_inclusion_exclusion.py",
        "src/fern/types/customer_preferences.py",
        "src/fern/types/customer_query.py",
        "src/fern/types/customer_segment.py",
        "src/fern/types/customer_sort.py",
        "src/fern/types/customer_sort_field.py",
        "src/fern/types/customer_text_filter.py",
        "src/fern/types/date_range.py",
        "src/fern/types/day_of_week.py",
        "src/fern/types/delete_break_type_request.py",
        "src/fern/types/delete_break_type_response.py",
        "src/fern/types/delete_catalog_object_request.py",
        "src/fern/types/delete_catalog_object_response.py",
        "src/fern/types/delete_customer_card_request.py",
        "src/fern/types/delete_customer_card_response.py",
        "src/fern/types/delete_customer_group_request.py",
        "src/fern/types/delete_customer_group_response.py",
        "src/fern/types/delete_customer_request.py",
        "src/fern/types/delete_customer_response.py",
        "src/fern/types/delete_dispute_evidence_request.py",
        "src/fern/types/delete_dispute_evidence_response.py",
        "src/fern/types/delete_invoice_request.py",
        "src/fern/types/delete_invoice_response.py",
        "src/fern/types/delete_loyalty_reward_request.py",
        "src/fern/types/delete_loyalty_reward_response.py",
        "src/fern/types/delete_shift_request.py",
        "src/fern/types/delete_shift_response.py",
        "src/fern/types/delete_snippet_request.py",
        "src/fern/types/delete_snippet_response.py",
        "src/fern/types/deprecated_create_dispute_evidence_file_request.py",
        "src/fern/types/deprecated_create_dispute_evidence_file_response.py",
        "src/fern/types/deprecated_create_dispute_evidence_text_request.py",
        "src/fern/types/deprecated_create_dispute_evidence_text_response.py",
        "src/fern/types/device.py",
        "src/fern/types/device_checkout_options.py",
        "src/fern/types/device_code.py",
        "src/fern/types/device_code_status.py",
        "src/fern/types/device_details.py",
        "src/fern/types/digital_wallet_details.py",
        "src/fern/types/disable_card_request.py",
        "src/fern/types/disable_card_response.py",
        "src/fern/types/dispute.py",
        "src/fern/types/dispute_evidence.py",
        "src/fern/types/dispute_evidence_created_webhook.py",
        "src/fern/types/dispute_evidence_created_webhook_data.py",
        "src/fern/types/dispute_evidence_created_webhook_object.py",
        "src/fern/types/dispute_evidence_file.py",
        "src/fern/types/dispute_evidence_type.py",
        "src/fern/types/dispute_reason.py",
        "src/fern/types/dispute_state.py",
        "src/fern/types/disputed_payment.py",
        "src/fern/types/ecom_visibility.py",
        "src/fern/types/employee.py",
        "src/fern/types/employee_status.py",
        "src/fern/types/employee_wage.py",
        "src/fern/types/error.py",
        "src/fern/types/error_category.py",
        "src/fern/types/error_code.py",
        "src/fern/types/exclude_strategy.py",
        "src/fern/types/external_payment_details.py",
        "src/fern/types/filter_value.py",
        "src/fern/types/gan_source.py",
        "src/fern/types/get_bank_account_by_v1id_request.py",
        "src/fern/types/get_bank_account_by_v1id_response.py",
        "src/fern/types/get_bank_account_request.py",
        "src/fern/types/get_bank_account_response.py",
        "src/fern/types/get_break_type_request.py",
        "src/fern/types/get_break_type_response.py",
        "src/fern/types/get_device_code_request.py",
        "src/fern/types/get_device_code_response.py",
        "src/fern/types/get_employee_wage_request.py",
        "src/fern/types/get_employee_wage_response.py",
        "src/fern/types/get_invoice_request.py",
        "src/fern/types/get_invoice_response.py",
        "src/fern/types/get_payment_refund_request.py",
        "src/fern/types/get_payment_refund_response.py",
        "src/fern/types/get_payment_request.py",
        "src/fern/types/get_payment_response.py",
        "src/fern/types/get_shift_request.py",
        "src/fern/types/get_shift_response.py",
        "src/fern/types/get_team_member_wage_request.py",
        "src/fern/types/get_team_member_wage_response.py",
        "src/fern/types/get_terminal_checkout_request.py",
        "src/fern/types/get_terminal_checkout_response.py",
        "src/fern/types/get_terminal_refund_request.py",
        "src/fern/types/get_terminal_refund_response.py",
        "src/fern/types/gift_card.py",
        "src/fern/types/gift_card_activity.py",
        "src/fern/types/gift_card_activity_activate.py",
        "src/fern/types/gift_card_activity_adjust_decrement.py",
        "src/fern/types/gift_card_activity_adjust_decrement_reason.py",
        "src/fern/types/gift_card_activity_adjust_increment.py",
        "src/fern/types/gift_card_activity_adjust_increment_reason.py",
        "src/fern/types/gift_card_activity_block.py",
        "src/fern/types/gift_card_activity_block_reason.py",
        "src/fern/types/gift_card_activity_clear_balance.py",
        "src/fern/types/gift_card_activity_clear_balance_reason.py",
        "src/fern/types/gift_card_activity_deactivate.py",
        "src/fern/types/gift_card_activity_deactivate_reason.py",
        "src/fern/types/gift_card_activity_import.py",
        "src/fern/types/gift_card_activity_import_reversal.py",
        "src/fern/types/gift_card_activity_load.py",
        "src/fern/types/gift_card_activity_redeem.py",
        "src/fern/types/gift_card_activity_refund.py",
        "src/fern/types/gift_card_activity_type.py",
        "src/fern/types/gift_card_activity_unblock.py",
        "src/fern/types/gift_card_activity_unblock_reason.py",
        "src/fern/types/gift_card_activity_unlinked_activity_refund.py",
        "src/fern/types/gift_card_gan_source.py",
        "src/fern/types/gift_card_status.py",
        "src/fern/types/gift_card_type.py",
        "src/fern/types/info.py",
        "src/fern/types/info_code.py",
        "src/fern/types/inline_types.py",
        "src/fern/types/inventory_adjustment.py",
        "src/fern/types/inventory_adjustment_group.py",
        "src/fern/types/inventory_alert_type.py",
        "src/fern/types/inventory_change.py",
        "src/fern/types/inventory_change_type.py",
        "src/fern/types/inventory_count.py",
        "src/fern/types/inventory_physical_count.py",
        "src/fern/types/inventory_state.py",
        "src/fern/types/inventory_transfer.py",
        "src/fern/types/invoice.py",
        "src/fern/types/invoice_accepted_payment_methods.py",
        "src/fern/types/invoice_automatic_payment_source.py",
        "src/fern/types/invoice_custom_field.py",
        "src/fern/types/invoice_custom_field_placement.py",
        "src/fern/types/invoice_delivery_method.py",
        "src/fern/types/invoice_delivery_method_invoice_delivery_method.py",
        "src/fern/types/invoice_filter.py",
        "src/fern/types/invoice_payment_reminder.py",
        "src/fern/types/invoice_payment_reminder_status.py",
        "src/fern/types/invoice_payment_request.py",
        "src/fern/types/invoice_query.py",
        "src/fern/types/invoice_recipient.py",
        "src/fern/types/invoice_request_method.py",
        "src/fern/types/invoice_request_type.py",
        "src/fern/types/invoice_sort.py",
        "src/fern/types/invoice_sort_field.py",
        "src/fern/types/invoice_status.py",
        "src/fern/types/item_variation_location_overrides.py",
        "src/fern/types/job_assignment.py",
        "src/fern/types/job_assignment_pay_type.py",
        "src/fern/types/link_customer_to_gift_card_response.py",
        "src/fern/types/list_bank_accounts_request.py",
        "src/fern/types/list_bank_accounts_response.py",
        "src/fern/types/list_break_types_request.py",
        "src/fern/types/list_break_types_response.py",
        "src/fern/types/list_cards_request.py",
        "src/fern/types/list_cards_response.py",
        "src/fern/types/list_cash_drawer_shift_events_request.py",
        "src/fern/types/list_cash_drawer_shift_events_response.py",
        "src/fern/types/list_cash_drawer_shifts_request.py",
        "src/fern/types/list_cash_drawer_shifts_response.py",
        "src/fern/types/list_catalog_request.py",
        "src/fern/types/list_catalog_response.py",
        "src/fern/types/list_customer_groups_request.py",
        "src/fern/types/list_customer_groups_response.py",
        "src/fern/types/list_customer_segments_request.py",
        "src/fern/types/list_customer_segments_response.py",
        "src/fern/types/list_customers_request.py",
        "src/fern/types/list_customers_response.py",
        "src/fern/types/list_device_codes_request.py",
        "src/fern/types/list_device_codes_response.py",
        "src/fern/types/list_dispute_evidence_request.py",
        "src/fern/types/list_dispute_evidence_response.py",
        "src/fern/types/list_disputes_request.py",
        "src/fern/types/list_disputes_response.py",
        "src/fern/types/list_employee_wages_request.py",
        "src/fern/types/list_employee_wages_response.py",
        "src/fern/types/list_employees_request.py",
        "src/fern/types/list_employees_response.py",
        "src/fern/types/list_gift_card_activities_request.py",
        "src/fern/types/list_gift_card_activities_response.py",
        "src/fern/types/list_gift_cards_request.py",
        "src/fern/types/list_gift_cards_response.py",
        "src/fern/types/list_invoices_request.py",
        "src/fern/types/list_invoices_response.py",
        "src/fern/types/list_locations_request.py",
        "src/fern/types/list_locations_response.py",
        "src/fern/types/list_loyalty_programs_request.py",
        "src/fern/types/list_loyalty_programs_response.py",
        "src/fern/types/list_merchants_request.py",
        "src/fern/types/list_merchants_response.py",
        "src/fern/types/list_payment_refunds_request.py",
        "src/fern/types/list_payment_refunds_response.py",
        "src/fern/types/list_payments_request.py",
        "src/fern/types/list_payments_response.py",
        "src/fern/types/list_refunds_request.py",
        "src/fern/types/list_refunds_response.py",
        "src/fern/types/list_sites_request.py",
        "src/fern/types/list_sites_response.py",
        "src/fern/types/list_subscription_events_request.py",
        "src/fern/types/list_subscription_events_response.py",
        "src/fern/types/list_team_member_booking_profiles_request.py",
        "src/fern/types/list_team_member_booking_profiles_response.py",
        "src/fern/types/list_team_member_wages_request.py",
        "src/fern/types/list_team_member_wages_response.py",
        "src/fern/types/list_transactions_request.py",
        "src/fern/types/list_transactions_response.py",
        "src/fern/types/list_workweek_configs_request.py",
        "src/fern/types/list_workweek_configs_response.py",
        "src/fern/types/location.py",
        "src/fern/types/location_capability.py",
        "src/fern/types/location_status.py",
        "src/fern/types/location_type.py",
        "src/fern/types/loyalty_account.py",
        "src/fern/types/loyalty_account_expiring_point_deadline.py",
        "src/fern/types/loyalty_account_mapping.py",
        "src/fern/types/loyalty_account_mapping_type.py",
        "src/fern/types/loyalty_event.py",
        "src/fern/types/loyalty_event_accumulate_points.py",
        "src/fern/types/loyalty_event_adjust_points.py",
        "src/fern/types/loyalty_event_create_reward.py",
        "src/fern/types/loyalty_event_date_time_filter.py",
        "src/fern/types/loyalty_event_delete_reward.py",
        "src/fern/types/loyalty_event_expire_points.py",
        "src/fern/types/loyalty_event_filter.py",
        "src/fern/types/loyalty_event_location_filter.py",
        "src/fern/types/loyalty_event_loyalty_account_filter.py",
        "src/fern/types/loyalty_event_order_filter.py",
        "src/fern/types/loyalty_event_other.py",
        "src/fern/types/loyalty_event_query.py",
        "src/fern/types/loyalty_event_redeem_reward.py",
        "src/fern/types/loyalty_event_source.py",
        "src/fern/types/loyalty_event_type.py",
        "src/fern/types/loyalty_event_type_filter.py",
        "src/fern/types/loyalty_program.py",
        "src/fern/types/loyalty_program_accrual_rule.py",
        "src/fern/types/loyalty_program_accrual_rule_type.py",
        "src/fern/types/loyalty_program_expiration_policy.py",
        "src/fern/types/loyalty_program_reward_definition.py",
        "src/fern/types/loyalty_program_reward_definition_scope.py",
        "src/fern/types/loyalty_program_reward_definition_type.py",
        "src/fern/types/loyalty_program_reward_tier.py",
        "src/fern/types/loyalty_program_status.py",
        "src/fern/types/loyalty_program_terminology.py",
        "src/fern/types/loyalty_reward.py",
        "src/fern/types/loyalty_reward_status.py",
        "src/fern/types/measurement_unit.py",
        "src/fern/types/measurement_unit_area.py",
        "src/fern/types/measurement_unit_custom.py",
        "src/fern/types/measurement_unit_generic.py",
        "src/fern/types/measurement_unit_length.py",
        "src/fern/types/measurement_unit_time.py",
        "src/fern/types/measurement_unit_unit_type.py",
        "src/fern/types/measurement_unit_volume.py",
        "src/fern/types/measurement_unit_weight.py",
        "src/fern/types/merchant.py",
        "src/fern/types/merchant_status.py",
        "src/fern/types/money.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/obtain_token_response.py",
        "src/fern/types/onboard_appointments_request.py",
        "src/fern/types/order.py",
        "src/fern/types/order_created.py",
        "src/fern/types/order_created_object.py",
        "src/fern/types/order_entry.py",
        "src/fern/types/order_fulfillment.py",
        "src/fern/types/order_fulfillment_pickup_details.py",
        "src/fern/types/order_fulfillment_pickup_details_curbside_pickup_details.py",
        "src/fern/types/order_fulfillment_pickup_details_schedule_type.py",
        "src/fern/types/order_fulfillment_recipient.py",
        "src/fern/types/order_fulfillment_shipment_details.py",
        "src/fern/types/order_fulfillment_state.py",
        "src/fern/types/order_fulfillment_type.py",
        "src/fern/types/order_fulfillment_updated.py",
        "src/fern/types/order_fulfillment_updated_object.py",
        "src/fern/types/order_fulfillment_updated_update.py",
        "src/fern/types/order_line_item.py",
        "src/fern/types/order_line_item_applied_discount.py",
        "src/fern/types/order_line_item_applied_tax.py",
        "src/fern/types/order_line_item_discount.py",
        "src/fern/types/order_line_item_discount_scope.py",
        "src/fern/types/order_line_item_discount_type.py",
        "src/fern/types/order_line_item_item_type.py",
        "src/fern/types/order_line_item_modifier.py",
        "src/fern/types/order_line_item_pricing_blocklists.py",
        "src/fern/types/order_line_item_pricing_blocklists_blocked_discount.py",
        "src/fern/types/order_line_item_pricing_blocklists_blocked_tax.py",
        "src/fern/types/order_line_item_tax.py",
        "src/fern/types/order_line_item_tax_scope.py",
        "src/fern/types/order_line_item_tax_type.py",
        "src/fern/types/order_money_amounts.py",
        "src/fern/types/order_pricing_options.py",
        "src/fern/types/order_quantity_unit.py",
        "src/fern/types/order_return.py",
        "src/fern/types/order_return_discount.py",
        "src/fern/types/order_return_line_item.py",
        "src/fern/types/order_return_line_item_modifier.py",
        "src/fern/types/order_return_service_charge.py",
        "src/fern/types/order_return_tax.py",
        "src/fern/types/order_reward.py",
        "src/fern/types/order_rounding_adjustment.py",
        "src/fern/types/order_service_charge.py",
        "src/fern/types/order_service_charge_calculation_phase.py",
        "src/fern/types/order_service_charge_type.py",
        "src/fern/types/order_source.py",
        "src/fern/types/order_state.py",
        "src/fern/types/order_updated.py",
        "src/fern/types/order_updated_object.py",
        "src/fern/types/pay_order_response.py",
        "src/fern/types/payment.py",
        "src/fern/types/payment_options.py",
        "src/fern/types/payment_refund.py",
        "src/fern/types/processing_fee.py",
        "src/fern/types/product.py",
        "src/fern/types/product_type.py",
        "src/fern/types/publish_invoice_response.py",
        "src/fern/types/quantity_ratio.py",
        "src/fern/types/range.py",
        "src/fern/types/reason.py",
        "src/fern/types/redeem_loyalty_reward_response.py",
        "src/fern/types/refund.py",
        "src/fern/types/refund_payment_response.py",
        "src/fern/types/refund_status.py",
        "src/fern/types/register_domain_response.py",
        "src/fern/types/register_domain_response_status.py",
        "src/fern/types/remove_group_from_customer_request.py",
        "src/fern/types/remove_group_from_customer_response.py",
        "src/fern/types/renew_token_response.py",
        "src/fern/types/resume_subscription_request.py",
        "src/fern/types/resume_subscription_response.py",
        "src/fern/types/retrieve_booking_request.py",
        "src/fern/types/retrieve_booking_response.py",
        "src/fern/types/retrieve_business_booking_profile_request.py",
        "src/fern/types/retrieve_business_booking_profile_response.py",
        "src/fern/types/retrieve_card_request.py",
        "src/fern/types/retrieve_card_response.py",
        "src/fern/types/retrieve_cash_drawer_shift_request.py",
        "src/fern/types/retrieve_cash_drawer_shift_response.py",
        "src/fern/types/retrieve_catalog_object_request.py",
        "src/fern/types/retrieve_catalog_object_response.py",
        "src/fern/types/retrieve_customer_group_request.py",
        "src/fern/types/retrieve_customer_group_response.py",
        "src/fern/types/retrieve_customer_request.py",
        "src/fern/types/retrieve_customer_response.py",
        "src/fern/types/retrieve_customer_segment_request.py",
        "src/fern/types/retrieve_customer_segment_response.py",
        "src/fern/types/retrieve_dispute_evidence_request.py",
        "src/fern/types/retrieve_dispute_evidence_response.py",
        "src/fern/types/retrieve_dispute_request.py",
        "src/fern/types/retrieve_dispute_response.py",
        "src/fern/types/retrieve_employee_request.py",
        "src/fern/types/retrieve_employee_response.py",
        "src/fern/types/retrieve_gift_card_from_gan_response.py",
        "src/fern/types/retrieve_gift_card_from_nonce_response.py",
        "src/fern/types/retrieve_gift_card_request.py",
        "src/fern/types/retrieve_gift_card_response.py",
        "src/fern/types/retrieve_inventory_adjustment_request.py",
        "src/fern/types/retrieve_inventory_adjustment_response.py",
        "src/fern/types/retrieve_inventory_changes_request.py",
        "src/fern/types/retrieve_inventory_changes_response.py",
        "src/fern/types/retrieve_inventory_count_request.py",
        "src/fern/types/retrieve_inventory_count_response.py",
        "src/fern/types/retrieve_inventory_physical_count_request.py",
        "src/fern/types/retrieve_inventory_physical_count_response.py",
        "src/fern/types/retrieve_inventory_transfer_request.py",
        "src/fern/types/retrieve_inventory_transfer_response.py",
        "src/fern/types/retrieve_location_request.py",
        "src/fern/types/retrieve_location_response.py",
        "src/fern/types/retrieve_loyalty_account_request.py",
        "src/fern/types/retrieve_loyalty_account_response.py",
        "src/fern/types/retrieve_loyalty_program_request.py",
        "src/fern/types/retrieve_loyalty_program_response.py",
        "src/fern/types/retrieve_loyalty_reward_request.py",
        "src/fern/types/retrieve_loyalty_reward_response.py",
        "src/fern/types/retrieve_merchant_request.py",
        "src/fern/types/retrieve_merchant_response.py",
        "src/fern/types/retrieve_obs_migration_profile_request.py",
        "src/fern/types/retrieve_order_request.py",
        "src/fern/types/retrieve_order_response.py",
        "src/fern/types/retrieve_snippet_request.py",
        "src/fern/types/retrieve_snippet_response.py",
        "src/fern/types/retrieve_subscription_request.py",
        "src/fern/types/retrieve_subscription_response.py",
        "src/fern/types/retrieve_team_member_booking_profile_request.py",
        "src/fern/types/retrieve_team_member_booking_profile_response.py",
        "src/fern/types/retrieve_team_member_request.py",
        "src/fern/types/retrieve_team_member_response.py",
        "src/fern/types/retrieve_transaction_request.py",
        "src/fern/types/retrieve_transaction_response.py",
        "src/fern/types/retrieve_wage_setting_request.py",
        "src/fern/types/retrieve_wage_setting_response.py",
        "src/fern/types/revoke_token_response.py",
        "src/fern/types/risk_evaluation.py",
        "src/fern/types/risk_evaluation_risk_level.py",
        "src/fern/types/search_availability_filter.py",
        "src/fern/types/search_availability_query.py",
        "src/fern/types/search_availability_response.py",
        "src/fern/types/search_catalog_items_request_stock_level.py",
        "src/fern/types/search_catalog_items_response.py",
        "src/fern/types/search_catalog_objects_response.py",
        "src/fern/types/search_customers_response.py",
        "src/fern/types/search_invoices_response.py",
        "src/fern/types/search_loyalty_accounts_request_loyalty_account_query.py",
        "src/fern/types/search_loyalty_accounts_response.py",
        "src/fern/types/search_loyalty_events_response.py",
        "src/fern/types/search_loyalty_rewards_request_loyalty_reward_query.py",
        "src/fern/types/search_loyalty_rewards_response.py",
        "src/fern/types/search_orders_customer_filter.py",
        "src/fern/types/search_orders_date_time_filter.py",
        "src/fern/types/search_orders_filter.py",
        "src/fern/types/search_orders_fulfillment_filter.py",
        "src/fern/types/search_orders_query.py",
        "src/fern/types/search_orders_response.py",
        "src/fern/types/search_orders_sort.py",
        "src/fern/types/search_orders_sort_field.py",
        "src/fern/types/search_orders_source_filter.py",
        "src/fern/types/search_orders_state_filter.py",
        "src/fern/types/search_shifts_response.py",
        "src/fern/types/search_subscriptions_filter.py",
        "src/fern/types/search_subscriptions_query.py",
        "src/fern/types/search_subscriptions_response.py",
        "src/fern/types/search_team_members_filter.py",
        "src/fern/types/search_team_members_query.py",
        "src/fern/types/search_team_members_response.py",
        "src/fern/types/search_terminal_checkouts_response.py",
        "src/fern/types/search_terminal_refunds_response.py",
        "src/fern/types/segment_filter.py",
        "src/fern/types/shift.py",
        "src/fern/types/shift_filter.py",
        "src/fern/types/shift_filter_status.py",
        "src/fern/types/shift_query.py",
        "src/fern/types/shift_sort.py",
        "src/fern/types/shift_sort_field.py",
        "src/fern/types/shift_status.py",
        "src/fern/types/shift_wage.py",
        "src/fern/types/shift_workday.py",
        "src/fern/types/shift_workday_matcher.py",
        "src/fern/types/site.py",
        "src/fern/types/snippet.py",
        "src/fern/types/snippet_response.py",
        "src/fern/types/sort_order.py",
        "src/fern/types/source_application.py",
        "src/fern/types/standard_unit_description.py",
        "src/fern/types/standard_unit_description_group.py",
        "src/fern/types/status.py",
        "src/fern/types/submit_evidence_request.py",
        "src/fern/types/submit_evidence_response.py",
        "src/fern/types/subscription.py",
        "src/fern/types/subscription_cadence.py",
        "src/fern/types/subscription_event.py",
        "src/fern/types/subscription_event_info.py",
        "src/fern/types/subscription_event_info_code.py",
        "src/fern/types/subscription_event_subscription_event_type.py",
        "src/fern/types/subscription_phase.py",
        "src/fern/types/subscription_status.py",
        "src/fern/types/tax_calculation_phase.py",
        "src/fern/types/tax_ids.py",
        "src/fern/types/tax_inclusion_type.py",
        "src/fern/types/team_member.py",
        "src/fern/types/team_member_assigned_locations.py",
        "src/fern/types/team_member_assigned_locations_assignment_type.py",
        "src/fern/types/team_member_booking_profile.py",
        "src/fern/types/team_member_invitation_status.py",
        "src/fern/types/team_member_status.py",
        "src/fern/types/team_member_wage.py",
        "src/fern/types/tender.py",
        "src/fern/types/tender_card_details.py",
        "src/fern/types/tender_card_details_entry_method.py",
        "src/fern/types/tender_card_details_status.py",
        "src/fern/types/tender_cash_details.py",
        "src/fern/types/tender_type.py",
        "src/fern/types/terminal_checkout.py",
        "src/fern/types/terminal_checkout_query.py",
        "src/fern/types/terminal_checkout_query_filter.py",
        "src/fern/types/terminal_checkout_query_sort.py",
        "src/fern/types/terminal_refund.py",
        "src/fern/types/terminal_refund_query.py",
        "src/fern/types/terminal_refund_query_filter.py",
        "src/fern/types/terminal_refund_query_sort.py",
        "src/fern/types/time_range.py",
        "src/fern/types/tip_settings.py",
        "src/fern/types/transaction.py",
        "src/fern/types/transaction_product.py",
        "src/fern/types/transaction_type.py",
        "src/fern/types/type.py",
        "src/fern/types/unlink_customer_from_gift_card_response.py",
        "src/fern/types/update_booking_response.py",
        "src/fern/types/update_break_type_response.py",
        "src/fern/types/update_customer_group_response.py",
        "src/fern/types/update_customer_response.py",
        "src/fern/types/update_invoice_response.py",
        "src/fern/types/update_item_modifier_lists_response.py",
        "src/fern/types/update_item_taxes_response.py",
        "src/fern/types/update_location_response.py",
        "src/fern/types/update_order_response.py",
        "src/fern/types/update_payment_response.py",
        "src/fern/types/update_shift_response.py",
        "src/fern/types/update_subscription_response.py",
        "src/fern/types/update_team_member_request.py",
        "src/fern/types/update_team_member_response.py",
        "src/fern/types/update_wage_setting_response.py",
        "src/fern/types/update_workweek_config_response.py",
        "src/fern/types/upsert_catalog_object_response.py",
        "src/fern/types/upsert_snippet_response.py",
        "src/fern/types/v1create_employee_role_request.py",
        "src/fern/types/v1create_refund_request_type.py",
        "src/fern/types/v1employee.py",
        "src/fern/types/v1employee_role.py",
        "src/fern/types/v1employee_role_permissions.py",
        "src/fern/types/v1employee_status.py",
        "src/fern/types/v1list_employee_roles_request.py",
        "src/fern/types/v1list_employee_roles_response.py",
        "src/fern/types/v1list_employees_request.py",
        "src/fern/types/v1list_employees_request_status.py",
        "src/fern/types/v1list_employees_response.py",
        "src/fern/types/v1list_orders_request.py",
        "src/fern/types/v1list_orders_response.py",
        "src/fern/types/v1list_payments_request.py",
        "src/fern/types/v1list_payments_response.py",
        "src/fern/types/v1list_refunds_request.py",
        "src/fern/types/v1list_refunds_response.py",
        "src/fern/types/v1list_settlements_request.py",
        "src/fern/types/v1list_settlements_request_status.py",
        "src/fern/types/v1list_settlements_response.py",
        "src/fern/types/v1money.py",
        "src/fern/types/v1order.py",
        "src/fern/types/v1order_history_entry.py",
        "src/fern/types/v1order_history_entry_action.py",
        "src/fern/types/v1order_state.py",
        "src/fern/types/v1payment.py",
        "src/fern/types/v1payment_discount.py",
        "src/fern/types/v1payment_item_detail.py",
        "src/fern/types/v1payment_itemization.py",
        "src/fern/types/v1payment_itemization_itemization_type.py",
        "src/fern/types/v1payment_modifier.py",
        "src/fern/types/v1payment_surcharge.py",
        "src/fern/types/v1payment_surcharge_type.py",
        "src/fern/types/v1payment_tax.py",
        "src/fern/types/v1payment_tax_inclusion_type.py",
        "src/fern/types/v1phone_number.py",
        "src/fern/types/v1refund.py",
        "src/fern/types/v1refund_type.py",
        "src/fern/types/v1retrieve_employee_request.py",
        "src/fern/types/v1retrieve_employee_role_request.py",
        "src/fern/types/v1retrieve_order_request.py",
        "src/fern/types/v1retrieve_payment_request.py",
        "src/fern/types/v1retrieve_settlement_request.py",
        "src/fern/types/v1settlement.py",
        "src/fern/types/v1settlement_entry.py",
        "src/fern/types/v1settlement_entry_type.py",
        "src/fern/types/v1settlement_status.py",
        "src/fern/types/v1tender.py",
        "src/fern/types/v1tender_card_brand.py",
        "src/fern/types/v1tender_entry_method.py",
        "src/fern/types/v1tender_type.py",
        "src/fern/types/v1update_employee_request.py",
        "src/fern/types/v1update_employee_role_request.py",
        "src/fern/types/v1update_order_request_action.py",
        "src/fern/types/void_transaction_request.py",
        "src/fern/types/void_transaction_response.py",
        "src/fern/types/wage_setting.py",
        "src/fern/types/weekday.py",
        "src/fern/types/workweek_config.py",
        "src/fern/v1employees/__init__.py",
        "src/fern/v1transactions/__init__.py",
        "src/fern/v1transactions/raw_client.py",
        "src/fern/version.py",
        "README.md",
        "src/fern/apple_pay/client.py",
        "src/fern/bank_accounts/client.py",
        "src/fern/cards/client.py",
        "src/fern/cash_drawers/client.py",
        "src/fern/checkout/client.py",
        "src/fern/client.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/customer_groups/client.py",
        "src/fern/customer_segments/client.py",
        "src/fern/devices/client.py",
        "src/fern/disputes/client.py",
        "src/fern/employees/client.py",
        "src/fern/inventory/client.py",
        "src/fern/invoices/client.py",
        "src/fern/labor/client.py",
        "src/fern/locations/client.py",
        "src/fern/loyalty/client.py",
        "src/fern/merchants/client.py",
        "src/fern/mobile_authorization/client.py",
        "src/fern/o_auth/client.py",
        "src/fern/orders/client.py",
        "src/fern/payments/client.py",
        "src/fern/refunds/client.py",
        "src/fern/sites/client.py",
        "src/fern/snippets/client.py",
        "src/fern/subscriptions/client.py",
        "src/fern/team/client.py",
        "src/fern/terminal/client.py",
        "src/fern/transactions/client.py",
        "src/fern/v1transactions/client.py",
        "src/fern/cards/raw_client.py",
        "src/fern/customer_groups/raw_client.py",
        "src/fern/invoices/raw_client.py",
        "src/fern/labor/raw_client.py",
        "src/fern/locations/raw_client.py",
        "src/fern/loyalty/raw_client.py",
        "src/fern/mobile_authorization/raw_client.py",
        "src/fern/payments/raw_client.py",
        "src/fern/refunds/raw_client.py",
        "src/fern/subscriptions/raw_client.py",
        "src/fern/bookings/client.py",
        "src/fern/catalog/client.py",
        "src/fern/catalog/raw_client.py",
        "src/fern/customers/client.py",
        "src/fern/customers/raw_client.py",
        "src/fern/orders/raw_client.py",
        "src/fern/team/raw_client.py",
        "src/fern/types/catalog_item_option_for_item.py",
        "src/fern/v1employees/client.py",
        "src/fern/v1employees/raw_client.py",
        "reference.md",
        "src/fern/gift_card_activities/client.py",
        "src/fern/gift_cards/client.py",
    ],
};

const AMAZONAWS_COM_CLOUDFORMATION: Corpus = Corpus {
    api: "amazonaws.com-cloudformation",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/py.typed",
        "src/fern/types/accept_terms_and_conditions.py",
        "src/fern/types/account.py",
        "src/fern/types/account_filter_type.py",
        "src/fern/types/account_gate_status.py",
        "src/fern/types/account_gate_status_reason.py",
        "src/fern/types/account_limit_list.py",
        "src/fern/types/account_list.py",
        "src/fern/types/accounts_url.py",
        "src/fern/types/allowed_value.py",
        "src/fern/types/allowed_values.py",
        "src/fern/types/already_exists_exception.py",
        "src/fern/types/arn.py",
        "src/fern/types/auto_deployment_nullable.py",
        "src/fern/types/auto_update.py",
        "src/fern/types/batch_describe_type_configurations_errors.py",
        "src/fern/types/boxed_integer.py",
        "src/fern/types/boxed_max_results.py",
        "src/fern/types/call_as.py",
        "src/fern/types/capabilities.py",
        "src/fern/types/capabilities_reason.py",
        "src/fern/types/capability.py",
        "src/fern/types/category.py",
        "src/fern/types/causing_entity.py",
        "src/fern/types/cfn_registry_exception.py",
        "src/fern/types/change_action.py",
        "src/fern/types/change_set_hooks.py",
        "src/fern/types/change_set_hooks_status.py",
        "src/fern/types/change_set_id.py",
        "src/fern/types/change_set_name.py",
        "src/fern/types/change_set_name_or_id.py",
        "src/fern/types/change_set_not_found_exception.py",
        "src/fern/types/change_set_status.py",
        "src/fern/types/change_set_status_reason.py",
        "src/fern/types/change_set_summaries.py",
        "src/fern/types/change_set_type.py",
        "src/fern/types/change_source.py",
        "src/fern/types/changes.py",
        "src/fern/types/client_request_token.py",
        "src/fern/types/client_token.py",
        "src/fern/types/configuration_schema.py",
        "src/fern/types/connection_arn.py",
        "src/fern/types/continue_update_rollback_output.py",
        "src/fern/types/created_but_modified_exception.py",
        "src/fern/types/creation_time.py",
        "src/fern/types/deactivate_type_output.py",
        "src/fern/types/delete_change_set_output.py",
        "src/fern/types/delete_stack_set_output.py",
        "src/fern/types/deletion_time.py",
        "src/fern/types/deprecated_status.py",
        "src/fern/types/deregister_type_output.py",
        "src/fern/types/description.py",
        "src/fern/types/difference_type.py",
        "src/fern/types/disable_rollback.py",
        "src/fern/types/drifted_stack_instances_count.py",
        "src/fern/types/enable_termination_protection.py",
        "src/fern/types/error_code.py",
        "src/fern/types/error_message.py",
        "src/fern/types/evaluation_type.py",
        "src/fern/types/event_id.py",
        "src/fern/types/execute_change_set_output.py",
        "src/fern/types/execution_role_name.py",
        "src/fern/types/execution_status.py",
        "src/fern/types/exports.py",
        "src/fern/types/failed_stack_instances_count.py",
        "src/fern/types/failure_tolerance_count.py",
        "src/fern/types/failure_tolerance_percentage.py",
        "src/fern/types/get_activate_type_request_action.py",
        "src/fern/types/get_activate_type_request_type.py",
        "src/fern/types/get_activate_type_request_version.py",
        "src/fern/types/get_activate_type_request_version_bump.py",
        "src/fern/types/get_batch_describe_type_configurations_request_action.py",
        "src/fern/types/get_batch_describe_type_configurations_request_version.py",
        "src/fern/types/get_cancel_update_stack_request_action.py",
        "src/fern/types/get_cancel_update_stack_request_version.py",
        "src/fern/types/get_continue_update_rollback_request_action.py",
        "src/fern/types/get_continue_update_rollback_request_version.py",
        "src/fern/types/get_create_change_set_request_action.py",
        "src/fern/types/get_create_change_set_request_change_set_type.py",
        "src/fern/types/get_create_change_set_request_version.py",
        "src/fern/types/get_create_stack_instances_request_action.py",
        "src/fern/types/get_create_stack_instances_request_call_as.py",
        "src/fern/types/get_create_stack_instances_request_version.py",
        "src/fern/types/get_create_stack_request_action.py",
        "src/fern/types/get_create_stack_request_on_failure.py",
        "src/fern/types/get_create_stack_request_version.py",
        "src/fern/types/get_create_stack_set_request_action.py",
        "src/fern/types/get_create_stack_set_request_call_as.py",
        "src/fern/types/get_create_stack_set_request_permission_model.py",
        "src/fern/types/get_create_stack_set_request_version.py",
        "src/fern/types/get_deactivate_type_request_action.py",
        "src/fern/types/get_deactivate_type_request_type.py",
        "src/fern/types/get_deactivate_type_request_version.py",
        "src/fern/types/get_delete_change_set_request_action.py",
        "src/fern/types/get_delete_change_set_request_version.py",
        "src/fern/types/get_delete_stack_instances_request_action.py",
        "src/fern/types/get_delete_stack_instances_request_call_as.py",
        "src/fern/types/get_delete_stack_instances_request_version.py",
        "src/fern/types/get_delete_stack_request_action.py",
        "src/fern/types/get_delete_stack_request_version.py",
        "src/fern/types/get_delete_stack_set_request_action.py",
        "src/fern/types/get_delete_stack_set_request_call_as.py",
        "src/fern/types/get_delete_stack_set_request_version.py",
        "src/fern/types/get_deregister_type_request_action.py",
        "src/fern/types/get_deregister_type_request_type.py",
        "src/fern/types/get_deregister_type_request_version.py",
        "src/fern/types/get_describe_account_limits_request_action.py",
        "src/fern/types/get_describe_account_limits_request_version.py",
        "src/fern/types/get_describe_change_set_hooks_request_action.py",
        "src/fern/types/get_describe_change_set_hooks_request_version.py",
        "src/fern/types/get_describe_change_set_request_action.py",
        "src/fern/types/get_describe_change_set_request_version.py",
        "src/fern/types/get_describe_publisher_request_action.py",
        "src/fern/types/get_describe_publisher_request_version.py",
        "src/fern/types/get_describe_stack_drift_detection_status_request_action.py",
        "src/fern/types/get_describe_stack_drift_detection_status_request_version.py",
        "src/fern/types/get_describe_stack_events_request_action.py",
        "src/fern/types/get_describe_stack_events_request_version.py",
        "src/fern/types/get_describe_stack_instance_request_action.py",
        "src/fern/types/get_describe_stack_instance_request_call_as.py",
        "src/fern/types/get_describe_stack_instance_request_version.py",
        "src/fern/types/get_describe_stack_resource_drifts_request_action.py",
        "src/fern/types/get_describe_stack_resource_drifts_request_version.py",
        "src/fern/types/get_describe_stack_resource_request_action.py",
        "src/fern/types/get_describe_stack_resource_request_version.py",
        "src/fern/types/get_describe_stack_resources_request_action.py",
        "src/fern/types/get_describe_stack_resources_request_version.py",
        "src/fern/types/get_describe_stack_set_operation_request_action.py",
        "src/fern/types/get_describe_stack_set_operation_request_call_as.py",
        "src/fern/types/get_describe_stack_set_operation_request_version.py",
        "src/fern/types/get_describe_stack_set_request_action.py",
        "src/fern/types/get_describe_stack_set_request_call_as.py",
        "src/fern/types/get_describe_stack_set_request_version.py",
        "src/fern/types/get_describe_stacks_request_action.py",
        "src/fern/types/get_describe_stacks_request_version.py",
        "src/fern/types/get_describe_type_registration_request_action.py",
        "src/fern/types/get_describe_type_registration_request_version.py",
        "src/fern/types/get_describe_type_request_action.py",
        "src/fern/types/get_describe_type_request_type.py",
        "src/fern/types/get_describe_type_request_version.py",
        "src/fern/types/get_detect_stack_drift_request_action.py",
        "src/fern/types/get_detect_stack_drift_request_version.py",
        "src/fern/types/get_detect_stack_resource_drift_request_action.py",
        "src/fern/types/get_detect_stack_resource_drift_request_version.py",
        "src/fern/types/get_detect_stack_set_drift_request_action.py",
        "src/fern/types/get_detect_stack_set_drift_request_call_as.py",
        "src/fern/types/get_detect_stack_set_drift_request_version.py",
        "src/fern/types/get_estimate_template_cost_request_action.py",
        "src/fern/types/get_estimate_template_cost_request_version.py",
        "src/fern/types/get_execute_change_set_request_action.py",
        "src/fern/types/get_execute_change_set_request_version.py",
        "src/fern/types/get_get_stack_policy_request_action.py",
        "src/fern/types/get_get_stack_policy_request_version.py",
        "src/fern/types/get_get_template_request_action.py",
        "src/fern/types/get_get_template_request_template_stage.py",
        "src/fern/types/get_get_template_request_version.py",
        "src/fern/types/get_get_template_summary_request_action.py",
        "src/fern/types/get_get_template_summary_request_call_as.py",
        "src/fern/types/get_get_template_summary_request_version.py",
        "src/fern/types/get_import_stacks_to_stack_set_request_action.py",
        "src/fern/types/get_import_stacks_to_stack_set_request_call_as.py",
        "src/fern/types/get_import_stacks_to_stack_set_request_version.py",
        "src/fern/types/get_list_change_sets_request_action.py",
        "src/fern/types/get_list_change_sets_request_version.py",
        "src/fern/types/get_list_exports_request_action.py",
        "src/fern/types/get_list_exports_request_version.py",
        "src/fern/types/get_list_imports_request_action.py",
        "src/fern/types/get_list_imports_request_version.py",
        "src/fern/types/get_list_stack_instances_request_action.py",
        "src/fern/types/get_list_stack_instances_request_call_as.py",
        "src/fern/types/get_list_stack_instances_request_version.py",
        "src/fern/types/get_list_stack_resources_request_action.py",
        "src/fern/types/get_list_stack_resources_request_version.py",
        "src/fern/types/get_list_stack_set_operation_results_request_action.py",
        "src/fern/types/get_list_stack_set_operation_results_request_call_as.py",
        "src/fern/types/get_list_stack_set_operation_results_request_version.py",
        "src/fern/types/get_list_stack_set_operations_request_action.py",
        "src/fern/types/get_list_stack_set_operations_request_call_as.py",
        "src/fern/types/get_list_stack_set_operations_request_version.py",
        "src/fern/types/get_list_stack_sets_request_action.py",
        "src/fern/types/get_list_stack_sets_request_call_as.py",
        "src/fern/types/get_list_stack_sets_request_status.py",
        "src/fern/types/get_list_stack_sets_request_version.py",
        "src/fern/types/get_list_stacks_request_action.py",
        "src/fern/types/get_list_stacks_request_version.py",
        "src/fern/types/get_list_type_registrations_request_action.py",
        "src/fern/types/get_list_type_registrations_request_registration_status_filter.py",
        "src/fern/types/get_list_type_registrations_request_type.py",
        "src/fern/types/get_list_type_registrations_request_version.py",
        "src/fern/types/get_list_type_versions_request_action.py",
        "src/fern/types/get_list_type_versions_request_deprecated_status.py",
        "src/fern/types/get_list_type_versions_request_type.py",
        "src/fern/types/get_list_type_versions_request_version.py",
        "src/fern/types/get_list_types_request_action.py",
        "src/fern/types/get_list_types_request_deprecated_status.py",
        "src/fern/types/get_list_types_request_provisioning_type.py",
        "src/fern/types/get_list_types_request_type.py",
        "src/fern/types/get_list_types_request_version.py",
        "src/fern/types/get_list_types_request_visibility.py",
        "src/fern/types/get_publish_type_request_action.py",
        "src/fern/types/get_publish_type_request_type.py",
        "src/fern/types/get_publish_type_request_version.py",
        "src/fern/types/get_record_handler_progress_request_action.py",
        "src/fern/types/get_record_handler_progress_request_current_operation_status.py",
        "src/fern/types/get_record_handler_progress_request_error_code.py",
        "src/fern/types/get_record_handler_progress_request_operation_status.py",
        "src/fern/types/get_record_handler_progress_request_version.py",
        "src/fern/types/get_register_publisher_request_action.py",
        "src/fern/types/get_register_publisher_request_version.py",
        "src/fern/types/get_register_type_request_action.py",
        "src/fern/types/get_register_type_request_type.py",
        "src/fern/types/get_register_type_request_version.py",
        "src/fern/types/get_rollback_stack_request_action.py",
        "src/fern/types/get_rollback_stack_request_version.py",
        "src/fern/types/get_set_stack_policy_request_action.py",
        "src/fern/types/get_set_stack_policy_request_version.py",
        "src/fern/types/get_set_type_configuration_request_action.py",
        "src/fern/types/get_set_type_configuration_request_type.py",
        "src/fern/types/get_set_type_configuration_request_version.py",
        "src/fern/types/get_set_type_default_version_request_action.py",
        "src/fern/types/get_set_type_default_version_request_type.py",
        "src/fern/types/get_set_type_default_version_request_version.py",
        "src/fern/types/get_signal_resource_request_action.py",
        "src/fern/types/get_signal_resource_request_status.py",
        "src/fern/types/get_signal_resource_request_version.py",
        "src/fern/types/get_stop_stack_set_operation_request_action.py",
        "src/fern/types/get_stop_stack_set_operation_request_call_as.py",
        "src/fern/types/get_stop_stack_set_operation_request_version.py",
        "src/fern/types/get_test_type_request_action.py",
        "src/fern/types/get_test_type_request_type.py",
        "src/fern/types/get_test_type_request_version.py",
        "src/fern/types/get_update_stack_instances_request_action.py",
        "src/fern/types/get_update_stack_instances_request_call_as.py",
        "src/fern/types/get_update_stack_instances_request_version.py",
        "src/fern/types/get_update_stack_request_action.py",
        "src/fern/types/get_update_stack_request_version.py",
        "src/fern/types/get_update_stack_set_request_action.py",
        "src/fern/types/get_update_stack_set_request_call_as.py",
        "src/fern/types/get_update_stack_set_request_permission_model.py",
        "src/fern/types/get_update_stack_set_request_version.py",
        "src/fern/types/get_update_termination_protection_request_action.py",
        "src/fern/types/get_update_termination_protection_request_version.py",
        "src/fern/types/get_validate_template_request_action.py",
        "src/fern/types/get_validate_template_request_version.py",
        "src/fern/types/handler_error_code.py",
        "src/fern/types/hook_failure_mode.py",
        "src/fern/types/hook_invocation_count.py",
        "src/fern/types/hook_invocation_point.py",
        "src/fern/types/hook_status.py",
        "src/fern/types/hook_status_reason.py",
        "src/fern/types/hook_target_type.py",
        "src/fern/types/hook_target_type_name.py",
        "src/fern/types/hook_type.py",
        "src/fern/types/hook_type_configuration_version_id.py",
        "src/fern/types/hook_type_name.py",
        "src/fern/types/hook_type_version_id.py",
        "src/fern/types/identity_provider.py",
        "src/fern/types/imports.py",
        "src/fern/types/in_progress_stack_instances_count.py",
        "src/fern/types/in_sync_stack_instances_count.py",
        "src/fern/types/include_nested_stacks.py",
        "src/fern/types/insufficient_capabilities_exception.py",
        "src/fern/types/invalid_change_set_status_exception.py",
        "src/fern/types/invalid_operation_exception.py",
        "src/fern/types/invalid_state_transition_exception.py",
        "src/fern/types/is_activated.py",
        "src/fern/types/is_default_configuration.py",
        "src/fern/types/is_default_version.py",
        "src/fern/types/key.py",
        "src/fern/types/last_updated_time.py",
        "src/fern/types/limit_exceeded_exception.py",
        "src/fern/types/limit_name.py",
        "src/fern/types/limit_value.py",
        "src/fern/types/log_group_name.py",
        "src/fern/types/logical_id_hierarchy.py",
        "src/fern/types/logical_resource_id.py",
        "src/fern/types/logical_resource_ids.py",
        "src/fern/types/major_version.py",
        "src/fern/types/managed_execution_nullable.py",
        "src/fern/types/max_concurrent_count.py",
        "src/fern/types/max_concurrent_percentage.py",
        "src/fern/types/max_results.py",
        "src/fern/types/metadata.py",
        "src/fern/types/monitoring_time_in_minutes.py",
        "src/fern/types/name_already_exists_exception.py",
        "src/fern/types/next_token.py",
        "src/fern/types/no_echo.py",
        "src/fern/types/notification_ar_ns.py",
        "src/fern/types/notification_arn.py",
        "src/fern/types/on_failure.py",
        "src/fern/types/operation_id_already_exists_exception.py",
        "src/fern/types/operation_in_progress_exception.py",
        "src/fern/types/operation_not_found_exception.py",
        "src/fern/types/operation_result_filter_name.py",
        "src/fern/types/operation_result_filter_values.py",
        "src/fern/types/operation_result_filters.py",
        "src/fern/types/operation_status.py",
        "src/fern/types/operation_status_check_failed_exception.py",
        "src/fern/types/optional_secure_url.py",
        "src/fern/types/organizational_unit_id.py",
        "src/fern/types/organizational_unit_id_list.py",
        "src/fern/types/output_key.py",
        "src/fern/types/output_value.py",
        "src/fern/types/outputs.py",
        "src/fern/types/parameter_declarations.py",
        "src/fern/types/parameter_key.py",
        "src/fern/types/parameter_type.py",
        "src/fern/types/parameter_value.py",
        "src/fern/types/parameters.py",
        "src/fern/types/permission_models.py",
        "src/fern/types/physical_resource_id.py",
        "src/fern/types/physical_resource_id_context.py",
        "src/fern/types/post_activate_type_request_action.py",
        "src/fern/types/post_activate_type_request_version.py",
        "src/fern/types/post_batch_describe_type_configurations_request_action.py",
        "src/fern/types/post_batch_describe_type_configurations_request_version.py",
        "src/fern/types/post_cancel_update_stack_request_action.py",
        "src/fern/types/post_cancel_update_stack_request_version.py",
        "src/fern/types/post_continue_update_rollback_request_action.py",
        "src/fern/types/post_continue_update_rollback_request_version.py",
        "src/fern/types/post_create_change_set_request_action.py",
        "src/fern/types/post_create_change_set_request_version.py",
        "src/fern/types/post_create_stack_instances_request_action.py",
        "src/fern/types/post_create_stack_instances_request_version.py",
        "src/fern/types/post_create_stack_request_action.py",
        "src/fern/types/post_create_stack_request_version.py",
        "src/fern/types/post_create_stack_set_request_action.py",
        "src/fern/types/post_create_stack_set_request_version.py",
        "src/fern/types/post_deactivate_type_request_action.py",
        "src/fern/types/post_deactivate_type_request_version.py",
        "src/fern/types/post_delete_change_set_request_action.py",
        "src/fern/types/post_delete_change_set_request_version.py",
        "src/fern/types/post_delete_stack_instances_request_action.py",
        "src/fern/types/post_delete_stack_instances_request_version.py",
        "src/fern/types/post_delete_stack_request_action.py",
        "src/fern/types/post_delete_stack_request_version.py",
        "src/fern/types/post_delete_stack_set_request_action.py",
        "src/fern/types/post_delete_stack_set_request_version.py",
        "src/fern/types/post_deregister_type_request_action.py",
        "src/fern/types/post_deregister_type_request_version.py",
        "src/fern/types/post_describe_account_limits_request_action.py",
        "src/fern/types/post_describe_account_limits_request_version.py",
        "src/fern/types/post_describe_change_set_hooks_request_action.py",
        "src/fern/types/post_describe_change_set_hooks_request_version.py",
        "src/fern/types/post_describe_change_set_request_action.py",
        "src/fern/types/post_describe_change_set_request_version.py",
        "src/fern/types/post_describe_publisher_request_action.py",
        "src/fern/types/post_describe_publisher_request_version.py",
        "src/fern/types/post_describe_stack_drift_detection_status_request_action.py",
        "src/fern/types/post_describe_stack_drift_detection_status_request_version.py",
        "src/fern/types/post_describe_stack_events_request_action.py",
        "src/fern/types/post_describe_stack_events_request_version.py",
        "src/fern/types/post_describe_stack_instance_request_action.py",
        "src/fern/types/post_describe_stack_instance_request_version.py",
        "src/fern/types/post_describe_stack_resource_drifts_request_action.py",
        "src/fern/types/post_describe_stack_resource_drifts_request_version.py",
        "src/fern/types/post_describe_stack_resource_request_action.py",
        "src/fern/types/post_describe_stack_resource_request_version.py",
        "src/fern/types/post_describe_stack_resources_request_action.py",
        "src/fern/types/post_describe_stack_resources_request_version.py",
        "src/fern/types/post_describe_stack_set_operation_request_action.py",
        "src/fern/types/post_describe_stack_set_operation_request_version.py",
        "src/fern/types/post_describe_stack_set_request_action.py",
        "src/fern/types/post_describe_stack_set_request_version.py",
        "src/fern/types/post_describe_stacks_request_action.py",
        "src/fern/types/post_describe_stacks_request_version.py",
        "src/fern/types/post_describe_type_registration_request_action.py",
        "src/fern/types/post_describe_type_registration_request_version.py",
        "src/fern/types/post_describe_type_request_action.py",
        "src/fern/types/post_describe_type_request_version.py",
        "src/fern/types/post_detect_stack_drift_request_action.py",
        "src/fern/types/post_detect_stack_drift_request_version.py",
        "src/fern/types/post_detect_stack_resource_drift_request_action.py",
        "src/fern/types/post_detect_stack_resource_drift_request_version.py",
        "src/fern/types/post_detect_stack_set_drift_request_action.py",
        "src/fern/types/post_detect_stack_set_drift_request_version.py",
        "src/fern/types/post_estimate_template_cost_request_action.py",
        "src/fern/types/post_estimate_template_cost_request_version.py",
        "src/fern/types/post_execute_change_set_request_action.py",
        "src/fern/types/post_execute_change_set_request_version.py",
        "src/fern/types/post_get_stack_policy_request_action.py",
        "src/fern/types/post_get_stack_policy_request_version.py",
        "src/fern/types/post_get_template_request_action.py",
        "src/fern/types/post_get_template_request_version.py",
        "src/fern/types/post_get_template_summary_request_action.py",
        "src/fern/types/post_get_template_summary_request_version.py",
        "src/fern/types/post_import_stacks_to_stack_set_request_action.py",
        "src/fern/types/post_import_stacks_to_stack_set_request_version.py",
        "src/fern/types/post_list_change_sets_request_action.py",
        "src/fern/types/post_list_change_sets_request_version.py",
        "src/fern/types/post_list_exports_request_action.py",
        "src/fern/types/post_list_exports_request_version.py",
        "src/fern/types/post_list_imports_request_action.py",
        "src/fern/types/post_list_imports_request_version.py",
        "src/fern/types/post_list_stack_instances_request_action.py",
        "src/fern/types/post_list_stack_instances_request_version.py",
        "src/fern/types/post_list_stack_resources_request_action.py",
        "src/fern/types/post_list_stack_resources_request_version.py",
        "src/fern/types/post_list_stack_set_operation_results_request_action.py",
        "src/fern/types/post_list_stack_set_operation_results_request_version.py",
        "src/fern/types/post_list_stack_set_operations_request_action.py",
        "src/fern/types/post_list_stack_set_operations_request_version.py",
        "src/fern/types/post_list_stack_sets_request_action.py",
        "src/fern/types/post_list_stack_sets_request_version.py",
        "src/fern/types/post_list_stacks_request_action.py",
        "src/fern/types/post_list_stacks_request_version.py",
        "src/fern/types/post_list_type_registrations_request_action.py",
        "src/fern/types/post_list_type_registrations_request_version.py",
        "src/fern/types/post_list_type_versions_request_action.py",
        "src/fern/types/post_list_type_versions_request_version.py",
        "src/fern/types/post_list_types_request_action.py",
        "src/fern/types/post_list_types_request_version.py",
        "src/fern/types/post_publish_type_request_action.py",
        "src/fern/types/post_publish_type_request_version.py",
        "src/fern/types/post_record_handler_progress_request_action.py",
        "src/fern/types/post_record_handler_progress_request_version.py",
        "src/fern/types/post_register_publisher_request_action.py",
        "src/fern/types/post_register_publisher_request_version.py",
        "src/fern/types/post_register_type_request_action.py",
        "src/fern/types/post_register_type_request_version.py",
        "src/fern/types/post_rollback_stack_request_action.py",
        "src/fern/types/post_rollback_stack_request_version.py",
        "src/fern/types/post_set_stack_policy_request_action.py",
        "src/fern/types/post_set_stack_policy_request_version.py",
        "src/fern/types/post_set_type_configuration_request_action.py",
        "src/fern/types/post_set_type_configuration_request_version.py",
        "src/fern/types/post_set_type_default_version_request_action.py",
        "src/fern/types/post_set_type_default_version_request_version.py",
        "src/fern/types/post_signal_resource_request_action.py",
        "src/fern/types/post_signal_resource_request_version.py",
        "src/fern/types/post_stop_stack_set_operation_request_action.py",
        "src/fern/types/post_stop_stack_set_operation_request_version.py",
        "src/fern/types/post_test_type_request_action.py",
        "src/fern/types/post_test_type_request_version.py",
        "src/fern/types/post_update_stack_instances_request_action.py",
        "src/fern/types/post_update_stack_instances_request_version.py",
        "src/fern/types/post_update_stack_request_action.py",
        "src/fern/types/post_update_stack_request_version.py",
        "src/fern/types/post_update_stack_set_request_action.py",
        "src/fern/types/post_update_stack_set_request_version.py",
        "src/fern/types/post_update_termination_protection_request_action.py",
        "src/fern/types/post_update_termination_protection_request_version.py",
        "src/fern/types/post_validate_template_request_action.py",
        "src/fern/types/post_validate_template_request_version.py",
        "src/fern/types/private_type_arn.py",
        "src/fern/types/properties.py",
        "src/fern/types/property_differences.py",
        "src/fern/types/property_name.py",
        "src/fern/types/property_path.py",
        "src/fern/types/property_value.py",
        "src/fern/types/provisioning_type.py",
        "src/fern/types/public_version_number.py",
        "src/fern/types/publisher_id.py",
        "src/fern/types/publisher_name.py",
        "src/fern/types/publisher_profile.py",
        "src/fern/types/publisher_status.py",
        "src/fern/types/reason.py",
        "src/fern/types/record_handler_progress_output.py",
        "src/fern/types/region.py",
        "src/fern/types/region_concurrency_type.py",
        "src/fern/types/region_list.py",
        "src/fern/types/registration_status.py",
        "src/fern/types/registration_token.py",
        "src/fern/types/registration_token_list.py",
        "src/fern/types/registry_type.py",
        "src/fern/types/replacement.py",
        "src/fern/types/request_token.py",
        "src/fern/types/required_activated_types.py",
        "src/fern/types/requires_recreation.py",
        "src/fern/types/resource_attribute.py",
        "src/fern/types/resource_change_details.py",
        "src/fern/types/resource_identifier_properties.py",
        "src/fern/types/resource_identifier_property_key.py",
        "src/fern/types/resource_identifier_property_value.py",
        "src/fern/types/resource_identifier_summaries.py",
        "src/fern/types/resource_identifiers.py",
        "src/fern/types/resource_model.py",
        "src/fern/types/resource_properties.py",
        "src/fern/types/resource_signal_status.py",
        "src/fern/types/resource_signal_unique_id.py",
        "src/fern/types/resource_status.py",
        "src/fern/types/resource_status_reason.py",
        "src/fern/types/resource_to_skip.py",
        "src/fern/types/resource_type.py",
        "src/fern/types/resource_types.py",
        "src/fern/types/resources_to_import.py",
        "src/fern/types/resources_to_skip.py",
        "src/fern/types/retain_resources.py",
        "src/fern/types/retain_stacks.py",
        "src/fern/types/retain_stacks_nullable.py",
        "src/fern/types/retain_stacks_on_account_removal_nullable.py",
        "src/fern/types/role_arn.py",
        "src/fern/types/rollback_triggers.py",
        "src/fern/types/s3bucket.py",
        "src/fern/types/s3url.py",
        "src/fern/types/scope.py",
        "src/fern/types/set_type_default_version_output.py",
        "src/fern/types/stack_drift_detection_id.py",
        "src/fern/types/stack_drift_detection_status.py",
        "src/fern/types/stack_drift_detection_status_reason.py",
        "src/fern/types/stack_drift_status.py",
        "src/fern/types/stack_events.py",
        "src/fern/types/stack_id.py",
        "src/fern/types/stack_id_list.py",
        "src/fern/types/stack_ids_url.py",
        "src/fern/types/stack_instance_detailed_status.py",
        "src/fern/types/stack_instance_filter_name.py",
        "src/fern/types/stack_instance_filter_values.py",
        "src/fern/types/stack_instance_filters.py",
        "src/fern/types/stack_instance_not_found_exception.py",
        "src/fern/types/stack_instance_status.py",
        "src/fern/types/stack_instance_summaries.py",
        "src/fern/types/stack_name.py",
        "src/fern/types/stack_name_or_id.py",
        "src/fern/types/stack_not_found_exception.py",
        "src/fern/types/stack_policy_body.py",
        "src/fern/types/stack_policy_during_update_body.py",
        "src/fern/types/stack_policy_during_update_url.py",
        "src/fern/types/stack_policy_url.py",
        "src/fern/types/stack_resource_drift_status.py",
        "src/fern/types/stack_resource_drift_status_filters.py",
        "src/fern/types/stack_resource_drifts.py",
        "src/fern/types/stack_resource_summaries.py",
        "src/fern/types/stack_resources.py",
        "src/fern/types/stack_set_arn.py",
        "src/fern/types/stack_set_drift_detection_status.py",
        "src/fern/types/stack_set_drift_status.py",
        "src/fern/types/stack_set_id.py",
        "src/fern/types/stack_set_name.py",
        "src/fern/types/stack_set_name_or_id.py",
        "src/fern/types/stack_set_not_empty_exception.py",
        "src/fern/types/stack_set_not_found_exception.py",
        "src/fern/types/stack_set_operation_action.py",
        "src/fern/types/stack_set_operation_result_status.py",
        "src/fern/types/stack_set_operation_result_summaries.py",
        "src/fern/types/stack_set_operation_status.py",
        "src/fern/types/stack_set_operation_status_reason.py",
        "src/fern/types/stack_set_operation_summaries.py",
        "src/fern/types/stack_set_status.py",
        "src/fern/types/stack_set_summaries.py",
        "src/fern/types/stack_status.py",
        "src/fern/types/stack_status_filter.py",
        "src/fern/types/stack_status_reason.py",
        "src/fern/types/stack_summaries.py",
        "src/fern/types/stacks.py",
        "src/fern/types/stage_list.py",
        "src/fern/types/stale_request_exception.py",
        "src/fern/types/status_message.py",
        "src/fern/types/stop_stack_set_operation_output.py",
        "src/fern/types/supported_major_version.py",
        "src/fern/types/supported_major_versions.py",
        "src/fern/types/tag_key.py",
        "src/fern/types/tag_value.py",
        "src/fern/types/tags.py",
        "src/fern/types/template_body.py",
        "src/fern/types/template_description.py",
        "src/fern/types/template_parameters.py",
        "src/fern/types/template_stage.py",
        "src/fern/types/template_url.py",
        "src/fern/types/third_party_type.py",
        "src/fern/types/third_party_type_arn.py",
        "src/fern/types/timeout_minutes.py",
        "src/fern/types/timestamp.py",
        "src/fern/types/token_already_exists_exception.py",
        "src/fern/types/total_stack_instances_count.py",
        "src/fern/types/transform_name.py",
        "src/fern/types/transforms_list.py",
        "src/fern/types/type.py",
        "src/fern/types/type_arn.py",
        "src/fern/types/type_configuration.py",
        "src/fern/types/type_configuration_alias.py",
        "src/fern/types/type_configuration_arn.py",
        "src/fern/types/type_configuration_details_list.py",
        "src/fern/types/type_configuration_identifiers.py",
        "src/fern/types/type_configuration_not_found_exception.py",
        "src/fern/types/type_hierarchy.py",
        "src/fern/types/type_name.py",
        "src/fern/types/type_name_prefix.py",
        "src/fern/types/type_not_found_exception.py",
        "src/fern/types/type_schema.py",
        "src/fern/types/type_summaries.py",
        "src/fern/types/type_tests_status.py",
        "src/fern/types/type_tests_status_description.py",
        "src/fern/types/type_version_id.py",
        "src/fern/types/type_version_summaries.py",
        "src/fern/types/unprocessed_type_configurations.py",
        "src/fern/types/url.py",
        "src/fern/types/use_previous_template.py",
        "src/fern/types/use_previous_value.py",
        "src/fern/types/value.py",
        "src/fern/types/version.py",
        "src/fern/types/version_bump.py",
        "src/fern/types/visibility.py",
        "src/fern/version.py",
        "src/fern/types/account_gate_result.py",
        "src/fern/types/account_gate_result_status.py",
        "src/fern/types/account_limit.py",
        "src/fern/types/activate_type_input.py",
        "src/fern/types/activate_type_input_type.py",
        "src/fern/types/activate_type_input_version_bump.py",
        "src/fern/types/activate_type_output.py",
        "src/fern/types/auto_deployment.py",
        "src/fern/types/batch_describe_type_configurations_error.py",
        "src/fern/types/batch_describe_type_configurations_input.py",
        "src/fern/types/batch_describe_type_configurations_output.py",
        "src/fern/types/cancel_update_stack_input.py",
        "src/fern/types/change.py",
        "src/fern/types/change_resource_change.py",
        "src/fern/types/change_resource_change_action.py",
        "src/fern/types/change_resource_change_module_info.py",
        "src/fern/types/change_resource_change_replacement.py",
        "src/fern/types/change_set_hook.py",
        "src/fern/types/change_set_hook_failure_mode.py",
        "src/fern/types/change_set_hook_invocation_point.py",
        "src/fern/types/change_set_hook_resource_target_details.py",
        "src/fern/types/change_set_hook_resource_target_details_resource_action.py",
        "src/fern/types/change_set_hook_target_details.py",
        "src/fern/types/change_set_hook_target_details_resource_target_details.py",
        "src/fern/types/change_set_hook_target_details_resource_target_details_resource_action.py",
        "src/fern/types/change_set_hook_target_details_target_type.py",
        "src/fern/types/change_set_summary.py",
        "src/fern/types/change_set_summary_execution_status.py",
        "src/fern/types/change_set_summary_status.py",
        "src/fern/types/change_type.py",
        "src/fern/types/continue_update_rollback_input.py",
        "src/fern/types/create_change_set_input.py",
        "src/fern/types/create_change_set_input_change_set_type.py",
        "src/fern/types/create_change_set_input_rollback_configuration.py",
        "src/fern/types/create_change_set_output.py",
        "src/fern/types/create_stack_input.py",
        "src/fern/types/create_stack_input_on_failure.py",
        "src/fern/types/create_stack_input_rollback_configuration.py",
        "src/fern/types/create_stack_instances_input.py",
        "src/fern/types/create_stack_instances_input_call_as.py",
        "src/fern/types/create_stack_instances_input_deployment_targets.py",
        "src/fern/types/create_stack_instances_input_deployment_targets_account_filter_type.py",
        "src/fern/types/create_stack_instances_input_operation_preferences.py",
        "src/fern/types/create_stack_instances_input_operation_preferences_region_concurrency_type.py",
        "src/fern/types/create_stack_instances_output.py",
        "src/fern/types/create_stack_output.py",
        "src/fern/types/create_stack_set_input.py",
        "src/fern/types/create_stack_set_input_auto_deployment.py",
        "src/fern/types/create_stack_set_input_call_as.py",
        "src/fern/types/create_stack_set_input_managed_execution.py",
        "src/fern/types/create_stack_set_input_permission_model.py",
        "src/fern/types/create_stack_set_output.py",
        "src/fern/types/deactivate_type_input.py",
        "src/fern/types/deactivate_type_input_type.py",
        "src/fern/types/delete_change_set_input.py",
        "src/fern/types/delete_stack_input.py",
        "src/fern/types/delete_stack_instances_input.py",
        "src/fern/types/delete_stack_instances_input_call_as.py",
        "src/fern/types/delete_stack_instances_input_deployment_targets.py",
        "src/fern/types/delete_stack_instances_input_deployment_targets_account_filter_type.py",
        "src/fern/types/delete_stack_instances_input_operation_preferences.py",
        "src/fern/types/delete_stack_instances_input_operation_preferences_region_concurrency_type.py",
        "src/fern/types/delete_stack_instances_output.py",
        "src/fern/types/delete_stack_set_input.py",
        "src/fern/types/delete_stack_set_input_call_as.py",
        "src/fern/types/deployment_targets.py",
        "src/fern/types/deployment_targets_account_filter_type.py",
        "src/fern/types/deregister_type_input.py",
        "src/fern/types/deregister_type_input_type.py",
        "src/fern/types/describe_account_limits_input.py",
        "src/fern/types/describe_account_limits_output.py",
        "src/fern/types/describe_change_set_hooks_input.py",
        "src/fern/types/describe_change_set_hooks_output.py",
        "src/fern/types/describe_change_set_hooks_output_status.py",
        "src/fern/types/describe_change_set_input.py",
        "src/fern/types/describe_change_set_output.py",
        "src/fern/types/describe_change_set_output_execution_status.py",
        "src/fern/types/describe_change_set_output_rollback_configuration.py",
        "src/fern/types/describe_change_set_output_status.py",
        "src/fern/types/describe_publisher_input.py",
        "src/fern/types/describe_publisher_output.py",
        "src/fern/types/describe_publisher_output_identity_provider.py",
        "src/fern/types/describe_publisher_output_publisher_status.py",
        "src/fern/types/describe_stack_drift_detection_status_input.py",
        "src/fern/types/describe_stack_drift_detection_status_output.py",
        "src/fern/types/describe_stack_drift_detection_status_output_detection_status.py",
        "src/fern/types/describe_stack_drift_detection_status_output_stack_drift_status.py",
        "src/fern/types/describe_stack_events_input.py",
        "src/fern/types/describe_stack_events_output.py",
        "src/fern/types/describe_stack_instance_input.py",
        "src/fern/types/describe_stack_instance_input_call_as.py",
        "src/fern/types/describe_stack_instance_output.py",
        "src/fern/types/describe_stack_instance_output_stack_instance.py",
        "src/fern/types/describe_stack_instance_output_stack_instance_drift_status.py",
        "src/fern/types/describe_stack_instance_output_stack_instance_stack_instance_status.py",
        "src/fern/types/describe_stack_instance_output_stack_instance_stack_instance_status_detailed_status.py",
        "src/fern/types/describe_stack_instance_output_stack_instance_status.py",
        "src/fern/types/describe_stack_resource_drifts_input.py",
        "src/fern/types/describe_stack_resource_drifts_output.py",
        "src/fern/types/describe_stack_resource_input.py",
        "src/fern/types/describe_stack_resource_output.py",
        "src/fern/types/describe_stack_resource_output_stack_resource_detail.py",
        "src/fern/types/describe_stack_resource_output_stack_resource_detail_drift_information.py",
        "src/fern/types/describe_stack_resource_output_stack_resource_detail_drift_information_stack_resource_drift_status.py",
        "src/fern/types/describe_stack_resource_output_stack_resource_detail_module_info.py",
        "src/fern/types/describe_stack_resource_output_stack_resource_detail_resource_status.py",
        "src/fern/types/describe_stack_resources_input.py",
        "src/fern/types/describe_stack_resources_output.py",
        "src/fern/types/describe_stack_set_input.py",
        "src/fern/types/describe_stack_set_input_call_as.py",
        "src/fern/types/describe_stack_set_operation_input.py",
        "src/fern/types/describe_stack_set_operation_input_call_as.py",
        "src/fern/types/describe_stack_set_operation_output.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_action.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_deployment_targets.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_deployment_targets_account_filter_type.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_operation_preferences.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_operation_preferences_region_concurrency_type.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_detection_status.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_status.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_status.py",
        "src/fern/types/describe_stack_set_operation_output_stack_set_operation_status_details.py",
        "src/fern/types/describe_stack_set_output.py",
        "src/fern/types/describe_stack_set_output_stack_set.py",
        "src/fern/types/describe_stack_set_output_stack_set_auto_deployment.py",
        "src/fern/types/describe_stack_set_output_stack_set_managed_execution.py",
        "src/fern/types/describe_stack_set_output_stack_set_permission_model.py",
        "src/fern/types/describe_stack_set_output_stack_set_stack_set_drift_detection_details.py",
        "src/fern/types/describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_detection_status.py",
        "src/fern/types/describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_status.py",
        "src/fern/types/describe_stack_set_output_stack_set_status.py",
        "src/fern/types/describe_stacks_input.py",
        "src/fern/types/describe_stacks_output.py",
        "src/fern/types/describe_type_input.py",
        "src/fern/types/describe_type_input_type.py",
        "src/fern/types/describe_type_output.py",
        "src/fern/types/describe_type_output_deprecated_status.py",
        "src/fern/types/describe_type_output_logging_config.py",
        "src/fern/types/describe_type_output_provisioning_type.py",
        "src/fern/types/describe_type_output_type.py",
        "src/fern/types/describe_type_output_type_tests_status.py",
        "src/fern/types/describe_type_output_visibility.py",
        "src/fern/types/describe_type_registration_input.py",
        "src/fern/types/describe_type_registration_output.py",
        "src/fern/types/describe_type_registration_output_progress_status.py",
        "src/fern/types/detect_stack_drift_input.py",
        "src/fern/types/detect_stack_drift_output.py",
        "src/fern/types/detect_stack_resource_drift_input.py",
        "src/fern/types/detect_stack_resource_drift_output.py",
        "src/fern/types/detect_stack_resource_drift_output_stack_resource_drift.py",
        "src/fern/types/detect_stack_resource_drift_output_stack_resource_drift_module_info.py",
        "src/fern/types/detect_stack_resource_drift_output_stack_resource_drift_stack_resource_drift_status.py",
        "src/fern/types/detect_stack_set_drift_input.py",
        "src/fern/types/detect_stack_set_drift_input_call_as.py",
        "src/fern/types/detect_stack_set_drift_output.py",
        "src/fern/types/estimate_template_cost_input.py",
        "src/fern/types/estimate_template_cost_output.py",
        "src/fern/types/execute_change_set_input.py",
        "src/fern/types/export.py",
        "src/fern/types/export_name.py",
        "src/fern/types/export_value.py",
        "src/fern/types/get_stack_policy_input.py",
        "src/fern/types/get_stack_policy_output.py",
        "src/fern/types/get_template_input.py",
        "src/fern/types/get_template_input_template_stage.py",
        "src/fern/types/get_template_output.py",
        "src/fern/types/get_template_summary_input.py",
        "src/fern/types/get_template_summary_input_call_as.py",
        "src/fern/types/get_template_summary_output.py",
        "src/fern/types/import_stacks_to_stack_set_input.py",
        "src/fern/types/import_stacks_to_stack_set_input_call_as.py",
        "src/fern/types/import_stacks_to_stack_set_output.py",
        "src/fern/types/list_change_sets_input.py",
        "src/fern/types/list_change_sets_output.py",
        "src/fern/types/list_exports_input.py",
        "src/fern/types/list_exports_output.py",
        "src/fern/types/list_imports_input.py",
        "src/fern/types/list_imports_output.py",
        "src/fern/types/list_stack_instances_input.py",
        "src/fern/types/list_stack_instances_input_call_as.py",
        "src/fern/types/list_stack_instances_output.py",
        "src/fern/types/list_stack_resources_input.py",
        "src/fern/types/list_stack_resources_output.py",
        "src/fern/types/list_stack_set_operation_results_input.py",
        "src/fern/types/list_stack_set_operation_results_input_call_as.py",
        "src/fern/types/list_stack_set_operation_results_output.py",
        "src/fern/types/list_stack_set_operations_input.py",
        "src/fern/types/list_stack_set_operations_input_call_as.py",
        "src/fern/types/list_stack_set_operations_output.py",
        "src/fern/types/list_stack_sets_input.py",
        "src/fern/types/list_stack_sets_input_call_as.py",
        "src/fern/types/list_stack_sets_input_status.py",
        "src/fern/types/list_stack_sets_output.py",
        "src/fern/types/list_stacks_input.py",
        "src/fern/types/list_stacks_output.py",
        "src/fern/types/list_type_registrations_input.py",
        "src/fern/types/list_type_registrations_input_registration_status_filter.py",
        "src/fern/types/list_type_registrations_input_type.py",
        "src/fern/types/list_type_registrations_output.py",
        "src/fern/types/list_type_versions_input.py",
        "src/fern/types/list_type_versions_input_deprecated_status.py",
        "src/fern/types/list_type_versions_input_type.py",
        "src/fern/types/list_type_versions_output.py",
        "src/fern/types/list_types_input.py",
        "src/fern/types/list_types_input_deprecated_status.py",
        "src/fern/types/list_types_input_filters.py",
        "src/fern/types/list_types_input_filters_category.py",
        "src/fern/types/list_types_input_provisioning_type.py",
        "src/fern/types/list_types_input_type.py",
        "src/fern/types/list_types_input_visibility.py",
        "src/fern/types/list_types_output.py",
        "src/fern/types/logging_config.py",
        "src/fern/types/managed_execution.py",
        "src/fern/types/module_info.py",
        "src/fern/types/operation_result_filter.py",
        "src/fern/types/output.py",
        "src/fern/types/parameter.py",
        "src/fern/types/parameter_constraints.py",
        "src/fern/types/parameter_declaration.py",
        "src/fern/types/parameter_declaration_parameter_constraints.py",
        "src/fern/types/physical_resource_id_context_key_value_pair.py",
        "src/fern/types/property_difference.py",
        "src/fern/types/property_difference_difference_type.py",
        "src/fern/types/publish_type_input.py",
        "src/fern/types/publish_type_input_type.py",
        "src/fern/types/publish_type_output.py",
        "src/fern/types/record_handler_progress_input.py",
        "src/fern/types/record_handler_progress_input_current_operation_status.py",
        "src/fern/types/record_handler_progress_input_error_code.py",
        "src/fern/types/record_handler_progress_input_operation_status.py",
        "src/fern/types/register_publisher_input.py",
        "src/fern/types/register_publisher_output.py",
        "src/fern/types/register_type_input.py",
        "src/fern/types/register_type_input_logging_config.py",
        "src/fern/types/register_type_input_type.py",
        "src/fern/types/register_type_output.py",
        "src/fern/types/required_activated_type.py",
        "src/fern/types/resource_change.py",
        "src/fern/types/resource_change_action.py",
        "src/fern/types/resource_change_detail.py",
        "src/fern/types/resource_change_detail_change_source.py",
        "src/fern/types/resource_change_detail_evaluation.py",
        "src/fern/types/resource_change_detail_target.py",
        "src/fern/types/resource_change_detail_target_attribute.py",
        "src/fern/types/resource_change_detail_target_requires_recreation.py",
        "src/fern/types/resource_change_module_info.py",
        "src/fern/types/resource_change_replacement.py",
        "src/fern/types/resource_identifier_summary.py",
        "src/fern/types/resource_target_definition.py",
        "src/fern/types/resource_target_definition_attribute.py",
        "src/fern/types/resource_target_definition_requires_recreation.py",
        "src/fern/types/resource_to_import.py",
        "src/fern/types/rollback_configuration.py",
        "src/fern/types/rollback_stack_input.py",
        "src/fern/types/rollback_stack_output.py",
        "src/fern/types/rollback_trigger.py",
        "src/fern/types/set_stack_policy_input.py",
        "src/fern/types/set_type_configuration_input.py",
        "src/fern/types/set_type_configuration_input_type.py",
        "src/fern/types/set_type_configuration_output.py",
        "src/fern/types/set_type_default_version_input.py",
        "src/fern/types/set_type_default_version_input_type.py",
        "src/fern/types/signal_resource_input.py",
        "src/fern/types/signal_resource_input_status.py",
        "src/fern/types/stack.py",
        "src/fern/types/stack_drift_information.py",
        "src/fern/types/stack_drift_information_stack_drift_status.py",
        "src/fern/types/stack_drift_information_summary.py",
        "src/fern/types/stack_drift_information_summary_stack_drift_status.py",
        "src/fern/types/stack_event.py",
        "src/fern/types/stack_event_hook_failure_mode.py",
        "src/fern/types/stack_event_hook_invocation_point.py",
        "src/fern/types/stack_event_hook_status.py",
        "src/fern/types/stack_event_resource_status.py",
        "src/fern/types/stack_instance.py",
        "src/fern/types/stack_instance_comprehensive_status.py",
        "src/fern/types/stack_instance_comprehensive_status_detailed_status.py",
        "src/fern/types/stack_instance_drift_status.py",
        "src/fern/types/stack_instance_filter.py",
        "src/fern/types/stack_instance_stack_instance_status.py",
        "src/fern/types/stack_instance_stack_instance_status_detailed_status.py",
        "src/fern/types/stack_instance_summary.py",
        "src/fern/types/stack_instance_summary_drift_status.py",
        "src/fern/types/stack_instance_summary_stack_instance_status.py",
        "src/fern/types/stack_instance_summary_stack_instance_status_detailed_status.py",
        "src/fern/types/stack_instance_summary_status.py",
        "src/fern/types/stack_resource.py",
        "src/fern/types/stack_resource_detail.py",
        "src/fern/types/stack_resource_detail_drift_information.py",
        "src/fern/types/stack_resource_detail_drift_information_stack_resource_drift_status.py",
        "src/fern/types/stack_resource_detail_module_info.py",
        "src/fern/types/stack_resource_detail_resource_status.py",
        "src/fern/types/stack_resource_drift.py",
        "src/fern/types/stack_resource_drift_information.py",
        "src/fern/types/stack_resource_drift_information_stack_resource_drift_status.py",
        "src/fern/types/stack_resource_drift_information_summary.py",
        "src/fern/types/stack_resource_drift_information_summary_stack_resource_drift_status.py",
        "src/fern/types/stack_resource_drift_module_info.py",
        "src/fern/types/stack_resource_drift_stack_resource_drift_status.py",
        "src/fern/types/stack_resource_module_info.py",
        "src/fern/types/stack_resource_resource_status.py",
        "src/fern/types/stack_resource_summary.py",
        "src/fern/types/stack_resource_summary_drift_information.py",
        "src/fern/types/stack_resource_summary_drift_information_stack_resource_drift_status.py",
        "src/fern/types/stack_resource_summary_module_info.py",
        "src/fern/types/stack_resource_summary_resource_status.py",
        "src/fern/types/stack_rollback_configuration.py",
        "src/fern/types/stack_set.py",
        "src/fern/types/stack_set_auto_deployment.py",
        "src/fern/types/stack_set_drift_detection_details.py",
        "src/fern/types/stack_set_drift_detection_details_drift_detection_status.py",
        "src/fern/types/stack_set_drift_detection_details_drift_status.py",
        "src/fern/types/stack_set_managed_execution.py",
        "src/fern/types/stack_set_operation.py",
        "src/fern/types/stack_set_operation_deployment_targets.py",
        "src/fern/types/stack_set_operation_deployment_targets_account_filter_type.py",
        "src/fern/types/stack_set_operation_operation_preferences.py",
        "src/fern/types/stack_set_operation_operation_preferences_region_concurrency_type.py",
        "src/fern/types/stack_set_operation_preferences.py",
        "src/fern/types/stack_set_operation_preferences_region_concurrency_type.py",
        "src/fern/types/stack_set_operation_result_summary.py",
        "src/fern/types/stack_set_operation_result_summary_account_gate_result.py",
        "src/fern/types/stack_set_operation_result_summary_account_gate_result_status.py",
        "src/fern/types/stack_set_operation_result_summary_status.py",
        "src/fern/types/stack_set_operation_stack_set_drift_detection_details.py",
        "src/fern/types/stack_set_operation_stack_set_drift_detection_details_drift_detection_status.py",
        "src/fern/types/stack_set_operation_stack_set_drift_detection_details_drift_status.py",
        "src/fern/types/stack_set_operation_status_details.py",
        "src/fern/types/stack_set_operation_summary.py",
        "src/fern/types/stack_set_operation_summary_action.py",
        "src/fern/types/stack_set_operation_summary_status.py",
        "src/fern/types/stack_set_operation_summary_status_details.py",
        "src/fern/types/stack_set_permission_model.py",
        "src/fern/types/stack_set_stack_set_drift_detection_details.py",
        "src/fern/types/stack_set_stack_set_drift_detection_details_drift_detection_status.py",
        "src/fern/types/stack_set_stack_set_drift_detection_details_drift_status.py",
        "src/fern/types/stack_set_summary.py",
        "src/fern/types/stack_set_summary_auto_deployment.py",
        "src/fern/types/stack_set_summary_drift_status.py",
        "src/fern/types/stack_set_summary_managed_execution.py",
        "src/fern/types/stack_set_summary_permission_model.py",
        "src/fern/types/stack_set_summary_status.py",
        "src/fern/types/stack_stack_status.py",
        "src/fern/types/stack_summary.py",
        "src/fern/types/stack_summary_drift_information.py",
        "src/fern/types/stack_summary_drift_information_stack_drift_status.py",
        "src/fern/types/stack_summary_stack_status.py",
        "src/fern/types/stop_stack_set_operation_input.py",
        "src/fern/types/stop_stack_set_operation_input_call_as.py",
        "src/fern/types/tag.py",
        "src/fern/types/template_parameter.py",
        "src/fern/types/test_type_input.py",
        "src/fern/types/test_type_input_type.py",
        "src/fern/types/test_type_output.py",
        "src/fern/types/type_configuration_details.py",
        "src/fern/types/type_configuration_identifier.py",
        "src/fern/types/type_configuration_identifier_type.py",
        "src/fern/types/type_filters.py",
        "src/fern/types/type_filters_category.py",
        "src/fern/types/type_summary.py",
        "src/fern/types/type_summary_publisher_identity.py",
        "src/fern/types/type_summary_type.py",
        "src/fern/types/type_version_summary.py",
        "src/fern/types/type_version_summary_type.py",
        "src/fern/types/update_stack_input.py",
        "src/fern/types/update_stack_input_rollback_configuration.py",
        "src/fern/types/update_stack_instances_input.py",
        "src/fern/types/update_stack_instances_input_call_as.py",
        "src/fern/types/update_stack_instances_input_deployment_targets.py",
        "src/fern/types/update_stack_instances_input_deployment_targets_account_filter_type.py",
        "src/fern/types/update_stack_instances_input_operation_preferences.py",
        "src/fern/types/update_stack_instances_input_operation_preferences_region_concurrency_type.py",
        "src/fern/types/update_stack_instances_output.py",
        "src/fern/types/update_stack_output.py",
        "src/fern/types/update_stack_set_input.py",
        "src/fern/types/update_stack_set_input_auto_deployment.py",
        "src/fern/types/update_stack_set_input_call_as.py",
        "src/fern/types/update_stack_set_input_deployment_targets.py",
        "src/fern/types/update_stack_set_input_deployment_targets_account_filter_type.py",
        "src/fern/types/update_stack_set_input_managed_execution.py",
        "src/fern/types/update_stack_set_input_operation_preferences.py",
        "src/fern/types/update_stack_set_input_operation_preferences_region_concurrency_type.py",
        "src/fern/types/update_stack_set_input_permission_model.py",
        "src/fern/types/update_stack_set_output.py",
        "src/fern/types/update_termination_protection_input.py",
        "src/fern/types/update_termination_protection_output.py",
        "src/fern/types/validate_template_input.py",
        "src/fern/types/validate_template_output.py",
        "src/fern/__init__.py",
        "src/fern/types/__init__.py",
        "src/fern/types/get_activate_type_request_logging_config.py",
        "src/fern/types/get_create_change_set_request_rollback_configuration.py",
        "src/fern/types/get_create_stack_instances_request_deployment_targets.py",
        "src/fern/types/get_create_stack_instances_request_deployment_targets_account_filter_type.py",
        "src/fern/types/get_create_stack_instances_request_operation_preferences.py",
        "src/fern/types/get_create_stack_instances_request_operation_preferences_region_concurrency_type.py",
        "src/fern/types/get_create_stack_request_rollback_configuration.py",
        "src/fern/types/get_create_stack_set_request_auto_deployment.py",
        "src/fern/types/get_create_stack_set_request_managed_execution.py",
        "src/fern/types/get_delete_stack_instances_request_deployment_targets.py",
        "src/fern/types/get_delete_stack_instances_request_deployment_targets_account_filter_type.py",
        "src/fern/types/get_delete_stack_instances_request_operation_preferences.py",
        "src/fern/types/get_delete_stack_instances_request_operation_preferences_region_concurrency_type.py",
        "src/fern/types/get_detect_stack_set_drift_request_operation_preferences.py",
        "src/fern/types/get_detect_stack_set_drift_request_operation_preferences_region_concurrency_type.py",
        "src/fern/types/get_import_stacks_to_stack_set_request_operation_preferences.py",
        "src/fern/types/get_import_stacks_to_stack_set_request_operation_preferences_region_concurrency_type.py",
        "src/fern/types/get_list_types_request_filters.py",
        "src/fern/types/get_list_types_request_filters_category.py",
        "src/fern/types/get_register_type_request_logging_config.py",
        "src/fern/types/get_update_stack_instances_request_deployment_targets.py",
        "src/fern/types/get_update_stack_instances_request_deployment_targets_account_filter_type.py",
        "src/fern/types/get_update_stack_instances_request_operation_preferences.py",
        "src/fern/types/get_update_stack_instances_request_operation_preferences_region_concurrency_type.py",
        "src/fern/types/get_update_stack_request_rollback_configuration.py",
        "src/fern/types/get_update_stack_set_request_auto_deployment.py",
        "src/fern/types/get_update_stack_set_request_deployment_targets.py",
        "src/fern/types/get_update_stack_set_request_deployment_targets_account_filter_type.py",
        "src/fern/types/get_update_stack_set_request_managed_execution.py",
        "src/fern/types/get_update_stack_set_request_operation_preferences.py",
        "src/fern/types/get_update_stack_set_request_operation_preferences_region_concurrency_type.py",
        "src/fern/raw_client.py",
        "README.md",
        "src/fern/client.py",
        "reference.md",
    ],
};

/// `redocly.com-museum`: a compact OpenAPI 3.1 corpus spanning eight operations,
/// `allOf`, string formats, reusable examples, binary responses, and non-JSON
/// media types. Fully matched: all 63 Fern output files reproduce byte-for-byte.
const REDOCLY_COM_MUSEUM: Corpus = Corpus {
    api: "redocly.com-museum",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/events/__init__.py",
        "src/fern/events/client.py",
        "src/fern/events/raw_client.py",
        "src/fern/operations/__init__.py",
        "src/fern/operations/client.py",
        "src/fern/operations/raw_client.py",
        "src/fern/py.typed",
        "src/fern/tickets/__init__.py",
        "src/fern/tickets/client.py",
        "src/fern/tickets/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/date.py",
        "src/fern/types/email.py",
        "src/fern/types/error.py",
        "src/fern/types/event_dates.py",
        "src/fern/types/event_description.py",
        "src/fern/types/event_id.py",
        "src/fern/types/event_location.py",
        "src/fern/types/event_name.py",
        "src/fern/types/event_price.py",
        "src/fern/types/museum_daily_hours.py",
        "src/fern/types/museum_hours.py",
        "src/fern/types/museum_tickets_confirmation.py",
        "src/fern/types/special_event.py",
        "src/fern/types/special_event_collection.py",
        "src/fern/types/ticket.py",
        "src/fern/types/ticket_code_image.py",
        "src/fern/types/ticket_confirmation.py",
        "src/fern/types/ticket_id.py",
        "src/fern/types/ticket_message.py",
        "src/fern/types/ticket_type.py",
        "src/fern/version.py",
    ],
};

/// `http-toolkit`: HTTP Toolkit's OpenAPI 3.0 service API, spanning 26 operations,
/// wildcard paths, five HTTP methods, basic and bearer auth, UUIDs, and binary
/// responses. Fully matched against its workflow-generated Fern golden.
const HTTP_TOOLKIT: Corpus = Corpus {
    api: "http-toolkit",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/authenticated_routes/__init__.py",
        "src/fern/authenticated_routes/client.py",
        "src/fern/authenticated_routes/raw_client.py",
        "src/fern/base_routes/__init__.py",
        "src/fern/base_routes/client.py",
        "src/fern/base_routes/raw_client.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/unauthorized_error.py",
        "src/fern/inspect_routes/__init__.py",
        "src/fern/inspect_routes/client.py",
        "src/fern/inspect_routes/raw_client.py",
        "src/fern/py.typed",
        "src/fern/types/__init__.py",
        "src/fern/types/ok.py",
        "src/fern/types/request_info.py",
        "src/fern/types/system_info.py",
        "src/fern/utility_routes/__init__.py",
        "src/fern/utility_routes/client.py",
        "src/fern/utility_routes/raw_client.py",
        "src/fern/version.py",
        "src/fern/wildcard_inspection_routes/__init__.py",
        "src/fern/wildcard_inspection_routes/client.py",
        "src/fern/wildcard_inspection_routes/raw_client.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `frankfurter`: a real OpenAPI 3.1.2 currency API exercising nullable schemas
/// expressed with JSON Schema type arrays. Fern accepts the raw pinned spec;
/// byte matching begins after the workflow generates its golden.
const FRANKFURTER: Corpus = Corpus {
    api: "frankfurter",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/currency.py",
        "src/fern/types/currency_detail.py",
        "src/fern/types/currency_detail_peg.py",
        "src/fern/types/get_currencies_request_scope.py",
        "src/fern/types/get_rates_request_expand.py",
        "src/fern/types/get_rates_request_group.py",
        "src/fern/types/not_found_error_body.py",
        "src/fern/types/provider.py",
        "src/fern/types/provider_publish_cadence.py",
        "src/fern/types/rate.py",
        "src/fern/types/rate_providers_item.py",
        "src/fern/types/unprocessable_entity_error_body.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `worldcoin-signup-sequencer`: Worldcoin's OpenAPI 3.1 API, including tuple
/// arrays represented with `prefixItems`. Fern accepts the raw pinned spec; the
/// golden is workflow-owned.
const WORLDCOIN_SIGNUP_SEQUENCER: Corpus = Corpus {
    api: "worldcoin-signup-sequencer",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/gone_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/identities/__init__.py",
        "src/fern/identities/client.py",
        "src/fern/identities/raw_client.py",
        "src/fern/identities/types/__init__.py",
        "src/fern/identities/types/get_v3identities_commitment_inclusion_proof_inclusion_proof_type_request_inclusion_proof_type.py",
        "src/fern/py.typed",
        "src/fern/semaphore_proof/__init__.py",
        "src/fern/semaphore_proof/client.py",
        "src/fern/semaphore_proof/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/compressed_semaphore_proof.py",
        "src/fern/types/error.py",
        "src/fern/types/field_element.py",
        "src/fern/types/g1.py",
        "src/fern/types/g2.py",
        "src/fern/types/identity.py",
        "src/fern/types/inclusion_proof.py",
        "src/fern/types/inclusion_proof_proof_item.py",
        "src/fern/types/inclusion_proof_proof_item_left.py",
        "src/fern/types/inclusion_proof_proof_item_right.py",
        "src/fern/types/semaphore_proof.py",
        "src/fern/types/semaphore_proof_verification_result.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `electric-sql`: Electric's OpenAPI 3.1 HTTP API, exercising JSON Schema
/// `patternProperties`. Fern accepts the raw pinned spec; the golden is workflow-owned.
const ELECTRIC_SQL: Corpus = Corpus {
    api: "electric-sql",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/_default_clients.py",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/content_too_large_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/py.typed",
        "src/fern/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/conflict_error_body_item.py",
        "src/fern/types/conflict_error_body_item_headers.py",
        "src/fern/types/conflict_error_body_item_headers_control.py",
        "src/fern/types/get_v1shape_request_log.py",
        "src/fern/types/get_v1shape_request_replica.py",
        "src/fern/types/get_v1shape_response.py",
        "src/fern/types/get_v1shape_response_data.py",
        "src/fern/types/get_v1shape_response_data_data_item.py",
        "src/fern/types/get_v1shape_response_data_data_item_headers.py",
        "src/fern/types/get_v1shape_response_data_data_item_headers_operation.py",
        "src/fern/types/get_v1shape_response_data_metadata.py",
        "src/fern/types/get_v1shape_response_zero_item.py",
        "src/fern/types/get_v1shape_response_zero_item_headers.py",
        "src/fern/types/get_v1shape_response_zero_item_headers_control.py",
        "src/fern/types/get_v1shape_response_zero_item_headers_operation.py",
        "src/fern/types/post_v1shape_request_log.py",
        "src/fern/types/post_v1shape_request_replica.py",
        "src/fern/types/post_v1shape_response.py",
        "src/fern/types/post_v1shape_response_data_item.py",
        "src/fern/types/post_v1shape_response_metadata.py",
        "src/fern/types/too_many_requests_error_body.py",
        "src/fern/environment.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `tamoss`: TAMOSS's OpenAPI 3.1 contract, covering conditional schemas,
/// `const`, and top-level webhooks. Fern accepts the raw pinned spec; the golden
/// is workflow-owned.
const TAMOSS: Corpus = Corpus {
    api: "tamoss",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/flow_delete_requests/__init__.py",
        "src/fern/flow_delete_requests/client.py",
        "src/fern/flow_delete_requests/raw_client.py",
        "src/fern/flow_segments/__init__.py",
        "src/fern/flow_segments/client.py",
        "src/fern/flow_segments/raw_client.py",
        "src/fern/flow_segments/types/__init__.py",
        "src/fern/flow_segments/types/post_flows_flow_id_segments_request_body.py",
        "src/fern/flows/__init__.py",
        "src/fern/flows/client.py",
        "src/fern/flows/raw_client.py",
        "src/fern/media_storage/__init__.py",
        "src/fern/media_storage/client.py",
        "src/fern/media_storage/raw_client.py",
        "src/fern/objects/__init__.py",
        "src/fern/objects/client.py",
        "src/fern/objects/raw_client.py",
        "src/fern/py.typed",
        "src/fern/service/__init__.py",
        "src/fern/service/client.py",
        "src/fern/service/raw_client.py",
        "src/fern/sources/__init__.py",
        "src/fern/sources/client.py",
        "src/fern/sources/raw_client.py",
        "src/fern/types/collection_item.py",
        "src/fern/types/container_mapping.py",
        "src/fern/types/container_mapping_audio_track.py",
        "src/fern/types/container_mapping_isobmff_container.py",
        "src/fern/types/container_mapping_mp2ts_container.py",
        "src/fern/types/container_mapping_mxf_container.py",
        "src/fern/types/content_format.py",
        "src/fern/types/deletion_request.py",
        "src/fern/types/deletion_request_status.py",
        "src/fern/types/error.py",
        "src/fern/types/error_payload.py",
        "src/fern/types/event_stream_common.py",
        "src/fern/types/flow_audio.py",
        "src/fern/types/flow.py",
        "src/fern/types/flow_audio_essence_parameters.py",
        "src/fern/types/flow_audio_essence_parameters_codec_parameters.py",
        "src/fern/types/flow_audio_essence_parameters_unc_parameters.py",
        "src/fern/types/flow_audio_essence_parameters_unc_parameters_unc_type.py",
        "src/fern/types/flow_audio_format.py",
        "src/fern/types/flow_collection.py",
        "src/fern/types/flow_collection_item.py",
        "src/fern/types/flow_core.py",
        "src/fern/types/flow_core_segment_duration.py",
        "src/fern/types/flow_data.py",
        "src/fern/types/flow_data_essence_parameters.py",
        "src/fern/types/flow_data_format.py",
        "src/fern/types/flow_image.py",
        "src/fern/types/flow_image_essence_parameters.py",
        "src/fern/types/flow_image_essence_parameters_aspect_ratio.py",
        "src/fern/types/flow_image_format.py",
        "src/fern/types/flow_multi.py",
        "src/fern/types/flow_multi_format.py",
        "src/fern/types/flow_segment.py",
        "src/fern/types/flow_segment_bulk_failure.py",
        "src/fern/types/flow_segment_bulk_failure_failed_segments_item.py",
        "src/fern/types/flow_segment_post.py",
        "src/fern/types/flow_segment_post_get_urls_item.py",
        "src/fern/types/flow_storage.py",
        "src/fern/types/flow_storage_media_objects_item.py",
        "src/fern/types/flow_video.py",
        "src/fern/types/flow_video_essence_parameters.py",
        "src/fern/types/flow_video_essence_parameters_aspect_ratio.py",
        "src/fern/types/flow_video_essence_parameters_avc_parameters.py",
        "src/fern/types/flow_video_essence_parameters_colorspace.py",
        "src/fern/types/flow_video_essence_parameters_component_type.py",
        "src/fern/types/flow_video_essence_parameters_frame_rate.py",
        "src/fern/types/flow_video_essence_parameters_interlace_mode.py",
        "src/fern/types/flow_video_essence_parameters_pixel_aspect_ratio.py",
        "src/fern/types/flow_video_essence_parameters_transfer_characteristic.py",
        "src/fern/types/flow_video_essence_parameters_unc_parameters.py",
        "src/fern/types/flow_video_essence_parameters_unc_parameters_unc_type.py",
        "src/fern/types/flow_video_format.py",
        "src/fern/types/http_request.py",
        "src/fern/types/mime_type.py",
        "src/fern/types/object.py",
        "src/fern/types/object_core.py",
        "src/fern/types/object_core_get_urls_item.py",
        "src/fern/types/objects_instances_post.py",
        "src/fern/types/objects_instances_post_label.py",
        "src/fern/types/objects_instances_post_storage_id.py",
        "src/fern/types/__init__.py",
        "src/fern/types/post_flows_created_payload.py",
        "src/fern/types/post_flows_created_payload_event.py",
        "src/fern/types/post_flows_created_payload_event_type.py",
        "src/fern/types/post_flows_deleted_payload.py",
        "src/fern/types/post_flows_deleted_payload_event.py",
        "src/fern/types/post_flows_deleted_payload_event_type.py",
        "src/fern/types/post_flows_segments_added_payload.py",
        "src/fern/types/post_flows_segments_added_payload_event.py",
        "src/fern/types/post_flows_segments_added_payload_event_type.py",
        "src/fern/types/post_flows_segments_deleted_payload.py",
        "src/fern/types/post_flows_segments_deleted_payload_event.py",
        "src/fern/types/post_flows_segments_deleted_payload_event_type.py",
        "src/fern/types/post_flows_updated_payload.py",
        "src/fern/types/post_flows_updated_payload_event.py",
        "src/fern/types/post_flows_updated_payload_event_type.py",
        "src/fern/types/post_sources_created_payload.py",
        "src/fern/types/post_sources_created_payload_event.py",
        "src/fern/types/post_sources_created_payload_event_type.py",
        "src/fern/types/post_sources_deleted_payload.py",
        "src/fern/types/post_sources_deleted_payload_event.py",
        "src/fern/types/post_sources_deleted_payload_event_type.py",
        "src/fern/types/post_sources_updated_payload.py",
        "src/fern/types/post_sources_updated_payload_event.py",
        "src/fern/types/post_sources_updated_payload_event_type.py",
        "src/fern/types/service.py",
        "src/fern/types/source.py",
        "src/fern/types/storage_backend.py",
        "src/fern/types/storage_backends_list_item.py",
        "src/fern/types/tags.py",
        "src/fern/types/tags_value.py",
        "src/fern/types/storage_backend_store_type.py",
        "src/fern/types/storage_backends_list.py",
        "src/fern/types/timerange.py",
        "src/fern/types/timestamp.py",
        "src/fern/types/url_label_list.py",
        "src/fern/types/url_tag_list.py",
        "src/fern/types/uuid_.py",
        "src/fern/types/uuid_list.py",
        "src/fern/types/webhook.py",
        "src/fern/types/webhook_events_item.py",
        "src/fern/types/webhook_get.py",
        "src/fern/types/webhook_get_status.py",
        "src/fern/types/webhook_with_id.py",
        "src/fern/version.py",
        "src/fern/webhooks/__init__.py",
        "src/fern/webhooks/client.py",
        "src/fern/webhooks/raw_client.py",
        "src/fern/webhooks/types/__init__.py",
        "src/fern/webhooks/types/webhook_post_status.py",
        "src/fern/webhooks/types/webhook_put_status.py",
        "README.md",
        "src/fern/client.py",
        "src/fern/environment.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `appng-rest-api`: appNG's deployed REST API exercises matrix serialization
/// and cookie parameters. Fern accepts the raw pinned spec.
const APPNG_REST_API: Corpus = Corpus {
    api: "appng-rest-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[],
};

/// `slurmdb-rest`: UB CCR's SlurmDB REST API exercises label and explicit form
/// serialization. Fern accepts the raw pinned spec.
const SLURMDB_REST: Corpus = Corpus {
    api: "slurmdb-rest",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/openapi/__init__.py",
        "src/fern/openapi/client.py",
        "src/fern/openapi/raw_client.py",
        "src/fern/py.typed",
        "src/fern/slurm/__init__.py",
        "src/fern/slurm/client.py",
        "src/fern/slurm/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/dbv0037account.py",
        "src/fern/types/dbv0037account_info.py",
        "src/fern/types/dbv0037account_response.py",
        "src/fern/types/dbv0037association.py",
        "src/fern/types/dbv0037association_default.py",
        "src/fern/types/dbv0037association_max.py",
        "src/fern/types/dbv0037association_max_jobs.py",
        "src/fern/types/dbv0037association_max_jobs_per.py",
        "src/fern/types/dbv0037association_max_per.py",
        "src/fern/types/dbv0037association_max_per_account.py",
        "src/fern/types/dbv0037association_max_tres.py",
        "src/fern/types/dbv0037association_max_tres_minutes.py",
        "src/fern/types/dbv0037association_max_tres_minutes_per.py",
        "src/fern/types/dbv0037association_max_tres_minutes_per_job_item.py",
        "src/fern/types/dbv0037association_max_tres_minutes_total_item.py",
        "src/fern/types/dbv0037association_max_tres_per.py",
        "src/fern/types/dbv0037association_max_tres_per_job_item.py",
        "src/fern/types/dbv0037association_max_tres_per_node_item.py",
        "src/fern/types/dbv0037association_max_tres_total_item.py",
        "src/fern/types/dbv0037association_min.py",
        "src/fern/types/dbv0037association_short_info.py",
        "src/fern/types/dbv0037association_usage.py",
        "src/fern/types/dbv0037associations_info.py",
        "src/fern/types/dbv0037cluster_info.py",
        "src/fern/types/dbv0037cluster_info_associations.py",
        "src/fern/types/dbv0037cluster_info_controller.py",
        "src/fern/types/dbv0037config_info.py",
        "src/fern/types/dbv0037config_response.py",
        "src/fern/types/dbv0037coordinator_info.py",
        "src/fern/types/dbv0037diag.py",
        "src/fern/types/dbv0037diag_statistics.py",
        "src/fern/types/dbv0037diag_statistics_rollups.py",
        "src/fern/types/dbv0037diag_statistics_rp_cs.py",
        "src/fern/types/dbv0037diag_statistics_time.py",
        "src/fern/types/dbv0037diag_statistics_time1.py",
        "src/fern/types/dbv0037diag_statistics_users.py",
        "src/fern/types/dbv0037error.py",
        "src/fern/types/dbv0037job.py",
        "src/fern/types/dbv0037job_array.py",
        "src/fern/types/dbv0037job_array_limits.py",
        "src/fern/types/dbv0037job_array_limits_max.py",
        "src/fern/types/dbv0037job_array_limits_max_running.py",
        "src/fern/types/dbv0037job_comment.py",
        "src/fern/types/dbv0037job_exit_code.py",
        "src/fern/types/dbv0037job_exit_code_signal.py",
        "src/fern/types/dbv0037job_het.py",
        "src/fern/types/dbv0037job_info.py",
        "src/fern/types/dbv0037job_mcs.py",
        "src/fern/types/dbv0037job_required.py",
        "src/fern/types/dbv0037job_reservation.py",
        "src/fern/types/dbv0037job_state.py",
        "src/fern/types/dbv0037job_step.py",
        "src/fern/types/dbv0037job_step_cpu.py",
        "src/fern/types/dbv0037job_step_cpu_requested_frequency.py",
        "src/fern/types/dbv0037job_step_nodes.py",
        "src/fern/types/dbv0037job_step_statistics.py",
        "src/fern/types/dbv0037job_step_statistics_cpu.py",
        "src/fern/types/dbv0037job_step_statistics_energy.py",
        "src/fern/types/dbv0037job_step_step.py",
        "src/fern/types/dbv0037job_step_step_het.py",
        "src/fern/types/dbv0037job_step_step_task.py",
        "src/fern/types/dbv0037job_step_step_tres.py",
        "src/fern/types/dbv0037job_step_step_tres_allocated_item.py",
        "src/fern/types/dbv0037job_step_step_tres_requested.py",
        "src/fern/types/dbv0037job_step_step_tres_requested_average_item.py",
        "src/fern/types/dbv0037job_step_step_tres_requested_max_item.py",
        "src/fern/types/dbv0037job_step_step_tres_requested_min_item.py",
        "src/fern/types/dbv0037job_step_step_tres_requested_total_item.py",
        "src/fern/types/dbv0037job_step_tasks.py",
        "src/fern/types/dbv0037job_step_time.py",
        "src/fern/types/dbv0037job_time.py",
        "src/fern/types/dbv0037job_time_system.py",
        "src/fern/types/dbv0037job_time_total.py",
        "src/fern/types/dbv0037job_time_user.py",
        "src/fern/types/dbv0037job_tres.py",
        "src/fern/types/dbv0037job_tres_allocated_item.py",
        "src/fern/types/dbv0037job_tres_requested_item.py",
        "src/fern/types/dbv0037job_wckey.py",
        "src/fern/types/dbv0037qos.py",
        "src/fern/types/dbv0037qos_info.py",
        "src/fern/types/dbv0037qos_limits.py",
        "src/fern/types/dbv0037qos_limits_max.py",
        "src/fern/types/dbv0037qos_limits_max_accruing.py",
        "src/fern/types/dbv0037qos_limits_max_accruing_per.py",
        "src/fern/types/dbv0037qos_limits_max_jobs.py",
        "src/fern/types/dbv0037qos_limits_max_jobs_per.py",
        "src/fern/types/dbv0037qos_limits_max_tres.py",
        "src/fern/types/dbv0037qos_limits_max_tres_minutes.py",
        "src/fern/types/dbv0037qos_limits_max_tres_minutes_per.py",
        "src/fern/types/dbv0037qos_limits_max_tres_minutes_per_account_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_minutes_per_job_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_minutes_per_user_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_per.py",
        "src/fern/types/dbv0037qos_limits_max_tres_per_account_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_per_job_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_per_node_item.py",
        "src/fern/types/dbv0037qos_limits_max_tres_per_user_item.py",
        "src/fern/types/dbv0037qos_limits_max_wall_clock.py",
        "src/fern/types/dbv0037qos_limits_max_wall_clock_per.py",
        "src/fern/types/dbv0037qos_limits_min.py",
        "src/fern/types/dbv0037qos_limits_min_tres.py",
        "src/fern/types/dbv0037qos_limits_min_tres_per.py",
        "src/fern/types/dbv0037qos_limits_min_tres_per_job_item.py",
        "src/fern/types/dbv0037qos_preempt.py",
        "src/fern/types/dbv0037response_account_delete.py",
        "src/fern/types/dbv0037response_association_delete.py",
        "src/fern/types/dbv0037response_cluster_add.py",
        "src/fern/types/dbv0037response_cluster_delete.py",
        "src/fern/types/dbv0037response_qos_delete.py",
        "src/fern/types/dbv0037response_tres.py",
        "src/fern/types/dbv0037response_user_delete.py",
        "src/fern/types/dbv0037response_user_update.py",
        "src/fern/types/dbv0037response_wckey_add.py",
        "src/fern/types/dbv0037response_wckey_delete.py",
        "src/fern/types/dbv0037tres_info.py",
        "src/fern/types/dbv0037tres_list.py",
        "src/fern/types/dbv0037tres_list_item.py",
        "src/fern/types/dbv0037user.py",
        "src/fern/types/dbv0037user_associations.py",
        "src/fern/types/dbv0037user_default.py",
        "src/fern/types/dbv0037user_info.py",
        "src/fern/types/dbv0037wckey.py",
        "src/fern/types/dbv0037wckey_info.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `nimisampo`: the deployed NameSampo API carries JSON in a parameter-level
/// `content` object and exercises `allowReserved`. Fern accepts the raw spec.
const NIMISAMPO: Corpus = Corpus {
    api: "nimisampo",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "requirements.txt",
        "reference.md",
        "src/fern/_default_clients.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/py.typed",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/raw_client.py",
        "src/fern/types/get_full_text_search_response.py",
        "src/fern/types/post_faceted_search_result_class_count_response.py",
        "src/fern/types/post_faceted_search_result_class_paginated_response.py",
        "src/fern/types/post_result_class_page_uri_response.py",
        "src/fern/types/__init__.py",
        "src/fern/types/post_faceted_search_facet_class_facet_id_response.py",
        "src/fern/types/post_faceted_search_facet_class_facet_id_response_data.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `free5gc-pdu-session`: free5GC's PDU Session API exercises multipart
/// properties with both a content type and per-part headers.
const FREE5GC_PDU_SESSION: Corpus = Corpus {
    api: "free5gc-pdu-session",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/_default_clients.py",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/content_too_large_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/gateway_timeout_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/length_required_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/service_unavailable_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/errors/unsupported_media_type_error.py",
        "src/fern/individual_pdu_session_h_smf/__init__.py",
        "src/fern/individual_pdu_session_h_smf/client.py",
        "src/fern/individual_pdu_session_h_smf/raw_client.py",
        "src/fern/individual_sm_context/__init__.py",
        "src/fern/individual_sm_context/client.py",
        "src/fern/individual_sm_context/raw_client.py",
        "src/fern/pdu_sessions_collection/__init__.py",
        "src/fern/pdu_sessions_collection/client.py",
        "src/fern/pdu_sessions_collection/raw_client.py",
        "src/fern/py.typed",
        "src/fern/sm_contexts_collection/__init__.py",
        "src/fern/sm_contexts_collection/client.py",
        "src/fern/sm_contexts_collection/raw_client.py",
        "src/fern/types/access_type.py",
        "src/fern/types/additional_qos_flow_info.py",
        "src/fern/types/__init__.py",
        "src/fern/types/ambr.py",
        "src/fern/types/amf_id.py",
        "src/fern/types/amf_name.py",
        "src/fern/types/arp.py",
        "src/fern/types/arp_priority_level.py",
        "src/fern/types/aver_window.py",
        "src/fern/types/backup_amf_info.py",
        "src/fern/types/bit_rate.py",
        "src/fern/types/bytes.py",
        "src/fern/types/cause.py",
        "src/fern/types/date_time.py",
        "src/fern/types/dnn.py",
        "src/fern/types/dnn_selection_mode.py",
        "src/fern/types/duration_sec.py",
        "src/fern/types/dynamic5qi.py",
        "src/fern/types/ebi_arp_mapping.py",
        "src/fern/types/ecgi.py",
        "src/fern/types/eps_bearer_container.py",
        "src/fern/types/eps_bearer_id.py",
        "src/fern/types/eps_bearer_info.py",
        "src/fern/types/eps_interworking_indication.py",
        "src/fern/types/eps_pdn_cnx_container.py",
        "src/fern/types/eps_pdn_cnx_info.py",
        "src/fern/types/eutra_cell_id.py",
        "src/fern/types/eutra_location.py",
        "src/fern/types/g_nb_id.py",
        "src/fern/types/five_g_mm_cause.py",
        "src/fern/types/five_qi.py",
        "src/fern/types/five_qi_priority_level.py",
        "src/fern/types/gbr_qos_flow_information.py",
        "src/fern/types/global_ran_node_id.py",
        "src/fern/types/gpsi.py",
        "src/fern/types/guami.py",
        "src/fern/types/ho_state.py",
        "src/fern/types/hsmf_update_data.py",
        "src/fern/types/hsmf_update_error.py",
        "src/fern/types/ipv6addr.py",
        "src/fern/types/ipv6prefix.py",
        "src/fern/types/hsmf_updated_data.py",
        "src/fern/types/int64.py",
        "src/fern/types/invalid_param.py",
        "src/fern/types/ipv4addr.py",
        "src/fern/types/max_data_burst_vol.py",
        "src/fern/types/max_integrity_protected_data_rate.py",
        "src/fern/types/mcc.py",
        "src/fern/types/mme_capabilities.py",
        "src/fern/types/mnc.py",
        "src/fern/types/n2sm_info_type.py",
        "src/fern/types/n3ga_location.py",
        "src/fern/types/n3iwf_id.py",
        "src/fern/types/ncgi.py",
        "src/fern/types/nf_group_id.py",
        "src/fern/types/nf_instance_id.py",
        "src/fern/types/ng_ap_cause.py",
        "src/fern/types/nge_nb_id.py",
        "src/fern/types/non_dynamic5qi.py",
        "src/fern/types/notification_cause.py",
        "src/fern/types/notification_control.py",
        "src/fern/types/nr_cell_id.py",
        "src/fern/types/nr_location.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/packet_del_budget.py",
        "src/fern/types/packet_err_rate.py",
        "src/fern/types/packet_loss_rate.py",
        "src/fern/types/partial_record_method.py",
        "src/fern/types/pdu_session_create_data.py",
        "src/fern/types/pdu_session_create_error.py",
        "src/fern/types/pdu_session_created_data.py",
        "src/fern/types/pdu_session_id.py",
        "src/fern/types/pdu_session_notify_item.py",
        "src/fern/types/pdu_session_type.py",
        "src/fern/types/pei.py",
        "src/fern/types/plmn_id.py",
        "src/fern/types/post_pdu_sessions_request_body.py",
        "src/fern/types/post_pdu_sessions_response201.py",
        "src/fern/types/post_pdu_sessions_response400.py",
        "src/fern/types/post_sm_contexts_response201.py",
        "src/fern/types/post_sm_contexts_response400.py",
        "src/fern/types/post_sm_contexts_response403.py",
        "src/fern/types/post_sm_contexts_response404.py",
        "src/fern/types/post_sm_contexts_response500.py",
        "src/fern/types/post_sm_contexts_response503.py",
        "src/fern/types/post_sm_contexts_response504.py",
        "src/fern/types/preemption_capability.py",
        "src/fern/types/preemption_vulnerability.py",
        "src/fern/types/presence_state.py",
        "src/fern/types/problem_details.py",
        "src/fern/types/procedure_transaction_id.py",
        "src/fern/types/qfi.py",
        "src/fern/types/qos_flow_add_modify_request_item.py",
        "src/fern/types/qos_flow_item.py",
        "src/fern/types/qos_flow_notify_item.py",
        "src/fern/types/qos_flow_profile.py",
        "src/fern/types/qos_flow_release_request_item.py",
        "src/fern/types/qos_flow_setup_item.py",
        "src/fern/types/qos_flow_usage_report.py",
        "src/fern/types/qos_resource_type.py",
        "src/fern/types/rat_type.py",
        "src/fern/types/ref_to_binary_data.py",
        "src/fern/types/reflective_qo_s_attribute.py",
        "src/fern/types/release_sm_context_request_body.py",
        "src/fern/types/released_data.py",
        "src/fern/types/request_indication.py",
        "src/fern/types/request_type.py",
        "src/fern/types/resource_status.py",
        "src/fern/types/roaming_charging_profile.py",
        "src/fern/types/secondary_rat_usage_report.py",
        "src/fern/types/service_name.py",
        "src/fern/types/sm_context_create_data.py",
        "src/fern/types/sm_context_create_error.py",
        "src/fern/types/sm_context_created_data.py",
        "src/fern/types/sm_context_release_data.py",
        "src/fern/types/sm_context_retrieved_data.py",
        "src/fern/types/sm_context_status_notification.py",
        "src/fern/types/sm_context_update_data.py",
        "src/fern/types/sm_context_update_error.py",
        "src/fern/types/sm_context_updated_data.py",
        "src/fern/types/snssai.py",
        "src/fern/types/status_info.py",
        "src/fern/types/status_notification.py",
        "src/fern/types/supi.py",
        "src/fern/types/supported_features.py",
        "src/fern/types/tac.py",
        "src/fern/types/tai.py",
        "src/fern/types/teid.py",
        "src/fern/types/time_zone.py",
        "src/fern/types/trace_data.py",
        "src/fern/types/trace_depth.py",
        "src/fern/types/trigger.py",
        "src/fern/types/trigger_category.py",
        "src/fern/types/trigger_type.py",
        "src/fern/types/tunnel_info.py",
        "src/fern/types/uint32.py",
        "src/fern/types/uinteger.py",
        "src/fern/types/up_cnx_state.py",
        "src/fern/types/up_confidentiality.py",
        "src/fern/types/up_integrity.py",
        "src/fern/types/up_security.py",
        "src/fern/types/update_pdu_session_request_body.py",
        "src/fern/types/update_pdu_session_response200.py",
        "src/fern/types/update_pdu_session_response400.py",
        "src/fern/types/update_sm_context_request_body.py",
        "src/fern/types/update_sm_context_response200.py",
        "src/fern/types/update_sm_context_response400.py",
        "src/fern/types/update_sm_context_response403.py",
        "src/fern/types/update_sm_context_response404.py",
        "src/fern/types/update_sm_context_response500.py",
        "src/fern/types/update_sm_context_response503.py",
        "src/fern/types/uri.py",
        "src/fern/types/user_location.py",
        "src/fern/types/vsmf_update_data.py",
        "src/fern/types/vsmf_update_error.py",
        "src/fern/types/vsmf_updated_data.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
    ],
};

/// `sigstore-rekor`: Rekor combines ranged/default responses, implicit
/// discriminators, and nested models with request- and response-only fields.
const SIGSTORE_REKOR: Corpus = Corpus {
    api: "sigstore-rekor",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/_default_clients.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/entries/__init__.py",
        "src/fern/environment.py",
        "src/fern/index/__init__.py",
        "src/fern/index/types/__init__.py",
        "src/fern/index/types/search_index_operator.py",
        "src/fern/index/types/search_index_public_key.py",
        "src/fern/index/types/search_index_public_key_format.py",
        "src/fern/pubkey/__init__.py",
        "src/fern/pubkey/client.py",
        "src/fern/pubkey/raw_client.py",
        "src/fern/py.typed",
        "src/fern/tlog/__init__.py",
        "src/fern/types/alpine.py",
        "src/fern/types/consistency_proof.py",
        "src/fern/types/cose.py",
        "src/fern/types/dsse.py",
        "src/fern/types/error.py",
        "src/fern/types/hashedrekord.py",
        "src/fern/types/helm.py",
        "src/fern/types/inactive_shard_log_info.py",
        "src/fern/types/inclusion_proof.py",
        "src/fern/types/intoto.py",
        "src/fern/types/intoto_schema_public_key.py",
        "src/fern/types/intoto_schema_public_key_content.py",
        "src/fern/types/intoto_schema_public_key_content_hash.py",
        "src/fern/types/intoto_schema_public_key_content_hash_algorithm.py",
        "src/fern/types/intoto_schema_public_key_content_payload_hash.py",
        "src/fern/types/intoto_schema_public_key_content_payload_hash_algorithm.py",
        "src/fern/types/jar.py",
        "src/fern/types/log_info.py",
        "src/fern/types/proposed_entry.py",
        "src/fern/types/rekord.py",
        "src/fern/types/rfc3161.py",
        "src/fern/types/rpm.py",
        "src/fern/types/tuf.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
        "src/fern/types/alpine_package_schema.py",
        "src/fern/types/alpine_package_schema_package_hash.py",
        "src/fern/types/alpine_package_schema_package_hash_algorithm.py",
        "src/fern/types/alpine_package_schema_public_key.py",
        "src/fern/types/cose_schema.py",
        "src/fern/types/cose_schema_data.py",
        "src/fern/types/cose_schema_data_envelope_hash.py",
        "src/fern/types/cose_schema_data_envelope_hash_algorithm.py",
        "src/fern/types/cose_schema_data_payload_hash.py",
        "src/fern/types/cose_schema_data_payload_hash_algorithm.py",
        "src/fern/types/dsse_schema_envelope_hash.py",
        "src/fern/types/dsse_schema_envelope_hash_algorithm.py",
        "src/fern/types/dsse_schema_payload_hash.py",
        "src/fern/types/dsse_schema_payload_hash_algorithm.py",
        "src/fern/types/dsse_schema_proposed_content.py",
        "src/fern/types/dsse_schema_signatures_item.py",
        "src/fern/types/hashedrekord_schema.py",
        "src/fern/types/hashedrekord_schema_data.py",
        "src/fern/types/hashedrekord_schema_data_hash.py",
        "src/fern/types/hashedrekord_schema_data_hash_algorithm.py",
        "src/fern/types/hashedrekord_schema_signature.py",
        "src/fern/types/hashedrekord_schema_signature_public_key.py",
        "src/fern/types/helm_schema.py",
        "src/fern/types/helm_schema_chart.py",
        "src/fern/types/helm_schema_chart_hash.py",
        "src/fern/types/helm_schema_chart_hash_algorithm.py",
        "src/fern/types/helm_schema_chart_provenance_signature.py",
        "src/fern/types/helm_schema_public_key.py",
        "src/fern/types/jar_schema.py",
        "src/fern/types/jar_schema_archive_hash.py",
        "src/fern/types/jar_schema_archive_hash_algorithm.py",
        "src/fern/types/jar_schema_signature.py",
        "src/fern/types/jar_schema_signature_public_key.py",
        "src/fern/types/rekor_schema.py",
        "src/fern/types/rekor_schema_data_hash.py",
        "src/fern/types/rekor_schema_data_hash_algorithm.py",
        "src/fern/types/rekor_schema_signature.py",
        "src/fern/types/rekor_schema_signature_format.py",
        "src/fern/types/rekor_schema_signature_public_key.py",
        "src/fern/types/rpm_schema.py",
        "src/fern/types/rpm_schema_package_hash.py",
        "src/fern/types/rpm_schema_package_hash_algorithm.py",
        "src/fern/types/rpm_schema_public_key.py",
        "src/fern/types/timestamp_schema.py",
        "src/fern/types/timestamp_schema_tsr.py",
        "src/fern/types/tuf_schema.py",
        "src/fern/types/tuf_schema_metadata.py",
        "src/fern/types/tuf_schema_root.py",
        "src/fern/__init__.py",
        "src/fern/types/__init__.py",
        "src/fern/types/alpine_package_schema_package.py",
        "src/fern/types/dsse_schema.py",
        "src/fern/types/helm_schema_chart_provenance.py",
        "src/fern/types/intoto_schema.py",
        "src/fern/types/intoto_schema_one.py",
        "src/fern/types/intoto_schema_one_content.py",
        "src/fern/types/intoto_schema_one_content_envelope.py",
        "src/fern/types/intoto_schema_one_content_envelope_signatures_item.py",
        "src/fern/types/intoto_schema_one_content_hash.py",
        "src/fern/types/intoto_schema_one_content_hash_algorithm.py",
        "src/fern/types/intoto_schema_one_content_payload_hash.py",
        "src/fern/types/intoto_schema_one_content_payload_hash_algorithm.py",
        "src/fern/types/jar_schema_archive.py",
        "src/fern/types/log_entry.py",
        "src/fern/types/log_entry_value.py",
        "src/fern/types/log_entry_value_attestation.py",
        "src/fern/types/log_entry_value_verification.py",
        "src/fern/types/rekor_schema_data.py",
        "src/fern/types/rpm_schema_package.py",
        "reference.md",
        "src/fern/entries/client.py",
        "src/fern/entries/raw_client.py",
        "src/fern/index/client.py",
        "src/fern/index/raw_client.py",
        "src/fern/tlog/client.py",
        "src/fern/tlog/raw_client.py",
    ],
};

/// `letta`: Letta's agent API combines SSE responses, implicit discriminators,
/// deeply nested unions, and a map whose values are a union.
const LETTA: Corpus = Corpus {
    api: "letta",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "pyproject.toml",
        "requirements.txt",
        "src/fern/_default_clients.py",
        "src/fern/agents/types/agents_get_agent_variables_response.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_combinator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_agent_id.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_agent_id_operator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_identity.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_identity_operator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_name.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_name_operator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_tags.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_tags_operator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_template_name.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_template_name_operator.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_search_item_version.py",
        "src/fern/agents/types/agents_search_deployed_agents_request_sort_by.py",
        "src/fern/agents/types/agents_search_deployed_agents_response.py",
        "src/fern/agents/types/list_agent_sources_request_order.py",
        "src/fern/agents/types/list_agent_sources_request_order_by.py",
        "src/fern/agents/types/list_agents_request_include_item.py",
        "src/fern/agents/types/list_agents_request_order.py",
        "src/fern/agents/types/list_agents_request_order_by.py",
        "src/fern/agents/types/list_core_memory_blocks_request_order.py",
        "src/fern/agents/types/list_core_memory_blocks_request_order_by.py",
        "src/fern/agents/types/list_files_for_agent_request_order.py",
        "src/fern/agents/types/list_files_for_agent_request_order_by.py",
        "src/fern/agents/types/list_folders_for_agent_request_order.py",
        "src/fern/agents/types/list_folders_for_agent_request_order_by.py",
        "src/fern/agents/types/list_groups_for_agent_request_order.py",
        "src/fern/agents/types/list_groups_for_agent_request_order_by.py",
        "src/fern/agents/types/list_messages_request_order.py",
        "src/fern/agents/types/list_messages_request_order_by.py",
        "src/fern/agents/types/list_tools_for_agent_request_order.py",
        "src/fern/agents/types/list_tools_for_agent_request_order_by.py",
        "src/fern/agents/types/message_search_request_search_mode.py",
        "src/fern/agents/types/preview_model_request_request_body.py",
        "src/fern/agents/types/retrieve_agent_request_include_item.py",
        "src/fern/agents/types/search_archival_memory_request_tag_match_mode.py",
        "src/fern/archives/types/list_agents_for_archive_request_include_item.py",
        "src/fern/archives/types/list_agents_for_archive_request_order.py",
        "src/fern/archives/types/list_archives_request_order.py",
        "src/fern/archives/types/list_archives_request_order_by.py",
        "src/fern/blocks/__init__.py",
        "src/fern/blocks/types/__init__.py",
        "src/fern/blocks/types/list_agents_for_block_request_include_item.py",
        "src/fern/blocks/types/list_agents_for_block_request_order.py",
        "src/fern/blocks/types/list_agents_for_block_request_order_by.py",
        "src/fern/blocks/types/list_blocks_request_order.py",
        "src/fern/blocks/types/list_blocks_request_order_by.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response_policy.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response_policy_version.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_version.py",
        "src/fern/conversations/types/list_conversation_messages_request_order.py",
        "src/fern/conversations/types/list_conversation_messages_request_order_by.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/embeddings/__init__.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/gone_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/payment_required_error.py",
        "src/fern/errors/unprocessable_entity_error.py",
        "src/fern/feeds/types/feeds_backfill_subscription_response.py",
        "src/fern/feeds/types/feeds_create_feed_response.py",
        "src/fern/feeds/types/feeds_delete_feed_response.py",
        "src/fern/feeds/types/feeds_delete_subscription_response.py",
        "src/fern/feeds/types/feeds_get_feed_response.py",
        "src/fern/feeds/types/feeds_get_message_response.py",
        "src/fern/feeds/types/feeds_get_message_response_message.py",
        "src/fern/feeds/types/feeds_list_feeds_response.py",
        "src/fern/feeds/types/feeds_list_feeds_response_feeds_item.py",
        "src/fern/feeds/types/feeds_list_messages_response.py",
        "src/fern/feeds/types/feeds_list_messages_response_messages_item.py",
        "src/fern/feeds/types/feeds_list_subscription_history_response.py",
        "src/fern/feeds/types/feeds_list_subscription_history_response_runs_item.py",
        "src/fern/feeds/types/feeds_list_subscription_history_response_runs_item_status.py",
        "src/fern/feeds/types/feeds_list_subscription_history_response_runs_item_type.py",
        "src/fern/feeds/types/feeds_list_subscriptions_response.py",
        "src/fern/feeds/types/feeds_list_subscriptions_response_subscriptions_item.py",
        "src/fern/feeds/types/feeds_list_subscriptions_response_subscriptions_item_merge_strategy.py",
        "src/fern/feeds/types/feeds_publish_messages_request_messages_item.py",
        "src/fern/feeds/types/feeds_publish_messages_response.py",
        "src/fern/feeds/types/feeds_subscribe_agent_response.py",
        "src/fern/feeds/types/feeds_subscribe_agent_response_merge_strategy.py",
        "src/fern/feeds/types/feeds_trigger_subscription_response.py",
        "src/fern/feeds/types/feeds_unsubscribe_agent_response.py",
        "src/fern/feeds/types/feeds_update_all_subscriptions_cron_response.py",
        "src/fern/feeds/types/feeds_update_subscription_response.py",
        "src/fern/feeds/types/feeds_update_subscription_response_merge_strategy.py",
        "src/fern/folders/__init__.py",
        "src/fern/folders/types/__init__.py",
        "src/fern/folders/types/list_agents_for_folder_request_order.py",
        "src/fern/folders/types/list_agents_for_folder_request_order_by.py",
        "src/fern/folders/types/list_files_for_folder_request_order.py",
        "src/fern/folders/types/list_files_for_folder_request_order_by.py",
        "src/fern/folders/types/list_folder_passages_request_order.py",
        "src/fern/folders/types/list_folder_passages_request_order_by.py",
        "src/fern/folders/types/list_folders_request_order.py",
        "src/fern/folders/types/list_folders_request_order_by.py",
        "src/fern/groups/types/list_group_messages_request_order.py",
        "src/fern/groups/types/list_group_messages_request_order_by.py",
        "src/fern/groups/types/list_groups_request_order.py",
        "src/fern/groups/types/list_groups_request_order_by.py",
        "src/fern/health/__init__.py",
        "src/fern/health/client.py",
        "src/fern/health/raw_client.py",
        "src/fern/identities/types/list_agents_for_identity_request_include_item.py",
        "src/fern/identities/types/list_agents_for_identity_request_order.py",
        "src/fern/identities/types/list_agents_for_identity_request_order_by.py",
        "src/fern/identities/types/list_blocks_for_identity_request_order.py",
        "src/fern/identities/types/list_blocks_for_identity_request_order_by.py",
        "src/fern/identities/types/list_identities_request_order.py",
        "src/fern/identities/types/list_identities_request_order_by.py",
        "src/fern/internal_agents/__init__.py",
        "src/fern/internal_blocks/__init__.py",
        "src/fern/internal_blocks/types/__init__.py",
        "src/fern/internal_blocks/types/list_agents_for_internal_block_request_order.py",
        "src/fern/internal_blocks/types/list_agents_for_internal_block_request_order_by.py",
        "src/fern/internal_blocks/types/list_internal_blocks_request_order.py",
        "src/fern/internal_blocks/types/list_internal_blocks_request_order_by.py",
        "src/fern/internal_runs/types/list_internal_runs_request_order.py",
        "src/fern/internal_runs/types/list_internal_runs_request_order_by.py",
        "src/fern/jobs/__init__.py",
        "src/fern/jobs/types/__init__.py",
        "src/fern/jobs/types/list_jobs_request_order.py",
        "src/fern/jobs/types/list_jobs_request_order_by.py",
        "src/fern/messages/types/list_all_messages_request_order.py",
        "src/fern/messages/types/list_batches_request_order.py",
        "src/fern/messages/types/list_batches_request_order_by.py",
        "src/fern/messages/types/list_messages_for_batch_request_order.py",
        "src/fern/messages/types/list_messages_for_batch_request_order_by.py",
        "src/fern/messages/types/search_all_messages_request_search_mode.py",
        "src/fern/metadata/raw_client.py",
        "src/fern/metadata/types/metadata_get_status_response.py",
        "src/fern/metadata/types/metadata_get_user_response.py",
        "src/fern/metadata/types/metadata_retrieve_current_balances_response.py",
        "src/fern/metadata/types/metadata_send_feedback_request_feature.py",
        "src/fern/metadata/types/metadata_send_feedback_response.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_service.py",
        "src/fern/metadata/types/metadata_send_telemetry_response.py",
        "src/fern/models/__init__.py",
        "src/fern/passages/types/passage_search_request_tag_match_mode.py",
        "src/fern/pipelines/types/pipelines_count_pipelines_response.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_request_integration_type.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline_integration_type.py",
        "src/fern/pipelines/types/pipelines_delete_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline_integration_type.py",
        "src/fern/pipelines/types/pipelines_list_pipeline_sync_history_response.py",
        "src/fern/pipelines/types/pipelines_list_pipeline_sync_history_response_runs_item.py",
        "src/fern/pipelines/types/pipelines_list_pipeline_sync_history_response_runs_item_error.py",
        "src/fern/pipelines/types/pipelines_list_pipeline_sync_history_response_runs_item_status.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item_integration_type.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_request_integration_type.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_sync_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline_integration_type.py",
        "src/fern/projects/__init__.py",
        "src/fern/projects/types/__init__.py",
        "src/fern/projects/types/projects_create_project_response.py",
        "src/fern/projects/types/projects_delete_project_response.py",
        "src/fern/projects/types/projects_list_projects_response.py",
        "src/fern/projects/types/projects_list_projects_response_projects_item.py",
        "src/fern/providers/types/list_providers_request_order.py",
        "src/fern/providers/types/list_providers_request_order_by.py",
        "src/fern/py.typed",
        "src/fern/runs/__init__.py",
        "src/fern/runs/types/__init__.py",
        "src/fern/runs/types/list_messages_for_run_request_order.py",
        "src/fern/runs/types/list_messages_for_run_request_order_by.py",
        "src/fern/runs/types/list_runs_request_order.py",
        "src/fern/runs/types/list_runs_request_order_by.py",
        "src/fern/runs/types/list_steps_for_run_request_order.py",
        "src/fern/runs/types/list_steps_for_run_request_order_by.py",
        "src/fern/scheduled_messages/types/scheduled_messages_delete_scheduled_message_response.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_role.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_role.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_role.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_response.py",
        "src/fern/sources/__init__.py",
        "src/fern/steps/types/list_messages_for_step_request_order.py",
        "src/fern/steps/types/list_messages_for_step_request_order_by.py",
        "src/fern/steps/types/list_steps_request_order.py",
        "src/fern/steps/types/list_steps_request_order_by.py",
        "src/fern/tag/__init__.py",
        "src/fern/tag/types/__init__.py",
        "src/fern/tag/types/list_tags_request_order.py",
        "src/fern/tag/types/list_tags_request_order_by.py",
        "src/fern/templates/types/templates_create_agents_from_template_no_project_request_initial_message_sequence_item.py",
        "src/fern/templates/types/templates_create_agents_from_template_no_project_request_initial_message_sequence_item_role.py",
        "src/fern/templates/types/templates_create_agents_from_template_no_project_response.py",
        "src/fern/templates/types/templates_create_agents_from_template_request_initial_message_sequence_item.py",
        "src/fern/templates/types/templates_create_agents_from_template_request_initial_message_sequence_item_role.py",
        "src/fern/templates/types/templates_create_template_no_project_response.py",
        "src/fern/templates/types/templates_create_template_response.py",
        "src/fern/templates/types/templates_delete_template_no_project_response.py",
        "src/fern/templates/types/templates_delete_template_response.py",
        "src/fern/templates/types/templates_fork_template_response.py",
        "src/fern/templates/types/templates_get_template_snapshot_response.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_agent_type.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_memory_variables.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_memory_variables_data_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_properties.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_properties_reasoning_effort.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_properties_verbosity_level.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_variables.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_variables_data_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_blocks_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_configuration.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_relationships_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_type.py",
        "src/fern/templates/types/templates_legacy_migration_response.py",
        "src/fern/templates/types/templates_list_template_versions_response.py",
        "src/fern/templates/types/templates_list_template_versions_response_versions_item.py",
        "src/fern/templates/types/templates_list_templates_request_sort_by.py",
        "src/fern/templates/types/templates_list_templates_response.py",
        "src/fern/templates/types/templates_list_templates_response_templates_item.py",
        "src/fern/templates/types/templates_migrate_deployment_response.py",
        "src/fern/templates/types/templates_rename_template_response.py",
        "src/fern/templates/types/templates_save_template_version_request_block_reconciliation_strategy.py",
        "src/fern/templates/types/templates_save_template_version_response.py",
        "src/fern/templates/types/templates_set_current_template_from_snapshot_response.py",
        "src/fern/templates/types/templates_update_current_template_from_agent_file_no_project_response.py",
        "src/fern/templates/types/templates_update_current_template_from_agent_file_response.py",
        "src/fern/templates/types/templates_update_template_description_response.py",
        "src/fern/tools/types/add_mcp_server_request.py",
        "src/fern/tools/types/add_mcp_server_response_item.py",
        "src/fern/tools/types/connect_mcp_server_request.py",
        "src/fern/tools/types/delete_mcp_server_response_item.py",
        "src/fern/tools/types/list_tools_request_order.py",
        "src/fern/tools/types/list_tools_request_order_by.py",
        "src/fern/tools/types/test_mcp_server_request.py",
        "src/fern/tools/types/tool_search_request_search_mode.py",
        "src/fern/tools/types/update_mcp_server_request_body.py",
        "src/fern/tools/types/update_mcp_server_response.py",
        "src/fern/types/agent_type.py",
        "src/fern/types/annotation.py",
        "src/fern/types/annotation_type.py",
        "src/fern/types/annotation_url_citation.py",
        "src/fern/types/anthropic_model_settings.py",
        "src/fern/types/anthropic_thinking.py",
        "src/fern/types/anthropic_thinking_type.py",
        "src/fern/types/approval_create_type.py",
        "src/fern/types/approval_request_message_tool_call.py",
        "src/fern/types/archival_memory_search_response.py",
        "src/fern/types/archival_memory_search_result.py",
        "src/fern/types/assistant_message_content.py",
        "src/fern/types/assistant_message_list_result_content.py",
        "src/fern/types/audio.py",
        "src/fern/types/auth_request.py",
        "src/fern/types/azure_model_settings.py",
        "src/fern/types/base_tool_rule_schema.py",
        "src/fern/types/bedrock_model_settings.py",
        "src/fern/types/chat_completion_audio.py",
        "src/fern/types/chat_completion_content_part_text_param.py",
        "src/fern/types/chat_completion_content_part_text_param_type.py",
        "src/fern/types/chat_completion_developer_message_param_content.py",
        "src/fern/types/chat_completion_message_function_tool_call_input.py",
        "src/fern/types/chat_completion_message_function_tool_call_input_type.py",
        "src/fern/types/chat_completion_message_function_tool_call_output.py",
        "src/fern/types/chat_completion_message_function_tool_call_output_type.py",
        "src/fern/types/chat_completion_message_role.py",
        "src/fern/types/chat_completion_object.py",
        "src/fern/types/chat_completion_system_message_param_content.py",
        "src/fern/types/chat_completion_tool_message_param_content.py",
        "src/fern/types/chat_completion_user_message_param_content.py",
        "src/fern/types/chat_gpto_auth_model_settings.py",
        "src/fern/types/chat_gpto_auth_reasoning.py",
        "src/fern/types/chat_gpto_auth_reasoning_reasoning_effort.py",
        "src/fern/types/child_tool_rule_schema.py",
        "src/fern/types/choice.py",
        "src/fern/types/choice_finish_reason.py",
        "src/fern/types/compaction_response.py",
        "src/fern/types/compaction_settings_input_mode.py",
        "src/fern/types/compaction_settings_output_mode.py",
        "src/fern/types/comparison_operator.py",
        "src/fern/types/conflict_error_body.py",
        "src/fern/types/custom_input.py",
        "src/fern/types/custom_output.py",
        "src/fern/types/deepseek_model_settings.py",
        "src/fern/types/delete_deployment_response.py",
        "src/fern/types/duplicate_file_handling.py",
        "src/fern/types/embedding_config_embedding_endpoint_type.py",
        "src/fern/types/embedding_model_embedding_endpoint_type.py",
        "src/fern/types/embedding_model_model_type.py",
        "src/fern/types/event_message_event_type.py",
        "src/fern/types/feedback_type.py",
        "src/fern/types/file_file.py",
        "src/fern/types/file_processing_status.py",
        "src/fern/types/function_call_input.py",
        "src/fern/types/function_call_output.py",
        "src/fern/types/function_output.py",
        "src/fern/types/function_tool.py",
        "src/fern/types/function_tool_type.py",
        "src/fern/types/gemini_thinking_config.py",
        "src/fern/types/generate_tool_output.py",
        "src/fern/types/google_ai_model_settings.py",
        "src/fern/types/google_vertex_model_settings.py",
        "src/fern/types/groq_model_settings.py",
        "src/fern/types/health.py",
        "src/fern/types/hidden_reasoning_message_state.py",
        "src/fern/types/http_validation_error.py",
        "src/fern/types/identity_property.py",
        "src/fern/types/identity_property_type.py",
        "src/fern/types/identity_property_value.py",
        "src/fern/types/identity_type.py",
        "src/fern/types/image_url.py",
        "src/fern/types/image_url_detail.py",
        "src/fern/types/imported_agents_response.py",
        "src/fern/types/input_audio.py",
        "src/fern/types/input_audio_format.py",
        "src/fern/types/internal_server_error_body.py",
        "src/fern/types/job_status.py",
        "src/fern/types/job_type.py",
        "src/fern/types/json_object_response_format.py",
        "src/fern/types/json_schema_response_format.py",
        "src/fern/types/letta_batch_messages.py",
        "src/fern/types/letta_error_message.py",
        "src/fern/types/letta_response.py",
        "src/fern/types/letta_schemas_agent_file_message_schema_content.py",
        "src/fern/types/letta_schemas_letta_message_tool_return_status.py",
        "src/fern/types/letta_schemas_letta_message_tool_return_tool_return.py",
        "src/fern/types/letta_schemas_mcp_server_tool_execute_request.py",
        "src/fern/types/letta_schemas_message_tool_return_input_status.py",
        "src/fern/types/letta_schemas_message_tool_return_output_status.py",
        "src/fern/types/letta_serialize_schemas_pydantic_agent_schema_agent_schema_tool_rules_item.py",
        "src/fern/types/list_deployment_entities_response.py",
        "src/fern/types/llm_config_model_endpoint_type.py",
        "src/fern/types/manager_type.py",
        "src/fern/types/max_count_per_step_tool_rule_schema.py",
        "src/fern/types/mcp_server_type.py",
        "src/fern/types/mcp_tool_health.py",
        "src/fern/types/memory.py",
        "src/fern/types/message_create_content.py",
        "src/fern/types/message_create_role.py",
        "src/fern/types/message_role.py",
        "src/fern/types/message_type.py",
        "src/fern/types/modal_sandbox_config_language.py",
        "src/fern/types/model_model_endpoint_type.py",
        "src/fern/types/model_model_type.py",
        "src/fern/types/modify_approval_request.py",
        "src/fern/types/not_found_error_body_message.py",
        "src/fern/types/open_ai_model_settings.py",
        "src/fern/types/open_ai_reasoning.py",
        "src/fern/types/open_ai_reasoning_reasoning_effort.py",
        "src/fern/types/openai_types_chat_chat_completion_message_function_tool_call_function.py",
        "src/fern/types/openai_types_chat_chat_completion_message_function_tool_call_param_function.py",
        "src/fern/types/organization_sources_stats.py",
        "src/fern/types/passage_search_result.py",
        "src/fern/types/payment_required_error_body.py",
        "src/fern/types/provider_category.py",
        "src/fern/types/provider_type.py",
        "src/fern/types/reasoning_message_source.py",
        "src/fern/types/redacted_reasoning_content.py",
        "src/fern/types/run_status.py",
        "src/fern/types/sandbox_config_create.py",
        "src/fern/types/sandbox_config_create_config.py",
        "src/fern/types/sandbox_config_update.py",
        "src/fern/types/sandbox_config_update_config.py",
        "src/fern/types/sandbox_type.py",
        "src/fern/types/source_stats.py",
        "src/fern/types/step_status.py",
        "src/fern/types/stop_reason_type.py",
        "src/fern/types/summarized_reasoning_content.py",
        "src/fern/types/summarized_reasoning_content_part.py",
        "src/fern/types/supervisor_manager.py",
        "src/fern/types/tag_schema.py",
        "src/fern/types/text_response_format.py",
        "src/fern/types/together_model_settings.py",
        "src/fern/types/tool_call.py",
        "src/fern/types/tool_call_message_tool_call.py",
        "src/fern/types/tool_execution_result_status.py",
        "src/fern/types/tool_return_content.py",
        "src/fern/types/tool_return_message_status.py",
        "src/fern/types/tool_type.py",
        "src/fern/types/update_assistant_message_content.py",
        "src/fern/types/update_user_message_content.py",
        "src/fern/types/url_image.py",
        "src/fern/types/user_create.py",
        "src/fern/types/user_message_content.py",
        "src/fern/types/user_message_list_result_content.py",
        "src/fern/types/validation_error.py",
        "src/fern/types/validation_error_loc_item.py",
        "src/fern/types/vector_db_provider.py",
        "src/fern/types/xai_model_settings.py",
        "src/fern/types/zai_model_settings.py",
        "src/fern/version.py",
        "src/fern/voice/__init__.py",
        "src/fern/voice/client.py",
        "src/fern/voice/raw_client.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
        "src/fern/providers/__init__.py",
        "src/fern/providers/types/__init__.py",
        "src/fern/types/agent_environment_variable.py",
        "src/fern/types/agent_file_attachment.py",
        "src/fern/types/agent_file_schema.py",
        "src/fern/types/assistant_message.py",
        "src/fern/types/auth_response.py",
        "src/fern/types/base64image.py",
        "src/fern/types/code_input.py",
        "src/fern/types/compaction_settings_input.py",
        "src/fern/types/compaction_settings_output.py",
        "src/fern/types/completion_tokens_details.py",
        "src/fern/types/conditional_tool_rule.py",
        "src/fern/types/continue_tool_rule.py",
        "src/fern/types/conversation.py",
        "src/fern/types/deployment_entity.py",
        "src/fern/types/dynamic_manager.py",
        "src/fern/types/dynamic_manager_update.py",
        "src/fern/types/embedding_config.py",
        "src/fern/types/embedding_model.py",
        "src/fern/types/event_message.py",
        "src/fern/types/file_agent_schema.py",
        "src/fern/types/file_metadata.py",
        "src/fern/types/file_schema.py",
        "src/fern/types/file_stats.py",
        "src/fern/types/generate_tool_input.py",
        "src/fern/types/group.py",
        "src/fern/types/hidden_reasoning_message.py",
        "src/fern/types/identity.py",
        "src/fern/types/letta_image.py",
        "src/fern/types/letta_ping.py",
        "src/fern/types/local_sandbox_config.py",
        "src/fern/types/max_count_per_step_tool_rule.py",
        "src/fern/types/message_search_result.py",
        "src/fern/types/npm_requirement.py",
        "src/fern/types/omitted_reasoning_content.py",
        "src/fern/types/organization.py",
        "src/fern/types/organization_create.py",
        "src/fern/types/organization_update.py",
        "src/fern/types/paginated_agent_files.py",
        "src/fern/types/parameter_properties.py",
        "src/fern/types/parameters_schema.py",
        "src/fern/types/parent_tool_rule.py",
        "src/fern/types/pip_requirement.py",
        "src/fern/types/prompt_tokens_details.py",
        "src/fern/types/provider.py",
        "src/fern/types/reasoning_content.py",
        "src/fern/types/reasoning_message.py",
        "src/fern/types/required_before_exit_tool_rule.py",
        "src/fern/types/requires_approval_tool_rule.py",
        "src/fern/types/retrieve_stream_request.py",
        "src/fern/types/round_robin_manager.py",
        "src/fern/types/round_robin_manager_update.py",
        "src/fern/types/sandbox_config.py",
        "src/fern/types/sandbox_environment_variable.py",
        "src/fern/types/sandbox_environment_variable_create.py",
        "src/fern/types/sandbox_environment_variable_update.py",
        "src/fern/types/sleeptime_manager.py",
        "src/fern/types/sleeptime_manager_update.py",
        "src/fern/types/step_metrics.py",
        "src/fern/types/summary_message.py",
        "src/fern/types/system_message.py",
        "src/fern/types/terminal_tool_rule.py",
        "src/fern/types/text_content.py",
        "src/fern/types/tool_annotations.py",
        "src/fern/types/tool_call_content.py",
        "src/fern/types/tool_call_delta.py",
        "src/fern/types/tool_call_message.py",
        "src/fern/types/tool_search_result.py",
        "src/fern/types/usage_statistics_completion_token_details.py",
        "src/fern/types/usage_statistics_prompt_token_details.py",
        "src/fern/types/user.py",
        "src/fern/types/user_message.py",
        "src/fern/types/user_update.py",
        "src/fern/types/voice_sleeptime_manager.py",
        "src/fern/types/voice_sleeptime_manager_update.py",
        "src/fern/agents/types/create_agent_request_model_settings.py",
        "src/fern/agents/types/create_agent_request_response_format.py",
        "src/fern/agents/types/update_agent_model_settings.py",
        "src/fern/agents/types/update_agent_response_format.py",
        "src/fern/internal_templates/types/internal_template_agent_create_model_settings.py",
        "src/fern/internal_templates/types/internal_template_agent_create_response_format.py",
        "src/fern/types/agent_state_model_settings.py",
        "src/fern/types/agent_state_response_format.py",
        "src/fern/types/anthropic_model_settings_response_format.py",
        "src/fern/types/azure_model_settings_response_format.py",
        "src/fern/types/bedrock_model_settings_response_format.py",
        "src/fern/types/compaction_settings_input_model_settings.py",
        "src/fern/types/compaction_settings_output_model_settings.py",
        "src/fern/types/deepseek_model_settings_response_format.py",
        "src/fern/types/google_ai_model_settings_response_schema.py",
        "src/fern/types/google_vertex_model_settings_response_schema.py",
        "src/fern/types/groq_model_settings_response_format.py",
        "src/fern/types/letta_schemas_agent_file_agent_schema_model_settings.py",
        "src/fern/types/letta_schemas_agent_file_agent_schema_response_format.py",
        "src/fern/types/llm_config_response_format.py",
        "src/fern/types/model_response_format.py",
        "src/fern/types/open_ai_model_settings_response_format.py",
        "src/fern/types/together_model_settings_response_format.py",
        "src/fern/types/xai_model_settings_response_format.py",
        "src/fern/types/zai_model_settings_response_format.py",
        "src/fern/agents/types/create_agent_request_tool_rules_item.py",
        "src/fern/agents/types/letta_async_request_messages_item.py",
        "src/fern/agents/types/update_agent_tool_rules_item.py",
        "src/fern/internal_templates/types/internal_template_agent_create_tool_rules_item.py",
        "src/fern/types/agent_state_tool_rules_item.py",
        "src/fern/types/approval_create.py",
        "src/fern/types/approval_create_approvals_item.py",
        "src/fern/types/approval_response_message.py",
        "src/fern/types/approval_response_message_approvals_item.py",
        "src/fern/types/letta_batch_request_messages_item.py",
        "src/fern/types/letta_message_content_union.py",
        "src/fern/types/letta_schemas_agent_file_agent_schema_tool_rules_item.py",
        "src/fern/types/letta_schemas_agent_file_message_schema_approvals_item.py",
        "src/fern/types/letta_streaming_request_messages_item.py",
        "src/fern/types/letta_tool_return_content_union.py",
        "src/fern/types/letta_user_message_content_union.py",
        "src/fern/types/message_approvals_item.py",
        "src/fern/types/message_content_item.py",
        "src/fern/groups/types/group_create_manager_config.py",
        "src/fern/internal_templates/types/internal_template_group_create_manager_config.py",
        "src/fern/types/group_schema.py",
        "src/fern/types/group_schema_manager_config.py",
        "src/fern/types/image_content.py",
        "src/fern/types/image_content_source.py",
        "src/fern/metadata/__init__.py",
        "src/fern/metadata/types/__init__.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_error.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_error_data.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_session_end.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_session_end_data.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_session_start.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_session_start_data.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_tool_usage.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_tool_usage_data.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_user_input.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item_user_input_data.py",
        "src/fern/pipelines/__init__.py",
        "src/fern/pipelines/types/__init__.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_request_producer_config.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_request_producer_config_data.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_request_producer_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_request_producer_config_type.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline_config.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline_config_data.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_create_pipeline_response_pipeline_config_type.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline_config.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline_config_data.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_get_pipeline_response_pipeline_config_type.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item_config.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item_config_data.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_list_pipelines_response_pipelines_item_config_type.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_request_producer_config.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_request_producer_config_data.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_request_producer_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_preview_pipeline_request_producer_config_type.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline_config.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline_config_data.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline_config_data_channels_item.py",
        "src/fern/pipelines/types/pipelines_update_pipeline_response_pipeline_config_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_one_time.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_recurring.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_schedule.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_schedule_one_time.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_schedule_recurring.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_schedule.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_schedule_one_time.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_schedule_recurring.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_conditional.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_continue_loop.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_exit_loop.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_max_count_per_step.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_parent_last_tool.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_required_before_exit.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_requires_approval.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_include_return_message_types_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_include_return_message_types_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_include_return_message_types_item.py",
        "src/fern/client_side_access_tokens/__init__.py",
        "src/fern/client_side_access_tokens/types/__init__.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_request_policy_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_request_policy_item_access_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_request_policy_item_type.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response_policy_data_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response_policy_data_item_access_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_create_client_side_access_token_response_policy_data_item_type.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_access_item.py",
        "src/fern/client_side_access_tokens/types/client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_text.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_text.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source_type.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_text.py",
        "src/fern/metadata/types/metadata_send_telemetry_request_events_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item.py",
        "src/fern/scheduled_messages/types/scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item.py",
        "src/fern/internal_runs/__init__.py",
        "src/fern/internal_runs/types/__init__.py",
        "src/fern/internal_runs/types/list_internal_runs_request_duration_operator.py",
        "src/fern/pipelines/client.py",
        "src/fern/steps/types/list_steps_request_feedback.py",
        "src/fern/types/feeds_list_feeds_request_offset.py",
        "src/fern/types/feeds_list_subscriptions_request_offset.py",
        "src/fern/types/pipelines_list_pipelines_request_offset.py",
        "src/fern/types/projects_list_projects_request_offset.py",
        "src/fern/types/templates_list_template_versions_request_offset.py",
        "src/fern/types/templates_list_templates_request_offset.py",
        "src/fern/types/approval_request_message.py",
        "src/fern/types/approval_request_message_message_type.py",
        "src/fern/types/letta_stop_reason.py",
        "src/fern/types/letta_stop_reason_message_type.py",
        "src/fern/types/letta_usage_statistics_message_type.py",
        "src/fern/types/tool_return_message_message_type.py",
        "src/fern/feeds/__init__.py",
        "src/fern/feeds/types/__init__.py",
        "src/fern/feeds/types/feeds_delete_feed_request_body.py",
        "src/fern/feeds/types/feeds_delete_subscription_request_body.py",
        "src/fern/scheduled_messages/__init__.py",
        "src/fern/scheduled_messages/types/__init__.py",
        "src/fern/scheduled_messages/types/scheduled_messages_delete_scheduled_message_request_body.py",
        "src/fern/tools/types/list_mcp_servers_response_value.py",
        "src/fern/types/bad_request_error_body.py",
        "src/fern/types/bad_request_error_body_error_code.py",
        "src/fern/types/not_found_error_body_error_code.py",
        "src/fern/types/body_export_agent.py",
        "src/fern/types/chat_completion.py",
        "src/fern/types/compaction_request.py",
        "src/fern/types/completion_usage.py",
        "src/fern/types/letta_schemas_mcp_update_stdio_mcp_server.py",
        "src/fern/types/usage_statistics.py",
        "src/fern/types/chat_completion_message.py",
        "src/fern/types/child_tool_rule.py",
        "src/fern/types/choice_logprobs.py",
        "src/fern/types/letta_batch_request.py",
        "src/fern/types/letta_request.py",
        "src/fern/types/letta_request_config.py",
        "src/fern/types/letta_request_messages_item.py",
        "src/fern/types/letta_streaming_request.py",
        "src/fern/agents/types/letta_async_request_input.py",
        "src/fern/chat/types/chat_completion_request_stop.py",
        "src/fern/types/approval_request_message_tool_calls.py",
        "src/fern/types/chat_completion_assistant_message_param_content.py",
        "src/fern/types/letta_batch_request_input.py",
        "src/fern/types/letta_request_input.py",
        "src/fern/types/letta_schemas_message_tool_return_input_func_response.py",
        "src/fern/types/letta_schemas_message_tool_return_output_func_response.py",
        "src/fern/types/letta_streaming_request_input.py",
        "src/fern/types/memory_agent_type.py",
        "src/fern/types/tool_call_message_tool_calls.py",
        "src/fern/agents/types/letta_async_request_input_one_item.py",
        "src/fern/types/letta_batch_request_input_one_item.py",
        "src/fern/types/letta_request_input_one_item.py",
        "src/fern/types/letta_schemas_message_tool_return_input_func_response_one_item.py",
        "src/fern/types/letta_schemas_message_tool_return_output_func_response_one_item.py",
        "src/fern/types/letta_streaming_request_input_one_item.py",
        "src/fern/types/anthropic_model_settings_effort.py",
        "src/fern/types/anthropic_model_settings_verbosity.py",
        "src/fern/types/approval_return.py",
        "src/fern/types/approval_return_type.py",
        "src/fern/types/chat_completion_service_tier.py",
        "src/fern/types/letta_schemas_agent_file_message_schema.py",
        "src/fern/types/letta_schemas_agent_file_message_schema_type.py",
        "src/fern/types/letta_schemas_letta_message_tool_return_type.py",
        "src/fern/types/llm_config_compatibility_type.py",
        "src/fern/types/llm_config_effort.py",
        "src/fern/types/llm_config_reasoning_effort.py",
        "src/fern/types/llm_config_verbosity.py",
        "src/fern/types/message_create.py",
        "src/fern/types/message_create_type.py",
        "src/fern/types/model_compatibility_type.py",
        "src/fern/types/model_effort.py",
        "src/fern/types/model_reasoning_effort.py",
        "src/fern/types/model_verbosity.py",
        "src/fern/types/step_feedback.py",
        "src/fern/archives/__init__.py",
        "src/fern/archives/types/__init__.py",
        "src/fern/internal_templates/__init__.py",
        "src/fern/internal_templates/types/__init__.py",
        "src/fern/passages/__init__.py",
        "src/fern/passages/client.py",
        "src/fern/passages/raw_client.py",
        "src/fern/passages/types/__init__.py",
        "src/fern/tools/__init__.py",
        "src/fern/tools/types/__init__.py",
        "src/fern/types/archive.py",
        "src/fern/types/block.py",
        "src/fern/types/block_response.py",
        "src/fern/types/block_schema.py",
        "src/fern/types/block_update.py",
        "src/fern/types/chat_completion_token_logprob.py",
        "src/fern/types/client_tool_schema.py",
        "src/fern/types/create_block.py",
        "src/fern/types/e2b_sandbox_config.py",
        "src/fern/types/file_block.py",
        "src/fern/types/folder.py",
        "src/fern/types/function_definition.py",
        "src/fern/types/init_tool_rule.py",
        "src/fern/types/internal_template_block_create.py",
        "src/fern/types/letta_schemas_agent_file_tool_schema.py",
        "src/fern/types/letta_schemas_letta_message_tool_return.py",
        "src/fern/types/letta_usage_statistics.py",
        "src/fern/types/mcp_server_schema.py",
        "src/fern/types/mcp_tool.py",
        "src/fern/types/modal_sandbox_config.py",
        "src/fern/types/provider_trace.py",
        "src/fern/types/run_metrics.py",
        "src/fern/types/source.py",
        "src/fern/types/source_create.py",
        "src/fern/types/source_schema.py",
        "src/fern/types/source_update.py",
        "src/fern/types/tool.py",
        "src/fern/types/tool_call_node.py",
        "src/fern/types/tool_create.py",
        "src/fern/types/tool_json_schema.py",
        "src/fern/types/tool_return_message.py",
        "src/fern/types/top_logprob.py",
        "src/fern/identities/__init__.py",
        "src/fern/identities/types/__init__.py",
        "src/fern/types/agent_state.py",
        "src/fern/types/batch_job.py",
        "src/fern/types/job.py",
        "src/fern/types/llm_config.py",
        "src/fern/types/model.py",
        "src/fern/types/run.py",
        "src/fern/types/step.py",
        "src/fern/archives/client.py",
        "src/fern/folders/client.py",
        "src/fern/identities/client.py",
        "src/fern/jobs/client.py",
        "src/fern/jobs/raw_client.py",
        "src/fern/mcp_servers/raw_client.py",
        "src/fern/messages/client.py",
        "src/fern/messages/raw_client.py",
        "src/fern/providers/client.py",
        "src/fern/providers/raw_client.py",
        "src/fern/sources/client.py",
        "src/fern/tag/client.py",
        "src/fern/tag/raw_client.py",
        "src/fern/internal_blocks/client.py",
        "src/fern/internal_blocks/raw_client.py",
        "src/fern/internal_runs/client.py",
        "src/fern/internal_runs/raw_client.py",
        "src/fern/models/client.py",
        "src/fern/models/raw_client.py",
        "src/fern/runs/client.py",
        "src/fern/runs/raw_client.py",
        "src/fern/tools/client.py",
        "src/fern/internal_templates/client.py",
        "src/fern/types/create_ssemcp_server.py",
        "src/fern/types/create_stdio_mcp_server.py",
        "src/fern/types/create_streamable_httpmcp_server.py",
        "src/fern/types/letta_schemas_agent_file_agent_schema.py",
        "src/fern/types/letta_schemas_mcp_update_ssemcp_server.py",
        "src/fern/types/letta_schemas_mcp_update_streamable_httpmcp_server.py",
        "src/fern/types/sse_server_config.py",
        "src/fern/types/stdio_server_config.py",
        "src/fern/types/streamable_http_server_config.py",
        "src/fern/steps/client.py",
        "src/fern/steps/raw_client.py",
        "src/fern/telemetry/__init__.py",
        "src/fern/telemetry/client.py",
        "src/fern/telemetry/raw_client.py",
        "src/fern/blocks/client.py",
        "src/fern/blocks/raw_client.py",
        "src/fern/internal_agents/client.py",
        "src/fern/internal_agents/raw_client.py",
        "src/fern/archives/raw_client.py",
        "src/fern/chat/raw_client.py",
        "src/fern/folders/raw_client.py",
        "src/fern/identities/raw_client.py",
        "src/fern/sources/raw_client.py",
        "src/fern/tools/raw_client.py",
        "src/fern/conversations/__init__.py",
        "src/fern/conversations/client.py",
        "src/fern/conversations/types/__init__.py",
        "src/fern/types/assistant_message_list_result.py",
        "src/fern/types/reasoning_message_list_result.py",
        "src/fern/types/system_message_list_result.py",
        "src/fern/types/user_message_list_result.py",
        "README.md",
        "src/fern/client.py",
        "src/fern/environment.py",
        "src/fern/groups/types/group_update_manager_config.py",
        "src/fern/types/conditional_tool_rule_schema.py",
        "src/fern/types/context_window_overview.py",
        "src/fern/types/core_memory_block_schema.py",
        "src/fern/types/letta_schemas_mcp_server_update_ssemcp_server.py",
        "src/fern/types/letta_schemas_mcp_server_update_stdio_mcp_server.py",
        "src/fern/types/letta_schemas_mcp_server_update_streamable_httpmcp_server.py",
        "src/fern/types/letta_serialize_schemas_pydantic_agent_schema_message_schema.py",
        "src/fern/types/passage.py",
        "src/fern/types/supervisor_manager_update.py",
        "src/fern/types/tool_env_var_schema.py",
        "src/fern/types/letta_schemas_message_tool_return_input.py",
        "src/fern/types/letta_schemas_message_tool_return_output.py",
        "src/fern/types/letta_serialize_schemas_pydantic_agent_schema_agent_schema.py",
        "src/fern/types/letta_serialize_schemas_pydantic_agent_schema_tool_schema.py",
        "src/fern/types/tool_execution_result.py",
        "src/fern/types/not_found_error_body.py",
        "src/fern/chat/__init__.py",
        "src/fern/chat/types/__init__.py",
        "src/fern/types/chat_completion_assistant_message_param.py",
        "src/fern/types/chat_completion_developer_message_param.py",
        "src/fern/types/chat_completion_function_message_param.py",
        "src/fern/types/chat_completion_system_message_param.py",
        "src/fern/types/chat_completion_tool_message_param.py",
        "src/fern/types/chat_completion_user_message_param.py",
        "src/fern/types/ssemcp_server.py",
        "src/fern/types/stdio_mcp_server.py",
        "src/fern/types/streamable_httpmcp_server.py",
        "src/fern/types/update_assistant_message.py",
        "src/fern/types/update_reasoning_message.py",
        "src/fern/types/update_system_message.py",
        "src/fern/types/update_user_message.py",
        "src/fern/types/letta_message_union.py",
        "src/fern/types/letta_streaming_response.py",
        "src/fern/types/chat_completion_assistant_message_param_content_one_item.py",
        "src/fern/types/chat_completion_assistant_message_param_tool_calls_item.py",
        "src/fern/types/chat_completion_message_tool_calls_item.py",
        "src/fern/types/chat_completion_user_message_param_content_one_item.py",
        "src/fern/agents/types/modify_message_request_body.py",
        "src/fern/groups/types/modify_group_message_request_body.py",
        "src/fern/templates/__init__.py",
        "src/fern/templates/types/__init__.py",
        "src/fern/templates/types/templates_create_template_no_project_request.py",
        "src/fern/templates/types/templates_create_template_request_body.py",
        "src/fern/agents/client.py",
        "src/fern/chat/client.py",
        "src/fern/groups/client.py",
        "src/fern/agents/raw_client.py",
        "src/fern/conversations/raw_client.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/projects/client.py",
        "src/fern/templates/client.py",
        "src/fern/mcp_servers/client.py",
        "src/fern/feeds/client.py",
        "src/fern/scheduled_messages/client.py",
        "src/fern/scheduled_messages/raw_client.py",
        "src/fern/feeds/raw_client.py",
        "src/fern/pipelines/raw_client.py",
        "src/fern/projects/raw_client.py",
        "src/fern/templates/raw_client.py",
        "src/fern/types/letta_assistant_message_content_union.py",
        "src/fern/types/message.py",
        "src/fern/agents/__init__.py",
        "src/fern/agents/types/__init__.py",
        "src/fern/agents/types/modify_message_response.py",
        "src/fern/groups/__init__.py",
        "src/fern/groups/types/__init__.py",
        "src/fern/groups/types/modify_group_message_response.py",
        "src/fern/mcp_servers/types/create_mcp_server_request_config.py",
        "src/fern/mcp_servers/types/mcp_create_mcp_server_response.py",
        "src/fern/mcp_servers/types/mcp_retrieve_mcp_server_response.py",
        "src/fern/mcp_servers/types/mcp_update_mcp_server_response.py",
        "src/fern/mcp_servers/types/update_mcp_server_request_config.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools_child_arg_nodes_item.py",
        "src/fern/templates/types/templates_get_template_snapshot_response_agents_item_tool_rules_item_run_first.py",
        "src/fern/types/chat_completion_content_part_image_param.py",
        "src/fern/types/chat_completion_content_part_input_audio_param.py",
        "src/fern/types/chat_completion_content_part_refusal_param.py",
        "src/fern/types/chat_completion_message_custom_tool_call.py",
        "src/fern/types/chat_completion_message_custom_tool_call_param.py",
        "src/fern/types/chat_completion_message_function_tool_call_param.py",
        "src/fern/types/file.py",
        "src/fern/mcp_servers/__init__.py",
        "src/fern/mcp_servers/types/__init__.py",
        "src/fern/mcp_servers/types/mcp_list_mcp_servers_response_item.py",
        "src/fern/messages/__init__.py",
        "src/fern/messages/types/__init__.py",
        "src/fern/messages/types/search_all_messages_response_item.py",
        "src/fern/steps/__init__.py",
        "src/fern/steps/types/__init__.py",
        "src/fern/steps/types/list_messages_for_step_response_item.py",
        "src/fern/__init__.py",
        "src/fern/types/__init__.py",
        "src/fern/chat/types/chat_completion_request_messages_item.py",
        "src/fern/groups/raw_client.py",
        "src/fern/client_side_access_tokens/raw_client.py",
        "src/fern/internal_templates/raw_client.py",
        "src/fern/embeddings/client.py",
        "src/fern/embeddings/raw_client.py",
        "src/fern/client_side_access_tokens/client.py",
        "src/fern/templates/types/templates_create_template_no_project_request_agent.py",
        "src/fern/templates/types/templates_create_template_no_project_request_agent_file.py",
        "src/fern/templates/types/templates_create_template_request_body_agent.py",
        "src/fern/templates/types/templates_create_template_request_body_agent_file.py",
    ],
};

/// `free5gc-namf-communication`: the AMF Communication API nests `oneOf` and
/// `not` inside `allOf` and uses problem+json across its error responses.
const FREE5GC_NAMF_COMMUNICATION: Corpus = Corpus {
    api: "free5gc-namf-communication",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[
        ".fern/metadata.json",
        "CONTRIBUTING.md",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/_default_clients.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/enum.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/logging.py",
        "src/fern/core/parse_error.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/environment.py",
        "src/fern/errors/__init__.py",
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/conflict_error.py",
        "src/fern/errors/content_too_large_error.py",
        "src/fern/errors/forbidden_error.py",
        "src/fern/errors/gateway_timeout_error.py",
        "src/fern/errors/internal_server_error.py",
        "src/fern/errors/length_required_error.py",
        "src/fern/errors/not_found_error.py",
        "src/fern/errors/service_unavailable_error.py",
        "src/fern/errors/too_many_requests_error.py",
        "src/fern/errors/unsupported_media_type_error.py",
        "src/fern/individual_subscription_document/__init__.py",
        "src/fern/individual_subscription_document/client.py",
        "src/fern/individual_subscription_document/raw_client.py",
        "src/fern/individual_ue_context_document/__init__.py",
        "src/fern/individual_ue_context_document/client.py",
        "src/fern/individual_ue_context_document/raw_client.py",
        "src/fern/n1n2individual_subscription_document/__init__.py",
        "src/fern/n1n2individual_subscription_document/client.py",
        "src/fern/n1n2individual_subscription_document/raw_client.py",
        "src/fern/n1n2message_collection_document/__init__.py",
        "src/fern/n1n2subscriptions_collection_for_individual_ue_contexts_document/__init__.py",
        "src/fern/n1n2subscriptions_collection_for_individual_ue_contexts_document/client.py",
        "src/fern/n1n2subscriptions_collection_for_individual_ue_contexts_document/raw_client.py",
        "src/fern/non_ue_n2message_notification_individual_subscription_document/__init__.py",
        "src/fern/non_ue_n2message_notification_individual_subscription_document/client.py",
        "src/fern/non_ue_n2message_notification_individual_subscription_document/raw_client.py",
        "src/fern/non_ue_n2messages_collection_document/__init__.py",
        "src/fern/non_ue_n2messages_collection_document/client.py",
        "src/fern/non_ue_n2messages_collection_document/raw_client.py",
        "src/fern/non_ue_n2messages_subscriptions_collection_document/__init__.py",
        "src/fern/non_ue_n2messages_subscriptions_collection_document/client.py",
        "src/fern/non_ue_n2messages_subscriptions_collection_document/raw_client.py",
        "src/fern/py.typed",
        "src/fern/subscriptions_collection_document/__init__.py",
        "src/fern/subscriptions_collection_document/client.py",
        "src/fern/types/__init__.py",
        "src/fern/types/access_type.py",
        "src/fern/types/allowed_nssai.py",
        "src/fern/types/allowed_snssai.py",
        "src/fern/types/am_policy_req_trigger.py",
        "src/fern/types/ambr.py",
        "src/fern/types/amf_event.py",
        "src/fern/types/amf_event_area.py",
        "src/fern/types/amf_event_mode.py",
        "src/fern/types/amf_event_subscription.py",
        "src/fern/types/amf_event_trigger.py",
        "src/fern/types/amf_event_type.py",
        "src/fern/types/amf_id.py",
        "src/fern/types/amf_name.py",
        "src/fern/types/amf_status_change_notification.py",
        "src/fern/types/amf_status_info.py",
        "src/fern/types/area.py",
        "src/fern/types/area_code.py",
        "src/fern/types/area_of_validity.py",
        "src/fern/types/arp.py",
        "src/fern/types/arp_priority_level.py",
        "src/fern/types/assign_ebi_error.py",
        "src/fern/types/assign_ebi_failed.py",
        "src/fern/types/assigned_ebi_data.py",
        "src/fern/types/bit_rate.py",
        "src/fern/types/bytes.py",
        "src/fern/types/ciphering_algorithm.py",
        "src/fern/types/configured_snssai.py",
        "src/fern/types/core_network_type.py",
        "src/fern/types/correlation_id.py",
        "src/fern/types/create_ue_context_response201.py",
        "src/fern/types/date_time.py",
        "src/fern/types/dnn.py",
        "src/fern/types/drx_parameter.py",
        "src/fern/types/ebi_arp_mapping.py",
        "src/fern/types/ecgi.py",
        "src/fern/types/eps_bearer_id.py",
        "src/fern/types/eps_bearer_id2.py",
        "src/fern/types/eutra_cell_id.py",
        "src/fern/types/eutra_location.py",
        "src/fern/types/expected_ue_behavior.py",
        "src/fern/types/five_g_mm_capability.py",
        "src/fern/types/five_qi.py",
        "src/fern/types/g_nb_id.py",
        "src/fern/types/global_ran_node_id.py",
        "src/fern/types/gpsi.py",
        "src/fern/types/group_id.py",
        "src/fern/types/guami.py",
        "src/fern/types/integrity_algorithm.py",
        "src/fern/types/invalid_param.py",
        "src/fern/types/ipv4addr.py",
        "src/fern/types/ipv6addr.py",
        "src/fern/types/key_amf.py",
        "src/fern/types/key_amf_type.py",
        "src/fern/types/ladn_info.py",
        "src/fern/types/location_filter.py",
        "src/fern/types/mcc.py",
        "src/fern/types/mm_context.py",
        "src/fern/types/mnc.py",
        "src/fern/types/n1message_class.py",
        "src/fern/types/n1message_container.py",
        "src/fern/types/n1message_notification.py",
        "src/fern/types/n1n2message_transfer_cause.py",
        "src/fern/types/n1n2message_transfer_error.py",
        "src/fern/types/n1n2message_transfer_req_data.py",
        "src/fern/types/n1n2message_transfer_request_body.py",
        "src/fern/types/n1n2message_transfer_rsp_data.py",
        "src/fern/types/n1n2msg_txfr_err_detail.py",
        "src/fern/types/n1n2msg_txfr_failure_notification.py",
        "src/fern/types/n2info_container.py",
        "src/fern/types/n2info_content.py",
        "src/fern/types/n2info_notify_reason.py",
        "src/fern/types/n2information_class.py",
        "src/fern/types/n2information_notification.py",
        "src/fern/types/n2information_transfer_error.py",
        "src/fern/types/n2information_transfer_req_data.py",
        "src/fern/types/n2information_transfer_result.py",
        "src/fern/types/n2information_transfer_rsp_data.py",
        "src/fern/types/n2ran_information.py",
        "src/fern/types/n2sm_information.py",
        "src/fern/types/n3ga_location.py",
        "src/fern/types/n3iwf_id.py",
        "src/fern/types/nas_count.py",
        "src/fern/types/nas_security_mode.py",
        "src/fern/types/ncgi.py",
        "src/fern/types/nf_group_id.py",
        "src/fern/types/nf_instance_id.py",
        "src/fern/types/ng_ap_cause.py",
        "src/fern/types/ng_ksi.py",
        "src/fern/types/ng_ran_target_id.py",
        "src/fern/types/ngap_ie_type.py",
        "src/fern/types/nge_nb_id.py",
        "src/fern/types/non_ue_n2info_subscription_created_data.py",
        "src/fern/types/non_ue_n2message_transfer_request_body.py",
        "src/fern/types/nr_cell_id.py",
        "src/fern/types/nr_location.py",
        "src/fern/types/nrppa_information.py",
        "src/fern/types/nsi_id.py",
        "src/fern/types/nsi_information.py",
        "src/fern/types/nssai_mapping.py",
        "src/fern/types/oauth_scope.py",
        "src/fern/types/omc_identifier.py",
        "src/fern/types/pdu_session_context.py",
        "src/fern/types/pdu_session_id.py",
        "src/fern/types/pei.py",
        "src/fern/types/plmn_id.py",
        "src/fern/types/ppi.py",
        "src/fern/types/preemption_capability.py",
        "src/fern/types/preemption_vulnerability.py",
        "src/fern/types/presence_info.py",
        "src/fern/types/presence_state.py",
        "src/fern/types/problem_details.py",
        "src/fern/types/pws_error_data.py",
        "src/fern/types/pws_information.py",
        "src/fern/types/pws_response_data.py",
        "src/fern/types/rat_selector.py",
        "src/fern/types/rat_type.py",
        "src/fern/types/ref_to_binary_data.py",
        "src/fern/types/registration_context_container.py",
        "src/fern/types/restriction_type.py",
        "src/fern/types/rfsp_index.py",
        "src/fern/types/s1ue_network_capability.py",
        "src/fern/types/sc_type.py",
        "src/fern/types/seaf_data.py",
        "src/fern/types/service_area_restriction.py",
        "src/fern/types/sms_support.py",
        "src/fern/types/snssai.py",
        "src/fern/types/status_change.py",
        "src/fern/types/subscribed_data_filter.py",
        "src/fern/types/subscription_data.py",
        "src/fern/types/supi.py",
        "src/fern/types/supported_features.py",
        "src/fern/types/tac.py",
        "src/fern/types/tai.py",
        "src/fern/types/time_zone.py",
        "src/fern/types/trace_data.py",
        "src/fern/types/trace_depth.py",
        "src/fern/types/transfer_reason.py",
        "src/fern/types/ue_context.py",
        "src/fern/types/ue_context_create_data.py",
        "src/fern/types/ue_context_create_error.py",
        "src/fern/types/ue_context_created_data.py",
        "src/fern/types/ue_context_transfer_req_data.py",
        "src/fern/types/ue_context_transfer_request_body.py",
        "src/fern/types/ue_context_transfer_response200.py",
        "src/fern/types/ue_context_transfer_rsp_data.py",
        "src/fern/types/ue_context_transfer_status.py",
        "src/fern/types/ue_n1n2info_subscription_created_data.py",
        "src/fern/types/ue_reg_status_update_rsp_data.py",
        "src/fern/types/ue_security_capability.py",
        "src/fern/types/uint16.py",
        "src/fern/types/uinteger.py",
        "src/fern/types/uri.py",
        "src/fern/types/user_location.py",
        "src/fern/version.py",
        "tests/conftest.py",
        "tests/test_aiohttp_autodetect.py",
        "src/fern/n1n2message_collection_document/client.py",
        "src/fern/n1n2message_collection_document/raw_client.py",
        "src/fern/subscriptions_collection_document/raw_client.py",
    ],
};

#[test]
fn squareup_com_matches_fern_output() {
    if corpus_spec(SQUAREUP_COM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Square corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&SQUAREUP_COM);
}

#[test]
fn amazonaws_com_cloudformation_matches_fern_output() {
    if corpus_spec(AMAZONAWS_COM_CLOUDFORMATION.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the AWS CloudFormation corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&AMAZONAWS_COM_CLOUDFORMATION);
}

#[test]
fn redocly_com_museum_matches_fern_output() {
    if corpus_spec(REDOCLY_COM_MUSEUM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Redocly Museum corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&REDOCLY_COM_MUSEUM);
}

#[test]
fn http_toolkit_matches_fern_output() {
    if corpus_spec(HTTP_TOOLKIT.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the HTTP Toolkit corpus spec is not fetched; run scripts/fetch-corpus.sh first"
        );
        return;
    }
    assert_corpus_matches(&HTTP_TOOLKIT);
}

fn assert_link_ok_corpus_matches(corpus: &Corpus) {
    if corpus_spec(corpus.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the {} corpus spec is not fetched; run scripts/fetch-corpus.sh first",
            corpus.api
        );
        return;
    }
    assert_corpus_matches(corpus);
}

#[test]
fn frankfurter_matches_fern_output() {
    assert_link_ok_corpus_matches(&FRANKFURTER);
}

#[test]
fn worldcoin_signup_sequencer_matches_fern_output() {
    assert_link_ok_corpus_matches(&WORLDCOIN_SIGNUP_SEQUENCER);
}

#[test]
fn electric_sql_matches_fern_output() {
    assert_link_ok_corpus_matches(&ELECTRIC_SQL);
}

#[test]
fn tamoss_matches_fern_output() {
    assert_link_ok_corpus_matches(&TAMOSS);
}

#[test]
fn appng_rest_api_matches_fern_output() {
    assert_link_ok_corpus_matches(&APPNG_REST_API);
}

#[test]
fn slurmdb_rest_matches_fern_output() {
    assert_link_ok_corpus_matches(&SLURMDB_REST);
}

#[test]
fn nimisampo_matches_fern_output() {
    assert_link_ok_corpus_matches(&NIMISAMPO);
}

#[test]
fn free5gc_pdu_session_matches_fern_output() {
    assert_link_ok_corpus_matches(&FREE5GC_PDU_SESSION);
}

#[test]
fn sigstore_rekor_matches_fern_output() {
    assert_link_ok_corpus_matches(&SIGSTORE_REKOR);
}

#[test]
fn letta_matches_fern_output() {
    assert_link_ok_corpus_matches(&LETTA);
}

#[test]
fn free5gc_namf_communication_matches_fern_output() {
    assert_link_ok_corpus_matches(&FREE5GC_NAMF_COMMUNICATION);
}

#[test]
fn feature_target_specs_generate_without_panicking() {
    // A feature-coverage target with a populated `matched` list is byte-compared
    // file-by-file; one with an empty `matched` list asserts only that crozier
    // consumes the spec and writes a tree (exit 0, "generated" on stderr) without
    // panicking. Every target is fully matched today; a future gap target starts
    // empty (golden Fern tree not yet generated) and grows its `matched` list as
    // generation lands, and the same helper then starts byte-comparing files.
    for target in FEATURE_TARGETS {
        assert_corpus_matches(target);
    }
}

/// Coverage-growth aid — NOT a gate (ignored by default so it never runs under
/// `check`). For every corpus, generate its tree and report which committed
/// fixture files crozier already reproduces byte-for-byte but that are absent from
/// the corpus's `matched` list. It prints each such file as a ready-to-paste array
/// entry, turning manifest growth from a manual diff into copy-paste. Run it via
/// `just fixtures-candidates` after a generator change; see tests/fixtures/AGENTS.md.
///
/// It also self-checks: a positive control asserts its detection pipeline re-confirms
/// every file already in `matched`, so a broken walk/matcher fails loudly rather than
/// silently reporting nothing.
#[test]
#[ignore = "coverage-growth aid, not a gate; run via `just fixtures-candidates`"]
fn report_matched_candidates() {
    let corpus_filter = std::env::var("CROZIER_CANDIDATES_CORPUS")
        .ok()
        .filter(|s| !s.is_empty());

    let mut corpora: Vec<&Corpus> = vec![&QUERY_PARAMETERS, &EXHAUSTIVE, &BUNQ];
    corpora.extend(FEATURE_TARGETS.iter());
    // bungie's spec is fetched, not vendored, and its `expected/` tree is pending;
    // include it only once the source spec is available so offline reporter runs do
    // not walk a missing fixture.
    if corpus_spec(BUNGIE.api).is_some() {
        corpora.push(&BUNGIE);
    }
    // The five batch corpora are the same: fetched, not vendored, golden pending —
    // include each only when its source spec is present so an offline run does not
    // walk a missing fixture.
    for c in [
        &ANCHORE,
        &APACHE_AIRFLOW,
        &DISCOURSE,
        &APPWRITE_SERVER,
        &APICURIO,
        &GAMBITCOMM_MIMIC,
        &DND5EAPI,
        &APACHE_QAKKA,
        &AUTHENTIQIO,
        &ETSI_MEC010_2,
        &APIDECK_WEBHOOK,
        &APIDECK_VAULT,
        &AIRBYTE_CONFIG,
        &BINTABLE,
        &APIS_GURU,
        &COLOR_PIZZA,
        &BYAUTOMATA_IO,
        &APIDECK_PROXY,
        &APIDECK_CONNECTOR,
        &APIDECK_ECOMMERCE,
        &APIDECK_ISSUE_TRACKING,
        &APPWRITE_CLIENT,
        &APIDECK_FILE_STORAGE,
        &APIDECK_HRIS,
        &APIDECK_ACCOUNTING,
        &CALORIENINJAS,
        &EOS,
        &APIDECK_SMS,
        &APIDECK_ECOSYSTEM,
        &APIDECK_CUSTOMER_SUPPORT,
        &APIDECK_LEAD,
        &APACHE_ORG_AIRFLOW,
        &OPENFIGI,
        &TWILIO_VOICE_V1,
        &MICROCKS_LOCAL,
        &REDHAT_CATALOG_INVENTORY,
        &XERO_PAYROLL_AU,
        &TRACCAR,
        &REVERB_COM,
        &MAIF_OTOROSHI,
        &PORTFOLIOOPTIMIZER_IO,
        &OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI,
        &NETBOX_DEV,
        &SQUAREUP_COM,
        &AMAZONAWS_COM_CLOUDFORMATION,
        &REDOCLY_COM_MUSEUM,
        &HTTP_TOOLKIT,
        &FRANKFURTER,
        &WORLDCOIN_SIGNUP_SEQUENCER,
        &ELECTRIC_SQL,
        &TAMOSS,
        &SLURMDB_REST,
        &NIMISAMPO,
        &FREE5GC_PDU_SESSION,
        &SIGSTORE_REKOR,
        &LETTA,
        &FREE5GC_NAMF_COMMUNICATION,
    ] {
        if corpus_spec(c.api).is_some() {
            corpora.push(c);
        }
    }
    if let Some(f) = &corpus_filter {
        corpora.retain(|c| c.api == f.as_str());
        assert!(
            !corpora.is_empty(),
            "CROZIER_CANDIDATES_CORPUS={f:?} matched no corpus (or its spec is unfetched)"
        );
    }

    let mut total = 0usize;
    for c in corpora {
        let expected_root = fixture_dir(c.api).join("expected");
        let matched: std::collections::HashSet<&str> = c.matched.iter().copied().collect();
        let out = generate_corpus(c);

        // Every expected file the reporter's own pipeline (walk + emit + match)
        // confirms crozier reproduces byte-for-byte — matched-or-not.
        let confirmed: std::collections::HashSet<String> = walk_files(&expected_root)
            .into_iter()
            .filter(|rel| {
                // Confirmed only if crozier emits it AND it matches. Skip anything
                // unreadable as UTF-8 (nothing in the corpus is binary today).
                let (Ok(expected), Ok(generated)) = (
                    std::fs::read_to_string(expected_root.join(rel)),
                    std::fs::read_to_string(out.path().join(rel)),
                ) else {
                    return false;
                };
                generated_matches_fixture(rel, &generated, &expected)
            })
            .collect();

        // Positive control — assert real behavior, not just printing. Every file
        // already in `matched` is proven byte-identical by the gate, so the
        // reporter's detection MUST re-confirm it; if it doesn't, the pipeline is
        // broken (an empty walk, an always-false matcher, a bad path) and any
        // "0 candidates" result is a false negative. Fail loudly instead.
        for rel in c.matched {
            assert!(
                confirmed.contains(*rel),
                "{}: reporter failed to re-confirm already-matched {rel} — candidate detection is broken",
                c.api
            );
        }

        let mut candidates: Vec<&String> = confirmed
            .iter()
            .filter(|rel| !matched.contains(rel.as_str()))
            .collect();
        candidates.sort();

        println!("\n=== {} ===", c.api);
        println!("  {} file(s) already in `matched`.", matched.len());
        if candidates.is_empty() {
            println!("  no new byte-matching files.");
        } else {
            total += candidates.len();
            println!(
                "  {} new byte-matching file(s) — add to this corpus's `matched` in tests/e2e.rs:",
                candidates.len()
            );
            for rel in candidates {
                println!("        \"{rel}\",");
            }
        }
    }
    println!("\n{total} new candidate file(s) across all corpora.");
}

fn registered_diff_corpora() -> Vec<&'static Corpus> {
    let mut seen = std::collections::HashSet::new();
    CORPORA
        .iter()
        .copied()
        .chain(FEATURE_TARGETS.iter())
        .filter(|corpus| seen.insert(corpus.api))
        .collect()
}

fn select_diff_corpora(requested: Option<&str>) -> (Vec<&'static Corpus>, Vec<(String, String)>) {
    let registered = registered_diff_corpora();
    let mut failures = Vec::new();
    let mut selected = Vec::new();
    let mut seen = std::collections::HashSet::new();

    let names: Vec<&str> = match requested {
        Some(value) => value.split(',').collect(),
        None => registered.iter().map(|corpus| corpus.api).collect(),
    };
    for name in names {
        if name.is_empty() || !seen.insert(name) {
            failures.push((
                name.to_string(),
                "empty or duplicate requested corpus name".to_string(),
            ));
            continue;
        }
        let Some(corpus) = registered.iter().copied().find(|corpus| corpus.api == name) else {
            failures.push((
                name.to_string(),
                "fixture is not registered in the e2e Corpus registry".to_string(),
            ));
            continue;
        };
        let expected = fixture_dir(corpus.api).join("expected");
        if expected.is_symlink() {
            if requested.is_some() {
                failures.push((
                    name.to_string(),
                    "refusing to compare a symlinked expected/ golden tree".to_string(),
                ));
            }
            continue;
        }
        if !expected.is_dir() {
            if requested.is_some() {
                failures.push((
                    name.to_string(),
                    "fixture has no expected/ golden tree".to_string(),
                ));
            }
            continue;
        }
        if corpus_spec(corpus.api).is_none() {
            if requested.is_some() {
                failures.push((
                    name.to_string(),
                    "fixture spec is unavailable after the fetch phase".to_string(),
                ));
            }
            continue;
        }
        selected.push(corpus);
    }
    (selected, failures)
}

#[derive(Debug, PartialEq, Eq)]
enum FixtureDifference {
    MissingGenerated,
    UnexpectedGenerated,
    Text(Option<String>),
    Binary { expected: usize, generated: usize },
    Processing(String),
}

fn fixture_differences(
    expected_root: &Path,
    generated_root: &Path,
    file_filter: Option<&str>,
    include_text_diffs: bool,
) -> Result<Vec<(String, FixtureDifference)>, String> {
    let expected_files: std::collections::BTreeSet<String> =
        try_walk_files(expected_root)?.into_iter().collect();
    if expected_files.is_empty() && file_filter.is_none() {
        return Err(format!(
            "no Fern files under {} — the fixture walk is broken",
            expected_root.display()
        ));
    }
    let generated_files: std::collections::BTreeSet<String> =
        try_walk_files(generated_root)?.into_iter().collect();
    let paths: std::collections::BTreeSet<&String> =
        expected_files.union(&generated_files).collect();
    let mut differences = Vec::new();

    for rel in paths {
        if file_filter.is_some_and(|filter| !rel.contains(filter)) {
            continue;
        }
        let expected_present = expected_files.contains(rel);
        let generated_present = generated_files.contains(rel);
        let difference = match (expected_present, generated_present) {
            (true, false) => Some(FixtureDifference::MissingGenerated),
            (false, true) => Some(FixtureDifference::UnexpectedGenerated),
            (true, true) => {
                let expected = match std::fs::read(expected_root.join(rel)) {
                    Ok(content) => content,
                    Err(error) => {
                        differences.push((
                            rel.clone(),
                            FixtureDifference::Processing(format!(
                                "could not read Fern golden: {error}"
                            )),
                        ));
                        continue;
                    }
                };
                let generated = match std::fs::read(generated_root.join(rel)) {
                    Ok(content) => content,
                    Err(error) => {
                        differences.push((
                            rel.clone(),
                            FixtureDifference::Processing(format!(
                                "could not read Crozier output: {error}"
                            )),
                        ));
                        continue;
                    }
                };
                if expected == generated {
                    None
                } else {
                    match (
                        std::str::from_utf8(&expected),
                        std::str::from_utf8(&generated),
                    ) {
                        (Ok(expected), Ok(generated)) => {
                            match try_normalized_pair(rel, generated, expected) {
                                Ok((actual, expected)) if actual == expected => None,
                                Ok((actual, expected)) => {
                                    Some(FixtureDifference::Text(include_text_diffs.then(|| {
                                        unified_diff(&expected, &actual).unwrap_or_default()
                                    })))
                                }
                                Err(error) => Some(FixtureDifference::Processing(error)),
                            }
                        }
                        _ => Some(FixtureDifference::Binary {
                            expected: expected.len(),
                            generated: generated.len(),
                        }),
                    }
                }
            }
            (false, false) => unreachable!("path came from the union"),
        };
        if let Some(difference) = difference {
            differences.push((rel.clone(), difference));
        }
    }
    Ok(differences)
}

/// Mismatch-investigation aid — NOT a gate (ignored by default). The inverse of
/// [`report_matched_candidates`]: instead of reporting files that now match, it
/// prints the normalized unified diff of every committed fixture file crozier does
/// NOT reproduce byte-for-byte — exactly the bytes the gate compares (comments,
/// SDK-identity headers, and `__init__.py` import order already normalized out via
/// [`normalized_pair`]), with `-` = Fern golden and `+` = crozier. This is the
/// "why doesn't this file match" loop as one command; run it via `just fixtures-diff`.
///
/// Scope with two env vars (the `just` recipe forwards its positional args):
/// `CROZIER_DIFF_CORPUS=<api>` limits to one corpus, `CROZIER_DIFF_FILE=<substr>`
/// to fixture paths containing `<substr>`. The Fern refresh automation instead
/// invokes one exact corpus at a time with `CROZIER_DIFF_SUMMARY_ONLY=1`; that
/// reports every differing path without retaining potentially huge unified diffs.
/// `CROZIER_DIFF_CORPORA=<api>,...` remains available for exact multi-corpus
/// callers. Missing registry entries are processing failures rather than silent
/// omissions. Pure reporter — it never asserts on a diff (a diff is the point).
#[test]
#[ignore = "mismatch-investigation aid, not a gate; run via `just fixtures-diff`"]
fn report_fixture_diffs() {
    let corpus_filter = std::env::var("CROZIER_DIFF_CORPUS")
        .ok()
        .filter(|s| !s.is_empty());
    let file_filter = std::env::var("CROZIER_DIFF_FILE")
        .ok()
        .filter(|s| !s.is_empty());
    let include_text_diffs = std::env::var_os("CROZIER_DIFF_SUMMARY_ONLY").is_none();

    let requested = std::env::var("CROZIER_DIFF_CORPORA").ok();
    let (mut corpora, selection_failures) = select_diff_corpora(requested.as_deref());
    if let Some(f) = &corpus_filter {
        corpora.retain(|c| c.api == f.as_str());
        assert!(
            !corpora.is_empty(),
            "CROZIER_DIFF_CORPUS={f:?} matched no corpus (or its spec is unfetched)"
        );
    }

    let mut total = 0usize;
    let mut generation_failures = 0usize;
    let mut processing_failures = selection_failures.len();
    for (fixture, error) in selection_failures {
        println!("\n=== {fixture} ===");
        println!("  Comparison setup failed: {error}");
    }
    for c in corpora {
        let expected_root = fixture_dir(c.api).join("expected");
        let matched: std::collections::HashSet<&str> = c.matched.iter().copied().collect();
        let known_failure = match known_fern_failure(c) {
            Ok(known_failure) => known_failure,
            Err(error) => {
                println!("\n=== {} ===", c.api);
                println!("  Comparison processing failed: {error}");
                processing_failures += 1;
                continue;
            }
        };
        let out = match try_generate_corpus(c) {
            Ok(out) => out,
            Err(error) => {
                println!("\n=== {} ===", c.api);
                println!("  Crozier generation failed: {error}");
                generation_failures += 1;
                continue;
            }
        };

        println!("\n=== {} ===", c.api);
        if let Some(known_failure) = known_failure {
            println!("{}", known_fern_failure_marker(c, &known_failure));
            continue;
        }
        let differences = match fixture_differences(
            &expected_root,
            out.path(),
            file_filter.as_deref(),
            include_text_diffs,
        ) {
            Ok(differences) => differences,
            Err(error) => {
                println!("  Comparison processing failed: {error}");
                processing_failures += 1;
                continue;
            }
        };
        for (rel, difference) in &differences {
            // A file already in `matched` differing is a regression, not a coverage
            // gap — flag it so it reads differently from a not-yet-matched file.
            let tag = if matched.contains(rel.as_str()) {
                " [REGRESSION — in `matched`]"
            } else {
                ""
            };
            println!("\n--- {rel}{tag} ---");
            match difference {
                FixtureDifference::MissingGenerated => {
                    println!("  Crozier did not emit this Fern file.");
                }
                FixtureDifference::UnexpectedGenerated => {
                    println!("  Crozier emitted this file, but Fern did not.");
                }
                FixtureDifference::Text(Some(diff)) => {
                    println!("  (`-` Fern golden, `+` crozier)\n{diff}");
                }
                FixtureDifference::Text(None) => {
                    println!("  Normalized text differs; unified diff omitted in summary mode.");
                }
                FixtureDifference::Binary {
                    expected,
                    generated,
                } => {
                    println!(
                        "  Binary bytes differ (Fern: {expected} bytes; Crozier: {generated} bytes)."
                    );
                }
                FixtureDifference::Processing(error) => {
                    println!("  Could not normalize/compare this file: {error}");
                }
            }
        }
        if differences.is_empty() {
            println!("  no differences.");
        }
        total += differences.len();
    }
    println!(
        "\n{generation_failures} comparison generation failure(s) across the reported corpora."
    );
    println!("{processing_failures} comparison processing failure(s) across the reported corpora.");
    println!("\n{total} differing file(s) across the reported corpora.");
}

/// [`unified_diff`] correctness — a real self-test so the diff the reporters and the
/// gate's failure message print is trustworthy (this binary is coverage-excluded, so
/// the assertions here are the guardrail).
#[test]
fn unified_diff_reports_only_real_changes() {
    // Identical input → no diff.
    assert_eq!(unified_diff("a\nb\nc", "a\nb\nc"), None);

    // A single changed line surfaces as a `-`/`+` pair; unchanged neighbours stay ` `.
    let d = unified_diff("a\nb\nc", "a\nB\nc").expect("differs");
    assert!(d.contains("- b"), "want the golden line: {d}");
    assert!(d.contains("+ B"), "want the crozier line: {d}");
    assert!(d.contains("  a") && d.contains("  c"), "want context: {d}");

    // Far-apart changes collapse the unchanged middle to an elision marker.
    let big = (0..40)
        .map(|n| n.to_string())
        .collect::<Vec<_>>()
        .join("\n");
    let mut lines: Vec<String> = big.lines().map(String::from).collect();
    lines[0] = "changed".into();
    let d = unified_diff(&big, &lines.join("\n")).expect("differs");
    assert!(d.contains("unchanged line(s)"), "want elision marker: {d}");
    assert!(!d.contains("\n  20\n"), "middle should be elided: {d}");
}

#[test]
fn aggregate_fixture_diff_includes_missing_unexpected_and_changed_files() {
    let expected = tempfile::tempdir().expect("expected tempdir");
    let generated = tempfile::tempdir().expect("generated tempdir");
    std::fs::write(expected.path().join("same.txt"), "same\n").unwrap();
    std::fs::write(generated.path().join("same.txt"), "same\n").unwrap();
    std::fs::write(expected.path().join("changed.txt"), "Fern\n").unwrap();
    std::fs::write(generated.path().join("changed.txt"), "Crozier\n").unwrap();
    std::fs::write(expected.path().join("missing.txt"), "Fern only\n").unwrap();
    std::fs::write(generated.path().join("unexpected.txt"), "Crozier only\n").unwrap();
    std::fs::write(
        expected.path().join(".crozier-fern-golden.json"),
        "provenance is not Fern output\n",
    )
    .unwrap();

    let differences = fixture_differences(expected.path(), generated.path(), None, true).unwrap();
    assert_eq!(differences.len(), 3, "{differences:?}");
    assert!(differences.iter().any(|(path, difference)| {
        path == "changed.txt" && matches!(difference, FixtureDifference::Text(_))
    }));
    assert!(differences.iter().any(|(path, difference)| {
        path == "missing.txt" && difference == &FixtureDifference::MissingGenerated
    }));
    assert!(differences.iter().any(|(path, difference)| {
        path == "unexpected.txt" && difference == &FixtureDifference::UnexpectedGenerated
    }));

    let summary = fixture_differences(expected.path(), generated.path(), None, false).unwrap();
    assert!(summary.iter().any(|(path, difference)| {
        path == "changed.txt" && difference == &FixtureDifference::Text(None)
    }));
}

#[cfg(unix)]
#[test]
fn aggregate_fixture_diff_refuses_to_follow_symlinks() {
    use std::os::unix::fs::symlink;

    let expected = tempfile::tempdir().expect("expected tempdir");
    let generated = tempfile::tempdir().expect("generated tempdir");
    let outside = tempfile::NamedTempFile::new().expect("outside file");
    symlink(outside.path(), expected.path().join("outside-link")).expect("create symlink");

    let error = fixture_differences(expected.path(), generated.path(), None, true).unwrap_err();
    assert!(
        error.contains("refusing to follow symbolic link"),
        "{error}"
    );
}

#[test]
fn exact_comparison_scope_reports_unregistered_managed_fixtures() {
    let (selected, failures) =
        select_diff_corpora(Some("query-parameters-openapi,new-unregistered-fixture"));
    assert_eq!(
        selected.iter().map(|corpus| corpus.api).collect::<Vec<_>>(),
        ["query-parameters-openapi"]
    );
    assert_eq!(failures.len(), 1, "{failures:?}");
    assert_eq!(failures[0].0, "new-unregistered-fixture");
    assert!(failures[0].1.contains("not registered"));
}

fn safe_fixture_name(value: &str) -> bool {
    value
        .chars()
        .next()
        .is_some_and(|first| first.is_ascii_alphanumeric())
        && value
            .chars()
            .all(|character| character.is_ascii_alphanumeric() || "._-".contains(character))
        && !value.contains("..")
}

fn corpus_fixture_aliases() -> Result<Vec<(&'static str, &'static str)>, String> {
    let mut aliases = Vec::new();
    let mut sources = std::collections::HashSet::new();
    let mut fixtures = std::collections::HashSet::new();
    for (index, line) in include_str!("fixtures/corpus-aliases.tsv")
        .lines()
        .enumerate()
    {
        if line.trim().is_empty() || line.trim_start().starts_with('#') {
            continue;
        }
        let cells: Vec<&str> = line.split('\t').collect();
        if cells.len() != 2 || !safe_fixture_name(cells[0]) || !safe_fixture_name(cells[1]) {
            return Err(format!(
                "corpus-aliases.tsv line {} must contain two safe fixture names separated by one tab",
                index + 1
            ));
        }
        let (name, fixture) = (cells[0], cells[1]);
        if name == fixture {
            return Err(format!(
                "corpus-aliases.tsv line {} maps a fixture name to itself",
                index + 1
            ));
        }
        if !sources.insert(name) {
            return Err(format!(
                "corpus-aliases.tsv line {} duplicates alias source {name:?}",
                index + 1
            ));
        }
        if !fixtures.insert(fixture) {
            return Err(format!(
                "corpus-aliases.tsv line {} duplicates fixture directory {fixture:?}",
                index + 1
            ));
        }
        aliases.push((name, fixture));
    }
    if aliases.is_empty() {
        return Err("corpus-aliases.tsv contains no aliases".to_string());
    }
    Ok(aliases)
}

fn corpus_fixture_for<'a>(name: &'a str, aliases: &[(&'a str, &'a str)]) -> &'a str {
    aliases
        .iter()
        .find_map(|(source, fixture)| (*source == name).then_some(*fixture))
        .unwrap_or(name)
}

#[test]
fn corpus_fixture_aliases_resolve_to_registered_goldens() {
    let aliases = corpus_fixture_aliases().expect("valid corpus fixture aliases");
    let registered: std::collections::HashSet<&str> = registered_diff_corpora()
        .into_iter()
        .map(|corpus| corpus.api)
        .collect();
    for (name, fixture) in &aliases {
        assert_eq!(corpus_fixture_for(name, &aliases), *fixture);
        assert!(
            fixture_dir(fixture).join("expected").is_dir(),
            "fixture alias {name:?} points at missing golden {fixture:?}"
        );
        assert!(
            registered.contains(fixture),
            "fixture alias {name:?} points at unregistered golden {fixture:?}"
        );
    }
    assert_eq!(
        corpus_fixture_for("unaliased-corpus", &aliases),
        "unaliased-corpus"
    );
}

#[test]
fn every_existing_manifest_golden_is_registered_for_aggregate_comparison() {
    let aliases = corpus_fixture_aliases().expect("valid corpus fixture aliases");
    let registered: std::collections::HashSet<&str> = registered_diff_corpora()
        .into_iter()
        .map(|corpus| corpus.api)
        .collect();
    let mut missing = Vec::new();
    for line in include_str!("fixtures/CORPUS.md").lines() {
        let cells: Vec<&str> = line
            .trim()
            .trim_matches('|')
            .split('|')
            .map(str::trim)
            .collect();
        if cells
            .first()
            .is_none_or(|number| number.is_empty() || !number.chars().all(|c| c.is_ascii_digit()))
        {
            continue;
        }
        let name = cells[1].trim_matches('`');
        let fixture = corpus_fixture_for(name, &aliases);
        if fixture_dir(fixture).join("expected").is_dir() && !registered.contains(fixture) {
            missing.push(fixture);
        }
    }
    assert!(
        missing.is_empty(),
        "manifest fixtures with expected/ but no e2e Corpus registration: {missing:?}"
    );
}

/// Every file under `root`, as `/`-separated paths relative to `root`, sorted.
/// A small hand-rolled walk to avoid a `walkdir` dev-dependency for one use.
fn walk_files(root: &Path) -> Vec<String> {
    try_walk_files(root).unwrap_or_else(|error| panic!("{error}"))
}

fn try_walk_files(root: &Path) -> Result<Vec<String>, String> {
    fn rec(base: &Path, dir: &Path, out: &mut Vec<String>) -> Result<(), String> {
        let mut entries = Vec::new();
        let directory = std::fs::read_dir(dir)
            .map_err(|error| format!("read_dir {}: {error}", dir.display()))?;
        for entry in directory {
            entries.push(
                entry
                    .map_err(|error| format!("read_dir entry in {}: {error}", dir.display()))?
                    .path(),
            );
        }
        entries.sort();
        for path in entries {
            let metadata = std::fs::symlink_metadata(&path)
                .map_err(|error| format!("metadata {}: {error}", path.display()))?;
            if metadata.file_type().is_symlink() {
                return Err(format!(
                    "refusing to follow symbolic link while walking {}",
                    path.display()
                ));
            }
            if metadata.is_dir() {
                rec(base, &path, out)?;
            } else {
                let rel = path.strip_prefix(base).map_err(|error| {
                    format!(
                        "{} is not below {}: {error}",
                        path.display(),
                        base.display()
                    )
                })?;
                let rel = rel.to_string_lossy().replace('\\', "/");
                // Automation provenance is committed atomically inside the
                // golden directory, but it is not Fern output and Crozier must
                // not be expected to emit it.
                if rel != ".crozier-fern-golden.json" {
                    out.push(rel);
                }
            }
        }
        Ok(())
    }
    let mut out = Vec::new();
    if root.is_symlink() {
        return Err(format!(
            "refusing to follow symbolic link while walking {}",
            root.display()
        ));
    }
    if root.is_dir() {
        rec(root, root, &mut out)?;
    }
    Ok(out)
}

#[test]
fn missing_spec_fails_with_actionable_message() {
    let out = tempfile::tempdir().expect("tempdir");
    crozier()
        .args(["generate", "--spec", "does-not-exist.yml", "--output"])
        .arg(out.path())
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("could not read spec"));
}

#[test]
fn unsupported_extension_fails() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.txt");
    std::fs::write(&spec, "openapi: 3.0.0").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("unsupported spec extension"));
}

#[test]
fn non_openapi_document_fails_clearly() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "just: some yaml\nnot: openapi\n").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("missing `openapi` version"));
}

#[test]
fn unsupported_openapi_version_fails() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "openapi: 2.0\ninfo:\n  title: Old\n").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("crozier supports 3.x"));
}

#[test]
fn help_lists_generate() {
    crozier()
        .arg("--help")
        .assert()
        .success()
        .stdout(predicate::str::contains("generate"));
}

#[test]
fn version_flag_reports_crate_version() {
    // The literal first thing a user types. `--version` prints the crate version;
    // the release smoke test asserts the same string against the published binary.
    crozier()
        .arg("--version")
        .assert()
        .success()
        .stdout(predicate::str::contains(env!("CARGO_PKG_VERSION")));
}

/// A spec that is *not* in the Fern corpus, exercising a schema-only object, an
/// enum, an array field, and an endpoint — and crucially declaring **no** error
/// responses, the shape that once emitted an empty `from .errors import` (invalid
/// Python that byte-matching the two golden corpora never exercised). The title
/// has spaces so the default-naming path snake_cases it to `my_cool_api`.
const ARBITRARY_SPEC: &str = "\
openapi: 3.0.0
info:
  title: My Cool API
  version: 2.3.0
paths:
  /widgets/{id}:
    get:
      operationId: getWidget
      tags: [Widgets]
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Widget' }
components:
  schemas:
    Widget:
      type: object
      properties:
        id: { type: string }
        tags:
          type: array
          items: { type: string }
    Color:
      type: string
      enum: [red, green, blue]
";

/// Locate a Python interpreter for the "generated SDK is valid Python" checks.
/// GitHub's ubuntu/macos/windows runners all ship one, so the gate always runs
/// it; a sandbox without Python skips (as the coverage tier does — see
/// docs/matching.md) rather than failing spuriously.
fn python_interpreter() -> Option<&'static str> {
    ["python3", "python"].into_iter().find(|candidate| {
        std::process::Command::new(candidate)
            .arg("--version")
            .stdout(std::process::Stdio::null())
            .stderr(std::process::Stdio::null())
            .status()
            .map(|s| s.success())
            .unwrap_or(false)
    })
}

/// Byte-check is text equality; this asserts the generated tree is *valid Python*
/// by compiling every module (`compileall`). Byte-matching Fern proves the two
/// corpora; this proves crozier does not emit syntactically broken Python for
/// specs outside them.
fn assert_valid_python(out: &Path) {
    let Some(py) = python_interpreter() else {
        eprintln!("skipping Python validity check: no python3/python on PATH");
        return;
    };
    let status = std::process::Command::new(py)
        .args(["-m", "compileall", "-q", "-f"])
        .arg(out)
        .status()
        .expect("run python -m compileall");
    assert!(
        status.success(),
        "generated Python under {} failed to compile with {py}",
        out.display()
    );
}

/// The venv interpreter path for a given venv root, across platforms.
fn venv_python(venv: &Path) -> PathBuf {
    if cfg!(windows) {
        venv.join("Scripts").join("python.exe")
    } else {
        venv.join("bin").join("python")
    }
}

/// Whether `uv` (the fast installer) is on PATH.
fn uv_available() -> bool {
    std::process::Command::new("uv")
        .arg("--version")
        .stdout(std::process::Stdio::null())
        .stderr(std::process::Stdio::null())
        .status()
        .map(|s| s.success())
        .unwrap_or(false)
}

/// Whether `py` can import the generated SDK's runtime dependencies plus the test
/// runner (`pytest`) the wire suite is driven with.
fn can_import_sdk_deps(py: &Path) -> bool {
    std::process::Command::new(py)
        .args(["-c", "import httpx, pydantic, pytest"])
        .stdout(std::process::Stdio::null())
        .stderr(std::process::Stdio::null())
        .status()
        .map(|s| s.success())
        .unwrap_or(false)
}

/// Prepare (creating and caching if needed) a virtualenv holding the generated
/// SDK's runtime dependencies (`httpx`, `pydantic`) and `pytest`, and return its
/// interpreter, so the runtime wire suite can import and drive a generated
/// client. Returns an `Err` describing why the env could not be prepared — no
/// base interpreter, no venv support, or a failed dependency install (e.g.
/// offline) — which the caller turns into a skip locally / a hard failure in CI.
///
/// The venv is cached under the system temp dir and reused whenever it already
/// imports the dependencies, so repeated `just check` runs pay the install once.
/// `uv` is used when present (seconds); otherwise the stdlib `venv` + `pip`.
fn runtime_python_env() -> Result<PathBuf, String> {
    // The SDK's own runtime deps plus the wire suite's test runner.
    const DEPS: [&str; 3] = ["httpx", "pydantic", "pytest"];
    let base = python_interpreter().ok_or("no python3/python on PATH")?;
    let venv = std::env::temp_dir().join("crozier-runtime-venv-v2");
    let venv_py = venv_python(&venv);

    if venv_py.exists() && can_import_sdk_deps(&venv_py) {
        return Ok(venv_py);
    }

    let run = |mut cmd: std::process::Command, what: &str| -> Result<(), String> {
        let output = cmd
            .output()
            .map_err(|e| format!("failed to spawn {what}: {e}"))?;
        if output.status.success() {
            return Ok(());
        }
        Err(format!(
            "{what} failed:\n{}",
            String::from_utf8_lossy(&output.stderr)
        ))
    };

    if uv_available() {
        let mut venv_cmd = std::process::Command::new("uv");
        venv_cmd.arg("venv").arg(&venv);
        run(venv_cmd, "uv venv")?;
        let mut install = std::process::Command::new("uv");
        install
            .args(["pip", "install", "--python"])
            .arg(&venv_py)
            .args(DEPS);
        run(install, "uv pip install")?;
    } else {
        let mut venv_cmd = std::process::Command::new(base);
        venv_cmd.args(["-m", "venv"]).arg(&venv);
        run(venv_cmd, "python -m venv")?;
        let mut install = std::process::Command::new(&venv_py);
        install.args(["-m", "pip", "install"]).args(DEPS);
        run(install, "pip install")?;
    }

    if can_import_sdk_deps(&venv_py) {
        Ok(venv_py)
    } else {
        Err("venv prepared but httpx/pydantic/pytest still not importable".into())
    }
}

/// Runtime ("wire") behavior of a generated SDK, verified **differentially
/// against Fern**: byte-matching Fern proves the source is right and
/// `assert_valid_python` proves it compiles, but neither proves the compiled
/// client issues the right HTTP request or parses the response. Rather than
/// hand-author the expected behavior, this derives it from Fern: the committed
/// pytest suite ([`tests/runtime/test_wire.py`]) records the client's behavior
/// (via an injected `httpx.MockTransport`) for **both** the committed Fern fixture
/// SDK (`exhaustive/expected/src`, real runnable Fern output) and the
/// crozier-generated SDK, and asserts — per journey — that the recordings match.
///
/// Each journey captures the outgoing request (method, URL, headers, serialized
/// body) and the outcome (the response model dumped to a dict, or the typed
/// error's class/status/body) — covering request construction, auth + SDK-identity
/// headers, body field-aliasing and `OMIT` filtering, query encoding, typed
/// pydantic deserialization, and typed error raising, sync and async. The *only*
/// allowed difference is the deliberate SDK-identity branding (`X-Crozier-*` vs
/// `X-Fern-*`), which the recorder folds to a common prefix on both sides. It
/// omits Fern 5.20's Runtime/Platform identity pair because the runnable
/// `exhaustive` fixture predates them; managed 5.20 byte fixtures gate those lines
/// exactly. This is the in-process analog of Fern's own WireMock
/// wire tests (Docker/Enterprise-gated output crozier does not emit). This test
/// drives the compiled binary and the compiled client, so it lives in the e2e
/// tier. See docs/matching.md.
#[test]
fn crozier_matches_fern_runtime_behavior() {
    let out = tempfile::tempdir().expect("tempdir");
    let spec = fixture_dir("exhaustive").join("openapi.yml");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(out.path())
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ])
        .assert()
        .success();

    let py = match runtime_python_env() {
        Ok(py) => py,
        Err(reason) => {
            // Keep the gate honest in CI (its runners ship Python and have
            // network) while letting a restricted local sandbox skip — the same
            // posture as the Python-validity check above.
            if std::env::var_os("CI").is_some() {
                panic!("runtime wire tests require a Python env, unavailable in CI: {reason}");
            }
            eprintln!("skipping SDK runtime tests: {reason}");
            return;
        }
    };

    let runtime_dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/runtime");
    let fern_src = fixture_dir("exhaustive").join("expected/src");
    let output = std::process::Command::new(&py)
        .args(["-m", "pytest", "-q", "-p", "no:cacheprovider"])
        .arg(&runtime_dir)
        // FERN_SDK_SRC supplies the derived-from-Fern expectations; CROZIER_SDK_SRC
        // is the SDK under test. Keep the repo tree clean of pytest byte-caches.
        .env("FERN_SDK_SRC", &fern_src)
        .env("CROZIER_SDK_SRC", out.path().join("src"))
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output()
        .expect("run the runtime wire-test suite (pytest)");
    assert!(
        output.status.success(),
        "runtime wire tests failed (crozier's client behaves differently from \
         Fern's beyond the normalized SDK-identity headers):\n{}{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr),
    );
}

#[test]
fn arbitrary_spec_generates_valid_python() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, ARBITRARY_SPEC).unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "acme"])
        .assert()
        .success();
    assert_valid_python(&out);
}

/// Generate from `spec`, asserting success, and return the output directory
/// (kept alive by the returned `TempDir`). Shared by the issue-#40 real-world
/// regression tests below.
fn generate_ok(spec: &str) -> (tempfile::TempDir, std::path::PathBuf) {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(&path, spec).unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&path)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "acme"])
        .assert()
        .success();
    assert_valid_python(&out);
    (dir, out)
}

#[test]
fn hyphenated_operation_id_generates_valid_python() {
    // Issue #40 case 1a: a hyphen in the operationId once produced a module dir
    // and identifiers that failed to parse. It must sanitize to a legal name.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: get-all-widgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: \
         { type: string } } } } }\n",
    );
    assert!(
        out.join("src/acme/widgets").is_dir(),
        "a groupless operationId is grouped by its tag into a legal module directory"
    );
}

#[test]
fn paths_level_extension_generates_valid_python() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  \
         x-codegen-contextRoot: /api/v1\n  /widgets:\n    get:\n      operationId: listWidgets\n      \
         tags: [widgets]\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n  /groups:\n    get:\n      \
         operationId: GroupV2.GetGroups\n      tags: [GroupV2]\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    assert!(
        out.join("src/acme/widgets").is_dir(),
        "paths-level x-* extensions are metadata, not API paths"
    );
}

#[test]
fn spaced_operation_id_generates_valid_python() {
    // Issue #40 case 1b: a space in the operationId.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /verify:\n    \
         post:\n      operationId: verify code\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: object, \
         properties: { ok: { type: boolean } } } } } }\n",
    );
    assert!(
        out.join("src/acme/widgets").is_dir(),
        "a spaced operationId is grouped by its tag into a legal module directory"
    );
    // The method identifier itself is sanitized to snake_case.
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("def verify_code("),
        "spaced id → verify_code method: {raw}"
    );
}

#[test]
fn empty_dotted_operation_namespace_overwrites_the_root_surface() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      operationId: .ListWidgets\n      responses:\n        '200':\n          description: OK\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n                  count: { type: integer }\n",
    );
    assert!(
        !out.join("src/acme/_").exists(),
        "an explicit empty namespace must not invent an underscore package"
    );
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    let raw = std::fs::read_to_string(out.join("src/acme/raw_client.py"))
        .expect("root raw client is generated");
    let init = std::fs::read_to_string(out.join("src/acme/__init__.py"))
        .expect("package initializer is generated");
    assert!(
        client.contains("class Client:")
            && client.contains("def listwidgets(")
            && !client.contains("class AcmeApi:")
            && raw.contains("class RawClient:")
            && out
                .join("src/acme/types/list_widgets_response.py")
                .is_file()
            && init.contains("ListWidgetsResponse")
            && !init.contains("AcmeApi")
            && !init.contains("__version__"),
        "Fern's empty tag package should overwrite the ordinary root files: {client}\n{init}"
    );
}

#[test]
fn digit_leading_property_gets_f_prefix_and_alias() {
    // Issue #40 case 2: a property name starting with a digit is not a legal
    // identifier. Fern renames it `f_<name>` and keeps the wire name as an alias.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /thing:\n    \
         get:\n      operationId: getThing\n      responses:\n        '200': { description: OK, \
         content: { application/json: { schema: { $ref: '#/components/schemas/Thing' } } } }\n\
         components:\n  schemas:\n    Thing:\n      type: object\n      properties:\n        \
         \"2fa_enabled\": { type: boolean }\n",
    );
    let thing = std::fs::read_to_string(out.join("src/acme/types/thing.py"))
        .expect("Thing model is generated");
    assert!(
        thing.contains("f_2fa_enabled"),
        "digit-leading property should be renamed to f_2fa_enabled: {thing}"
    );
    assert!(
        thing.contains("FieldMetadata(alias=\"2fa_enabled\")"),
        "the wire name should be preserved as a FieldMetadata alias: {thing}"
    );
}

#[test]
fn digit_leading_schema_name_generates_valid_python() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: 5G API, version: 1.0.0 }\npaths:\n  /cause:\n    \
         get:\n      operationId: getCause\n      responses:\n        '200': { description: OK, \
         content: { application/json: { schema: { $ref: '#/components/schemas/5GmmCause' } } } }\n\
         components:\n  schemas:\n    5GmmCause:\n      type: object\n      properties:\n        \
         code: { type: integer }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/five_gmm_cause.py"))
        .expect("digit-leading schema model is generated");
    assert!(
        model.contains("class FiveGmmCause(UniversalBaseModel):"),
        "digit-leading schema should become a legal Python class: {model}"
    );
    assert_valid_python(&out);
}

#[test]
fn numeric_field_segments_collapse_and_keep_wire_aliases() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [day_0_end_time]\n                properties:\n                  day_0_end_time: { type: integer }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("response model is generated");
    assert!(
        model.contains("day0end_time: typing_extensions.Annotated[")
            && model.contains("FieldMetadata(alias=\"day_0_end_time\")")
            && model.contains("pydantic.Field(alias=\"day_0_end_time\")"),
        "numeric segments should collapse while preserving the wire alias: {model}"
    );
}

#[test]
fn bracketed_property_names_generate_valid_python() {
    // Issue #74: bracketed JSON:API / Rails / Stripe params (`filter[name]`,
    // `page[size]`) aren't legal identifiers. crozier once emitted them verbatim
    // as function parameters, so `ruff format` refused to parse the file and the
    // whole SDK was discarded. Both the query params and the urlencoded form-body
    // properties must sanitize to legal snake_case identifiers while keeping the
    // raw bracketed name as the wire key. `generate_ok` compiles every module, so
    // reaching this point already proves the output parses.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  \
         /widgets/search:\n    post:\n      operationId: searchWidgets\n      tags: [widgets]\n      \
         parameters:\n        - { name: \"page[size]\", in: query, required: false, schema: { type: \
         integer } }\n      requestBody:\n        content:\n          application/x-www-form-urlencoded:\n            \
         schema:\n              type: object\n              properties:\n                \"filter[name]\": { type: \
         string }\n                \"filter[color]\": { type: string }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: object, properties: \
         { count: { type: integer } } } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    // The parameters are legal identifiers...
    assert!(
        raw.contains("filter_name:") && raw.contains("filter_color:") && raw.contains("page_size:"),
        "bracketed params should fold to snake_case identifiers: {raw}"
    );
    // ...while the raw bracketed name stays the wire serialization key.
    assert!(
        raw.contains("\"filter[name]\": filter_name") && raw.contains("\"page[size]\": page_size"),
        "the raw bracketed name should remain the wire key: {raw}"
    );
    // The broken form must be gone entirely.
    assert!(
        !raw.contains("filter[name]:"),
        "the illegal `filter[name]` identifier must not appear: {raw}"
    );
}

#[test]
fn enum_sanitization_generates_valid_python() {
    // Issue #50: enum member names and `visit()` parameters are derived from the
    // raw wire values, so a value that is not already a bare identifier once
    // produced Python that failed the final `ruff format` and discarded the whole
    // SDK. This spec packs the crashing shapes into one enum — a Python keyword
    // (`global`), punctuation + a leading digit (`0: Active`), and the
    // digit-leading value `_01_00_AM` that Fern itself rejects (so it has no
    // byte-match fixture) — plus a `type: string` enum whose values are all
    // integers. Generation must succeed and every module must compile.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        \
         - { name: size, in: query, required: false, schema: { type: string, enum: [100, 125] } }\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: \
         { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  schemas:\n    Widget:\n      \
         type: object\n      properties:\n        scope: { $ref: '#/components/schemas/WidgetScope' }\n        \
         hour: { $ref: '#/components/schemas/WidgetHour' }\n    WidgetScope:\n      type: string\n      \
         enum: [\"global\", \"practice\"]\n    WidgetHour:\n      type: string\n      \
         enum: [\"_01_00_AM\", \"_12_00_PM\"]\n",
    );
    // The keyword value's `visit` parameter is keyword-escaped, and the leading
    // digit that Fern rejects is prefixed into a legal identifier by crozier.
    let scope = std::fs::read_to_string(out.join("src/acme/types/widget_scope.py"))
        .expect("WidgetScope enum is generated");
    assert!(
        scope.contains("global_: typing.Callable"),
        "keyword value → keyword-escaped visit param: {scope}"
    );
    let hour = std::fs::read_to_string(out.join("src/acme/types/widget_hour.py"))
        .expect("WidgetHour enum is generated");
    assert!(
        hour.contains("_01_00_AM = \"_01_00_AM\""),
        "digit-leading member is prefixed into a legal identifier: {hour}"
    );
    // The type-mismatched enum (string type, integer values) drops its members and
    // falls back to the base `str` type rather than emitting an empty enum class.
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("size: typing.Optional[str] = None"),
        "a type-mismatched string enum falls back to str: {raw}"
    );
}

#[test]
fn omitted_schema_type_infers_enum_and_open_map_shapes() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\n\
         components:\n  schemas:\n    Widget:\n      type: object\n      required: [kind, target]\n      \
         properties:\n        kind: { enum: [tag, digest] }\n        target: { additionalProperties: true }\n        \
         extra: {}\n",
    );
    let widget = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("Widget model is generated");
    assert!(
        widget.contains("from .widget_kind import WidgetKind"),
        "an enum without an explicit type should be hoisted as a string enum: {widget}"
    );
    assert!(
        widget.contains("kind: WidgetKind"),
        "the required no-type enum field should reference the hoisted enum: {widget}"
    );
    assert!(
        widget.contains("target: typing.Dict[str, typing.Any]"),
        "Fern 5.20 keeps an unconstrained open-map value bare: {widget}"
    );
    assert!(
        widget.contains("extra: typing.Optional[typing.Any] = None"),
        "an unknown optional field keeps Fern's existing single-optional annotation: {widget}"
    );
}

#[test]
fn unknown_metadata_fields_are_single_optional() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  \
         schemas:\n    Widget:\n      type: object\n      properties:\n        metadata: {}\n        unknown: {}\n",
    );
    let widget =
        std::fs::read_to_string(out.join("src/acme/types/widget.py")).expect("Widget model");
    assert!(
        widget.contains("metadata: typing.Optional[typing.Any] = None"),
        "Fern 5.20 models field absence once around unknown metadata: {widget}"
    );
    assert!(
        widget.contains("unknown: typing.Optional[typing.Any] = None"),
        "ordinary unknown fields should keep the existing single optional annotation: {widget}"
    );
}

#[test]
fn slash_only_server_url_generates_empty_default_environment() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nservers:\n  - url: /\npaths:\n  \
         /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    let environment = std::fs::read_to_string(out.join("src/acme/environment.py"))
        .expect("environment module is generated");
    assert!(
        environment.contains("DEFAULT = \"\""),
        "a slash-only server URL should match Fern's empty default environment: {environment}"
    );
}

#[test]
fn examples_use_one_line_client_constructor_when_no_args_are_needed() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nservers:\n  - url: /\npaths:\n  \
         /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("client = AcmeApi()"),
        "no-argument examples should use Fern's one-line constructor: {client}"
    );
    let root =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    assert!(
        root.contains("client = AcmeApi()"),
        "root client examples should use Fern's one-line constructor: {root}"
    );
}

#[test]
fn mixed_error_body_shapes_downgrade_status_class_to_any() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: { type: string } } } } }\n        \
         '400': { description: Bad request }\n  /gadgets:\n    get:\n      operationId: listGadgets\n      \
         tags: [gadgets]\n      responses:\n        '200': { description: OK, content: { application/json: { schema: { \
         type: array, items: { type: string } } } } }\n        '400': { description: Bad request, content: { \
         application/json: { schema: { $ref: '#/components/schemas/ErrorBody' } } } }\ncomponents:\n  schemas:\n    \
         ErrorBody:\n      type: object\n      properties:\n        message: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/gadgets/raw_client.py"))
        .expect("gadgets raw client is generated");
    assert!(
        raw.contains("type_=typing.Any"),
        "a status class with any bodyless response should parse every branch as Any: {raw}"
    );
    let error = std::fs::read_to_string(out.join("src/acme/errors/bad_request_error.py"))
        .expect("BadRequestError is generated");
    assert!(
        error.contains("body: typing.Any"),
        "the generated error class should also accept Any: {error}"
    );
}

#[test]
fn conflicting_error_body_types_downgrade_status_class_to_any() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      responses:\n        '204': { description: Created }\n        '409': { description: Conflict, content: { application/json: { schema: { $ref: '#/components/schemas/WidgetConflict' } } } }\n  /gadgets:\n    post:\n      operationId: createGadget\n      tags: [gadgets]\n      responses:\n        '204': { description: Created }\n        '409': { description: Conflict, content: { application/json: { schema: { $ref: '#/components/schemas/GadgetConflict' } } } }\ncomponents:\n  schemas:\n    WidgetConflict: { type: object, properties: { message: { type: string } } }\n    GadgetConflict: { type: object, properties: { reason: { type: string } } }\n",
    );
    let error = std::fs::read_to_string(out.join("src/acme/errors/conflict_error.py"))
        .expect("ConflictError is generated");
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        error.contains("body: typing.Any") && raw.contains("type_=typing.Any"),
        "a shared status with conflicting body schemas should use Any:\n{error}\n{raw}"
    );
}

#[test]
fn endpoint_docstrings_preserve_literal_backslashes() {
    let (_dir, out) = generate_ok(
        r#"openapi: 3.0.3
info: { title: Widget API, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: listWidgets
      tags: [widgets]
      description: |
        Read C:\temp before continuing with curl \
      responses:
        '204': { description: Done }
"#,
    );
    for file in [
        "src/acme/widgets/client.py",
        "src/acme/widgets/raw_client.py",
    ] {
        let generated = std::fs::read_to_string(out.join(file)).expect("client is generated");
        assert!(
            generated.contains(r"Read C:\\temp before continuing with curl \\"),
            "Python docstrings must escape literal backslashes in {file}:\n{generated}"
        );
    }
}

#[test]
fn unknown_array_items_are_bare_any_elements() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\n\
         components:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        values: { \
         type: array, items: {} }\n",
    );
    let widget = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("Widget model is generated");
    assert!(
        widget.contains("values: typing.Optional[typing.List[typing.Any]] = None"),
        "Fern 5.20 keeps unknown array elements intrinsically non-nullable: {widget}"
    );
}

#[test]
fn array_item_enums_hoist_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        - name: \
         status\n          in: query\n          required: false\n          explode: false\n          schema:\n            type: array\n            \
         items: { type: string, enum: [active, archived] }\n      responses:\n        '200':\n          \
         description: OK\n          content:\n            application/json:\n              schema:\n                \
         type: array\n                items: { type: string, enum: [public, private] }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        client.contains(
            "from .types.list_widgets_request_status_item import ListWidgetsRequestStatusItem"
        ),
        "query array item enums should be imported as tag-scoped types: {client}"
    );
    assert!(
        client.contains("from .types.list_widgets_response_item import ListWidgetsResponseItem"),
        "response array item enums should be imported as tag-scoped types: {client}"
    );
    assert!(
        client.contains(
            "typing.Union[ListWidgetsRequestStatusItem, typing.Sequence[ListWidgetsRequestStatusItem]]"
        ),
        "query array item enums should use the named enum in scalar-or-sequence params: {client}"
    );
    assert!(
        raw.contains("\",\".join(map(str, status)) if isinstance(status"),
        "explode=false query arrays should serialize as one comma-separated value: {raw}"
    );
    assert!(
        client.contains("typing.List[ListWidgetsResponseItem]"),
        "response array item enums should use the named enum in return types: {client}"
    );
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference.md is generated");
    assert!(
        reference.contains(
            "**status:** `typing.Optional[typing.Union[ListWidgetsRequestStatusItem, typing.Sequence[ListWidgetsRequestStatusItem]]]`"
        ),
        "reference tables should preserve Fern 5.20's flat scalar-or-sequence annotation: {reference}"
    );
}

#[test]
fn path_parameter_enums_hoist_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{state}:\n    delete:\n      operationId: deleteWidget\n      tags: [widgets]\n      parameters:\n        - name: state\n          in: path\n          required: true\n          schema: { type: string, enum: [ACTIVE, DISABLED] }\n      responses:\n        '204': { description: Deleted }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        out.join("src/acme/widgets/types/delete_widget_request_state.py")
            .is_file()
            && raw.contains(
                "from .types.delete_widget_request_state import DeleteWidgetRequestState"
            )
            && raw.contains("state: DeleteWidgetRequestState"),
        "inline path enums should hoist under the endpoint tag: {raw}"
    );
}

#[test]
fn referenced_parameter_examples_populate_worked_calls() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { $ref: '#/components/schemas/WidgetId' } }\n        - { name: X-Mode, in: header, required: true, schema: { $ref: '#/components/schemas/Mode' } }\n      responses:\n        '204': { description: Found }\ncomponents:\n  schemas:\n    WidgetId: { type: string, example: '\"widget-123\"' }\n    Mode: { type: string, example: 'safe' }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("id='\"widget-123\"'") && client.contains("mode=\"safe\""),
        "examples on referenced parameter schemas should populate worked calls: {client}"
    );
}

#[test]
fn referenced_query_examples_populate_worked_calls() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        - { name: mode, in: query, schema: { $ref: '#/components/schemas/WidgetMode' } }\n      responses:\n        '204': { description: Found }\ncomponents:\n  schemas:\n    WidgetMode: { type: string, example: FAST }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("mode=\"FAST\""),
        "examples on referenced query schemas should populate worked calls: {client}"
    );
}

#[test]
fn declared_tag_labels_are_preserved_in_reference_headings() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\ntags:\n  - { name: 'Widget rules' }\npaths:\n  /rules:\n    get:\n      operationId: listWidgetRules\n      tags: ['Widget rules']\n      responses:\n        '204': { description: Found }\n",
    );
    let reference = std::fs::read_to_string(out.join("reference.md"))
        .expect("reference documentation is generated");
    assert!(
        reference.contains("## Widget rules"),
        "declared tag labels should remain verbatim in headings: {reference}"
    );
}

#[test]
fn reference_preserves_terminal_description_paragraphs() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      description: |+\n        Creates a widget.\n\n      responses:\n        '204': { description: Created }\n",
    );
    let reference = std::fs::read_to_string(out.join("reference.md"))
        .expect("reference documentation is generated");
    assert!(
        reference.contains("Creates a widget.\n\n</dd>"),
        "terminal description paragraphs should remain in reference docs: {reference}"
    );
}

#[test]
fn readme_skips_binary_endpoints_for_worked_examples() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /upload:\n    post:\n      operationId: uploadWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/octet-stream:\n            schema: { type: string, format: binary }\n      responses:\n        '204': { description: Uploaded }\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              properties:\n                name: { type: string }\n              required: [name]\n      responses:\n        '204': { description: Created }\n",
    );
    let readme = std::fs::read_to_string(out.join("README.md")).expect("README is generated");
    assert!(
        readme.contains("client.widgets.create_widget("),
        "README should use the first example-capable endpoint: {readme}"
    );
}

#[test]
fn readme_marks_referenced_object_bodies_as_complex() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\ncomponents:\n  schemas:\n    CreateWidget:\n      type: object\n      description: A widget creation request.\n      example: { name: example }\n      properties:\n        name: { type: string }\n        note: { type: string }\n      required: [name]\n",
    );
    let readme = std::fs::read_to_string(out.join("README.md")).expect("README is generated");
    assert!(
        readme.contains("client.widgets.create_widget(...)")
            && readme.contains("with_raw_response.create_widget(...)"),
        "referenced object bodies should be complex in abbreviated calls: {readme}"
    );
    let raw_client = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("raw client is generated");
    assert!(
        !raw_client.contains("\"content-type\": \"application/json\""),
        "example-backed optional bodies should leave content type to the transport: {raw_client}"
    );
}

#[test]
fn inline_response_array_objects_hoist_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [items]\n                properties:\n                  items:\n                    type: array\n                    items:\n                      type: object\n                      required: [id, details]\n                      properties:\n                        id: { type: integer }\n                        details:\n                          type: object\n                          required: [name]\n                          properties:\n                            name: { type: string }\n",
    );
    let response =
        std::fs::read_to_string(out.join("src/acme/widgets/types/list_widgets_response.py"))
            .expect("inline response wrapper is generated");
    assert!(
        response.contains("typing.List[ListWidgetsResponseItemsItem]"),
        "array items should use their coined model: {response}"
    );
    let item = std::fs::read_to_string(
        out.join("src/acme/widgets/types/list_widgets_response_items_item.py"),
    )
    .expect("inline array item model is generated");
    assert!(
        item.contains("details: ListWidgetsResponseItemsItemDetails"),
        "nested inline objects should retain the item context: {item}"
    );
}

#[test]
fn openapi_31_null_types_generate_optional_fields() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [name]\n                properties:\n                  name: { type: [string, 'null'] }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("inline response model is generated");
    assert!(
        model.contains("name: typing.Optional[str] = None"),
        "3.1 null unions should produce optional fields: {model}"
    );
}

#[test]
fn openapi_31_null_only_array_items_collapse_to_bare_any() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [values]\n                properties:\n                  values:\n                    type: array\n                    items: { type: ['null'] }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("inline response model is generated");
    assert!(
        model.contains("values: typing.List[typing.Any]"),
        "Fern 5.20 collapses null-only array elements to bare unknowns: {model}"
    );
}

#[test]
fn arrays_without_items_use_bare_any_elements() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [values]\n                properties:\n                  values: { type: array }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("inline response model is generated");
    assert!(
        model.contains("values: typing.List[typing.Any]"),
        "Fern 5.20 keeps unconstrained array elements as bare unknowns: {model}"
    );
}

#[test]
fn inline_request_enums_generate_emittable_clients() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              type: object\n              required: [mode]\n              properties:\n                mode: { type: string, enum: [FAST, SAFE] }\n      responses:\n        '204': { description: Created }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("client with an inline request enum is generated");
    assert!(
        raw.contains("mode: CreateWidgetRequestMode"),
        "request field should use its coined enum: {raw}"
    );
    assert!(
        out.join("src/acme/widgets/types/create_widget_request_mode.py")
            .is_file(),
        "request-scoped enum module should be emitted"
    );
}

#[test]
fn multipart_request_enums_hoist_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          multipart/form-data:\n            schema:\n              type: object\n              required: [mode]\n              properties:\n                mode: { type: string, enum: [FAST, SAFE] }\n                file: { type: string, format: binary }\n      responses:\n        '204': { description: Created }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("multipart client is generated");
    assert!(
        raw.contains("mode: CreateWidgetRequestMode"),
        "multipart enum should use its coined type: {raw}"
    );
    assert!(out
        .join("src/acme/widgets/types/create_widget_request_mode.py")
        .is_file());
}

#[test]
fn short_multiple_request_enum_imports_stay_flat() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              required: [mode, status]\n              properties:\n                mode: { type: string, enum: [FAST, SAFE] }\n                status: { type: string, enum: [ACTIVE, PAUSED] }\n      responses:\n        '204': { description: Created }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains(
            "from acme.widgets import CreateWidgetRequestMode, CreateWidgetRequestStatus"
        ),
        "tag-scoped example imports within 88 columns should stay flat: {client}"
    );
}

#[test]
fn multipart_unknown_fields_model_only_field_absence_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /uploads:\n    post:\n      operationId: createUpload\n      tags: [uploads]\n      requestBody:\n        content:\n          multipart/form-data:\n            schema:\n              type: object\n              properties:\n                file: {}\n      responses:\n        '204': { description: Created }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/uploads/client.py"))
        .expect("multipart client is generated");
    assert!(
        client.contains("file: typing.Optional[typing.Any] = OMIT"),
        "an omittable unknown form field should model absence only once: {client}"
    );
}

#[test]
fn request_array_examples_are_used_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidgets\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              required: [ids]\n              properties:\n                ids:\n                  type: array\n                  examples: [[1, 2, 3]]\n      responses:\n        '204': { description: Created }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("ids=[1, 2, 3]"),
        "a required array should use its explicit schema example: {client}"
    );
}

#[test]
fn top_level_inline_response_array_items_hoist_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: array\n                items:\n                  type: object\n                  required: [id]\n                  properties:\n                    id: { type: integer }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("client is generated");
    assert!(
        client.contains("typing.List[ListWidgetsResponseItem]"),
        "top-level response arrays should use their coined item model: {client}"
    );
    assert!(
        out.join("src/acme/widgets/types/list_widgets_response_item.py")
            .is_file(),
        "response item module should be emitted"
    );
}

#[test]
fn closed_empty_inline_objects_hoist_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [metadata]\n                properties:\n                  metadata:\n                    type: object\n                    properties: {}\n                    additionalProperties: false\n",
    );
    let response =
        std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
            .expect("response model is generated");
    assert!(
        response.contains("metadata: GetWidgetResponseMetadata"),
        "closed empty objects should use a coined model: {response}"
    );
    assert!(
        out.join("src/acme/widgets/types/get_widget_response_metadata.py")
            .is_file(),
        "closed empty object model should be emitted"
    );
}

#[test]
fn operation_id_equal_to_tag_generates_on_root_client() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /search:\n    get:\n      operationId: search\n      tags: [Search]\n      description: |\n        Search help.\n\n        ```sh\n        echo search\n        ```\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [result]\n                properties:\n                  result:\n                    type: object\n                    required: [count]\n                    properties:\n                      count: { type: integer }\n  /health:\n    get:\n      operationId: getHealth\n      tags: [System]\n      responses:\n        '204': { description: Healthy }\n",
    );
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    assert!(
        client.contains("def search(") && !client.contains("def search(self):"),
        "an operation named exactly for its tag should remain a root method: {client}"
    );
    assert!(
        !client.contains("OMIT ="),
        "a root client with no request body should not declare OMIT: {client}"
    );
    assert!(
        client.contains("```sh\n        echo search\n        ```\n        \n"),
        "fenced root method docstrings should preserve Fern's blank indentation: {client}"
    );
    assert!(out.join("src/acme/raw_client.py").is_file());
    assert!(out.join("src/acme/types/search_response.py").is_file());
    assert!(out
        .join("src/acme/types/search_response_result.py")
        .is_file());
    let response = std::fs::read_to_string(out.join("src/acme/types/search_response.py"))
        .expect("root response model is generated");
    assert!(
        response.contains("from ..core.pydantic_utilities import"),
        "root response types should use root-relative imports: {response}"
    );
    let package = std::fs::read_to_string(out.join("src/acme/__init__.py"))
        .expect("package initializer is generated");
    assert!(
        package.contains("\"SearchResponse\": \".types\"")
            && package.contains("from .types import SearchResponse"),
        "root-hoisted types should export through the root types package: {package}"
    );
}

#[test]
fn header_parameter_enums_hoist_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      parameters:\n        - name: X-Widget-Mode\n          in: header\n          required: true\n          schema: { type: string, enum: [FAST, SAFE] }\n      responses:\n        '204': { description: Created }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        out.join("src/acme/widgets/types/create_widget_request_x_widget_mode.py")
            .is_file()
            && raw.contains("CreateWidgetRequestXWidgetMode")
            && raw.contains(
                "\"X-Widget-Mode\": widget_mode.value if widget_mode is not None else None"
            ),
        "inline header enums should hoist under the endpoint tag: {raw}"
    );
}

#[test]
fn referenced_unknown_response_keeps_empty_body_guard() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Proxy API, version: 1.0.0 }\npaths:\n  /proxy:\n    get:\n      operationId: getProxy\n      tags: [proxy]\n      responses:\n        '200': { $ref: '#/components/responses/Ok' }\ncomponents:\n  responses:\n    Ok:\n      description: Arbitrary JSON\n      content:\n        application/json:\n          schema: {}\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/proxy/raw_client.py"))
        .expect("proxy raw client is generated");
    assert!(raw.contains("HttpResponse[typing.Any]"), "{raw}");
    assert!(
        raw.contains("if _response is None or not _response.text.strip():"),
        "a referenced unknown response keeps Fern's empty-body guard: {raw}"
    );
}

#[test]
fn inherited_union_discriminants_are_not_duplicated_in_wrappers() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Exchange API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    AbstractExchange:\n      type: object\n      required: [type]\n      properties:\n        type: { type: string, enum: [reqRespPair, unidirEvent] }\n    RequestResponsePair:\n      type: object\n      allOf:\n        - type: object\n          required: [request]\n          properties:\n            request: { type: string }\n        - { $ref: '#/components/schemas/AbstractExchange' }\n    UnidirectionalEvent:\n      type: object\n      allOf:\n        - type: object\n          required: [eventMessage]\n          properties:\n            eventMessage: { type: string }\n        - { $ref: '#/components/schemas/AbstractExchange' }\n    Exchange:\n      oneOf:\n        - { $ref: '#/components/schemas/RequestResponsePair' }\n        - { $ref: '#/components/schemas/UnidirectionalEvent' }\n      discriminator:\n        propertyName: type\n        mapping:\n          reqRespPair: '#/components/schemas/RequestResponsePair'\n          unidirEvent: '#/components/schemas/UnidirectionalEvent'\n",
    );
    let exchange = std::fs::read_to_string(out.join("src/acme/types/exchange.py"))
        .expect("discriminated union is generated");
    assert_eq!(
        exchange.matches("\n    type:").count(),
        2,
        "each wrapper should contain only its literal discriminator: {exchange}"
    );
    assert!(
        !exchange.contains("AbstractExchangeType"),
        "the inherited enum discriminator must not be re-added: {exchange}"
    );
}

#[test]
fn binary_success_responses_stream_bytes() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/download:\n    \
         get:\n      operationId: downloadWidget\n      tags: [widgets]\n      parameters:\n        - name: id\n          \
         in: path\n          required: true\n          schema: { type: string }\n      responses:\n        '200':\n          \
         description: Widget archive\n          content:\n            application/octet-stream:\n              \
         schema: { type: string, format: binary }\n        '500': { description: Broken }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("@contextlib.contextmanager")
            && raw.contains("self._client_wrapper.httpx_client.stream(")
            && raw.contains("typing.Iterator[HttpResponse[typing.Iterator[bytes]]]")
            && raw.contains("_response.iter_bytes(chunk_size=_chunk_size)"),
        "binary responses should stream bytes from the raw client: {raw}"
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains(") -> typing.Iterator[bytes]:")
            && client.contains("with self._raw_client.download_widget(")
            && client.contains("yield from r.data"),
        "high-level binary response methods should yield bytes from the raw stream: {client}"
    );
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference.md is generated");
    assert!(
        reference.contains(
            "**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration."
        ),
        "binary response reference docs should use Fern 5.20's standard request_options prose: {reference}"
    );
}

#[test]
fn referenced_binary_success_responses_stream_bytes() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /export:\n    get:\n      operationId: exportWidgets\n      tags: [widgets]\n      description: Exports all widgets.\n      responses:\n        '200':\n          description: Export\n          content:\n            application/zip:\n              schema: { $ref: '#/components/schemas/FileContent' }\ncomponents:\n  schemas:\n    FileContent: { type: string, format: binary }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("@contextlib.contextmanager")
            && raw.contains("typing.Iterator[HttpResponse[typing.Iterator[bytes]]]")
            && raw.contains("httpx_client.stream(")
            && !raw.contains("import FileContent")
            && raw.contains("        Exports all widgets.\n\n        Parameters"),
        "referenced binary response schemas should use the streaming interface: {raw}"
    );
}

#[test]
fn binary_response_examples_use_neutral_path_placeholders() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/export:\n    get:\n      operationId: exportWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { $ref: '#/components/schemas/WidgetId' } }\n      responses:\n        '200': { description: Export, content: { application/zip: { schema: { $ref: '#/components/schemas/FileContent' } } } }\ncomponents:\n  schemas:\n    WidgetId: { type: string, example: '\"widget-123\"' }\n    FileContent: { type: string, format: binary }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("id=\"id\"") && !client.contains("widget-123"),
        "binary response examples should use neutral path placeholders: {client}"
    );
}

#[test]
fn binary_request_media_types_are_preserved() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /import:\n    post:\n      operationId: importWidgets\n      tags: [widgets]\n      requestBody:\n        content:\n          application/zip:\n            schema: { $ref: '#/components/schemas/FileContent' }\n      responses:\n        '204': { description: Imported }\n  /create:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          '*/*':\n            schema: { $ref: '#/components/schemas/FileContent' }\n          application/vnd.create+json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\ncomponents:\n  schemas:\n    FileContent: { type: string, format: binary }\n    CreateWidget:\n      type: object\n      properties:\n        name: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("content=request,\n            headers={\n                \"content-type\": \"application/zip\"")
            && raw.contains("def create_widget(\n        self, *, request: typing.Optional[FileContent] = None")
            && raw.contains("json=request,"),
        "binary request media selection should preserve ZIP and wildcard semantics: {raw}"
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("request=\"string\"") && !client.contains("request=b\"string\""),
        "referenced binary request examples use Fern's string literal: {client}"
    );
}

#[test]
fn wildcard_binary_requests_with_path_params_omit_json_content_type() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/test:\n    put:\n      operationId: testWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { type: string } }\n      requestBody:\n        required: true\n        content:\n          '*/*':\n            schema: { type: string, format: binary }\n      responses:\n        '204': { description: Tested }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("request: bytes")
            && raw.contains("json=request,")
            && !raw.contains("\"content-type\": \"application/json\""),
        "wildcard binary-schema requests should not gain JSON headers from path params: {raw}"
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("request: bytes")
            && client.contains("request=\"string\"")
            && !client.contains("request=b\"string\""),
        "the high-level bytes method should use Fern's string example: {client}"
    );
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference is generated");
    assert!(
        reference.contains("**request:** `str`"),
        "reference docs should retain Fern's source-schema type: {reference}"
    );
}

#[test]
fn binary_requests_ignore_declared_operation_headers() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /import:\n    post:\n      operationId: importWidgets\n      tags: [widgets]\n      parameters:\n        - { name: X-Preserve-Ids, in: header, schema: { type: boolean } }\n      requestBody:\n        content:\n          application/zip:\n            schema: { $ref: '#/components/schemas/FileContent' }\n      responses:\n        '204': { description: Imported }\ncomponents:\n  schemas:\n    FileContent: { type: string, format: binary }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("content=request,") && !raw.contains("preserve_ids"),
        "raw binary operations should not expose transport metadata headers: {raw}"
    );
}

#[test]
fn tag_prefixed_multi_segment_operation_ids_drop_the_tag_segment() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /query/widgets/by_name:\n    \
         get:\n      operationId: query_widgets_by_name\n      tags: [Query]\n      parameters:\n        - name: \
         name\n          in: query\n          required: true\n          schema: { type: string }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/query/client.py"))
        .expect("query client is generated");
    assert!(
        client.contains("def widgets_by_name("),
        "a multi-segment operationId starting with the tag should drop only that tag segment: {client}"
    );
    assert!(
        !client.contains("def query_widgets_by_name("),
        "the tag segment should not be duplicated in the method name: {client}"
    );
}

#[test]
fn file_only_multipart_requests_include_empty_data() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/import:\n    \
         post:\n      operationId: importWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          \
         multipart/form-data:\n            schema:\n              type: object\n              properties:\n                \
         archive: { type: string, format: binary }\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("data={},") && raw.contains("files={"),
        "file-only multipart requests should still pass an empty data mapping: {raw}"
    );
}

#[test]
fn inline_json_bodies_matching_response_schema_omit_content_type() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/rules:\n    \
         post:\n      operationId: createWidgetRule\n      tags: [widgets]\n      requestBody:\n        content:\n          \
         application/json:\n            schema: { $ref: '#/components/schemas/WidgetRule' }\n        required: true\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/WidgetRule' } } } }\ncomponents:\n  \
         schemas:\n    WidgetRule:\n      type: object\n      required: [transition]\n      properties:\n        transition: { \
         type: string, enum: [archive, delete] }\n        count: { type: integer }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("transition: WidgetRuleTransition")
            && raw.contains("json={")
            && !raw.contains("\"content-type\": \"application/json\""),
        "inlined JSON bodies whose request and response share a schema should omit explicit content-type when no route/header params force headers: {raw}"
    );
}

#[test]
fn colliding_query_and_body_fields_serialize_from_query_name() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}:\n    \
         put:\n      operationId: updateWidget\n      tags: [widgets]\n      parameters:\n        - name: id\n          \
         in: path\n          required: true\n          schema: { type: string }\n        - name: active\n          in: \
         query\n          required: false\n          schema: { type: boolean }\n      requestBody:\n        content:\n          \
         application/json:\n            schema: { $ref: '#/components/schemas/WidgetRecord' }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/WidgetRecord' } } } }\ncomponents:\n  \
         schemas:\n    WidgetRecord:\n      type: object\n      properties:\n        active: { type: boolean }\n        \
         name: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("widget_record_active: typing.Optional[bool] = OMIT"),
        "colliding body fields should be prefixed in the method signature: {raw}"
    );
    assert!(
        raw.contains("\"active\": active,"),
        "Fern serializes a colliding body field from the original query parameter name: {raw}"
    );
    assert!(
        !raw.contains("\"active\": widget_record_active,"),
        "the prefixed signature name should not be used in the JSON dict for this collision: {raw}"
    );
}

#[test]
fn camel_case_tags_generate_snake_case_client_packages() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /runs:\n    \
         get:\n      operationId: get_runs\n      tags: [DagRun]\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n  /entries:\n    get:\n      \
         operationId: get_entries\n      tags: [XCom]\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n  /groups:\n    get:\n      \
         operationId: GroupV2.GetGroups\n      tags: [GroupV2]\n      responses:\n        '200': { description: OK, content: { \
         application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    assert!(
        out.join("src/acme/dag_run/raw_client.py").is_file(),
        "PascalCase tags should generate snake_case client package paths"
    );
    assert!(
        out.join("src/acme/x_com/raw_client.py").is_file(),
        "mixed acronym tags should preserve their word boundary"
    );
    assert!(
        out.join("src/acme/groupv2/raw_client.py").is_file(),
        "dotted operation namespaces should retain Fern's compact tag package"
    );
}

#[test]
fn inline_all_of_responses_preserve_component_bases() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      \
         operationId: listWidgets\n      tags: [widgets]\n      responses:\n        '200':\n          description: OK\n          content:\n            \
         application/json:\n              schema:\n                allOf:\n                  - { $ref: '#/components/schemas/WidgetCollection' }\n                  \
         - { $ref: '#/components/schemas/PageInfo' }\ncomponents:\n  schemas:\n    WidgetCollection:\n      type: object\n      properties:\n        \
         widgets: { type: array, items: { type: string } }\n    PageInfo:\n      type: object\n      properties:\n        total: { type: integer }\n",
    );
    let response =
        std::fs::read_to_string(out.join("src/acme/widgets/types/list_widgets_response.py"))
            .expect("inline allOf response model is generated");
    assert!(
        response.contains("from ...types.page_info import PageInfo")
            && response.contains("from ...types.widget_collection import WidgetCollection")
            && response.contains("class ListWidgetsResponse(WidgetCollection, PageInfo):"),
        "inline allOf response models should inherit every referenced component: {response}"
    );
}

#[test]
fn all_of_request_bodies_flatten_inherited_fields() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}:\n    patch:\n      \
         operationId: patchWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { type: string } }\n      \
         requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/Widget' }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  schemas:\n    WidgetBase:\n      \
         type: object\n      properties:\n        id: { type: string }\n        label: { type: string }\n    Widget:\n      allOf:\n        - { $ref: '#/components/schemas/WidgetBase' }\n        \
         - type: object\n          properties:\n            active: { type: boolean }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("id_: str,")
            && raw.contains("active: typing.Optional[bool] = OMIT")
            && raw.contains("id: typing.Optional[str] = OMIT")
            && raw.contains("label: typing.Optional[str] = OMIT")
            && raw.contains("\"id\": id,"),
        "allOf request bodies should flatten child and inherited fields before resolving collisions: {raw}"
    );
}

#[test]
fn pathless_all_of_bodies_omit_explicit_content_type() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/test:\n    post:\n      operationId: testWidget\n      tags: [widgets]\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/Widget' }\n      responses:\n        '200': { description: OK }\ncomponents:\n  schemas:\n    WidgetBase:\n      type: object\n      properties:\n        name: { type: string }\n    Widget:\n      allOf:\n        - { $ref: '#/components/schemas/WidgetBase' }\n        - type: object\n          properties:\n            active: { type: boolean }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        !raw.contains("\"content-type\": \"application/json\""),
        "pathless allOf request bodies should leave content type to the transport: {raw}"
    );
}

#[test]
fn single_use_request_component_enums_move_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    patch:\n      operationId: patchWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/UpdateWidget' }\n      responses:\n        '204': { description: Updated }\ncomponents:\n  schemas:\n    UpdateWidget:\n      type: object\n      properties:\n        state: { type: string, enum: [enabled, disabled] }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        out.join("src/acme/widgets/types/update_widget_state.py")
            .is_file()
            && !out.join("src/acme/types/update_widget_state.py").exists()
            && raw.contains("from .types.update_widget_state import UpdateWidgetState"),
        "an enum owned only by an elided request component should move into the endpoint tag: {raw}"
    );
}

#[test]
fn shared_request_component_enums_remain_root_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\n  /widgets/state:\n    put:\n      operationId: updateWidgetState\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/UpdateWidget' }\n      responses:\n        '204': { description: Updated }\ncomponents:\n  schemas:\n    WidgetState: { type: string, enum: [ACTIVE, DISABLED] }\n    CreateWidget:\n      type: object\n      properties:\n        state: { $ref: '#/components/schemas/WidgetState' }\n    UpdateWidget:\n      type: object\n      properties:\n        state: { $ref: '#/components/schemas/WidgetState' }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        out.join("src/acme/types/widget_state.py").is_file()
            && !out.join("src/acme/widgets/types/widget_state.py").exists()
            && raw.contains("from ..types.widget_state import WidgetState"),
        "an enum shared by elided request components should remain package-root: {raw}"
    );
}

#[test]
fn enums_referenced_by_retained_models_remain_root_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '200': { description: Created, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  schemas:\n    WidgetState: { type: string, enum: [ACTIVE, DISABLED] }\n    CreateWidget:\n      type: object\n      properties:\n        state: { $ref: '#/components/schemas/WidgetState' }\n    Widget:\n      type: object\n      properties:\n        state: { $ref: '#/components/schemas/WidgetState' }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    assert!(
        out.join("src/acme/types/widget_state.py").is_file()
            && !out.join("src/acme/widgets/types/widget_state.py").exists()
            && model.contains("from .widget_state import WidgetState"),
        "an enum referenced by a retained model should remain package-root: {model}"
    );
}

#[test]
fn nullable_body_fields_and_array_items_use_optional_annotations() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    patch:\n      operationId: patchWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/UpdateWidget' }\n      responses:\n        '200':\n          description: Updated\n          content:\n            application/json:\n              schema: { $ref: '#/components/schemas/UpdateWidget' }\ncomponents:\n  schemas:\n    Language: { type: string, nullable: true }\n    WidgetMeta:\n      type: object\n      properties:\n        type: { type: string }\n    UpdateWidget:\n      type: object\n      properties:\n        languages: { type: array, items: { $ref: '#/components/schemas/Language' } }\n        metadata: { $ref: '#/components/schemas/WidgetMeta', nullable: true, readOnly: true }\n        team:\n          type: object\n          nullable: true\n          properties:\n            name: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    let model = std::fs::read_to_string(out.join("src/acme/types/update_widget.py"))
        .expect("update widget model is generated");
    assert!(
        raw.contains("annotation=typing.Optional[WidgetMeta], direction=\"write\"")
            && raw.contains("metadata: typing.Optional[WidgetMeta] = OMIT")
            && raw.contains("annotation=typing.Optional[UpdateWidgetTeam], direction=\"write\"")
            && raw.contains("team: typing.Optional[UpdateWidgetTeam] = OMIT")
            && raw.contains(
                "languages: typing.Optional[typing.Sequence[typing.Optional[Language]]] = OMIT"
            )
            && model.contains(
                "languages: typing.Optional[typing.List[typing.Optional[Language]]] = None"
            ),
        "nullable conversion metadata and referenced array items should remain optional:\n{raw}\n{model}"
    );
}

#[test]
fn request_media_examples_populate_optional_body_fields() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    patch:\n      operationId: patchWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            example: { active: true }\n            schema: { $ref: '#/components/schemas/UpdateWidget' }\n      responses:\n        '204': { description: Updated }\ncomponents:\n  schemas:\n    UpdateWidget:\n      type: object\n      properties:\n        active: { type: boolean }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("client.widgets.patch_widget(\n            active=True,\n        )"),
        "request media examples should populate optional body arguments in worked examples: {client}"
    );
}

#[test]
fn first_referenced_request_example_drives_typed_worked_examples() {
    let (_dir, out) = generate_ok(
        r##"openapi: 3.1.0
info: { title: Events API, version: 1.0.0 }
paths:
  /events:
    post:
      operationId: createEvent
      tags: [events]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/Event' }
            examples:
              primary: { $ref: '#/components/examples/PrimaryEvent' }
              alternate: { $ref: '#/components/examples/AlternateEvent' }
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Event' }
components:
  schemas:
    EventDate: { type: string, format: date }
    EventDates:
      type: array
      items: { $ref: '#/components/schemas/EventDate' }
    EventPrice: { type: number, format: float }
    EventBase:
      type: object
      required: [name, dates, price]
      properties:
        name: { type: string }
        dates: { $ref: '#/components/schemas/EventDates' }
        price: { $ref: '#/components/schemas/EventPrice' }
    Event:
      allOf:
        - { $ref: '#/components/schemas/EventBase' }
        - type: object
          properties:
            note: { type: string }
            code: { type: string }
  examples:
    PrimaryEvent:
      value:
        name: Primary event
        dates: ['2024-02-03', '2024-02-03', '2024-02-04']
        price: 0
        note: Primary note
    AlternateEvent:
      value:
        name: Alternate event
        dates: ['2024-03-05']
        price: 15
        code: ALT-1
        note: Alternate note
"##,
    );
    let readme = std::fs::read_to_string(out.join("README.md")).expect("README is generated");
    let client = std::fs::read_to_string(out.join("src/acme/events/client.py"))
        .expect("events client is generated");
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference is generated");

    for rendered in [&readme, &client] {
        assert!(rendered.contains("name=\"Primary event\""), "{rendered}");
        assert!(rendered.contains("price=0"), "{rendered}");
        assert!(rendered.contains("note=\"Primary note\""), "{rendered}");
        assert_eq!(
            rendered.matches("\"2024-02-03\"").count(),
            2,
            "duplicate dates should be omitted once per sync/async example: {rendered}"
        );
        assert!(!rendered.contains("code=\"ALT-1\""), "{rendered}");
    }
    assert!(reference.contains("name=\"Primary event\""), "{reference}");
    assert!(reference.contains("price=0"), "{reference}");
    assert!(reference.contains("note=\"Primary note\""), "{reference}");
    assert!(!reference.contains("code=\"ALT-1\""), "{reference}");
}

#[test]
fn date_query_examples_use_dates_while_wire_values_use_str() {
    let (_dir, out) = generate_ok(
        r#"openapi: 3.0.3
info: { title: Events API, version: 1.0.0 }
paths:
  /events:
    get:
      operationId: listEvents
      tags: [events]
      parameters:
        - name: startDate
          in: query
          schema: { type: string, format: date, example: '2024-02-03' }
        - name: page
          in: query
          schema: { type: integer, example: 2 }
        - name: limit
          in: query
          schema: { type: integer, example: 15 }
        - name: updatedAfter
          in: query
          schema: { type: string, format: date-time }
      responses:
        '204': { description: Found }
"#,
    );
    let client = std::fs::read_to_string(out.join("src/acme/events/client.py"))
        .expect("events client is generated");
    let raw = std::fs::read_to_string(out.join("src/acme/events/raw_client.py"))
        .expect("events raw client is generated");

    assert!(
        client.contains(
            "start_date=datetime.date.fromisoformat(\n                \"2024-02-03\",\n            ),\n            page=2,\n            limit=15,"
        ),
        "date examples should be typed without suppressing later scalar examples: {client}"
    );
    assert!(
        raw.contains("\"startDate\": str(start_date) if start_date is not None else None,")
            && !raw.contains("serialize_datetime(start_date)")
            && raw.contains(
                "\"updatedAfter\": serialize_datetime(updated_after) if updated_after is not None else None,"
            )
            && raw.contains("from ..core.datetime_utils import serialize_datetime"),
        "date and date-time query serialization should remain distinct: {raw}"
    );
}

#[test]
fn referenced_request_examples_force_json_content_type_for_composed_bodies() {
    let (_dir, out) = generate_ok(
        r##"openapi: 3.0.3
info: { title: Tickets API, version: 1.0.0 }
paths:
  /tickets:
    post:
      operationId: buyTicket
      tags: [tickets]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/BuyTicket' }
            examples:
              general: { $ref: '#/components/examples/GeneralTicket' }
              event: { $ref: '#/components/examples/EventTicket' }
      responses:
        '204': { description: Purchased }
components:
  schemas:
    Ticket:
      type: object
      required: [kind]
      properties:
        kind: { type: string }
    BuyTicket:
      allOf:
        - { $ref: '#/components/schemas/Ticket' }
        - type: object
          properties:
            email: { type: string }
  examples:
    GeneralTicket: { value: { kind: general } }
    EventTicket: { value: { kind: event, email: buyer@example.com } }
"##,
    );
    let raw = std::fs::read_to_string(out.join("src/acme/tickets/raw_client.py"))
        .expect("tickets raw client is generated");
    assert_eq!(
        raw.matches("\"content-type\": \"application/json\"")
            .count(),
        2,
        "both sync and async requests need the explicit JSON content type: {raw}"
    );
}

#[test]
fn schema_examples_arrays_populate_worked_calls() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              required: [name]\n              properties:\n                name: { type: string, examples: [example-name] }\n      responses:\n        '204': { description: Created }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("client is generated");
    assert!(
        client.contains("name=\"example-name\""),
        "the first schema example should populate the worked call: {client}"
    );
}

#[test]
fn component_examples_populate_inlined_body_fields() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\ncomponents:\n  schemas:\n    WidgetState: { type: string, enum: [ACTIVE, DISABLED] }\n    CreateWidget:\n      type: object\n      required: [name, state]\n      example: { name: Example Widget, state: DISABLED }\n      properties:\n        name: { type: string }\n        state: { $ref: '#/components/schemas/WidgetState' }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("name=\"Example Widget\"") && client.contains("state=WidgetState.DISABLED"),
        "component examples should populate inlined request examples: {client}"
    );
}

#[test]
fn component_examples_populate_composite_body_fields() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\ncomponents:\n  schemas:\n    CreateWidget:\n      type: object\n      example: { labels: [regional, global], properties: { custom: value } }\n      properties:\n        labels: { type: array, items: { type: string } }\n        properties: { type: object, additionalProperties: { type: string } }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
    assert!(
        client.contains("labels=[\"regional\", \"global\"]")
            && client.contains("properties={\"custom\": \"value\"}"),
        "component examples should populate composite request fields: {client}"
    );
}

#[test]
fn readme_marks_composed_object_bodies_as_complex() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/CreateWidget' }\n      responses:\n        '204': { description: Created }\ncomponents:\n  schemas:\n    WidgetBase:\n      type: object\n      properties:\n        name: { type: string }\n    CreateWidget:\n      allOf:\n        - { $ref: '#/components/schemas/WidgetBase' }\n        - type: object\n          properties:\n            active: { type: boolean }\n",
    );
    let readme = std::fs::read_to_string(out.join("README.md")).expect("README is generated");
    assert!(
        readme.contains("client.widgets.create_widget(...)")
            && readme.contains("client.widgets.with_raw_response.create_widget(...)")
            && readme.contains("client.widgets.create_widget(..., request_options={"),
        "composed object request bodies should retain README argument placeholders: {readme}"
    );
}

#[test]
fn globally_optional_basic_auth_generates_optional_credentials() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nsecurity: []\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        '200': { description: OK }\ncomponents:\n  securitySchemes:\n    Basic:\n      type: http\n      scheme: basic\n",
    );
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    let wrapper = std::fs::read_to_string(out.join("src/acme/core/client_wrapper.py"))
        .expect("client wrapper is generated");
    assert!(
        client.contains(
            "username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None"
        ) && client.contains(
            "password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None"
        ) && wrapper.contains("if username is not None and password is not None:"),
        "a globally optional Basic scheme should not require credentials: {client}\n{wrapper}"
    );
}

#[test]
fn relative_server_paths_use_the_default_environment_member() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nservers:\n  - url: /api/v1\n    description: Widget Stable API\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        '200': { description: OK }\n",
    );
    let environment = std::fs::read_to_string(out.join("src/acme/environment.py"))
        .expect("environment module is generated");
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    assert!(
        environment.contains("DEFAULT = \"/api/v1\"")
            && client.contains("AcmeApiEnvironment.DEFAULT"),
        "relative server paths should use Fern's DEFAULT environment member: {environment}\n{client}"
    );
}

#[test]
fn server_url_variables_are_exposed_by_the_root_client() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nservers:\n  - url: https://api.example.com/{basePath}\n    variables:\n      basePath: { default: v1 }\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      responses:\n        '200': { description: OK }\n",
    );
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    assert!(
        client.contains(
            "base_path : typing.Optional[str]\n        Server URL variable for 'basePath'. Defaults to 'v1'."
        ) && client.matches("base_path: typing.Optional[str] = None").count() == 2
            && client.matches("if base_path is not None:").count() == 2
            && client.matches("_base_path = base_path if base_path is not None else \"v1\"").count()
                == 2
            && client
                .matches(
                    "base_url = \"https://api.example.com/{basePath}\".format(basePath=_base_path)"
                )
                .count()
                == 2,
        "sync and async root clients should expose and apply the server URL variable: {client}"
    );
}

#[test]
fn multiline_parameter_docs_remain_indented() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      \
         operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        - name: order_by\n          in: query\n          description: |\n            \
         Field used to order results.\n            Prefix with `-` to reverse ordering.\n\n            *New in version 1.0*\n          schema: { type: string }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: { type: string } } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains(
            "        order_by : typing.Optional[str]\n            Field used to order results.\n            Prefix with `-` to reverse ordering.\n\n            *New in version 1.0*"
        ),
        "every line of a parameter description should remain inside the method docstring: {raw}"
    );
}

#[test]
fn multiline_parameter_docs_use_reference_paragraphs() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        - name: order_by\n          in: query\n          description: |\n            Field used to order results.\n            Prefix with `-` to reverse ordering.\n          schema: { type: string }\n      responses:\n        '200': { description: OK }\n",
    );
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference is generated");
    assert!(
        reference.contains(
            "**order_by:** `typing.Optional[str]` \n\nField used to order results.\nPrefix with `-` to reverse ordering."
        ),
        "multiline parameter descriptions should render as reference paragraphs: {reference}"
    );
}

#[test]
fn multiline_path_parameter_docs_remain_indented() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      parameters:\n        - name: id\n          in: path\n          required: true\n          description: |\n            Widget identifier.\n            It may use an external namespace.\n          schema: { type: string }\n      responses:\n        '200': { description: OK, content: { application/json: { schema: { type: string } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains(
            "        id : str\n            Widget identifier.\n            It may use an external namespace."
        ),
        "every line of a path parameter description should remain inside the method docstring: {raw}"
    );
}

#[test]
fn path_parameters_preserve_declaration_order() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/{slug}:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      parameters:\n        - { name: slug, in: path, required: true, schema: { type: string } }\n        - { name: id, in: path, required: true, schema: { type: integer } }\n      responses:\n        '204': { description: Found }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("client is generated");
    assert!(
        client.contains("self, slug: str, id: int,"),
        "path arguments should preserve parameter declaration order: {client}"
    );
}

#[test]
fn pydantic_model_api_fields_are_aliased() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        schema: { type: string }\n        kwargs: { type: string }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    assert!(
        model.contains("schema_: typing_extensions.Annotated[")
            && model.contains("FieldMetadata(alias=\"schema\")")
            && model.contains("kwargs_: typing_extensions.Annotated[")
            && model.contains("FieldMetadata(alias=\"kwargs\")"),
        "fields that collide with pydantic's model API should retain their wire aliases: {model}"
    );
}

#[test]
fn model_field_docs_trim_terminal_line_breaks() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        name:\n          type: string\n          description: |\n            Widget name.\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    assert!(
        model.contains("    Widget name.\n    \"\"\"")
            && !model.contains("    Widget name.\n    \n    \"\"\""),
        "terminal description line breaks should not add a blank field-doc line: {model}"
    );
}

#[test]
fn declared_empty_schema_descriptions_emit_class_docstrings() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      description: ''\n      properties:\n        id: { type: integer, format: int64 }\n    WidgetState:\n      type: string\n      description: ''\n      enum: [ACTIVE]\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    let state = std::fs::read_to_string(out.join("src/acme/types/widget_state.py"))
        .expect("widget state enum is generated");
    assert!(
        model.contains("class Widget(UniversalBaseModel):\n    \"\"\" \"\"\"\n\n    id: typing.Optional[int]")
            && state.contains("class WidgetState(enum.StrEnum):\n    \"\"\" \"\"\"\n\n    ACTIVE = \"ACTIVE\""),
        "declared empty schema descriptions should remain visible in generated classes:\n{model}\n{state}"
    );
}

#[test]
fn overlapping_all_of_fields_flatten_the_base_model() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    WidgetBase:\n      type: object\n      properties:\n        name: { type: string, description: Base name. }\n        size: { type: integer }\n    Widget:\n      allOf:\n        - { $ref: '#/components/schemas/WidgetBase' }\n        - type: object\n          properties:\n            name: { type: string }\n            active: { type: boolean }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    let name_pos = model.find("name:").expect("child name field is generated");
    let active_pos = model
        .find("active:")
        .expect("child active field is generated");
    let size_pos = model
        .find("size:")
        .expect("inherited size field is generated");
    assert!(
        model.contains("class Widget(UniversalBaseModel):")
            && name_pos < active_pos
            && active_pos < size_pos
            && model.contains("Base name."),
        "overlapping allOf fields should flatten with child fields taking precedence: {model}"
    );
}

#[test]
fn nested_and_union_nullability_is_preserved() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths: {}\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        labels:\n          type: array\n          items: { type: string, nullable: true }\n        roles:\n          type: array\n          items:\n            type: object\n            nullable: true\n            properties:\n              name: { type: string }\n    Schedule:\n      nullable: true\n      anyOf:\n        - { type: integer }\n        - { type: string }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/types/widget.py"))
        .expect("widget model is generated");
    let alias = std::fs::read_to_string(out.join("src/acme/types/schedule.py"))
        .expect("schedule alias is generated");
    assert!(
        model.contains("typing.List[typing.Optional[str]]")
            && model.contains("typing.List[typing.Optional[WidgetRolesItem]]")
            && alias.contains("Schedule = typing.Union[int, typing.Optional[str]]"),
        "nested and union nullability should be retained at the schema node that declares it: {model}\n{alias}"
    );
}

#[test]
fn array_ref_request_body_generates_single_named_request_argument() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/archive:\n    \
         post:\n      operationId: archiveWidgets\n      tags: [widgets]\n      requestBody:\n        \
         required: true\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/WidgetIds' }\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: { type: object, properties: \
         { ok: { type: boolean } } } } } }\ncomponents:\n  schemas:\n    WidgetIds:\n      type: array\n      \
         items: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("request: WidgetIds"),
        "a $ref array body should be passed as a single named request argument: {raw}"
    );
    assert!(
        raw.contains("json=request,"),
        "the named array request should serialize as json=request: {raw}"
    );
}

#[test]
fn component_request_body_refs_generate_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /credentials:\n    \
         post:\n      operationId: addCredential\n      tags: [identity]\n      requestBody: { $ref: \
         '#/components/requestBodies/CredentialBody' }\n      responses:\n        '200': { description: OK, \
         content: { application/json: { schema: { type: object, properties: { ok: { type: boolean } } } } } }\ncomponents:\n  \
         requestBodies:\n    CredentialBody:\n      required: true\n      content:\n        application/json:\n          \
         schema: { $ref: '#/components/schemas/Credential' }\n  schemas:\n    Credential:\n      type: object\n      \
         required: [username]\n      properties:\n        username: { type: string }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/identity/raw_client.py"))
        .expect("identity raw client is generated");
    assert!(
        raw.contains("username: str"),
        "a component requestBody ref should resolve and inline the referenced object fields: {raw}"
    );
}

#[test]
fn text_plain_request_bodies_are_ignored_for_python_generation() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /uploads/{id}:\n    \
         post:\n      operationId: uploadText\n      tags: [uploads]\n      parameters:\n        - { name: id, \
         in: path, required: true, schema: { type: string } }\n      requestBody:\n        required: true\n        \
         content:\n          text/plain; utf-8:\n            schema: { type: string }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: object, properties: { ok: { type: \
         boolean } } } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/uploads/raw_client.py"))
        .expect("uploads raw client is generated");
    assert!(
        raw.contains("def upload_text(") && !raw.contains("request:"),
        "text/plain request bodies should not surface a request argument: {raw}"
    );
}

#[test]
fn get_request_bodies_are_ignored_through_the_cli() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema:\n              type: object\n              required: [filter]\n              properties:\n                filter: { type: string }\n      responses:\n        '204': { description: Found }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("raw client is generated");
    assert!(
        !raw.contains("filter:") && !raw.contains("json={"),
        "GET request bodies should not enter the generated interface: {raw}"
    );
}

#[test]
fn vendor_json_bare_object_request_body_is_open_map() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /manifests/{id}:\n    \
         post:\n      operationId: importManifest\n      tags: [imports]\n      parameters:\n        - { name: id, \
         in: path, required: true, schema: { type: string } }\n      requestBody:\n        required: true\n        \
         content:\n          application/vnd.example+json:\n            schema: { type: object }\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: object, properties: { ok: { type: \
         boolean } } } } } }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/imports/raw_client.py"))
        .expect("imports raw client is generated");
    assert!(
        raw.contains("request: typing.Dict[str, typing.Any]")
            && raw.contains("\"content-type\": \"application/vnd.example+json\""),
        "vendor +json bodies should be open-map requests with the exact media type: {raw}"
    );
}

#[test]
fn missing_operation_id_generates_valid_python() {
    // Issue #40 case 3: an operation without an operationId is valid OpenAPI and
    // must generate (crozier synthesizes a name), not hard-error.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      summary: List widgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { type: array, items: \
         { type: string } } } } }\n",
    );
    assert!(
        out.join("src/acme/widgets").is_dir(),
        "the tag should name the synthesized client module"
    );
}

#[test]
fn exhaustive_output_is_valid_python() {
    let fixtures = fixture_dir("exhaustive");
    let out = tempfile::tempdir().expect("tempdir");
    crozier()
        .args(["generate", "--spec"])
        .arg(fixtures.join("openapi.yml"))
        .arg("--output")
        .arg(out.path())
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ])
        .assert()
        .success();
    assert_valid_python(out.path());
}

#[test]
fn default_naming_derives_package_from_title() {
    // The most common first invocation: no --package-name / --project-name, so the
    // package dir is snake_case(title) and version.py records the same name.
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, ARBITRARY_SPEC).unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));

    let version = out.join("src/my_cool_api/version.py");
    let body = std::fs::read_to_string(&version)
        .expect("default package dir should be snake_case of the API title");
    assert!(
        body.contains("my_cool_api"),
        "project name should default from the title: {body}"
    );
}

#[test]
fn default_naming_sanitizes_title_punctuation() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.3\ninfo: { title: 'Airflow API (Stable)', version: 1.0.0 }\npaths: {}\n",
    )
    .unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));

    let package = out.join("src/airflow_api_stable");
    assert!(
        package.is_dir(),
        "title punctuation should become identifier word boundaries"
    );
    let version = std::fs::read_to_string(package.join("version.py"))
        .expect("sanitized default package should contain version.py");
    assert!(
        version.contains("metadata.version(\"airflow_api_stable\")"),
        "project name should use the sanitized package default: {version}"
    );
    assert_valid_python(&out);
}

#[test]
fn regeneration_prunes_stale_modules_and_stays_valid() {
    // Users regenerate into the same --output constantly. A schema dropped from the
    // spec must not leave an orphaned module behind, and the result must still be
    // valid Python.
    let dir = tempfile::tempdir().expect("tempdir");
    let out = dir.path().join("out");

    let two = dir.path().join("two.yml");
    std::fs::write(
        &two,
        "openapi: 3.0.0\ninfo:\n  title: Regen\ncomponents:\n  schemas:\n    \
         Widget:\n      type: object\n      properties:\n        id: { type: string }\n    \
         Gadget:\n      type: object\n      properties:\n        id: { type: string }\n",
    )
    .unwrap();
    crozier()
        .args(["generate", "--spec"])
        .arg(&two)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "regen"])
        .assert()
        .success();
    assert!(out.join("src/regen/types/widget.py").is_file());
    assert!(out.join("src/regen/types/gadget.py").is_file());

    let one = dir.path().join("one.yml");
    std::fs::write(
        &one,
        "openapi: 3.0.0\ninfo:\n  title: Regen\ncomponents:\n  schemas:\n    \
         Widget:\n      type: object\n      properties:\n        id: { type: string }\n",
    )
    .unwrap();
    crozier()
        .args(["generate", "--spec"])
        .arg(&one)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "regen"])
        .assert()
        .success();
    assert!(out.join("src/regen/types/widget.py").is_file());
    assert!(
        !out.join("src/regen/types/gadget.py").exists(),
        "stale module was not pruned on regeneration"
    );
    assert_valid_python(&out);
}

#[test]
fn audience_filter_prunes_through_the_binary_and_stays_valid() {
    // Drive the real binary over the committed `audience-filter` spec both ways.
    // The `feature_target_specs` byte-match already proves `--audience public`
    // equals Fern's pruned golden; this adds the two things that check cannot: the
    // filter-vs-unfiltered *contrast* through the CLI, and that the pruned subset
    // still compiles (no dangling import to a removed type).
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = fixture_dir("audience-filter").join("openapi.yml");

    // Unfiltered: both the public `widgets` client and the internal `admin` client
    // (with its `Stats` type) are generated.
    let full = dir.path().join("full");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&full)
        .args(["--package-name", "aud"])
        .assert()
        .success();
    assert!(full.join("src/aud/widgets/client.py").is_file());
    assert!(full.join("src/aud/admin/client.py").is_file());
    assert!(full.join("src/aud/types/stats.py").is_file());
    assert_valid_python(&full);

    // Filtered to `public`: the internal `admin` client and its internal-only
    // `Stats` type are pruned; the public client and its transitive `Widget`
    // closure remain, and the result still compiles.
    let pub_only = dir.path().join("public");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&pub_only)
        .args(["--package-name", "aud", "--audience", "public"])
        .assert()
        .success();
    assert!(pub_only.join("src/aud/widgets/client.py").is_file());
    assert!(
        !pub_only.join("src/aud/admin").exists(),
        "internal admin client should be pruned by --audience public"
    );
    assert!(
        !pub_only.join("src/aud/types/stats.py").exists(),
        "internal-only Stats type should be pruned by --audience public"
    );
    assert!(pub_only.join("src/aud/types/widget.py").is_file());
    assert!(pub_only.join("src/aud/types/widget_detail.py").is_file());
    assert_valid_python(&pub_only);
}

#[test]
fn strict_audience_excludes_unannotated_ops_through_the_binary() {
    // Drive the real binary over the `audience-filter-strict` spec (which carries an
    // un-annotated `/health` op) both permissive and strict, proving the issue #62
    // contrast the byte-match cannot: the same `--audience public` keeps the
    // un-annotated op by default but drops it under `--audience-strict`, and both
    // pruned subsets still compile.
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = fixture_dir("audience-filter-strict").join("openapi.yml");

    // Permissive `--audience public`: the un-annotated `health` op is *kept* (the
    // documented "or none at all" rule); only the internal `admin` op is pruned.
    let permissive = dir.path().join("permissive");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&permissive)
        .args(["--package-name", "aud", "--audience", "public"])
        .assert()
        .success();
    assert!(permissive.join("src/aud/widgets/client.py").is_file());
    assert!(
        permissive.join("src/aud/health/client.py").is_file(),
        "un-annotated health op should be kept by permissive --audience public"
    );
    assert!(!permissive.join("src/aud/admin").exists());
    assert_valid_python(&permissive);

    // Strict `--audience public --audience-strict`: the un-annotated `health` op and
    // its `Health` type are *also* pruned, leaving only the public subset — Fern's
    // exclusive behaviour.
    let strict = dir.path().join("strict");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&strict)
        .args([
            "--package-name",
            "aud",
            "--audience",
            "public",
            "--audience-strict",
        ])
        .assert()
        .success();
    assert!(strict.join("src/aud/widgets/client.py").is_file());
    assert!(
        !strict.join("src/aud/health").exists(),
        "un-annotated health op should be pruned by --audience-strict"
    );
    assert!(
        !strict.join("src/aud/types/health.py").exists(),
        "un-annotated op's Health type should be pruned by --audience-strict"
    );
    assert!(!strict.join("src/aud/admin").exists());
    assert!(strict.join("src/aud/types/widget.py").is_file());
    assert!(strict.join("src/aud/types/widget_detail.py").is_file());
    assert_valid_python(&strict);
}

#[test]
fn ignore_extension_prunes_marked_ops_through_the_binary_and_stays_valid() {
    // Drive the real binary over a spec carrying both ignore spellings (issue #78).
    // `x-fern-ignore` and `x-crozier-ignore` each drop their operation and the type
    // it exclusively referenced, while an explicit `x-crozier-ignore: false`
    // overrides a sibling `x-fern-ignore: true` (the Overlay un-ignore pattern). The
    // pruned SDK must still compile — no dangling import to a removed type.
    let ignore_spec = r##"
openapi: 3.0.3
info: { title: Widget API, version: 1.0.0 }
paths:
  /keep:
    get:
      operationId: keepOp
      tags: [keep]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Keep" }
  /fern:
    get:
      operationId: fernIgnoredOp
      tags: [fern]
      x-fern-ignore: true
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/OnlyFern" }
  /crozier:
    get:
      operationId: crozierIgnoredOp
      tags: [crozier]
      x-crozier-ignore: true
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/OnlyCrozier" }
  /unignore:
    get:
      operationId: unignoreOp
      tags: [unignore]
      x-fern-ignore: true
      x-crozier-ignore: false
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Kept" }
components:
  schemas:
    Keep: { type: object, properties: { note: { type: string } } }
    Kept: { type: object, properties: { note: { type: string } } }
    OnlyFern: { type: object, properties: { note: { type: string } } }
    OnlyCrozier: { type: object, properties: { note: { type: string } } }
"##;
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("widget.yml");
    std::fs::write(&spec, ignore_spec).unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "widgetapi"])
        .assert()
        .success();

    // Kept and un-ignored ops (and their types) are generated.
    assert!(out.join("src/widgetapi/keep/client.py").is_file());
    assert!(out.join("src/widgetapi/types/keep.py").is_file());
    assert!(
        out.join("src/widgetapi/unignore/client.py").is_file(),
        "x-crozier-ignore: false keeps the op despite x-fern-ignore: true"
    );
    assert!(out.join("src/widgetapi/types/kept.py").is_file());

    // Both ignore spellings drop their client and their exclusive type.
    assert!(
        !out.join("src/widgetapi/fern").exists(),
        "x-fern-ignore op should be pruned"
    );
    assert!(
        !out.join("src/widgetapi/crozier").exists(),
        "x-crozier-ignore op should be pruned"
    );
    assert!(!out.join("src/widgetapi/types/only_fern.py").exists());
    assert!(!out.join("src/widgetapi/types/only_crozier.py").exists());
    assert_valid_python(&out);
}

/// A minimal one-schema OpenAPI document for the config-layer e2e journeys —
/// enough to drive a real `crozier generate` without a fixture corpus.
const TINY_SPEC: &str = "openapi: 3.0.0\ninfo:\n  title: Tiny\ncomponents:\n  schemas:\n    Thing:\n      type: object\n      properties:\n        name: { type: string }\n";

#[test]
fn config_file_is_discovered_in_the_working_directory() {
    // A `crozier.yml` in the working directory is picked up with no `--config`
    // flag; relative paths in it resolve against that directory.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(
        dir.path().join("crozier.yml"),
        "generators:\n  admin:\n    spec: ./api.yml\n    output: ./out\n    package-name: admin\n",
    )
    .unwrap();

    // No selector → run the single configured generator.
    crozier()
        .current_dir(dir.path())
        .arg("generate")
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    assert!(dir.path().join("out/src/admin/types/thing.py").is_file());
}

#[test]
fn env_var_overrides_config_and_cli_overrides_env() {
    // Precedence CLI > CROZIER_* env > config file, through the real process env.
    let base = "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    package-name: fromconfig\n";

    // env beats config: no CLI override, so CROZIER_PACKAGE_NAME wins.
    let a = tempfile::tempdir().expect("tempdir");
    std::fs::write(a.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(a.path().join("crozier.yml"), base).unwrap();
    crozier()
        .current_dir(a.path())
        .env("CROZIER_PACKAGE_NAME", "fromenv")
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(a.path().join("out/src/fromenv/types/thing.py").is_file());

    // CLI beats env: --package-name wins over CROZIER_PACKAGE_NAME.
    let b = tempfile::tempdir().expect("tempdir");
    std::fs::write(b.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(b.path().join("crozier.yml"), base).unwrap();
    crozier()
        .current_dir(b.path())
        .env("CROZIER_PACKAGE_NAME", "fromenv")
        .args(["generate", "python", "--package-name", "fromcli"])
        .assert()
        .success();
    assert!(b.path().join("out/src/fromcli/types/thing.py").is_file());
}

#[test]
fn generate_all_runs_every_configured_generator_through_the_binary() {
    // Bare `crozier` (no subcommand) generates every configured generator.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\ngenerators:\n  a:\n    output: ./a\n    package-name: a\n  b:\n    output: ./b\n    package-name: b\n",
    )
    .unwrap();

    crozier().current_dir(dir.path()).assert().success();
    assert!(dir.path().join("a/src/a/types/thing.py").is_file());
    assert!(dir.path().join("b/src/b/types/thing.py").is_file());
}

#[test]
fn init_then_config_round_trips_through_the_binary() {
    // `crozier init` (default path) writes a discoverable `crozier.yml`; `crozier
    // config` then reports it with per-field sources on stdout.
    let dir = tempfile::tempdir().expect("tempdir");
    crozier()
        .current_dir(dir.path())
        .arg("init")
        .assert()
        .success()
        .stderr(predicate::str::contains("wrote"));
    assert!(dir.path().join("crozier.yml").is_file());

    crozier()
        .current_dir(dir.path())
        .arg("config")
        .assert()
        .success()
        // The discovered file is reported, and each field carries its source.
        .stdout(
            predicate::str::contains("config files:").and(predicate::str::contains("crozier.yml")),
        )
        .stdout(predicate::str::contains("generator `python`"))
        .stdout(predicate::str::contains("(shared)"))
        .stdout(predicate::str::contains("(generator)"));
}

#[test]
fn config_flag_selects_one_generator_through_the_binary() {
    // Explicit `--config` + `generate <name>` runs only that config-defined
    // generator, leaving the others untouched.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    let cfg = dir.path().join("gen.yml");
    std::fs::write(
        &cfg,
        "spec: ./api.yml\ngenerators:\n  admin:\n    output: ./admin\n    package-name: admin\n  extra:\n    output: ./extra\n    package-name: extra\n",
    )
    .unwrap();

    crozier()
        .current_dir(dir.path())
        .arg("--config")
        .arg(&cfg)
        .args(["generate", "admin"])
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    assert!(dir.path().join("admin/src/admin/types/thing.py").is_file());
    assert!(
        !dir.path().join("extra").exists(),
        "only the named generator runs"
    );
}

#[test]
fn crozier_config_env_var_names_the_file_through_the_binary() {
    // `CROZIER_CONFIG` points at a config outside the working directory.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    let cfg = dir.path().join("elsewhere.yml");
    std::fs::write(
        &cfg,
        "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    package-name: viaenv\n",
    )
    .unwrap();

    crozier()
        .current_dir(dir.path())
        .env("CROZIER_CONFIG", &cfg)
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(dir.path().join("out/src/viaenv/types/thing.py").is_file());
}

#[test]
fn unknown_generator_exits_nonzero_with_an_actionable_message() {
    let dir = tempfile::tempdir().expect("tempdir");
    crozier()
        .current_dir(dir.path())
        .args(["--no-config", "generate", "typescript"])
        .assert()
        .failure()
        .code(1)
        .stderr(
            predicate::str::contains("unknown generator").and(predicate::str::contains("python")),
        );
}

#[test]
fn per_generation_flags_with_multiple_generators_exit_nonzero() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\ngenerators:\n  a:\n    output: ./a\n  b:\n    output: ./b\n",
    )
    .unwrap();

    crozier()
        .current_dir(dir.path())
        .args(["generate", "--package-name", "x"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("single generator"));
}

#[test]
fn init_force_overwrites_and_refuses_without_it_through_the_binary() {
    let dir = tempfile::tempdir().expect("tempdir");
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(&cfg, "spec: ./seed.yml\n").unwrap();

    // Refuses to clobber (exit 1) without --force.
    crozier()
        .current_dir(dir.path())
        .arg("init")
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("already exists"));
    // --force overwrites with the starter.
    crozier()
        .current_dir(dir.path())
        .args(["init", "--force"])
        .assert()
        .success()
        .stderr(predicate::str::contains("wrote"));
    assert!(std::fs::read_to_string(&cfg)
        .unwrap()
        .contains("generators:"));
}

#[test]
fn config_selects_one_generator_and_honors_no_config_through_the_binary() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\ngenerators:\n  a:\n    output: ./a\n  b:\n    output: ./b\n",
    )
    .unwrap();

    // `config <name>` shows only that generator.
    crozier()
        .current_dir(dir.path())
        .args(["config", "a"])
        .assert()
        .success()
        .stdout(
            predicate::str::contains("generator `a`")
                .and(predicate::str::contains("generator `b`").not()),
        );
    // `--no-config` ignores the discovered file → the built-in python only.
    crozier()
        .current_dir(dir.path())
        .args(["--no-config", "config"])
        .assert()
        .success()
        .stdout(
            predicate::str::contains("none (built-in defaults)")
                .and(predicate::str::contains("generator `python`")),
        );
}

#[test]
fn schema_command_prints_the_config_json_schema() {
    // `crozier schema` emits exactly the derived schema, as valid JSON.
    let out = crozier()
        .arg("schema")
        .output()
        .expect("run crozier schema");
    assert!(out.status.success(), "schema command exits 0");
    let printed: serde_json::Value =
        serde_json::from_slice(&out.stdout).expect("schema stdout is valid JSON");
    // It is the same schema the drift test pins and `init` references.
    assert_eq!(printed, crozier::schema::build());
    // Sanity: it describes the config, including the merged `client-class-name`.
    assert_eq!(printed["$id"], crozier::schema::SCHEMA_URL);
    assert!(printed["properties"]["generators"].is_object());
    assert!(printed["$defs"]["GeneratorSettings"]["properties"]
        .get("client-class-name")
        .is_some());
}

#[test]
fn multiple_config_files_layer_later_wins_through_the_binary() {
    // Repeatable `--config`: the later file wins per field, and an untouched field
    // from the earlier file survives — through the real process.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    let base = dir.path().join("base.yml");
    let over = dir.path().join("over.yml");
    std::fs::write(
        &base,
        "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    package-name: frombase\n",
    )
    .unwrap();
    std::fs::write(
        &over,
        "generators:\n  python:\n    package-name: fromover\n",
    )
    .unwrap();

    crozier()
        .current_dir(dir.path())
        .arg("--config")
        .arg(&base)
        .arg("--config")
        .arg(&over)
        .args(["generate", "python"])
        .assert()
        .success();
    // package-name comes from the later file; spec/output survive from the first.
    assert!(dir.path().join("out/src/fromover/types/thing.py").is_file());
}

#[test]
fn client_class_name_is_configurable_via_the_config_file() {
    // The field #65 added as a flag is also a first-class config value: setting it
    // in `crozier.yml` renames the generated root client class, same as the flag.
    let dir = tempfile::tempdir().expect("tempdir");
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "generators:\n  python:\n    spec: {}\n    output: ./out\n    package-name: fern\n    client-class-name: AcmeClient\n",
            fixture_dir("client-class-name").join("openapi.yml").display()
        ),
    )
    .unwrap();

    crozier()
        .current_dir(dir.path())
        .arg("--config")
        .arg(&cfg)
        .args(["generate", "python"])
        .assert()
        .success();
    let client = std::fs::read_to_string(dir.path().join("out/src/fern/client.py"))
        .expect("client.py generated");
    assert!(
        client.contains("class AcmeClient"),
        "config-set client-class-name should reach generation"
    );
}
