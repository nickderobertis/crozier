



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .any import Any
    from .bulk_patch_body import BulkPatchBody
    from .bulk_response_body import BulkResponseBody
    from .byte_stream_body import ByteStreamBody
    from .cert_valid_response import CertValidResponse
    from .done import Done
    from .empty import Empty
    from .error_response import ErrorResponse
    from .error_template_list import ErrorTemplateList
    from .global_config_import_body import GlobalConfigImportBody
    from .health_check_event_list import HealthCheckEventList
    from .host_metrics import HostMetrics
    from .lets_encrypt_cert_body import LetsEncryptCertBody
    from .live_stats import LiveStats
    from .otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
    from .otoroshi_auth_basic_auth_module_config import OtoroshiAuthBasicAuthModuleConfig
    from .otoroshi_auth_basic_auth_module_config_type import OtoroshiAuthBasicAuthModuleConfigType
    from .otoroshi_auth_basic_auth_user import OtoroshiAuthBasicAuthUser
    from .otoroshi_auth_basic_auth_user_webauthn import OtoroshiAuthBasicAuthUserWebauthn
    from .otoroshi_auth_generic_oauth2module_config import OtoroshiAuthGenericOauth2ModuleConfig
    from .otoroshi_auth_generic_oauth2module_config_jwt_verifier import OtoroshiAuthGenericOauth2ModuleConfigJwtVerifier
    from .otoroshi_auth_generic_oauth2module_config_oid_config import OtoroshiAuthGenericOauth2ModuleConfigOidConfig
    from .otoroshi_auth_generic_oauth2module_config_pkce import OtoroshiAuthGenericOauth2ModuleConfigPkce
    from .otoroshi_auth_generic_oauth2module_config_proxy import OtoroshiAuthGenericOauth2ModuleConfigProxy
    from .otoroshi_auth_generic_oauth2module_config_type import OtoroshiAuthGenericOauth2ModuleConfigType
    from .otoroshi_auth_group_filter import OtoroshiAuthGroupFilter
    from .otoroshi_auth_group_rights import OtoroshiAuthGroupRights
    from .otoroshi_auth_ldap_auth_module_config import OtoroshiAuthLdapAuthModuleConfig
    from .otoroshi_auth_ldap_auth_module_config_admin_password import OtoroshiAuthLdapAuthModuleConfigAdminPassword
    from .otoroshi_auth_ldap_auth_module_config_admin_username import OtoroshiAuthLdapAuthModuleConfigAdminUsername
    from .otoroshi_auth_ldap_auth_module_config_metadata_field import OtoroshiAuthLdapAuthModuleConfigMetadataField
    from .otoroshi_auth_ldap_auth_module_config_type import OtoroshiAuthLdapAuthModuleConfigType
    from .otoroshi_auth_ldap_auth_module_config_user_base import OtoroshiAuthLdapAuthModuleConfigUserBase
    from .otoroshi_auth_oauth1module_config import OtoroshiAuthOauth1ModuleConfig
    from .otoroshi_auth_oauth1module_config_type import OtoroshiAuthOauth1ModuleConfigType
    from .otoroshi_auth_pkce_config import OtoroshiAuthPkceConfig
    from .otoroshi_auth_saml_auth_module_config import OtoroshiAuthSamlAuthModuleConfig
    from .otoroshi_auth_saml_auth_module_config_email_attribute_name import (
        OtoroshiAuthSamlAuthModuleConfigEmailAttributeName,
    )
    from .otoroshi_auth_saml_auth_module_config_single_logout_url import OtoroshiAuthSamlAuthModuleConfigSingleLogoutUrl
    from .otoroshi_auth_saml_auth_module_config_type import OtoroshiAuthSamlAuthModuleConfigType
    from .otoroshi_auth_web_authn_details import OtoroshiAuthWebAuthnDetails
    from .otoroshi_events_health_check_event import OtoroshiEventsHealthCheckEvent
    from .otoroshi_events_health_check_event_error import OtoroshiEventsHealthCheckEventError
    from .otoroshi_events_health_check_event_health import OtoroshiEventsHealthCheckEventHealth
    from .otoroshi_events_kafka_config import OtoroshiEventsKafkaConfig
    from .otoroshi_events_kafka_config_key_pass import OtoroshiEventsKafkaConfigKeyPass
    from .otoroshi_events_kafka_config_keystore import OtoroshiEventsKafkaConfigKeystore
    from .otoroshi_events_kafka_config_sasl_config import OtoroshiEventsKafkaConfigSaslConfig
    from .otoroshi_events_kafka_config_truststore import OtoroshiEventsKafkaConfigTruststore
    from .otoroshi_events_kafka_config_type import OtoroshiEventsKafkaConfigType
    from .otoroshi_events_sasl_config import OtoroshiEventsSaslConfig
    from .otoroshi_events_statsd_config import OtoroshiEventsStatsdConfig
    from .otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
    from .otoroshi_models_api_key import OtoroshiModelsApiKey
    from .otoroshi_models_api_key_valid_until import OtoroshiModelsApiKeyValidUntil
    from .otoroshi_models_clever_cloud_settings import OtoroshiModelsCleverCloudSettings
    from .otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
    from .otoroshi_models_elastic_analytics_config import OtoroshiModelsElasticAnalyticsConfig
    from .otoroshi_models_elastic_analytics_config_index import OtoroshiModelsElasticAnalyticsConfigIndex
    from .otoroshi_models_elastic_analytics_config_password import OtoroshiModelsElasticAnalyticsConfigPassword
    from .otoroshi_models_elastic_analytics_config_type import OtoroshiModelsElasticAnalyticsConfigType
    from .otoroshi_models_elastic_analytics_config_user import OtoroshiModelsElasticAnalyticsConfigUser
    from .otoroshi_models_elastic_analytics_config_version import OtoroshiModelsElasticAnalyticsConfigVersion
    from .otoroshi_models_entity_identifier import OtoroshiModelsEntityIdentifier
    from .otoroshi_models_error_template import OtoroshiModelsErrorTemplate
    from .otoroshi_models_es_algo_settings import OtoroshiModelsEsAlgoSettings
    from .otoroshi_models_es_algo_settings_private_key import OtoroshiModelsEsAlgoSettingsPrivateKey
    from .otoroshi_models_es_algo_settings_type import OtoroshiModelsEsAlgoSettingsType
    from .otoroshi_models_eskp_algo_settings import OtoroshiModelsEskpAlgoSettings
    from .otoroshi_models_eskp_algo_settings_type import OtoroshiModelsEskpAlgoSettingsType
    from .otoroshi_models_global_config import OtoroshiModelsGlobalConfig
    from .otoroshi_models_global_config_back_office_auth_ref import OtoroshiModelsGlobalConfigBackOfficeAuthRef
    from .otoroshi_models_global_config_clever_settings import OtoroshiModelsGlobalConfigCleverSettings
    from .otoroshi_models_global_config_elastic_reads_config import OtoroshiModelsGlobalConfigElasticReadsConfig
    from .otoroshi_models_global_config_kafka_config import OtoroshiModelsGlobalConfigKafkaConfig
    from .otoroshi_models_global_config_mailer_settings import OtoroshiModelsGlobalConfigMailerSettings
    from .otoroshi_models_global_config_statsd_config import OtoroshiModelsGlobalConfigStatsdConfig
    from .otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
    from .otoroshi_models_global_jwt_verifier_type import OtoroshiModelsGlobalJwtVerifierType
    from .otoroshi_models_hs_algo_settings import OtoroshiModelsHsAlgoSettings
    from .otoroshi_models_hs_algo_settings_type import OtoroshiModelsHsAlgoSettingsType
    from .otoroshi_models_jwks_algo_settings import OtoroshiModelsJwksAlgoSettings
    from .otoroshi_models_jwks_algo_settings_proxy import OtoroshiModelsJwksAlgoSettingsProxy
    from .otoroshi_models_jwks_algo_settings_type import OtoroshiModelsJwksAlgoSettingsType
    from .otoroshi_models_kid_algo_settings import OtoroshiModelsKidAlgoSettings
    from .otoroshi_models_kid_algo_settings_type import OtoroshiModelsKidAlgoSettingsType
    from .otoroshi_models_otoroshi_admin import OtoroshiModelsOtoroshiAdmin
    from .otoroshi_models_outage import OtoroshiModelsOutage
    from .otoroshi_models_remaining_quotas import OtoroshiModelsRemainingQuotas
    from .otoroshi_models_rs_algo_settings import OtoroshiModelsRsAlgoSettings
    from .otoroshi_models_rs_algo_settings_private_key import OtoroshiModelsRsAlgoSettingsPrivateKey
    from .otoroshi_models_rs_algo_settings_type import OtoroshiModelsRsAlgoSettingsType
    from .otoroshi_models_rsakp_algo_settings import OtoroshiModelsRsakpAlgoSettings
    from .otoroshi_models_rsakp_algo_settings_type import OtoroshiModelsRsakpAlgoSettingsType
    from .otoroshi_models_service_descriptor import OtoroshiModelsServiceDescriptor
    from .otoroshi_models_service_descriptor_auth_config_ref import OtoroshiModelsServiceDescriptorAuthConfigRef
    from .otoroshi_models_service_descriptor_client_validator_ref import (
        OtoroshiModelsServiceDescriptorClientValidatorRef,
    )
    from .otoroshi_models_service_descriptor_identifier import OtoroshiModelsServiceDescriptorIdentifier
    from .otoroshi_models_service_descriptor_issue_cert_ca import OtoroshiModelsServiceDescriptorIssueCertCa
    from .otoroshi_models_service_descriptor_matching_root import OtoroshiModelsServiceDescriptorMatchingRoot
    from .otoroshi_models_service_group import OtoroshiModelsServiceGroup
    from .otoroshi_models_service_group_identifier import OtoroshiModelsServiceGroupIdentifier
    from .otoroshi_models_simple_otoroshi_admin import OtoroshiModelsSimpleOtoroshiAdmin
    from .otoroshi_models_simple_otoroshi_admin_type import OtoroshiModelsSimpleOtoroshiAdminType
    from .otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
    from .otoroshi_models_target import OtoroshiModelsTarget
    from .otoroshi_models_target_ip_address import OtoroshiModelsTargetIpAddress
    from .otoroshi_models_target_protocol import OtoroshiModelsTargetProtocol
    from .otoroshi_models_team import OtoroshiModelsTeam
    from .otoroshi_models_team_access import OtoroshiModelsTeamAccess
    from .otoroshi_models_tenant import OtoroshiModelsTenant
    from .otoroshi_models_user_right import OtoroshiModelsUserRight
    from .otoroshi_models_user_rights import OtoroshiModelsUserRights
    from .otoroshi_models_web_authn_otoroshi_admin import OtoroshiModelsWebAuthnOtoroshiAdmin
    from .otoroshi_models_web_authn_otoroshi_admin_type import OtoroshiModelsWebAuthnOtoroshiAdminType
    from .otoroshi_models_webhook import OtoroshiModelsWebhook
    from .otoroshi_models_webhook_type import OtoroshiModelsWebhookType
    from .otoroshi_next_models_ng_minimal_route import OtoroshiNextModelsNgMinimalRoute
    from .otoroshi_next_models_ng_minimal_route_backend_ref import OtoroshiNextModelsNgMinimalRouteBackendRef
    from .otoroshi_next_models_ng_route import OtoroshiNextModelsNgRoute
    from .otoroshi_next_models_ng_route_backend_ref import OtoroshiNextModelsNgRouteBackendRef
    from .otoroshi_next_models_ng_route_composition import OtoroshiNextModelsNgRouteComposition
    from .otoroshi_next_models_stored_ng_backend import OtoroshiNextModelsStoredNgBackend
    from .otoroshi_script_script import OtoroshiScriptScript
    from .otoroshi_ssl_cert import OtoroshiSslCert
    from .otoroshi_ssl_cert_ca_ref import OtoroshiSslCertCaRef
    from .otoroshi_ssl_cert_cert_type import OtoroshiSslCertCertType
    from .otoroshi_ssl_cert_password import OtoroshiSslCertPassword
    from .otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
    from .otoroshi_ssl_pki_models_gen_cert_response_csr_query import OtoroshiSslPkiModelsGenCertResponseCsrQuery
    from .otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
    from .otoroshi_ssl_pki_models_gen_csr_query_existing_serial_number import (
        OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
    )
    from .otoroshi_ssl_pki_models_gen_csr_query_subject import OtoroshiSslPkiModelsGenCsrQuerySubject
    from .otoroshi_ssl_pki_models_gen_csr_response import OtoroshiSslPkiModelsGenCsrResponse
    from .otoroshi_ssl_pki_models_gen_key_pair_query import OtoroshiSslPkiModelsGenKeyPairQuery
    from .otoroshi_ssl_pki_models_gen_key_pair_response import OtoroshiSslPkiModelsGenKeyPairResponse
    from .otoroshi_ssl_pki_models_sign_cert_response import OtoroshiSslPkiModelsSignCertResponse
    from .otoroshi_ssl_pki_models_sign_cert_response_ca import OtoroshiSslPkiModelsSignCertResponseCa
    from .otoroshi_tcp_tcp_rule import OtoroshiTcpTcpRule
    from .otoroshi_tcp_tcp_service import OtoroshiTcpTcpService
    from .otoroshi_tcp_tcp_target import OtoroshiTcpTcpTarget
    from .otoroshi_tcp_tcp_target_ip import OtoroshiTcpTcpTargetIp
    from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator
    from .otoroshi_utils_json_path_validator_error import OtoroshiUtilsJsonPathValidatorError
    from .otoroshi_utils_mailer_console_mailer_settings import OtoroshiUtilsMailerConsoleMailerSettings
    from .otoroshi_utils_mailer_console_mailer_settings_type import OtoroshiUtilsMailerConsoleMailerSettingsType
    from .otoroshi_utils_mailer_email_location import OtoroshiUtilsMailerEmailLocation
    from .otoroshi_utils_mailer_generic_mailer_settings import OtoroshiUtilsMailerGenericMailerSettings
    from .otoroshi_utils_mailer_generic_mailer_settings_type import OtoroshiUtilsMailerGenericMailerSettingsType
    from .otoroshi_utils_mailer_mailer_settings import OtoroshiUtilsMailerMailerSettings
    from .otoroshi_utils_mailer_mailgun_settings import OtoroshiUtilsMailerMailgunSettings
    from .otoroshi_utils_mailer_mailgun_settings_type import OtoroshiUtilsMailerMailgunSettingsType
    from .otoroshi_utils_mailer_mailjet_settings import OtoroshiUtilsMailerMailjetSettings
    from .otoroshi_utils_mailer_mailjet_settings_type import OtoroshiUtilsMailerMailjetSettingsType
    from .otoroshi_utils_mailer_none_mailer_settings import OtoroshiUtilsMailerNoneMailerSettings
    from .otoroshi_utils_mailer_none_mailer_settings_type import OtoroshiUtilsMailerNoneMailerSettingsType
    from .otoroshi_utils_mailer_sendgrid_settings import OtoroshiUtilsMailerSendgridSettings
    from .otoroshi_utils_mailer_sendgrid_settings_type import OtoroshiUtilsMailerSendgridSettingsType
    from .outages_list import OutagesList
    from .patch_body import PatchBody
    from .patch_document import PatchDocument
    from .patch_document_op import PatchDocumentOp
    from .pem_certificate_body import PemCertificateBody
    from .pem_csr_body import PemCsrBody
    from .play_api_libs_ws_ws_proxy_server import PlayApiLibsWsWsProxyServer
    from .service_descriptor_list import ServiceDescriptorList
    from .string_list import StringList
    from .targets_list import TargetsList
    from .unknown import Unknown
    from .web_authn_registration_finish_body import WebAuthnRegistrationFinishBody
    from .web_authn_registration_start_body import WebAuthnRegistrationStartBody
_dynamic_imports: typing.Dict[str, str] = {
    "Any": ".any",
    "BulkPatchBody": ".bulk_patch_body",
    "BulkResponseBody": ".bulk_response_body",
    "ByteStreamBody": ".byte_stream_body",
    "CertValidResponse": ".cert_valid_response",
    "Done": ".done",
    "Empty": ".empty",
    "ErrorResponse": ".error_response",
    "ErrorTemplateList": ".error_template_list",
    "GlobalConfigImportBody": ".global_config_import_body",
    "HealthCheckEventList": ".health_check_event_list",
    "HostMetrics": ".host_metrics",
    "LetsEncryptCertBody": ".lets_encrypt_cert_body",
    "LiveStats": ".live_stats",
    "OtoroshiAuthAuthModuleConfig": ".otoroshi_auth_auth_module_config",
    "OtoroshiAuthBasicAuthModuleConfig": ".otoroshi_auth_basic_auth_module_config",
    "OtoroshiAuthBasicAuthModuleConfigType": ".otoroshi_auth_basic_auth_module_config_type",
    "OtoroshiAuthBasicAuthUser": ".otoroshi_auth_basic_auth_user",
    "OtoroshiAuthBasicAuthUserWebauthn": ".otoroshi_auth_basic_auth_user_webauthn",
    "OtoroshiAuthGenericOauth2ModuleConfig": ".otoroshi_auth_generic_oauth2module_config",
    "OtoroshiAuthGenericOauth2ModuleConfigJwtVerifier": ".otoroshi_auth_generic_oauth2module_config_jwt_verifier",
    "OtoroshiAuthGenericOauth2ModuleConfigOidConfig": ".otoroshi_auth_generic_oauth2module_config_oid_config",
    "OtoroshiAuthGenericOauth2ModuleConfigPkce": ".otoroshi_auth_generic_oauth2module_config_pkce",
    "OtoroshiAuthGenericOauth2ModuleConfigProxy": ".otoroshi_auth_generic_oauth2module_config_proxy",
    "OtoroshiAuthGenericOauth2ModuleConfigType": ".otoroshi_auth_generic_oauth2module_config_type",
    "OtoroshiAuthGroupFilter": ".otoroshi_auth_group_filter",
    "OtoroshiAuthGroupRights": ".otoroshi_auth_group_rights",
    "OtoroshiAuthLdapAuthModuleConfig": ".otoroshi_auth_ldap_auth_module_config",
    "OtoroshiAuthLdapAuthModuleConfigAdminPassword": ".otoroshi_auth_ldap_auth_module_config_admin_password",
    "OtoroshiAuthLdapAuthModuleConfigAdminUsername": ".otoroshi_auth_ldap_auth_module_config_admin_username",
    "OtoroshiAuthLdapAuthModuleConfigMetadataField": ".otoroshi_auth_ldap_auth_module_config_metadata_field",
    "OtoroshiAuthLdapAuthModuleConfigType": ".otoroshi_auth_ldap_auth_module_config_type",
    "OtoroshiAuthLdapAuthModuleConfigUserBase": ".otoroshi_auth_ldap_auth_module_config_user_base",
    "OtoroshiAuthOauth1ModuleConfig": ".otoroshi_auth_oauth1module_config",
    "OtoroshiAuthOauth1ModuleConfigType": ".otoroshi_auth_oauth1module_config_type",
    "OtoroshiAuthPkceConfig": ".otoroshi_auth_pkce_config",
    "OtoroshiAuthSamlAuthModuleConfig": ".otoroshi_auth_saml_auth_module_config",
    "OtoroshiAuthSamlAuthModuleConfigEmailAttributeName": ".otoroshi_auth_saml_auth_module_config_email_attribute_name",
    "OtoroshiAuthSamlAuthModuleConfigSingleLogoutUrl": ".otoroshi_auth_saml_auth_module_config_single_logout_url",
    "OtoroshiAuthSamlAuthModuleConfigType": ".otoroshi_auth_saml_auth_module_config_type",
    "OtoroshiAuthWebAuthnDetails": ".otoroshi_auth_web_authn_details",
    "OtoroshiEventsHealthCheckEvent": ".otoroshi_events_health_check_event",
    "OtoroshiEventsHealthCheckEventError": ".otoroshi_events_health_check_event_error",
    "OtoroshiEventsHealthCheckEventHealth": ".otoroshi_events_health_check_event_health",
    "OtoroshiEventsKafkaConfig": ".otoroshi_events_kafka_config",
    "OtoroshiEventsKafkaConfigKeyPass": ".otoroshi_events_kafka_config_key_pass",
    "OtoroshiEventsKafkaConfigKeystore": ".otoroshi_events_kafka_config_keystore",
    "OtoroshiEventsKafkaConfigSaslConfig": ".otoroshi_events_kafka_config_sasl_config",
    "OtoroshiEventsKafkaConfigTruststore": ".otoroshi_events_kafka_config_truststore",
    "OtoroshiEventsKafkaConfigType": ".otoroshi_events_kafka_config_type",
    "OtoroshiEventsSaslConfig": ".otoroshi_events_sasl_config",
    "OtoroshiEventsStatsdConfig": ".otoroshi_events_statsd_config",
    "OtoroshiModelsAlgoSettings": ".otoroshi_models_algo_settings",
    "OtoroshiModelsApiKey": ".otoroshi_models_api_key",
    "OtoroshiModelsApiKeyValidUntil": ".otoroshi_models_api_key_valid_until",
    "OtoroshiModelsCleverCloudSettings": ".otoroshi_models_clever_cloud_settings",
    "OtoroshiModelsDataExporterConfig": ".otoroshi_models_data_exporter_config",
    "OtoroshiModelsElasticAnalyticsConfig": ".otoroshi_models_elastic_analytics_config",
    "OtoroshiModelsElasticAnalyticsConfigIndex": ".otoroshi_models_elastic_analytics_config_index",
    "OtoroshiModelsElasticAnalyticsConfigPassword": ".otoroshi_models_elastic_analytics_config_password",
    "OtoroshiModelsElasticAnalyticsConfigType": ".otoroshi_models_elastic_analytics_config_type",
    "OtoroshiModelsElasticAnalyticsConfigUser": ".otoroshi_models_elastic_analytics_config_user",
    "OtoroshiModelsElasticAnalyticsConfigVersion": ".otoroshi_models_elastic_analytics_config_version",
    "OtoroshiModelsEntityIdentifier": ".otoroshi_models_entity_identifier",
    "OtoroshiModelsErrorTemplate": ".otoroshi_models_error_template",
    "OtoroshiModelsEsAlgoSettings": ".otoroshi_models_es_algo_settings",
    "OtoroshiModelsEsAlgoSettingsPrivateKey": ".otoroshi_models_es_algo_settings_private_key",
    "OtoroshiModelsEsAlgoSettingsType": ".otoroshi_models_es_algo_settings_type",
    "OtoroshiModelsEskpAlgoSettings": ".otoroshi_models_eskp_algo_settings",
    "OtoroshiModelsEskpAlgoSettingsType": ".otoroshi_models_eskp_algo_settings_type",
    "OtoroshiModelsGlobalConfig": ".otoroshi_models_global_config",
    "OtoroshiModelsGlobalConfigBackOfficeAuthRef": ".otoroshi_models_global_config_back_office_auth_ref",
    "OtoroshiModelsGlobalConfigCleverSettings": ".otoroshi_models_global_config_clever_settings",
    "OtoroshiModelsGlobalConfigElasticReadsConfig": ".otoroshi_models_global_config_elastic_reads_config",
    "OtoroshiModelsGlobalConfigKafkaConfig": ".otoroshi_models_global_config_kafka_config",
    "OtoroshiModelsGlobalConfigMailerSettings": ".otoroshi_models_global_config_mailer_settings",
    "OtoroshiModelsGlobalConfigStatsdConfig": ".otoroshi_models_global_config_statsd_config",
    "OtoroshiModelsGlobalJwtVerifier": ".otoroshi_models_global_jwt_verifier",
    "OtoroshiModelsGlobalJwtVerifierType": ".otoroshi_models_global_jwt_verifier_type",
    "OtoroshiModelsHsAlgoSettings": ".otoroshi_models_hs_algo_settings",
    "OtoroshiModelsHsAlgoSettingsType": ".otoroshi_models_hs_algo_settings_type",
    "OtoroshiModelsJwksAlgoSettings": ".otoroshi_models_jwks_algo_settings",
    "OtoroshiModelsJwksAlgoSettingsProxy": ".otoroshi_models_jwks_algo_settings_proxy",
    "OtoroshiModelsJwksAlgoSettingsType": ".otoroshi_models_jwks_algo_settings_type",
    "OtoroshiModelsKidAlgoSettings": ".otoroshi_models_kid_algo_settings",
    "OtoroshiModelsKidAlgoSettingsType": ".otoroshi_models_kid_algo_settings_type",
    "OtoroshiModelsOtoroshiAdmin": ".otoroshi_models_otoroshi_admin",
    "OtoroshiModelsOutage": ".otoroshi_models_outage",
    "OtoroshiModelsRemainingQuotas": ".otoroshi_models_remaining_quotas",
    "OtoroshiModelsRsAlgoSettings": ".otoroshi_models_rs_algo_settings",
    "OtoroshiModelsRsAlgoSettingsPrivateKey": ".otoroshi_models_rs_algo_settings_private_key",
    "OtoroshiModelsRsAlgoSettingsType": ".otoroshi_models_rs_algo_settings_type",
    "OtoroshiModelsRsakpAlgoSettings": ".otoroshi_models_rsakp_algo_settings",
    "OtoroshiModelsRsakpAlgoSettingsType": ".otoroshi_models_rsakp_algo_settings_type",
    "OtoroshiModelsServiceDescriptor": ".otoroshi_models_service_descriptor",
    "OtoroshiModelsServiceDescriptorAuthConfigRef": ".otoroshi_models_service_descriptor_auth_config_ref",
    "OtoroshiModelsServiceDescriptorClientValidatorRef": ".otoroshi_models_service_descriptor_client_validator_ref",
    "OtoroshiModelsServiceDescriptorIdentifier": ".otoroshi_models_service_descriptor_identifier",
    "OtoroshiModelsServiceDescriptorIssueCertCa": ".otoroshi_models_service_descriptor_issue_cert_ca",
    "OtoroshiModelsServiceDescriptorMatchingRoot": ".otoroshi_models_service_descriptor_matching_root",
    "OtoroshiModelsServiceGroup": ".otoroshi_models_service_group",
    "OtoroshiModelsServiceGroupIdentifier": ".otoroshi_models_service_group_identifier",
    "OtoroshiModelsSimpleOtoroshiAdmin": ".otoroshi_models_simple_otoroshi_admin",
    "OtoroshiModelsSimpleOtoroshiAdminType": ".otoroshi_models_simple_otoroshi_admin_type",
    "OtoroshiModelsSnowMonkeyConfig": ".otoroshi_models_snow_monkey_config",
    "OtoroshiModelsTarget": ".otoroshi_models_target",
    "OtoroshiModelsTargetIpAddress": ".otoroshi_models_target_ip_address",
    "OtoroshiModelsTargetProtocol": ".otoroshi_models_target_protocol",
    "OtoroshiModelsTeam": ".otoroshi_models_team",
    "OtoroshiModelsTeamAccess": ".otoroshi_models_team_access",
    "OtoroshiModelsTenant": ".otoroshi_models_tenant",
    "OtoroshiModelsUserRight": ".otoroshi_models_user_right",
    "OtoroshiModelsUserRights": ".otoroshi_models_user_rights",
    "OtoroshiModelsWebAuthnOtoroshiAdmin": ".otoroshi_models_web_authn_otoroshi_admin",
    "OtoroshiModelsWebAuthnOtoroshiAdminType": ".otoroshi_models_web_authn_otoroshi_admin_type",
    "OtoroshiModelsWebhook": ".otoroshi_models_webhook",
    "OtoroshiModelsWebhookType": ".otoroshi_models_webhook_type",
    "OtoroshiNextModelsNgMinimalRoute": ".otoroshi_next_models_ng_minimal_route",
    "OtoroshiNextModelsNgMinimalRouteBackendRef": ".otoroshi_next_models_ng_minimal_route_backend_ref",
    "OtoroshiNextModelsNgRoute": ".otoroshi_next_models_ng_route",
    "OtoroshiNextModelsNgRouteBackendRef": ".otoroshi_next_models_ng_route_backend_ref",
    "OtoroshiNextModelsNgRouteComposition": ".otoroshi_next_models_ng_route_composition",
    "OtoroshiNextModelsStoredNgBackend": ".otoroshi_next_models_stored_ng_backend",
    "OtoroshiScriptScript": ".otoroshi_script_script",
    "OtoroshiSslCert": ".otoroshi_ssl_cert",
    "OtoroshiSslCertCaRef": ".otoroshi_ssl_cert_ca_ref",
    "OtoroshiSslCertCertType": ".otoroshi_ssl_cert_cert_type",
    "OtoroshiSslCertPassword": ".otoroshi_ssl_cert_password",
    "OtoroshiSslPkiModelsGenCertResponse": ".otoroshi_ssl_pki_models_gen_cert_response",
    "OtoroshiSslPkiModelsGenCertResponseCsrQuery": ".otoroshi_ssl_pki_models_gen_cert_response_csr_query",
    "OtoroshiSslPkiModelsGenCsrQuery": ".otoroshi_ssl_pki_models_gen_csr_query",
    "OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber": ".otoroshi_ssl_pki_models_gen_csr_query_existing_serial_number",
    "OtoroshiSslPkiModelsGenCsrQuerySubject": ".otoroshi_ssl_pki_models_gen_csr_query_subject",
    "OtoroshiSslPkiModelsGenCsrResponse": ".otoroshi_ssl_pki_models_gen_csr_response",
    "OtoroshiSslPkiModelsGenKeyPairQuery": ".otoroshi_ssl_pki_models_gen_key_pair_query",
    "OtoroshiSslPkiModelsGenKeyPairResponse": ".otoroshi_ssl_pki_models_gen_key_pair_response",
    "OtoroshiSslPkiModelsSignCertResponse": ".otoroshi_ssl_pki_models_sign_cert_response",
    "OtoroshiSslPkiModelsSignCertResponseCa": ".otoroshi_ssl_pki_models_sign_cert_response_ca",
    "OtoroshiTcpTcpRule": ".otoroshi_tcp_tcp_rule",
    "OtoroshiTcpTcpService": ".otoroshi_tcp_tcp_service",
    "OtoroshiTcpTcpTarget": ".otoroshi_tcp_tcp_target",
    "OtoroshiTcpTcpTargetIp": ".otoroshi_tcp_tcp_target_ip",
    "OtoroshiUtilsJsonPathValidator": ".otoroshi_utils_json_path_validator",
    "OtoroshiUtilsJsonPathValidatorError": ".otoroshi_utils_json_path_validator_error",
    "OtoroshiUtilsMailerConsoleMailerSettings": ".otoroshi_utils_mailer_console_mailer_settings",
    "OtoroshiUtilsMailerConsoleMailerSettingsType": ".otoroshi_utils_mailer_console_mailer_settings_type",
    "OtoroshiUtilsMailerEmailLocation": ".otoroshi_utils_mailer_email_location",
    "OtoroshiUtilsMailerGenericMailerSettings": ".otoroshi_utils_mailer_generic_mailer_settings",
    "OtoroshiUtilsMailerGenericMailerSettingsType": ".otoroshi_utils_mailer_generic_mailer_settings_type",
    "OtoroshiUtilsMailerMailerSettings": ".otoroshi_utils_mailer_mailer_settings",
    "OtoroshiUtilsMailerMailgunSettings": ".otoroshi_utils_mailer_mailgun_settings",
    "OtoroshiUtilsMailerMailgunSettingsType": ".otoroshi_utils_mailer_mailgun_settings_type",
    "OtoroshiUtilsMailerMailjetSettings": ".otoroshi_utils_mailer_mailjet_settings",
    "OtoroshiUtilsMailerMailjetSettingsType": ".otoroshi_utils_mailer_mailjet_settings_type",
    "OtoroshiUtilsMailerNoneMailerSettings": ".otoroshi_utils_mailer_none_mailer_settings",
    "OtoroshiUtilsMailerNoneMailerSettingsType": ".otoroshi_utils_mailer_none_mailer_settings_type",
    "OtoroshiUtilsMailerSendgridSettings": ".otoroshi_utils_mailer_sendgrid_settings",
    "OtoroshiUtilsMailerSendgridSettingsType": ".otoroshi_utils_mailer_sendgrid_settings_type",
    "OutagesList": ".outages_list",
    "PatchBody": ".patch_body",
    "PatchDocument": ".patch_document",
    "PatchDocumentOp": ".patch_document_op",
    "PemCertificateBody": ".pem_certificate_body",
    "PemCsrBody": ".pem_csr_body",
    "PlayApiLibsWsWsProxyServer": ".play_api_libs_ws_ws_proxy_server",
    "ServiceDescriptorList": ".service_descriptor_list",
    "StringList": ".string_list",
    "TargetsList": ".targets_list",
    "Unknown": ".unknown",
    "WebAuthnRegistrationFinishBody": ".web_authn_registration_finish_body",
    "WebAuthnRegistrationStartBody": ".web_authn_registration_start_body",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Any",
    "BulkPatchBody",
    "BulkResponseBody",
    "ByteStreamBody",
    "CertValidResponse",
    "Done",
    "Empty",
    "ErrorResponse",
    "ErrorTemplateList",
    "GlobalConfigImportBody",
    "HealthCheckEventList",
    "HostMetrics",
    "LetsEncryptCertBody",
    "LiveStats",
    "OtoroshiAuthAuthModuleConfig",
    "OtoroshiAuthBasicAuthModuleConfig",
    "OtoroshiAuthBasicAuthModuleConfigType",
    "OtoroshiAuthBasicAuthUser",
    "OtoroshiAuthBasicAuthUserWebauthn",
    "OtoroshiAuthGenericOauth2ModuleConfig",
    "OtoroshiAuthGenericOauth2ModuleConfigJwtVerifier",
    "OtoroshiAuthGenericOauth2ModuleConfigOidConfig",
    "OtoroshiAuthGenericOauth2ModuleConfigPkce",
    "OtoroshiAuthGenericOauth2ModuleConfigProxy",
    "OtoroshiAuthGenericOauth2ModuleConfigType",
    "OtoroshiAuthGroupFilter",
    "OtoroshiAuthGroupRights",
    "OtoroshiAuthLdapAuthModuleConfig",
    "OtoroshiAuthLdapAuthModuleConfigAdminPassword",
    "OtoroshiAuthLdapAuthModuleConfigAdminUsername",
    "OtoroshiAuthLdapAuthModuleConfigMetadataField",
    "OtoroshiAuthLdapAuthModuleConfigType",
    "OtoroshiAuthLdapAuthModuleConfigUserBase",
    "OtoroshiAuthOauth1ModuleConfig",
    "OtoroshiAuthOauth1ModuleConfigType",
    "OtoroshiAuthPkceConfig",
    "OtoroshiAuthSamlAuthModuleConfig",
    "OtoroshiAuthSamlAuthModuleConfigEmailAttributeName",
    "OtoroshiAuthSamlAuthModuleConfigSingleLogoutUrl",
    "OtoroshiAuthSamlAuthModuleConfigType",
    "OtoroshiAuthWebAuthnDetails",
    "OtoroshiEventsHealthCheckEvent",
    "OtoroshiEventsHealthCheckEventError",
    "OtoroshiEventsHealthCheckEventHealth",
    "OtoroshiEventsKafkaConfig",
    "OtoroshiEventsKafkaConfigKeyPass",
    "OtoroshiEventsKafkaConfigKeystore",
    "OtoroshiEventsKafkaConfigSaslConfig",
    "OtoroshiEventsKafkaConfigTruststore",
    "OtoroshiEventsKafkaConfigType",
    "OtoroshiEventsSaslConfig",
    "OtoroshiEventsStatsdConfig",
    "OtoroshiModelsAlgoSettings",
    "OtoroshiModelsApiKey",
    "OtoroshiModelsApiKeyValidUntil",
    "OtoroshiModelsCleverCloudSettings",
    "OtoroshiModelsDataExporterConfig",
    "OtoroshiModelsElasticAnalyticsConfig",
    "OtoroshiModelsElasticAnalyticsConfigIndex",
    "OtoroshiModelsElasticAnalyticsConfigPassword",
    "OtoroshiModelsElasticAnalyticsConfigType",
    "OtoroshiModelsElasticAnalyticsConfigUser",
    "OtoroshiModelsElasticAnalyticsConfigVersion",
    "OtoroshiModelsEntityIdentifier",
    "OtoroshiModelsErrorTemplate",
    "OtoroshiModelsEsAlgoSettings",
    "OtoroshiModelsEsAlgoSettingsPrivateKey",
    "OtoroshiModelsEsAlgoSettingsType",
    "OtoroshiModelsEskpAlgoSettings",
    "OtoroshiModelsEskpAlgoSettingsType",
    "OtoroshiModelsGlobalConfig",
    "OtoroshiModelsGlobalConfigBackOfficeAuthRef",
    "OtoroshiModelsGlobalConfigCleverSettings",
    "OtoroshiModelsGlobalConfigElasticReadsConfig",
    "OtoroshiModelsGlobalConfigKafkaConfig",
    "OtoroshiModelsGlobalConfigMailerSettings",
    "OtoroshiModelsGlobalConfigStatsdConfig",
    "OtoroshiModelsGlobalJwtVerifier",
    "OtoroshiModelsGlobalJwtVerifierType",
    "OtoroshiModelsHsAlgoSettings",
    "OtoroshiModelsHsAlgoSettingsType",
    "OtoroshiModelsJwksAlgoSettings",
    "OtoroshiModelsJwksAlgoSettingsProxy",
    "OtoroshiModelsJwksAlgoSettingsType",
    "OtoroshiModelsKidAlgoSettings",
    "OtoroshiModelsKidAlgoSettingsType",
    "OtoroshiModelsOtoroshiAdmin",
    "OtoroshiModelsOutage",
    "OtoroshiModelsRemainingQuotas",
    "OtoroshiModelsRsAlgoSettings",
    "OtoroshiModelsRsAlgoSettingsPrivateKey",
    "OtoroshiModelsRsAlgoSettingsType",
    "OtoroshiModelsRsakpAlgoSettings",
    "OtoroshiModelsRsakpAlgoSettingsType",
    "OtoroshiModelsServiceDescriptor",
    "OtoroshiModelsServiceDescriptorAuthConfigRef",
    "OtoroshiModelsServiceDescriptorClientValidatorRef",
    "OtoroshiModelsServiceDescriptorIdentifier",
    "OtoroshiModelsServiceDescriptorIssueCertCa",
    "OtoroshiModelsServiceDescriptorMatchingRoot",
    "OtoroshiModelsServiceGroup",
    "OtoroshiModelsServiceGroupIdentifier",
    "OtoroshiModelsSimpleOtoroshiAdmin",
    "OtoroshiModelsSimpleOtoroshiAdminType",
    "OtoroshiModelsSnowMonkeyConfig",
    "OtoroshiModelsTarget",
    "OtoroshiModelsTargetIpAddress",
    "OtoroshiModelsTargetProtocol",
    "OtoroshiModelsTeam",
    "OtoroshiModelsTeamAccess",
    "OtoroshiModelsTenant",
    "OtoroshiModelsUserRight",
    "OtoroshiModelsUserRights",
    "OtoroshiModelsWebAuthnOtoroshiAdmin",
    "OtoroshiModelsWebAuthnOtoroshiAdminType",
    "OtoroshiModelsWebhook",
    "OtoroshiModelsWebhookType",
    "OtoroshiNextModelsNgMinimalRoute",
    "OtoroshiNextModelsNgMinimalRouteBackendRef",
    "OtoroshiNextModelsNgRoute",
    "OtoroshiNextModelsNgRouteBackendRef",
    "OtoroshiNextModelsNgRouteComposition",
    "OtoroshiNextModelsStoredNgBackend",
    "OtoroshiScriptScript",
    "OtoroshiSslCert",
    "OtoroshiSslCertCaRef",
    "OtoroshiSslCertCertType",
    "OtoroshiSslCertPassword",
    "OtoroshiSslPkiModelsGenCertResponse",
    "OtoroshiSslPkiModelsGenCertResponseCsrQuery",
    "OtoroshiSslPkiModelsGenCsrQuery",
    "OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber",
    "OtoroshiSslPkiModelsGenCsrQuerySubject",
    "OtoroshiSslPkiModelsGenCsrResponse",
    "OtoroshiSslPkiModelsGenKeyPairQuery",
    "OtoroshiSslPkiModelsGenKeyPairResponse",
    "OtoroshiSslPkiModelsSignCertResponse",
    "OtoroshiSslPkiModelsSignCertResponseCa",
    "OtoroshiTcpTcpRule",
    "OtoroshiTcpTcpService",
    "OtoroshiTcpTcpTarget",
    "OtoroshiTcpTcpTargetIp",
    "OtoroshiUtilsJsonPathValidator",
    "OtoroshiUtilsJsonPathValidatorError",
    "OtoroshiUtilsMailerConsoleMailerSettings",
    "OtoroshiUtilsMailerConsoleMailerSettingsType",
    "OtoroshiUtilsMailerEmailLocation",
    "OtoroshiUtilsMailerGenericMailerSettings",
    "OtoroshiUtilsMailerGenericMailerSettingsType",
    "OtoroshiUtilsMailerMailerSettings",
    "OtoroshiUtilsMailerMailgunSettings",
    "OtoroshiUtilsMailerMailgunSettingsType",
    "OtoroshiUtilsMailerMailjetSettings",
    "OtoroshiUtilsMailerMailjetSettingsType",
    "OtoroshiUtilsMailerNoneMailerSettings",
    "OtoroshiUtilsMailerNoneMailerSettingsType",
    "OtoroshiUtilsMailerSendgridSettings",
    "OtoroshiUtilsMailerSendgridSettingsType",
    "OutagesList",
    "PatchBody",
    "PatchDocument",
    "PatchDocumentOp",
    "PemCertificateBody",
    "PemCsrBody",
    "PlayApiLibsWsWsProxyServer",
    "ServiceDescriptorList",
    "StringList",
    "TargetsList",
    "Unknown",
    "WebAuthnRegistrationFinishBody",
    "WebAuthnRegistrationStartBody",
]
