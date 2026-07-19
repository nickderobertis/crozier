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
/// byte-for-byte today (paths relative to the output root). `unmatched` is the
/// measured residual task list; every other expected file is gated.
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
    unmatched: &'static [&'static str],
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
    unmatched: &[
        ".fern/metadata.json",
        ".github/workflows/ci.yml",
        ".gitignore",
        "README.md",
        "poetry.lock",
        "pyproject.toml",
        "reference.md",
        "snippet.json",
        "src/seed/_default_clients.py",
        "src/seed/client.py",
        "src/seed/core/client_wrapper.py",
        "src/seed/core/http_client.py",
        "src/seed/raw_client.py",
        "tests/custom/test_client.py",
        "tests/utils/__init__.py",
        "tests/utils/assets/models/__init__.py",
        "tests/utils/assets/models/circle.py",
        "tests/utils/assets/models/color.py",
        "tests/utils/assets/models/object_with_defaults.py",
        "tests/utils/assets/models/object_with_optional_field.py",
        "tests/utils/assets/models/shape.py",
        "tests/utils/assets/models/square.py",
        "tests/utils/assets/models/undiscriminated_shape.py",
        "tests/utils/test_http_client.py",
        "tests/utils/test_query_encoding.py",
        "tests/utils/test_serialization.py",
    ],
};

/// The broad legacy `exhaustive` target: Fern 4.35 output over the vendored
/// OpenAPI document (see scripts/generate-fern-fixture.sh). Its residual list
/// captures paths changed by the Fern 5.20 upgrade.
/// See docs/matching.md.
const EXHAUSTIVE: Corpus = Corpus {
    api: "exhaustive",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/endpoints_container/raw_client.py",
        "src/fern/endpoints_content_type/raw_client.py",
        "src/fern/endpoints_enum/raw_client.py",
        "src/fern/endpoints_http_methods/raw_client.py",
        "src/fern/endpoints_object/client.py",
        "src/fern/endpoints_object/raw_client.py",
        "src/fern/endpoints_pagination/raw_client.py",
        "src/fern/endpoints_params/raw_client.py",
        "src/fern/endpoints_primitive/raw_client.py",
        "src/fern/endpoints_put/raw_client.py",
        "src/fern/endpoints_union/raw_client.py",
        "src/fern/endpoints_urls/raw_client.py",
        "src/fern/inlinedrequests/raw_client.py",
        "src/fern/noauth/raw_client.py",
        "src/fern/noreqbody/raw_client.py",
        "src/fern/reqwithheaders/raw_client.py",
        "src/fern/types/endpoints_error_category.py",
        "src/fern/types/endpoints_error_code.py",
        "src/fern/types/types_animal_one_animal.py",
        "src/fern/types/types_animal_zero_animal.py",
        "src/fern/types/types_cat.py",
        "src/fern/types/types_documented_unknown_type.py",
        "src/fern/types/types_dog.py",
        "src/fern/types/types_double_optional.py",
        "src/fern/types/types_map_of_documented_unknown_type.py",
        "src/fern/types/types_nested_object_with_optional_field.py",
        "src/fern/types/types_nested_object_with_required_field.py",
        "src/fern/types/types_object_with_datetime_like_string.py",
        "src/fern/types/types_object_with_documented_unknown_type.py",
        "src/fern/types/types_object_with_map_of_map.py",
        "src/fern/types/types_object_with_optional_field.py",
        "src/fern/types/types_object_with_unknown_field.py",
        "src/fern/types/types_weather_report.py",
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
/// so the corpora drive crozier with the same naming. Each `unmatched` list is a
/// measured residual task list.
const FEATURE_TARGETS: &[Corpus] = &[
    Corpus {
        api: "auth-schemes",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/apikeyauth/raw_client.py",
            "src/fern/basicauth/raw_client.py",
            "src/fern/bearerauth/raw_client.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/oauth/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/inlined/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/cookies/raw_client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/forms/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/shapes/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/accounts/raw_client.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/enums/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/subscriptions/raw_client.py",
            "src/fern/types/event.py",
            "src/fern/types/subscription.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/user/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/auth/raw_client.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/users/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/items/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/users/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/widgets/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/widgets/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/errors/not_found_error.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/gadgets/raw_client.py",
            "src/fern/widgets/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/widgets/raw_client.py",
            "src/fern/widgets/types/list_widgets_request_level.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/messages/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/types/widget_scope.py",
            "src/fern/types/widget_status.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/types/widget_binding.py",
            "src/fern/types/widget_owner.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/pred/raw_client.py",
            "src/fern/tree/raw_client.py",
            "src/fern/types/and_node.py",
            "src/fern/types/node.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
            "src/fern/widgets/raw_client.py",
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
        unmatched: &[
            ".fern/metadata.json",
            "README.md",
            "pyproject.toml",
            "reference.md",
            "requirements.txt",
            "src/fern/__init__.py",
            "src/fern/client.py",
            "src/fern/core/__init__.py",
            "src/fern/core/client_wrapper.py",
            "src/fern/core/datetime_utils.py",
            "src/fern/core/http_client.py",
            "src/fern/core/http_response.py",
            "src/fern/core/http_sse/_api.py",
            "src/fern/core/http_sse/_decoders.py",
            "src/fern/core/jsonable_encoder.py",
            "src/fern/core/pydantic_utilities.py",
            "src/fern/core/request_options.py",
            "src/fern/core/serialization.py",
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

/// Require every Fern file except explicit residual gaps to match byte-for-byte.
fn assert_corpus_matches(c: &Corpus) {
    let fixtures = fixture_dir(c.api);
    let out = generate_corpus(c);

    let expected_root = fixtures.join("expected");
    for rel in walk_files(&expected_root) {
        if c.unmatched.contains(&rel.as_str()) {
            continue;
        }
        let generated = std::fs::read_to_string(out.path().join(&rel))
            .unwrap_or_else(|e| panic!("crozier did not write {rel}: {e}"));
        let expected = std::fs::read_to_string(expected_root.join(&rel))
            .unwrap_or_else(|e| panic!("missing fixture {rel}: {e}"));
        if !generated_matches_fixture(&rel, &generated, &expected) {
            // Show the exact gate-relevant diff inline instead of a bare "does not
            // match" — the normalized bytes the comparison actually decides on, so a
            // regression is diagnosable straight from the test output (no second
            // generate-and-diff pass). `just fixtures-diff` prints the same thing on
            // demand for a file not (yet) in `matched`.
            let (actual, expected) = normalized_pair(&rel, &generated, &expected);
            let diff = unified_diff(&expected, &actual).unwrap_or_default();
            panic!(
                "generated {rel} does not match the Fern fixture \
                 (normalized diff; `-` = Fern golden, `+` = crozier). \
                 Reproduce with `just fixtures-diff {} {rel}`; fix the generator, \
                 never the fixture; if this is a genuine open gap, add the path \
                 to `unmatched`.\n{diff}",
                c.api
            );
        }
    }

    for rel in c.unmatched {
        let expected = std::fs::read_to_string(expected_root.join(rel))
            .unwrap_or_else(|e| panic!("unmatched path is not in the Fern fixture: {rel}: {e}"));
        if let Ok(generated) = std::fs::read_to_string(out.path().join(rel)) {
            assert!(
                !generated_matches_fixture(rel, &generated, &expected),
                "{rel} now matches Fern — remove it from `unmatched`"
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

/// `apideck.com-crm`: a real-world `link-ok` corpus API (issue #77). Its OpenAPI
/// spec is fetched, not vendored (`corpus_spec`); its full Fern golden is
/// committed and reproduced byte-for-byte.
const APIDECK_CRM: Corpus = Corpus {
    api: "apideck.com-crm",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_HRIS: Corpus = Corpus {
    api: "apideck.com-hris",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

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
    assert_corpus_matches(&APIDECK_CRM);
}

/// `bunq.com`: a large real-world `link-ok` corpus API (issue #77) — 421 endpoints
/// across 118 sub-clients (~10× apideck), the pipeline's at-scale stress target. Its
/// OpenAPI spec is fetched, not vendored (`corpus_spec`); its full Fern golden is
/// committed. crozier reproduces the files in [`BUNQ.unmatched`] byte-for-byte; the
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
    unmatched: &[],
};

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
    unmatched: &[],
};

// ---------------------------------------------------------------------------
// Five additional real-world `link-ok` corpora (issue #77), added together as a
// batch of harder, feature-diverse targets. Each passes `fern check` cleanly (the
// prerequisite — Fern must accept the raw spec first); their Fern golden `expected/`
// trees are generated with Docker (`just fixtures-generate-corpus --only <name>`)
// and land in the same PR before byte-matching begins. `unmatched` is populated
// by `just fixtures-gaps` and shrinks as the generator is brought to a byte-match.
// Where crozier does not yet consume the spec cleanly, the gap is named
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
    unmatched: &[],
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
    unmatched: &[],
};

/// `discourse.local`: the Discourse API — an all-inline shape (0 named component
/// schemas; ~113 inline request/response objects Fern must coin names for), unlike
/// any fully matched corpus. Fully matched: all 328 files reproduce Fern byte-for-byte.
const DISCOURSE: Corpus = Corpus {
    api: "discourse.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
};

const DND5EAPI: Corpus = Corpus {
    api: "dnd5eapi.co",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APACHE_QAKKA: Corpus = Corpus {
    api: "apache.org-qakka",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const AUTHENTIQIO: Corpus = Corpus {
    api: "6-dot-authentiqio.appspot.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const ETSI_MEC010_2: Corpus = Corpus {
    api: "etsi.local-mec010-2_apppkgmgmt",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_WEBHOOK: Corpus = Corpus {
    api: "apideck.com-webhook",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_VAULT: Corpus = Corpus {
    api: "apideck.com-vault",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const AIRBYTE_CONFIG: Corpus = Corpus {
    api: "airbyte.local-config",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const BINTABLE: Corpus = Corpus {
    api: "bintable.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIS_GURU: Corpus = Corpus {
    api: "apis.guru",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const COLOR_PIZZA: Corpus = Corpus {
    api: "color.pizza",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const BYAUTOMATA_IO: Corpus = Corpus {
    api: "byautomata.io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_PROXY: Corpus = Corpus {
    api: "apideck.com-proxy",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_CONNECTOR: Corpus = Corpus {
    api: "apideck.com-connector",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_ECOMMERCE: Corpus = Corpus {
    api: "apideck.com-ecommerce",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_ISSUE_TRACKING: Corpus = Corpus {
    api: "apideck.com-issue-tracking",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APPWRITE_CLIENT: Corpus = Corpus {
    api: "appwrite.io-client",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_FILE_STORAGE: Corpus = Corpus {
    api: "apideck.com-file-storage",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_ACCOUNTING: Corpus = Corpus {
    api: "apideck.com-accounting",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
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
    unmatched: &[
        ".fern/metadata.json",
        "README.md",
        "pyproject.toml",
        "reference.md",
        "requirements.txt",
        "src/fern/__init__.py",
        "src/fern/client.py",
        "src/fern/core/__init__.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/raw_client.py",
    ],
};

const EOS: Corpus = Corpus {
    api: "eos.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_SMS: Corpus = Corpus {
    api: "apideck.com-sms",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_ECOSYSTEM: Corpus = Corpus {
    api: "apideck.com-ecosystem",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_CUSTOMER_SUPPORT: Corpus = Corpus {
    api: "apideck.com-customer-support",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APIDECK_LEAD: Corpus = Corpus {
    api: "apideck.com-lead",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const APACHE_ORG_AIRFLOW: Corpus = Corpus {
    api: "apache.org-airflow",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const OPENFIGI: Corpus = Corpus {
    api: "openfigi.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const TWILIO_VOICE_V1: Corpus = Corpus {
    api: "twilio.com-twilio_voice_v1",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const MICROCKS_LOCAL: Corpus = Corpus {
    api: "microcks.local",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const REDHAT_CATALOG_INVENTORY: Corpus = Corpus {
    api: "redhat.com-catalog_inventory",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const XERO_PAYROLL_AU: Corpus = Corpus {
    api: "xero.com-xero-payroll-au",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const TRACCAR: Corpus = Corpus {
    api: "traccar.org",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const REVERB_COM: Corpus = Corpus {
    api: "reverb.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const MAIF_OTOROSHI: Corpus = Corpus {
    api: "maif.local-otoroshi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const PORTFOLIOOPTIMIZER_IO: Corpus = Corpus {
    api: "portfoliooptimizer.io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const OPENBANKING_ORG_UK_ACCOUNT_INFO_OPENAPI: Corpus = Corpus {
    api: "openbanking.org.uk-account-info-openapi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const NETBOX_DEV: Corpus = Corpus {
    api: "netbox.dev",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
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
fn every_unmatched_entry_exists_in_its_own_golden() {
    // Single source of truth: iterate the CORPORA registry directly and identify each
    // corpus by its unique `api` (which maps 1:1 to a `const _: Corpus`), so there is no
    // parallel name array to drift out of sync with it.
    let mut violations = Vec::new();
    for corpus in CORPORA {
        let expected = fixture_dir(corpus.api).join("expected");
        for relative in corpus.unmatched {
            if !expected.join(relative).is_file() {
                violations.push(format!("{} -> {relative}", corpus.api));
            }
        }
    }
    assert!(
        violations.is_empty(),
        "unmatched entries missing from their corpus golden:\n{}",
        violations.join("\n")
    );
}

#[test]
fn bunq_matches_fern_output() {
    // `link-ok` like apideck: the spec is fetched (not vendored), so this **skips**
    // when it is absent — including the offline `check` gate — and **fails** when
    // `CROZIER_REQUIRE_CORPUS` is set (the CI corpus leg fetches first, then sets
    // it), so the enforced leg can never silently no-op. Unlike apideck, bunq is not
    // yet fully matched, so this byte-compares only `BUNQ.unmatched` (via
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
    // `BUNGIE_UNMATCHED` covers the full committed golden, so this enforces the
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
    unmatched: &[],
};

const AMAZONAWS_COM_CLOUDFORMATION: Corpus = Corpus {
    api: "amazonaws.com-cloudformation",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &[],
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
    unmatched: &["reference.md"],
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
    unmatched: &[],
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
    // Every feature target walks its complete expected tree; only measured
    // residual paths in `unmatched` are exempted and reverse-checked.
    for target in FEATURE_TARGETS {
        assert_corpus_matches(target);
    }
}

/// Measurement aid — generate every available corpus and print the exact residual
/// `unmatched` task list. Run via `just fixtures-gaps`.
#[test]
#[ignore = "corpus census aid, not a gate; run via `just fixtures-gaps`"]
fn report_fixture_gaps() {
    let corpus_filter = std::env::var("CROZIER_GAPS_CORPUS")
        .ok()
        .filter(|value| !value.is_empty());
    let mut corpora = registered_diff_corpora();
    corpora.retain(|corpus| corpus_spec(corpus.api).is_some());

    if let Some(filter) = &corpus_filter {
        corpora.retain(|corpus| corpus.api == filter);
        assert!(
            !corpora.is_empty(),
            "CROZIER_GAPS_CORPUS={filter:?} matched no corpus (or its spec is unfetched)"
        );
    }

    let corpus_count = corpora.len();
    let mut total_expected = 0usize;
    let mut total_unmatched = 0usize;
    for corpus in corpora {
        let expected_root = fixture_dir(corpus.api).join("expected");
        let expected_files = walk_files(&expected_root);
        let out = generate_corpus(corpus);
        let confirmed: std::collections::HashSet<String> = expected_files
            .iter()
            .filter(|rel| {
                let (Ok(expected), Ok(generated)) = (
                    std::fs::read_to_string(expected_root.join(rel)),
                    std::fs::read_to_string(out.path().join(rel)),
                ) else {
                    return false;
                };
                generated_matches_fixture(rel, &generated, &expected)
            })
            .cloned()
            .collect();
        let divergent: Vec<&String> = expected_files
            .iter()
            .filter(|rel| !confirmed.contains(rel.as_str()))
            .collect();

        println!("\n=== {} ===", corpus.api);
        println!("  {} expected file(s).", expected_files.len());
        if divergent.is_empty() {
            println!("  no unmatched files.");
        } else {
            println!(
                "  {} file(s) still unmatched — use as this corpus's `unmatched`:",
                divergent.len()
            );
            for rel in &divergent {
                println!("        \"{rel}\",");
            }
        }

        // Once the measured lists are installed, these checks ensure both sides
        // of the opt-out contract remain truthful.
        for rel in &expected_files {
            assert_eq!(
                confirmed.contains(rel.as_str()),
                !corpus.unmatched.contains(&rel.as_str()),
                "{}: `unmatched` census is stale for {rel}",
                corpus.api
            );
        }

        total_expected += expected_files.len();
        total_unmatched += divergent.len();
    }
    println!(
        "\n{total_unmatched} file(s) still unmatched across all corpora; \
         {total_expected} expected file(s) across {corpus_count} corpora."
    );
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

/// Mismatch-investigation aid — NOT a gate (ignored by default). Complementing
/// [`report_fixture_gaps`], it
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
        let unmatched: std::collections::HashSet<&str> = c.unmatched.iter().copied().collect();
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
            // A difference outside `unmatched` is a regression; explicit gaps
            // remain ordinary task-list entries.
            let tag = if unmatched.contains(rel.as_str()) {
                ""
            } else {
                " [REGRESSION — not in `unmatched`]"
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
