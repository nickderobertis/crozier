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
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
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
            "src/fern/pred/__init__.py",
            "src/fern/py.typed",
            "src/fern/tree/__init__.py",
            "src/fern/tree/client.py",
            "src/fern/types/__init__.py",
            // The recursion payoff: a self-referential model and a recursive
            // discriminated union, each with forward refs + `update_forward_refs`.
            "src/fern/types/and_node.py",
            "src/fern/types/leaf_node.py",
            "src/fern/types/node.py",
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
            "src/fern/py.typed",
            "src/fern/version.py",
            "src/fern/widgets/__init__.py",
            "src/fern/widgets/client.py",
            "src/fern/widgets/raw_client.py",
            "src/fern/widgets/types/__init__.py",
            // The fix's payoff: a nested per-operation type reaching `core` at the
            // right relative depth (`...core.serialization`, not `..core`).
            "src/fern/widgets/types/update_widget_request_details.py",
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

/// The OpenAPI spec a corpus generates from. A vendored corpus ships its
/// `openapi.yml`; a `link-ok` corpus (`tests/fixtures/CORPUS.md`, spec not
/// redistributed) is fetched into `.local/corpus/<api>/openapi.json` by
/// `scripts/fetch-corpus.sh` — `None` when that fetch has not run.
fn corpus_spec(api: &str) -> Option<PathBuf> {
    let vendored = fixture_dir(api).join("openapi.yml");
    if vendored.exists() {
        return Some(vendored);
    }
    let fetched = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(".local/corpus")
        .join(api)
        .join("openapi.json");
    fetched.exists().then_some(fetched)
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
    crozier()
        .args(["generate", "--spec"])
        .arg(corpus_spec(c.api).unwrap_or_else(|| fixture_dir(c.api).join("openapi.yml")))
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
    let generated = normalize_sdk_headers(generated);
    let expected = normalize_sdk_headers(expected);
    if rel.ends_with("__init__.py") {
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
    "pyproject.toml",
    "requirements.txt",
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
    let mut corpora: Vec<&Corpus> = vec![&QUERY_PARAMETERS, &EXHAUSTIVE, &BUNQ];
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
/// to fixture paths containing `<substr>`. Pure reporter — it never asserts on a
/// diff (a diff is the point), but it guards against a silently-broken walk that
/// would print "no differences" as a false negative.
#[test]
#[ignore = "mismatch-investigation aid, not a gate; run via `just fixtures-diff`"]
fn report_fixture_diffs() {
    let corpus_filter = std::env::var("CROZIER_DIFF_CORPUS")
        .ok()
        .filter(|s| !s.is_empty());
    let file_filter = std::env::var("CROZIER_DIFF_FILE")
        .ok()
        .filter(|s| !s.is_empty());

    let mut corpora: Vec<&Corpus> = vec![&QUERY_PARAMETERS, &EXHAUSTIVE];
    corpora.extend(FEATURE_TARGETS.iter());
    // apideck's spec is fetched, not vendored; include it only when present, so the
    // reporter skips it exactly as the byte-diff gate does on an offline checkout.
    if corpus_spec(APIDECK_CRM.api).is_some() {
        corpora.push(&APIDECK_CRM);
    }
    if let Some(f) = &corpus_filter {
        corpora.retain(|c| c.api == f.as_str());
        assert!(
            !corpora.is_empty(),
            "CROZIER_DIFF_CORPUS={f:?} matched no corpus (or its spec is unfetched)"
        );
    }

    let mut total = 0usize;
    for c in corpora {
        let expected_root = fixture_dir(c.api).join("expected");
        let matched: std::collections::HashSet<&str> = c.matched.iter().copied().collect();
        let out = generate_corpus(c);

        let files = walk_files(&expected_root);
        // Guard the pipeline: a corpus always has expected files, so an empty walk
        // means a broken path — fail loudly rather than reporting "no differences".
        // Skipped when a file filter is set (it may legitimately match nothing).
        if file_filter.is_none() {
            assert!(
                !files.is_empty(),
                "{}: no files under {} — the fixture walk is broken",
                c.api,
                expected_root.display()
            );
        }

        println!("\n=== {} ===", c.api);
        let mut printed = 0usize;
        for rel in files {
            if let Some(f) = &file_filter {
                if !rel.contains(f.as_str()) {
                    continue;
                }
            }
            let Ok(expected) = std::fs::read_to_string(expected_root.join(&rel)) else {
                continue; // binary/unreadable — nothing in the corpus is today.
            };
            let generated = match std::fs::read_to_string(out.path().join(&rel)) {
                Ok(g) => g,
                Err(_) => {
                    println!("\n--- {rel} ---\n  crozier did not emit this file.");
                    printed += 1;
                    continue;
                }
            };
            if generated_matches_fixture(&rel, &generated, &expected) {
                continue;
            }
            let (actual, expected) = normalized_pair(&rel, &generated, &expected);
            let diff = unified_diff(&expected, &actual).unwrap_or_default();
            // A file already in `matched` differing is a regression, not a coverage
            // gap — flag it so it reads differently from a not-yet-matched file.
            let tag = if matched.contains(rel.as_str()) {
                " [REGRESSION — in `matched`]"
            } else {
                ""
            };
            println!("\n--- {rel}{tag} (`-` Fern golden, `+` crozier) ---\n{diff}");
            printed += 1;
        }
        if printed == 0 {
            println!("  no differences.");
        }
        total += printed;
    }
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
