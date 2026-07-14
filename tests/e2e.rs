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
        "src/fern/_/__init__.py",
        "src/fern/_/client.py",
        "src/fern/_/raw_client.py",
        "src/fern/_/types/__init__.py",
        "src/fern/_/types/get_available_locales_response.py",
        "src/fern/_/types/get_common_settings_response.py",
        "src/fern/_/types/get_global_alerts_response.py",
        "src/fern/_/types/get_user_system_overrides_response.py",
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
/// any matched corpus. crozier consumes it today (224 files); golden pending.
const DISCOURSE: Corpus = Corpus {
    api: "discourse.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    matched: &[],
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
    if corpus_spec(BUNQ.api).is_some() {
        corpora.push(&BUNQ);
    }
    if corpus_spec(BUNGIE.api).is_some() {
        corpora.push(&BUNGIE);
    }
    // The five batch corpora (issue #77): fetched, not vendored — include each only
    // when its source spec is present, exactly as the byte-diff gate skips it offline.
    for c in [
        &ANCHORE,
        &APACHE_AIRFLOW,
        &DISCOURSE,
        &APPWRITE_SERVER,
        &APICURIO,
    ] {
        if corpus_spec(c.api).is_some() {
            corpora.push(c);
        }
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
fn numeric_field_segments_collapse_and_keep_wire_aliases() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [day_0_end_time]\n                properties:\n                  day_0_end_time: { type: integer }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("response model is generated");
    assert!(
        model.contains("day0end_time: typing_extensions.Annotated[int, FieldMetadata(alias=\"day_0_end_time\")]"),
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
        widget.contains("target: typing.Dict[str, typing.Optional[typing.Any]]"),
        "additionalProperties without an explicit object type should be an open map: {widget}"
    );
    assert!(
        widget.contains("extra: typing.Optional[typing.Any] = None"),
        "an unknown optional field keeps Fern's existing single-optional annotation: {widget}"
    );
}

#[test]
fn unknown_metadata_fields_are_double_optional() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      responses:\n        \
         '200': { description: OK, content: { application/json: { schema: { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  \
         schemas:\n    Widget:\n      type: object\n      properties:\n        metadata: {}\n        unknown: {}\n",
    );
    let widget =
        std::fs::read_to_string(out.join("src/acme/types/widget.py")).expect("Widget model");
    assert!(
        widget.contains("metadata: typing.Optional[typing.Optional[typing.Any]] = None"),
        "unknown metadata fields should match Fern's double-optional annotation: {widget}"
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
        raw.contains("type_=typing.Optional[typing.Any]"),
        "a status class with any bodyless response should parse every branch as Optional[Any]: {raw}"
    );
    let error = std::fs::read_to_string(out.join("src/acme/errors/bad_request_error.py"))
        .expect("BadRequestError is generated");
    assert!(
        error.contains("body: typing.Optional[typing.Any]"),
        "the generated error class should also accept Optional[Any]: {error}"
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
        error.contains("body: typing.Optional[typing.Any]")
            && raw.contains("type_=typing.Optional[typing.Any]"),
        "a shared status with conflicting body schemas should use Optional[Any]:\n{error}\n{raw}"
    );
}

#[test]
fn unknown_array_items_are_optional_any_elements() {
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
        widget.contains("values: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None"),
        "arrays of unknown items should preserve Optional[Any] element types: {widget}"
    );
}

#[test]
fn array_item_enums_hoist_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        - name: \
         status\n          in: query\n          required: false\n          schema:\n            type: array\n            \
         items: { type: string, enum: [active, archived] }\n      responses:\n        '200':\n          \
         description: OK\n          content:\n            application/json:\n              schema:\n                \
         type: array\n                items: { type: string, enum: [public, private] }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/widgets/client.py"))
        .expect("widgets client is generated");
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
        client.contains("typing.List[ListWidgetsResponseItem]"),
        "response array item enums should use the named enum in return types: {client}"
    );
    let reference =
        std::fs::read_to_string(out.join("reference.md")).expect("reference.md is generated");
    assert!(
        reference.contains(
            "**status:** `typing.Optional[\n    typing.Union[\n        ListWidgetsRequestStatusItem,\n        typing.Sequence[ListWidgetsRequestStatusItem],\n    ]\n]`"
        ),
        "reference tables should wrap scalar-or-sequence array query annotations: {reference}"
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
fn openapi_31_null_only_array_items_are_optional_any() {
    let (_dir, out) = generate_ok(
        "openapi: 3.1.0\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widget:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [values]\n                properties:\n                  values:\n                    type: array\n                    items: { type: ['null'] }\n",
    );
    let model = std::fs::read_to_string(out.join("src/acme/widgets/types/get_widget_response.py"))
        .expect("inline response model is generated");
    assert!(
        model.contains("values: typing.List[typing.Optional[typing.Any]]"),
        "null-only items should remain optional unknown values: {model}"
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
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /search:\n    get:\n      operationId: search\n      tags: [Search]\n      responses:\n        '200':\n          description: Found\n          content:\n            application/json:\n              schema:\n                type: object\n                required: [result]\n                properties:\n                  result:\n                    type: object\n                    required: [count]\n                    properties:\n                      count: { type: integer }\n  /health:\n    get:\n      operationId: getHealth\n      tags: [System]\n      responses:\n        '204': { description: Healthy }\n",
    );
    let client =
        std::fs::read_to_string(out.join("src/acme/client.py")).expect("root client is generated");
    assert!(
        client.contains("def search(") && !client.contains("def search(self):"),
        "an operation named exactly for its tag should remain a root method: {client}"
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
            && raw.contains("CreateWidgetRequestXWidgetMode"),
        "inline header enums should hoist under the endpoint tag: {raw}"
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
            "**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response."
        ),
        "binary response reference docs should mention stream request_options: {reference}"
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
}

#[test]
fn wildcard_binary_requests_with_path_params_omit_json_content_type() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/test:\n    put:\n      operationId: testWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { type: string } }\n      requestBody:\n        required: true\n        content:\n          '*/*':\n            schema: { $ref: '#/components/schemas/FileContent' }\n      responses:\n        '204': { description: Tested }\ncomponents:\n  schemas:\n    FileContent: { type: string, format: binary }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("json=request,") && !raw.contains("\"content-type\": \"application/json\""),
        "wildcard binary-schema requests should not gain JSON headers from path params: {raw}"
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
fn optional_converted_body_fields_use_optional_annotations() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    patch:\n      operationId: patchWidget\n      tags: [widgets]\n      requestBody:\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/UpdateWidget' }\n      responses:\n        '204': { description: Updated }\ncomponents:\n  schemas:\n    WidgetMeta:\n      type: object\n      properties:\n        type: { type: string }\n    UpdateWidget:\n      type: object\n      properties:\n        metadata: { $ref: '#/components/schemas/WidgetMeta', nullable: true, readOnly: true }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("annotation=typing.Optional[WidgetMeta], direction=\"write\"")
            && raw.contains("metadata: typing.Optional[WidgetMeta] = OMIT"),
        "conversion metadata should carry the same optionality as the body argument: {raw}"
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
            && state.contains("class WidgetState(str, enum.Enum):\n    \"\"\" \"\"\"\n\n    ACTIVE = \"ACTIVE\""),
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
        raw.contains("request: typing.Dict[str, typing.Optional[typing.Any]]")
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
