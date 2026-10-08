//! End-to-end tests: drive the compiled `crozier` binary the way a user does —
//! as a subprocess over real files in a real temp directory — and byte-compare
//! its (comment-stripped) output against the committed Fern fixtures.
//!
//! This is the product's only faithful QA loop, so it never mocks the generator,
//! the filesystem, or the process boundary. The `just check` gate runs it.

use std::path::{Path, PathBuf};

use assert_cmd::Command;
use crozier::departures::Context;
use crozier::parity::{self, Difference};
use predicates::prelude::*;

/// `crozier compare` journeys (a file under `tests/e2e/`, so cargo does not
/// build it as a test binary of its own).
#[path = "e2e/compare.rs"]
mod compare;

/// The "Migrating from Fern" guide's workflow, run from its own code blocks.
#[cfg(unix)]
#[path = "e2e/migration.rs"]
mod migration;

/// The GitHub Action's scripts (`scripts/action/`) over a real `crozier`.
#[cfg(unix)]
#[path = "e2e/action.rs"]
mod action;

/// `scripts/update-major-tag.sh`, the release's floating major tag.
#[cfg(unix)]
#[path = "e2e/major_tag.rs"]
mod major_tag;

/// `enum-type: literals` through the binary.
#[path = "e2e/literals.rs"]
mod literals;

/// `default-max-retries` through the binary.
#[path = "e2e/default_max_retries.rs"]
mod default_max_retries;

/// Non-default settings against Fern's overlay goldens (`expected-literals/`, …).
#[path = "e2e/overlay_goldens.rs"]
mod overlay_goldens;

/// The per-golden ledger of intended departures every golden comparison holds
/// its observed departures to.
#[path = "e2e/departures_ledger.rs"]
mod departures_ledger;

use departures_ledger::{GoldenLedger, Ledger, Observed};

/// The ledger's contract, driven through the gates' own comparison.
#[path = "e2e/departures_ledger_gate.rs"]
mod departures_ledger_gate;

/// A vendored Fern corpus: the spec at `tests/fixtures/<api>/openapi.yml`, the
/// naming flags crozier is driven with, and the generated files it reproduces
/// byte-for-byte today (paths relative to the output root). `unmatched` is the
/// measured residual task list — empty across the whole corpus today, so parity
/// is the default and every expected file is gated.
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
    /// (`ignore`) and `eos.local-extra-fields-forbid` (`forbid`) does.
    extra_fields: Option<&'static str>,
    unmatched: &'static [&'static str],
}

/// Files crozier emits that this corpus's Fern golden does not carry — the
/// file-set half of a declared residual, the mirror of `Corpus::unmatched`.
///
/// The comparison is bidirectional precisely so a crozier-only file cannot hide
/// behind Fern's tree lacking it, and this does not relax that: every such file is
/// **named here**, and the assertions that read this list fail if one of them
/// appears in the golden (it must enter byte comparison) or stops being emitted
/// (the list is stale). What it allows is registering a corpus whose measured
/// divergence includes names as well as bytes, which is the state
/// [`CORPUS.md`](../tests/fixtures/CORPUS.md)'s batch 14 records for `webflow-v2`:
/// 148 modules Fern names differently for a `oneOf` request body's hoisted
/// variants, listed rather than deleted so the next change to that naming has an
/// exact set to shorten.
fn crozier_only_files(c: &Corpus) -> &'static [&'static str] {
    if c.api == WEBFLOW_V2.api {
        WEBFLOW_V2_CROZIER_ONLY
    } else {
        &[]
    }
}

/// See [`crozier_only_files`]. Measured against the Fern 5.20.0 golden.
const WEBFLOW_V2_CROZIER_ONLY: &[&str] = &[
    "src/fern/collections/fields/types/create_fields_request_body_display_name_metadata.py",
    "src/fern/collections/fields/types/create_fields_request_body_display_name.py",
    "src/fern/collections/fields/types/create_fields_request_body_display_name_type.py",
    "src/fern/collections/fields/types/create_fields_request_body_one_metadata_options_item.py",
    "src/fern/collections/fields/types/create_fields_request_body_one_metadata.py",
    "src/fern/collections/fields/types/create_fields_request_body_one.py",
    "src/fern/collections/fields/types/create_fields_request_body_one_type.py",
    "src/fern/collections/fields/types/create_fields_request_body_zero.py",
    "src/fern/collections/fields/types/create_fields_request_body_zero_type.py",
    "src/fern/collections/fields/types/create_fields_response_display_name_metadata.py",
    "src/fern/collections/fields/types/create_fields_response_display_name.py",
    "src/fern/collections/fields/types/create_fields_response_display_name_type.py",
    "src/fern/collections/fields/types/create_fields_response_one_metadata_options_item.py",
    "src/fern/collections/fields/types/create_fields_response_one_metadata.py",
    "src/fern/collections/fields/types/create_fields_response_one.py",
    "src/fern/collections/fields/types/create_fields_response_one_type.py",
    "src/fern/collections/fields/types/create_fields_response_zero.py",
    "src/fern/collections/fields/types/create_fields_response_zero_type.py",
    "src/fern/collections/fields/types/update_fields_response_validations_additional_properties_additional_properties.py",
    "src/fern/collections/items/types/create_item_items_request_body_cms_locale_id_field_data.py",
    "src/fern/collections/items/types/create_item_items_request_body_cms_locale_id.py",
    "src/fern/collections/items/types/create_item_items_request_body_items_items_item_field_data.py",
    "src/fern/collections/items/types/create_item_items_request_body_items_items_item.py",
    "src/fern/collections/items/types/create_item_items_request_body_items.py",
    "src/fern/collections/items/types/create_item_live_items_request_body_cms_locale_id_field_data.py",
    "src/fern/collections/items/types/create_item_live_items_request_body_cms_locale_id.py",
    "src/fern/collections/items/types/create_item_live_items_request_body_items_items_item_field_data.py",
    "src/fern/collections/items/types/create_item_live_items_request_body_items_items_item.py",
    "src/fern/collections/items/types/create_item_live_items_request_body_items.py",
    "src/fern/collections/items/types/create_items_items_request_field_data_name.py",
    "src/fern/collections/items/types/create_items_items_request_field_data_one_item.py",
    "src/fern/collections/items/types/publish_item_items_request_body_item_ids.py",
    "src/fern/collections/items/types/publish_item_items_request_body_items_items_item.py",
    "src/fern/collections/items/types/publish_item_items_request_body_items.py",
    "src/fern/collections/types/create_collections_response_fields_item_validations_additional_properties_additional_properties.py",
    "src/fern/collections/types/get_collections_response_fields_item_validations_additional_properties_additional_properties.py",
    "src/fern/collections/types/patch_collections_response_fields_item_validations_additional_properties_additional_properties.py",
    "src/fern/types/post_collection_item_changed_payload_payload_field_data.py",
    "src/fern/types/post_collection_item_changed_payload_payload.py",
    "src/fern/types/post_collection_item_changed_payload.py",
    "src/fern/types/post_collection_item_changed_payload_trigger_type.py",
    "src/fern/types/post_collection_item_created_payload_payload_field_data.py",
    "src/fern/types/post_collection_item_created_payload_payload.py",
    "src/fern/types/post_collection_item_created_payload.py",
    "src/fern/types/post_collection_item_created_payload_trigger_type.py",
    "src/fern/types/post_collection_item_deleted_payload_payload_field_data.py",
    "src/fern/types/post_collection_item_deleted_payload_payload.py",
    "src/fern/types/post_collection_item_deleted_payload.py",
    "src/fern/types/post_collection_item_published_payload_payload_field_data.py",
    "src/fern/types/post_collection_item_published_payload_payload.py",
    "src/fern/types/post_collection_item_published_payload.py",
    "src/fern/types/post_collection_item_unpublished_payload_payload_field_data.py",
    "src/fern/types/post_collection_item_unpublished_payload_payload.py",
    "src/fern/types/post_collection_item_unpublished_payload.py",
    "src/fern/types/post_comment_created_payload_payload_author.py",
    "src/fern/types/post_comment_created_payload_payload_mentioned_users_item.py",
    "src/fern/types/post_comment_created_payload_payload.py",
    "src/fern/types/post_comment_created_payload_payload_type.py",
    "src/fern/types/post_comment_created_payload.py",
    "src/fern/types/post_ecomm_inventory_changed_payload_payload_inventory_type.py",
    "src/fern/types/post_ecomm_inventory_changed_payload_payload.py",
    "src/fern/types/post_ecomm_inventory_changed_payload.py",
    "src/fern/types/post_ecomm_inventory_changed_payload_trigger_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_all_addresses_item_japan_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_all_addresses_item.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_all_addresses_item_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_application_fee.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_billing_address_japan_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_billing_address.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_billing_address_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_customer_info.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_customer_paid.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_dispute_last_status.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_download_files_item.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_metadata.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_net_amount.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_paypal_details.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item_row_total.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item_variant_image_file.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item_variant_image_file_variants_item.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item_variant_image.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_purchased_items_item_variant_price.py",
    "src/fern/types/post_ecomm_new_order_payload_payload.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_shipping_address_japan_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_shipping_address.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_shipping_address_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_status.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_stripe_card_brand.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_stripe_card_expires.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_stripe_card.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_stripe_details.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals_extras_item_price.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals_extras_item.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals_extras_item_type.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals_subtotal.py",
    "src/fern/types/post_ecomm_new_order_payload_payload_totals_total.py",
    "src/fern/types/post_ecomm_new_order_payload.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_all_addresses_item_japan_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_all_addresses_item.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_all_addresses_item_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_application_fee.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_billing_address_japan_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_billing_address.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_billing_address_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_customer_info.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_customer_paid.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_dispute_last_status.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_download_files_item.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_metadata.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_net_amount.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_paypal_details.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item_row_total.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file_variants_item.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item_variant_image.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_purchased_items_item_variant_price.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_shipping_address_japan_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_shipping_address.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_shipping_address_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_status.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_stripe_card_brand.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_stripe_card_expires.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_stripe_card.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_stripe_details.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals_extras_item_price.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals_extras_item.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals_extras_item_type.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals_subtotal.py",
    "src/fern/types/post_ecomm_order_changed_payload_payload_totals_total.py",
    "src/fern/types/post_ecomm_order_changed_payload.py",
    "src/fern/types/post_form_submission_payload_payload.py",
    "src/fern/types/post_form_submission_payload_payload_schema_item_field_type.py",
    "src/fern/types/post_form_submission_payload_payload_schema_item.py",
    "src/fern/types/post_form_submission_payload.py",
    "src/fern/types/post_page_created_payload_payload.py",
    "src/fern/types/post_page_created_payload.py",
    "src/fern/types/post_page_deleted_payload_payload.py",
    "src/fern/types/post_page_deleted_payload.py",
    "src/fern/types/post_page_metadata_updated_payload_payload.py",
    "src/fern/types/post_page_metadata_updated_payload.py",
    "src/fern/types/post_site_publish_payload_payload_publish_scope.py",
    "src/fern/types/post_site_publish_payload_payload.py",
    "src/fern/types/post_site_publish_payload.py",
];

/// Feature-coverage target specs: hand-authored OpenAPI documents that each pin
/// one shape (see docs/matching.md) — auth schemes beyond bearer, inline
/// request/response hoisting, cookie params, form bodies, discriminated unions,
/// schema constraints, integer enums, and document-level
/// servers/webhooks/callbacks.
///
/// Their Fern `expected/` trees were produced by running Fern's container
/// generator with the scaffold defaults (`--package-name fern`,
/// `--project-name default_package_name`; see scripts/generate-fern-fixture.sh),
/// so the corpora drive crozier with the same naming. Every `unmatched` list is
/// empty: each target reproduces its whole golden byte-for-byte.
const FEATURE_TARGETS: &[Corpus] = &[
    // Every SDK-shaping extension declared in both spellings at once: the Fern one
    // Fern reads to produce the golden, and the canonical `x-crozier-*` one crozier
    // prefers over it. Matching the golden is what proves crozier read the
    // canonical spelling — the same dual-vocabulary check `audience-filter` makes
    // for `x-crozier-audiences`, here over the group and method names, the
    // pagination contract, the streaming `stream-condition` split and the enum
    // member names.
    Corpus {
        api: "crozier-sdk-extensions",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    // `x-fern-property-name` (and its canonical `x-crozier-property-name`)
    // renaming a request-body property clear of the same-named path parameter it
    // would collide with, and a response field, while both keep their wire keys.
    Corpus {
        api: "crozier-property-name",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "auth-schemes",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "inline-request-response",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "cookie-parameters",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "form-bodies",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "discriminated-unions",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "schema-constraints",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "integer-enums",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
    },
    Corpus {
        api: "servers-webhooks",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
    },
    // Real-world-spec robustness targets (issue #40). These minimal specs used to
    // make crozier emit invalid Python or hard-error; each now matches Fern across
    // the whole generated SDK — types, the tag-grouped raw/high-level clients, the
    // root client, and the package aggregators — with no auth (no bearer token).
    //
    // `digit-leading-property` also pins the root-client shape: its untagged,
    // groupless `getThing` operation is emitted directly on the root client.
    Corpus {
        api: "digit-leading-property",
        package_name: "fern",
        project_name: "default_package_name",
        audiences: &[],
        audience_strict: false,
        client_class_name: None,
        extra_fields: None,
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
    },
    // sse-streaming (issue #43, gap #3): a `text/event-stream` (SSE) response used to
    // collapse to a `-> None` method that discarded the stream. crozier now emits
    // Fern's context-managed streaming shape: the raw client is a
    // `@contextlib.(async)contextmanager` over `httpx_client.stream(...)` that decodes
    // events through the `core/http_sse` runtime (`EventSource.iter_sse`/`aiter_sse`)
    // into `typing.(Async)Iterator[typing.Any]` chunks (Fern's OpenAPI
    // importer does not resolve the `x-fern-streaming` `chunk-schema-ref`, so the chunk
    // stays `Any`), and the high-level client yields each chunk with a worked
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
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
        unmatched: &[],
    },
];

/// Path to a fixture directory under `tests/fixtures/`.
fn fixture_dir(api: &str) -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures")
        .join(api)
}

/// The repository's departure ledger, loaded once per test process against
/// every golden this suite compares; a ledger that breaks its contract fails
/// whichever comparison loads it first, naming each broken row.
fn departure_ledger() -> &'static Ledger {
    static LEDGER: std::sync::OnceLock<Ledger> = std::sync::OnceLock::new();
    LEDGER.get_or_init(|| {
        load_departure_ledger(Path::new(env!("CARGO_MANIFEST_DIR"))).unwrap_or_else(|failures| {
            panic!(
                "{} breaks its contract (docs/departures/README.md):\n{}",
                departures_ledger::LEDGER,
                failures.join("\n")
            )
        })
    })
}

/// Require the committed inventory to record `golden`, the tree a comparison
/// is about to read, so the ledger is validated against every golden read.
fn assert_inventoried(golden: &str) {
    assert!(
        departure_ledger().compares(golden),
        "{golden} is not in {}; regenerate it (see compared_goldens_inventory_is_current)",
        departures_ledger::INVENTORY
    );
}

/// `root`'s ledger, validated against `root`'s committed inventory of compared
/// goldens and the catalog — the one load every comparison goes through.
fn load_departure_ledger(root: &Path) -> Result<Ledger, Vec<String>> {
    Ledger::load(root)
}

/// The inventory of compared goldens, derived from the comparisons' own
/// registrations under `root`: each registered corpus's `expected/` and each
/// overlay golden of one, with that corpus's file-level carve-outs; each flat
/// golden; each probe, authored-probe, hand-written and measured
/// parameter-lowering tree; and each Fern
/// reference tree a departure's evidence holds, which `crozier compare` reads in
/// `departures_ledger_gate`. An overlay
/// golden holds the files it carries but its manifest; a file it takes from
/// `expected/` unchanged is accounted for under `expected/`. The committed
/// [`departures_ledger::INVENTORY`] is held to this by
/// `compared_goldens_inventory_is_current`.
fn compared_goldens(root: &Path) -> departures_ledger::Inventory {
    let mut inventory = departures_ledger::Inventory::default();
    let mut add = |golden: String, compared: departures_ledger::ComparedGolden| {
        inventory.goldens.insert(golden, compared);
    };
    for corpus in registered_diff_corpora() {
        let golden = format!("tests/fixtures/{}/expected", corpus.api);
        if root.join(&golden).is_dir() {
            add(
                golden,
                departures_ledger::ComparedGolden {
                    excluded: Vec::new(),
                    carve_outs: recorded_carve_outs(corpus),
                },
            );
        }
    }
    for (golden, corpus, excluded) in overlay_goldens::compared() {
        add(
            golden,
            departures_ledger::ComparedGolden {
                excluded,
                carve_outs: recorded_carve_outs(corpus),
            },
        );
    }
    for golden in FLAT_GOLDENS {
        add(
            format!("tests/fixtures/{}/{FLAT_GOLDEN_DIR}", golden.fixture),
            departures_ledger::ComparedGolden::default(),
        );
    }
    for (dir, tree) in [
        (AUTHORED_PROBES_DIR, "fern-expected"),
        (HANDWRITTEN_DIR, "fern-expected"),
        (PARAMETER_LOWERING_DIR, "fern-expected"),
        ("docs/fern-measurements/bodies-responses", "fern-expected"),
        (
            crozier::departures::EVIDENCE_DIR.trim_end_matches('/'),
            departures_ledger_gate::REFERENCE_TREE,
        ),
    ] {
        let Ok(entries) = std::fs::read_dir(root.join(dir)) else {
            continue;
        };
        for entry in entries.filter_map(Result::ok) {
            if entry.path().join(tree).is_dir() {
                add(
                    format!("{dir}/{}/{tree}", entry.file_name().to_string_lossy()),
                    departures_ledger::ComparedGolden::default(),
                );
            }
        }
    }
    let manifest = std::fs::read_to_string(root.join(PROBE_EXPECTED_DIR).join("MANIFEST.tsv"))
        .unwrap_or_default();
    for proof in parse_probe_manifest(&manifest).0 {
        match proof.form.as_str() {
            "absent-tree" => add(proof.artifact, departures_ledger::ComparedGolden::default()),
            "differential" => {
                add(proof.artifact, departures_ledger::ComparedGolden::default());
                add(
                    format!("{PROBE_EXPECTED_DIR}/{}", proof.control),
                    departures_ledger::ComparedGolden::default(),
                );
            }
            _ => {}
        }
    }
    inventory
}

/// Corpus `c`'s file-level carve-outs, each as its slug in
/// [`departures_ledger::CARVE_OUT_KINDS`] and the files it covers.
fn corpus_carve_outs(c: &Corpus) -> Vec<(&'static str, Vec<&'static str>)> {
    vec![
        ("unmatched", c.unmatched.to_vec()),
        ("crozier-only", crozier_only_files(c).to_vec()),
    ]
}

/// Nonempty corpus carve-outs, as recorded in the inventory.
fn recorded_carve_outs(c: &Corpus) -> std::collections::BTreeMap<String, Vec<String>> {
    corpus_carve_outs(c)
        .into_iter()
        .filter(|(_, files)| !files.is_empty())
        .map(|(slug, files)| {
            (
                slug.to_string(),
                files.into_iter().map(str::to_string).collect(),
            )
        })
        .collect()
}

/// `path`'s repository-relative, `/`-separated spelling — how a ledger row
/// names a golden. A tree outside the repository keeps its absolute spelling,
/// which no row names.
fn golden_path(path: &Path) -> String {
    path.strip_prefix(env!("CARGO_MANIFEST_DIR"))
        .map(|rel| {
            rel.components()
                .map(|part| part.as_os_str().to_string_lossy())
                .collect::<Vec<_>>()
                .join("/")
        })
        .unwrap_or_else(|_| path.display().to_string())
}

/// The rows `ledger` holds for corpus `c`'s golden `golden`, refused when one
/// names a file `c` already carves out at file level.
fn corpus_golden_ledger(
    ledger: &Ledger,
    golden: &str,
    c: &Corpus,
) -> Result<GoldenLedger, Vec<String>> {
    let carve_outs = corpus_carve_outs(c);
    let carve_outs: Vec<(&str, &[&str])> = carve_outs
        .iter()
        .map(|(slug, files)| (*slug, files.as_slice()))
        .collect();
    ledger.golden(golden, &carve_outs)
}

const KNOWN_FERN_FAILURE_FILE: &str = "known-fern-failure.json";

#[derive(Debug)]
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
    let label = path.display().to_string();
    let known = validate_known_fern_failure(c.api, &label, &bytes)?;
    if fixture_dir(c.api)
        .join("expected/.crozier-fern-golden.json")
        .exists()
    {
        return Err(format!(
            "{label} is stale because a provenance-current golden exists"
        ));
    }
    Ok(Some(known))
}

/// The registration's own content check, split out from the filesystem so the
/// exception mechanism can be driven with tampered and foreign registrations.
/// Every field is pinned to the one measured upstream failure, so a registration
/// cannot be copied onto a second corpus or loosened to excuse a divergence.
fn validate_known_fern_failure(
    api: &str,
    label: &str,
    bytes: &[u8],
) -> Result<KnownFernFailure, String> {
    let payload: serde_json::Value =
        serde_json::from_slice(bytes).map_err(|error| format!("invalid {label}: {error}"))?;
    let object = payload
        .as_object()
        .ok_or_else(|| format!("{label} must contain a JSON object"))?;
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
            "{label} does not have the exact known-failure contract keys"
        ));
    }
    let exact_values = [
        ("schema_version", serde_json::json!(1)),
        ("generator", serde_json::json!("fernapi/fern-python-sdk")),
        ("generator_version", serde_json::json!("5.20.0")),
        ("corpus_spec_name", serde_json::json!(api)),
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
            return Err(format!("{label} has stale {key}: expected {expected}"));
        }
    }
    let fingerprint = object["fingerprint"]
        .as_object()
        .ok_or_else(|| format!("{label} has no fingerprint object"))?;
    if fingerprint.get("failed_command")
        != Some(&serde_json::json!(
            "ruff check --fix --no-cache --ignore E741 /fern/output"
        ))
        || fingerprint.get("ruff_summary")
            != Some(&serde_json::json!(
                "Found 11 errors (5 fixed, 6 remaining)."
            ))
    {
        return Err(format!("{label} has stale Ruff failure markers"));
    }
    let diagnostics = fingerprint
        .get("diagnostics")
        .and_then(serde_json::Value::as_array)
        .ok_or_else(|| format!("{label} has no diagnostic list"))?;
    if diagnostics.len() != 6
        || diagnostics.iter().any(|diagnostic| {
            diagnostic.get("message")
                != Some(&serde_json::json!("SyntaxError: Expected an identifier"))
        })
    {
        return Err(format!(
            "{label} must fingerprint exactly six identifier syntax errors"
        ));
    }
    Ok(KnownFernFailure {
        generator: object["generator"].as_str().unwrap().to_owned(),
        generator_version: object["generator_version"].as_str().unwrap().to_owned(),
    })
}

fn known_fern_failure_marker(c: &Corpus, known: &KnownFernFailure) -> String {
    format!(
        "KNOWN UPSTREAM FERN FAILURE: {} at {}:{}; Crozier generation succeeded.",
        c.api, known.generator, known.generator_version
    )
}

/// Decide whether a corpus has a Fern tree to byte-compare. A validated exact
/// upstream failure is the only registration allowed to omit `expected/`;
/// every other missing tree is an error so aggregate comparison cannot silently
/// lose coverage.
fn corpus_has_comparable_golden(c: &Corpus, expected: &Path) -> Result<bool, String> {
    if expected.is_symlink() {
        return Err("refusing to compare a symlinked expected/ golden tree".to_string());
    }
    let known_failure = known_fern_failure(c)?;
    if expected.is_dir() {
        if known_failure.is_some() {
            return Err(
                "fixture has both known-fern-failure.json and an expected/ golden tree; \
                 remove the failure registration after Fern succeeds"
                    .to_string(),
            );
        }
        return Ok(true);
    }
    if known_failure.is_some() {
        return Ok(false);
    }
    Err("fixture has no expected/ golden tree".to_string())
}

/// The committed OpenAPI source used by a registered corpus.
fn corpus_spec(api: &str) -> Option<PathBuf> {
    let vendored = fixture_dir(api).join("openapi.yml");
    if vendored.exists() {
        return Some(vendored);
    }
    let committed = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures/corpus-sources")
        .join(api);
    ["openapi.json", "openapi.yaml", "openapi.yml"]
        .into_iter()
        .map(|name| committed.join(name))
        .find(|path| path.exists())
        .or_else(|| {
            let interpreter = if cfg!(windows) { "python" } else { "python3" };
            let output = std::process::Command::new(interpreter)
                .arg(
                    Path::new(env!("CARGO_MANIFEST_DIR")).join("scripts/corpus_remote_ref_pins.py"),
                )
                .arg("tree-root")
                .arg(api)
                .output()
                .ok()?;
            if !output.status.success() {
                return None;
            }
            let relative = String::from_utf8(output.stdout).ok()?;
            let path = committed.join(relative.trim());
            path.is_file().then_some(path)
        })
}

/// Fresh `crozier` command bound to the built binary.
fn crozier() -> Command {
    Command::cargo_bin("crozier").expect("crozier binary is built for tests")
}

/// Require every Fern file except explicit residual gaps to match byte-for-byte.
fn assert_corpus_matches(c: &Corpus) {
    let fixtures = fixture_dir(c.api);
    let expected_root = fixtures.join("expected");
    assert!(
        corpus_has_comparable_golden(c, &expected_root)
            .unwrap_or_else(|error| panic!("{}: {error}", c.api)),
        "{} has no Fern golden to compare",
        c.api
    );
    let golden = golden_path(&expected_root);
    assert_inventoried(&golden);
    let out = generate_corpus(c);
    let ledger = corpus_golden_ledger(departure_ledger(), &golden, c)
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    assert_generated_tree_matches(c, &ledger, &expected_root, out.path());
}

/// Require crozier's generated tree `out` for `c` to reproduce the Fern tree
/// `expected_root`, under the corpus's declared residuals — the comparison
/// [`assert_corpus_matches`] makes against `expected/`, shared with the overlay
/// gate, which makes it against a corpus's materialized overlay golden. The
/// departures the comparison applies are held to `ledger`, the golden's rows.
fn assert_generated_tree_matches(
    c: &Corpus,
    ledger: &GoldenLedger,
    expected_root: &Path,
    out: &Path,
) {
    let context = Context::from_trees(expected_root, out);
    let mut observed = Vec::new();
    for rel in walk_files(expected_root) {
        if c.unmatched.contains(&rel.as_str()) {
            continue;
        }
        let generated = std::fs::read_to_string(out.join(&rel))
            .unwrap_or_else(|e| panic!("crozier did not write {rel}: {e}"));
        let expected = std::fs::read_to_string(expected_root.join(&rel))
            .unwrap_or_else(|e| panic!("missing fixture {rel}: {e}"));
        let compared = compare_with_golden(&context, &rel, &generated, &expected);
        observed.extend(observed_in(&rel, &compared));
        if let Some(diff) = compared.diff() {
            // Show the exact gate-relevant diff inline instead of a bare "does not
            // match" — what the engine decided on, every catalog departure already
            // applied, so a regression is diagnosable straight from the test output
            // (no second generate-and-diff pass). `just fixtures-diff` prints the
            // same thing on demand for any divergent file.
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
    let failures = ledger.check(&observed, &|_| true);
    assert!(failures.is_empty(), "{}", failures.join("\n"));

    // The comparison is bidirectional: a newly emitted Crozier file cannot hide
    // merely because the golden lacks it.
    for rel in walk_files(out) {
        assert!(
            expected_root.join(&rel).is_file() || crozier_only_files(c).contains(&rel.as_str()),
            "Crozier emitted {rel}, but the Fern fixture has no corresponding file"
        );
    }

    // The declared crozier-only set is held to the same staleness contract as
    // `unmatched`: a listed file that reached the golden must enter byte
    // comparison, and one crozier no longer emits must leave the list.
    let emitted: std::collections::BTreeSet<String> = walk_files(out).into_iter().collect();
    for rel in crozier_only_files(c) {
        assert!(
            !expected_root.join(rel).is_file(),
            "{rel} is now in the Fern golden — remove it from the crozier-only list"
        );
        assert!(
            emitted.contains(*rel),
            "{rel} is no longer emitted — remove it from the crozier-only list"
        );
    }

    for rel in c.unmatched {
        let expected = std::fs::read_to_string(expected_root.join(rel))
            .unwrap_or_else(|e| panic!("unmatched path is not in the Fern fixture: {rel}: {e}"));
        if let Ok(generated) = std::fs::read_to_string(out.join(rel)) {
            assert!(
                !generated_matches_fixture(&context, rel, &generated, &expected),
                "{rel} now matches Fern — remove it from `unmatched`"
            );
        }
    }
}

/// Every committed Fern probe measurement, driven from the one declaration of
/// them: `docs/openapi-surface/probe-expected/MANIFEST.tsv` (Contract A in
/// `docs/openapi-surface-coverage.md`). These are probe expectations, not corpus
/// goldens: a probe never enters `CORPUS.md` and never counts as parity
/// evidence. The manifest names each proof's form, and this reads every row the
/// way its form requires — crozier against a committed tree, a refusal record
/// against the pin and against crozier's own outcome, a differential pair
/// against itself — and holds the artifacts on disk to the manifest in both
/// directions.
// llmlint: ignore[names_match_behavior] The name is the one this node's acceptance criteria and its `cargo nextest -E 'test(witness_supply_probes_match_fern_measurements)'` check select it by; renaming it would silently empty that filter.
#[test]
fn witness_supply_probes_match_fern_measurements() {
    let failures = probe_manifest_failures(Path::new(env!("CARGO_MANIFEST_DIR")));
    assert!(
        failures.is_empty(),
        "the committed probe measurements disagree with MANIFEST.tsv:\n{}",
        failures.join("\n")
    );
}

#[test]
fn refused_probe_inputs_report_the_unsupported_shape() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let probes = root.join(PROBE_DOCUMENTS_DIR);
    let path_item = tempfile::tempdir().expect("path-item probe tempdir");
    let path_item_probe = path_item.path().join("header-at-path-item.yml");
    std::fs::write(
        &path_item_probe,
        "openapi: 3.0.3\ninfo:\n  title: header-at-path-item\n  version: 1.0.0\npaths:\n  /probe:\n    parameters:\n      - name: probeParam\n        in: header\n        schema:\n          type: array\n          items:\n            type: string\n    get:\n      operationId: probe\n      responses:\n        '200':\n          description: OK\n",
    )
    .expect("write path-item probe");

    for (probe, diagnostic) in [
        (
            probes.join("header-array.yml"),
            "example-type-mismatch: GET /probe header probeParam",
        ),
        (
            probes.join("header-object.yml"),
            "GET /probe: header parameter `probeParam` has an unsupported object schema",
        ),
        (
            path_item_probe,
            "example-type-mismatch: GET /probe header probeParam",
        ),
        (
            probes.join("nonascii-operationId.yml"),
            "GET /probe: operationId `データを取得` has no ASCII identifier characters",
        ),
    ] {
        let out = tempfile::tempdir().expect("probe output tempdir");
        let target = out.path().join("sdk");
        let result = probe_command(&probe, &target)
            .output()
            .expect("run crozier over refused probe");
        assert!(!result.status.success(), "{} was accepted", probe.display());
        assert!(
            String::from_utf8_lossy(&result.stderr).contains(diagnostic),
            "{} did not report {diagnostic:?}: {}",
            probe.display(),
            String::from_utf8_lossy(&result.stderr)
        );
        assert!(
            !target.exists() || walk_files(&target).is_empty(),
            "{} wrote an SDK despite refusing the input",
            probe.display()
        );
    }
}

/// The member Fern names for an enum value that starts with a zero-led digit
/// run: the run is spelled and the rest collapses, so `01_00_AM` is `ONE00AM`.
/// `FERN` is the module Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0
/// generated from this probe, comment-stripped (the control of
/// `docs/fern-limitations.md`'s *Arms only a refused document reaches*).
#[test]
fn zero_led_enum_value_names_its_member_as_fern_does() {
    const FERN: &str = r#"

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SlotStart(enum.StrEnum):
    ONE00AM = "01_00_AM"
    NOON = "noon"

    def visit(self, one00am: typing.Callable[[], T_Result], noon: typing.Callable[[], T_Result]) -> T_Result:
        if self is SlotStart.ONE00AM:
            return one00am()
        if self is SlotStart.NOON:
            return noon()
"#;
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(PROBE_DOCUMENTS_DIR)
        .join("enum-leading-zero-member-refused-control.yml");
    let out = tempfile::tempdir().expect("probe output tempdir");
    probe_command(&probe, &out.path().join("sdk"))
        .assert()
        .success();
    let rel = "src/fern/types/slot_start.py";
    let generated = std::fs::read_to_string(out.path().join("sdk").join(rel)).expect("enum module");
    let compared = compare_with_golden(&Context::default(), rel, &generated, FERN);
    assert_eq!(compared.diff(), None);
    assert!(compared.departures.is_empty(), "{compared:?}");
}

const PROBE_EXPECTED_DIR: &str = "docs/openapi-surface/probe-expected";
const PROBE_DOCUMENTS_DIR: &str = "docs/openapi-surface/probes";
const PROBE_MANIFEST_HEADER: &str = "key\tform\tverdict\tartifact\tcontrol\tdigest";
const REFUSAL_FIELDS: [&str; 5] = [
    "fern_cli_version",
    "fern_python_sdk_version",
    "generate_exit",
    "diagnostic",
    "output_tree",
];

/// One row of `MANIFEST.tsv`.
struct ProbeProof {
    key: String,
    form: String,
    artifact: String,
    control: String,
    digest: String,
}

/// Read `MANIFEST.tsv` under `root` and return every way the committed probe
/// measurements fail to agree with it, each naming the key it is about. `root`
/// is the repository root for the real gate, and a scratch tree laid out the
/// same way for the fixture tests below, so both go through this one path.
fn probe_manifest_failures(root: &Path) -> Vec<String> {
    let expected_base = root.join(PROBE_EXPECTED_DIR);
    let manifest_path = expected_base.join("MANIFEST.tsv");
    let text = match std::fs::read_to_string(&manifest_path) {
        Ok(text) => text,
        Err(error) => return vec![format!("MANIFEST.tsv: cannot be read: {error}")],
    };
    let (proofs, mut failures) = parse_probe_manifest(&text);

    // Both directions: every row's artifact exists, and nothing under
    // `probe-expected/` exists that no row names.
    let mut named: std::collections::BTreeSet<String> =
        std::collections::BTreeSet::from(["MANIFEST.tsv".to_string()]);
    for proof in &proofs {
        if let Some(name) = proof
            .artifact
            .strip_prefix(&format!("{PROBE_EXPECTED_DIR}/"))
        {
            named.insert(name.to_string());
        }
        if proof.form == "differential" {
            named.insert(proof.control.clone());
        }
    }
    match std::fs::read_dir(&expected_base) {
        Ok(entries) => {
            let mut present: Vec<String> = entries
                .filter_map(Result::ok)
                .map(|entry| entry.file_name().to_string_lossy().into_owned())
                .collect();
            present.sort();
            for name in present {
                if !named.contains(&name) {
                    failures.push(format!(
                        "{name}: is under {PROBE_EXPECTED_DIR}/ but no MANIFEST.tsv row names it \
                         — declare it with a row, or remove it"
                    ));
                }
            }
        }
        Err(error) => failures.push(format!("{PROBE_EXPECTED_DIR}: cannot be listed: {error}")),
    }

    for proof in &proofs {
        failures.extend(probe_proof_failures(root, proof));
    }
    failures
}

/// The manifest's own shape: the header, six columns, sorted keys, and each
/// row's form, verdict, artifact path, control and digest spelled as Contract A
/// requires. Rows that parse are returned for the artifact checks even when a
/// sibling row failed, so one bad row cannot hide another.
fn parse_probe_manifest(text: &str) -> (Vec<ProbeProof>, Vec<String>) {
    let mut failures = Vec::new();
    let mut lines = text.lines();
    if lines.next() != Some(PROBE_MANIFEST_HEADER) {
        failures.push(format!(
            "MANIFEST.tsv: the header line must be exactly {PROBE_MANIFEST_HEADER:?}"
        ));
    }
    let mut proofs: Vec<ProbeProof> = Vec::new();
    for (index, line) in lines.enumerate() {
        let fields: Vec<&str> = line.split('\t').collect();
        let [key, form, verdict, artifact, control, digest] = fields[..] else {
            failures.push(format!(
                "MANIFEST.tsv line {}: {} column(s); every row has the six {PROBE_MANIFEST_HEADER:?}",
                index + 2,
                fields.len()
            ));
            continue;
        };
        if let Some(previous) = proofs
            .last()
            .filter(|previous| previous.key.as_str() >= key)
        {
            failures.push(format!(
                "{key}: MANIFEST.tsv rows must be sorted by key with no key twice; it follows {}",
                previous.key
            ));
        }
        let expected_verdicts: &[&str] = match form {
            "absent-tree" => &["discards", "measured"],
            "refusal" => &["refuses", "crashes"],
            "differential" => &["ignores", "coincidence"],
            _ => {
                failures.push(format!(
                    "{key}: form `{form}` is not one of `absent-tree`, `refusal`, `differential`"
                ));
                &[]
            }
        };
        if verdict == "implements" {
            failures.push(format!(
                "{key}: verdict `implements` — a shape Fern emits output derived from is not \
                 settleable by a probe; only a registered real-world specification settles it"
            ));
        } else if ![
            "discards",
            "ignores",
            "refuses",
            "crashes",
            "coincidence",
            "measured",
        ]
        .contains(&verdict)
        {
            failures.push(format!(
                "{key}: verdict `{verdict}` is not one Contract A admits \
                 (`discards`, `ignores`, `refuses`, `crashes`, `coincidence`, or `measured`)"
            ));
        } else if !expected_verdicts.is_empty() && !expected_verdicts.contains(&verdict) {
            failures.push(format!(
                "{key}: a `{form}` proof establishes {expected_verdicts:?}, not `{verdict}`"
            ));
        }
        let expected_artifact = if form == "refusal" {
            format!("{PROBE_EXPECTED_DIR}/{key}.fern-refusal.txt")
        } else {
            format!("{PROBE_EXPECTED_DIR}/{key}")
        };
        if artifact != expected_artifact {
            failures.push(format!(
                "{key}: artifact `{artifact}` must be `{expected_artifact}` for a `{form}` proof"
            ));
        }
        if form == "differential" {
            if control == "—" || control == key || control.is_empty() {
                failures.push(format!(
                    "{key}: a `differential` proof names its control probe's key in `control`"
                ));
            }
        } else if control != "—" {
            failures.push(format!("{key}: `control` is `—` for a `{form}` proof"));
        }
        if digest.len() != 64
            || !digest
                .bytes()
                .all(|byte| byte.is_ascii_digit() || (b'a'..=b'f').contains(&byte))
        {
            failures.push(format!(
                "{key}: digest `{digest}` is not a lower-case hex SHA-256"
            ));
        }
        proofs.push(ProbeProof {
            key: key.to_string(),
            form: form.to_string(),
            artifact: artifact.to_string(),
            control: control.to_string(),
            digest: digest.to_string(),
        });
    }
    (proofs, failures)
}

/// Every way one row's committed artifact fails its form, its digest, or
/// crozier's own run over the named probe.
fn probe_proof_failures(root: &Path, proof: &ProbeProof) -> Vec<String> {
    let key = proof.key.as_str();
    let artifact = root.join(&proof.artifact);
    let probe = root.join(PROBE_DOCUMENTS_DIR).join(format!("{key}.yml"));
    let mut failures = Vec::new();
    if !artifact.exists() {
        return vec![format!(
            "{key}: its artifact {} is missing — a declaration cannot outlive its artifact",
            proof.artifact
        )];
    }
    match probe_artifact_digest(&artifact) {
        Ok(actual) if actual == proof.digest => {}
        Ok(actual) => failures.push(format!(
            "{key}: {} hashes to {actual}, but MANIFEST.tsv declares {} — a committed Fern \
             artifact changed; restore it, never re-declare it to match",
            proof.artifact, proof.digest
        )),
        Err(error) => failures.push(format!("{key}: {error}")),
    }
    if !probe.is_file() {
        failures.push(format!(
            "{key}: its probe document {PROBE_DOCUMENTS_DIR}/{key}.yml is missing"
        ));
        return failures;
    }
    match proof.form.as_str() {
        "refusal" => failures.extend(refusal_proof_failures(root, proof, &artifact, &probe)),
        "absent-tree" => failures.extend(probe_tree_failures(key, &probe, &artifact)),
        "differential" => {
            let control_key = proof.control.as_str();
            let control = root
                .join(PROBE_DOCUMENTS_DIR)
                .join(format!("{control_key}.yml"));
            let control_tree = root.join(PROBE_EXPECTED_DIR).join(control_key);
            failures.extend(probe_tree_failures(key, &probe, &artifact));
            if !control.is_file() || !control_tree.is_dir() {
                failures.push(format!(
                    "{key}: its control `{control_key}` needs both \
                     {PROBE_DOCUMENTS_DIR}/{control_key}.yml and {PROBE_EXPECTED_DIR}/{control_key}/"
                ));
                return failures;
            }
            failures.extend(probe_tree_failures(key, &control, &control_tree));
            failures.extend(differential_tree_failures(key, &artifact, &control_tree));
            failures.extend(differential_isolation_failures(root, key, &probe, &control));
        }
        _ => {}
    }
    failures
}

/// A `refusal` row: the five-field record, the pin, no tree beside it, and
/// crozier's own run over the probe agreeing that nothing is generated.
fn refusal_proof_failures(
    root: &Path,
    proof: &ProbeProof,
    record: &Path,
    probe: &Path,
) -> Vec<String> {
    let key = proof.key.as_str();
    let mut failures = Vec::new();
    if root.join(PROBE_EXPECTED_DIR).join(key).exists() {
        failures.push(format!(
            "{key}: Fern emitted no SDK for a refused probe, so {PROBE_EXPECTED_DIR}/{key}/ \
             must not exist"
        ));
    }
    let text = match std::fs::read_to_string(record) {
        Ok(text) => text,
        Err(error) => return vec![format!("{key}: refusal record cannot be read: {error}")],
    };
    let fields: Vec<(&str, &str)> = text
        .lines()
        .map(|line| line.split_once(": ").unwrap_or((line, "")))
        .collect();
    let names: Vec<&str> = fields.iter().map(|(name, _)| *name).collect();
    if names != REFUSAL_FIELDS {
        failures.push(format!(
            "{key}: the refusal record carries fields {names:?}; Contract A requires exactly \
             {REFUSAL_FIELDS:?}, in that order and spelling"
        ));
    }
    let value = |name: &str| {
        fields
            .iter()
            .find(|(field, _)| *field == name)
            .map(|(_, value)| value.trim())
    };
    let (cli_pin, sdk_pin) = probe_fern_pins();
    for (name, pin) in [
        ("fern_cli_version", cli_pin.as_str()),
        ("fern_python_sdk_version", sdk_pin.as_str()),
    ] {
        if let Some(found) = value(name).filter(|found| *found != pin) {
            failures.push(format!(
                "{key}: {name} is `{found}`, but the corpus pins `{pin}`"
            ));
        }
    }
    if let Some(exit) =
        value("generate_exit").filter(|exit| !exit.parse::<i64>().is_ok_and(|code| code != 0))
    {
        failures.push(format!(
            "{key}: generate_exit is `{exit}`; a refusal records Fern's non-zero exit"
        ));
    }
    if value("diagnostic") == Some("") {
        failures.push(format!(
            "{key}: diagnostic is empty; a refusal quotes the phrase Fern printed"
        ));
    }
    if let Some(tree) = value("output_tree").filter(|tree| *tree != "none") {
        failures.push(format!(
            "{key}: output_tree is `{tree}`; a refusal records that Fern produced `none`"
        ));
    }

    // crozier is measured, not trusted: over a probe Fern refused it must
    // refuse too and write nothing.
    let out = tempfile::tempdir().expect("probe output tempdir");
    let target = out.path().join("sdk");
    match probe_command(probe, &target).output() {
        Ok(result) if result.status.success() => failures.push(format!(
            "{key}: crozier generated successfully over a probe the record says Fern refused"
        )),
        Ok(_) => {}
        Err(error) => failures.push(format!("{key}: could not run crozier: {error}")),
    }
    if target.exists() && !walk_files(&target).is_empty() {
        failures.push(format!(
            "{key}: crozier emitted an output tree for a probe the record says Fern emitted none for"
        ));
    }
    failures
}

/// The Fern CLI and `fernapi/fern-python-sdk` versions the corpus is pinned to,
/// read from the one place crozier itself carries them — the `cliVersion` and
/// `generatorVersion` of the `.fern/metadata.json` it emits — so a refusal record
/// is held to the pin the goldens are, not to a second copy of it.
fn probe_fern_pins() -> (String, String) {
    let metadata: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(
            Path::new(env!("CARGO_MANIFEST_DIR")).join("assets/scaffolding/metadata.json"),
        )
        .expect("crozier's packaged Fern metadata"),
    )
    .expect("crozier's packaged Fern metadata is JSON");
    let pin = |field: &str| {
        metadata[field]
            .as_str()
            .unwrap_or_else(|| panic!("assets/scaffolding/metadata.json has no {field}"))
            .to_string()
    };
    (pin("cliVersion"), pin("generatorVersion"))
}

/// crozier over one probe document, byte-compared against its committed tree
/// under the corpus gate's own normalization.
fn probe_tree_failures(key: &str, probe: &Path, expected_root: &Path) -> Vec<String> {
    filtered_tree_failures(key, &golden_path(expected_root), probe, expected_root, &[])
}

/// [`probe_tree_failures`] with crozier filtered to `audiences`, each passed as
/// `--audience` — the list a hand-written fixture's `evidence.toml` gave Fern's
/// generator group. Empty, it is the unfiltered generation. `golden` is how the
/// ledger names the tree: a case's repository-relative path, whichever copy of
/// it `expected_root` is.
fn filtered_tree_failures(
    key: &str,
    golden: &str,
    probe: &Path,
    expected_root: &Path,
    audiences: &[String],
) -> Vec<String> {
    let out = tempfile::tempdir().expect("probe output tempdir");
    let mut command = probe_command(probe, out.path());
    for audience in audiences {
        command.arg("--audience").arg(audience);
    }
    let result = match command.output() {
        Ok(result) => result,
        Err(error) => return vec![format!("{key}: could not run crozier: {error}")],
    };
    if !result.status.success() {
        return vec![format!(
            "{key}: crozier failed over {}: {}",
            probe.display(),
            String::from_utf8_lossy(&result.stderr)
        )];
    }
    let ledger = match departure_ledger().golden(golden, &[]) {
        Ok(ledger) => ledger,
        Err(failures) => return failures,
    };
    golden_tree_failures(
        key,
        &probe.display().to_string(),
        &ledger,
        expected_root,
        out.path(),
    )
}

/// Every way crozier's tree `out` differs from the committed Fern tree
/// `expected_root` under the comparison engine: a different file set, a file
/// that still differs once the catalog's departures are applied, or a
/// departure `ledger`, the golden's rows, does not record (or records but the
/// engine no longer applies). The comparison behind every probe, authored-probe
/// and hand-written gate; `source` names what crozier generated `out` from.
fn golden_tree_failures(
    key: &str,
    source: &str,
    ledger: &GoldenLedger,
    expected_root: &Path,
    out: &Path,
) -> Vec<String> {
    let mut failures = Vec::new();
    let expected_files = walk_files(expected_root);
    let generated_files = walk_files(out);
    if generated_files != expected_files {
        failures.push(format!(
            "{key}: crozier's file set over {source} differs from {}",
            expected_root.display()
        ));
        return failures;
    }
    let context = Context::from_trees(expected_root, out);
    let mut observed = Vec::new();
    for rel in expected_files {
        let generated = std::fs::read_to_string(out.join(&rel)).unwrap_or_default();
        let expected = std::fs::read_to_string(expected_root.join(&rel)).unwrap_or_default();
        let compared = match parity::compare_file(&context, &rel, &generated, &expected) {
            Ok(compared) => compared,
            Err(error) => {
                failures.push(format!("{key}: {rel}: {error}"));
                continue;
            }
        };
        observed.extend(observed_in(&rel, &compared));
        if let Some(diff) = compared.diff() {
            failures.push(format!(
                "{key}: generated {rel} differs from the committed Fern measurement \
                 (fix the generator, never the measurement)\n{diff}"
            ));
        }
    }
    failures.extend(
        ledger
            .check(&observed, &|_| true)
            .into_iter()
            .map(|failure| format!("{key}: {failure}")),
    );
    failures
}

/// A `differential` pair's two committed trees are the same bytes under the
/// gate's normalization; if they are not, the feature is generation and no
/// probe settles it.
fn differential_tree_failures(key: &str, tree: &Path, control_tree: &Path) -> Vec<String> {
    let files = walk_files(tree);
    if files != walk_files(control_tree) {
        return vec![format!(
            "{key}: the probe's and control's committed trees hold different files, so the \
             feature is generation — remove the row and route it to a real specification"
        )];
    }
    let mut failures = Vec::new();
    let context = Context::from_trees(control_tree, tree);
    for rel in files {
        let left = std::fs::read_to_string(tree.join(&rel)).unwrap_or_default();
        let right = std::fs::read_to_string(control_tree.join(&rel)).unwrap_or_default();
        if !generated_matches_fixture(&context, &rel, &left, &right) {
            failures.push(format!(
                "{key}: the probe's and control's committed {rel} differ, so the feature is \
                 generation — remove the row and route it to a real specification"
            ));
        }
    }
    failures
}

/// The three checks that make a pair isolate its feature, read off the parsed
/// documents by the census's own selector engine.
fn differential_isolation_failures(
    root: &Path,
    key: &str,
    probe: &Path,
    control: &Path,
) -> Vec<String> {
    let Some(python) = python_interpreter() else {
        return vec![format!(
            "{key}: no python3/python on PATH to run the census selector over the pair"
        )];
    };
    let script =
        Path::new(env!("CARGO_MANIFEST_DIR")).join("scripts/probe-differential-isolation.py");
    match std::process::Command::new(python)
        .arg(script)
        .arg(root)
        .arg(key)
        .arg(probe)
        .arg(control)
        .output()
    {
        Ok(result) if result.status.success() => Vec::new(),
        Ok(result) => {
            let said = format!(
                "{}{}",
                String::from_utf8_lossy(&result.stdout),
                String::from_utf8_lossy(&result.stderr)
            );
            let lines: Vec<String> = said.lines().map(str::to_string).collect();
            if lines.is_empty() {
                vec![format!(
                    "{key}: the isolation check failed and said nothing"
                )]
            } else {
                lines
            }
        }
        Err(error) => vec![format!("{key}: could not run the isolation check: {error}")],
    }
}

/// The CLI invocation every probe is generated with.
fn probe_command(probe: &Path, output: &Path) -> Command {
    let mut command = crozier();
    command
        .args(["generate", "python", "--spec"])
        .arg(probe)
        .arg("--output")
        .arg(output)
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ]);
    command
}

/// Contract A's digest: SHA-256 of a refusal record's bytes, or of a tree's
/// canonical stream — every file sorted by `/`-separated relative path, each
/// contributing its path, a NUL, its decimal byte length, a NUL, and its bytes.
fn probe_artifact_digest(artifact: &Path) -> Result<String, String> {
    let bytes = if artifact.is_dir() {
        let mut files = parity::walk_files(artifact)?;
        files.sort();
        let mut stream = Vec::new();
        for rel in files {
            let content = std::fs::read(artifact.join(&rel))
                .map_err(|error| format!("cannot read {rel}: {error}"))?;
            stream.extend_from_slice(rel.as_bytes());
            stream.push(0);
            stream.extend_from_slice(content.len().to_string().as_bytes());
            stream.push(0);
            stream.extend_from_slice(&content);
        }
        stream
    } else {
        std::fs::read(artifact)
            .map_err(|error| format!("cannot read {}: {error}", artifact.display()))?
    };
    Ok(sha256_hex(&bytes))
}

/// FIPS 180-4 SHA-256, so the digest check needs no hashing dev-dependency for
/// one use (as `crozier::parity` hand-rolls its tree walk and unified diff).
fn sha256_hex(message: &[u8]) -> String {
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];
    let mut state: [u32; 8] = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab,
        0x5be0cd19,
    ];
    let mut padded = message.to_vec();
    padded.push(0x80);
    while padded.len() % 64 != 56 {
        padded.push(0);
    }
    padded.extend_from_slice(&((message.len() as u64) * 8).to_be_bytes());
    for block in padded.chunks(64) {
        let mut w = [0u32; 64];
        for (index, word) in block.chunks(4).enumerate() {
            w[index] = u32::from_be_bytes([word[0], word[1], word[2], word[3]]);
        }
        for i in 16..64 {
            let s0 = w[i - 15].rotate_right(7) ^ w[i - 15].rotate_right(18) ^ (w[i - 15] >> 3);
            let s1 = w[i - 2].rotate_right(17) ^ w[i - 2].rotate_right(19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16]
                .wrapping_add(s0)
                .wrapping_add(w[i - 7])
                .wrapping_add(s1);
        }
        let [mut a, mut b, mut c, mut d, mut e, mut f, mut g, mut h] = state;
        for i in 0..64 {
            let s1 = e.rotate_right(6) ^ e.rotate_right(11) ^ e.rotate_right(25);
            let choice = (e & f) ^ (!e & g);
            let t1 = h
                .wrapping_add(s1)
                .wrapping_add(choice)
                .wrapping_add(K[i])
                .wrapping_add(w[i]);
            let s0 = a.rotate_right(2) ^ a.rotate_right(13) ^ a.rotate_right(22);
            let majority = (a & b) ^ (a & c) ^ (b & c);
            let t2 = s0.wrapping_add(majority);
            h = g;
            g = f;
            f = e;
            e = d.wrapping_add(t1);
            d = c;
            c = b;
            b = a;
            a = t1.wrapping_add(t2);
        }
        for (slot, value) in state.iter_mut().zip([a, b, c, d, e, f, g, h]) {
            *slot = slot.wrapping_add(value);
        }
    }
    state.iter().map(|word| format!("{word:08x}")).collect()
}

#[test]
fn sha256_matches_the_fips_180_4_test_vectors() {
    assert_eq!(
        sha256_hex(b""),
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    );
    assert_eq!(
        sha256_hex(b"abc"),
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    );
    assert_eq!(
        sha256_hex(b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"),
        "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1"
    );
}

const AUTHORED_PROBES_DIR: &str = "docs/openapi-surface/authored-probes";

/// The measured parameter-lowering cases `parameter_lowering_measurements_match_fern`
/// compares, one directory per case.
const PARAMETER_LOWERING_DIR: &str = "docs/fern-measurements/parameter-lowering";

/// The naming tickets' (#350, #354, #357) authored probes are the case
/// directories `376-<ticket>-<shape>`; `authored_probe_measurements_match_fern`
/// byte-compares each against Fern's tree by default. A document Fern refused
/// is no authored probe: it is an `evidence/376-*` probe of the registry class
/// crozier refuses it under.
const NAMING_TICKETS: [&str; 3] = ["376-350-", "376-354-", "376-357-"];

/// Every naming input Fern refused: the registry class crozier refuses it under,
/// the probe's stem in that class's `evidence/` (beside its `.pinned-fern.log`),
/// and the element its refusal line names. The two collisions fail Fern's check
/// on the merged type's example; the manager ruled them `type-name-collision`.
const NAMING_REFUSALS: [(&str, &str, &str); 3] = [
    (
        "type-name-not-letter-led",
        "376-350-declared-type-name-blank-digit-led",
        "123456",
    ),
    (
        "type-name-collision",
        "376-350-declared-type-name-shared-differing",
        "\"Widget\"",
    ),
    (
        "type-name-collision",
        "376-350-declared-type-name-taken",
        "\"Widget\"",
    ),
];

/// How the ledger names the authored-probe tree `tree`: by its case directory,
/// whichever copy of the case `tree` sits in.
fn authored_golden(tree: &Path) -> String {
    let case = tree
        .parent()
        .and_then(Path::file_name)
        .map(|case| case.to_string_lossy().into_owned())
        .unwrap_or_default();
    format!("{AUTHORED_PROBES_DIR}/{case}/fern-expected")
}

/// Where pinned Fern generated, crozier byte-matches its tree over `probe` in
/// both modes.
fn authored_probe_tree_failures(case: &str, probe: &Path, tree: &Path) -> Vec<String> {
    let mut failures = filtered_tree_failures(case, &authored_golden(tree), probe, tree, &[]);
    let strict = tempfile::tempdir().expect("strict output tempdir");
    match probe_command(probe, strict.path())
        .arg("--fern-strict")
        .output()
    {
        Ok(result) if result.status.success() => {
            if walk_files(strict.path()) != walk_files(tree) {
                failures.push(format!(
                    "{case}: crozier's --fern-strict file set over {} differs from {}",
                    probe.display(),
                    tree.display()
                ));
            }
        }
        Ok(result) => failures.push(format!(
            "{case}: crozier --fern-strict refused a probe Fern generates from: {}",
            String::from_utf8_lossy(&result.stderr)
        )),
        Err(error) => failures.push(format!("{case}: could not run crozier: {error}")),
    }
    failures
}

/// Where pinned Fern refused, crozier refuses in both modes under `class`,
/// naming `element` and writing nothing.
fn authored_probe_refusal_failures(
    case: &str,
    probe: &Path,
    class: &str,
    element: &str,
) -> Vec<String> {
    let mut failures = Vec::new();
    for strict in [false, true] {
        let out = tempfile::tempdir().expect("probe output tempdir");
        let target = out.path().join("sdk");
        let mut command = probe_command(probe, &target);
        if strict {
            command.arg("--fern-strict");
        }
        let result = match command.output() {
            Ok(result) => result,
            Err(error) => return vec![format!("{case}: could not run crozier: {error}")],
        };
        let stderr = String::from_utf8_lossy(&result.stderr);
        if result.status.code() != Some(1)
            || !stderr.contains(class)
            || !stderr.contains(element)
            || stderr.contains("fern-strict") != strict
            || target.exists()
        {
            failures.push(format!(
                "{case}: crozier (strict {strict}) must exit 1 naming {class} and {element}, \
                 writing nothing, where Fern refused; it exited {:?}: {stderr}",
                result.status.code()
            ));
        }
    }
    failures
}

/// Every naming probe Fern generated from also generates under `--fern-strict`,
/// and every one it refused is refused in both modes under its registry class.
#[test]
fn naming_authored_probes_match_pinned_fern() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let mut cases: Vec<String> = std::fs::read_dir(root.join(AUTHORED_PROBES_DIR))
        .expect("the authored probes")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .filter(|case| NAMING_TICKETS.iter().any(|ticket| case.starts_with(ticket)))
        .collect();
    cases.sort();
    for ticket in NAMING_TICKETS {
        assert!(
            cases.iter().any(|case| case.starts_with(ticket)),
            "no authored probe for {ticket}"
        );
    }
    let mut failures = Vec::new();
    for case in &cases {
        let dir = root.join(AUTHORED_PROBES_DIR).join(case);
        failures.extend(authored_probe_tree_failures(
            case,
            &dir.join("openapi.yml"),
            &dir.join("fern-expected"),
        ));
    }
    for (class, stem, element) in NAMING_REFUSALS {
        let evidence = root.join(FERN_REFUSALS_DIR).join(class).join("evidence");
        let log = std::fs::read_to_string(evidence.join(format!("{stem}.pinned-fern.log")))
            .unwrap_or_default();
        if !log.starts_with("Fern CLI 5.67.1, python-sdk 5.20.0\n")
            || !log.contains("\ngenerate exit: 1\n")
        {
            failures.push(format!(
                "{stem}: its pinned-fern.log is no refusal measured at the pin"
            ));
        }
        failures.extend(authored_probe_refusal_failures(
            stem,
            &evidence.join(format!("{stem}.yml")),
            class,
            element,
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// A webhook payload's reference to a component with a declared type name
/// follows the rename, as an operation's does, rather than dangling to the
/// unknown type.
#[test]
fn webhook_payload_references_follow_a_declared_type_name() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        r"openapi: 3.1.0
info: { title: probe, version: 1.0.0 }
paths: {}
webhooks:
  widgetMade:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                widget: { $ref: '#/components/schemas/Widget' }
      responses:
        '200': { description: OK }
components:
  schemas:
    Widget:
      x-crozier-type-name: Gadget
      type: object
      properties:
        id: { type: string }
",
    )
    .unwrap();
    let out = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .success();
    let types = out.join("src/probe/types");
    assert!(std::fs::read_to_string(types.join("gadget.py"))
        .unwrap()
        .contains("class Gadget("));
    assert!(!types.join("widget.py").exists());
    let payload = std::fs::read_to_string(types.join("post_widget_made_payload.py")).unwrap();
    assert!(payload.contains("from .gadget import Gadget"), "{payload}");
    assert!(
        payload.contains("widget: typing.Optional[Gadget] = None"),
        "{payload}"
    );
}

/// `x-crozier-type-name` is the canonical spelling of `x-fern-type-name`
/// (AGENTS.md, the dual-header policy): alone it names a component exactly as
/// the Fern spelling with the same value does, and beside a different Fern
/// spelling it wins. Both variants are held to the tree Fern generated from the
/// `x-fern-type-name` probe.
#[test]
fn canonical_type_name_hint_names_components_like_fern_spelling() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let probe = std::fs::read_to_string(
        root.join(AUTHORED_PROBES_DIR)
            .join("376-350-declared-type-name/openapi.yml"),
    )
    .expect("the declared type-name probe");
    assert_eq!(probe.matches("x-fern-type-name: ").count(), 2, "{probe}");
    let dir = tempfile::tempdir().unwrap();
    let canonical_only = probe.replace("x-fern-type-name: ", "x-crozier-type-name: ");
    let both = probe
        .replace(
            "x-fern-type-name: Gadget",
            "x-fern-type-name: Decoy\n      x-crozier-type-name: Gadget",
        )
        .replace(
            "x-fern-type-name: Thing",
            "x-fern-type-name: '9'\n      x-crozier-type-name: Thing",
        );
    let mut failures = Vec::new();
    for (name, document) in [("canonical-only", canonical_only), ("both", both)] {
        let spec = dir.path().join(format!("{name}.yml"));
        std::fs::write(&spec, document).unwrap();
        failures.extend(authored_probe_tree_failures(
            name,
            &spec,
            &root
                .join(AUTHORED_PROBES_DIR)
                .join("376-350-declared-type-name/fern-expected"),
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// Every authored-probe measurement, found by listing
/// `docs/openapi-surface/authored-probes/` and nothing else: crozier's output
/// over each case's `openapi.yml` byte-matches the `fern-expected/` tree pinned
/// Fern generated from it, under the gate's normalization. A case is neither a
/// hand-written fixture nor real-specification evidence (the directory's
/// README), so this is not a `*matches_fern_output*` test.
#[test]
fn authored_probe_measurements_match_fern() {
    let failures =
        authored_probe_failures(&Path::new(env!("CARGO_MANIFEST_DIR")).join(AUTHORED_PROBES_DIR));
    assert!(
        failures.is_empty(),
        "the authored-probe measurements break their contract \
         (docs/openapi-surface/authored-probes/README.md):\n{}",
        failures.join("\n")
    );
}

/// Every way the cases under `root` fail: a case missing its document, its
/// Fern log or its tree, a log that does not record Fern's exit statuses at the
/// pin, or crozier's output differing from the tree.
fn authored_probe_failures(root: &Path) -> Vec<String> {
    let Ok(entries) = std::fs::read_dir(root) else {
        return vec![format!("{}: no authored-probes directory", root.display())];
    };
    let mut cases: Vec<PathBuf> = entries
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.is_dir())
        .collect();
    cases.sort();
    if cases.is_empty() {
        return vec![format!("{}: no case directories", root.display())];
    }
    let (cli_pin, sdk_pin) = probe_fern_pins();
    let mut failures = Vec::new();
    for case in cases {
        let name = case
            .file_name()
            .map(|name| name.to_string_lossy().into_owned())
            .unwrap_or_default();
        let spec = case.join("openapi.yml");
        let expected = case.join("fern-expected");
        let log = std::fs::read_to_string(case.join("fern.log")).unwrap_or_default();
        let pin = format!("Fern CLI {cli_pin}, python-sdk {sdk_pin}");
        if !log.starts_with(&pin)
            || !log.contains("\ncheck exit: ")
            || !log.contains("\ngenerate exit: ")
        {
            failures.push(format!(
                "{name}: fern.log must open with `{pin}` and record `check exit:` and \
                 `generate exit:` — re-measure the case at the pin"
            ));
        }
        if !spec.is_file() || !expected.is_dir() {
            failures.push(format!(
                "{name}: a case holds openapi.yml and the fern-expected/ tree Fern generated from it"
            ));
            continue;
        }
        failures.extend(filtered_tree_failures(
            &name,
            &authored_golden(&expected),
            &spec,
            &expected,
            &[],
        ));
    }
    failures
}

#[test]
fn authored_probe_gate_names_a_broken_case() {
    let root = tempfile::tempdir().unwrap();
    let source = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(AUTHORED_PROBES_DIR)
        .join("358-absent-property");
    let case = root.path().join("358-absent-property");
    copy_dir(&source, &case);
    assert!(authored_probe_failures(root.path()).is_empty());
    // A Fern tree that no longer matches crozier is named, with its file.
    let holder = case.join("fern-expected/src/fern/types/holder.py");
    let text = std::fs::read_to_string(&holder).unwrap();
    std::fs::write(
        &holder,
        text.replace("typing.Optional[typing.Any]", "typing.Optional[str]"),
    )
    .unwrap();
    let failures = authored_probe_failures(root.path());
    assert!(
        failures.len() == 1
            && failures[0]
                .contains("358-absent-property: generated src/fern/types/holder.py differs"),
        "{failures:?}"
    );
    // So is a log that does not record the measurement.
    std::fs::write(&holder, text).unwrap();
    std::fs::write(case.join("fern.log"), "generate exit: 0\n").unwrap();
    let failures = authored_probe_failures(root.path());
    assert!(
        failures.len() == 1 && failures[0].contains("fern.log must open with"),
        "{failures:?}"
    );
    assert!(authored_probe_failures(&root.path().join("absent"))[0]
        .contains("no authored-probes directory"));
}

/// Copy every file under `source` to the same relative path under `target`.
fn copy_dir(source: &Path, target: &Path) {
    for rel in walk_files(source) {
        let to = target.join(&rel);
        std::fs::create_dir_all(to.parent().unwrap()).unwrap();
        std::fs::copy(source.join(&rel), to).unwrap();
    }
}

/// The relative imports of every generated module under `root` that name a
/// module the SDK does not contain, as `<file>: <import line>`.
fn unwritten_module_imports(root: &Path) -> Vec<String> {
    let mut missing = Vec::new();
    for rel in walk_files(root) {
        if !rel.ends_with(".py") {
            continue;
        }
        let file = root.join(&rel);
        let text = std::fs::read_to_string(&file).unwrap_or_default();
        for line in text.lines() {
            let Some(module) = line
                .trim_start()
                .strip_prefix("from .")
                .and_then(|rest| rest.split(" import ").next())
            else {
                continue;
            };
            let mut base = file.parent().unwrap().to_path_buf();
            let mut dotted = module;
            while let Some(rest) = dotted.strip_prefix('.') {
                base.pop();
                dotted = rest;
            }
            let target = dotted
                .split('.')
                .filter(|part| !part.is_empty())
                .fold(base, |path, part| path.join(part));
            if !target.with_extension("py").is_file() && !target.join("__init__.py").is_file() {
                missing.push(format!("{rel}: {}", line.trim()));
            }
        }
    }
    missing
}

/// crozier#358: a pointer past a declared component's head that names nothing
/// (`#/components/schemas/Named/properties/absent`) is the unknown type at every
/// use site, so no generated module imports one crozier never wrote. Each case
/// is the authored probe pinned Fern measured for that site.
#[test]
fn unresolved_nested_pointers_import_only_written_modules() {
    let probes = Path::new(env!("CARGO_MANIFEST_DIR")).join(AUTHORED_PROBES_DIR);
    for case in [
        "358-absent-property",
        "358-absent-required-property",
        "358-absent-array-item",
        "358-absent-map-value",
        "358-absent-allof-member",
        "358-absent-request-body",
        "358-absent-response-body",
        "358-absent-items-segment",
        "358-undeclared-head-properties-required",
    ] {
        let out = tempfile::tempdir().unwrap();
        let result = probe_command(&probes.join(case).join("openapi.yml"), out.path())
            .output()
            .unwrap();
        assert!(
            result.status.success(),
            "{case}: {}",
            String::from_utf8_lossy(&result.stderr)
        );
        let missing = unwritten_module_imports(out.path());
        assert!(
            missing.is_empty(),
            "{case} imports modules crozier did not write: {missing:?}"
        );
        assert!(
            !walk_files(out.path())
                .iter()
                .any(|rel| rel.contains("named_absent") || rel.contains("named_item")),
            "{case}"
        );
    }
}

#[test]
fn unwritten_module_imports_names_a_missing_module() {
    let root = tempfile::tempdir().unwrap();
    let types = root.path().join("src/fern/types");
    std::fs::create_dir_all(&types).unwrap();
    std::fs::write(types.join("__init__.py"), "").unwrap();
    std::fs::write(types.join("named.py"), "").unwrap();
    std::fs::write(
        types.join("holder.py"),
        "from .named import Named\nfrom .named_absent import NamedAbsent\nfrom ..core.http import X\n",
    )
    .unwrap();
    assert_eq!(
        unwritten_module_imports(root.path()),
        [
            "src/fern/types/holder.py: from .named_absent import NamedAbsent",
            "src/fern/types/holder.py: from ..core.http import X",
        ]
    );
}

const HANDWRITTEN_DIR: &str = "docs/openapi-surface/handwritten";

/// Every hand-written generation fixture, found by listing
/// `docs/openapi-surface/handwritten/` and nothing else, held to the contract
/// that directory's `AGENTS.md` states. A hand-written fixture is a lower level
/// of proof than a real specification: it is admitted only after a failed
/// real-specification search it cites, and never counts as a corpus golden, so
/// this is not a `*matches_fern_output*` test and the golden-only tier never
/// runs it. `scripts/handwritten-fixtures.py gate` checks what the committed
/// documents say; this adds Contract A's digest, the pin, and crozier's
/// byte-match against each fixture's `fern-expected/`.
// llmlint: ignore[names_match_behavior] The name is the one the contract in docs/openapi-surface/handwritten/AGENTS.md and this node's acceptance criteria give the gate, and the `cargo nextest -E 'test(handwritten_fixtures_match_fern_goldens)'` check selects it by; renaming it would silently empty that filter.
#[test]
fn handwritten_fixtures_match_fern_goldens() {
    let failures = handwritten_fixture_failures(Path::new(env!("CARGO_MANIFEST_DIR")));
    assert!(
        failures.is_empty(),
        "the hand-written fixtures break their contract \
         (docs/openapi-surface/handwritten/AGENTS.md):\n{}",
        failures.join("\n")
    );
}

/// A byte-formatted text response streams in either enum mode. The complete
/// certified tree is compared in both directions, and an unexplained change
/// to the method remains a parity failure.
#[test]
fn byte_text_response_matches_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let golden = "docs/openapi-surface/handwritten/byte-text-response/fern-expected";
    let fixture = root.join("docs/openapi-surface/handwritten/byte-text-response");
    for (mode, golden) in [
        ("python-enums", golden),
        (
            "literals",
            "docs/fern-measurements/bodies-responses/byte-text-response-literals/fern-expected",
        ),
    ] {
        let expected = root.join(golden);
        if mode == "literals" {
            let evidence = std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                .expect("literals evidence");
            let declared = evidence
                .split_once("Canonical tree SHA-256: `")
                .expect("a declared canonical digest")
                .1
                .split('`')
                .next()
                .expect("the digest");
            assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
        }
        let ledger = departure_ledger()
            .golden(golden, &[])
            .expect("golden ledger");
        let out = tempfile::tempdir().expect("output");
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(fixture.join("openapi.yml"))
            .arg("--output")
            .arg(out.path())
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
                "--enum-type",
                mode,
            ])
            .assert()
            .success();
        let failures =
            golden_tree_failures(mode, "byte text response", &ledger, &expected, out.path());
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        let client = out.path().join("src/fern/client.py");
        let text = std::fs::read_to_string(&client).expect("generated client");
        assert!(text.contains("def export_lanterns("), "{text}");
        std::fs::write(
            &client,
            text.replace("def export_lanterns(", "def unexplained_export("),
        )
        .unwrap();
        let failures = golden_tree_failures(
            mode,
            "induced unexplained mismatch",
            &ledger,
            &expected,
            out.path(),
        );
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains("src/fern/client.py")),
            "{}",
            failures.join("\n")
        );
    }
}

/// Resolving a byte-text component selects streaming; changing that component
/// to an ordinary string restores the regular response method through the CLI.
#[test]
fn referenced_byte_text_response_streams_and_plain_text_recovers() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("openapi.yml");
    let document = r#"openapi: 3.0.3
info: {title: Lantern Export, version: '1'}
paths:
  /exports:
    get:
      operationId: export_lanterns
      responses:
        '200':
          description: Lantern export
          content:
            text/plain:
              schema: {$ref: '#/components/schemas/Export'}
components:
  schemas:
    Export: {type: string, format: byte}
"#;
    for (format, streaming) in [("byte", true), ("uuid", false)] {
        std::fs::write(
            &spec,
            document.replace("format: byte", &format!("format: {format}")),
        )
        .unwrap();
        let out = dir.path().join(format);
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&out)
            .args(["--package-name", "fern"])
            .assert()
            .success();
        let raw = std::fs::read_to_string(out.join("src/fern/raw_client.py")).unwrap();
        assert_eq!(
            raw.contains("self._client_wrapper.httpx_client.stream("),
            streaming,
            "{raw}"
        );
        assert_eq!(raw.contains("_response.iter_bytes("), streaming, "{raw}");
        assert_eq!(
            raw.contains("self._client_wrapper.httpx_client.request("),
            !streaming,
            "{raw}"
        );
    }
}

/// The certified controls hold the JSON alternative's precedence and the
/// non-string guard through the real binary, with complete file-set equality.
#[test]
fn byte_text_response_dispatch_controls_match_certified_output() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let fixture = root.join("docs/openapi-surface/handwritten/byte-text-response-controls");
    let failures = filtered_tree_failures(
        "byte text response controls",
        "docs/openapi-surface/handwritten/byte-text-response-controls/fern-expected",
        &fixture.join("openapi.yml"),
        &fixture.join("fern-expected"),
        &[],
    );
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

#[test]
fn slashless_json_response_matches_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let fixture = root.join("docs/openapi-surface/handwritten/slashless-json-response");
    for (mode, golden) in [
        ("python-enums", "docs/openapi-surface/handwritten/slashless-json-response/fern-expected"),
        ("literals", "docs/fern-measurements/bodies-responses/slashless-json-response-literals/fern-expected"),
    ] {
        let expected = root.join(golden);
        if mode == "literals" {
            let evidence = std::fs::read_to_string(expected.parent().unwrap().join("evidence.md")).unwrap();
            let declared = evidence.split_once("Canonical tree SHA-256: `").unwrap().1.split('`').next().unwrap();
            assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
        }
        let ledger = departure_ledger().golden(golden, &[]).unwrap();
        let out = tempfile::tempdir().unwrap();
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(fixture.join("openapi.yml"))
            .arg("--output").arg(out.path())
            .args(["--package-name", "fern", "--project-name", "default_package_name", "--enum-type", mode])
            .assert().success();
        let failures = golden_tree_failures(mode, "slashless JSON response", &ledger, &expected, out.path());
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    }
}

/// Complete certified pairs cover the object alias and the shadowing field;
/// the required-file example correction is the only new permitted departure.
#[test]
fn multipart_object_encoding_matches_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for shape in ["multipart-alias-object", "multipart-json-module"] {
        let fixture = root.join("docs/openapi-surface/handwritten").join(shape);
        for mode in ["python-enums", "literals"] {
            let golden = if mode == "python-enums" {
                format!("docs/openapi-surface/handwritten/{shape}/fern-expected")
            } else {
                format!("docs/fern-measurements/bodies-responses/{shape}-literals/fern-expected")
            };
            let expected = root.join(&golden);
            if mode == "literals" {
                let evidence =
                    std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                        .unwrap();
                let declared = evidence
                    .split_once("Canonical tree SHA-256: `")
                    .unwrap()
                    .1
                    .split('`')
                    .next()
                    .unwrap();
                assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
            }
            let ledger = departure_ledger().golden(&golden, &[]).unwrap();
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(fixture.join("openapi.yml"))
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let failures = golden_tree_failures(mode, shape, &ledger, &expected, out.path());
            assert!(failures.is_empty(), "{}", failures.join("\n"));
            let client = out.path().join("src/fern/client.py");
            let generated = std::fs::read_to_string(&client).unwrap();
            assert!(generated.contains("bearing=1"));
            std::fs::write(&client, generated.replace("bearing=1", "bearing=91")).unwrap();
            let failures = golden_tree_failures(
                mode,
                "unexplained object example value",
                &ledger,
                &expected,
                out.path(),
            );
            assert!(
                failures
                    .iter()
                    .any(|failure| failure.contains("client.py differs")),
                "{failures:?}"
            );
        }
    }
}

#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_multipart_objects_encode_and_required_file_examples_bind() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let script = root.join("docs/departures/evidence/multipart-object-required-file-example.py");
    let python = runtime_python_env().expect("SDK runtime environment");
    for (shape, argument) in [
        ("multipart-alias-object", "alias"),
        ("multipart-json-module", "json"),
    ] {
        for mode in ["python-enums", "literals"] {
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(
                    root.join("docs/openapi-surface/handwritten")
                        .join(shape)
                        .join("openapi.yml"),
                )
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let run = std::process::Command::new(&python)
                .arg(&script)
                .arg(out.path().join("src"))
                .arg(argument)
                .args(["--examples", "valid", "--wire"])
                .env("PYTHONDONTWRITEBYTECODE", "1")
                .output()
                .unwrap();
            assert!(
                run.status.success(),
                "{shape}/{mode}: {}{}",
                String::from_utf8_lossy(&run.stdout),
                String::from_utf8_lossy(&run.stderr)
            );
        }
    }
}

/// Named request representations match their complete certified tree.
#[test]
fn named_request_media_match_certified_output_and_canonical_extensions() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for shape in ["request-media-methods"] {
        let fixture = root.join("docs/openapi-surface/handwritten").join(shape);
        for mode in ["python-enums", "literals"] {
            let golden = if mode == "python-enums" {
                format!("docs/openapi-surface/handwritten/{shape}/fern-expected")
            } else {
                format!("docs/fern-measurements/bodies-responses/{shape}-literals/fern-expected")
            };
            let expected = root.join(&golden);
            if mode == "literals" {
                let evidence =
                    std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                        .unwrap();
                let declared = evidence
                    .split_once("Canonical tree SHA-256: `")
                    .unwrap()
                    .1
                    .split('`')
                    .next()
                    .unwrap();
                assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
            }
            let ledger = departure_ledger().golden(&golden, &[]).unwrap();
            for spelling in ["fern", "crozier", "conflicting"] {
                let source = std::fs::read_to_string(fixture.join("openapi.yml")).unwrap();
                let source = match spelling {
                    "crozier" => source.replace("x-fern-sdk-method-name", "x-crozier-sdk-method-name"),
                    "conflicting" => source
                        .replace("x-fern-sdk-method-name: append_card_note", "x-fern-sdk-method-name: ignored_json\n            x-crozier-sdk-method-name: append_card_note")
                        .replace("x-fern-sdk-method-name: append_card_scan", "x-fern-sdk-method-name: ignored_scan\n            x-crozier-sdk-method-name: append_card_scan"),
                    _ => source,
                };
                let input = tempfile::tempdir().unwrap();
                let spec_path = input.path().join("openapi.yml");
                std::fs::write(&spec_path, &source).unwrap();
                let out = tempfile::tempdir().unwrap();
                crozier_clean_env()
                    .args(["--no-config", "generate", "python", "--spec"])
                    .arg(&spec_path)
                    .arg("--output")
                    .arg(out.path())
                    .args([
                        "--package-name",
                        "fern",
                        "--project-name",
                        "default_package_name",
                        "--enum-type",
                        mode,
                    ])
                    .assert()
                    .success();
                let failures = golden_tree_failures(mode, shape, &ledger, &expected, out.path());
                assert!(failures.is_empty(), "{}", failures.join("\n"));
                let client = out.path().join("src/fern/raw_client.py");
                let text = std::fs::read_to_string(&client).unwrap();
                assert!(text.contains("def append_card_note("));
                assert!(text.contains("def append_card_scan("));
                std::fs::write(client, text.replace("note: str", "note: int")).unwrap();
                let failures = golden_tree_failures(
                    mode,
                    "unexplained named media annotation",
                    &ledger,
                    &expected,
                    out.path(),
                );
                assert!(
                    failures
                        .iter()
                        .any(|failure| failure.contains("raw_client.py differs")),
                    "{failures:?}"
                );
                let invalid = source
                    .replace(
                        "x-crozier-sdk-method-name: append_card_note",
                        "x-crozier-sdk-method-name: [invalid]",
                    )
                    .replace(
                        "x-fern-sdk-method-name: append_card_note",
                        "x-fern-sdk-method-name: [invalid]",
                    );
                std::fs::write(&spec_path, invalid).unwrap();
                crozier_clean_env()
                    .args(["--no-config", "generate", "python", "--spec"])
                    .arg(&spec_path)
                    .arg("--output")
                    .arg(out.path())
                    .assert()
                    .failure()
                    .stderr(predicate::str::contains("expected a string"));
                std::fs::write(&spec_path, source).unwrap();
                crozier_clean_env()
                    .args(["--no-config", "generate", "python", "--spec"])
                    .arg(&spec_path)
                    .arg("--output")
                    .arg(out.path())
                    .args([
                        "--package-name",
                        "fern",
                        "--project-name",
                        "default_package_name",
                        "--enum-type",
                        mode,
                    ])
                    .assert()
                    .success();
                let failures = golden_tree_failures(
                    mode,
                    "recovered named media",
                    &ledger,
                    &expected,
                    out.path(),
                );
                assert!(failures.is_empty(), "{}", failures.join("\n"));
            }
        }
    }
}

/// Nullable file dispatch, inherited description and 3.1 array headers match together.
#[test]
fn multipart_nullable_and_array_body_shapes_match_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for shape in ["multipart-nullable-array"] {
        let fixture = root.join("docs/openapi-surface/handwritten").join(shape);
        for mode in ["python-enums", "literals"] {
            let golden = if mode == "python-enums" {
                format!("docs/openapi-surface/handwritten/{shape}/fern-expected")
            } else {
                format!("docs/fern-measurements/bodies-responses/{shape}-literals/fern-expected")
            };
            let expected = root.join(&golden);
            if mode == "literals" {
                let evidence =
                    std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                        .unwrap();
                let declared = evidence
                    .split_once("Canonical tree SHA-256: `")
                    .unwrap()
                    .1
                    .split('`')
                    .next()
                    .unwrap();
                assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
            }
            let ledger = departure_ledger().golden(&golden, &[]).unwrap();
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(fixture.join("openapi.yml"))
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let failures = golden_tree_failures(mode, shape, &ledger, &expected, out.path());
            assert!(failures.is_empty(), "{}", failures.join("\n"));
            let client = out.path().join("src/fern/raw_client.py");
            let text = std::fs::read_to_string(&client).unwrap();
            assert!(text.contains("page: typing.Optional[core.File]"));
            std::fs::write(
                client,
                text.replace(
                    "page: typing.Optional[core.File]",
                    "page: typing.Optional[bytes]",
                ),
            )
            .unwrap();
            let failures = golden_tree_failures(
                mode,
                "unexplained nullable file annotation",
                &ledger,
                &expected,
                out.path(),
            );
            assert!(
                failures
                    .iter()
                    .any(|failure| failure.contains("raw_client.py differs")),
                "{failures:?}"
            );
        }
    }
}

#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_nullable_multipart_files_send_their_payload_and_recover() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let python = runtime_python_env().expect("SDK runtime environment");
    for mode in ["python-enums", "literals"] {
        let out = tempfile::tempdir().unwrap();
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(root.join("docs/openapi-surface/handwritten/multipart-nullable-array/openapi.yml"))
            .arg("--output")
            .arg(out.path())
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
                "--enum-type",
                mode,
            ])
            .assert()
            .success();
        Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(root.join("tests/e2e/multipart_nullable_wire.py"))
            .arg(out.path().join("src"))
            .assert()
            .success();
    }
}

/// Complete error declarations, exports and parsing agree in both enum modes.
#[test]
fn error_body_shapes_match_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for shape in ["error-body-shapes"] {
        let fixture = root.join("docs/openapi-surface/handwritten").join(shape);
        for mode in ["python-enums", "literals"] {
            let golden = if mode == "python-enums" {
                format!("docs/openapi-surface/handwritten/{shape}/fern-expected")
            } else {
                format!("docs/fern-measurements/bodies-responses/{shape}-literals/fern-expected")
            };
            let expected = root.join(&golden);
            if mode == "literals" {
                let evidence =
                    std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                        .unwrap();
                let declared = evidence
                    .split_once("Canonical tree SHA-256: `")
                    .unwrap()
                    .1
                    .split('`')
                    .next()
                    .unwrap();
                assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
            }
            let ledger = departure_ledger().golden(&golden, &[]).unwrap();
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(fixture.join("openapi.yml"))
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let failures = golden_tree_failures(mode, shape, &ledger, &expected, out.path());
            assert!(failures.is_empty(), "{}", failures.join("\n"));
            let client = out.path().join("src/fern/types/conflict_error_body.py");
            let text = std::fs::read_to_string(&client).unwrap();
            assert!(text.contains("state: ConflictErrorBodyState"));
            std::fs::write(
                client,
                text.replace("state: ConflictErrorBodyState", "state: str"),
            )
            .unwrap();
            let failures = golden_tree_failures(
                mode,
                "unexplained error annotation",
                &ledger,
                &expected,
                out.path(),
            );
            assert!(
                failures
                    .iter()
                    .any(|failure| failure.contains("conflict_error_body.py differs")),
                "{failures:?}"
            );
        }
    }
}

/// Each full tree covers the request's signature, serialization, retained
/// models and worked examples together, including the reference-header controls.
#[test]
fn json_request_shapes_match_certified_output_in_both_enum_modes() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for shape in ["json-request-shapes", "json-binary-path"] {
        let fixture = root.join("docs/openapi-surface/handwritten").join(shape);
        for mode in ["python-enums", "literals"] {
            let golden = if mode == "python-enums" {
                format!("docs/openapi-surface/handwritten/{shape}/fern-expected")
            } else {
                format!("docs/fern-measurements/bodies-responses/{shape}-literals/fern-expected")
            };
            let expected = root.join(&golden);
            if mode == "literals" {
                let evidence =
                    std::fs::read_to_string(expected.parent().unwrap().join("evidence.md"))
                        .unwrap();
                let declared = evidence
                    .split_once("Canonical tree SHA-256: `")
                    .unwrap()
                    .1
                    .split('`')
                    .next()
                    .unwrap();
                assert_eq!(probe_artifact_digest(&expected).unwrap(), declared);
            }
            let ledger = departure_ledger().golden(&golden, &[]).unwrap();
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(fixture.join("openapi.yml"))
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let failures = golden_tree_failures(mode, shape, &ledger, &expected, out.path());
            assert!(failures.is_empty(), "{}", failures.join("\n"));
            let group = if shape == "json-binary-path" {
                "depository"
            } else {
                "vault"
            };
            let client = out.path().join(format!("src/fern/{group}/client.py"));
            let text = std::fs::read_to_string(&client).unwrap();
            assert!(text.contains("request=b\"string\""));
            std::fs::write(
                client,
                text.replace("request=b\"string\"", "request=b\"unexplained\""),
            )
            .unwrap();
            let failures = golden_tree_failures(
                mode,
                "unexplained binary example value",
                &ledger,
                &expected,
                out.path(),
            );
            assert!(
                failures
                    .iter()
                    .any(|failure| failure.contains("client.py differs")),
                "{failures:?}"
            );
        }
    }
}

#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_binary_json_examples_have_their_actual_argument_type_and_encode() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let script = root.join("docs/departures/evidence/binary-json-body-example.py");
    let python = runtime_python_env().expect("SDK runtime environment");
    for (shape, group, method) in [
        ("json-request-shapes", "vault", "deposit_bundle"),
        ("json-binary-path", "depository", "deposit_parcel"),
    ] {
        for mode in ["python-enums", "literals"] {
            let out = tempfile::tempdir().unwrap();
            crozier_clean_env()
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(
                    root.join("docs/openapi-surface/handwritten")
                        .join(shape)
                        .join("openapi.yml"),
                )
                .arg("--output")
                .arg(out.path())
                .args([
                    "--package-name",
                    "fern",
                    "--project-name",
                    "default_package_name",
                    "--enum-type",
                    mode,
                ])
                .assert()
                .success();
            let run = std::process::Command::new(&python)
                .arg(&script)
                .arg(out.path().join("src"))
                .arg(group)
                .arg(method)
                .args(["--examples", "valid"])
                .env("PYTHONDONTWRITEBYTECODE", "1")
                .output()
                .unwrap();
            assert!(
                run.status.success(),
                "{shape}/{mode}: {}{}",
                String::from_utf8_lossy(&run.stdout),
                String::from_utf8_lossy(&run.stderr)
            );
        }
    }
}

/// Every `date-time` value crozier's worked examples write over the
/// `unread-date-time-examples` hand-written fixture is an instant
/// `datetime.datetime.fromisoformat` reads: a UTC `YYYY-MM-DD[T ]HH:MM:SS+00:00`
/// with each field in range. The document's examples are a zone name and a
/// negative offset, which Fern replaces with its default, beside a `Z` value it
/// reads; no example carries either source string, and the docstring writer
/// changes nothing but the date-time separator.
#[test]
fn worked_date_time_examples_always_parse() {
    let fixture = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("docs/openapi-surface/handwritten/unread-date-time-examples/openapi.yml");
    let out = tempfile::tempdir().expect("tempdir");
    crozier()
        .args(["generate", "python", "--spec"])
        .arg(&fixture)
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
    let valid = |value: &str| {
        let bytes = value.as_bytes();
        let digits = |range: std::ops::Range<usize>| {
            value
                .get(range)
                .filter(|part| part.bytes().all(|byte| byte.is_ascii_digit()))
                .and_then(|part| part.parse::<u32>().ok())
        };
        value.len() == 25
            && value.ends_with("+00:00")
            && bytes[4] == b'-'
            && bytes[7] == b'-'
            && matches!(bytes[10], b'T' | b' ')
            && bytes[13] == b':'
            && bytes[16] == b':'
            && digits(0..4).is_some()
            && digits(5..7).is_some_and(|month| (1..=12).contains(&month))
            && digits(8..10).is_some_and(|day| (1..=31).contains(&day))
            && digits(11..13).is_some_and(|hour| hour < 24)
            && digits(14..16).is_some_and(|minute| minute < 60)
            && digits(17..19).is_some_and(|second| second < 60)
    };
    let mut seen = Vec::new();
    for rel in ["README.md", "reference.md", "src/fern/client.py"] {
        let text = std::fs::read_to_string(out.path().join(rel)).expect(rel);
        assert!(
            !text.contains("CDT") && !text.contains("-05:00"),
            "{rel} carries a source date-time Fern does not read"
        );
        let mut rest = text.as_str();
        while let Some(at) = rest.find("datetime.datetime.fromisoformat(") {
            rest = &rest[at + "datetime.datetime.fromisoformat(".len()..];
            let open = rest.find('"').expect("a quoted argument");
            let close = rest[open + 1..].find('"').expect("a closed argument") + open + 1;
            let value = &rest[open + 1..close];
            assert!(
                valid(value),
                "{rel}: `{value}` is not a date-time fromisoformat reads"
            );
            seen.push(value.to_string());
            rest = &rest[close..];
        }
    }
    for expected in [
        "2024-01-15T09:30:00+00:00",
        "2022-08-11T21:45:00+00:00",
        "2024-01-15 09:30:00+00:00",
        "2022-08-11 21:45:00+00:00",
    ] {
        assert!(
            seen.iter().any(|value| value == expected),
            "no example writes {expected}"
        );
    }
}

/// Every way the hand-written fixtures under `root` fail their contract, each
/// naming the fixture (or row, or ledger) it is about. `root` is the repository
/// for the real gate and a scratch tree laid out the same way for the tests
/// below, so both go through this one path.
fn handwritten_fixture_failures(root: &Path) -> Vec<String> {
    let (evidence, mut failures) = handwritten_documents(root);
    let Ok(entries) = std::fs::read_dir(root.join(HANDWRITTEN_DIR)) else {
        // The document check has already said the directory is missing.
        return failures;
    };
    let mut fixtures: Vec<PathBuf> = entries
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.is_dir())
        .collect();
    fixtures.sort();
    let (cli_pin, sdk_pin) = probe_fern_pins();
    for fixture in fixtures {
        let name = fixture
            .file_name()
            .map(|name| name.to_string_lossy().into_owned())
            .unwrap_or_default();
        let expected = fixture.join("fern-expected");
        let spec = fixture.join("openapi.yml");
        if let Some(declared) = evidence.get(&name) {
            for (field, pin) in [
                ("fern_cli_version", cli_pin.as_str()),
                ("fern_python_sdk_version", sdk_pin.as_str()),
            ] {
                let found = declared[field].as_str().unwrap_or_default();
                if found != pin {
                    failures.push(format!(
                        "{name}: evidence.toml {field} is `{found}`, but the corpus pins `{pin}` \
                         — regenerate fern-expected/ at the pin"
                    ));
                }
            }
            if expected.is_dir() {
                let digest = declared["digest"].as_str().unwrap_or_default();
                match probe_artifact_digest(&expected) {
                    Ok(actual) if actual == digest => {}
                    Ok(actual) => failures.push(format!(
                        "{name}: fern-expected/ hashes to {actual}, but evidence.toml declares \
                         `{digest}` — a committed Fern tree changed; restore it, never re-declare \
                         it to match"
                    )),
                    Err(error) => failures.push(format!("{name}: {error}")),
                }
            }
        }
        if expected.is_dir() && spec.is_file() {
            let audiences: Vec<String> = evidence
                .get(&name)
                .and_then(|declared| declared["audiences"].as_array())
                .map(|audiences| {
                    audiences
                        .iter()
                        .filter_map(|audience| audience.as_str().map(str::to_string))
                        .collect()
                })
                .unwrap_or_default();
            failures.extend(filtered_tree_failures(
                &name,
                &format!("{HANDWRITTEN_DIR}/{name}/fern-expected"),
                &spec,
                &expected,
                &audiences,
            ));
        }
    }
    failures
}

/// The document half of the gate: each fixture's parsed pins and digest, and
/// every failure `scripts/handwritten-fixtures.py gate` reports over `root`.
fn handwritten_documents(
    root: &Path,
) -> (
    std::collections::BTreeMap<String, serde_json::Value>,
    Vec<String>,
) {
    let Some(python) = python_interpreter() else {
        return (
            Default::default(),
            vec!["no python3/python on PATH to read the hand-written fixtures' documents".into()],
        );
    };
    let script = Path::new(env!("CARGO_MANIFEST_DIR")).join("scripts/handwritten-fixtures.py");
    let output = match std::process::Command::new(python)
        .arg(script)
        .arg("--repo-root")
        .arg(root)
        .arg("gate")
        .output()
    {
        Ok(output) => output,
        Err(error) => {
            return (
                Default::default(),
                vec![format!(
                    "could not run the hand-written fixture check: {error}"
                )],
            )
        }
    };
    let parsed: serde_json::Value = match serde_json::from_slice(&output.stdout) {
        Ok(parsed) if output.status.success() => parsed,
        _ => {
            return (
                Default::default(),
                vec![format!(
                    "the hand-written fixture check failed ({}): {}",
                    output.status,
                    String::from_utf8_lossy(&output.stderr)
                )],
            )
        }
    };
    let failures = parsed["failures"]
        .as_array()
        .map(|failures| {
            failures
                .iter()
                .filter_map(|failure| failure.as_str().map(str::to_string))
                .collect()
        })
        .unwrap_or_default();
    let evidence = parsed["fixtures"]
        .as_object()
        .map(|fixtures| {
            fixtures
                .iter()
                .map(|(name, declared)| (name.clone(), declared.clone()))
                .collect()
        })
        .unwrap_or_default();
    (evidence, failures)
}

/// The measured parameter-lowering cases under
/// `docs/fern-measurements/parameter-lowering/`: every case with a committed
/// `fern-expected/` tree is generated with crozier and compared whole, under the
/// same normalization the hand-written gate applies. Its README states the rule
/// each case pins.
#[test]
fn parameter_lowering_measurements_match_fern() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR")).join(PARAMETER_LOWERING_DIR);
    let mut cases: Vec<PathBuf> = std::fs::read_dir(&root)
        .expect("the measurement directory exists")
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.join("fern-expected").is_dir())
        .collect();
    cases.sort();
    assert!(
        cases.len() >= 18,
        "the measured cases are missing: {cases:?}"
    );
    let failures: Vec<String> = cases
        .iter()
        .flat_map(|case| {
            let name = case
                .file_name()
                .map(|name| name.to_string_lossy().into_owned())
                .unwrap_or_default();
            {
                let expected = case.join("fern-expected");
                filtered_tree_failures(
                    &name,
                    &golden_path(&expected),
                    &case.join("openapi.yml"),
                    &expected,
                    &[],
                )
            }
        })
        .collect();
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// `x-crozier-base-path` is `x-fern-base-path` under crozier's own spelling: on
/// its own it generates the tree Fern measured for the `x-fern-base-path`
/// document, and beside an `x-fern-base-path` naming another base path it wins,
/// whichever of the two forms each one takes. The control: that other base
/// path, read alone, lifts nothing.
#[test]
fn crozier_base_path_alias_matches_and_wins() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR")).join(PARAMETER_LOWERING_DIR);
    let lifted = root.join("base-path-lifted-unincluded");
    let literal = root.join("base-path-string");
    let document = std::fs::read_to_string(lifted.join("openapi.yml")).unwrap();
    let object = "x-fern-base-path:\n  path: /{edition}\n  parameters:\n    edition:\n      type: string\n      default: v2\n";
    assert!(
        document.contains(object),
        "the lifted document's extension moved"
    );
    let crozier_object = object.replace("x-fern-base-path:", "x-crozier-base-path:");
    let cases = [
        ("alias-alone", crozier_object.clone(), &lifted),
        (
            "alias-wins-over-a-literal",
            format!("x-fern-base-path: /v2\n{crozier_object}"),
            &lifted,
        ),
        (
            "alias-wins-over-an-object",
            format!("{object}x-crozier-base-path: /v2\n"),
            &literal,
        ),
    ];
    let work = tempfile::tempdir().expect("alias tempdir");
    for (name, extension, golden) in cases {
        let spec = work.path().join(format!("{name}.yml"));
        std::fs::write(&spec, document.replace(object, &extension)).unwrap();
        let expected = golden.join("fern-expected");
        let failures = filtered_tree_failures(name, &golden_path(&expected), &spec, &expected, &[]);
        assert!(failures.is_empty(), "{}", failures.join("\n\n"));
    }
    // The control, outside the ledger-recording comparison: the literal base
    // path alone lifts nothing, so the client takes no `edition`.
    let spec = work.path().join("control.yml");
    std::fs::write(&spec, document.replace(object, "x-fern-base-path: /v2\n")).unwrap();
    let out = work.path().join("control");
    let result = probe_command(&spec, &out).output().expect("crozier runs");
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let client = std::fs::read_to_string(out.join("src/fern/client.py")).unwrap();
    assert!(
        !client.contains("edition"),
        "the literal base path alone lifted a parameter: {client}"
    );
}

/// The gate's name keeps it out of the golden-only tier, which selects every
/// `*matches_fern_output*` test in `scripts/fixtures-coverage.sh` and in
/// `scripts/openapi-surface-census.py`, whose selector `scripts/golden-reach.py`
/// imports: a hand-written fixture never counts as a corpus golden.
#[test]
fn the_handwritten_gate_is_outside_the_golden_only_tier() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    for (script, selector) in [
        (
            "scripts/fixtures-coverage.sh",
            "test(/matches_fern_output/)",
        ),
        (
            "scripts/openapi-surface-census.py",
            "GOLDEN_TEST = re.compile(r\"matches_fern_output\")",
        ),
        ("scripts/golden-reach.py", "_census_module().GOLDEN_TEST"),
    ] {
        let text = std::fs::read_to_string(root.join(script)).expect("tier selector script");
        assert!(
            text.contains(selector),
            "{script} no longer selects the golden-only tier by {selector}; re-read this check"
        );
    }
    let source = std::fs::read_to_string(root.join("tests/e2e.rs")).expect("this suite's source");
    let declared: Vec<&str> = source
        .lines()
        .filter_map(|line| line.strip_prefix("fn "))
        .filter_map(|rest| rest.split('(').next())
        .collect();
    assert!(
        declared.contains(&"handwritten_fixtures_match_fern_goldens"),
        "the hand-written gate is no longer declared under the name the contract gives it"
    );
    for name in declared.iter().filter(|name| name.contains("handwritten")) {
        assert!(
            !name.contains("matches_fern_output"),
            "{name} would join the golden-only tier, which never reads a hand-written fixture"
        );
    }
}

/// The contract states the pin in prose and in its `evidence.toml` example; the
/// gate holds each fixture to `assets/scaffolding/metadata.json`, so this holds
/// the prose to it too. Every version the contract names is one of the two pins.
#[test]
fn the_handwritten_contract_states_the_corpus_pin() {
    let contract = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR")).join(format!("{HANDWRITTEN_DIR}/AGENTS.md")),
    )
    .expect("the hand-written fixture contract");
    let (cli_pin, sdk_pin) = probe_fern_pins();
    for (field, pin) in [
        ("fern_cli_version", &cli_pin),
        ("fern_python_sdk_version", &sdk_pin),
    ] {
        assert!(
            contract.contains(&format!("{field} = \"{pin}\"")),
            "the contract's evidence.toml example does not pin {field} to {pin}"
        );
    }
    let versions: Vec<&str> = contract
        .split(|c: char| !(c.is_ascii_digit() || c == '.'))
        .filter(|token| {
            token.split('.').count() == 3 && token.split('.').all(|part| !part.is_empty())
        })
        .collect();
    assert!(
        !versions.is_empty(),
        "the contract no longer states the pin"
    );
    for version in versions {
        assert!(
            version == cli_pin || version == sdk_pin,
            "the contract names version {version}, which is neither pin ({cli_pin}, {sdk_pin})"
        );
    }
}

/// A scratch repository laid out as the real one is, holding one valid
/// hand-written fixture with a feature-level and an arm-level cover, and the
/// region row, ledgers and search records they cite, for the gate to be driven
/// over through the same [`handwritten_fixture_failures`] the real tree takes.
/// Its `fern-expected/` is crozier's own comment-stripped output standing in for
/// Fern's: this exercises the gate's reading of a fixture, not any Fern verdict.
struct HandwrittenFixture {
    dir: tempfile::TempDir,
}

const HANDWRITTEN_FIXTURE: &str = "sample-fixture";
const HANDWRITTEN_ARM: &str = "src/ir.rs::scalar_body[=^ {12}_ => return None]";
const HANDWRITTEN_SPEC: &str = "openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
paths:
  /probe:
    post:
      operationId: probe
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: string
              format: email
      responses:
        \"200\":
          description: ok
";

impl HandwrittenFixture {
    fn new() -> Self {
        let dir = tempfile::tempdir().expect("fixture repository");
        let fixture = Self { dir };
        let regions = fixture.path("docs/openapi-surface");
        std::fs::create_dir_all(fixture.fixture_dir()).expect("fixture directory");
        std::fs::create_dir_all(fixture.path("tests/fixtures")).expect("corpus directory");
        std::fs::write(
            fixture.path(&format!("{HANDWRITTEN_DIR}/AGENTS.md")),
            "# fixtures\n",
        )
        .expect("fixture AGENTS.md");
        std::fs::write(
            fixture.path("tests/fixtures/CORPUS.md"),
            "| # | name | source |\n|---|---|---|\n| 1 | registered-spec | https://example.com/openapi.yml |\n",
        )
        .expect("fixture CORPUS.md");
        std::fs::write(
            regions.join("sample.md"),
            "| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |\n\
             |---|---|---|---|---|---|---|---|\n\
             | `sample-shape` | both | Schema Object.sample | handwritten | handwritten: sample-fixture; search: exhausted ([record](sample-search.md#witness-search-exhaustive)) |  |  |  |\n\
             | `sample-golden` | both | Schema Object.format | golden | census `schema.format=email` | reach: sample |  |  |\n",
        )
        .expect("fixture region file");
        std::fs::write(
            regions.join("sample-search.md"),
            format!(
                "# Searches\n\n### Witness search (exhaustive)\n\n\
                 The arm searched for: `{HANDWRITTEN_ARM}`.\n\n\
                 | key | outcome |\n|---|---|\n\
                 | `sample-shape` | `exhausted` |\n| `sample-golden` | `exhausted` |\n\n\
                 ### Incomplete search\n\n| key | outcome |\n|---|---|\n\
                 | `sample-shape` | `search-incomplete` |\n"
            ),
        )
        .expect("fixture search record");
        std::fs::write(
            regions.join("sample-renewed.md"),
            "| key | outcome |\n|---|---|\n| `sample-shape` | `none-registrable` |\n",
        )
        .expect("fixture renewed record");
        std::fs::write(
            regions.join("witness-search-keys.tsv"),
            "key\tselector\tregion\tcensus_status\nsample-shape\tschema.format=email\tsample.md\tsupported\n",
        )
        .expect("fixture key set");
        std::fs::write(
            regions.join("golden-reach-sites.tsv"),
            format!("key\tselectors\tsites\tnote\nsample-golden\tschema.format=email\t{HANDWRITTEN_ARM}\t\n"),
        )
        .expect("fixture site table");
        std::fs::write(
            regions.join("golden-reach.tsv"),
            format!(
                "# golden-reach ledger — fixture\n\
                 rank\tkey\tregion\tunreached_sites\tunreached_regions\tregions\twitnesses\toutside\tsites\tnote\n\
                 1\tsample-golden\tsample\t1\t1\t1\tregistered-spec\t-\t{HANDWRITTEN_ARM}=0/1\t-\n"
            ),
        )
        .expect("fixture golden-reach ledger");
        fixture.write_reach(&format!(
            "{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t1\t1\n"
        ));
        fixture.write_gates("");
        std::fs::write(fixture.fixture_dir().join("openapi.yml"), HANDWRITTEN_SPEC)
            .expect("fixture document");
        write_stripped_crozier_tree(
            &fixture.fixture_dir().join("openapi.yml"),
            &fixture.fixture_dir().join("fern-expected"),
        );
        fixture.declare(
            "[[covers]]\nkey = \"sample-shape\"\n\
             search = \"docs/openapi-surface/sample-search.md#witness-search-exhaustive\"\n\
             verdict = \"exhausted\"\n\n\
             [[covers]]\nkey = \"sample-golden\"\n\
             arm = \"src/ir.rs::scalar_body[=^ {12}_ => return None]\"\n\
             search = \"docs/openapi-surface/sample-search.md#witness-search-exhaustive\"\n\
             verdict = \"exhausted\"\n",
        );
        fixture
    }

    fn root(&self) -> &Path {
        self.dir.path()
    }

    fn path(&self, rel: &str) -> PathBuf {
        self.root().join(rel)
    }

    fn fixture_dir(&self) -> PathBuf {
        self.path(&format!("{HANDWRITTEN_DIR}/{HANDWRITTEN_FIXTURE}"))
    }

    fn evidence(&self) -> PathBuf {
        self.fixture_dir().join("evidence.toml")
    }

    fn write_reach(&self, rows: &str) {
        std::fs::write(
            self.path("docs/openapi-surface/handwritten-reach.tsv"),
            format!("fixture\tkey\tsite\tregions_executed\tregions\n{rows}"),
        )
        .expect("fixture reach ledger");
    }

    fn write_gates(&self, rows: &str) {
        std::fs::write(
            self.path("docs/openapi-surface/handwritten-config-gates.tsv"),
            format!("fixture\tkey\tsite\tsetting\tregions_executed\tregions\n{rows}"),
        )
        .expect("fixture configuration-gate ledger");
    }

    /// Write `evidence.toml` at the pin and the tree's current digest, with `covers`.
    fn declare(&self, covers: &str) {
        let (cli_pin, sdk_pin) = probe_fern_pins();
        let digest = probe_artifact_digest(&self.fixture_dir().join("fern-expected"))
            .expect("fixture tree digest");
        std::fs::write(
            self.evidence(),
            format!(
                "fern_cli_version = \"{cli_pin}\"\nfern_python_sdk_version = \"{sdk_pin}\"\n\
                 digest = \"{digest}\"\n\n{covers}"
            ),
        )
        .expect("fixture evidence");
    }

    fn edit_evidence(&self, from: &str, to: &str) {
        let text = std::fs::read_to_string(self.evidence()).expect("fixture evidence");
        assert!(text.contains(from), "fixture evidence has no {from:?}");
        std::fs::write(self.evidence(), text.replacen(from, to, 1)).expect("fixture evidence");
    }

    fn failures(&self) -> Vec<String> {
        handwritten_fixture_failures(self.root())
    }

    /// The failure an induced case must produce, naming `subject` and `message`.
    fn assert_refused(&self, subject: &str, message: &str) {
        let failures = self.failures();
        assert!(
            failures
                .iter()
                .any(|failure| failure.starts_with(&format!("{subject}: "))
                    && failure.contains(message)),
            "expected a failure naming {subject} and saying {message:?}; got:\n{}",
            failures.join("\n")
        );
    }
}

/// crozier's output for `spec`, comment-stripped the way a Fern golden is.
fn write_stripped_crozier_tree(spec: &Path, tree: &Path) {
    write_filtered_crozier_tree(spec, tree, &[]);
}

/// [`write_stripped_crozier_tree`] filtered to `audiences`.
fn write_filtered_crozier_tree(spec: &Path, tree: &Path, audiences: &[&str]) {
    let mut command = probe_command(spec, tree);
    for audience in audiences {
        command.args(["--audience", audience]);
    }
    command.assert().success();
    for rel in walk_files(tree) {
        if rel.ends_with(".py") {
            let path = tree.join(&rel);
            let text = std::fs::read_to_string(&path).expect("generated module");
            std::fs::write(&path, crozier::strip_python_comments(&text)).expect("stripped module");
        }
    }
}

#[test]
fn handwritten_gate_accepts_a_well_formed_fixture() {
    let fixture = HandwrittenFixture::new();
    assert_eq!(Vec::<String>::new(), fixture.failures());
    // A `search-incomplete` cover is admitted with its renewed record.
    fixture.edit_evidence(
        "#witness-search-exhaustive\"\nverdict = \"exhausted\"\n\n",
        "#incomplete-search\"\nverdict = \"search-incomplete\"\n\
         renewed = \"docs/openapi-surface/sample-renewed.md\"\n\n",
    );
    std::fs::write(
        fixture.path("docs/openapi-surface/sample.md"),
        std::fs::read_to_string(fixture.path("docs/openapi-surface/sample.md"))
            .expect("region file")
            .replace(
                "search: exhausted ([record](sample-search.md#witness-search-exhaustive))",
                "search: search-incomplete ([record](sample-search.md#incomplete-search))",
            ),
    )
    .expect("region file");
    assert_eq!(Vec::<String>::new(), fixture.failures());
}

/// A fixture's `audiences` reach crozier as `--audience`: a tree generated for
/// `public` matches only while the fixture declares it, and a fixture without
/// the key is generated whole, as before the key existed.
#[test]
fn handwritten_gate_generates_a_fixture_for_its_declared_audiences() {
    let fixture = HandwrittenFixture::new();
    // Without the key the fixture is the unfiltered generation it always was.
    assert_eq!(Vec::<String>::new(), fixture.failures());
    let spec = fixture.fixture_dir().join("openapi.yml");
    let labelled = HANDWRITTEN_SPEC.replace(
        "      operationId: probe\n",
        "      operationId: probe\n      x-crozier-audiences: [public]\n",
    ) + "  /internal:
    get:
      operationId: internalOnly
      x-crozier-audiences: [internal]
      responses:
        \"200\":
          description: ok
          content:
            application/json:
              schema:
                $ref: \"#/components/schemas/InternalOnly\"
components:
  schemas:
    InternalOnly:
      type: object
      properties:
        id:
          type: string
";
    std::fs::write(&spec, labelled).expect("labelled document");
    let tree = fixture.fixture_dir().join("fern-expected");
    std::fs::remove_dir_all(&tree).expect("remove unfiltered tree");
    write_filtered_crozier_tree(&spec, &tree, &["public"]);
    let covers = std::fs::read_to_string(fixture.evidence()).expect("evidence");
    let covers = &covers[covers.find("[[covers]]").expect("a cover")..];
    fixture.declare(&format!("audiences = [\"public\"]\n\n{covers}"));
    // Its arm-level cover owes the measured pair, with the setting and without.
    fixture.assert_refused(
        "handwritten-config-gates.tsv",
        "with setting `audiences=public` — run `just handwritten-reach`",
    );
    fixture.write_gates(&format!(
        "{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t-\t1\t1\n\
         {HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\taudiences=public\t1\t1\n"
    ));
    assert_eq!(Vec::<String>::new(), fixture.failures());

    fixture.edit_evidence("audiences = [\"public\"]\n", "");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "crozier's file set over");

    for malformed in ["[]", "\"public\"", "[\"\"]"] {
        fixture.declare(&format!("audiences = {malformed}\n\n{covers}"));
        fixture.assert_refused(HANDWRITTEN_FIXTURE, "evidence.toml `audiences` is");
    }

    // A `config-gated` cover rests on a setting its fixture must declare.
    fixture.declare(&covers.replace("verdict = \"exhausted\"", "verdict = \"config-gated\""));
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "a `config-gated` cover is arm-level and its fixture declares the setting",
    );
}

/// The configuration-gate ledger is held to its form, and to the covers it
/// measures: a missing, misheaded, malformed, repeated or orphaned row is refused.
#[test]
fn handwritten_gate_refuses_a_malformed_or_orphaned_configuration_gate_ledger() {
    let fixture = HandwrittenFixture::new();
    let ledger = fixture.path("docs/openapi-surface/handwritten-config-gates.tsv");
    let row = format!("{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t-\t0\t1\n");

    fixture.write_gates(&row);
    fixture.assert_refused(
        "handwritten-config-gates.tsv",
        "names no live arm-level cover of a fixture declaring that setting",
    );
    fixture.write_gates(&format!("{row}{row}"));
    fixture.assert_refused("handwritten-config-gates.tsv", "rows are not sorted");
    fixture.write_gates("sample-fixture\tsample-golden\n");
    fixture.assert_refused(
        "handwritten-config-gates.tsv line 2",
        "not six tab-separated fields",
    );
    std::fs::write(&ledger, "fixture\tkey\n").expect("misheaded ledger");
    fixture.assert_refused(
        "handwritten-config-gates.tsv",
        "the header line must be exactly",
    );
    std::fs::remove_file(&ledger).expect("remove ledger");
    fixture.assert_refused("handwritten-config-gates.tsv", "missing — restore it");
}

#[test]
fn handwritten_gate_refuses_a_fixture_whose_fern_tree_is_missing_or_moved() {
    let fixture = HandwrittenFixture::new();
    std::fs::remove_dir_all(fixture.fixture_dir().join("fern-expected")).expect("remove tree");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "fern-expected is missing");

    let fixture = HandwrittenFixture::new();
    let readme = fixture.fixture_dir().join("fern-expected/README.md");
    let text = std::fs::read_to_string(&readme).expect("tree README");
    std::fs::write(&readme, format!("{text}\ntouched\n")).expect("touched README");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "but evidence.toml declares");

    for field in ["fern_cli_version", "fern_python_sdk_version"] {
        let fixture = HandwrittenFixture::new();
        fixture.edit_evidence(&format!("{field} = \""), &format!("{field} = \"0."));
        fixture.assert_refused(HANDWRITTEN_FIXTURE, &format!("{field} is `0."));
    }
}

#[test]
fn handwritten_gate_refuses_a_tree_crozier_diverges_from() {
    let fixture = HandwrittenFixture::new();
    let readme = fixture.fixture_dir().join("fern-expected/README.md");
    let text = std::fs::read_to_string(&readme).expect("tree README");
    std::fs::write(&readme, format!("{text}\ndrift\n")).expect("drifted README");
    fixture.edit_evidence("digest = \"", "digest = \"stale");
    let digest =
        probe_artifact_digest(&fixture.fixture_dir().join("fern-expected")).expect("digest");
    let evidence = std::fs::read_to_string(fixture.evidence()).expect("evidence");
    let stale = evidence
        .lines()
        .find(|line| line.starts_with("digest = "))
        .expect("digest line")
        .to_string();
    fixture.edit_evidence(&stale, &format!("digest = \"{digest}\""));
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "differs from the committed Fern measurement",
    );
}

#[test]
fn handwritten_gate_refuses_a_cover_its_search_record_does_not_support() {
    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("#witness-search-exhaustive", "#no-such-heading");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "its search anchor does not resolve");

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("verdict = \"exhausted\"", "verdict = \"search-incomplete\"");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "states ['exhausted'] for `sample-shape`",
    );

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence(
        "#witness-search-exhaustive\"\nverdict = \"exhausted\"\n\n",
        "#incomplete-search\"\nverdict = \"search-incomplete\"\n\n",
    );
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "without a `renewed` record");

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence(
        "#witness-search-exhaustive\"\nverdict = \"exhausted\"\n\n",
        "#incomplete-search\"\nverdict = \"search-incomplete\"\n\
         renewed = \"docs/openapi-surface/sample-search.md\"\n\n",
    );
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "with the outcome `none-registrable`");
}

#[test]
fn handwritten_gate_refuses_an_arm_cover_the_reach_ledgers_do_not_support() {
    let fixture = HandwrittenFixture::new();
    fixture.write_reach("");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "handwritten-reach.tsv has no row for it",
    );

    let fixture = HandwrittenFixture::new();
    fixture.write_reach(&format!(
        "{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t0\t1\n"
    ));
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "measures 0 of its 1 regions executed");

    let fixture = HandwrittenFixture::new();
    let ledger = fixture.path("docs/openapi-surface/golden-reach.tsv");
    let text = std::fs::read_to_string(&ledger).expect("golden-reach ledger");
    std::fs::write(&ledger, text.replace("=0/1", "=1/1")).expect("golden-reach ledger");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "reached by a real specification");

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence(
        "arm = \"src/ir.rs::scalar_body",
        "arm = \"src/ir.rs::base_type_ref",
    );
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "golden-reach-sites.tsv lists no such site",
    );

    let fixture = HandwrittenFixture::new();
    fixture.write_reach(&format!(
        "{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t1\t1\n\
         {HANDWRITTEN_FIXTURE}\tsample-shape\t{HANDWRITTEN_ARM}\t1\t1\n"
    ));
    fixture.assert_refused("handwritten-reach.tsv", "names no live arm-level cover");
}

#[test]
fn handwritten_gate_holds_fixtures_and_rows_to_each_other() {
    let fixture = HandwrittenFixture::new();
    let text = std::fs::read_to_string(fixture.evidence()).expect("evidence");
    std::fs::write(
        fixture.evidence(),
        &text[..text.find("[[covers]]").expect("covers")],
    )
    .expect("coverless evidence");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "has no cover");
    // With the cover gone, the row it named has none either.
    fixture.assert_refused("sample-shape", "no fixture's feature-level cover names it");

    let fixture = HandwrittenFixture::new();
    std::fs::write(
        fixture.fixture_dir().join("openapi.yml"),
        HANDWRITTEN_SPEC.replace("format: email", "format: uuid"),
    )
    .expect("document without the shape");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "declares no site of `schema.format=email`",
    );

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("key = \"sample-shape\"", "key = \"sample-golden\"");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "must read `handwritten`, and it reads `golden`",
    );

    let fixture = HandwrittenFixture::new();
    std::fs::write(
        fixture.path("docs/openapi-surface/witness-search-keys.tsv"),
        "name\tshape\nsample-shape\tschema.format=email\n",
    )
    .expect("malformed key set");
    fixture.assert_refused(
        "witness-search-keys.tsv",
        "has no `key` and `selector` columns",
    );

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("key = \"sample-shape\"", "key = \"no-such-row\"");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "no region row carries this key");
}

#[test]
fn handwritten_gate_keeps_fixtures_out_of_every_real_specification_count() {
    let fixture = HandwrittenFixture::new();
    std::fs::write(
        fixture.path("tests/fixtures/CORPUS.md"),
        format!("| # | name | source |\n|---|---|---|\n| 1 | {HANDWRITTEN_FIXTURE} | https://example.com/openapi.yml |\n"),
    )
    .expect("CORPUS.md");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "is also a CORPUS.md row");

    let fixture = HandwrittenFixture::new();
    std::fs::create_dir_all(fixture.path(&format!("tests/fixtures/{HANDWRITTEN_FIXTURE}")))
        .expect("corpus golden directory");
    std::fs::copy(
        fixture.fixture_dir().join("openapi.yml"),
        fixture.path(&format!("tests/fixtures/{HANDWRITTEN_FIXTURE}/openapi.yml")),
    )
    .expect("vendored copy");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "is never a corpus golden");

    let fixture = HandwrittenFixture::new();
    let ledger = fixture.path("docs/openapi-surface/golden-reach.tsv");
    let text = std::fs::read_to_string(&ledger).expect("golden-reach ledger");
    std::fs::write(
        &ledger,
        text.replace("\tregistered-spec\t", &format!("\t{HANDWRITTEN_FIXTURE}\t")),
    )
    .expect("golden-reach ledger");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "golden-reach.tsv counts it as a witness",
    );

    let fixture = HandwrittenFixture::new();
    std::fs::write(
        fixture.path("tests/fixtures/CORPUS.md"),
        format!("| # | name | source |\n|---|---|---|\n| 1 | copied | {HANDWRITTEN_DIR}/{HANDWRITTEN_FIXTURE}/openapi.yml |\n"),
    )
    .expect("CORPUS.md");
    fixture.assert_refused("CORPUS.md", "a hand-written fixture is never a corpus row");
}

#[test]
fn handwritten_gate_refuses_a_malformed_fixture_directory_or_evidence() {
    let fixture = HandwrittenFixture::new();
    std::fs::write(fixture.evidence(), "digest = [unterminated\n").expect("broken evidence");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "evidence.toml is not TOML");

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("verdict = \"exhausted\"", "verdict = \"witness-found\"");
    fixture.assert_refused(
        HANDWRITTEN_FIXTURE,
        "verdict `witness-found` is not `exhausted`, `search-incomplete` or `config-gated`",
    );

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence(
        "verdict = \"exhausted\"\n\n",
        "verdict = \"exhausted\"\nrenewed = \"docs/openapi-surface/sample-renewed.md\"\n\n",
    );
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "`renewed` is required exactly when");

    let fixture = HandwrittenFixture::new();
    fixture.edit_evidence("digest = ", "extra = \"field\"\ndigest = ");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "the contract admits exactly");

    let fixture = HandwrittenFixture::new();
    std::fs::write(fixture.fixture_dir().join("notes.md"), "notes\n").expect("stray entry");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "notes.md is not part of a fixture");

    let fixture = HandwrittenFixture::new();
    std::fs::rename(
        fixture.fixture_dir(),
        fixture.path(&format!("{HANDWRITTEN_DIR}/Sample_Fixture")),
    )
    .expect("renamed fixture");
    fixture.assert_refused("Sample_Fixture", "a fixture name is lower-kebab");
}

#[test]
fn handwritten_gate_refuses_a_row_its_covers_do_not_describe() {
    let region = "docs/openapi-surface/sample.md";
    for (from, to, message) in [
        (
            "handwritten: sample-fixture;",
            "handwritten: other-fixture;",
            "its evidence cell names ['other-fixture']",
        ),
        (
            "search: exhausted ([record](sample-search.md#witness-search-exhaustive))",
            "search: exhausted ([record](sample-renewed.md#witness-search-exhaustive))",
            "its evidence cell cites `exhausted` at `docs/openapi-surface/sample-renewed.md",
        ),
        (
            "#witness-search-exhaustive)) |  |  |  |",
            "#witness-search-exhaustive)) | 1 site |  |  |",
            "`settlement` cells are empty",
        ),
        (
            "| handwritten | handwritten: sample-fixture; search: exhausted",
            "| handwritten | handwritten sample-fixture, search exhausted",
            "its evidence cell must read",
        ),
    ] {
        let fixture = HandwrittenFixture::new();
        let text = std::fs::read_to_string(fixture.path(region)).expect("region file");
        assert!(text.contains(from), "fixture region file has no {from:?}");
        std::fs::write(fixture.path(region), text.replacen(from, to, 1)).expect("region file");
        fixture.assert_refused("sample-shape", message);
    }

    let fixture = HandwrittenFixture::new();
    std::fs::create_dir_all(fixture.path(PROBE_EXPECTED_DIR)).expect("probe directory");
    std::fs::write(
        fixture.path(&format!("{PROBE_EXPECTED_DIR}/MANIFEST.tsv")),
        format!("{PROBE_MANIFEST_HEADER}\nsample-shape\tabsent-tree\tdiscards\tx\t—\tx\n"),
    )
    .expect("fixture manifest");
    fixture.assert_refused(
        "sample-shape",
        "a committed non-generation proof settles it",
    );

    let fixture = HandwrittenFixture::new();
    let record = fixture.path("docs/openapi-surface/sample-search.md");
    let text = std::fs::read_to_string(&record).expect("search record");
    std::fs::write(
        &record,
        text.replace(&format!("`{HANDWRITTEN_ARM}`"), "an arm"),
    )
    .expect("search record");
    fixture.assert_refused(HANDWRITTEN_FIXTURE, "does not name the arm");
}

/// One induced breakage per remaining rule of the contract, each on a fresh
/// well-formed fixture, each refused with the fixture (or file) and the rule named.
#[test]
fn handwritten_gate_refuses_each_remaining_contract_breakage() {
    type Breakage = fn(&HandwrittenFixture);
    let cases: [(&str, &str, Breakage); 18] = [
        (HANDWRITTEN_FIXTURE, "evidence.toml cannot be read", |f| {
            std::fs::write(f.evidence(), [0xff, 0xfe, 0x00]).expect("undecodable evidence")
        }),
        (
            HANDWRITTEN_FIXTURE,
            "evidence.toml `digest` is not a string",
            |f| {
                let text = std::fs::read_to_string(f.evidence()).expect("evidence");
                let line = text
                    .lines()
                    .find(|l| l.starts_with("digest = "))
                    .expect("digest")
                    .to_string();
                f.edit_evidence(&line, "digest = 5");
            },
        ),
        (HANDWRITTEN_FIXTURE, "is not a `[[covers]]` table", |f| {
            let text = std::fs::read_to_string(f.evidence()).expect("evidence");
            let head = &text[..text.find("[[covers]]").expect("covers")];
            std::fs::write(f.evidence(), format!("{head}covers = [\"x\"]\n")).expect("evidence");
        }),
        (
            HANDWRITTEN_FIXTURE,
            "carries unknown field(s) ['note']",
            |f| {
                f.edit_evidence(
                    "key = \"sample-shape\"",
                    "key = \"sample-shape\"\nnote = \"x\"",
                )
            },
        ),
        (
            HANDWRITTEN_FIXTURE,
            "every field is a non-empty string",
            |f| f.edit_evidence("key = \"sample-shape\"", "key = \"\""),
        ),
        (
            HANDWRITTEN_FIXTURE,
            "its `renewed` record `docs/none.md` does not exist",
            |f| {
                f.edit_evidence(
                "#witness-search-exhaustive\"\nverdict = \"exhausted\"\n\n",
                "#incomplete-search\"\nverdict = \"search-incomplete\"\nrenewed = \"docs/none.md\"\n\n",
            )
            },
        ),
        ("handwritten-reach.tsv", "missing — restore it", |f| {
            std::fs::remove_file(f.path("docs/openapi-surface/handwritten-reach.tsv"))
                .expect("ledger")
        }),
        (
            "handwritten-reach.tsv",
            "the header line must be exactly",
            |f| {
                std::fs::write(
                    f.path("docs/openapi-surface/handwritten-reach.tsv"),
                    "fixture\tkey\n",
                )
                .expect("ledger")
            },
        ),
        (
            "handwritten-reach.tsv line 2",
            "not five tab-separated fields",
            |f| f.write_reach("sample-fixture\tsample-golden\n"),
        ),
        ("handwritten-reach.tsv", "rows are not sorted", |f| {
            f.write_reach(&format!(
                "{HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t1\t1\n\
                 {HANDWRITTEN_FIXTURE}\tsample-golden\t{HANDWRITTEN_ARM}\t1\t1\n"
            ))
        }),
        (
            HANDWRITTEN_DIR,
            "missing — the fixture directory must exist",
            |f| std::fs::remove_dir_all(f.path(HANDWRITTEN_DIR)).expect("fixture directory"),
        ),
        ("stray.txt", "is not a fixture directory", |f| {
            std::fs::write(f.path(&format!("{HANDWRITTEN_DIR}/stray.txt")), "x\n").expect("stray")
        }),
        (
            HANDWRITTEN_FIXTURE,
            "fern-expected is not a directory",
            |f| {
                let tree = f.fixture_dir().join("fern-expected");
                std::fs::remove_dir_all(&tree).expect("tree");
                std::fs::write(&tree, "x\n").expect("tree as a file");
            },
        ),
        (
            HANDWRITTEN_FIXTURE,
            "records no selector for this key",
            |f| {
                std::fs::write(
                    f.path("docs/openapi-surface/witness-search-keys.tsv"),
                    "key\tselector\tregion\tcensus_status\n",
                )
                .expect("key set")
            },
        ),
        (
            HANDWRITTEN_FIXTURE,
            "the census cannot read openapi.yml",
            |f| {
                std::fs::write(
                    f.fixture_dir().join("openapi.yml"),
                    "openapi: 3.0.3\n\tinfo: [\n",
                )
                .expect("unreadable document")
            },
        ),
        (
            HANDWRITTEN_FIXTURE,
            "an arm-level cover's row must read `golden`",
            |f| {
                f.edit_evidence(
                    "key = \"sample-golden\"\narm",
                    "key = \"sample-shape\"\narm",
                )
            },
        ),
        (
            HANDWRITTEN_FIXTURE,
            "golden-reach.tsv measures no such site",
            |f| {
                let ledger = f.path("docs/openapi-surface/golden-reach.tsv");
                let text = std::fs::read_to_string(&ledger).expect("golden-reach ledger");
                std::fs::write(
                    &ledger,
                    text.replace(&format!("{HANDWRITTEN_ARM}=0/1"), "src/ir.rs::other=0/1"),
                )
                .expect("golden-reach ledger");
            },
        ),
        ("sample-shape", "golden-reach-sites.tsv lists it", |f| {
            let table = f.path("docs/openapi-surface/golden-reach-sites.tsv");
            let text = std::fs::read_to_string(&table).expect("site table");
            std::fs::write(
                &table,
                format!("{text}sample-shape\tschema.format=email\tnone\t\n"),
            )
            .expect("site table");
        }),
    ];
    for (subject, message, breakage) in cases {
        let fixture = HandwrittenFixture::new();
        breakage(&fixture);
        fixture.assert_refused(subject, message);
    }
}

/// A census source read from inside the fixture directory — here a vendored
/// corpus directory that is a link to one — is refused whatever it is named.
#[cfg(unix)]
#[test]
fn handwritten_gate_refuses_a_census_source_read_from_a_fixture() {
    let fixture = HandwrittenFixture::new();
    std::os::unix::fs::symlink(
        fixture.fixture_dir(),
        fixture.path("tests/fixtures/linked-spec"),
    )
    .expect("linked corpus directory");
    fixture.assert_refused("linked-spec", "is never a census source");
}

/// A scratch repository laid out as the real one is, holding one valid
/// `differential` pair and one valid `refusal`, for the gate to be driven over
/// through the same [`probe_manifest_failures`] the real manifest takes. The
/// two trees are crozier's own comment-stripped output standing in for Fern's —
/// this exercises the gate's reading of a manifest, not any Fern verdict.
struct ProbeManifestFixture {
    dir: tempfile::TempDir,
}

const FIXTURE_DIFFERENTIAL_KEY: &str = "sample-extension";
const FIXTURE_CONTROL_KEY: &str = "sample-extension-control";
const FIXTURE_REFUSAL_KEY: &str = "sample-refused";
const FIXTURE_PROBE: &str = "openapi: 3.1.0
info:
  title: sample
  version: 1.0.0
  x-sample-extension: true
paths:
  /probe:
    get:
      operationId: probe
      responses:
        \"200\":
          description: ok
          content:
            application/json:
              schema:
                type: object
                properties:
                  ok:
                    type: boolean
";

impl ProbeManifestFixture {
    fn new() -> Self {
        let dir = tempfile::tempdir().expect("fixture repository");
        let fixture = Self { dir };
        let root = fixture.root();
        let probes = root.join(PROBE_DOCUMENTS_DIR);
        let expected = root.join(PROBE_EXPECTED_DIR);
        std::fs::create_dir_all(&probes).expect("fixture probes directory");
        std::fs::create_dir_all(&expected).expect("fixture expectation directory");
        std::fs::write(
            root.join("docs/openapi-surface/sample.md"),
            format!(
                "| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |\n\
                 |---|---|---|---|---|---|---|---|\n\
                 | `{FIXTURE_DIFFERENTIAL_KEY}` | both | Info Object.x-sample-extension | limitations | census `info.x-sample-extension`: 0 declarations |  |  |  |\n"
            ),
        )
        .expect("fixture region file");
        let control = FIXTURE_PROBE.replace("  x-sample-extension: true\n", "");
        std::fs::write(
            probes.join(format!("{FIXTURE_DIFFERENTIAL_KEY}.yml")),
            FIXTURE_PROBE,
        )
        .expect("fixture probe");
        std::fs::write(probes.join(format!("{FIXTURE_CONTROL_KEY}.yml")), control)
            .expect("fixture control");
        std::fs::copy(
            Path::new(env!("CARGO_MANIFEST_DIR"))
                .join(PROBE_DOCUMENTS_DIR)
                .join("ref-pointer-unnamed-segment.yml"),
            probes.join(format!("{FIXTURE_REFUSAL_KEY}.yml")),
        )
        .expect("fixture refused probe");
        for key in [FIXTURE_DIFFERENTIAL_KEY, FIXTURE_CONTROL_KEY] {
            fixture.write_stripped_tree(key);
        }
        let (cli_pin, sdk_pin) = probe_fern_pins();
        std::fs::write(
            fixture.refusal_record(),
            format!(
                "fern_cli_version: {cli_pin}\nfern_python_sdk_version: {sdk_pin}\n\
                 generate_exit: 1\ndiagnostic: Type name must begin with a letter\n\
                 output_tree: none\n"
            ),
        )
        .expect("fixture refusal record");
        fixture.declare();
        fixture
    }

    fn root(&self) -> &Path {
        self.dir.path()
    }

    fn path(&self, rel: &str) -> PathBuf {
        self.root().join(rel)
    }

    fn tree(&self, key: &str) -> PathBuf {
        self.root().join(PROBE_EXPECTED_DIR).join(key)
    }

    fn refusal_record(&self) -> PathBuf {
        self.root()
            .join(PROBE_EXPECTED_DIR)
            .join(format!("{FIXTURE_REFUSAL_KEY}.fern-refusal.txt"))
    }

    /// crozier's output for `key`'s probe, stripped the way a Fern golden is.
    fn write_stripped_tree(&self, key: &str) {
        write_stripped_crozier_tree(
            &self
                .root()
                .join(PROBE_DOCUMENTS_DIR)
                .join(format!("{key}.yml")),
            &self.tree(key),
        );
    }

    /// Write `MANIFEST.tsv` declaring the two proofs at their current digests.
    fn declare(&self) {
        let tree = format!("{PROBE_EXPECTED_DIR}/{FIXTURE_DIFFERENTIAL_KEY}");
        let record = format!("{PROBE_EXPECTED_DIR}/{FIXTURE_REFUSAL_KEY}.fern-refusal.txt");
        let tree_digest = probe_artifact_digest(&self.path(&tree)).expect("tree digest");
        let record_digest = probe_artifact_digest(&self.path(&record)).expect("record digest");
        self.write_manifest(&format!(
            "{PROBE_MANIFEST_HEADER}\n\
             {FIXTURE_DIFFERENTIAL_KEY}\tdifferential\tignores\t{tree}\t{FIXTURE_CONTROL_KEY}\t{tree_digest}\n\
             {FIXTURE_REFUSAL_KEY}\trefusal\trefuses\t{record}\t—\t{record_digest}\n"
        ));
    }

    fn manifest(&self) -> String {
        std::fs::read_to_string(self.path(&format!("{PROBE_EXPECTED_DIR}/MANIFEST.tsv")))
            .expect("fixture manifest")
    }

    fn write_manifest(&self, text: &str) {
        std::fs::write(
            self.path(&format!("{PROBE_EXPECTED_DIR}/MANIFEST.tsv")),
            text,
        )
        .expect("fixture manifest");
    }

    fn edit_manifest(&self, from: &str, to: &str) {
        let text = self.manifest();
        assert!(text.contains(from), "fixture manifest has no {from:?}");
        self.write_manifest(&text.replacen(from, to, 1));
    }

    fn edit_record(&self, from: &str, to: &str) {
        let text = std::fs::read_to_string(self.refusal_record()).expect("fixture record");
        assert!(text.contains(from), "fixture record has no {from:?}");
        std::fs::write(self.refusal_record(), text.replacen(from, to, 1)).expect("fixture record");
        // Re-declare, so the failure observed is the one induced and not the
        // digest that any edit to a record also trips.
        self.declare();
    }

    fn failures(&self) -> Vec<String> {
        probe_manifest_failures(self.root())
    }

    /// The one failure an induced case is expected to produce, naming its key.
    fn assert_refused(&self, key: &str, message: &str) {
        let failures = self.failures();
        assert!(
            failures.iter().any(
                |failure| failure.starts_with(&format!("{key}: ")) && failure.contains(message)
            ),
            "expected a failure naming {key} and saying {message:?}; got:\n{}",
            failures.join("\n")
        );
    }
}

#[test]
fn probe_manifest_accepts_a_valid_differential_pair_and_refusal() {
    let fixture = ProbeManifestFixture::new();
    assert_eq!(Vec::<String>::new(), fixture.failures());
}

#[test]
fn probe_manifest_refuses_an_undeclared_or_missing_artifact() {
    let fixture = ProbeManifestFixture::new();
    std::fs::create_dir(fixture.tree("sample-stray")).expect("stray tree");
    fixture.assert_refused("sample-stray", "no MANIFEST.tsv row names it");

    let fixture = ProbeManifestFixture::new();
    std::fs::copy(
        fixture.refusal_record(),
        fixture.path(&format!(
            "{PROBE_EXPECTED_DIR}/sample-stray.fern-refusal.txt"
        )),
    )
    .expect("stray record");
    fixture.assert_refused(
        "sample-stray.fern-refusal.txt",
        "no MANIFEST.tsv row names it",
    );

    let fixture = ProbeManifestFixture::new();
    std::fs::remove_dir_all(fixture.tree(FIXTURE_DIFFERENTIAL_KEY)).expect("remove tree");
    fixture.assert_refused(FIXTURE_DIFFERENTIAL_KEY, "is missing");
}

#[test]
fn probe_manifest_refuses_an_artifact_whose_digest_moved() {
    let fixture = ProbeManifestFixture::new();
    let text = std::fs::read_to_string(fixture.refusal_record()).expect("record");
    std::fs::write(
        fixture.refusal_record(),
        text.replace("must begin with a letter", "must begin with a digit"),
    )
    .expect("edited record");
    fixture.assert_refused(FIXTURE_REFUSAL_KEY, "but MANIFEST.tsv declares");

    // A still-valid exit value is caught by the digest alone.
    let fixture = ProbeManifestFixture::new();
    let text = std::fs::read_to_string(fixture.refusal_record()).expect("record");
    std::fs::write(
        fixture.refusal_record(),
        text.replace("generate_exit: 1", "generate_exit: 2"),
    )
    .expect("edited record");
    fixture.assert_refused(FIXTURE_REFUSAL_KEY, "but MANIFEST.tsv declares");

    let fixture = ProbeManifestFixture::new();
    let readme = fixture.tree(FIXTURE_DIFFERENTIAL_KEY).join("README.md");
    let text = std::fs::read_to_string(&readme).expect("probe README");
    std::fs::write(&readme, format!("{text}\ntouched\n")).expect("touched README");
    fixture.assert_refused(FIXTURE_DIFFERENTIAL_KEY, "but MANIFEST.tsv declares");
}

#[test]
fn probe_manifest_refuses_an_implements_verdict() {
    let fixture = ProbeManifestFixture::new();
    fixture.edit_manifest("\tignores\t", "\timplements\t");
    fixture.assert_refused(
        FIXTURE_DIFFERENTIAL_KEY,
        "a shape Fern emits output derived from is not settleable by a probe",
    );
}

#[test]
fn probe_manifest_refuses_a_malformed_refusal_record() {
    for (from, to, message) in [
        (
            "diagnostic: Type name must begin with a letter\n",
            "",
            "Contract A requires exactly",
        ),
        (
            "generate_exit: 1\ndiagnostic: Type name must begin with a letter\n",
            "diagnostic: Type name must begin with a letter\ngenerate_exit: 1\n",
            "Contract A requires exactly",
        ),
        (
            "fern_python_sdk_version: ",
            "fern_python_sdk_version: 0.",
            "the corpus pins",
        ),
        (
            "fern_cli_version: ",
            "fern_cli_version: 0.",
            "the corpus pins",
        ),
        (
            "generate_exit: 1",
            "generate_exit_code: 1",
            "Contract A requires exactly",
        ),
        ("generate_exit: 1", "generate_exit: 0", "non-zero exit"),
        (
            "diagnostic: Type name must begin with a letter",
            "diagnostic: ",
            "diagnostic is empty",
        ),
        (
            "output_tree: none",
            "output_tree: fern-python-sdk/",
            "output_tree is",
        ),
    ] {
        let fixture = ProbeManifestFixture::new();
        fixture.edit_record(from, to);
        fixture.assert_refused(FIXTURE_REFUSAL_KEY, message);
    }
}

#[test]
fn probe_manifest_refuses_a_refusal_crozier_does_not_share() {
    let fixture = ProbeManifestFixture::new();
    std::fs::create_dir(fixture.tree(FIXTURE_REFUSAL_KEY)).expect("tree beside refusal");
    fixture.assert_refused(FIXTURE_REFUSAL_KEY, "must not exist");

    // A probe crozier generates, declared as one Fern refused.
    let fixture = ProbeManifestFixture::new();
    std::fs::copy(
        fixture.path(&format!("{PROBE_DOCUMENTS_DIR}/{FIXTURE_CONTROL_KEY}.yml")),
        fixture.path(&format!("{PROBE_DOCUMENTS_DIR}/{FIXTURE_REFUSAL_KEY}.yml")),
    )
    .expect("generating probe");
    fixture.assert_refused(FIXTURE_REFUSAL_KEY, "crozier generated successfully");
    fixture.assert_refused(FIXTURE_REFUSAL_KEY, "crozier emitted an output tree");
}

#[test]
fn probe_manifest_refuses_a_tree_crozier_diverges_from() {
    let fixture = ProbeManifestFixture::new();
    let readme = fixture.tree(FIXTURE_DIFFERENTIAL_KEY).join("README.md");
    let text = std::fs::read_to_string(&readme).expect("tree README");
    std::fs::write(&readme, format!("{text}\ndrift\n")).expect("drifted README");
    fixture.declare();
    fixture.assert_refused(
        FIXTURE_DIFFERENTIAL_KEY,
        "differs from the committed Fern measurement",
    );
}

#[test]
fn probe_manifest_refuses_a_differential_pair_that_does_not_isolate_its_feature() {
    // The two committed trees disagree: the feature is generation.
    let fixture = ProbeManifestFixture::new();
    let readme = fixture.tree(FIXTURE_CONTROL_KEY).join("README.md");
    let text = std::fs::read_to_string(&readme).expect("control README");
    std::fs::write(&readme, format!("{text}\ndrift\n")).expect("drifted README");
    fixture.assert_refused(FIXTURE_DIFFERENTIAL_KEY, "so the feature is generation");

    let probe = format!("{PROBE_DOCUMENTS_DIR}/{FIXTURE_DIFFERENTIAL_KEY}.yml");
    let control = format!("{PROBE_DOCUMENTS_DIR}/{FIXTURE_CONTROL_KEY}.yml");
    for (document, text, message) in [
        (
            probe.as_str(),
            FIXTURE_PROBE.replace("  x-sample-extension: true\n", ""),
            "byte-identical",
        ),
        (
            probe.as_str(),
            FIXTURE_PROBE.replace("x-sample-extension", "x-other-extension"),
            "the probe does not declare",
        ),
        (
            control.as_str(),
            FIXTURE_PROBE.to_string(),
            "the control declares",
        ),
        (
            probe.as_str(),
            FIXTURE_PROBE.replace("description: ok", "description: fine"),
            "outside the `info.x-sample-extension` declaration",
        ),
    ] {
        let fixture = ProbeManifestFixture::new();
        std::fs::write(fixture.path(document), text).expect("edited pair document");
        fixture.assert_refused(FIXTURE_DIFFERENTIAL_KEY, message);
    }
}

/// Re-run the one refused witness-supply probe through Fern itself. Kept out of
/// the offline gate because Fern's pinned Python generator runs in Docker.
#[test]
#[ignore = "requires the Fern CLI, Docker, and generator image"]
fn fern_ref_pointer_unnamed_segment_refusal_matches_measurement() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let workspace = tempfile::tempdir().expect("Fern probe workspace");
    let fern_root = workspace.path().join("fern");
    let openapi = fern_root.join("openapi");
    std::fs::create_dir_all(&openapi).expect("Fern OpenAPI directory");
    std::fs::copy(
        root.join("docs/openapi-surface/probes/ref-pointer-unnamed-segment.yml"),
        openapi.join("openapi.yml"),
    )
    .expect("copy refused probe into Fern workspace");
    std::fs::write(
        fern_root.join("fern.config.json"),
        "{ \"organization\": \"fern\", \"version\": \"5.67.1\" }\n",
    )
    .expect("write pinned Fern CLI configuration");
    std::fs::write(
        fern_root.join("generators.yml"),
        "api:\n  path: openapi/openapi.yml\ngroups:\n  python-sdk:\n    generators:\n      - name: fernapi/fern-python-sdk\n        version: 5.20.0\n        config:\n          pydantic_config:\n            enum_type: python_enums\n        output:\n          location: local-file-system\n          path: ../generated/python\n",
    )
    .expect("write pinned Fern generator configuration");

    let preview = workspace.path().join("preview");
    let output = std::process::Command::new("fern")
        .current_dir(&fern_root)
        .env("FERN_TOKEN", "preview-only-no-publish")
        .env("CI", "true")
        .env("GITHUB_ACTIONS", "true")
        .args([
            "generate",
            "--group",
            "python-sdk",
            "--local",
            "--preview",
            "--output",
        ])
        .arg(&preview)
        .arg("--force")
        .output()
        .expect("run pinned Fern measurement");
    assert_eq!(output.status.code(), Some(1), "Fern must refuse the probe");
    let diagnostic = format!(
        "{}{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    );
    assert!(
        diagnostic.contains("Type name must begin with a letter"),
        "Fern returned the wrong refusal:\n{diagnostic}"
    );
    assert!(
        !preview.join("fern-python-sdk").exists(),
        "Fern must not write an SDK output tree for a refused probe"
    );

    let observed = "fern_cli_version: 5.67.1\nfern_python_sdk_version: 5.20.0\ngenerate_exit: 1\ndiagnostic: Type name must begin with a letter\noutput_tree: none\n";
    let expected =
        std::fs::read_to_string(root.join(
            "docs/openapi-surface/probe-expected/ref-pointer-unnamed-segment.fern-refusal.txt",
        ))
        .expect("committed Fern refusal measurement");
    assert_eq!(
        observed, expected,
        "normalized Fern refusal metadata drifted"
    );
}

/// Generate a corpus's SDK into a fresh tempdir with that corpus's naming, and
/// return the dir (the caller keeps it alive). Fails the test if crozier errors —
/// shared by the gate and the gap reporter so both drive the binary
/// identically.
fn generate_corpus(c: &Corpus) -> tempfile::TempDir {
    generate_corpus_with(c, &[])
}

/// [`generate_corpus`] with `extra` flags appended to the corpus's own — the
/// overlay gate's setting, such as `--enum-type literals`.
fn generate_corpus_with(c: &Corpus, extra: &[&str]) -> tempfile::TempDir {
    let out = tempfile::tempdir().expect("tempdir");
    let (mut command, _source) = corpus_command(c, out.path());
    command
        .args(extra)
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    out
}

/// The exact public CLI invocation used for a corpus. Reporters call the same
/// command without assert_cmd's fail-fast assertion so one broken corpus cannot
/// hide differences in its siblings. It never passes `--no-config`: `just
/// test-corpus-match-strict` turns strict Fern compatibility on through
/// `CROZIER_FERN_STRICT`, which `--no-config` would silently drop. Keep the
/// returned source directory alive until the subprocess finishes; then dropping
/// it removes the staged copies.
fn corpus_command(c: &Corpus, output: &Path) -> (Command, tempfile::TempDir) {
    let staged = tempfile::tempdir().expect("source staging directory");
    let prepared = std::process::Command::new(if cfg!(windows) { "python" } else { "python3" })
        .arg(Path::new(env!("CARGO_MANIFEST_DIR")).join("scripts/corpus_sources.py"))
        .args(["prepare", "--fixture", c.api, "--output"])
        .arg(staged.path())
        .output()
        .expect("prepare committed corpus source");
    assert!(
        prepared.status.success(),
        "{}",
        String::from_utf8_lossy(&prepared.stderr)
    );
    let spec = String::from_utf8(prepared.stdout).expect("source path is UTF-8");
    let mut command = crozier();
    command
        .args(["generate", "--spec"])
        .arg(spec.trim())
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
    (command, staged)
}

fn try_generate_corpus(c: &Corpus) -> Result<tempfile::TempDir, String> {
    let out = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let (mut command, _source) = corpus_command(c, out.path());
    let result = command
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

/// How crozier's `generated` output for `rel` compares with the committed
/// fixture `expected` under the one comparison engine, `context` describing the
/// two trees — the single definition of "matches" every comparison here and
/// `crozier compare` share (`crozier::parity`; see docs/departures/README.md).
/// Its diff is precisely what the engine decided on, never a raw diff polluted
/// by comments or by a departure the catalog accounts for. Panics on a pair a
/// rule cannot run on.
fn compare_with_golden(
    context: &Context,
    rel: &str,
    generated: &str,
    expected: &str,
) -> parity::FileComparison {
    parity::compare_file(context, rel, generated, expected)
        .unwrap_or_else(|error| panic!("{rel}: {error}"))
}

/// Whether crozier's `generated` output for `rel` matches the committed
/// fixture once the catalog's departures are applied ([`compare_with_golden`]).
fn generated_matches_fixture(
    context: &Context,
    rel: &str,
    generated: &str,
    expected: &str,
) -> bool {
    compare_with_golden(context, rel, generated, expected).matches()
}

/// Each departure `compared` applied in `rel`, as a ledger check reads it.
fn observed_in(rel: &str, compared: &parity::FileComparison) -> Vec<Observed> {
    compared
        .departures
        .iter()
        .map(|departure| (rel.to_string(), departure.line, departure.id.to_string()))
        .collect()
}

/// `apideck.com-crm`: a real-world committed corpus API (issue #77). Its OpenAPI
/// spec is committed (`corpus_spec`); its full Fern golden is
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

/// Enforce the real-world Apideck byte-match against its committed source.
#[test]
fn apideck_crm_matches_fern_output() {
    if corpus_spec(APIDECK_CRM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apideck committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping apideck byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_CRM);
}

/// `bunq.com`: a large real-world committed corpus API (issue #77) — one sub-client
/// per tag over ~10× apideck's surface (docs/matching.md holds the measured
/// endpoint/schema/tag counts), the pipeline's at-scale stress target. Its
/// OpenAPI spec is committed (`corpus_spec`); its full Fern golden is
/// committed and crozier reproduces the entire golden byte-for-byte. Its empty
/// `unmatched` list makes any future divergence fail by default.
const BUNQ: Corpus = Corpus {
    api: "bunq.com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `bungie.net`: a real-world committed corpus API (issue #77) chosen as the
/// schema-heavy counterpart to endpoint-heavy bunq — 869 component schemas across
/// only 13 tags. Fern accepts the raw spec cleanly and crozier consumes it without
/// error; its OpenAPI spec is committed (`corpus_spec`), and crozier
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
// Five additional real-world committed corpora (issue #77), added together as a
// batch of harder, feature-diverse targets. Each passes `fern check` cleanly (the
// prerequisite — Fern must accept the raw spec first); their Fern golden `expected/`
// trees are workflow-managed. All five reproduce their goldens byte-for-byte, so
// each `unmatched` list is empty and any future divergence fails by default. The
// offline `check` gate and `just test-corpus-match` both read committed sources.
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
    // upstream failure is covered at the process boundary, with no golden.
    unmatched: &[],
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

/// `openlinksw-osdb`: corpus row 191, OpenLink's OSDB REST API. Its string
/// schemas declare `format: uri-template`, which no other golden-bearing source
/// does; its namespaced body property `osdb:output_type` and its example-only
/// `2XX` beside a `default` error pin two generator repairs.
const OPENLINKSW_OSDB: Corpus = Corpus {
    api: "openlinksw-osdb",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `ziptax-node`: corpus row 192, ZipTax's sales-tax API as its Node SDK
/// repository publishes it. All 34 operations carry `x-fern-audiences` by API
/// version (`v10`-`v60`), and generating for `v60` keeps 27 and filters out 7 —
/// the first real-world document the audience filter runs over.
const ZIPTAX_NODE: Corpus = Corpus {
    api: "ziptax-node",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &["v60"],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `nexmo-messages`: corpus row 193, the Vonage (Nexmo) Messages API 1.4.0. Its
/// `sendMessage` body is a `oneOf` of channel `oneOf`s over `allOf` members — an
/// operation-level union whose members are compositions, which no earlier golden
/// sends down `hoist_union_variant`'s inline-object arm.
const NEXMO_MESSAGES: Corpus = Corpus {
    api: "nexmo-messages",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `deepsearch-ds-v2`: corpus row 194, IBM's Deep Search (DS) API 3.0.0 as the
/// DS4SD toolkit pins it. Its properties declare `anyOf` discriminated unions
/// inline, which no earlier golden hoists through `hoist_discriminated_union`.
const DEEPSEARCH_DS_V2: Corpus = Corpus {
    api: "deepsearch-ds-v2",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `mindee-ocr`: corpus row 195, the Mindee OCR API as its publisher serves it.
/// It pins Fern's output for that spec byte for byte; it does not execute
/// `items-oneof-element`'s unreached arm, so it is no witness for that row.
const MINDEE_OCR: Corpus = Corpus {
    api: "mindee-ocr",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `opencodeui`: corpus row 196, the opencode server API as the OpenCodeUI web
/// client pins it. Its array items declare an `anyOf` of one inline object,
/// which no earlier golden sends down `hoist_array_item_type`'s sole-member arm.
const OPENCODEUI: Corpus = Corpus {
    api: "opencodeui",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const CORPORA: &[&Corpus] = &[
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
    &APIDECK_ATS,
    &BUILDRELAY,
    &TLON_NOTES,
    &TWILIO_MESSAGING_V1,
    &LIVEPEER_AI_RUNNER,
    &EOS_EXTRA_FIELDS_FORBID,
    &MED_ANVISA_PRICE,
    &SAC_BACKEND,
    &KYTOS_SDNTRACE_CP,
    &WITHSECURE_GDPR_SUBJECT_RIGHTS,
    &PROMETHEUS_X_EDGE_COMPUTING,
    &EXA_GATE,
    &AMAZONAWS_COM_CLOUDFRONT,
    &KHOAINATS,
    &HELIOS_VERIFIABLE_API,
    &EOZILLA,
    &OPENEPCIS_DPP_READY,
    &NDW_ACCESSIBILITY_MAP,
    &MARIMO,
    &MARIMO_CLIENT_CLASS_NAME,
    &BLACKADI_OAUTH2,
    &MOSIP_ESIGNET,
    &OPENBANKINGPROJECT_CH_KUNDENBEZIEHUNG,
    &CYBERARK_CONJUR_API,
    &ADYEN_REPORT_NOTIFICATION,
    &ADYEN_MANAGED_RISK_NOTIFICATION,
    &GO_KRATOS_CASBIN_ADMIN,
    &DESCOPE_AUTHZCACHE,
    &SWAGGER_PETSTORE,
    &CYCLONEDX_TRANSPARENCY_EXCHANGE,
    &ADYEN_CAPITAL,
    &APIVIDEO_ANDROID_UPLOADER,
    &TRUEFOUNDRY_TRUEFORGE,
    &VOLVIEW_BACKEND_CONTRACT,
    &OSPARC_SIMCORE_WEBSERVER,
    &HELIXDB_HTTP_API,
    &FLOWDAPT,
    &K8S_CONTAINER_SERVICE_PROVIDER,
    &DANIWEB_CONNECT,
    &CHAINGATEWAY_IO,
    &HUBSPOT_EVENTS,
    &PALOALTO_REMOTE_NETWORKS,
    &OPENINTEGRATIONHUB_SECRET_SERVICE,
    &STRAPI_REST_API,
    &LISTENNOTES,
    &VTEX_PRICING,
    &AWS_IMPORTEXPORT,
    &OPENBANKING_BRASIL_DIRECTORY,
    &API_OPENVERSE_ORG,
    &DISCORD_COM,
    &BRAINTRUST_DEV,
    &AGCO_ATS,
    &TORRENTARR,
    &SVIX_WEBHOOKS,
    &KOMGA,
    &SHORT_IO,
    &WEBFLOW_V2,
    &LORIS_DATAQUERY,
    &SFTPGO,
    &GOOGLEAPIS_SERVICEBROKER,
    &AUDIOBOOKSHELF,
    &STEAMINPUTDB,
    &PAYPAL_CATALOG_PRODUCTS,
    &FOLIO_MOD_AUTHTOKEN,
    &RAYBOT,
    &OPENLINKSW_OSDB,
    &ZIPTAX_NODE,
    &NEXMO_MESSAGES,
    &DEEPSEARCH_DS_V2,
    &MINDEE_OCR,
    &OPENCODEUI,
    &PALOALTO_CSPM_ALERTS,
    &PALOALTO_CSPM_REPORTS,
    &PALOALTO_CSPM_SEARCH_MANAGER,
    &THRIVECART,
    &TRUEFOUNDRY_TRUEFORGE_5ADDE28,
    &FERGUS,
    &GROUPE_PSA,
    &TIMELYAPP,
    &NEXTGEN,
    &AUTO_AGENT_PROTOCOL,
    &SKOOL,
    &SPENDESK,
    &BILLIE,
    &ALMA_FRANCE,
    &OUTREACH,
    &TALLY,
    &BILLIE_ENTRY,
    &SKOOL_ENTRY,
    &TIMELYAPP_ENTRY,
    &CRADL,
    &ZULIP,
    &ZULIP_JENTIC,
    &ZULIP_JENTIC_ENTRY,
    &MILVUS_RESTFUL_V2_3,
    &MILVUS_RESTFUL_V2_4,
    &RAMU_SHOGI,
    &LANGCHAIN_AGENT_PROTOCOL,
    &HSE,
    &MILVUS_VECTOR_OPERATIONS,
    &MISTLE_CONTROL_PLANE,
    &OSPARC_PAYMENTS,
    &HUATUO_NODE,
    &HUATUO_SERVER,
    &VISKIT_STUDIO,
    &EMBEDPDF_CLOUDPDF,
    &NPQ_REGISTRATION,
    &SIM_LOGS,
    &SIM_TABLES,
    &VELLUM_GATEWAY,
    &DOT_AI,
    &PALOALTO_CODE_TECHNOLOGIES,
    &MARIMO_PLUGINS,
    &OTOROSHI,
    &GOOGLEAPIS_MONITORING_V1,
    &DOCU_GOAPISERVER,
    &ONEVOICE,
    &XFSC_OIDC_IDENTITY_RESOLVER,
    &ADYEN_ACS_NOTIFICATION,
    &PEOPLEDATALABS,
    &STANDRIG,
    &MOCKSERVER,
    &IDEACONSULT_ENANOMAPPER,
    &OPENAIRE_GRAPH,
    &QREDENCE_FLEET_RLM,
    &FIWARE_CONTEXT_GENERATOR,
    &HASURA_METADATA,
    &ZOONK,
    &OPENFOODFACTS_TAXONOMY_EDITOR,
    &QONTRACT_API,
    &OAL_EXAMPLE,
    &MILLENIUM_FALCON_CHALLENGE,
    &MAXIMO_WXO_INTEGRATION,
    &MI_MUSIC,
    &G4BRYM_DOWNLOAD_MANAGER,
    &OPENTOSCA_LICENSE_ENGINE,
    &CHAT_REST_API,
    &ESP32_STREAMLINE_BRIDGE,
    &CPHOS_AI_QUESTION,
    &FLASK_EXAMPLE_HEROKU,
    &OIP_WEB_API,
    &WAYLAY_QUERIES,
    &CONFLUENT_KAFKA_CONNECT,
    &NETGSM_SMS,
    &BREIZHSPORT_CATALOGUE,
    &PROTOFORM_CONFORMANCE,
    &ERE_PS_APP,
    &TYPESCRIPT_SERVICE_TEMPLATE,
    &HUATUO_NODE_TREE,
    &APIDECK_ECOSYSTEM_CLIENT_CLASS_NAME,
    &YOURBRAND_TICKETING,
    &LOOTLOG_BATTLELOG,
    &EGO_MICROSERVICES,
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
    // An empty opt-out list makes the entire committed golden mandatory.
    if corpus_spec(BUNQ.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the bunq committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping bunq byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&BUNQ);
}

#[test]
fn bungie_matches_fern_output() {
    if corpus_spec(BUNGIE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the bungie committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping bungie byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&BUNGIE);
}

// Each batch corpus compares its complete golden using committed sources.

#[test]
fn anchore_matches_fern_output() {
    if corpus_spec(ANCHORE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the anchore committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping anchore byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&ANCHORE);
}

#[test]
fn apache_airflow_matches_fern_output() {
    if corpus_spec(APACHE_AIRFLOW.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apache committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping apache byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&APACHE_AIRFLOW);
}

#[test]
fn discourse_matches_fern_output() {
    if corpus_spec(DISCOURSE.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the discourse committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!("skipping discourse byte-match: committed source missing (run just lint-corpus-sources)");
        return;
    }
    assert_corpus_matches(&DISCOURSE);
}

#[test]
fn appwrite_server_matches_fern_output() {
    if corpus_spec(APPWRITE_SERVER.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the appwrite committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping appwrite byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&APPWRITE_SERVER);
}

#[test]
fn apicurio_matches_fern_output() {
    if corpus_spec(APICURIO.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the apicurio committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!(
            "skipping apicurio byte-match: committed source missing (run just lint-corpus-sources)"
        );
        return;
    }
    assert_corpus_matches(&APICURIO);
}

#[test]
fn gambitcomm_mimic_matches_fern_output() {
    if corpus_spec(GAMBITCOMM_MIMIC.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the gambitcomm committed corpus spec is missing; \
             run just lint-corpus-sources to diagnose the missing committed source"
        );
        eprintln!("skipping gambitcomm byte-match: committed source missing (run just lint-corpus-sources)");
        return;
    }
    assert_corpus_matches(&GAMBITCOMM_MIMIC);
}

#[test]
fn dnd5eapi_matches_fern_output() {
    if corpus_spec(DND5EAPI.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the dnd5eapi committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the apache-qakka committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the authentiqio committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the ETSI MEC 010-2 committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Webhook committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Vault committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Airbyte Config committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Bintable committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the APIs.guru committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Color Pizza committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the By Automata committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Proxy committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Connector committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Ecommerce committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Issue Tracking committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Appwrite Client committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck File Storage committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck HRIS committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Accounting committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the CalorieNinjas committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the EOS committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck SMS committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Ecosystem committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Customer Support committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apideck Lead committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Apache Airflow committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the OpenFIGI committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Twilio Voice v1 committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Microcks committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Red Hat Catalog Inventory committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Xero Payroll AU committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Traccar committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Reverb committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the MAIF Otoroshi committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Portfolio Optimizer committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Open Banking account info committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the NetBox committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
/// `const`, and top-level webhooks — the only corpus pinning webhook payload
/// hoisting (eight inline webhook bodies become `Post*Payload` types). Fern
/// accepts the raw pinned spec; the golden is workflow-owned.
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
    unmatched: &[],
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

/// `apideck.com-ats`: the ATS API nests an inline social-link object in an
/// array property of the `Applicant` component schema.
const APIDECK_ATS: Corpus = Corpus {
    api: "apideck.com-ats",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `buildrelay`: the BuildRelay API declares a direct inline-object body on its
/// internal-server-error response.
const BUILDRELAY: Corpus = Corpus {
    api: "buildrelay",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `tlon-notes`: the Notes API combines four inline, untitled discriminated
/// unions without explicit mappings with a recursive `ImportNode` schema.
const TLON_NOTES: Corpus = Corpus {
    api: "tlon-notes",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `twilio.com-twilio_messaging_v1`: the Twilio Messaging API includes a
/// `russell_3000` property whose Python identifier drops the final underscore.
const TWILIO_MESSAGING_V1: Corpus = Corpus {
    api: "twilio.com-twilio_messaging_v1",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `livepeer-ai-runner`: the production inference runtime publishes three
/// untagged, groupless operations alongside ten tagged pipeline operations.
const LIVEPEER_AI_RUNNER: Corpus = Corpus {
    api: "livepeer-ai-runner",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `amazonaws.com-cloudfront`: every CloudFront operation declares the whole `5xx`
/// tail — `502`, `505`, `506`, `507`, `508`, `510` and `511` — so this row pins
/// Fern's exception name for each of the seven at once.
const AMAZONAWS_COM_CLOUDFRONT: Corpus = Corpus {
    api: "amazonaws.com-cloudfront",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `khoainats`: the Khoai NATS Admin API declares an `openIdConnect` scheme
/// (`Roles`) beside an HTTP bearer one, and leaves `/v1/noauth` unsecured.
/// `openIdConnect` is the one member of its scheme family Fern's importer keeps
/// rather than drops, so this is the corpus's only golden over a document that
/// declares one: Fern emits a bearer `token` on `Authorization`, optional
/// because not every operation is authenticated. Crozier reaches the same bytes
/// through `auth_model`'s HTTP-bearer arm, since `BearerToken` precedes `Roles`
/// in the document — no public spec the corpus screened declares
/// `openIdConnect` without a supported scheme ahead of it, so the golden pins
/// the emitted credential rather than the fallthrough arm.
const KHOAINATS: Corpus = Corpus {
    api: "khoainats",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `helios-verifiable-api`: every one of its 27 component schemas is a
/// remote-URL `$ref` into an `ethereum/execution-apis` document, the one
/// reference form Fern follows rather than discards. Fern fetches each
/// referenced document over HTTPS and resolves it transitively, so this row is
/// the corpus's only evidence that crozier opens a second document at all.
const HELIOS_VERIFIABLE_API: Corpus = Corpus {
    api: "helios-verifiable-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `eozilla`: the Eozilla OGC API - Processes server is the corpus's only
/// document whose schema graph closes a cycle through `additionalProperties`
/// rather than through `properties` or `items`. Its `Schema` component names
/// itself twice as a map value — `Schema.properties` and
/// `Schema.discriminator.mapping` — and Fern reads that map-of-self rather than
/// flattening it: the golden carries `from __future__ import annotations`, a
/// forward-referenced `typing.Optional[typing.Dict[str, "Schema"]]`, and a
/// trailing `update_forward_refs`. 335 golden files already call
/// `update_forward_refs`, but none of them for a map, so this row is what pins
/// the map arm of crozier's recursion handling against Fern rather than against
/// crozier's own expectation.
const EOZILLA: Corpus = Corpus {
    api: "eozilla",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openepcis-dpp-ready`: the EN 18222 Digital Product Passport API declares two
/// `type: [string, number, boolean]` schemas — multi-member type arrays with more
/// than one *non-null* member. Every one of the corpus's other 498 `type` arrays
/// has a single non-null member, so before this row the only `typing.Union`s in
/// any golden came from `oneOf`/`anyOf` and nothing pinned what Fern does with a
/// multi-type array. It emits a union over the declared members, and this row
/// holds crozier to that.
const OPENEPCIS_DPP_READY: Corpus = Corpus {
    api: "openepcis-dpp-ready",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `ndw-accessibility-map`: the NDW Location Services accessibility-map API is the
/// corpus's only source whose `components.headers` entries declare
/// `allowEmptyValue`. Both Header Objects (`Accept-encoding`, `Content-encoding`)
/// carry it, and `Content-encoding` is referenced from a response, so the field is
/// declared where a generator would read it rather than in an orphaned component.
/// Crozier models no Header Object at all, so nothing it emits derives from the
/// field; this row is what holds that silence to Fern's rather than to crozier's
/// own expectation.
const NDW_ACCESSIBILITY_MAP: Corpus = Corpus {
    api: "ndw-accessibility-map",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `marimo`: the Marimo API's `Base64String` component declares
/// `contentEncoding: base64`. No prior golden source declares this JSON Schema
/// 2020-12 keyword, so this row holds Crozier's treatment to Fern's output.
const MARIMO: Corpus = Corpus {
    api: "marimo",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Configured class names over the registered package-root API.
const MARIMO_CLIENT_CLASS_NAME: Corpus = Corpus {
    api: "marimo-client-class-name",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: Some("DispatchClient"),
    extra_fields: None,
    unmatched: &[],
};

/// `blackadi-oauth2`: the OAuth 2.0 authorization-server API is the corpus's only
/// source declaring an IANA HTTP authentication scheme Fern's importer does not
/// support — `dpopAuth` carries `scheme: dpop` (RFC 9449) beside a `bearer` and a
/// `basic` scheme. Fern imports the supported scheme and drops the DPoP one
/// without a trace in the SDK, so this row is what holds crozier's identical
/// silence to Fern's output rather than to crozier's own expectation.
const BLACKADI_OAUTH2: Corpus = Corpus {
    api: "blackadi-oauth2",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `mosip-esignet`: the MOSIP eSignet API is the corpus's second `scheme: dpop`
/// witness and the one that declares the IANA registry's own mixed-case spelling
/// — `Authorization-DPoP` carries `scheme: DPoP` beside four `bearer` schemes,
/// where `blackadi-oauth2` declares the lowercase form. Fern imports a supported
/// scheme and drops the DPoP one whatever its case, so this row holds crozier's
/// identical silence to Fern's output on the spelling the registry publishes.
const MOSIP_ESIGNET: Corpus = Corpus {
    api: "mosip-esignet",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openbankingproject-ch-kundenbeziehung`: the Swiss Open Banking
/// customer-relationship API declares `scheme: DPoP` beside `bearer`, and is the
/// corpus's first source declaring `type: mutualTLS` — the Security Scheme type
/// 3.1 added, which Fern's importer drops as it drops DPoP. Its document-level
/// `security` pairs the dropped `mTLS` scheme with a supported `bearer` one, so
/// this row pins that crozier drops both in exactly the places Fern does.
const OPENBANKINGPROJECT_CH_KUNDENBEZIEHUNG: Corpus = Corpus {
    api: "openbankingproject-ch-kundenbeziehung",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `cyberark-conjur-api`: the CyberArk Conjur 5.3.2 bundle is the corpus's only
/// source declaring `scheme: mutual` (RFC 8120) — `conjurKubernetesMutualTls`
/// carries it beside a `basic` scheme and an `apiKey` one, and the document-level
/// `security` names all three. Fern imports the two it supports and drops the
/// mutual one without a trace, so this row holds crozier's identical silence to
/// Fern's output. Its `paths` are relative-file `$ref`s into sibling documents the
/// pinned URL does not carry, which Fern discards without diagnosing, so the
/// golden is the endpoint-free client that pairing leaves behind: required
/// `authorization`, `username` and `password` arguments over eight component
/// types and no methods.
const CYBERARK_CONJUR_API: Corpus = Corpus {
    api: "cyberark-conjur-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `adyen-report-notification`: Adyen's "Report webhooks" document is the
/// corpus's first source that omits `paths` altogether — a valid OpenAPI 3.1
/// document whose only API surface is one webhook
/// (`balancePlatform.report.created`) over five component schemas. Every other
/// registered source declares a Paths Object, so this row pins what crozier
/// generates when the field the whole endpoint pipeline reads is absent.
const ADYEN_REPORT_NOTIFICATION: Corpus = Corpus {
    api: "adyen-report-notification",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `adyen-managed-risk-notification`: Adyen's "Managed risk webhooks" document
/// declares eight top-level `webhooks` and no `paths` at all, the webhook-only
/// shape 3.1 added. Row 69 (`tamoss`) declares webhooks beside paths; this row
/// is the first registered source where the webhooks stand alone, so its golden
/// pins that Fern emits no webhook payload model and crozier emits the same
/// endpoint-free client. It also declares `jsonSchemaDialect`.
const ADYEN_MANAGED_RISK_NOTIFICATION: Corpus = Corpus {
    api: "adyen-managed-risk-notification",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `go-kratos-casbin-admin`: the protoc-gen-openapi document the go-kratos
/// Casbin example ships is one of the corpus's two independent witnesses of an
/// *empty* Paths Object — `paths: {}` beside `components.schemas: {}` and an
/// empty `info.title` — which is a different shape from omitting `paths`
/// entirely (rows 100 and 101). `descope-authzcache` (row 103) is the other.
/// Its golden pins the empty client and documentation scaffolding Fern leaves
/// behind.
const GO_KRATOS_CASBIN_ADMIN: Corpus = Corpus {
    api: "go-kratos-casbin-admin",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `descope-authzcache`: a second, independent witness of the empty Paths Object
/// from another project — the `protoc-gen-openapi` document Descope's authzcache
/// service ships declares the same `paths: {}` beside `components.schemas: {}`
/// and an empty `info.title` that row 102 does, out of a separately maintained
/// repository (both are MIT). Two witnesses from unrelated projects is what tells
/// an empty Paths Object apart from one project's quirk, the way rows 83 and 84
/// pin the accent-dropping property rule.
const DESCOPE_AUTHZCACHE: Corpus = Corpus {
    api: "descope-authzcache",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `swagger-petstore`: the Swagger Petstore reference document is the corpus's
/// only source declaring `openapi: 3.0.4`, the patch level OpenAPI's 3.0
/// maintenance release added. Every other registered source stops at `3.0.3` or
/// jumps to 3.1, so this row is what pins that crozier reads the newer 3.0 patch
/// spelling the way Fern does rather than refusing it at the boundary.
const SWAGGER_PETSTORE: Corpus = Corpus {
    api: "swagger-petstore",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `cyclonedx-transparency-exchange`: the OWASP Transparency Exchange API
/// specification is the corpus's only source declaring `openapi: 3.1.1`, and its
/// second declaring `jsonSchemaDialect` after row 101, this one beside a
/// populated Paths Object. It pins both document-level 3.1 declarations at once:
/// the newer patch spelling, and the dialect field, over 23 real endpoints.
const CYCLONEDX_TRANSPARENCY_EXCHANGE: Corpus = Corpus {
    api: "cyclonedx-transparency-exchange",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `adyen-capital`: the Adyen Capital API is the document the `json-schema-dialect`
/// witness search named, and the corpus's third source declaring
/// `jsonSchemaDialect`. Rows 101 and 105 declare it over a webhook-only document
/// and a `3.1.1` one; this row pins the dialect beside an ordinary populated
/// Paths Object, so the declaration is measured where endpoints, models and auth
/// are all generated from schemas the dialect nominally governs.
const ADYEN_CAPITAL: Corpus = Corpus {
    api: "adyen-capital",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `apivideo-android-uploader`: the api.video document is the corpus's only
/// source declaring a Reference Object `description` sibling — its
/// `components.parameters.filterBy` is a `$ref` to `filterBy_2` carrying its own
/// `description`. Every other registered source writes `$ref` alone, so this row
/// is what pins that crozier reads a reference with a sibling the way Fern does
/// rather than tripping over the extra key.
const APIVIDEO_ANDROID_UPLOADER: Corpus = Corpus {
    api: "apivideo-android-uploader",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `truefoundry-trueforge`: the TrueForge API is the corpus's only source
/// declaring `x-fern-ignore`, on four Operation Objects, and the only one
/// declaring Fern's SDK-shaping extensions beside it — `x-fern-sdk-group-name`
/// (54 sites, eight of them two-level nested groups), `x-fern-sdk-method-name`
/// (54), `x-fern-pagination` (7) and `x-fern-streaming` (2). It therefore pins
/// nested sub-clients, cursor pagination and the dual-header ignore policy at
/// once, over 40 paths and 218 component schemas that carry no `operationId` at
/// all, so every method name comes from an extension or from the path.
const TRUEFOUNDRY_TRUEFORGE: Corpus = Corpus {
    api: "truefoundry-trueforge",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `volview-backend-contract`: the neutral backend contract VolView's own client
/// calls is the corpus's only source declaring `$comment`, the JSON Schema
/// 2020-12 annotation keyword — `components.schemas.TaskSpec` and
/// `components.schemas.AnnotationsFile` each carry one. It is also the only
/// registered source whose `jsonSchemaDialect` names the JSON Schema 2020-12
/// meta-schema rather than the OAS 3.1 dialect rows 101, 105 and 106 name, so
/// this row pins that crozier ignores an annotation-only schema keyword exactly
/// where Fern does, over nine paths and 15 component schemas.
const VOLVIEW_BACKEND_CONTRACT: Corpus = Corpus {
    api: "volview-backend-contract",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `osparc-simcore-webserver`: the web API the IT'IS Foundation's own oSPARC
/// front end calls is the corpus's only source declaring the JSON Schema
/// 2020-12 string-encoding pair — `contentMediaType` at 24 sites and
/// `contentSchema` at 24 — and the only one whose `exclusiveMaximum` carries a
/// *numeric* value (8 sites), the 3.1 spelling beside the 3.0 boolean the
/// corpus already pins. It is also the corpus's second `propertyNames`
/// declarer (30 sites, beside row 109's 7), so this row pins what Fern does
/// with four annotation-only 2020-12 keywords over 214 paths and 480 component
/// schemas.
const OSPARC_SIMCORE_WEBSERVER: Corpus = Corpus {
    api: "osparc-simcore-webserver",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `helixdb-http-api`: the HTTP API HelixDB's own database serves is the
/// corpus's only source declaring `dependentRequired` —
/// `components.schemas.ReadQueryRequest` and
/// `components.schemas.WriteQueryRequest` each carry one — so this row pins
/// what Fern does with the 2020-12 conditional-requirement keyword, over three
/// paths, 17 component schemas and a `bearerAuth` scheme.
const HELIXDB_HTTP_API: Corpus = Corpus {
    api: "helixdb-http-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `flowdapt`: the API the Flowdapt server publishes for itself is the corpus's
/// only source declaring `$defs`, the 2020-12 subschema-bundle keyword — seven
/// of them inside `components.schemas` — and it declares them inside an
/// `openapi: 3.0.2` document, so this row pins what Fern does with a 2020-12
/// definitions keyword written where the 3.0 dialect does not define it.
const FLOWDAPT: Corpus = Corpus {
    api: "flowdapt",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `k8s-container-service-provider`: the API the DCM project's own Kubernetes
/// container service provider serves is the corpus's only source declaring
/// `format: json-pointer` — `components.schemas.Error.pointer` and
/// `components.schemas.ErrorDetail.pointer` each annotate a string field with
/// the RFC 6901 format, on the RFC 7807 problem detail the service returns — so
/// this row pins what Fern does with a registered JSON Schema string format it
/// has no narrower Python type for, over three paths and 18 component schemas.
const K8S_CONTAINER_SERVICE_PROVIDER: Corpus = Corpus {
    api: "k8s-container-service-provider",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `daniweb-connect`: the DaniWeb Connect API is the corpus's only source
/// crossing `style: simple` with `in: path` over an *array* schema — 15 of
/// them, the `ID` parameter of `/apps/{ID}`, `/audiences/{ID}`,
/// `/conversations/{ID}` and twelve more, each an array of integers — so this
/// row pins the path segment Fern interpolates a list-valued parameter into.
const DANIWEB_CONNECT: Corpus = Corpus {
    api: "daniweb-connect",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `chaingateway-io`: the Ethereum gateway Chaingateway.io describes for
/// itself is the corpus's densest source crossing `style: simple` with
/// `in: header` over a scalar schema — 26 of them across its 21 operations,
/// where corpus row 107 declares the same crossing twice — so this row pins
/// the header value `raw_client.py` sends for an explicitly-styled header
/// parameter and the argument `client.py` declares for it.
const CHAINGATEWAY_IO: Corpus = Corpus {
    api: "chaingateway-io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `hubspot-events`: HubSpot's Events API v3 is the corpus's only source
/// crossing `style: form` with `in: query` over an *object* schema —
/// `objectProperty.{propname}` and `property.{propname}` on
/// `GET /events/v3/events/`, each `explode: true` over `{type: object}` — so
/// this row pins the argument Fern declares for a free-form object query
/// parameter whose wire name itself carries a template.
const HUBSPOT_EVENTS: Corpus = Corpus {
    api: "hubspot-events",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `paloalto-remote-networks`: the Configuration Orchestration API Palo Alto
/// Networks publishes on its own developer portal is the corpus's only source
/// crossing `style: deepObject` with an *array* schema —
/// `components.parameters.RemoteNetworksNames`, `explode: true` over
/// `{type: array}` — so this row pins what Fern serialises when the
/// object-only style meets a list.
const PALOALTO_REMOTE_NETWORKS: Corpus = Corpus {
    api: "paloalto-remote-networks",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openintegrationhub-secret-service`: the description the Open Integration
/// Hub's Secrets Service ships beside its own source is the corpus's only
/// source crossing `style: deepObject` with a *scalar* schema —
/// `components.parameters.pageSize`, `{in: query, style: deepObject}` over
/// `{type: integer}` — the crossing the specification leaves undefined, so
/// this row pins what Fern does with a style its schema cannot satisfy.
const OPENINTEGRATIONHUB_SECRET_SERVICE: Corpus = Corpus {
    api: "openintegrationhub-secret-service",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `strapi-rest-api`: Strapi's REST API is the corpus's second declarer of
/// `style: deepObject` over an *array* schema — `components.parameters.fields`,
/// `explode: true` over `{type: array}` — so this row and corpus row 117 pin the
/// same crossing on two independent documents, which is what keeps the parity
/// evidence from resting on one publisher's spelling of it.
const STRAPI_REST_API: Corpus = Corpus {
    api: "strapi-rest-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `listennotes`: the Listen Notes podcast API is a second and independent
/// declarer of `style: simple` over an `in: header` scalar
/// (`components.parameters.apiKeyParam`), and the corpus's densest
/// `openapi: 3.1.0` source — 23 paths over 102 component schemas — whose four
/// Response Header Objects reach the Header Object rows through
/// `components.headers` rather than inline.
const LISTENNOTES: Corpus = Corpus {
    api: "listennotes",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `vtex-pricing`: VTEX's Pricing API is the corpus's only source declaring a
/// Header Object's `content` — 22 Response Header Objects carry a media type
/// instead of a `schema` — so this row pins whatever Fern derives from a field
/// crozier models nothing of. It is also the corpus's densest `style: simple`
/// header declarer at 28, beside corpus rows 115 and 120.
const VTEX_PRICING: Corpus = Corpus {
    api: "vtex-pricing",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `aws-importexport`: the AWS Import/Export Service description is the corpus's
/// densest declarer of a parameter redeclared at both the Path Item and the
/// Operation level — each of its six paths declares `Action` and `Version`
/// through `components.parameters`, and each path's `get` and `post` redeclare
/// both `(name, in)` pairs inline, 24 collisions — so this row pins whether Fern
/// honours the specification's rule that the operation-level parameter wins.
const AWS_IMPORTEXPORT: Corpus = Corpus {
    api: "aws-importexport",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openbanking-brasil-directory`: Open Banking Brasil's participant directory is
/// the corpus's only source whose OAuth Flows Object declares more than one flow —
/// `components.securitySchemes.oAuth` names `clientCredentials` (scopes
/// `directory:admin`, `directory:software`) and `authorizationCode` (scope
/// `directory:website`) — and the two scope sets are disjoint, so this row pins
/// which flow Fern reads a scope enum out of where the corpus's other ten Flows
/// Objects each name exactly one.
const OPENBANKING_BRASIL_DIRECTORY: Corpus = Corpus {
    api: "openbanking-brasil-directory",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `api-openverse-org`: the Openverse media-search API is the corpus's first
/// golden-bearing declarer of an operation-level optional security requirement —
/// six Operation Objects whose `security` array holds `{}` — so this row pins
/// whether an operation that opts authentication out still reaches the generated
/// client's constructor.
const API_OPENVERSE_ORG: Corpus = Corpus {
    api: "api-openverse-org",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `discord-com`: Discord's API v10 is the corpus's second declarer of an
/// operation-level optional security requirement (22 `{}` requirements) and its
/// second whose OAuth Flows Object declares more than one flow — three, whose
/// scope sets differ pairwise — so one `openapi: 3.1.0` document witnesses both
/// of this batch's shapes beside corpus rows 123 and 124's separate ones.
const DISCORD_COM: Corpus = Corpus {
    api: "discord-com",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `braintrust-dev`: the Braintrust API is the corpus's densest declarer of an
/// operation-level optional security requirement — 148 Operation Objects whose
/// `security` array holds `{}` — against the single `bearerAuth` scheme Fern's
/// importer supports, so it witnesses corpus row 124's shape at 25 times the
/// density on an independent publisher.
const BRAINTRUST_DEV: Corpus = Corpus {
    api: "braintrust-dev",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `agco-ats`: AGCO's Advanced Technical Support API is the corpus's first source
/// that collides with itself. Its Paths Object declares
/// `/api/v2/Releases/{ReleaseId}` beside `/api/v2/Releases/{releaseId}`, two keys
/// crozier's own `naming::field_name` normalizes to one
/// `/api/v2/Releases/{release_id}`; and 22 of its Operation Objects share 11
/// `operationId` values, each written exactly twice. The golden's raw clients say
/// what Fern does with each: it keeps both colliding routes (`getrelease` over
/// `release_id`, `putcontentdefinition` over `release_id_`), and it drops the
/// *first* declaration of every duplicated `operationId`, so 269 of the document's
/// 280 operations reach the client.
const AGCO_ATS: Corpus = Corpus {
    api: "agco-ats",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `torrentarr`: the Torrentarr automation API is the corpus's only source
/// declaring a media type range other than `*/*` — six `200` responses keyed on
/// `image/*` over `{type: string, format: binary}`, which Fern emits as streamed
/// `typing.Iterator[bytes]` methods — and its second declarer of
/// normalized-equivalent path templates, where all four colliding operations
/// survive as two methods per normalized route.
const TORRENTARR: Corpus = Corpus {
    api: "torrentarr",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `komga`: the Komga comics server's own API is the corpus's second declarer of
/// a media type range other than `*/*` — one `image/*` `default` response over
/// `svix-webhooks`: the Svix API is the corpus's second declarer of a duplicated
/// `operationId` — `GET /api/v1/health` and `HEAD /api/v1/health` both carry
/// `v1.health.get` — where the two operations differ only in HTTP method.
const SVIX_WEBHOOKS: Corpus = Corpus {
    api: "svix-webhooks",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `webflow-v2`: Webflow's Data API v2 is the corpus's third declarer of a
/// duplicated `operationId` and the one where Fern's answer differs — both
/// `komga`: the Komga comics server's own API is the corpus's second declarer of
/// a media type range other than `*/*` — one `image/*` `default` response over
/// `{type: string, format: binary}`, against corpus row 127's six and on the same
/// response side — so the two goldens pin the range on an independent publisher
/// each. Registered with the measured `unmatched` set below rather than at full
/// parity; `tests/fixtures/CORPUS.md`'s batch 14 records what each entry is.
const KOMGA: Corpus = Corpus {
    api: "komga",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[
        "reference.md",
        "src/fern/book_pages/client.py",
        "src/fern/book_pages/raw_client.py",
        "src/fern/book_poster/client.py",
        "src/fern/book_poster/raw_client.py",
        "src/fern/client_settings/client.py",
        "src/fern/collection_poster/client.py",
        "src/fern/collection_poster/raw_client.py",
        "src/fern/duplicate_pages/client.py",
        "src/fern/duplicate_pages/raw_client.py",
        "src/fern/readlist_poster/client.py",
        "src/fern/readlist_poster/raw_client.py",
        "src/fern/series_poster/client.py",
        "src/fern/series_poster/raw_client.py",
        "src/fern/types/search_operator_boolean.py",
        "src/fern/types/search_operator_date.py",
    ],
};

/// `short-io`: the Short.io link API is the corpus's third declarer of two path
/// templates that normalize to one — `/links/{link_id}` beside `/links/{linkId}`,
/// both `GET` — and the first whose colliding pair shares an HTTP method.
/// Registered with the measured `unmatched` set below rather than at full parity.
const SHORT_IO: Corpus = Corpus {
    api: "short-io",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[
        "reference.md",
        "src/fern/__init__.py",
        "src/fern/link_management/__init__.py",
        "src/fern/link_management/client.py",
        "src/fern/link_management/types/__init__.py",
        "src/fern/link_management/types/post_links_bulk_request_links_item_created_at.py",
        "src/fern/link_management/types/post_links_bulk_request_links_item_expires_at.py",
        "src/fern/link_management/types/post_links_bulk_request_links_item_ttl.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_expires_at.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_redirect_type.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_source.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_split_urlv2item.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_ttl.py",
        "src/fern/link_management/types/post_links_duplicate_link_id_response_user.py",
        "src/fern/link_management/types/post_links_examples_response_links_item.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_expires_at.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_redirect_type.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_source.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_split_urlv2item.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_ttl.py",
        "src/fern/link_management/types/post_links_examples_response_links_item_user.py",
        "src/fern/link_management/types/post_links_link_id_request_created_at.py",
        "src/fern/link_management/types/post_links_link_id_request_expires_at.py",
        "src/fern/link_management/types/post_links_link_id_request_ttl.py",
        "src/fern/link_management/types/post_links_link_id_response_expires_at.py",
        "src/fern/link_management/types/post_links_link_id_response_ttl.py",
        "src/fern/link_management/types/post_links_public_request_created_at.py",
        "src/fern/link_management/types/post_links_public_request_expires_at.py",
        "src/fern/link_management/types/post_links_public_request_ttl.py",
        "src/fern/link_management/types/post_links_public_response.py",
        "src/fern/link_management/types/post_links_public_response_expires_at.py",
        "src/fern/link_management/types/post_links_public_response_redirect_type.py",
        "src/fern/link_management/types/post_links_public_response_source.py",
        "src/fern/link_management/types/post_links_public_response_split_urlv2item.py",
        "src/fern/link_management/types/post_links_public_response_ttl.py",
        "src/fern/link_management/types/post_links_public_response_user.py",
        "src/fern/link_management/types/post_links_request_created_at.py",
        "src/fern/link_management/types/post_links_request_expires_at.py",
        "src/fern/link_management/types/post_links_request_ttl.py",
        "src/fern/link_management/types/post_links_response.py",
        "src/fern/link_management/types/post_links_response_expires_at.py",
        "src/fern/link_management/types/post_links_response_redirect_type.py",
        "src/fern/link_management/types/post_links_response_source.py",
        "src/fern/link_management/types/post_links_response_split_urlv2item.py",
        "src/fern/link_management/types/post_links_response_ttl.py",
        "src/fern/link_management/types/post_links_response_user.py",
        "src/fern/link_queries/types/get_api_links_response_links_item_expires_at.py",
        "src/fern/link_queries/types/get_api_links_response_links_item_ttl.py",
        "src/fern/link_queries/types/get_links_expand_response_expires_at.py",
        "src/fern/link_queries/types/get_links_expand_response_ttl.py",
        "src/fern/link_queries/types/get_links_link_id_response_expires_at.py",
        "src/fern/link_queries/types/get_links_link_id_response_ttl.py",
        "src/fern/types/bad_request_error_body.py",
        "src/fern/types/conflict_error_body.py",
        "src/fern/types/forbidden_error_body.py",
        "src/fern/types/internal_server_error_body.py",
        "src/fern/types/not_found_error_body.py",
        "src/fern/types/payment_required_error_body.py",
        "src/fern/types/unauthorized_error_body.py",
    ],
};

/// `webflow-v2`: Webflow's Data API v2 is the corpus's third declarer of a
/// duplicated `operationId` and the one where Fern's answer differs — both
/// `list-submissions` operations survive, under different sub-clients sharing one
/// response type, where corpus rows 128 and 129 each lose an operation.
/// Registered with the measured `unmatched` set below rather than at full parity.
const WEBFLOW_V2: Corpus = Corpus {
    api: "webflow-v2",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[
        "README.md",
        "reference.md",
        "src/fern/__init__.py",
        "src/fern/analyze/__init__.py",
        "src/fern/analyze/reports/__init__.py",
        "src/fern/analyze/reports/client.py",
        "src/fern/analyze/reports/raw_client.py",
        "src/fern/analyze/reports/types/__init__.py",
        "src/fern/analyze/reports/types/top_pages_reports_request_sort_by.py",
        "src/fern/assets/raw_client.py",
        "src/fern/client.py",
        "src/fern/collections/__init__.py",
        "src/fern/collections/client.py",
        "src/fern/collections/fields/__init__.py",
        "src/fern/collections/fields/client.py",
        "src/fern/collections/fields/raw_client.py",
        "src/fern/collections/fields/types/__init__.py",
        "src/fern/collections/fields/types/create_fields_request_body.py",
        "src/fern/collections/fields/types/create_fields_response.py",
        "src/fern/collections/fields/types/option_field.py",
        "src/fern/collections/fields/types/option_field_metadata.py",
        "src/fern/collections/fields/types/option_field_metadata_options_item.py",
        "src/fern/collections/fields/types/option_field_type.py",
        "src/fern/collections/fields/types/reference_field.py",
        "src/fern/collections/fields/types/reference_field_metadata.py",
        "src/fern/collections/fields/types/reference_field_type.py",
        "src/fern/collections/fields/types/static_field.py",
        "src/fern/collections/fields/types/static_field_type.py",
        "src/fern/collections/fields/types/update_fields_response_validations_additional_properties.py",
        "src/fern/collections/items/__init__.py",
        "src/fern/collections/items/client.py",
        "src/fern/collections/items/raw_client.py",
        "src/fern/collections/items/types/__init__.py",
        "src/fern/collections/items/types/create_item_items_request_body.py",
        "src/fern/collections/items/types/create_item_live_items_request_body.py",
        "src/fern/collections/items/types/create_items_items_request_field_data.py",
        "src/fern/collections/items/types/item_i_ds.py",
        "src/fern/collections/items/types/item_i_ds_with_locales.py",
        "src/fern/collections/items/types/item_i_ds_with_locales_items_item.py",
        "src/fern/collections/items/types/list_items_items_request_filter_value.py",
        "src/fern/collections/items/types/list_items_items_request_filter_value_exists.py",
        "src/fern/collections/items/types/list_items_items_request_filter_value_in.py",
        "src/fern/collections/items/types/list_items_items_request_filter_value_nin.py",
        "src/fern/collections/items/types/list_items_items_request_sort_value.py",
        "src/fern/collections/items/types/list_items_live_items_request_filter_value.py",
        "src/fern/collections/items/types/list_items_live_items_request_filter_value_exists.py",
        "src/fern/collections/items/types/list_items_live_items_request_filter_value_in.py",
        "src/fern/collections/items/types/list_items_live_items_request_filter_value_nin.py",
        "src/fern/collections/items/types/list_items_live_items_request_sort_value.py",
        "src/fern/collections/items/types/multiple_cms_items_item.py",
        "src/fern/collections/items/types/multiple_items.py",
        "src/fern/collections/items/types/multiple_items_items_item.py",
        "src/fern/collections/items/types/multiple_items_items_item_field_data.py",
        "src/fern/collections/items/types/multiple_live_items.py",
        "src/fern/collections/items/types/multiple_live_items_items_item.py",
        "src/fern/collections/items/types/multiple_live_items_items_item_field_data.py",
        "src/fern/collections/items/types/publish_item_items_request_body.py",
        "src/fern/collections/items/types/single_cms_item.py",
        "src/fern/collections/items/types/single_item.py",
        "src/fern/collections/items/types/single_item_field_data.py",
        "src/fern/collections/items/types/single_live_item.py",
        "src/fern/collections/items/types/single_live_item_field_data.py",
        "src/fern/collections/raw_client.py",
        "src/fern/collections/types/__init__.py",
        "src/fern/collections/types/create_collections_request_fields_item.py",
        "src/fern/collections/types/create_collections_response_fields_item_validations_additional_properties.py",
        "src/fern/collections/types/get_collections_response_fields_item_validations_additional_properties.py",
        "src/fern/collections/types/option_field.py",
        "src/fern/collections/types/option_field_metadata.py",
        "src/fern/collections/types/option_field_metadata_options_item.py",
        "src/fern/collections/types/option_field_type.py",
        "src/fern/collections/types/patch_collections_response_fields_item_validations_additional_properties.py",
        "src/fern/collections/types/reference_field.py",
        "src/fern/collections/types/reference_field_metadata.py",
        "src/fern/collections/types/reference_field_type.py",
        "src/fern/collections/types/static_field.py",
        "src/fern/collections/types/static_field_type.py",
        "src/fern/comments/__init__.py",
        "src/fern/comments/types/__init__.py",
        "src/fern/comments/types/comment_created_payload.py",
        "src/fern/comments/types/comment_created_payload_payload.py",
        "src/fern/comments/types/comment_created_payload_payload_author.py",
        "src/fern/comments/types/comment_created_payload_payload_mentioned_users_item.py",
        "src/fern/comments/types/comment_created_payload_payload_type.py",
        "src/fern/components/__init__.py",
        "src/fern/components/client.py",
        "src/fern/components/raw_client.py",
        "src/fern/components/types/__init__.py",
        "src/fern/components/types/get_content_components_response_nodes_item_component_instance_property_overrides_item.py",
        "src/fern/components/types/update_content_components_request_nodes_item.py",
        "src/fern/components/types/update_content_components_request_nodes_item_choices.py",
        "src/fern/components/types/update_content_components_request_nodes_item_choices_choices_item.py",
        "src/fern/components/types/update_content_components_request_nodes_item_five.py",
        "src/fern/components/types/update_content_components_request_nodes_item_placeholder.py",
        "src/fern/components/types/update_content_components_request_nodes_item_property_overrides.py",
        "src/fern/components/types/update_content_components_request_nodes_item_property_overrides_property_overrides_item.py",
        "src/fern/components/types/update_content_components_request_nodes_item_text.py",
        "src/fern/components/types/update_content_components_request_nodes_item_waiting_text.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/custom_fonts/raw_client.py",
        "src/fern/ecommerce/raw_client.py",
        "src/fern/environment.py",
        "src/fern/forms/__init__.py",
        "src/fern/forms/client.py",
        "src/fern/forms/raw_client.py",
        "src/fern/forms/types/__init__.py",
        "src/fern/forms/types/form_submission_payload.py",
        "src/fern/forms/types/form_submission_payload_payload.py",
        "src/fern/forms/types/form_submission_payload_payload_schema_item.py",
        "src/fern/forms/types/form_submission_payload_payload_schema_item_field_type.py",
        "src/fern/forms/types/list_submissions_forms_response.py",
        "src/fern/inventory/__init__.py",
        "src/fern/inventory/raw_client.py",
        "src/fern/inventory/types/__init__.py",
        "src/fern/inventory/types/ecomm_inventory_changed_payload.py",
        "src/fern/inventory/types/ecomm_inventory_changed_payload_payload.py",
        "src/fern/inventory/types/ecomm_inventory_changed_payload_payload_inventory_type.py",
        "src/fern/inventory/types/ecomm_inventory_changed_payload_trigger_type.py",
        "src/fern/items/__init__.py",
        "src/fern/items/types/__init__.py",
        "src/fern/items/types/collection_item_changed_payload.py",
        "src/fern/items/types/collection_item_changed_payload_payload.py",
        "src/fern/items/types/collection_item_changed_payload_payload_field_data.py",
        "src/fern/items/types/collection_item_changed_payload_trigger_type.py",
        "src/fern/items/types/collection_item_created_payload.py",
        "src/fern/items/types/collection_item_created_payload_payload.py",
        "src/fern/items/types/collection_item_created_payload_payload_field_data.py",
        "src/fern/items/types/collection_item_created_payload_trigger_type.py",
        "src/fern/items/types/collection_item_deleted_payload.py",
        "src/fern/items/types/collection_item_deleted_payload_payload.py",
        "src/fern/items/types/collection_item_deleted_payload_payload_field_data.py",
        "src/fern/items/types/collection_item_published_payload.py",
        "src/fern/items/types/collection_item_published_payload_payload.py",
        "src/fern/items/types/collection_item_published_payload_payload_field_data.py",
        "src/fern/items/types/collection_item_unpublished_payload.py",
        "src/fern/items/types/collection_item_unpublished_payload_payload.py",
        "src/fern/items/types/collection_item_unpublished_payload_payload_field_data.py",
        "src/fern/orders/__init__.py",
        "src/fern/orders/raw_client.py",
        "src/fern/orders/types/__init__.py",
        "src/fern/orders/types/ecomm_new_order_payload.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_all_addresses_item.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_all_addresses_item_japan_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_all_addresses_item_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_application_fee.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_billing_address.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_billing_address_japan_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_billing_address_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_customer_info.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_customer_paid.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_dispute_last_status.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_download_files_item.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_metadata.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_net_amount.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_paypal_details.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item_row_total.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item_variant_image.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item_variant_image_file.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item_variant_image_file_variants_item.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_purchased_items_item_variant_price.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_shipping_address.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_shipping_address_japan_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_shipping_address_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_status.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_stripe_card.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_stripe_card_brand.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_stripe_card_expires.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_stripe_details.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals_extras_item.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals_extras_item_price.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals_extras_item_type.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals_subtotal.py",
        "src/fern/orders/types/ecomm_new_order_payload_payload_totals_total.py",
        "src/fern/orders/types/ecomm_order_changed_payload.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_all_addresses_item.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_all_addresses_item_japan_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_all_addresses_item_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_application_fee.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_billing_address.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_billing_address_japan_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_billing_address_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_customer_info.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_customer_paid.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_dispute_last_status.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_download_files_item.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_metadata.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_net_amount.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_paypal_details.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item_row_total.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item_variant_image.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file_variants_item.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_purchased_items_item_variant_price.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_shipping_address.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_shipping_address_japan_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_shipping_address_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_status.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_stripe_card.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_stripe_card_brand.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_stripe_card_expires.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_stripe_details.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals_extras_item.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals_extras_item_price.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals_extras_item_type.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals_subtotal.py",
        "src/fern/orders/types/ecomm_order_changed_payload_payload_totals_total.py",
        "src/fern/pages/__init__.py",
        "src/fern/pages/client.py",
        "src/fern/pages/raw_client.py",
        "src/fern/pages/scripts/client.py",
        "src/fern/pages/scripts/raw_client.py",
        "src/fern/pages/scripts/types/get_custom_code_scripts_response.py",
        "src/fern/pages/scripts/types/get_custom_code_scripts_response_scripts_item.py",
        "src/fern/pages/scripts/types/upsert_custom_code_scripts_request_scripts_item.py",
        "src/fern/pages/scripts/types/upsert_custom_code_scripts_response.py",
        "src/fern/pages/scripts/types/upsert_custom_code_scripts_response_scripts_item.py",
        "src/fern/pages/types/__init__.py",
        "src/fern/pages/types/get_content_pages_response_nodes_item_component_instance_property_overrides_item.py",
        "src/fern/pages/types/page_created_payload.py",
        "src/fern/pages/types/page_created_payload_payload.py",
        "src/fern/pages/types/page_deleted_payload.py",
        "src/fern/pages/types/page_deleted_payload_payload.py",
        "src/fern/pages/types/page_metadata_updated_payload.py",
        "src/fern/pages/types/page_metadata_updated_payload_payload.py",
        "src/fern/pages/types/update_static_content_request_nodes_item.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_choices.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_choices_choices_item.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_five.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_placeholder.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_property_overrides.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_property_overrides_property_overrides_item.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_text.py",
        "src/fern/pages/types/update_static_content_request_nodes_item_waiting_text.py",
        "src/fern/products/client.py",
        "src/fern/products/raw_client.py",
        "src/fern/products/types/create_products_request_product.py",
        "src/fern/scripts/raw_client.py",
        "src/fern/sites/__init__.py",
        "src/fern/sites/activity_logs/raw_client.py",
        "src/fern/sites/comments/raw_client.py",
        "src/fern/sites/forms/raw_client.py",
        "src/fern/sites/google_tag/raw_client.py",
        "src/fern/sites/plans/raw_client.py",
        "src/fern/sites/raw_client.py",
        "src/fern/sites/redirects/client.py",
        "src/fern/sites/redirects/raw_client.py",
        "src/fern/sites/robots_txt/client.py",
        "src/fern/sites/robots_txt/raw_client.py",
        "src/fern/sites/scripts/client.py",
        "src/fern/sites/scripts/raw_client.py",
        "src/fern/sites/types/__init__.py",
        "src/fern/sites/types/site_publish_payload.py",
        "src/fern/sites/types/site_publish_payload_payload.py",
        "src/fern/sites/types/site_publish_payload_payload_publish_scope.py",
        "src/fern/sites/well_known/raw_client.py",
        "src/fern/token/raw_client.py",
        "src/fern/types/__init__.py",
        "src/fern/webhooks/client.py",
        "src/fern/webhooks/raw_client.py",
        "src/fern/workspaces/__init__.py",
        "src/fern/workspaces/audit_logs/__init__.py",
        "src/fern/workspaces/audit_logs/raw_client.py",
        "src/fern/workspaces/audit_logs/types/__init__.py",
        "src/fern/workspaces/audit_logs/types/custom_role.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_custom_role.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_custom_role_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_site_membership.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_site_membership_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_user_access.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_user_access_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting.py",
        "src/fern/workspaces/audit_logs/types/get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting_event_sub_type.py",
        "src/fern/workspaces/audit_logs/types/setting_change.py",
        "src/fern/workspaces/audit_logs/types/setting_change_method.py",
        "src/fern/workspaces/audit_logs/types/setting_change_setting.py",
        "src/fern/workspaces/audit_logs/types/site_membership.py",
        "src/fern/workspaces/audit_logs/types/site_membership_granular_access.py",
        "src/fern/workspaces/audit_logs/types/site_membership_granular_access_type.py",
        "src/fern/workspaces/audit_logs/types/site_membership_method.py",
        "src/fern/workspaces/audit_logs/types/site_membership_site.py",
        "src/fern/workspaces/audit_logs/types/site_membership_target_user.py",
        "src/fern/workspaces/audit_logs/types/site_membership_user_type.py",
        "src/fern/workspaces/audit_logs/types/user_access.py",
        "src/fern/workspaces/audit_logs/types/user_access_method.py",
        "src/fern/workspaces/audit_logs/types/workspace_invitation.py",
        "src/fern/workspaces/audit_logs/types/workspace_invitation_method.py",
        "src/fern/workspaces/audit_logs/types/workspace_invitation_target_user.py",
        "src/fern/workspaces/audit_logs/types/workspace_invitation_target_users_item.py",
        "src/fern/workspaces/audit_logs/types/workspace_invitation_user_type.py",
        "src/fern/workspaces/audit_logs/types/workspace_membership.py",
        "src/fern/workspaces/audit_logs/types/workspace_membership_method.py",
        "src/fern/workspaces/audit_logs/types/workspace_membership_target_user.py",
        "src/fern/workspaces/audit_logs/types/workspace_membership_user_type.py",
    ],
};

/// `loris-dataquery`: the LORIS Data Query Tool API is the corpus's only source
/// declaring `style: spaceDelimited` over a query parameter — `share` and `star`
/// on `PATCH /queries/{QueryID}`, each over `{type: boolean}` — and its densest
/// declarer of `style: pipeDelimited` over one, at four. Both are the
/// specification's array-only serialisations declared over a *scalar* schema, so
/// the golden says what Fern emits for a style the schema cannot satisfy.
const LORIS_DATAQUERY: Corpus = Corpus {
    api: "loris-dataquery",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `sftpgo`: SFTPGo's own administration API is the corpus's densest declarer of
/// a media type range other than `*/*` — ten content-map keys over five distinct
/// ranges — and the first to declare one on the *request* side, where rows 127
/// and 130 declare theirs on responses. It is also the corpus's second declarer
/// of a parameter redeclared at both Path Item and Operation level.
const SFTPGO: Corpus = Corpus {
    api: "sftpgo",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `googleapis-servicebroker`: Google's Service Broker API is the corpus's fourth
/// declarer of two path templates that normalize to one, and the first whose two
/// colliding groups nest — `…/service_instances/{instanceId}` beside
/// `…/{instance_id}`, and one segment deeper `…/service_bindings/{bindingId}`
/// beside `…/{binding_id}`.
const GOOGLEAPIS_SERVICEBROKER: Corpus = Corpus {
    api: "googleapis-servicebroker",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `audiobookshelf`: the Audiobookshelf server's own API is the corpus's fourth
/// declarer of a media type range other than `*/*`, and the only source declaring
/// one beside two concrete media types of its own type — the `200` of
/// `GET /api/authors/{id}/image` is keyed `image/webp`, `image/jpeg` and
/// `image/*`, all three over `{type: string, format: binary}`.
const AUDIOBOOKSHELF: Corpus = Corpus {
    api: "audiobookshelf",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// PayPal's catalog API declares sole-member `anyOf` error detail items.
const PAYPAL_CATALOG_PRODUCTS: Corpus = Corpus {
    api: "paypal-catalog-products",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `steaminputdb`: the SteamInputDB API is the corpus's first source whose only
/// security scheme is an `oauth2` Security Scheme Object carrying a stray
/// `scheme: OAuth` and `in: query` beside its flows, and its `servers` declare a
/// localhost development URL ahead of the live one.
const STEAMINPUTDB: Corpus = Corpus {
    api: "steaminputdb",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `exa-gate`: the Exa Gate API declares both `423` and `426` responses, pinning
/// Fern's `LockedError` and `UpgradeRequiredError` names for those statuses.
const EXA_GATE: Corpus = Corpus {
    api: "exa-gate",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `prometheus-x-edge-computing`: the Prometheus-X edge-computing API declares
/// both `408` and `412` responses, pinning Fern's `RequestTimeoutError` and
/// `PreconditionFailedError` names for those statuses.
const PROMETHEUS_X_EDGE_COMPUTING: Corpus = Corpus {
    api: "prometheus-x-edge-computing",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `withsecure-gdpr-subject-rights`: every operation of WithSecure's GDPR
/// subject-rights API declares a `451` response, pinning Fern's
/// `UnavailableForLegalReasonsError` name for that status.
const WITHSECURE_GDPR_SUBJECT_RIGHTS: Corpus = Corpus {
    api: "withsecure-gdpr-subject-rights",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `kytos-sdntrace-cp`: both operations of the Kytos SDN tracing API declare a
/// `424` response, so this row is the first golden to pin Fern's
/// `FailedDependencyError` name for that status.
const KYTOS_SDNTRACE_CP: Corpus = Corpus {
    api: "kytos-sdntrace-cp",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

// Issue #63: `extra_fields: forbid` — the one `--extra-fields` value no golden
// pinned. A generator setting is not expressible in an OpenAPI document, so this
// row reuses `eos.local`'s already registered source (CORPUS.md row 43) under a
// second corpus name whose `fern-generator-config.txt` entry carries
// `extra_fields: forbid`. Its four models pin both halves of the pydantic
// asymmetry `pydantic-extra-fields` documents: the v2 `model_config` spells
// `extra="forbid"` out, and the v1 `Config` writes `pydantic.Extra.forbid`.
const EOS_EXTRA_FIELDS_FORBID: Corpus = Corpus {
    api: "eos.local-extra-fields-forbid",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: Some("forbid"),
    unmatched: &[],
};

/// `med-anvisa-price`: the Anvisa medication-price API spells its filter enum
/// values and its `Medication` property names with the same Latin-1 accented
/// words, so one document pins both halves of Fern's asymmetry — the accent is
/// folded away in an enum member name (`SUBSTANCIA = "SUBSTÂNCIA"`) and dropped
/// as a separator in a property identifier (`laborat_rio`, aliased back to
/// `LABORATÓRIO`).
const MED_ANVISA_PRICE: Corpus = Corpus {
    api: "med-anvisa-price",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `sac-backend`: the SAC request-classification API witnesses the accent-
/// dropping property rule from a second project and a second language — its
/// `tamaño` page-size field becomes `tama_o`, with the accented wire name kept
/// as the serialization alias.
const SAC_BACKEND: Corpus = Corpus {
    api: "sac-backend",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// FOLIO's token API keeps six component schemas in sibling JSON files.
const FOLIO_MOD_AUTHTOKEN: Corpus = Corpus {
    api: "folio-mod-authtoken",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Raybot keeps Path Items, parameters, and schemas in sibling documents.
const RAYBOT: Corpus = Corpus {
    api: "raybot",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Prisma Cloud Alerts annotates `$ref`s to composed and `oneOf` targets.
const PALOALTO_CSPM_ALERTS: Corpus = Corpus {
    api: "paloalto-cspm-alerts",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Prisma Cloud Reports annotates `$ref`s to `oneOf` targets.
const PALOALTO_CSPM_REPORTS: Corpus = Corpus {
    api: "paloalto-cspm-reports",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Prisma Cloud Search Manager annotates `$ref`s to `oneOf` targets.
const PALOALTO_CSPM_SEARCH_MANAGER: Corpus = Corpus {
    api: "paloalto-cspm-search-manager",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// ThriveCart points `$ref`s under an undeclared component head.
const THRIVECART: Corpus = Corpus {
    api: "thrivecart",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// A later TrueForge revision annotates `$ref`s to closed-object targets.
const TRUEFOUNDRY_TRUEFORGE_5ADDE28: Corpus = Corpus {
    api: "truefoundry-trueforge-5adde28",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Fergus declares `anyOf` array variants with struct items.
const FERGUS: Corpus = Corpus {
    api: "fergus",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Groupe PSA Connected Car annotates `$ref`s to composed targets.
const GROUPE_PSA: Corpus = Corpus {
    api: "groupe-psa",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Timely declares `anyOf` array variants with struct items.
const TIMELYAPP: Corpus = Corpus {
    api: "timelyapp",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// NextGen points `$ref`s under an undeclared component head and names schemas with non-identifiers.
const NEXTGEN: Corpus = Corpus {
    api: "nextgen",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Auto Agent Protocol walks a `$ref` pointer through an unnamed segment.
const AUTO_AGENT_PROTOCOL: Corpus = Corpus {
    api: "auto-agent-protocol",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Skool points `$ref`s under an undeclared component head.
const SKOOL: Corpus = Corpus {
    api: "skool",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Spendesk API — the jentic-public-apis aggregation's copy; a `$ref` under an undeclared component head.
const SPENDESK: Corpus = Corpus {
    api: "spendesk",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Billie Direct API — the jentic-public-apis aggregation's copy; `$ref`s under an undeclared component head.
const BILLIE: Corpus = Corpus {
    api: "billie",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Alma Payments API (France) — the jentic-public-apis aggregation's copy; `$ref`s under an undeclared component head.
const ALMA_FRANCE: Corpus = Corpus {
    api: "alma-france",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Outreach API — the jentic-public-apis aggregation's copy; `$ref`s under an undeclared component head.
const OUTREACH: Corpus = Corpus {
    api: "outreach",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Tally API — the jentic-public-apis aggregation's copy; `$ref`s under an undeclared component head.
const TALLY: Corpus = Corpus {
    api: "tally",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Billie Direct API — jentic's import entry, row 156's document with its keys reordered.
const BILLIE_ENTRY: Corpus = Corpus {
    api: "billie-entry",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Skool API — jentic's import entry, row 154's document with its keys reordered.
const SKOOL_ENTRY: Corpus = Corpus {
    api: "skool-entry",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Timely API — jentic's import entry, row 151's document with its keys reordered.
const TIMELYAPP_ENTRY: Corpus = Corpus {
    api: "timelyapp-entry",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Cradl API — the jentic-public-apis aggregation's copy; an `anyOf` array variant whose item is a struct.
const CRADL: Corpus = Corpus {
    api: "cradl",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Zulip API — the publisher's own description at a pinned commit.
const ZULIP: Corpus = Corpus {
    api: "zulip",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Zulip API — the jentic-public-apis aggregation's JSON import, a different revision of row 164's document.
const ZULIP_JENTIC: Corpus = Corpus {
    api: "zulip-jentic",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Zulip API — jentic's import entry, row 165's document with its keys reordered.
const ZULIP_JENTIC_ENTRY: Corpus = Corpus {
    api: "zulip-jentic-entry",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Milvus RESTful API v2 (the v2.3.x reference) — corpus row 168, the publisher's own description.
const MILVUS_RESTFUL_V2_3: Corpus = Corpus {
    api: "milvus-restful-v2-3",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Milvus RESTful API (the v2.4.x reference) — corpus row 169, the publisher's own description.
const MILVUS_RESTFUL_V2_4: Corpus = Corpus {
    api: "milvus-restful-v2-4",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Ramu Shogi API contract — corpus row 170, the publisher's own description.
const RAMU_SHOGI: Corpus = Corpus {
    api: "ramu-shogi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// LangChain Agent Protocol — corpus row 172, the publisher's own description.
const LANGCHAIN_AGENT_PROTOCOL: Corpus = Corpus {
    api: "langchain-agent-protocol",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// HSE REST API — corpus row 173, the publisher's own description.
const HSE: Corpus = Corpus {
    api: "hse",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Milvus vector operations (apifox export) — corpus row 174, the publisher's own description.
const MILVUS_VECTOR_OPERATIONS: Corpus = Corpus {
    api: "milvus-vector-operations",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Mistle control-plane internal API v1 — corpus row 176, the publisher's own description.
const MISTLE_CONTROL_PLANE: Corpus = Corpus {
    api: "mistle-control-plane",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// o²S²PARC payments service — corpus row 177, the publisher's own description.
const OSPARC_PAYMENTS: Corpus = Corpus {
    api: "osparc-payments",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// HuaTuo node API v1 — corpus row 178, the publisher's own description.
const HUATUO_NODE: Corpus = Corpus {
    api: "huatuo-node",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// HuaTuo server API v1 — corpus row 179, the publisher's own description.
const HUATUO_SERVER: Corpus = Corpus {
    api: "huatuo-server",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// HuaTuo node API v1 as its repository authors it — corpus row 309, the
/// two-file tree row 178 is bundled from. Its `BearerAuth` names the scheme
/// `../components.yaml` declares, so its bearer credential witnesses a security
/// scheme resolved from another document.
const HUATUO_NODE_TREE: Corpus = Corpus {
    api: "huatuo-node-tree",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Lootlog's Battle Log API — corpus row 317, the publisher's own description.
/// Its `POST /internal/delete-user-data` takes an optional header spelled
/// `authorization` beside an `http: bearer` scheme, which Fern keeps as a method
/// argument because only the exact spelling `Authorization` is the credential's.
const LOOTLOG_BATTLELOG: Corpus = Corpus {
    api: "lootlog-battlelog",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Ego's microservices API — corpus row 318, the publisher's own description.
/// Its paginated listings' query `offset` and `limit` are `anyOf: [integer, $ref
/// Empty]`, a union naming a component string enum with no array member, which
/// Fern sends raw.
const EGO_MICROSERVICES: Corpus = Corpus {
    api: "ego-microservices",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// VisKit Studio API — corpus row 167, the publisher's own description.
const VISKIT_STUDIO: Corpus = Corpus {
    api: "viskit-studio",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// CloudPDF contract API — corpus row 171, the publisher's own description.
const EMBEDPDF_CLOUDPDF: Corpus = Corpus {
    api: "embedpdf-cloudpdf",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// NPQ registration API v3 — corpus row 175, the publisher's own description.
const NPQ_REGISTRATION: Corpus = Corpus {
    api: "npq-registration",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `sim-logs`: corpus row 216, Sim API v2 — Logs. It declares
/// `anyof-array-variant-closed-object-item`, a row already `golden`.
const SIM_LOGS: Corpus = Corpus {
    api: "sim-logs",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `sim-tables`: corpus row 217, Sim Tables API v2. It declares
/// `anyof-array-variant-closed-object-item`, a row already `golden`.
const SIM_TABLES: Corpus = Corpus {
    api: "sim-tables",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `vellum-gateway`: corpus row 218, the Vellum Gateway API. It declares
/// `anyof-array-variant-closed-object-item`, a row already `golden`.
const VELLUM_GATEWAY: Corpus = Corpus {
    api: "vellum-gateway",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `dot-ai`: corpus row 219, the DevOps AI Toolkit REST API. It declares
/// `anyof-array-variant-closed-object-item`, a row already `golden`.
const DOT_AI: Corpus = Corpus {
    api: "dot-ai",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `paloalto-code-technologies`: corpus row 220, the Prisma Cloud Technologies
/// API. It declares `anyof-array-variant-struct-item`, a row already `golden`.
const PALOALTO_CODE_TECHNOLOGIES: Corpus = Corpus {
    api: "paloalto-code-technologies",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `marimo-plugins`: corpus row 221, marimo's plugin contracts. It declares
/// `anyof-array-variant-struct-item`, a row already `golden`.
const MARIMO_PLUGINS: Corpus = Corpus {
    api: "marimo-plugins",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `otoroshi`: corpus row 222, the Otoroshi Admin API as its repository pins
/// it. It declares `ref-pointer-undeclared-component-head`, a row already
/// `golden`.
const OTOROSHI: Corpus = Corpus {
    api: "otoroshi",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `standrig`: corpus row 231, the StandRig Modeling Tools core API from
/// sayaka-aiart/StandRig, whose `anyOf` alternatives include a string `const`
const STANDRIG: Corpus = Corpus {
    api: "standrig",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `mockserver`: corpus row 232, MockServer's own control-plane API description
/// from mock-server/mockserver-monorepo, whose draft-04 meta-schema `$ref` is
/// pinned
const MOCKSERVER: Corpus = Corpus {
    api: "mockserver",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `ideaconsult-enanomapper`: corpus row 301, the eNanoMapper database API 4.0.0
/// as APIs.guru pins it, whose operations declare `externalDocs`
const IDEACONSULT_ENANOMAPPER: Corpus = Corpus {
    api: "ideaconsult-enanomapper",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openaire-graph`: corpus row 302, the OpenAIRE Graph API 2.0 from
/// jentic/jentic-public-apis, whose schemas declare `xml.attribute`
const OPENAIRE_GRAPH: Corpus = Corpus {
    api: "openaire-graph",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `qredence-fleet-rlm`: corpus row 303, fleet-rlm's own server description
/// from Qredence/fleet-rlm, whose `oneOf` holds a variant that is an `anyOf`
const QREDENCE_FLEET_RLM: Corpus = Corpus {
    api: "qredence-fleet-rlm",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `fiware-context-generator`: corpus row 304, the LiveBuildings data model API
/// from live-buildings/context-generator, whose array item's `oneOf` holds an
/// `anyOf`
const FIWARE_CONTEXT_GENERATOR: Corpus = Corpus {
    api: "fiware-context-generator",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `hasura-metadata`: corpus row 305, Hasura GraphQL Engine's metadata schema
/// from hasura/graphql-engine, whose properties' `oneOf` holds an `anyOf`
const HASURA_METADATA: Corpus = Corpus {
    api: "hasura-metadata",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `zoonk`: corpus row 306, Zoonk's API from zoonk/zoonk, whose `MeDeletion`
/// `oneOf` offers a closed empty object
const ZOONK: Corpus = Corpus {
    api: "zoonk",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `openfoodfacts-taxonomy-editor`: corpus row 310, the Open Food Facts
/// taxonomy editor's API, whose discriminated search-filter members list
/// `readOnly` properties in `required`
const OPENFOODFACTS_TAXONOMY_EDITOR: Corpus = Corpus {
    api: "openfoodfacts-taxonomy-editor",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `qontract-api`: corpus row 311, qontract-reconcile's Qontract API, whose
/// task results' actions are `$ref` members tagging `action_type` with a
/// one-value `enum` that `required` leaves out
const QONTRACT_API: Corpus = Corpus {
    api: "qontract-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `breizhsport-catalogue`: corpus row 313, whose `Article.rating` is declared
/// `type: float` beside two `type: int` properties.
const BREIZHSPORT_CATALOGUE: Corpus = Corpus {
    api: "breizhsport-catalogue",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `protoform-conformance`: corpus row 314, whose `DeleteBook` answers with an
/// inline object closed with `additionalProperties: false` and no `properties`.
const PROTOFORM_CONFORMANCE: Corpus = Corpus {
    api: "protoform-conformance",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `ere-ps-app`: corpus row 315, 48 of whose models reach two or more reference
/// cycles in an order no sort of their members reproduces.
const ERE_PS_APP: Corpus = Corpus {
    api: "ere-ps-app",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `typescript-service-template`: corpus row 316, a TypeScript service
/// template's users API, whose `usersPatch` takes a required query array of
/// `$ref UserID` items and answers JSON, so Fern's worked example passes it
const TYPESCRIPT_SERVICE_TEMPLATE: Corpus = Corpus {
    api: "typescript-service-template",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `oal-example`: corpus row 312, the OAL project's example description,
/// whose `obj3.stuff` property `anyOf` holds an inline `oneOf` member
const OAL_EXAMPLE: Corpus = Corpus {
    api: "oal-example",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// Waylay's query API, corpus row 329: both URL and JSON body keys named
/// `resource` have distinct signature arguments. The body/query departure keeps
/// the body value the caller passed while the query keeps its own value.
const WAYLAY_QUERIES: Corpus = Corpus {
    api: "waylay-queries",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const CONFLUENT_KAFKA_CONNECT: Corpus = Corpus {
    api: "confluent-kafka-connect",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

const NETGSM_SMS: Corpus = Corpus {
    api: "netgsm-sms",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `millenium-falcon-challenge`: corpus row 319, the Millennium Falcon challenge's odds API,
/// whose `POST /odds` posts a FastAPI `Body_odds_odds_post` body nothing else names
const MILLENIUM_FALCON_CHALLENGE: Corpus = Corpus {
    api: "millenium-falcon-challenge",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `maximo-wxo-integration`: corpus row 320, IBM's Maximo integration API, whose OpenAPI 3.0.0
/// success responses are inline `application/json` bodies declaring `{}`
const MAXIMO_WXO_INTEGRATION: Corpus = Corpus {
    api: "maximo-wxo-integration",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `mi-music`: corpus row 321, mi_music's API, with schemaless `text/plain`, `audio/mpeg` and
/// `video/mp4` successes and titled bodies under HTTP Basic security
const MI_MUSIC: Corpus = Corpus {
    api: "mi-music",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `g4brym-download-manager`: corpus row 322, download-manager's API, whose parameterless
/// 3.0 operations post inline arrays titled `Files`
const G4BRYM_DOWNLOAD_MANAGER: Corpus = Corpus {
    api: "g4brym-download-manager",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `opentosca-license-engine`: corpus row 323, the OpenTOSCA license engine's API, with a
/// titled inline string-array body and inline `{}` successes in a 3.0 document
const OPENTOSCA_LICENSE_ENGINE: Corpus = Corpus {
    api: "opentosca-license-engine",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `chat-rest-api`: corpus row 324, chat-rest-api's API, whose error keys `404-message`
/// and `404-file` both name 404 and whose success lists `text/plain` before
/// `application/octet-stream`
const CHAT_REST_API: Corpus = Corpus {
    api: "chat-rest-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `esp32-streamline-bridge`: corpus row 325, the StreamLine bridge API, whose recordings
/// answer a schemaless `audio/wav`
const ESP32_STREAMLINE_BRIDGE: Corpus = Corpus {
    api: "esp32-streamline-bridge",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `cphos-ai-question`: corpus row 326, CPhOS's question-generation API, whose artifact
/// download lists a schemaless `application/pdf` before `text/markdown`
const CPHOS_AI_QUESTION: Corpus = Corpus {
    api: "cphos-ai-question",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `flask-example-heroku`: corpus row 327, a package-name extractor whose one operation
/// declares a JSON request body with no schema
const FLASK_EXAMPLE_HEROKU: Corpus = Corpus {
    api: "flask-example-heroku",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `oip-web-api`: corpus row 328, the Oip service web API, whose parameterless
/// module registration declares an empty `requestBody.description`
const OIP_WEB_API: Corpus = Corpus {
    api: "oip-web-api",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `apideck.com-ecosystem-client-class-name`: corpus row 307, row 13's Ecosystem
/// API under `client_class_name: EcosystemClient` — the class name of its own
/// `ecosystem` resource's sub-client. The root `client.py` imports that
/// sub-client's classes aliased (`ecosystem_client_EcosystemClient`), so the
/// root class it defines does not shadow the `ecosystem` property's type.
const APIDECK_ECOSYSTEM_CLIENT_CLASS_NAME: Corpus = Corpus {
    api: "apideck.com-ecosystem-client-class-name",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: Some("EcosystemClient"),
    extra_fields: None,
    unmatched: &[],
};

/// `yourbrand-ticketing`: corpus row 308, YourBrand's Ticketing service API
/// from marinasundstrom/YourBrand, whose two `format: duration` string bodies
/// reach `scalar_body`'s plain-string arm
const YOURBRAND_TICKETING: Corpus = Corpus {
    api: "yourbrand-ticketing",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `peopledatalabs`: corpus row 230, People Data Labs API 5.0 from
/// jentic/jentic-public-apis, whose company-size enums hold `10001+`
const PEOPLEDATALABS: Corpus = Corpus {
    api: "peopledatalabs",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `adyen-acs-notification`: corpus row 229, Adyen's Authentication webhooks v1
/// from Adyen/adyen-openapi, whose enum members lead with a digit
const ADYEN_ACS_NOTIFICATION: Corpus = Corpus {
    api: "adyen-acs-notification",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `googleapis-monitoring-v1`: corpus row 225, Google's Cloud Monitoring API v1
/// from APIs.guru, whose enums carry members with leading zeros
const GOOGLEAPIS_MONITORING_V1: Corpus = Corpus {
    api: "googleapis-monitoring-v1",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `docu-goapiserver`: corpus row 226, the Primula Tracker API V3 description
/// in JuaniGit/docu-goapiserver, whose `anyOf` variants nest an `anyOf`
const DOCU_GOAPISERVER: Corpus = Corpus {
    api: "docu-goapiserver",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `onevoice`: corpus row 227, the OneVoice API description in f1xgun/onevoice,
/// which declares a `mutualTLS` security scheme
const ONEVOICE: Corpus = Corpus {
    api: "onevoice",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

/// `xfsc-oidc-identity-resolver`: corpus row 228, the Eclipse XFSC notarization
/// service's oidc-identity-resolver description, whose only security schemes
/// are `openIdConnect`
const XFSC_OIDC_IDENTITY_RESOLVER: Corpus = Corpus {
    api: "xfsc-oidc-identity-resolver",
    package_name: "fern",
    project_name: "default_package_name",
    audiences: &[],
    audience_strict: false,
    client_class_name: None,
    extra_fields: None,
    unmatched: &[],
};

#[test]
fn apideck_ats_matches_fern_output() {
    if corpus_spec(APIDECK_ATS.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Apideck ATS committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
        );
        return;
    }
    assert_corpus_matches(&APIDECK_ATS);
}

#[test]
fn buildrelay_matches_fern_output() {
    if corpus_spec(BUILDRELAY.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the BuildRelay committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
        );
        return;
    }
    assert_corpus_matches(&BUILDRELAY);
}

#[test]
fn tlon_notes_matches_fern_output() {
    if corpus_spec(TLON_NOTES.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Tlon Notes committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
        );
        return;
    }
    assert_corpus_matches(&TLON_NOTES);
}

#[test]
fn twilio_messaging_v1_matches_fern_output() {
    assert_committed_corpus_matches(&TWILIO_MESSAGING_V1);
}

#[test]
fn livepeer_ai_runner_matches_fern_output() {
    assert_committed_corpus_matches(&LIVEPEER_AI_RUNNER);
}

#[test]
fn eos_extra_fields_forbid_matches_fern_output() {
    assert_committed_corpus_matches(&EOS_EXTRA_FIELDS_FORBID);
}

#[test]
fn med_anvisa_price_matches_fern_output() {
    assert_committed_corpus_matches(&MED_ANVISA_PRICE);
    let spec = corpus_spec(MED_ANVISA_PRICE.api).expect("registered medication-price source");
    let document: serde_yaml_ng::Value = serde_yaml_ng::from_str(
        &std::fs::read_to_string(spec).expect("read medication-price source"),
    )
    .expect("parse medication-price source");
    let parameter = &document["paths"]["/medication"]["get"]["parameters"][1];
    assert_eq!(parameter["name"].as_str(), Some("value"));
    assert!(parameter.get("schema").is_none());
    assert!(parameter.get("content").is_none());
    let out = generate_corpus(&MED_ANVISA_PRICE);
    for path in ["client.py", "raw_client.py"] {
        let source = std::fs::read_to_string(out.path().join("src/fern/medication").join(path))
            .expect("generated medication query client");
        assert_eq!(
            source.matches("value: typing.Optional[str] = None").count(),
            2,
            "{path}"
        );
    }
}

#[test]
fn sac_backend_matches_fern_output() {
    assert_committed_corpus_matches(&SAC_BACKEND);
}

#[test]
fn kytos_sdntrace_cp_matches_fern_output() {
    assert_committed_corpus_matches(&KYTOS_SDNTRACE_CP);
}

#[test]
fn withsecure_gdpr_subject_rights_matches_fern_output() {
    assert_committed_corpus_matches(&WITHSECURE_GDPR_SUBJECT_RIGHTS);
}

#[test]
fn prometheus_x_edge_computing_matches_fern_output() {
    assert_committed_corpus_matches(&PROMETHEUS_X_EDGE_COMPUTING);
}

#[test]
fn exa_gate_matches_fern_output() {
    assert_committed_corpus_matches(&EXA_GATE);
}

#[test]
fn amazonaws_com_cloudfront_matches_fern_output() {
    assert_committed_corpus_matches(&AMAZONAWS_COM_CLOUDFRONT);
}

#[test]
fn khoainats_matches_fern_output() {
    assert_committed_corpus_matches(&KHOAINATS);
}

#[test]
fn helios_verifiable_api_matches_fern_output() {
    assert_committed_corpus_matches(&HELIOS_VERIFIABLE_API);
}

#[test]
fn eozilla_matches_fern_output() {
    assert_committed_corpus_matches(&EOZILLA);
}

#[test]
fn openepcis_dpp_ready_matches_fern_output() {
    assert_committed_corpus_matches(&OPENEPCIS_DPP_READY);
}

#[test]
fn ndw_accessibility_map_matches_fern_output() {
    assert_committed_corpus_matches(&NDW_ACCESSIBILITY_MAP);
}

#[test]
fn marimo_matches_fern_output() {
    assert_committed_corpus_matches(&MARIMO);
}

#[test]
fn marimo_client_class_name_matches_fern_output() {
    assert_committed_corpus_matches(&MARIMO_CLIENT_CLASS_NAME);
    let out = generate_corpus(&MARIMO_CLIENT_CLASS_NAME);
    for (path, classes) in [
        (
            "client.py",
            ["class DispatchClient:", "class AsyncDispatchClient:"],
        ),
        (
            "raw_client.py",
            ["class RawDispatchClient:", "class AsyncRawDispatchClient:"],
        ),
    ] {
        let source = std::fs::read_to_string(out.path().join("src/fern").join(path))
            .expect("generated package-root client");
        for class in classes {
            assert!(source.contains(class), "{path} is missing {class}");
        }
    }
}

#[test]
fn blackadi_oauth2_matches_fern_output() {
    assert_committed_corpus_matches(&BLACKADI_OAUTH2);
}

#[test]
fn mosip_esignet_matches_fern_output() {
    assert_committed_corpus_matches(&MOSIP_ESIGNET);
}

#[test]
fn openbankingproject_ch_kundenbeziehung_matches_fern_output() {
    assert_committed_corpus_matches(&OPENBANKINGPROJECT_CH_KUNDENBEZIEHUNG);
}

#[test]
fn cyberark_conjur_api_matches_fern_output() {
    assert_committed_corpus_matches(&CYBERARK_CONJUR_API);
}

#[test]
fn adyen_report_notification_matches_fern_output() {
    assert_committed_corpus_matches(&ADYEN_REPORT_NOTIFICATION);
}

#[test]
fn adyen_managed_risk_notification_matches_fern_output() {
    assert_committed_corpus_matches(&ADYEN_MANAGED_RISK_NOTIFICATION);
}

#[test]
fn go_kratos_casbin_admin_matches_fern_output() {
    assert_committed_corpus_matches(&GO_KRATOS_CASBIN_ADMIN);
}

#[test]
fn descope_authzcache_matches_fern_output() {
    assert_committed_corpus_matches(&DESCOPE_AUTHZCACHE);
}

#[test]
fn swagger_petstore_matches_fern_output() {
    assert_committed_corpus_matches(&SWAGGER_PETSTORE);
}

#[test]
fn cyclonedx_transparency_exchange_matches_fern_output() {
    assert_committed_corpus_matches(&CYCLONEDX_TRANSPARENCY_EXCHANGE);
}

#[test]
fn adyen_capital_matches_fern_output() {
    assert_committed_corpus_matches(&ADYEN_CAPITAL);
}

#[test]
fn apivideo_android_uploader_matches_fern_output() {
    assert_committed_corpus_matches(&APIVIDEO_ANDROID_UPLOADER);
}

#[test]
fn truefoundry_trueforge_matches_fern_output() {
    assert_committed_corpus_matches(&TRUEFOUNDRY_TRUEFORGE);
}

#[test]
fn volview_backend_contract_matches_fern_output() {
    assert_committed_corpus_matches(&VOLVIEW_BACKEND_CONTRACT);
}

#[test]
fn osparc_simcore_webserver_matches_fern_output() {
    assert_committed_corpus_matches(&OSPARC_SIMCORE_WEBSERVER);
}

#[test]
fn helixdb_http_api_matches_fern_output() {
    assert_committed_corpus_matches(&HELIXDB_HTTP_API);
}

#[test]
fn flowdapt_matches_fern_output() {
    assert_committed_corpus_matches(&FLOWDAPT);
}

#[test]
fn k8s_container_service_provider_matches_fern_output() {
    assert_committed_corpus_matches(&K8S_CONTAINER_SERVICE_PROVIDER);
}

#[test]
fn daniweb_connect_matches_fern_output() {
    assert_committed_corpus_matches(&DANIWEB_CONNECT);
}

#[test]
fn chaingateway_io_matches_fern_output() {
    assert_committed_corpus_matches(&CHAINGATEWAY_IO);
}

#[test]
fn hubspot_events_matches_fern_output() {
    assert_committed_corpus_matches(&HUBSPOT_EVENTS);
}

#[test]
fn paloalto_remote_networks_matches_fern_output() {
    assert_committed_corpus_matches(&PALOALTO_REMOTE_NETWORKS);
}

#[test]
fn openintegrationhub_secret_service_matches_fern_output() {
    assert_committed_corpus_matches(&OPENINTEGRATIONHUB_SECRET_SERVICE);
}

#[test]
fn strapi_rest_api_matches_fern_output() {
    assert_committed_corpus_matches(&STRAPI_REST_API);
}

#[test]
fn listennotes_matches_fern_output() {
    assert_committed_corpus_matches(&LISTENNOTES);
}

#[test]
fn vtex_pricing_matches_fern_output() {
    assert_committed_corpus_matches(&VTEX_PRICING);
}

#[test]
fn aws_importexport_matches_fern_output() {
    assert_committed_corpus_matches(&AWS_IMPORTEXPORT);
}

#[test]
fn openbanking_brasil_directory_matches_fern_output() {
    assert_committed_corpus_matches(&OPENBANKING_BRASIL_DIRECTORY);
}

#[test]
fn api_openverse_org_matches_fern_output() {
    assert_committed_corpus_matches(&API_OPENVERSE_ORG);
}

#[test]
fn discord_com_matches_fern_output() {
    assert_committed_corpus_matches(&DISCORD_COM);
}

#[test]
fn braintrust_dev_matches_fern_output() {
    assert_committed_corpus_matches(&BRAINTRUST_DEV);
}

#[test]
fn agco_ats_matches_fern_output() {
    assert_committed_corpus_matches(&AGCO_ATS);
}

#[test]
fn torrentarr_matches_fern_output() {
    assert_committed_corpus_matches(&TORRENTARR);
}

#[test]
fn svix_webhooks_matches_fern_output() {
    assert_committed_corpus_matches(&SVIX_WEBHOOKS);
}

#[test]
fn komga_matches_fern_output() {
    assert_committed_corpus_matches(&KOMGA);
}

#[test]
fn short_io_matches_fern_output() {
    assert_committed_corpus_matches(&SHORT_IO);
}

#[test]
fn webflow_v2_matches_fern_output() {
    assert_committed_corpus_matches(&WEBFLOW_V2);
}

#[test]
fn loris_dataquery_matches_fern_output() {
    assert_committed_corpus_matches(&LORIS_DATAQUERY);
}

#[test]
fn sftpgo_matches_fern_output() {
    assert_committed_corpus_matches(&SFTPGO);
}

#[test]
fn googleapis_servicebroker_matches_fern_output() {
    assert_committed_corpus_matches(&GOOGLEAPIS_SERVICEBROKER);
}

#[test]
fn audiobookshelf_matches_fern_output() {
    assert_committed_corpus_matches(&AUDIOBOOKSHELF);
}

#[test]
fn steaminputdb_matches_fern_output() {
    assert_committed_corpus_matches(&STEAMINPUTDB);
}

#[test]
fn squareup_com_matches_fern_output() {
    if corpus_spec(SQUAREUP_COM.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the Square committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the AWS CloudFormation committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the Redocly Museum committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
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
            "CROZIER_REQUIRE_CORPUS is set but the HTTP Toolkit committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
        );
        return;
    }
    assert_corpus_matches(&HTTP_TOOLKIT);
}

fn assert_committed_corpus_matches(corpus: &Corpus) {
    if corpus_spec(corpus.api).is_none() {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the {} committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source",
            corpus.api
        );
        return;
    }
    assert_corpus_matches(corpus);
}

#[test]
fn folio_mod_authtoken_matches_fern_output() {
    assert_committed_corpus_matches(&FOLIO_MOD_AUTHTOKEN);
}

#[test]
fn raybot_matches_fern_output() {
    assert_committed_corpus_matches(&RAYBOT);
}

#[test]
fn paloalto_cspm_alerts_matches_fern_output() {
    assert_committed_corpus_matches(&PALOALTO_CSPM_ALERTS);
}

#[test]
fn paloalto_cspm_reports_matches_fern_output() {
    assert_committed_corpus_matches(&PALOALTO_CSPM_REPORTS);
}

#[test]
fn paloalto_cspm_search_manager_matches_fern_output() {
    assert_committed_corpus_matches(&PALOALTO_CSPM_SEARCH_MANAGER);
}

#[test]
fn thrivecart_matches_fern_output() {
    assert_committed_corpus_matches(&THRIVECART);
}

#[test]
fn frankfurter_matches_fern_output() {
    assert_committed_corpus_matches(&FRANKFURTER);
}

#[test]
fn worldcoin_signup_sequencer_matches_fern_output() {
    assert_committed_corpus_matches(&WORLDCOIN_SIGNUP_SEQUENCER);
}

#[test]
fn electric_sql_matches_fern_output() {
    assert_committed_corpus_matches(&ELECTRIC_SQL);
}

#[test]
fn tamoss_matches_fern_output() {
    assert_committed_corpus_matches(&TAMOSS);
}

#[test]
fn slurmdb_rest_matches_fern_output() {
    assert_committed_corpus_matches(&SLURMDB_REST);
}

#[test]
fn nimisampo_matches_fern_output() {
    assert_committed_corpus_matches(&NIMISAMPO);
}

#[test]
fn free5gc_pdu_session_matches_fern_output() {
    assert_committed_corpus_matches(&FREE5GC_PDU_SESSION);
}

#[test]
fn sigstore_rekor_matches_fern_output() {
    assert_committed_corpus_matches(&SIGSTORE_REKOR);
}

#[test]
fn confluent_kafka_connect_matches_fern_output() {
    assert_committed_corpus_matches(&CONFLUENT_KAFKA_CONNECT);
}

#[test]
fn netgsm_sms_matches_fern_output() {
    assert_committed_corpus_matches(&NETGSM_SMS);
}

#[test]
fn waylay_queries_matches_fern_output() {
    assert_committed_corpus_matches(&WAYLAY_QUERIES);
}

#[test]
fn letta_matches_fern_output() {
    assert_committed_corpus_matches(&LETTA);
}

#[test]
fn free5gc_namf_communication_matches_fern_output() {
    assert_committed_corpus_matches(&FREE5GC_NAMF_COMMUNICATION);
}

#[test]
fn openlinksw_osdb_matches_fern_output() {
    assert_committed_corpus_matches(&OPENLINKSW_OSDB);
}

#[test]
fn ziptax_node_matches_fern_output() {
    assert_committed_corpus_matches(&ZIPTAX_NODE);
}

#[test]
fn nexmo_messages_matches_fern_output() {
    assert_committed_corpus_matches(&NEXMO_MESSAGES);
}

#[test]
fn deepsearch_ds_v2_matches_fern_output() {
    assert_committed_corpus_matches(&DEEPSEARCH_DS_V2);
}

#[test]
fn mindee_ocr_matches_fern_output() {
    assert_committed_corpus_matches(&MINDEE_OCR);
}

#[test]
fn opencodeui_matches_fern_output() {
    assert_committed_corpus_matches(&OPENCODEUI);
}

/// One golden test per feature target, named like every other corpus's, so each
/// target's Fern golden is compared on its own and the `golden-only` tier of
/// `just fixtures-coverage` (every `*matches_fern_output*` test) counts it: a
/// feature target's `expected/` tree is Fern's output exactly as a real-world
/// corpus's is. Every target walks its complete expected tree; only measured
/// residual paths in `unmatched` are exempted and reverse-checked.
macro_rules! feature_target_goldens {
    ($($test:ident => $api:literal),* $(,)?) => {
        $(
            #[test]
            fn $test() {
                assert_feature_target_matches($api);
            }
        )*

        /// The `api` of every feature target a golden test above drives.
        const FEATURE_TARGET_GOLDEN_TESTS: &[&str] = &[$($api),*];
        const FEATURE_TARGET_GOLDEN_NAMES: &[(&str, &str)] = &[$((stringify!($test), $api)),*];
    };
}

feature_target_goldens! {
    crozier_sdk_extensions_matches_fern_output => "crozier-sdk-extensions",
    crozier_property_name_matches_fern_output => "crozier-property-name",
    auth_schemes_matches_fern_output => "auth-schemes",
    inline_request_response_matches_fern_output => "inline-request-response",
    cookie_parameters_matches_fern_output => "cookie-parameters",
    form_bodies_matches_fern_output => "form-bodies",
    discriminated_unions_matches_fern_output => "discriminated-unions",
    schema_constraints_matches_fern_output => "schema-constraints",
    integer_enums_matches_fern_output => "integer-enums",
    servers_webhooks_matches_fern_output => "servers-webhooks",
    basic_auth_matches_fern_output => "basic-auth",
    oauth_client_credentials_matches_fern_output => "oauth-client-credentials",
    inline_array_request_matches_fern_output => "inline-array-request",
    writeonly_fields_matches_fern_output => "writeonly-fields",
    digit_leading_property_matches_fern_output => "digit-leading-property",
    operation_id_non_identifier_matches_fern_output => "operation-id-non-identifier",
    bracketed_property_names_matches_fern_output => "bracketed-property-names",
    missing_operation_id_matches_fern_output => "missing-operation-id",
    error_responses_matches_fern_output => "error-responses",
    tag_based_grouping_matches_fern_output => "tag-based-grouping",
    enum_query_param_matches_fern_output => "enum-query-param",
    audience_filter_matches_fern_output => "audience-filter",
    audience_filter_strict_matches_fern_output => "audience-filter-strict",
    sse_streaming_matches_fern_output => "sse-streaming",
    enum_name_sanitization_matches_fern_output => "enum-name-sanitization",
    enum_receiver_collision_matches_fern_output => "enum-receiver-collision",
    client_class_name_matches_fern_output => "client-class-name",
    pydantic_extra_fields_matches_fern_output => "pydantic-extra-fields",
    recursive_types_matches_fern_output => "recursive-types",
    nested_core_imports_matches_fern_output => "nested-core-imports",
    malformed_property_schema_matches_fern_output => "malformed-property-schema",
}

fn assert_feature_target_matches(api: &str) {
    let target = FEATURE_TARGETS
        .iter()
        .find(|target| target.api == api)
        .unwrap_or_else(|| panic!("{api} is not a FEATURE_TARGETS entry"));
    assert_corpus_matches(target);
}

#[test]
fn every_feature_target_has_its_own_golden_test() {
    let declared: std::collections::BTreeSet<&str> =
        FEATURE_TARGETS.iter().map(|target| target.api).collect();
    let driven: std::collections::BTreeSet<&str> =
        FEATURE_TARGET_GOLDEN_TESTS.iter().copied().collect();
    assert_eq!(
        declared, driven,
        "every FEATURE_TARGETS entry needs exactly one `feature_target_goldens!` test"
    );
    assert_eq!(
        FEATURE_TARGET_GOLDEN_TESTS.len(),
        driven.len(),
        "a feature target is driven by two golden tests"
    );
}

// --- Flat-layout goldens -----------------------------------------------------
// Fern writes two trees: the packaged SDK (`--preview --output`, the `expected/`
// goldens above) and a flat module tree (a `local-file-system` output path).
// crozier reproduces the second with `--layout flat`; these goldens are Fern's
// own flat output, produced by `scripts/generate-fern-fixture.sh --layout flat`
// and compared under exactly the rules the packaged goldens are.

/// The directory holding a fixture's flat golden, beside its packaged `expected/`.
const FLAT_GOLDEN_DIR: &str = "expected-flat";

/// One committed flat Fern golden, `tests/fixtures/<fixture>/expected-flat/`.
struct FlatGolden {
    /// The fixture directory holding the golden.
    fixture: &'static str,
    /// The spec and settings crozier is driven with. `None` reuses the registered
    /// corpus of the same name — the flat golden shares its packaged sibling's
    /// settings. `Some` is a golden whose directory has no spec of its own: `api`
    /// names the fixture whose vendored document it generates from.
    corpus: Option<&'static Corpus>,
}

/// Every flat golden, one per row of `tests/fixtures/flat-goldens.txt` (held to
/// it by `flat_goldens_are_the_declared_set`). Between them they exercise every
/// setting that changes the flat tree: the default names (`swagger-petstore`), a
/// client class name, audiences with strictness, a non-default `extra-fields`,
/// a custom package and project name, and a mixed-case package name. Fern's
/// `organization` is what names the module, client and README the way crozier's
/// `--package-name` does, and a flat tree carries no distribution, so the
/// project name reaches no file of it (see docs/matching.md).
const FLAT_GOLDENS: &[FlatGolden] = &[
    FlatGolden {
        fixture: "swagger-petstore",
        corpus: None,
    },
    FlatGolden {
        fixture: "swagger-petstore-distribution",
        corpus: Some(&Corpus {
            api: "swagger-petstore",
            package_name: "acme",
            project_name: "acme-dist",
            audiences: &[],
            audience_strict: false,
            client_class_name: None,
            extra_fields: None,
            unmatched: &[],
        }),
    },
    FlatGolden {
        fixture: "client-class-name",
        corpus: None,
    },
    FlatGolden {
        fixture: "audience-filter-strict",
        corpus: None,
    },
    FlatGolden {
        fixture: "eos.local-extra-fields-forbid",
        corpus: None,
    },
    // Fern's organization with an inner capital and no client class name: the
    // code names `PetStoreApi`, and so does crozier everywhere, where Fern's
    // README lowers the inner capital (the `readme-client-class-casing`
    // departure). Its docstrings import a tag package's type from a package not
    // named `fern`, which Fern's isort pass groups with the root import.
    FlatGolden {
        fixture: "swagger-petstore-organization",
        corpus: Some(&Corpus {
            api: "swagger-petstore",
            package_name: "PetStore",
            project_name: "PetStore",
            audiences: &[],
            audience_strict: false,
            client_class_name: None,
            extra_fields: None,
            unmatched: &[],
        }),
    },
];

/// The spec and settings a flat golden drives crozier with.
fn flat_golden_corpus(golden: &FlatGolden) -> &'static Corpus {
    golden.corpus.unwrap_or_else(|| {
        registered_diff_corpora()
            .into_iter()
            .find(|corpus| corpus.api == golden.fixture)
            .unwrap_or_else(|| panic!("{} is not a registered corpus", golden.fixture))
    })
}

/// Generate a flat golden's crozier side, or say why it could not be generated.
/// `Ok(None)` is a fetched-spec golden whose spec has not been fetched.
fn try_generate_flat(golden: &FlatGolden) -> Result<Option<tempfile::TempDir>, String> {
    let corpus = flat_golden_corpus(golden);
    if corpus_spec(corpus.api).is_none() {
        return Ok(None);
    }
    let out = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let (mut command, _source) = corpus_command(corpus, out.path());
    let result = command
        .args(["--layout", "flat"])
        .output()
        .map_err(|error| format!("could not run crozier: {error}"))?;
    let stderr = String::from_utf8_lossy(&result.stderr);
    if !result.status.success() || !stderr.contains("generated") {
        return Err(format!(
            "crozier --layout flat exited {:?}: {}",
            result.status.code(),
            stderr.trim()
        ));
    }
    Ok(Some(out))
}

/// [`parity::compare_trees`] of the Fern tree `expected_root` and crozier's
/// `out` — the comparison the flat gate and the reporters print — with the
/// departures it applied held to `ledger`, the golden's rows (or why they
/// cannot be read), in the files `file_filter` keeps. Fails, naming each row,
/// where the ledger disagrees.
fn golden_differences(
    expected_root: &Path,
    out: &Path,
    file_filter: Option<&str>,
    include_text_diffs: bool,
    ledger: Result<GoldenLedger, Vec<String>>,
) -> Result<Vec<(String, Difference)>, String> {
    let ledger = ledger.map_err(|failures| failures.join("\n"))?;
    let compared = parity::compare_trees(expected_root, out, file_filter, include_text_diffs)?;
    let observed: Vec<Observed> = compared
        .departures
        .into_iter()
        .map(|departure| (departure.file, departure.line, departure.id))
        .collect();
    let failures = ledger.check(&observed, &|rel| {
        file_filter.is_none_or(|filter| rel.contains(filter))
    });
    if failures.is_empty() {
        Ok(compared.differences)
    } else {
        Err(failures.join("\n"))
    }
}

/// Require crozier's `--layout flat` output to equal the flat golden file for
/// file, in both directions, under the packaged goldens' normalization.
fn assert_flat_golden_matches(fixture: &str) {
    let golden = FLAT_GOLDENS
        .iter()
        .find(|golden| golden.fixture == fixture)
        .unwrap_or_else(|| panic!("{fixture} is not a FLAT_GOLDENS entry"));
    let expected_root = fixture_dir(fixture).join(FLAT_GOLDEN_DIR);
    assert!(
        expected_root.is_dir() && !expected_root.is_symlink(),
        "{fixture} has no {FLAT_GOLDEN_DIR}/ golden"
    );
    let Some(out) = try_generate_flat(golden).unwrap_or_else(|error| panic!("{fixture}: {error}"))
    else {
        assert!(
            std::env::var_os("CROZIER_REQUIRE_CORPUS").is_none(),
            "CROZIER_REQUIRE_CORPUS is set but the {fixture} committed corpus spec is missing; run just lint-corpus-sources to diagnose the missing committed source"
        );
        return;
    };
    assert_inventoried(&golden_path(&expected_root));
    let differences = golden_differences(
        &expected_root,
        out.path(),
        None,
        true,
        departure_ledger().golden(&golden_path(&expected_root), &[]),
    )
    .unwrap_or_else(|error| panic!("{fixture}: {error}"));
    let report: Vec<String> = differences
        .iter()
        .map(|(rel, difference)| match difference {
            Difference::Text(Some(diff)) => format!("--- {rel} ---\n{diff}"),
            other => format!("--- {rel} --- {other:?}"),
        })
        .collect();
    assert!(
        report.is_empty(),
        "{fixture}: crozier's flat output does not match Fern's flat golden \
         (normalized; `-` = Fern golden, `+` = crozier). Reproduce with \
         `just fixtures-diff {fixture}`; fix the generator, never the golden.\n{}",
        report.join("\n")
    );
}

macro_rules! flat_goldens {
    ($($test:ident => $fixture:literal),* $(,)?) => {
        $(
            #[test]
            fn $test() {
                assert_flat_golden_matches($fixture);
            }
        )*

        /// The fixture of every flat golden a test above drives.
        const FLAT_GOLDEN_TESTS: &[(&str, &str)] = &[$((stringify!($test), $fixture)),*];
    };
}

flat_goldens! {
    swagger_petstore_flat_matches_fern => "swagger-petstore",
    swagger_petstore_distribution_flat_matches_fern => "swagger-petstore-distribution",
    client_class_name_flat_matches_fern => "client-class-name",
    audience_filter_strict_flat_matches_fern => "audience-filter-strict",
    eos_extra_fields_forbid_flat_matches_fern => "eos.local-extra-fields-forbid",
    swagger_petstore_organization_flat_matches_fern => "swagger-petstore-organization",
}

/// `tests/fixtures/flat-goldens.txt` as `(fixture, spec fixture)` rows, the spec
/// column empty when the golden uses its own fixture's spec.
fn declared_flat_goldens() -> Vec<(String, String)> {
    let table = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures/flat-goldens.txt"),
    )
    .expect("read tests/fixtures/flat-goldens.txt");
    table
        .lines()
        .filter(|line| !line.trim().is_empty() && !line.starts_with('#'))
        .map(|line| {
            let (fixture, spec) = line
                .split_once('|')
                .unwrap_or_else(|| panic!("flat-goldens.txt row without `|`: {line}"));
            (fixture.to_string(), spec.to_string())
        })
        .collect()
}

#[test]
fn flat_goldens_are_the_declared_set() {
    // The table the scripts read, the registry the gate reads, the tests that
    // drive it, and the directories on disk must all name the same goldens, so a
    // golden cannot be generated that nothing compares, or compared from a spec
    // the scripts would not generate it from.
    let declared = declared_flat_goldens();
    let registry: Vec<(String, String)> = FLAT_GOLDENS
        .iter()
        .map(|golden| {
            let spec = golden
                .corpus
                .map_or(String::new(), |corpus| corpus.api.to_string());
            (golden.fixture.to_string(), spec)
        })
        .collect();
    assert_eq!(
        declared, registry,
        "FLAT_GOLDENS drifted from tests/fixtures/flat-goldens.txt"
    );

    let driven: Vec<&str> = FLAT_GOLDEN_TESTS
        .iter()
        .map(|(_, fixture)| *fixture)
        .collect();
    let registered: Vec<&str> = FLAT_GOLDENS.iter().map(|golden| golden.fixture).collect();
    assert_eq!(
        driven, registered,
        "every flat golden needs exactly one test"
    );

    let on_disk: std::collections::BTreeSet<String> =
        std::fs::read_dir(Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures"))
            .expect("read tests/fixtures")
            .map(|entry| entry.expect("fixture entry").path())
            .filter(|path| path.join(FLAT_GOLDEN_DIR).exists())
            .map(|path| path.file_name().unwrap().to_string_lossy().into_owned())
            .collect();
    let registered: std::collections::BTreeSet<String> = registered
        .iter()
        .map(|fixture| fixture.to_string())
        .collect();
    assert_eq!(
        on_disk, registered,
        "a fixture's {FLAT_GOLDEN_DIR}/ is not in FLAT_GOLDENS, or a listed one is missing"
    );

    for golden in FLAT_GOLDENS {
        let corpus = flat_golden_corpus(golden);
        // A spec-less golden rides a vendored or committed document; any other
        // uses its own.
        if golden.corpus.is_some() {
            assert!(
                !fixture_dir(golden.fixture).join("openapi.yml").exists(),
                "{}: a golden with its own spec must not name another",
                golden.fixture
            );
            assert!(
                corpus_spec(corpus.api).is_some_and(|spec| spec.is_file()),
                "{}: names `{}`, which has no vendored or committed spec",
                golden.fixture,
                corpus.api
            );
        }
        // Provenance names the layout, so a flat golden is never mistaken for
        // (or refreshed as) a packaged one.
        let state = fixture_dir(golden.fixture)
            .join(FLAT_GOLDEN_DIR)
            .join(".crozier-fern-golden.json");
        let state: serde_json::Value = serde_json::from_str(
            &std::fs::read_to_string(&state)
                .unwrap_or_else(|error| panic!("{}: {error}", state.display())),
        )
        .expect("flat provenance is JSON");
        assert_eq!(
            state["layout"], "flat",
            "{}: flat provenance must record its layout",
            golden.fixture
        );
        assert_eq!(
            state["fern_python_sdk_version"], "5.20.0",
            "{}",
            golden.fixture
        );
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
    let (mut corpora, selection_failures) = select_diff_corpora(None);
    assert!(
        selection_failures.is_empty(),
        "corpus selection failures:\n{}",
        selection_failures
            .iter()
            .map(|(name, error)| format!("{name}: {error}"))
            .collect::<Vec<_>>()
            .join("\n")
    );
    corpora.retain(|corpus| corpus_spec(corpus.api).is_some());
    let flat_goldens = select_flat_goldens(None, corpus_filter.as_deref());

    if let Some(filter) = &corpus_filter {
        corpora.retain(|corpus| corpus.api == filter);
        assert!(
            !corpora.is_empty() || !flat_goldens.is_empty(),
            "CROZIER_GAPS_CORPUS={filter:?} matched no corpus (or its spec is unfetched)"
        );
    }

    let corpus_count = corpora.len() + flat_goldens.len();
    let mut total_expected = 0usize;
    let mut total_unmatched = 0usize;
    for corpus in corpora {
        let expected_root = fixture_dir(corpus.api).join("expected");
        let expected_files = walk_files(&expected_root);
        let out = generate_corpus(corpus);
        let context = Context::from_trees(&expected_root, out.path());
        let confirmed: std::collections::HashSet<String> = expected_files
            .iter()
            .filter(|rel| {
                let (Ok(expected), Ok(generated)) = (
                    std::fs::read_to_string(expected_root.join(rel)),
                    std::fs::read_to_string(out.path().join(rel)),
                ) else {
                    return false;
                };
                generated_matches_fixture(&context, rel, &generated, &expected)
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
                divergent.len(),
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
    for golden in flat_goldens {
        let expected_root = fixture_dir(golden.fixture).join(FLAT_GOLDEN_DIR);
        let out = try_generate_flat(golden)
            .unwrap_or_else(|error| panic!("{}: {error}", golden.fixture))
            .expect("only flat goldens with an available spec are selected");
        let differences = golden_differences(
            &expected_root,
            out.path(),
            None,
            false,
            departure_ledger().golden(&golden_path(&expected_root), &[]),
        )
        .unwrap_or_else(|error| panic!("{}: {error}", golden.fixture));
        let expected_files = walk_files(&expected_root).len();
        println!("\n=== {} ({FLAT_GOLDEN_DIR}) ===", golden.fixture);
        println!("  {expected_files} expected file(s).");
        if differences.is_empty() {
            println!("  no unmatched files.");
        } else {
            println!(
                "  {} file(s) differ — a flat golden has no `unmatched` list, so fix the generator:",
                differences.len()
            );
            for (rel, _) in &differences {
                println!("        \"{rel}\",");
            }
        }
        total_expected += expected_files;
        total_unmatched += differences.len();
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
        match corpus_has_comparable_golden(corpus, &expected) {
            Ok(true) => {}
            Ok(false) => continue,
            Err(error) => {
                failures.push((name.to_string(), error));
                continue;
            }
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

/// Mismatch-investigation aid — NOT a gate (ignored by default). Complementing
/// [`report_fixture_gaps`], it
/// prints the normalized unified diff of every committed fixture file crozier does
/// NOT reproduce byte-for-byte — exactly what the gate's engine decides on
/// (comments stripped and every catalog departure applied, via
/// [`golden_differences`]), with `-` = Fern golden and `+` = crozier. This is the
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
    // A flat golden with no packaged sibling is not a registered corpus, so it is
    // selected by name here rather than through `select_diff_corpora`.
    let requested_corpora = requested.as_deref().map(|value| {
        value
            .split(',')
            .filter(|name| !is_flat_only_golden(name))
            .collect::<Vec<_>>()
            .join(",")
    });
    let (mut corpora, selection_failures) = match requested_corpora.as_deref() {
        Some("") => (Vec::new(), Vec::new()),
        other => select_diff_corpora(other),
    };
    let flat_goldens = select_flat_goldens(requested.as_deref(), corpus_filter.as_deref());
    if let Some(f) = &corpus_filter {
        corpora.retain(|c| c.api == f.as_str());
        assert!(
            !corpora.is_empty() || !flat_goldens.is_empty(),
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
        let differences = match golden_differences(
            &expected_root,
            out.path(),
            file_filter.as_deref(),
            include_text_diffs,
            corpus_golden_ledger(departure_ledger(), &golden_path(&expected_root), c),
        ) {
            Ok(differences) => differences,
            Err(error) => {
                println!("  Comparison processing failed: {error}");
                processing_failures += 1;
                continue;
            }
        };
        print_fixture_differences(&differences, &unmatched);
        total += differences.len();
    }
    for golden in flat_goldens {
        let label = format!("{} ({FLAT_GOLDEN_DIR})", golden.fixture);
        let out = match try_generate_flat(golden) {
            Ok(Some(out)) => out,
            Ok(None) => {
                println!("\n=== {label} ===");
                println!(
                    "  Comparison setup failed: fixture spec is unavailable after the fetch phase"
                );
                processing_failures += 1;
                continue;
            }
            Err(error) => {
                println!("\n=== {label} ===");
                println!("  Crozier generation failed: {error}");
                generation_failures += 1;
                continue;
            }
        };
        println!("\n=== {label} ===");
        let expected_root = fixture_dir(golden.fixture).join(FLAT_GOLDEN_DIR);
        let differences = match golden_differences(
            &expected_root,
            out.path(),
            file_filter.as_deref(),
            include_text_diffs,
            departure_ledger().golden(&golden_path(&expected_root), &[]),
        ) {
            Ok(differences) => differences,
            Err(error) => {
                println!("  Comparison processing failed: {error}");
                processing_failures += 1;
                continue;
            }
        };
        // A flat golden has no `unmatched` list: every difference is a regression.
        print_fixture_differences(&differences, &std::collections::HashSet::new());
        total += differences.len();
    }
    println!(
        "\n{generation_failures} comparison generation failure(s) across the reported corpora."
    );
    println!("{processing_failures} comparison processing failure(s) across the reported corpora.");
    println!("\n{total} differing file(s) across the reported corpora.");
}

/// Print one golden's differences for `report_fixture_diffs`, tagging each one
/// outside `unmatched` as a regression.
fn print_fixture_differences(
    differences: &[(String, Difference)],
    unmatched: &std::collections::HashSet<&str>,
) {
    for (rel, difference) in differences {
        // A difference outside `unmatched` is a regression; explicit gaps
        // remain ordinary task-list entries.
        let tag = if unmatched.contains(rel.as_str()) {
            ""
        } else {
            " [REGRESSION — not in `unmatched`]"
        };
        println!("\n--- {rel}{tag} ---");
        match difference {
            Difference::OnlyInReference => {
                println!("  Crozier did not emit this Fern file.");
            }
            Difference::OnlyInCrozier => {
                println!("  Crozier emitted this file, but Fern did not.");
            }
            Difference::Text(Some(diff)) => {
                println!("  (`-` Fern golden, `+` crozier)\n{diff}");
            }
            Difference::Text(None) => {
                println!("  Normalized text differs; unified diff omitted in summary mode.");
            }
            Difference::Binary {
                reference: expected,
                crozier: generated,
            } => {
                println!(
                    "  Binary bytes differ (Fern: {expected} bytes; Crozier: {generated} bytes)."
                );
            }
            Difference::Processing(error) => {
                println!("  Could not normalize/compare this file: {error}");
            }
        }
    }
    if differences.is_empty() {
        println!("  no differences.");
    }
}

/// Whether `name` is a flat golden with no registered corpus of its own.
fn is_flat_only_golden(name: &str) -> bool {
    FLAT_GOLDENS
        .iter()
        .any(|golden| golden.fixture == name && golden.corpus.is_some())
}

/// The flat goldens a reporter covers: those named by `requested` (a
/// comma-separated list) and `filter` when given, and otherwise every one whose
/// spec is available. An explicitly requested golden is kept even when its spec
/// is unfetched, so the reporter can say so.
fn select_flat_goldens(requested: Option<&str>, filter: Option<&str>) -> Vec<&'static FlatGolden> {
    FLAT_GOLDENS
        .iter()
        .filter(|golden| {
            requested.is_none_or(|value| value.split(',').any(|name| name == golden.fixture))
                && filter.is_none_or(|name| name == golden.fixture)
                && (requested.is_some() || corpus_spec(flat_golden_corpus(golden).api).is_some())
        })
        .collect()
}

#[test]
fn exact_comparison_scope_reports_unregistered_managed_fixtures() {
    let (selected, failures) = select_diff_corpora(Some("frankfurter,new-unregistered-fixture"));
    assert_eq!(
        selected.iter().map(|corpus| corpus.api).collect::<Vec<_>>(),
        ["frankfurter"]
    );
    assert_eq!(failures.len(), 1, "{failures:?}");
    assert_eq!(failures[0].0, "new-unregistered-fixture");
    assert!(failures[0].1.contains("not registered"));
}

#[test]
fn missing_golden_is_allowed_only_for_a_validated_known_fern_failure() {
    let missing = tempfile::tempdir()
        .expect("temporary parent")
        .path()
        .join("expected");
    let error = corpus_has_comparable_golden(&BUNQ, &missing)
        .expect_err("a normal corpus must never silently skip a missing golden");
    assert_eq!(error, "fixture has no expected/ golden tree");

    assert!(
        !corpus_has_comparable_golden(
            &CALORIENINJAS,
            &fixture_dir(CALORIENINJAS.api).join("expected")
        )
        .expect("CalorieNinjas has a valid exact known-failure registration"),
        "an exact known Fern failure has no golden to compare"
    );
}

/// The accepted-exception mechanism is the only way a registered corpus escapes
/// byte comparison, so it must be impossible to reuse as a suppression. Drive the
/// validator with the real registration and with the tampered forms someone would
/// reach for to excuse a divergence: copying it onto another corpus, moving it to
/// a newer Fern, shrinking the fingerprint, or widening the contract.
#[test]
fn a_known_fern_failure_registration_cannot_excuse_anything_else() {
    let path = fixture_dir(CALORIENINJAS.api).join(KNOWN_FERN_FAILURE_FILE);
    let bytes = std::fs::read(&path).expect("the registered exception is committed");
    validate_known_fern_failure(CALORIENINJAS.api, "registered", &bytes)
        .expect("the one registered exception is valid");

    // Bound to the spec it was measured against: the same bytes cannot cover a
    // corpus whose golden merely started diverging.
    let error = validate_known_fern_failure(BUNQ.api, "copied", &bytes)
        .expect_err("a registration must not transfer to another corpus");
    assert!(error.contains("stale corpus_spec_name"), "{error}");

    let tampered = |mutate: &dyn Fn(&mut serde_json::Value)| {
        let mut payload: serde_json::Value =
            serde_json::from_slice(&bytes).expect("the registration is JSON");
        mutate(&mut payload);
        validate_known_fern_failure(
            CALORIENINJAS.api,
            "tampered",
            serde_json::to_vec(&payload).expect("re-encode").as_slice(),
        )
        .expect_err("a tampered registration must be rejected")
    };

    // Bound to the exact generator that fails, so it cannot silently outlive it.
    let error = tampered(&|payload| payload["generator_version"] = serde_json::json!("5.21.0"));
    assert!(error.contains("stale generator_version"), "{error}");

    // Bound to the exact evidence, so the fingerprint cannot be blurred.
    let error = tampered(&|payload| {
        payload["fingerprint"]["diagnostics"]
            .as_array_mut()
            .expect("diagnostic list")
            .pop();
    });
    assert!(error.contains("exactly six identifier"), "{error}");

    // Bound to an exact key set, so no extra field can be smuggled in.
    let error = tampered(&|payload| payload["also_ignore"] = serde_json::json!("everything"));
    assert!(
        error.contains("exact known-failure contract keys"),
        "{error}"
    );
}

/// Registration only becomes coverage when something *runs* it. A `Corpus` that
/// no test drives, or a committed-source corpus missing from `just test-corpus-match`,
/// would miss the explicit corpus recipe — so a reintroduced residual would go
/// unnoticed exactly where the corpus is supposed to catch it. Both wirings are
/// derived from the sources themselves, so adding a corpus without them fails
/// here rather than years later.
#[test]
fn every_registered_corpus_is_wired_into_the_gate() {
    let source = include_str!("e2e.rs");
    let recipe = corpus_match_recipe(include_str!("../justfile"));

    let mut enforced = std::collections::BTreeSet::new();
    for corpus in registered_diff_corpora() {
        if let Some((test, _)) = FEATURE_TARGET_GOLDEN_NAMES
            .iter()
            .find(|(_, api)| *api == corpus.api)
        {
            assert!(
                recipe.iter().any(|listed| listed == test),
                "{}: {test} is missing from just test-corpus-match",
                corpus.api
            );
            enforced.insert((*test).to_string());
            continue;
        }
        let constant = corpus_constant_for(source, corpus.api).unwrap_or_else(|| {
            panic!(
                "{}: registered corpora need a named `Corpus` const",
                corpus.api
            )
        });
        let test = corpus_test_for(source, &constant).unwrap_or_else(|| {
            panic!(
                "{}: no #[test] drives {constant}, so the gate would never compare it",
                corpus.api
            )
        });
        assert!(
            recipe.contains(&test),
            "{}: {test} is missing from `just test-corpus-match`, so CI would omit its committed source",
            corpus.api
        );
        enforced.insert(test);
    }
    // A flat golden needs the same corpus-recipe wiring as its
    // packaged sibling, or the corpus leg would skip it too.
    for (test, fixture) in FLAT_GOLDEN_TESTS {
        assert!(
            recipe.iter().any(|listed| listed == test),
            "{fixture}: {test} is missing from `just test-corpus-match`, so CI would omit its committed source"
        );
        enforced.insert((*test).to_string());
    }

    // The overlay gate compares every setting's targeted goldens in one test,
    // over the same committed sources; the name must still be its test's.
    assert!(
        include_str!("e2e/overlay_goldens.rs")
            .contains(&format!("fn {}()", overlay_goldens::CORPUS_TEST)),
        "no #[test] is named {}",
        overlay_goldens::CORPUS_TEST
    );
    assert!(
        recipe
            .iter()
            .any(|listed| listed == overlay_goldens::CORPUS_TEST),
        "{} is missing from `just test-corpus-match`",
        overlay_goldens::CORPUS_TEST
    );
    enforced.insert(overlay_goldens::CORPUS_TEST.to_string());

    let listed: std::collections::BTreeSet<String> = recipe.iter().cloned().collect();
    assert_eq!(
        listed, enforced,
        "`just test-corpus-match` lists tests that no registered corpus owns"
    );
}

/// The test names `just test-corpus-match` enforces, in recipe order.
fn corpus_match_recipe(justfile: &str) -> Vec<String> {
    let tests: Vec<String> = justfile
        .lines()
        .skip_while(|line| !line.starts_with("test-corpus-match:"))
        .skip(1)
        .take_while(|line| line.starts_with(' ') || line.starts_with('\t'))
        .filter_map(|line| {
            line.trim_end()
                .rsplit_once("--test e2e ")
                .map(|(_, test)| test.to_string())
        })
        .collect();
    assert!(!tests.is_empty(), "`test-corpus-match` enforces no tests");
    tests
}

/// The `const NAME: Corpus` whose `api` field is `api`.
fn corpus_constant_for(source: &str, api: &str) -> Option<String> {
    let mut pending: Option<&str> = None;
    for line in source.lines() {
        if let Some(rest) = line.strip_prefix("const ") {
            if rest.contains(": Corpus = Corpus {") {
                pending = rest.split(':').next().map(str::trim);
            }
            continue;
        }
        if let Some(rest) = line.trim().strip_prefix("api: \"") {
            let declared = rest.trim_end_matches(',').trim_matches('"');
            if let Some(name) = pending.take() {
                if declared == api {
                    return Some(name.to_string());
                }
            }
        }
    }
    None
}

/// The `#[test] fn` that drives `constant` through a byte comparison or, for the
/// accepted exception, through its known-failure boundary.
fn corpus_test_for(source: &str, constant: &str) -> Option<String> {
    const DRIVERS: [&str; 3] = [
        "assert_corpus_matches(&",
        "assert_committed_corpus_matches(&",
        "known_fern_failure(&",
    ];
    let mut current = None;
    for line in source.lines() {
        if let Some(rest) = line.strip_prefix("fn ") {
            current = rest.split('(').next();
        }
        for driver in DRIVERS {
            let Some((_, rest)) = line.split_once(driver) else {
                continue;
            };
            if rest.split([')', ',']).next() == Some(constant) {
                return current.map(str::to_string);
            }
        }
    }
    None
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
    parse_corpus_fixture_aliases(include_str!("fixtures/corpus-aliases.tsv"))
}

fn parse_corpus_fixture_aliases(input: &str) -> Result<Vec<(&str, &str)>, String> {
    let mut aliases = Vec::new();
    let mut sources = std::collections::HashSet::new();
    let mut fixtures = std::collections::HashSet::new();
    for (index, line) in input.lines().enumerate() {
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
    Ok(aliases)
}

fn corpus_fixture_for<'a>(name: &'a str, aliases: &[(&'a str, &'a str)]) -> &'a str {
    aliases
        .iter()
        .find_map(|(source, fixture)| (*source == name).then_some(*fixture))
        .unwrap_or(name)
}

// llmlint: ignore-block[e2e_not_mocked, tests_mirror_real_usage] The readers under test are the real scripts/fern-goldens and scripts/fetch-corpus.sh, copied unmodified into a temp repo by FernGoldensBoundaryTests, the harness `just test-fern-goldens` drives them through; its stand-in `curl`/`just` replace only the network fetch and the Fern run, external processes an offline gate cannot reach that act after the alias registry is read and validated. The third reader, `parse_corpus_fixture_aliases`/`corpus_fixture_for`, is this e2e binary's own fixture locator with no public entry point, so the test calls it directly to hold it to the two scripts.
#[cfg(not(windows))]
#[test]
fn fixture_alias_readers_agree_on_validation_and_resolution() {
    let python = python_interpreter().expect("Python is required for alias reader agreement");
    let journey = r#"
import json, subprocess, sys
from tests.fern_goldens_test import FernGoldensBoundaryTests, ALIASES
case = FernGoldensBoundaryTests()
case.setUp()
try:
    (case.root / 'tests/fixtures' / ALIASES.name).write_text(sys.argv[1], encoding='utf-8', newline='\n')
    name = sys.argv[2]
    (case.root / 'tests/fixtures/CORPUS.md').write_text(
        '| # | name | method | source | pinned ref | license | decision | shapes |\n'
        f'| 1 | `{name}` | test | https://example.test/alpha/openapi.yaml | `1` | MIT | link-ok | alias |\n',
        encoding='utf-8',
        newline='\n',
    )
    generated = case.run_tool('generate', '--version', '4.9.0', '--fixture', name)
    fetched = subprocess.run(
        [case.root / 'scripts/fetch-corpus.sh', '--dry-run', '--fixture', 'alpha'],
        cwd=case.root, text=True, encoding='utf-8', capture_output=True,
    )
    if generated.returncode == 0:
        case.assertEqual(name, case.state('alpha')['corpus_spec_name'])
    if fetched.returncode == 0:
        case.assertTrue(fetched.stdout.startswith(name + '\t'), fetched.stdout)
    print(json.dumps({'python': generated.returncode, 'shell': fetched.returncode}))
finally:
    case.tearDown()
"#;
    for (input, requested, expected) in [
        ("# aliases\n", "alpha", Some("alpha")),
        (
            "planet-window\talpha\nsignal-history\tbeta\n",
            "planet-window",
            Some("alpha"),
        ),
        ("../outside\talpha\n", "alpha", None),
        ("only-one-cell\n", "alpha", None),
        ("planet-window\talpha\nplanet-window\tbeta\n", "alpha", None),
        (
            "planet-window\talpha\nsignal-history\talpha\n",
            "alpha",
            None,
        ),
        ("alpha\talpha\n", "alpha", None),
    ] {
        let rust = parse_corpus_fixture_aliases(input);
        assert_eq!(rust.is_ok(), expected.is_some(), "Rust reader: {input:?}");
        if let Some(expected) = expected {
            assert_eq!(corpus_fixture_for(requested, &rust.unwrap()), expected);
        }
        let output = std::process::Command::new(python)
            .args(["-c", journey, input, requested])
            .env("PYTHONUTF8", "1")
            .output()
            .expect("public alias workflows");
        assert!(
            output.status.success(),
            "alias journey: {}",
            String::from_utf8_lossy(&output.stderr)
        );
        let statuses: serde_json::Value = serde_json::from_slice(&output.stdout).unwrap();
        for reader in ["python", "shell"] {
            assert_eq!(
                statuses[reader] == 0,
                expected.is_some(),
                "{reader}: {input:?}: {statuses}"
            );
        }
    }
}
// llmlint: ignore-end[e2e_not_mocked, tests_mirror_real_usage]

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

/// Every file under `root`, as `/`-separated paths relative to `root`, sorted —
/// the library's [`parity::walk_files`], panicking on a walk it refuses.
fn walk_files(root: &Path) -> Vec<String> {
    parity::walk_files(root).unwrap_or_else(|error| panic!("{error}"))
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

/// Where the cached Python environments are built: the system temp dir, or
/// `CROZIER_TEST_ENV_ROOT` where a test needs a root no run has built in yet
/// (see [`sdk_env_journeys_survive_concurrent_first_use`]).
fn python_env_root() -> PathBuf {
    std::env::var_os("CROZIER_TEST_ENV_ROOT").map_or_else(std::env::temp_dir, PathBuf::from)
}

/// Prepare (creating and caching if needed) a virtualenv holding the generated
/// SDK's runtime dependencies (`httpx`, `pydantic`) and `pytest`, and return its
/// interpreter, so the runtime wire suite can import and drive a generated
/// client. Returns an `Err` describing why the env could not be prepared — no
/// base interpreter, no venv support, or a failed dependency install (e.g.
/// offline) — which fails the journey.
///
/// The venv is cached under [`python_env_root`] and reused once marked ready,
/// so repeated runs pay the install once. `uv` is used when present (seconds);
/// otherwise the stdlib `venv` + `pip`. Concurrent runs share it the way they
/// share [`sdk_python_env_in`]'s: whoever holds the lock builds, the rest wait
/// and find it ready, and a directory without the marker is a build that died
/// part-way, so it is cleared rather than built over.
fn runtime_python_env() -> Result<PathBuf, String> {
    // The SDK's own runtime deps plus the wire suite's test runner.
    const DEPS: [&str; 3] = ["httpx", "pydantic", "pytest"];
    let base = python_interpreter().ok_or("no python3/python on PATH")?;
    let root = python_env_root();
    let venv = root.join("crozier-runtime-venv-v2");
    let venv_py = venv_python(&venv);
    let ready = venv.join(".crozier-ready");

    let lock = hold_lock(&root.join("crozier-runtime-venv-v2.lock"))?;
    if venv_py.exists() && ready.is_file() && can_import_sdk_deps(&venv_py) {
        return Ok(venv_py);
    }
    if venv.exists() {
        std::fs::remove_dir_all(&venv)
            .map_err(|error| format!("cannot clear partial {}: {error}", venv.display()))?;
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

    if !can_import_sdk_deps(&venv_py) {
        return Err("venv prepared but httpx/pydantic/pytest still not importable".into());
    }
    std::fs::write(&ready, DEPS.join("\n"))
        .map_err(|error| format!("cannot mark {} ready: {error}", venv.display()))?;
    drop(lock);
    Ok(venv_py)
}

/// Runtime ("wire") behavior of a generated SDK, verified **differentially
/// against Fern**: byte-matching Fern proves the source is right and
/// `assert_valid_python` proves it compiles, but neither proves the compiled
/// client issues the right HTTP request or parses the response. Rather than
/// hand-author the expected behavior, this derives it from Fern: the committed
/// pytest suite ([`tests/runtime/test_wire.py`]) records the client's behavior
/// (via an injected `httpx.MockTransport`) for **both** the committed Fern fixture
/// SDK (`airbyte.local-config/expected/src`, generated from the registered API) and the
/// crozier-generated SDK, and asserts — per journey — that the recordings match.
///
/// Each journey captures the outgoing request (method, URL, headers, serialized
/// body) and the outcome (the response model dumped to a dict, or the typed
/// error's class/status/body) — covering request construction, auth + SDK-identity
/// headers, body field-aliasing and `OMIT` filtering, query encoding, typed
/// pydantic deserialization, and typed error raising, sync and async. The *only*
/// allowed difference is the deliberate SDK-identity branding (`X-Crozier-*` vs
/// `X-Fern-*`), which the recorder folds to a common prefix on both sides. It
/// drives the compiled binary and the compiled client, so it lives in the e2e
/// binary, in its SDK Python-environment tier. See docs/matching.md.
// llmlint: ignore-block[e2e_not_mocked] The double is `httpx.MockTransport` at the HTTP transport, the boundary tests/runtime and the refusal registry's wire tests double by convention: it records the real generated clients, crozier's and Fern's, through one transport so their requests and outcomes can be compared; crossing a real network is the live Prism tier's job (`just test-live-e2e`).
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_crozier_matches_fern_runtime_behavior() {
    let out = tempfile::tempdir().expect("tempdir");
    let spec = corpus_spec(AIRBYTE_CONFIG.api).expect("registered Airbyte source");
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

    let py = runtime_python_env()
        .unwrap_or_else(|reason| panic!("runtime wire tests require a Python env: {reason}"));

    let runtime_dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/runtime");
    let fern_src = fixture_dir(AIRBYTE_CONFIG.api).join("expected/src");
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
// llmlint: ignore-end[e2e_not_mocked]

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
fn a_security_scheme_reference_emits_the_credential_it_names() {
    // Measured at fernapi/fern-python-sdk:5.20.0 on
    // docs/openapi-surface/probes/securityscheme-ref.yml and its control: a
    // Reference Object in the `components.securitySchemes` position is resolved
    // in-document, and the referenced scheme is imported under the REFERENCING key
    // — so a document whose map holds a reference beside its target takes two
    // credentials, where the control's single inline scheme takes one. crozier used
    // to deserialize the reference to the default scheme and drop it, which diverged
    // from Fern in `client.py`, `core/client_wrapper.py`, `reference.md` and
    // `README.md` (openapi.rs's `normalize_security_scheme_refs`).
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\nsecurity:\n  \
         - ProbeScheme: []\npaths:\n  /a:\n    get:\n      operationId: getA\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: \
         { type: string } } } }\ncomponents:\n  securitySchemes:\n    ProbeScheme: \
         { $ref: '#/components/securitySchemes/ProbeApiKey' }\n    ProbeApiKey: { type: apiKey, \
         name: X-Probe-Key, in: header }\n",
    );
    let wrapper = std::fs::read_to_string(out.join("src/acme/core/client_wrapper.py"))
        .expect("client_wrapper.py");
    assert_eq!(
        2,
        wrapper.matches("headers[\"X-Probe-Key\"]").count(),
        "the reference and its target each contribute a credential; wrapper has:\n{wrapper}"
    );
    let client = std::fs::read_to_string(out.join("src/acme/client.py")).expect("client.py");
    assert!(
        client.contains("probe_key: str,") && client.contains("api_key: str,"),
        "both credentials reach the client constructor; client.py has:\n{client}"
    );
}

#[test]
fn a_pure_ref_component_names_the_response_it_types() {
    // Measured at fernapi/fern-python-sdk:5.20.0 while probing the documents under
    // docs/openapi-surface/probes/: a component schema that is nothing but a LOCAL
    // `$ref` types an operation response under its OWN name, not its target's.
    // crozier used to follow every such alias, which diverged from Fern on all
    // four spellings probed — the bare `$ref`, and the same `$ref` beside a
    // `title`, a `description` or an `unevaluatedProperties`. The rewrite is now
    // confined to an alias of a *remotely* declared schema, which is the form
    // helios-verifiable-api's `BlockResponse` over its fetched `Block` carries and
    // the only form Fern was measured to follow (openapi.rs's
    // `normalize_fetched_response_alias_refs`).
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /a:\n    \
         get:\n      operationId: getA\n      responses:\n        '200': { description: OK, \
         content: { application/json: { schema: { $ref: '#/components/schemas/AliasOfThing' } } } }\n\
         components:\n  schemas:\n    Thing: { type: object, properties: { value: { type: string } } }\n    \
         AliasOfThing: { $ref: '#/components/schemas/Thing', title: AliasOfThing }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/client.py")).expect("client.py");
    assert!(
        client.contains("-> AliasOfThing:"),
        "the response keeps the alias name Fern emits; client.py has:\n{client}"
    );
    assert!(
        !client.contains("-> Thing:"),
        "the alias target must not stand in for the alias at the response"
    );
    assert_eq!(
        "AliasOfThing = Thing\n",
        std::fs::read_to_string(out.join("src/acme/types/alias_of_thing.py"))
            .expect("alias module")
            .lines()
            .filter(|line| !line.trim_start().starts_with('#') && !line.trim().is_empty())
            .filter(|line| !line.starts_with("from "))
            .map(|line| format!("{line}\n"))
            .collect::<String>(),
        "the alias module itself still declares the alias"
    );
}

#[test]
fn an_object_typed_path_parameter_is_converted_into_the_url_and_documented_by_its_type() {
    // Measured at fernapi/fern-python-sdk:5.20.0 on
    // docs/openapi-surface/probes/parameter-style-simple-path-object.yml, the
    // probe that settles the `parameter-style-simple-path-object` row: no
    // registered corpus source declares a path parameter over an object schema,
    // so nothing else holds crozier to Fern here. Three behaviours in one
    // document, because they are one shape: the URL segment wraps the model in
    // `convert_and_respect_annotation_metadata`, the Markdown writers construct
    // the model with values read off each field's TYPE (`role="string"`, not the
    // `role="role"` a request body's field takes), and the docstring writer keeps
    // the plain name placeholder a scalar parameter would show.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  \
         /probe/{probeParam}:\n    get:\n      operationId: probe\n      parameters:\n        \
         - { name: probeParam, in: path, required: true, style: simple, schema: { $ref: '#/components/schemas/ProbeParam' } }\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: \
         { $ref: '#/components/schemas/ProbeResult' } } } }\ncomponents:\n  schemas:\n    \
         ProbeParam: { title: ProbeParam, type: object, properties: { role: { type: string }, \
         level: { type: integer } }, required: [role] }\n    \
         ProbeResult: { title: ProbeResult, type: object, properties: { ok: { type: boolean } }, required: [ok] }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/raw_client.py")).expect("raw_client.py");
    assert!(
        raw.contains(
            "f\"probe/{encode_path_param(convert_and_respect_annotation_metadata(object_=probe_param, annotation=ProbeParam, direction='write'))}\""
        ),
        "the object-typed path parameter is serialized through the converter; raw_client.py has:\n{raw}"
    );
    let readme = std::fs::read_to_string(out.join("README.md")).expect("README.md");
    assert!(
        readme.contains("        role=\"string\",\n"),
        "the README example reads the field's value off its type; README.md has:\n{readme}"
    );
    let client = std::fs::read_to_string(out.join("src/acme/client.py")).expect("client.py");
    assert!(
        client.contains("            probe_param=\"probeParam\",\n"),
        "the docstring example keeps the name placeholder; client.py has:\n{client}"
    );
    assert!(
        !client.contains("from acme import AcmeApi, ProbeParam"),
        "a docstring that documents the placeholder imports no model into its example; client.py has:\n{client}"
    );
}

#[test]
fn a_path_parameter_object_with_a_model_field_documents_no_example_at_all() {
    // The other half of the same measurement: Fern renders the constructed model
    // only where every required field is one its writer can render — an array is
    // `[]` and a map `{}`, and a required field that is itself a generated model
    // costs the endpoint its whole example, in all three writers at once.
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  \
         /probe/{probeParam}:\n    get:\n      operationId: probe\n      parameters:\n        \
         - { name: probeParam, in: path, required: true, schema: { $ref: '#/components/schemas/ProbeParam' } }\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: \
         { $ref: '#/components/schemas/ProbeResult' } } } }\ncomponents:\n  schemas:\n    \
         Inner: { title: Inner, type: object, properties: { label: { type: string } }, required: [label] }\n    \
         ProbeParam: { title: ProbeParam, type: object, properties: { role: { type: string }, \
         nested: { $ref: '#/components/schemas/Inner' } }, required: [role, nested] }\n    \
         ProbeResult: { title: ProbeResult, type: object, properties: { ok: { type: boolean } }, required: [ok] }\n",
    );
    let client = std::fs::read_to_string(out.join("src/acme/client.py")).expect("client.py");
    assert!(
        !client.contains("\n        client.probe("),
        "the method documents no worked example; client.py has:\n{client}"
    );
    let reference = std::fs::read_to_string(out.join("reference.md")).expect("reference.md");
    assert!(
        reference.contains("```python\nclient.probe(...)\n```"),
        "reference.md abbreviates the call with no snippet gap; it has:\n{reference}"
    );
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
    // SDK. This spec packs the crashing shapes Fern generates from into one
    // document — a Python keyword (`global`) and a `type: string` enum whose
    // values are all integers. Generation must succeed and every module must
    // compile. The digit-run value `_01_00_AM`, which Fern rejects, is refused
    // instead (the `enum-name-unsuitable` class, asserted below).
    let spec = "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    \
         get:\n      operationId: listWidgets\n      tags: [widgets]\n      parameters:\n        \
         - { name: size, in: query, required: false, schema: { type: string, enum: [100, 125] } }\n      \
         responses:\n        '200': { description: OK, content: { application/json: { schema: \
         { $ref: '#/components/schemas/Widget' } } } }\ncomponents:\n  schemas:\n    Widget:\n      \
         type: object\n      properties:\n        scope: { $ref: '#/components/schemas/WidgetScope' }\n    \
         WidgetScope:\n      type: string\n      enum: [\"global\", \"practice\"]\n";
    let (_dir, out) = generate_ok(spec);
    // The keyword value's `visit` parameter is keyword-escaped.
    let scope = std::fs::read_to_string(out.join("src/acme/types/widget_scope.py"))
        .expect("WidgetScope enum is generated");
    assert!(
        scope.contains("global_: typing.Callable"),
        "keyword value → keyword-escaped visit param: {scope}"
    );
    // The type-mismatched enum (string type, integer values) drops its members and
    // falls back to the base `str` type rather than emitting an empty enum class.
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("size: typing.Optional[str] = None"),
        "a type-mismatched string enum falls back to str: {raw}"
    );

    // Adding the digit-run enum Fern refuses turns the same document into a
    // refusal: exit 1, nothing written, the class and value named on stderr.
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(
        &path,
        format!(
            "{spec}    WidgetHour:\n      type: string\n      enum: [\"_01_00_AM\", \"_12_00_PM\"]\n"
        ),
    )
    .unwrap();
    let refused = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&path)
        .arg("--output")
        .arg(&refused)
        .args(["--package-name", "acme"])
        .assert()
        .code(1)
        .stderr(predicates::str::contains(
            "enum-name-unsuitable: #/components/schemas/WidgetHour enum value \"_01_00_AM\"",
        ));
    assert!(!refused.exists(), "a refused document writes nothing");
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

/// A second operation keeps the `X-Mode` header a method argument rather than a
/// promoted client field.
#[test]
fn referenced_parameter_examples_populate_worked_calls() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { $ref: '#/components/schemas/WidgetId' } }\n        - { name: X-Mode, in: header, required: true, schema: { $ref: '#/components/schemas/Mode' } }\n      responses:\n        '204': { description: Found }\n  /widgets:\n    get:\n      operationId: countWidgets\n      tags: [widgets]\n      responses:\n        '204': { description: Counted }\ncomponents:\n  schemas:\n    WidgetId: { type: string, example: '\"widget-123\"' }\n    Mode: { type: string, example: 'safe' }\n",
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
fn non_json_multipart_part_serializes_value_through_the_cli() {
    let (_dir, out) = generate_ok(
        r#"openapi: 3.1.0
info: { title: Widget API, version: 1.0.0 }
paths:
  /uploads:
    post:
      operationId: createUpload
      tags: [uploads]
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              required: [metadata]
              properties:
                metadata: { $ref: '#/components/schemas/Metadata' }
            encoding:
              metadata: { contentType: text/plain }
      responses:
        '204': { description: Created }
components:
  schemas:
    Metadata:
      type: object
      properties:
        note: { type: string }
"#,
    );
    let raw = std::fs::read_to_string(out.join("src/acme/uploads/raw_client.py"))
        .expect("multipart raw client is generated");
    assert!(
        raw.contains(
            "\"metadata\": (None, json.dumps(jsonable_encoder(metadata)), \"text/plain\")"
        ),
        "non-JSON part serializes the value and keeps its declared content type: {raw}"
    );
}

#[test]
fn non_json_multipart_array_part_keeps_encoded_list_through_the_cli() {
    let (_dir, out) = generate_ok(include_str!(
        "../docs/openapi-surface/probes/encoding-explode.yml"
    ));
    let raw = std::fs::read_to_string(out.join("src/acme/raw_client.py"))
        .expect("multipart raw client is generated");
    let part = "\"tags\": (None, jsonable_encoder(tags), \"text/plain\")";
    assert_eq!(
        raw.matches(part).count(),
        2,
        "sync and async list parts: {raw}"
    );
    assert!(
        !raw.contains("json.dumps(jsonable_encoder(tags))"),
        "non-JSON array parts keep the encoded list instead of serializing it: {raw}"
    );
}

#[test]
fn responses_extension_beside_status_code_is_ignored_through_the_cli() {
    let (_probe_dir, probe_out) = generate_ok(include_str!(
        "../docs/openapi-surface/probes/extension-responses.yml"
    ));
    let (_control_dir, control_out) = generate_ok(include_str!(
        "../docs/openapi-surface/probes/extension-responses-control.yml"
    ));
    let path = "src/acme/raw_client.py";
    let probe =
        std::fs::read_to_string(probe_out.join(path)).expect("response client is generated");
    let control =
        std::fs::read_to_string(control_out.join(path)).expect("control client is generated");
    assert!(
        probe.contains("def probe("),
        "status response is retained: {probe}"
    );
    assert_eq!(
        probe, control,
        "the Responses Object extension has no SDK effect"
    );
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

/// A lone inline header enum is a document pinned Fern fails to generate
/// (`generator-missing-type`); a second operation without the header keeps it
/// an endpoint parameter, the shape Fern generates and hoists.
#[test]
fn header_parameter_enums_hoist_to_tag_types() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets:\n    post:\n      operationId: createWidget\n      tags: [widgets]\n      parameters:\n        - name: X-Widget-Mode\n          in: header\n          required: true\n          schema: { type: string, enum: [FAST, SAFE] }\n      responses:\n        '204': { description: Created }\n  /widgets/{id}:\n    get:\n      operationId: getWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { type: string } }\n      responses:\n        '204': { description: Found }\n",
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
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/{id}/export:\n    get:\n      operationId: exportWidget\n      tags: [widgets]\n      parameters:\n        - { name: id, in: path, required: true, schema: { $ref: '#/components/schemas/WidgetId' } }\n      responses:\n        '200': { description: Export, content: { application/zip: { schema: { $ref: '#/components/schemas/FileContent' } } } }\n        '404': { description: Missing }\ncomponents:\n  schemas:\n    WidgetId: { type: string, example: '\"widget-123\"' }\n    FileContent: { type: string, format: binary }\n",
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
fn colliding_query_and_body_fields_serialize_from_body_argument() {
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
        "query parameters keep their own original argument: {raw}"
    );
    assert!(
        raw.contains("\"active\": widget_record_active,"),
        "the JSON body must use its renamed caller argument: {raw}"
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

/// A single-use `allOf` body Fern drops from the type layer is flattened into the
/// method like any dropped `$ref` body, and keeps the JSON content-type header
/// that a surviving schema's body leaves to httpx: measured at Fern 5.20.0 on this
/// document, with the `$ref` member first, last, or under a `type: object`.
#[test]
fn pathless_single_use_all_of_bodies_send_the_content_type() {
    let (_dir, out) = generate_ok(
        "openapi: 3.0.3\ninfo: { title: Widget API, version: 1.0.0 }\npaths:\n  /widgets/test:\n    post:\n      operationId: testWidget\n      tags: [widgets]\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema: { $ref: '#/components/schemas/Widget' }\n      responses:\n        '200': { description: OK }\ncomponents:\n  schemas:\n    WidgetBase:\n      type: object\n      properties:\n        name: { type: string }\n    Widget:\n      allOf:\n        - { $ref: '#/components/schemas/WidgetBase' }\n        - type: object\n          properties:\n            active: { type: boolean }\n",
    );
    let raw = std::fs::read_to_string(out.join("src/acme/widgets/raw_client.py"))
        .expect("widgets raw client is generated");
    assert!(
        raw.contains("\"content-type\": \"application/json\""),
        "a single-use allOf request body sends the JSON content type: {raw}"
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
fn marimo_output_is_valid_python() {
    let out = generate_corpus(&MARIMO);
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
    // `x-fern-ignore` and `x-crozier-ignore` each drop their operation and keep the
    // type it exclusively referenced, as Fern's TrueForge golden does, while an
    // explicit `x-crozier-ignore: false` overrides a sibling `x-fern-ignore: true`
    // (the Overlay un-ignore pattern). The pruned SDK must still compile.
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

    // Both ignore spellings drop their client and keep their exclusive type.
    assert!(
        !out.join("src/widgetapi/fern").exists(),
        "x-fern-ignore op should be pruned"
    );
    assert!(
        !out.join("src/widgetapi/crozier").exists(),
        "x-crozier-ignore op should be pruned"
    );
    assert!(out.join("src/widgetapi/types/only_fern.py").is_file());
    assert!(out.join("src/widgetapi/types/only_crozier.py").is_file());
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

// --- Configuration-surface journeys ------------------------------------------
// Everything below drives the real binary over a real temp directory and real
// config files to prove the *layering* — discovery, the `CROZIER_*` env layer,
// the documented precedence, multi-generator selection, and the `init`/`config`/
// `schema` subcommands. The pure merge logic is unit-tested in `src/settings.rs`;
// these are the journeys a user actually takes.

/// The `CROZIER_*` variables the settings layer reads (the documented set in
/// `docs/configuration.md`). The journeys below drive this layer deliberately, so
/// they start from a known-clean environment rather than inheriting whatever the
/// developer's shell happens to export.
const CROZIER_ENV_VARS: &[&str] = &[
    "CROZIER_CONFIG",
    "CROZIER_SPEC",
    "CROZIER_OUTPUT",
    "CROZIER_PACKAGE_NAME",
    "CROZIER_PROJECT_NAME",
    "CROZIER_CLIENT_CLASS_NAME",
    "CROZIER_AUDIENCES",
    "CROZIER_AUDIENCE_STRICT",
    "CROZIER_FERN_STRICT",
    "CROZIER_EXTRA_FIELDS",
    "CROZIER_ENUM_TYPE",
    "CROZIER_DEFAULT_MAX_RETRIES",
    "CROZIER_LAYOUT",
];

/// Every `CROZIER_*` identifier mentioned in a source file, in order.
fn crozier_env_names(source: &str) -> Vec<String> {
    let bytes = source.as_bytes();
    let mut names = Vec::new();
    let mut cursor = 0;
    while let Some(offset) = source[cursor..].find("CROZIER_") {
        let start = cursor + offset;
        let mut end = start + "CROZIER_".len();
        while end < bytes.len() && (bytes[end].is_ascii_uppercase() || bytes[end] == b'_') {
            end += 1;
        }
        // `CROZIER_*` in prose stops at the glob, leaving the bare prefix; only a
        // real variable name has something after it.
        if end > start + "CROZIER_".len() {
            names.push(source[start..end].to_string());
        }
        cursor = end;
    }
    names
}

#[test]
fn the_cleared_env_list_covers_every_variable_the_settings_surface_reads() {
    // `crozier_clean_env` is only isolation if it names *every* `CROZIER_*`
    // variable the binary reads: a new one added to the settings surface would
    // otherwise leak in from the developer's shell and quietly weaken every
    // journey below. Pin the list to the two modules that read the environment —
    // the same drift-gate shape `DISCOVERED_CONFIG_NAMES` uses.
    let mut read_by_the_binary: Vec<String> = ["src/settings.rs", "src/cli.rs"]
        .iter()
        .flat_map(|relative| {
            let source =
                std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join(relative))
                    .expect("read the settings surface");
            crozier_env_names(&source)
        })
        .collect();
    read_by_the_binary.sort();
    read_by_the_binary.dedup();

    let mut cleared: Vec<String> = CROZIER_ENV_VARS.iter().map(|n| (*n).to_string()).collect();
    cleared.sort();

    assert_eq!(
        read_by_the_binary, cleared,
        "CROZIER_ENV_VARS drifted from the variables src/settings.rs and src/cli.rs read"
    );
}

/// `TINY_SPEC` plus one operation, so the run also emits a root `client.py` —
/// needed wherever a journey asserts the generated client class name.
const TINY_SPEC_WITH_OP: &str = "openapi: 3.0.0\ninfo:\n  title: Tiny\npaths:\n  /thing:\n    get:\n      operationId: getThing\n      tags: [Thing]\n      responses:\n        '200':\n          description: OK\n          content:\n            application/json:\n              schema: { $ref: '#/components/schemas/Thing' }\ncomponents:\n  schemas:\n    Thing:\n      type: object\n      properties:\n        name: { type: string }\n";

/// The binary with every `CROZIER_*` override cleared, so a journey's env layer
/// is exactly what the journey sets.
fn crozier_clean_env() -> Command {
    let mut cmd = crozier();
    for name in CROZIER_ENV_VARS {
        cmd.env_remove(name);
    }
    cmd
}

/// The config-file names crozier auto-discovers, highest priority first. Mirrors
/// `settings::CONFIG_NAMES` — asserted against it so the journey below can never
/// silently test a stale list.
const DISCOVERED_CONFIG_NAMES: &[&str] = &[
    "crozier.yml",
    "crozier.yaml",
    ".crozier.yml",
    ".crozier.yaml",
];

/// A config naming one generator that writes `<name>` as its package, so which
/// file was loaded is visible in the generated tree.
fn config_naming(package: &str) -> String {
    format!(
        "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    package-name: {package}\n"
    )
}

#[test]
fn every_discovered_config_filename_is_loaded_in_priority_order() {
    assert_eq!(
        DISCOVERED_CONFIG_NAMES,
        crozier::settings::CONFIG_NAMES,
        "the journey's filename list drifted from the discovery order"
    );

    // Each name on its own is discovered with no `--config` flag at all.
    for name in DISCOVERED_CONFIG_NAMES {
        let dir = tempfile::tempdir().expect("tempdir");
        std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
        let package = name.replace(['.', '-'], "_");
        std::fs::write(dir.path().join(name), config_naming(&package)).unwrap();

        crozier_clean_env()
            .current_dir(dir.path())
            .arg("generate")
            .assert()
            .success()
            .stderr(predicate::str::contains("generated"));
        assert!(
            dir.path()
                .join(format!("out/src/{package}/types/thing.py"))
                .is_file(),
            "{name} should be discovered in the working directory"
        );
    }

    // All four present at once: the highest-priority name wins, and removing it
    // promotes the next — walking the whole documented priority order.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    for (i, name) in DISCOVERED_CONFIG_NAMES.iter().enumerate() {
        std::fs::write(dir.path().join(name), config_naming(&format!("rank{i}"))).unwrap();
    }
    for (i, name) in DISCOVERED_CONFIG_NAMES.iter().enumerate() {
        crozier_clean_env()
            .current_dir(dir.path())
            .arg("generate")
            .assert()
            .success();
        assert!(
            dir.path()
                .join(format!("out/src/rank{i}/types/thing.py"))
                .is_file(),
            "{name} should win once the higher-priority names are gone"
        );
        std::fs::remove_file(dir.path().join(name)).unwrap();
    }
}

#[test]
fn the_env_layer_supplies_the_naming_and_output_settings() {
    // No config file at all: `CROZIER_*` alone drives a complete run of the
    // built-in `python` generator, through the real process environment. The two
    // audience variables are the sibling journey below.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC_WITH_OP).unwrap();

    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_SPEC", "./api.yml")
        .env("CROZIER_OUTPUT", "./from-env")
        .env("CROZIER_PACKAGE_NAME", "envpkg")
        .env("CROZIER_PROJECT_NAME", "env-dist")
        .env("CROZIER_CLIENT_CLASS_NAME", "EnvClient")
        .env("CROZIER_EXTRA_FIELDS", "forbid")
        .assert()
        .success()
        .stderr(predicate::str::contains("./from-env"));

    let root = dir.path().join("from-env/src/envpkg");
    assert!(
        root.join("types/thing.py").is_file(),
        "CROZIER_OUTPUT/_PACKAGE_NAME"
    );
    assert!(
        std::fs::read_to_string(root.join("version.py"))
            .unwrap()
            .contains("metadata.version(\"env-dist\")"),
        "CROZIER_PROJECT_NAME should reach version.py"
    );
    assert!(
        std::fs::read_to_string(root.join("client.py"))
            .unwrap()
            .contains("class EnvClient"),
        "CROZIER_CLIENT_CLASS_NAME should name the root client"
    );
    assert!(
        std::fs::read_to_string(root.join("types/thing.py"))
            .unwrap()
            .contains("extra=\"forbid\""),
        "CROZIER_EXTRA_FIELDS should reach the pydantic config"
    );
}

#[test]
fn the_env_layer_filters_audiences_like_the_flags_do() {
    // `CROZIER_AUDIENCES` is comma-separated and `CROZIER_AUDIENCE_STRICT` is a
    // permissive boolean; both must prune exactly as `--audience`/
    // `--audience-strict` do over the same spec.
    let spec = fixture_dir("audience-filter-strict").join("openapi.yml");

    let permissive = tempfile::tempdir().expect("tempdir");
    crozier_clean_env()
        .current_dir(permissive.path())
        .env("CROZIER_SPEC", &spec)
        .env("CROZIER_OUTPUT", "./out")
        .env("CROZIER_PACKAGE_NAME", "aud")
        .env("CROZIER_AUDIENCES", " public , public ")
        .env("CROZIER_AUDIENCE_STRICT", "false")
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(permissive
        .path()
        .join("out/src/aud/widgets/client.py")
        .is_file());
    assert!(
        permissive
            .path()
            .join("out/src/aud/health/client.py")
            .is_file(),
        "a permissive CROZIER_AUDIENCES keeps the un-annotated op"
    );
    assert!(
        !permissive.path().join("out/src/aud/admin").exists(),
        "CROZIER_AUDIENCES should prune the internal op"
    );

    let strict = tempfile::tempdir().expect("tempdir");
    crozier_clean_env()
        .current_dir(strict.path())
        .env("CROZIER_SPEC", &spec)
        .env("CROZIER_OUTPUT", "./out")
        .env("CROZIER_PACKAGE_NAME", "aud")
        .env("CROZIER_AUDIENCES", "public")
        .env("CROZIER_AUDIENCE_STRICT", "1")
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(strict
        .path()
        .join("out/src/aud/widgets/client.py")
        .is_file());
    assert!(
        !strict.path().join("out/src/aud/health").exists(),
        "CROZIER_AUDIENCE_STRICT=1 should also prune the un-annotated op"
    );
}

#[test]
fn a_malformed_env_override_exits_nonzero_with_an_actionable_message() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();

    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_SPEC", "./api.yml")
        .env("CROZIER_OUTPUT", "./out")
        .env("CROZIER_AUDIENCE_STRICT", "maybe")
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(
            predicate::str::contains("CROZIER_AUDIENCE_STRICT")
                .and(predicate::str::contains("`true` or `false`"))
                .and(predicate::str::contains("panicked").not()),
        );

    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_SPEC", "./api.yml")
        .env("CROZIER_OUTPUT", "./out")
        .env("CROZIER_EXTRA_FIELDS", "sometimes")
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(
            predicate::str::contains("CROZIER_EXTRA_FIELDS")
                .and(predicate::str::contains("forbid"))
                .and(predicate::str::contains("panicked").not()),
        );

    assert!(
        !dir.path().join("out").exists(),
        "a rejected override must not generate anything"
    );
}

/// Run `crozier generate python` in a fresh directory holding `TINY_SPEC` and
/// `config`, with `env` exported and `extra_args` appended. Returns the directory
/// so the caller can assert which package name the layering produced.
fn layered_run(config: &str, env: &[(&str, &str)], extra_args: &[&str]) -> tempfile::TempDir {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(dir.path().join("crozier.yml"), config).unwrap();
    let mut cmd = crozier_clean_env();
    cmd.current_dir(dir.path()).args(["generate", "python"]);
    for (name, value) in env {
        cmd.env(name, value);
    }
    cmd.args(extra_args).assert().success();
    dir
}

/// One case of the precedence journey: a config file, the env layer, the CLI
/// flags, and the `package-name` the documented order should resolve to.
struct PrecedenceCase {
    config: &'static str,
    env: &'static [(&'static str, &'static str)],
    args: &'static [&'static str],
    winner: &'static str,
}

#[test]
fn a_field_resolves_cli_then_env_then_generator_then_shared_then_default() {
    // One field — `package-name` — supplied by all four layers at once, then
    // peeled one layer at a time. The generated package directory names the
    // winner, so the documented order is proven end to end rather than asserted
    // about the merge function.
    let all_four =
        "spec: ./api.yml\npackage-name: fromshared\ngenerators:\n  python:\n    output: ./out\n    package-name: fromgenerator\n";
    let shared_only =
        "spec: ./api.yml\npackage-name: fromshared\ngenerators:\n  python:\n    output: ./out\n";
    let neither = "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n";

    let cases = [
        // All four layers supply it: the CLI flag wins.
        PrecedenceCase {
            config: all_four,
            env: &[("CROZIER_PACKAGE_NAME", "fromenv")],
            args: &["--package-name", "fromcli"],
            winner: "fromcli",
        },
        // Drop the flag: the environment wins over both config layers.
        PrecedenceCase {
            config: all_four,
            env: &[("CROZIER_PACKAGE_NAME", "fromenv")],
            args: &[],
            winner: "fromenv",
        },
        // Drop the environment: the generator's own value beats the shared one.
        PrecedenceCase {
            config: all_four,
            env: &[],
            args: &[],
            winner: "fromgenerator",
        },
        // Drop the generator's value: the shared top-level value is inherited.
        PrecedenceCase {
            config: shared_only,
            env: &[],
            args: &[],
            winner: "fromshared",
        },
        // Drop every layer: the built-in default is a snake_case of the API title.
        PrecedenceCase {
            config: neither,
            env: &[],
            args: &[],
            winner: "tiny",
        },
    ];

    for case in cases {
        let dir = layered_run(case.config, case.env, case.args);
        let winner = case.winner;
        assert!(
            dir.path()
                .join(format!("out/src/{winner}/types/thing.py"))
                .is_file(),
            "expected `{winner}` to win; generated instead: {:?}",
            std::fs::read_dir(dir.path().join("out/src")).map(|entries| entries
                .filter_map(|entry| entry.ok().map(|entry| entry.file_name()))
                .collect::<Vec<_>>()),
        );
    }
}

#[test]
fn a_generator_overrides_the_shared_top_level_field_by_field() {
    // Shared defaults plus one generator that overrides some of them: the
    // generator's `spec`/`output`/`package-name` win, while the shared
    // `project-name` it does not set is inherited. The two specs declare
    // different schemas, so which document was read is visible in the tree.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("shared.yml"), TINY_SPEC).unwrap();
    std::fs::write(
        dir.path().join("own.yml"),
        TINY_SPEC.replace("Thing:", "Gadget:"),
    )
    .unwrap();
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./shared.yml\noutput: ./shared-out\npackage-name: sharedpkg\nproject-name: shared-dist\n\
         generators:\n  python:\n    spec: ./own.yml\n    output: ./own-out\n    package-name: ownpkg\n",
    )
    .unwrap();

    crozier_clean_env()
        .current_dir(dir.path())
        .args(["generate", "python"])
        .assert()
        .success()
        .stderr(predicate::str::contains("./own-out"));

    assert!(
        !dir.path().join("shared-out").exists(),
        "the generator's `output` should win over the shared one"
    );
    let root = dir.path().join("own-out/src/ownpkg");
    assert!(
        root.is_dir() && !dir.path().join("own-out/src/sharedpkg").exists(),
        "the generator's `package-name` should win over the shared one"
    );
    assert!(
        root.join("types/gadget.py").is_file() && !root.join("types/thing.py").exists(),
        "the generator's `spec` should be the document that was read"
    );
    assert!(
        std::fs::read_to_string(root.join("version.py"))
            .unwrap()
            .contains("metadata.version(\"shared-dist\")"),
        "a shared field the generator does not set is still inherited"
    );
}

#[test]
fn config_flag_beats_crozier_config_env_which_beats_discovery() {
    // Three candidate configs in one directory: the discovered `crozier.yml`, one
    // named by `CROZIER_CONFIG`, and one named by `--config`.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(dir.path().join("crozier.yml"), config_naming("discovered")).unwrap();
    std::fs::write(dir.path().join("from-env.yml"), config_naming("viaenv")).unwrap();
    std::fs::write(dir.path().join("from-flag.yml"), config_naming("viaflag")).unwrap();

    // `--config` wins outright, even with `CROZIER_CONFIG` set.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CONFIG", "./from-env.yml")
        .args(["--config", "./from-flag.yml", "generate", "python"])
        .assert()
        .success();
    assert!(dir.path().join("out/src/viaflag/types/thing.py").is_file());

    // Without the flag, `CROZIER_CONFIG` beats the discovered `crozier.yml`.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CONFIG", "./from-env.yml")
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(dir.path().join("out/src/viaenv/types/thing.py").is_file());

    // An empty `CROZIER_CONFIG` counts as unset, so discovery applies.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CONFIG", "")
        .args(["generate", "python"])
        .assert()
        .success();
    assert!(dir
        .path()
        .join("out/src/discovered/types/thing.py")
        .is_file());
}

#[test]
fn no_config_ignores_the_discovered_file_and_the_env_layer() {
    // `--no-config` is the hermetic escape hatch: neither the discovered
    // `crozier.yml` nor `CROZIER_*` may shape the run, only CLI flags and
    // built-in defaults. docs/configuration.md is the source of truth here; the
    // flag's own `--help` line still claims the env layer survives.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(dir.path().join("crozier.yml"), config_naming("fromconfig")).unwrap();

    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_PACKAGE_NAME", "fromenv")
        .env("CROZIER_OUTPUT", "./from-env")
        .args([
            "--no-config",
            "generate",
            "python",
            "--spec",
            "./api.yml",
            "--output",
            "./hermetic",
        ])
        .assert()
        .success();

    // The package name fell all the way through to the title-derived default.
    assert!(dir
        .path()
        .join("hermetic/src/tiny/types/thing.py")
        .is_file());
    assert!(
        !dir.path().join("hermetic/src/fromconfig").exists()
            && !dir.path().join("hermetic/src/fromenv").exists(),
        "--no-config must ignore both the config file and the env layer"
    );
    assert!(
        !dir.path().join("out").exists() && !dir.path().join("from-env").exists(),
        "--no-config must ignore the config's and the env's output directories"
    );
    // And with those layers gone there is nothing to generate from at all.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_SPEC", "./api.yml")
        .env("CROZIER_OUTPUT", "./out")
        .args(["--no-config", "generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("has no spec"));
}

#[test]
fn generators_run_in_declaration_order_not_sorted_order() {
    // `generators` is an ordered map: bare `crozier` runs every configured
    // generator in *file* order. Names chosen so declaration order differs from
    // both alphabetical and reverse-alphabetical order.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\ngenerators:\n  zeta:\n    output: ./z\n    package-name: z\n  \
         alpha:\n    output: ./a\n    package-name: a\n  middle:\n    output: ./m\n    package-name: m\n",
    )
    .unwrap();

    let out = crozier_clean_env()
        .current_dir(dir.path())
        .output()
        .expect("run crozier");
    assert!(out.status.success(), "bare crozier runs the configured set");
    let stderr = String::from_utf8(out.stderr).expect("utf-8 stderr");

    let positions: Vec<usize> = ["zeta:", "alpha:", "middle:"]
        .iter()
        .map(|name| {
            stderr
                .find(name)
                .unwrap_or_else(|| panic!("no summary line for {name} in:\n{stderr}"))
        })
        .collect();
    assert!(
        positions[0] < positions[1] && positions[1] < positions[2],
        "generators should run in declaration order (zeta, alpha, middle):\n{stderr}"
    );

    // Every one of them actually generated, each into its own output.
    assert!(dir.path().join("z/src/z/types/thing.py").is_file());
    assert!(dir.path().join("a/src/a/types/thing.py").is_file());
    assert!(dir.path().join("m/src/m/types/thing.py").is_file());

    // `crozier generate <name>` narrows the same set to one.
    let single = tempfile::tempdir().expect("tempdir");
    std::fs::write(single.path().join("api.yml"), TINY_SPEC).unwrap();
    std::fs::copy(
        dir.path().join("crozier.yml"),
        single.path().join("crozier.yml"),
    )
    .unwrap();
    crozier_clean_env()
        .current_dir(single.path())
        .args(["generate", "middle"])
        .assert()
        .success()
        // The single-generator summary is unprefixed.
        .stderr(predicate::str::contains("middle:").not());
    assert!(single.path().join("m/src/m/types/thing.py").is_file());
    assert!(
        !single.path().join("z").exists() && !single.path().join("a").exists(),
        "naming one generator must not run the others"
    );
}

/// Parse `crozier config` stdout into `(field, value, source)` rows for one
/// generator, so the user-visible table can be asserted as output.
fn config_rows(stdout: &str, generator: &str) -> Vec<(String, String, String)> {
    let header = format!("generator `{generator}`");
    stdout
        .lines()
        .skip_while(|line| *line != header)
        .skip(1)
        .take_while(|line| line.starts_with("  "))
        .map(|line| {
            let open = line.rfind('(').expect("a source label");
            let close = line.rfind(')').expect("a closed source label");
            let mut cells = line[..open].split_whitespace();
            let field = cells.next().expect("a field name").to_string();
            let value = cells.collect::<Vec<_>>().join(" ");
            (field, value, line[open + 1..close].to_string())
        })
        .collect()
}

#[test]
fn config_labels_the_layer_every_field_came_from() {
    // `crozier config` is the tool users reach for when the layering surprises
    // them, so its per-field source column is asserted verbatim.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    // Several fields are supplied by *more than one* layer, so the reported label
    // has to name the layer that actually won, not merely the only one present.
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\npackage-name: fromshared\nproject-name: shared-dist\naudiences: [internal]\n\
         reference:\n  command: ./reference.sh --all\n\
         generators:\n  python:\n    type: python\n    output: ./out\n    package-name: fromgenerator\n    audiences: [public]\n    extra-fields: forbid\n",
    )
    .unwrap();

    let out = crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CLIENT_CLASS_NAME", "FromEnv")
        .env("CROZIER_PROJECT_NAME", "env-dist")
        .env("CROZIER_AUDIENCE_STRICT", "true")
        .args(["config", "python"])
        .output()
        .expect("run crozier config");
    assert!(out.status.success());
    let stdout = String::from_utf8(out.stdout).expect("utf-8 stdout");

    // The discovered file is reported by path.
    assert!(
        stdout.starts_with("config files: ") && stdout.contains("crozier.yml"),
        "{stdout}"
    );
    let rows = config_rows(&stdout, "python");
    let expected = [
        ("type", "python", "generator"),
        ("spec", "./api.yml", "shared"),
        ("output", "./out", "generator"),
        // Also set at the shared top level: the generator's value wins.
        ("package-name", "fromgenerator", "generator"),
        // Also set at the shared top level: the environment wins.
        ("project-name", "env-dist", "env"),
        ("client-class-name", "FromEnv", "env"),
        // Also set at the shared top level: the generator's list wins.
        ("audiences", "public", "generator"),
        ("audience-strict", "true", "env"),
        ("fern-strict", "false", "default"),
        ("extra-fields", "forbid", "generator"),
        // Never unset: with no layer supplying it, the value a run would use.
        ("enum-type", "python-enums", "default"),
        ("default-max-retries", "2", "default"),
        ("layout", "packaged", "default"),
        // `crozier compare`'s command, from the shared block.
        ("reference.command", "./reference.sh --all", "shared"),
    ];
    assert_eq!(rows.len(), expected.len(), "{stdout}");
    for (row, want) in rows.iter().zip(expected) {
        assert_eq!(
            (row.0.as_str(), row.1.as_str(), row.2.as_str()),
            want,
            "{stdout}"
        );
    }

    // With every layer gone, each field is `(unset)` from the built-in default —
    // and `config` still succeeds, because it never runs generation.
    let bare = crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CLIENT_CLASS_NAME", "FromEnv")
        .args(["--no-config", "config"])
        .output()
        .expect("run crozier config --no-config");
    assert!(bare.status.success());
    let bare_stdout = String::from_utf8(bare.stdout).expect("utf-8 stdout");
    assert!(
        bare_stdout.contains("config files: none (built-in defaults)"),
        "{bare_stdout}"
    );
    for (field, value, source) in config_rows(&bare_stdout, "python") {
        assert_eq!(
            source, "default",
            "{field} should fall to the default layer"
        );
        let expected = match field.as_str() {
            "type" => "python",
            // Strict Fern compatibility is off unless a layer turns it on, and
            // `config` shows the `false` a run would use.
            "fern-strict" => "false",
            "enum-type" => "python-enums",
            "default-max-retries" => "2",
            "layout" => "packaged",
            _ => "(unset)",
        };
        assert_eq!(value, expected, "{field}");
    }
}

/// Which tree a run wrote under `out/`: `packaged` (`pyproject.toml` beside
/// `src/<package>/`) or `flat` (the package's modules at the root, no packaging).
fn written_layout(out: &Path, package: &str) -> &'static str {
    let packaged = out.join("pyproject.toml").is_file()
        && out.join(format!("src/{package}/__init__.py")).is_file();
    let flat = out.join("__init__.py").is_file()
        && out.join("types/thing.py").is_file()
        && !out.join("pyproject.toml").exists()
        && !out.join("src").exists();
    match (packaged, flat) {
        (true, false) => "packaged",
        (false, true) => "flat",
        _ => panic!("{} holds neither layout", out.display()),
    }
}

/// One case of the layout precedence journey: the layers present, the value the
/// documented order resolves to, and the source `crozier config` should name.
struct LayoutCase {
    config: &'static str,
    env: &'static [(&'static str, &'static str)],
    args: &'static [&'static str],
    winner: &'static str,
    source: &'static str,
}

#[test]
fn layout_resolves_flag_then_env_then_generator_then_shared_then_default() {
    // Each case peels one layer, and each winner differs from the layer below it,
    // so every step of the order is observable in the tree the run writes.
    let four = "spec: ./api.yml\nlayout: flat\ngenerators:\n  python:\n    output: ./out\n    package-name: tiny\n    layout: packaged\n";
    let generator_flat = "spec: ./api.yml\nlayout: packaged\ngenerators:\n  python:\n    output: ./out\n    package-name: tiny\n    layout: flat\n";
    let shared_flat = "spec: ./api.yml\nlayout: flat\ngenerators:\n  python:\n    output: ./out\n    package-name: tiny\n";
    let neither =
        "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    package-name: tiny\n";
    let cases = [
        // The flag beats an env var, a generator value and a shared value.
        LayoutCase {
            config: four,
            env: &[("CROZIER_LAYOUT", "flat")],
            args: &["--layout", "packaged"],
            winner: "packaged",
            source: "env",
        },
        // `CROZIER_LAYOUT` beats the generator's own value.
        LayoutCase {
            config: four,
            env: &[("CROZIER_LAYOUT", "flat")],
            args: &[],
            winner: "flat",
            source: "env",
        },
        // The generator's value beats the shared one.
        LayoutCase {
            config: four,
            env: &[],
            args: &[],
            winner: "packaged",
            source: "generator",
        },
        LayoutCase {
            config: generator_flat,
            env: &[],
            args: &[],
            winner: "flat",
            source: "generator",
        },
        // An empty `CROZIER_LAYOUT` counts as unset.
        LayoutCase {
            config: generator_flat,
            env: &[("CROZIER_LAYOUT", "")],
            args: &[],
            winner: "flat",
            source: "generator",
        },
        // The shared top-level value is inherited.
        LayoutCase {
            config: shared_flat,
            env: &[],
            args: &[],
            winner: "flat",
            source: "shared",
        },
        // No layer at all: the built-in `packaged`.
        LayoutCase {
            config: neither,
            env: &[],
            args: &[],
            winner: "packaged",
            source: "default",
        },
    ];

    for case in cases {
        let dir = layered_run(case.config, case.env, case.args);
        assert_eq!(
            written_layout(&dir.path().join("out"), "tiny"),
            case.winner,
            "config {:?}, env {:?}, args {:?}",
            case.config,
            case.env,
            case.args
        );

        // `crozier config` (which has no `--layout` flag) names the same layer
        // for the env/config layers the run above saw.
        let mut config = crozier_clean_env();
        config.current_dir(dir.path()).args(["config", "python"]);
        for (name, value) in case.env {
            config.env(name, value);
        }
        let out = config.output().expect("run crozier config");
        assert!(out.status.success());
        let stdout = String::from_utf8(out.stdout).expect("utf-8 stdout");
        let layout = config_rows(&stdout, "python")
            .into_iter()
            .find(|row| row.0 == "layout")
            .unwrap_or_else(|| panic!("no layout row in {stdout}"));
        let shown = if case.args.is_empty() {
            case.winner
        } else {
            "flat"
        };
        assert_eq!(
            (layout.1.as_str(), layout.2.as_str()),
            (shown, case.source),
            "{stdout}"
        );
    }
}

#[test]
fn a_bad_layout_is_refused_naming_the_value_and_its_layer() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();
    let run = |config: Option<&str>, env: Option<&str>, args: &[&str]| {
        match config {
            Some(text) => std::fs::write(dir.path().join("crozier.yml"), text).unwrap(),
            None => {
                let _ = std::fs::remove_file(dir.path().join("crozier.yml"));
            }
        }
        let mut cmd = crozier_clean_env();
        cmd.current_dir(dir.path())
            .env("CROZIER_SPEC", "./api.yml")
            .env("CROZIER_OUTPUT", "./out")
            .args(["generate", "python"])
            .args(args);
        if let Some(value) = env {
            cmd.env("CROZIER_LAYOUT", value);
        }
        cmd.assert()
            .failure()
            .stderr(predicate::str::contains("panicked").not())
    };

    // The flag: a usage error (exit 2, as for any bad flag value) naming the
    // flag, the value, and the accepted values.
    run(None, None, &["--layout", "nested"]).code(2).stderr(
        predicate::str::contains("'nested'")
            .and(predicate::str::contains("--layout"))
            .and(predicate::str::contains("packaged, flat")),
    );
    // The environment: the variable and the value.
    run(None, Some("nested"), &[])
        .code(1)
        .stderr(predicate::str::contains(
            "`CROZIER_LAYOUT` must be `packaged` or `flat`, got `nested`",
        ));
    // The file, at either level: the file, the value, and the accepted values.
    for config in [
        "layout: nested\n",
        "generators:\n  python:\n    layout: nested\n",
    ] {
        run(Some(config), None, &[]).code(1).stderr(
            predicate::str::contains("invalid config")
                .and(predicate::str::contains("crozier.yml"))
                .and(predicate::str::contains("nested"))
                .and(predicate::str::contains("`packaged` or `flat`")),
        );
    }
    // `--layout` is a per-generation flag, so it cannot be broadcast to two.
    std::fs::write(
        dir.path().join("crozier.yml"),
        "generators:\n  a:\n    output: ./a\n  b:\n    output: ./b\n",
    )
    .unwrap();
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_SPEC", "./api.yml")
        .args(["generate", "--layout", "flat"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains(
            "apply to a single generator, but 2",
        ));
    assert!(
        !dir.path().join("out").exists()
            && !dir.path().join("a").exists()
            && !dir.path().join("b").exists(),
        "a refused layout must not generate anything"
    );
}

#[test]
fn a_malformed_config_file_exits_nonzero_naming_the_file() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();

    // Broken YAML.
    std::fs::write(
        dir.path().join("crozier.yml"),
        "generators:\n  python:\n   - not: a map\n",
    )
    .unwrap();
    crozier_clean_env()
        .current_dir(dir.path())
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(
            predicate::str::contains("invalid config")
                .and(predicate::str::contains("crozier.yml"))
                .and(predicate::str::contains("panicked").not()),
        );

    // Structurally valid YAML with a misspelled field: the typo is named, not
    // silently ignored.
    std::fs::write(
        dir.path().join("crozier.yml"),
        "spec: ./api.yml\ngenerators:\n  python:\n    output: ./out\n    packge-name: oops\n",
    )
    .unwrap();
    crozier_clean_env()
        .current_dir(dir.path())
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(
            predicate::str::contains("invalid config").and(predicate::str::contains("packge-name")),
        );

    // `crozier config` reports the same failure rather than printing a half-read
    // config.
    crozier_clean_env()
        .current_dir(dir.path())
        .arg("config")
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("invalid config"));

    assert!(
        !dir.path().join("out").exists(),
        "a rejected config must not generate anything"
    );
}

#[test]
fn a_named_but_missing_config_file_exits_nonzero() {
    // A file the user *named* must exist; a merely-discovered one need not.
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC).unwrap();

    for args in [
        vec!["--config", "./no-such-config.yml", "generate", "python"],
        vec!["--config", "./no-such-config.yml", "config"],
    ] {
        crozier_clean_env()
            .current_dir(dir.path())
            .args(&args)
            .assert()
            .failure()
            .code(1)
            .stderr(
                predicate::str::contains("config file not found")
                    .and(predicate::str::contains("no-such-config.yml"))
                    .and(predicate::str::contains("panicked").not()),
            );
    }

    // The same path via `CROZIER_CONFIG` is equally an error.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_CONFIG", "./no-such-config.yml")
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("config file not found"));

    // But with no config file present and none named, discovery is simply empty —
    // the CLI flags carry the run.
    crozier_clean_env()
        .current_dir(dir.path())
        .args([
            "generate",
            "python",
            "--spec",
            "./api.yml",
            "--output",
            "./out",
        ])
        .assert()
        .success();
    assert!(dir.path().join("out/src/tiny/types/thing.py").is_file());
}

#[test]
fn init_writes_a_config_a_later_run_generates_from() {
    // The starter config is only useful if it actually runs: `init`, drop the spec
    // where it points, and bare `crozier` generates with zero further arguments.
    let dir = tempfile::tempdir().expect("tempdir");
    crozier_clean_env()
        .current_dir(dir.path())
        .arg("init")
        .assert()
        .success()
        .stderr(predicate::str::contains("wrote crozier.yml"));

    let written = std::fs::read_to_string(dir.path().join("crozier.yml")).expect("init wrote");
    let modeline = written.lines().next().expect("a modeline");
    let url = modeline
        .strip_prefix("# yaml-language-server: $schema=")
        .unwrap_or_else(|| panic!("unexpected modeline: {modeline}"));

    // `crozier schema` prints the very schema that modeline points at.
    let schema = crozier_clean_env()
        .arg("schema")
        .output()
        .expect("run crozier schema");
    assert!(schema.status.success());
    let printed: serde_json::Value =
        serde_json::from_slice(&schema.stdout).expect("schema stdout is valid JSON");
    assert_eq!(
        printed["$id"], url,
        "`init`'s modeline and `schema`'s $id must name the same document"
    );

    // The starter points at `./openapi.yml`; put one there and run it.
    std::fs::write(dir.path().join("openapi.yml"), TINY_SPEC).unwrap();
    crozier_clean_env()
        .current_dir(dir.path())
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));
    assert!(
        dir.path()
            .join("sdk/python/src/tiny/types/thing.py")
            .is_file(),
        "the starter config's `output`/defaults should generate as written"
    );
}

/// The `fern-strict` row `crozier config` prints for `generator` in `dir`, with
/// exactly the environment `env` sets, as `(value, source)`.
fn fern_strict_row(dir: &Path, env: &[(&str, &str)], args: &[&str]) -> (String, String) {
    let mut command = crozier_clean_env();
    command.current_dir(dir);
    for (name, value) in env {
        command.env(name, value);
    }
    let out = command
        .args(args)
        .arg("config")
        .output()
        .expect("run crozier config");
    let stdout = String::from_utf8(out.stdout).expect("utf-8 stdout");
    assert!(
        out.status.success(),
        "{stdout}{}",
        String::from_utf8_lossy(&out.stderr)
    );
    config_rows(&stdout, "python")
        .into_iter()
        .find(|(field, _, _)| field == "fern-strict")
        .map(|(_, value, source)| (value, source))
        .unwrap_or_else(|| panic!("`crozier config` printed no fern-strict row:\n{stdout}"))
}

#[test]
fn fern_strict_resolves_through_every_layer_through_the_binary() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), TINY_SPEC_WITH_OP).unwrap();
    let pair = |value: &str, source: &str| (value.to_string(), source.to_string());

    // No layer sets it: off, from the built-in default.
    assert_eq!(
        fern_strict_row(dir.path(), &[], &[]),
        pair("false", "default")
    );

    // The shared top level, then the generator's own entry over it.
    let config = dir.path().join("crozier.yml");
    std::fs::write(
        &config,
        "spec: ./api.yml\nfern-strict: true\ngenerators:\n  python:\n    output: ./out\n",
    )
    .unwrap();
    assert_eq!(
        fern_strict_row(dir.path(), &[], &[]),
        pair("true", "shared")
    );
    std::fs::write(
        &config,
        "spec: ./api.yml\nfern-strict: true\ngenerators:\n  python:\n    output: ./out\n    fern-strict: false\n",
    )
    .unwrap();
    assert_eq!(
        fern_strict_row(dir.path(), &[], &[]),
        pair("false", "generator")
    );

    // The environment beats both config layers, and `--no-config` drops it with
    // them rather than carrying it silently.
    let env_on = [("CROZIER_FERN_STRICT", "true")];
    assert_eq!(
        fern_strict_row(dir.path(), &env_on, &[]),
        pair("true", "env")
    );
    assert_eq!(
        fern_strict_row(dir.path(), &env_on, &["--no-config"]),
        pair("false", "default")
    );

    // A value that is not a boolean is refused before anything is written.
    crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_FERN_STRICT", "sometimes")
        .args(["generate", "python"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains(
            "`CROZIER_FERN_STRICT` must be `true` or `false`",
        ));
    assert!(!dir.path().join("out").exists());

    // The CLI flag is the top layer. Strict mode only decides whether an SDK is
    // written, so over a document no refusal class covers it writes the very
    // bytes the default mode does.
    for (label, flag, env) in [
        ("default", None, "false"),
        ("flag", Some("--fern-strict"), "false"),
        ("env", None, "true"),
    ] {
        crozier_clean_env()
            .current_dir(dir.path())
            .env("CROZIER_FERN_STRICT", env)
            .args(["generate", "python", "--output"])
            .arg(format!("./{label}"))
            .args(flag)
            .assert()
            .success()
            .stderr(predicate::str::contains("generated"));
    }
    let tree = |label: &str| {
        let root = dir.path().join(label);
        let mut files = walk_files(&root);
        files.sort();
        files
            .into_iter()
            .map(|rel| {
                let bytes = std::fs::read(root.join(&rel)).expect("read generated file");
                (rel, bytes)
            })
            .collect::<Vec<_>>()
    };
    let default_tree = tree("default");
    assert!(!default_tree.is_empty());
    assert_eq!(default_tree, tree("flag"), "--fern-strict changed the SDK");
    assert_eq!(
        default_tree,
        tree("env"),
        "CROZIER_FERN_STRICT changed the SDK"
    );
}

#[test]
fn init_starter_carries_fern_strict_and_the_schema_documents_it() {
    let dir = tempfile::tempdir().expect("tempdir");
    crozier_clean_env()
        .current_dir(dir.path())
        .arg("init")
        .assert()
        .success();
    let starter = std::fs::read_to_string(dir.path().join("crozier.yml")).expect("init wrote");
    assert!(
        starter
            .lines()
            .any(|line| line.starts_with("# fern-strict: false")),
        "the starter should show fern-strict at its shared top level:\n{starter}"
    );
    // As written, the starter leaves it off...
    assert_eq!(
        fern_strict_row(dir.path(), &[], &[]),
        ("false".into(), "default".into())
    );
    // ...and uncommenting the line turns it on for every generator.
    std::fs::write(
        dir.path().join("crozier.yml"),
        starter.replace("# fern-strict: false", "fern-strict: true"),
    )
    .unwrap();
    assert_eq!(
        fern_strict_row(dir.path(), &[], &[]),
        ("true".into(), "shared".into())
    );

    let schema = crozier_clean_env()
        .arg("schema")
        .output()
        .expect("run crozier schema");
    assert!(schema.status.success());
    let printed: serde_json::Value =
        serde_json::from_slice(&schema.stdout).expect("schema stdout is valid JSON");
    for at in [
        &printed["properties"]["fern-strict"],
        &printed["$defs"]["GeneratorSettings"]["properties"]["fern-strict"],
    ] {
        assert!(
            at["description"].as_str().is_some_and(|d| !d.is_empty())
                && at["type"]
                    .as_array()
                    .is_some_and(|t| t.contains(&"boolean".into())),
            "`crozier schema` should document fern-strict as a boolean: {at}"
        );
    }
}

/// A local HTTP server for the remote-`$ref` journeys.
///
/// crozier fetches a document a `$ref` names by absolute URL, so the only honest
/// test of that is a real request over a real socket. This serves a fixed
/// path → body map on an ephemeral loopback port, which keeps the journey
/// offline and free of the fixed-port collisions a shared port would invite.
struct LocalDocumentServer {
    base_url: String,
}

impl LocalDocumentServer {
    fn start(documents: &'static [(&'static str, &'static str)]) -> Self {
        let listener = std::net::TcpListener::bind("127.0.0.1:0")
            .expect("bind a loopback port for the server");
        let base_url = format!(
            "http://{}",
            listener.local_addr().expect("the bound address")
        );
        std::thread::spawn(move || {
            for stream in listener.incoming() {
                let Ok(mut stream) = stream else { break };
                Self::serve(&mut stream, documents);
            }
        });
        Self { base_url }
    }

    fn serve(stream: &mut std::net::TcpStream, documents: &[(&str, &str)]) {
        use std::io::{BufRead, BufReader, Write};
        let mut reader = BufReader::new(stream.try_clone().expect("clone the accepted socket"));
        let mut request_line = String::new();
        if reader.read_line(&mut request_line).is_err() {
            return;
        }
        // Drain the headers so the client sees a complete exchange.
        loop {
            let mut header = String::new();
            match reader.read_line(&mut header) {
                Ok(0) => break,
                Ok(_) if header.trim().is_empty() => break,
                Ok(_) => {}
                Err(_) => return,
            }
        }
        let path = request_line.split_whitespace().nth(1).unwrap_or_default();
        let response = match documents.iter().find(|(name, _)| *name == path) {
            Some((_, body)) => format!(
                "HTTP/1.1 200 OK\r\nContent-Type: text/yaml\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}",
                body.len()
            ),
            None => "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
                .to_string(),
        };
        let _ = stream.write_all(response.as_bytes());
        let _ = stream.flush();
    }
}

const REMOTE_REF_DOCUMENT: &str = "\
Address:
  type: string
Tags:
  type: array
  items:
    $ref: '#/components/schemas/Address'
";

/// A `$ref` naming another document by absolute URL is fetched and resolved.
///
/// Fern's importer opens the referenced document, and every other corpus spec is
/// self-contained, so this is the journey that proves crozier opens a second one
/// at all: the whole run goes through the real binary against a real HTTP server,
/// and the generated SDK is typed against schemas that exist only in the fetched
/// document. `Tags` also pins the transitive half — a pointer *inside* the fetched
/// document resolves against the root's components, as Fern resolves it.
#[test]
fn a_remote_url_ref_is_fetched_and_generates_against_the_referenced_document() {
    let server = LocalDocumentServer::start(&[("/schemas.yaml", REMOTE_REF_DOCUMENT)]);
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("openapi.yml");
    std::fs::write(
        &spec,
        format!(
            "openapi: 3.0.0\n\
             info: {{ title: Remote Ref API, version: '1.0' }}\n\
             paths:\n\
             \x20 /widgets:\n\
             \x20   get:\n\
             \x20     operationId: listWidgets\n\
             \x20     responses:\n\
             \x20       '200':\n\
             \x20         description: OK\n\
             \x20         content:\n\
             \x20           application/json:\n\
             \x20             schema: {{ $ref: '#/components/schemas/Widget' }}\n\
             components:\n\
             \x20 schemas:\n\
             \x20   Widget:\n\
             \x20     type: object\n\
             \x20     properties:\n\
             \x20       owner: {{ $ref: '#/components/schemas/Address' }}\n\
             \x20       tags: {{ $ref: '#/components/schemas/Tags' }}\n\
             \x20   Address:\n\
             \x20     $ref: {base}/schemas.yaml#/Address\n\
             \x20   Tags:\n\
             \x20     $ref: {base}/schemas.yaml#/Tags\n",
            base = server.base_url
        ),
    )
    .unwrap();

    let out = dir.path().join("sdk");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "fern"])
        .assert()
        .success();

    let types = out.join("src/fern/types");
    let address = std::fs::read_to_string(types.join("address.py")).expect("address.py");
    assert!(
        address.contains("Address = str"),
        "the fetched string schema should type the alias:\n{address}"
    );
    let tags = std::fs::read_to_string(types.join("tags.py")).expect("tags.py");
    assert!(
        tags.contains("Tags = typing.List[Address]"),
        "a pointer inside the fetched document resolves against the root:\n{tags}"
    );
    let widget = std::fs::read_to_string(types.join("widget.py")).expect("widget.py");
    assert!(
        widget.contains("owner: typing.Optional[Address] = None")
            && widget.contains("tags: typing.Optional[Tags] = None"),
        "the model should be typed against the fetched schemas:\n{widget}"
    );
}

/// A referenced document that cannot be fetched fails the run with an actionable
/// message rather than silently generating an SDK with the wrong types in it.
#[test]
fn a_remote_ref_that_cannot_be_fetched_fails_with_an_actionable_message() {
    let server = LocalDocumentServer::start(&[]);
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("openapi.yml");
    let reference = format!("{}/missing.yaml#/Address", server.base_url);
    std::fs::write(
        &spec,
        format!(
            "openapi: 3.0.0\n\
             info: {{ title: Remote Ref API, version: '1.0' }}\n\
             paths: {{}}\n\
             components:\n\
             \x20 schemas:\n\
             \x20   Address:\n\
             \x20     $ref: {reference}\n"
        ),
    )
    .unwrap();

    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("sdk"))
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not resolve remote $ref"))
        .stderr(predicate::str::contains(reference));
    assert!(
        !dir.path().join("sdk").exists(),
        "a failed fetch should write no SDK"
    );
}

#[test]
fn a_missing_relative_path_item_is_discarded_without_losing_other_endpoints() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("openapi.yml");
    let sdk = dir.path().join("sdk");
    std::fs::write(
        &spec,
        "openapi: 3.0.3\ninfo: {title: Ref API, version: '1'}\npaths:\n  /ping:\n    $ref: './parts.yaml#/item'\n  /live:\n    get:\n      operationId: getLive\n      responses:\n        '204': {description: No content}\n",
    )
    .unwrap();
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&sdk)
        .assert()
        .success();
    let reference = std::fs::read_to_string(sdk.join("reference.md")).expect("reference guide");
    assert!(reference.contains("get_live"), "{reference}");
    assert!(!reference.contains("get_ping"), "{reference}");
}

#[test]
fn relative_path_item_refs_report_missing_pointers_and_wrong_shapes() {
    for (document, reference, message) in [
        (
            "other: {}\n",
            "./parts.yaml#/item",
            "no Path Item at that pointer",
        ),
        ("item: []\n", "./parts.yaml#/item", "not a Path Item"),
    ] {
        let dir = tempfile::tempdir().expect("tempdir");
        let spec = dir.path().join("openapi.yml");
        std::fs::write(
            &spec,
            format!(
                "openapi: 3.0.3\ninfo: {{title: Ref API, version: '1'}}\npaths:\n  /ping:\n    $ref: '{reference}'\n"
            ),
        )
        .unwrap();
        std::fs::write(dir.path().join("parts.yaml"), document).unwrap();
        crozier()
            .args(["generate", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(dir.path().join("sdk"))
            .assert()
            .failure()
            .stderr(predicate::str::contains(message));
        assert!(!dir.path().join("sdk").exists());
    }
}

#[test]
fn relative_parameter_refs_report_missing_pointers_and_wrong_shapes() {
    for (document, message) in [
        ("other: {}\n", "no parameter at that pointer"),
        ("item: []\n", "not a parameter"),
    ] {
        let dir = tempfile::tempdir().expect("tempdir");
        let spec = dir.path().join("openapi.yml");
        std::fs::write(
            &spec,
            "openapi: 3.0.3\ninfo: {title: Ref API, version: '1'}\npaths:\n  /ping:\n    get:\n      operationId: ping\n      parameters:\n        - $ref: './params.yaml#/item'\n      responses:\n        '200': {description: OK}\n",
        )
        .unwrap();
        std::fs::write(dir.path().join("params.yaml"), document).unwrap();
        crozier()
            .args(["generate", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(dir.path().join("sdk"))
            .assert()
            .failure()
            .stderr(predicate::str::contains(message));
        assert!(!dir.path().join("sdk").exists());
    }
}

#[test]
fn an_absolute_path_item_ref_fetches_its_relative_parameter_sibling() {
    let server = LocalDocumentServer::start(&[
        (
            "/path.yaml",
            "item:\n  get:\n    operationId: getVersion\n    parameters:\n      - $ref: './params.yaml#/param'\n    responses:\n      '200': {description: OK}\n",
        ),
        (
            "/params.yaml",
            "param:\n  name: filter\n  in: query\n  schema: {type: string}\n",
        ),
    ]);
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("openapi.yml");
    std::fs::write(
        &spec,
        format!(
            "openapi: 3.0.3\ninfo: {{title: Remote Path, version: '1'}}\npaths:\n  /version:\n    $ref: '{}/path.yaml#/item'\n",
            server.base_url
        ),
    )
    .unwrap();
    let out = dir.path().join("sdk");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "fern"])
        .assert()
        .success();
    let client = std::fs::read_to_string(out.join("src/fern/client.py")).expect("client");
    assert!(
        client.contains("filter:"),
        "the remote parameter must reach the SDK: {client}"
    );
}

#[test]
fn relative_schema_refs_report_missing_files_pointers_and_wrong_shapes() {
    for (document, message) in [
        (None, "could not read"),
        (Some("Other: {type: string}\n"), "no node at that pointer"),
        (Some("Bad: []\n"), "not a schema"),
    ] {
        let dir = tempfile::tempdir().expect("tempdir");
        let spec = dir.path().join("openapi.yml");
        std::fs::write(
            &spec,
            "openapi: 3.0.3\ninfo: {title: Ref API, version: '1'}\npaths:\n  /ping:\n    get:\n      operationId: ping\n      responses:\n        '200':\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: './schemas.yaml#/Bad'\n",
        )
        .unwrap();
        if let Some(document) = document {
            std::fs::write(dir.path().join("schemas.yaml"), document).unwrap();
        }
        crozier()
            .args(["generate", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(dir.path().join("sdk"))
            .assert()
            .failure()
            .stderr(predicate::str::contains(message));
        assert!(!dir.path().join("sdk").exists());
    }
}

#[test]
fn paypal_catalog_products_matches_fern_output() {
    assert_committed_corpus_matches(&PAYPAL_CATALOG_PRODUCTS);
}

#[test]
fn paypal_catalog_products_recovers_from_missing_and_malformed_source() {
    let Some(source) = corpus_spec(PAYPAL_CATALOG_PRODUCTS.api) else {
        return;
    };
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.json");
    let output = dir.path().join("sdk");
    let command = || {
        let mut command = crozier();
        command
            .args(["generate", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
            ]);
        command
    };
    command()
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    std::fs::write(&spec, "{invalid JSON").unwrap();
    command().assert().failure().code(1);
    assert!(!output.exists());
    std::fs::copy(source, &spec).unwrap();
    command().assert().success();
    let golden = fixture_dir(PAYPAL_CATALOG_PRODUCTS.api).join("expected");
    let ledger = corpus_golden_ledger(
        departure_ledger(),
        &golden_path(&golden),
        &PAYPAL_CATALOG_PRODUCTS,
    )
    .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let context = Context::from_trees(&golden, &output);
    let mut observed = Vec::new();
    let checked = [
        "src/fern/types/four_hundred_details_item.py",
        "src/fern/types/error_default.py",
        "src/fern/types/bad_request_error_body.py",
        "src/fern/products/client.py",
        "src/fern/products/raw_client.py",
        "reference.md",
    ];
    for relative in checked {
        let actual = std::fs::read_to_string(output.join(relative)).unwrap();
        let expected = std::fs::read_to_string(golden.join(relative)).unwrap();
        let compared = compare_with_golden(&context, relative, &actual, &expected);
        assert!(compared.matches(), "{relative}: {:?}", compared.diff());
        observed.extend(observed_in(relative, &compared));
    }
    let failures = ledger.check(&observed, &|rel| checked.contains(&rel));
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

#[test]
fn truefoundry_trueforge_5adde28_matches_fern_output() {
    assert_committed_corpus_matches(&TRUEFOUNDRY_TRUEFORGE_5ADDE28);
}

#[test]
fn fergus_matches_fern_output() {
    assert_committed_corpus_matches(&FERGUS);
}

#[test]
fn groupe_psa_matches_fern_output() {
    assert_committed_corpus_matches(&GROUPE_PSA);
}

#[test]
fn timelyapp_matches_fern_output() {
    assert_committed_corpus_matches(&TIMELYAPP);
}

#[test]
fn nextgen_matches_fern_output() {
    assert_committed_corpus_matches(&NEXTGEN);
}

#[test]
fn auto_agent_protocol_matches_fern_output() {
    assert_committed_corpus_matches(&AUTO_AGENT_PROTOCOL);
}

#[test]
fn skool_matches_fern_output() {
    assert_committed_corpus_matches(&SKOOL);
}

#[test]
fn spendesk_matches_fern_output() {
    assert_committed_corpus_matches(&SPENDESK);
}

#[test]
fn billie_matches_fern_output() {
    assert_committed_corpus_matches(&BILLIE);
}

#[test]
fn alma_france_matches_fern_output() {
    assert_committed_corpus_matches(&ALMA_FRANCE);
}

#[test]
fn outreach_matches_fern_output() {
    assert_committed_corpus_matches(&OUTREACH);
}

#[test]
fn tally_matches_fern_output() {
    assert_committed_corpus_matches(&TALLY);
}

#[test]
fn billie_entry_matches_fern_output() {
    assert_committed_corpus_matches(&BILLIE_ENTRY);
}

#[test]
fn skool_entry_matches_fern_output() {
    assert_committed_corpus_matches(&SKOOL_ENTRY);
}

#[test]
fn timelyapp_entry_matches_fern_output() {
    assert_committed_corpus_matches(&TIMELYAPP_ENTRY);
}

#[test]
fn cradl_matches_fern_output() {
    assert_committed_corpus_matches(&CRADL);
}

#[test]
fn zulip_matches_fern_output() {
    assert_committed_corpus_matches(&ZULIP);
}

#[test]
fn zulip_jentic_matches_fern_output() {
    assert_committed_corpus_matches(&ZULIP_JENTIC);
}

#[test]
fn zulip_jentic_entry_matches_fern_output() {
    assert_committed_corpus_matches(&ZULIP_JENTIC_ENTRY);
}

#[test]
fn milvus_restful_v2_3_matches_fern_output() {
    assert_committed_corpus_matches(&MILVUS_RESTFUL_V2_3);
}

#[test]
fn milvus_restful_v2_4_matches_fern_output() {
    assert_committed_corpus_matches(&MILVUS_RESTFUL_V2_4);
}

#[test]
fn ramu_shogi_matches_fern_output() {
    assert_committed_corpus_matches(&RAMU_SHOGI);
}

#[test]
fn langchain_agent_protocol_matches_fern_output() {
    assert_committed_corpus_matches(&LANGCHAIN_AGENT_PROTOCOL);
}

#[test]
fn hse_matches_fern_output() {
    assert_committed_corpus_matches(&HSE);
}

#[test]
fn milvus_vector_operations_matches_fern_output() {
    assert_committed_corpus_matches(&MILVUS_VECTOR_OPERATIONS);
}

#[test]
fn mistle_control_plane_matches_fern_output() {
    assert_committed_corpus_matches(&MISTLE_CONTROL_PLANE);
}

#[test]
fn osparc_payments_matches_fern_output() {
    assert_committed_corpus_matches(&OSPARC_PAYMENTS);
}

#[test]
fn huatuo_node_matches_fern_output() {
    assert_committed_corpus_matches(&HUATUO_NODE);
}

#[test]
fn huatuo_server_matches_fern_output() {
    assert_committed_corpus_matches(&HUATUO_SERVER);
}

#[test]
fn huatuo_node_tree_matches_fern_output() {
    assert_committed_corpus_matches(&HUATUO_NODE_TREE);
}

#[test]
fn lootlog_battlelog_matches_fern_output() {
    assert_committed_corpus_matches(&LOOTLOG_BATTLELOG);
}

#[test]
fn ego_microservices_matches_fern_output() {
    assert_committed_corpus_matches(&EGO_MICROSERVICES);
}

#[test]
fn viskit_studio_matches_fern_output() {
    assert_committed_corpus_matches(&VISKIT_STUDIO);
}

#[test]
fn embedpdf_cloudpdf_matches_fern_output() {
    assert_committed_corpus_matches(&EMBEDPDF_CLOUDPDF);
}

#[test]
fn npq_registration_matches_fern_output() {
    assert_committed_corpus_matches(&NPQ_REGISTRATION);
}

#[test]
fn sim_logs_matches_fern_output() {
    assert_committed_corpus_matches(&SIM_LOGS);
}

#[test]
fn sim_tables_matches_fern_output() {
    assert_committed_corpus_matches(&SIM_TABLES);
}

#[test]
fn vellum_gateway_matches_fern_output() {
    assert_committed_corpus_matches(&VELLUM_GATEWAY);
}

#[test]
fn dot_ai_matches_fern_output() {
    assert_committed_corpus_matches(&DOT_AI);
}

#[test]
fn paloalto_code_technologies_matches_fern_output() {
    assert_committed_corpus_matches(&PALOALTO_CODE_TECHNOLOGIES);
}

#[test]
fn marimo_plugins_matches_fern_output() {
    assert_committed_corpus_matches(&MARIMO_PLUGINS);
}

#[test]
fn otoroshi_matches_fern_output() {
    assert_committed_corpus_matches(&OTOROSHI);
}

#[test]
fn standrig_matches_fern_output() {
    assert_committed_corpus_matches(&STANDRIG);
}

#[test]
fn mockserver_matches_fern_output() {
    assert_committed_corpus_matches(&MOCKSERVER);
}

#[test]
fn ideaconsult_enanomapper_matches_fern_output() {
    assert_committed_corpus_matches(&IDEACONSULT_ENANOMAPPER);
}

#[test]
fn openaire_graph_matches_fern_output() {
    assert_committed_corpus_matches(&OPENAIRE_GRAPH);
}

#[test]
fn qredence_fleet_rlm_matches_fern_output() {
    assert_committed_corpus_matches(&QREDENCE_FLEET_RLM);
}

#[test]
fn fiware_context_generator_matches_fern_output() {
    assert_committed_corpus_matches(&FIWARE_CONTEXT_GENERATOR);
}

#[test]
fn hasura_metadata_matches_fern_output() {
    assert_committed_corpus_matches(&HASURA_METADATA);
}

#[test]
fn zoonk_matches_fern_output() {
    assert_committed_corpus_matches(&ZOONK);
}

#[test]
fn openfoodfacts_taxonomy_editor_matches_fern_output() {
    assert_committed_corpus_matches(&OPENFOODFACTS_TAXONOMY_EDITOR);
}

#[test]
fn qontract_api_matches_fern_output() {
    assert_committed_corpus_matches(&QONTRACT_API);
}

#[test]
fn oal_example_matches_fern_output() {
    assert_committed_corpus_matches(&OAL_EXAMPLE);
}

#[test]
fn millenium_falcon_challenge_matches_fern_output() {
    assert_committed_corpus_matches(&MILLENIUM_FALCON_CHALLENGE);
}

#[test]
fn maximo_wxo_integration_matches_fern_output() {
    assert_committed_corpus_matches(&MAXIMO_WXO_INTEGRATION);
}

#[test]
fn mi_music_matches_fern_output() {
    assert_committed_corpus_matches(&MI_MUSIC);
}

#[test]
fn g4brym_download_manager_matches_fern_output() {
    assert_committed_corpus_matches(&G4BRYM_DOWNLOAD_MANAGER);
}

#[test]
fn opentosca_license_engine_matches_fern_output() {
    assert_committed_corpus_matches(&OPENTOSCA_LICENSE_ENGINE);
}

#[test]
fn chat_rest_api_matches_fern_output() {
    assert_committed_corpus_matches(&CHAT_REST_API);
}

#[test]
fn esp32_streamline_bridge_matches_fern_output() {
    assert_committed_corpus_matches(&ESP32_STREAMLINE_BRIDGE);
}

#[test]
fn cphos_ai_question_matches_fern_output() {
    assert_committed_corpus_matches(&CPHOS_AI_QUESTION);
}

#[test]
fn flask_example_heroku_matches_fern_output() {
    assert_committed_corpus_matches(&FLASK_EXAMPLE_HEROKU);
}

#[test]
fn oip_web_api_matches_fern_output() {
    assert_committed_corpus_matches(&OIP_WEB_API);
}

#[test]
fn breizhsport_catalogue_matches_fern_output() {
    assert_committed_corpus_matches(&BREIZHSPORT_CATALOGUE);
}

#[test]
fn protoform_conformance_matches_fern_output() {
    assert_committed_corpus_matches(&PROTOFORM_CONFORMANCE);
}

#[test]
fn ere_ps_app_matches_fern_output() {
    assert_committed_corpus_matches(&ERE_PS_APP);
}

#[test]
fn typescript_service_template_matches_fern_output() {
    assert_committed_corpus_matches(&TYPESCRIPT_SERVICE_TEMPLATE);
}

#[test]
fn apideck_ecosystem_client_class_name_matches_fern_output() {
    assert_committed_corpus_matches(&APIDECK_ECOSYSTEM_CLIENT_CLASS_NAME);
}

#[test]
fn yourbrand_ticketing_matches_fern_output() {
    assert_committed_corpus_matches(&YOURBRAND_TICKETING);
}

#[test]
fn peopledatalabs_matches_fern_output() {
    assert_committed_corpus_matches(&PEOPLEDATALABS);
}

#[test]
fn adyen_acs_notification_matches_fern_output() {
    assert_committed_corpus_matches(&ADYEN_ACS_NOTIFICATION);
}

#[test]
fn googleapis_monitoring_v1_matches_fern_output() {
    assert_committed_corpus_matches(&GOOGLEAPIS_MONITORING_V1);
}

#[test]
fn docu_goapiserver_matches_fern_output() {
    assert_committed_corpus_matches(&DOCU_GOAPISERVER);
}

#[test]
fn onevoice_matches_fern_output() {
    assert_committed_corpus_matches(&ONEVOICE);
}

#[test]
fn xfsc_oidc_identity_resolver_matches_fern_output() {
    assert_committed_corpus_matches(&XFSC_OIDC_IDENTITY_RESOLVER);
}

// ---------------------------------------------------------------------------
// The Fern refusal registry (`docs/fern-refusals/`): the classes of input Fern
// refuses, crashes on, or falsely reports success over, and what crozier does
// with each in its default and `--fern-strict` modes. See
// docs/fern-refusals/README.md for the contract this gate enforces.
// ---------------------------------------------------------------------------

const FERN_REFUSALS_DIR: &str = "docs/fern-refusals";
const FERN_REFUSAL_CLASSES_HEADER: &str = "class\tfamily\tfern_stage\tfern_exit\tdiagnostic\tdocuments\tstatus\tcrozier_diagnostic\tpopulation_strict";
const FERN_REFUSAL_DOCUMENTS_HEADER: &str = "digest\tsource\tlocator\trevision\trecorded_by\tfern_stage\tfern_exit\tfern_log\tclasses\tcrozier_exit\tcrozier_files\tcrozier_strict_exit";

/// One `classes.tsv` row, as far as the gate reads it.
struct RefusalClass {
    class: String,
    status: String,
    fern_exit: String,
    documents: String,
    crozier_diagnostic: String,
    population_strict: String,
}

/// What `documents.tsv` records for one class: the rows carrying it, and of
/// those the ones with a measured `crozier_strict_exit` and the ones it refused.
#[derive(Default)]
struct RefusalClassDocuments {
    carried: usize,
    measured: usize,
    refused: usize,
}

/// Whether the gate runs each `generate` class's `wire_test.py`. Running one
/// builds the SDK's Python environment from PyPI and runs `mypy` and `pytest`,
/// so the offline `check` tier skips it and the SDK-env tier runs it.
#[derive(Clone, Copy, PartialEq)]
enum WireTests {
    Skip,
    Run,
}

/// Every refusal class the registry declares holds: see [`fern_refusal_failures`].
/// Every condition but the `wire_test.py` runs, which
/// [`sdk_env_fern_refusal_wire_tests_hold`] adds.
#[test]
fn fern_refusal_classes_hold() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let mut failures = fern_refusal_failures(&registry, &crozier, WireTests::Skip);
    failures.extend(nested_items_required_control_failures(&registry, &crozier));
    assert!(
        failures.is_empty(),
        "{FERN_REFUSALS_DIR}/ does not hold:\n{}",
        failures.join("\n")
    );
}

/// A body-bearing HEAD fails before writing; removing the body recovers.
#[test]
fn head_request_body_refuses_then_recovers() {
    let source = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("docs/fern-refusals/head-request-body/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &source, strict).unwrap();
        assert!(
            refused_failures("head-request-body", &run, "HEAD /patina", strict).is_empty(),
            "{}",
            run.stderr
        );
        assert_eq!(run.stderr.lines().count(), 1, "{}", run.stderr);
    }
    let temp = tempfile::tempdir().unwrap();
    let control = temp.path().join("control.yml");
    let text = std::fs::read_to_string(source).unwrap();
    let start = text.find("      requestBody:").unwrap();
    let end = text.find("      responses:").unwrap();
    std::fs::write(&control, format!("{}{}", &text[..start], &text[end..])).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &control, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
    // An ignored HEAD generates nothing for its body, so it is not refused,
    // under either spelling of the ignore extension.
    for extension in ["x-crozier-ignore", "x-fern-ignore"] {
        let ignored = temp.path().join(format!("{extension}.yml"));
        let marked = text.replacen(
            "      operationId: inspect_patina\n",
            &format!("      operationId: inspect_patina\n      {extension}: true\n"),
            1,
        );
        assert_ne!(marked, text, "the probe's HEAD operation moved");
        std::fs::write(&ignored, marked).unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &ignored, strict).unwrap();
            assert_eq!(run.code, Some(0), "{extension}: {}", run.stderr);
            assert!(!run.files.is_empty(), "{extension}: wrote nothing");
        }
    }
}

/// crozier#358's one refused use site: a required property whose pointer,
/// naming no `properties`, reaches nothing (`Named/items` on an object with no
/// `items`). Pinned Fern fails to resolve it
/// (`unresolved-schema-reference/evaluation-logs/fern-nested-items-required.log`),
/// so the committed control is refused in both modes with exactly one line
/// naming the class and the pointer.
fn nested_items_required_control_failures(
    registry: &Path,
    generator: &dyn Fn() -> Command,
) -> Vec<String> {
    let control = registry
        .join("unresolved-schema-reference")
        .join("nested-items-required-control.yml");
    let mut failures = Vec::new();
    for strict in [false, true] {
        let run = match refusal_run(generator, &control, strict) {
            Ok(run) => run,
            Err(error) => {
                failures.push(format!("nested-items-required-control.yml: {error}"));
                continue;
            }
        };
        failures.extend(refused_failures(
            "unresolved-schema-reference",
            &run,
            "reference #/components/schemas/Named/items",
            strict,
        ));
        let lines = run.stderr.lines().count();
        if lines != 1 {
            failures.push(format!(
                "nested-items-required-control.yml: crozier's refusal (strict: {strict}) printed \
                 {lines} stderr lines; a refusal prints one: {}",
                run.stderr.trim()
            ));
        }
    }
    failures
}

/// Removing an unsupported required credential recovers generation; merely
/// declaring an unused cookie scheme is allowed, and strict mode changes no SDK
/// bytes on that accepted document.
#[test]
fn service_auth_refusal_recovers_when_security_is_removed() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let probe = registry.join("service-auth-undefined/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures("service-auth-undefined", &run, "security/session", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1, "{}", run.stderr);
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    std::fs::write(&repaired, text.replace("security:\n  - session: []\n", "")).unwrap();
    let normal = refusal_run(&crozier, &repaired, false).unwrap();
    let strict = refusal_run(&crozier, &repaired, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap(),
            "{file}"
        );
    }
}

#[test]
fn unsupported_version_refusal_recovers_with_openapi_31() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let probe = registry.join("unsupported-openapi-version/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures =
            refused_failures("unsupported-openapi-version", &run, "openapi 3.2.0", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1, "{}", run.stderr);
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    std::fs::write(&repaired, text.replace("openapi: 3.2.0", "openapi: 3.1.0")).unwrap();
    let normal = refusal_run(&crozier, &repaired, false).unwrap();
    let strict = refusal_run(&crozier, &repaired, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap(),
            "{file}"
        );
    }
}

#[test]
fn endpoint_auth_refusal_recovers_when_security_is_removed() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let probe = registry.join("endpoint-auth-undefined/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "endpoint-auth-undefined",
            &run,
            "GET /probe security/session",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1, "{}", run.stderr);
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    std::fs::write(
        &repaired,
        text.replace("      security:\n        - session: []\n", ""),
    )
    .unwrap();
    let normal = refusal_run(&crozier, &repaired, false).unwrap();
    let strict = refusal_run(&crozier, &repaired, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap(),
            "{file}"
        );
    }
}

#[test]
fn inherited_auth_in_a_mixed_service_names_the_private_endpoint() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let text = std::fs::read_to_string(registry.join("service-auth-undefined/probe.yml")).unwrap();
    let dir = tempfile::tempdir().unwrap();
    let probe = dir.path().join("openapi.yml");
    let text = text.replace(
        "components:\n",
        "  /public:\n    get:\n      operationId: publicProbe\n      security: []\n      responses:\n        '204': {description: No Content}\ncomponents:\n",
    );
    std::fs::write(&probe, &text).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "endpoint-auth-undefined",
            &run,
            "GET /probe security/session",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    std::fs::write(&probe, text.replace("security:\n  - session: []\n", "")).unwrap();
    let run = refusal_run(&crozier, &probe, true).unwrap();
    assert_eq!(run.code, Some(0), "{}", run.stderr);
    assert!(!run.files.is_empty());
}

/// The whole gate over the committed registry, each `generate` class's
/// `wire_test.py` included.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_fern_refusal_wire_tests_hold() {
    let registry = Path::new(env!("CARGO_MANIFEST_DIR")).join(FERN_REFUSALS_DIR);
    let failures = fern_refusal_failures(&registry, &crozier, WireTests::Run);
    assert!(
        failures.is_empty(),
        "{FERN_REFUSALS_DIR}/ does not hold:\n{}",
        failures.join("\n")
    );
}

/// Every way the refusal registry at `registry` fails its contract, each line
/// naming the class (or file) and the condition it breaks. `generator` builds
/// the command that stands for crozier — the real binary for the gate, and a
/// subprocess double wrapping it where a test needs behaviour crozier does not
/// have yet.
///
/// `classes.tsv` alone says which classes exist. Each row's `probe.yml` and
/// `fern-refusal.txt` must exist, the record must carry Contract A's five
/// fields at the corpus pin with a non-empty `diagnostic`, and nothing more is
/// asked of an `unevaluated` row. A `refuse` class's probe is refused with and
/// without `--fern-strict`; a `generate` class's probe generates by default, its
/// `wire_test.py` passes against that SDK, and it is refused under
/// `--fern-strict` with a line saying `fern-strict` caused it. Every
/// `documents.tsv` class id and every directory under the registry is a
/// `classes.tsv` row. `wire` says whether the `wire_test.py` runs.
fn fern_refusal_failures(
    registry: &Path,
    generator: &dyn Fn() -> Command,
    wire: WireTests,
) -> Vec<String> {
    let text = match std::fs::read_to_string(registry.join("classes.tsv")) {
        Ok(text) => text,
        Err(error) => return vec![format!("classes.tsv: cannot be read: {error}")],
    };
    let (classes, mut failures) = parse_refusal_classes(&text);
    let known: std::collections::BTreeSet<&str> =
        classes.iter().map(|class| class.class.as_str()).collect();

    match std::fs::read_dir(registry) {
        Ok(entries) => {
            let mut directories: Vec<String> = entries
                .filter_map(Result::ok)
                .filter(|entry| entry.path().is_dir())
                .map(|entry| entry.file_name().to_string_lossy().into_owned())
                .collect();
            directories.sort();
            for name in directories {
                if !known.contains(name.as_str()) {
                    failures.push(format!(
                        "{name}: is a directory under the registry but no classes.tsv row names it \
                         — add its row, or remove the directory"
                    ));
                }
            }
        }
        Err(error) => failures.push(format!("the registry cannot be listed: {error}")),
    }

    let carried = refusal_document_class_counts(registry, &known, &mut failures);
    for class in &classes {
        let recorded = carried.get(class.class.as_str());
        let count = recorded.map_or(0, |recorded| recorded.carried);
        if class.documents != count.to_string() {
            failures.push(format!(
                "{}: classes.tsv counts {} document(s), but {count} documents.tsv row(s) carry it",
                class.class, class.documents
            ));
        }
        if class.status != "unevaluated" {
            let measured = recorded.map_or_else(
                || "0/0".to_owned(),
                |recorded| format!("{}/{}", recorded.refused, recorded.measured),
            );
            if class.population_strict != measured {
                failures.push(format!(
                    "{}: classes.tsv population_strict is {}, but documents.tsv's \
                     crozier_strict_exit refuses {measured} of the rows that carry it",
                    class.class, class.population_strict
                ));
            }
        }
        failures.extend(refusal_class_failures(registry, class, generator, wire));
    }
    failures
}

/// The header, the column count, the sort order and each cell's vocabulary.
/// Rows that parse are returned even when a sibling failed, so one bad row
/// cannot hide another.
fn parse_refusal_classes(text: &str) -> (Vec<RefusalClass>, Vec<String>) {
    let mut failures = Vec::new();
    let mut lines = text.lines();
    if lines.next() != Some(FERN_REFUSAL_CLASSES_HEADER) {
        failures.push(format!(
            "classes.tsv: the header line must be exactly {FERN_REFUSAL_CLASSES_HEADER:?}"
        ));
    }
    let mut classes: Vec<RefusalClass> = Vec::new();
    for (index, line) in lines.enumerate() {
        let fields: Vec<&str> = line.split('\t').collect();
        let [class, family, fern_stage, fern_exit, diagnostic, documents, status, crozier_diagnostic, population_strict] =
            fields[..]
        else {
            failures.push(format!(
                "classes.tsv line {}: {} column(s); every row has the nine of the header",
                index + 2,
                fields.len()
            ));
            continue;
        };
        if let Some(previous) = classes
            .last()
            .filter(|previous| previous.class.as_str() >= class)
        {
            failures.push(format!(
                "{class}: classes.tsv rows must be sorted by class with no class twice; it follows {}",
                previous.class
            ));
        }
        let kebab = !class.is_empty()
            && !class.starts_with('-')
            && !class.ends_with('-')
            && !class.contains("--")
            && class
                .bytes()
                .all(|byte| byte.is_ascii_lowercase() || byte.is_ascii_digit() || byte == b'-');
        if !kebab {
            failures.push(format!("{class}: a class id is kebab-case"));
        }
        if !["names", "documents"].contains(&family) {
            failures.push(format!(
                "{class}: family `{family}` is not `names` or `documents`"
            ));
        }
        if !["check", "generate"].contains(&fern_stage) {
            failures.push(format!(
                "{class}: fern_stage `{fern_stage}` is not `check` or `generate`"
            ));
        }
        if fern_exit.parse::<i64>().is_err() {
            failures.push(format!(
                "{class}: fern_exit `{fern_exit}` is not an exit status"
            ));
        }
        if diagnostic.trim().is_empty() || diagnostic == "—" {
            failures.push(format!(
                "{class}: diagnostic is empty; it quotes Fern's phrase"
            ));
        }
        if documents.parse::<u64>().is_err() {
            failures.push(format!("{class}: documents `{documents}` is not a count"));
        }
        let evaluated = match status {
            "unevaluated" => false,
            "generate" | "refuse" => true,
            _ => {
                failures.push(format!(
                    "{class}: status `{status}` is not `unevaluated`, `generate` or `refuse`"
                ));
                false
            }
        };
        if evaluated {
            if crozier_diagnostic.trim().is_empty() || crozier_diagnostic == "—" {
                failures.push(format!(
                    "{class}: a `{status}` class names the substring crozier's refusal line carries in crozier_diagnostic"
                ));
            }
            let fraction = population_strict
                .split_once('/')
                .and_then(|(refused, total)| {
                    Some((refused.parse::<u64>().ok()?, total.parse::<u64>().ok()?))
                });
            if fraction.is_none_or(|(refused, total)| refused > total) {
                failures.push(format!(
                    "{class}: population_strict `{population_strict}` is not `<refused>/<total>`"
                ));
            }
        } else if status == "unevaluated" && (crozier_diagnostic != "—" || population_strict != "—")
        {
            failures.push(format!(
                "{class}: an `unevaluated` class carries `—` in crozier_diagnostic and population_strict"
            ));
        }
        classes.push(RefusalClass {
            class: class.to_string(),
            status: status.to_string(),
            fern_exit: fern_exit.to_string(),
            documents: documents.to_string(),
            crozier_diagnostic: crozier_diagnostic.to_string(),
            population_strict: population_strict.to_string(),
        });
    }
    (classes, failures)
}

/// `documents.tsv`'s header and order, and per class how many rows carry it and
/// how their `crozier_strict_exit` reads; a class id that is no `classes.tsv` row
/// is a failure.
fn refusal_document_class_counts<'a>(
    registry: &Path,
    known: &std::collections::BTreeSet<&'a str>,
    failures: &mut Vec<String>,
) -> std::collections::BTreeMap<&'a str, RefusalClassDocuments> {
    let mut counts = std::collections::BTreeMap::new();
    let text = match std::fs::read_to_string(registry.join("documents.tsv")) {
        Ok(text) => text,
        Err(error) => {
            failures.push(format!("documents.tsv: cannot be read: {error}"));
            return counts;
        }
    };
    let mut lines = text.lines();
    if lines.next() != Some(FERN_REFUSAL_DOCUMENTS_HEADER) {
        failures.push(format!(
            "documents.tsv: the header line must be exactly {FERN_REFUSAL_DOCUMENTS_HEADER:?}"
        ));
    }
    let mut previous: Option<&str> = None;
    for (index, line) in lines.enumerate() {
        let fields: Vec<&str> = line.split('\t').collect();
        if fields.len() != 12 {
            failures.push(format!(
                "documents.tsv line {}: {} column(s); every row has the twelve of the header",
                index + 2,
                fields.len()
            ));
            continue;
        }
        let digest = fields[0];
        if previous.is_some_and(|previous| previous >= digest) {
            failures.push(format!(
                "documents.tsv line {}: rows must be sorted by digest with no digest twice",
                index + 2
            ));
        }
        previous = Some(digest);
        if fields[8].is_empty() {
            failures.push(format!("{digest}: documents.tsv carries no class"));
        }
        for id in fields[8].split(',').filter(|id| !id.is_empty()) {
            match known.get(id) {
                Some(class) => {
                    let recorded: &mut RefusalClassDocuments = counts.entry(*class).or_default();
                    recorded.carried += 1;
                    if fields[11] != "—" {
                        recorded.measured += 1;
                        recorded.refused += usize::from(fields[11] == "1");
                    }
                }
                None => failures.push(format!(
                    "{id}: documents.tsv row {digest} carries it, but it is not a classes.tsv row"
                )),
            }
        }
    }
    counts
}

/// One class's files, record and — once evaluated — crozier's behaviour over its probe.
fn refusal_class_failures(
    registry: &Path,
    class: &RefusalClass,
    generator: &dyn Fn() -> Command,
    wire: WireTests,
) -> Vec<String> {
    let id = class.class.as_str();
    let dir = registry.join(id);
    let probe = dir.join("probe.yml");
    let record = dir.join("fern-refusal.txt");
    let mut failures = Vec::new();
    if !probe.is_file() {
        failures.push(format!("{id}: its probe {id}/probe.yml is missing"));
    }
    match std::fs::read_to_string(&record) {
        Ok(text) => failures.extend(refusal_record_failures(id, &text, &class.fern_exit)),
        Err(_) => failures.push(format!(
            "{id}: its Fern record {id}/fern-refusal.txt is missing"
        )),
    }
    let wire_test = dir.join("wire_test.py");
    if class.status == "generate" && !wire_test.is_file() {
        failures.push(format!(
            "{id}: a `generate` class carries {id}/wire_test.py"
        ));
    } else if class.status != "generate" && wire_test.exists() {
        failures.push(format!(
            "{id}: {id}/wire_test.py is present, but only a `generate` class carries one"
        ));
    }
    if class.status != "unevaluated" && !dir.join("evaluation.md").is_file() {
        failures.push(format!(
            "{id}: an evaluated class carries {id}/evaluation.md"
        ));
    }
    if class.status == "unevaluated" || !probe.is_file() {
        return failures;
    }

    let diagnostic = class.crozier_diagnostic.as_str();
    match class.status.as_str() {
        "refuse" => {
            for strict in [false, true] {
                match refusal_run(generator, &probe, strict) {
                    Ok(run) => failures.extend(refused_failures(id, &run, diagnostic, false)),
                    Err(error) => failures.push(format!("{id}: {error}")),
                }
            }
        }
        "generate" => {
            match refusal_run(generator, &probe, false) {
                Ok(run) if run.code == Some(0) && !run.files.is_empty() => {
                    if wire == WireTests::Run {
                        failures.extend(wire_test_failures(id, &wire_test, &run.target, &probe));
                    }
                }
                Ok(run) => failures.push(format!(
                    "{id}: a `generate` class's probe is refused by default (exit {}), where \
                     crozier should generate: {}",
                    exit_label(run.code),
                    run.stderr.trim()
                )),
                Err(error) => failures.push(format!("{id}: {error}")),
            }
            match refusal_run(generator, &probe, true) {
                Ok(run) => failures.extend(refused_failures(id, &run, diagnostic, true)),
                Err(error) => failures.push(format!("{id}: {error}")),
            }
        }
        _ => {}
    }
    failures
}

/// A class's `fern-refusal.txt`: Contract A's five fields in order, at the
/// corpus pin, with Fern's non-empty phrase and the exit `classes.tsv` states.
/// A false success records exit 0, so the exit is held to the row rather than
/// to non-zero.
fn refusal_record_failures(id: &str, text: &str, fern_exit: &str) -> Vec<String> {
    let mut failures = Vec::new();
    let fields: Vec<(&str, &str)> = text
        .lines()
        .map(|line| line.split_once(": ").unwrap_or((line, "")))
        .collect();
    let names: Vec<&str> = fields.iter().map(|(name, _)| *name).collect();
    if names != REFUSAL_FIELDS {
        failures.push(format!(
            "{id}: fern-refusal.txt carries fields {names:?}; it carries exactly \
             {REFUSAL_FIELDS:?}, in that order and spelling"
        ));
    }
    let value = |name: &str| {
        fields
            .iter()
            .find(|(field, _)| *field == name)
            .map(|(_, value)| value.trim())
    };
    let (cli_pin, sdk_pin) = probe_fern_pins();
    for (name, pin) in [
        ("fern_cli_version", cli_pin.as_str()),
        ("fern_python_sdk_version", sdk_pin.as_str()),
    ] {
        if value(name) != Some(pin) {
            failures.push(format!(
                "{id}: fern-refusal.txt's {name} is `{}`, but the corpus pins `{pin}`",
                value(name).unwrap_or("")
            ));
        }
    }
    if value("diagnostic").is_none_or(str::is_empty) {
        failures.push(format!(
            "{id}: fern-refusal.txt's diagnostic is empty; it quotes the phrase Fern printed"
        ));
    }
    if let Some(exit) = value("generate_exit").filter(|exit| *exit != fern_exit) {
        failures.push(format!(
            "{id}: fern-refusal.txt records generate_exit `{exit}`, but classes.tsv's fern_exit is `{fern_exit}`"
        ));
    }
    failures
}

/// One crozier run over a probe, into a fresh output directory it may not create.
struct RefusalRun {
    code: Option<i32>,
    stderr: String,
    files: Vec<String>,
    target: PathBuf,
    _out: tempfile::TempDir,
}

fn exit_label(code: Option<i32>) -> String {
    code.map_or_else(|| "without a status".to_string(), |code| code.to_string())
}

/// crozier over `probe` exactly as a user runs it — hermetic (`--no-config`, no
/// `CROZIER_*` override), with or without `--fern-strict` — keeping the output
/// directory so what it wrote can be counted.
fn refusal_run(
    generator: &dyn Fn() -> Command,
    probe: &Path,
    strict: bool,
) -> Result<RefusalRun, String> {
    let out = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let target = out.path().join("sdk");
    let mut command = generator();
    for name in CROZIER_ENV_VARS {
        command.env_remove(name);
    }
    let result = command
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(probe)
        .arg("--output")
        .arg(&target)
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ])
        .args(strict.then_some("--fern-strict"))
        .output()
        .map_err(|error| format!("could not run crozier: {error}"))?;
    let files = if target.exists() {
        parity::walk_files(&target)?
    } else {
        Vec::new()
    };
    Ok(RefusalRun {
        code: result.status.code(),
        stderr: String::from_utf8_lossy(&result.stderr).into_owned(),
        files,
        target,
        _out: out,
    })
}

/// Whether one run is a refusal in the contract's sense: exit 1, nothing
/// written, and one stderr line carrying the class id and `diagnostic` — and,
/// when strict mode alone caused it, saying `fern-strict` did.
fn refused_failures(
    id: &str,
    run: &RefusalRun,
    diagnostic: &str,
    strict_caused: bool,
) -> Vec<String> {
    let mode = if strict_caused {
        "under --fern-strict"
    } else {
        "in its mode"
    };
    let mut failures = Vec::new();
    if run.code == Some(0) {
        failures.push(format!(
            "{id}: crozier generated from the probe {mode}; the class says it is refused \
             ({} file(s) written)",
            run.files.len()
        ));
        return failures;
    }
    if run.code != Some(1) {
        failures.push(format!(
            "{id}: crozier's refusal {mode} exited {}; a refusal exits 1",
            exit_label(run.code)
        ));
    }
    if !run.files.is_empty() {
        failures.push(format!(
            "{id}: crozier's refusal {mode} wrote {} file(s) to the output directory ({}); a \
             refusal writes nothing",
            run.files.len(),
            run.files.join(", ")
        ));
    }
    match run.stderr.lines().find(|line| line.contains(diagnostic)) {
        None => failures.push(format!(
            "{id}: crozier's refusal {mode} printed no line containing crozier_diagnostic \
             {diagnostic:?}; it printed: {}",
            run.stderr.trim()
        )),
        Some(line) => {
            if !line.contains(id) {
                failures.push(format!(
                    "{id}: crozier's refusal line {mode} does not name the class: {line}"
                ));
            }
            if strict_caused && !line.contains("fern-strict") {
                failures.push(format!(
                    "{id}: crozier's refusal line under --fern-strict does not say fern-strict \
                     caused it: {line}"
                ));
            }
        }
    }
    failures
}

/// Run a `generate` class's `wire_test.py` against crozier's default SDK for its
/// probe, in an environment holding exactly what that SDK's `pyproject.toml`
/// declares (its pinned `mypy` among it).
fn wire_test_failures(id: &str, wire_test: &Path, sdk: &Path, probe: &Path) -> Vec<String> {
    let py = match sdk_python_env(&sdk.join("pyproject.toml")) {
        Ok(py) => py,
        Err(reason) => {
            return vec![format!(
                "{id}: wire_test.py cannot run, because the SDK's Python environment is \
                 unavailable: {reason}"
            )];
        }
    };
    let (mypy_cache, _cache_lock) = match lock_sdk_mypy_cache(&py) {
        Ok(cache) => cache,
        Err(reason) => return vec![format!("{id}: wire_test.py cannot run: {reason}")],
    };
    let class_dir = wire_test.parent().unwrap_or(wire_test);
    let result = std::process::Command::new(&py)
        .args(["-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir"])
        .arg(class_dir)
        .arg(wire_test)
        .env("CROZIER_SDK_DIR", sdk)
        .env("CROZIER_SDK_SRC", sdk.join("src"))
        .env("CROZIER_PROBE", probe)
        .env("MYPY_CACHE_DIR", &mypy_cache)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output();
    match result {
        Ok(output) if output.status.success() => Vec::new(),
        Ok(output) => vec![format!(
            "{id}: wire_test.py failed against crozier's default SDK for the probe:\n{}{}",
            String::from_utf8_lossy(&output.stdout),
            String::from_utf8_lossy(&output.stderr)
        )],
        Err(error) => vec![format!("{id}: could not run wire_test.py: {error}")],
    }
}

/// The pip requirements a generated `pyproject.toml` declares — its runtime
/// dependencies, its optional extras, and its dev group (the pinned `mypy`
/// among them) — translated from Poetry's constraint syntax. `python` itself is
/// the interpreter, not a requirement.
fn pyproject_requirements(pyproject: &str) -> Vec<String> {
    const SECTIONS: [&str; 2] = [
        "[tool.poetry.dependencies]",
        "[tool.poetry.group.dev.dependencies]",
    ];
    let mut requirements = Vec::new();
    let mut in_section = false;
    for line in pyproject.lines() {
        let line = line.trim();
        if line.starts_with('[') {
            in_section = SECTIONS.contains(&line);
            continue;
        }
        let Some((name, value)) = line.split_once('=').filter(|_| in_section) else {
            continue;
        };
        let name = name.trim();
        if name.is_empty() || name == "python" {
            continue;
        }
        let value = value.trim();
        let quoted = |text: &str| text.split('"').nth(1).map(str::to_string);
        let constraint = if value.starts_with('{') {
            value
                .split_once("version")
                .and_then(|(_, rest)| quoted(rest))
        } else {
            quoted(value)
        };
        let Some(constraint) = constraint else {
            continue;
        };
        requirements.push(format!("{name}{}", pip_constraint(&constraint)));
    }
    requirements
}

/// One Poetry constraint as a pip specifier: `^1.2.3` is `>=1.2.3,<2` (`^0.2.3`
/// is `>=0.2.3,<0.3`), a bare version is exact, and anything else is already a
/// comparison.
fn pip_constraint(constraint: &str) -> String {
    let constraint: String = constraint.chars().filter(|c| !c.is_whitespace()).collect();
    if let Some(version) = constraint.strip_prefix('^') {
        let parts: Vec<u64> = version
            .split('.')
            .map_while(|part| part.parse().ok())
            .collect();
        let upper = match parts.as_slice() {
            [0, minor, ..] => format!("0.{}", minor + 1),
            [major, ..] => (major + 1).to_string(),
            [] => return format!(">={version}"),
        };
        return format!(">={version},<{upper}");
    }
    if constraint.starts_with(|c: char| c.is_ascii_digit()) {
        return format!("=={constraint}");
    }
    constraint
}

/// Prepare (creating and caching) a virtualenv holding what a generated SDK's
/// `pyproject.toml` declares, and return its interpreter. Cached under the
/// [`python_env_root`] by a digest of the requirement list, so a change to the
/// pins builds a fresh one. `uv` is used when present, else `venv` + `pip`.
fn sdk_python_env(pyproject: &Path) -> Result<PathBuf, String> {
    sdk_python_env_in(&python_env_root(), pyproject, uv_available())
}

/// [`sdk_python_env`] under `root`, building with `uv` or with `venv` + `pip`.
fn sdk_python_env_in(root: &Path, pyproject: &Path, use_uv: bool) -> Result<PathBuf, String> {
    let text = std::fs::read_to_string(pyproject)
        .map_err(|error| format!("cannot read {}: {error}", pyproject.display()))?;
    let requirements = pyproject_requirements(&text);
    if !requirements.iter().any(|r| r.starts_with("mypy==")) {
        return Err(format!("{} declares no pinned mypy", pyproject.display()));
    }
    cached_python_env(root, "crozier-sdk-env", &requirements, use_uv)
}

/// Prepare (creating and caching) a virtualenv holding exactly `requirements`
/// under `root`, named `{prefix}-{digest}` by a digest of the list, and return
/// its interpreter. Built with `uv` or with `venv` + `pip`.
fn cached_python_env(
    root: &Path,
    prefix: &str,
    requirements: &[String],
    use_uv: bool,
) -> Result<PathBuf, String> {
    let base = python_interpreter().ok_or("no python3/python on PATH")?;
    let key = sha256_hex(requirements.join("\n").as_bytes());
    let venv = root.join(format!("{prefix}-{}", &key[..16]));
    let venv_py = venv_python(&venv);
    let ready = venv.join(".crozier-ready");
    // Tests run in parallel processes and threads, and all of them want this
    // one environment: whoever holds the lock builds it, the rest wait and then
    // find it ready. A directory left without the marker is a build that died
    // part-way, so it is cleared rather than built over.
    let lock = hold_lock(&root.join(format!("{prefix}-{}.lock", &key[..16])))?;
    if venv_py.exists() && ready.is_file() {
        return Ok(venv_py);
    }
    if venv.exists() {
        std::fs::remove_dir_all(&venv)
            .map_err(|error| format!("cannot clear partial {}: {error}", venv.display()))?;
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
    if use_uv {
        let mut venv_cmd = std::process::Command::new("uv");
        venv_cmd.args(["venv", "--allow-existing"]).arg(&venv);
        run(venv_cmd, "uv venv")?;
        let mut install = std::process::Command::new("uv");
        install
            .args(["pip", "install", "--python"])
            .arg(&venv_py)
            .args(requirements);
        run(install, "uv pip install")?;
    } else {
        let mut venv_cmd = std::process::Command::new(base);
        venv_cmd.args(["-m", "venv"]).arg(&venv);
        run(venv_cmd, "python -m venv")?;
        let mut install = std::process::Command::new(&venv_py);
        install.args(["-m", "pip", "install"]).args(requirements);
        run(install, "pip install")?;
    }
    std::fs::write(&ready, requirements.join("\n"))
        .map_err(|error| format!("cannot mark {} ready: {error}", venv.display()))?;
    drop(lock);
    Ok(venv_py)
}

/// Open `path` and hold an exclusive lock on it until the returned file drops.
/// The lock is the OS's, so it serializes threads and processes alike and is
/// released if the holder dies.
fn hold_lock(path: &Path) -> Result<std::fs::File, String> {
    let file = std::fs::OpenOptions::new()
        .create(true)
        .truncate(false)
        .write(true)
        .open(path)
        .map_err(|error| format!("cannot open lock {}: {error}", path.display()))?;
    file.lock()
        .map_err(|error| format!("cannot lock {}: {error}", path.display()))?;
    Ok(file)
}

/// Concurrent tests share one cached SDK environment, so its first build is
/// raced: several callers asking for the same fresh environment at once (as the
/// refusal-gate journeys do under the parallel runner) each get a working
/// interpreter, over both builders.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_survives_concurrent_first_use() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, TINY_SPEC_WITH_OP).unwrap();
    let sdk = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&sdk)
        .args(["--package-name", "fern"])
        .assert()
        .success();
    let pyproject = sdk.join("pyproject.toml");
    let builders: &[bool] = if uv_available() {
        &[false, true]
    } else {
        &[false]
    };
    for &use_uv in builders {
        let root = tempfile::tempdir().expect("env root");
        let results: Vec<Result<PathBuf, String>> = std::thread::scope(|scope| {
            let callers: Vec<_> = (0..4)
                .map(|_| scope.spawn(|| sdk_python_env_in(root.path(), &pyproject, use_uv)))
                .collect();
            callers
                .into_iter()
                .map(|caller| caller.join().expect("caller panicked"))
                .collect()
        });
        let builder = if use_uv { "uv" } else { "venv + pip" };
        for result in &results {
            let py = result
                .as_ref()
                .unwrap_or_else(|reason| panic!("a concurrent {builder} build failed: {reason}"));
            let status = std::process::Command::new(py)
                .args(["-c", "import mypy, pydantic, httpx"])
                .status()
                .expect("run the environment's interpreter");
            assert!(
                status.success(),
                "{builder}: {} cannot import the SDK's pins",
                py.display()
            );
        }
    }
}

/// The `#[ignore]` reason that puts a journey in the SDK Python-environment
/// tier, which `just test-sdk-env` selects by the `sdk_env_` name prefix.
const SDK_ENV_TIER_IGNORE: &str = "#[ignore = \"SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`\"]";

/// What a test calls to build the SDK's Python environment or run a wire test in it.
const SDK_ENV_CALLS: [&str; 4] = [
    "sdk_python_env(",
    "sdk_python_env_in(",
    "runtime_python_env(",
    "WireTests::Run",
];

/// The offline tier never builds the SDK's Python environment: every test that
/// reaches one (or runs the gate's `wire_test.py`) is an `sdk_env_` journey
/// carrying the tier's `#[ignore]`, and every `sdk_env_` test carries it, so
/// `just test-sdk-env` runs each of them and `test-e2e` none.
#[test]
fn only_the_sdk_env_tier_builds_the_sdk_python_environment() {
    let source = include_str!("e2e.rs");
    let mut offending = Vec::new();
    for chunk in source.split("\n#[test]\n").skip(1) {
        let Some(name) = chunk
            .split_once("fn ")
            .and_then(|(_, rest)| rest.split_once('('))
            .map(|(name, _)| name)
        else {
            continue;
        };
        let body = chunk.split_once("\n}\n").map_or(chunk, |(body, _)| body);
        let ignored = chunk.starts_with(SDK_ENV_TIER_IGNORE);
        let reaches_env = SDK_ENV_CALLS.iter().any(|call| body.contains(call));
        if name.starts_with("sdk_env_") != ignored || (reaches_env && !ignored) {
            offending.push(name);
        }
    }
    assert!(
        offending.is_empty(),
        "these tests build the SDK Python environment outside its tier, or are named \
         `sdk_env_` without its `{SDK_ENV_TIER_IGNORE}`: {offending:?}"
    );
}

/// The journeys that build or reuse a cached Python environment, run as
/// concurrent processes of this test binary the way the parallel runner and
/// two checkouts on one host run them, over a root no run has built in yet: two
/// copies each of the runtime wire suite and the SDK type-check race to build
/// the runtime venv and the SDK env, and every one passes.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_journeys_survive_concurrent_first_use() {
    const JOURNEYS: [&str; 2] = [
        "sdk_env_crozier_matches_fern_runtime_behavior",
        "sdk_env_generated_sdk_typechecks_clean_under_its_own_mypy_pin",
    ];
    let root = tempfile::tempdir().expect("env root");
    let binary = std::env::current_exe().expect("the e2e test binary");
    let runs: Vec<(&str, std::process::Child)> = JOURNEYS
        .iter()
        .chain(JOURNEYS.iter())
        .map(|journey| {
            let child = std::process::Command::new(&binary)
                .args([*journey, "--exact", "--ignored", "--test-threads", "1"])
                .env("CROZIER_TEST_ENV_ROOT", root.path())
                .stdout(std::process::Stdio::piped())
                .stderr(std::process::Stdio::piped())
                .spawn()
                .expect("spawn a journey");
            (*journey, child)
        })
        .collect();
    let mut failures = Vec::new();
    for (journey, child) in runs {
        let output = child.wait_with_output().expect("wait for a journey");
        let stdout = String::from_utf8_lossy(&output.stdout);
        if !output.status.success() || !stdout.contains("1 passed") {
            failures.push(format!(
                "{journey} failed under concurrent first use:\n{stdout}{}",
                String::from_utf8_lossy(&output.stderr)
            ));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n"));
    assert!(
        root.path()
            .join("crozier-runtime-venv-v2/.crozier-ready")
            .is_file(),
        "the journeys did not build the runtime venv under the fresh root"
    );
}

/// The `mypy` cache kept beside an SDK environment, so repeated runs re-check
/// only what changed rather than the whole standard library and pydantic, and
/// the lock a run holds while it uses it: concurrent `mypy` runs replacing the
/// same cache files fail on Windows, so they take turns.
fn lock_sdk_mypy_cache(py: &Path) -> Result<(PathBuf, std::fs::File), String> {
    let env = py
        .parent()
        .and_then(Path::parent)
        .map_or_else(std::env::temp_dir, Path::to_path_buf);
    let lock = hold_lock(&env.join("mypy-cache.lock"))?;
    Ok((env.join("mypy-cache"), lock))
}

#[test]
fn pyproject_requirements_translate_poetry_constraints() {
    let text = "[tool.poetry.dependencies]\npython = \"^3.10\"\naiohttp = { version = \">=3.14.1,<4\", optional = true, python = \">=3.10\"}\nhttpx-aiohttp = { version = \"0.1.8\", optional = true}\npydantic = \">= 1.9.2\"\n\n[tool.poetry.group.dev.dependencies]\nmypy = \"==1.13.0\"\npytest = \"^9.0.3\"\nlegacy = \"^0.4.1\"\n\n[tool.pytest.ini_options]\ntestpaths = [ \"tests\" ]\n";
    assert_eq!(
        pyproject_requirements(text),
        [
            "aiohttp>=3.14.1,<4",
            "httpx-aiohttp==0.1.8",
            "pydantic>=1.9.2",
            "mypy==1.13.0",
            "pytest>=9.0.3,<10",
            "legacy>=0.4.1,<0.5",
        ]
    );
}

/// Restoring Fern's `# type: ignore` pragmas to the copied runtime is what lets
/// a generated SDK type-check: over a minimal one-operation document, crozier's
/// default SDK reports zero `mypy` errors under its own `pyproject.toml` — its
/// pinned `mypy`, its configuration, and exactly the dependencies it declares.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_generated_sdk_typechecks_clean_under_its_own_mypy_pin() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, TINY_SPEC_WITH_OP).unwrap();
    let sdk = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&sdk)
        .args(["--package-name", "fern"])
        .assert()
        .success();
    let py = sdk_python_env(&sdk.join("pyproject.toml"))
        .unwrap_or_else(|reason| panic!("the SDK type-check needs a Python env: {reason}"));
    let (mypy_cache, _cache_lock) = lock_sdk_mypy_cache(&py).expect("lock the SDK's mypy cache");
    let output = std::process::Command::new(&py)
        .args(["-m", "mypy", "."])
        .current_dir(&sdk)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .env("MYPY_CACHE_DIR", &mypy_cache)
        .output()
        .expect("run mypy over the generated SDK");
    let report = String::from_utf8_lossy(&output.stdout);
    assert!(
        output.status.success() && report.contains("Success: no issues found"),
        "mypy reports errors in crozier's SDK under its own pin:\n{report}{}",
        String::from_utf8_lossy(&output.stderr)
    );
}

/// The pyright a consumer's editor runs, pinned with its own Node.js so the
/// journey needs no system `node`.
const PYRIGHT_REQUIREMENT: &str = "pyright[nodejs]==1.1.414";

/// `client-class-name` set to the class name of one of the spec's own resource
/// sub-clients (corpus row 307: `EcosystemClient` over Apideck's `Ecosystem`
/// resource) leaves the root client's `ecosystem` property typed as the
/// sub-client, not as the root class that shares its name: a consumer's pyright
/// resolves the sub-client's method through the property of both root clients,
/// as it does a sub-client whose name collides with nothing (`category`).
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_sub_client_named_like_the_root_client_typechecks_through_its_property() {
    let dir = tempfile::tempdir().expect("tempdir");
    let sdk = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(
            corpus_spec("apideck.com-ecosystem-client-class-name")
                .expect("row 307's committed source"),
        )
        .arg("--output")
        .arg(&sdk)
        .args([
            "--package-name",
            "fern",
            "--client-class-name",
            "EcosystemClient",
        ])
        .assert()
        .success();
    std::fs::write(
        sdk.join("consumer.py"),
        r#"from fern import AsyncEcosystemClient, EcosystemClient
from fern.types import GetCategoriesResponse, GetEcosystemResponse

client = EcosystemClient()
ecosystem: GetEcosystemResponse = client.ecosystem.ecosystems_one(ecosystem_id="ecosystem_id")
categories: GetCategoriesResponse = client.category.categories_all(ecosystem_id="ecosystem_id")


async def main() -> None:
    async_client = AsyncEcosystemClient()
    response: GetEcosystemResponse = await async_client.ecosystem.ecosystems_one(ecosystem_id="ecosystem_id")
"#,
    )
    .unwrap();
    let sdk_py = sdk_python_env(&sdk.join("pyproject.toml"))
        .unwrap_or_else(|reason| panic!("the consumer type-check needs the SDK's env: {reason}"));
    let pyright_py = cached_python_env(
        &python_env_root(),
        "crozier-pyright-env",
        &[PYRIGHT_REQUIREMENT.to_string()],
        uv_available(),
    )
    .unwrap_or_else(|reason| panic!("the consumer type-check needs pyright: {reason}"));
    let output = std::process::Command::new(&pyright_py)
        .args(["-m", "pyright", "--pythonpath"])
        .arg(&sdk_py)
        .arg("consumer.py")
        .current_dir(&sdk)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output()
        .expect("run pyright over the consumer");
    let report = String::from_utf8_lossy(&output.stdout);
    assert!(
        output.status.success() && report.contains("0 errors"),
        "pyright cannot resolve a sub-client through the root client's property:\n{report}{}",
        String::from_utf8_lossy(&output.stderr)
    );
}

/// `enum-type: literals` exists so a server that adds an enum value does not
/// break parsing a response: the generated literals SDK validates a model whose
/// enum field holds a value the spec does not list, and type-checks clean under
/// its own `mypy` pin; the python-enums SDK over the same document rejects that
/// value, which is the failure the setting avoids.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_literal_enums_accept_a_value_the_spec_does_not_list() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, literals::ENUM_SPEC).unwrap();
    let script = r#"
import sys

import pydantic

from pets import Pet
from pets.core.pydantic_utilities import parse_obj_as

try:
    pet = parse_obj_as(Pet, {"status": "hibernating"})
except pydantic.ValidationError:
    print("rejected")
    sys.exit(0)
assert pet.status == "hibernating", pet
assert parse_obj_as(Pet, {"status": "active"}).status == "active"
print("accepted")
"#;
    let mut outcomes = Vec::new();
    for enum_type in ["literals", "python-enums"] {
        let sdk = dir.path().join(enum_type);
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&sdk)
            .args(["--package-name", "pets", "--enum-type", enum_type])
            .assert()
            .success();
        let py = sdk_python_env(&sdk.join("pyproject.toml"))
            .unwrap_or_else(|reason| panic!("the SDK runtime check needs a Python env: {reason}"));
        let run = std::process::Command::new(&py)
            .args(["-c", script])
            .current_dir(sdk.join("src"))
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .expect("validate a model in the generated SDK");
        assert!(
            run.status.success(),
            "{enum_type}: {}",
            String::from_utf8_lossy(&run.stderr)
        );
        outcomes.push(String::from_utf8_lossy(&run.stdout).trim().to_string());
        if enum_type == "literals" {
            // A cache of its own: the shared one beside the environment holds
            // other SDKs' modules at these same paths, and mypy reuses an entry
            // whose file size and mtime match — `pets` and another test's `fern`
            // package are the same length, written in the same second.
            let mypy_cache = dir.path().join("mypy-cache");
            let mypy = std::process::Command::new(&py)
                .args(["-m", "mypy", "."])
                .current_dir(&sdk)
                .env("PYTHONDONTWRITEBYTECODE", "1")
                .env("MYPY_CACHE_DIR", &mypy_cache)
                .output()
                .expect("run mypy over the literals SDK");
            assert!(
                mypy.status.success(),
                "mypy reports errors in the literals SDK:\n{}",
                String::from_utf8_lossy(&mypy.stdout)
            );
        }
    }
    assert_eq!(outcomes, ["accepted", "rejected"]);
}

/// `x-fern-property-name` / `x-crozier-property-name` rename a property only on
/// the Python side: the `crozier-property-name` SDK, driven through a mock
/// transport, sends each renamed request keyword argument under the property's
/// JSON key — a referenced, an inline and a form body, and a nested inline
/// object — and parses responses keyed that way into the renamed model fields,
/// a discriminated union's variant among them, which serialize back to the key.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_renamed_properties_keep_their_json_keys_on_the_wire() {
    let dir = tempfile::tempdir().expect("tempdir");
    let sdk = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(fixture_dir("crozier-property-name").join("openapi.yml"))
        .arg("--output")
        .arg(&sdk)
        .args(["--package-name", "practice"])
        .assert()
        .success();
    let script = r#"
import json
from urllib.parse import parse_qs

import httpx

from practice import PracticeApi
from practice.practice import CreateInsuranceProductRequestCoverage

RESPONSES = {
    "/practice/p-1/service-metadata": {
        "id": "m-1",
        "practice_id": "p-owner",
        "service_name": "checkup",
        "displayName": "Checkup",
    },
    "/practice/p-1/intents": {"id": "i-1", "intent": "book"},
    "/practice/p-1/insurance-products": {"kind": "opened", "practice_id": "p-opened"},
}
sent = []


def handle(request):
    content_type = request.headers.get("content-type", "")
    if content_type.startswith("application/json"):
        body = json.loads(request.content)
    else:
        body = {key: values[0] for key, values in parse_qs(request.content.decode()).items()}
    sent.append((request.url.path, body))
    if request.url.path in RESPONSES:
        return httpx.Response(200, json=RESPONSES[request.url.path])
    return httpx.Response(204)


client = PracticeApi(
    base_url="https://api.test",
    httpx_client=httpx.Client(transport=httpx.MockTransport(handle)),
)
metadata = client.practice.create_service_metadata(
    "p-1",
    practice_service_metadata_create_practice_id="p-body",
    service_name="checkup",
)
client.practice.create_intent("p-1", practice_intent_create_practice_id="p-intent", intent="book")
event = client.practice.create_insurance_product(
    "p-1",
    insurance_product_practice_id="p-product",
    coverage=CreateInsuranceProductRequestCoverage(plan="gold"),
)
client.practice.create_note("p-1", note_practice_id="p-note", body="hello")

assert sent == [
    ("/practice/p-1/service-metadata", {"practice_id": "p-body", "service_name": "checkup"}),
    ("/practice/p-1/intents", {"practice_id": "p-intent", "intent": "book"}),
    ("/practice/p-1/insurance-products", {"practice_id": "p-product", "coverage": {"planCode": "gold"}}),
    ("/practice/p-1/notes", {"practice_id": "p-note", "body": "hello"}),
], sent
assert (metadata.owning_practice_id, metadata.label) == ("p-owner", "Checkup"), metadata
assert metadata.dict()["practice_id"] == "p-owner", metadata.dict()
assert metadata.dict()["displayName"] == "Checkup", metadata.dict()
assert (event.kind, event.opened_practice_id) == ("opened", "p-opened"), event
print("ok")
"#;
    let py = sdk_python_env(&sdk.join("pyproject.toml"))
        .unwrap_or_else(|reason| panic!("the SDK runtime check needs a Python env: {reason}"));
    let run = std::process::Command::new(&py)
        .args(["-c", script])
        .current_dir(sdk.join("src"))
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output()
        .expect("drive the generated SDK");
    assert!(
        run.status.success(),
        "{}{}",
        String::from_utf8_lossy(&run.stdout),
        String::from_utf8_lossy(&run.stderr)
    );
    assert_eq!(String::from_utf8_lossy(&run.stdout).trim(), "ok");
}

/// `default-max-retries` decides how many times a generated client retries a
/// failed request when the caller does not say: against a local server that
/// answers every request `503`, a client generated with `0` makes one attempt
/// and one generated with the default makes three (two retries), while a
/// per-request `max_retries` still overrides either.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_default_max_retries_bounds_the_attempts_a_client_makes() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, default_max_retries::SPEC).unwrap();
    let script = r#"
import http.server
import threading

from pets import PetsApi
from pets.core.api_error import ApiError

hits = []


class Unavailable(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        hits.append(self.path)
        self.send_response(503)
        self.send_header("Retry-After", "1")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *args):
        pass


server = http.server.HTTPServer(("127.0.0.1", 0), Unavailable)
threading.Thread(target=server.serve_forever, daemon=True).start()
client = PetsApi(base_url=f"http://127.0.0.1:{server.server_port}")


def attempts(**kwargs):
    before = len(hits)
    try:
        client.pets.list_pets(**kwargs)
    except ApiError as error:
        assert error.status_code == 503, error
    else:
        raise AssertionError("a 503 did not raise")
    return len(hits) - before


print(attempts(), attempts(request_options={"max_retries": 1}))
"#;
    let mut outcomes = Vec::new();
    for (name, args) in [
        ("zero", &["--default-max-retries", "0"][..]),
        ("default", &[][..]),
    ] {
        let sdk = dir.path().join(name);
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&sdk)
            .args(["--package-name", "pets"])
            .args(args)
            .assert()
            .success();
        let py = sdk_python_env(&sdk.join("pyproject.toml"))
            .unwrap_or_else(|reason| panic!("the SDK runtime check needs a Python env: {reason}"));
        let run = std::process::Command::new(&py)
            .args(["-c", script])
            .current_dir(sdk.join("src"))
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .expect("drive the generated client");
        assert!(
            run.status.success(),
            "{name}: {}",
            String::from_utf8_lossy(&run.stderr)
        );
        outcomes.push(String::from_utf8_lossy(&run.stdout).trim().to_string());
    }
    assert_eq!(outcomes, ["1 2", "3 2"]);
}

/// One class written into a scratch registry: its row, probe, Fern record and,
/// where the row calls for them, its wire test and evaluation.
struct ScratchClass<'a> {
    id: &'a str,
    status: &'a str,
    crozier_diagnostic: &'a str,
    probe: &'a str,
    wire_test: Option<&'a str>,
    record: bool,
}

/// Lay out `docs/fern-refusals/` under `root`: `classes.tsv` sorted by class,
/// each class's directory, and a `documents.tsv` whose rows carry `documents`.
fn write_scratch_registry(root: &Path, classes: &[ScratchClass], documents: &[(&str, &str)]) {
    let (cli, sdk) = probe_fern_pins();
    let mut sorted: Vec<&ScratchClass> = classes.iter().collect();
    sorted.sort_by_key(|class| class.id);
    let mut table = format!("{FERN_REFUSAL_CLASSES_HEADER}\n");
    for class in sorted {
        let carried = documents
            .iter()
            .filter(|(_, ids)| ids.split(',').any(|id| id == class.id))
            .count();
        let (diagnostic, population) = if class.status == "unevaluated" {
            ("—", "—")
        } else {
            (class.crozier_diagnostic, "0/0")
        };
        table.push_str(&format!(
            "{}\tdocuments\tcheck\t1\tA scratch phrase about <…>\t{carried}\t{}\t{diagnostic}\t{population}\n",
            class.id, class.status
        ));
        let dir = root.join(class.id);
        std::fs::create_dir_all(&dir).unwrap();
        std::fs::write(dir.join("probe.yml"), class.probe).unwrap();
        if class.record {
            std::fs::write(
                dir.join("fern-refusal.txt"),
                format!(
                    "fern_cli_version: {cli}\nfern_python_sdk_version: {sdk}\ngenerate_exit: 1\n\
                     diagnostic: A scratch phrase about x\noutput_tree: none\n"
                ),
            )
            .unwrap();
        }
        if let Some(wire_test) = class.wire_test {
            std::fs::write(dir.join("wire_test.py"), wire_test).unwrap();
        }
        if class.status != "unevaluated" {
            std::fs::write(dir.join("evaluation.md"), "# Scratch evaluation\n").unwrap();
        }
    }
    std::fs::write(root.join("classes.tsv"), table).unwrap();
    let mut rows = format!("{FERN_REFUSAL_DOCUMENTS_HEADER}\n");
    for (digest, ids) in documents {
        rows.push_str(&format!(
            "{digest}\tscratch\t—\t—\t—\tcheck\t1\t—\t{ids}\t0\t1\t—\n"
        ));
    }
    std::fs::write(root.join("documents.tsv"), rows).unwrap();
}

/// A `wire_test.py` holding the contract against `TINY_SPEC_WITH_OP`'s SDK: the
/// package imports, `mypy` under its own pin reports zero errors, and through
/// an injected `httpx.MockTransport` the request reaches `GET /thing` and the
/// declared response parses into `Thing`.
const SCRATCH_PASSING_WIRE_TEST: &str = r#"import os
import subprocess
import sys

import httpx

SDK = os.environ["CROZIER_SDK_DIR"]
sys.path.insert(0, os.environ["CROZIER_SDK_SRC"])

from fern import FernApi  # noqa: E402 - importable only once sys.path names the SDK under test
from fern.types import Thing  # noqa: E402 - importable only once sys.path names the SDK under test


def test_mypy_reports_no_error_under_the_sdk_pin():
    run = subprocess.run([sys.executable, "-m", "mypy", "."], cwd=SDK, capture_output=True, text=True)
    assert run.returncode == 0, run.stdout + run.stderr


def test_the_request_and_its_response_round_trip():
    seen = []

    def answer(request):
        seen.append(request)
        return httpx.Response(200, json={"name": "widget"})

    client = FernApi(base_url="https://api.test", httpx_client=httpx.Client(transport=httpx.MockTransport(answer)))
    thing = client.thing.get_thing()
    assert [(request.method, str(request.url)) for request in seen] == [("GET", "https://api.test/thing")]
    assert thing == Thing(name="widget")
"#;

const SCRATCH_FAILING_WIRE_TEST: &str =
    "def test_the_wire_disagrees():\n    assert False, \"scratch wire test fails on purpose\"\n";

/// A stand-in for crozier as it will behave once classes are evaluated: it
/// reads the class's own `classes.tsv` row and refuses a `refuse` class's probe
/// in both modes, and a `generate` class's under `--fern-strict`, printing the
/// one line the contract asks for; everything else runs the real binary. With
/// `STUB_WRITES_ON_REFUSAL` set it writes a file before refusing.
const SCRATCH_STRICT_CROZIER: &str = r#"import os
import subprocess
import sys
from pathlib import Path

args = sys.argv[1:]
spec = Path(args[args.index("--spec") + 1])
out = Path(args[args.index("--output") + 1])
cls = spec.parent.name
rows = [line.split("\t") for line in (spec.parent.parent / "classes.tsv").read_text().splitlines()[1:]]
status, phrase = next((row[6], row[7]) for row in rows if row[0] == cls)
strict = "--fern-strict" in args
if status == "refuse" or (status == "generate" and strict):
    if os.environ.get("STUB_WRITES_ON_REFUSAL"):
        out.mkdir(parents=True, exist_ok=True)
        (out / "partial.py").write_text("")
    cause = " (refused by fern-strict: Fern refuses this document)" if status == "generate" else ""
    print(f"error: [{cls}] {phrase}{cause}", file=sys.stderr)
    sys.exit(1)
sys.exit(subprocess.run([os.environ["STUB_CROZIER"], *[a for a in args if a != "--fern-strict"]]).returncode)
"#;

/// The command that runs [`SCRATCH_STRICT_CROZIER`] from `dir`, or `None` (a
/// skip locally, a failure in CI) when no Python is on PATH.
fn scratch_strict_crozier(dir: &Path, writes_on_refusal: bool) -> Option<impl Fn() -> Command> {
    let Some(py) = python_interpreter() else {
        assert!(
            std::env::var_os("CI").is_none(),
            "the refusal-gate journeys need Python, unavailable in CI"
        );
        eprintln!("skipping: no python3/python on PATH");
        return None;
    };
    let stub = dir.join("strict_crozier.py");
    std::fs::write(&stub, SCRATCH_STRICT_CROZIER).unwrap();
    let real = assert_cmd::cargo::cargo_bin("crozier");
    Some(move || {
        let mut command = Command::new(py);
        command.arg(&stub).env("STUB_CROZIER", &real);
        if writes_on_refusal {
            command.env("STUB_WRITES_ON_REFUSAL", "1");
        }
        command
    })
}

fn header_array_probe() -> String {
    std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/openapi-surface/probes/header-array.yml"),
    )
    .expect("the header-array probe crozier refuses")
}

// llmlint: ignore[e2e_not_mocked] No class is evaluated yet, so the real binary refuses nothing under --fern-strict and no journey over it can reach the gate's accepting or wrote-output branches; the stand-in emulates only the refusal line the contract fixes and runs the real binary for every generation. The gate under test is real, and the failing journeys drive the real binary.
#[test]
fn fern_refusal_gate_accepts_a_registry_whose_classes_hold() {
    let scratch = tempfile::tempdir().expect("tempdir");
    let registry = scratch.path().join("fern-refusals");
    let Some(generator) = scratch_strict_crozier(scratch.path(), false) else {
        return;
    };
    write_scratch_registry(
        &registry,
        &[
            ScratchClass {
                id: "scratch-generate",
                status: "generate",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: Some(SCRATCH_PASSING_WIRE_TEST),
                record: true,
            },
            ScratchClass {
                id: "scratch-refuse",
                status: "refuse",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: None,
                record: true,
            },
            ScratchClass {
                id: "scratch-unevaluated",
                status: "unevaluated",
                crozier_diagnostic: "—",
                probe: TINY_SPEC_WITH_OP,
                wire_test: None,
                record: true,
            },
        ],
        &[("0".repeat(64).as_str(), "scratch-generate,scratch-refuse")],
    );
    let failures = fern_refusal_failures(&registry, &generator, WireTests::Skip);
    assert!(
        failures.is_empty(),
        "a registry whose classes hold was refused:\n{}",
        failures.join("\n")
    );
}

#[test]
fn fern_refusal_gate_names_each_class_and_condition_it_breaks() {
    let scratch = tempfile::tempdir().expect("tempdir");
    let registry = scratch.path().join("fern-refusals");
    let refused = header_array_probe();
    write_scratch_registry(
        &registry,
        &[
            ScratchClass {
                id: "generated-though-refuse",
                status: "refuse",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: None,
                record: true,
            },
            ScratchClass {
                id: "refused-by-default",
                status: "generate",
                crozier_diagnostic: "unsupported array schema",
                probe: &refused,
                wire_test: Some(SCRATCH_PASSING_WIRE_TEST),
                record: true,
            },
            ScratchClass {
                id: "not-refused-when-strict",
                status: "generate",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: Some(SCRATCH_PASSING_WIRE_TEST),
                record: true,
            },
            ScratchClass {
                id: "missing-diagnostic",
                status: "refuse",
                crozier_diagnostic: "a phrase crozier never prints",
                probe: &refused,
                wire_test: None,
                record: true,
            },
            ScratchClass {
                id: "no-record",
                status: "unevaluated",
                crozier_diagnostic: "—",
                probe: TINY_SPEC_WITH_OP,
                wire_test: None,
                record: false,
            },
        ],
        &[(
            "1".repeat(64).as_str(),
            "generated-though-refuse,ghost-class",
        )],
    );
    std::fs::create_dir_all(registry.join("stray-directory")).unwrap();
    // A fraction no documents.tsv row measured: the one carrying the class has
    // no `crozier_strict_exit`, so the gate reads 0/0 where the table claims 1/1.
    let classes = std::fs::read_to_string(registry.join("classes.tsv")).unwrap();
    let drifted = classes.replace(
        "\tGET /thing: the scratch element\t0/0\n",
        "\tGET /thing: the scratch element\t1/1\n",
    );
    assert_ne!(classes, drifted, "the scratch row to drift was not found");
    std::fs::write(registry.join("classes.tsv"), drifted).unwrap();

    let failures = fern_refusal_failures(&registry, &crozier, WireTests::Skip);
    let report = failures.join("\n");
    let expected = [
        (
            "generated-though-refuse:",
            "crozier generated from the probe in its mode",
        ),
        (
            "refused-by-default:",
            "a `generate` class's probe is refused by default",
        ),
        (
            "not-refused-when-strict:",
            "crozier generated from the probe under --fern-strict",
        ),
        (
            "missing-diagnostic:",
            "printed no line containing crozier_diagnostic \"a phrase crozier never prints\"",
        ),
        (
            "no-record:",
            "its Fern record no-record/fern-refusal.txt is missing",
        ),
        (
            "stray-directory:",
            "is a directory under the registry but no classes.tsv row names it",
        ),
        ("ghost-class:", "but it is not a classes.tsv row"),
        (
            "generated-though-refuse:",
            "population_strict is 1/1, but documents.tsv's crozier_strict_exit refuses 0/0",
        ),
    ];
    for (class, condition) in expected {
        assert!(
            failures
                .iter()
                .any(|line| line.starts_with(class) && line.contains(condition)),
            "no failure names {class} with {condition:?}:\n{report}"
        );
    }
    assert!(
        !report.contains("wire_test.py failed"),
        "the offline gate ran a wire test:\n{report}"
    );
}

/// The gate's `wire_test.py` condition, over the real binary: a `generate`
/// class whose wire test fails is named with that condition and the test's own
/// message, and one whose wire test passes against crozier's SDK is not. (Both
/// are also reported as not refused under `--fern-strict`, which crozier does
/// not do yet; that condition is the offline journey's.)
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_fern_refusal_gate_runs_each_wire_test() {
    let scratch = tempfile::tempdir().expect("tempdir");
    let registry = scratch.path().join("fern-refusals");
    write_scratch_registry(
        &registry,
        &[
            ScratchClass {
                id: "failing-wire-test",
                status: "generate",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: Some(SCRATCH_FAILING_WIRE_TEST),
                record: true,
            },
            ScratchClass {
                id: "passing-wire-test",
                status: "generate",
                crozier_diagnostic: "GET /thing: the scratch element",
                probe: TINY_SPEC_WITH_OP,
                wire_test: Some(SCRATCH_PASSING_WIRE_TEST),
                record: true,
            },
        ],
        &[],
    );
    let failures = fern_refusal_failures(&registry, &crozier, WireTests::Run);
    let report = failures.join("\n");
    assert!(
        failures
            .iter()
            .any(|line| line.starts_with("failing-wire-test:")
                && line.contains("wire_test.py failed against crozier's default SDK")
                && line.contains("scratch wire test fails on purpose")),
        "no failure names failing-wire-test with its failed wire test:\n{report}"
    );
    assert!(
        !failures
            .iter()
            .any(|line| line.starts_with("passing-wire-test:") && line.contains("wire_test.py")),
        "a passing wire test was reported:\n{report}"
    );
}

// llmlint: ignore[e2e_not_mocked] No class is evaluated yet, so the real binary refuses nothing under --fern-strict and no journey over it can reach the gate's accepting or wrote-output branches; the stand-in emulates only the refusal line the contract fixes and runs the real binary for every generation. The gate under test is real, and the failing journeys drive the real binary.
#[test]
fn fern_refusal_gate_reports_a_refusal_that_wrote_output() {
    let scratch = tempfile::tempdir().expect("tempdir");
    let registry = scratch.path().join("fern-refusals");
    let Some(generator) = scratch_strict_crozier(scratch.path(), true) else {
        return;
    };
    write_scratch_registry(
        &registry,
        &[ScratchClass {
            id: "writes-on-refusal",
            status: "refuse",
            crozier_diagnostic: "GET /thing: the scratch element",
            probe: TINY_SPEC_WITH_OP,
            wire_test: None,
            record: true,
        }],
        &[],
    );
    let failures = fern_refusal_failures(&registry, &generator, WireTests::Skip);
    assert!(
        failures
            .iter()
            .any(|line| line.starts_with("writes-on-refusal:")
                && line.contains("wrote 1 file(s) to the output directory (partial.py)")),
        "a refusal that wrote output was not reported:\n{}",
        failures.join("\n")
    );
}

/// An unresolved security Reference Object is refused before auth normalization;
/// replacing it with the declared bearer scheme restores identical SDK bytes.
#[test]
fn unresolved_security_reference_recovers_with_inline_scheme() {
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("unresolved-reference/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "unresolved-reference",
            &run,
            "components/securitySchemes/BearerAuth",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(probe).unwrap();
    std::fs::write(
        &repaired,
        text.replace(
            "      $ref: './components.yaml#/components/securitySchemes/BearerAuth'",
            "      type: http\n      scheme: bearer",
        ),
    )
    .unwrap();
    let normal = refusal_run(&crozier, &repaired, false).unwrap();
    let strict = refusal_run(&crozier, &repaired, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
}

#[test]
fn noncomponent_response_reference_recovers_when_inlined() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = "openapi: 3.0.3\ninfo: {title: Probe, version: '1'}\npaths:\n  /probe:\n    get:\n      operationId: probe\n      responses:\n        204: {description: Empty}\n        401: {$ref: '#/$defs/Denied'}\n$defs:\n  Denied: {description: Unauthorized}\n";
    std::fs::write(&spec, text).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        let failures = refused_failures(
            "unresolved-reference",
            &run,
            "paths//probe/get/responses/401",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    std::fs::write(
        &spec,
        text.replace("{$ref: '#/$defs/Denied'}", "{description: Unauthorized}"),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
}

#[test]
fn ignored_security_reference_uses_canonical_precedence_through_cli() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("unresolved-reference/probe.yml");
    let text = std::fs::read_to_string(probe)
        .unwrap()
        .replace("security:\n  - BearerAuth: []\n", "");
    for (extensions, refused) in [
        ("x-crozier-ignore: true\n      x-fern-ignore: false", false),
        ("x-crozier-ignore: false\n      x-fern-ignore: true", true),
    ] {
        std::fs::write(
            &spec,
            text.replace(
                "BearerAuth:\n",
                &format!("BearerAuth:\n      {extensions}\n"),
            ),
        )
        .unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            if refused {
                let failures = refused_failures(
                    "unresolved-reference",
                    &run,
                    "components/securitySchemes/BearerAuth",
                    strict,
                );
                assert!(failures.is_empty(), "{}", failures.join("\n"));
            } else {
                assert_eq!(run.code, Some(0), "{}", run.stderr);
                assert!(!run.files.is_empty());
            }
        }
    }
}

#[test]
fn path_without_leading_slash_recovers_with_valid_path() {
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("path-without-leading-slash/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures("path-without-leading-slash", &run, "paths/things", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(probe).unwrap();
    std::fs::write(&spec, text.replace("  things:", "  /things:")).unwrap();
    let ignored = dir.path().join("ignored.yml");
    std::fs::write(
        &ignored,
        text.replace(
            "      operationId:",
            "      x-fern-ignore: true\n      operationId:",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &ignored, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
    let normal = refusal_run(&crozier, &spec, false).unwrap();
    let strict = refusal_run(&crozier, &spec, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
}

#[test]
fn unreferenced_path_parameter_recovers_when_placeholder_is_added() {
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("path-parameter-unreferenced/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "path-parameter-unreferenced",
            &run,
            "GET /things parameter id",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(probe).unwrap();
    std::fs::write(&spec, text.replace("  /things:", "  /things/{id}:")).unwrap();
    let ignored = dir.path().join("ignored.yml");
    std::fs::write(
        &ignored,
        text.replace(
            "      operationId:",
            "      x-crozier-ignore: true\n      operationId:",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &ignored, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
    let normal = refusal_run(&crozier, &spec, false).unwrap();
    let strict = refusal_run(&crozier, &spec, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
}

#[test]
fn shared_referenced_path_parameter_recovers_with_placeholder() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = "openapi: 3.0.3\ninfo: {title: Probe, version: '1'}\npaths:\n  /things:\n    parameters:\n      - {$ref: '#/components/parameters/ThingId'}\n    get:\n      operationId: listThings\n      responses: {'204': {description: Empty}}\ncomponents:\n  parameters:\n    ThingId:\n      name: id\n      in: path\n      required: true\n      schema: {type: string}\n";
    std::fs::write(&spec, text).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        let failures = refused_failures(
            "path-parameter-unreferenced",
            &run,
            "GET /things parameter id",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    std::fs::write(&spec, text.replace("  /things:", "  /things/{id}:")).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
}

#[test]
fn missing_parameter_component_recovers_when_definition_is_added() {
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("undefined-component-reference/probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures =
            refused_failures("undefined-component-reference", &run, "CartIdParam", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = std::fs::read_to_string(probe).unwrap();
    std::fs::write(&spec, format!("{text}    CartIdParam:\n      name: id\n      in: path\n      required: true\n      schema: {{type: string}}\n")).unwrap();
    let unused = dir.path().join("unused.yml");
    let repaired = std::fs::read_to_string(&spec).unwrap();
    std::fs::write(
        &unused,
        format!("{repaired}    UnusedAlias:\n      $ref: '#/components/parameters/AbsentUnused'\n"),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &unused, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
    let normal = refusal_run(&crozier, &spec, false).unwrap();
    let strict = refusal_run(&crozier, &spec, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
}

#[test]
fn nested_named_example_reference_recovers_with_example_component() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("undefined-component-reference");
    let probe = class.join("named-example-probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "undefined-component-reference",
            &run,
            "JSONEXAMPLES/value/COMPANIES_GET",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let missing_dir = tempfile::tempdir().unwrap();
    let missing = missing_dir.path().join("missing.yml");
    std::fs::write(
        &missing,
        std::fs::read_to_string(&probe).unwrap().replace(
            "#/components/examples/JSONEXAMPLES/value/COMPANIES_GET",
            "#/components/examples/AbsentExample",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &missing, strict).unwrap();
        let failures = refused_failures(
            "undefined-component-reference",
            &run,
            "AbsentExample",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let control = class.join("named-example-control.yml");
    let normal = refusal_run(&crozier, &control, false).unwrap();
    let strict = refusal_run(&crozier, &control, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
    let dir = tempfile::tempdir().unwrap();
    let data = dir.path().join("data.yml");
    let text = std::fs::read_to_string(control).unwrap().replace(
        "                  companies:",
        "                  opaque: {type: object, additionalProperties: true}\n                  companies:");
    std::fs::write(
        &data,
        text.replace(
            "value: {companies: [ACME]}",
            "value: {companies: [ACME], opaque: {$ref: '#/components/parameters/Absent'}}",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &data, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
}

#[test]
fn response_parameter_reference_recovers_with_inline_response() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let text = "openapi: 3.0.3\ninfo: {title: Probe, version: '1'}\npaths:\n  /probe:\n    get:\n      operationId: probe\n      responses:\n        '204': {$ref: '#/components/parameters/ID'}\ncomponents:\n  parameters:\n    ID: {name: id, in: query, schema: {type: string}}\n";
    std::fs::write(&spec, text).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        let failures = refused_failures(
            "unresolved-reference",
            &run,
            "paths//probe/get/responses/204",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    std::fs::write(
        &spec,
        text.replace(
            "{$ref: '#/components/parameters/ID'}",
            "{description: Empty}",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
}

#[test]
fn response_component_fragment_is_not_an_operation_reference() {
    let control = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("unresolved-reference/response-fragment-control.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &control, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert!(!run.files.is_empty());
    }
    let dir = tempfile::tempdir().unwrap();
    let direct = dir.path().join("direct.yml");
    let text = std::fs::read_to_string(control).unwrap();
    std::fs::write(
        &direct,
        text.replace(
            "'204': {$ref: '#/components/responses/Empty'}",
            "'204': {$ref: '#/x-fragment/base'}",
        ),
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &direct, strict).unwrap();
        let failures = refused_failures(
            "unresolved-reference",
            &run,
            "paths//probe/get/responses/204",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
}

#[test]
fn security_reference_recovers_when_the_referenced_document_is_present() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("openapi.yml");
    let probe = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("unresolved-reference/probe.yml");
    std::fs::copy(probe, &spec).unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        let failures = refused_failures("unresolved-reference", &run, "components.yaml", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    }
    std::fs::write(
        dir.path().join("components.yaml"),
        "components:\n  securitySchemes:\n    BearerAuth: {type: http, scheme: bearer}\n",
    )
    .unwrap();
    let normal = refusal_run(&crozier, &spec, false).unwrap();
    let strict = refusal_run(&crozier, &spec, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
    // The referenced scheme authenticates exactly as the same scheme declared
    // in the document does: one `token` credential, sent as a bearer header.
    let inline = dir.path().join("inline.yml");
    std::fs::write(
        &inline,
        std::fs::read_to_string(&spec).unwrap().replace(
            "$ref: './components.yaml#/components/securitySchemes/BearerAuth'",
            "{type: http, scheme: bearer}",
        ),
    )
    .unwrap();
    let declared = refusal_run(&crozier, &inline, false).unwrap();
    assert_eq!(declared.code, Some(0), "{}", declared.stderr);
    assert_eq!(normal.files, declared.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read_to_string(normal.target.join(file)).unwrap(),
            std::fs::read_to_string(declared.target.join(file)).unwrap(),
            "{file}"
        );
    }
    let wrapper = normal
        .files
        .iter()
        .find(|file| file.ends_with("core/client_wrapper.py"))
        .expect("a client wrapper");
    let wrapper = std::fs::read_to_string(normal.target.join(wrapper)).unwrap();
    assert!(
        wrapper.contains("token: typing.Union[str, typing.Callable[[], str]]")
            && wrapper.contains("headers[\"Authorization\"] = f\"Bearer {self._get_token()}\""),
        "{wrapper}"
    );
    std::fs::write(
        dir.path().join("components.yaml"),
        "components:\n  securitySchemes:\n    BearerAuth: {$ref: '#/components/securitySchemes/Actual'}\n    Actual: {type: http, scheme: bearer}\n",
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        assert_eq!(run.code, Some(0), "{}", run.stderr);
        assert_eq!(normal.files, run.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(run.target.join(file)).unwrap()
            );
        }
    }
    std::fs::write(
        dir.path().join("components.yaml"),
        "components:\n  securitySchemes:\n    BearerAuth: {type: apiKey, in: cookie, name: SID}\n",
    )
    .unwrap();
    for strict in [false, true] {
        let run = refusal_run(&crozier, &spec, strict).unwrap();
        let failures = refused_failures("service-auth-undefined", &run, "BearerAuth", strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
    }
}

#[test]
fn primitive_default_refusal_recovers_with_declared_types() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("default-not-valid-for-type");
    for case in [
        "probe.yml",
        "number-string-control.yml",
        "integer-fraction-control.yml",
        "integer-boolean-control.yml",
        "number-boolean-control.yml",
        "unused-property-control.yml",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures("default-not-valid-for-type", &run, "default", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("repaired.yml");
    std::fs::write(
        &repaired,
        std::fs::read_to_string(class.join("probe.yml"))
            .unwrap()
            .replace("default: 'one'", "default: 2"),
    )
    .unwrap();
    for label in ["shared-parameter", "referenced-parameter"] {
        let text = std::fs::read_to_string(class.join(format!("{label}-control.yml"))).unwrap();
        let spec = dir.path().join(format!("{label}.yml"));
        std::fs::write(&spec, &text).unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures = refused_failures("default-not-valid-for-type", &run, "page", strict);
            assert!(failures.is_empty(), "{label}: {}", failures.join("\n"));
        }
        std::fs::write(&spec, text.replace("default: one", "default: 2")).unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            assert_eq!(run.code, Some(0), "{label}: {}", run.stderr);
            assert!(!run.files.is_empty());
        }
    }
    let mut accepted = vec![repaired];
    accepted.extend(
        [
            "integer-null-control.yml",
            "boolean-string-control.yml",
            "string-number-control.yml",
            "number-valid-control.yml",
            "integer-integral-float-control.yml",
            "unused-integer-control.yml",
            "response-integer-valid-yaml-control.yml",
        ]
        .map(|case| class.join(case)),
    );
    for spec in accepted {
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(
            normal.code,
            Some(0),
            "{}: {}",
            spec.display(),
            normal.stderr
        );
        assert_eq!(
            strict.code,
            Some(0),
            "{}: {}",
            spec.display(),
            strict.stderr
        );
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn list_default_refusal_recovers_with_an_array() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("list-default-not-array");
    for case in ["probe.yml", "boolean-default-control.yml"] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures(
                "list-default-not-array",
                &run,
                "Thing/properties/tags",
                strict,
            );
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    for case in [
        "header-array-control.yml",
        "valid-list-control.yml",
        "null-list-control.yml",
        "unused-array-control.yml",
        "query-array-control.yml",
    ] {
        let normal = refusal_run(&crozier, &class.join(case), false).unwrap();
        let strict = refusal_run(&crozier, &class.join(case), true).unwrap();
        assert_eq!(normal.code, Some(0), "{case}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{case}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn object_extension_refusal_preserves_scalar_aliases_and_object_bases() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("object-extends-non-object");
    for case in [
        "probe.yml",
        "array-base-control.yml",
        "empty-object-base-control.yml",
        "map-base-control.yml",
        "two-scalar-refs-control.yml",
        "ordered-shadowed-object-control.yml",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures =
                refused_failures("object-extends-non-object", &run, "allOf extends", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    for case in [
        "object-base-control.yml",
        "empty-properties-base-control.yml",
        "scalar-alias-control.yml",
        "scalar-constrained-control.yml",
        "typed-two-scalar-refs-control.yml",
        "nullable-typed-two-scalar-refs-control.yml",
        "inline-scalar-object-control.yml",
        "object-alias-control.yml",
        "shadowed-object-control.yml",
        "ordered-renamed-union-control.yml",
    ] {
        let normal = refusal_run(&crozier, &class.join(case), false).unwrap();
        let strict = refusal_run(&crozier, &class.join(case), true).unwrap();
        assert_eq!(normal.code, Some(0), "{case}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{case}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn inline_header_enum_refusal_recovers_with_a_named_schema() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("generator-missing-type");
    for case in [
        "probe.yml",
        "optional-singleton-control.yml",
        "two-values-control.yml",
        "other-header-control.yml",
        "accept-header-control.yml",
        "inferred-type-control.yml",
        "const-header-control.yml",
        "two-operations-control.yml",
        "three-of-four-control.yml",
        "second-declaration-control.yml",
        "referenced-header-control.yml",
        "path-header-control.yml",
        "ignored-operation-control.yml",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures("generator-missing-type", &run, "schema", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let text = std::fs::read_to_string(class.join("probe.yml")).unwrap();
    for spelling in ["x-fern-ignore", "x-crozier-ignore"] {
        let spec = dir.path().join(format!("{spelling}.yml"));
        std::fs::write(
            &spec,
            text.replace(
                "            type: string",
                &format!("            {spelling}: true\n            type: string"),
            ),
        )
        .unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            assert_eq!(run.code, Some(0), "{spelling}: {}", run.stderr);
            assert!(!run.files.is_empty());
        }
    }
    for case in [
        "named-enum-control.yml",
        "partial-header-control.yml",
        "two-of-three-control.yml",
        "implicit-declaration-control.yml",
        "first-declaration-control.yml",
        "fallback-declared-control.yml",
        "fallback-partial-control.yml",
        "sdk-method-declared-control.yml",
        "sdk-method-partial-control.yml",
        "authorization-header-control.yml",
        "user-agent-header-control.yml",
        "content-type-header-control.yml",
        "numeric-enum-control.yml",
    ] {
        let normal = refusal_run(&crozier, &class.join(case), false).unwrap();
        let strict = refusal_run(&crozier, &class.join(case), true).unwrap();
        assert_eq!(normal.code, Some(0), "{case}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{case}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        // Tie the refusal's inferred declaration name to actual SDK emission,
        // including both alternate naming branches, without changing SDK output.
        let declaration = match case {
            "partial-header-control.yml" => Some("list_agents_request_api_version.py"),
            "fallback-partial-control.yml" => Some("get_agents_request_api_version.py"),
            "sdk-method-partial-control.yml" => Some("fetch_agents_request_api_version.py"),
            _ => None,
        };
        if let Some(declaration) = declaration {
            assert!(
                normal.files.iter().any(|file| Path::new(file)
                    .file_name()
                    .is_some_and(|name| name == declaration)),
                "{case}: inferred declaration name drifted from the SDK"
            );
        }
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn named_default_refusal_preserves_declared_aliases_and_recovers_without_a_default() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("named-type-default");
    for case in [
        "probe.yml",
        "union-declaration-control.yml",
        "multiple-values-collision-control.yml",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures(
                "named-type-default",
                &run,
                "ticket/properties/type/default",
                strict,
            );
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let ignored = dir.path().join("ignored.yml");
    std::fs::write(
        &ignored,
        std::fs::read_to_string(class.join("probe.yml"))
            .unwrap()
            .replace(
                "    ticket:\n",
                "    ticket:\n      x-crozier-ignore: true\n",
            ),
    )
    .unwrap();
    let mut accepted = vec![ignored];
    accepted.extend(
        [
            "renamed-model-control.yml",
            "no-default-control.yml",
            "named-string-control.yml",
            "named-object-control.yml",
            "named-enum-control.yml",
            "string-declaration-control.yml",
            "enum-declaration-control.yml",
            "null-default-control.yml",
            "inline-object-control.yml",
            "inline-union-control.yml",
            "inline-map-control.yml",
            "root-object-control.yml",
            "reversed-unused-control.yml",
            "typed-union-declaration-control.yml",
        ]
        .map(|case| class.join(case)),
    );
    for spec in accepted {
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(
            normal.code,
            Some(0),
            "{}: {}",
            spec.display(),
            normal.stderr
        );
        assert_eq!(
            strict.code,
            Some(0),
            "{}: {}",
            spec.display(),
            strict.stderr
        );
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn extension_cycle_refusal_preserves_ordinary_recursive_schemas() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("extension-reference-cycle");
    for (case, diagnostic) in [
        ("probe.yml", "schemas/Node/x-"),
        ("other-extension-control.yml", "schemas/Node/x-"),
        ("two-schema-cycle-control.yml", "schemas/Node/x-"),
        ("direct-link-control.json", "schemas/Node/x-link"),
        (
            "direct-mapped-control.json",
            "schemas/Node/x-mapped-definition",
        ),
        (
            "nested-mapped-control.json",
            "schemas/Node/x-mapped-definition",
        ),
        (
            "direct-stripe-control.json",
            "schemas/Node/x-stripeProperty",
        ),
        ("qualified-root-control.json", "schemas/My.Node/x-link"),
        (
            "field-integer-control.json",
            "schemas/Node/properties/id/x-link",
        ),
        (
            "field-string-control.json",
            "schemas/Node/properties/id/x-link",
        ),
        (
            "field-boolean-control.json",
            "schemas/Node/properties/id/x-link",
        ),
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures("extension-reference-cycle", &run, diagnostic, strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let ignored = dir.path().join("ignored.yml");
    std::fs::write(
        &ignored,
        std::fs::read_to_string(class.join("probe.yml"))
            .unwrap()
            .replace("    Node:\n", "    Node:\n      x-fern-ignore: true\n"),
    )
    .unwrap();
    let mut accepted = vec![ignored];
    accepted.extend(
        [
            "ordinary-recursion-control.yml",
            "acyclic-extension-control.yml",
            "ordinary-return-edge-control.yml",
            "field-mapped-control.json",
            "field-direct-link-control.json",
            "field-object-mapped-control.json",
            "field-string-mapped-control.json",
            "qualified-field-control.json",
            "unsigned-field-control.json",
        ]
        .map(|case| class.join(case)),
    );
    for spec in accepted {
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(
            normal.code,
            Some(0),
            "{}: {}",
            spec.display(),
            normal.stderr
        );
        assert_eq!(
            strict.code,
            Some(0),
            "{}: {}",
            spec.display(),
            strict.stderr
        );
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn unresolved_schema_refusal_preserves_optional_and_response_root_references() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("unresolved-schema-reference");
    for case in [
        "probe.yml",
        "deep-definitions-field-control.yml",
        "deep-defs-field-control.yml",
        "required-response-field-control.yml",
        "nullable-required-field-control.yml",
        "nullable-root-control.yml",
        "optional-known-child-control.yml",
        "union-first-member-control.yml",
        "anyof-first-member-control.yml",
        "nested-items-required-control.yml",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures(
                "unresolved-schema-reference",
                &run,
                "reference #/components/schemas/",
                strict,
            );
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let ignored = dir.path().join("ignored.yml");
    std::fs::write(
        &ignored,
        std::fs::read_to_string(class.join("probe.yml"))
            .unwrap()
            .replace(
                "      operationId: createContact",
                "      x-crozier-ignore: true\n      operationId: createContact",
            ),
    )
    .unwrap();
    let mut accepted = vec![ignored];
    let text = std::fs::read_to_string(class.join("probe.yml")).unwrap();
    for spelling in ["x-fern-ignore", "x-crozier-ignore"] {
        let spec = dir.path().join(format!("schema-{spelling}.yml"));
        std::fs::write(
            &spec,
            text.replace(
                "attributes: {$ref: '#/components/schemas/custom_attributes'}",
                &format!("attributes: {{$ref: '#/components/schemas/custom_attributes', {spelling}: true}}"),
            ),
        )
        .unwrap();
        accepted.push(spec);
    }
    accepted.extend(
        [
            "defined-field-control.yml",
            "deep-field-control.yml",
            "missing-response-root-control.yml",
            "missing-request-root-control.yml",
            "unused-missing-field-control.yml",
            "optional-field-control.yml",
            "unused-required-field-control.yml",
            "optional-response-field-control.yml",
            "deep-response-root-control.yml",
            "unused-deep-field-control.yml",
            "explicit-optional-request-control.yml",
            "required-array-control.yml",
            "optional-deep-field-control.yml",
            "definitions-property-name-control.yml",
            "union-second-member-control.yml",
            "union-inline-second-member-control.yml",
            "anyof-second-member-control.yml",
        ]
        .map(|case| class.join(case)),
    );
    // A required pointer naming `properties` is walked, and Fern generates from
    // one reaching nothing or a `$defs` member; each is an authored probe whose
    // Fern tree `authored_probe_measurements_match_fern` byte-matches.
    let probes = Path::new(env!("CARGO_MANIFEST_DIR")).join(AUTHORED_PROBES_DIR);
    accepted.extend(
        [
            "358-absent-required-property",
            "358-undeclared-head-properties-required",
            "356-defs-required-property",
        ]
        .map(|case| probes.join(case).join("openapi.yml")),
    );
    for spec in accepted {
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(
            normal.code,
            Some(0),
            "{}: {}",
            spec.display(),
            normal.stderr
        );
        assert_eq!(
            strict.code,
            Some(0),
            "{}: {}",
            spec.display(),
            strict.stderr
        );
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

#[test]
fn recursive_inline_union_refusal_preserves_named_recursion() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("heap-exhausted");
    for case in [
        "probe.yml",
        "single-child-control.yml",
        "recursive-union-allof-control.json",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(case), strict).unwrap();
            let failures = refused_failures("heap-exhausted", &run, "components/schemas", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let dir = tempfile::tempdir().unwrap();
    let probe = std::fs::read_to_string(class.join("probe.yml")).unwrap();
    for spelling in ["x-fern-ignore", "x-crozier-ignore"] {
        let spec = dir.path().join(format!("{spelling}.yml"));
        std::fs::write(
            &spec,
            probe.replace(
                "        composition:\n",
                &format!("        composition:\n          {spelling}: true\n"),
            ),
        )
        .unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            assert_eq!(run.code, Some(0), "{spelling}: {}", run.stderr);
            assert!(!run.files.is_empty());
        }
    }
    for case in [
        "named-object-recursion-control.yml",
        "nonrecursive-union-control.yml",
        "named-binary-recursion-control.json",
    ] {
        let normal = refusal_run(&crozier, &class.join(case), false).unwrap();
        let strict = refusal_run(&crozier, &class.join(case), true).unwrap();
        assert_eq!(normal.code, Some(0), "{case}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{case}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

/// Generates in both modes with byte-identical output.
fn generates_identically_in_both_modes(spec: &Path) {
    let normal = refusal_run(&crozier, spec, false).unwrap();
    let strict = refusal_run(&crozier, spec, true).unwrap();
    assert_eq!(
        normal.code,
        Some(0),
        "{}: {}",
        spec.display(),
        normal.stderr
    );
    assert_eq!(
        strict.code,
        Some(0),
        "{}: {}",
        spec.display(),
        strict.stderr
    );
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
}

#[test]
fn type_not_defined_refuses_api_file_references_and_body_member_unions() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("type-not-defined");
    for (spec, element) in [
        ("probe.yml", "POST /users responses/403"),
        ("api-status-sweep-probe.yml", "POST /s400 responses/400"),
        ("api-response-probe.yml", "POST /users responses/201"),
        ("api-parameter-probe.yml", "POST /users/{f} parameter f"),
        ("api-body-probe.yml", "POST /users requestBody"),
        (
            "union-member-body-probe.yml",
            "components/schemas/Proc/properties/events/oneOf/0",
        ),
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(spec), strict).unwrap();
            let failures = refused_failures("type-not-defined", &run, element, strict);
            assert!(failures.is_empty(), "{spec}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1, "{spec}: {}", run.stderr);
        }
    }
    // Recovery: the same operation filed under another tag, and the union
    // with one member no longer carrying a single discriminant value.
    let dir = tempfile::tempdir().unwrap();
    let probe = std::fs::read_to_string(class.join("probe.yml")).unwrap();
    let union = std::fs::read_to_string(class.join("union-member-body-probe.yml")).unwrap();
    for (name, text) in [
        (
            "users-tag.yml",
            probe.replace("tags: [api]", "tags: [users]"),
        ),
        (
            "plain-member.yml",
            union.replace("{type: string, enum: [OPERATOR]}", "{type: string}"),
        ),
    ] {
        let recovered = dir.path().join(name);
        std::fs::write(&recovered, text).unwrap();
        generates_identically_in_both_modes(&recovered);
    }
    for control in [
        "api-file-accepted-control.yml",
        "other-file-control.yml",
        "group-name-control.yml",
        "union-member-control.yml",
    ] {
        generates_identically_in_both_modes(&class.join(control));
    }
}

#[test]
fn missing_discriminant_refusal_follows_fern_examples_and_recovers_with_a_mapped_variant() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("missing-discriminant-property");
    let id = "missing-discriminant-property";
    let probe = class.join("probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            id,
            &run,
            "GET /pets response 200 components/schemas/Pet discriminator kind",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    // Fern refuses every one of these with the class's diagnostic: its own example
    // reaching a union with no mapping target, or an `x-fern-examples` value
    // lacking the discriminant. Plain examples and `x-crozier-examples` rescue none.
    for (case, element) in [
        (
            "request-absent-mapping",
            "POST /pets request components/schemas/Pet",
        ),
        (
            "optional-depth3-absent-mapping",
            "GET /pets response 200 components/schemas/Pet",
        ),
        ("required-depth12-absent-mapping", "components/schemas/Pet"),
        (
            "optional-request-absent-mapping",
            "POST /pets request components/schemas/Pet",
        ),
        ("array-item-absent-mapping", "components/schemas/Pet"),
        ("nullable-absent-mapping", "components/schemas/Pet"),
        (
            "error-response-absent-mapping",
            "GET /pets response 400 components/schemas/Pet",
        ),
        ("no-members-absent-mapping", "components/schemas/Pet"),
        ("nested-union-absent-mapping", "components/schemas/Pet"),
        ("map-value-absent-mapping", "components/schemas/Pet"),
        ("allof-absent-mapping", "components/schemas/Pet"),
        (
            "x-fern-example-without-kind-mapped",
            "GET /pets response 200 x-fern-examples/0",
        ),
        (
            "x-fern-request-example-without-kind-mapped",
            "POST /pets request x-fern-examples/0",
        ),
        (
            "x-fern-example-nested-without-kind-mapped",
            "x-fern-examples/0/pet",
        ),
        (
            "x-crozier-example-with-kind-absent-mapping",
            "components/schemas/Pet",
        ),
        ("example-with-kind-absent-mapping", "components/schemas/Pet"),
    ] {
        let spec = class.join(format!("{case}-probe.yml"));
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures = refused_failures(id, &run, element, strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert!(
                run.stderr.contains("discriminator kind"),
                "{case}: {}",
                run.stderr
            );
            assert_eq!(run.stderr.lines().count(), 1);
        }
    }
    let assert_generates_identically = |spec: &Path| {
        let normal = refusal_run(&crozier, spec, false).unwrap();
        let strict = refusal_run(&crozier, spec, true).unwrap();
        let name = spec.display();
        assert_eq!(normal.code, Some(0), "{name}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{name}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap(),
                "{name}: {file}"
            );
        }
    };
    // One mapping target that resolves gives Fern's example its discriminant.
    let dir = tempfile::tempdir().unwrap();
    let recovered = dir.path().join("recovered.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    std::fs::write(&recovered, text.replace("schemas/Kitten", "schemas/Cat")).unwrap();
    assert_generates_identically(&recovered);
    for control in [
        "half-absent-mapping",
        "first-absent-mapping",
        "anyof-absent-mapping",
        "unused-absent-mapping",
        "optional-depth4-absent-mapping",
        "required3-optional-absent-mapping",
        "nested-union-second-absent-mapping",
        "x-fern-example-with-kind-absent-mapping",
        "x-fern-ignore-operation-absent-mapping",
        "example-without-kind-mapped",
        "empty-mapping",
        "empty-schema-mapping",
    ] {
        assert_generates_identically(&class.join(format!("{control}-control.yml")));
    }
}

/// One example-value class's committed evidence, through the real CLI: the
/// probe is refused in both modes with `diagnostic`, every other measured
/// refused shape (`*-probe.yml`) is refused with the class, and every accepted
/// near miss (`*-control.yml`) generates identical bytes in both modes.
fn example_value_class_holds(id: &str, diagnostic: &str) {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join(id);
    for strict in [false, true] {
        let run = refusal_run(&crozier, &class.join("probe.yml"), strict).unwrap();
        let failures = refused_failures(id, &run, diagnostic, strict);
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1, "{}", run.stderr);
    }
    let mut cases: Vec<_> = std::fs::read_dir(&class)
        .unwrap()
        .map(|entry| entry.unwrap().file_name().into_string().unwrap())
        .filter(|name| name.ends_with("-probe.yml") || name.ends_with("-control.yml"))
        .collect();
    cases.sort();
    assert!(!cases.is_empty(), "{id}: no measured shapes committed");
    for case in cases {
        let spec = class.join(&case);
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        if case.ends_with("-probe.yml") {
            for (run, strict) in [(&normal, false), (&strict, true)] {
                let failures = refused_failures(id, run, &format!("{id}: "), strict);
                assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            }
            continue;
        }
        assert_eq!(normal.code, Some(0), "{case}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{case}: {}", strict.stderr);
        assert!(!normal.files.is_empty(), "{case}");
        assert_eq!(normal.files, strict.files, "{case}");
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap(),
                "{case}: {file}"
            );
        }
    }
}

#[test]
fn example_type_mismatch_refusal_covers_measured_shapes() {
    example_value_class_holds(
        "example-type-mismatch",
        "example-type-mismatch: GET /probe response example",
    );
}

#[test]
fn example_not_enum_value_refusal_covers_measured_shapes() {
    example_value_class_holds(
        "example-not-enum-value",
        "example-not-enum-value: GET /activities x-fern-examples response",
    );
}

#[test]
fn example_unexpected_property_refusal_covers_measured_shapes() {
    example_value_class_holds(
        "example-unexpected-property",
        "example-unexpected-property: GET /probe components/schemas/Thing_Item collides with ThingItem",
    );
}

#[test]
fn example_missing_required_property_refusal_covers_measured_shapes() {
    example_value_class_holds(
        "example-missing-required-property",
        "example-missing-required-property: GET /requests/{id} response extends nullable",
    );
}

#[test]
fn enum_default_refusal_recovers_with_a_retained_default() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("default-not-enum-value");
    let probe = class.join("probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            "default-not-enum-value",
            &run,
            "ListRequest/properties/sort",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    let dir = tempfile::tempdir().unwrap();
    let repaired = dir.path().join("repaired.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    std::fs::write(
        &repaired,
        text.replace("default: -createdAt", "default: createdAt"),
    )
    .unwrap();
    let normal = refusal_run(&crozier, &repaired, false).unwrap();
    let strict = refusal_run(&crozier, &repaired, true).unwrap();
    assert_eq!(normal.code, Some(0), "{}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{}", strict.stderr);
    assert!(!normal.files.is_empty());
    assert_eq!(normal.files, strict.files);
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap()
        );
    }
    for case in [
        "operation-scalar-collision",
        "operation-array",
        "unused-schema-collision",
        "unused-object-property-collision",
        "response-root-collision",
        "request-root-collision",
        "shared-parameter-collision",
    ] {
        let spec = class.join(format!("{case}-probe.yml"));
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures = refused_failures("default-not-enum-value", &run, "default", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1);
        }
        let recovered = dir.path().join(format!("{case}.yml"));
        let text = std::fs::read_to_string(&spec).unwrap();
        std::fs::write(
            &recovered,
            text.replace("default: -createdAt", "default: createdAt")
                .replace("default: third", "default: first"),
        )
        .unwrap();
        for strict in [false, true] {
            let run = refusal_run(&crozier, &recovered, strict).unwrap();
            assert_eq!(run.code, Some(0), "{case}: {}", run.stderr);
            assert!(!run.files.is_empty());
        }
    }
    for control in [
        "declared-members-control.yml",
        "canonical-empty-members-control.yml",
        "shared-parameter-control.yml",
        "unused-object-control.yml",
        "response-root-control.yml",
        "request-root-control.yml",
    ] {
        let spec = class.join(control);
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(normal.code, Some(0), "{control}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{control}: {}", strict.stderr);
        assert!(!normal.files.is_empty());
        assert_eq!(normal.files, strict.files);
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap()
            );
        }
    }
}

/// `generator-lint-failure`: each shape whose generated Python pinned Fern's own
/// `ruff check` rejects is refused in both modes, naming the element, while
/// every measured near-miss Fern generates from writes the same SDK in both.
#[test]
fn generator_lint_refusals_name_each_shape_and_spare_measured_near_misses() {
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("generator-lint-failure");
    for (probe, element) in [
        (
            "probe.yml",
            "type Event variants \"user:account_deleted\" and \"user_account:deleted\" are both Event_UserAccountDeleted",
        ),
        ("root-collision-probe.yml", "GET /search root method and sub-client search"),
        (
            "tag-suffix-collision-probe.yml",
            "GET /search root method and sub-client search",
        ),
        ("untitled-summary-probe.yml", "POST /change-requests method name is empty"),
        ("server-hyphen-probe.yml", "variable \"api-version\""),
        ("server-dot-probe.yml", "variable \"api.version\""),
        ("server-keyword-probe.yml", "variable \"class\""),
        ("server-unbound-placeholder-probe.yml", "placeholder \"extra\""),
        ("slash-property-probe.yml", "type Result property \"/\""),
        ("empty-enum-probe.yml", "components/schemas/Result enum has no non-null value"),
        ("null-only-enum-probe.yml", "components/schemas/Result enum has no non-null value"),
        ("null-enum-not-nullable-probe.yml", "components/schemas/Result enum has no non-null value"),
        (
            "inline-null-only-enum-probe.yml",
            "components/schemas/Result/properties/temperature/anyOf/1 enum has no non-null value",
        ),
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &class.join(probe), strict).unwrap();
            let failures = refused_failures("generator-lint-failure", &run, element, strict);
            assert!(failures.is_empty(), "{probe}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1, "{probe}: {}", run.stderr);
        }
    }
    for control in [
        "distinct-discriminants-control.yml",
        "single-root-method-control.yml",
        "canonical-group-name-control.yml",
        "ascii-summary-control.yml",
        "server-identifier-control.yml",
        "server-secondary-hyphen-control.yml",
        "server-placeholder-without-variables-control.yml",
        "slash-prefixed-property-control.yml",
        "null-and-value-enum-control.yml",
    ] {
        let spec = class.join(control);
        let normal = refusal_run(&crozier, &spec, false).unwrap();
        let strict = refusal_run(&crozier, &spec, true).unwrap();
        assert_eq!(normal.code, Some(0), "{control}: {}", normal.stderr);
        assert_eq!(strict.code, Some(0), "{control}: {}", strict.stderr);
        assert!(!normal.files.is_empty(), "{control}");
        assert_eq!(normal.files, strict.files, "{control}");
        for file in &normal.files {
            assert_eq!(
                std::fs::read(normal.target.join(file)).unwrap(),
                std::fs::read(strict.target.join(file)).unwrap(),
                "{control}: {file:?}"
            );
        }
    }
}

/// Asserts a spec generates, with identical bytes with and without `--fern-strict`.
fn assert_generates_in_both_modes(spec: &Path, label: &str) {
    let normal = refusal_run(&crozier, spec, false).unwrap();
    let strict = refusal_run(&crozier, spec, true).unwrap();
    assert_eq!(normal.code, Some(0), "{label}: {}", normal.stderr);
    assert_eq!(strict.code, Some(0), "{label}: {}", strict.stderr);
    assert!(!normal.files.is_empty(), "{label}");
    assert_eq!(normal.files, strict.files, "{label}");
    for file in &normal.files {
        assert_eq!(
            std::fs::read(normal.target.join(file)).unwrap(),
            std::fs::read(strict.target.join(file)).unwrap(),
            "{label}: {file:?}"
        );
    }
}

#[test]
fn duplicate_example_name_refusal_follows_the_examples_fern_names() {
    let id = "duplicate-example-name";
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join(id);
    let probe = class.join("probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            id,
            &run,
            "POST /probe request example name Order updated",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    // Every shape pinned Fern refuses, each named where Fern names it.
    for (case, element) in [
        ("response-dupe", "POST /probe response example name Same"),
        (
            "first-2xx-dupe-201-202",
            "GET /probe response example name Same",
        ),
        (
            "resp-200-nocontent-201-dupe",
            "GET /probe response example name Same",
        ),
        (
            "resp-200-xml-201-dupe",
            "GET /probe response example name Same",
        ),
        (
            "default-response-dupe",
            "GET /probe response example name Same",
        ),
        (
            "resp-400-and-default-dupe",
            "GET /probe response example name Same",
        ),
        ("form-request-dupe", "POST /probe request example name Same"),
        (
            "req-vnd-dupe-then-json",
            "POST /probe request example name Same",
        ),
        (
            "x-fern-examples-dupe",
            "POST /probe x-fern-examples name Same",
        ),
        (
            "x-fern-examples-empty-list",
            "POST /probe request example name Same",
        ),
        (
            "summary-equals-key",
            "POST /probe request example name second",
        ),
        ("empty-summaries", "POST /probe request example name "),
        ("numeric-summaries", "POST /probe request example name 1"),
        (
            "ref-summary-override",
            "POST /probe request example name Same",
        ),
        (
            "referenced-summary",
            "POST /probe request example name Order updated",
        ),
        (
            "ignored-example",
            "POST /probe request example name Order updated",
        ),
        (
            "component-response",
            "POST /probe response example name Same",
        ),
        (
            "component-request-body",
            "POST /probe request example name Same",
        ),
    ] {
        let spec = class.join(format!("{case}-probe.yml"));
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures = refused_failures(id, &run, element, strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1, "{case}");
        }
    }
    // Distinct summaries recover the probe.
    let dir = tempfile::tempdir().unwrap();
    let recovered = dir.path().join("recovered.yml");
    let mut text = std::fs::read_to_string(&probe).unwrap();
    let second = text.rfind("summary: Order updated").unwrap();
    text.insert_str(second + "summary: Order updated".len(), " again");
    std::fs::write(&recovered, text).unwrap();
    assert_generates_in_both_modes(&recovered, "recovered probe");
    // Near misses pinned Fern accepts generate identical bytes in both modes.
    for control in [
        "req-resp-summary",
        "across-operations",
        "error-response-dupe",
        "second-2xx-dupe",
        "resp-204-206-dupe",
        "resp-201-nocontent-default-dupe",
        "resp-200-html-201-dupe",
        "resp-2XX-dupe",
        "req-json-then-form-dupe",
        "multipart-request-dupe",
        "second-json-media-type-dupe",
        "req-xml-dupe-only",
        "number-vs-string-summary",
        "request-null-summary",
        "ref-no-summary-same-target",
        "x-fern-examples-plus-openapi-dupe",
        "x-fern-examples-unnamed",
        "x-crozier-examples-dupe",
        "ignored-operation",
        "ignored-path-item",
        "webhook-dupe",
        "unused-component-response",
        "parameter-examples-dupe",
        "different-case",
        "trailing-space",
    ] {
        assert_generates_in_both_modes(&class.join(format!("{control}-control.yml")), control);
    }
}

#[test]
fn example_query_parameter_refusal_follows_the_examples_fern_checks() {
    let id = "example-missing-required-query-parameter";
    let class = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join(id);
    let probe = class.join("probe.yml");
    for strict in [false, true] {
        let run = refusal_run(&crozier, &probe, strict).unwrap();
        let failures = refused_failures(
            id,
            &run,
            "GET /collections x-fern-examples/0 query parameter f",
            strict,
        );
        assert!(failures.is_empty(), "{}", failures.join("\n"));
        assert_eq!(run.stderr.lines().count(), 1);
    }
    // Every shape pinned Fern refuses, each named where Fern names it.
    for (case, element) in [
        (
            "required-default-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "required-null-value",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "path-level-required-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "response-only-example",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "wrong-case-key",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "second-entry-omits",
            "GET /collections x-fern-examples/1 query parameter f",
        ),
        (
            "renamed-param-uses-sdk-name",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "ref-param-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "two-required-one-given",
            "GET /collections x-fern-examples/0 query parameter b",
        ),
        (
            "required-object-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "required-untyped-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
        (
            "required-content-param-omitted",
            "GET /collections x-fern-examples/0 query parameter f",
        ),
    ] {
        let spec = class.join(format!("{case}-probe.yml"));
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures = refused_failures(id, &run, element, strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
            assert_eq!(run.stderr.lines().count(), 1, "{case}");
        }
    }
    // Fern also reports the parameter missing from the example it writes for
    // an optional named query type in its `api.yml` file; that file is the
    // `type-not-defined` mechanism, whose refusal names the parameter first.
    for case in [
        "api-tag-optional-enum",
        "api-tag-lower-optional-enum",
        "api-tag-optional-ref-enum",
        "api-tag-optional-array-enum",
        "api-tag-nullable-enum",
    ] {
        let spec = class.join(format!("{case}-probe.yml"));
        for strict in [false, true] {
            let run = refusal_run(&crozier, &spec, strict).unwrap();
            let failures =
                refused_failures("type-not-defined", &run, "GET /things parameter f", strict);
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
        }
    }
    // Giving the required parameter recovers the probe.
    let dir = tempfile::tempdir().unwrap();
    let recovered = dir.path().join("recovered.yml");
    let text = std::fs::read_to_string(&probe).unwrap();
    assert!(text.contains("query-parameters: {}"));
    std::fs::write(
        &recovered,
        text.replace("query-parameters: {}", "query-parameters: {f: json}"),
    )
    .unwrap();
    assert_generates_in_both_modes(&recovered, "recovered probe");
    // Near misses pinned Fern accepts generate identical bytes in both modes.
    for control in [
        "no-query-parameters-key",
        "optional-param-omitted",
        "required-with-example-no-ext",
        "required-no-examples",
        "required-nullable-omitted",
        "x-crozier-examples-omitted",
        "required-array-omitted",
        "renamed-param-uses-wire-name",
        "required-31-null-union-omitted",
        "ignored-operation",
        "query-parameters-null",
        "empty-list",
        "ignored-param-omitted",
        "api-tag-optional-string",
        "api-tag-optional-array-string",
        "api-second-tag-optional-enum",
        "other-tag-optional-enum",
        "untagged-optional-enum",
    ] {
        assert_generates_in_both_modes(&class.join(format!("{control}-control.yml")), control);
    }
}
/// Refusal happens before touching an existing SDK; an explicit document name
/// recovers generation without changing the declared enum wire value.
#[test]
fn unnameable_enum_refusal_preserves_output_and_recovers_with_declared_name() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let output = dir.path().join("sdk");
    std::fs::create_dir(&output).unwrap();
    std::fs::write(output.join("keep.txt"), "existing SDK").unwrap();
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/enum-value-unnameable/probe.yml"),
    )
    .unwrap();
    std::fs::write(&spec, &probe).unwrap();
    for strict in [false, true] {
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .args(["--package-name", "probe"]);
        if strict {
            command.arg("--fern-strict");
        }
        let run = command.output().unwrap();
        assert_eq!(run.status.code(), Some(1));
        let stderr = String::from_utf8(run.stderr).unwrap();
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        assert!(stderr.contains("enum-value-unnameable"), "{stderr}");
        if strict {
            assert!(stderr.contains("fern-strict"), "{stderr}");
        }
        assert!(
            stderr.contains("Minutes") && stderr.contains("10080"),
            "{stderr}"
        );
        assert_eq!(std::fs::read_dir(&output).unwrap().count(), 1);
        assert_eq!(
            std::fs::read_to_string(output.join("keep.txt")).unwrap(),
            "existing SDK"
        );
    }
    for (first, second) in [("緊急", "補助"), ("!!!", "???")] {
        std::fs::write(
            &spec,
            probe.replace("10080", first).replace("20160", second),
        )
        .unwrap();
        let run = crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .arg("--fern-strict")
            .output()
            .unwrap();
        assert_eq!(run.status.code(), Some(1));
        let stderr = String::from_utf8(run.stderr).unwrap();
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        let class = if first.is_ascii() {
            "enum-name-unsuitable"
        } else {
            "enum-value-unnameable"
        };
        assert!(
            stderr.contains(class) && stderr.contains("fern-strict"),
            "{stderr}"
        );
        assert!(
            stderr.contains(first) && stderr.contains("Minutes"),
            "{stderr}"
        );
        assert_eq!(std::fs::read_dir(&output).unwrap().count(), 1);
    }
    std::fs::write(
        &spec,
        probe.replace(
            "      enum:",
            "      x-crozier-enum:\n        '10080': {name: 2fa}\n      enum:",
        ),
    )
    .unwrap();
    let run = crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&output)
        .output()
        .unwrap();
    assert_eq!(run.status.code(), Some(1));
    assert!(String::from_utf8(run.stderr)
        .unwrap()
        .contains("enum-value-unnameable"));
    assert_eq!(std::fs::read_dir(&output).unwrap().count(), 1);
    std::fs::write(
        &spec,
        probe.replace(
            "      enum:",
            "      x-crozier-enum:\n        '10080': {name: WEEK}\n        '20160': {name: FORTNIGHT}\n      enum:",
        ),
    )
    .unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&output)
        .args(["--package-name", "probe", "--fern-strict"])
        .assert()
        .success();
    let module = std::fs::read_to_string(output.join("src/probe/types/minutes.py")).unwrap();
    assert!(module.contains("WEEK = \"10080\""), "{module}");
    assert!(module.contains("FORTNIGHT = \"20160\""), "{module}");
}

#[test]
fn inline_unnameable_enums_report_their_operation_and_recover() {
    let enum_schema = serde_json::json!({"type": "string", "enum": ["10080", "20160"]});
    for (kind, location) in [
        ("parameter", "GET /probe parameter mode"),
        ("parameter-content", "GET /probe parameter mode"),
        ("body", "GET /probe request body/items/additionalProperties"),
        (
            "response",
            "GET /probe response 200/oneOf/0/allOf/0/anyOf/0",
        ),
    ] {
        let dir = tempfile::tempdir().unwrap();
        let spec = dir.path().join("api.json");
        let output = dir.path().join("sdk");
        let mut operation = serde_json::json!({
            "operationId": "probe",
            "responses": {"204": {"description": "No content"}}
        });
        match kind {
            "parameter" => {
                operation["parameters"] = serde_json::json!([
                    {"name": "mode", "in": "query", "schema": enum_schema}
                ]);
            }
            "parameter-content" => {
                operation["parameters"] = serde_json::json!([
                    {"name": "mode", "in": "query", "content": {
                        "application/json": {"schema": enum_schema}
                    }}
                ]);
            }
            "body" => {
                operation["requestBody"] = serde_json::json!({"content": {
                    "application/json": {"schema": {"type": "array", "items": {
                        "type": "object", "additionalProperties": enum_schema
                    }}}
                }});
            }
            "response" => {
                operation["responses"] = serde_json::json!({"200": {
                    "description": "Enum result", "content": {"application/json": {
                        "schema": {"oneOf": [{"allOf": [{"anyOf": [enum_schema]}]}]}
                    }}
                }});
            }
            _ => unreachable!(),
        }
        let document = serde_json::json!({
            "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
            "paths": {"/probe": {"get": operation}}
        });
        let text = serde_json::to_string(&document).unwrap();
        std::fs::write(&spec, &text).unwrap();
        let run = crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .args(["--package-name", "probe"])
            .output()
            .unwrap();
        let stderr = String::from_utf8(run.stderr).unwrap();
        assert_eq!(run.status.code(), Some(1), "{kind}: {stderr}");
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        assert!(stderr.contains("enum-value-unnameable"), "{stderr}");
        assert!(stderr.contains(location), "{kind}: {stderr}");
        assert!(stderr.contains("10080"), "{stderr}");
        assert!(!output.exists(), "{kind}: refusal created output");
        std::fs::write(
            &spec,
            text.replace("10080", "9999").replace("20160", "9000"),
        )
        .unwrap();
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .args(["--package-name", "probe", "--fern-strict"])
            .assert()
            .success();
        assert!(output.join("pyproject.toml").is_file(), "{kind}");
    }
}

/// Fern treats integer enums and mixed-kind string enums as scalar aliases,
/// including Bungie's integer bit flags written with string enum values.
#[test]
fn non_string_and_mixed_enums_generate_without_name_refusals() {
    for (ty, values, alias) in [
        ("integer", serde_json::json!(["10080", "20160"]), "int"),
        ("string", serde_json::json!(["10080", false]), "str"),
    ] {
        let dir = tempfile::tempdir().unwrap();
        let spec = dir.path().join("api.json");
        let output = dir.path().join("sdk");
        let document = serde_json::json!({
            "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
            "paths": {"/probe": {"get": {"operationId": "probe", "responses": {
                "200": {"description": "Scope value", "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/Scopes"}
                }}}
            }}}},
            "components": {"schemas": {"Scopes": {"type": ty, "enum": values}}}
        });
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output)
                .args(["--package-name", "probe"]);
            if strict {
                command.arg("--fern-strict");
            }
            command.assert().success();
            let module = std::fs::read_to_string(output.join("src/probe/types/scopes.py")).unwrap();
            assert!(module.contains(&format!("Scopes = {alias}")), "{module}");
            assert!(!module.contains("_10080"), "{module}");
        }
    }
}

#[test]
fn discriminant_refusals_recover_with_a_valid_document_name() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let output = dir.path().join("sdk");
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/discriminant-value-unsuitable/probe.yml"),
    )
    .unwrap();
    for name in ["_t", "kind-name", "1kind"] {
        std::fs::write(&spec, probe.replace("_t", name)).unwrap();
        for strict in [false, true] {
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            let run = command.output().unwrap();
            assert_eq!(run.status.code(), Some(1));
            let stderr = String::from_utf8(run.stderr).unwrap();
            assert_eq!(stderr.lines().count(), 1, "{stderr}");
            assert!(stderr.contains("discriminant-value-unsuitable"), "{stderr}");
            assert!(
                stderr.contains("Asset") && stderr.contains(name),
                "{stderr}"
            );
            if strict {
                assert!(stderr.contains("fern-strict"), "{stderr}");
            }
            assert!(!output.exists());
        }
    }
    for inferred in [false, true] {
        let mut document: serde_json::Value = serde_yaml_ng::from_str(&probe).unwrap();
        if inferred {
            document["components"]["schemas"]["Asset"]
                .as_object_mut()
                .unwrap()
                .remove("discriminator");
            for (variant, value) in [("ImageAsset", "image"), ("TextAsset", "text")] {
                document["components"]["schemas"][variant]["properties"]["_t"]["enum"] =
                    serde_json::json!([value]);
            }
        } else {
            document["components"]["schemas"]["Asset"]
                .as_object_mut()
                .unwrap()
                .remove("oneOf");
        }
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output)
            .arg("--fern-strict")
            .assert()
            .code(1)
            .stderr(predicates::str::contains("discriminant-value-unsuitable"));
        assert!(!output.exists());
    }
    std::fs::write(&spec, probe.replace("_t", "kind_name")).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&output)
        .args(["--package-name", "probe", "--fern-strict"])
        .assert()
        .success();
    let module = std::fs::read_to_string(output.join("src/probe/types/asset.py")).unwrap();
    assert!(module.contains("kind_name:"), "{module}");
}

#[test]
fn scalar_singleton_body_enum_needs_no_member_but_nested_enums_do() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    for nested in [false, true] {
        let scalar = serde_json::json!({"type": "string", "enum": ["10080"]});
        let schema = if nested {
            serde_json::json!({"type": "object", "properties": {"minutes": scalar}})
        } else {
            scalar
        };
        let document = serde_json::json!({
            "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
            "paths": {"/probe": {"post": {"operationId": "probe", "requestBody": {
                "required": true, "content": {"application/json": {"schema": schema}}
            }, "responses": {"204": {"description": "Done"}}}}}
        });
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let output = dir.path().join(format!("sdk-{nested}-{strict}"));
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output)
                .args(["--package-name", "probe"]);
            if strict {
                command.arg("--fern-strict");
            }
            if nested {
                command
                    .assert()
                    .code(1)
                    .stderr(predicates::str::contains("enum-value-unnameable"));
                assert!(!output.exists());
            } else {
                command.assert().success();
                assert!(output.join("pyproject.toml").is_file());
            }
        }
    }
}

#[test]
fn repeated_path_names_refuse_and_distinct_positions_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/duplicate-path-parameter/probe.yml"),
    )
    .unwrap();
    let document: serde_json::Value = serde_yaml_ng::from_str(&probe).unwrap();
    let mut item = document["paths"]["/accounts/{account_id}/members/{account_id}"].clone();
    item["get"]["parameters"]
        .as_array_mut()
        .unwrap()
        .push(serde_json::json!({
            "name": "member_id", "in": "path", "required": true, "schema": {"type": "string"}
        }));
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        std::fs::write(&spec, &probe).unwrap();
        let run = |refused: bool| {
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            if refused {
                command
                    .assert()
                    .code(1)
                    .stderr(predicates::str::contains("duplicate-path-parameter"));
                assert!(!output.exists());
            } else {
                command.assert().success();
            }
        };
        run(true);
        let mut recovered = document.clone();
        recovered["paths"] =
            serde_json::json!({"/accounts/{account_id}/members/{member_id}": item});
        std::fs::write(&spec, serde_json::to_string(&recovered).unwrap()).unwrap();
        run(false);
        // A repeated declaration for one position is accepted by pinned Fern.
        recovered["paths"] = serde_json::json!({"/accounts/{account_id}": {
            "get": {"operationId": "getMember", "parameters": [
                {"name": "account_id", "in": "path", "required": true, "schema": {"type": "string"}},
                {"name": "account_id", "in": "path", "required": true, "schema": {"type": "string"}}
            ], "responses": {"204": {"description": "Done"}}}
        }});
        std::fs::write(&spec, serde_json::to_string(&recovered).unwrap()).unwrap();
        run(false);
    }
}

#[test]
fn normalized_parameter_collisions_refuse_and_renamed_parameters_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/request-property-camelcase-collision/probe.yml"),
    )
    .unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        std::fs::write(&spec, &probe).unwrap();
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        command.assert().code(1).stderr(predicates::str::contains(
            "request-property-camelcase-collision",
        ));
        assert!(!output.exists());
        std::fs::write(&spec, probe.replace("accountId", "otherAccountId")).unwrap();
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        command.assert().success();
        assert!(output.join("pyproject.toml").is_file());
    }
}

#[test]
fn inferred_path_and_body_parameter_names_share_collision_validation() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    for (route, parameters, body) in [
        (
            "/accounts/{+accountId}",
            serde_json::json!([{"name": "accountId", "in": "path", "required": true, "schema": {"type": "string"}}]),
            serde_json::Value::Null,
        ),
        (
            "/accounts",
            serde_json::json!([{"name": "accountId", "in": "query", "schema": {"type": "string"}}]),
            serde_json::json!({"type": "object", "properties": {"account_id": {"type": "string"}}}),
        ),
    ] {
        let mut op = serde_json::json!({"operationId": "probe", "parameters": parameters, "responses": {"204": {"description": "Done"}}});
        if !body.is_null() {
            op["requestBody"] =
                serde_json::json!({"content": {"application/json": {"schema": body}}});
        }
        let document = serde_json::json!({"openapi": "3.0.3", "info": {"title": "probe", "version": "1"}, "paths": {route: {"post": op}}});
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let output = dir.path().join(format!("sdk-{strict}"));
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            // Pinned Fern reports both an unreferenced path parameter and the
            // camelCase collision for `{+accountId}`
            // (type-name-collision/evidence/reserved-expansion-path.pinned-fern.log);
            // the document-family check names it first.
            let class = if route.contains('+') {
                "path-parameter-unreferenced"
            } else {
                "request-property-camelcase-collision"
            };
            command
                .assert()
                .code(1)
                .stderr(predicates::str::contains(class));
            assert!(!output.exists());
        }
    }
}

#[test]
fn declared_parameter_names_deconflict_refusals_without_repairing_generation() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/request-property-camelcase-collision/probe.yml"),
    )
    .unwrap();
    for body in [false, true] {
        let mut document: serde_json::Value = serde_yaml_ng::from_str(&probe).unwrap();
        let op = &mut document["paths"]["/accounts"]["get"];
        let hint = serde_json::json!({"type": "string", "x-fern-parameter-name": "account_id", "x-crozier-parameter-name": "otherAccount"});
        if body {
            op["parameters"].as_array_mut().unwrap().truncate(1);
            op["requestBody"] = serde_json::json!({"content": {"application/json": {"schema": {"type": "object", "properties": {"accountId": hint}}}}});
        } else {
            op["parameters"][1]["x-fern-parameter-name"] = serde_json::json!("account_id");
            op["parameters"][1]["x-crozier-parameter-name"] = serde_json::json!("otherAccount");
        }
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let output = dir.path().join(format!("sdk-{body}-{strict}"));
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            let result = command.output().unwrap();
            let stderr = String::from_utf8(result.stderr).unwrap();
            // Parameter-only baseline generation still fails at ruff. The
            // body case already generates; this node changes neither outcome.
            assert!(
                !stderr.contains("request-property-camelcase-collision"),
                "{stderr}"
            );
            if body {
                assert_eq!(result.status.code(), Some(0), "{stderr}");
                assert!(output.join("pyproject.toml").is_file());
            } else {
                assert_eq!(result.status.code(), Some(1), "{stderr}");
                // ruff words this per version ("Duplicate parameter" at the
                // pinned .ruff-version, "Duplicate keyword argument" later).
                assert!(
                    stderr.contains("with ruff failed")
                        && stderr.contains("Duplicate")
                        && stderr.contains("\"account_id\""),
                    "{stderr}"
                );
                assert!(!output.exists());
            }
        }
    }
}

#[test]
fn body_names_colliding_with_path_names_refuse_but_query_and_header_names_generate() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let probe = std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/request-property-name-collision/probe.yml"),
    )
    .unwrap();
    for location in ["path", "query", "header"] {
        let mut document: serde_json::Value = serde_yaml_ng::from_str(&probe).unwrap();
        let mut op = document["paths"]["/repos/{name}"]["patch"].clone();
        op["parameters"][0]["in"] = serde_json::json!(location);
        let route = if location == "path" {
            "/repos/{name}"
        } else {
            "/repos"
        };
        document["paths"] = serde_json::json!({route: {"patch": op}});
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let output = dir.path().join(format!("sdk-{location}-{strict}"));
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            if location == "path" {
                command
                    .assert()
                    .code(1)
                    .stderr(predicates::str::contains("request-property-name-collision"));
                assert!(!output.exists());
            } else {
                command.assert().success();
                assert!(output.join("pyproject.toml").is_file());
            }
        }
    }
    let recovered = probe
        .replace("name: name", "name: repo_name")
        .replace("{name}", "{repo_name}");
    std::fs::write(&spec, recovered).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn parameters_in_different_locations_refuse_and_declared_names_recover_classification() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "paths": {"/probe": {"get": {"operationId": "probe", "parameters": [
            {"name": "name", "in": "query", "schema": {"type": "string"}},
            {"name": "name", "in": "header", "schema": {"type": "string"}}
        ], "responses": {"204": {"description": "Done"}}}}}
    });
    for declared in [false, true] {
        if declared {
            document["paths"]["/probe"]["get"]["parameters"][1]["x-fern-parameter-name"] =
                serde_json::json!("headerName");
        }
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for strict in [false, true] {
            let output = dir.path().join(format!("sdk-{declared}-{strict}"));
            let mut command = crozier_clean_env();
            command
                .args(["--no-config", "generate", "python", "--spec"])
                .arg(&spec)
                .arg("--output")
                .arg(&output);
            if strict {
                command.arg("--fern-strict");
            }
            let result = command.output().unwrap();
            let stderr = String::from_utf8(result.stderr).unwrap();
            if declared {
                assert!(
                    !stderr.contains("request-property-camelcase-collision"),
                    "{stderr}"
                );
                if !result.status.success() {
                    assert!(stderr.contains("ruff"), "{stderr}");
                } else {
                    assert!(output.join("pyproject.toml").is_file());
                }
            } else {
                assert_eq!(result.status.code(), Some(1), "{stderr}");
                assert!(
                    stderr.contains("request-property-camelcase-collision"),
                    "{stderr}"
                );
                assert!(!output.exists());
            }
        }
    }
}

/// Runs `crozier generate python` over `document` in both modes, asserting each
/// refusal exits 1, writes nothing, prints one line naming `class` and
/// `element`, and names `fern-strict` only in strict mode.
fn assert_name_refusal_in_both_modes(document: &serde_json::Value, class: &str, element: &str) {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        assert!(stderr.contains(class), "{stderr}");
        assert!(stderr.contains(element), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict, "{stderr}");
        assert!(!output.exists());
    }
}

fn assert_generates_under_fern_strict(document: &serde_json::Value) {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("sdk"))
        .arg("--fern-strict")
        .assert()
        .success();
    assert!(dir.path().join("sdk/pyproject.toml").is_file());
}

#[test]
fn parameters_with_different_wire_names_but_one_declared_name_refuse_as_name_collisions() {
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "paths": {"/probe": {"get": {"operationId": "probe", "parameters": [
            {"name": "q", "in": "query", "x-fern-parameter-name": "filter",
             "schema": {"type": "string"}},
            {"name": "F", "in": "header", "x-crozier-parameter-name": "filter",
             "schema": {"type": "string"}}
        ], "responses": {"204": {"description": "Done"}}}}}
    });
    assert_name_refusal_in_both_modes(&document, "request-property-name-collision", "\"filter\"");
    document["paths"]["/probe"]["get"]["parameters"][1]["x-crozier-parameter-name"] =
        serde_json::json!("headerFilter");
    assert_generates_under_fern_strict(&document);
}

#[test]
fn x_prefixed_headers_collide_under_fern_header_naming_and_recover_when_renamed() {
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "paths": {"/probe": {"get": {"operationId": "probe", "parameters": [
            {"name": "requestId", "in": "query", "schema": {"type": "string"}},
            {"name": "X-Request-Id", "in": "header", "schema": {"type": "string"}}
        ], "responses": {"204": {"description": "Done"}}}}}
    });
    assert_name_refusal_in_both_modes(
        &document,
        "request-property-name-collision",
        "\"X-Request-Id\"",
    );
    document["paths"]["/probe"]["get"]["parameters"][0]["name"] = serde_json::json!("traceId");
    assert_generates_under_fern_strict(&document);
}

#[test]
fn duplicate_inherited_body_properties_refuse_in_a_cleanly_parsed_document() {
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "components": {"schemas": {
            "Base": {"type": "object", "properties": {"name": {"type": "string"}}}
        }},
        "paths": {"/probe": {"post": {"operationId": "probe", "requestBody": {"content": {
            "application/json": {"schema": {"allOf": [
                {"$ref": "#/components/schemas/Base"},
                {"type": "object", "properties": {"name": {"type": "string"}}}
            ]}}
        }}, "responses": {"204": {"description": "Done"}}}}}
    });
    assert_name_refusal_in_both_modes(
        &document,
        "request-property-name-collision",
        "body property \"name\"",
    );
    document["paths"]["/probe"]["post"]["requestBody"]["content"]["application/json"]["schema"]
        ["allOf"][1]["properties"] = serde_json::json!({"otherName": {"type": "string"}});
    assert_generates_under_fern_strict(&document);
}

#[test]
fn body_name_refusal_survives_an_unrelated_parse_failure_and_preserves_recovery() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "components": {"schemas": {
            "Base": {"type": "object", "properties": {"name": {"type": "string"}}},
            "Malformed": {"type": "string", "nullable": 1}
        }},
        "paths": {"/probe": {"post": {"operationId": "probe", "requestBody": {"content": {
            "application/json": {"schema": {"allOf": [
                {"$ref": "#/components/schemas/Base"},
                {"type": "object", "properties": {"name": {"type": "string"}}}
            ]}}
        }}, "responses": {"204": {"description": "Done"}}}}}
    });
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1));
        assert!(
            stderr.contains("request-property-name-collision"),
            "{stderr}"
        );
        assert_eq!(stderr.contains("fern-strict"), strict, "{stderr}");
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        assert!(!output.exists());
    }
    // An ignored operation does not acquire a name refusal. Its unrelated
    // malformed schema still receives the existing parser diagnostic.
    document["paths"]["/probe"]["post"]["x-crozier-ignore"] = serde_json::json!(true);
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    let result = crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("ignored"))
        .arg("--fern-strict")
        .output()
        .unwrap();
    let stderr = String::from_utf8(result.stderr).unwrap();
    assert_eq!(result.status.code(), Some(1));
    assert!(stderr.contains("expected a boolean"), "{stderr}");
    assert!(
        !stderr.contains("request-property-name-collision"),
        "{stderr}"
    );
    document["paths"]["/probe"]["post"]
        .as_object_mut()
        .unwrap()
        .remove("x-crozier-ignore");
    for labelled in [false, true] {
        let op = document["paths"]["/probe"]["post"].as_object_mut().unwrap();
        if labelled {
            op.insert("x-fern-audiences".to_owned(), serde_json::json!(["public"]));
            op.insert(
                "x-crozier-audiences".to_owned(),
                serde_json::json!(["private"]),
            );
        } else {
            op.remove("x-fern-audiences");
            op.remove("x-crozier-audiences");
        }
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        for audience in ["public", "private"] {
            for audience_strict in [false, true] {
                let output = dir
                    .path()
                    .join(format!("audience-{labelled}-{audience}-{audience_strict}"));
                let mut command = crozier_clean_env();
                command
                    .args(["--no-config", "generate", "python", "--spec"])
                    .arg(&spec)
                    .arg("--output")
                    .arg(&output)
                    .args(["--fern-strict", "--audience", audience]);
                if audience_strict {
                    command.arg("--audience-strict");
                }
                let result = command.output().unwrap();
                let stderr = String::from_utf8(result.stderr).unwrap();
                let kept = if labelled {
                    audience == "private"
                } else {
                    !audience_strict
                };
                assert_eq!(result.status.code(), Some(1), "{stderr}");
                assert_eq!(
                    stderr.contains("request-property-name-collision"),
                    kept,
                    "{stderr}"
                );
                if !kept {
                    assert!(stderr.contains("expected a boolean"), "{stderr}");
                }
                assert!(!output.exists());
            }
        }
    }
    document["components"]["schemas"]["Malformed"]["nullable"] = serde_json::json!(false);
    document["paths"]["/probe"]["post"]
        .as_object_mut()
        .unwrap()
        .remove("x-crozier-ignore");
    document["paths"]["/probe"]["post"]["requestBody"]["content"]["application/json"]["schema"]
        ["allOf"][1]["properties"] = serde_json::json!({"otherName": {"type": "string"}});
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

/// Write `document` as JSON, with each `"BIG"` string replaced by 2^64,
/// an integer YAML's reader rejects, and run `generate --fern-strict` on it.
fn generate_strict_with_big_integers(
    dir: &Path,
    document: &serde_json::Value,
) -> (Option<i32>, String) {
    let spec = dir.join("api.json");
    let text = serde_json::to_string(document)
        .unwrap()
        .replace("\"BIG\"", "18446744073709551616");
    std::fs::write(&spec, text).unwrap();
    let output = dir.join("sdk");
    let _ = std::fs::remove_dir_all(&output);
    let result = crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&output)
        .arg("--fern-strict")
        .output()
        .unwrap();
    (
        result.status.code(),
        String::from_utf8(result.stderr).unwrap(),
    )
}

#[test]
fn read_only_body_properties_and_oversized_json_integers_do_not_change_name_refusals() {
    let dir = tempfile::tempdir().unwrap();
    // `Base.name` collides with the inline `name` an inheriting body redeclares,
    // and `Base.count`'s example is an integer YAML's reader rejects.
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "components": {"schemas": {
            "Base": {"type": "object", "properties": {
                "name": {"type": "string"},
                "count": {"type": "integer", "example": "BIG"}
            }},
            "ReadOnlyName": {"type": "string", "readOnly": true}
        }},
        "paths": {"/probe": {"post": {"operationId": "probe", "requestBody": {"content": {
            "application/json": {"schema": {"allOf": [
                {"$ref": "#/components/schemas/Base"},
                {"type": "object", "properties": {"name": {"type": "string"}}}
            ]}}
        }}, "responses": {"204": {"description": "Done"}}}}}
    });
    // The oversized integer does not hide the collision from the detector.
    let (code, stderr) = generate_strict_with_big_integers(dir.path(), &document);
    assert_eq!(code, Some(1), "{stderr}");
    assert!(
        stderr.contains("request-property-name-collision: POST /probe body property \"name\""),
        "{stderr}"
    );
    // A readOnly property is never sent, so it collides with nothing in the
    // request: declared on the property, or on the component it references.
    for read_only in [
        serde_json::json!({"type": "string", "readOnly": true}),
        serde_json::json!({"$ref": "#/components/schemas/ReadOnlyName"}),
    ] {
        document["components"]["schemas"]["Base"]["properties"]["name"] = read_only;
        let (code, stderr) = generate_strict_with_big_integers(dir.path(), &document);
        assert_eq!(code, Some(0), "{stderr}");
        assert!(dir.path().join("sdk/pyproject.toml").is_file());
    }
    // The source-level fallback, reached when another field fails to parse,
    // skips the readOnly property too, leaving the parser's own diagnostic.
    document["components"]["schemas"]["Base"]["properties"]["name"] =
        serde_json::json!({"type": "string", "readOnly": true});
    document["components"]["schemas"]["Malformed"] =
        serde_json::json!({"type": "string", "nullable": 1});
    let (code, stderr) = generate_strict_with_big_integers(dir.path(), &document);
    assert_eq!(code, Some(1), "{stderr}");
    assert!(stderr.contains("expected a boolean"), "{stderr}");
    assert!(
        !stderr.contains("request-property-name-collision"),
        "{stderr}"
    );
    assert!(!dir.path().join("sdk").exists());
    // Without readOnly the fallback still refuses the collision.
    document["components"]["schemas"]["Base"]["properties"]["name"] =
        serde_json::json!({"type": "string"});
    let (code, stderr) = generate_strict_with_big_integers(dir.path(), &document);
    assert_eq!(code, Some(1), "{stderr}");
    assert!(
        stderr.contains("request-property-name-collision"),
        "{stderr}"
    );
}

#[test]
fn name_refusals_escape_line_breaks_in_offending_schema_names() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"}, "paths": {},
        "components": {"schemas": {"Minutes\nPrivate": {"type": "string", "enum": ["10080", "20160"]}}}
    });
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1));
        assert_eq!(stderr.lines().count(), 1, "{stderr}");
        assert!(stderr.contains("Minutes\\nPrivate"), "{stderr}");
        assert!(stderr.contains("enum-value-unnameable"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict, "{stderr}");
        assert!(!output.exists());
    }
}

#[test]
fn explicit_sdk_method_collisions_refuse_and_distinct_names_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document: serde_json::Value = serde_yaml_ng::from_str(include_str!(
        "../docs/fern-refusals/sdk-method-collision/probe.yml"
    ))
    .unwrap();
    for strict in [false, true] {
        std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
        let output = dir.path().join(format!("refused-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("sdk-method-collision"), "{stderr}");
        assert!(stderr.contains("analytics.create"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert_eq!(stderr.lines().count(), 1);
        assert!(!output.exists());
    }
    document["paths"]["/reports"]["post"]["x-crozier-sdk-method-name"] =
        serde_json::json!("createReport");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
    document["paths"]["/reports"]["post"]
        .as_object_mut()
        .unwrap()
        .remove("x-crozier-sdk-method-name");
    document["paths"]["/reports"]["post"]
        .as_object_mut()
        .unwrap()
        .remove("x-fern-sdk-method-name");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("inferred"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn nullable_inherited_property_collisions_refuse_and_nonnullable_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document: serde_json::Value = serde_yaml_ng::from_str(include_str!(
        "../docs/fern-refusals/object-property-name-collision/probe.yml"
    ))
    .unwrap();
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(
            stderr.contains("object-property-name-collision"),
            "{stderr}"
        );
        assert!(stderr.contains("sha1"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    document["components"]["schemas"]["FileMini"]["nullable"] = serde_json::json!(false);
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn type_names_across_namespaces_refuse_and_distinct_contexts_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document: serde_json::Value = serde_yaml_ng::from_str(include_str!(
        "../docs/fern-refusals/type-name-collision/probe.yml"
    ))
    .unwrap();
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("type-name-collision"), "{stderr}");
        assert!(stderr.contains("GetThingResponse"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    document["paths"]["/b"]["get"]["operationId"] = serde_json::json!("getOtherThing");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
    document["paths"]["/b"]["get"]["operationId"] = serde_json::json!("getThing");
    document["paths"]["/b"]["get"]["tags"] = serde_json::json!(["alpha"]);
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("same-namespace"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn numeric_type_names_refuse_and_valid_declared_names_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document: serde_json::Value = serde_yaml_ng::from_str(include_str!(
        "../docs/fern-refusals/type-name-not-letter-led/probe.yml"
    ))
    .unwrap();
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("type-name-not-letter-led"), "{stderr}");
        assert!(stderr.contains("123456"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    document["components"]["schemas"]["123456"]["x-fern-type-name"] = serde_json::json!("123456");
    document["components"]["schemas"]["123456"]["x-crozier-type-name"] = serde_json::json!("Thing");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    let declared = dir.path().join("declared-name");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&declared)
        .arg("--fern-strict")
        .assert()
        .success();
    // The canonical declaration names the class, its module and the method's
    // return annotation, as Fern names a component by its `x-fern-type-name`
    // (the authored probe `376-350-declared-type-name`).
    assert!(
        std::fs::read_to_string(declared.join("src/probe/types/thing.py"))
            .unwrap()
            .contains("class Thing(")
    );
    assert!(!declared.join("src/probe/types/one23456.py").exists());
    assert!(
        std::fs::read_to_string(declared.join("src/probe/client.py"))
            .unwrap()
            .contains("-> Thing:")
    );
    document["components"]["schemas"]["123456"]
        .as_object_mut()
        .unwrap()
        .remove("x-crozier-type-name");
    document["components"]["schemas"]["123456"]
        .as_object_mut()
        .unwrap()
        .remove("x-fern-type-name");
    let schema = document["components"]["schemas"]
        .as_object_mut()
        .unwrap()
        .remove("123456")
        .unwrap();
    document["components"]["schemas"]["9999"] = schema;
    document["paths"]["/things"]["get"]["responses"]["200"]["content"]["application/json"]
        ["schema"]["$ref"] = serde_json::json!("#/components/schemas/9999");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn oversized_generated_names_refuse_without_writes_and_shorter_names_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    let original = include_str!("../docs/fern-refusals/generated-file-name-too-long/probe.yml");
    std::fs::write(&spec, original).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("generated-file-name-too-long"), "{stderr}");
        assert!(stderr.contains("thing_level5"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    std::fs::write(
        &spec,
        original.replace("_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", ""),
    )
    .unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn unnamed_legacy_object_references_refuse_and_component_references_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"},
        "paths": {"/probe": {"get": {"operationId": "probe", "responses": {
            "200": {"description": "OK", "content": {"application/json": {"schema": {"$ref": "#/definitions/Thing"}}}}
        }}}},
        "definitions": {"Thing": {"type": "object", "properties": {"id": {"type": "string"}}}}
    });
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("type-name-not-letter-led"), "{stderr}");
        assert!(stderr.contains("#/definitions/Thing"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    document["components"] =
        serde_json::json!({"schemas": {"Thing": document["definitions"]["Thing"].clone()}});
    document["paths"]["/probe"]["get"]["responses"]["200"]["content"]["application/json"]
        ["schema"]["$ref"] = serde_json::json!("#/components/schemas/Thing");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn recursive_inline_property_names_refuse_and_named_recursion_recovers() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document = serde_json::json!({
        "openapi": "3.0.3", "info": {"title": "probe", "version": "1"}, "paths": {},
        "components": {"schemas": {"Thing": {"type": "object", "properties": {
            "child": {"type": "object", "properties": {"child": {"$ref": "#/components/schemas/Thing/properties/child"}}}
        }}}}
    });
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("generated-file-name-too-long"), "{stderr}");
        assert!(stderr.contains("#/components/schemas/Thing"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    document["components"]["schemas"]["Thing"]["properties"]["child"] =
        serde_json::json!({"$ref": "#/components/schemas/Thing"});
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

fn assert_measured_name_refusal(document: &serde_json::Value, class: &str, element: &str) {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("sdk-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains(class), "{stderr}");
        assert!(stderr.contains(element), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert_eq!(stderr.lines().count(), 1);
        assert!(!output.exists());
    }
}

#[test]
fn named_components_and_virtual_requests_refuse_their_measured_collisions() {
    let mut document = serde_json::json!({
        "openapi":"3.0.3","info":{"title":"probe","version":"1"},"paths":{},
        "components":{"schemas":{"Thing":{"type":"object","properties":{"id":{"type":"string"}}},
        "thing":{"type":"object","properties":{"name":{"type":"string"}}}}}
    });
    assert_measured_name_refusal(&document, "type-name-collision", "component schemas");
    document["components"]["schemas"]
        .as_object_mut()
        .unwrap()
        .remove("thing");
    let operation = serde_json::json!({"operationId":"closeThing","tags":["alpha"],"parameters":[{"name":"id","in":"path","required":true,"schema":{"type":"string"}}],"responses":{"204":{"description":"OK"}}});
    document["paths"]["/a/{id}"] = serde_json::json!({"put":operation.clone()});
    document["paths"]["/b/{id}"] = serde_json::json!({"put":operation});
    document["paths"]["/b/{id}"]["put"]["tags"] = serde_json::json!(["beta"]);
    assert_measured_name_refusal(
        &document,
        "type-name-collision",
        "request type CloseThingRequest",
    );
    document["paths"]["/b/{id}"]["put"]["operationId"] = serde_json::json!("closeOtherThing");
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("sdk"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn inline_request_names_are_checked_against_the_emitted_naming_contract() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let mut document = serde_json::json!({
        "openapi":"3.0.3","info":{"title":"probe","version":"1"},
        "paths":{"/things":{"post":{"operationId":"createThing","tags":["alpha"],"requestBody":{"content":{"application/json":{"schema":{"type":"object","properties":{"color":{"type":"string","enum":["red","blue"]}}}}}},"responses":{"204":{"description":"OK"}}}}},
        "components":{"schemas":{}}
    });
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    let sdk = dir.path().join("sdk");
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&sdk)
        .assert()
        .success();
    let types = sdk.join("src/probe/alpha/types");
    let emitted = std::fs::read_dir(types)
        .unwrap()
        .map(|entry| entry.unwrap().path())
        .find(|path| std::fs::read_to_string(path).is_ok_and(|text| text.contains(" = \"red\"")))
        .unwrap();
    let text = std::fs::read_to_string(emitted).unwrap();
    let name = text
        .lines()
        .find_map(|line| {
            line.strip_prefix("class ")
                .and_then(|name| name.split_once('('))
                .map(|(name, _)| name)
        })
        .unwrap();
    let request_name = name.strip_suffix("Color").unwrap();
    document["components"]["schemas"][request_name] =
        serde_json::json!({"type":"object","properties":{"id":{"type":"string"}}});
    assert_measured_name_refusal(
        &document,
        "type-name-collision",
        &format!("request type {request_name}"),
    );
    document["components"]["schemas"]
        .as_object_mut()
        .unwrap()
        .clear();
    document["components"]["schemas"][name] =
        serde_json::json!({"type":"string","enum":["other","value"]});
    assert_measured_name_refusal(
        &document,
        "type-name-collision",
        &format!("enum {name} in namespace alpha"),
    );
    document["components"]["schemas"]
        .as_object_mut()
        .unwrap()
        .clear();
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn dropped_body_enum_names_refuse_and_distinct_component_names_recover() {
    let mut document = serde_json::json!({
        "openapi":"3.0.3","info":{"title":"probe","version":"1"},
        "paths":{"/things":{"post":{"operationId":"createThing","tags":["alpha"],"requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Thing"}}}},"responses":{"204":{"description":"OK"}}}}},
        "components":{"schemas":{"Thing":{"type":"object","properties":{"color":{"type":"string","enum":["red","blue"]}}},"ThingColor":{"type":"string","enum":["other","value"]}}}
    });
    assert_measured_name_refusal(
        &document,
        "type-name-collision",
        "body property \"color\" declares enum ThingColor",
    );
    document["components"]["schemas"]
        .as_object_mut()
        .unwrap()
        .remove("ThingColor");
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn unavailable_relative_type_aliases_refuse_and_available_files_recover() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    let document = serde_json::json!({
        "openapi":"3.0.3","info":{"title":"probe","version":"1"},"paths":{},
        "components":{"schemas":{"Thing":{"$ref":"common.json"}}}
    });
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    for strict in [false, true] {
        let output = dir.path().join(format!("bad-{strict}"));
        let mut command = crozier_clean_env();
        command
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&output);
        if strict {
            command.arg("--fern-strict");
        }
        let result = command.output().unwrap();
        let stderr = String::from_utf8(result.stderr).unwrap();
        assert_eq!(result.status.code(), Some(1), "{stderr}");
        assert!(stderr.contains("type-name-not-letter-led"), "{stderr}");
        assert!(stderr.contains("#/components/schemas/Thing"), "{stderr}");
        assert_eq!(stderr.contains("fern-strict"), strict);
        assert!(!output.exists());
    }
    std::fs::write(
        dir.path().join("common.json"),
        r#"{"type":"object","properties":{"id":{"type":"string"}}}"#,
    )
    .unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

#[test]
fn webhook_local_object_names_refuse_and_component_names_recover() {
    let mut document = serde_json::json!({
        "openapi":"3.1.0","info":{"title":"probe","version":"1"},"paths":{},
        "webhooks":{"event":{"post":{"requestBody":{"content":{"application/json":{"schema":{
            "type":"object","properties":{"payload":{"$ref":"#/webhooks/event/post/requestBody/content/application~1json/schema/definitions/Payload"}},
            "definitions":{"Payload":{"type":"object","properties":{"id":{"type":"string"}}}}
        }}}},"responses":{"204":{"description":"OK"}}}}}
    });
    assert_measured_name_refusal(&document, "type-name-not-letter-led", "webhook event");
    document["components"] = serde_json::json!({"schemas":{"Payload":{"type":"object","properties":{"id":{"type":"string"}}}}});
    document["webhooks"]["event"]["post"]["requestBody"]["content"]["application/json"]["schema"]
        ["properties"]["payload"]["$ref"] = serde_json::json!("#/components/schemas/Payload");
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, serde_json::to_string(&document).unwrap()).unwrap();
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(dir.path().join("recovered"))
        .arg("--fern-strict")
        .assert()
        .success();
}

/// A tag or SDK-group enum named like a root schema: pinned Fern refuses a
/// query parameter's as already declared, and checks and generates a header
/// parameter's whatever its values
/// (type-name-collision/evidence/namespaced-*.pinned-fern.log).
#[test]
fn namespaced_enum_collisions_follow_the_parameter_location() {
    let evidence = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(FERN_REFUSALS_DIR)
        .join("type-name-collision/evidence");
    for case in [
        "namespaced-query-enum-same",
        "namespaced-query-enum-diff",
        "namespaced-query-enum-same-tag",
        "namespaced-query-enum-diff-tag",
    ] {
        for strict in [false, true] {
            let run = refusal_run(&crozier, &evidence.join(format!("{case}.yml")), strict).unwrap();
            let failures = refused_failures(
                "type-name-collision",
                &run,
                "collides with a schema declaration",
                strict,
            );
            assert!(failures.is_empty(), "{case}: {}", failures.join("\n"));
        }
    }
    for case in [
        "namespaced-header-enum-same",
        "namespaced-header-enum-diff",
        "namespaced-header-enum-diff-tag",
    ] {
        assert_generates_in_both_modes(&evidence.join(format!("{case}.yml")), case);
    }
}

#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_body_query_collision_keeps_both_callers_values() {
    let source = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures/corpus-sources/waylay-queries/openapi.yaml");
    let script = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("docs/departures/evidence/body-query-parameter-value.py");
    let directory = tempfile::tempdir().expect("collision SDKs");
    for version in ["3.0.3", "3.1.0"] {
        let spec = directory.path().join(format!("{version}.yaml"));
        let sdk = directory.path().join(version);
        std::fs::write(
            &spec,
            std::fs::read_to_string(&source).unwrap().replacen(
                "openapi: 3.1.0",
                &format!("openapi: {version}"),
                1,
            ),
        )
        .unwrap();
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&sdk)
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
            ])
            .assert()
            .success();
        let python = runtime_python_env().expect("SDK runtime environment");
        let run = std::process::Command::new(python)
            .arg(&script)
            .arg(sdk.join("src"))
            .arg("body-value")
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .unwrap();
        assert!(
            run.status.success(),
            "{version}: {}{}",
            String::from_utf8_lossy(&run.stdout),
            String::from_utf8_lossy(&run.stderr)
        );
    }
}
