



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agent_response import AgentResponse
    from .available_settings_result import AvailableSettingsResult
    from .azure_location import AzureLocation
    from .bill_summary import BillSummary
    from .billable_owner_body import BillableOwnerBody
    from .billable_owner_type import BillableOwnerType
    from .billing_properties import BillingProperties
    from .client_usage_data import ClientUsageData
    from .client_usage_session import ClientUsageSession
    from .cloud_environment_result import CloudEnvironmentResult
    from .cloud_environment_state import CloudEnvironmentState
    from .collected_data import CollectedData
    from .compute_usage_detail import ComputeUsageDetail
    from .connection_info_body import ConnectionInfoBody
    from .consumer_type import ConsumerType
    from .container_info import ContainerInfo
    from .container_info_body import ContainerInfoBody
    from .create_environment_pool_resource_body import CreateEnvironmentPoolResourceBody
    from .create_or_update_pool_body import CreateOrUpdatePoolBody
    from .create_template_result import CreateTemplateResult
    from .delegate_identity import DelegateIdentity
    from .domain_user_credentials import DomainUserCredentials
    from .environment_billing_info import EnvironmentBillingInfo
    from .environment_registration_callback_payload_body import EnvironmentRegistrationCallbackPayloadBody
    from .environment_state_change import EnvironmentStateChange
    from .environment_usage import EnvironmentUsage
    from .experimental_features_body import ExperimentalFeaturesBody
    from .failover_details import FailoverDetails
    from .git_config_options_body import GitConfigOptionsBody
    from .git_status import GitStatus
    from .hot_pool_settings import HotPoolSettings
    from .identity_body import IdentityBody
    from .issue_delegate_plan_access_token_body import IssueDelegatePlanAccessTokenBody
    from .location_info_result import LocationInfoResult
    from .locations_result import LocationsResult
    from .message_codes import MessageCodes
    from .netmon_correlation_data_body import NetmonCorrelationDataBody
    from .network_settings_resource import NetworkSettingsResource
    from .network_settings_resource_list import NetworkSettingsResourceList
    from .network_settings_resource_properties import NetworkSettingsResourceProperties
    from .personalization_info_body import PersonalizationInfoBody
    from .plan_resource import PlanResource
    from .plan_resource_encryption_properties import PlanResourceEncryptionProperties
    from .plan_resource_headers import PlanResourceHeaders
    from .plan_resource_identity import PlanResourceIdentity
    from .plan_resource_key_vault_properties import PlanResourceKeyVaultProperties
    from .plan_resource_list import PlanResourceList
    from .plan_resource_properties import PlanResourceProperties
    from .plan_resource_update_body import PlanResourceUpdateBody
    from .pool import Pool
    from .pool_definition_input import PoolDefinitionInput
    from .pool_group_result import PoolGroupResult
    from .pool_result import PoolResult
    from .pool_settings_body import PoolSettingsBody
    from .pool_status_response_body import PoolStatusResponseBody
    from .prebuild_environment_options import PrebuildEnvironmentOptions
    from .prebuild_mode import PrebuildMode
    from .prebuild_readiness_result import PrebuildReadinessResult
    from .prebuild_template_info import PrebuildTemplateInfo
    from .prebuild_template_info_result import PrebuildTemplateInfoResult
    from .privacy_enum import PrivacyEnum
    from .problem_details import ProblemDetails
    from .profile_specifier import ProfileSpecifier
    from .provisioning_status_result import ProvisioningStatusResult
    from .refresh_profile_telemetry_properties_response import RefreshProfileTelemetryPropertiesResponse
    from .repository_info_body import RepositoryInfoBody
    from .resource_subtype import ResourceSubtype
    from .resource_type import ResourceType
    from .resource_usage_detail import ResourceUsageDetail
    from .rp_subscription_notification import RpSubscriptionNotification
    from .rp_subscription_properties import RpSubscriptionProperties
    from .runtime_constraints_body import RuntimeConstraintsBody
    from .scoped_secret_result_body import ScopedSecretResultBody
    from .secret_data_body import SecretDataBody
    from .secret_filter_body import SecretFilterBody
    from .secret_filter_type import SecretFilterType
    from .secret_scope import SecretScope
    from .secret_type import SecretType
    from .seed_info_body import SeedInfoBody
    from .sku import Sku
    from .sku_info_result import SkuInfoResult
    from .storage_type import StorageType
    from .storage_usage_detail import StorageUsageDetail
    from .string_string_key_value_pair import StringStringKeyValuePair
    from .subscription_account_owner import SubscriptionAccountOwner
    from .subscription_additional_properties import SubscriptionAdditionalProperties
    from .subscription_data import SubscriptionData
    from .system_configuration_response import SystemConfigurationResponse
    from .telemetry_data import TelemetryData
    from .tenant_info_result import TenantInfoResult
    from .tunnel_port_info_result import TunnelPortInfoResult
    from .tunnel_properties import TunnelProperties
    from .tunnel_type import TunnelType
    from .under_investigation_response_body import UnderInvestigationResponseBody
    from .unfiltered_cloud_environment_result import UnfilteredCloudEnvironmentResult
    from .user_identity import UserIdentity
    from .vm_connection_info import VmConnectionInfo
    from .vm_connection_type import VmConnectionType
    from .vm_disk_type import VmDiskType
    from .vm_logs_upload_info import VmLogsUploadInfo
    from .vm_result import VmResult
    from .vm_specs import VmSpecs
    from .vm_status import VmStatus
    from .vnet_properties import VnetProperties
    from .vso_plan_info import VsoPlanInfo
_dynamic_imports: typing.Dict[str, str] = {
    "AgentResponse": ".agent_response",
    "AvailableSettingsResult": ".available_settings_result",
    "AzureLocation": ".azure_location",
    "BillSummary": ".bill_summary",
    "BillableOwnerBody": ".billable_owner_body",
    "BillableOwnerType": ".billable_owner_type",
    "BillingProperties": ".billing_properties",
    "ClientUsageData": ".client_usage_data",
    "ClientUsageSession": ".client_usage_session",
    "CloudEnvironmentResult": ".cloud_environment_result",
    "CloudEnvironmentState": ".cloud_environment_state",
    "CollectedData": ".collected_data",
    "ComputeUsageDetail": ".compute_usage_detail",
    "ConnectionInfoBody": ".connection_info_body",
    "ConsumerType": ".consumer_type",
    "ContainerInfo": ".container_info",
    "ContainerInfoBody": ".container_info_body",
    "CreateEnvironmentPoolResourceBody": ".create_environment_pool_resource_body",
    "CreateOrUpdatePoolBody": ".create_or_update_pool_body",
    "CreateTemplateResult": ".create_template_result",
    "DelegateIdentity": ".delegate_identity",
    "DomainUserCredentials": ".domain_user_credentials",
    "EnvironmentBillingInfo": ".environment_billing_info",
    "EnvironmentRegistrationCallbackPayloadBody": ".environment_registration_callback_payload_body",
    "EnvironmentStateChange": ".environment_state_change",
    "EnvironmentUsage": ".environment_usage",
    "ExperimentalFeaturesBody": ".experimental_features_body",
    "FailoverDetails": ".failover_details",
    "GitConfigOptionsBody": ".git_config_options_body",
    "GitStatus": ".git_status",
    "HotPoolSettings": ".hot_pool_settings",
    "IdentityBody": ".identity_body",
    "IssueDelegatePlanAccessTokenBody": ".issue_delegate_plan_access_token_body",
    "LocationInfoResult": ".location_info_result",
    "LocationsResult": ".locations_result",
    "MessageCodes": ".message_codes",
    "NetmonCorrelationDataBody": ".netmon_correlation_data_body",
    "NetworkSettingsResource": ".network_settings_resource",
    "NetworkSettingsResourceList": ".network_settings_resource_list",
    "NetworkSettingsResourceProperties": ".network_settings_resource_properties",
    "PersonalizationInfoBody": ".personalization_info_body",
    "PlanResource": ".plan_resource",
    "PlanResourceEncryptionProperties": ".plan_resource_encryption_properties",
    "PlanResourceHeaders": ".plan_resource_headers",
    "PlanResourceIdentity": ".plan_resource_identity",
    "PlanResourceKeyVaultProperties": ".plan_resource_key_vault_properties",
    "PlanResourceList": ".plan_resource_list",
    "PlanResourceProperties": ".plan_resource_properties",
    "PlanResourceUpdateBody": ".plan_resource_update_body",
    "Pool": ".pool",
    "PoolDefinitionInput": ".pool_definition_input",
    "PoolGroupResult": ".pool_group_result",
    "PoolResult": ".pool_result",
    "PoolSettingsBody": ".pool_settings_body",
    "PoolStatusResponseBody": ".pool_status_response_body",
    "PrebuildEnvironmentOptions": ".prebuild_environment_options",
    "PrebuildMode": ".prebuild_mode",
    "PrebuildReadinessResult": ".prebuild_readiness_result",
    "PrebuildTemplateInfo": ".prebuild_template_info",
    "PrebuildTemplateInfoResult": ".prebuild_template_info_result",
    "PrivacyEnum": ".privacy_enum",
    "ProblemDetails": ".problem_details",
    "ProfileSpecifier": ".profile_specifier",
    "ProvisioningStatusResult": ".provisioning_status_result",
    "RefreshProfileTelemetryPropertiesResponse": ".refresh_profile_telemetry_properties_response",
    "RepositoryInfoBody": ".repository_info_body",
    "ResourceSubtype": ".resource_subtype",
    "ResourceType": ".resource_type",
    "ResourceUsageDetail": ".resource_usage_detail",
    "RpSubscriptionNotification": ".rp_subscription_notification",
    "RpSubscriptionProperties": ".rp_subscription_properties",
    "RuntimeConstraintsBody": ".runtime_constraints_body",
    "ScopedSecretResultBody": ".scoped_secret_result_body",
    "SecretDataBody": ".secret_data_body",
    "SecretFilterBody": ".secret_filter_body",
    "SecretFilterType": ".secret_filter_type",
    "SecretScope": ".secret_scope",
    "SecretType": ".secret_type",
    "SeedInfoBody": ".seed_info_body",
    "Sku": ".sku",
    "SkuInfoResult": ".sku_info_result",
    "StorageType": ".storage_type",
    "StorageUsageDetail": ".storage_usage_detail",
    "StringStringKeyValuePair": ".string_string_key_value_pair",
    "SubscriptionAccountOwner": ".subscription_account_owner",
    "SubscriptionAdditionalProperties": ".subscription_additional_properties",
    "SubscriptionData": ".subscription_data",
    "SystemConfigurationResponse": ".system_configuration_response",
    "TelemetryData": ".telemetry_data",
    "TenantInfoResult": ".tenant_info_result",
    "TunnelPortInfoResult": ".tunnel_port_info_result",
    "TunnelProperties": ".tunnel_properties",
    "TunnelType": ".tunnel_type",
    "UnderInvestigationResponseBody": ".under_investigation_response_body",
    "UnfilteredCloudEnvironmentResult": ".unfiltered_cloud_environment_result",
    "UserIdentity": ".user_identity",
    "VmConnectionInfo": ".vm_connection_info",
    "VmConnectionType": ".vm_connection_type",
    "VmDiskType": ".vm_disk_type",
    "VmLogsUploadInfo": ".vm_logs_upload_info",
    "VmResult": ".vm_result",
    "VmSpecs": ".vm_specs",
    "VmStatus": ".vm_status",
    "VnetProperties": ".vnet_properties",
    "VsoPlanInfo": ".vso_plan_info",
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
    "AgentResponse",
    "AvailableSettingsResult",
    "AzureLocation",
    "BillSummary",
    "BillableOwnerBody",
    "BillableOwnerType",
    "BillingProperties",
    "ClientUsageData",
    "ClientUsageSession",
    "CloudEnvironmentResult",
    "CloudEnvironmentState",
    "CollectedData",
    "ComputeUsageDetail",
    "ConnectionInfoBody",
    "ConsumerType",
    "ContainerInfo",
    "ContainerInfoBody",
    "CreateEnvironmentPoolResourceBody",
    "CreateOrUpdatePoolBody",
    "CreateTemplateResult",
    "DelegateIdentity",
    "DomainUserCredentials",
    "EnvironmentBillingInfo",
    "EnvironmentRegistrationCallbackPayloadBody",
    "EnvironmentStateChange",
    "EnvironmentUsage",
    "ExperimentalFeaturesBody",
    "FailoverDetails",
    "GitConfigOptionsBody",
    "GitStatus",
    "HotPoolSettings",
    "IdentityBody",
    "IssueDelegatePlanAccessTokenBody",
    "LocationInfoResult",
    "LocationsResult",
    "MessageCodes",
    "NetmonCorrelationDataBody",
    "NetworkSettingsResource",
    "NetworkSettingsResourceList",
    "NetworkSettingsResourceProperties",
    "PersonalizationInfoBody",
    "PlanResource",
    "PlanResourceEncryptionProperties",
    "PlanResourceHeaders",
    "PlanResourceIdentity",
    "PlanResourceKeyVaultProperties",
    "PlanResourceList",
    "PlanResourceProperties",
    "PlanResourceUpdateBody",
    "Pool",
    "PoolDefinitionInput",
    "PoolGroupResult",
    "PoolResult",
    "PoolSettingsBody",
    "PoolStatusResponseBody",
    "PrebuildEnvironmentOptions",
    "PrebuildMode",
    "PrebuildReadinessResult",
    "PrebuildTemplateInfo",
    "PrebuildTemplateInfoResult",
    "PrivacyEnum",
    "ProblemDetails",
    "ProfileSpecifier",
    "ProvisioningStatusResult",
    "RefreshProfileTelemetryPropertiesResponse",
    "RepositoryInfoBody",
    "ResourceSubtype",
    "ResourceType",
    "ResourceUsageDetail",
    "RpSubscriptionNotification",
    "RpSubscriptionProperties",
    "RuntimeConstraintsBody",
    "ScopedSecretResultBody",
    "SecretDataBody",
    "SecretFilterBody",
    "SecretFilterType",
    "SecretScope",
    "SecretType",
    "SeedInfoBody",
    "Sku",
    "SkuInfoResult",
    "StorageType",
    "StorageUsageDetail",
    "StringStringKeyValuePair",
    "SubscriptionAccountOwner",
    "SubscriptionAdditionalProperties",
    "SubscriptionData",
    "SystemConfigurationResponse",
    "TelemetryData",
    "TenantInfoResult",
    "TunnelPortInfoResult",
    "TunnelProperties",
    "TunnelType",
    "UnderInvestigationResponseBody",
    "UnfilteredCloudEnvironmentResult",
    "UserIdentity",
    "VmConnectionInfo",
    "VmConnectionType",
    "VmDiskType",
    "VmLogsUploadInfo",
    "VmResult",
    "VmSpecs",
    "VmStatus",
    "VnetProperties",
    "VsoPlanInfo",
]
