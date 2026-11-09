



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abstract_condition import AbstractCondition
    from .abstract_condition_dto import AbstractConditionDto
    from .alias_mapper_parameters import AliasMapperParameters
    from .array_condition_dto import ArrayConditionDto
    from .array_condition_dto_operator_type import ArrayConditionDtoOperatorType
    from .async_search_status_dto import AsyncSearchStatusDto
    from .async_search_status_dto_search_job_status import AsyncSearchStatusDtoSearchJobStatus
    from .audit_actor_info_dto import AuditActorInfoDto
    from .audit_event_dto import AuditEventDto
    from .audit_event_dto_severity import AuditEventDtoSeverity
    from .cancel_async_search_dto import CancelAsyncSearchDto
    from .cancel_async_search_dto_current_search_job_status import CancelAsyncSearchDtoCurrentSearchJobStatus
    from .cursor_pagination_info_dto import CursorPaginationInfoDto
    from .delete_technical_user200response_dto import DeleteTechnicalUser200ResponseDto
    from .edge_message_dto import EdgeMessageDto
    from .edge_message_header import EdgeMessageHeader
    from .edge_message_meta_data import EdgeMessageMetaData
    from .entity_audit_events_response_dto import EntityAuditEventsResponseDto
    from .entity_audit_events_response_dto_items_item import EntityAuditEventsResponseDtoItemsItem
    from .entity_change_audit_event_dto import EntityChangeAuditEventDto
    from .entity_change_audit_event_dto_change_type import EntityChangeAuditEventDtoChangeType
    from .entity_change_meta import EntityChangeMeta
    from .entity_change_meta_change_type import EntityChangeMetaChangeType
    from .entity_changes_dto import EntityChangesDto
    from .entity_metadata_dto import EntityMetadataDto
    from .entity_model_action_result_dto import EntityModelActionResultDto
    from .entity_model_dto import EntityModelDto
    from .entity_model_key import EntityModelKey
    from .entity_result_dto import EntityResultDto
    from .entity_transaction_response import EntityTransactionResponse
    from .entity_transaction_response_error import EntityTransactionResponseError
    from .entity_transaction_response_failed_item import EntityTransactionResponseFailedItem
    from .entity_transaction_response_failed_item_error import EntityTransactionResponseFailedItemError
    from .error_response import ErrorResponse
    from .error_response_dto import ErrorResponseDto
    from .error_response_dto_error import ErrorResponseDtoError
    from .error_response_error_code import ErrorResponseErrorCode
    from .externalized_function_config_dto import ExternalizedFunctionConfigDto
    from .externalized_function_dto import ExternalizedFunctionDto
    from .externalized_processor_config_dto import ExternalizedProcessorConfigDto
    from .externalized_processor_definition_dto import ExternalizedProcessorDefinitionDto
    from .externalized_processor_definition_dto_execution_mode import ExternalizedProcessorDefinitionDtoExecutionMode
    from .field_config_dto import FieldConfigDto
    from .function_condition_dto import FunctionConditionDto
    from .group_condition_dto import GroupConditionDto
    from .group_condition_dto_conditions_item import GroupConditionDtoConditionsItem
    from .group_condition_dto_operator import GroupConditionDtoOperator
    from .index_configuration_dto import IndexConfigurationDto
    from .index_configuration_dto_decision import IndexConfigurationDtoDecision
    from .invalidate_key_request_dto import InvalidateKeyRequestDto
    from .json_node import JsonNode
    from .jwt_key_pair_response_dto import JwtKeyPairResponseDto
    from .jwt_key_pair_response_dto_algorithm import JwtKeyPairResponseDtoAlgorithm
    from .laureate_dto import LaureateDto
    from .leaf_col_info import LeafColInfo
    from .leaf_col_info_decision import LeafColInfoDecision
    from .leaf_col_info_type import LeafColInfoType
    from .legal_entity_info_dto import LegalEntityInfoDto
    from .lifecycle_condition_dto import LifecycleConditionDto
    from .lifecycle_condition_dto_operator_type import LifecycleConditionDtoOperatorType
    from .local_time import LocalTime
    from .model_state_stats_dto import ModelStateStatsDto
    from .model_stats_dto import ModelStatsDto
    from .oidc_provider_response_dto import OidcProviderResponseDto
    from .page_metadata_dto import PageMetadataDto
    from .paged_entity_results_dto import PagedEntityResultsDto
    from .prize import Prize
    from .problem_detail import ProblemDetail
    from .problem_detail_dto import ProblemDetailDto
    from .processor_definition_dto import ProcessorDefinitionDto
    from .query_condition_dto import QueryConditionDto
    from .query_plan_dto import QueryPlanDto
    from .query_plan_keys_node_dto import QueryPlanKeysNodeDto
    from .query_plan_keys_node_dto_type import QueryPlanKeysNodeDtoType
    from .rejected_transition_criterion_dto import RejectedTransitionCriterionDto
    from .report_alias_def import ReportAliasDef
    from .report_alias_path_def import ReportAliasPathDef
    from .report_col_def import ReportColDef
    from .report_col_part_def import ReportColPartDef
    from .report_column import ReportColumn
    from .report_column_type import ReportColumnType
    from .report_row_container import ReportRowContainer
    from .scheduled_transition_config_dto import ScheduledTransitionConfigDto
    from .scheduled_transition_processor_definition_dto import ScheduledTransitionProcessorDefinitionDto
    from .schema_config_dto import SchemaConfigDto
    from .simple_condition_dto import SimpleConditionDto
    from .simple_condition_dto_operator_type import SimpleConditionDtoOperatorType
    from .single_delete_result import SingleDeleteResult
    from .state_definition_dto import StateDefinitionDto
    from .state_machine_audit_event_dto import StateMachineAuditEventDto
    from .state_machine_audit_event_dto_data import StateMachineAuditEventDtoData
    from .state_machine_audit_event_dto_event_type import StateMachineAuditEventDtoEventType
    from .state_machine_cancelled_dto import StateMachineCancelledDto
    from .state_machine_event_dto import StateMachineEventDto
    from .state_machine_finished_dto import StateMachineFinishedDto
    from .state_machine_forced_success_dto import StateMachineForcedSuccessDto
    from .state_machine_process_criterion_not_matched_dto import StateMachineProcessCriterionNotMatchedDto
    from .state_machine_processing_paused_dto import StateMachineProcessingPausedDto
    from .state_machine_started_dto import StateMachineStartedDto
    from .state_machine_state_process_result_dto import StateMachineStateProcessResultDto
    from .state_machine_state_process_result_dto_state_process_type import (
        StateMachineStateProcessResultDtoStateProcessType,
    )
    from .state_machine_transition_criterion_not_matched_dto import StateMachineTransitionCriterionNotMatchedDto
    from .state_machine_transition_made_dto import StateMachineTransitionMadeDto
    from .state_machine_transition_not_found_dto import StateMachineTransitionNotFoundDto
    from .state_machine_workflow_found_dto import StateMachineWorkflowFoundDto
    from .state_machine_workflow_not_found_dto import StateMachineWorkflowNotFoundDto
    from .state_machine_workflow_skipped_dto import StateMachineWorkflowSkippedDto
    from .state_process_id_dto import StateProcessIdDto
    from .stream_data_config_def import StreamDataConfigDef
    from .stream_data_config_def_container import StreamDataConfigDefContainer
    from .stream_data_def import StreamDataDef
    from .stream_data_delete_result import StreamDataDeleteResult
    from .stream_data_fetch_result import StreamDataFetchResult
    from .stream_data_request import StreamDataRequest
    from .stream_delete_result import StreamDeleteResult
    from .subscription_dto import SubscriptionDto
    from .subscription_limit_dto import SubscriptionLimitDto
    from .subscription_limit_dto_time_interval_bound import SubscriptionLimitDtoTimeIntervalBound
    from .subscriptions_response_dto import SubscriptionsResponseDto
    from .system_audit_event_dto import SystemAuditEventDto
    from .table_config_dto import TableConfigDto
    from .table_operation_stats_dto import TableOperationStatsDto
    from .table_time_stats_dto import TableTimeStatsDto
    from .technical_user_credentials_dto import TechnicalUserCredentialsDto
    from .technical_user_credentials_dto_grant_type import TechnicalUserCredentialsDtoGrantType
    from .technical_user_dto import TechnicalUserDto
    from .time_stat_data_dto import TimeStatDataDto
    from .time_stat_data_dto_measure_desc import TimeStatDataDtoMeasureDesc
    from .token_response_dto import TokenResponseDto
    from .token_response_dto_issued_token_type import TokenResponseDtoIssuedTokenType
    from .token_response_dto_token_type import TokenResponseDtoTokenType
    from .transition_definition_dto import TransitionDefinitionDto
    from .transition_definition_dto_criterion import TransitionDefinitionDtoCriterion
    from .transition_definition_dto_processors_item import TransitionDefinitionDtoProcessorsItem
    from .trusted_key_response_dto import TrustedKeyResponseDto
    from .trusted_key_response_dto_audience import TrustedKeyResponseDtoAudience
    from .user_account_info_dto import UserAccountInfoDto
    from .user_account_info_response_dto import UserAccountInfoResponseDto
    from .user_role_dto import UserRoleDto
    from .value_maps import ValueMaps
    from .value_maps_type_references_value import ValueMapsTypeReferencesValue
    from .value_maps_year_months_value import ValueMapsYearMonthsValue
    from .value_maps_year_months_value_month import ValueMapsYearMonthsValueMonth
    from .value_maps_years_value import ValueMapsYearsValue
    from .workflow_configuration_dto import WorkflowConfigurationDto
    from .workflow_configuration_dto_criterion import WorkflowConfigurationDtoCriterion
    from .workflow_export_response_dto import WorkflowExportResponseDto
    from .workflow_stop_reason_dto import WorkflowStopReasonDto
    from .workflow_stop_reason_dto_type import WorkflowStopReasonDtoType
_dynamic_imports: typing.Dict[str, str] = {
    "AbstractCondition": ".abstract_condition",
    "AbstractConditionDto": ".abstract_condition_dto",
    "AliasMapperParameters": ".alias_mapper_parameters",
    "ArrayConditionDto": ".array_condition_dto",
    "ArrayConditionDtoOperatorType": ".array_condition_dto_operator_type",
    "AsyncSearchStatusDto": ".async_search_status_dto",
    "AsyncSearchStatusDtoSearchJobStatus": ".async_search_status_dto_search_job_status",
    "AuditActorInfoDto": ".audit_actor_info_dto",
    "AuditEventDto": ".audit_event_dto",
    "AuditEventDtoSeverity": ".audit_event_dto_severity",
    "CancelAsyncSearchDto": ".cancel_async_search_dto",
    "CancelAsyncSearchDtoCurrentSearchJobStatus": ".cancel_async_search_dto_current_search_job_status",
    "CursorPaginationInfoDto": ".cursor_pagination_info_dto",
    "DeleteTechnicalUser200ResponseDto": ".delete_technical_user200response_dto",
    "EdgeMessageDto": ".edge_message_dto",
    "EdgeMessageHeader": ".edge_message_header",
    "EdgeMessageMetaData": ".edge_message_meta_data",
    "EntityAuditEventsResponseDto": ".entity_audit_events_response_dto",
    "EntityAuditEventsResponseDtoItemsItem": ".entity_audit_events_response_dto_items_item",
    "EntityChangeAuditEventDto": ".entity_change_audit_event_dto",
    "EntityChangeAuditEventDtoChangeType": ".entity_change_audit_event_dto_change_type",
    "EntityChangeMeta": ".entity_change_meta",
    "EntityChangeMetaChangeType": ".entity_change_meta_change_type",
    "EntityChangesDto": ".entity_changes_dto",
    "EntityMetadataDto": ".entity_metadata_dto",
    "EntityModelActionResultDto": ".entity_model_action_result_dto",
    "EntityModelDto": ".entity_model_dto",
    "EntityModelKey": ".entity_model_key",
    "EntityResultDto": ".entity_result_dto",
    "EntityTransactionResponse": ".entity_transaction_response",
    "EntityTransactionResponseError": ".entity_transaction_response_error",
    "EntityTransactionResponseFailedItem": ".entity_transaction_response_failed_item",
    "EntityTransactionResponseFailedItemError": ".entity_transaction_response_failed_item_error",
    "ErrorResponse": ".error_response",
    "ErrorResponseDto": ".error_response_dto",
    "ErrorResponseDtoError": ".error_response_dto_error",
    "ErrorResponseErrorCode": ".error_response_error_code",
    "ExternalizedFunctionConfigDto": ".externalized_function_config_dto",
    "ExternalizedFunctionDto": ".externalized_function_dto",
    "ExternalizedProcessorConfigDto": ".externalized_processor_config_dto",
    "ExternalizedProcessorDefinitionDto": ".externalized_processor_definition_dto",
    "ExternalizedProcessorDefinitionDtoExecutionMode": ".externalized_processor_definition_dto_execution_mode",
    "FieldConfigDto": ".field_config_dto",
    "FunctionConditionDto": ".function_condition_dto",
    "GroupConditionDto": ".group_condition_dto",
    "GroupConditionDtoConditionsItem": ".group_condition_dto_conditions_item",
    "GroupConditionDtoOperator": ".group_condition_dto_operator",
    "IndexConfigurationDto": ".index_configuration_dto",
    "IndexConfigurationDtoDecision": ".index_configuration_dto_decision",
    "InvalidateKeyRequestDto": ".invalidate_key_request_dto",
    "JsonNode": ".json_node",
    "JwtKeyPairResponseDto": ".jwt_key_pair_response_dto",
    "JwtKeyPairResponseDtoAlgorithm": ".jwt_key_pair_response_dto_algorithm",
    "LaureateDto": ".laureate_dto",
    "LeafColInfo": ".leaf_col_info",
    "LeafColInfoDecision": ".leaf_col_info_decision",
    "LeafColInfoType": ".leaf_col_info_type",
    "LegalEntityInfoDto": ".legal_entity_info_dto",
    "LifecycleConditionDto": ".lifecycle_condition_dto",
    "LifecycleConditionDtoOperatorType": ".lifecycle_condition_dto_operator_type",
    "LocalTime": ".local_time",
    "ModelStateStatsDto": ".model_state_stats_dto",
    "ModelStatsDto": ".model_stats_dto",
    "OidcProviderResponseDto": ".oidc_provider_response_dto",
    "PageMetadataDto": ".page_metadata_dto",
    "PagedEntityResultsDto": ".paged_entity_results_dto",
    "Prize": ".prize",
    "ProblemDetail": ".problem_detail",
    "ProblemDetailDto": ".problem_detail_dto",
    "ProcessorDefinitionDto": ".processor_definition_dto",
    "QueryConditionDto": ".query_condition_dto",
    "QueryPlanDto": ".query_plan_dto",
    "QueryPlanKeysNodeDto": ".query_plan_keys_node_dto",
    "QueryPlanKeysNodeDtoType": ".query_plan_keys_node_dto_type",
    "RejectedTransitionCriterionDto": ".rejected_transition_criterion_dto",
    "ReportAliasDef": ".report_alias_def",
    "ReportAliasPathDef": ".report_alias_path_def",
    "ReportColDef": ".report_col_def",
    "ReportColPartDef": ".report_col_part_def",
    "ReportColumn": ".report_column",
    "ReportColumnType": ".report_column_type",
    "ReportRowContainer": ".report_row_container",
    "ScheduledTransitionConfigDto": ".scheduled_transition_config_dto",
    "ScheduledTransitionProcessorDefinitionDto": ".scheduled_transition_processor_definition_dto",
    "SchemaConfigDto": ".schema_config_dto",
    "SimpleConditionDto": ".simple_condition_dto",
    "SimpleConditionDtoOperatorType": ".simple_condition_dto_operator_type",
    "SingleDeleteResult": ".single_delete_result",
    "StateDefinitionDto": ".state_definition_dto",
    "StateMachineAuditEventDto": ".state_machine_audit_event_dto",
    "StateMachineAuditEventDtoData": ".state_machine_audit_event_dto_data",
    "StateMachineAuditEventDtoEventType": ".state_machine_audit_event_dto_event_type",
    "StateMachineCancelledDto": ".state_machine_cancelled_dto",
    "StateMachineEventDto": ".state_machine_event_dto",
    "StateMachineFinishedDto": ".state_machine_finished_dto",
    "StateMachineForcedSuccessDto": ".state_machine_forced_success_dto",
    "StateMachineProcessCriterionNotMatchedDto": ".state_machine_process_criterion_not_matched_dto",
    "StateMachineProcessingPausedDto": ".state_machine_processing_paused_dto",
    "StateMachineStartedDto": ".state_machine_started_dto",
    "StateMachineStateProcessResultDto": ".state_machine_state_process_result_dto",
    "StateMachineStateProcessResultDtoStateProcessType": ".state_machine_state_process_result_dto_state_process_type",
    "StateMachineTransitionCriterionNotMatchedDto": ".state_machine_transition_criterion_not_matched_dto",
    "StateMachineTransitionMadeDto": ".state_machine_transition_made_dto",
    "StateMachineTransitionNotFoundDto": ".state_machine_transition_not_found_dto",
    "StateMachineWorkflowFoundDto": ".state_machine_workflow_found_dto",
    "StateMachineWorkflowNotFoundDto": ".state_machine_workflow_not_found_dto",
    "StateMachineWorkflowSkippedDto": ".state_machine_workflow_skipped_dto",
    "StateProcessIdDto": ".state_process_id_dto",
    "StreamDataConfigDef": ".stream_data_config_def",
    "StreamDataConfigDefContainer": ".stream_data_config_def_container",
    "StreamDataDef": ".stream_data_def",
    "StreamDataDeleteResult": ".stream_data_delete_result",
    "StreamDataFetchResult": ".stream_data_fetch_result",
    "StreamDataRequest": ".stream_data_request",
    "StreamDeleteResult": ".stream_delete_result",
    "SubscriptionDto": ".subscription_dto",
    "SubscriptionLimitDto": ".subscription_limit_dto",
    "SubscriptionLimitDtoTimeIntervalBound": ".subscription_limit_dto_time_interval_bound",
    "SubscriptionsResponseDto": ".subscriptions_response_dto",
    "SystemAuditEventDto": ".system_audit_event_dto",
    "TableConfigDto": ".table_config_dto",
    "TableOperationStatsDto": ".table_operation_stats_dto",
    "TableTimeStatsDto": ".table_time_stats_dto",
    "TechnicalUserCredentialsDto": ".technical_user_credentials_dto",
    "TechnicalUserCredentialsDtoGrantType": ".technical_user_credentials_dto_grant_type",
    "TechnicalUserDto": ".technical_user_dto",
    "TimeStatDataDto": ".time_stat_data_dto",
    "TimeStatDataDtoMeasureDesc": ".time_stat_data_dto_measure_desc",
    "TokenResponseDto": ".token_response_dto",
    "TokenResponseDtoIssuedTokenType": ".token_response_dto_issued_token_type",
    "TokenResponseDtoTokenType": ".token_response_dto_token_type",
    "TransitionDefinitionDto": ".transition_definition_dto",
    "TransitionDefinitionDtoCriterion": ".transition_definition_dto_criterion",
    "TransitionDefinitionDtoProcessorsItem": ".transition_definition_dto_processors_item",
    "TrustedKeyResponseDto": ".trusted_key_response_dto",
    "TrustedKeyResponseDtoAudience": ".trusted_key_response_dto_audience",
    "UserAccountInfoDto": ".user_account_info_dto",
    "UserAccountInfoResponseDto": ".user_account_info_response_dto",
    "UserRoleDto": ".user_role_dto",
    "ValueMaps": ".value_maps",
    "ValueMapsTypeReferencesValue": ".value_maps_type_references_value",
    "ValueMapsYearMonthsValue": ".value_maps_year_months_value",
    "ValueMapsYearMonthsValueMonth": ".value_maps_year_months_value_month",
    "ValueMapsYearsValue": ".value_maps_years_value",
    "WorkflowConfigurationDto": ".workflow_configuration_dto",
    "WorkflowConfigurationDtoCriterion": ".workflow_configuration_dto_criterion",
    "WorkflowExportResponseDto": ".workflow_export_response_dto",
    "WorkflowStopReasonDto": ".workflow_stop_reason_dto",
    "WorkflowStopReasonDtoType": ".workflow_stop_reason_dto_type",
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
    "AbstractCondition",
    "AbstractConditionDto",
    "AliasMapperParameters",
    "ArrayConditionDto",
    "ArrayConditionDtoOperatorType",
    "AsyncSearchStatusDto",
    "AsyncSearchStatusDtoSearchJobStatus",
    "AuditActorInfoDto",
    "AuditEventDto",
    "AuditEventDtoSeverity",
    "CancelAsyncSearchDto",
    "CancelAsyncSearchDtoCurrentSearchJobStatus",
    "CursorPaginationInfoDto",
    "DeleteTechnicalUser200ResponseDto",
    "EdgeMessageDto",
    "EdgeMessageHeader",
    "EdgeMessageMetaData",
    "EntityAuditEventsResponseDto",
    "EntityAuditEventsResponseDtoItemsItem",
    "EntityChangeAuditEventDto",
    "EntityChangeAuditEventDtoChangeType",
    "EntityChangeMeta",
    "EntityChangeMetaChangeType",
    "EntityChangesDto",
    "EntityMetadataDto",
    "EntityModelActionResultDto",
    "EntityModelDto",
    "EntityModelKey",
    "EntityResultDto",
    "EntityTransactionResponse",
    "EntityTransactionResponseError",
    "EntityTransactionResponseFailedItem",
    "EntityTransactionResponseFailedItemError",
    "ErrorResponse",
    "ErrorResponseDto",
    "ErrorResponseDtoError",
    "ErrorResponseErrorCode",
    "ExternalizedFunctionConfigDto",
    "ExternalizedFunctionDto",
    "ExternalizedProcessorConfigDto",
    "ExternalizedProcessorDefinitionDto",
    "ExternalizedProcessorDefinitionDtoExecutionMode",
    "FieldConfigDto",
    "FunctionConditionDto",
    "GroupConditionDto",
    "GroupConditionDtoConditionsItem",
    "GroupConditionDtoOperator",
    "IndexConfigurationDto",
    "IndexConfigurationDtoDecision",
    "InvalidateKeyRequestDto",
    "JsonNode",
    "JwtKeyPairResponseDto",
    "JwtKeyPairResponseDtoAlgorithm",
    "LaureateDto",
    "LeafColInfo",
    "LeafColInfoDecision",
    "LeafColInfoType",
    "LegalEntityInfoDto",
    "LifecycleConditionDto",
    "LifecycleConditionDtoOperatorType",
    "LocalTime",
    "ModelStateStatsDto",
    "ModelStatsDto",
    "OidcProviderResponseDto",
    "PageMetadataDto",
    "PagedEntityResultsDto",
    "Prize",
    "ProblemDetail",
    "ProblemDetailDto",
    "ProcessorDefinitionDto",
    "QueryConditionDto",
    "QueryPlanDto",
    "QueryPlanKeysNodeDto",
    "QueryPlanKeysNodeDtoType",
    "RejectedTransitionCriterionDto",
    "ReportAliasDef",
    "ReportAliasPathDef",
    "ReportColDef",
    "ReportColPartDef",
    "ReportColumn",
    "ReportColumnType",
    "ReportRowContainer",
    "ScheduledTransitionConfigDto",
    "ScheduledTransitionProcessorDefinitionDto",
    "SchemaConfigDto",
    "SimpleConditionDto",
    "SimpleConditionDtoOperatorType",
    "SingleDeleteResult",
    "StateDefinitionDto",
    "StateMachineAuditEventDto",
    "StateMachineAuditEventDtoData",
    "StateMachineAuditEventDtoEventType",
    "StateMachineCancelledDto",
    "StateMachineEventDto",
    "StateMachineFinishedDto",
    "StateMachineForcedSuccessDto",
    "StateMachineProcessCriterionNotMatchedDto",
    "StateMachineProcessingPausedDto",
    "StateMachineStartedDto",
    "StateMachineStateProcessResultDto",
    "StateMachineStateProcessResultDtoStateProcessType",
    "StateMachineTransitionCriterionNotMatchedDto",
    "StateMachineTransitionMadeDto",
    "StateMachineTransitionNotFoundDto",
    "StateMachineWorkflowFoundDto",
    "StateMachineWorkflowNotFoundDto",
    "StateMachineWorkflowSkippedDto",
    "StateProcessIdDto",
    "StreamDataConfigDef",
    "StreamDataConfigDefContainer",
    "StreamDataDef",
    "StreamDataDeleteResult",
    "StreamDataFetchResult",
    "StreamDataRequest",
    "StreamDeleteResult",
    "SubscriptionDto",
    "SubscriptionLimitDto",
    "SubscriptionLimitDtoTimeIntervalBound",
    "SubscriptionsResponseDto",
    "SystemAuditEventDto",
    "TableConfigDto",
    "TableOperationStatsDto",
    "TableTimeStatsDto",
    "TechnicalUserCredentialsDto",
    "TechnicalUserCredentialsDtoGrantType",
    "TechnicalUserDto",
    "TimeStatDataDto",
    "TimeStatDataDtoMeasureDesc",
    "TokenResponseDto",
    "TokenResponseDtoIssuedTokenType",
    "TokenResponseDtoTokenType",
    "TransitionDefinitionDto",
    "TransitionDefinitionDtoCriterion",
    "TransitionDefinitionDtoProcessorsItem",
    "TrustedKeyResponseDto",
    "TrustedKeyResponseDtoAudience",
    "UserAccountInfoDto",
    "UserAccountInfoResponseDto",
    "UserRoleDto",
    "ValueMaps",
    "ValueMapsTypeReferencesValue",
    "ValueMapsYearMonthsValue",
    "ValueMapsYearMonthsValueMonth",
    "ValueMapsYearsValue",
    "WorkflowConfigurationDto",
    "WorkflowConfigurationDtoCriterion",
    "WorkflowExportResponseDto",
    "WorkflowStopReasonDto",
    "WorkflowStopReasonDtoType",
]
