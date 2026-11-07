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
# from a skip into a hard failure so the leg cannot no-op. The inventory below
# runs as ONE `cargo nextest run` with an exact-name filter per test, so it
# selects no more and no fewer tests than it lists (a `cargo test <name>` filter
# matches by substring); nextest still runs each test in its own process, and
# `--no-fail-fast` names every failing golden in its summary, so a source
# problem stays attributable to its API. Before running, the selection is
# checked against `cargo nextest list` name for name; `CORPUS_MATCH_LIST=PATH`
# writes that checked selection to PATH and stops before the source check and
# the run.
#
# The inventory is held to the registered corpora in both directions by
# crates/crozier-e2e/tests/e2e.rs's `every_registered_corpus_is_wired_into_the_gate`:
# a registered corpus whose test is missing here fails it, and so does a line
# naming a test no registered corpus owns, so a renamed test cannot drop a corpus
# silently. A test inside a module is listed by its full nextest path.
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
    cargo run --locked --quiet -- config python | grep -E '^  fern-strict +true +\(env\)$' >/dev/null || {
      echo "corpus-match --strict: crozier config did not report fern-strict true from CROZIER_FERN_STRICT; check that no crozier.yml or CROZIER_CONFIG overrides it here" >&2
      exit 1
    }
    ;;
  *)
    echo "corpus-match: unknown argument '$1' — usage: tests/corpus_match/match.sh [--strict]" >&2
    exit 2
    ;;
esac

# Every build and corpus run below stops the stage on its own failure; this names
# which one, after cargo's own error.
trap 'status=$?; echo "corpus-match: \`$BASH_COMMAND\` exited $status — fix the build or corpus failure above (a first build fetches crates, so it needs network once), then re-run" >&2' ERR

cargo build --locked --quiet -p crozier --bin crozier

# At most this many goldens run at once. Each spawns crozier and then `ruff
# format`, so a test spends much of its time waiting on a subprocess; twice a
# 4-vCPU CI runner keeps it busy without letting memory grow with the host.
threads=8

inventory=(
  registered_literals_amrc_factoryplus_documentation_be5e3789_matches_fern_output
  registered_literals_apis_guru_openapi_directory_2f8c36b9_matches_fern_output
  registered_literals_apis_guru_openapi_directory_9031af6a_matches_fern_output
  registered_literals_apis_guru_openapi_directory_7edd79be_matches_fern_output
  registered_literals_apis_guru_openapi_directory_72fccf73_matches_fern_output
  registered_literals_apis_guru_openapi_directory_468bf5ef_matches_fern_output
  registered_literals_apis_guru_openapi_directory_cdcf7865_matches_fern_output
  registered_literals_apis_guru_openapi_directory_a0bd29a9_matches_fern_output
  registered_literals_cryptotyson_n8n_skyvern_117c4acb_matches_fern_output
  registered_literals_gravitlauncher_launcher_e883f698_matches_fern_output
  registered_literals_hardonian_reach_f36ad5db_matches_fern_output
  registered_literals_jhuapl_dtnma_dtnma_tools_de4dc81f_matches_fern_output
  registered_literals_observation_management_service_ewms_workflow_management_service_2b4dea85_matches_fern_output
  registered_literals_openapitools_openapi_generator_3d039741_matches_fern_output
  registered_literals_openapitools_openapi_generator_98d94419_matches_fern_output
  registered_literals_openapitools_openapi_generator_83482829_matches_fern_output
  registered_literals_openbanking_brasil_areadesenvolvedor_7fb4ca57_matches_fern_output
  registered_literals_seekstorm_seekstorm_b73096c4_matches_fern_output
  registered_literals_skyvern_ai_skyvern_7989ab3e_matches_fern_output
  registered_literals_skyvern_ai_skyvern_a61ee2be_matches_fern_output
  registered_literals_touk_nussknacker_895f3518_matches_fern_output
  registered_literals_trueblocks_trueblocks_core_2a176f14_matches_fern_output
  registered_literals_ballerina_platform_openapi_connectors_97a587f5_matches_fern_output
  registered_literals_bytedance_sandboxfusion_0b64b21d_matches_fern_output
  registered_literals_codosseum_org_backend_9fa232be_matches_fern_output
  registered_literals_confluentinc_schema_registry_sdk_go_aa65c204_matches_fern_output
  registered_literals_core_ncsrd_katana_7ddfc420_matches_fern_output
  registered_literals_craftgodotdev_craftgo_d6e4a55a_matches_fern_output
  registered_literals_darwin_studios_darwin_cli_ee5e2a21_matches_fern_output
  registered_literals_debezium_debezium_platform_043f3a5f_matches_fern_output
  registered_literals_fern_api_docs_5aa6dbf5_matches_fern_output
  registered_literals_fern_api_docs_74ff1c45_matches_fern_output
  registered_literals_geoserver_geoserver_b34cf587_matches_fern_output
  registered_literals_gleez_nats_http_gateway_e8767ae7_matches_fern_output
  registered_literals_halo_dev_halo_7e48a553_matches_fern_output
  registered_literals_halo_dev_halo_6e341cac_matches_fern_output
  registered_literals_hey_api_hey_api_30fbd0e5_matches_fern_output
  registered_literals_i_am_bee_agentstack_7d68b3f8_matches_fern_output
  registered_literals_ihulsbus_cookbook_0ac7df49_matches_fern_output
  registered_literals_jentic_jentic_public_apis_a96f8580_matches_fern_output
  registered_literals_koala73_worldmonitor_35041bfc_matches_fern_output
  registered_literals_konfig_dev_konfig_1115ef92_matches_fern_output
  registered_literals_konfig_dev_konfig_614a2b05_matches_fern_output
  registered_literals_konfig_sdks_openapi_examples_63042193_matches_fern_output
  registered_literals_landing_ai_ade_cli_d11fa644_matches_fern_output
  registered_literals_malach_it_boruta_server_26683af5_matches_fern_output
  registered_literals_marcelo_earth_generative_manim_8e1e6b29_matches_fern_output
  registered_literals_medizininformatik_initiative_dataportal_backend_4d419c8a_matches_fern_output
  registered_literals_msgbyte_tianji_1843a239_matches_fern_output
  registered_literals_neilthomas89440_crypto_inferna_next_24442375_matches_fern_output
  registered_literals_neo773_macgamingdb_2af442ce_matches_fern_output
  registered_literals_nextcloud_client_sdks_adbf3118_matches_fern_output
  registered_literals_opengeospatial_t17_api_d166_ffbd86a7_matches_fern_output
  registered_literals_openresponses_openresponses_ee8c96e1_matches_fern_output
  registered_literals_openresponses_openresponses_d598753c_matches_fern_output
  registered_literals_radio_aktywne_jasmine_bf07beed_matches_fern_output
  registered_literals_radio_aktywne_magnolia_f02e99f9_matches_fern_output
  registered_literals_rd_alliance_metadata_catalog_v2_c5da87bb_matches_fern_output
  registered_literals_resemble_ai_resemble_mcp_48c5814b_matches_fern_output
  registered_literals_stripe_sync_engine_7f4c6ed5_matches_fern_output
  registered_literals_stripe_sync_engine_0fb02347_matches_fern_output
  registered_literals_sumup_sumup_openapi_b1d4ab06_matches_fern_output
  registered_literals_teunmooij_payload_tools_ecbf9ccc_matches_fern_output
  registered_literals_teunmooij_payload_tools_7296685e_matches_fern_output
  registered_literals_tranphita_skyvern_0f3a701b_matches_fern_output
  registered_literals_truefoundry_trueforge_09fcb1c2_matches_fern_output
  registered_literals_truefoundry_trueforge_e259dee6_matches_fern_output
  registered_literals_webr0m_teldrive_nodejs_bb74a9e2_matches_fern_output
  registered_literals_whatwatt_ch_whatwatt_go_documentation_29ffa265_matches_fern_output
  registered_literals_whatwatt_ch_whatwatt_go_documentation_4cd56f72_matches_fern_output
  registered_literals_zalando_incubator_agentic_identity_broker_c7fb9242_matches_fern_output
  remeasured_grafikart_filemanager_element_e36a74ce_matches_fern_output
  remeasured_arawa_workspace_0c8259f6_matches_fern_output
  remeasured_clencyc_mozillafestivalbackend_b2264b38_matches_fern_output
  remeasured_hashicorp_terraform_plugin_codegen_openapi_1f6aea4c_matches_fern_output
  remeasured_membrane_api_gateway_8340f5da_matches_fern_output
  crozier_sdk_extensions_matches_fern_output
  crozier_property_name_matches_fern_output
  auth_schemes_matches_fern_output
  inline_request_response_matches_fern_output
  cookie_parameters_matches_fern_output
  form_bodies_matches_fern_output
  discriminated_unions_matches_fern_output
  schema_constraints_matches_fern_output
  integer_enums_matches_fern_output
  servers_webhooks_matches_fern_output
  basic_auth_matches_fern_output
  oauth_client_credentials_matches_fern_output
  inline_array_request_matches_fern_output
  writeonly_fields_matches_fern_output
  digit_leading_property_matches_fern_output
  operation_id_non_identifier_matches_fern_output
  bracketed_property_names_matches_fern_output
  missing_operation_id_matches_fern_output
  error_responses_matches_fern_output
  tag_based_grouping_matches_fern_output
  enum_query_param_matches_fern_output
  audience_filter_matches_fern_output
  audience_filter_strict_matches_fern_output
  sse_streaming_matches_fern_output
  enum_name_sanitization_matches_fern_output
  enum_receiver_collision_matches_fern_output
  client_class_name_matches_fern_output
  pydantic_extra_fields_matches_fern_output
  recursive_types_matches_fern_output
  nested_core_imports_matches_fern_output
  malformed_property_schema_matches_fern_output
  swagger_petstore_flat_matches_fern
  swagger_petstore_distribution_flat_matches_fern
  client_class_name_flat_matches_fern
  audience_filter_strict_flat_matches_fern
  overlay_goldens::overlay_goldens_match_fern_output
  apideck_crm_matches_fern_output
  bunq_matches_fern_output
  bungie_matches_fern_output
  appwrite_server_matches_fern_output
  anchore_matches_fern_output
  apache_airflow_matches_fern_output
  apicurio_matches_fern_output
  discourse_matches_fern_output
  gambitcomm_mimic_matches_fern_output
  dnd5eapi_matches_fern_output
  apache_qakka_matches_fern_output
  authentiqio_matches_fern_output
  etsi_mec010_2_matches_fern_output
  apideck_webhook_matches_fern_output
  apideck_vault_matches_fern_output
  airbyte_config_matches_fern_output
  bintable_matches_fern_output
  apis_guru_matches_fern_output
  color_pizza_matches_fern_output
  amazonaws_com_cloudformation_matches_fern_output
  byautomata_io_matches_fern_output
  apideck_proxy_matches_fern_output
  apideck_connector_matches_fern_output
  apideck_ecommerce_matches_fern_output
  apideck_issue_tracking_matches_fern_output
  appwrite_client_matches_fern_output
  apideck_file_storage_matches_fern_output
  apideck_hris_matches_fern_output
  apideck_accounting_matches_fern_output
  calorieninjas_reproduces_the_exact_known_fern_failure_boundary
  eos_matches_fern_output
  apideck_sms_matches_fern_output
  apideck_ecosystem_matches_fern_output
  apideck_customer_support_matches_fern_output
  apideck_lead_matches_fern_output
  apache_org_airflow_matches_fern_output
  openfigi_com_matches_fern_output
  twilio_voice_v1_matches_fern_output
  microcks_local_matches_fern_output
  redhat_catalog_inventory_matches_fern_output
  xero_payroll_au_matches_fern_output
  traccar_matches_fern_output
  reverb_com_matches_fern_output
  maif_otoroshi_matches_fern_output
  portfoliooptimizer_io_matches_fern_output
  openbanking_org_uk_account_info_openapi_matches_fern_output
  netbox_dev_matches_fern_output
  squareup_com_matches_fern_output
  redocly_com_museum_matches_fern_output
  http_toolkit_matches_fern_output
  frankfurter_matches_fern_output
  worldcoin_signup_sequencer_matches_fern_output
  electric_sql_matches_fern_output
  tamoss_matches_fern_output
  slurmdb_rest_matches_fern_output
  nimisampo_matches_fern_output
  free5gc_pdu_session_matches_fern_output
  sigstore_rekor_matches_fern_output
  letta_matches_fern_output
  free5gc_namf_communication_matches_fern_output
  apideck_ats_matches_fern_output
  buildrelay_matches_fern_output
  tlon_notes_matches_fern_output
  twilio_messaging_v1_matches_fern_output
  livepeer_ai_runner_matches_fern_output
  eos_extra_fields_forbid_matches_fern_output
  eos_extra_fields_forbid_flat_matches_fern
  med_anvisa_price_matches_fern_output
  sac_backend_matches_fern_output
  kytos_sdntrace_cp_matches_fern_output
  withsecure_gdpr_subject_rights_matches_fern_output
  prometheus_x_edge_computing_matches_fern_output
  exa_gate_matches_fern_output
  amazonaws_com_cloudfront_matches_fern_output
  khoainats_matches_fern_output
  helios_verifiable_api_matches_fern_output
  eozilla_matches_fern_output
  openepcis_dpp_ready_matches_fern_output
  ndw_accessibility_map_matches_fern_output
  marimo_matches_fern_output
  marimo_client_class_name_matches_fern_output
  blackadi_oauth2_matches_fern_output
  mosip_esignet_matches_fern_output
  openbankingproject_ch_kundenbeziehung_matches_fern_output
  cyberark_conjur_api_matches_fern_output
  adyen_report_notification_matches_fern_output
  adyen_managed_risk_notification_matches_fern_output
  go_kratos_casbin_admin_matches_fern_output
  descope_authzcache_matches_fern_output
  swagger_petstore_matches_fern_output
  swagger_petstore_organization_flat_matches_fern
  cyclonedx_transparency_exchange_matches_fern_output
  adyen_capital_matches_fern_output
  apivideo_android_uploader_matches_fern_output
  truefoundry_trueforge_matches_fern_output
  truefoundry_trueforge_flat_matches_fern
  googleapis_youtubeanalytics_v1_flat_matches_fern
  volview_backend_contract_matches_fern_output
  osparc_simcore_webserver_matches_fern_output
  helixdb_http_api_matches_fern_output
  flowdapt_matches_fern_output
  k8s_container_service_provider_matches_fern_output
  daniweb_connect_matches_fern_output
  chaingateway_io_matches_fern_output
  hubspot_events_matches_fern_output
  paloalto_remote_networks_matches_fern_output
  openintegrationhub_secret_service_matches_fern_output
  strapi_rest_api_matches_fern_output
  listennotes_matches_fern_output
  vtex_pricing_matches_fern_output
  aws_importexport_matches_fern_output
  openbanking_brasil_directory_matches_fern_output
  api_openverse_org_matches_fern_output
  discord_com_matches_fern_output
  braintrust_dev_matches_fern_output
  agco_ats_matches_fern_output
  torrentarr_matches_fern_output
  svix_webhooks_matches_fern_output
  komga_matches_fern_output
  short_io_matches_fern_output
  webflow_v2_matches_fern_output
  loris_dataquery_matches_fern_output
  sftpgo_matches_fern_output
  googleapis_servicebroker_matches_fern_output
  audiobookshelf_matches_fern_output
  steaminputdb_matches_fern_output
  paypal_catalog_products_matches_fern_output
  folio_mod_authtoken_matches_fern_output
  raybot_matches_fern_output
  openlinksw_osdb_matches_fern_output
  ziptax_node_matches_fern_output
  nexmo_messages_matches_fern_output
  deepsearch_ds_v2_matches_fern_output
  mindee_ocr_matches_fern_output
  opencodeui_matches_fern_output
  paloalto_cspm_alerts_matches_fern_output
  paloalto_cspm_reports_matches_fern_output
  paloalto_cspm_search_manager_matches_fern_output
  thrivecart_matches_fern_output
  truefoundry_trueforge_5adde28_matches_fern_output
  fergus_matches_fern_output
  groupe_psa_matches_fern_output
  timelyapp_matches_fern_output
  nextgen_matches_fern_output
  auto_agent_protocol_matches_fern_output
  skool_matches_fern_output
  spendesk_matches_fern_output
  billie_matches_fern_output
  alma_france_matches_fern_output
  outreach_matches_fern_output
  tally_matches_fern_output
  billie_entry_matches_fern_output
  skool_entry_matches_fern_output
  timelyapp_entry_matches_fern_output
  cradl_matches_fern_output
  zulip_matches_fern_output
  zulip_jentic_matches_fern_output
  zulip_jentic_entry_matches_fern_output
  milvus_restful_v2_3_matches_fern_output
  milvus_restful_v2_4_matches_fern_output
  ramu_shogi_matches_fern_output
  langchain_agent_protocol_matches_fern_output
  hse_matches_fern_output
  milvus_vector_operations_matches_fern_output
  mistle_control_plane_matches_fern_output
  osparc_payments_matches_fern_output
  huatuo_node_matches_fern_output
  huatuo_server_matches_fern_output
  viskit_studio_matches_fern_output
  embedpdf_cloudpdf_matches_fern_output
  npq_registration_matches_fern_output
  sim_logs_matches_fern_output
  sim_tables_matches_fern_output
  vellum_gateway_matches_fern_output
  dot_ai_matches_fern_output
  paloalto_code_technologies_matches_fern_output
  marimo_plugins_matches_fern_output
  otoroshi_matches_fern_output
  standrig_matches_fern_output
  mockserver_matches_fern_output
  ideaconsult_enanomapper_matches_fern_output
  openaire_graph_matches_fern_output
  qredence_fleet_rlm_matches_fern_output
  fiware_context_generator_matches_fern_output
  hasura_metadata_matches_fern_output
  zoonk_matches_fern_output
  openfoodfacts_taxonomy_editor_matches_fern_output
  qontract_api_matches_fern_output
  typescript_service_template_matches_fern_output
  oal_example_matches_fern_output
  millenium_falcon_challenge_matches_fern_output
  maximo_wxo_integration_matches_fern_output
  mi_music_matches_fern_output
  g4brym_download_manager_matches_fern_output
  opentosca_license_engine_matches_fern_output
  chat_rest_api_matches_fern_output
  esp32_streamline_bridge_matches_fern_output
  cphos_ai_question_matches_fern_output
  flask_example_heroku_matches_fern_output
  oip_web_api_matches_fern_output
  waylay_queries_matches_fern_output
  offchain_metadata_tools_matches_fern_output
  subsloth_matches_fern_output
  confluent_kafka_connect_matches_fern_output
  breizhsport_catalogue_matches_fern_output
  protoform_conformance_matches_fern_output
  ere_ps_app_matches_fern_output
  apideck_ecosystem_client_class_name_matches_fern_output
  yourbrand_ticketing_matches_fern_output
  peopledatalabs_matches_fern_output
  adyen_acs_notification_matches_fern_output
  googleapis_monitoring_v1_matches_fern_output
  docu_goapiserver_matches_fern_output
  onevoice_matches_fern_output
  xfsc_oidc_identity_resolver_matches_fern_output
  huatuo_node_tree_matches_fern_output
  lootlog_battlelog_matches_fern_output
  ego_microservices_matches_fern_output
  netgsm_sms_matches_fern_output
  zylon_private_gpt_matches_fern_output
  aws_mobileanalytics_matches_fern_output
  mermade_openapi_converter_matches_fern_output
  googleapis_speech_v2beta1_matches_fern_output
  googleapis_youtubeanalytics_v1_matches_fern_output
  vocode_core_matches_fern_output
  dystore_api_matches_fern_output
  langchain_agent_server_matches_fern_output
  rice_shower_matches_fern_output
  supabase_api_v1_matches_fern_output
  rta_in_japan_twitter_matches_fern_output
  onmyshelf_api_matches_fern_output
  formbricks_matches_fern_output
  panoptes_matches_fern_output
  fletch_mcp_matches_fern_output
  microsoft_adme_seismic_matches_fern_output
  dashy_route_api_matches_fern_output
  ahasend_api_matches_fern_output
  farmvibes_ai_matches_fern_output
  rgb_lightning_node_matches_fern_output
  rapidata_identity_matches_fern_output
  ecommerce_ai_skills_runtime_matches_fern_output
  get_a_room_matches_fern_output
  grantly_matches_fern_output
  ebusd_matches_fern_output
  openapitools_csharp_allof_matches_fern_output
  swagger_parser_null_types_matches_fern_output
  tooljet_microsoft_teams_matches_fern_output
  openapi_generator_composed_schema_lowering_matches_fern_output
  rs_server_matches_fern_output
  ingef_conquery_matches_fern_output
  vtex_marketplace_protocol_matches_fern_output
  stellastra_com_matches_fern_output
  contribly_com_matches_fern_output
  openapi_generator_oneof_two_primitives_matches_fern_output
  sourcefuse_bpmn_service_matches_fern_output
  readme_api_application_json_matches_fern_output
  konfig_lucca_organization_matches_fern_output
  ably_sdk_test_proxy_matches_fern_output
  dipjyotimetia_friday_matches_fern_output
  openapi_generator_model_deprecated_matches_fern_output
  nvke_controller_matches_fern_output
  andreychh_coopera_matches_fern_output
  chrome_webstatus_backend_matches_fern_output
  canonical_test_observer_matches_fern_output
  psychic_spec_helpers_testapp_matches_fern_output
  openapi_generator_allof_extension_parent_matches_fern_output
  trpc_openapi_app_router_matches_fern_output
  azure_databox_management_matches_fern_output
  nixtla_timegpt_matches_fern_output
  ollama_api_matches_fern_output
  osparc_director_v2_matches_fern_output
  tuxedo_dapp_matches_fern_output
  blufiles_api_matches_fern_output
  parcelis_api_matches_fern_output
  synthwerk_llm_matches_fern_output
  kompaz_web_frontend_matches_fern_output
  jobster_api_matches_fern_output
  openparser_ocr_matches_fern_output
  openiap_opencore_matches_fern_output
  speech_ai_forge_matches_fern_output
  ummaya_agent_delegation_matches_fern_output
  amrc_acs_directory_matches_fern_output
  notion_mcp_server_matches_fern_output
  laposta_matches_fern_output
  mcp_handle_matches_fern_output
  microsoft_adme_crs_converter_matches_fern_output
  wiim_httpapi_matches_fern_output
  loonfs_matches_fern_output
  happy_hamster_matches_fern_output
  seldon_wrapper_matches_fern_output
)

filter="test(=${inventory[0]})"
for test in "${inventory[@]:1}"; do filter+=" | test(=$test)"; done
nextest=(--locked -p crozier-e2e --test e2e -E "$filter")

listed=$(printf '%s\n' "${inventory[@]}" | sort)
# Nx and CI force colour on; a coloured name would never equal its listed one.
selected=$(cargo nextest list "${nextest[@]}" --message-format oneline --color never | awk '{print $2}' | sort)
[ "$selected" = "$listed" ] || {
  echo "corpus-match: nextest's selection differs from the inventory in tests/corpus_match/match.sh (< listed only, > selected only):" >&2
  diff <(printf '%s\n' "$listed") <(printf '%s\n' "$selected") | grep '^[<>]' >&2 || true
  echo "corpus-match: list each test once, by its exact nextest name (a test in a module by its full path, as \`cargo nextest list -p crozier-e2e --test e2e\` prints it), then re-run" >&2
  exit 1
}
if [ -n "${CORPUS_MATCH_LIST:-}" ]; then
  printf '%s\n' "$selected" >"$CORPUS_MATCH_LIST"
  exit 0
fi

# The source check takes a second; the surface census takes minutes, so it runs
# once the goldens have passed rather than delaying a golden's failure.
python3 tools/corpus/corpus_sources.py check
CROZIER_REQUIRE_CORPUS=1 cargo nextest run "${nextest[@]}" --test-threads "$threads" --no-fail-fast \
  --status-level fail --final-status-level fail
sh scripts/census-python.sh tests/corpus_match/corpus_surface_census_test.py
