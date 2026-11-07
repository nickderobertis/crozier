



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alert import Alert
    from .alert_alert_source import AlertAlertSource
    from .alert_data_item import AlertDataItem
    from .alert_data_item_alert_source import AlertDataItemAlertSource
    from .alert_data_item_source_type import AlertDataItemSourceType
    from .alert_monitor_type import AlertMonitorType
    from .alert_notifications_item import AlertNotificationsItem
    from .alert_notifications_item_notification_type import AlertNotificationsItemNotificationType
    from .app_uid_list import AppUidList
    from .aws_role_config import AwsRoleConfig
    from .aws_route import AwsRoute
    from .azure_route import AzureRoute
    from .batch_job_requests import BatchJobRequests
    from .billing_account import BillingAccount
    from .billing_account_role import BillingAccountRole
    from .blynk_route import BlynkRoute
    from .cellular_plan import CellularPlan
    from .cellular_usage import CellularUsage
    from .contact import Contact
    from .create_update_repository import CreateUpdateRepository
    from .created_repository import CreatedRepository
    from .current_firmware import CurrentFirmware
    from .data_field import DataField
    from .data_set import DataSet
    from .data_set_field import DataSetField
    from .data_usage import DataUsage
    from .datacake_route import DatacakeRoute
    from .description_record import DescriptionRecord
    from .description_record_list import DescriptionRecordList
    from .device import Device
    from .device_dfu_history import DeviceDfuHistory
    from .device_dfu_history_current import DeviceDfuHistoryCurrent
    from .device_dfu_history_page import DeviceDfuHistoryPage
    from .device_dfu_state_machine import DeviceDfuStateMachine
    from .device_dfu_state_machine_node import DeviceDfuStateMachineNode
    from .device_dfu_status import DeviceDfuStatus
    from .device_dfu_status_current import DeviceDfuStatusCurrent
    from .device_dfu_status_page import DeviceDfuStatusPage
    from .device_session import DeviceSession
    from .device_tower_info import DeviceTowerInfo
    from .device_usage import DeviceUsage
    from .dfu_env import DfuEnv
    from .dfu_state import DfuState
    from .dfu_state_mode import DfuStateMode
    from .dfu_state_type import DfuStateType
    from .email_notification import EmailNotification
    from .empty import Empty
    from .env_tree_json_node import EnvTreeJsonNode
    from .env_var import EnvVar
    from .environment_variables import EnvironmentVariables
    from .error import Error
    from .event import Event
    from .filter import Filter
    from .firmware import Firmware
    from .firmware_info import FirmwareInfo
    from .fleet import Fleet
    from .fleet_connectivity_assurance import FleetConnectivityAssurance
    from .fleet_rule import FleetRule
    from .fleets_uid_list import FleetsUidList
    from .get_project_secrets_response import GetProjectSecretsResponse
    from .google_route import GoogleRoute
    from .http_route import HttpRoute
    from .job import Job
    from .job_definition import JobDefinition
    from .job_definition_report_options import JobDefinitionReportOptions
    from .job_definition_select import JobDefinitionSelect
    from .job_detail import JobDetail
    from .job_run import JobRun
    from .jso_nata import JsoNata
    from .location import Location
    from .monitor import Monitor
    from .monitor_aggregate_function import MonitorAggregateFunction
    from .monitor_alert_routes_item import MonitorAlertRoutesItem
    from .monitor_condition_type import MonitorConditionType
    from .monitor_source_type import MonitorSourceType
    from .mqtt_route import MqttRoute
    from .note import Note
    from .note_input import NoteInput
    from .notefile import Notefile
    from .notefile_list import NotefileList
    from .notefile_schema import NotefileSchema
    from .notehub_route import NotehubRoute
    from .notehub_route_summary import NotehubRouteSummary
    from .o_auth2error import OAuth2Error
    from .o_auth2error_error import OAuth2ErrorError
    from .o_auth2token_response import OAuth2TokenResponse
    from .organization import Organization
    from .organization_role import OrganizationRole
    from .personal_access_token import PersonalAccessToken
    from .personal_access_token_created_by import PersonalAccessTokenCreatedBy
    from .personal_access_token_info import PersonalAccessTokenInfo
    from .personal_access_token_secret import PersonalAccessTokenSecret
    from .product import Product
    from .project import Project
    from .project_member import ProjectMember
    from .project_secret import ProjectSecret
    from .proxy_route import ProxyRoute
    from .qubitro_route import QubitroRoute
    from .rad_route import RadRoute
    from .repository import Repository
    from .repository_list_response import RepositoryListResponse
    from .repository_token_request import RepositoryTokenRequest
    from .repository_token_request_intent import RepositoryTokenRequestIntent
    from .repository_token_response import RepositoryTokenResponse
    from .role import Role
    from .route_log import RouteLog
    from .route_transform_settings import RouteTransformSettings
    from .s3archive_route import S3ArchiveRoute
    from .satellite_data_usage import SatelliteDataUsage
    from .satellite_plan import SatellitePlan
    from .schema_property import SchemaProperty
    from .schema_property_type import SchemaPropertyType
    from .sim_usage import SimUsage
    from .slack_bearer_notification import SlackBearerNotification
    from .slack_bearer_notification_message_type import SlackBearerNotificationMessageType
    from .slack_route import SlackRoute
    from .slack_web_hook_notification import SlackWebHookNotification
    from .slack_web_hook_notification_message_type import SlackWebHookNotificationMessageType
    from .snowflake_route import SnowflakeRoute
    from .snowpipe_streaming_route import SnowpipeStreamingRoute
    from .thingworx_route import ThingworxRoute
    from .tower_location import TowerLocation
    from .twilio_route import TwilioRoute
    from .upload_metadata import UploadMetadata
    from .usage_data import UsageData
    from .usage_events_data import UsageEventsData
    from .usage_events_response import UsageEventsResponse
    from .usage_route_logs_data import UsageRouteLogsData
    from .usage_sessions_data import UsageSessionsData
    from .usage_truncated_field import UsageTruncatedField
    from .user_dfu_state_machine import UserDfuStateMachine
    from .user_dfu_state_machine_status import UserDfuStateMachineStatus
    from .user_firmware_info import UserFirmwareInfo
    from .webhook_settings import WebhookSettings
_dynamic_imports: typing.Dict[str, str] = {
    "Alert": ".alert",
    "AlertAlertSource": ".alert_alert_source",
    "AlertDataItem": ".alert_data_item",
    "AlertDataItemAlertSource": ".alert_data_item_alert_source",
    "AlertDataItemSourceType": ".alert_data_item_source_type",
    "AlertMonitorType": ".alert_monitor_type",
    "AlertNotificationsItem": ".alert_notifications_item",
    "AlertNotificationsItemNotificationType": ".alert_notifications_item_notification_type",
    "AppUidList": ".app_uid_list",
    "AwsRoleConfig": ".aws_role_config",
    "AwsRoute": ".aws_route",
    "AzureRoute": ".azure_route",
    "BatchJobRequests": ".batch_job_requests",
    "BillingAccount": ".billing_account",
    "BillingAccountRole": ".billing_account_role",
    "BlynkRoute": ".blynk_route",
    "CellularPlan": ".cellular_plan",
    "CellularUsage": ".cellular_usage",
    "Contact": ".contact",
    "CreateUpdateRepository": ".create_update_repository",
    "CreatedRepository": ".created_repository",
    "CurrentFirmware": ".current_firmware",
    "DataField": ".data_field",
    "DataSet": ".data_set",
    "DataSetField": ".data_set_field",
    "DataUsage": ".data_usage",
    "DatacakeRoute": ".datacake_route",
    "DescriptionRecord": ".description_record",
    "DescriptionRecordList": ".description_record_list",
    "Device": ".device",
    "DeviceDfuHistory": ".device_dfu_history",
    "DeviceDfuHistoryCurrent": ".device_dfu_history_current",
    "DeviceDfuHistoryPage": ".device_dfu_history_page",
    "DeviceDfuStateMachine": ".device_dfu_state_machine",
    "DeviceDfuStateMachineNode": ".device_dfu_state_machine_node",
    "DeviceDfuStatus": ".device_dfu_status",
    "DeviceDfuStatusCurrent": ".device_dfu_status_current",
    "DeviceDfuStatusPage": ".device_dfu_status_page",
    "DeviceSession": ".device_session",
    "DeviceTowerInfo": ".device_tower_info",
    "DeviceUsage": ".device_usage",
    "DfuEnv": ".dfu_env",
    "DfuState": ".dfu_state",
    "DfuStateMode": ".dfu_state_mode",
    "DfuStateType": ".dfu_state_type",
    "EmailNotification": ".email_notification",
    "Empty": ".empty",
    "EnvTreeJsonNode": ".env_tree_json_node",
    "EnvVar": ".env_var",
    "EnvironmentVariables": ".environment_variables",
    "Error": ".error",
    "Event": ".event",
    "Filter": ".filter",
    "Firmware": ".firmware",
    "FirmwareInfo": ".firmware_info",
    "Fleet": ".fleet",
    "FleetConnectivityAssurance": ".fleet_connectivity_assurance",
    "FleetRule": ".fleet_rule",
    "FleetsUidList": ".fleets_uid_list",
    "GetProjectSecretsResponse": ".get_project_secrets_response",
    "GoogleRoute": ".google_route",
    "HttpRoute": ".http_route",
    "Job": ".job",
    "JobDefinition": ".job_definition",
    "JobDefinitionReportOptions": ".job_definition_report_options",
    "JobDefinitionSelect": ".job_definition_select",
    "JobDetail": ".job_detail",
    "JobRun": ".job_run",
    "JsoNata": ".jso_nata",
    "Location": ".location",
    "Monitor": ".monitor",
    "MonitorAggregateFunction": ".monitor_aggregate_function",
    "MonitorAlertRoutesItem": ".monitor_alert_routes_item",
    "MonitorConditionType": ".monitor_condition_type",
    "MonitorSourceType": ".monitor_source_type",
    "MqttRoute": ".mqtt_route",
    "Note": ".note",
    "NoteInput": ".note_input",
    "Notefile": ".notefile",
    "NotefileList": ".notefile_list",
    "NotefileSchema": ".notefile_schema",
    "NotehubRoute": ".notehub_route",
    "NotehubRouteSummary": ".notehub_route_summary",
    "OAuth2Error": ".o_auth2error",
    "OAuth2ErrorError": ".o_auth2error_error",
    "OAuth2TokenResponse": ".o_auth2token_response",
    "Organization": ".organization",
    "OrganizationRole": ".organization_role",
    "PersonalAccessToken": ".personal_access_token",
    "PersonalAccessTokenCreatedBy": ".personal_access_token_created_by",
    "PersonalAccessTokenInfo": ".personal_access_token_info",
    "PersonalAccessTokenSecret": ".personal_access_token_secret",
    "Product": ".product",
    "Project": ".project",
    "ProjectMember": ".project_member",
    "ProjectSecret": ".project_secret",
    "ProxyRoute": ".proxy_route",
    "QubitroRoute": ".qubitro_route",
    "RadRoute": ".rad_route",
    "Repository": ".repository",
    "RepositoryListResponse": ".repository_list_response",
    "RepositoryTokenRequest": ".repository_token_request",
    "RepositoryTokenRequestIntent": ".repository_token_request_intent",
    "RepositoryTokenResponse": ".repository_token_response",
    "Role": ".role",
    "RouteLog": ".route_log",
    "RouteTransformSettings": ".route_transform_settings",
    "S3ArchiveRoute": ".s3archive_route",
    "SatelliteDataUsage": ".satellite_data_usage",
    "SatellitePlan": ".satellite_plan",
    "SchemaProperty": ".schema_property",
    "SchemaPropertyType": ".schema_property_type",
    "SimUsage": ".sim_usage",
    "SlackBearerNotification": ".slack_bearer_notification",
    "SlackBearerNotificationMessageType": ".slack_bearer_notification_message_type",
    "SlackRoute": ".slack_route",
    "SlackWebHookNotification": ".slack_web_hook_notification",
    "SlackWebHookNotificationMessageType": ".slack_web_hook_notification_message_type",
    "SnowflakeRoute": ".snowflake_route",
    "SnowpipeStreamingRoute": ".snowpipe_streaming_route",
    "ThingworxRoute": ".thingworx_route",
    "TowerLocation": ".tower_location",
    "TwilioRoute": ".twilio_route",
    "UploadMetadata": ".upload_metadata",
    "UsageData": ".usage_data",
    "UsageEventsData": ".usage_events_data",
    "UsageEventsResponse": ".usage_events_response",
    "UsageRouteLogsData": ".usage_route_logs_data",
    "UsageSessionsData": ".usage_sessions_data",
    "UsageTruncatedField": ".usage_truncated_field",
    "UserDfuStateMachine": ".user_dfu_state_machine",
    "UserDfuStateMachineStatus": ".user_dfu_state_machine_status",
    "UserFirmwareInfo": ".user_firmware_info",
    "WebhookSettings": ".webhook_settings",
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
    "Alert",
    "AlertAlertSource",
    "AlertDataItem",
    "AlertDataItemAlertSource",
    "AlertDataItemSourceType",
    "AlertMonitorType",
    "AlertNotificationsItem",
    "AlertNotificationsItemNotificationType",
    "AppUidList",
    "AwsRoleConfig",
    "AwsRoute",
    "AzureRoute",
    "BatchJobRequests",
    "BillingAccount",
    "BillingAccountRole",
    "BlynkRoute",
    "CellularPlan",
    "CellularUsage",
    "Contact",
    "CreateUpdateRepository",
    "CreatedRepository",
    "CurrentFirmware",
    "DataField",
    "DataSet",
    "DataSetField",
    "DataUsage",
    "DatacakeRoute",
    "DescriptionRecord",
    "DescriptionRecordList",
    "Device",
    "DeviceDfuHistory",
    "DeviceDfuHistoryCurrent",
    "DeviceDfuHistoryPage",
    "DeviceDfuStateMachine",
    "DeviceDfuStateMachineNode",
    "DeviceDfuStatus",
    "DeviceDfuStatusCurrent",
    "DeviceDfuStatusPage",
    "DeviceSession",
    "DeviceTowerInfo",
    "DeviceUsage",
    "DfuEnv",
    "DfuState",
    "DfuStateMode",
    "DfuStateType",
    "EmailNotification",
    "Empty",
    "EnvTreeJsonNode",
    "EnvVar",
    "EnvironmentVariables",
    "Error",
    "Event",
    "Filter",
    "Firmware",
    "FirmwareInfo",
    "Fleet",
    "FleetConnectivityAssurance",
    "FleetRule",
    "FleetsUidList",
    "GetProjectSecretsResponse",
    "GoogleRoute",
    "HttpRoute",
    "Job",
    "JobDefinition",
    "JobDefinitionReportOptions",
    "JobDefinitionSelect",
    "JobDetail",
    "JobRun",
    "JsoNata",
    "Location",
    "Monitor",
    "MonitorAggregateFunction",
    "MonitorAlertRoutesItem",
    "MonitorConditionType",
    "MonitorSourceType",
    "MqttRoute",
    "Note",
    "NoteInput",
    "Notefile",
    "NotefileList",
    "NotefileSchema",
    "NotehubRoute",
    "NotehubRouteSummary",
    "OAuth2Error",
    "OAuth2ErrorError",
    "OAuth2TokenResponse",
    "Organization",
    "OrganizationRole",
    "PersonalAccessToken",
    "PersonalAccessTokenCreatedBy",
    "PersonalAccessTokenInfo",
    "PersonalAccessTokenSecret",
    "Product",
    "Project",
    "ProjectMember",
    "ProjectSecret",
    "ProxyRoute",
    "QubitroRoute",
    "RadRoute",
    "Repository",
    "RepositoryListResponse",
    "RepositoryTokenRequest",
    "RepositoryTokenRequestIntent",
    "RepositoryTokenResponse",
    "Role",
    "RouteLog",
    "RouteTransformSettings",
    "S3ArchiveRoute",
    "SatelliteDataUsage",
    "SatellitePlan",
    "SchemaProperty",
    "SchemaPropertyType",
    "SimUsage",
    "SlackBearerNotification",
    "SlackBearerNotificationMessageType",
    "SlackRoute",
    "SlackWebHookNotification",
    "SlackWebHookNotificationMessageType",
    "SnowflakeRoute",
    "SnowpipeStreamingRoute",
    "ThingworxRoute",
    "TowerLocation",
    "TwilioRoute",
    "UploadMetadata",
    "UsageData",
    "UsageEventsData",
    "UsageEventsResponse",
    "UsageRouteLogsData",
    "UsageSessionsData",
    "UsageTruncatedField",
    "UserDfuStateMachine",
    "UserDfuStateMachineStatus",
    "UserFirmwareInfo",
    "WebhookSettings",
]
