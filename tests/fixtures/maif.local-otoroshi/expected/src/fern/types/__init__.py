



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_key import ApiKey
    from .auth0config import Auth0Config
    from .bad_response import BadResponse
    from .bad_responses_fault_config import BadResponsesFaultConfig
    from .canary import Canary
    from .certificate import Certificate
    from .chaos_config import ChaosConfig
    from .clever_settings import CleverSettings
    from .client_config import ClientConfig
    from .console_data_exporter_config import ConsoleDataExporterConfig
    from .cors_settings import CorsSettings
    from .custom_data_exporter_config import CustomDataExporterConfig
    from .data_exporter_config import DataExporterConfig
    from .data_exporter_config_config import DataExporterConfigConfig
    from .data_exporter_config_typ import DataExporterConfigTyp
    from .deleted import Deleted
    from .done import Done
    from .elastic_config import ElasticConfig
    from .environment import Environment
    from .error_template import ErrorTemplate
    from .es_algo_settings import EsAlgoSettings
    from .exposed_api import ExposedApi
    from .file_data_exporter_config import FileDataExporterConfig
    from .filtering import Filtering
    from .generic_oauth2module_config import GenericOauth2ModuleConfig
    from .generic_oauth2module_config_jwt_verifier import GenericOauth2ModuleConfigJwtVerifier
    from .global_config import GlobalConfig
    from .global_jwt_verifier import GlobalJwtVerifier
    from .global_jwt_verifier_algo_settings import GlobalJwtVerifierAlgoSettings
    from .global_jwt_verifier_source import GlobalJwtVerifierSource
    from .global_jwt_verifier_strategy import GlobalJwtVerifierStrategy
    from .group import Group
    from .gzip import Gzip
    from .health_check import HealthCheck
    from .hs_algo_settings import HsAlgoSettings
    from .import_export import ImportExport
    from .import_export_admins_item import ImportExportAdminsItem
    from .import_export_api_keys_item import ImportExportApiKeysItem
    from .import_export_error_templates_item import ImportExportErrorTemplatesItem
    from .import_export_service_descriptors_item import ImportExportServiceDescriptorsItem
    from .import_export_service_descriptors_item_jwt_verifier import ImportExportServiceDescriptorsItemJwtVerifier
    from .import_export_service_descriptors_item_sec_com_settings import (
        ImportExportServiceDescriptorsItemSecComSettings,
    )
    from .import_export_service_groups_item import ImportExportServiceGroupsItem
    from .import_export_simple_admins_item import ImportExportSimpleAdminsItem
    from .import_export_stats import ImportExportStats
    from .in_cookie import InCookie
    from .in_header import InHeader
    from .in_memory_auth_module_config import InMemoryAuthModuleConfig
    from .in_memory_user import InMemoryUser
    from .in_query_param import InQueryParam
    from .ip_filtering import IpFiltering
    from .jwks_algo_settings import JwksAlgoSettings
    from .kafka_config import KafkaConfig
    from .large_request_fault_config import LargeRequestFaultConfig
    from .large_response_fault_config import LargeResponseFaultConfig
    from .latency_injection_fault_config import LatencyInjectionFaultConfig
    from .ldap_auth_module_config import LdapAuthModuleConfig
    from .ldap_user import LdapUser
    from .local_jwt_verifier import LocalJwtVerifier
    from .local_jwt_verifier_algo_settings import LocalJwtVerifierAlgoSettings
    from .local_jwt_verifier_source import LocalJwtVerifierSource
    from .local_jwt_verifier_strategy import LocalJwtVerifierStrategy
    from .location import Location
    from .mailer_console_exporter_config import MailerConsoleExporterConfig
    from .mailer_console_exporter_config_type import MailerConsoleExporterConfigType
    from .mailer_generic_exporter_config import MailerGenericExporterConfig
    from .mailer_generic_exporter_config_type import MailerGenericExporterConfigType
    from .mailer_mailgun_exporter_config import MailerMailgunExporterConfig
    from .mailer_mailgun_exporter_config_type import MailerMailgunExporterConfigType
    from .mailer_mailjet_exporter_config import MailerMailjetExporterConfig
    from .mailer_mailjet_exporter_config_type import MailerMailjetExporterConfigType
    from .mailer_sendgrid_exporter_config import MailerSendgridExporterConfig
    from .mailer_sendgrid_exporter_config_type import MailerSendgridExporterConfigType
    from .mailer_settings import MailerSettings
    from .mapping_settings import MappingSettings
    from .otoroshi_health import OtoroshiHealth
    from .otoroshi_health_datastore import OtoroshiHealthDatastore
    from .otoroshi_health_otoroshi import OtoroshiHealthOtoroshi
    from .outage import Outage
    from .outage_strategy import OutageStrategy
    from .pass_through import PassThrough
    from .patch import Patch
    from .patch_item import PatchItem
    from .patch_item_op import PatchItemOp
    from .pulsar_data_exporter_config import PulsarDataExporterConfig
    from .quotas import Quotas
    from .redirection_settings import RedirectionSettings
    from .ref_jwt_verifier import RefJwtVerifier
    from .rs_algo_settings import RsAlgoSettings
    from .script import Script
    from .script_compilation_error import ScriptCompilationError
    from .script_compilation_result import ScriptCompilationResult
    from .service import Service
    from .service_jwt_verifier import ServiceJwtVerifier
    from .service_sec_com_settings import ServiceSecComSettings
    from .sign import Sign
    from .sign_algo_settings import SignAlgoSettings
    from .simple_admin import SimpleAdmin
    from .snow_monkey_config import SnowMonkeyConfig
    from .stats import Stats
    from .statsd_config import StatsdConfig
    from .target import Target
    from .transform import Transform
    from .transform_algo_settings import TransformAlgoSettings
    from .transform_settings import TransformSettings
    from .transform_settings_location import TransformSettingsLocation
    from .u2f_admin import U2FAdmin
    from .validation_authority import ValidationAuthority
    from .verification_settings import VerificationSettings
    from .webhook import Webhook
    from .whebhook_config import WhebhookConfig
_dynamic_imports: typing.Dict[str, str] = {
    "ApiKey": ".api_key",
    "Auth0Config": ".auth0config",
    "BadResponse": ".bad_response",
    "BadResponsesFaultConfig": ".bad_responses_fault_config",
    "Canary": ".canary",
    "Certificate": ".certificate",
    "ChaosConfig": ".chaos_config",
    "CleverSettings": ".clever_settings",
    "ClientConfig": ".client_config",
    "ConsoleDataExporterConfig": ".console_data_exporter_config",
    "CorsSettings": ".cors_settings",
    "CustomDataExporterConfig": ".custom_data_exporter_config",
    "DataExporterConfig": ".data_exporter_config",
    "DataExporterConfigConfig": ".data_exporter_config_config",
    "DataExporterConfigTyp": ".data_exporter_config_typ",
    "Deleted": ".deleted",
    "Done": ".done",
    "ElasticConfig": ".elastic_config",
    "Environment": ".environment",
    "ErrorTemplate": ".error_template",
    "EsAlgoSettings": ".es_algo_settings",
    "ExposedApi": ".exposed_api",
    "FileDataExporterConfig": ".file_data_exporter_config",
    "Filtering": ".filtering",
    "GenericOauth2ModuleConfig": ".generic_oauth2module_config",
    "GenericOauth2ModuleConfigJwtVerifier": ".generic_oauth2module_config_jwt_verifier",
    "GlobalConfig": ".global_config",
    "GlobalJwtVerifier": ".global_jwt_verifier",
    "GlobalJwtVerifierAlgoSettings": ".global_jwt_verifier_algo_settings",
    "GlobalJwtVerifierSource": ".global_jwt_verifier_source",
    "GlobalJwtVerifierStrategy": ".global_jwt_verifier_strategy",
    "Group": ".group",
    "Gzip": ".gzip",
    "HealthCheck": ".health_check",
    "HsAlgoSettings": ".hs_algo_settings",
    "ImportExport": ".import_export",
    "ImportExportAdminsItem": ".import_export_admins_item",
    "ImportExportApiKeysItem": ".import_export_api_keys_item",
    "ImportExportErrorTemplatesItem": ".import_export_error_templates_item",
    "ImportExportServiceDescriptorsItem": ".import_export_service_descriptors_item",
    "ImportExportServiceDescriptorsItemJwtVerifier": ".import_export_service_descriptors_item_jwt_verifier",
    "ImportExportServiceDescriptorsItemSecComSettings": ".import_export_service_descriptors_item_sec_com_settings",
    "ImportExportServiceGroupsItem": ".import_export_service_groups_item",
    "ImportExportSimpleAdminsItem": ".import_export_simple_admins_item",
    "ImportExportStats": ".import_export_stats",
    "InCookie": ".in_cookie",
    "InHeader": ".in_header",
    "InMemoryAuthModuleConfig": ".in_memory_auth_module_config",
    "InMemoryUser": ".in_memory_user",
    "InQueryParam": ".in_query_param",
    "IpFiltering": ".ip_filtering",
    "JwksAlgoSettings": ".jwks_algo_settings",
    "KafkaConfig": ".kafka_config",
    "LargeRequestFaultConfig": ".large_request_fault_config",
    "LargeResponseFaultConfig": ".large_response_fault_config",
    "LatencyInjectionFaultConfig": ".latency_injection_fault_config",
    "LdapAuthModuleConfig": ".ldap_auth_module_config",
    "LdapUser": ".ldap_user",
    "LocalJwtVerifier": ".local_jwt_verifier",
    "LocalJwtVerifierAlgoSettings": ".local_jwt_verifier_algo_settings",
    "LocalJwtVerifierSource": ".local_jwt_verifier_source",
    "LocalJwtVerifierStrategy": ".local_jwt_verifier_strategy",
    "Location": ".location",
    "MailerConsoleExporterConfig": ".mailer_console_exporter_config",
    "MailerConsoleExporterConfigType": ".mailer_console_exporter_config_type",
    "MailerGenericExporterConfig": ".mailer_generic_exporter_config",
    "MailerGenericExporterConfigType": ".mailer_generic_exporter_config_type",
    "MailerMailgunExporterConfig": ".mailer_mailgun_exporter_config",
    "MailerMailgunExporterConfigType": ".mailer_mailgun_exporter_config_type",
    "MailerMailjetExporterConfig": ".mailer_mailjet_exporter_config",
    "MailerMailjetExporterConfigType": ".mailer_mailjet_exporter_config_type",
    "MailerSendgridExporterConfig": ".mailer_sendgrid_exporter_config",
    "MailerSendgridExporterConfigType": ".mailer_sendgrid_exporter_config_type",
    "MailerSettings": ".mailer_settings",
    "MappingSettings": ".mapping_settings",
    "OtoroshiHealth": ".otoroshi_health",
    "OtoroshiHealthDatastore": ".otoroshi_health_datastore",
    "OtoroshiHealthOtoroshi": ".otoroshi_health_otoroshi",
    "Outage": ".outage",
    "OutageStrategy": ".outage_strategy",
    "PassThrough": ".pass_through",
    "Patch": ".patch",
    "PatchItem": ".patch_item",
    "PatchItemOp": ".patch_item_op",
    "PulsarDataExporterConfig": ".pulsar_data_exporter_config",
    "Quotas": ".quotas",
    "RedirectionSettings": ".redirection_settings",
    "RefJwtVerifier": ".ref_jwt_verifier",
    "RsAlgoSettings": ".rs_algo_settings",
    "Script": ".script",
    "ScriptCompilationError": ".script_compilation_error",
    "ScriptCompilationResult": ".script_compilation_result",
    "Service": ".service",
    "ServiceJwtVerifier": ".service_jwt_verifier",
    "ServiceSecComSettings": ".service_sec_com_settings",
    "Sign": ".sign",
    "SignAlgoSettings": ".sign_algo_settings",
    "SimpleAdmin": ".simple_admin",
    "SnowMonkeyConfig": ".snow_monkey_config",
    "Stats": ".stats",
    "StatsdConfig": ".statsd_config",
    "Target": ".target",
    "Transform": ".transform",
    "TransformAlgoSettings": ".transform_algo_settings",
    "TransformSettings": ".transform_settings",
    "TransformSettingsLocation": ".transform_settings_location",
    "U2FAdmin": ".u2f_admin",
    "ValidationAuthority": ".validation_authority",
    "VerificationSettings": ".verification_settings",
    "Webhook": ".webhook",
    "WhebhookConfig": ".whebhook_config",
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
    "ApiKey",
    "Auth0Config",
    "BadResponse",
    "BadResponsesFaultConfig",
    "Canary",
    "Certificate",
    "ChaosConfig",
    "CleverSettings",
    "ClientConfig",
    "ConsoleDataExporterConfig",
    "CorsSettings",
    "CustomDataExporterConfig",
    "DataExporterConfig",
    "DataExporterConfigConfig",
    "DataExporterConfigTyp",
    "Deleted",
    "Done",
    "ElasticConfig",
    "Environment",
    "ErrorTemplate",
    "EsAlgoSettings",
    "ExposedApi",
    "FileDataExporterConfig",
    "Filtering",
    "GenericOauth2ModuleConfig",
    "GenericOauth2ModuleConfigJwtVerifier",
    "GlobalConfig",
    "GlobalJwtVerifier",
    "GlobalJwtVerifierAlgoSettings",
    "GlobalJwtVerifierSource",
    "GlobalJwtVerifierStrategy",
    "Group",
    "Gzip",
    "HealthCheck",
    "HsAlgoSettings",
    "ImportExport",
    "ImportExportAdminsItem",
    "ImportExportApiKeysItem",
    "ImportExportErrorTemplatesItem",
    "ImportExportServiceDescriptorsItem",
    "ImportExportServiceDescriptorsItemJwtVerifier",
    "ImportExportServiceDescriptorsItemSecComSettings",
    "ImportExportServiceGroupsItem",
    "ImportExportSimpleAdminsItem",
    "ImportExportStats",
    "InCookie",
    "InHeader",
    "InMemoryAuthModuleConfig",
    "InMemoryUser",
    "InQueryParam",
    "IpFiltering",
    "JwksAlgoSettings",
    "KafkaConfig",
    "LargeRequestFaultConfig",
    "LargeResponseFaultConfig",
    "LatencyInjectionFaultConfig",
    "LdapAuthModuleConfig",
    "LdapUser",
    "LocalJwtVerifier",
    "LocalJwtVerifierAlgoSettings",
    "LocalJwtVerifierSource",
    "LocalJwtVerifierStrategy",
    "Location",
    "MailerConsoleExporterConfig",
    "MailerConsoleExporterConfigType",
    "MailerGenericExporterConfig",
    "MailerGenericExporterConfigType",
    "MailerMailgunExporterConfig",
    "MailerMailgunExporterConfigType",
    "MailerMailjetExporterConfig",
    "MailerMailjetExporterConfigType",
    "MailerSendgridExporterConfig",
    "MailerSendgridExporterConfigType",
    "MailerSettings",
    "MappingSettings",
    "OtoroshiHealth",
    "OtoroshiHealthDatastore",
    "OtoroshiHealthOtoroshi",
    "Outage",
    "OutageStrategy",
    "PassThrough",
    "Patch",
    "PatchItem",
    "PatchItemOp",
    "PulsarDataExporterConfig",
    "Quotas",
    "RedirectionSettings",
    "RefJwtVerifier",
    "RsAlgoSettings",
    "Script",
    "ScriptCompilationError",
    "ScriptCompilationResult",
    "Service",
    "ServiceJwtVerifier",
    "ServiceSecComSettings",
    "Sign",
    "SignAlgoSettings",
    "SimpleAdmin",
    "SnowMonkeyConfig",
    "Stats",
    "StatsdConfig",
    "Target",
    "Transform",
    "TransformAlgoSettings",
    "TransformSettings",
    "TransformSettingsLocation",
    "U2FAdmin",
    "ValidationAuthority",
    "VerificationSettings",
    "Webhook",
    "WhebhookConfig",
]
