



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin import Admin
    from .admin_filters import AdminFilters
    from .admin_group_mapping import AdminGroupMapping
    from .admin_group_mapping_options import AdminGroupMappingOptions
    from .admin_permissions import AdminPermissions
    from .admin_preferences import AdminPreferences
    from .admin_profile import AdminProfile
    from .admin_totp_config import AdminTotpConfig
    from .api_key import ApiKey
    from .api_key_scope import ApiKeyScope
    from .api_response import ApiResponse
    from .azure_blob_fs_config import AzureBlobFsConfig
    from .azure_blob_fs_config_access_tier import AzureBlobFsConfigAccessTier
    from .backup_data import BackupData
    from .bandwidth_limit import BandwidthLimit
    from .base_event_action import BaseEventAction
    from .base_event_action_options import BaseEventActionOptions
    from .base_event_rule import BaseEventRule
    from .base_totp_config import BaseTotpConfig
    from .base_user_filters import BaseUserFilters
    from .base_virtual_folder import BaseVirtualFolder
    from .condition_options import ConditionOptions
    from .condition_options_protocols_item import ConditionOptionsProtocolsItem
    from .condition_options_provider_objects_item import ConditionOptionsProviderObjectsItem
    from .condition_pattern import ConditionPattern
    from .connection_status import ConnectionStatus
    from .connection_status_protocol import ConnectionStatusProtocol
    from .crypt_fs_config import CryptFsConfig
    from .data_provider_status import DataProviderStatus
    from .defender_entry import DefenderEntry
    from .dir_entry import DirEntry
    from .dump_data_scopes import DumpDataScopes
    from .event_action import EventAction
    from .event_action_command_config import EventActionCommandConfig
    from .event_action_data_retention_config import EventActionDataRetentionConfig
    from .event_action_email_config import EventActionEmailConfig
    from .event_action_filesystem_config import EventActionFilesystemConfig
    from .event_action_fs_compress import EventActionFsCompress
    from .event_action_http_config import EventActionHttpConfig
    from .event_action_http_config_method import EventActionHttpConfigMethod
    from .event_action_idp_account_check import EventActionIdpAccountCheck
    from .event_action_minimal import EventActionMinimal
    from .event_action_options import EventActionOptions
    from .event_action_password_expiration import EventActionPasswordExpiration
    from .event_action_types import EventActionTypes
    from .event_action_user_inactivity import EventActionUserInactivity
    from .event_conditions import EventConditions
    from .event_conditions_fs_events_item import EventConditionsFsEventsItem
    from .event_conditions_provider_events_item import EventConditionsProviderEventsItem
    from .event_protocols import EventProtocols
    from .event_rule import EventRule
    from .event_rule_minimal import EventRuleMinimal
    from .event_trigger_types import EventTriggerTypes
    from .filesystem_action_types import FilesystemActionTypes
    from .filesystem_config import FilesystemConfig
    from .folder_quota_scan import FolderQuotaScan
    from .folder_retention import FolderRetention
    from .fs_event import FsEvent
    from .fs_event_action import FsEventAction
    from .fs_event_status import FsEventStatus
    from .fs_providers import FsProviders
    from .ftp_passive_port_range import FtpPassivePortRange
    from .ftp_service_status import FtpServiceStatus
    from .ftpd_binding import FtpdBinding
    from .gcs_config import GcsConfig
    from .group import Group
    from .group_mapping import GroupMapping
    from .group_user_settings import GroupUserSettings
    from .hooks_filter import HooksFilter
    from .http_fs_config import HttpFsConfig
    from .http_part import HttpPart
    from .ip_list_entry import IpListEntry
    from .ip_list_mode import IpListMode
    from .ip_list_type import IpListType
    from .key_value import KeyValue
    from .log_event import LogEvent
    from .log_event_type import LogEventType
    from .login_methods import LoginMethods
    from .mfa_protocols import MfaProtocols
    from .mfa_status import MfaStatus
    from .os_fs_config import OsFsConfig
    from .passive_ip_override import PassiveIpOverride
    from .patterns_filter import PatternsFilter
    from .permission import Permission
    from .provider_event import ProviderEvent
    from .provider_event_action import ProviderEventAction
    from .provider_event_object_type import ProviderEventObjectType
    from .pwd_change import PwdChange
    from .quota_scan import QuotaScan
    from .quota_usage import QuotaUsage
    from .recovery_code import RecoveryCode
    from .rename_config import RenameConfig
    from .retention_check import RetentionCheck
    from .role import Role
    from .s3config import S3Config
    from .schedule import Schedule
    from .secret import Secret
    from .secret_status import SecretStatus
    from .services_status import ServicesStatus
    from .services_status_allow_list import ServicesStatusAllowList
    from .services_status_defender import ServicesStatusDefender
    from .services_status_rate_limiters import ServicesStatusRateLimiters
    from .sftp_fs_config import SftpFsConfig
    from .share import Share
    from .share_scope import ShareScope
    from .ssh_authentications import SshAuthentications
    from .ssh_binding import SshBinding
    from .ssh_host_key import SshHostKey
    from .ssh_service_status import SshServiceStatus
    from .supported_protocols import SupportedProtocols
    from .time_period import TimePeriod
    from .tls_versions import TlsVersions
    from .token import Token
    from .totp_config import TotpConfig
    from .totph_mac_algo import TotphMacAlgo
    from .transfer import Transfer
    from .transfer_operation_type import TransferOperationType
    from .user import User
    from .user_filters import UserFilters
    from .user_profile import UserProfile
    from .user_totp_config import UserTotpConfig
    from .user_type import UserType
    from .version_info import VersionInfo
    from .virtual_folder import VirtualFolder
    from .web_client_options import WebClientOptions
    from .web_dav_binding import WebDavBinding
    from .web_dav_service_status import WebDavServiceStatus
_dynamic_imports: typing.Dict[str, str] = {
    "Admin": ".admin",
    "AdminFilters": ".admin_filters",
    "AdminGroupMapping": ".admin_group_mapping",
    "AdminGroupMappingOptions": ".admin_group_mapping_options",
    "AdminPermissions": ".admin_permissions",
    "AdminPreferences": ".admin_preferences",
    "AdminProfile": ".admin_profile",
    "AdminTotpConfig": ".admin_totp_config",
    "ApiKey": ".api_key",
    "ApiKeyScope": ".api_key_scope",
    "ApiResponse": ".api_response",
    "AzureBlobFsConfig": ".azure_blob_fs_config",
    "AzureBlobFsConfigAccessTier": ".azure_blob_fs_config_access_tier",
    "BackupData": ".backup_data",
    "BandwidthLimit": ".bandwidth_limit",
    "BaseEventAction": ".base_event_action",
    "BaseEventActionOptions": ".base_event_action_options",
    "BaseEventRule": ".base_event_rule",
    "BaseTotpConfig": ".base_totp_config",
    "BaseUserFilters": ".base_user_filters",
    "BaseVirtualFolder": ".base_virtual_folder",
    "ConditionOptions": ".condition_options",
    "ConditionOptionsProtocolsItem": ".condition_options_protocols_item",
    "ConditionOptionsProviderObjectsItem": ".condition_options_provider_objects_item",
    "ConditionPattern": ".condition_pattern",
    "ConnectionStatus": ".connection_status",
    "ConnectionStatusProtocol": ".connection_status_protocol",
    "CryptFsConfig": ".crypt_fs_config",
    "DataProviderStatus": ".data_provider_status",
    "DefenderEntry": ".defender_entry",
    "DirEntry": ".dir_entry",
    "DumpDataScopes": ".dump_data_scopes",
    "EventAction": ".event_action",
    "EventActionCommandConfig": ".event_action_command_config",
    "EventActionDataRetentionConfig": ".event_action_data_retention_config",
    "EventActionEmailConfig": ".event_action_email_config",
    "EventActionFilesystemConfig": ".event_action_filesystem_config",
    "EventActionFsCompress": ".event_action_fs_compress",
    "EventActionHttpConfig": ".event_action_http_config",
    "EventActionHttpConfigMethod": ".event_action_http_config_method",
    "EventActionIdpAccountCheck": ".event_action_idp_account_check",
    "EventActionMinimal": ".event_action_minimal",
    "EventActionOptions": ".event_action_options",
    "EventActionPasswordExpiration": ".event_action_password_expiration",
    "EventActionTypes": ".event_action_types",
    "EventActionUserInactivity": ".event_action_user_inactivity",
    "EventConditions": ".event_conditions",
    "EventConditionsFsEventsItem": ".event_conditions_fs_events_item",
    "EventConditionsProviderEventsItem": ".event_conditions_provider_events_item",
    "EventProtocols": ".event_protocols",
    "EventRule": ".event_rule",
    "EventRuleMinimal": ".event_rule_minimal",
    "EventTriggerTypes": ".event_trigger_types",
    "FilesystemActionTypes": ".filesystem_action_types",
    "FilesystemConfig": ".filesystem_config",
    "FolderQuotaScan": ".folder_quota_scan",
    "FolderRetention": ".folder_retention",
    "FsEvent": ".fs_event",
    "FsEventAction": ".fs_event_action",
    "FsEventStatus": ".fs_event_status",
    "FsProviders": ".fs_providers",
    "FtpPassivePortRange": ".ftp_passive_port_range",
    "FtpServiceStatus": ".ftp_service_status",
    "FtpdBinding": ".ftpd_binding",
    "GcsConfig": ".gcs_config",
    "Group": ".group",
    "GroupMapping": ".group_mapping",
    "GroupUserSettings": ".group_user_settings",
    "HooksFilter": ".hooks_filter",
    "HttpFsConfig": ".http_fs_config",
    "HttpPart": ".http_part",
    "IpListEntry": ".ip_list_entry",
    "IpListMode": ".ip_list_mode",
    "IpListType": ".ip_list_type",
    "KeyValue": ".key_value",
    "LogEvent": ".log_event",
    "LogEventType": ".log_event_type",
    "LoginMethods": ".login_methods",
    "MfaProtocols": ".mfa_protocols",
    "MfaStatus": ".mfa_status",
    "OsFsConfig": ".os_fs_config",
    "PassiveIpOverride": ".passive_ip_override",
    "PatternsFilter": ".patterns_filter",
    "Permission": ".permission",
    "ProviderEvent": ".provider_event",
    "ProviderEventAction": ".provider_event_action",
    "ProviderEventObjectType": ".provider_event_object_type",
    "PwdChange": ".pwd_change",
    "QuotaScan": ".quota_scan",
    "QuotaUsage": ".quota_usage",
    "RecoveryCode": ".recovery_code",
    "RenameConfig": ".rename_config",
    "RetentionCheck": ".retention_check",
    "Role": ".role",
    "S3Config": ".s3config",
    "Schedule": ".schedule",
    "Secret": ".secret",
    "SecretStatus": ".secret_status",
    "ServicesStatus": ".services_status",
    "ServicesStatusAllowList": ".services_status_allow_list",
    "ServicesStatusDefender": ".services_status_defender",
    "ServicesStatusRateLimiters": ".services_status_rate_limiters",
    "SftpFsConfig": ".sftp_fs_config",
    "Share": ".share",
    "ShareScope": ".share_scope",
    "SshAuthentications": ".ssh_authentications",
    "SshBinding": ".ssh_binding",
    "SshHostKey": ".ssh_host_key",
    "SshServiceStatus": ".ssh_service_status",
    "SupportedProtocols": ".supported_protocols",
    "TimePeriod": ".time_period",
    "TlsVersions": ".tls_versions",
    "Token": ".token",
    "TotpConfig": ".totp_config",
    "TotphMacAlgo": ".totph_mac_algo",
    "Transfer": ".transfer",
    "TransferOperationType": ".transfer_operation_type",
    "User": ".user",
    "UserFilters": ".user_filters",
    "UserProfile": ".user_profile",
    "UserTotpConfig": ".user_totp_config",
    "UserType": ".user_type",
    "VersionInfo": ".version_info",
    "VirtualFolder": ".virtual_folder",
    "WebClientOptions": ".web_client_options",
    "WebDavBinding": ".web_dav_binding",
    "WebDavServiceStatus": ".web_dav_service_status",
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
    "Admin",
    "AdminFilters",
    "AdminGroupMapping",
    "AdminGroupMappingOptions",
    "AdminPermissions",
    "AdminPreferences",
    "AdminProfile",
    "AdminTotpConfig",
    "ApiKey",
    "ApiKeyScope",
    "ApiResponse",
    "AzureBlobFsConfig",
    "AzureBlobFsConfigAccessTier",
    "BackupData",
    "BandwidthLimit",
    "BaseEventAction",
    "BaseEventActionOptions",
    "BaseEventRule",
    "BaseTotpConfig",
    "BaseUserFilters",
    "BaseVirtualFolder",
    "ConditionOptions",
    "ConditionOptionsProtocolsItem",
    "ConditionOptionsProviderObjectsItem",
    "ConditionPattern",
    "ConnectionStatus",
    "ConnectionStatusProtocol",
    "CryptFsConfig",
    "DataProviderStatus",
    "DefenderEntry",
    "DirEntry",
    "DumpDataScopes",
    "EventAction",
    "EventActionCommandConfig",
    "EventActionDataRetentionConfig",
    "EventActionEmailConfig",
    "EventActionFilesystemConfig",
    "EventActionFsCompress",
    "EventActionHttpConfig",
    "EventActionHttpConfigMethod",
    "EventActionIdpAccountCheck",
    "EventActionMinimal",
    "EventActionOptions",
    "EventActionPasswordExpiration",
    "EventActionTypes",
    "EventActionUserInactivity",
    "EventConditions",
    "EventConditionsFsEventsItem",
    "EventConditionsProviderEventsItem",
    "EventProtocols",
    "EventRule",
    "EventRuleMinimal",
    "EventTriggerTypes",
    "FilesystemActionTypes",
    "FilesystemConfig",
    "FolderQuotaScan",
    "FolderRetention",
    "FsEvent",
    "FsEventAction",
    "FsEventStatus",
    "FsProviders",
    "FtpPassivePortRange",
    "FtpServiceStatus",
    "FtpdBinding",
    "GcsConfig",
    "Group",
    "GroupMapping",
    "GroupUserSettings",
    "HooksFilter",
    "HttpFsConfig",
    "HttpPart",
    "IpListEntry",
    "IpListMode",
    "IpListType",
    "KeyValue",
    "LogEvent",
    "LogEventType",
    "LoginMethods",
    "MfaProtocols",
    "MfaStatus",
    "OsFsConfig",
    "PassiveIpOverride",
    "PatternsFilter",
    "Permission",
    "ProviderEvent",
    "ProviderEventAction",
    "ProviderEventObjectType",
    "PwdChange",
    "QuotaScan",
    "QuotaUsage",
    "RecoveryCode",
    "RenameConfig",
    "RetentionCheck",
    "Role",
    "S3Config",
    "Schedule",
    "Secret",
    "SecretStatus",
    "ServicesStatus",
    "ServicesStatusAllowList",
    "ServicesStatusDefender",
    "ServicesStatusRateLimiters",
    "SftpFsConfig",
    "Share",
    "ShareScope",
    "SshAuthentications",
    "SshBinding",
    "SshHostKey",
    "SshServiceStatus",
    "SupportedProtocols",
    "TimePeriod",
    "TlsVersions",
    "Token",
    "TotpConfig",
    "TotphMacAlgo",
    "Transfer",
    "TransferOperationType",
    "User",
    "UserFilters",
    "UserProfile",
    "UserTotpConfig",
    "UserType",
    "VersionInfo",
    "VirtualFolder",
    "WebClientOptions",
    "WebDavBinding",
    "WebDavServiceStatus",
]
