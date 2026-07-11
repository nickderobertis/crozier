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
    matched: &'static [&'static str],
}

/// Fern's OpenAPI-sourced `query-parameters-openapi` seed (offline corpus).
const QUERY_PARAMETERS: Corpus = Corpus {
    api: "query-parameters-openapi",
    package_name: "seed",
    project_name: "fern_query-parameters-openapi",
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

/// The broad `exhaustive` target: Fern's Python output regenerated from the
/// vendored OpenAPI document (see scripts/generate-fern-fixture.sh). **All 104
/// files match** — the type layer, the `core/` runtime, the whole endpoint layer
/// (raw + high-level per-tag clients + root client), the `errors/` package, the
/// package `__init__.py` aggregators, the generated docs (`README.md`,
/// `reference.md`), and the project scaffolding. See docs/matching.md.
const EXHAUSTIVE: Corpus = Corpus {
    api: "exhaustive",
    package_name: "fern",
    project_name: "default_package_name",
    matched: &[
        "src/fern/version.py",
        "src/fern/py.typed",
        // The static core runtime, emitted verbatim (assets/core/).
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
        "src/fern/types/bad_object_request_info.py",
        "src/fern/types/endpoints_error.py",
        "src/fern/types/endpoints_error_category.py",
        "src/fern/types/endpoints_error_code.py",
        "src/fern/types/endpoints_paginated_response.py",
        "src/fern/types/endpoints_put_response.py",
        "src/fern/types/types_animal.py",
        "src/fern/types/types_animal_one.py",
        "src/fern/types/types_animal_one_animal.py",
        "src/fern/types/types_animal_zero.py",
        "src/fern/types/types_animal_zero_animal.py",
        "src/fern/types/types_cat.py",
        "src/fern/types/types_documented_unknown_type.py",
        "src/fern/types/types_dog.py",
        "src/fern/types/types_double_optional.py",
        "src/fern/types/types_map_of_documented_unknown_type.py",
        "src/fern/types/types_mixed_type.py",
        "src/fern/types/types_nested_object_with_optional_field.py",
        "src/fern/types/types_nested_object_with_required_field.py",
        "src/fern/types/types_object_with_datetime_like_string.py",
        "src/fern/types/types_object_with_docs.py",
        "src/fern/types/types_object_with_documented_unknown_type.py",
        "src/fern/types/types_object_with_map_of_map.py",
        "src/fern/types/types_object_with_optional_field.py",
        "src/fern/types/types_object_with_required_field.py",
        "src/fern/types/types_object_with_unknown_field.py",
        "src/fern/types/types_optional_alias.py",
        "src/fern/types/types_weather_report.py",
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
        // Per-tag raw clients for the no-request-body tags (path params only,
        // single JSON success response). Other tags await wider endpoint support.
        "src/fern/endpoints_put/raw_client.py",
        "src/fern/endpoints_urls/raw_client.py",
        "src/fern/noreqbody/raw_client.py",
        // Query-parameter-only tag (no request body, no headers).
        "src/fern/endpoints_pagination/raw_client.py",
        // Named enum (`$ref`) request body → `json=request` + content-type header.
        "src/fern/endpoints_enum/raw_client.py",
        // Scalar request bodies, incl. the uuid/byte content-type nuance.
        "src/fern/endpoints_primitive/raw_client.py",
        // Named union (`$ref`) request body → `convert_and_respect_annotation_metadata`.
        "src/fern/endpoints_union/raw_client.py",
        // Header params + a scalar body + a 204 (no-content) response.
        "src/fern/reqwithheaders/raw_client.py",
        // Inlined plain-object request bodies (fields hoisted to keyword-only
        // args), per-field convert, request-context `typing.Sequence`, and a
        // path/body name collision.
        "src/fern/endpoints_object/raw_client.py",
        // Also unlocked by inline hoisting: the HTTP-method matrix and the
        // content-type-header tags.
        "src/fern/endpoints_http_methods/raw_client.py",
        "src/fern/endpoints_content_type/raw_client.py",
        // Declared 4xx error responses raise generated exceptions; the `errors/`
        // package (a class per error + a lazy-loading `__init__.py`) backs them.
        // `noauth` also exercises an unknown (`{}`) body; `inlinedrequests` an
        // inline (non-`$ref`) object body.
        "src/fern/errors/bad_request_error.py",
        "src/fern/errors/__init__.py",
        "src/fern/noauth/raw_client.py",
        "src/fern/inlinedrequests/raw_client.py",
        // Container request/response bodies: lists, sets, and maps of primitives
        // (plain `json=request`) and of objects/unions (the convert wrapper), plus
        // an inline optional object body.
        "src/fern/endpoints_container/raw_client.py",
        // Mixed path/query/body, `application/octet-stream` (bytes) bodies, and
        // array (allow-multiple) query parameters.
        "src/fern/endpoints_params/raw_client.py",
        // Per-tag high-level `client.py`: the sync+async wrappers that return
        // `_response.data`, each with a worked `Examples` docstring synthesized by
        // the example-value generator (objects with required fields, unions, maps,
        // containers, enums, datetimes, the `long` placeholder, ...).
        "src/fern/endpoints_container/client.py",
        "src/fern/endpoints_content_type/client.py",
        "src/fern/endpoints_enum/client.py",
        "src/fern/endpoints_http_methods/client.py",
        "src/fern/endpoints_object/client.py",
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
        // Root client: `FernApi`/`AsyncFernApi` aggregating the tag clients (bearer
        // auth). Its class name is `PascalCase(package_name) + "Api"`.
        "src/fern/client.py",
        // Package aggregators: lazy loaders re-exporting the type layer and the
        // whole SDK surface. `_dynamic_imports`/`__all__` are alphabetical; the
        // `types/__init__.py` `TYPE_CHECKING` block follows Fern's traversal order.
        "src/fern/types/__init__.py",
        "src/fern/__init__.py",
        // Generated `README.md`: static prose plus a worked usage example (sync +
        // async) synthesized from the first endpoint. Compared verbatim.
        "README.md",
        // Generated `reference.md`: a per-endpoint reference grouped by tag, each
        // a `<details>` block with a worked example and a parameter table.
        "reference.md",
        // Project-root scaffolding (near-static; name/version substituted).
        "pyproject.toml",
        "requirements.txt",
        ".fern/metadata.json",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/apikeyauth/__init__.py",
            "src/fern/apikeyauth/client.py",
            "src/fern/apikeyauth/raw_client.py",
            "src/fern/basicauth/__init__.py",
            "src/fern/basicauth/client.py",
            "src/fern/basicauth/raw_client.py",
            "src/fern/bearerauth/__init__.py",
            "src/fern/bearerauth/client.py",
            "src/fern/bearerauth/raw_client.py",
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
            "src/fern/oauth/__init__.py",
            "src/fern/oauth/client.py",
            "src/fern/oauth/raw_client.py",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/inlined/__init__.py",
            "src/fern/inlined/client.py",
            "src/fern/inlined/raw_client.py",
            "src/fern/inlined/types/__init__.py",
            "src/fern/inlined/types/inlined_index_response.py",
            "src/fern/inlined/types/inlined_search_request_filter.py",
            "src/fern/inlined/types/inlined_search_response.py",
            "src/fern/inlined/types/inlined_search_response_neighbor.py",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/cookies/__init__.py",
            "src/fern/cookies/client.py",
            "src/fern/cookies/raw_client.py",
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
            "src/fern/forms/__init__.py",
            "src/fern/forms/client.py",
            "src/fern/forms/raw_client.py",
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
            "src/fern/py.typed",
            "src/fern/shapes/__init__.py",
            "src/fern/shapes/client.py",
            "src/fern/shapes/raw_client.py",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/accounts/__init__.py",
            "src/fern/accounts/client.py",
            "src/fern/accounts/raw_client.py",
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
            "src/fern/enums/__init__.py",
            "src/fern/enums/client.py",
            "src/fern/enums/raw_client.py",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/environment.py",
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
            "src/fern/py.typed",
            "src/fern/subscriptions/__init__.py",
            "src/fern/subscriptions/client.py",
            "src/fern/subscriptions/raw_client.py",
            "src/fern/types/__init__.py",
            "src/fern/types/event.py",
            "src/fern/types/subscription.py",
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
            "src/fern/py.typed",
            "src/fern/user/__init__.py",
            "src/fern/user/client.py",
            "src/fern/user/raw_client.py",
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
        matched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/auth/__init__.py",
            "src/fern/auth/client.py",
            "src/fern/auth/raw_client.py",
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
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/token_response.py",
            "src/fern/types/user.py",
            "src/fern/users/__init__.py",
            "src/fern/users/client.py",
            "src/fern/users/raw_client.py",
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
            "src/fern/items/__init__.py",
            "src/fern/items/client.py",
            "src/fern/items/raw_client.py",
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
            "src/fern/py.typed",
            "src/fern/types/__init__.py",
            "src/fern/types/user.py",
            "src/fern/users/__init__.py",
            "src/fern/users/client.py",
            "src/fern/users/raw_client.py",
            "src/fern/version.py",
        ],
    },
];

/// Path to a fixture directory under `tests/fixtures/`.
fn fixture_dir(api: &str) -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures")
        .join(api)
}

/// Fresh `crozier` command bound to the built binary.
fn crozier() -> Command {
    Command::cargo_bin("crozier").expect("crozier binary is built for tests")
}

/// Normalize a lazy-loader `__init__.py` for comparison: drop leading blank lines
/// (a comment-strip artifact) and canonicalize the import order with `ruff` isort,
/// so the semantically-irrelevant `TYPE_CHECKING` ordering does not gate the match.
fn normalize_init(content: &str) -> String {
    let trimmed: String = content
        .split_inclusive('\n')
        .skip_while(|line| line.trim().is_empty())
        .collect();
    ruff_isort(&trimmed)
}

/// Run `ruff check --select I --fix` over a source string, returning the
/// import-sorted result. Uses the same `ruff` the generator depends on.
fn ruff_isort(source: &str) -> String {
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
        .expect("ruff is on PATH for the e2e (see docs/matching.md)");
    child
        .stdin
        .take()
        .expect("piped stdin")
        .write_all(source.as_bytes())
        .expect("write to ruff");
    let out = child.wait_with_output().expect("ruff ran");
    // Trust ruff's stdout only when it exited cleanly — a non-zero exit (e.g. a
    // syntax error in the input) must surface, not silently yield wrong text.
    assert!(
        out.status.success(),
        "ruff isort failed ({}): {}",
        out.status,
        String::from_utf8_lossy(&out.stderr)
    );
    String::from_utf8(out.stdout).expect("ruff output is UTF-8")
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
        assert!(
            generated_matches_fixture(rel, &generated, &expected),
            "generated {rel} does not match the Fern fixture"
        );
    }
}

/// Generate a corpus's SDK into a fresh tempdir with that corpus's naming, and
/// return the dir (the caller keeps it alive). Fails the test if crozier errors —
/// shared by the gate and the candidate reporter so both drive the binary
/// identically.
fn generate_corpus(c: &Corpus) -> tempfile::TempDir {
    let out = tempfile::tempdir().expect("tempdir");
    crozier()
        .args(["generate", "--spec"])
        .arg(fixture_dir(c.api).join("openapi.yml"))
        .arg("--output")
        .arg(out.path())
        .args([
            "--package-name",
            c.package_name,
            "--project-name",
            c.project_name,
        ])
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    out
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
fn generated_matches_fixture(rel: &str, generated: &str, expected: &str) -> bool {
    let (actual, expected) = if rel.ends_with("__init__.py") {
        (
            normalize_init(&crozier::strip_python_comments(generated)),
            normalize_init(expected),
        )
    } else if rel.ends_with(".py") {
        (
            crozier::strip_python_comments(generated),
            expected.to_string(),
        )
    } else {
        (generated.to_string(), expected.to_string())
    };
    actual == expected
}

#[test]
fn query_parameters_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&QUERY_PARAMETERS);
}

#[test]
fn exhaustive_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&EXHAUSTIVE);
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
    let mut corpora: Vec<&Corpus> = vec![&QUERY_PARAMETERS, &EXHAUSTIVE];
    corpora.extend(FEATURE_TARGETS.iter());

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

/// Every file under `root`, as `/`-separated paths relative to `root`, sorted.
/// A small hand-rolled walk to avoid a `walkdir` dev-dependency for one use.
fn walk_files(root: &Path) -> Vec<String> {
    fn rec(base: &Path, dir: &Path, out: &mut Vec<String>) {
        let mut entries: Vec<PathBuf> = std::fs::read_dir(dir)
            .unwrap_or_else(|e| panic!("read_dir {}: {e}", dir.display()))
            .map(|e| e.expect("dir entry").path())
            .collect();
        entries.sort();
        for path in entries {
            if path.is_dir() {
                rec(base, &path, out);
            } else {
                let rel = path.strip_prefix(base).expect("path is under base");
                out.push(rel.to_string_lossy().replace('\\', "/"));
            }
        }
    }
    let mut out = Vec::new();
    if root.is_dir() {
        rec(root, root, &mut out);
    }
    out
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
        out.join("src/acme/get_all_widgets").is_dir(),
        "hyphenated operationId should sanitize to a legal module directory"
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
        out.join("src/acme/verify_code").is_dir(),
        "spaced operationId should sanitize to a legal module directory"
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
