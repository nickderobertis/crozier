

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.account import Account
from .types.capability import Capability
from .types.get_activate_type_request_action import GetActivateTypeRequestAction
from .types.get_activate_type_request_logging_config import GetActivateTypeRequestLoggingConfig
from .types.get_activate_type_request_type import GetActivateTypeRequestType
from .types.get_activate_type_request_version import GetActivateTypeRequestVersion
from .types.get_activate_type_request_version_bump import GetActivateTypeRequestVersionBump
from .types.get_batch_describe_type_configurations_request_action import GetBatchDescribeTypeConfigurationsRequestAction
from .types.get_batch_describe_type_configurations_request_version import (
    GetBatchDescribeTypeConfigurationsRequestVersion,
)
from .types.get_cancel_update_stack_request_action import GetCancelUpdateStackRequestAction
from .types.get_cancel_update_stack_request_version import GetCancelUpdateStackRequestVersion
from .types.get_continue_update_rollback_request_action import GetContinueUpdateRollbackRequestAction
from .types.get_continue_update_rollback_request_version import GetContinueUpdateRollbackRequestVersion
from .types.get_create_change_set_request_action import GetCreateChangeSetRequestAction
from .types.get_create_change_set_request_change_set_type import GetCreateChangeSetRequestChangeSetType
from .types.get_create_change_set_request_rollback_configuration import GetCreateChangeSetRequestRollbackConfiguration
from .types.get_create_change_set_request_version import GetCreateChangeSetRequestVersion
from .types.get_create_stack_instances_request_action import GetCreateStackInstancesRequestAction
from .types.get_create_stack_instances_request_call_as import GetCreateStackInstancesRequestCallAs
from .types.get_create_stack_instances_request_deployment_targets import GetCreateStackInstancesRequestDeploymentTargets
from .types.get_create_stack_instances_request_operation_preferences import (
    GetCreateStackInstancesRequestOperationPreferences,
)
from .types.get_create_stack_instances_request_version import GetCreateStackInstancesRequestVersion
from .types.get_create_stack_request_action import GetCreateStackRequestAction
from .types.get_create_stack_request_on_failure import GetCreateStackRequestOnFailure
from .types.get_create_stack_request_rollback_configuration import GetCreateStackRequestRollbackConfiguration
from .types.get_create_stack_request_version import GetCreateStackRequestVersion
from .types.get_create_stack_set_request_action import GetCreateStackSetRequestAction
from .types.get_create_stack_set_request_auto_deployment import GetCreateStackSetRequestAutoDeployment
from .types.get_create_stack_set_request_call_as import GetCreateStackSetRequestCallAs
from .types.get_create_stack_set_request_managed_execution import GetCreateStackSetRequestManagedExecution
from .types.get_create_stack_set_request_permission_model import GetCreateStackSetRequestPermissionModel
from .types.get_create_stack_set_request_version import GetCreateStackSetRequestVersion
from .types.get_deactivate_type_request_action import GetDeactivateTypeRequestAction
from .types.get_deactivate_type_request_type import GetDeactivateTypeRequestType
from .types.get_deactivate_type_request_version import GetDeactivateTypeRequestVersion
from .types.get_delete_change_set_request_action import GetDeleteChangeSetRequestAction
from .types.get_delete_change_set_request_version import GetDeleteChangeSetRequestVersion
from .types.get_delete_stack_instances_request_action import GetDeleteStackInstancesRequestAction
from .types.get_delete_stack_instances_request_call_as import GetDeleteStackInstancesRequestCallAs
from .types.get_delete_stack_instances_request_deployment_targets import GetDeleteStackInstancesRequestDeploymentTargets
from .types.get_delete_stack_instances_request_operation_preferences import (
    GetDeleteStackInstancesRequestOperationPreferences,
)
from .types.get_delete_stack_instances_request_version import GetDeleteStackInstancesRequestVersion
from .types.get_delete_stack_request_action import GetDeleteStackRequestAction
from .types.get_delete_stack_request_version import GetDeleteStackRequestVersion
from .types.get_delete_stack_set_request_action import GetDeleteStackSetRequestAction
from .types.get_delete_stack_set_request_call_as import GetDeleteStackSetRequestCallAs
from .types.get_delete_stack_set_request_version import GetDeleteStackSetRequestVersion
from .types.get_deregister_type_request_action import GetDeregisterTypeRequestAction
from .types.get_deregister_type_request_type import GetDeregisterTypeRequestType
from .types.get_deregister_type_request_version import GetDeregisterTypeRequestVersion
from .types.get_describe_account_limits_request_action import GetDescribeAccountLimitsRequestAction
from .types.get_describe_account_limits_request_version import GetDescribeAccountLimitsRequestVersion
from .types.get_describe_change_set_hooks_request_action import GetDescribeChangeSetHooksRequestAction
from .types.get_describe_change_set_hooks_request_version import GetDescribeChangeSetHooksRequestVersion
from .types.get_describe_change_set_request_action import GetDescribeChangeSetRequestAction
from .types.get_describe_change_set_request_version import GetDescribeChangeSetRequestVersion
from .types.get_describe_publisher_request_action import GetDescribePublisherRequestAction
from .types.get_describe_publisher_request_version import GetDescribePublisherRequestVersion
from .types.get_describe_stack_drift_detection_status_request_action import (
    GetDescribeStackDriftDetectionStatusRequestAction,
)
from .types.get_describe_stack_drift_detection_status_request_version import (
    GetDescribeStackDriftDetectionStatusRequestVersion,
)
from .types.get_describe_stack_events_request_action import GetDescribeStackEventsRequestAction
from .types.get_describe_stack_events_request_version import GetDescribeStackEventsRequestVersion
from .types.get_describe_stack_instance_request_action import GetDescribeStackInstanceRequestAction
from .types.get_describe_stack_instance_request_call_as import GetDescribeStackInstanceRequestCallAs
from .types.get_describe_stack_instance_request_version import GetDescribeStackInstanceRequestVersion
from .types.get_describe_stack_resource_drifts_request_action import GetDescribeStackResourceDriftsRequestAction
from .types.get_describe_stack_resource_drifts_request_version import GetDescribeStackResourceDriftsRequestVersion
from .types.get_describe_stack_resource_request_action import GetDescribeStackResourceRequestAction
from .types.get_describe_stack_resource_request_version import GetDescribeStackResourceRequestVersion
from .types.get_describe_stack_resources_request_action import GetDescribeStackResourcesRequestAction
from .types.get_describe_stack_resources_request_version import GetDescribeStackResourcesRequestVersion
from .types.get_describe_stack_set_operation_request_action import GetDescribeStackSetOperationRequestAction
from .types.get_describe_stack_set_operation_request_call_as import GetDescribeStackSetOperationRequestCallAs
from .types.get_describe_stack_set_operation_request_version import GetDescribeStackSetOperationRequestVersion
from .types.get_describe_stack_set_request_action import GetDescribeStackSetRequestAction
from .types.get_describe_stack_set_request_call_as import GetDescribeStackSetRequestCallAs
from .types.get_describe_stack_set_request_version import GetDescribeStackSetRequestVersion
from .types.get_describe_stacks_request_action import GetDescribeStacksRequestAction
from .types.get_describe_stacks_request_version import GetDescribeStacksRequestVersion
from .types.get_describe_type_registration_request_action import GetDescribeTypeRegistrationRequestAction
from .types.get_describe_type_registration_request_version import GetDescribeTypeRegistrationRequestVersion
from .types.get_describe_type_request_action import GetDescribeTypeRequestAction
from .types.get_describe_type_request_type import GetDescribeTypeRequestType
from .types.get_describe_type_request_version import GetDescribeTypeRequestVersion
from .types.get_detect_stack_drift_request_action import GetDetectStackDriftRequestAction
from .types.get_detect_stack_drift_request_version import GetDetectStackDriftRequestVersion
from .types.get_detect_stack_resource_drift_request_action import GetDetectStackResourceDriftRequestAction
from .types.get_detect_stack_resource_drift_request_version import GetDetectStackResourceDriftRequestVersion
from .types.get_detect_stack_set_drift_request_action import GetDetectStackSetDriftRequestAction
from .types.get_detect_stack_set_drift_request_call_as import GetDetectStackSetDriftRequestCallAs
from .types.get_detect_stack_set_drift_request_operation_preferences import (
    GetDetectStackSetDriftRequestOperationPreferences,
)
from .types.get_detect_stack_set_drift_request_version import GetDetectStackSetDriftRequestVersion
from .types.get_estimate_template_cost_request_action import GetEstimateTemplateCostRequestAction
from .types.get_estimate_template_cost_request_version import GetEstimateTemplateCostRequestVersion
from .types.get_execute_change_set_request_action import GetExecuteChangeSetRequestAction
from .types.get_execute_change_set_request_version import GetExecuteChangeSetRequestVersion
from .types.get_get_stack_policy_request_action import GetGetStackPolicyRequestAction
from .types.get_get_stack_policy_request_version import GetGetStackPolicyRequestVersion
from .types.get_get_template_request_action import GetGetTemplateRequestAction
from .types.get_get_template_request_template_stage import GetGetTemplateRequestTemplateStage
from .types.get_get_template_request_version import GetGetTemplateRequestVersion
from .types.get_get_template_summary_request_action import GetGetTemplateSummaryRequestAction
from .types.get_get_template_summary_request_call_as import GetGetTemplateSummaryRequestCallAs
from .types.get_get_template_summary_request_version import GetGetTemplateSummaryRequestVersion
from .types.get_import_stacks_to_stack_set_request_action import GetImportStacksToStackSetRequestAction
from .types.get_import_stacks_to_stack_set_request_call_as import GetImportStacksToStackSetRequestCallAs
from .types.get_import_stacks_to_stack_set_request_operation_preferences import (
    GetImportStacksToStackSetRequestOperationPreferences,
)
from .types.get_import_stacks_to_stack_set_request_version import GetImportStacksToStackSetRequestVersion
from .types.get_list_change_sets_request_action import GetListChangeSetsRequestAction
from .types.get_list_change_sets_request_version import GetListChangeSetsRequestVersion
from .types.get_list_exports_request_action import GetListExportsRequestAction
from .types.get_list_exports_request_version import GetListExportsRequestVersion
from .types.get_list_imports_request_action import GetListImportsRequestAction
from .types.get_list_imports_request_version import GetListImportsRequestVersion
from .types.get_list_stack_instances_request_action import GetListStackInstancesRequestAction
from .types.get_list_stack_instances_request_call_as import GetListStackInstancesRequestCallAs
from .types.get_list_stack_instances_request_version import GetListStackInstancesRequestVersion
from .types.get_list_stack_resources_request_action import GetListStackResourcesRequestAction
from .types.get_list_stack_resources_request_version import GetListStackResourcesRequestVersion
from .types.get_list_stack_set_operation_results_request_action import GetListStackSetOperationResultsRequestAction
from .types.get_list_stack_set_operation_results_request_call_as import GetListStackSetOperationResultsRequestCallAs
from .types.get_list_stack_set_operation_results_request_version import GetListStackSetOperationResultsRequestVersion
from .types.get_list_stack_set_operations_request_action import GetListStackSetOperationsRequestAction
from .types.get_list_stack_set_operations_request_call_as import GetListStackSetOperationsRequestCallAs
from .types.get_list_stack_set_operations_request_version import GetListStackSetOperationsRequestVersion
from .types.get_list_stack_sets_request_action import GetListStackSetsRequestAction
from .types.get_list_stack_sets_request_call_as import GetListStackSetsRequestCallAs
from .types.get_list_stack_sets_request_status import GetListStackSetsRequestStatus
from .types.get_list_stack_sets_request_version import GetListStackSetsRequestVersion
from .types.get_list_stacks_request_action import GetListStacksRequestAction
from .types.get_list_stacks_request_version import GetListStacksRequestVersion
from .types.get_list_type_registrations_request_action import GetListTypeRegistrationsRequestAction
from .types.get_list_type_registrations_request_registration_status_filter import (
    GetListTypeRegistrationsRequestRegistrationStatusFilter,
)
from .types.get_list_type_registrations_request_type import GetListTypeRegistrationsRequestType
from .types.get_list_type_registrations_request_version import GetListTypeRegistrationsRequestVersion
from .types.get_list_type_versions_request_action import GetListTypeVersionsRequestAction
from .types.get_list_type_versions_request_deprecated_status import GetListTypeVersionsRequestDeprecatedStatus
from .types.get_list_type_versions_request_type import GetListTypeVersionsRequestType
from .types.get_list_type_versions_request_version import GetListTypeVersionsRequestVersion
from .types.get_list_types_request_action import GetListTypesRequestAction
from .types.get_list_types_request_deprecated_status import GetListTypesRequestDeprecatedStatus
from .types.get_list_types_request_filters import GetListTypesRequestFilters
from .types.get_list_types_request_provisioning_type import GetListTypesRequestProvisioningType
from .types.get_list_types_request_type import GetListTypesRequestType
from .types.get_list_types_request_version import GetListTypesRequestVersion
from .types.get_list_types_request_visibility import GetListTypesRequestVisibility
from .types.get_publish_type_request_action import GetPublishTypeRequestAction
from .types.get_publish_type_request_type import GetPublishTypeRequestType
from .types.get_publish_type_request_version import GetPublishTypeRequestVersion
from .types.get_record_handler_progress_request_action import GetRecordHandlerProgressRequestAction
from .types.get_record_handler_progress_request_current_operation_status import (
    GetRecordHandlerProgressRequestCurrentOperationStatus,
)
from .types.get_record_handler_progress_request_error_code import GetRecordHandlerProgressRequestErrorCode
from .types.get_record_handler_progress_request_operation_status import GetRecordHandlerProgressRequestOperationStatus
from .types.get_record_handler_progress_request_version import GetRecordHandlerProgressRequestVersion
from .types.get_register_publisher_request_action import GetRegisterPublisherRequestAction
from .types.get_register_publisher_request_version import GetRegisterPublisherRequestVersion
from .types.get_register_type_request_action import GetRegisterTypeRequestAction
from .types.get_register_type_request_logging_config import GetRegisterTypeRequestLoggingConfig
from .types.get_register_type_request_type import GetRegisterTypeRequestType
from .types.get_register_type_request_version import GetRegisterTypeRequestVersion
from .types.get_rollback_stack_request_action import GetRollbackStackRequestAction
from .types.get_rollback_stack_request_version import GetRollbackStackRequestVersion
from .types.get_set_stack_policy_request_action import GetSetStackPolicyRequestAction
from .types.get_set_stack_policy_request_version import GetSetStackPolicyRequestVersion
from .types.get_set_type_configuration_request_action import GetSetTypeConfigurationRequestAction
from .types.get_set_type_configuration_request_type import GetSetTypeConfigurationRequestType
from .types.get_set_type_configuration_request_version import GetSetTypeConfigurationRequestVersion
from .types.get_set_type_default_version_request_action import GetSetTypeDefaultVersionRequestAction
from .types.get_set_type_default_version_request_type import GetSetTypeDefaultVersionRequestType
from .types.get_set_type_default_version_request_version import GetSetTypeDefaultVersionRequestVersion
from .types.get_signal_resource_request_action import GetSignalResourceRequestAction
from .types.get_signal_resource_request_status import GetSignalResourceRequestStatus
from .types.get_signal_resource_request_version import GetSignalResourceRequestVersion
from .types.get_stop_stack_set_operation_request_action import GetStopStackSetOperationRequestAction
from .types.get_stop_stack_set_operation_request_call_as import GetStopStackSetOperationRequestCallAs
from .types.get_stop_stack_set_operation_request_version import GetStopStackSetOperationRequestVersion
from .types.get_test_type_request_action import GetTestTypeRequestAction
from .types.get_test_type_request_type import GetTestTypeRequestType
from .types.get_test_type_request_version import GetTestTypeRequestVersion
from .types.get_update_stack_instances_request_action import GetUpdateStackInstancesRequestAction
from .types.get_update_stack_instances_request_call_as import GetUpdateStackInstancesRequestCallAs
from .types.get_update_stack_instances_request_deployment_targets import GetUpdateStackInstancesRequestDeploymentTargets
from .types.get_update_stack_instances_request_operation_preferences import (
    GetUpdateStackInstancesRequestOperationPreferences,
)
from .types.get_update_stack_instances_request_version import GetUpdateStackInstancesRequestVersion
from .types.get_update_stack_request_action import GetUpdateStackRequestAction
from .types.get_update_stack_request_rollback_configuration import GetUpdateStackRequestRollbackConfiguration
from .types.get_update_stack_request_version import GetUpdateStackRequestVersion
from .types.get_update_stack_set_request_action import GetUpdateStackSetRequestAction
from .types.get_update_stack_set_request_auto_deployment import GetUpdateStackSetRequestAutoDeployment
from .types.get_update_stack_set_request_call_as import GetUpdateStackSetRequestCallAs
from .types.get_update_stack_set_request_deployment_targets import GetUpdateStackSetRequestDeploymentTargets
from .types.get_update_stack_set_request_managed_execution import GetUpdateStackSetRequestManagedExecution
from .types.get_update_stack_set_request_operation_preferences import GetUpdateStackSetRequestOperationPreferences
from .types.get_update_stack_set_request_permission_model import GetUpdateStackSetRequestPermissionModel
from .types.get_update_stack_set_request_version import GetUpdateStackSetRequestVersion
from .types.get_update_termination_protection_request_action import GetUpdateTerminationProtectionRequestAction
from .types.get_update_termination_protection_request_version import GetUpdateTerminationProtectionRequestVersion
from .types.get_validate_template_request_action import GetValidateTemplateRequestAction
from .types.get_validate_template_request_version import GetValidateTemplateRequestVersion
from .types.logical_resource_id import LogicalResourceId
from .types.notification_arn import NotificationArn
from .types.operation_result_filter import OperationResultFilter
from .types.organizational_unit_id import OrganizationalUnitId
from .types.parameter import Parameter
from .types.post_activate_type_request_action import PostActivateTypeRequestAction
from .types.post_activate_type_request_version import PostActivateTypeRequestVersion
from .types.post_batch_describe_type_configurations_request_action import (
    PostBatchDescribeTypeConfigurationsRequestAction,
)
from .types.post_batch_describe_type_configurations_request_version import (
    PostBatchDescribeTypeConfigurationsRequestVersion,
)
from .types.post_cancel_update_stack_request_action import PostCancelUpdateStackRequestAction
from .types.post_cancel_update_stack_request_version import PostCancelUpdateStackRequestVersion
from .types.post_continue_update_rollback_request_action import PostContinueUpdateRollbackRequestAction
from .types.post_continue_update_rollback_request_version import PostContinueUpdateRollbackRequestVersion
from .types.post_create_change_set_request_action import PostCreateChangeSetRequestAction
from .types.post_create_change_set_request_version import PostCreateChangeSetRequestVersion
from .types.post_create_stack_instances_request_action import PostCreateStackInstancesRequestAction
from .types.post_create_stack_instances_request_version import PostCreateStackInstancesRequestVersion
from .types.post_create_stack_request_action import PostCreateStackRequestAction
from .types.post_create_stack_request_version import PostCreateStackRequestVersion
from .types.post_create_stack_set_request_action import PostCreateStackSetRequestAction
from .types.post_create_stack_set_request_version import PostCreateStackSetRequestVersion
from .types.post_deactivate_type_request_action import PostDeactivateTypeRequestAction
from .types.post_deactivate_type_request_version import PostDeactivateTypeRequestVersion
from .types.post_delete_change_set_request_action import PostDeleteChangeSetRequestAction
from .types.post_delete_change_set_request_version import PostDeleteChangeSetRequestVersion
from .types.post_delete_stack_instances_request_action import PostDeleteStackInstancesRequestAction
from .types.post_delete_stack_instances_request_version import PostDeleteStackInstancesRequestVersion
from .types.post_delete_stack_request_action import PostDeleteStackRequestAction
from .types.post_delete_stack_request_version import PostDeleteStackRequestVersion
from .types.post_delete_stack_set_request_action import PostDeleteStackSetRequestAction
from .types.post_delete_stack_set_request_version import PostDeleteStackSetRequestVersion
from .types.post_deregister_type_request_action import PostDeregisterTypeRequestAction
from .types.post_deregister_type_request_version import PostDeregisterTypeRequestVersion
from .types.post_describe_account_limits_request_action import PostDescribeAccountLimitsRequestAction
from .types.post_describe_account_limits_request_version import PostDescribeAccountLimitsRequestVersion
from .types.post_describe_change_set_hooks_request_action import PostDescribeChangeSetHooksRequestAction
from .types.post_describe_change_set_hooks_request_version import PostDescribeChangeSetHooksRequestVersion
from .types.post_describe_change_set_request_action import PostDescribeChangeSetRequestAction
from .types.post_describe_change_set_request_version import PostDescribeChangeSetRequestVersion
from .types.post_describe_publisher_request_action import PostDescribePublisherRequestAction
from .types.post_describe_publisher_request_version import PostDescribePublisherRequestVersion
from .types.post_describe_stack_drift_detection_status_request_action import (
    PostDescribeStackDriftDetectionStatusRequestAction,
)
from .types.post_describe_stack_drift_detection_status_request_version import (
    PostDescribeStackDriftDetectionStatusRequestVersion,
)
from .types.post_describe_stack_events_request_action import PostDescribeStackEventsRequestAction
from .types.post_describe_stack_events_request_version import PostDescribeStackEventsRequestVersion
from .types.post_describe_stack_instance_request_action import PostDescribeStackInstanceRequestAction
from .types.post_describe_stack_instance_request_version import PostDescribeStackInstanceRequestVersion
from .types.post_describe_stack_resource_drifts_request_action import PostDescribeStackResourceDriftsRequestAction
from .types.post_describe_stack_resource_drifts_request_version import PostDescribeStackResourceDriftsRequestVersion
from .types.post_describe_stack_resource_request_action import PostDescribeStackResourceRequestAction
from .types.post_describe_stack_resource_request_version import PostDescribeStackResourceRequestVersion
from .types.post_describe_stack_resources_request_action import PostDescribeStackResourcesRequestAction
from .types.post_describe_stack_resources_request_version import PostDescribeStackResourcesRequestVersion
from .types.post_describe_stack_set_operation_request_action import PostDescribeStackSetOperationRequestAction
from .types.post_describe_stack_set_operation_request_version import PostDescribeStackSetOperationRequestVersion
from .types.post_describe_stack_set_request_action import PostDescribeStackSetRequestAction
from .types.post_describe_stack_set_request_version import PostDescribeStackSetRequestVersion
from .types.post_describe_stacks_request_action import PostDescribeStacksRequestAction
from .types.post_describe_stacks_request_version import PostDescribeStacksRequestVersion
from .types.post_describe_type_registration_request_action import PostDescribeTypeRegistrationRequestAction
from .types.post_describe_type_registration_request_version import PostDescribeTypeRegistrationRequestVersion
from .types.post_describe_type_request_action import PostDescribeTypeRequestAction
from .types.post_describe_type_request_version import PostDescribeTypeRequestVersion
from .types.post_detect_stack_drift_request_action import PostDetectStackDriftRequestAction
from .types.post_detect_stack_drift_request_version import PostDetectStackDriftRequestVersion
from .types.post_detect_stack_resource_drift_request_action import PostDetectStackResourceDriftRequestAction
from .types.post_detect_stack_resource_drift_request_version import PostDetectStackResourceDriftRequestVersion
from .types.post_detect_stack_set_drift_request_action import PostDetectStackSetDriftRequestAction
from .types.post_detect_stack_set_drift_request_version import PostDetectStackSetDriftRequestVersion
from .types.post_estimate_template_cost_request_action import PostEstimateTemplateCostRequestAction
from .types.post_estimate_template_cost_request_version import PostEstimateTemplateCostRequestVersion
from .types.post_execute_change_set_request_action import PostExecuteChangeSetRequestAction
from .types.post_execute_change_set_request_version import PostExecuteChangeSetRequestVersion
from .types.post_get_stack_policy_request_action import PostGetStackPolicyRequestAction
from .types.post_get_stack_policy_request_version import PostGetStackPolicyRequestVersion
from .types.post_get_template_request_action import PostGetTemplateRequestAction
from .types.post_get_template_request_version import PostGetTemplateRequestVersion
from .types.post_get_template_summary_request_action import PostGetTemplateSummaryRequestAction
from .types.post_get_template_summary_request_version import PostGetTemplateSummaryRequestVersion
from .types.post_import_stacks_to_stack_set_request_action import PostImportStacksToStackSetRequestAction
from .types.post_import_stacks_to_stack_set_request_version import PostImportStacksToStackSetRequestVersion
from .types.post_list_change_sets_request_action import PostListChangeSetsRequestAction
from .types.post_list_change_sets_request_version import PostListChangeSetsRequestVersion
from .types.post_list_exports_request_action import PostListExportsRequestAction
from .types.post_list_exports_request_version import PostListExportsRequestVersion
from .types.post_list_imports_request_action import PostListImportsRequestAction
from .types.post_list_imports_request_version import PostListImportsRequestVersion
from .types.post_list_stack_instances_request_action import PostListStackInstancesRequestAction
from .types.post_list_stack_instances_request_version import PostListStackInstancesRequestVersion
from .types.post_list_stack_resources_request_action import PostListStackResourcesRequestAction
from .types.post_list_stack_resources_request_version import PostListStackResourcesRequestVersion
from .types.post_list_stack_set_operation_results_request_action import PostListStackSetOperationResultsRequestAction
from .types.post_list_stack_set_operation_results_request_version import PostListStackSetOperationResultsRequestVersion
from .types.post_list_stack_set_operations_request_action import PostListStackSetOperationsRequestAction
from .types.post_list_stack_set_operations_request_version import PostListStackSetOperationsRequestVersion
from .types.post_list_stack_sets_request_action import PostListStackSetsRequestAction
from .types.post_list_stack_sets_request_version import PostListStackSetsRequestVersion
from .types.post_list_stacks_request_action import PostListStacksRequestAction
from .types.post_list_stacks_request_version import PostListStacksRequestVersion
from .types.post_list_type_registrations_request_action import PostListTypeRegistrationsRequestAction
from .types.post_list_type_registrations_request_version import PostListTypeRegistrationsRequestVersion
from .types.post_list_type_versions_request_action import PostListTypeVersionsRequestAction
from .types.post_list_type_versions_request_version import PostListTypeVersionsRequestVersion
from .types.post_list_types_request_action import PostListTypesRequestAction
from .types.post_list_types_request_version import PostListTypesRequestVersion
from .types.post_publish_type_request_action import PostPublishTypeRequestAction
from .types.post_publish_type_request_version import PostPublishTypeRequestVersion
from .types.post_record_handler_progress_request_action import PostRecordHandlerProgressRequestAction
from .types.post_record_handler_progress_request_version import PostRecordHandlerProgressRequestVersion
from .types.post_register_publisher_request_action import PostRegisterPublisherRequestAction
from .types.post_register_publisher_request_version import PostRegisterPublisherRequestVersion
from .types.post_register_type_request_action import PostRegisterTypeRequestAction
from .types.post_register_type_request_version import PostRegisterTypeRequestVersion
from .types.post_rollback_stack_request_action import PostRollbackStackRequestAction
from .types.post_rollback_stack_request_version import PostRollbackStackRequestVersion
from .types.post_set_stack_policy_request_action import PostSetStackPolicyRequestAction
from .types.post_set_stack_policy_request_version import PostSetStackPolicyRequestVersion
from .types.post_set_type_configuration_request_action import PostSetTypeConfigurationRequestAction
from .types.post_set_type_configuration_request_version import PostSetTypeConfigurationRequestVersion
from .types.post_set_type_default_version_request_action import PostSetTypeDefaultVersionRequestAction
from .types.post_set_type_default_version_request_version import PostSetTypeDefaultVersionRequestVersion
from .types.post_signal_resource_request_action import PostSignalResourceRequestAction
from .types.post_signal_resource_request_version import PostSignalResourceRequestVersion
from .types.post_stop_stack_set_operation_request_action import PostStopStackSetOperationRequestAction
from .types.post_stop_stack_set_operation_request_version import PostStopStackSetOperationRequestVersion
from .types.post_test_type_request_action import PostTestTypeRequestAction
from .types.post_test_type_request_version import PostTestTypeRequestVersion
from .types.post_update_stack_instances_request_action import PostUpdateStackInstancesRequestAction
from .types.post_update_stack_instances_request_version import PostUpdateStackInstancesRequestVersion
from .types.post_update_stack_request_action import PostUpdateStackRequestAction
from .types.post_update_stack_request_version import PostUpdateStackRequestVersion
from .types.post_update_stack_set_request_action import PostUpdateStackSetRequestAction
from .types.post_update_stack_set_request_version import PostUpdateStackSetRequestVersion
from .types.post_update_termination_protection_request_action import PostUpdateTerminationProtectionRequestAction
from .types.post_update_termination_protection_request_version import PostUpdateTerminationProtectionRequestVersion
from .types.post_validate_template_request_action import PostValidateTemplateRequestAction
from .types.post_validate_template_request_version import PostValidateTemplateRequestVersion
from .types.region import Region
from .types.resource_to_import import ResourceToImport
from .types.resource_to_skip import ResourceToSkip
from .types.resource_type import ResourceType
from .types.stack_id import StackId
from .types.stack_instance_filter import StackInstanceFilter
from .types.stack_resource_drift_status import StackResourceDriftStatus
from .types.stack_status import StackStatus
from .types.tag import Tag
from .types.type_configuration_identifier import TypeConfigurationIdentifier
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_activate_type(
        self,
        *,
        action: GetActivateTypeRequestAction,
        version: GetActivateTypeRequestVersion,
        type: typing.Optional[GetActivateTypeRequestType] = None,
        public_type_arn: typing.Optional[str] = None,
        publisher_id: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        type_name_alias: typing.Optional[str] = None,
        auto_update: typing.Optional[bool] = None,
        logging_config: typing.Optional[GetActivateTypeRequestLoggingConfig] = None,
        execution_role_arn: typing.Optional[str] = None,
        version_bump: typing.Optional[GetActivateTypeRequestVersionBump] = None,
        major_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : GetActivateTypeRequestAction

        version : GetActivateTypeRequestVersion

        type : typing.Optional[GetActivateTypeRequestType]
            <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        public_type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        publisher_id : typing.Optional[str]
            <p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        type_name_alias : typing.Optional[str]
            <p>An alias to assign to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and region. You can activate the same public resource multiple times in the same account and region, using different type name aliases.</p>

        auto_update : typing.Optional[bool]
            <p>Whether to automatically update the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>

        logging_config : typing.Optional[GetActivateTypeRequestLoggingConfig]


        execution_role_arn : typing.Optional[str]
            The name of the IAM execution role to use to activate the extension.

        version_bump : typing.Optional[GetActivateTypeRequestVersionBump]
            <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>

        major_version : typing.Optional[int]
            <p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ActivateType",
            method="GET",
            params={
                "Type": type,
                "PublicTypeArn": public_type_arn,
                "PublisherId": publisher_id,
                "TypeName": type_name,
                "TypeNameAlias": type_name_alias,
                "AutoUpdate": auto_update,
                "LoggingConfig": convert_and_respect_annotation_metadata(
                    object_=logging_config, annotation=GetActivateTypeRequestLoggingConfig, direction="write"
                ),
                "ExecutionRoleArn": execution_role_arn,
                "VersionBump": version_bump,
                "MajorVersion": major_version,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_activate_type(
        self,
        *,
        action: PostActivateTypeRequestAction,
        version: PostActivateTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostActivateTypeRequestAction

        version : PostActivateTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ActivateType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_batch_describe_type_configurations(
        self,
        *,
        action: GetBatchDescribeTypeConfigurationsRequestAction,
        version: GetBatchDescribeTypeConfigurationsRequestVersion,
        type_configuration_identifiers: typing.Optional[
            typing.Union[TypeConfigurationIdentifier, typing.Sequence[TypeConfigurationIdentifier]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : GetBatchDescribeTypeConfigurationsRequestAction

        version : GetBatchDescribeTypeConfigurationsRequestVersion

        type_configuration_identifiers : typing.Optional[typing.Union[TypeConfigurationIdentifier, typing.Sequence[TypeConfigurationIdentifier]]]
            The list of identifiers for the desired extension configurations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=BatchDescribeTypeConfigurations",
            method="GET",
            params={
                "TypeConfigurationIdentifiers": convert_and_respect_annotation_metadata(
                    object_=type_configuration_identifiers, annotation=TypeConfigurationIdentifier, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_batch_describe_type_configurations(
        self,
        *,
        action: PostBatchDescribeTypeConfigurationsRequestAction,
        version: PostBatchDescribeTypeConfigurationsRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostBatchDescribeTypeConfigurationsRequestAction

        version : PostBatchDescribeTypeConfigurationsRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=BatchDescribeTypeConfigurations",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_cancel_update_stack(
        self,
        *,
        stack_name: str,
        action: GetCancelUpdateStackRequestAction,
        version: GetCancelUpdateStackRequestVersion,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        <p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>

        Parameters
        ----------
        stack_name : str
            The name or the unique stack ID that's associated with the stack.

        action : GetCancelUpdateStackRequestAction

        version : GetCancelUpdateStackRequestVersion

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CancelUpdateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_cancel_update_stack(
        self,
        *,
        action: PostCancelUpdateStackRequestAction,
        version: PostCancelUpdateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        <p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>

        Parameters
        ----------
        action : PostCancelUpdateStackRequestAction

        version : PostCancelUpdateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CancelUpdateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_continue_update_rollback(
        self,
        *,
        stack_name: str,
        action: GetContinueUpdateRollbackRequestAction,
        version: GetContinueUpdateRollbackRequestVersion,
        role_arn: typing.Optional[str] = None,
        resources_to_skip: typing.Optional[typing.Union[ResourceToSkip, typing.Sequence[ResourceToSkip]]] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique ID of the stack that you want to continue rolling back.</p> <note> <p>Don't specify the name of a nested stack (a stack that was created by using the <code>AWS::CloudFormation::Stack</code> resource). Instead, use this operation on the parent stack (the stack that contains the <code>AWS::CloudFormation::Stack</code> resource).</p> </note>

        action : GetContinueUpdateRollbackRequestAction

        version : GetContinueUpdateRollbackRequestVersion

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to roll back the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        resources_to_skip : typing.Optional[typing.Union[ResourceToSkip, typing.Sequence[ResourceToSkip]]]
            <p>A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the <code>UPDATE_FAILED</code> state because a rollback failed. You can't specify resources that are in the <code>UPDATE_FAILED</code> state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the <a>DescribeStackResources</a> action, and view the resource status reason.</p> <important> <p>Specify this property to skip rolling back resources that CloudFormation can't successfully roll back. We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> troubleshoot</a> resources before skipping them. CloudFormation sets the status of the specified resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> </important> <p>Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.</p> <p>To skip resources that are part of nested stacks, use the following format: <code>NestedStackName.ResourceLogicalID</code>. If you want to specify the logical ID of a stack resource (<code>Type: AWS::CloudFormation::Stack</code>) in the <code>ResourcesToSkip</code> list, then its corresponding embedded stack must be in one of the following states: <code>DELETE_IN_PROGRESS</code>, <code>DELETE_COMPLETE</code>, or <code>DELETE_FAILED</code>.</p> <note> <p>Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks">Using ResourcesToSkip to recover a nested stacks hierarchy</a>.</p> </note>

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>ContinueUpdateRollback</code> request. Specify this token if you plan to retry requests so that CloudFormationknows that you're not attempting to continue the rollback to a stack with the same name. You might retry <code>ContinueUpdateRollback</code> requests to ensure that CloudFormation successfully received them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ContinueUpdateRollback",
            method="GET",
            params={
                "StackName": stack_name,
                "RoleARN": role_arn,
                "ResourcesToSkip": resources_to_skip,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_continue_update_rollback(
        self,
        *,
        action: PostContinueUpdateRollbackRequestAction,
        version: PostContinueUpdateRollbackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>

        Parameters
        ----------
        action : PostContinueUpdateRollbackRequestAction

        version : PostContinueUpdateRollbackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ContinueUpdateRollback",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_create_change_set(
        self,
        *,
        stack_name: str,
        change_set_name: str,
        action: GetCreateChangeSetRequestAction,
        version: GetCreateChangeSetRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        rollback_configuration: typing.Optional[GetCreateChangeSetRequestRollbackConfiguration] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        client_token: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        change_set_type: typing.Optional[GetCreateChangeSetRequestChangeSetType] = None,
        resources_to_import: typing.Optional[typing.Union[ResourceToImport, typing.Sequence[ResourceToImport]]] = None,
        include_nested_stacks: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>

        Parameters
        ----------
        stack_name : str
            The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.

        change_set_name : str
            <p>The name of the change set. The name must be unique among all change sets that are associated with the specified stack.</p> <p>A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.</p>

        action : GetCreateChangeSetRequestAction

        version : GetCreateChangeSetRequestVersion

        template_body : typing.Optional[str]
            <p>A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>

        use_previous_template : typing.Optional[bool]
            Whether to reuse the template that's associated with the stack to create the change set.

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the change set. For more information, see the <a>Parameter</a> data type.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <note> <p>This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create or update the stack directly from the template using the <a>CreateStack</a> or <a>UpdateStack</a> action, and specifying this capability.</p> </note> <p>For more information about macros, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with if you execute this change set, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling access with Identity and Access Management</a> in the CloudFormation User Guide.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>

        rollback_configuration : typing.Optional[GetCreateChangeSetRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.

        client_token : typing.Optional[str]
            A unique identifier for this <code>CreateChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another change set with the same name. You might retry <code>CreateChangeSet</code> requests to ensure that CloudFormation successfully received them.

        description : typing.Optional[str]
            A description to help you identify this change set.

        change_set_type : typing.Optional[GetCreateChangeSetRequestChangeSetType]
            <p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995"> <code>REVIEW_IN_PROGRESS</code> </a> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>

        resources_to_import : typing.Optional[typing.Union[ResourceToImport, typing.Sequence[ResourceToImport]]]
            The resources to import into your stack.

        include_nested_stacks : typing.Optional[bool]
            Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to <code>False</code>. To include nested sets in a change set, specify <code>True</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateChangeSet",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetCreateChangeSetRequestRollbackConfiguration,
                    direction="write",
                ),
                "NotificationARNs": notification_ar_ns,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "ChangeSetName": change_set_name,
                "ClientToken": client_token,
                "Description": description,
                "ChangeSetType": change_set_type,
                "ResourcesToImport": convert_and_respect_annotation_metadata(
                    object_=resources_to_import, annotation=ResourceToImport, direction="write"
                ),
                "IncludeNestedStacks": include_nested_stacks,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_create_change_set(
        self,
        *,
        action: PostCreateChangeSetRequestAction,
        version: PostCreateChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>

        Parameters
        ----------
        action : PostCreateChangeSetRequestAction

        version : PostCreateChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_create_stack(
        self,
        *,
        stack_name: str,
        action: GetCreateStackRequestAction,
        version: GetCreateStackRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        disable_rollback: typing.Optional[bool] = None,
        rollback_configuration: typing.Optional[GetCreateStackRequestRollbackConfiguration] = None,
        timeout_in_minutes: typing.Optional[int] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        on_failure: typing.Optional[GetCreateStackRequestOnFailure] = None,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        client_request_token: typing.Optional[str] = None,
        enable_termination_protection: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.

        Parameters
        ----------
        stack_name : str
            <p>The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.</p> <note> <p>A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.</p> </note>

        action : GetCreateStackRequestAction

        version : GetCreateStackRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.

        disable_rollback : typing.Optional[bool]
            <p>Set to <code>true</code> to disable rollback of the stack if stack creation failed. You can specify either <code>DisableRollback</code> or <code>OnFailure</code>, but not both.</p> <p>Default: <code>false</code> </p>

        rollback_configuration : typing.Optional[GetCreateStackRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        timeout_in_minutes : typing.Optional[int]
            The amount of time that can pass before the stack status becomes CREATE_FAILED; if <code>DisableRollback</code> is not set or is set to <code>false</code>, the stack will be rolled back.

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create the stack directly from the template using this capability.</p> <important> <p>You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with for this create stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>. Use the following syntax to describe template resource types: <code>AWS::*</code> (for all Amazon Web Services resources), <code>Custom::*</code> (for all custom resources), <code>Custom::<i>logical_ID</i> </code> (for a specific custom resource), <code>AWS::<i>service_name</i>::*</code> (for all resources of a particular Amazon Web Services service), and <code>AWS::<i>service_name</i>::<i>resource_logical_ID</i> </code> (for a specific Amazon Web Services resource).</p> <p>If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        on_failure : typing.Optional[GetCreateStackRequestOnFailure]
            <p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <p>Default: <code>ROLLBACK</code> </p>

        stack_policy_body : typing.Optional[str]
            Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent Updates to Stack Resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        stack_policy_url : typing.Optional[str]
            Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>CreateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create a stack with the same name. You might retry <code>CreateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        enable_termination_protection : typing.Optional[bool]
            <p>Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>. Termination protection is deactivated on stacks by default.</p> <p>For <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "DisableRollback": disable_rollback,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetCreateStackRequestRollbackConfiguration,
                    direction="write",
                ),
                "TimeoutInMinutes": timeout_in_minutes,
                "NotificationARNs": notification_ar_ns,
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "OnFailure": on_failure,
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "ClientRequestToken": client_request_token,
                "EnableTerminationProtection": enable_termination_protection,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_create_stack(
        self,
        *,
        action: PostCreateStackRequestAction,
        version: PostCreateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.

        Parameters
        ----------
        action : PostCreateStackRequestAction

        version : PostCreateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_create_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetCreateStackInstancesRequestAction,
        version: GetCreateStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetCreateStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        parameter_overrides: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        operation_preferences: typing.Optional[GetCreateStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetCreateStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to create stack instances from.

        action : GetCreateStackInstancesRequestAction

        version : GetCreateStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetCreateStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.

        parameter_overrides : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            <p>A list of stack set parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template.</p>

        operation_preferences : typing.Optional[GetCreateStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        call_as : typing.Optional[GetCreateStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetCreateStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "ParameterOverrides": convert_and_respect_annotation_metadata(
                    object_=parameter_overrides, annotation=Parameter, direction="write"
                ),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetCreateStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_create_stack_instances(
        self,
        *,
        action: PostCreateStackInstancesRequestAction,
        version: PostCreateStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.

        Parameters
        ----------
        action : PostCreateStackInstancesRequestAction

        version : PostCreateStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_create_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetCreateStackSetRequestAction,
        version: GetCreateStackSetRequestVersion,
        description: typing.Optional[str] = None,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        stack_id: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        administration_role_arn: typing.Optional[str] = None,
        execution_role_name: typing.Optional[str] = None,
        permission_model: typing.Optional[GetCreateStackSetRequestPermissionModel] = None,
        auto_deployment: typing.Optional[GetCreateStackSetRequestAutoDeployment] = None,
        call_as: typing.Optional[GetCreateStackSetRequestCallAs] = None,
        client_request_token: typing.Optional[str] = None,
        managed_execution: typing.Optional[GetCreateStackSetRequestManagedExecution] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates a stack set.

        Parameters
        ----------
        stack_set_name : str
            <p>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>

        action : GetCreateStackSetRequestAction

        version : GetCreateStackSetRequestVersion

        description : typing.Optional[str]
            A description of the stack set. You can use the description to identify the stack set's purpose or other important information.

        template_body : typing.Optional[str]
            <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>

        stack_id : typing.Optional[str]
            The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            The input parameters for the stack set template.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not created.</p>

        administration_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>

        execution_role_name : typing.Optional[str]
            <p>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p>

        permission_model : typing.Optional[GetCreateStackSetRequestPermissionModel]
            <p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>

        auto_deployment : typing.Optional[GetCreateStackSetRequestAutoDeployment]
            Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>.

        call_as : typing.Optional[GetCreateStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>To create a stack set with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.</p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>

        managed_execution : typing.Optional[GetCreateStackSetRequestManagedExecution]
            Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Description": description,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "StackId": stack_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "AdministrationRoleARN": administration_role_arn,
                "ExecutionRoleName": execution_role_name,
                "PermissionModel": permission_model,
                "AutoDeployment": convert_and_respect_annotation_metadata(
                    object_=auto_deployment, annotation=GetCreateStackSetRequestAutoDeployment, direction="write"
                ),
                "CallAs": call_as,
                "ClientRequestToken": client_request_token,
                "ManagedExecution": convert_and_respect_annotation_metadata(
                    object_=managed_execution, annotation=GetCreateStackSetRequestManagedExecution, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_create_stack_set(
        self,
        *,
        action: PostCreateStackSetRequestAction,
        version: PostCreateStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates a stack set.

        Parameters
        ----------
        action : PostCreateStackSetRequestAction

        version : PostCreateStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=CreateStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_deactivate_type(
        self,
        *,
        action: GetDeactivateTypeRequestAction,
        version: GetDeactivateTypeRequestVersion,
        type_name: typing.Optional[str] = None,
        type: typing.Optional[GetDeactivateTypeRequestType] = None,
        arn: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>

        Parameters
        ----------
        action : GetDeactivateTypeRequestAction

        version : GetDeactivateTypeRequestVersion

        type_name : typing.Optional[str]
            <p>The type name of the extension, in this account and region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type : typing.Optional[GetDeactivateTypeRequestType]
            <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeactivateType",
            method="GET",
            params={
                "TypeName": type_name,
                "Type": type,
                "Arn": arn,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_deactivate_type(
        self,
        *,
        action: PostDeactivateTypeRequestAction,
        version: PostDeactivateTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>

        Parameters
        ----------
        action : PostDeactivateTypeRequestAction

        version : PostDeactivateTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeactivateType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_delete_change_set(
        self,
        *,
        change_set_name: str,
        action: GetDeleteChangeSetRequestAction,
        version: GetDeleteChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to delete.

        action : GetDeleteChangeSetRequestAction

        version : GetDeleteChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_delete_change_set(
        self,
        *,
        action: PostDeleteChangeSetRequestAction,
        version: PostDeleteChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>

        Parameters
        ----------
        action : PostDeleteChangeSetRequestAction

        version : PostDeleteChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_delete_stack(
        self,
        *,
        stack_name: str,
        action: GetDeleteStackRequestAction,
        version: GetDeleteStackRequestVersion,
        retain_resources: typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]] = None,
        role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.

        Parameters
        ----------
        stack_name : str
            The name or the unique stack ID that's associated with the stack.

        action : GetDeleteStackRequestAction

        version : GetDeleteStackRequestVersion

        retain_resources : typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]
            <p>For stacks in the <code>DELETE_FAILED</code> state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, CloudFormation deletes the stack but doesn't delete the retained resources.</p> <p>Retaining resources is useful when you can't delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to delete the stack. CloudFormation uses the role's credentials to make calls on your behalf.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>DeleteStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to delete a stack with the same name. You might retry <code>DeleteStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStack",
            method="GET",
            params={
                "StackName": stack_name,
                "RetainResources": retain_resources,
                "RoleARN": role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_delete_stack(
        self,
        *,
        action: PostDeleteStackRequestAction,
        version: PostDeleteStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.

        Parameters
        ----------
        action : PostDeleteStackRequestAction

        version : PostDeleteStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_delete_stack_instances(
        self,
        *,
        stack_set_name: str,
        retain_stacks: bool,
        action: GetDeleteStackInstancesRequestAction,
        version: GetDeleteStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetDeleteStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        operation_preferences: typing.Optional[GetDeleteStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetDeleteStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to delete stack instances for.

        retain_stacks : bool
            <p>Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack set operation options</a>.</p>

        action : GetDeleteStackInstancesRequestAction

        version : GetDeleteStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetDeleteStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The Amazon Web Services Regions where you want to delete stack set instances.

        operation_preferences : typing.Optional[GetDeleteStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        call_as : typing.Optional[GetDeleteStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetDeleteStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetDeleteStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "RetainStacks": retain_stacks,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_delete_stack_instances(
        self,
        *,
        action: PostDeleteStackInstancesRequestAction,
        version: PostDeleteStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

        Parameters
        ----------
        action : PostDeleteStackInstancesRequestAction

        version : PostDeleteStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_delete_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetDeleteStackSetRequestAction,
        version: GetDeleteStackSetRequestVersion,
        call_as: typing.Optional[GetDeleteStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you're deleting. You can obtain this value by running <a>ListStackSets</a>.

        action : GetDeleteStackSetRequestAction

        version : GetDeleteStackSetRequestVersion

        call_as : typing.Optional[GetDeleteStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_delete_stack_set(
        self,
        *,
        action: PostDeleteStackSetRequestAction,
        version: PostDeleteStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.

        Parameters
        ----------
        action : PostDeleteStackSetRequestAction

        version : PostDeleteStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_deregister_type(
        self,
        *,
        action: GetDeregisterTypeRequestAction,
        version: GetDeregisterTypeRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetDeregisterTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>

        Parameters
        ----------
        action : GetDeregisterTypeRequestAction

        version : GetDeregisterTypeRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type : typing.Optional[GetDeregisterTypeRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeregisterType",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_deregister_type(
        self,
        *,
        action: PostDeregisterTypeRequestAction,
        version: PostDeregisterTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>

        Parameters
        ----------
        action : PostDeregisterTypeRequestAction

        version : PostDeregisterTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DeregisterType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_account_limits(
        self,
        *,
        action: GetDescribeAccountLimitsRequestAction,
        version: GetDescribeAccountLimitsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.

        Parameters
        ----------
        action : GetDescribeAccountLimitsRequestAction

        version : GetDescribeAccountLimitsRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of limits that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeAccountLimits",
            method="GET",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_account_limits(
        self,
        *,
        action: PostDescribeAccountLimitsRequestAction,
        version: PostDescribeAccountLimitsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.

        Parameters
        ----------
        action : PostDescribeAccountLimitsRequestAction

        version : PostDescribeAccountLimitsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeAccountLimits",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_change_set(
        self,
        *,
        change_set_name: str,
        action: GetDescribeChangeSetRequestAction,
        version: GetDescribeChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.

        action : GetDescribeChangeSetRequestAction

        version : GetDescribeChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.

        next_token : typing.Optional[str]
            A string (provided by the <a>DescribeChangeSet</a> response output) that identifies the next page of information that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_change_set(
        self,
        *,
        action: PostDescribeChangeSetRequestAction,
        version: PostDescribeChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.

        Parameters
        ----------
        action : PostDescribeChangeSetRequestAction

        version : PostDescribeChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_change_set_hooks(
        self,
        *,
        change_set_name: str,
        action: GetDescribeChangeSetHooksRequestAction,
        version: GetDescribeChangeSetHooksRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        logical_resource_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.

        action : GetDescribeChangeSetHooksRequestAction

        version : GetDescribeChangeSetHooksRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.

        next_token : typing.Optional[str]
            A string, provided by the <code>DescribeChangeSetHooks</code> response output, that identifies the next page of information that you want to retrieve.

        logical_resource_id : typing.Optional[str]
            If specified, lists only the hooks related to the specified <code>LogicalResourceId</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSetHooks",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "NextToken": next_token,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_change_set_hooks(
        self,
        *,
        action: PostDescribeChangeSetHooksRequestAction,
        version: PostDescribeChangeSetHooksRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

        Parameters
        ----------
        action : PostDescribeChangeSetHooksRequestAction

        version : PostDescribeChangeSetHooksRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSetHooks",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_publisher(
        self,
        *,
        action: GetDescribePublisherRequestAction,
        version: GetDescribePublisherRequestVersion,
        publisher_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>

        Parameters
        ----------
        action : GetDescribePublisherRequestAction

        version : GetDescribePublisherRequestVersion

        publisher_id : typing.Optional[str]
            <p>The ID of the extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribePublisher",
            method="GET",
            params={
                "PublisherId": publisher_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_publisher(
        self,
        *,
        action: PostDescribePublisherRequestAction,
        version: PostDescribePublisherRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>

        Parameters
        ----------
        action : PostDescribePublisherRequestAction

        version : PostDescribePublisherRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribePublisher",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_drift_detection_status(
        self,
        *,
        stack_drift_detection_id: str,
        action: GetDescribeStackDriftDetectionStatusRequestAction,
        version: GetDescribeStackDriftDetectionStatusRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>

        Parameters
        ----------
        stack_drift_detection_id : str
            <p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.</p>

        action : GetDescribeStackDriftDetectionStatusRequestAction

        version : GetDescribeStackDriftDetectionStatusRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackDriftDetectionStatus",
            method="GET",
            params={
                "StackDriftDetectionId": stack_drift_detection_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_drift_detection_status(
        self,
        *,
        action: PostDescribeStackDriftDetectionStatusRequestAction,
        version: PostDescribeStackDriftDetectionStatusRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>

        Parameters
        ----------
        action : PostDescribeStackDriftDetectionStatusRequestAction

        version : PostDescribeStackDriftDetectionStatusRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackDriftDetectionStatus",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_events(
        self,
        *,
        action: GetDescribeStackEventsRequestAction,
        version: GetDescribeStackEventsRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>

        Parameters
        ----------
        action : GetDescribeStackEventsRequestAction

        version : GetDescribeStackEventsRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        next_token : typing.Optional[str]
            A string that identifies the next page of events that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackEvents",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_events(
        self,
        *,
        action: PostDescribeStackEventsRequestAction,
        version: PostDescribeStackEventsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>

        Parameters
        ----------
        action : PostDescribeStackEventsRequestAction

        version : PostDescribeStackEventsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackEvents",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_instance(
        self,
        *,
        stack_set_name: str,
        stack_instance_account: str,
        stack_instance_region: str,
        action: GetDescribeStackInstanceRequestAction,
        version: GetDescribeStackInstanceRequestVersion,
        call_as: typing.Optional[GetDescribeStackInstanceRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or the unique stack ID of the stack set that you want to get stack instance information for.

        stack_instance_account : str
            The ID of an Amazon Web Services account that's associated with this stack instance.

        stack_instance_region : str
            The name of a Region that's associated with this stack instance.

        action : GetDescribeStackInstanceRequestAction

        version : GetDescribeStackInstanceRequestVersion

        call_as : typing.Optional[GetDescribeStackInstanceRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackInstance",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "StackInstanceAccount": stack_instance_account,
                "StackInstanceRegion": stack_instance_region,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_instance(
        self,
        *,
        action: PostDescribeStackInstanceRequestAction,
        version: PostDescribeStackInstanceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>

        Parameters
        ----------
        action : PostDescribeStackInstanceRequestAction

        version : PostDescribeStackInstanceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackInstance",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_resource(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        action: GetDescribeStackResourceRequestAction,
        version: GetDescribeStackResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        logical_resource_id : str
            <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>

        action : GetDescribeStackResourceRequestAction

        version : GetDescribeStackResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResource",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_resource(
        self,
        *,
        action: PostDescribeStackResourceRequestAction,
        version: PostDescribeStackResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        action : PostDescribeStackResourceRequestAction

        version : PostDescribeStackResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResource",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_resource_drifts(
        self,
        *,
        stack_name: str,
        action: GetDescribeStackResourceDriftsRequestAction,
        version: GetDescribeStackResourceDriftsRequestVersion,
        stack_resource_drift_status_filters: typing.Optional[
            typing.Union[StackResourceDriftStatus, typing.Sequence[StackResourceDriftStatus]]
        ] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack for which you want drift information.

        action : GetDescribeStackResourceDriftsRequestAction

        version : GetDescribeStackResourceDriftsRequestVersion

        stack_resource_drift_status_filters : typing.Optional[typing.Union[StackResourceDriftStatus, typing.Sequence[StackResourceDriftStatus]]]
            <p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>

        next_token : typing.Optional[str]
            A string that identifies the next page of stack resource drift results.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResourceDrifts",
            method="GET",
            params={
                "StackName": stack_name,
                "StackResourceDriftStatusFilters": stack_resource_drift_status_filters,
                "NextToken": next_token,
                "MaxResults": max_results,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_resource_drifts(
        self,
        *,
        action: PostDescribeStackResourceDriftsRequestAction,
        version: PostDescribeStackResourceDriftsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>

        Parameters
        ----------
        action : PostDescribeStackResourceDriftsRequestAction

        version : PostDescribeStackResourceDriftsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResourceDrifts",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_resources(
        self,
        *,
        action: GetDescribeStackResourcesRequestAction,
        version: GetDescribeStackResourcesRequestVersion,
        stack_name: typing.Optional[str] = None,
        logical_resource_id: typing.Optional[str] = None,
        physical_resource_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>

        Parameters
        ----------
        action : GetDescribeStackResourcesRequestAction

        version : GetDescribeStackResourcesRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p> <p>Required: Conditional. If you don't specify <code>StackName</code>, you must specify <code>PhysicalResourceId</code>.</p>

        logical_resource_id : typing.Optional[str]
            <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>

        physical_resource_id : typing.Optional[str]
            <p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p> <p>For example, for an Amazon Elastic Compute Cloud (EC2) instance, <code>PhysicalResourceId</code> corresponds to the <code>InstanceId</code>. You can pass the EC2 <code>InstanceId</code> to <code>DescribeStackResources</code> to find which stack the instance belongs to and what other resources are part of the stack.</p> <p>Required: Conditional. If you don't specify <code>PhysicalResourceId</code>, you must specify <code>StackName</code>.</p> <p>Default: There is no default value.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResources",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "PhysicalResourceId": physical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_resources(
        self,
        *,
        action: PostDescribeStackResourcesRequestAction,
        version: PostDescribeStackResourcesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>

        Parameters
        ----------
        action : PostDescribeStackResourcesRequestAction

        version : PostDescribeStackResourcesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResources",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetDescribeStackSetRequestAction,
        version: GetDescribeStackSetRequestVersion,
        call_as: typing.Optional[GetDescribeStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the description of the specified stack set.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set whose description you want.

        action : GetDescribeStackSetRequestAction

        version : GetDescribeStackSetRequestVersion

        call_as : typing.Optional[GetDescribeStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_set(
        self,
        *,
        action: PostDescribeStackSetRequestAction,
        version: PostDescribeStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the description of the specified stack set.

        Parameters
        ----------
        action : PostDescribeStackSetRequestAction

        version : PostDescribeStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stack_set_operation(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetDescribeStackSetOperationRequestAction,
        version: GetDescribeStackSetOperationRequestVersion,
        call_as: typing.Optional[GetDescribeStackSetOperationRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the description of the specified stack set operation.

        Parameters
        ----------
        stack_set_name : str
            The name or the unique stack ID of the stack set for the stack operation.

        operation_id : str
            The unique ID of the stack set operation.

        action : GetDescribeStackSetOperationRequestAction

        version : GetDescribeStackSetOperationRequestVersion

        call_as : typing.Optional[GetDescribeStackSetOperationRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSetOperation",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stack_set_operation(
        self,
        *,
        action: PostDescribeStackSetOperationRequestAction,
        version: PostDescribeStackSetOperationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the description of the specified stack set operation.

        Parameters
        ----------
        action : PostDescribeStackSetOperationRequestAction

        version : PostDescribeStackSetOperationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSetOperation",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_stacks(
        self,
        *,
        action: GetDescribeStacksRequestAction,
        version: GetDescribeStacksRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : GetDescribeStacksRequestAction

        version : GetDescribeStacksRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        next_token : typing.Optional[str]
            A string that identifies the next page of stacks that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStacks",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_stacks(
        self,
        *,
        action: PostDescribeStacksRequestAction,
        version: PostDescribeStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : PostDescribeStacksRequestAction

        version : PostDescribeStacksRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeStacks",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_type(
        self,
        *,
        action: GetDescribeTypeRequestAction,
        version: GetDescribeTypeRequestVersion,
        type: typing.Optional[GetDescribeTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        arn: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        publisher_id: typing.Optional[str] = None,
        public_version_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        Parameters
        ----------
        action : GetDescribeTypeRequestAction

        version : GetDescribeTypeRequestVersion

        type : typing.Optional[GetDescribeTypeRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        publisher_id : typing.Optional[str]
            <p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>

        public_version_number : typing.Optional[str]
            The version number of a public third-party extension.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeType",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "Arn": arn,
                "VersionId": version_id,
                "PublisherId": publisher_id,
                "PublicVersionNumber": public_version_number,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_type(
        self,
        *,
        action: PostDescribeTypeRequestAction,
        version: PostDescribeTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        Parameters
        ----------
        action : PostDescribeTypeRequestAction

        version : PostDescribeTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_describe_type_registration(
        self,
        *,
        registration_token: str,
        action: GetDescribeTypeRegistrationRequestAction,
        version: GetDescribeTypeRegistrationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>

        Parameters
        ----------
        registration_token : str
            <p>The identifier for this registration request.</p> <p>This registration token is generated by CloudFormation when you initiate a registration request using <code> <a>RegisterType</a> </code>.</p>

        action : GetDescribeTypeRegistrationRequestAction

        version : GetDescribeTypeRegistrationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeTypeRegistration",
            method="GET",
            params={
                "RegistrationToken": registration_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_describe_type_registration(
        self,
        *,
        action: PostDescribeTypeRegistrationRequestAction,
        version: PostDescribeTypeRegistrationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>

        Parameters
        ----------
        action : PostDescribeTypeRegistrationRequestAction

        version : PostDescribeTypeRegistrationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DescribeTypeRegistration",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_detect_stack_drift(
        self,
        *,
        stack_name: str,
        action: GetDetectStackDriftRequestAction,
        version: GetDetectStackDriftRequestVersion,
        logical_resource_ids: typing.Optional[
            typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack for which you want to detect drift.

        action : GetDetectStackDriftRequestAction

        version : GetDetectStackDriftRequestVersion

        logical_resource_ids : typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]
            The logical names of any resources you want to use as filters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackDrift",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceIds": logical_resource_ids,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_detect_stack_drift(
        self,
        *,
        action: PostDetectStackDriftRequestAction,
        version: PostDetectStackDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>

        Parameters
        ----------
        action : PostDetectStackDriftRequestAction

        version : PostDetectStackDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_detect_stack_resource_drift(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        action: GetDetectStackResourceDriftRequestAction,
        version: GetDetectStackResourceDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack to which the resource belongs.

        logical_resource_id : str
            The logical name of the resource for which to return drift information.

        action : GetDetectStackResourceDriftRequestAction

        version : GetDetectStackResourceDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackResourceDrift",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_detect_stack_resource_drift(
        self,
        *,
        action: PostDetectStackResourceDriftRequestAction,
        version: PostDetectStackResourceDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>

        Parameters
        ----------
        action : PostDetectStackResourceDriftRequestAction

        version : PostDetectStackResourceDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackResourceDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_detect_stack_set_drift(
        self,
        *,
        stack_set_name: str,
        action: GetDetectStackSetDriftRequestAction,
        version: GetDetectStackSetDriftRequestVersion,
        operation_preferences: typing.Optional[GetDetectStackSetDriftRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetDetectStackSetDriftRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name of the stack set on which to perform the drift detection operation.

        action : GetDetectStackSetDriftRequestAction

        version : GetDetectStackSetDriftRequestVersion

        operation_preferences : typing.Optional[GetDetectStackSetDriftRequestOperationPreferences]


        operation_id : typing.Optional[str]
             <i>The ID of the stack set operation.</i>

        call_as : typing.Optional[GetDetectStackSetDriftRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackSetDrift",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetDetectStackSetDriftRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_detect_stack_set_drift(
        self,
        *,
        action: PostDetectStackSetDriftRequestAction,
        version: PostDetectStackSetDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>

        Parameters
        ----------
        action : PostDetectStackSetDriftRequestAction

        version : PostDetectStackSetDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=DetectStackSetDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_estimate_template_cost(
        self,
        *,
        action: GetEstimateTemplateCostRequestAction,
        version: GetEstimateTemplateCostRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

        Parameters
        ----------
        action : GetEstimateTemplateCostRequestAction

        version : GetEstimateTemplateCostRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must pass <code>TemplateBody</code> or <code>TemplateURL</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=EstimateTemplateCost",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_estimate_template_cost(
        self,
        *,
        action: PostEstimateTemplateCostRequestAction,
        version: PostEstimateTemplateCostRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

        Parameters
        ----------
        action : PostEstimateTemplateCostRequestAction

        version : PostEstimateTemplateCostRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=EstimateTemplateCost",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_execute_change_set(
        self,
        *,
        change_set_name: str,
        action: GetExecuteChangeSetRequestAction,
        version: GetExecuteChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        disable_rollback: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.

        action : GetExecuteChangeSetRequestAction

        version : GetExecuteChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.

        disable_rollback : typing.Optional[bool]
            <p>Preserves the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>True</code> </p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ExecuteChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "ClientRequestToken": client_request_token,
                "DisableRollback": disable_rollback,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_execute_change_set(
        self,
        *,
        action: PostExecuteChangeSetRequestAction,
        version: PostExecuteChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>

        Parameters
        ----------
        action : PostExecuteChangeSetRequestAction

        version : PostExecuteChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ExecuteChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_get_stack_policy(
        self,
        *,
        stack_name: str,
        action: GetGetStackPolicyRequestAction,
        version: GetGetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID that's associated with the stack whose policy you want to get.

        action : GetGetStackPolicyRequestAction

        version : GetGetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetStackPolicy",
            method="GET",
            params={
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_get_stack_policy(
        self,
        *,
        action: PostGetStackPolicyRequestAction,
        version: PostGetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.

        Parameters
        ----------
        action : PostGetStackPolicyRequestAction

        version : PostGetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetStackPolicy",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_get_template(
        self,
        *,
        action: GetGetTemplateRequestAction,
        version: GetGetTemplateRequestVersion,
        stack_name: typing.Optional[str] = None,
        change_set_name: typing.Optional[str] = None,
        template_stage: typing.Optional[GetGetTemplateRequestTemplateStage] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : GetGetTemplateRequestAction

        version : GetGetTemplateRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        change_set_name : typing.Optional[str]
            The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.

        template_stage : typing.Optional[GetGetTemplateRequestTemplateStage]
            <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetTemplate",
            method="GET",
            params={
                "StackName": stack_name,
                "ChangeSetName": change_set_name,
                "TemplateStage": template_stage,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_get_template(
        self,
        *,
        action: PostGetTemplateRequestAction,
        version: PostGetTemplateRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : PostGetTemplateRequestAction

        version : PostGetTemplateRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetTemplate",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_get_template_summary(
        self,
        *,
        action: GetGetTemplateSummaryRequestAction,
        version: GetGetTemplateSummaryRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        stack_name: typing.Optional[str] = None,
        stack_set_name: typing.Optional[str] = None,
        call_as: typing.Optional[GetGetTemplateSummaryRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>

        Parameters
        ----------
        action : GetGetTemplateSummaryRequestAction

        version : GetGetTemplateSummaryRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        stack_name : typing.Optional[str]
            <p>The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        stack_set_name : typing.Optional[str]
            <p>The name or unique ID of the stack set from which the stack was created.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        call_as : typing.Optional[GetGetTemplateSummaryRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetTemplateSummary",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "StackName": stack_name,
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_get_template_summary(
        self,
        *,
        action: PostGetTemplateSummaryRequestAction,
        version: PostGetTemplateSummaryRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>

        Parameters
        ----------
        action : PostGetTemplateSummaryRequestAction

        version : PostGetTemplateSummaryRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=GetTemplateSummary",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_import_stacks_to_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetImportStacksToStackSetRequestAction,
        version: GetImportStacksToStackSetRequestVersion,
        stack_ids: typing.Optional[typing.Union[StackId, typing.Sequence[StackId]]] = None,
        stack_ids_url: typing.Optional[str] = None,
        organizational_unit_ids: typing.Optional[
            typing.Union[OrganizationalUnitId, typing.Sequence[OrganizationalUnitId]]
        ] = None,
        operation_preferences: typing.Optional[GetImportStacksToStackSetRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetImportStacksToStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>

        Parameters
        ----------
        stack_set_name : str
            The name of the stack set. The name must be unique in the Region where you create your stack set.

        action : GetImportStacksToStackSetRequestAction

        version : GetImportStacksToStackSetRequestVersion

        stack_ids : typing.Optional[typing.Union[StackId, typing.Sequence[StackId]]]
            <p>The IDs of the stacks you are importing into a stack set. You import up to 10 stacks per stack set at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>

        stack_ids_url : typing.Optional[str]
            <p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>

        organizational_unit_ids : typing.Optional[typing.Union[OrganizationalUnitId, typing.Sequence[OrganizationalUnitId]]]
            The list of OU ID's to which the stacks being imported has to be mapped as deployment target.

        operation_preferences : typing.Optional[GetImportStacksToStackSetRequestOperationPreferences]


        operation_id : typing.Optional[str]
            A unique, user defined, identifier for the stack set operation.

        call_as : typing.Optional[GetImportStacksToStackSetRequestCallAs]
            <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed stack sets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ImportStacksToStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "StackIds": stack_ids,
                "StackIdsUrl": stack_ids_url,
                "OrganizationalUnitIds": organizational_unit_ids,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetImportStacksToStackSetRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_import_stacks_to_stack_set(
        self,
        *,
        action: PostImportStacksToStackSetRequestAction,
        version: PostImportStacksToStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>

        Parameters
        ----------
        action : PostImportStacksToStackSetRequestAction

        version : PostImportStacksToStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ImportStacksToStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_change_sets(
        self,
        *,
        stack_name: str,
        action: GetListChangeSetsRequestAction,
        version: GetListChangeSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.

        Parameters
        ----------
        stack_name : str
            The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.

        action : GetListChangeSetsRequestAction

        version : GetListChangeSetsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListChangeSets</a> response output) that identifies the next page of change sets that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListChangeSets",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_change_sets(
        self,
        *,
        action: PostListChangeSetsRequestAction,
        version: PostListChangeSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.

        Parameters
        ----------
        action : PostListChangeSetsRequestAction

        version : PostListChangeSetsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListChangeSets",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_exports(
        self,
        *,
        action: GetListExportsRequestAction,
        version: GetListExportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>

        Parameters
        ----------
        action : GetListExportsRequestAction

        version : GetListExportsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListExports</a> response output) that identifies the next page of exported output values that you asked to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListExports",
            method="GET",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_exports(
        self,
        *,
        action: PostListExportsRequestAction,
        version: PostListExportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>

        Parameters
        ----------
        action : PostListExportsRequestAction

        version : PostListExportsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListExports",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_imports(
        self,
        *,
        export_name: str,
        action: GetListImportsRequestAction,
        version: GetListImportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>

        Parameters
        ----------
        export_name : str
            The name of the exported output value. CloudFormation returns the stack names that are importing this value.

        action : GetListImportsRequestAction

        version : GetListImportsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListImports</a> response output) that identifies the next page of stacks that are importing the specified exported output value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListImports",
            method="GET",
            params={
                "ExportName": export_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_imports(
        self,
        *,
        action: PostListImportsRequestAction,
        version: PostListImportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>

        Parameters
        ----------
        action : PostListImportsRequestAction

        version : PostListImportsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListImports",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetListStackInstancesRequestAction,
        version: GetListStackInstancesRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        filters: typing.Optional[typing.Union[StackInstanceFilter, typing.Sequence[StackInstanceFilter]]] = None,
        stack_instance_account: typing.Optional[str] = None,
        stack_instance_region: typing.Optional[str] = None,
        call_as: typing.Optional[GetListStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to list stack instances for.

        action : GetListStackInstancesRequestAction

        version : GetListStackInstancesRequestVersion

        next_token : typing.Optional[str]
            If the previous request didn't return all the remaining results, the response's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        filters : typing.Optional[typing.Union[StackInstanceFilter, typing.Sequence[StackInstanceFilter]]]
            The filter to apply to stack instances

        stack_instance_account : typing.Optional[str]
            The name of the Amazon Web Services account that you want to list stack instances for.

        stack_instance_region : typing.Optional[str]
            The name of the Region where you want to list stack instances.

        call_as : typing.Optional[GetListStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "NextToken": next_token,
                "MaxResults": max_results,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=StackInstanceFilter, direction="write"
                ),
                "StackInstanceAccount": stack_instance_account,
                "StackInstanceRegion": stack_instance_region,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stack_instances(
        self,
        *,
        action: PostListStackInstancesRequestAction,
        version: PostListStackInstancesRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

        Parameters
        ----------
        action : PostListStackInstancesRequestAction

        version : PostListStackInstancesRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackInstances",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stack_resources(
        self,
        *,
        stack_name: str,
        action: GetListStackResourcesRequestAction,
        version: GetListStackResourcesRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        action : GetListStackResourcesRequestAction

        version : GetListStackResourcesRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of stack resources that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackResources",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stack_resources(
        self,
        *,
        action: PostListStackResourcesRequestAction,
        version: PostListStackResourcesRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        action : PostListStackResourcesRequestAction

        version : PostListStackResourcesRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackResources",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stack_set_operation_results(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetListStackSetOperationResultsRequestAction,
        version: GetListStackSetOperationResultsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        call_as: typing.Optional[GetListStackSetOperationResultsRequestCallAs] = None,
        filters: typing.Optional[typing.Union[OperationResultFilter, typing.Sequence[OperationResultFilter]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about the results of a stack set operation.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to get operation results for.

        operation_id : str
            The ID of the stack set operation.

        action : GetListStackSetOperationResultsRequestAction

        version : GetListStackSetOperationResultsRequestVersion

        next_token : typing.Optional[str]
            If the previous request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        call_as : typing.Optional[GetListStackSetOperationResultsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        filters : typing.Optional[typing.Union[OperationResultFilter, typing.Sequence[OperationResultFilter]]]
            The filter to apply to operation results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperationResults",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "NextToken": next_token,
                "MaxResults": max_results,
                "CallAs": call_as,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=OperationResultFilter, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stack_set_operation_results(
        self,
        *,
        action: PostListStackSetOperationResultsRequestAction,
        version: PostListStackSetOperationResultsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about the results of a stack set operation.

        Parameters
        ----------
        action : PostListStackSetOperationResultsRequestAction

        version : PostListStackSetOperationResultsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperationResults",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stack_set_operations(
        self,
        *,
        stack_set_name: str,
        action: GetListStackSetOperationsRequestAction,
        version: GetListStackSetOperationsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        call_as: typing.Optional[GetListStackSetOperationsRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about operations performed on a stack set.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to get operation summaries for.

        action : GetListStackSetOperationsRequestAction

        version : GetListStackSetOperationsRequestVersion

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperations</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        call_as : typing.Optional[GetListStackSetOperationsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperations",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "NextToken": next_token,
                "MaxResults": max_results,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stack_set_operations(
        self,
        *,
        action: PostListStackSetOperationsRequestAction,
        version: PostListStackSetOperationsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about operations performed on a stack set.

        Parameters
        ----------
        action : PostListStackSetOperationsRequestAction

        version : PostListStackSetOperationsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperations",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stack_sets(
        self,
        *,
        action: GetListStackSetsRequestAction,
        version: GetListStackSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetListStackSetsRequestStatus] = None,
        call_as: typing.Optional[GetListStackSetsRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>

        Parameters
        ----------
        action : GetListStackSetsRequestAction

        version : GetListStackSetsRequestVersion

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSets</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        status : typing.Optional[GetListStackSetsRequestStatus]
            The status of the stack sets that you want to get summary information about.

        call_as : typing.Optional[GetListStackSetsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSets",
            method="GET",
            params={
                "NextToken": next_token,
                "MaxResults": max_results,
                "Status": status,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stack_sets(
        self,
        *,
        action: PostListStackSetsRequestAction,
        version: PostListStackSetsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>

        Parameters
        ----------
        action : PostListStackSetsRequestAction

        version : PostListStackSetsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStackSets",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_stacks(
        self,
        *,
        action: GetListStacksRequestAction,
        version: GetListStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        stack_status_filter: typing.Optional[typing.Union[StackStatus, typing.Sequence[StackStatus]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

        Parameters
        ----------
        action : GetListStacksRequestAction

        version : GetListStacksRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of stacks that you want to retrieve.

        stack_status_filter : typing.Optional[typing.Union[StackStatus, typing.Sequence[StackStatus]]]
            Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStacks",
            method="GET",
            params={
                "NextToken": next_token,
                "StackStatusFilter": stack_status_filter,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_stacks(
        self,
        *,
        action: PostListStacksRequestAction,
        version: PostListStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

        Parameters
        ----------
        action : PostListStacksRequestAction

        version : PostListStacksRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListStacks",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_type_registrations(
        self,
        *,
        action: GetListTypeRegistrationsRequestAction,
        version: GetListTypeRegistrationsRequestVersion,
        type: typing.Optional[GetListTypeRegistrationsRequestType] = None,
        type_name: typing.Optional[str] = None,
        type_arn: typing.Optional[str] = None,
        registration_status_filter: typing.Optional[GetListTypeRegistrationsRequestRegistrationStatusFilter] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns a list of registration tokens for the specified extension(s).

        Parameters
        ----------
        action : GetListTypeRegistrationsRequestAction

        version : GetListTypeRegistrationsRequestVersion

        type : typing.Optional[GetListTypeRegistrationsRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        registration_status_filter : typing.Optional[GetListTypeRegistrationsRequestRegistrationStatusFilter]
            <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypeRegistrations",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "TypeArn": type_arn,
                "RegistrationStatusFilter": registration_status_filter,
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_type_registrations(
        self,
        *,
        action: PostListTypeRegistrationsRequestAction,
        version: PostListTypeRegistrationsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns a list of registration tokens for the specified extension(s).

        Parameters
        ----------
        action : PostListTypeRegistrationsRequestAction

        version : PostListTypeRegistrationsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypeRegistrations",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_type_versions(
        self,
        *,
        action: GetListTypeVersionsRequestAction,
        version: GetListTypeVersionsRequestVersion,
        type: typing.Optional[GetListTypeVersionsRequestType] = None,
        type_name: typing.Optional[str] = None,
        arn: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        deprecated_status: typing.Optional[GetListTypeVersionsRequestDeprecatedStatus] = None,
        publisher_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about the versions of an extension.

        Parameters
        ----------
        action : GetListTypeVersionsRequestAction

        version : GetListTypeVersionsRequestVersion

        type : typing.Optional[GetListTypeVersionsRequestType]
            <p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        deprecated_status : typing.Optional[GetListTypeVersionsRequestDeprecatedStatus]
            <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>

        publisher_id : typing.Optional[str]
            <p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypeVersions",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "Arn": arn,
                "MaxResults": max_results,
                "NextToken": next_token,
                "DeprecatedStatus": deprecated_status,
                "PublisherId": publisher_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_type_versions(
        self,
        *,
        action: PostListTypeVersionsRequestAction,
        version: PostListTypeVersionsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about the versions of an extension.

        Parameters
        ----------
        action : PostListTypeVersionsRequestAction

        version : PostListTypeVersionsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypeVersions",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_list_types(
        self,
        *,
        action: GetListTypesRequestAction,
        version: GetListTypesRequestVersion,
        visibility: typing.Optional[GetListTypesRequestVisibility] = None,
        provisioning_type: typing.Optional[GetListTypesRequestProvisioningType] = None,
        deprecated_status: typing.Optional[GetListTypesRequestDeprecatedStatus] = None,
        type: typing.Optional[GetListTypesRequestType] = None,
        filters: typing.Optional[GetListTypesRequestFilters] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about extension that have been registered with CloudFormation.

        Parameters
        ----------
        action : GetListTypesRequestAction

        version : GetListTypesRequestVersion

        visibility : typing.Optional[GetListTypesRequestVisibility]
            <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and region.</p> </li> <li> <p>Public extensions that you have activated in this account and region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>

        provisioning_type : typing.Optional[GetListTypesRequestProvisioningType]
            <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>

        deprecated_status : typing.Optional[GetListTypesRequestDeprecatedStatus]
            <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>

        type : typing.Optional[GetListTypesRequestType]
            The type of extension.

        filters : typing.Optional[GetListTypesRequestFilters]
            <p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypes",
            method="GET",
            params={
                "Visibility": visibility,
                "ProvisioningType": provisioning_type,
                "DeprecatedStatus": deprecated_status,
                "Type": type,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=GetListTypesRequestFilters, direction="write"
                ),
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_list_types(
        self,
        *,
        action: PostListTypesRequestAction,
        version: PostListTypesRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Returns summary information about extension that have been registered with CloudFormation.

        Parameters
        ----------
        action : PostListTypesRequestAction

        version : PostListTypesRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ListTypes",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_publish_type(
        self,
        *,
        action: GetPublishTypeRequestAction,
        version: GetPublishTypeRequestVersion,
        type: typing.Optional[GetPublishTypeRequestType] = None,
        arn: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        public_version_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>

        Parameters
        ----------
        action : GetPublishTypeRequestAction

        version : GetPublishTypeRequestVersion

        type : typing.Optional[GetPublishTypeRequestType]
            <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        public_version_number : typing.Optional[str]
            <p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=PublishType",
            method="GET",
            params={
                "Type": type,
                "Arn": arn,
                "TypeName": type_name,
                "PublicVersionNumber": public_version_number,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_publish_type(
        self,
        *,
        action: PostPublishTypeRequestAction,
        version: PostPublishTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>

        Parameters
        ----------
        action : PostPublishTypeRequestAction

        version : PostPublishTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=PublishType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_record_handler_progress(
        self,
        *,
        bearer_token: str,
        operation_status: GetRecordHandlerProgressRequestOperationStatus,
        action: GetRecordHandlerProgressRequestAction,
        version: GetRecordHandlerProgressRequestVersion,
        current_operation_status: typing.Optional[GetRecordHandlerProgressRequestCurrentOperationStatus] = None,
        status_message: typing.Optional[str] = None,
        error_code: typing.Optional[GetRecordHandlerProgressRequestErrorCode] = None,
        resource_model: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>

        Parameters
        ----------
        bearer_token : str
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        operation_status : GetRecordHandlerProgressRequestOperationStatus
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        action : GetRecordHandlerProgressRequestAction

        version : GetRecordHandlerProgressRequestVersion

        current_operation_status : typing.Optional[GetRecordHandlerProgressRequestCurrentOperationStatus]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        status_message : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        error_code : typing.Optional[GetRecordHandlerProgressRequestErrorCode]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        resource_model : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        client_request_token : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RecordHandlerProgress",
            method="GET",
            params={
                "BearerToken": bearer_token,
                "OperationStatus": operation_status,
                "CurrentOperationStatus": current_operation_status,
                "StatusMessage": status_message,
                "ErrorCode": error_code,
                "ResourceModel": resource_model,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_record_handler_progress(
        self,
        *,
        action: PostRecordHandlerProgressRequestAction,
        version: PostRecordHandlerProgressRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>

        Parameters
        ----------
        action : PostRecordHandlerProgressRequestAction

        version : PostRecordHandlerProgressRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RecordHandlerProgress",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_register_publisher(
        self,
        *,
        action: GetRegisterPublisherRequestAction,
        version: GetRegisterPublisherRequestVersion,
        accept_terms_and_conditions: typing.Optional[bool] = None,
        connection_arn: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>

        Parameters
        ----------
        action : GetRegisterPublisherRequestAction

        version : GetRegisterPublisherRequestVersion

        accept_terms_and_conditions : typing.Optional[bool]
            <p>Whether you accept the <a href="https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf">Terms and Conditions</a> for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.</p> <p>The default is <code>false</code>.</p>

        connection_arn : typing.Optional[str]
            <p>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RegisterPublisher",
            method="GET",
            params={
                "AcceptTermsAndConditions": accept_terms_and_conditions,
                "ConnectionArn": connection_arn,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_register_publisher(
        self,
        *,
        action: PostRegisterPublisherRequestAction,
        version: PostRegisterPublisherRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>

        Parameters
        ----------
        action : PostRegisterPublisherRequestAction

        version : PostRegisterPublisherRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RegisterPublisher",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_register_type(
        self,
        *,
        type_name: str,
        schema_handler_package: str,
        action: GetRegisterTypeRequestAction,
        version: GetRegisterTypeRequestVersion,
        type: typing.Optional[GetRegisterTypeRequestType] = None,
        logging_config: typing.Optional[GetRegisterTypeRequestLoggingConfig] = None,
        execution_role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        type_name : str
            <p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <i>company_or_organization</i>::<i>service</i>::<i>type</i>.</p> </li> <li> <p>For modules, <i>company_or_organization</i>::<i>service</i>::<i>type</i>::MODULE.</p> </li> <li> <p>For hooks, <i>MyCompany</i>::<i>Testing</i>::<i>MyTestHook</i>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>

        schema_handler_package : str
            <p>A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation CLI User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>

        action : GetRegisterTypeRequestAction

        version : GetRegisterTypeRequestVersion

        type : typing.Optional[GetRegisterTypeRequestType]
            The kind of extension.

        logging_config : typing.Optional[GetRegisterTypeRequestLoggingConfig]
            Specifies logging configuration information for an extension.

        execution_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>

        client_request_token : typing.Optional[str]
            A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RegisterType",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "SchemaHandlerPackage": schema_handler_package,
                "LoggingConfig": convert_and_respect_annotation_metadata(
                    object_=logging_config, annotation=GetRegisterTypeRequestLoggingConfig, direction="write"
                ),
                "ExecutionRoleArn": execution_role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_register_type(
        self,
        *,
        action: PostRegisterTypeRequestAction,
        version: PostRegisterTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostRegisterTypeRequestAction

        version : PostRegisterTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RegisterType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_rollback_stack(
        self,
        *,
        stack_name: str,
        action: GetRollbackStackRequestAction,
        version: GetRollbackStackRequestVersion,
        role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>

        Parameters
        ----------
        stack_name : str
            The name that's associated with the stack.

        action : GetRollbackStackRequestAction

        version : GetRollbackStackRequestVersion

        role_arn : typing.Optional[str]
            The Amazon Resource Name (ARN) of an Identity and Access Management role that CloudFormation assumes to rollback the stack.

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>RollbackStack</code> request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RollbackStack",
            method="GET",
            params={
                "StackName": stack_name,
                "RoleARN": role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_rollback_stack(
        self,
        *,
        action: PostRollbackStackRequestAction,
        version: PostRollbackStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>

        Parameters
        ----------
        action : PostRollbackStackRequestAction

        version : PostRollbackStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=RollbackStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_set_stack_policy(
        self,
        *,
        stack_name: str,
        action: GetSetStackPolicyRequestAction,
        version: GetSetStackPolicyRequestVersion,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Sets a stack policy for a specified stack.

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID that you want to associate a policy with.

        action : GetSetStackPolicyRequestAction

        version : GetSetStackPolicyRequestVersion

        stack_policy_body : typing.Optional[str]
            Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent updates to stack resources</a> in the CloudFormation User Guide. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        stack_policy_url : typing.Optional[str]
            Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetStackPolicy",
            method="GET",
            params={
                "StackName": stack_name,
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_set_stack_policy(
        self,
        *,
        action: PostSetStackPolicyRequestAction,
        version: PostSetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Sets a stack policy for a specified stack.

        Parameters
        ----------
        action : PostSetStackPolicyRequestAction

        version : PostSetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetStackPolicy",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_set_type_configuration(
        self,
        *,
        configuration: str,
        action: GetSetTypeConfigurationRequestAction,
        version: GetSetTypeConfigurationRequestVersion,
        type_arn: typing.Optional[str] = None,
        configuration_alias: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        type: typing.Optional[GetSetTypeConfigurationRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>

        Parameters
        ----------
        configuration : str
            <p>The configuration data for the extension, in this account and region.</p> <p>The configuration data must be formatted as JSON, and validate against the schema returned in the <code>ConfigurationSchema</code> response element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">API_DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining account-level configuration data for an extension</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        action : GetSetTypeConfigurationRequestAction

        version : GetSetTypeConfigurationRequestVersion

        type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>

        configuration_alias : typing.Optional[str]
            <p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>

        type : typing.Optional[GetSetTypeConfigurationRequestType]
            <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetTypeConfiguration",
            method="GET",
            params={
                "TypeArn": type_arn,
                "Configuration": configuration,
                "ConfigurationAlias": configuration_alias,
                "TypeName": type_name,
                "Type": type,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_set_type_configuration(
        self,
        *,
        action: PostSetTypeConfigurationRequestAction,
        version: PostSetTypeConfigurationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>

        Parameters
        ----------
        action : PostSetTypeConfigurationRequestAction

        version : PostSetTypeConfigurationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetTypeConfiguration",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_set_type_default_version(
        self,
        *,
        action: GetSetTypeDefaultVersionRequestAction,
        version: GetSetTypeDefaultVersionRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetSetTypeDefaultVersionRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

        Parameters
        ----------
        action : GetSetTypeDefaultVersionRequestAction

        version : GetSetTypeDefaultVersionRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type : typing.Optional[GetSetTypeDefaultVersionRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetTypeDefaultVersion",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_set_type_default_version(
        self,
        *,
        action: PostSetTypeDefaultVersionRequestAction,
        version: PostSetTypeDefaultVersionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

        Parameters
        ----------
        action : PostSetTypeDefaultVersionRequestAction

        version : PostSetTypeDefaultVersionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SetTypeDefaultVersion",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_signal_resource(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        unique_id: str,
        status: GetSignalResourceRequestStatus,
        action: GetSignalResourceRequestAction,
        version: GetSignalResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

        Parameters
        ----------
        stack_name : str
            The stack name or unique stack ID that includes the resource that you want to signal.

        logical_resource_id : str
            The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.

        unique_id : str
            A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.

        status : GetSignalResourceRequestStatus
            The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.

        action : GetSignalResourceRequestAction

        version : GetSignalResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SignalResource",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "UniqueId": unique_id,
                "Status": status,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_signal_resource(
        self,
        *,
        action: PostSignalResourceRequestAction,
        version: PostSignalResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

        Parameters
        ----------
        action : PostSignalResourceRequestAction

        version : PostSignalResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=SignalResource",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_stop_stack_set_operation(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetStopStackSetOperationRequestAction,
        version: GetStopStackSetOperationRequestVersion,
        call_as: typing.Optional[GetStopStackSetOperationRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to stop the operation for.

        operation_id : str
            The ID of the stack operation.

        action : GetStopStackSetOperationRequestAction

        version : GetStopStackSetOperationRequestVersion

        call_as : typing.Optional[GetStopStackSetOperationRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=StopStackSetOperation",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_stop_stack_set_operation(
        self,
        *,
        action: PostStopStackSetOperationRequestAction,
        version: PostStopStackSetOperationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

        Parameters
        ----------
        action : PostStopStackSetOperationRequestAction

        version : PostStopStackSetOperationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=StopStackSetOperation",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_test_type(
        self,
        *,
        action: GetTestTypeRequestAction,
        version: GetTestTypeRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetTestTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        log_delivery_bucket: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        Parameters
        ----------
        action : GetTestTypeRequestAction

        version : GetTestTypeRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type : typing.Optional[GetTestTypeRequestType]
            <p>The type of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        version_id : typing.Optional[str]
            <p>The version of the extension to test.</p> <p>You can specify the version id with either <code>Arn</code>, or with <code>TypeName</code> and <code>Type</code>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in this account and region for testing.</p>

        log_delivery_bucket : typing.Optional[str]
            <p>The S3 bucket to which CloudFormation delivers the contract test execution logs.</p> <p>CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of <code>PASSED</code> or <code>FAILED</code>.</p> <p>The user calling <code>TestType</code> must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:</p> <ul> <li> <p> <code>GetObject</code> </p> </li> <li> <p> <code>PutObject</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=TestType",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "LogDeliveryBucket": log_delivery_bucket,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_test_type(
        self,
        *,
        action: PostTestTypeRequestAction,
        version: PostTestTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        Parameters
        ----------
        action : PostTestTypeRequestAction

        version : PostTestTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=TestType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_update_stack(
        self,
        *,
        stack_name: str,
        action: GetUpdateStackRequestAction,
        version: GetUpdateStackRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        stack_policy_during_update_body: typing.Optional[str] = None,
        stack_policy_during_update_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        rollback_configuration: typing.Optional[GetUpdateStackRequestRollbackConfiguration] = None,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        disable_rollback: typing.Optional[bool] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID of the stack to update.

        action : GetUpdateStackRequestAction

        version : GetUpdateStackRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        use_previous_template : typing.Optional[bool]
            <p>Reuse the existing template that is associated with the stack that you are updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        stack_policy_during_update_body : typing.Optional[str]
            <p>Structure containing the temporary overriding stack policy body. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>

        stack_policy_during_update_url : typing.Optional[str]
            <p>Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to update a stack from a stack template that contains macros <i>and</i> nested stacks, you must update the stack directly from the template using this capability.</p> <important> <p>You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with for this update stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to update the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>

        rollback_configuration : typing.Optional[GetUpdateStackRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        stack_policy_body : typing.Optional[str]
            <p>Structure containing a new stack policy body. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>

        stack_policy_url : typing.Optional[str]
            <p>Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.</p> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you specify an empty value, CloudFormation removes all associated tags.</p>

        disable_rollback : typing.Optional[bool]
            <p>Preserve the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>False</code> </p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>UpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to update a stack with the same name. You might retry <code>UpdateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "StackPolicyDuringUpdateBody": stack_policy_during_update_body,
                "StackPolicyDuringUpdateURL": stack_policy_during_update_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetUpdateStackRequestRollbackConfiguration,
                    direction="write",
                ),
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "NotificationARNs": notification_ar_ns,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "DisableRollback": disable_rollback,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_update_stack(
        self,
        *,
        action: PostUpdateStackRequestAction,
        version: PostUpdateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>

        Parameters
        ----------
        action : PostUpdateStackRequestAction

        version : PostUpdateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_update_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetUpdateStackInstancesRequestAction,
        version: GetUpdateStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetUpdateStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        parameter_overrides: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        operation_preferences: typing.Optional[GetUpdateStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetUpdateStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set associated with the stack instances.

        action : GetUpdateStackInstancesRequestAction

        version : GetUpdateStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetUpdateStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won't use the overridden values.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.

        parameter_overrides : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            <p>A list of input parameters whose values you want to update for the specified stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <code>UpdateStackSet</code> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        operation_preferences : typing.Optional[GetUpdateStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>

        call_as : typing.Optional[GetUpdateStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetUpdateStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "ParameterOverrides": convert_and_respect_annotation_metadata(
                    object_=parameter_overrides, annotation=Parameter, direction="write"
                ),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetUpdateStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_update_stack_instances(
        self,
        *,
        action: PostUpdateStackInstancesRequestAction,
        version: PostUpdateStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        Parameters
        ----------
        action : PostUpdateStackInstancesRequestAction

        version : PostUpdateStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_update_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetUpdateStackSetRequestAction,
        version: GetUpdateStackSetRequestVersion,
        description: typing.Optional[str] = None,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        operation_preferences: typing.Optional[GetUpdateStackSetRequestOperationPreferences] = None,
        administration_role_arn: typing.Optional[str] = None,
        execution_role_name: typing.Optional[str] = None,
        deployment_targets: typing.Optional[GetUpdateStackSetRequestDeploymentTargets] = None,
        permission_model: typing.Optional[GetUpdateStackSetRequestPermissionModel] = None,
        auto_deployment: typing.Optional[GetUpdateStackSetRequestAutoDeployment] = None,
        operation_id: typing.Optional[str] = None,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        call_as: typing.Optional[GetUpdateStackSetRequestCallAs] = None,
        managed_execution: typing.Optional[GetUpdateStackSetRequestManagedExecution] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to update.

        action : GetUpdateStackSetRequestAction

        version : GetUpdateStackSetRequestVersion

        description : typing.Optional[str]
            A brief description of updates that you are making.

        template_body : typing.Optional[str]
            <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        use_previous_template : typing.Optional[bool]
            <p>Use the existing template that's associated with the stack set that you're updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of input parameters for the stack set template.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack set and its associated stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html"> AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html"> AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must update the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To update the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions do not currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.</p> <p>If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:</p> <ul> <li> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags.</p> </li> <li> <p>If you specify <i>any</i> tags using this parameter, you must specify <i>all</i> the tags that you want associated with this stack set, even tags you've specified before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don't include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.</p> </li> <li> <p>If you specify an empty value, CloudFormation removes all currently associated tags.</p> </li> </ul> <p>If you specify new tags as part of an <code>UpdateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire <code>UpdateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not updated.</p>

        operation_preferences : typing.Optional[GetUpdateStackSetRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        administration_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role to use to update this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.</p>

        execution_role_name : typing.Optional[str]
            <p>The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p> <p>If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.</p>

        deployment_targets : typing.Optional[GetUpdateStackSetRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts in which to update associated stack instances.</p> <p>To update all the stack instances associated with this stack set, do not specify <code>DeploymentTargets</code> or <code>Regions</code>.</p> <p>If the stack set update includes changes to the template (that is, if <code>TemplateBody</code> or <code>TemplateURL</code> is specified), or the <code>Parameters</code>, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update doesn't include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>

        permission_model : typing.Optional[GetUpdateStackSetRequestPermissionModel]
            <p>Describes how the IAM roles required for stack set operations are created. You cannot modify <code>PermissionModel</code> if there are stack instances associated with your stack set.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>

        auto_deployment : typing.Optional[GetUpdateStackSetRequestAutoDeployment]
            <p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).</p> <p>If you specify <code>AutoDeployment</code>, don't specify <code>DeploymentTargets</code> or <code>Regions</code>.</p>

        operation_id : typing.Optional[str]
            <p>The unique ID for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, CloudFormation generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, don't specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            <p>The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, do not specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>

        call_as : typing.Optional[GetUpdateStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        managed_execution : typing.Optional[GetUpdateStackSetRequestManagedExecution]
            Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Description": description,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetUpdateStackSetRequestOperationPreferences,
                    direction="write",
                ),
                "AdministrationRoleARN": administration_role_arn,
                "ExecutionRoleName": execution_role_name,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets, annotation=GetUpdateStackSetRequestDeploymentTargets, direction="write"
                ),
                "PermissionModel": permission_model,
                "AutoDeployment": convert_and_respect_annotation_metadata(
                    object_=auto_deployment, annotation=GetUpdateStackSetRequestAutoDeployment, direction="write"
                ),
                "OperationId": operation_id,
                "Accounts": accounts,
                "Regions": regions,
                "CallAs": call_as,
                "ManagedExecution": convert_and_respect_annotation_metadata(
                    object_=managed_execution, annotation=GetUpdateStackSetRequestManagedExecution, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_update_stack_set(
        self,
        *,
        action: PostUpdateStackSetRequestAction,
        version: PostUpdateStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>

        Parameters
        ----------
        action : PostUpdateStackSetRequestAction

        version : PostUpdateStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_update_termination_protection(
        self,
        *,
        enable_termination_protection: bool,
        stack_name: str,
        action: GetUpdateTerminationProtectionRequestAction,
        version: GetUpdateTerminationProtectionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        Parameters
        ----------
        enable_termination_protection : bool
            Whether to enable termination protection on the specified stack.

        stack_name : str
            The name or unique ID of the stack for which you want to set termination protection.

        action : GetUpdateTerminationProtectionRequestAction

        version : GetUpdateTerminationProtectionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateTerminationProtection",
            method="GET",
            params={
                "EnableTerminationProtection": enable_termination_protection,
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_update_termination_protection(
        self,
        *,
        action: PostUpdateTerminationProtectionRequestAction,
        version: PostUpdateTerminationProtectionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        <p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        Parameters
        ----------
        action : PostUpdateTerminationProtectionRequestAction

        version : PostUpdateTerminationProtectionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=UpdateTerminationProtection",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_validate_template(
        self,
        *,
        action: GetValidateTemplateRequestAction,
        version: GetValidateTemplateRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

        Parameters
        ----------
        action : GetValidateTemplateRequestAction

        version : GetValidateTemplateRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ValidateTemplate",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_validate_template(
        self,
        *,
        action: PostValidateTemplateRequestAction,
        version: PostValidateTemplateRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

        Parameters
        ----------
        action : PostValidateTemplateRequestAction

        version : PostValidateTemplateRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Action=ValidateTemplate",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_activate_type(
        self,
        *,
        action: GetActivateTypeRequestAction,
        version: GetActivateTypeRequestVersion,
        type: typing.Optional[GetActivateTypeRequestType] = None,
        public_type_arn: typing.Optional[str] = None,
        publisher_id: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        type_name_alias: typing.Optional[str] = None,
        auto_update: typing.Optional[bool] = None,
        logging_config: typing.Optional[GetActivateTypeRequestLoggingConfig] = None,
        execution_role_arn: typing.Optional[str] = None,
        version_bump: typing.Optional[GetActivateTypeRequestVersionBump] = None,
        major_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : GetActivateTypeRequestAction

        version : GetActivateTypeRequestVersion

        type : typing.Optional[GetActivateTypeRequestType]
            <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        public_type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        publisher_id : typing.Optional[str]
            <p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>

        type_name_alias : typing.Optional[str]
            <p>An alias to assign to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and region. You can activate the same public resource multiple times in the same account and region, using different type name aliases.</p>

        auto_update : typing.Optional[bool]
            <p>Whether to automatically update the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>

        logging_config : typing.Optional[GetActivateTypeRequestLoggingConfig]


        execution_role_arn : typing.Optional[str]
            The name of the IAM execution role to use to activate the extension.

        version_bump : typing.Optional[GetActivateTypeRequestVersionBump]
            <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>

        major_version : typing.Optional[int]
            <p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ActivateType",
            method="GET",
            params={
                "Type": type,
                "PublicTypeArn": public_type_arn,
                "PublisherId": publisher_id,
                "TypeName": type_name,
                "TypeNameAlias": type_name_alias,
                "AutoUpdate": auto_update,
                "LoggingConfig": convert_and_respect_annotation_metadata(
                    object_=logging_config, annotation=GetActivateTypeRequestLoggingConfig, direction="write"
                ),
                "ExecutionRoleArn": execution_role_arn,
                "VersionBump": version_bump,
                "MajorVersion": major_version,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_activate_type(
        self,
        *,
        action: PostActivateTypeRequestAction,
        version: PostActivateTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostActivateTypeRequestAction

        version : PostActivateTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ActivateType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_batch_describe_type_configurations(
        self,
        *,
        action: GetBatchDescribeTypeConfigurationsRequestAction,
        version: GetBatchDescribeTypeConfigurationsRequestVersion,
        type_configuration_identifiers: typing.Optional[
            typing.Union[TypeConfigurationIdentifier, typing.Sequence[TypeConfigurationIdentifier]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : GetBatchDescribeTypeConfigurationsRequestAction

        version : GetBatchDescribeTypeConfigurationsRequestVersion

        type_configuration_identifiers : typing.Optional[typing.Union[TypeConfigurationIdentifier, typing.Sequence[TypeConfigurationIdentifier]]]
            The list of identifiers for the desired extension configurations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=BatchDescribeTypeConfigurations",
            method="GET",
            params={
                "TypeConfigurationIdentifiers": convert_and_respect_annotation_metadata(
                    object_=type_configuration_identifiers, annotation=TypeConfigurationIdentifier, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_batch_describe_type_configurations(
        self,
        *,
        action: PostBatchDescribeTypeConfigurationsRequestAction,
        version: PostBatchDescribeTypeConfigurationsRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostBatchDescribeTypeConfigurationsRequestAction

        version : PostBatchDescribeTypeConfigurationsRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=BatchDescribeTypeConfigurations",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_cancel_update_stack(
        self,
        *,
        stack_name: str,
        action: GetCancelUpdateStackRequestAction,
        version: GetCancelUpdateStackRequestVersion,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        <p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>

        Parameters
        ----------
        stack_name : str
            The name or the unique stack ID that's associated with the stack.

        action : GetCancelUpdateStackRequestAction

        version : GetCancelUpdateStackRequestVersion

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CancelUpdateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_cancel_update_stack(
        self,
        *,
        action: PostCancelUpdateStackRequestAction,
        version: PostCancelUpdateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        <p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>

        Parameters
        ----------
        action : PostCancelUpdateStackRequestAction

        version : PostCancelUpdateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CancelUpdateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_continue_update_rollback(
        self,
        *,
        stack_name: str,
        action: GetContinueUpdateRollbackRequestAction,
        version: GetContinueUpdateRollbackRequestVersion,
        role_arn: typing.Optional[str] = None,
        resources_to_skip: typing.Optional[typing.Union[ResourceToSkip, typing.Sequence[ResourceToSkip]]] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique ID of the stack that you want to continue rolling back.</p> <note> <p>Don't specify the name of a nested stack (a stack that was created by using the <code>AWS::CloudFormation::Stack</code> resource). Instead, use this operation on the parent stack (the stack that contains the <code>AWS::CloudFormation::Stack</code> resource).</p> </note>

        action : GetContinueUpdateRollbackRequestAction

        version : GetContinueUpdateRollbackRequestVersion

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to roll back the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        resources_to_skip : typing.Optional[typing.Union[ResourceToSkip, typing.Sequence[ResourceToSkip]]]
            <p>A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the <code>UPDATE_FAILED</code> state because a rollback failed. You can't specify resources that are in the <code>UPDATE_FAILED</code> state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the <a>DescribeStackResources</a> action, and view the resource status reason.</p> <important> <p>Specify this property to skip rolling back resources that CloudFormation can't successfully roll back. We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> troubleshoot</a> resources before skipping them. CloudFormation sets the status of the specified resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> </important> <p>Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.</p> <p>To skip resources that are part of nested stacks, use the following format: <code>NestedStackName.ResourceLogicalID</code>. If you want to specify the logical ID of a stack resource (<code>Type: AWS::CloudFormation::Stack</code>) in the <code>ResourcesToSkip</code> list, then its corresponding embedded stack must be in one of the following states: <code>DELETE_IN_PROGRESS</code>, <code>DELETE_COMPLETE</code>, or <code>DELETE_FAILED</code>.</p> <note> <p>Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks">Using ResourcesToSkip to recover a nested stacks hierarchy</a>.</p> </note>

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>ContinueUpdateRollback</code> request. Specify this token if you plan to retry requests so that CloudFormationknows that you're not attempting to continue the rollback to a stack with the same name. You might retry <code>ContinueUpdateRollback</code> requests to ensure that CloudFormation successfully received them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ContinueUpdateRollback",
            method="GET",
            params={
                "StackName": stack_name,
                "RoleARN": role_arn,
                "ResourcesToSkip": resources_to_skip,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_continue_update_rollback(
        self,
        *,
        action: PostContinueUpdateRollbackRequestAction,
        version: PostContinueUpdateRollbackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>

        Parameters
        ----------
        action : PostContinueUpdateRollbackRequestAction

        version : PostContinueUpdateRollbackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ContinueUpdateRollback",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_create_change_set(
        self,
        *,
        stack_name: str,
        change_set_name: str,
        action: GetCreateChangeSetRequestAction,
        version: GetCreateChangeSetRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        rollback_configuration: typing.Optional[GetCreateChangeSetRequestRollbackConfiguration] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        client_token: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        change_set_type: typing.Optional[GetCreateChangeSetRequestChangeSetType] = None,
        resources_to_import: typing.Optional[typing.Union[ResourceToImport, typing.Sequence[ResourceToImport]]] = None,
        include_nested_stacks: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>

        Parameters
        ----------
        stack_name : str
            The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.

        change_set_name : str
            <p>The name of the change set. The name must be unique among all change sets that are associated with the specified stack.</p> <p>A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.</p>

        action : GetCreateChangeSetRequestAction

        version : GetCreateChangeSetRequestVersion

        template_body : typing.Optional[str]
            <p>A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>

        use_previous_template : typing.Optional[bool]
            Whether to reuse the template that's associated with the stack to create the change set.

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the change set. For more information, see the <a>Parameter</a> data type.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <note> <p>This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create or update the stack directly from the template using the <a>CreateStack</a> or <a>UpdateStack</a> action, and specifying this capability.</p> </note> <p>For more information about macros, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with if you execute this change set, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling access with Identity and Access Management</a> in the CloudFormation User Guide.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>

        rollback_configuration : typing.Optional[GetCreateChangeSetRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.

        client_token : typing.Optional[str]
            A unique identifier for this <code>CreateChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another change set with the same name. You might retry <code>CreateChangeSet</code> requests to ensure that CloudFormation successfully received them.

        description : typing.Optional[str]
            A description to help you identify this change set.

        change_set_type : typing.Optional[GetCreateChangeSetRequestChangeSetType]
            <p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995"> <code>REVIEW_IN_PROGRESS</code> </a> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>

        resources_to_import : typing.Optional[typing.Union[ResourceToImport, typing.Sequence[ResourceToImport]]]
            The resources to import into your stack.

        include_nested_stacks : typing.Optional[bool]
            Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to <code>False</code>. To include nested sets in a change set, specify <code>True</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateChangeSet",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetCreateChangeSetRequestRollbackConfiguration,
                    direction="write",
                ),
                "NotificationARNs": notification_ar_ns,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "ChangeSetName": change_set_name,
                "ClientToken": client_token,
                "Description": description,
                "ChangeSetType": change_set_type,
                "ResourcesToImport": convert_and_respect_annotation_metadata(
                    object_=resources_to_import, annotation=ResourceToImport, direction="write"
                ),
                "IncludeNestedStacks": include_nested_stacks,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_create_change_set(
        self,
        *,
        action: PostCreateChangeSetRequestAction,
        version: PostCreateChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>

        Parameters
        ----------
        action : PostCreateChangeSetRequestAction

        version : PostCreateChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_create_stack(
        self,
        *,
        stack_name: str,
        action: GetCreateStackRequestAction,
        version: GetCreateStackRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        disable_rollback: typing.Optional[bool] = None,
        rollback_configuration: typing.Optional[GetCreateStackRequestRollbackConfiguration] = None,
        timeout_in_minutes: typing.Optional[int] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        on_failure: typing.Optional[GetCreateStackRequestOnFailure] = None,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        client_request_token: typing.Optional[str] = None,
        enable_termination_protection: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.

        Parameters
        ----------
        stack_name : str
            <p>The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.</p> <note> <p>A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.</p> </note>

        action : GetCreateStackRequestAction

        version : GetCreateStackRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.

        disable_rollback : typing.Optional[bool]
            <p>Set to <code>true</code> to disable rollback of the stack if stack creation failed. You can specify either <code>DisableRollback</code> or <code>OnFailure</code>, but not both.</p> <p>Default: <code>false</code> </p>

        rollback_configuration : typing.Optional[GetCreateStackRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        timeout_in_minutes : typing.Optional[int]
            The amount of time that can pass before the stack status becomes CREATE_FAILED; if <code>DisableRollback</code> is not set or is set to <code>false</code>, the stack will be rolled back.

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create the stack directly from the template using this capability.</p> <important> <p>You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with for this create stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>. Use the following syntax to describe template resource types: <code>AWS::*</code> (for all Amazon Web Services resources), <code>Custom::*</code> (for all custom resources), <code>Custom::<i>logical_ID</i> </code> (for a specific custom resource), <code>AWS::<i>service_name</i>::*</code> (for all resources of a particular Amazon Web Services service), and <code>AWS::<i>service_name</i>::<i>resource_logical_ID</i> </code> (for a specific Amazon Web Services resource).</p> <p>If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        on_failure : typing.Optional[GetCreateStackRequestOnFailure]
            <p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <p>Default: <code>ROLLBACK</code> </p>

        stack_policy_body : typing.Optional[str]
            Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent Updates to Stack Resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        stack_policy_url : typing.Optional[str]
            Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>CreateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create a stack with the same name. You might retry <code>CreateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        enable_termination_protection : typing.Optional[bool]
            <p>Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>. Termination protection is deactivated on stacks by default.</p> <p>For <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "DisableRollback": disable_rollback,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetCreateStackRequestRollbackConfiguration,
                    direction="write",
                ),
                "TimeoutInMinutes": timeout_in_minutes,
                "NotificationARNs": notification_ar_ns,
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "OnFailure": on_failure,
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "ClientRequestToken": client_request_token,
                "EnableTerminationProtection": enable_termination_protection,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_create_stack(
        self,
        *,
        action: PostCreateStackRequestAction,
        version: PostCreateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.

        Parameters
        ----------
        action : PostCreateStackRequestAction

        version : PostCreateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_create_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetCreateStackInstancesRequestAction,
        version: GetCreateStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetCreateStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        parameter_overrides: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        operation_preferences: typing.Optional[GetCreateStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetCreateStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to create stack instances from.

        action : GetCreateStackInstancesRequestAction

        version : GetCreateStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetCreateStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.

        parameter_overrides : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            <p>A list of stack set parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template.</p>

        operation_preferences : typing.Optional[GetCreateStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        call_as : typing.Optional[GetCreateStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetCreateStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "ParameterOverrides": convert_and_respect_annotation_metadata(
                    object_=parameter_overrides, annotation=Parameter, direction="write"
                ),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetCreateStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_create_stack_instances(
        self,
        *,
        action: PostCreateStackInstancesRequestAction,
        version: PostCreateStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.

        Parameters
        ----------
        action : PostCreateStackInstancesRequestAction

        version : PostCreateStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_create_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetCreateStackSetRequestAction,
        version: GetCreateStackSetRequestVersion,
        description: typing.Optional[str] = None,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        stack_id: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        administration_role_arn: typing.Optional[str] = None,
        execution_role_name: typing.Optional[str] = None,
        permission_model: typing.Optional[GetCreateStackSetRequestPermissionModel] = None,
        auto_deployment: typing.Optional[GetCreateStackSetRequestAutoDeployment] = None,
        call_as: typing.Optional[GetCreateStackSetRequestCallAs] = None,
        client_request_token: typing.Optional[str] = None,
        managed_execution: typing.Optional[GetCreateStackSetRequestManagedExecution] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates a stack set.

        Parameters
        ----------
        stack_set_name : str
            <p>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>

        action : GetCreateStackSetRequestAction

        version : GetCreateStackSetRequestVersion

        description : typing.Optional[str]
            A description of the stack set. You can use the description to identify the stack set's purpose or other important information.

        template_body : typing.Optional[str]
            <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>

        stack_id : typing.Optional[str]
            The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            The input parameters for the stack set template.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not created.</p>

        administration_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>

        execution_role_name : typing.Optional[str]
            <p>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p>

        permission_model : typing.Optional[GetCreateStackSetRequestPermissionModel]
            <p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>

        auto_deployment : typing.Optional[GetCreateStackSetRequestAutoDeployment]
            Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>.

        call_as : typing.Optional[GetCreateStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>To create a stack set with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.</p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>

        managed_execution : typing.Optional[GetCreateStackSetRequestManagedExecution]
            Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Description": description,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "StackId": stack_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "AdministrationRoleARN": administration_role_arn,
                "ExecutionRoleName": execution_role_name,
                "PermissionModel": permission_model,
                "AutoDeployment": convert_and_respect_annotation_metadata(
                    object_=auto_deployment, annotation=GetCreateStackSetRequestAutoDeployment, direction="write"
                ),
                "CallAs": call_as,
                "ClientRequestToken": client_request_token,
                "ManagedExecution": convert_and_respect_annotation_metadata(
                    object_=managed_execution, annotation=GetCreateStackSetRequestManagedExecution, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_create_stack_set(
        self,
        *,
        action: PostCreateStackSetRequestAction,
        version: PostCreateStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates a stack set.

        Parameters
        ----------
        action : PostCreateStackSetRequestAction

        version : PostCreateStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=CreateStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_deactivate_type(
        self,
        *,
        action: GetDeactivateTypeRequestAction,
        version: GetDeactivateTypeRequestVersion,
        type_name: typing.Optional[str] = None,
        type: typing.Optional[GetDeactivateTypeRequestType] = None,
        arn: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>

        Parameters
        ----------
        action : GetDeactivateTypeRequestAction

        version : GetDeactivateTypeRequestVersion

        type_name : typing.Optional[str]
            <p>The type name of the extension, in this account and region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type : typing.Optional[GetDeactivateTypeRequestType]
            <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeactivateType",
            method="GET",
            params={
                "TypeName": type_name,
                "Type": type,
                "Arn": arn,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_deactivate_type(
        self,
        *,
        action: PostDeactivateTypeRequestAction,
        version: PostDeactivateTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>

        Parameters
        ----------
        action : PostDeactivateTypeRequestAction

        version : PostDeactivateTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeactivateType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_delete_change_set(
        self,
        *,
        change_set_name: str,
        action: GetDeleteChangeSetRequestAction,
        version: GetDeleteChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to delete.

        action : GetDeleteChangeSetRequestAction

        version : GetDeleteChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_delete_change_set(
        self,
        *,
        action: PostDeleteChangeSetRequestAction,
        version: PostDeleteChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>

        Parameters
        ----------
        action : PostDeleteChangeSetRequestAction

        version : PostDeleteChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_delete_stack(
        self,
        *,
        stack_name: str,
        action: GetDeleteStackRequestAction,
        version: GetDeleteStackRequestVersion,
        retain_resources: typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]] = None,
        role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.

        Parameters
        ----------
        stack_name : str
            The name or the unique stack ID that's associated with the stack.

        action : GetDeleteStackRequestAction

        version : GetDeleteStackRequestVersion

        retain_resources : typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]
            <p>For stacks in the <code>DELETE_FAILED</code> state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, CloudFormation deletes the stack but doesn't delete the retained resources.</p> <p>Retaining resources is useful when you can't delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to delete the stack. CloudFormation uses the role's credentials to make calls on your behalf.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>DeleteStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to delete a stack with the same name. You might retry <code>DeleteStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStack",
            method="GET",
            params={
                "StackName": stack_name,
                "RetainResources": retain_resources,
                "RoleARN": role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_delete_stack(
        self,
        *,
        action: PostDeleteStackRequestAction,
        version: PostDeleteStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.

        Parameters
        ----------
        action : PostDeleteStackRequestAction

        version : PostDeleteStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_delete_stack_instances(
        self,
        *,
        stack_set_name: str,
        retain_stacks: bool,
        action: GetDeleteStackInstancesRequestAction,
        version: GetDeleteStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetDeleteStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        operation_preferences: typing.Optional[GetDeleteStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetDeleteStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to delete stack instances for.

        retain_stacks : bool
            <p>Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack set operation options</a>.</p>

        action : GetDeleteStackInstancesRequestAction

        version : GetDeleteStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetDeleteStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The Amazon Web Services Regions where you want to delete stack set instances.

        operation_preferences : typing.Optional[GetDeleteStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        call_as : typing.Optional[GetDeleteStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetDeleteStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetDeleteStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "RetainStacks": retain_stacks,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_delete_stack_instances(
        self,
        *,
        action: PostDeleteStackInstancesRequestAction,
        version: PostDeleteStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

        Parameters
        ----------
        action : PostDeleteStackInstancesRequestAction

        version : PostDeleteStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_delete_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetDeleteStackSetRequestAction,
        version: GetDeleteStackSetRequestVersion,
        call_as: typing.Optional[GetDeleteStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you're deleting. You can obtain this value by running <a>ListStackSets</a>.

        action : GetDeleteStackSetRequestAction

        version : GetDeleteStackSetRequestVersion

        call_as : typing.Optional[GetDeleteStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_delete_stack_set(
        self,
        *,
        action: PostDeleteStackSetRequestAction,
        version: PostDeleteStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.

        Parameters
        ----------
        action : PostDeleteStackSetRequestAction

        version : PostDeleteStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeleteStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_deregister_type(
        self,
        *,
        action: GetDeregisterTypeRequestAction,
        version: GetDeregisterTypeRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetDeregisterTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>

        Parameters
        ----------
        action : GetDeregisterTypeRequestAction

        version : GetDeregisterTypeRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type : typing.Optional[GetDeregisterTypeRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeregisterType",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_deregister_type(
        self,
        *,
        action: PostDeregisterTypeRequestAction,
        version: PostDeregisterTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>

        Parameters
        ----------
        action : PostDeregisterTypeRequestAction

        version : PostDeregisterTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DeregisterType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_account_limits(
        self,
        *,
        action: GetDescribeAccountLimitsRequestAction,
        version: GetDescribeAccountLimitsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.

        Parameters
        ----------
        action : GetDescribeAccountLimitsRequestAction

        version : GetDescribeAccountLimitsRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of limits that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeAccountLimits",
            method="GET",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_account_limits(
        self,
        *,
        action: PostDescribeAccountLimitsRequestAction,
        version: PostDescribeAccountLimitsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.

        Parameters
        ----------
        action : PostDescribeAccountLimitsRequestAction

        version : PostDescribeAccountLimitsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeAccountLimits",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_change_set(
        self,
        *,
        change_set_name: str,
        action: GetDescribeChangeSetRequestAction,
        version: GetDescribeChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.

        action : GetDescribeChangeSetRequestAction

        version : GetDescribeChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.

        next_token : typing.Optional[str]
            A string (provided by the <a>DescribeChangeSet</a> response output) that identifies the next page of information that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_change_set(
        self,
        *,
        action: PostDescribeChangeSetRequestAction,
        version: PostDescribeChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.

        Parameters
        ----------
        action : PostDescribeChangeSetRequestAction

        version : PostDescribeChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_change_set_hooks(
        self,
        *,
        change_set_name: str,
        action: GetDescribeChangeSetHooksRequestAction,
        version: GetDescribeChangeSetHooksRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        logical_resource_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.

        action : GetDescribeChangeSetHooksRequestAction

        version : GetDescribeChangeSetHooksRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.

        next_token : typing.Optional[str]
            A string, provided by the <code>DescribeChangeSetHooks</code> response output, that identifies the next page of information that you want to retrieve.

        logical_resource_id : typing.Optional[str]
            If specified, lists only the hooks related to the specified <code>LogicalResourceId</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSetHooks",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "NextToken": next_token,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_change_set_hooks(
        self,
        *,
        action: PostDescribeChangeSetHooksRequestAction,
        version: PostDescribeChangeSetHooksRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

        Parameters
        ----------
        action : PostDescribeChangeSetHooksRequestAction

        version : PostDescribeChangeSetHooksRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeChangeSetHooks",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_publisher(
        self,
        *,
        action: GetDescribePublisherRequestAction,
        version: GetDescribePublisherRequestVersion,
        publisher_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>

        Parameters
        ----------
        action : GetDescribePublisherRequestAction

        version : GetDescribePublisherRequestVersion

        publisher_id : typing.Optional[str]
            <p>The ID of the extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribePublisher",
            method="GET",
            params={
                "PublisherId": publisher_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_publisher(
        self,
        *,
        action: PostDescribePublisherRequestAction,
        version: PostDescribePublisherRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>

        Parameters
        ----------
        action : PostDescribePublisherRequestAction

        version : PostDescribePublisherRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribePublisher",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_drift_detection_status(
        self,
        *,
        stack_drift_detection_id: str,
        action: GetDescribeStackDriftDetectionStatusRequestAction,
        version: GetDescribeStackDriftDetectionStatusRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>

        Parameters
        ----------
        stack_drift_detection_id : str
            <p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.</p>

        action : GetDescribeStackDriftDetectionStatusRequestAction

        version : GetDescribeStackDriftDetectionStatusRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackDriftDetectionStatus",
            method="GET",
            params={
                "StackDriftDetectionId": stack_drift_detection_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_drift_detection_status(
        self,
        *,
        action: PostDescribeStackDriftDetectionStatusRequestAction,
        version: PostDescribeStackDriftDetectionStatusRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>

        Parameters
        ----------
        action : PostDescribeStackDriftDetectionStatusRequestAction

        version : PostDescribeStackDriftDetectionStatusRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackDriftDetectionStatus",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_events(
        self,
        *,
        action: GetDescribeStackEventsRequestAction,
        version: GetDescribeStackEventsRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>

        Parameters
        ----------
        action : GetDescribeStackEventsRequestAction

        version : GetDescribeStackEventsRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        next_token : typing.Optional[str]
            A string that identifies the next page of events that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackEvents",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_events(
        self,
        *,
        action: PostDescribeStackEventsRequestAction,
        version: PostDescribeStackEventsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>

        Parameters
        ----------
        action : PostDescribeStackEventsRequestAction

        version : PostDescribeStackEventsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackEvents",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_instance(
        self,
        *,
        stack_set_name: str,
        stack_instance_account: str,
        stack_instance_region: str,
        action: GetDescribeStackInstanceRequestAction,
        version: GetDescribeStackInstanceRequestVersion,
        call_as: typing.Optional[GetDescribeStackInstanceRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or the unique stack ID of the stack set that you want to get stack instance information for.

        stack_instance_account : str
            The ID of an Amazon Web Services account that's associated with this stack instance.

        stack_instance_region : str
            The name of a Region that's associated with this stack instance.

        action : GetDescribeStackInstanceRequestAction

        version : GetDescribeStackInstanceRequestVersion

        call_as : typing.Optional[GetDescribeStackInstanceRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackInstance",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "StackInstanceAccount": stack_instance_account,
                "StackInstanceRegion": stack_instance_region,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_instance(
        self,
        *,
        action: PostDescribeStackInstanceRequestAction,
        version: PostDescribeStackInstanceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>

        Parameters
        ----------
        action : PostDescribeStackInstanceRequestAction

        version : PostDescribeStackInstanceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackInstance",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_resource(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        action: GetDescribeStackResourceRequestAction,
        version: GetDescribeStackResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        logical_resource_id : str
            <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>

        action : GetDescribeStackResourceRequestAction

        version : GetDescribeStackResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResource",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_resource(
        self,
        *,
        action: PostDescribeStackResourceRequestAction,
        version: PostDescribeStackResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        action : PostDescribeStackResourceRequestAction

        version : PostDescribeStackResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResource",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_resource_drifts(
        self,
        *,
        stack_name: str,
        action: GetDescribeStackResourceDriftsRequestAction,
        version: GetDescribeStackResourceDriftsRequestVersion,
        stack_resource_drift_status_filters: typing.Optional[
            typing.Union[StackResourceDriftStatus, typing.Sequence[StackResourceDriftStatus]]
        ] = None,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack for which you want drift information.

        action : GetDescribeStackResourceDriftsRequestAction

        version : GetDescribeStackResourceDriftsRequestVersion

        stack_resource_drift_status_filters : typing.Optional[typing.Union[StackResourceDriftStatus, typing.Sequence[StackResourceDriftStatus]]]
            <p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>

        next_token : typing.Optional[str]
            A string that identifies the next page of stack resource drift results.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResourceDrifts",
            method="GET",
            params={
                "StackName": stack_name,
                "StackResourceDriftStatusFilters": stack_resource_drift_status_filters,
                "NextToken": next_token,
                "MaxResults": max_results,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_resource_drifts(
        self,
        *,
        action: PostDescribeStackResourceDriftsRequestAction,
        version: PostDescribeStackResourceDriftsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>

        Parameters
        ----------
        action : PostDescribeStackResourceDriftsRequestAction

        version : PostDescribeStackResourceDriftsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResourceDrifts",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_resources(
        self,
        *,
        action: GetDescribeStackResourcesRequestAction,
        version: GetDescribeStackResourcesRequestVersion,
        stack_name: typing.Optional[str] = None,
        logical_resource_id: typing.Optional[str] = None,
        physical_resource_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>

        Parameters
        ----------
        action : GetDescribeStackResourcesRequestAction

        version : GetDescribeStackResourcesRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p> <p>Required: Conditional. If you don't specify <code>StackName</code>, you must specify <code>PhysicalResourceId</code>.</p>

        logical_resource_id : typing.Optional[str]
            <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>

        physical_resource_id : typing.Optional[str]
            <p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p> <p>For example, for an Amazon Elastic Compute Cloud (EC2) instance, <code>PhysicalResourceId</code> corresponds to the <code>InstanceId</code>. You can pass the EC2 <code>InstanceId</code> to <code>DescribeStackResources</code> to find which stack the instance belongs to and what other resources are part of the stack.</p> <p>Required: Conditional. If you don't specify <code>PhysicalResourceId</code>, you must specify <code>StackName</code>.</p> <p>Default: There is no default value.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResources",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "PhysicalResourceId": physical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_resources(
        self,
        *,
        action: PostDescribeStackResourcesRequestAction,
        version: PostDescribeStackResourcesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>

        Parameters
        ----------
        action : PostDescribeStackResourcesRequestAction

        version : PostDescribeStackResourcesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackResources",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetDescribeStackSetRequestAction,
        version: GetDescribeStackSetRequestVersion,
        call_as: typing.Optional[GetDescribeStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the description of the specified stack set.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set whose description you want.

        action : GetDescribeStackSetRequestAction

        version : GetDescribeStackSetRequestVersion

        call_as : typing.Optional[GetDescribeStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_set(
        self,
        *,
        action: PostDescribeStackSetRequestAction,
        version: PostDescribeStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the description of the specified stack set.

        Parameters
        ----------
        action : PostDescribeStackSetRequestAction

        version : PostDescribeStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stack_set_operation(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetDescribeStackSetOperationRequestAction,
        version: GetDescribeStackSetOperationRequestVersion,
        call_as: typing.Optional[GetDescribeStackSetOperationRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the description of the specified stack set operation.

        Parameters
        ----------
        stack_set_name : str
            The name or the unique stack ID of the stack set for the stack operation.

        operation_id : str
            The unique ID of the stack set operation.

        action : GetDescribeStackSetOperationRequestAction

        version : GetDescribeStackSetOperationRequestVersion

        call_as : typing.Optional[GetDescribeStackSetOperationRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSetOperation",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stack_set_operation(
        self,
        *,
        action: PostDescribeStackSetOperationRequestAction,
        version: PostDescribeStackSetOperationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the description of the specified stack set operation.

        Parameters
        ----------
        action : PostDescribeStackSetOperationRequestAction

        version : PostDescribeStackSetOperationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStackSetOperation",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_stacks(
        self,
        *,
        action: GetDescribeStacksRequestAction,
        version: GetDescribeStacksRequestVersion,
        stack_name: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : GetDescribeStacksRequestAction

        version : GetDescribeStacksRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        next_token : typing.Optional[str]
            A string that identifies the next page of stacks that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStacks",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_stacks(
        self,
        *,
        action: PostDescribeStacksRequestAction,
        version: PostDescribeStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : PostDescribeStacksRequestAction

        version : PostDescribeStacksRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeStacks",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_type(
        self,
        *,
        action: GetDescribeTypeRequestAction,
        version: GetDescribeTypeRequestVersion,
        type: typing.Optional[GetDescribeTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        arn: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        publisher_id: typing.Optional[str] = None,
        public_version_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        Parameters
        ----------
        action : GetDescribeTypeRequestAction

        version : GetDescribeTypeRequestVersion

        type : typing.Optional[GetDescribeTypeRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        publisher_id : typing.Optional[str]
            <p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>

        public_version_number : typing.Optional[str]
            The version number of a public third-party extension.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeType",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "Arn": arn,
                "VersionId": version_id,
                "PublisherId": publisher_id,
                "PublicVersionNumber": public_version_number,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_type(
        self,
        *,
        action: PostDescribeTypeRequestAction,
        version: PostDescribeTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>

        Parameters
        ----------
        action : PostDescribeTypeRequestAction

        version : PostDescribeTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_describe_type_registration(
        self,
        *,
        registration_token: str,
        action: GetDescribeTypeRegistrationRequestAction,
        version: GetDescribeTypeRegistrationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>

        Parameters
        ----------
        registration_token : str
            <p>The identifier for this registration request.</p> <p>This registration token is generated by CloudFormation when you initiate a registration request using <code> <a>RegisterType</a> </code>.</p>

        action : GetDescribeTypeRegistrationRequestAction

        version : GetDescribeTypeRegistrationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeTypeRegistration",
            method="GET",
            params={
                "RegistrationToken": registration_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_describe_type_registration(
        self,
        *,
        action: PostDescribeTypeRegistrationRequestAction,
        version: PostDescribeTypeRegistrationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>

        Parameters
        ----------
        action : PostDescribeTypeRegistrationRequestAction

        version : PostDescribeTypeRegistrationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DescribeTypeRegistration",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_detect_stack_drift(
        self,
        *,
        stack_name: str,
        action: GetDetectStackDriftRequestAction,
        version: GetDetectStackDriftRequestVersion,
        logical_resource_ids: typing.Optional[
            typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack for which you want to detect drift.

        action : GetDetectStackDriftRequestAction

        version : GetDetectStackDriftRequestVersion

        logical_resource_ids : typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]
            The logical names of any resources you want to use as filters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackDrift",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceIds": logical_resource_ids,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_detect_stack_drift(
        self,
        *,
        action: PostDetectStackDriftRequestAction,
        version: PostDetectStackDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>

        Parameters
        ----------
        action : PostDetectStackDriftRequestAction

        version : PostDetectStackDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_detect_stack_resource_drift(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        action: GetDetectStackResourceDriftRequestAction,
        version: GetDetectStackResourceDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>

        Parameters
        ----------
        stack_name : str
            The name of the stack to which the resource belongs.

        logical_resource_id : str
            The logical name of the resource for which to return drift information.

        action : GetDetectStackResourceDriftRequestAction

        version : GetDetectStackResourceDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackResourceDrift",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_detect_stack_resource_drift(
        self,
        *,
        action: PostDetectStackResourceDriftRequestAction,
        version: PostDetectStackResourceDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>

        Parameters
        ----------
        action : PostDetectStackResourceDriftRequestAction

        version : PostDetectStackResourceDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackResourceDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_detect_stack_set_drift(
        self,
        *,
        stack_set_name: str,
        action: GetDetectStackSetDriftRequestAction,
        version: GetDetectStackSetDriftRequestVersion,
        operation_preferences: typing.Optional[GetDetectStackSetDriftRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetDetectStackSetDriftRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name of the stack set on which to perform the drift detection operation.

        action : GetDetectStackSetDriftRequestAction

        version : GetDetectStackSetDriftRequestVersion

        operation_preferences : typing.Optional[GetDetectStackSetDriftRequestOperationPreferences]


        operation_id : typing.Optional[str]
             <i>The ID of the stack set operation.</i>

        call_as : typing.Optional[GetDetectStackSetDriftRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackSetDrift",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetDetectStackSetDriftRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_detect_stack_set_drift(
        self,
        *,
        action: PostDetectStackSetDriftRequestAction,
        version: PostDetectStackSetDriftRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>

        Parameters
        ----------
        action : PostDetectStackSetDriftRequestAction

        version : PostDetectStackSetDriftRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=DetectStackSetDrift",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_estimate_template_cost(
        self,
        *,
        action: GetEstimateTemplateCostRequestAction,
        version: GetEstimateTemplateCostRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

        Parameters
        ----------
        action : GetEstimateTemplateCostRequestAction

        version : GetEstimateTemplateCostRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must pass <code>TemplateBody</code> or <code>TemplateURL</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=EstimateTemplateCost",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_estimate_template_cost(
        self,
        *,
        action: PostEstimateTemplateCostRequestAction,
        version: PostEstimateTemplateCostRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

        Parameters
        ----------
        action : PostEstimateTemplateCostRequestAction

        version : PostEstimateTemplateCostRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=EstimateTemplateCost",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_execute_change_set(
        self,
        *,
        change_set_name: str,
        action: GetExecuteChangeSetRequestAction,
        version: GetExecuteChangeSetRequestVersion,
        stack_name: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        disable_rollback: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>

        Parameters
        ----------
        change_set_name : str
            The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.

        action : GetExecuteChangeSetRequestAction

        version : GetExecuteChangeSetRequestVersion

        stack_name : typing.Optional[str]
            If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.

        disable_rollback : typing.Optional[bool]
            <p>Preserves the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>True</code> </p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ExecuteChangeSet",
            method="GET",
            params={
                "ChangeSetName": change_set_name,
                "StackName": stack_name,
                "ClientRequestToken": client_request_token,
                "DisableRollback": disable_rollback,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_execute_change_set(
        self,
        *,
        action: PostExecuteChangeSetRequestAction,
        version: PostExecuteChangeSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>

        Parameters
        ----------
        action : PostExecuteChangeSetRequestAction

        version : PostExecuteChangeSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ExecuteChangeSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_get_stack_policy(
        self,
        *,
        stack_name: str,
        action: GetGetStackPolicyRequestAction,
        version: GetGetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID that's associated with the stack whose policy you want to get.

        action : GetGetStackPolicyRequestAction

        version : GetGetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetStackPolicy",
            method="GET",
            params={
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_get_stack_policy(
        self,
        *,
        action: PostGetStackPolicyRequestAction,
        version: PostGetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.

        Parameters
        ----------
        action : PostGetStackPolicyRequestAction

        version : PostGetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetStackPolicy",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_get_template(
        self,
        *,
        action: GetGetTemplateRequestAction,
        version: GetGetTemplateRequestVersion,
        stack_name: typing.Optional[str] = None,
        change_set_name: typing.Optional[str] = None,
        template_stage: typing.Optional[GetGetTemplateRequestTemplateStage] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : GetGetTemplateRequestAction

        version : GetGetTemplateRequestVersion

        stack_name : typing.Optional[str]
            <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        change_set_name : typing.Optional[str]
            The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.

        template_stage : typing.Optional[GetGetTemplateRequestTemplateStage]
            <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetTemplate",
            method="GET",
            params={
                "StackName": stack_name,
                "ChangeSetName": change_set_name,
                "TemplateStage": template_stage,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_get_template(
        self,
        *,
        action: PostGetTemplateRequestAction,
        version: PostGetTemplateRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Parameters
        ----------
        action : PostGetTemplateRequestAction

        version : PostGetTemplateRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetTemplate",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_get_template_summary(
        self,
        *,
        action: GetGetTemplateSummaryRequestAction,
        version: GetGetTemplateSummaryRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        stack_name: typing.Optional[str] = None,
        stack_set_name: typing.Optional[str] = None,
        call_as: typing.Optional[GetGetTemplateSummaryRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>

        Parameters
        ----------
        action : GetGetTemplateSummaryRequestAction

        version : GetGetTemplateSummaryRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        stack_name : typing.Optional[str]
            <p>The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        stack_set_name : typing.Optional[str]
            <p>The name or unique ID of the stack set from which the stack was created.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>

        call_as : typing.Optional[GetGetTemplateSummaryRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetTemplateSummary",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "StackName": stack_name,
                "StackSetName": stack_set_name,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_get_template_summary(
        self,
        *,
        action: PostGetTemplateSummaryRequestAction,
        version: PostGetTemplateSummaryRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>

        Parameters
        ----------
        action : PostGetTemplateSummaryRequestAction

        version : PostGetTemplateSummaryRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=GetTemplateSummary",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_import_stacks_to_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetImportStacksToStackSetRequestAction,
        version: GetImportStacksToStackSetRequestVersion,
        stack_ids: typing.Optional[typing.Union[StackId, typing.Sequence[StackId]]] = None,
        stack_ids_url: typing.Optional[str] = None,
        organizational_unit_ids: typing.Optional[
            typing.Union[OrganizationalUnitId, typing.Sequence[OrganizationalUnitId]]
        ] = None,
        operation_preferences: typing.Optional[GetImportStacksToStackSetRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetImportStacksToStackSetRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>

        Parameters
        ----------
        stack_set_name : str
            The name of the stack set. The name must be unique in the Region where you create your stack set.

        action : GetImportStacksToStackSetRequestAction

        version : GetImportStacksToStackSetRequestVersion

        stack_ids : typing.Optional[typing.Union[StackId, typing.Sequence[StackId]]]
            <p>The IDs of the stacks you are importing into a stack set. You import up to 10 stacks per stack set at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>

        stack_ids_url : typing.Optional[str]
            <p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>

        organizational_unit_ids : typing.Optional[typing.Union[OrganizationalUnitId, typing.Sequence[OrganizationalUnitId]]]
            The list of OU ID's to which the stacks being imported has to be mapped as deployment target.

        operation_preferences : typing.Optional[GetImportStacksToStackSetRequestOperationPreferences]


        operation_id : typing.Optional[str]
            A unique, user defined, identifier for the stack set operation.

        call_as : typing.Optional[GetImportStacksToStackSetRequestCallAs]
            <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed stack sets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ImportStacksToStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "StackIds": stack_ids,
                "StackIdsUrl": stack_ids_url,
                "OrganizationalUnitIds": organizational_unit_ids,
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetImportStacksToStackSetRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_import_stacks_to_stack_set(
        self,
        *,
        action: PostImportStacksToStackSetRequestAction,
        version: PostImportStacksToStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>

        Parameters
        ----------
        action : PostImportStacksToStackSetRequestAction

        version : PostImportStacksToStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ImportStacksToStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_change_sets(
        self,
        *,
        stack_name: str,
        action: GetListChangeSetsRequestAction,
        version: GetListChangeSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.

        Parameters
        ----------
        stack_name : str
            The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.

        action : GetListChangeSetsRequestAction

        version : GetListChangeSetsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListChangeSets</a> response output) that identifies the next page of change sets that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListChangeSets",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_change_sets(
        self,
        *,
        action: PostListChangeSetsRequestAction,
        version: PostListChangeSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.

        Parameters
        ----------
        action : PostListChangeSetsRequestAction

        version : PostListChangeSetsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListChangeSets",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_exports(
        self,
        *,
        action: GetListExportsRequestAction,
        version: GetListExportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>

        Parameters
        ----------
        action : GetListExportsRequestAction

        version : GetListExportsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListExports</a> response output) that identifies the next page of exported output values that you asked to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListExports",
            method="GET",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_exports(
        self,
        *,
        action: PostListExportsRequestAction,
        version: PostListExportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>

        Parameters
        ----------
        action : PostListExportsRequestAction

        version : PostListExportsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListExports",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_imports(
        self,
        *,
        export_name: str,
        action: GetListImportsRequestAction,
        version: GetListImportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>

        Parameters
        ----------
        export_name : str
            The name of the exported output value. CloudFormation returns the stack names that are importing this value.

        action : GetListImportsRequestAction

        version : GetListImportsRequestVersion

        next_token : typing.Optional[str]
            A string (provided by the <a>ListImports</a> response output) that identifies the next page of stacks that are importing the specified exported output value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListImports",
            method="GET",
            params={
                "ExportName": export_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_imports(
        self,
        *,
        action: PostListImportsRequestAction,
        version: PostListImportsRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>

        Parameters
        ----------
        action : PostListImportsRequestAction

        version : PostListImportsRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListImports",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetListStackInstancesRequestAction,
        version: GetListStackInstancesRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        filters: typing.Optional[typing.Union[StackInstanceFilter, typing.Sequence[StackInstanceFilter]]] = None,
        stack_instance_account: typing.Optional[str] = None,
        stack_instance_region: typing.Optional[str] = None,
        call_as: typing.Optional[GetListStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to list stack instances for.

        action : GetListStackInstancesRequestAction

        version : GetListStackInstancesRequestVersion

        next_token : typing.Optional[str]
            If the previous request didn't return all the remaining results, the response's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        filters : typing.Optional[typing.Union[StackInstanceFilter, typing.Sequence[StackInstanceFilter]]]
            The filter to apply to stack instances

        stack_instance_account : typing.Optional[str]
            The name of the Amazon Web Services account that you want to list stack instances for.

        stack_instance_region : typing.Optional[str]
            The name of the Region where you want to list stack instances.

        call_as : typing.Optional[GetListStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "NextToken": next_token,
                "MaxResults": max_results,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=StackInstanceFilter, direction="write"
                ),
                "StackInstanceAccount": stack_instance_account,
                "StackInstanceRegion": stack_instance_region,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stack_instances(
        self,
        *,
        action: PostListStackInstancesRequestAction,
        version: PostListStackInstancesRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

        Parameters
        ----------
        action : PostListStackInstancesRequestAction

        version : PostListStackInstancesRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackInstances",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stack_resources(
        self,
        *,
        stack_name: str,
        action: GetListStackResourcesRequestAction,
        version: GetListStackResourcesRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        stack_name : str
            <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>

        action : GetListStackResourcesRequestAction

        version : GetListStackResourcesRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of stack resources that you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackResources",
            method="GET",
            params={
                "StackName": stack_name,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stack_resources(
        self,
        *,
        action: PostListStackResourcesRequestAction,
        version: PostListStackResourcesRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>

        Parameters
        ----------
        action : PostListStackResourcesRequestAction

        version : PostListStackResourcesRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackResources",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stack_set_operation_results(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetListStackSetOperationResultsRequestAction,
        version: GetListStackSetOperationResultsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        call_as: typing.Optional[GetListStackSetOperationResultsRequestCallAs] = None,
        filters: typing.Optional[typing.Union[OperationResultFilter, typing.Sequence[OperationResultFilter]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about the results of a stack set operation.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to get operation results for.

        operation_id : str
            The ID of the stack set operation.

        action : GetListStackSetOperationResultsRequestAction

        version : GetListStackSetOperationResultsRequestVersion

        next_token : typing.Optional[str]
            If the previous request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        call_as : typing.Optional[GetListStackSetOperationResultsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        filters : typing.Optional[typing.Union[OperationResultFilter, typing.Sequence[OperationResultFilter]]]
            The filter to apply to operation results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperationResults",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "NextToken": next_token,
                "MaxResults": max_results,
                "CallAs": call_as,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=OperationResultFilter, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stack_set_operation_results(
        self,
        *,
        action: PostListStackSetOperationResultsRequestAction,
        version: PostListStackSetOperationResultsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about the results of a stack set operation.

        Parameters
        ----------
        action : PostListStackSetOperationResultsRequestAction

        version : PostListStackSetOperationResultsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperationResults",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stack_set_operations(
        self,
        *,
        stack_set_name: str,
        action: GetListStackSetOperationsRequestAction,
        version: GetListStackSetOperationsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        call_as: typing.Optional[GetListStackSetOperationsRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about operations performed on a stack set.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to get operation summaries for.

        action : GetListStackSetOperationsRequestAction

        version : GetListStackSetOperationsRequestVersion

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperations</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        call_as : typing.Optional[GetListStackSetOperationsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperations",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "NextToken": next_token,
                "MaxResults": max_results,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stack_set_operations(
        self,
        *,
        action: PostListStackSetOperationsRequestAction,
        version: PostListStackSetOperationsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about operations performed on a stack set.

        Parameters
        ----------
        action : PostListStackSetOperationsRequestAction

        version : PostListStackSetOperationsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSetOperations",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stack_sets(
        self,
        *,
        action: GetListStackSetsRequestAction,
        version: GetListStackSetsRequestVersion,
        next_token: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        status: typing.Optional[GetListStackSetsRequestStatus] = None,
        call_as: typing.Optional[GetListStackSetsRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>

        Parameters
        ----------
        action : GetListStackSetsRequestAction

        version : GetListStackSetsRequestVersion

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSets</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        status : typing.Optional[GetListStackSetsRequestStatus]
            The status of the stack sets that you want to get summary information about.

        call_as : typing.Optional[GetListStackSetsRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSets",
            method="GET",
            params={
                "NextToken": next_token,
                "MaxResults": max_results,
                "Status": status,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stack_sets(
        self,
        *,
        action: PostListStackSetsRequestAction,
        version: PostListStackSetsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>

        Parameters
        ----------
        action : PostListStackSetsRequestAction

        version : PostListStackSetsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStackSets",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_stacks(
        self,
        *,
        action: GetListStacksRequestAction,
        version: GetListStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        stack_status_filter: typing.Optional[typing.Union[StackStatus, typing.Sequence[StackStatus]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

        Parameters
        ----------
        action : GetListStacksRequestAction

        version : GetListStacksRequestVersion

        next_token : typing.Optional[str]
            A string that identifies the next page of stacks that you want to retrieve.

        stack_status_filter : typing.Optional[typing.Union[StackStatus, typing.Sequence[StackStatus]]]
            Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStacks",
            method="GET",
            params={
                "NextToken": next_token,
                "StackStatusFilter": stack_status_filter,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_stacks(
        self,
        *,
        action: PostListStacksRequestAction,
        version: PostListStacksRequestVersion,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

        Parameters
        ----------
        action : PostListStacksRequestAction

        version : PostListStacksRequestVersion

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListStacks",
            method="POST",
            params={
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_type_registrations(
        self,
        *,
        action: GetListTypeRegistrationsRequestAction,
        version: GetListTypeRegistrationsRequestVersion,
        type: typing.Optional[GetListTypeRegistrationsRequestType] = None,
        type_name: typing.Optional[str] = None,
        type_arn: typing.Optional[str] = None,
        registration_status_filter: typing.Optional[GetListTypeRegistrationsRequestRegistrationStatusFilter] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns a list of registration tokens for the specified extension(s).

        Parameters
        ----------
        action : GetListTypeRegistrationsRequestAction

        version : GetListTypeRegistrationsRequestVersion

        type : typing.Optional[GetListTypeRegistrationsRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        registration_status_filter : typing.Optional[GetListTypeRegistrationsRequestRegistrationStatusFilter]
            <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypeRegistrations",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "TypeArn": type_arn,
                "RegistrationStatusFilter": registration_status_filter,
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_type_registrations(
        self,
        *,
        action: PostListTypeRegistrationsRequestAction,
        version: PostListTypeRegistrationsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns a list of registration tokens for the specified extension(s).

        Parameters
        ----------
        action : PostListTypeRegistrationsRequestAction

        version : PostListTypeRegistrationsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypeRegistrations",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_type_versions(
        self,
        *,
        action: GetListTypeVersionsRequestAction,
        version: GetListTypeVersionsRequestVersion,
        type: typing.Optional[GetListTypeVersionsRequestType] = None,
        type_name: typing.Optional[str] = None,
        arn: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        deprecated_status: typing.Optional[GetListTypeVersionsRequestDeprecatedStatus] = None,
        publisher_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about the versions of an extension.

        Parameters
        ----------
        action : GetListTypeVersionsRequestAction

        version : GetListTypeVersionsRequestVersion

        type : typing.Optional[GetListTypeVersionsRequestType]
            <p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        deprecated_status : typing.Optional[GetListTypeVersionsRequestDeprecatedStatus]
            <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>

        publisher_id : typing.Optional[str]
            <p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypeVersions",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "Arn": arn,
                "MaxResults": max_results,
                "NextToken": next_token,
                "DeprecatedStatus": deprecated_status,
                "PublisherId": publisher_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_type_versions(
        self,
        *,
        action: PostListTypeVersionsRequestAction,
        version: PostListTypeVersionsRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about the versions of an extension.

        Parameters
        ----------
        action : PostListTypeVersionsRequestAction

        version : PostListTypeVersionsRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypeVersions",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_list_types(
        self,
        *,
        action: GetListTypesRequestAction,
        version: GetListTypesRequestVersion,
        visibility: typing.Optional[GetListTypesRequestVisibility] = None,
        provisioning_type: typing.Optional[GetListTypesRequestProvisioningType] = None,
        deprecated_status: typing.Optional[GetListTypesRequestDeprecatedStatus] = None,
        type: typing.Optional[GetListTypesRequestType] = None,
        filters: typing.Optional[GetListTypesRequestFilters] = None,
        max_results: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about extension that have been registered with CloudFormation.

        Parameters
        ----------
        action : GetListTypesRequestAction

        version : GetListTypesRequestVersion

        visibility : typing.Optional[GetListTypesRequestVisibility]
            <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and region.</p> </li> <li> <p>Public extensions that you have activated in this account and region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>

        provisioning_type : typing.Optional[GetListTypesRequestProvisioningType]
            <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>

        deprecated_status : typing.Optional[GetListTypesRequestDeprecatedStatus]
            <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>

        type : typing.Optional[GetListTypesRequestType]
            The type of extension.

        filters : typing.Optional[GetListTypesRequestFilters]
            <p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>

        max_results : typing.Optional[int]
            The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.

        next_token : typing.Optional[str]
            If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypes",
            method="GET",
            params={
                "Visibility": visibility,
                "ProvisioningType": provisioning_type,
                "DeprecatedStatus": deprecated_status,
                "Type": type,
                "Filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=GetListTypesRequestFilters, direction="write"
                ),
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_list_types(
        self,
        *,
        action: PostListTypesRequestAction,
        version: PostListTypesRequestVersion,
        max_results: typing.Optional[str] = None,
        next_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Returns summary information about extension that have been registered with CloudFormation.

        Parameters
        ----------
        action : PostListTypesRequestAction

        version : PostListTypesRequestVersion

        max_results : typing.Optional[str]
            Pagination limit

        next_token : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ListTypes",
            method="POST",
            params={
                "MaxResults": max_results,
                "NextToken": next_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_publish_type(
        self,
        *,
        action: GetPublishTypeRequestAction,
        version: GetPublishTypeRequestVersion,
        type: typing.Optional[GetPublishTypeRequestType] = None,
        arn: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        public_version_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>

        Parameters
        ----------
        action : GetPublishTypeRequestAction

        version : GetPublishTypeRequestVersion

        type : typing.Optional[GetPublishTypeRequestType]
            <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        public_version_number : typing.Optional[str]
            <p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=PublishType",
            method="GET",
            params={
                "Type": type,
                "Arn": arn,
                "TypeName": type_name,
                "PublicVersionNumber": public_version_number,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_publish_type(
        self,
        *,
        action: PostPublishTypeRequestAction,
        version: PostPublishTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>

        Parameters
        ----------
        action : PostPublishTypeRequestAction

        version : PostPublishTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=PublishType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_record_handler_progress(
        self,
        *,
        bearer_token: str,
        operation_status: GetRecordHandlerProgressRequestOperationStatus,
        action: GetRecordHandlerProgressRequestAction,
        version: GetRecordHandlerProgressRequestVersion,
        current_operation_status: typing.Optional[GetRecordHandlerProgressRequestCurrentOperationStatus] = None,
        status_message: typing.Optional[str] = None,
        error_code: typing.Optional[GetRecordHandlerProgressRequestErrorCode] = None,
        resource_model: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>

        Parameters
        ----------
        bearer_token : str
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        operation_status : GetRecordHandlerProgressRequestOperationStatus
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        action : GetRecordHandlerProgressRequestAction

        version : GetRecordHandlerProgressRequestVersion

        current_operation_status : typing.Optional[GetRecordHandlerProgressRequestCurrentOperationStatus]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        status_message : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        error_code : typing.Optional[GetRecordHandlerProgressRequestErrorCode]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        resource_model : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        client_request_token : typing.Optional[str]
            Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RecordHandlerProgress",
            method="GET",
            params={
                "BearerToken": bearer_token,
                "OperationStatus": operation_status,
                "CurrentOperationStatus": current_operation_status,
                "StatusMessage": status_message,
                "ErrorCode": error_code,
                "ResourceModel": resource_model,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_record_handler_progress(
        self,
        *,
        action: PostRecordHandlerProgressRequestAction,
        version: PostRecordHandlerProgressRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>

        Parameters
        ----------
        action : PostRecordHandlerProgressRequestAction

        version : PostRecordHandlerProgressRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RecordHandlerProgress",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_register_publisher(
        self,
        *,
        action: GetRegisterPublisherRequestAction,
        version: GetRegisterPublisherRequestVersion,
        accept_terms_and_conditions: typing.Optional[bool] = None,
        connection_arn: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>

        Parameters
        ----------
        action : GetRegisterPublisherRequestAction

        version : GetRegisterPublisherRequestVersion

        accept_terms_and_conditions : typing.Optional[bool]
            <p>Whether you accept the <a href="https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf">Terms and Conditions</a> for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.</p> <p>The default is <code>false</code>.</p>

        connection_arn : typing.Optional[str]
            <p>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RegisterPublisher",
            method="GET",
            params={
                "AcceptTermsAndConditions": accept_terms_and_conditions,
                "ConnectionArn": connection_arn,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_register_publisher(
        self,
        *,
        action: PostRegisterPublisherRequestAction,
        version: PostRegisterPublisherRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>

        Parameters
        ----------
        action : PostRegisterPublisherRequestAction

        version : PostRegisterPublisherRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RegisterPublisher",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_register_type(
        self,
        *,
        type_name: str,
        schema_handler_package: str,
        action: GetRegisterTypeRequestAction,
        version: GetRegisterTypeRequestVersion,
        type: typing.Optional[GetRegisterTypeRequestType] = None,
        logging_config: typing.Optional[GetRegisterTypeRequestLoggingConfig] = None,
        execution_role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        type_name : str
            <p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <i>company_or_organization</i>::<i>service</i>::<i>type</i>.</p> </li> <li> <p>For modules, <i>company_or_organization</i>::<i>service</i>::<i>type</i>::MODULE.</p> </li> <li> <p>For hooks, <i>MyCompany</i>::<i>Testing</i>::<i>MyTestHook</i>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>

        schema_handler_package : str
            <p>A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation CLI User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>

        action : GetRegisterTypeRequestAction

        version : GetRegisterTypeRequestVersion

        type : typing.Optional[GetRegisterTypeRequestType]
            The kind of extension.

        logging_config : typing.Optional[GetRegisterTypeRequestLoggingConfig]
            Specifies logging configuration information for an extension.

        execution_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>

        client_request_token : typing.Optional[str]
            A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RegisterType",
            method="GET",
            params={
                "Type": type,
                "TypeName": type_name,
                "SchemaHandlerPackage": schema_handler_package,
                "LoggingConfig": convert_and_respect_annotation_metadata(
                    object_=logging_config, annotation=GetRegisterTypeRequestLoggingConfig, direction="write"
                ),
                "ExecutionRoleArn": execution_role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_register_type(
        self,
        *,
        action: PostRegisterTypeRequestAction,
        version: PostRegisterTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>

        Parameters
        ----------
        action : PostRegisterTypeRequestAction

        version : PostRegisterTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RegisterType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_rollback_stack(
        self,
        *,
        stack_name: str,
        action: GetRollbackStackRequestAction,
        version: GetRollbackStackRequestVersion,
        role_arn: typing.Optional[str] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>

        Parameters
        ----------
        stack_name : str
            The name that's associated with the stack.

        action : GetRollbackStackRequestAction

        version : GetRollbackStackRequestVersion

        role_arn : typing.Optional[str]
            The Amazon Resource Name (ARN) of an Identity and Access Management role that CloudFormation assumes to rollback the stack.

        client_request_token : typing.Optional[str]
            A unique identifier for this <code>RollbackStack</code> request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RollbackStack",
            method="GET",
            params={
                "StackName": stack_name,
                "RoleARN": role_arn,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_rollback_stack(
        self,
        *,
        action: PostRollbackStackRequestAction,
        version: PostRollbackStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>

        Parameters
        ----------
        action : PostRollbackStackRequestAction

        version : PostRollbackStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=RollbackStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_set_stack_policy(
        self,
        *,
        stack_name: str,
        action: GetSetStackPolicyRequestAction,
        version: GetSetStackPolicyRequestVersion,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Sets a stack policy for a specified stack.

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID that you want to associate a policy with.

        action : GetSetStackPolicyRequestAction

        version : GetSetStackPolicyRequestVersion

        stack_policy_body : typing.Optional[str]
            Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent updates to stack resources</a> in the CloudFormation User Guide. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        stack_policy_url : typing.Optional[str]
            Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetStackPolicy",
            method="GET",
            params={
                "StackName": stack_name,
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_set_stack_policy(
        self,
        *,
        action: PostSetStackPolicyRequestAction,
        version: PostSetStackPolicyRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Sets a stack policy for a specified stack.

        Parameters
        ----------
        action : PostSetStackPolicyRequestAction

        version : PostSetStackPolicyRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetStackPolicy",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_set_type_configuration(
        self,
        *,
        configuration: str,
        action: GetSetTypeConfigurationRequestAction,
        version: GetSetTypeConfigurationRequestVersion,
        type_arn: typing.Optional[str] = None,
        configuration_alias: typing.Optional[str] = None,
        type_name: typing.Optional[str] = None,
        type: typing.Optional[GetSetTypeConfigurationRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>

        Parameters
        ----------
        configuration : str
            <p>The configuration data for the extension, in this account and region.</p> <p>The configuration data must be formatted as JSON, and validate against the schema returned in the <code>ConfigurationSchema</code> response element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">API_DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining account-level configuration data for an extension</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        action : GetSetTypeConfigurationRequestAction

        version : GetSetTypeConfigurationRequestVersion

        type_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>

        configuration_alias : typing.Optional[str]
            <p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>

        type : typing.Optional[GetSetTypeConfigurationRequestType]
            <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetTypeConfiguration",
            method="GET",
            params={
                "TypeArn": type_arn,
                "Configuration": configuration,
                "ConfigurationAlias": configuration_alias,
                "TypeName": type_name,
                "Type": type,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_set_type_configuration(
        self,
        *,
        action: PostSetTypeConfigurationRequestAction,
        version: PostSetTypeConfigurationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>

        Parameters
        ----------
        action : PostSetTypeConfigurationRequestAction

        version : PostSetTypeConfigurationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetTypeConfiguration",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_set_type_default_version(
        self,
        *,
        action: GetSetTypeDefaultVersionRequestAction,
        version: GetSetTypeDefaultVersionRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetSetTypeDefaultVersionRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

        Parameters
        ----------
        action : GetSetTypeDefaultVersionRequestAction

        version : GetSetTypeDefaultVersionRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type : typing.Optional[GetSetTypeDefaultVersionRequestType]
            <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>

        version_id : typing.Optional[str]
            The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetTypeDefaultVersion",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_set_type_default_version(
        self,
        *,
        action: PostSetTypeDefaultVersionRequestAction,
        version: PostSetTypeDefaultVersionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

        Parameters
        ----------
        action : PostSetTypeDefaultVersionRequestAction

        version : PostSetTypeDefaultVersionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SetTypeDefaultVersion",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_signal_resource(
        self,
        *,
        stack_name: str,
        logical_resource_id: str,
        unique_id: str,
        status: GetSignalResourceRequestStatus,
        action: GetSignalResourceRequestAction,
        version: GetSignalResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

        Parameters
        ----------
        stack_name : str
            The stack name or unique stack ID that includes the resource that you want to signal.

        logical_resource_id : str
            The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.

        unique_id : str
            A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.

        status : GetSignalResourceRequestStatus
            The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.

        action : GetSignalResourceRequestAction

        version : GetSignalResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SignalResource",
            method="GET",
            params={
                "StackName": stack_name,
                "LogicalResourceId": logical_resource_id,
                "UniqueId": unique_id,
                "Status": status,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_signal_resource(
        self,
        *,
        action: PostSignalResourceRequestAction,
        version: PostSignalResourceRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

        Parameters
        ----------
        action : PostSignalResourceRequestAction

        version : PostSignalResourceRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=SignalResource",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_stop_stack_set_operation(
        self,
        *,
        stack_set_name: str,
        operation_id: str,
        action: GetStopStackSetOperationRequestAction,
        version: GetStopStackSetOperationRequestVersion,
        call_as: typing.Optional[GetStopStackSetOperationRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to stop the operation for.

        operation_id : str
            The ID of the stack operation.

        action : GetStopStackSetOperationRequestAction

        version : GetStopStackSetOperationRequestVersion

        call_as : typing.Optional[GetStopStackSetOperationRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=StopStackSetOperation",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_stop_stack_set_operation(
        self,
        *,
        action: PostStopStackSetOperationRequestAction,
        version: PostStopStackSetOperationRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

        Parameters
        ----------
        action : PostStopStackSetOperationRequestAction

        version : PostStopStackSetOperationRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=StopStackSetOperation",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_test_type(
        self,
        *,
        action: GetTestTypeRequestAction,
        version: GetTestTypeRequestVersion,
        arn: typing.Optional[str] = None,
        type: typing.Optional[GetTestTypeRequestType] = None,
        type_name: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        log_delivery_bucket: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        Parameters
        ----------
        action : GetTestTypeRequestAction

        version : GetTestTypeRequestVersion

        arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type : typing.Optional[GetTestTypeRequestType]
            <p>The type of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        type_name : typing.Optional[str]
            <p>The name of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        version_id : typing.Optional[str]
            <p>The version of the extension to test.</p> <p>You can specify the version id with either <code>Arn</code>, or with <code>TypeName</code> and <code>Type</code>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in this account and region for testing.</p>

        log_delivery_bucket : typing.Optional[str]
            <p>The S3 bucket to which CloudFormation delivers the contract test execution logs.</p> <p>CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of <code>PASSED</code> or <code>FAILED</code>.</p> <p>The user calling <code>TestType</code> must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:</p> <ul> <li> <p> <code>GetObject</code> </p> </li> <li> <p> <code>PutObject</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=TestType",
            method="GET",
            params={
                "Arn": arn,
                "Type": type,
                "TypeName": type_name,
                "VersionId": version_id,
                "LogDeliveryBucket": log_delivery_bucket,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_test_type(
        self,
        *,
        action: PostTestTypeRequestAction,
        version: PostTestTypeRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>

        Parameters
        ----------
        action : PostTestTypeRequestAction

        version : PostTestTypeRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=TestType",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_update_stack(
        self,
        *,
        stack_name: str,
        action: GetUpdateStackRequestAction,
        version: GetUpdateStackRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        stack_policy_during_update_body: typing.Optional[str] = None,
        stack_policy_during_update_url: typing.Optional[str] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        resource_types: typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]] = None,
        role_arn: typing.Optional[str] = None,
        rollback_configuration: typing.Optional[GetUpdateStackRequestRollbackConfiguration] = None,
        stack_policy_body: typing.Optional[str] = None,
        stack_policy_url: typing.Optional[str] = None,
        notification_ar_ns: typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        disable_rollback: typing.Optional[bool] = None,
        client_request_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>

        Parameters
        ----------
        stack_name : str
            The name or unique stack ID of the stack to update.

        action : GetUpdateStackRequestAction

        version : GetUpdateStackRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        use_previous_template : typing.Optional[bool]
            <p>Reuse the existing template that is associated with the stack that you are updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>

        stack_policy_during_update_body : typing.Optional[str]
            <p>Structure containing the temporary overriding stack policy body. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>

        stack_policy_during_update_url : typing.Optional[str]
            <p>Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to update a stack from a stack template that contains macros <i>and</i> nested stacks, you must update the stack directly from the template using this capability.</p> <important> <p>You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> </li> </ul>

        resource_types : typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]
            <p>The template resource types that you have permissions to work with for this update stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>

        role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to update the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>

        rollback_configuration : typing.Optional[GetUpdateStackRequestRollbackConfiguration]
            The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

        stack_policy_body : typing.Optional[str]
            <p>Structure containing a new stack policy body. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>

        stack_policy_url : typing.Optional[str]
            <p>Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>

        notification_ar_ns : typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]
            Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.</p> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you specify an empty value, CloudFormation removes all associated tags.</p>

        disable_rollback : typing.Optional[bool]
            <p>Preserve the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>False</code> </p>

        client_request_token : typing.Optional[str]
            <p>A unique identifier for this <code>UpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to update a stack with the same name. You might retry <code>UpdateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStack",
            method="GET",
            params={
                "StackName": stack_name,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "StackPolicyDuringUpdateBody": stack_policy_during_update_body,
                "StackPolicyDuringUpdateURL": stack_policy_during_update_url,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "ResourceTypes": resource_types,
                "RoleARN": role_arn,
                "RollbackConfiguration": convert_and_respect_annotation_metadata(
                    object_=rollback_configuration,
                    annotation=GetUpdateStackRequestRollbackConfiguration,
                    direction="write",
                ),
                "StackPolicyBody": stack_policy_body,
                "StackPolicyURL": stack_policy_url,
                "NotificationARNs": notification_ar_ns,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "DisableRollback": disable_rollback,
                "ClientRequestToken": client_request_token,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_update_stack(
        self,
        *,
        action: PostUpdateStackRequestAction,
        version: PostUpdateStackRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>

        Parameters
        ----------
        action : PostUpdateStackRequestAction

        version : PostUpdateStackRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStack",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_update_stack_instances(
        self,
        *,
        stack_set_name: str,
        action: GetUpdateStackInstancesRequestAction,
        version: GetUpdateStackInstancesRequestVersion,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        deployment_targets: typing.Optional[GetUpdateStackInstancesRequestDeploymentTargets] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        parameter_overrides: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        operation_preferences: typing.Optional[GetUpdateStackInstancesRequestOperationPreferences] = None,
        operation_id: typing.Optional[str] = None,
        call_as: typing.Optional[GetUpdateStackInstancesRequestCallAs] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set associated with the stack instances.

        action : GetUpdateStackInstancesRequestAction

        version : GetUpdateStackInstancesRequestVersion

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        deployment_targets : typing.Optional[GetUpdateStackInstancesRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won't use the overridden values.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.

        parameter_overrides : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            <p>A list of input parameters whose values you want to update for the specified stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <code>UpdateStackSet</code> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        operation_preferences : typing.Optional[GetUpdateStackInstancesRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        operation_id : typing.Optional[str]
            <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>

        call_as : typing.Optional[GetUpdateStackInstancesRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackInstances",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Accounts": accounts,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets,
                    annotation=GetUpdateStackInstancesRequestDeploymentTargets,
                    direction="write",
                ),
                "Regions": regions,
                "ParameterOverrides": convert_and_respect_annotation_metadata(
                    object_=parameter_overrides, annotation=Parameter, direction="write"
                ),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetUpdateStackInstancesRequestOperationPreferences,
                    direction="write",
                ),
                "OperationId": operation_id,
                "CallAs": call_as,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_update_stack_instances(
        self,
        *,
        action: PostUpdateStackInstancesRequestAction,
        version: PostUpdateStackInstancesRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>

        Parameters
        ----------
        action : PostUpdateStackInstancesRequestAction

        version : PostUpdateStackInstancesRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackInstances",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_update_stack_set(
        self,
        *,
        stack_set_name: str,
        action: GetUpdateStackSetRequestAction,
        version: GetUpdateStackSetRequestVersion,
        description: typing.Optional[str] = None,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        use_previous_template: typing.Optional[bool] = None,
        parameters: typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]] = None,
        capabilities: typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]] = None,
        tags: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        operation_preferences: typing.Optional[GetUpdateStackSetRequestOperationPreferences] = None,
        administration_role_arn: typing.Optional[str] = None,
        execution_role_name: typing.Optional[str] = None,
        deployment_targets: typing.Optional[GetUpdateStackSetRequestDeploymentTargets] = None,
        permission_model: typing.Optional[GetUpdateStackSetRequestPermissionModel] = None,
        auto_deployment: typing.Optional[GetUpdateStackSetRequestAutoDeployment] = None,
        operation_id: typing.Optional[str] = None,
        accounts: typing.Optional[typing.Union[Account, typing.Sequence[Account]]] = None,
        regions: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        call_as: typing.Optional[GetUpdateStackSetRequestCallAs] = None,
        managed_execution: typing.Optional[GetUpdateStackSetRequestManagedExecution] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>

        Parameters
        ----------
        stack_set_name : str
            The name or unique ID of the stack set that you want to update.

        action : GetUpdateStackSetRequestAction

        version : GetUpdateStackSetRequestVersion

        description : typing.Optional[str]
            A brief description of updates that you are making.

        template_body : typing.Optional[str]
            <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        template_url : typing.Optional[str]
            <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        use_previous_template : typing.Optional[bool]
            <p>Use the existing template that's associated with the stack set that you're updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>

        parameters : typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]
            A list of input parameters for the stack set template.

        capabilities : typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]
            <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack set and its associated stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html"> AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html"> AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must update the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To update the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions do not currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>

        tags : typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]
            <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.</p> <p>If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:</p> <ul> <li> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags.</p> </li> <li> <p>If you specify <i>any</i> tags using this parameter, you must specify <i>all</i> the tags that you want associated with this stack set, even tags you've specified before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don't include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.</p> </li> <li> <p>If you specify an empty value, CloudFormation removes all currently associated tags.</p> </li> </ul> <p>If you specify new tags as part of an <code>UpdateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire <code>UpdateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not updated.</p>

        operation_preferences : typing.Optional[GetUpdateStackSetRequestOperationPreferences]
            Preferences for how CloudFormation performs this stack set operation.

        administration_role_arn : typing.Optional[str]
            <p>The Amazon Resource Name (ARN) of the IAM role to use to update this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.</p>

        execution_role_name : typing.Optional[str]
            <p>The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p> <p>If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.</p>

        deployment_targets : typing.Optional[GetUpdateStackSetRequestDeploymentTargets]
            <p>[Service-managed permissions] The Organizations accounts in which to update associated stack instances.</p> <p>To update all the stack instances associated with this stack set, do not specify <code>DeploymentTargets</code> or <code>Regions</code>.</p> <p>If the stack set update includes changes to the template (that is, if <code>TemplateBody</code> or <code>TemplateURL</code> is specified), or the <code>Parameters</code>, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update doesn't include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>

        permission_model : typing.Optional[GetUpdateStackSetRequestPermissionModel]
            <p>Describes how the IAM roles required for stack set operations are created. You cannot modify <code>PermissionModel</code> if there are stack instances associated with your stack set.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>

        auto_deployment : typing.Optional[GetUpdateStackSetRequestAutoDeployment]
            <p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).</p> <p>If you specify <code>AutoDeployment</code>, don't specify <code>DeploymentTargets</code> or <code>Regions</code>.</p>

        operation_id : typing.Optional[str]
            <p>The unique ID for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, CloudFormation generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>

        accounts : typing.Optional[typing.Union[Account, typing.Sequence[Account]]]
            <p>[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, don't specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.</p>

        regions : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]
            <p>The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, do not specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>

        call_as : typing.Optional[GetUpdateStackSetRequestCallAs]
            <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        managed_execution : typing.Optional[GetUpdateStackSetRequestManagedExecution]
            Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackSet",
            method="GET",
            params={
                "StackSetName": stack_set_name,
                "Description": description,
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "UsePreviousTemplate": use_previous_template,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=Parameter, direction="write"
                ),
                "Capabilities": capabilities,
                "Tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tag, direction="write"),
                "OperationPreferences": convert_and_respect_annotation_metadata(
                    object_=operation_preferences,
                    annotation=GetUpdateStackSetRequestOperationPreferences,
                    direction="write",
                ),
                "AdministrationRoleARN": administration_role_arn,
                "ExecutionRoleName": execution_role_name,
                "DeploymentTargets": convert_and_respect_annotation_metadata(
                    object_=deployment_targets, annotation=GetUpdateStackSetRequestDeploymentTargets, direction="write"
                ),
                "PermissionModel": permission_model,
                "AutoDeployment": convert_and_respect_annotation_metadata(
                    object_=auto_deployment, annotation=GetUpdateStackSetRequestAutoDeployment, direction="write"
                ),
                "OperationId": operation_id,
                "Accounts": accounts,
                "Regions": regions,
                "CallAs": call_as,
                "ManagedExecution": convert_and_respect_annotation_metadata(
                    object_=managed_execution, annotation=GetUpdateStackSetRequestManagedExecution, direction="write"
                ),
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_update_stack_set(
        self,
        *,
        action: PostUpdateStackSetRequestAction,
        version: PostUpdateStackSetRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>

        Parameters
        ----------
        action : PostUpdateStackSetRequestAction

        version : PostUpdateStackSetRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateStackSet",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_update_termination_protection(
        self,
        *,
        enable_termination_protection: bool,
        stack_name: str,
        action: GetUpdateTerminationProtectionRequestAction,
        version: GetUpdateTerminationProtectionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        Parameters
        ----------
        enable_termination_protection : bool
            Whether to enable termination protection on the specified stack.

        stack_name : str
            The name or unique ID of the stack for which you want to set termination protection.

        action : GetUpdateTerminationProtectionRequestAction

        version : GetUpdateTerminationProtectionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateTerminationProtection",
            method="GET",
            params={
                "EnableTerminationProtection": enable_termination_protection,
                "StackName": stack_name,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_update_termination_protection(
        self,
        *,
        action: PostUpdateTerminationProtectionRequestAction,
        version: PostUpdateTerminationProtectionRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        <p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        Parameters
        ----------
        action : PostUpdateTerminationProtectionRequestAction

        version : PostUpdateTerminationProtectionRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=UpdateTerminationProtection",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_validate_template(
        self,
        *,
        action: GetValidateTemplateRequestAction,
        version: GetValidateTemplateRequestVersion,
        template_body: typing.Optional[str] = None,
        template_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

        Parameters
        ----------
        action : GetValidateTemplateRequestAction

        version : GetValidateTemplateRequestVersion

        template_body : typing.Optional[str]
            <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        template_url : typing.Optional[str]
            <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ValidateTemplate",
            method="GET",
            params={
                "TemplateBody": template_body,
                "TemplateURL": template_url,
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_validate_template(
        self,
        *,
        action: PostValidateTemplateRequestAction,
        version: PostValidateTemplateRequestVersion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

        Parameters
        ----------
        action : PostValidateTemplateRequestAction

        version : PostValidateTemplateRequestVersion

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Action=ValidateTemplate",
            method="POST",
            params={
                "Action": action,
                "Version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
