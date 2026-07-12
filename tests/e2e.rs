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
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
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
            "src/fern/types/__init__.py",
            "src/fern/types/thing.py",
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
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            ".fern/metadata.json",
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
            "src/fern/errors/__init__.py",
            "src/fern/errors/bad_request_error.py",
            "src/fern/errors/internal_server_error.py",
            "src/fern/errors/not_found_error.py",
            "src/fern/errors/service_unavailable_error.py",
            "src/fern/errors/unprocessable_entity_error.py",
            "src/fern/types/__init__.py",
            "src/fern/types/error.py",
            "src/fern/types/widget.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            ".fern/metadata.json",
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
            "src/fern/gadgets/__init__.py",
            "src/fern/gadgets/client.py",
            "src/fern/gadgets/raw_client.py",
            "src/fern/gadgets/types/__init__.py",
            "src/fern/gadgets/types/create_gadget_response.py",
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
            "src/fern/widgets/types/__init__.py",
            "src/fern/widgets/types/list_widgets_request_level.py",
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
            "src/fern/types/widget.py",
            "src/fern/types/widget_detail.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/types/widget.py",
            "src/fern/types/widget_detail.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            ".fern/metadata.json",
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
            "src/fern/messages/__init__.py",
            "src/fern/messages/client.py",
            "src/fern/messages/raw_client.py",
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
            "src/fern/types/widget.py",
            "src/fern/types/widget_scope.py",
            "src/fern/types/widget_status.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/types/widget.py",
            "src/fern/types/widget_binding.py",
            "src/fern/types/widget_owner.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
            "src/fern/types/widget.py",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
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
fn normalize_init(content: &str) -> String {
    let trimmed: String = content
        .split_inclusive('\n')
        .skip_while(|line| line.trim().is_empty())
        .collect();
    ruff_isort(&trimmed)
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
        .args(c.audiences.iter().flat_map(|a| ["--audience", a]))
        .args(c.audience_strict.then_some("--audience-strict"))
        .args(
            c.client_class_name
                .iter()
                .flat_map(|n| ["--client-class-name", n]),
        )
        .args(c.extra_fields.iter().flat_map(|e| ["--extra-fields", e]))
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
///
/// The SDK-identity headers are also normalized out of both sides (see
/// [`normalize_sdk_headers`]): crozier's `X-Crozier-*` rebrand and the
/// packaging-only `SDK-Name`/`SDK-Version` lines are deliberate, non-behavioral
/// differences in tool branding/packaging.
fn generated_matches_fixture(rel: &str, generated: &str, expected: &str) -> bool {
    let generated = normalize_sdk_headers(generated);
    let expected = normalize_sdk_headers(expected);
    let (actual, expected) = if rel.ends_with("__init__.py") {
        (
            normalize_init(&crozier::strip_python_comments(&generated)),
            normalize_init(&expected),
        )
    } else if rel.ends_with(".py") {
        (crozier::strip_python_comments(&generated), expected)
    } else if rel.ends_with("metadata.json") {
        (
            normalize_metadata(&generated),
            normalize_metadata(&expected),
        )
    } else {
        (generated, expected)
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
/// `X-Fern-*`), which the recorder folds to a common prefix on both sides — the
/// runtime analog of the byte-diff's `normalize_sdk_headers`. This is the
/// in-process analog of Fern's own WireMock
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
