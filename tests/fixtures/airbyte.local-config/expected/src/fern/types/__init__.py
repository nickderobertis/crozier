



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .actor_catalog_with_updated_at import ActorCatalogWithUpdatedAt
    from .actor_definition_resource_requirements import ActorDefinitionResourceRequirements
    from .advanced_auth import AdvancedAuth
    from .advanced_auth_auth_flow_type import AdvancedAuthAuthFlowType
    from .airbyte_archive import AirbyteArchive
    from .airbyte_catalog import AirbyteCatalog
    from .airbyte_stream import AirbyteStream
    from .airbyte_stream_and_configuration import AirbyteStreamAndConfiguration
    from .airbyte_stream_configuration import AirbyteStreamConfiguration
    from .attempt_failure_origin import AttemptFailureOrigin
    from .attempt_failure_reason import AttemptFailureReason
    from .attempt_failure_summary import AttemptFailureSummary
    from .attempt_failure_type import AttemptFailureType
    from .attempt_info_read import AttemptInfoRead
    from .attempt_normalization_status_read import AttemptNormalizationStatusRead
    from .attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
    from .attempt_number import AttemptNumber
    from .attempt_read import AttemptRead
    from .attempt_stats import AttemptStats
    from .attempt_status import AttemptStatus
    from .attempt_stream_stats import AttemptStreamStats
    from .attempt_sync_config import AttemptSyncConfig
    from .auth_specification import AuthSpecification
    from .auth_specification_auth_type import AuthSpecificationAuthType
    from .catalog_diff import CatalogDiff
    from .check_connection_read import CheckConnectionRead
    from .check_connection_read_status import CheckConnectionReadStatus
    from .check_operation_read import CheckOperationRead
    from .check_operation_read_status import CheckOperationReadStatus
    from .complete_o_auth_response import CompleteOAuthResponse
    from .connection_id import ConnectionId
    from .connection_id_request_body import ConnectionIdRequestBody
    from .connection_read import ConnectionRead
    from .connection_read_list import ConnectionReadList
    from .connection_schedule import ConnectionSchedule
    from .connection_schedule_data import ConnectionScheduleData
    from .connection_schedule_data_basic_schedule import ConnectionScheduleDataBasicSchedule
    from .connection_schedule_data_basic_schedule_time_unit import ConnectionScheduleDataBasicScheduleTimeUnit
    from .connection_schedule_data_cron import ConnectionScheduleDataCron
    from .connection_schedule_time_unit import ConnectionScheduleTimeUnit
    from .connection_schedule_type import ConnectionScheduleType
    from .connection_state import ConnectionState
    from .connection_state_type import ConnectionStateType
    from .connection_status import ConnectionStatus
    from .customer_id import CustomerId
    from .customerio_notification_configuration import CustomerioNotificationConfiguration
    from .data_type import DataType
    from .db_migration_execution_read import DbMigrationExecutionRead
    from .db_migration_read import DbMigrationRead
    from .db_migration_read_list import DbMigrationReadList
    from .db_migration_request_body import DbMigrationRequestBody
    from .db_migration_state import DbMigrationState
    from .destination_auth_specification import DestinationAuthSpecification
    from .destination_clone_configuration import DestinationCloneConfiguration
    from .destination_configuration import DestinationConfiguration
    from .destination_definition_create import DestinationDefinitionCreate
    from .destination_definition_id import DestinationDefinitionId
    from .destination_definition_id_request_body import DestinationDefinitionIdRequestBody
    from .destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
    from .destination_definition_read import DestinationDefinitionRead
    from .destination_definition_read_list import DestinationDefinitionReadList
    from .destination_definition_specification import DestinationDefinitionSpecification
    from .destination_definition_specification_read import DestinationDefinitionSpecificationRead
    from .destination_id import DestinationId
    from .destination_id_request_body import DestinationIdRequestBody
    from .destination_read import DestinationRead
    from .destination_read_list import DestinationReadList
    from .destination_search import DestinationSearch
    from .destination_snippet_read import DestinationSnippetRead
    from .destination_sync_mode import DestinationSyncMode
    from .destination_update import DestinationUpdate
    from .discover_catalog_result import DiscoverCatalogResult
    from .field_add import FieldAdd
    from .field_name import FieldName
    from .field_remove import FieldRemove
    from .field_schema import FieldSchema
    from .field_schema_update import FieldSchemaUpdate
    from .field_transform import FieldTransform
    from .field_transform_transform_type import FieldTransformTransformType
    from .geography import Geography
    from .global_state import GlobalState
    from .health_check_read import HealthCheckRead
    from .import_read import ImportRead
    from .import_read_status import ImportReadStatus
    from .import_request_body import ImportRequestBody
    from .internal_operation_result import InternalOperationResult
    from .invalid_input_exception_info import InvalidInputExceptionInfo
    from .invalid_input_property import InvalidInputProperty
    from .job_config_type import JobConfigType
    from .job_created_at import JobCreatedAt
    from .job_debug_info_read import JobDebugInfoRead
    from .job_debug_read import JobDebugRead
    from .job_id import JobId
    from .job_id_request_body import JobIdRequestBody
    from .job_info_light_read import JobInfoLightRead
    from .job_info_read import JobInfoRead
    from .job_optional_read import JobOptionalRead
    from .job_read import JobRead
    from .job_read_list import JobReadList
    from .job_status import JobStatus
    from .job_type import JobType
    from .job_type_resource_limit import JobTypeResourceLimit
    from .job_with_attempts_read import JobWithAttemptsRead
    from .known_exception_info import KnownExceptionInfo
    from .log_read import LogRead
    from .log_type import LogType
    from .namespace_definition_type import NamespaceDefinitionType
    from .non_breaking_changes_preference import NonBreakingChangesPreference
    from .normalization_destination_definition_config import NormalizationDestinationDefinitionConfig
    from .not_found_known_exception_info import NotFoundKnownExceptionInfo
    from .notification import Notification
    from .notification_read import NotificationRead
    from .notification_read_status import NotificationReadStatus
    from .notification_type import NotificationType
    from .o_auth2specification import OAuth2Specification
    from .o_auth_config_specification import OAuthConfigSpecification
    from .o_auth_configuration import OAuthConfiguration
    from .o_auth_consent_read import OAuthConsentRead
    from .o_auth_input_configuration import OAuthInputConfiguration
    from .operation_create import OperationCreate
    from .operation_id import OperationId
    from .operation_id_request_body import OperationIdRequestBody
    from .operation_read import OperationRead
    from .operation_read_list import OperationReadList
    from .operator_configuration import OperatorConfiguration
    from .operator_dbt import OperatorDbt
    from .operator_normalization import OperatorNormalization
    from .operator_normalization_option import OperatorNormalizationOption
    from .operator_type import OperatorType
    from .operator_webhook import OperatorWebhook
    from .operator_webhook_dbt_cloud import OperatorWebhookDbtCloud
    from .operator_webhook_webhook_type import OperatorWebhookWebhookType
    from .pagination import Pagination
    from .private_destination_definition_read import PrivateDestinationDefinitionRead
    from .private_destination_definition_read_list import PrivateDestinationDefinitionReadList
    from .private_source_definition_read import PrivateSourceDefinitionRead
    from .private_source_definition_read_list import PrivateSourceDefinitionReadList
    from .release_stage import ReleaseStage
    from .reset_config import ResetConfig
    from .resource_id import ResourceId
    from .resource_requirements import ResourceRequirements
    from .schema_change import SchemaChange
    from .selected_field_info import SelectedFieldInfo
    from .slack_notification_configuration import SlackNotificationConfiguration
    from .source_auth_specification import SourceAuthSpecification
    from .source_clone_configuration import SourceCloneConfiguration
    from .source_configuration import SourceConfiguration
    from .source_core_config import SourceCoreConfig
    from .source_definition_create import SourceDefinitionCreate
    from .source_definition_id import SourceDefinitionId
    from .source_definition_id_request_body import SourceDefinitionIdRequestBody
    from .source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
    from .source_definition_read import SourceDefinitionRead
    from .source_definition_read_list import SourceDefinitionReadList
    from .source_definition_read_source_type import SourceDefinitionReadSourceType
    from .source_definition_specification import SourceDefinitionSpecification
    from .source_definition_specification_read import SourceDefinitionSpecificationRead
    from .source_discover_schema_read import SourceDiscoverSchemaRead
    from .source_id import SourceId
    from .source_id_request_body import SourceIdRequestBody
    from .source_read import SourceRead
    from .source_read_list import SourceReadList
    from .source_search import SourceSearch
    from .source_snippet_read import SourceSnippetRead
    from .source_update import SourceUpdate
    from .state_blob import StateBlob
    from .stream_descriptor import StreamDescriptor
    from .stream_json_schema import StreamJsonSchema
    from .stream_state import StreamState
    from .stream_transform import StreamTransform
    from .stream_transform_transform_type import StreamTransformTransformType
    from .sync_mode import SyncMode
    from .synchronous_job_read import SynchronousJobRead
    from .upload_read import UploadRead
    from .upload_read_status import UploadReadStatus
    from .web_backend_check_updates_read import WebBackendCheckUpdatesRead
    from .web_backend_connection_list_item import WebBackendConnectionListItem
    from .web_backend_connection_read import WebBackendConnectionRead
    from .web_backend_connection_read_list import WebBackendConnectionReadList
    from .web_backend_geographies_list_result import WebBackendGeographiesListResult
    from .web_backend_operation_create_or_update import WebBackendOperationCreateOrUpdate
    from .web_backend_workspace_state_result import WebBackendWorkspaceStateResult
    from .webhook_config_read import WebhookConfigRead
    from .webhook_config_write import WebhookConfigWrite
    from .workflow_id import WorkflowId
    from .workflow_state_read import WorkflowStateRead
    from .workspace_id import WorkspaceId
    from .workspace_id_request_body import WorkspaceIdRequestBody
    from .workspace_read import WorkspaceRead
    from .workspace_read_list import WorkspaceReadList
_dynamic_imports: typing.Dict[str, str] = {
    "ActorCatalogWithUpdatedAt": ".actor_catalog_with_updated_at",
    "ActorDefinitionResourceRequirements": ".actor_definition_resource_requirements",
    "AdvancedAuth": ".advanced_auth",
    "AdvancedAuthAuthFlowType": ".advanced_auth_auth_flow_type",
    "AirbyteArchive": ".airbyte_archive",
    "AirbyteCatalog": ".airbyte_catalog",
    "AirbyteStream": ".airbyte_stream",
    "AirbyteStreamAndConfiguration": ".airbyte_stream_and_configuration",
    "AirbyteStreamConfiguration": ".airbyte_stream_configuration",
    "AttemptFailureOrigin": ".attempt_failure_origin",
    "AttemptFailureReason": ".attempt_failure_reason",
    "AttemptFailureSummary": ".attempt_failure_summary",
    "AttemptFailureType": ".attempt_failure_type",
    "AttemptInfoRead": ".attempt_info_read",
    "AttemptNormalizationStatusRead": ".attempt_normalization_status_read",
    "AttemptNormalizationStatusReadList": ".attempt_normalization_status_read_list",
    "AttemptNumber": ".attempt_number",
    "AttemptRead": ".attempt_read",
    "AttemptStats": ".attempt_stats",
    "AttemptStatus": ".attempt_status",
    "AttemptStreamStats": ".attempt_stream_stats",
    "AttemptSyncConfig": ".attempt_sync_config",
    "AuthSpecification": ".auth_specification",
    "AuthSpecificationAuthType": ".auth_specification_auth_type",
    "CatalogDiff": ".catalog_diff",
    "CheckConnectionRead": ".check_connection_read",
    "CheckConnectionReadStatus": ".check_connection_read_status",
    "CheckOperationRead": ".check_operation_read",
    "CheckOperationReadStatus": ".check_operation_read_status",
    "CompleteOAuthResponse": ".complete_o_auth_response",
    "ConnectionId": ".connection_id",
    "ConnectionIdRequestBody": ".connection_id_request_body",
    "ConnectionRead": ".connection_read",
    "ConnectionReadList": ".connection_read_list",
    "ConnectionSchedule": ".connection_schedule",
    "ConnectionScheduleData": ".connection_schedule_data",
    "ConnectionScheduleDataBasicSchedule": ".connection_schedule_data_basic_schedule",
    "ConnectionScheduleDataBasicScheduleTimeUnit": ".connection_schedule_data_basic_schedule_time_unit",
    "ConnectionScheduleDataCron": ".connection_schedule_data_cron",
    "ConnectionScheduleTimeUnit": ".connection_schedule_time_unit",
    "ConnectionScheduleType": ".connection_schedule_type",
    "ConnectionState": ".connection_state",
    "ConnectionStateType": ".connection_state_type",
    "ConnectionStatus": ".connection_status",
    "CustomerId": ".customer_id",
    "CustomerioNotificationConfiguration": ".customerio_notification_configuration",
    "DataType": ".data_type",
    "DbMigrationExecutionRead": ".db_migration_execution_read",
    "DbMigrationRead": ".db_migration_read",
    "DbMigrationReadList": ".db_migration_read_list",
    "DbMigrationRequestBody": ".db_migration_request_body",
    "DbMigrationState": ".db_migration_state",
    "DestinationAuthSpecification": ".destination_auth_specification",
    "DestinationCloneConfiguration": ".destination_clone_configuration",
    "DestinationConfiguration": ".destination_configuration",
    "DestinationDefinitionCreate": ".destination_definition_create",
    "DestinationDefinitionId": ".destination_definition_id",
    "DestinationDefinitionIdRequestBody": ".destination_definition_id_request_body",
    "DestinationDefinitionIdWithWorkspaceId": ".destination_definition_id_with_workspace_id",
    "DestinationDefinitionRead": ".destination_definition_read",
    "DestinationDefinitionReadList": ".destination_definition_read_list",
    "DestinationDefinitionSpecification": ".destination_definition_specification",
    "DestinationDefinitionSpecificationRead": ".destination_definition_specification_read",
    "DestinationId": ".destination_id",
    "DestinationIdRequestBody": ".destination_id_request_body",
    "DestinationRead": ".destination_read",
    "DestinationReadList": ".destination_read_list",
    "DestinationSearch": ".destination_search",
    "DestinationSnippetRead": ".destination_snippet_read",
    "DestinationSyncMode": ".destination_sync_mode",
    "DestinationUpdate": ".destination_update",
    "DiscoverCatalogResult": ".discover_catalog_result",
    "FieldAdd": ".field_add",
    "FieldName": ".field_name",
    "FieldRemove": ".field_remove",
    "FieldSchema": ".field_schema",
    "FieldSchemaUpdate": ".field_schema_update",
    "FieldTransform": ".field_transform",
    "FieldTransformTransformType": ".field_transform_transform_type",
    "Geography": ".geography",
    "GlobalState": ".global_state",
    "HealthCheckRead": ".health_check_read",
    "ImportRead": ".import_read",
    "ImportReadStatus": ".import_read_status",
    "ImportRequestBody": ".import_request_body",
    "InternalOperationResult": ".internal_operation_result",
    "InvalidInputExceptionInfo": ".invalid_input_exception_info",
    "InvalidInputProperty": ".invalid_input_property",
    "JobConfigType": ".job_config_type",
    "JobCreatedAt": ".job_created_at",
    "JobDebugInfoRead": ".job_debug_info_read",
    "JobDebugRead": ".job_debug_read",
    "JobId": ".job_id",
    "JobIdRequestBody": ".job_id_request_body",
    "JobInfoLightRead": ".job_info_light_read",
    "JobInfoRead": ".job_info_read",
    "JobOptionalRead": ".job_optional_read",
    "JobRead": ".job_read",
    "JobReadList": ".job_read_list",
    "JobStatus": ".job_status",
    "JobType": ".job_type",
    "JobTypeResourceLimit": ".job_type_resource_limit",
    "JobWithAttemptsRead": ".job_with_attempts_read",
    "KnownExceptionInfo": ".known_exception_info",
    "LogRead": ".log_read",
    "LogType": ".log_type",
    "NamespaceDefinitionType": ".namespace_definition_type",
    "NonBreakingChangesPreference": ".non_breaking_changes_preference",
    "NormalizationDestinationDefinitionConfig": ".normalization_destination_definition_config",
    "NotFoundKnownExceptionInfo": ".not_found_known_exception_info",
    "Notification": ".notification",
    "NotificationRead": ".notification_read",
    "NotificationReadStatus": ".notification_read_status",
    "NotificationType": ".notification_type",
    "OAuth2Specification": ".o_auth2specification",
    "OAuthConfigSpecification": ".o_auth_config_specification",
    "OAuthConfiguration": ".o_auth_configuration",
    "OAuthConsentRead": ".o_auth_consent_read",
    "OAuthInputConfiguration": ".o_auth_input_configuration",
    "OperationCreate": ".operation_create",
    "OperationId": ".operation_id",
    "OperationIdRequestBody": ".operation_id_request_body",
    "OperationRead": ".operation_read",
    "OperationReadList": ".operation_read_list",
    "OperatorConfiguration": ".operator_configuration",
    "OperatorDbt": ".operator_dbt",
    "OperatorNormalization": ".operator_normalization",
    "OperatorNormalizationOption": ".operator_normalization_option",
    "OperatorType": ".operator_type",
    "OperatorWebhook": ".operator_webhook",
    "OperatorWebhookDbtCloud": ".operator_webhook_dbt_cloud",
    "OperatorWebhookWebhookType": ".operator_webhook_webhook_type",
    "Pagination": ".pagination",
    "PrivateDestinationDefinitionRead": ".private_destination_definition_read",
    "PrivateDestinationDefinitionReadList": ".private_destination_definition_read_list",
    "PrivateSourceDefinitionRead": ".private_source_definition_read",
    "PrivateSourceDefinitionReadList": ".private_source_definition_read_list",
    "ReleaseStage": ".release_stage",
    "ResetConfig": ".reset_config",
    "ResourceId": ".resource_id",
    "ResourceRequirements": ".resource_requirements",
    "SchemaChange": ".schema_change",
    "SelectedFieldInfo": ".selected_field_info",
    "SlackNotificationConfiguration": ".slack_notification_configuration",
    "SourceAuthSpecification": ".source_auth_specification",
    "SourceCloneConfiguration": ".source_clone_configuration",
    "SourceConfiguration": ".source_configuration",
    "SourceCoreConfig": ".source_core_config",
    "SourceDefinitionCreate": ".source_definition_create",
    "SourceDefinitionId": ".source_definition_id",
    "SourceDefinitionIdRequestBody": ".source_definition_id_request_body",
    "SourceDefinitionIdWithWorkspaceId": ".source_definition_id_with_workspace_id",
    "SourceDefinitionRead": ".source_definition_read",
    "SourceDefinitionReadList": ".source_definition_read_list",
    "SourceDefinitionReadSourceType": ".source_definition_read_source_type",
    "SourceDefinitionSpecification": ".source_definition_specification",
    "SourceDefinitionSpecificationRead": ".source_definition_specification_read",
    "SourceDiscoverSchemaRead": ".source_discover_schema_read",
    "SourceId": ".source_id",
    "SourceIdRequestBody": ".source_id_request_body",
    "SourceRead": ".source_read",
    "SourceReadList": ".source_read_list",
    "SourceSearch": ".source_search",
    "SourceSnippetRead": ".source_snippet_read",
    "SourceUpdate": ".source_update",
    "StateBlob": ".state_blob",
    "StreamDescriptor": ".stream_descriptor",
    "StreamJsonSchema": ".stream_json_schema",
    "StreamState": ".stream_state",
    "StreamTransform": ".stream_transform",
    "StreamTransformTransformType": ".stream_transform_transform_type",
    "SyncMode": ".sync_mode",
    "SynchronousJobRead": ".synchronous_job_read",
    "UploadRead": ".upload_read",
    "UploadReadStatus": ".upload_read_status",
    "WebBackendCheckUpdatesRead": ".web_backend_check_updates_read",
    "WebBackendConnectionListItem": ".web_backend_connection_list_item",
    "WebBackendConnectionRead": ".web_backend_connection_read",
    "WebBackendConnectionReadList": ".web_backend_connection_read_list",
    "WebBackendGeographiesListResult": ".web_backend_geographies_list_result",
    "WebBackendOperationCreateOrUpdate": ".web_backend_operation_create_or_update",
    "WebBackendWorkspaceStateResult": ".web_backend_workspace_state_result",
    "WebhookConfigRead": ".webhook_config_read",
    "WebhookConfigWrite": ".webhook_config_write",
    "WorkflowId": ".workflow_id",
    "WorkflowStateRead": ".workflow_state_read",
    "WorkspaceId": ".workspace_id",
    "WorkspaceIdRequestBody": ".workspace_id_request_body",
    "WorkspaceRead": ".workspace_read",
    "WorkspaceReadList": ".workspace_read_list",
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
    "ActorCatalogWithUpdatedAt",
    "ActorDefinitionResourceRequirements",
    "AdvancedAuth",
    "AdvancedAuthAuthFlowType",
    "AirbyteArchive",
    "AirbyteCatalog",
    "AirbyteStream",
    "AirbyteStreamAndConfiguration",
    "AirbyteStreamConfiguration",
    "AttemptFailureOrigin",
    "AttemptFailureReason",
    "AttemptFailureSummary",
    "AttemptFailureType",
    "AttemptInfoRead",
    "AttemptNormalizationStatusRead",
    "AttemptNormalizationStatusReadList",
    "AttemptNumber",
    "AttemptRead",
    "AttemptStats",
    "AttemptStatus",
    "AttemptStreamStats",
    "AttemptSyncConfig",
    "AuthSpecification",
    "AuthSpecificationAuthType",
    "CatalogDiff",
    "CheckConnectionRead",
    "CheckConnectionReadStatus",
    "CheckOperationRead",
    "CheckOperationReadStatus",
    "CompleteOAuthResponse",
    "ConnectionId",
    "ConnectionIdRequestBody",
    "ConnectionRead",
    "ConnectionReadList",
    "ConnectionSchedule",
    "ConnectionScheduleData",
    "ConnectionScheduleDataBasicSchedule",
    "ConnectionScheduleDataBasicScheduleTimeUnit",
    "ConnectionScheduleDataCron",
    "ConnectionScheduleTimeUnit",
    "ConnectionScheduleType",
    "ConnectionState",
    "ConnectionStateType",
    "ConnectionStatus",
    "CustomerId",
    "CustomerioNotificationConfiguration",
    "DataType",
    "DbMigrationExecutionRead",
    "DbMigrationRead",
    "DbMigrationReadList",
    "DbMigrationRequestBody",
    "DbMigrationState",
    "DestinationAuthSpecification",
    "DestinationCloneConfiguration",
    "DestinationConfiguration",
    "DestinationDefinitionCreate",
    "DestinationDefinitionId",
    "DestinationDefinitionIdRequestBody",
    "DestinationDefinitionIdWithWorkspaceId",
    "DestinationDefinitionRead",
    "DestinationDefinitionReadList",
    "DestinationDefinitionSpecification",
    "DestinationDefinitionSpecificationRead",
    "DestinationId",
    "DestinationIdRequestBody",
    "DestinationRead",
    "DestinationReadList",
    "DestinationSearch",
    "DestinationSnippetRead",
    "DestinationSyncMode",
    "DestinationUpdate",
    "DiscoverCatalogResult",
    "FieldAdd",
    "FieldName",
    "FieldRemove",
    "FieldSchema",
    "FieldSchemaUpdate",
    "FieldTransform",
    "FieldTransformTransformType",
    "Geography",
    "GlobalState",
    "HealthCheckRead",
    "ImportRead",
    "ImportReadStatus",
    "ImportRequestBody",
    "InternalOperationResult",
    "InvalidInputExceptionInfo",
    "InvalidInputProperty",
    "JobConfigType",
    "JobCreatedAt",
    "JobDebugInfoRead",
    "JobDebugRead",
    "JobId",
    "JobIdRequestBody",
    "JobInfoLightRead",
    "JobInfoRead",
    "JobOptionalRead",
    "JobRead",
    "JobReadList",
    "JobStatus",
    "JobType",
    "JobTypeResourceLimit",
    "JobWithAttemptsRead",
    "KnownExceptionInfo",
    "LogRead",
    "LogType",
    "NamespaceDefinitionType",
    "NonBreakingChangesPreference",
    "NormalizationDestinationDefinitionConfig",
    "NotFoundKnownExceptionInfo",
    "Notification",
    "NotificationRead",
    "NotificationReadStatus",
    "NotificationType",
    "OAuth2Specification",
    "OAuthConfigSpecification",
    "OAuthConfiguration",
    "OAuthConsentRead",
    "OAuthInputConfiguration",
    "OperationCreate",
    "OperationId",
    "OperationIdRequestBody",
    "OperationRead",
    "OperationReadList",
    "OperatorConfiguration",
    "OperatorDbt",
    "OperatorNormalization",
    "OperatorNormalizationOption",
    "OperatorType",
    "OperatorWebhook",
    "OperatorWebhookDbtCloud",
    "OperatorWebhookWebhookType",
    "Pagination",
    "PrivateDestinationDefinitionRead",
    "PrivateDestinationDefinitionReadList",
    "PrivateSourceDefinitionRead",
    "PrivateSourceDefinitionReadList",
    "ReleaseStage",
    "ResetConfig",
    "ResourceId",
    "ResourceRequirements",
    "SchemaChange",
    "SelectedFieldInfo",
    "SlackNotificationConfiguration",
    "SourceAuthSpecification",
    "SourceCloneConfiguration",
    "SourceConfiguration",
    "SourceCoreConfig",
    "SourceDefinitionCreate",
    "SourceDefinitionId",
    "SourceDefinitionIdRequestBody",
    "SourceDefinitionIdWithWorkspaceId",
    "SourceDefinitionRead",
    "SourceDefinitionReadList",
    "SourceDefinitionReadSourceType",
    "SourceDefinitionSpecification",
    "SourceDefinitionSpecificationRead",
    "SourceDiscoverSchemaRead",
    "SourceId",
    "SourceIdRequestBody",
    "SourceRead",
    "SourceReadList",
    "SourceSearch",
    "SourceSnippetRead",
    "SourceUpdate",
    "StateBlob",
    "StreamDescriptor",
    "StreamJsonSchema",
    "StreamState",
    "StreamTransform",
    "StreamTransformTransformType",
    "SyncMode",
    "SynchronousJobRead",
    "UploadRead",
    "UploadReadStatus",
    "WebBackendCheckUpdatesRead",
    "WebBackendConnectionListItem",
    "WebBackendConnectionRead",
    "WebBackendConnectionReadList",
    "WebBackendGeographiesListResult",
    "WebBackendOperationCreateOrUpdate",
    "WebBackendWorkspaceStateResult",
    "WebhookConfigRead",
    "WebhookConfigWrite",
    "WorkflowId",
    "WorkflowStateRead",
    "WorkspaceId",
    "WorkspaceIdRequestBody",
    "WorkspaceRead",
    "WorkspaceReadList",
]
