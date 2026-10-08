#!/usr/bin/env bash
# The real-world corpus byte-match: validate the committed corpus sources, then
# byte-compare crozier's output for every vendored Fern golden and require every
# registered source to generate. `--strict` runs it with strict Fern
# compatibility on (docs/fern-refusals/), so a refusal class that refuses a
# document Fern generates from fails it.
#
# The `corpus-match` project's `test-match` and `test-strict` targets run this
# (`just test-corpus-match`, `just test-corpus-match-strict`); CI runs both in
# its live-e2e leg. `CROZIER_REQUIRE_CORPUS` turns a missing committed source
# from a skip into a hard failure so the leg cannot no-op. One `cargo test`
# invocation per corpus keeps a source problem attributable to its API rather
# than hidden in a shared filter. The list below is held to the registered
# corpora in both directions by crates/crozier-e2e/tests/e2e.rs's
# `every_registered_corpus_is_wired_into_the_gate`: a registered corpus whose
# test is missing here fails it, and so does a line naming a test no registered
# corpus owns, so a renamed test cannot drop a corpus silently.
set -euo pipefail
cd "$(dirname "$0")/../.." || {
  echo "corpus-match: cannot enter the checkout above $0 — run it by its path from a readable checkout, then re-run" >&2
  exit 1
}

[ "$#" -le 1 ] || { echo "corpus-match: takes at most one argument, got $# — usage: tests/corpus_match/match.sh [--strict]" >&2; exit 2; }
case "${1:-}" in
  "") ;;
  --strict)
    # Every corpus run reads `CROZIER_FERN_STRICT`, because none passes
    # `--no-config`; this proves crozier sees it from here before relying on it.
    export CROZIER_FERN_STRICT=true
    cargo run --locked --quiet -- config python | grep -Eq '^  fern-strict +true +\(env\)$' || {
      echo "corpus-match --strict: crozier config did not report fern-strict true from CROZIER_FERN_STRICT; check that no crozier.yml or CROZIER_CONFIG overrides it here" >&2
      exit 1
    }
    ;;
  *)
    echo "corpus-match: unknown argument '$1' — usage: tests/corpus_match/match.sh [--strict]" >&2
    exit 2
    ;;
esac

cargo build --locked --quiet -p crozier --bin crozier
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e query_parameters_matches_fern_output_byte_for_byte
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e exhaustive_matches_fern_output_byte_for_byte
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e crozier_sdk_extensions_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e crozier_property_name_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e auth_schemes_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e inline_request_response_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e cookie_parameters_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e form_bodies_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e discriminated_unions_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e schema_constraints_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e integer_enums_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e servers_webhooks_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e basic_auth_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e oauth_client_credentials_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e inline_array_request_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e writeonly_fields_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e digit_leading_property_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e operation_id_non_identifier_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e bracketed_property_names_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e missing_operation_id_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e error_responses_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e tag_based_grouping_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e enum_query_param_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e audience_filter_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e audience_filter_strict_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sse_streaming_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e enum_name_sanitization_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e enum_receiver_collision_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e client_class_name_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e pydantic_extra_fields_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e recursive_types_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e nested_core_imports_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e malformed_property_schema_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e exhaustive_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e client_class_name_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e audience_filter_strict_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e exhaustive_package_name_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e overlay_goldens_match_fern_output
python3 tools/corpus/corpus_sources.py check
sh scripts/census-python.sh tests/corpus_match/corpus_surface_census_test.py
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_crm_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e bunq_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e bungie_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e appwrite_server_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e anchore_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apache_airflow_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apicurio_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e discourse_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e gambitcomm_mimic_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e dnd5eapi_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apache_qakka_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e authentiqio_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e etsi_mec010_2_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_webhook_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_vault_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e airbyte_config_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e bintable_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apis_guru_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e color_pizza_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e amazonaws_com_cloudformation_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e byautomata_io_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_proxy_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_connector_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_ecommerce_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_issue_tracking_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e appwrite_client_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_file_storage_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_hris_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_accounting_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e calorieninjas_reproduces_the_exact_known_fern_failure_boundary
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e eos_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_sms_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_ecosystem_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_customer_support_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_lead_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apache_org_airflow_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openfigi_com_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e twilio_voice_v1_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e microcks_local_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e redhat_catalog_inventory_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e xero_payroll_au_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e traccar_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e reverb_com_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e maif_otoroshi_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e portfoliooptimizer_io_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openbanking_org_uk_account_info_openapi_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e netbox_dev_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e squareup_com_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e redocly_com_museum_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e http_toolkit_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e frankfurter_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e worldcoin_signup_sequencer_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e electric_sql_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e tamoss_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e slurmdb_rest_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e nimisampo_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e free5gc_pdu_session_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sigstore_rekor_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e letta_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e free5gc_namf_communication_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_ats_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e buildrelay_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e tlon_notes_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e twilio_messaging_v1_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e livepeer_ai_runner_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e eos_extra_fields_forbid_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e eos_extra_fields_forbid_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e med_anvisa_price_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sac_backend_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e kytos_sdntrace_cp_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e withsecure_gdpr_subject_rights_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e prometheus_x_edge_computing_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e exa_gate_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e amazonaws_com_cloudfront_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e khoainats_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e helios_verifiable_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e eozilla_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openepcis_dpp_ready_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ndw_accessibility_map_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e marimo_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e blackadi_oauth2_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e mosip_esignet_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openbankingproject_ch_kundenbeziehung_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e cyberark_conjur_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e adyen_report_notification_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e adyen_managed_risk_notification_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e go_kratos_casbin_admin_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e descope_authzcache_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e swagger_petstore_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e swagger_petstore_organization_flat_matches_fern
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e cyclonedx_transparency_exchange_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e adyen_capital_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apivideo_android_uploader_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e truefoundry_trueforge_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e volview_backend_contract_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e osparc_simcore_webserver_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e helixdb_http_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e flowdapt_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e k8s_container_service_provider_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e daniweb_connect_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e chaingateway_io_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e hubspot_events_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paloalto_remote_networks_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openintegrationhub_secret_service_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e strapi_rest_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e listennotes_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e vtex_pricing_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e aws_importexport_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openbanking_brasil_directory_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e api_openverse_org_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e discord_com_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e braintrust_dev_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e agco_ats_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e torrentarr_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e svix_webhooks_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e komga_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e short_io_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e webflow_v2_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e loris_dataquery_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sftpgo_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e googleapis_servicebroker_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e audiobookshelf_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e steaminputdb_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paypal_catalog_products_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e folio_mod_authtoken_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e raybot_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openlinksw_osdb_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ziptax_node_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e nexmo_messages_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e deepsearch_ds_v2_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e mindee_ocr_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e opencodeui_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paloalto_cspm_alerts_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paloalto_cspm_reports_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paloalto_cspm_search_manager_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e thrivecart_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e truefoundry_trueforge_5adde28_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e fergus_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e groupe_psa_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e timelyapp_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e nextgen_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e auto_agent_protocol_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e skool_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e spendesk_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e billie_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e alma_france_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e outreach_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e tally_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e billie_entry_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e skool_entry_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e timelyapp_entry_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e cradl_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e zulip_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e zulip_jentic_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e zulip_jentic_entry_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e milvus_restful_v2_3_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e milvus_restful_v2_4_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ramu_shogi_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e langchain_agent_protocol_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e hse_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e milvus_vector_operations_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e mistle_control_plane_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e osparc_payments_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e huatuo_node_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e huatuo_server_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e viskit_studio_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e embedpdf_cloudpdf_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e npq_registration_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sim_logs_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e sim_tables_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e vellum_gateway_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e dot_ai_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e paloalto_code_technologies_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e marimo_plugins_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e otoroshi_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e standrig_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e mockserver_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ideaconsult_enanomapper_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openaire_graph_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e qredence_fleet_rlm_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e fiware_context_generator_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e hasura_metadata_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e zoonk_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e openfoodfacts_taxonomy_editor_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e qontract_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e typescript_service_template_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e oal_example_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e millenium_falcon_challenge_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e maximo_wxo_integration_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e mi_music_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e g4brym_download_manager_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e opentosca_license_engine_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e chat_rest_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e esp32_streamline_bridge_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e cphos_ai_question_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e flask_example_heroku_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e oip_web_api_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e waylay_queries_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e breizhsport_catalogue_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e protoform_conformance_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ere_ps_app_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e apideck_ecosystem_client_class_name_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e yourbrand_ticketing_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e peopledatalabs_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e adyen_acs_notification_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e googleapis_monitoring_v1_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e docu_goapiserver_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e onevoice_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e xfsc_oidc_identity_resolver_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e huatuo_node_tree_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e lootlog_battlelog_matches_fern_output
CROZIER_REQUIRE_CORPUS=1 cargo test --locked -p crozier-e2e --test e2e ego_microservices_matches_fern_output
