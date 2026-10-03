# Canonical command surface for crozier. Keep this list small and memorable.
# `just bootstrap` must work from a clean clone; `just check` is the full gate
# and must fail on any issue (no warnings-only mode).

set positional-arguments := true

# List available recipes.
default:
    @just --list

# Set up from a clean clone: toolchain (from rust-toolchain.toml), deps, dev tools.
bootstrap:
    @rustup show active-toolchain >/dev/null 2>&1 || rustup toolchain install
    @rustup component add rustfmt clippy llvm-tools-preview >/dev/null 2>&1 || true
    cargo fetch --locked
    @./scripts/install-dev-tools.sh
    @./scripts/install-ruff.sh
    @git config core.hooksPath .githooks
    @echo "enabled .githooks (visual-regression pre-push guard)"

# Full quality gate. Fails on any issue. e2e is part of the gate, not opt-in.
check: test-witness-search-redo test-witness-search-acquisition test-witness-search-github test-rate-limit-guard test-fern-refusals fmt-check lint test test-e2e test-fern-goldens test-fixtures-coverage test-surface-census test-llmlint-plugins test-llmlint-diff lint-corpus-licensing test-corpus-licensing lint-corpus-remote-ref-pins test-corpus-remote-ref-pins lint-corpus-sources test-corpus-sources lint-licence-rescreening test-licence-rescreening supply-chain doc
    @echo "check: ok"

# Format check (does not modify files).
fmt-check:
    cargo fmt --all -- --check

# Lint; warnings are errors.
lint:
    cargo clippy --all-targets --all-features --locked -- -D warnings

# Fast tests (unit + integration, excluding the e2e binary target) with coverage
# enforced. 95% line coverage is the gate; lower it only with a reason in AGENTS.md.
test:
    cargo llvm-cov --locked --fail-under-lines 95 \
        --ignore-filename-regex 'main\.rs$' \
        nextest -E 'not binary(e2e)'

# End-to-end: drive the compiled binary the way a user runs it (assert_cmd),
# byte-comparing its stripped output to the committed Fern fixtures. Also run by
# `check`; this recipe runs the journeys in isolation.
test-e2e:
    cargo nextest run --locked -E 'binary(e2e)'

# SDK Python-environment tier: the e2e journeys (`sdk_env_*`, `#[ignore]`d so the
# offline `test-e2e`/`check` never runs them) that build a virtualenv from PyPI
# for a generated SDK and run mypy or pytest in it — the runtime wire suite, the
# SDK's own-pin type-check, the shared env's concurrent first build, and the
# fern-refusals gate's `wire_test.py` condition. SEPARATE from `check` because it
# needs network and Python; CI runs it in the `sdk-env` job, which `gate`
# requires. Needs Python (uv used when present).
test-sdk-env:
    cargo nextest run --locked --run-ignored only -E 'binary(e2e) and test(/^sdk_env_/)'

# Runtime ("wire") test only: record the compiled client's behavior via an
# injected httpx.MockTransport (the pytest suite in tests/runtime/) and assert it
# matches the real Fern fixture SDK's behavior, modulo the normalized SDK-identity
# headers. Part of `test-sdk-env`; this runs it in isolation. Needs Python +
# httpx/pydantic/pytest (uv or pip); see tests/runtime/AGENTS.md.
test-runtime:
    cargo nextest run --locked --run-ignored only -E 'binary(e2e) and test(sdk_env_crozier_matches_fern_runtime_behavior)'

# Live e2e: boot a Prism OpenAPI mock server from each fixture's spec and drive the
# generated SDK through every documented endpoint, asserting a value of the method's
# declared return type comes back over real HTTP. Spec-driven (the endpoints and
# example args come from the SDK's generated reference.md), so it grows to more
# fixtures via conftest.FIXTURES. SEPARATE from `check` to keep the core gate
# Node-free; CI runs it as its own required leg. Needs Node/Prism + uv + ruff; see
# tests/live_e2e/AGENTS.md.
test-live-e2e *args:
    ./scripts/live-e2e.sh {{args}}

# Enforce the real-world corpus byte-match: validate the committed corpus sources and byte-compare crozier's output for the
# vendored Fern goldens and require every registered source to generate.
# CI also runs it in the live-e2e leg. `CROZIER_REQUIRE_CORPUS` turns a
# missing committed source from a skip into a hard failure so the leg cannot no-op.
# One `cargo test` invocation per corpus keeps a source problem attributable to
# its API rather than hidden in a shared filter. The list below is held to the
# registered corpora in both directions by `tests/e2e.rs`'s
# `every_registered_corpus_is_wired_into_the_gate` (part of `check`): a registered
# corpus whose test is missing here fails it, and so does a line naming a test no
# registered corpus owns, so a renamed test cannot drop a corpus silently.
test-corpus-match:
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e query_parameters_matches_fern_output_byte_for_byte
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e exhaustive_matches_fern_output_byte_for_byte
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e crozier_sdk_extensions_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e auth_schemes_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e inline_request_response_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e cookie_parameters_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e form_bodies_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e discriminated_unions_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e schema_constraints_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e integer_enums_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e servers_webhooks_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e basic_auth_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e oauth_client_credentials_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e inline_array_request_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e writeonly_fields_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e digit_leading_property_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e operation_id_non_identifier_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bracketed_property_names_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e missing_operation_id_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e error_responses_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e tag_based_grouping_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e enum_query_param_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e audience_filter_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e audience_filter_strict_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sse_streaming_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e enum_name_sanitization_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e enum_receiver_collision_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e client_class_name_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e pydantic_extra_fields_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e recursive_types_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e nested_core_imports_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e malformed_property_schema_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e exhaustive_flat_matches_fern
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e client_class_name_flat_matches_fern
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e audience_filter_strict_flat_matches_fern
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e exhaustive_package_name_flat_matches_fern
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e overlay_goldens_match_fern_output
    python3 scripts/corpus_sources.py check
    "$(./scripts/census-python.sh)" tests/corpus_surface_census_test.py
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_crm_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bunq_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bungie_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e appwrite_server_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e anchore_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_airflow_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apicurio_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e discourse_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e gambitcomm_mimic_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e dnd5eapi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_qakka_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e authentiqio_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e etsi_mec010_2_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_webhook_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_vault_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e airbyte_config_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bintable_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apis_guru_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e color_pizza_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e amazonaws_com_cloudformation_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e byautomata_io_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_proxy_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_connector_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ecommerce_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_issue_tracking_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e appwrite_client_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_file_storage_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_hris_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_accounting_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e calorieninjas_reproduces_the_exact_known_fern_failure_boundary
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e eos_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_sms_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ecosystem_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_customer_support_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_lead_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_org_airflow_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openfigi_com_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e twilio_voice_v1_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e microcks_local_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e redhat_catalog_inventory_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e xero_payroll_au_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e traccar_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e reverb_com_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e maif_otoroshi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e portfoliooptimizer_io_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openbanking_org_uk_account_info_openapi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e netbox_dev_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e squareup_com_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e redocly_com_museum_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e http_toolkit_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e frankfurter_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e worldcoin_signup_sequencer_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e electric_sql_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e tamoss_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e slurmdb_rest_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e nimisampo_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e free5gc_pdu_session_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sigstore_rekor_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e letta_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e free5gc_namf_communication_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ats_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e buildrelay_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e tlon_notes_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e twilio_messaging_v1_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e livepeer_ai_runner_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e eos_extra_fields_forbid_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e eos_extra_fields_forbid_flat_matches_fern
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e med_anvisa_price_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sac_backend_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e kytos_sdntrace_cp_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e withsecure_gdpr_subject_rights_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e prometheus_x_edge_computing_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e exa_gate_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e amazonaws_com_cloudfront_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e khoainats_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e helios_verifiable_api_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e eozilla_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openepcis_dpp_ready_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e ndw_accessibility_map_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e marimo_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e blackadi_oauth2_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e mosip_esignet_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openbankingproject_ch_kundenbeziehung_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e cyberark_conjur_api_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e adyen_report_notification_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e adyen_managed_risk_notification_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e go_kratos_casbin_admin_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e descope_authzcache_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e swagger_petstore_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e cyclonedx_transparency_exchange_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e adyen_capital_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apivideo_android_uploader_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e truefoundry_trueforge_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e volview_backend_contract_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e osparc_simcore_webserver_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e helixdb_http_api_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e flowdapt_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e k8s_container_service_provider_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e daniweb_connect_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e chaingateway_io_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e hubspot_events_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paloalto_remote_networks_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openintegrationhub_secret_service_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e strapi_rest_api_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e listennotes_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e vtex_pricing_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e aws_importexport_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openbanking_brasil_directory_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e api_openverse_org_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e discord_com_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e braintrust_dev_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e agco_ats_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e torrentarr_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e svix_webhooks_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e komga_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e short_io_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e webflow_v2_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e loris_dataquery_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sftpgo_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e googleapis_servicebroker_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e audiobookshelf_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e steaminputdb_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paypal_catalog_products_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e folio_mod_authtoken_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e raybot_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openlinksw_osdb_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e ziptax_node_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e nexmo_messages_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e deepsearch_ds_v2_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e mindee_ocr_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e opencodeui_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paloalto_cspm_alerts_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paloalto_cspm_reports_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paloalto_cspm_search_manager_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e thrivecart_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e truefoundry_trueforge_5adde28_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e fergus_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e groupe_psa_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e timelyapp_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e nextgen_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e auto_agent_protocol_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e skool_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e spendesk_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e billie_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e alma_france_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e outreach_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e tally_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e billie_entry_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e skool_entry_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e timelyapp_entry_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e cradl_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e zulip_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e zulip_jentic_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e zulip_jentic_entry_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e milvus_restful_v2_3_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e milvus_restful_v2_4_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e ramu_shogi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e langchain_agent_protocol_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e hse_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e milvus_vector_operations_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e mistle_control_plane_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e osparc_payments_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e huatuo_node_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e huatuo_server_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e viskit_studio_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e embedpdf_cloudpdf_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e npq_registration_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sim_logs_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e sim_tables_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e vellum_gateway_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e dot_ai_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e paloalto_code_technologies_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e marimo_plugins_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e otoroshi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e standrig_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e mockserver_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e ideaconsult_enanomapper_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e openaire_graph_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e qredence_fleet_rlm_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e fiware_context_generator_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e hasura_metadata_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e zoonk_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ecosystem_client_class_name_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e peopledatalabs_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e adyen_acs_notification_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e googleapis_monitoring_v1_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e docu_goapiserver_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e onevoice_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e xfsc_oidc_identity_resolver_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e huatuo_node_tree_matches_fern_output

# The corpus byte-match with strict Fern compatibility on (docs/fern-refusals/):
# a refusal class that refuses a document Fern generates from fails it. The
# setting travels by `CROZIER_FERN_STRICT`, which every corpus run reads because
# none passes `--no-config`; the first line proves crozier sees it from here.
test-corpus-match-strict:
    CROZIER_FERN_STRICT=true cargo run --locked --quiet -- config python | grep -Eq '^  fern-strict +true +\(env\)$' || { echo "test-corpus-match-strict: crozier config did not report fern-strict true from CROZIER_FERN_STRICT; check that no crozier.yml or CROZIER_CONFIG overrides it here" >&2; exit 1; }
    CROZIER_FERN_STRICT=true just test-corpus-match

# Format the codebase in place.
format:
    cargo fmt --all

# Supply-chain gate (Linux; run once, not across an OS matrix).
supply-chain:
    cargo deny --locked check
    cargo machete

# Docs must build cleanly (broken intra-doc links are errors).
doc:
    RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features --locked

# Upgrade dependencies, then re-run the full gate.
upgrade:
    cargo update
    @just check

# Legacy reproduction aid for the offline seed; pass `exhaustive` to reproduce
# that historical container-generated target too. Numbered corpus maintenance
# uses the Fern goldens workflow; see docs/fern-goldens.md.
fixtures-refresh *args:
    ./scripts/fixtures-refresh.sh {{args}}


# Rebuild-only: fetch pinned corpus sources into .local/corpus or a supplied
# destination. Routine checks use committed copies; this is Fern maintenance.
fetch-corpus *args:
    ./scripts/fetch-corpus.sh {{args}}


# Legacy local reproduction for issue #77 goldens. Routine generation and safe
# publication belong to the Fern goldens workflow. Needs Docker + fern.
fixtures-generate-corpus *args:
    ./scripts/generate-corpus-fixtures.sh {{args}}

# Local diagnostic for the workflow lifecycle: resolve an exact generator tag,
# generate every selected corpus independently, then aggregate all Crozier byte
# diffs. `--fixture NAME` may be repeated; omitting it selects existing goldens.
fern-goldens *args:
    ./scripts/fern-goldens run "$@"

# Phase recipes used by the workflow so successful goldens can be published
# before generation/diff failures determine the final status.
fern-goldens-generate *args:
    ./scripts/fern-goldens generate "$@"

fern-goldens-compare:
    ./scripts/fern-goldens compare

fern-goldens-publish branch:
    ./scripts/fern-goldens publish --branch "$1"

fern-goldens-result *args:
    ./scripts/fern-goldens result "$@"

# Process/filesystem/workflow-boundary coverage for the automation itself.
test-fern-goldens:
    python3 tests/fern_goldens_test.py

# Live Fern measurement for the witness-supply probe Fern refuses. Separate
# from `check`: Fern's pinned Python generator runs in Docker and needs network.
test-fern-probe-refusal:
    cargo test --test e2e fern_ref_pointer_unnamed_segment_refusal_matches_measurement -- --ignored --exact --nocapture

# Process/filesystem/test-selection-boundary coverage for `fixtures-coverage`.
# Drives the real recipe under a SCOPE so it measures a handful of tests instead
# of the whole corpus; the unmeasured thing would otherwise be the measurement.
# Part of `check` (the recipe itself is not — it needs network and is slow).
# The hand-written reach recipe is driven the same way, over temporary fixtures.
# The golden-reach suite runs twice: the second time without `fcntl` and the
# other POSIX-only modules, as on Windows, on every host.
test-fixtures-coverage:
    python3 tests/fixtures_coverage_test.py
    python3 tests/handwritten_reach_test.py
    python3 tests/golden_reach_test.py
    PYTHONPATH=tests/without-posix-modules python3 tests/golden_reach_test.py

# The arm search's YAML fallback against the census's stdlib loader: identical
# counts on every registered YAML source, and each refused form's committed sample
# (`tests/data/census-fallback-sample/`) read as what it declares. Fetches no
# specification; `test-corpus-offline` runs it with sockets denied.
test-census-fallback-samples:
    python3 scripts/corpus_sources.py check
    CROZIER_REQUIRE_CORPUS=1 uv run --no-project --with "$(sed -n 's/^# dependencies = \["\(.*\)"\]$/\1/p' scripts/golden-reach-search.py)" python3 tests/golden_reach_census_fallback_test.py

# The samples above, then the arm search and the witness-search re-census CLI
# over temporary ledgers, a loopback GitHub and Sourcegraph, and the same pinned
# parser. Outside `check` — it needs the pinned ruamel.yaml (read from each
# script's own inline metadata); CI's live-e2e leg runs it.
test-census-fallback: test-census-fallback-samples
    CROZIER_REQUIRE_CORPUS=1 uv run --no-project --with "$(sed -n 's/^# dependencies = \["\(.*\)"\]$/\1/p' scripts/golden-reach-search.py)" python3 tests/golden_reach_test.py
    uv run --no-project --with "$(sed -n 's/^# dependencies = \["\(.*\)"\]$/\1/p' scripts/witness-search-recensus.py)" python3 tests/witness_search_recensus_test.py

# Census aid: report the exact expected files crozier still does not reproduce.
# The output is the ready-to-paste `unmatched` task list. Not part of `check`.
# The grep is a drift gate: `cargo test <name>` exits 0 even when the exact-name
# filter matches nothing, so if `report_fixture_gaps` is renamed/removed in
# tests/e2e.rs this recipe would silently no-op — asserting the report's summary
# line turns that into a hard failure instead.
fixtures-gaps corpus="":
    #!/usr/bin/env bash
    set -uo pipefail
    out=$(mktemp "${TMPDIR:-/tmp}/crozier-fixtures-gaps.XXXXXX")
    trap 'rm -f "$out"' EXIT
    status=0
    CROZIER_GAPS_CORPUS="{{corpus}}" \
      cargo test --locked --test e2e -- --ignored --nocapture report_fixture_gaps \
      >"$out" 2>&1 || status=$?
    if [ "$status" -eq 0 ] && grep -q 'file(s) still unmatched across all corpora' "$out"; then
      # Quiet on success: print only the report the user asked for, not cargo's
      # build/test scaffolding — from the first corpus header through the summary.
      awk '/^=== /{p=1} p; /file\(s\) still unmatched across all corpora/{p=0}' "$out"
    else
      # Drift (test renamed → 0 tests run) or a failed self-check: surface it all.
      cat "$out" >&2
      echo "fixtures-gaps: no report from report_fixture_gaps — renamed/removed in tests/e2e.rs, or its self-check failed" >&2
      exit 1
    fi

# Backward-compatible alias for the former reporter name.
fixtures-candidates corpus="":
    just fixtures-gaps "{{corpus}}"

# Mismatch-investigation aid: print the
# normalized unified diff of every committed fixture file crozier does NOT
# reproduce byte-for-byte — exactly the bytes the gate compares (`-` = Fern
# golden, `+` = crozier; comments, SDK headers, and __init__ import order already
# normalized out), so what you see is what to fix. Optional args narrow scope:
# `just fixtures-diff <corpus> <file-substring>`. Not part of `check`. Run it to
# see WHY a file doesn't match; see tests/fixtures/AGENTS.md. Same drift guard as
# `fixtures-gaps`: assert the report's summary line so a renamed
# `report_fixture_diffs` fails loudly instead of silently no-op'ing.
fixtures-diff corpus="" file="":
    #!/usr/bin/env bash
    set -uo pipefail
    out=$(mktemp "${TMPDIR:-/tmp}/crozier-fixtures-diff.XXXXXX")
    trap 'rm -f "$out"' EXIT
    status=0
    CROZIER_DIFF_CORPUS="{{corpus}}" CROZIER_DIFF_FILE="{{file}}" \
      cargo test --locked --test e2e -- --ignored --nocapture report_fixture_diffs \
      >"$out" 2>&1 || status=$?
    if [ "$status" -eq 0 ] && grep -q 'differing file(s) across the reported corpora' "$out"; then
      # Quiet on success: print only the report (corpus headers, diffs, summary),
      # not cargo's build/test scaffolding.
      awk '/^=== /{p=1} p; /differing file\(s\) across the reported corpora/{p=0}' "$out"
    else
      # Drift (test renamed → 0 tests run) or a bad-corpus/broken-walk assertion.
      cat "$out" >&2
      echo "fixtures-diff: no report from report_fixture_diffs — renamed/removed in tests/e2e.rs, or the corpus filter matched nothing" >&2
      exit 1
    fi

# Measure what the committed Fern GOLDENS reach in src/, apart from what
# crozier's own tests reach — the number that answers "which fixture next?".
# Outside `check`: needs network and runs the whole corpus instrumented. Takes an
# optional cargo-nextest filter expression to scope it. Reading the split:
# tests/fixtures/AGENTS.md.
fixtures-coverage *args:
    ./scripts/fixtures-coverage.sh "$@"

# Per `golden` census row: which of crozier's declared handling sites for it
# (docs/openapi-surface/golden-reach-sites.tsv) the row's own witnesses execute
# in the golden-only tier, one instrumented run per golden test. Writes the
# ranked ledger (docs/openapi-surface/golden-reach.tsv) and every golden row's
# reach cell. Outside `check`: runs the corpus instrumented.
golden-reach:
    python3 scripts/corpus_sources.py check
    python3 scripts/golden-reach.py measure
    "$(./scripts/census-python.sh)" ./scripts/openapi-surface-census.py --json > .local/golden-reach/census.json
    python3 scripts/golden-reach.py report --write

# Re-join the last `just golden-reach` measurement after the site table changes.
golden-reach-report:
    python3 scripts/golden-reach.py report --write

# Per arm-level cover of a hand-written fixture (docs/openapi-surface/handwritten/AGENTS.md):
# how many regions of its arm an instrumented crozier run over that fixture's
# openapi.yml alone executes, one run per fixture as `golden-reach` scopes one
# golden test. Writes docs/openapi-surface/handwritten-reach.tsv, and for a
# fixture declaring a setting, its arms with and without it into
# handwritten-config-gates.tsv. Outside `check`, like `golden-reach`: it builds
# and runs crozier instrumented. `--handwritten-dir DIR --ledger PATH --gates
# PATH` measure another tree into other files.
handwritten-reach *args:
    python3 scripts/handwritten-fixtures.py measure "$@"

# Census which OpenAPI shapes the registered golden sources DECLARE — the input
# to docs/openapi-surface-coverage.md, and the only measurement of what the
# corpus has never seen. Walks each source document's object model (never its
# generated expected/ tree, never a text match) and prints one row per
# (selector, fixture, count). Reads the committed source copies. The script's own flags pass straight through, e.g.
# `just surface-census --selector pathItem.trace --json`.
surface-census *args:
    "$(./scripts/census-python.sh)" ./scripts/openapi-surface-census.py "$@"

# Boundary coverage for `surface-census`: drives the REAL script over the REAL
# vendored source documents, offline, so the gate keeps the instrument honest
# without the network the unscoped recipe needs. Part of `check` (the recipe
# above is not). Same split as test-fixtures-coverage vs fixtures-coverage.
test-surface-census:
    "$(./scripts/census-python.sh)" tests/surface_census_test.py
    "$(./scripts/census-python.sh)" tests/apis_guru_gap_screen_test.py

# Screen every APIs.guru catalogue version for the owned surface-gap selectors.
apis-guru-gap-screen *args:
    "$(./scripts/census-python.sh)" ./scripts/apis-guru-gap-screen.py {{args}}

# The corpus's admissible-licence rule is stated in ONE file,
# docs/corpus-licensing.md. This fails when any other tracked Markdown document
# enumerates the admissible licences again — the drift that left a dozen copies
# of the old set and no source. Prose that REFERS to the rule is fine; a second
# list of licence names is not. Part of `check`.
lint-corpus-licensing:
    python3 scripts/corpus-licensing-drift.py

# Boundary coverage for that gate: drives the REAL script over the REAL tree,
# and over the real tree with a second enumeration planted in it, so a check
# that had stopped discriminating fails here instead of passing silently.
# Part of `check`.
test-corpus-licensing:
    python3 tests/corpus_licensing_test.py

# A corpus row whose document names another document by absolute URL is only
# reproducible if that URL is immutable. tests/fixtures/corpus-remote-ref-pins.tsv
# records the substitutions that make it so; this is the offline gate over the
# manifest itself — well-formed records, real corpus names, immutable pinned URLs,
# no duplicates, sorted. No network. Part of `check`.
lint-corpus-remote-ref-pins:
    python3 scripts/corpus_remote_ref_pins.py check

# Boundary coverage for the pin MECHANISM, which the manifest cannot prove: drives
# the REAL scripts/fetch-corpus.sh against a loopback HTTP server the suite starts
# itself, so real curl and the real filesystem publish a real document. Also holds
# the offline lint's malformed-manifest cases. No test reaches GitHub, so `check`
# takes a loopback socket and no external host. Part of `check`.
test-corpus-remote-ref-pins:
    python3 tests/corpus_remote_ref_pins_test.py

# Every registered corpus row's source document is committed under
# tests/fixtures/corpus-sources/, recorded with the SHA-256 of the bytes fetched
# at its pinned revision in tests/fixtures/corpus-sources.tsv, so no gate fetches
# one. This is the offline gate over those copies: every row committed and
# recorded, every byte at its digest, every multi-document file present, no
# stray file. No network. Part of `check`.
lint-corpus-sources:
    python3 scripts/corpus_sources.py check

# Boundary coverage for that gate and for the rebuild tooling below: the real
# tree, a synthetic root broken one demand at a time, and `vendor`/`audit`
# through the real fetch against a loopback server. Part of `check`.
test-corpus-sources:
    python3 tests/corpus_sources_test.py

# Linux CI proof: run the real byte-match, census, refusal and census-fallback
# sample recipes with sockets denied and the ignored corpus caches absent. Does
# not fetch a specification (cargo fetches the locked crates and uv the pinned
# parser first).
test-corpus-offline:
    python3 tests/corpus_offline_test.py

# Rebuild-only: `vendor --fixture NAME` fetches a row from its pinned URL and
# commits its source (run it when a row is added or its pin moves); `audit`
# re-fetches and compares without writing. Needs network; never part of a gate.
corpus-sources *args:
    python3 scripts/corpus_sources.py "$@"

# The screening record for the widened admissible-licence rule,
# docs/licence-rescreening.md: one line per candidate the six region files
# record as blocked on a licence. This fails when a line omits its admission
# verdict, the reason behind it, the ref it was screened at, either half of the
# Fern screen, or names a coverage row no region file carries. Part of `check`.
lint-licence-rescreening:
    python3 scripts/licence-rescreening-check.py

# Boundary coverage for that gate: drives the REAL script over the REAL record,
# then over a record breaking each demand in turn, so a gate that had stopped
# discriminating fails here instead of passing silently. Part of `check`.
test-licence-rescreening:
    python3 tests/licence_rescreening_test.py

# The Fern refusal registry's population tables (docs/fern-refusals/) against
# the committed records they are built from: scripts/fern-refusals.py `check`
# over the real tree, `build` reproducing it, and drift cases that must fail.
test-fern-refusals:
    python3 tests/fern_refusals_test.py

# Measure the Fern refusal population (docs/fern-refusals/): fetch each document,
# run Fern and crozier over it. Rebuilds the release binary first, so crozier's
# counts come from the current tree. Network + Fern (`just setup-fern`).
fern-refusals-measure *args:
    cargo build --release --locked --bin crozier
    python3 scripts/fern-refusals.py measure {{args}}

# Install/refresh the llmlint toolchain (oneharness + llmlint). Idempotent.
setup-llmlint:
    ./scripts/setup-llmlint.sh

# Re-fetch every plugin `llmlint-plugins/lock.json` records, at its recorded
# `@pin`, and rewrite the vendored copies + the lock. This is the ONLY way an
# upstream rule change reaches the judged tier — it lands as a reviewable diff
# rather than on whatever the network answers mid-PR. Needs network + llmlint.
# See docs/llmlint-plugins.md.
# Refresh the vendored llmlint rule plugins and their lock.
llmlint-plugins-refresh:
    ./scripts/llmlint-plugins.py refresh

# Boundary coverage for that plugin set: drives the REAL llmlint over the REAL
# llmlint.yml with the plugin origin refused (a proxy at a closed port, a cold
# cache), so a job-time fetch reintroduced into the config fails here instead of
# failing a required PR check on a flaked connection. Part of `check`; skips
# where llmlint is absent unless CROZIER_REQUIRE_LLMLINT=1, which CI's llmlint
# job sets so the step cannot no-op.
# Prove the judged tier resolves its rules with the plugin origin unreachable.
test-llmlint-plugins:
    python3 tests/llmlint_plugins_test.py

# Set up local Fern-golden reproduction (Fern CLI, Docker daemon, release binary).
# Idempotent; also run by the SessionStart hook. The hosted workflow is the normal
# maintenance path. See docs/fern-goldens.md.
setup-fern:
    ./scripts/setup-fern.sh

# LLM-judge lint (llmlint) — non-deterministic, harness-backed; kept OUT of
# `check`. Run on demand over the configured set (or pass paths). See llmlint.yml.
lint-llm *paths:
    @command -v llmlint >/dev/null 2>&1 || { echo "llmlint not installed — run 'just setup-llmlint'"; exit 1; }
    llmlint {{paths}}


# Deterministic llmlint config/ignore/version-bump validation.
lint-llm-validate *args:
    PATH="$HOME/.local/bin:$PATH" llmlint validate {{args}}

# `--diff` lints only what this branch introduced against the merge base, and
# honors llmlint.yml's excludes. llmlint hands one rule batch every changed file,
# so scripts/llmlint-diff.py splits a diff too large for the judge into file
# batches it can hold, and runs the one plain invocation otherwise.
# Blocking `llmlint` PR check; run before pushing. BASE defaults to origin/main.
lint-llm-diff base="origin/main" *args:
    python3 scripts/llmlint-diff.py {{base}} {{args}}

# Offline tests of the batching wrapper, against a stub llmlint.
test-llmlint-diff:
    python3 tests/llmlint_diff_test.py

# --- Terminal screenshots (informational; never part of `check`) --------------
# Deterministic SVGs of the real CLI output, rendered by `freeze` from a vendored
# pinned font and gated/galleried/PR-commented by screencomp. Regenerating is out
# of the gate; CI's Visual-docs workflow owns the comparison, and the pre-push
# guard re-captures locally on drift. See screenshots/AGENTS.md.

# Install the screenshot renderer (`freeze`) on demand, pinned to `.freeze-version`
# (the single source of truth CI's Visual-docs capture reads too). Needs Go.
screenshots-tools:
    @command -v go >/dev/null || { echo "go not found: needed to install freeze; see https://go.dev/dl" >&2; exit 1; }
    go install github.com/charmbracelet/freeze@v"$(cat .freeze-version)"
    @echo "installed freeze to $(go env GOPATH)/bin (ensure it is on PATH)"

# Capture the screenshots: drive the real binary against screenshots/petstore.yml,
# render each scene to shots/current/<arch>/ + docs/screenshots/. Needs `freeze`
# and `ruff` on PATH (the latter is crozier's generation-time dependency).
screenshots:
    @bash scripts/screenshots.sh

# Regenerate the animated demo GIF (docs/screenshots/demo.gif — the README hero:
# a real `generate` run, then the generated enum streaming in). Drives the REAL
# release binary against the demo spec, then draws faithful frames with the
# vendored JetBrains Mono font (Pillow only — no ttyd/ffmpeg). Informational, NOT
# hash-gated (a GIF isn't byte-reproducible), so regenerate on demand and commit
# the result. Needs Python 3 + Pillow (`pip install Pillow`).
screenshots-gif:
    @command -v python3 >/dev/null || { echo "python3 not found: needed to render the demo GIF" >&2; exit 1; }
    @python3 -c "import PIL" 2>/dev/null || { echo "Pillow not installed: pip install Pillow" >&2; exit 1; }
    cargo build --release --locked --bin crozier
    python3 scripts/demo-gif.py

# Refresh the committed baseline manifest from a fresh capture (after an intended
# output change). Commit shots/baseline/*.json + docs/screenshots/ alongside.
screenshots-bless: screenshots
    @command -v screencomp >/dev/null || { echo "screencomp not installed: https://github.com/nickderobertis/screencomp#install" >&2; exit 1; }
    screencomp manifest --input shots/current --output shots/baseline/$(uname -m | sed 's/amd64/x86_64/;s/aarch64/arm64/').json
    @echo "baseline refreshed; commit shots/baseline/ + docs/screenshots/"

# Validate the witness ledger and its CLI against real temporary documents.
test-witness-search-redo:
    "$(./scripts/census-python.sh)" tests/witness_search_redo_test.py

# Drive witness-search acquisition, census and ledger derivation through the real CLIs.
test-witness-search-acquisition:
    "$(./scripts/census-python.sh)" tests/witness_search_acquisition_test.py

# Offline HTTP journey for the GitHub/Sourcegraph witness acquisition path.
test-witness-search-github:
    "$(./scripts/census-python.sh)" tests/witness_search_github_test.py

# Canonical reproduction entry point; archived evidence retains original commands.
witness-search-local-census *args:
    @"$(./scripts/census-python.sh)" ./scripts/witness-search-local-census.py "$@"

# Drives the real module against a local HTTP server serving authored responses.
# Offline tier for the GitHub/Postman/Sourcegraph rate-limit guard.
test-rate-limit-guard:
    "$(./scripts/census-python.sh)" tests/rate_limit_guard_test.py

# Needs network (and GITHUB_TOKEN for the token's own buckets); never waits, so
# it stays out of `check`. Rule and interface: scripts/rate_limit_guard.py.
# Live GitHub REST bucket figures from one free /rate_limit read, plus paced-host spacing.
quota-status:
    @"$(./scripts/census-python.sh)" scripts/rate_limit_guard.py status
