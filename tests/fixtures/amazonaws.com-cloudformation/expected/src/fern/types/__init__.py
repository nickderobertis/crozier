



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .resources_to_import import ResourcesToImport
    from .resources_to_skip import ResourcesToSkip
    from .accept_terms_and_conditions import AcceptTermsAndConditions
    from .account import Account
    from .account_filter_type import AccountFilterType
    from .account_gate_result import AccountGateResult
    from .account_gate_result_status import AccountGateResultStatus
    from .account_gate_status import AccountGateStatus
    from .account_gate_status_reason import AccountGateStatusReason
    from .account_limit import AccountLimit
    from .account_limit_list import AccountLimitList
    from .account_list import AccountList
    from .accounts_url import AccountsUrl
    from .activate_type_input import ActivateTypeInput
    from .activate_type_input_type import ActivateTypeInputType
    from .activate_type_input_version_bump import ActivateTypeInputVersionBump
    from .activate_type_output import ActivateTypeOutput
    from .allowed_value import AllowedValue
    from .allowed_values import AllowedValues
    from .already_exists_exception import AlreadyExistsException
    from .arn import Arn
    from .auto_deployment import AutoDeployment
    from .auto_deployment_nullable import AutoDeploymentNullable
    from .auto_update import AutoUpdate
    from .batch_describe_type_configurations_error import BatchDescribeTypeConfigurationsError
    from .batch_describe_type_configurations_errors import BatchDescribeTypeConfigurationsErrors
    from .batch_describe_type_configurations_input import BatchDescribeTypeConfigurationsInput
    from .batch_describe_type_configurations_output import BatchDescribeTypeConfigurationsOutput
    from .boxed_integer import BoxedInteger
    from .boxed_max_results import BoxedMaxResults
    from .call_as import CallAs
    from .cancel_update_stack_input import CancelUpdateStackInput
    from .capabilities import Capabilities
    from .capabilities_reason import CapabilitiesReason
    from .capability import Capability
    from .category import Category
    from .causing_entity import CausingEntity
    from .cfn_registry_exception import CfnRegistryException
    from .change import Change
    from .change_action import ChangeAction
    from .change_resource_change import ChangeResourceChange
    from .change_resource_change_action import ChangeResourceChangeAction
    from .change_resource_change_module_info import ChangeResourceChangeModuleInfo
    from .change_resource_change_replacement import ChangeResourceChangeReplacement
    from .change_set_hook import ChangeSetHook
    from .change_set_hook_failure_mode import ChangeSetHookFailureMode
    from .change_set_hook_invocation_point import ChangeSetHookInvocationPoint
    from .change_set_hook_resource_target_details import ChangeSetHookResourceTargetDetails
    from .change_set_hook_resource_target_details_resource_action import (
        ChangeSetHookResourceTargetDetailsResourceAction,
    )
    from .change_set_hook_target_details import ChangeSetHookTargetDetails
    from .change_set_hook_target_details_resource_target_details import ChangeSetHookTargetDetailsResourceTargetDetails
    from .change_set_hook_target_details_resource_target_details_resource_action import (
        ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction,
    )
    from .change_set_hook_target_details_target_type import ChangeSetHookTargetDetailsTargetType
    from .change_set_hooks import ChangeSetHooks
    from .change_set_hooks_status import ChangeSetHooksStatus
    from .change_set_id import ChangeSetId
    from .change_set_name import ChangeSetName
    from .change_set_name_or_id import ChangeSetNameOrId
    from .change_set_not_found_exception import ChangeSetNotFoundException
    from .change_set_status import ChangeSetStatus
    from .change_set_status_reason import ChangeSetStatusReason
    from .change_set_summaries import ChangeSetSummaries
    from .change_set_summary import ChangeSetSummary
    from .change_set_summary_execution_status import ChangeSetSummaryExecutionStatus
    from .change_set_summary_status import ChangeSetSummaryStatus
    from .change_set_type import ChangeSetType
    from .change_source import ChangeSource
    from .change_type import ChangeType
    from .changes import Changes
    from .client_request_token import ClientRequestToken
    from .client_token import ClientToken
    from .configuration_schema import ConfigurationSchema
    from .connection_arn import ConnectionArn
    from .continue_update_rollback_input import ContinueUpdateRollbackInput
    from .continue_update_rollback_output import ContinueUpdateRollbackOutput
    from .create_change_set_input import CreateChangeSetInput
    from .create_change_set_input_change_set_type import CreateChangeSetInputChangeSetType
    from .create_change_set_input_rollback_configuration import CreateChangeSetInputRollbackConfiguration
    from .create_change_set_output import CreateChangeSetOutput
    from .create_stack_input import CreateStackInput
    from .create_stack_input_on_failure import CreateStackInputOnFailure
    from .create_stack_input_rollback_configuration import CreateStackInputRollbackConfiguration
    from .create_stack_instances_input import CreateStackInstancesInput
    from .create_stack_instances_input_call_as import CreateStackInstancesInputCallAs
    from .create_stack_instances_input_deployment_targets import CreateStackInstancesInputDeploymentTargets
    from .create_stack_instances_input_deployment_targets_account_filter_type import (
        CreateStackInstancesInputDeploymentTargetsAccountFilterType,
    )
    from .create_stack_instances_input_operation_preferences import CreateStackInstancesInputOperationPreferences
    from .create_stack_instances_input_operation_preferences_region_concurrency_type import (
        CreateStackInstancesInputOperationPreferencesRegionConcurrencyType,
    )
    from .create_stack_instances_output import CreateStackInstancesOutput
    from .create_stack_output import CreateStackOutput
    from .create_stack_set_input import CreateStackSetInput
    from .create_stack_set_input_auto_deployment import CreateStackSetInputAutoDeployment
    from .create_stack_set_input_call_as import CreateStackSetInputCallAs
    from .create_stack_set_input_managed_execution import CreateStackSetInputManagedExecution
    from .create_stack_set_input_permission_model import CreateStackSetInputPermissionModel
    from .create_stack_set_output import CreateStackSetOutput
    from .created_but_modified_exception import CreatedButModifiedException
    from .creation_time import CreationTime
    from .deactivate_type_input import DeactivateTypeInput
    from .deactivate_type_input_type import DeactivateTypeInputType
    from .deactivate_type_output import DeactivateTypeOutput
    from .delete_change_set_input import DeleteChangeSetInput
    from .delete_change_set_output import DeleteChangeSetOutput
    from .delete_stack_input import DeleteStackInput
    from .delete_stack_instances_input import DeleteStackInstancesInput
    from .delete_stack_instances_input_call_as import DeleteStackInstancesInputCallAs
    from .delete_stack_instances_input_deployment_targets import DeleteStackInstancesInputDeploymentTargets
    from .delete_stack_instances_input_deployment_targets_account_filter_type import (
        DeleteStackInstancesInputDeploymentTargetsAccountFilterType,
    )
    from .delete_stack_instances_input_operation_preferences import DeleteStackInstancesInputOperationPreferences
    from .delete_stack_instances_input_operation_preferences_region_concurrency_type import (
        DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType,
    )
    from .delete_stack_instances_output import DeleteStackInstancesOutput
    from .delete_stack_set_input import DeleteStackSetInput
    from .delete_stack_set_input_call_as import DeleteStackSetInputCallAs
    from .delete_stack_set_output import DeleteStackSetOutput
    from .deletion_time import DeletionTime
    from .deployment_targets import DeploymentTargets
    from .deployment_targets_account_filter_type import DeploymentTargetsAccountFilterType
    from .deprecated_status import DeprecatedStatus
    from .deregister_type_input import DeregisterTypeInput
    from .deregister_type_input_type import DeregisterTypeInputType
    from .deregister_type_output import DeregisterTypeOutput
    from .describe_account_limits_input import DescribeAccountLimitsInput
    from .describe_account_limits_output import DescribeAccountLimitsOutput
    from .describe_change_set_hooks_input import DescribeChangeSetHooksInput
    from .describe_change_set_hooks_output import DescribeChangeSetHooksOutput
    from .describe_change_set_hooks_output_status import DescribeChangeSetHooksOutputStatus
    from .describe_change_set_input import DescribeChangeSetInput
    from .describe_change_set_output import DescribeChangeSetOutput
    from .describe_change_set_output_execution_status import DescribeChangeSetOutputExecutionStatus
    from .describe_change_set_output_rollback_configuration import DescribeChangeSetOutputRollbackConfiguration
    from .describe_change_set_output_status import DescribeChangeSetOutputStatus
    from .describe_publisher_input import DescribePublisherInput
    from .describe_publisher_output import DescribePublisherOutput
    from .describe_publisher_output_identity_provider import DescribePublisherOutputIdentityProvider
    from .describe_publisher_output_publisher_status import DescribePublisherOutputPublisherStatus
    from .describe_stack_drift_detection_status_input import DescribeStackDriftDetectionStatusInput
    from .describe_stack_drift_detection_status_output import DescribeStackDriftDetectionStatusOutput
    from .describe_stack_drift_detection_status_output_detection_status import (
        DescribeStackDriftDetectionStatusOutputDetectionStatus,
    )
    from .describe_stack_drift_detection_status_output_stack_drift_status import (
        DescribeStackDriftDetectionStatusOutputStackDriftStatus,
    )
    from .describe_stack_events_input import DescribeStackEventsInput
    from .describe_stack_events_output import DescribeStackEventsOutput
    from .describe_stack_instance_input import DescribeStackInstanceInput
    from .describe_stack_instance_input_call_as import DescribeStackInstanceInputCallAs
    from .describe_stack_instance_output import DescribeStackInstanceOutput
    from .describe_stack_instance_output_stack_instance import DescribeStackInstanceOutputStackInstance
    from .describe_stack_instance_output_stack_instance_drift_status import (
        DescribeStackInstanceOutputStackInstanceDriftStatus,
    )
    from .describe_stack_instance_output_stack_instance_stack_instance_status import (
        DescribeStackInstanceOutputStackInstanceStackInstanceStatus,
    )
    from .describe_stack_instance_output_stack_instance_stack_instance_status_detailed_status import (
        DescribeStackInstanceOutputStackInstanceStackInstanceStatusDetailedStatus,
    )
    from .describe_stack_instance_output_stack_instance_status import DescribeStackInstanceOutputStackInstanceStatus
    from .describe_stack_resource_drifts_input import DescribeStackResourceDriftsInput
    from .describe_stack_resource_drifts_output import DescribeStackResourceDriftsOutput
    from .describe_stack_resource_input import DescribeStackResourceInput
    from .describe_stack_resource_output import DescribeStackResourceOutput
    from .describe_stack_resource_output_stack_resource_detail import DescribeStackResourceOutputStackResourceDetail
    from .describe_stack_resource_output_stack_resource_detail_drift_information import (
        DescribeStackResourceOutputStackResourceDetailDriftInformation,
    )
    from .describe_stack_resource_output_stack_resource_detail_drift_information_stack_resource_drift_status import (
        DescribeStackResourceOutputStackResourceDetailDriftInformationStackResourceDriftStatus,
    )
    from .describe_stack_resource_output_stack_resource_detail_module_info import (
        DescribeStackResourceOutputStackResourceDetailModuleInfo,
    )
    from .describe_stack_resource_output_stack_resource_detail_resource_status import (
        DescribeStackResourceOutputStackResourceDetailResourceStatus,
    )
    from .describe_stack_resources_input import DescribeStackResourcesInput
    from .describe_stack_resources_output import DescribeStackResourcesOutput
    from .describe_stack_set_input import DescribeStackSetInput
    from .describe_stack_set_input_call_as import DescribeStackSetInputCallAs
    from .describe_stack_set_operation_input import DescribeStackSetOperationInput
    from .describe_stack_set_operation_input_call_as import DescribeStackSetOperationInputCallAs
    from .describe_stack_set_operation_output import DescribeStackSetOperationOutput
    from .describe_stack_set_operation_output_stack_set_operation import (
        DescribeStackSetOperationOutputStackSetOperation,
    )
    from .describe_stack_set_operation_output_stack_set_operation_action import (
        DescribeStackSetOperationOutputStackSetOperationAction,
    )
    from .describe_stack_set_operation_output_stack_set_operation_deployment_targets import (
        DescribeStackSetOperationOutputStackSetOperationDeploymentTargets,
    )
    from .describe_stack_set_operation_output_stack_set_operation_deployment_targets_account_filter_type import (
        DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType,
    )
    from .describe_stack_set_operation_output_stack_set_operation_operation_preferences import (
        DescribeStackSetOperationOutputStackSetOperationOperationPreferences,
    )
    from .describe_stack_set_operation_output_stack_set_operation_operation_preferences_region_concurrency_type import (
        DescribeStackSetOperationOutputStackSetOperationOperationPreferencesRegionConcurrencyType,
    )
    from .describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details import (
        DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetails,
    )
    from .describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_detection_status import (
        DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus,
    )
    from .describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_status import (
        DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus,
    )
    from .describe_stack_set_operation_output_stack_set_operation_status import (
        DescribeStackSetOperationOutputStackSetOperationStatus,
    )
    from .describe_stack_set_operation_output_stack_set_operation_status_details import (
        DescribeStackSetOperationOutputStackSetOperationStatusDetails,
    )
    from .describe_stack_set_output import DescribeStackSetOutput
    from .describe_stack_set_output_stack_set import DescribeStackSetOutputStackSet
    from .describe_stack_set_output_stack_set_auto_deployment import DescribeStackSetOutputStackSetAutoDeployment
    from .describe_stack_set_output_stack_set_managed_execution import DescribeStackSetOutputStackSetManagedExecution
    from .describe_stack_set_output_stack_set_permission_model import DescribeStackSetOutputStackSetPermissionModel
    from .describe_stack_set_output_stack_set_stack_set_drift_detection_details import (
        DescribeStackSetOutputStackSetStackSetDriftDetectionDetails,
    )
    from .describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_detection_status import (
        DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftDetectionStatus,
    )
    from .describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_status import (
        DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftStatus,
    )
    from .describe_stack_set_output_stack_set_status import DescribeStackSetOutputStackSetStatus
    from .describe_stacks_input import DescribeStacksInput
    from .describe_stacks_output import DescribeStacksOutput
    from .describe_type_input import DescribeTypeInput
    from .describe_type_input_type import DescribeTypeInputType
    from .describe_type_output import DescribeTypeOutput
    from .describe_type_output_deprecated_status import DescribeTypeOutputDeprecatedStatus
    from .describe_type_output_logging_config import DescribeTypeOutputLoggingConfig
    from .describe_type_output_provisioning_type import DescribeTypeOutputProvisioningType
    from .describe_type_output_type import DescribeTypeOutputType
    from .describe_type_output_type_tests_status import DescribeTypeOutputTypeTestsStatus
    from .describe_type_output_visibility import DescribeTypeOutputVisibility
    from .describe_type_registration_input import DescribeTypeRegistrationInput
    from .describe_type_registration_output import DescribeTypeRegistrationOutput
    from .describe_type_registration_output_progress_status import DescribeTypeRegistrationOutputProgressStatus
    from .description import Description
    from .detect_stack_drift_input import DetectStackDriftInput
    from .detect_stack_drift_output import DetectStackDriftOutput
    from .detect_stack_resource_drift_input import DetectStackResourceDriftInput
    from .detect_stack_resource_drift_output import DetectStackResourceDriftOutput
    from .detect_stack_resource_drift_output_stack_resource_drift import (
        DetectStackResourceDriftOutputStackResourceDrift,
    )
    from .detect_stack_resource_drift_output_stack_resource_drift_module_info import (
        DetectStackResourceDriftOutputStackResourceDriftModuleInfo,
    )
    from .detect_stack_resource_drift_output_stack_resource_drift_stack_resource_drift_status import (
        DetectStackResourceDriftOutputStackResourceDriftStackResourceDriftStatus,
    )
    from .detect_stack_set_drift_input import DetectStackSetDriftInput
    from .detect_stack_set_drift_input_call_as import DetectStackSetDriftInputCallAs
    from .detect_stack_set_drift_output import DetectStackSetDriftOutput
    from .difference_type import DifferenceType
    from .disable_rollback import DisableRollback
    from .drifted_stack_instances_count import DriftedStackInstancesCount
    from .enable_termination_protection import EnableTerminationProtection
    from .error_code import ErrorCode
    from .error_message import ErrorMessage
    from .estimate_template_cost_input import EstimateTemplateCostInput
    from .estimate_template_cost_output import EstimateTemplateCostOutput
    from .evaluation_type import EvaluationType
    from .event_id import EventId
    from .execute_change_set_input import ExecuteChangeSetInput
    from .execute_change_set_output import ExecuteChangeSetOutput
    from .execution_role_name import ExecutionRoleName
    from .execution_status import ExecutionStatus
    from .export import Export
    from .export_name import ExportName
    from .export_value import ExportValue
    from .exports import Exports
    from .failed_stack_instances_count import FailedStackInstancesCount
    from .failure_tolerance_count import FailureToleranceCount
    from .failure_tolerance_percentage import FailureTolerancePercentage
    from .get_activate_type_request_action import GetActivateTypeRequestAction
    from .get_activate_type_request_logging_config import GetActivateTypeRequestLoggingConfig
    from .get_activate_type_request_type import GetActivateTypeRequestType
    from .get_activate_type_request_version import GetActivateTypeRequestVersion
    from .get_activate_type_request_version_bump import GetActivateTypeRequestVersionBump
    from .get_batch_describe_type_configurations_request_action import GetBatchDescribeTypeConfigurationsRequestAction
    from .get_batch_describe_type_configurations_request_version import GetBatchDescribeTypeConfigurationsRequestVersion
    from .get_cancel_update_stack_request_action import GetCancelUpdateStackRequestAction
    from .get_cancel_update_stack_request_version import GetCancelUpdateStackRequestVersion
    from .get_continue_update_rollback_request_action import GetContinueUpdateRollbackRequestAction
    from .get_continue_update_rollback_request_version import GetContinueUpdateRollbackRequestVersion
    from .get_create_change_set_request_action import GetCreateChangeSetRequestAction
    from .get_create_change_set_request_change_set_type import GetCreateChangeSetRequestChangeSetType
    from .get_create_change_set_request_rollback_configuration import GetCreateChangeSetRequestRollbackConfiguration
    from .get_create_change_set_request_version import GetCreateChangeSetRequestVersion
    from .get_create_stack_instances_request_action import GetCreateStackInstancesRequestAction
    from .get_create_stack_instances_request_call_as import GetCreateStackInstancesRequestCallAs
    from .get_create_stack_instances_request_deployment_targets import GetCreateStackInstancesRequestDeploymentTargets
    from .get_create_stack_instances_request_deployment_targets_account_filter_type import (
        GetCreateStackInstancesRequestDeploymentTargetsAccountFilterType,
    )
    from .get_create_stack_instances_request_operation_preferences import (
        GetCreateStackInstancesRequestOperationPreferences,
    )
    from .get_create_stack_instances_request_operation_preferences_region_concurrency_type import (
        GetCreateStackInstancesRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_create_stack_instances_request_version import GetCreateStackInstancesRequestVersion
    from .get_create_stack_request_action import GetCreateStackRequestAction
    from .get_create_stack_request_on_failure import GetCreateStackRequestOnFailure
    from .get_create_stack_request_rollback_configuration import GetCreateStackRequestRollbackConfiguration
    from .get_create_stack_request_version import GetCreateStackRequestVersion
    from .get_create_stack_set_request_action import GetCreateStackSetRequestAction
    from .get_create_stack_set_request_auto_deployment import GetCreateStackSetRequestAutoDeployment
    from .get_create_stack_set_request_call_as import GetCreateStackSetRequestCallAs
    from .get_create_stack_set_request_managed_execution import GetCreateStackSetRequestManagedExecution
    from .get_create_stack_set_request_permission_model import GetCreateStackSetRequestPermissionModel
    from .get_create_stack_set_request_version import GetCreateStackSetRequestVersion
    from .get_deactivate_type_request_action import GetDeactivateTypeRequestAction
    from .get_deactivate_type_request_type import GetDeactivateTypeRequestType
    from .get_deactivate_type_request_version import GetDeactivateTypeRequestVersion
    from .get_delete_change_set_request_action import GetDeleteChangeSetRequestAction
    from .get_delete_change_set_request_version import GetDeleteChangeSetRequestVersion
    from .get_delete_stack_instances_request_action import GetDeleteStackInstancesRequestAction
    from .get_delete_stack_instances_request_call_as import GetDeleteStackInstancesRequestCallAs
    from .get_delete_stack_instances_request_deployment_targets import GetDeleteStackInstancesRequestDeploymentTargets
    from .get_delete_stack_instances_request_deployment_targets_account_filter_type import (
        GetDeleteStackInstancesRequestDeploymentTargetsAccountFilterType,
    )
    from .get_delete_stack_instances_request_operation_preferences import (
        GetDeleteStackInstancesRequestOperationPreferences,
    )
    from .get_delete_stack_instances_request_operation_preferences_region_concurrency_type import (
        GetDeleteStackInstancesRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_delete_stack_instances_request_version import GetDeleteStackInstancesRequestVersion
    from .get_delete_stack_request_action import GetDeleteStackRequestAction
    from .get_delete_stack_request_version import GetDeleteStackRequestVersion
    from .get_delete_stack_set_request_action import GetDeleteStackSetRequestAction
    from .get_delete_stack_set_request_call_as import GetDeleteStackSetRequestCallAs
    from .get_delete_stack_set_request_version import GetDeleteStackSetRequestVersion
    from .get_deregister_type_request_action import GetDeregisterTypeRequestAction
    from .get_deregister_type_request_type import GetDeregisterTypeRequestType
    from .get_deregister_type_request_version import GetDeregisterTypeRequestVersion
    from .get_describe_account_limits_request_action import GetDescribeAccountLimitsRequestAction
    from .get_describe_account_limits_request_version import GetDescribeAccountLimitsRequestVersion
    from .get_describe_change_set_hooks_request_action import GetDescribeChangeSetHooksRequestAction
    from .get_describe_change_set_hooks_request_version import GetDescribeChangeSetHooksRequestVersion
    from .get_describe_change_set_request_action import GetDescribeChangeSetRequestAction
    from .get_describe_change_set_request_version import GetDescribeChangeSetRequestVersion
    from .get_describe_publisher_request_action import GetDescribePublisherRequestAction
    from .get_describe_publisher_request_version import GetDescribePublisherRequestVersion
    from .get_describe_stack_drift_detection_status_request_action import (
        GetDescribeStackDriftDetectionStatusRequestAction,
    )
    from .get_describe_stack_drift_detection_status_request_version import (
        GetDescribeStackDriftDetectionStatusRequestVersion,
    )
    from .get_describe_stack_events_request_action import GetDescribeStackEventsRequestAction
    from .get_describe_stack_events_request_version import GetDescribeStackEventsRequestVersion
    from .get_describe_stack_instance_request_action import GetDescribeStackInstanceRequestAction
    from .get_describe_stack_instance_request_call_as import GetDescribeStackInstanceRequestCallAs
    from .get_describe_stack_instance_request_version import GetDescribeStackInstanceRequestVersion
    from .get_describe_stack_resource_drifts_request_action import GetDescribeStackResourceDriftsRequestAction
    from .get_describe_stack_resource_drifts_request_version import GetDescribeStackResourceDriftsRequestVersion
    from .get_describe_stack_resource_request_action import GetDescribeStackResourceRequestAction
    from .get_describe_stack_resource_request_version import GetDescribeStackResourceRequestVersion
    from .get_describe_stack_resources_request_action import GetDescribeStackResourcesRequestAction
    from .get_describe_stack_resources_request_version import GetDescribeStackResourcesRequestVersion
    from .get_describe_stack_set_operation_request_action import GetDescribeStackSetOperationRequestAction
    from .get_describe_stack_set_operation_request_call_as import GetDescribeStackSetOperationRequestCallAs
    from .get_describe_stack_set_operation_request_version import GetDescribeStackSetOperationRequestVersion
    from .get_describe_stack_set_request_action import GetDescribeStackSetRequestAction
    from .get_describe_stack_set_request_call_as import GetDescribeStackSetRequestCallAs
    from .get_describe_stack_set_request_version import GetDescribeStackSetRequestVersion
    from .get_describe_stacks_request_action import GetDescribeStacksRequestAction
    from .get_describe_stacks_request_version import GetDescribeStacksRequestVersion
    from .get_describe_type_registration_request_action import GetDescribeTypeRegistrationRequestAction
    from .get_describe_type_registration_request_version import GetDescribeTypeRegistrationRequestVersion
    from .get_describe_type_request_action import GetDescribeTypeRequestAction
    from .get_describe_type_request_type import GetDescribeTypeRequestType
    from .get_describe_type_request_version import GetDescribeTypeRequestVersion
    from .get_detect_stack_drift_request_action import GetDetectStackDriftRequestAction
    from .get_detect_stack_drift_request_version import GetDetectStackDriftRequestVersion
    from .get_detect_stack_resource_drift_request_action import GetDetectStackResourceDriftRequestAction
    from .get_detect_stack_resource_drift_request_version import GetDetectStackResourceDriftRequestVersion
    from .get_detect_stack_set_drift_request_action import GetDetectStackSetDriftRequestAction
    from .get_detect_stack_set_drift_request_call_as import GetDetectStackSetDriftRequestCallAs
    from .get_detect_stack_set_drift_request_operation_preferences import (
        GetDetectStackSetDriftRequestOperationPreferences,
    )
    from .get_detect_stack_set_drift_request_operation_preferences_region_concurrency_type import (
        GetDetectStackSetDriftRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_detect_stack_set_drift_request_version import GetDetectStackSetDriftRequestVersion
    from .get_estimate_template_cost_request_action import GetEstimateTemplateCostRequestAction
    from .get_estimate_template_cost_request_version import GetEstimateTemplateCostRequestVersion
    from .get_execute_change_set_request_action import GetExecuteChangeSetRequestAction
    from .get_execute_change_set_request_version import GetExecuteChangeSetRequestVersion
    from .get_get_stack_policy_request_action import GetGetStackPolicyRequestAction
    from .get_get_stack_policy_request_version import GetGetStackPolicyRequestVersion
    from .get_get_template_request_action import GetGetTemplateRequestAction
    from .get_get_template_request_template_stage import GetGetTemplateRequestTemplateStage
    from .get_get_template_request_version import GetGetTemplateRequestVersion
    from .get_get_template_summary_request_action import GetGetTemplateSummaryRequestAction
    from .get_get_template_summary_request_call_as import GetGetTemplateSummaryRequestCallAs
    from .get_get_template_summary_request_version import GetGetTemplateSummaryRequestVersion
    from .get_import_stacks_to_stack_set_request_action import GetImportStacksToStackSetRequestAction
    from .get_import_stacks_to_stack_set_request_call_as import GetImportStacksToStackSetRequestCallAs
    from .get_import_stacks_to_stack_set_request_operation_preferences import (
        GetImportStacksToStackSetRequestOperationPreferences,
    )
    from .get_import_stacks_to_stack_set_request_operation_preferences_region_concurrency_type import (
        GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_import_stacks_to_stack_set_request_version import GetImportStacksToStackSetRequestVersion
    from .get_list_change_sets_request_action import GetListChangeSetsRequestAction
    from .get_list_change_sets_request_version import GetListChangeSetsRequestVersion
    from .get_list_exports_request_action import GetListExportsRequestAction
    from .get_list_exports_request_version import GetListExportsRequestVersion
    from .get_list_imports_request_action import GetListImportsRequestAction
    from .get_list_imports_request_version import GetListImportsRequestVersion
    from .get_list_stack_instances_request_action import GetListStackInstancesRequestAction
    from .get_list_stack_instances_request_call_as import GetListStackInstancesRequestCallAs
    from .get_list_stack_instances_request_version import GetListStackInstancesRequestVersion
    from .get_list_stack_resources_request_action import GetListStackResourcesRequestAction
    from .get_list_stack_resources_request_version import GetListStackResourcesRequestVersion
    from .get_list_stack_set_operation_results_request_action import GetListStackSetOperationResultsRequestAction
    from .get_list_stack_set_operation_results_request_call_as import GetListStackSetOperationResultsRequestCallAs
    from .get_list_stack_set_operation_results_request_version import GetListStackSetOperationResultsRequestVersion
    from .get_list_stack_set_operations_request_action import GetListStackSetOperationsRequestAction
    from .get_list_stack_set_operations_request_call_as import GetListStackSetOperationsRequestCallAs
    from .get_list_stack_set_operations_request_version import GetListStackSetOperationsRequestVersion
    from .get_list_stack_sets_request_action import GetListStackSetsRequestAction
    from .get_list_stack_sets_request_call_as import GetListStackSetsRequestCallAs
    from .get_list_stack_sets_request_status import GetListStackSetsRequestStatus
    from .get_list_stack_sets_request_version import GetListStackSetsRequestVersion
    from .get_list_stacks_request_action import GetListStacksRequestAction
    from .get_list_stacks_request_version import GetListStacksRequestVersion
    from .get_list_type_registrations_request_action import GetListTypeRegistrationsRequestAction
    from .get_list_type_registrations_request_registration_status_filter import (
        GetListTypeRegistrationsRequestRegistrationStatusFilter,
    )
    from .get_list_type_registrations_request_type import GetListTypeRegistrationsRequestType
    from .get_list_type_registrations_request_version import GetListTypeRegistrationsRequestVersion
    from .get_list_type_versions_request_action import GetListTypeVersionsRequestAction
    from .get_list_type_versions_request_deprecated_status import GetListTypeVersionsRequestDeprecatedStatus
    from .get_list_type_versions_request_type import GetListTypeVersionsRequestType
    from .get_list_type_versions_request_version import GetListTypeVersionsRequestVersion
    from .get_list_types_request_action import GetListTypesRequestAction
    from .get_list_types_request_deprecated_status import GetListTypesRequestDeprecatedStatus
    from .get_list_types_request_filters import GetListTypesRequestFilters
    from .get_list_types_request_filters_category import GetListTypesRequestFiltersCategory
    from .get_list_types_request_provisioning_type import GetListTypesRequestProvisioningType
    from .get_list_types_request_type import GetListTypesRequestType
    from .get_list_types_request_version import GetListTypesRequestVersion
    from .get_list_types_request_visibility import GetListTypesRequestVisibility
    from .get_publish_type_request_action import GetPublishTypeRequestAction
    from .get_publish_type_request_type import GetPublishTypeRequestType
    from .get_publish_type_request_version import GetPublishTypeRequestVersion
    from .get_record_handler_progress_request_action import GetRecordHandlerProgressRequestAction
    from .get_record_handler_progress_request_current_operation_status import (
        GetRecordHandlerProgressRequestCurrentOperationStatus,
    )
    from .get_record_handler_progress_request_error_code import GetRecordHandlerProgressRequestErrorCode
    from .get_record_handler_progress_request_operation_status import GetRecordHandlerProgressRequestOperationStatus
    from .get_record_handler_progress_request_version import GetRecordHandlerProgressRequestVersion
    from .get_register_publisher_request_action import GetRegisterPublisherRequestAction
    from .get_register_publisher_request_version import GetRegisterPublisherRequestVersion
    from .get_register_type_request_action import GetRegisterTypeRequestAction
    from .get_register_type_request_logging_config import GetRegisterTypeRequestLoggingConfig
    from .get_register_type_request_type import GetRegisterTypeRequestType
    from .get_register_type_request_version import GetRegisterTypeRequestVersion
    from .get_rollback_stack_request_action import GetRollbackStackRequestAction
    from .get_rollback_stack_request_version import GetRollbackStackRequestVersion
    from .get_set_stack_policy_request_action import GetSetStackPolicyRequestAction
    from .get_set_stack_policy_request_version import GetSetStackPolicyRequestVersion
    from .get_set_type_configuration_request_action import GetSetTypeConfigurationRequestAction
    from .get_set_type_configuration_request_type import GetSetTypeConfigurationRequestType
    from .get_set_type_configuration_request_version import GetSetTypeConfigurationRequestVersion
    from .get_set_type_default_version_request_action import GetSetTypeDefaultVersionRequestAction
    from .get_set_type_default_version_request_type import GetSetTypeDefaultVersionRequestType
    from .get_set_type_default_version_request_version import GetSetTypeDefaultVersionRequestVersion
    from .get_signal_resource_request_action import GetSignalResourceRequestAction
    from .get_signal_resource_request_status import GetSignalResourceRequestStatus
    from .get_signal_resource_request_version import GetSignalResourceRequestVersion
    from .get_stack_policy_input import GetStackPolicyInput
    from .get_stack_policy_output import GetStackPolicyOutput
    from .get_stop_stack_set_operation_request_action import GetStopStackSetOperationRequestAction
    from .get_stop_stack_set_operation_request_call_as import GetStopStackSetOperationRequestCallAs
    from .get_stop_stack_set_operation_request_version import GetStopStackSetOperationRequestVersion
    from .get_template_input import GetTemplateInput
    from .get_template_input_template_stage import GetTemplateInputTemplateStage
    from .get_template_output import GetTemplateOutput
    from .get_template_summary_input import GetTemplateSummaryInput
    from .get_template_summary_input_call_as import GetTemplateSummaryInputCallAs
    from .get_template_summary_output import GetTemplateSummaryOutput
    from .get_test_type_request_action import GetTestTypeRequestAction
    from .get_test_type_request_type import GetTestTypeRequestType
    from .get_test_type_request_version import GetTestTypeRequestVersion
    from .get_update_stack_instances_request_action import GetUpdateStackInstancesRequestAction
    from .get_update_stack_instances_request_call_as import GetUpdateStackInstancesRequestCallAs
    from .get_update_stack_instances_request_deployment_targets import GetUpdateStackInstancesRequestDeploymentTargets
    from .get_update_stack_instances_request_deployment_targets_account_filter_type import (
        GetUpdateStackInstancesRequestDeploymentTargetsAccountFilterType,
    )
    from .get_update_stack_instances_request_operation_preferences import (
        GetUpdateStackInstancesRequestOperationPreferences,
    )
    from .get_update_stack_instances_request_operation_preferences_region_concurrency_type import (
        GetUpdateStackInstancesRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_update_stack_instances_request_version import GetUpdateStackInstancesRequestVersion
    from .get_update_stack_request_action import GetUpdateStackRequestAction
    from .get_update_stack_request_rollback_configuration import GetUpdateStackRequestRollbackConfiguration
    from .get_update_stack_request_version import GetUpdateStackRequestVersion
    from .get_update_stack_set_request_action import GetUpdateStackSetRequestAction
    from .get_update_stack_set_request_auto_deployment import GetUpdateStackSetRequestAutoDeployment
    from .get_update_stack_set_request_call_as import GetUpdateStackSetRequestCallAs
    from .get_update_stack_set_request_deployment_targets import GetUpdateStackSetRequestDeploymentTargets
    from .get_update_stack_set_request_deployment_targets_account_filter_type import (
        GetUpdateStackSetRequestDeploymentTargetsAccountFilterType,
    )
    from .get_update_stack_set_request_managed_execution import GetUpdateStackSetRequestManagedExecution
    from .get_update_stack_set_request_operation_preferences import GetUpdateStackSetRequestOperationPreferences
    from .get_update_stack_set_request_operation_preferences_region_concurrency_type import (
        GetUpdateStackSetRequestOperationPreferencesRegionConcurrencyType,
    )
    from .get_update_stack_set_request_permission_model import GetUpdateStackSetRequestPermissionModel
    from .get_update_stack_set_request_version import GetUpdateStackSetRequestVersion
    from .get_update_termination_protection_request_action import GetUpdateTerminationProtectionRequestAction
    from .get_update_termination_protection_request_version import GetUpdateTerminationProtectionRequestVersion
    from .get_validate_template_request_action import GetValidateTemplateRequestAction
    from .get_validate_template_request_version import GetValidateTemplateRequestVersion
    from .handler_error_code import HandlerErrorCode
    from .hook_failure_mode import HookFailureMode
    from .hook_invocation_count import HookInvocationCount
    from .hook_invocation_point import HookInvocationPoint
    from .hook_status import HookStatus
    from .hook_status_reason import HookStatusReason
    from .hook_target_type import HookTargetType
    from .hook_target_type_name import HookTargetTypeName
    from .hook_type import HookType
    from .hook_type_configuration_version_id import HookTypeConfigurationVersionId
    from .hook_type_name import HookTypeName
    from .hook_type_version_id import HookTypeVersionId
    from .identity_provider import IdentityProvider
    from .import_stacks_to_stack_set_input import ImportStacksToStackSetInput
    from .import_stacks_to_stack_set_input_call_as import ImportStacksToStackSetInputCallAs
    from .import_stacks_to_stack_set_output import ImportStacksToStackSetOutput
    from .imports import Imports
    from .in_progress_stack_instances_count import InProgressStackInstancesCount
    from .in_sync_stack_instances_count import InSyncStackInstancesCount
    from .include_nested_stacks import IncludeNestedStacks
    from .insufficient_capabilities_exception import InsufficientCapabilitiesException
    from .invalid_change_set_status_exception import InvalidChangeSetStatusException
    from .invalid_operation_exception import InvalidOperationException
    from .invalid_state_transition_exception import InvalidStateTransitionException
    from .is_activated import IsActivated
    from .is_default_configuration import IsDefaultConfiguration
    from .is_default_version import IsDefaultVersion
    from .key import Key
    from .last_updated_time import LastUpdatedTime
    from .limit_exceeded_exception import LimitExceededException
    from .limit_name import LimitName
    from .limit_value import LimitValue
    from .list_change_sets_input import ListChangeSetsInput
    from .list_change_sets_output import ListChangeSetsOutput
    from .list_exports_input import ListExportsInput
    from .list_exports_output import ListExportsOutput
    from .list_imports_input import ListImportsInput
    from .list_imports_output import ListImportsOutput
    from .list_stack_instances_input import ListStackInstancesInput
    from .list_stack_instances_input_call_as import ListStackInstancesInputCallAs
    from .list_stack_instances_output import ListStackInstancesOutput
    from .list_stack_resources_input import ListStackResourcesInput
    from .list_stack_resources_output import ListStackResourcesOutput
    from .list_stack_set_operation_results_input import ListStackSetOperationResultsInput
    from .list_stack_set_operation_results_input_call_as import ListStackSetOperationResultsInputCallAs
    from .list_stack_set_operation_results_output import ListStackSetOperationResultsOutput
    from .list_stack_set_operations_input import ListStackSetOperationsInput
    from .list_stack_set_operations_input_call_as import ListStackSetOperationsInputCallAs
    from .list_stack_set_operations_output import ListStackSetOperationsOutput
    from .list_stack_sets_input import ListStackSetsInput
    from .list_stack_sets_input_call_as import ListStackSetsInputCallAs
    from .list_stack_sets_input_status import ListStackSetsInputStatus
    from .list_stack_sets_output import ListStackSetsOutput
    from .list_stacks_input import ListStacksInput
    from .list_stacks_output import ListStacksOutput
    from .list_type_registrations_input import ListTypeRegistrationsInput
    from .list_type_registrations_input_registration_status_filter import (
        ListTypeRegistrationsInputRegistrationStatusFilter,
    )
    from .list_type_registrations_input_type import ListTypeRegistrationsInputType
    from .list_type_registrations_output import ListTypeRegistrationsOutput
    from .list_type_versions_input import ListTypeVersionsInput
    from .list_type_versions_input_deprecated_status import ListTypeVersionsInputDeprecatedStatus
    from .list_type_versions_input_type import ListTypeVersionsInputType
    from .list_type_versions_output import ListTypeVersionsOutput
    from .list_types_input import ListTypesInput
    from .list_types_input_deprecated_status import ListTypesInputDeprecatedStatus
    from .list_types_input_filters import ListTypesInputFilters
    from .list_types_input_filters_category import ListTypesInputFiltersCategory
    from .list_types_input_provisioning_type import ListTypesInputProvisioningType
    from .list_types_input_type import ListTypesInputType
    from .list_types_input_visibility import ListTypesInputVisibility
    from .list_types_output import ListTypesOutput
    from .log_group_name import LogGroupName
    from .logging_config import LoggingConfig
    from .logical_id_hierarchy import LogicalIdHierarchy
    from .logical_resource_id import LogicalResourceId
    from .logical_resource_ids import LogicalResourceIds
    from .major_version import MajorVersion
    from .managed_execution import ManagedExecution
    from .managed_execution_nullable import ManagedExecutionNullable
    from .max_concurrent_count import MaxConcurrentCount
    from .max_concurrent_percentage import MaxConcurrentPercentage
    from .max_results import MaxResults
    from .metadata import Metadata
    from .module_info import ModuleInfo
    from .monitoring_time_in_minutes import MonitoringTimeInMinutes
    from .name_already_exists_exception import NameAlreadyExistsException
    from .next_token import NextToken
    from .no_echo import NoEcho
    from .notification_ar_ns import NotificationArNs
    from .notification_arn import NotificationArn
    from .on_failure import OnFailure
    from .operation_id_already_exists_exception import OperationIdAlreadyExistsException
    from .operation_in_progress_exception import OperationInProgressException
    from .operation_not_found_exception import OperationNotFoundException
    from .operation_result_filter import OperationResultFilter
    from .operation_result_filter_name import OperationResultFilterName
    from .operation_result_filter_values import OperationResultFilterValues
    from .operation_result_filters import OperationResultFilters
    from .operation_status import OperationStatus
    from .operation_status_check_failed_exception import OperationStatusCheckFailedException
    from .optional_secure_url import OptionalSecureUrl
    from .organizational_unit_id import OrganizationalUnitId
    from .organizational_unit_id_list import OrganizationalUnitIdList
    from .output import Output
    from .output_key import OutputKey
    from .output_value import OutputValue
    from .outputs import Outputs
    from .parameter import Parameter
    from .parameter_constraints import ParameterConstraints
    from .parameter_declaration import ParameterDeclaration
    from .parameter_declaration_parameter_constraints import ParameterDeclarationParameterConstraints
    from .parameter_declarations import ParameterDeclarations
    from .parameter_key import ParameterKey
    from .parameter_type import ParameterType
    from .parameter_value import ParameterValue
    from .parameters import Parameters
    from .permission_models import PermissionModels
    from .physical_resource_id import PhysicalResourceId
    from .physical_resource_id_context import PhysicalResourceIdContext
    from .physical_resource_id_context_key_value_pair import PhysicalResourceIdContextKeyValuePair
    from .post_activate_type_request_action import PostActivateTypeRequestAction
    from .post_activate_type_request_version import PostActivateTypeRequestVersion
    from .post_batch_describe_type_configurations_request_action import PostBatchDescribeTypeConfigurationsRequestAction
    from .post_batch_describe_type_configurations_request_version import (
        PostBatchDescribeTypeConfigurationsRequestVersion,
    )
    from .post_cancel_update_stack_request_action import PostCancelUpdateStackRequestAction
    from .post_cancel_update_stack_request_version import PostCancelUpdateStackRequestVersion
    from .post_continue_update_rollback_request_action import PostContinueUpdateRollbackRequestAction
    from .post_continue_update_rollback_request_version import PostContinueUpdateRollbackRequestVersion
    from .post_create_change_set_request_action import PostCreateChangeSetRequestAction
    from .post_create_change_set_request_version import PostCreateChangeSetRequestVersion
    from .post_create_stack_instances_request_action import PostCreateStackInstancesRequestAction
    from .post_create_stack_instances_request_version import PostCreateStackInstancesRequestVersion
    from .post_create_stack_request_action import PostCreateStackRequestAction
    from .post_create_stack_request_version import PostCreateStackRequestVersion
    from .post_create_stack_set_request_action import PostCreateStackSetRequestAction
    from .post_create_stack_set_request_version import PostCreateStackSetRequestVersion
    from .post_deactivate_type_request_action import PostDeactivateTypeRequestAction
    from .post_deactivate_type_request_version import PostDeactivateTypeRequestVersion
    from .post_delete_change_set_request_action import PostDeleteChangeSetRequestAction
    from .post_delete_change_set_request_version import PostDeleteChangeSetRequestVersion
    from .post_delete_stack_instances_request_action import PostDeleteStackInstancesRequestAction
    from .post_delete_stack_instances_request_version import PostDeleteStackInstancesRequestVersion
    from .post_delete_stack_request_action import PostDeleteStackRequestAction
    from .post_delete_stack_request_version import PostDeleteStackRequestVersion
    from .post_delete_stack_set_request_action import PostDeleteStackSetRequestAction
    from .post_delete_stack_set_request_version import PostDeleteStackSetRequestVersion
    from .post_deregister_type_request_action import PostDeregisterTypeRequestAction
    from .post_deregister_type_request_version import PostDeregisterTypeRequestVersion
    from .post_describe_account_limits_request_action import PostDescribeAccountLimitsRequestAction
    from .post_describe_account_limits_request_version import PostDescribeAccountLimitsRequestVersion
    from .post_describe_change_set_hooks_request_action import PostDescribeChangeSetHooksRequestAction
    from .post_describe_change_set_hooks_request_version import PostDescribeChangeSetHooksRequestVersion
    from .post_describe_change_set_request_action import PostDescribeChangeSetRequestAction
    from .post_describe_change_set_request_version import PostDescribeChangeSetRequestVersion
    from .post_describe_publisher_request_action import PostDescribePublisherRequestAction
    from .post_describe_publisher_request_version import PostDescribePublisherRequestVersion
    from .post_describe_stack_drift_detection_status_request_action import (
        PostDescribeStackDriftDetectionStatusRequestAction,
    )
    from .post_describe_stack_drift_detection_status_request_version import (
        PostDescribeStackDriftDetectionStatusRequestVersion,
    )
    from .post_describe_stack_events_request_action import PostDescribeStackEventsRequestAction
    from .post_describe_stack_events_request_version import PostDescribeStackEventsRequestVersion
    from .post_describe_stack_instance_request_action import PostDescribeStackInstanceRequestAction
    from .post_describe_stack_instance_request_version import PostDescribeStackInstanceRequestVersion
    from .post_describe_stack_resource_drifts_request_action import PostDescribeStackResourceDriftsRequestAction
    from .post_describe_stack_resource_drifts_request_version import PostDescribeStackResourceDriftsRequestVersion
    from .post_describe_stack_resource_request_action import PostDescribeStackResourceRequestAction
    from .post_describe_stack_resource_request_version import PostDescribeStackResourceRequestVersion
    from .post_describe_stack_resources_request_action import PostDescribeStackResourcesRequestAction
    from .post_describe_stack_resources_request_version import PostDescribeStackResourcesRequestVersion
    from .post_describe_stack_set_operation_request_action import PostDescribeStackSetOperationRequestAction
    from .post_describe_stack_set_operation_request_version import PostDescribeStackSetOperationRequestVersion
    from .post_describe_stack_set_request_action import PostDescribeStackSetRequestAction
    from .post_describe_stack_set_request_version import PostDescribeStackSetRequestVersion
    from .post_describe_stacks_request_action import PostDescribeStacksRequestAction
    from .post_describe_stacks_request_version import PostDescribeStacksRequestVersion
    from .post_describe_type_registration_request_action import PostDescribeTypeRegistrationRequestAction
    from .post_describe_type_registration_request_version import PostDescribeTypeRegistrationRequestVersion
    from .post_describe_type_request_action import PostDescribeTypeRequestAction
    from .post_describe_type_request_version import PostDescribeTypeRequestVersion
    from .post_detect_stack_drift_request_action import PostDetectStackDriftRequestAction
    from .post_detect_stack_drift_request_version import PostDetectStackDriftRequestVersion
    from .post_detect_stack_resource_drift_request_action import PostDetectStackResourceDriftRequestAction
    from .post_detect_stack_resource_drift_request_version import PostDetectStackResourceDriftRequestVersion
    from .post_detect_stack_set_drift_request_action import PostDetectStackSetDriftRequestAction
    from .post_detect_stack_set_drift_request_version import PostDetectStackSetDriftRequestVersion
    from .post_estimate_template_cost_request_action import PostEstimateTemplateCostRequestAction
    from .post_estimate_template_cost_request_version import PostEstimateTemplateCostRequestVersion
    from .post_execute_change_set_request_action import PostExecuteChangeSetRequestAction
    from .post_execute_change_set_request_version import PostExecuteChangeSetRequestVersion
    from .post_get_stack_policy_request_action import PostGetStackPolicyRequestAction
    from .post_get_stack_policy_request_version import PostGetStackPolicyRequestVersion
    from .post_get_template_request_action import PostGetTemplateRequestAction
    from .post_get_template_request_version import PostGetTemplateRequestVersion
    from .post_get_template_summary_request_action import PostGetTemplateSummaryRequestAction
    from .post_get_template_summary_request_version import PostGetTemplateSummaryRequestVersion
    from .post_import_stacks_to_stack_set_request_action import PostImportStacksToStackSetRequestAction
    from .post_import_stacks_to_stack_set_request_version import PostImportStacksToStackSetRequestVersion
    from .post_list_change_sets_request_action import PostListChangeSetsRequestAction
    from .post_list_change_sets_request_version import PostListChangeSetsRequestVersion
    from .post_list_exports_request_action import PostListExportsRequestAction
    from .post_list_exports_request_version import PostListExportsRequestVersion
    from .post_list_imports_request_action import PostListImportsRequestAction
    from .post_list_imports_request_version import PostListImportsRequestVersion
    from .post_list_stack_instances_request_action import PostListStackInstancesRequestAction
    from .post_list_stack_instances_request_version import PostListStackInstancesRequestVersion
    from .post_list_stack_resources_request_action import PostListStackResourcesRequestAction
    from .post_list_stack_resources_request_version import PostListStackResourcesRequestVersion
    from .post_list_stack_set_operation_results_request_action import PostListStackSetOperationResultsRequestAction
    from .post_list_stack_set_operation_results_request_version import PostListStackSetOperationResultsRequestVersion
    from .post_list_stack_set_operations_request_action import PostListStackSetOperationsRequestAction
    from .post_list_stack_set_operations_request_version import PostListStackSetOperationsRequestVersion
    from .post_list_stack_sets_request_action import PostListStackSetsRequestAction
    from .post_list_stack_sets_request_version import PostListStackSetsRequestVersion
    from .post_list_stacks_request_action import PostListStacksRequestAction
    from .post_list_stacks_request_version import PostListStacksRequestVersion
    from .post_list_type_registrations_request_action import PostListTypeRegistrationsRequestAction
    from .post_list_type_registrations_request_version import PostListTypeRegistrationsRequestVersion
    from .post_list_type_versions_request_action import PostListTypeVersionsRequestAction
    from .post_list_type_versions_request_version import PostListTypeVersionsRequestVersion
    from .post_list_types_request_action import PostListTypesRequestAction
    from .post_list_types_request_version import PostListTypesRequestVersion
    from .post_publish_type_request_action import PostPublishTypeRequestAction
    from .post_publish_type_request_version import PostPublishTypeRequestVersion
    from .post_record_handler_progress_request_action import PostRecordHandlerProgressRequestAction
    from .post_record_handler_progress_request_version import PostRecordHandlerProgressRequestVersion
    from .post_register_publisher_request_action import PostRegisterPublisherRequestAction
    from .post_register_publisher_request_version import PostRegisterPublisherRequestVersion
    from .post_register_type_request_action import PostRegisterTypeRequestAction
    from .post_register_type_request_version import PostRegisterTypeRequestVersion
    from .post_rollback_stack_request_action import PostRollbackStackRequestAction
    from .post_rollback_stack_request_version import PostRollbackStackRequestVersion
    from .post_set_stack_policy_request_action import PostSetStackPolicyRequestAction
    from .post_set_stack_policy_request_version import PostSetStackPolicyRequestVersion
    from .post_set_type_configuration_request_action import PostSetTypeConfigurationRequestAction
    from .post_set_type_configuration_request_version import PostSetTypeConfigurationRequestVersion
    from .post_set_type_default_version_request_action import PostSetTypeDefaultVersionRequestAction
    from .post_set_type_default_version_request_version import PostSetTypeDefaultVersionRequestVersion
    from .post_signal_resource_request_action import PostSignalResourceRequestAction
    from .post_signal_resource_request_version import PostSignalResourceRequestVersion
    from .post_stop_stack_set_operation_request_action import PostStopStackSetOperationRequestAction
    from .post_stop_stack_set_operation_request_version import PostStopStackSetOperationRequestVersion
    from .post_test_type_request_action import PostTestTypeRequestAction
    from .post_test_type_request_version import PostTestTypeRequestVersion
    from .post_update_stack_instances_request_action import PostUpdateStackInstancesRequestAction
    from .post_update_stack_instances_request_version import PostUpdateStackInstancesRequestVersion
    from .post_update_stack_request_action import PostUpdateStackRequestAction
    from .post_update_stack_request_version import PostUpdateStackRequestVersion
    from .post_update_stack_set_request_action import PostUpdateStackSetRequestAction
    from .post_update_stack_set_request_version import PostUpdateStackSetRequestVersion
    from .post_update_termination_protection_request_action import PostUpdateTerminationProtectionRequestAction
    from .post_update_termination_protection_request_version import PostUpdateTerminationProtectionRequestVersion
    from .post_validate_template_request_action import PostValidateTemplateRequestAction
    from .post_validate_template_request_version import PostValidateTemplateRequestVersion
    from .private_type_arn import PrivateTypeArn
    from .properties import Properties
    from .property_difference import PropertyDifference
    from .property_difference_difference_type import PropertyDifferenceDifferenceType
    from .property_differences import PropertyDifferences
    from .property_name import PropertyName
    from .property_path import PropertyPath
    from .property_value import PropertyValue
    from .provisioning_type import ProvisioningType
    from .public_version_number import PublicVersionNumber
    from .publish_type_input import PublishTypeInput
    from .publish_type_input_type import PublishTypeInputType
    from .publish_type_output import PublishTypeOutput
    from .publisher_id import PublisherId
    from .publisher_name import PublisherName
    from .publisher_profile import PublisherProfile
    from .publisher_status import PublisherStatus
    from .reason import Reason
    from .record_handler_progress_input import RecordHandlerProgressInput
    from .record_handler_progress_input_current_operation_status import RecordHandlerProgressInputCurrentOperationStatus
    from .record_handler_progress_input_error_code import RecordHandlerProgressInputErrorCode
    from .record_handler_progress_input_operation_status import RecordHandlerProgressInputOperationStatus
    from .record_handler_progress_output import RecordHandlerProgressOutput
    from .region import Region
    from .region_concurrency_type import RegionConcurrencyType
    from .region_list import RegionList
    from .register_publisher_input import RegisterPublisherInput
    from .register_publisher_output import RegisterPublisherOutput
    from .register_type_input import RegisterTypeInput
    from .register_type_input_logging_config import RegisterTypeInputLoggingConfig
    from .register_type_input_type import RegisterTypeInputType
    from .register_type_output import RegisterTypeOutput
    from .registration_status import RegistrationStatus
    from .registration_token import RegistrationToken
    from .registration_token_list import RegistrationTokenList
    from .registry_type import RegistryType
    from .replacement import Replacement
    from .request_token import RequestToken
    from .required_activated_type import RequiredActivatedType
    from .required_activated_types import RequiredActivatedTypes
    from .requires_recreation import RequiresRecreation
    from .resource_attribute import ResourceAttribute
    from .resource_change import ResourceChange
    from .resource_change_action import ResourceChangeAction
    from .resource_change_detail import ResourceChangeDetail
    from .resource_change_detail_change_source import ResourceChangeDetailChangeSource
    from .resource_change_detail_evaluation import ResourceChangeDetailEvaluation
    from .resource_change_detail_target import ResourceChangeDetailTarget
    from .resource_change_detail_target_attribute import ResourceChangeDetailTargetAttribute
    from .resource_change_detail_target_requires_recreation import ResourceChangeDetailTargetRequiresRecreation
    from .resource_change_details import ResourceChangeDetails
    from .resource_change_module_info import ResourceChangeModuleInfo
    from .resource_change_replacement import ResourceChangeReplacement
    from .resource_identifier_properties import ResourceIdentifierProperties
    from .resource_identifier_property_key import ResourceIdentifierPropertyKey
    from .resource_identifier_property_value import ResourceIdentifierPropertyValue
    from .resource_identifier_summaries import ResourceIdentifierSummaries
    from .resource_identifier_summary import ResourceIdentifierSummary
    from .resource_identifiers import ResourceIdentifiers
    from .resource_model import ResourceModel
    from .resource_properties import ResourceProperties
    from .resource_signal_status import ResourceSignalStatus
    from .resource_signal_unique_id import ResourceSignalUniqueId
    from .resource_status import ResourceStatus
    from .resource_status_reason import ResourceStatusReason
    from .resource_target_definition import ResourceTargetDefinition
    from .resource_target_definition_attribute import ResourceTargetDefinitionAttribute
    from .resource_target_definition_requires_recreation import ResourceTargetDefinitionRequiresRecreation
    from .resource_to_import import ResourceToImport
    from .resource_to_skip import ResourceToSkip
    from .resource_type import ResourceType
    from .resource_types import ResourceTypes
    from .retain_resources import RetainResources
    from .retain_stacks import RetainStacks
    from .retain_stacks_nullable import RetainStacksNullable
    from .retain_stacks_on_account_removal_nullable import RetainStacksOnAccountRemovalNullable
    from .role_arn import RoleArn
    from .rollback_configuration import RollbackConfiguration
    from .rollback_stack_input import RollbackStackInput
    from .rollback_stack_output import RollbackStackOutput
    from .rollback_trigger import RollbackTrigger
    from .rollback_triggers import RollbackTriggers
    from .s3bucket import S3Bucket
    from .s3url import S3Url
    from .scope import Scope
    from .set_stack_policy_input import SetStackPolicyInput
    from .set_type_configuration_input import SetTypeConfigurationInput
    from .set_type_configuration_input_type import SetTypeConfigurationInputType
    from .set_type_configuration_output import SetTypeConfigurationOutput
    from .set_type_default_version_input import SetTypeDefaultVersionInput
    from .set_type_default_version_input_type import SetTypeDefaultVersionInputType
    from .set_type_default_version_output import SetTypeDefaultVersionOutput
    from .signal_resource_input import SignalResourceInput
    from .signal_resource_input_status import SignalResourceInputStatus
    from .stack import Stack
    from .stack_drift_detection_id import StackDriftDetectionId
    from .stack_drift_detection_status import StackDriftDetectionStatus
    from .stack_drift_detection_status_reason import StackDriftDetectionStatusReason
    from .stack_drift_information import StackDriftInformation
    from .stack_drift_information_stack_drift_status import StackDriftInformationStackDriftStatus
    from .stack_drift_information_summary import StackDriftInformationSummary
    from .stack_drift_information_summary_stack_drift_status import StackDriftInformationSummaryStackDriftStatus
    from .stack_drift_status import StackDriftStatus
    from .stack_event import StackEvent
    from .stack_event_hook_failure_mode import StackEventHookFailureMode
    from .stack_event_hook_invocation_point import StackEventHookInvocationPoint
    from .stack_event_hook_status import StackEventHookStatus
    from .stack_event_resource_status import StackEventResourceStatus
    from .stack_events import StackEvents
    from .stack_id import StackId
    from .stack_id_list import StackIdList
    from .stack_ids_url import StackIdsUrl
    from .stack_instance import StackInstance
    from .stack_instance_comprehensive_status import StackInstanceComprehensiveStatus
    from .stack_instance_comprehensive_status_detailed_status import StackInstanceComprehensiveStatusDetailedStatus
    from .stack_instance_detailed_status import StackInstanceDetailedStatus
    from .stack_instance_drift_status import StackInstanceDriftStatus
    from .stack_instance_filter import StackInstanceFilter
    from .stack_instance_filter_name import StackInstanceFilterName
    from .stack_instance_filter_values import StackInstanceFilterValues
    from .stack_instance_filters import StackInstanceFilters
    from .stack_instance_not_found_exception import StackInstanceNotFoundException
    from .stack_instance_stack_instance_status import StackInstanceStackInstanceStatus
    from .stack_instance_stack_instance_status_detailed_status import StackInstanceStackInstanceStatusDetailedStatus
    from .stack_instance_status import StackInstanceStatus
    from .stack_instance_summaries import StackInstanceSummaries
    from .stack_instance_summary import StackInstanceSummary
    from .stack_instance_summary_drift_status import StackInstanceSummaryDriftStatus
    from .stack_instance_summary_stack_instance_status import StackInstanceSummaryStackInstanceStatus
    from .stack_instance_summary_stack_instance_status_detailed_status import (
        StackInstanceSummaryStackInstanceStatusDetailedStatus,
    )
    from .stack_instance_summary_status import StackInstanceSummaryStatus
    from .stack_name import StackName
    from .stack_name_or_id import StackNameOrId
    from .stack_not_found_exception import StackNotFoundException
    from .stack_policy_body import StackPolicyBody
    from .stack_policy_during_update_body import StackPolicyDuringUpdateBody
    from .stack_policy_during_update_url import StackPolicyDuringUpdateUrl
    from .stack_policy_url import StackPolicyUrl
    from .stack_resource import StackResource
    from .stack_resource_detail import StackResourceDetail
    from .stack_resource_detail_drift_information import StackResourceDetailDriftInformation
    from .stack_resource_detail_drift_information_stack_resource_drift_status import (
        StackResourceDetailDriftInformationStackResourceDriftStatus,
    )
    from .stack_resource_detail_module_info import StackResourceDetailModuleInfo
    from .stack_resource_detail_resource_status import StackResourceDetailResourceStatus
    from .stack_resource_drift import StackResourceDrift
    from .stack_resource_drift_information import StackResourceDriftInformation
    from .stack_resource_drift_information_stack_resource_drift_status import (
        StackResourceDriftInformationStackResourceDriftStatus,
    )
    from .stack_resource_drift_information_summary import StackResourceDriftInformationSummary
    from .stack_resource_drift_information_summary_stack_resource_drift_status import (
        StackResourceDriftInformationSummaryStackResourceDriftStatus,
    )
    from .stack_resource_drift_module_info import StackResourceDriftModuleInfo
    from .stack_resource_drift_stack_resource_drift_status import StackResourceDriftStackResourceDriftStatus
    from .stack_resource_drift_status import StackResourceDriftStatus
    from .stack_resource_drift_status_filters import StackResourceDriftStatusFilters
    from .stack_resource_drifts import StackResourceDrifts
    from .stack_resource_module_info import StackResourceModuleInfo
    from .stack_resource_resource_status import StackResourceResourceStatus
    from .stack_resource_summaries import StackResourceSummaries
    from .stack_resource_summary import StackResourceSummary
    from .stack_resource_summary_drift_information import StackResourceSummaryDriftInformation
    from .stack_resource_summary_drift_information_stack_resource_drift_status import (
        StackResourceSummaryDriftInformationStackResourceDriftStatus,
    )
    from .stack_resource_summary_module_info import StackResourceSummaryModuleInfo
    from .stack_resource_summary_resource_status import StackResourceSummaryResourceStatus
    from .stack_resources import StackResources
    from .stack_rollback_configuration import StackRollbackConfiguration
    from .stack_set import StackSet
    from .stack_set_arn import StackSetArn
    from .stack_set_auto_deployment import StackSetAutoDeployment
    from .stack_set_drift_detection_details import StackSetDriftDetectionDetails
    from .stack_set_drift_detection_details_drift_detection_status import (
        StackSetDriftDetectionDetailsDriftDetectionStatus,
    )
    from .stack_set_drift_detection_details_drift_status import StackSetDriftDetectionDetailsDriftStatus
    from .stack_set_drift_detection_status import StackSetDriftDetectionStatus
    from .stack_set_drift_status import StackSetDriftStatus
    from .stack_set_id import StackSetId
    from .stack_set_managed_execution import StackSetManagedExecution
    from .stack_set_name import StackSetName
    from .stack_set_name_or_id import StackSetNameOrId
    from .stack_set_not_empty_exception import StackSetNotEmptyException
    from .stack_set_not_found_exception import StackSetNotFoundException
    from .stack_set_operation import StackSetOperation
    from .stack_set_operation_action import StackSetOperationAction
    from .stack_set_operation_deployment_targets import StackSetOperationDeploymentTargets
    from .stack_set_operation_deployment_targets_account_filter_type import (
        StackSetOperationDeploymentTargetsAccountFilterType,
    )
    from .stack_set_operation_operation_preferences import StackSetOperationOperationPreferences
    from .stack_set_operation_operation_preferences_region_concurrency_type import (
        StackSetOperationOperationPreferencesRegionConcurrencyType,
    )
    from .stack_set_operation_preferences import StackSetOperationPreferences
    from .stack_set_operation_preferences_region_concurrency_type import (
        StackSetOperationPreferencesRegionConcurrencyType,
    )
    from .stack_set_operation_result_status import StackSetOperationResultStatus
    from .stack_set_operation_result_summaries import StackSetOperationResultSummaries
    from .stack_set_operation_result_summary import StackSetOperationResultSummary
    from .stack_set_operation_result_summary_account_gate_result import StackSetOperationResultSummaryAccountGateResult
    from .stack_set_operation_result_summary_account_gate_result_status import (
        StackSetOperationResultSummaryAccountGateResultStatus,
    )
    from .stack_set_operation_result_summary_status import StackSetOperationResultSummaryStatus
    from .stack_set_operation_stack_set_drift_detection_details import StackSetOperationStackSetDriftDetectionDetails
    from .stack_set_operation_stack_set_drift_detection_details_drift_detection_status import (
        StackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus,
    )
    from .stack_set_operation_stack_set_drift_detection_details_drift_status import (
        StackSetOperationStackSetDriftDetectionDetailsDriftStatus,
    )
    from .stack_set_operation_status import StackSetOperationStatus
    from .stack_set_operation_status_details import StackSetOperationStatusDetails
    from .stack_set_operation_status_reason import StackSetOperationStatusReason
    from .stack_set_operation_summaries import StackSetOperationSummaries
    from .stack_set_operation_summary import StackSetOperationSummary
    from .stack_set_operation_summary_action import StackSetOperationSummaryAction
    from .stack_set_operation_summary_status import StackSetOperationSummaryStatus
    from .stack_set_operation_summary_status_details import StackSetOperationSummaryStatusDetails
    from .stack_set_permission_model import StackSetPermissionModel
    from .stack_set_stack_set_drift_detection_details import StackSetStackSetDriftDetectionDetails
    from .stack_set_stack_set_drift_detection_details_drift_detection_status import (
        StackSetStackSetDriftDetectionDetailsDriftDetectionStatus,
    )
    from .stack_set_stack_set_drift_detection_details_drift_status import (
        StackSetStackSetDriftDetectionDetailsDriftStatus,
    )
    from .stack_set_status import StackSetStatus
    from .stack_set_summaries import StackSetSummaries
    from .stack_set_summary import StackSetSummary
    from .stack_set_summary_auto_deployment import StackSetSummaryAutoDeployment
    from .stack_set_summary_drift_status import StackSetSummaryDriftStatus
    from .stack_set_summary_managed_execution import StackSetSummaryManagedExecution
    from .stack_set_summary_permission_model import StackSetSummaryPermissionModel
    from .stack_set_summary_status import StackSetSummaryStatus
    from .stack_stack_status import StackStackStatus
    from .stack_status import StackStatus
    from .stack_status_filter import StackStatusFilter
    from .stack_status_reason import StackStatusReason
    from .stack_summaries import StackSummaries
    from .stack_summary import StackSummary
    from .stack_summary_drift_information import StackSummaryDriftInformation
    from .stack_summary_drift_information_stack_drift_status import StackSummaryDriftInformationStackDriftStatus
    from .stack_summary_stack_status import StackSummaryStackStatus
    from .stacks import Stacks
    from .stage_list import StageList
    from .stale_request_exception import StaleRequestException
    from .status_message import StatusMessage
    from .stop_stack_set_operation_input import StopStackSetOperationInput
    from .stop_stack_set_operation_input_call_as import StopStackSetOperationInputCallAs
    from .stop_stack_set_operation_output import StopStackSetOperationOutput
    from .supported_major_version import SupportedMajorVersion
    from .supported_major_versions import SupportedMajorVersions
    from .tag import Tag
    from .tag_key import TagKey
    from .tag_value import TagValue
    from .tags import Tags
    from .template_body import TemplateBody
    from .template_description import TemplateDescription
    from .template_parameter import TemplateParameter
    from .template_parameters import TemplateParameters
    from .template_stage import TemplateStage
    from .template_url import TemplateUrl
    from .test_type_input import TestTypeInput
    from .test_type_input_type import TestTypeInputType
    from .test_type_output import TestTypeOutput
    from .third_party_type import ThirdPartyType
    from .third_party_type_arn import ThirdPartyTypeArn
    from .timeout_minutes import TimeoutMinutes
    from .timestamp import Timestamp
    from .token_already_exists_exception import TokenAlreadyExistsException
    from .total_stack_instances_count import TotalStackInstancesCount
    from .transform_name import TransformName
    from .transforms_list import TransformsList
    from .type import Type
    from .type_arn import TypeArn
    from .type_configuration import TypeConfiguration
    from .type_configuration_alias import TypeConfigurationAlias
    from .type_configuration_arn import TypeConfigurationArn
    from .type_configuration_details import TypeConfigurationDetails
    from .type_configuration_details_list import TypeConfigurationDetailsList
    from .type_configuration_identifier import TypeConfigurationIdentifier
    from .type_configuration_identifier_type import TypeConfigurationIdentifierType
    from .type_configuration_identifiers import TypeConfigurationIdentifiers
    from .type_configuration_not_found_exception import TypeConfigurationNotFoundException
    from .type_filters import TypeFilters
    from .type_filters_category import TypeFiltersCategory
    from .type_hierarchy import TypeHierarchy
    from .type_name import TypeName
    from .type_name_prefix import TypeNamePrefix
    from .type_not_found_exception import TypeNotFoundException
    from .type_schema import TypeSchema
    from .type_summaries import TypeSummaries
    from .type_summary import TypeSummary
    from .type_summary_publisher_identity import TypeSummaryPublisherIdentity
    from .type_summary_type import TypeSummaryType
    from .type_tests_status import TypeTestsStatus
    from .type_tests_status_description import TypeTestsStatusDescription
    from .type_version_id import TypeVersionId
    from .type_version_summaries import TypeVersionSummaries
    from .type_version_summary import TypeVersionSummary
    from .type_version_summary_type import TypeVersionSummaryType
    from .unprocessed_type_configurations import UnprocessedTypeConfigurations
    from .update_stack_input import UpdateStackInput
    from .update_stack_input_rollback_configuration import UpdateStackInputRollbackConfiguration
    from .update_stack_instances_input import UpdateStackInstancesInput
    from .update_stack_instances_input_call_as import UpdateStackInstancesInputCallAs
    from .update_stack_instances_input_deployment_targets import UpdateStackInstancesInputDeploymentTargets
    from .update_stack_instances_input_deployment_targets_account_filter_type import (
        UpdateStackInstancesInputDeploymentTargetsAccountFilterType,
    )
    from .update_stack_instances_input_operation_preferences import UpdateStackInstancesInputOperationPreferences
    from .update_stack_instances_input_operation_preferences_region_concurrency_type import (
        UpdateStackInstancesInputOperationPreferencesRegionConcurrencyType,
    )
    from .update_stack_instances_output import UpdateStackInstancesOutput
    from .update_stack_output import UpdateStackOutput
    from .update_stack_set_input import UpdateStackSetInput
    from .update_stack_set_input_auto_deployment import UpdateStackSetInputAutoDeployment
    from .update_stack_set_input_call_as import UpdateStackSetInputCallAs
    from .update_stack_set_input_deployment_targets import UpdateStackSetInputDeploymentTargets
    from .update_stack_set_input_deployment_targets_account_filter_type import (
        UpdateStackSetInputDeploymentTargetsAccountFilterType,
    )
    from .update_stack_set_input_managed_execution import UpdateStackSetInputManagedExecution
    from .update_stack_set_input_operation_preferences import UpdateStackSetInputOperationPreferences
    from .update_stack_set_input_operation_preferences_region_concurrency_type import (
        UpdateStackSetInputOperationPreferencesRegionConcurrencyType,
    )
    from .update_stack_set_input_permission_model import UpdateStackSetInputPermissionModel
    from .update_stack_set_output import UpdateStackSetOutput
    from .update_termination_protection_input import UpdateTerminationProtectionInput
    from .update_termination_protection_output import UpdateTerminationProtectionOutput
    from .url import Url
    from .use_previous_template import UsePreviousTemplate
    from .use_previous_value import UsePreviousValue
    from .validate_template_input import ValidateTemplateInput
    from .validate_template_output import ValidateTemplateOutput
    from .value import Value
    from .version import Version
    from .version_bump import VersionBump
    from .visibility import Visibility
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptTermsAndConditions": ".accept_terms_and_conditions",
    "Account": ".account",
    "AccountFilterType": ".account_filter_type",
    "AccountGateResult": ".account_gate_result",
    "AccountGateResultStatus": ".account_gate_result_status",
    "AccountGateStatus": ".account_gate_status",
    "AccountGateStatusReason": ".account_gate_status_reason",
    "AccountLimit": ".account_limit",
    "AccountLimitList": ".account_limit_list",
    "AccountList": ".account_list",
    "AccountsUrl": ".accounts_url",
    "ActivateTypeInput": ".activate_type_input",
    "ActivateTypeInputType": ".activate_type_input_type",
    "ActivateTypeInputVersionBump": ".activate_type_input_version_bump",
    "ActivateTypeOutput": ".activate_type_output",
    "AllowedValue": ".allowed_value",
    "AllowedValues": ".allowed_values",
    "AlreadyExistsException": ".already_exists_exception",
    "Arn": ".arn",
    "AutoDeployment": ".auto_deployment",
    "AutoDeploymentNullable": ".auto_deployment_nullable",
    "AutoUpdate": ".auto_update",
    "BatchDescribeTypeConfigurationsError": ".batch_describe_type_configurations_error",
    "BatchDescribeTypeConfigurationsErrors": ".batch_describe_type_configurations_errors",
    "BatchDescribeTypeConfigurationsInput": ".batch_describe_type_configurations_input",
    "BatchDescribeTypeConfigurationsOutput": ".batch_describe_type_configurations_output",
    "BoxedInteger": ".boxed_integer",
    "BoxedMaxResults": ".boxed_max_results",
    "CallAs": ".call_as",
    "CancelUpdateStackInput": ".cancel_update_stack_input",
    "Capabilities": ".capabilities",
    "CapabilitiesReason": ".capabilities_reason",
    "Capability": ".capability",
    "Category": ".category",
    "CausingEntity": ".causing_entity",
    "CfnRegistryException": ".cfn_registry_exception",
    "Change": ".change",
    "ChangeAction": ".change_action",
    "ChangeResourceChange": ".change_resource_change",
    "ChangeResourceChangeAction": ".change_resource_change_action",
    "ChangeResourceChangeModuleInfo": ".change_resource_change_module_info",
    "ChangeResourceChangeReplacement": ".change_resource_change_replacement",
    "ChangeSetHook": ".change_set_hook",
    "ChangeSetHookFailureMode": ".change_set_hook_failure_mode",
    "ChangeSetHookInvocationPoint": ".change_set_hook_invocation_point",
    "ChangeSetHookResourceTargetDetails": ".change_set_hook_resource_target_details",
    "ChangeSetHookResourceTargetDetailsResourceAction": ".change_set_hook_resource_target_details_resource_action",
    "ChangeSetHookTargetDetails": ".change_set_hook_target_details",
    "ChangeSetHookTargetDetailsResourceTargetDetails": ".change_set_hook_target_details_resource_target_details",
    "ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction": ".change_set_hook_target_details_resource_target_details_resource_action",
    "ChangeSetHookTargetDetailsTargetType": ".change_set_hook_target_details_target_type",
    "ChangeSetHooks": ".change_set_hooks",
    "ChangeSetHooksStatus": ".change_set_hooks_status",
    "ChangeSetId": ".change_set_id",
    "ChangeSetName": ".change_set_name",
    "ChangeSetNameOrId": ".change_set_name_or_id",
    "ChangeSetNotFoundException": ".change_set_not_found_exception",
    "ChangeSetStatus": ".change_set_status",
    "ChangeSetStatusReason": ".change_set_status_reason",
    "ChangeSetSummaries": ".change_set_summaries",
    "ChangeSetSummary": ".change_set_summary",
    "ChangeSetSummaryExecutionStatus": ".change_set_summary_execution_status",
    "ChangeSetSummaryStatus": ".change_set_summary_status",
    "ChangeSetType": ".change_set_type",
    "ChangeSource": ".change_source",
    "ChangeType": ".change_type",
    "Changes": ".changes",
    "ClientRequestToken": ".client_request_token",
    "ClientToken": ".client_token",
    "ConfigurationSchema": ".configuration_schema",
    "ConnectionArn": ".connection_arn",
    "ContinueUpdateRollbackInput": ".continue_update_rollback_input",
    "ContinueUpdateRollbackOutput": ".continue_update_rollback_output",
    "CreateChangeSetInput": ".create_change_set_input",
    "CreateChangeSetInputChangeSetType": ".create_change_set_input_change_set_type",
    "CreateChangeSetInputRollbackConfiguration": ".create_change_set_input_rollback_configuration",
    "CreateChangeSetOutput": ".create_change_set_output",
    "CreateStackInput": ".create_stack_input",
    "CreateStackInputOnFailure": ".create_stack_input_on_failure",
    "CreateStackInputRollbackConfiguration": ".create_stack_input_rollback_configuration",
    "CreateStackInstancesInput": ".create_stack_instances_input",
    "CreateStackInstancesInputCallAs": ".create_stack_instances_input_call_as",
    "CreateStackInstancesInputDeploymentTargets": ".create_stack_instances_input_deployment_targets",
    "CreateStackInstancesInputDeploymentTargetsAccountFilterType": ".create_stack_instances_input_deployment_targets_account_filter_type",
    "CreateStackInstancesInputOperationPreferences": ".create_stack_instances_input_operation_preferences",
    "CreateStackInstancesInputOperationPreferencesRegionConcurrencyType": ".create_stack_instances_input_operation_preferences_region_concurrency_type",
    "CreateStackInstancesOutput": ".create_stack_instances_output",
    "CreateStackOutput": ".create_stack_output",
    "CreateStackSetInput": ".create_stack_set_input",
    "CreateStackSetInputAutoDeployment": ".create_stack_set_input_auto_deployment",
    "CreateStackSetInputCallAs": ".create_stack_set_input_call_as",
    "CreateStackSetInputManagedExecution": ".create_stack_set_input_managed_execution",
    "CreateStackSetInputPermissionModel": ".create_stack_set_input_permission_model",
    "CreateStackSetOutput": ".create_stack_set_output",
    "CreatedButModifiedException": ".created_but_modified_exception",
    "CreationTime": ".creation_time",
    "DeactivateTypeInput": ".deactivate_type_input",
    "DeactivateTypeInputType": ".deactivate_type_input_type",
    "DeactivateTypeOutput": ".deactivate_type_output",
    "DeleteChangeSetInput": ".delete_change_set_input",
    "DeleteChangeSetOutput": ".delete_change_set_output",
    "DeleteStackInput": ".delete_stack_input",
    "DeleteStackInstancesInput": ".delete_stack_instances_input",
    "DeleteStackInstancesInputCallAs": ".delete_stack_instances_input_call_as",
    "DeleteStackInstancesInputDeploymentTargets": ".delete_stack_instances_input_deployment_targets",
    "DeleteStackInstancesInputDeploymentTargetsAccountFilterType": ".delete_stack_instances_input_deployment_targets_account_filter_type",
    "DeleteStackInstancesInputOperationPreferences": ".delete_stack_instances_input_operation_preferences",
    "DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType": ".delete_stack_instances_input_operation_preferences_region_concurrency_type",
    "DeleteStackInstancesOutput": ".delete_stack_instances_output",
    "DeleteStackSetInput": ".delete_stack_set_input",
    "DeleteStackSetInputCallAs": ".delete_stack_set_input_call_as",
    "DeleteStackSetOutput": ".delete_stack_set_output",
    "DeletionTime": ".deletion_time",
    "DeploymentTargets": ".deployment_targets",
    "DeploymentTargetsAccountFilterType": ".deployment_targets_account_filter_type",
    "DeprecatedStatus": ".deprecated_status",
    "DeregisterTypeInput": ".deregister_type_input",
    "DeregisterTypeInputType": ".deregister_type_input_type",
    "DeregisterTypeOutput": ".deregister_type_output",
    "DescribeAccountLimitsInput": ".describe_account_limits_input",
    "DescribeAccountLimitsOutput": ".describe_account_limits_output",
    "DescribeChangeSetHooksInput": ".describe_change_set_hooks_input",
    "DescribeChangeSetHooksOutput": ".describe_change_set_hooks_output",
    "DescribeChangeSetHooksOutputStatus": ".describe_change_set_hooks_output_status",
    "DescribeChangeSetInput": ".describe_change_set_input",
    "DescribeChangeSetOutput": ".describe_change_set_output",
    "DescribeChangeSetOutputExecutionStatus": ".describe_change_set_output_execution_status",
    "DescribeChangeSetOutputRollbackConfiguration": ".describe_change_set_output_rollback_configuration",
    "DescribeChangeSetOutputStatus": ".describe_change_set_output_status",
    "DescribePublisherInput": ".describe_publisher_input",
    "DescribePublisherOutput": ".describe_publisher_output",
    "DescribePublisherOutputIdentityProvider": ".describe_publisher_output_identity_provider",
    "DescribePublisherOutputPublisherStatus": ".describe_publisher_output_publisher_status",
    "DescribeStackDriftDetectionStatusInput": ".describe_stack_drift_detection_status_input",
    "DescribeStackDriftDetectionStatusOutput": ".describe_stack_drift_detection_status_output",
    "DescribeStackDriftDetectionStatusOutputDetectionStatus": ".describe_stack_drift_detection_status_output_detection_status",
    "DescribeStackDriftDetectionStatusOutputStackDriftStatus": ".describe_stack_drift_detection_status_output_stack_drift_status",
    "DescribeStackEventsInput": ".describe_stack_events_input",
    "DescribeStackEventsOutput": ".describe_stack_events_output",
    "DescribeStackInstanceInput": ".describe_stack_instance_input",
    "DescribeStackInstanceInputCallAs": ".describe_stack_instance_input_call_as",
    "DescribeStackInstanceOutput": ".describe_stack_instance_output",
    "DescribeStackInstanceOutputStackInstance": ".describe_stack_instance_output_stack_instance",
    "DescribeStackInstanceOutputStackInstanceDriftStatus": ".describe_stack_instance_output_stack_instance_drift_status",
    "DescribeStackInstanceOutputStackInstanceStackInstanceStatus": ".describe_stack_instance_output_stack_instance_stack_instance_status",
    "DescribeStackInstanceOutputStackInstanceStackInstanceStatusDetailedStatus": ".describe_stack_instance_output_stack_instance_stack_instance_status_detailed_status",
    "DescribeStackInstanceOutputStackInstanceStatus": ".describe_stack_instance_output_stack_instance_status",
    "DescribeStackResourceDriftsInput": ".describe_stack_resource_drifts_input",
    "DescribeStackResourceDriftsOutput": ".describe_stack_resource_drifts_output",
    "DescribeStackResourceInput": ".describe_stack_resource_input",
    "DescribeStackResourceOutput": ".describe_stack_resource_output",
    "DescribeStackResourceOutputStackResourceDetail": ".describe_stack_resource_output_stack_resource_detail",
    "DescribeStackResourceOutputStackResourceDetailDriftInformation": ".describe_stack_resource_output_stack_resource_detail_drift_information",
    "DescribeStackResourceOutputStackResourceDetailDriftInformationStackResourceDriftStatus": ".describe_stack_resource_output_stack_resource_detail_drift_information_stack_resource_drift_status",
    "DescribeStackResourceOutputStackResourceDetailModuleInfo": ".describe_stack_resource_output_stack_resource_detail_module_info",
    "DescribeStackResourceOutputStackResourceDetailResourceStatus": ".describe_stack_resource_output_stack_resource_detail_resource_status",
    "DescribeStackResourcesInput": ".describe_stack_resources_input",
    "DescribeStackResourcesOutput": ".describe_stack_resources_output",
    "DescribeStackSetInput": ".describe_stack_set_input",
    "DescribeStackSetInputCallAs": ".describe_stack_set_input_call_as",
    "DescribeStackSetOperationInput": ".describe_stack_set_operation_input",
    "DescribeStackSetOperationInputCallAs": ".describe_stack_set_operation_input_call_as",
    "DescribeStackSetOperationOutput": ".describe_stack_set_operation_output",
    "DescribeStackSetOperationOutputStackSetOperation": ".describe_stack_set_operation_output_stack_set_operation",
    "DescribeStackSetOperationOutputStackSetOperationAction": ".describe_stack_set_operation_output_stack_set_operation_action",
    "DescribeStackSetOperationOutputStackSetOperationDeploymentTargets": ".describe_stack_set_operation_output_stack_set_operation_deployment_targets",
    "DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType": ".describe_stack_set_operation_output_stack_set_operation_deployment_targets_account_filter_type",
    "DescribeStackSetOperationOutputStackSetOperationOperationPreferences": ".describe_stack_set_operation_output_stack_set_operation_operation_preferences",
    "DescribeStackSetOperationOutputStackSetOperationOperationPreferencesRegionConcurrencyType": ".describe_stack_set_operation_output_stack_set_operation_operation_preferences_region_concurrency_type",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetails": ".describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus": ".describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_detection_status",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus": ".describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_status",
    "DescribeStackSetOperationOutputStackSetOperationStatus": ".describe_stack_set_operation_output_stack_set_operation_status",
    "DescribeStackSetOperationOutputStackSetOperationStatusDetails": ".describe_stack_set_operation_output_stack_set_operation_status_details",
    "DescribeStackSetOutput": ".describe_stack_set_output",
    "DescribeStackSetOutputStackSet": ".describe_stack_set_output_stack_set",
    "DescribeStackSetOutputStackSetAutoDeployment": ".describe_stack_set_output_stack_set_auto_deployment",
    "DescribeStackSetOutputStackSetManagedExecution": ".describe_stack_set_output_stack_set_managed_execution",
    "DescribeStackSetOutputStackSetPermissionModel": ".describe_stack_set_output_stack_set_permission_model",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetails": ".describe_stack_set_output_stack_set_stack_set_drift_detection_details",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftDetectionStatus": ".describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_detection_status",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftStatus": ".describe_stack_set_output_stack_set_stack_set_drift_detection_details_drift_status",
    "DescribeStackSetOutputStackSetStatus": ".describe_stack_set_output_stack_set_status",
    "DescribeStacksInput": ".describe_stacks_input",
    "DescribeStacksOutput": ".describe_stacks_output",
    "DescribeTypeInput": ".describe_type_input",
    "DescribeTypeInputType": ".describe_type_input_type",
    "DescribeTypeOutput": ".describe_type_output",
    "DescribeTypeOutputDeprecatedStatus": ".describe_type_output_deprecated_status",
    "DescribeTypeOutputLoggingConfig": ".describe_type_output_logging_config",
    "DescribeTypeOutputProvisioningType": ".describe_type_output_provisioning_type",
    "DescribeTypeOutputType": ".describe_type_output_type",
    "DescribeTypeOutputTypeTestsStatus": ".describe_type_output_type_tests_status",
    "DescribeTypeOutputVisibility": ".describe_type_output_visibility",
    "DescribeTypeRegistrationInput": ".describe_type_registration_input",
    "DescribeTypeRegistrationOutput": ".describe_type_registration_output",
    "DescribeTypeRegistrationOutputProgressStatus": ".describe_type_registration_output_progress_status",
    "Description": ".description",
    "DetectStackDriftInput": ".detect_stack_drift_input",
    "DetectStackDriftOutput": ".detect_stack_drift_output",
    "DetectStackResourceDriftInput": ".detect_stack_resource_drift_input",
    "DetectStackResourceDriftOutput": ".detect_stack_resource_drift_output",
    "DetectStackResourceDriftOutputStackResourceDrift": ".detect_stack_resource_drift_output_stack_resource_drift",
    "DetectStackResourceDriftOutputStackResourceDriftModuleInfo": ".detect_stack_resource_drift_output_stack_resource_drift_module_info",
    "DetectStackResourceDriftOutputStackResourceDriftStackResourceDriftStatus": ".detect_stack_resource_drift_output_stack_resource_drift_stack_resource_drift_status",
    "DetectStackSetDriftInput": ".detect_stack_set_drift_input",
    "DetectStackSetDriftInputCallAs": ".detect_stack_set_drift_input_call_as",
    "DetectStackSetDriftOutput": ".detect_stack_set_drift_output",
    "DifferenceType": ".difference_type",
    "DisableRollback": ".disable_rollback",
    "DriftedStackInstancesCount": ".drifted_stack_instances_count",
    "EnableTerminationProtection": ".enable_termination_protection",
    "ErrorCode": ".error_code",
    "ErrorMessage": ".error_message",
    "EstimateTemplateCostInput": ".estimate_template_cost_input",
    "EstimateTemplateCostOutput": ".estimate_template_cost_output",
    "EvaluationType": ".evaluation_type",
    "EventId": ".event_id",
    "ExecuteChangeSetInput": ".execute_change_set_input",
    "ExecuteChangeSetOutput": ".execute_change_set_output",
    "ExecutionRoleName": ".execution_role_name",
    "ExecutionStatus": ".execution_status",
    "Export": ".export",
    "ExportName": ".export_name",
    "ExportValue": ".export_value",
    "Exports": ".exports",
    "FailedStackInstancesCount": ".failed_stack_instances_count",
    "FailureToleranceCount": ".failure_tolerance_count",
    "FailureTolerancePercentage": ".failure_tolerance_percentage",
    "GetActivateTypeRequestAction": ".get_activate_type_request_action",
    "GetActivateTypeRequestLoggingConfig": ".get_activate_type_request_logging_config",
    "GetActivateTypeRequestType": ".get_activate_type_request_type",
    "GetActivateTypeRequestVersion": ".get_activate_type_request_version",
    "GetActivateTypeRequestVersionBump": ".get_activate_type_request_version_bump",
    "GetBatchDescribeTypeConfigurationsRequestAction": ".get_batch_describe_type_configurations_request_action",
    "GetBatchDescribeTypeConfigurationsRequestVersion": ".get_batch_describe_type_configurations_request_version",
    "GetCancelUpdateStackRequestAction": ".get_cancel_update_stack_request_action",
    "GetCancelUpdateStackRequestVersion": ".get_cancel_update_stack_request_version",
    "GetContinueUpdateRollbackRequestAction": ".get_continue_update_rollback_request_action",
    "GetContinueUpdateRollbackRequestVersion": ".get_continue_update_rollback_request_version",
    "GetCreateChangeSetRequestAction": ".get_create_change_set_request_action",
    "GetCreateChangeSetRequestChangeSetType": ".get_create_change_set_request_change_set_type",
    "GetCreateChangeSetRequestRollbackConfiguration": ".get_create_change_set_request_rollback_configuration",
    "GetCreateChangeSetRequestVersion": ".get_create_change_set_request_version",
    "GetCreateStackInstancesRequestAction": ".get_create_stack_instances_request_action",
    "GetCreateStackInstancesRequestCallAs": ".get_create_stack_instances_request_call_as",
    "GetCreateStackInstancesRequestDeploymentTargets": ".get_create_stack_instances_request_deployment_targets",
    "GetCreateStackInstancesRequestDeploymentTargetsAccountFilterType": ".get_create_stack_instances_request_deployment_targets_account_filter_type",
    "GetCreateStackInstancesRequestOperationPreferences": ".get_create_stack_instances_request_operation_preferences",
    "GetCreateStackInstancesRequestOperationPreferencesRegionConcurrencyType": ".get_create_stack_instances_request_operation_preferences_region_concurrency_type",
    "GetCreateStackInstancesRequestVersion": ".get_create_stack_instances_request_version",
    "GetCreateStackRequestAction": ".get_create_stack_request_action",
    "GetCreateStackRequestOnFailure": ".get_create_stack_request_on_failure",
    "GetCreateStackRequestRollbackConfiguration": ".get_create_stack_request_rollback_configuration",
    "GetCreateStackRequestVersion": ".get_create_stack_request_version",
    "GetCreateStackSetRequestAction": ".get_create_stack_set_request_action",
    "GetCreateStackSetRequestAutoDeployment": ".get_create_stack_set_request_auto_deployment",
    "GetCreateStackSetRequestCallAs": ".get_create_stack_set_request_call_as",
    "GetCreateStackSetRequestManagedExecution": ".get_create_stack_set_request_managed_execution",
    "GetCreateStackSetRequestPermissionModel": ".get_create_stack_set_request_permission_model",
    "GetCreateStackSetRequestVersion": ".get_create_stack_set_request_version",
    "GetDeactivateTypeRequestAction": ".get_deactivate_type_request_action",
    "GetDeactivateTypeRequestType": ".get_deactivate_type_request_type",
    "GetDeactivateTypeRequestVersion": ".get_deactivate_type_request_version",
    "GetDeleteChangeSetRequestAction": ".get_delete_change_set_request_action",
    "GetDeleteChangeSetRequestVersion": ".get_delete_change_set_request_version",
    "GetDeleteStackInstancesRequestAction": ".get_delete_stack_instances_request_action",
    "GetDeleteStackInstancesRequestCallAs": ".get_delete_stack_instances_request_call_as",
    "GetDeleteStackInstancesRequestDeploymentTargets": ".get_delete_stack_instances_request_deployment_targets",
    "GetDeleteStackInstancesRequestDeploymentTargetsAccountFilterType": ".get_delete_stack_instances_request_deployment_targets_account_filter_type",
    "GetDeleteStackInstancesRequestOperationPreferences": ".get_delete_stack_instances_request_operation_preferences",
    "GetDeleteStackInstancesRequestOperationPreferencesRegionConcurrencyType": ".get_delete_stack_instances_request_operation_preferences_region_concurrency_type",
    "GetDeleteStackInstancesRequestVersion": ".get_delete_stack_instances_request_version",
    "GetDeleteStackRequestAction": ".get_delete_stack_request_action",
    "GetDeleteStackRequestVersion": ".get_delete_stack_request_version",
    "GetDeleteStackSetRequestAction": ".get_delete_stack_set_request_action",
    "GetDeleteStackSetRequestCallAs": ".get_delete_stack_set_request_call_as",
    "GetDeleteStackSetRequestVersion": ".get_delete_stack_set_request_version",
    "GetDeregisterTypeRequestAction": ".get_deregister_type_request_action",
    "GetDeregisterTypeRequestType": ".get_deregister_type_request_type",
    "GetDeregisterTypeRequestVersion": ".get_deregister_type_request_version",
    "GetDescribeAccountLimitsRequestAction": ".get_describe_account_limits_request_action",
    "GetDescribeAccountLimitsRequestVersion": ".get_describe_account_limits_request_version",
    "GetDescribeChangeSetHooksRequestAction": ".get_describe_change_set_hooks_request_action",
    "GetDescribeChangeSetHooksRequestVersion": ".get_describe_change_set_hooks_request_version",
    "GetDescribeChangeSetRequestAction": ".get_describe_change_set_request_action",
    "GetDescribeChangeSetRequestVersion": ".get_describe_change_set_request_version",
    "GetDescribePublisherRequestAction": ".get_describe_publisher_request_action",
    "GetDescribePublisherRequestVersion": ".get_describe_publisher_request_version",
    "GetDescribeStackDriftDetectionStatusRequestAction": ".get_describe_stack_drift_detection_status_request_action",
    "GetDescribeStackDriftDetectionStatusRequestVersion": ".get_describe_stack_drift_detection_status_request_version",
    "GetDescribeStackEventsRequestAction": ".get_describe_stack_events_request_action",
    "GetDescribeStackEventsRequestVersion": ".get_describe_stack_events_request_version",
    "GetDescribeStackInstanceRequestAction": ".get_describe_stack_instance_request_action",
    "GetDescribeStackInstanceRequestCallAs": ".get_describe_stack_instance_request_call_as",
    "GetDescribeStackInstanceRequestVersion": ".get_describe_stack_instance_request_version",
    "GetDescribeStackResourceDriftsRequestAction": ".get_describe_stack_resource_drifts_request_action",
    "GetDescribeStackResourceDriftsRequestVersion": ".get_describe_stack_resource_drifts_request_version",
    "GetDescribeStackResourceRequestAction": ".get_describe_stack_resource_request_action",
    "GetDescribeStackResourceRequestVersion": ".get_describe_stack_resource_request_version",
    "GetDescribeStackResourcesRequestAction": ".get_describe_stack_resources_request_action",
    "GetDescribeStackResourcesRequestVersion": ".get_describe_stack_resources_request_version",
    "GetDescribeStackSetOperationRequestAction": ".get_describe_stack_set_operation_request_action",
    "GetDescribeStackSetOperationRequestCallAs": ".get_describe_stack_set_operation_request_call_as",
    "GetDescribeStackSetOperationRequestVersion": ".get_describe_stack_set_operation_request_version",
    "GetDescribeStackSetRequestAction": ".get_describe_stack_set_request_action",
    "GetDescribeStackSetRequestCallAs": ".get_describe_stack_set_request_call_as",
    "GetDescribeStackSetRequestVersion": ".get_describe_stack_set_request_version",
    "GetDescribeStacksRequestAction": ".get_describe_stacks_request_action",
    "GetDescribeStacksRequestVersion": ".get_describe_stacks_request_version",
    "GetDescribeTypeRegistrationRequestAction": ".get_describe_type_registration_request_action",
    "GetDescribeTypeRegistrationRequestVersion": ".get_describe_type_registration_request_version",
    "GetDescribeTypeRequestAction": ".get_describe_type_request_action",
    "GetDescribeTypeRequestType": ".get_describe_type_request_type",
    "GetDescribeTypeRequestVersion": ".get_describe_type_request_version",
    "GetDetectStackDriftRequestAction": ".get_detect_stack_drift_request_action",
    "GetDetectStackDriftRequestVersion": ".get_detect_stack_drift_request_version",
    "GetDetectStackResourceDriftRequestAction": ".get_detect_stack_resource_drift_request_action",
    "GetDetectStackResourceDriftRequestVersion": ".get_detect_stack_resource_drift_request_version",
    "GetDetectStackSetDriftRequestAction": ".get_detect_stack_set_drift_request_action",
    "GetDetectStackSetDriftRequestCallAs": ".get_detect_stack_set_drift_request_call_as",
    "GetDetectStackSetDriftRequestOperationPreferences": ".get_detect_stack_set_drift_request_operation_preferences",
    "GetDetectStackSetDriftRequestOperationPreferencesRegionConcurrencyType": ".get_detect_stack_set_drift_request_operation_preferences_region_concurrency_type",
    "GetDetectStackSetDriftRequestVersion": ".get_detect_stack_set_drift_request_version",
    "GetEstimateTemplateCostRequestAction": ".get_estimate_template_cost_request_action",
    "GetEstimateTemplateCostRequestVersion": ".get_estimate_template_cost_request_version",
    "GetExecuteChangeSetRequestAction": ".get_execute_change_set_request_action",
    "GetExecuteChangeSetRequestVersion": ".get_execute_change_set_request_version",
    "GetGetStackPolicyRequestAction": ".get_get_stack_policy_request_action",
    "GetGetStackPolicyRequestVersion": ".get_get_stack_policy_request_version",
    "GetGetTemplateRequestAction": ".get_get_template_request_action",
    "GetGetTemplateRequestTemplateStage": ".get_get_template_request_template_stage",
    "GetGetTemplateRequestVersion": ".get_get_template_request_version",
    "GetGetTemplateSummaryRequestAction": ".get_get_template_summary_request_action",
    "GetGetTemplateSummaryRequestCallAs": ".get_get_template_summary_request_call_as",
    "GetGetTemplateSummaryRequestVersion": ".get_get_template_summary_request_version",
    "GetImportStacksToStackSetRequestAction": ".get_import_stacks_to_stack_set_request_action",
    "GetImportStacksToStackSetRequestCallAs": ".get_import_stacks_to_stack_set_request_call_as",
    "GetImportStacksToStackSetRequestOperationPreferences": ".get_import_stacks_to_stack_set_request_operation_preferences",
    "GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType": ".get_import_stacks_to_stack_set_request_operation_preferences_region_concurrency_type",
    "GetImportStacksToStackSetRequestVersion": ".get_import_stacks_to_stack_set_request_version",
    "GetListChangeSetsRequestAction": ".get_list_change_sets_request_action",
    "GetListChangeSetsRequestVersion": ".get_list_change_sets_request_version",
    "GetListExportsRequestAction": ".get_list_exports_request_action",
    "GetListExportsRequestVersion": ".get_list_exports_request_version",
    "GetListImportsRequestAction": ".get_list_imports_request_action",
    "GetListImportsRequestVersion": ".get_list_imports_request_version",
    "GetListStackInstancesRequestAction": ".get_list_stack_instances_request_action",
    "GetListStackInstancesRequestCallAs": ".get_list_stack_instances_request_call_as",
    "GetListStackInstancesRequestVersion": ".get_list_stack_instances_request_version",
    "GetListStackResourcesRequestAction": ".get_list_stack_resources_request_action",
    "GetListStackResourcesRequestVersion": ".get_list_stack_resources_request_version",
    "GetListStackSetOperationResultsRequestAction": ".get_list_stack_set_operation_results_request_action",
    "GetListStackSetOperationResultsRequestCallAs": ".get_list_stack_set_operation_results_request_call_as",
    "GetListStackSetOperationResultsRequestVersion": ".get_list_stack_set_operation_results_request_version",
    "GetListStackSetOperationsRequestAction": ".get_list_stack_set_operations_request_action",
    "GetListStackSetOperationsRequestCallAs": ".get_list_stack_set_operations_request_call_as",
    "GetListStackSetOperationsRequestVersion": ".get_list_stack_set_operations_request_version",
    "GetListStackSetsRequestAction": ".get_list_stack_sets_request_action",
    "GetListStackSetsRequestCallAs": ".get_list_stack_sets_request_call_as",
    "GetListStackSetsRequestStatus": ".get_list_stack_sets_request_status",
    "GetListStackSetsRequestVersion": ".get_list_stack_sets_request_version",
    "GetListStacksRequestAction": ".get_list_stacks_request_action",
    "GetListStacksRequestVersion": ".get_list_stacks_request_version",
    "GetListTypeRegistrationsRequestAction": ".get_list_type_registrations_request_action",
    "GetListTypeRegistrationsRequestRegistrationStatusFilter": ".get_list_type_registrations_request_registration_status_filter",
    "GetListTypeRegistrationsRequestType": ".get_list_type_registrations_request_type",
    "GetListTypeRegistrationsRequestVersion": ".get_list_type_registrations_request_version",
    "GetListTypeVersionsRequestAction": ".get_list_type_versions_request_action",
    "GetListTypeVersionsRequestDeprecatedStatus": ".get_list_type_versions_request_deprecated_status",
    "GetListTypeVersionsRequestType": ".get_list_type_versions_request_type",
    "GetListTypeVersionsRequestVersion": ".get_list_type_versions_request_version",
    "GetListTypesRequestAction": ".get_list_types_request_action",
    "GetListTypesRequestDeprecatedStatus": ".get_list_types_request_deprecated_status",
    "GetListTypesRequestFilters": ".get_list_types_request_filters",
    "GetListTypesRequestFiltersCategory": ".get_list_types_request_filters_category",
    "GetListTypesRequestProvisioningType": ".get_list_types_request_provisioning_type",
    "GetListTypesRequestType": ".get_list_types_request_type",
    "GetListTypesRequestVersion": ".get_list_types_request_version",
    "GetListTypesRequestVisibility": ".get_list_types_request_visibility",
    "GetPublishTypeRequestAction": ".get_publish_type_request_action",
    "GetPublishTypeRequestType": ".get_publish_type_request_type",
    "GetPublishTypeRequestVersion": ".get_publish_type_request_version",
    "GetRecordHandlerProgressRequestAction": ".get_record_handler_progress_request_action",
    "GetRecordHandlerProgressRequestCurrentOperationStatus": ".get_record_handler_progress_request_current_operation_status",
    "GetRecordHandlerProgressRequestErrorCode": ".get_record_handler_progress_request_error_code",
    "GetRecordHandlerProgressRequestOperationStatus": ".get_record_handler_progress_request_operation_status",
    "GetRecordHandlerProgressRequestVersion": ".get_record_handler_progress_request_version",
    "GetRegisterPublisherRequestAction": ".get_register_publisher_request_action",
    "GetRegisterPublisherRequestVersion": ".get_register_publisher_request_version",
    "GetRegisterTypeRequestAction": ".get_register_type_request_action",
    "GetRegisterTypeRequestLoggingConfig": ".get_register_type_request_logging_config",
    "GetRegisterTypeRequestType": ".get_register_type_request_type",
    "GetRegisterTypeRequestVersion": ".get_register_type_request_version",
    "GetRollbackStackRequestAction": ".get_rollback_stack_request_action",
    "GetRollbackStackRequestVersion": ".get_rollback_stack_request_version",
    "GetSetStackPolicyRequestAction": ".get_set_stack_policy_request_action",
    "GetSetStackPolicyRequestVersion": ".get_set_stack_policy_request_version",
    "GetSetTypeConfigurationRequestAction": ".get_set_type_configuration_request_action",
    "GetSetTypeConfigurationRequestType": ".get_set_type_configuration_request_type",
    "GetSetTypeConfigurationRequestVersion": ".get_set_type_configuration_request_version",
    "GetSetTypeDefaultVersionRequestAction": ".get_set_type_default_version_request_action",
    "GetSetTypeDefaultVersionRequestType": ".get_set_type_default_version_request_type",
    "GetSetTypeDefaultVersionRequestVersion": ".get_set_type_default_version_request_version",
    "GetSignalResourceRequestAction": ".get_signal_resource_request_action",
    "GetSignalResourceRequestStatus": ".get_signal_resource_request_status",
    "GetSignalResourceRequestVersion": ".get_signal_resource_request_version",
    "GetStackPolicyInput": ".get_stack_policy_input",
    "GetStackPolicyOutput": ".get_stack_policy_output",
    "GetStopStackSetOperationRequestAction": ".get_stop_stack_set_operation_request_action",
    "GetStopStackSetOperationRequestCallAs": ".get_stop_stack_set_operation_request_call_as",
    "GetStopStackSetOperationRequestVersion": ".get_stop_stack_set_operation_request_version",
    "GetTemplateInput": ".get_template_input",
    "GetTemplateInputTemplateStage": ".get_template_input_template_stage",
    "GetTemplateOutput": ".get_template_output",
    "GetTemplateSummaryInput": ".get_template_summary_input",
    "GetTemplateSummaryInputCallAs": ".get_template_summary_input_call_as",
    "GetTemplateSummaryOutput": ".get_template_summary_output",
    "GetTestTypeRequestAction": ".get_test_type_request_action",
    "GetTestTypeRequestType": ".get_test_type_request_type",
    "GetTestTypeRequestVersion": ".get_test_type_request_version",
    "GetUpdateStackInstancesRequestAction": ".get_update_stack_instances_request_action",
    "GetUpdateStackInstancesRequestCallAs": ".get_update_stack_instances_request_call_as",
    "GetUpdateStackInstancesRequestDeploymentTargets": ".get_update_stack_instances_request_deployment_targets",
    "GetUpdateStackInstancesRequestDeploymentTargetsAccountFilterType": ".get_update_stack_instances_request_deployment_targets_account_filter_type",
    "GetUpdateStackInstancesRequestOperationPreferences": ".get_update_stack_instances_request_operation_preferences",
    "GetUpdateStackInstancesRequestOperationPreferencesRegionConcurrencyType": ".get_update_stack_instances_request_operation_preferences_region_concurrency_type",
    "GetUpdateStackInstancesRequestVersion": ".get_update_stack_instances_request_version",
    "GetUpdateStackRequestAction": ".get_update_stack_request_action",
    "GetUpdateStackRequestRollbackConfiguration": ".get_update_stack_request_rollback_configuration",
    "GetUpdateStackRequestVersion": ".get_update_stack_request_version",
    "GetUpdateStackSetRequestAction": ".get_update_stack_set_request_action",
    "GetUpdateStackSetRequestAutoDeployment": ".get_update_stack_set_request_auto_deployment",
    "GetUpdateStackSetRequestCallAs": ".get_update_stack_set_request_call_as",
    "GetUpdateStackSetRequestDeploymentTargets": ".get_update_stack_set_request_deployment_targets",
    "GetUpdateStackSetRequestDeploymentTargetsAccountFilterType": ".get_update_stack_set_request_deployment_targets_account_filter_type",
    "GetUpdateStackSetRequestManagedExecution": ".get_update_stack_set_request_managed_execution",
    "GetUpdateStackSetRequestOperationPreferences": ".get_update_stack_set_request_operation_preferences",
    "GetUpdateStackSetRequestOperationPreferencesRegionConcurrencyType": ".get_update_stack_set_request_operation_preferences_region_concurrency_type",
    "GetUpdateStackSetRequestPermissionModel": ".get_update_stack_set_request_permission_model",
    "GetUpdateStackSetRequestVersion": ".get_update_stack_set_request_version",
    "GetUpdateTerminationProtectionRequestAction": ".get_update_termination_protection_request_action",
    "GetUpdateTerminationProtectionRequestVersion": ".get_update_termination_protection_request_version",
    "GetValidateTemplateRequestAction": ".get_validate_template_request_action",
    "GetValidateTemplateRequestVersion": ".get_validate_template_request_version",
    "HandlerErrorCode": ".handler_error_code",
    "HookFailureMode": ".hook_failure_mode",
    "HookInvocationCount": ".hook_invocation_count",
    "HookInvocationPoint": ".hook_invocation_point",
    "HookStatus": ".hook_status",
    "HookStatusReason": ".hook_status_reason",
    "HookTargetType": ".hook_target_type",
    "HookTargetTypeName": ".hook_target_type_name",
    "HookType": ".hook_type",
    "HookTypeConfigurationVersionId": ".hook_type_configuration_version_id",
    "HookTypeName": ".hook_type_name",
    "HookTypeVersionId": ".hook_type_version_id",
    "IdentityProvider": ".identity_provider",
    "ImportStacksToStackSetInput": ".import_stacks_to_stack_set_input",
    "ImportStacksToStackSetInputCallAs": ".import_stacks_to_stack_set_input_call_as",
    "ImportStacksToStackSetOutput": ".import_stacks_to_stack_set_output",
    "Imports": ".imports",
    "InProgressStackInstancesCount": ".in_progress_stack_instances_count",
    "InSyncStackInstancesCount": ".in_sync_stack_instances_count",
    "IncludeNestedStacks": ".include_nested_stacks",
    "InsufficientCapabilitiesException": ".insufficient_capabilities_exception",
    "InvalidChangeSetStatusException": ".invalid_change_set_status_exception",
    "InvalidOperationException": ".invalid_operation_exception",
    "InvalidStateTransitionException": ".invalid_state_transition_exception",
    "IsActivated": ".is_activated",
    "IsDefaultConfiguration": ".is_default_configuration",
    "IsDefaultVersion": ".is_default_version",
    "Key": ".key",
    "LastUpdatedTime": ".last_updated_time",
    "LimitExceededException": ".limit_exceeded_exception",
    "LimitName": ".limit_name",
    "LimitValue": ".limit_value",
    "ListChangeSetsInput": ".list_change_sets_input",
    "ListChangeSetsOutput": ".list_change_sets_output",
    "ListExportsInput": ".list_exports_input",
    "ListExportsOutput": ".list_exports_output",
    "ListImportsInput": ".list_imports_input",
    "ListImportsOutput": ".list_imports_output",
    "ListStackInstancesInput": ".list_stack_instances_input",
    "ListStackInstancesInputCallAs": ".list_stack_instances_input_call_as",
    "ListStackInstancesOutput": ".list_stack_instances_output",
    "ListStackResourcesInput": ".list_stack_resources_input",
    "ListStackResourcesOutput": ".list_stack_resources_output",
    "ListStackSetOperationResultsInput": ".list_stack_set_operation_results_input",
    "ListStackSetOperationResultsInputCallAs": ".list_stack_set_operation_results_input_call_as",
    "ListStackSetOperationResultsOutput": ".list_stack_set_operation_results_output",
    "ListStackSetOperationsInput": ".list_stack_set_operations_input",
    "ListStackSetOperationsInputCallAs": ".list_stack_set_operations_input_call_as",
    "ListStackSetOperationsOutput": ".list_stack_set_operations_output",
    "ListStackSetsInput": ".list_stack_sets_input",
    "ListStackSetsInputCallAs": ".list_stack_sets_input_call_as",
    "ListStackSetsInputStatus": ".list_stack_sets_input_status",
    "ListStackSetsOutput": ".list_stack_sets_output",
    "ListStacksInput": ".list_stacks_input",
    "ListStacksOutput": ".list_stacks_output",
    "ListTypeRegistrationsInput": ".list_type_registrations_input",
    "ListTypeRegistrationsInputRegistrationStatusFilter": ".list_type_registrations_input_registration_status_filter",
    "ListTypeRegistrationsInputType": ".list_type_registrations_input_type",
    "ListTypeRegistrationsOutput": ".list_type_registrations_output",
    "ListTypeVersionsInput": ".list_type_versions_input",
    "ListTypeVersionsInputDeprecatedStatus": ".list_type_versions_input_deprecated_status",
    "ListTypeVersionsInputType": ".list_type_versions_input_type",
    "ListTypeVersionsOutput": ".list_type_versions_output",
    "ListTypesInput": ".list_types_input",
    "ListTypesInputDeprecatedStatus": ".list_types_input_deprecated_status",
    "ListTypesInputFilters": ".list_types_input_filters",
    "ListTypesInputFiltersCategory": ".list_types_input_filters_category",
    "ListTypesInputProvisioningType": ".list_types_input_provisioning_type",
    "ListTypesInputType": ".list_types_input_type",
    "ListTypesInputVisibility": ".list_types_input_visibility",
    "ListTypesOutput": ".list_types_output",
    "LogGroupName": ".log_group_name",
    "LoggingConfig": ".logging_config",
    "LogicalIdHierarchy": ".logical_id_hierarchy",
    "LogicalResourceId": ".logical_resource_id",
    "LogicalResourceIds": ".logical_resource_ids",
    "MajorVersion": ".major_version",
    "ManagedExecution": ".managed_execution",
    "ManagedExecutionNullable": ".managed_execution_nullable",
    "MaxConcurrentCount": ".max_concurrent_count",
    "MaxConcurrentPercentage": ".max_concurrent_percentage",
    "MaxResults": ".max_results",
    "Metadata": ".metadata",
    "ModuleInfo": ".module_info",
    "MonitoringTimeInMinutes": ".monitoring_time_in_minutes",
    "NameAlreadyExistsException": ".name_already_exists_exception",
    "NextToken": ".next_token",
    "NoEcho": ".no_echo",
    "NotificationArNs": ".notification_ar_ns",
    "NotificationArn": ".notification_arn",
    "OnFailure": ".on_failure",
    "OperationIdAlreadyExistsException": ".operation_id_already_exists_exception",
    "OperationInProgressException": ".operation_in_progress_exception",
    "OperationNotFoundException": ".operation_not_found_exception",
    "OperationResultFilter": ".operation_result_filter",
    "OperationResultFilterName": ".operation_result_filter_name",
    "OperationResultFilterValues": ".operation_result_filter_values",
    "OperationResultFilters": ".operation_result_filters",
    "OperationStatus": ".operation_status",
    "OperationStatusCheckFailedException": ".operation_status_check_failed_exception",
    "OptionalSecureUrl": ".optional_secure_url",
    "OrganizationalUnitId": ".organizational_unit_id",
    "OrganizationalUnitIdList": ".organizational_unit_id_list",
    "Output": ".output",
    "OutputKey": ".output_key",
    "OutputValue": ".output_value",
    "Outputs": ".outputs",
    "Parameter": ".parameter",
    "ParameterConstraints": ".parameter_constraints",
    "ParameterDeclaration": ".parameter_declaration",
    "ParameterDeclarationParameterConstraints": ".parameter_declaration_parameter_constraints",
    "ParameterDeclarations": ".parameter_declarations",
    "ParameterKey": ".parameter_key",
    "ParameterType": ".parameter_type",
    "ParameterValue": ".parameter_value",
    "Parameters": ".parameters",
    "PermissionModels": ".permission_models",
    "PhysicalResourceId": ".physical_resource_id",
    "PhysicalResourceIdContext": ".physical_resource_id_context",
    "PhysicalResourceIdContextKeyValuePair": ".physical_resource_id_context_key_value_pair",
    "PostActivateTypeRequestAction": ".post_activate_type_request_action",
    "PostActivateTypeRequestVersion": ".post_activate_type_request_version",
    "PostBatchDescribeTypeConfigurationsRequestAction": ".post_batch_describe_type_configurations_request_action",
    "PostBatchDescribeTypeConfigurationsRequestVersion": ".post_batch_describe_type_configurations_request_version",
    "PostCancelUpdateStackRequestAction": ".post_cancel_update_stack_request_action",
    "PostCancelUpdateStackRequestVersion": ".post_cancel_update_stack_request_version",
    "PostContinueUpdateRollbackRequestAction": ".post_continue_update_rollback_request_action",
    "PostContinueUpdateRollbackRequestVersion": ".post_continue_update_rollback_request_version",
    "PostCreateChangeSetRequestAction": ".post_create_change_set_request_action",
    "PostCreateChangeSetRequestVersion": ".post_create_change_set_request_version",
    "PostCreateStackInstancesRequestAction": ".post_create_stack_instances_request_action",
    "PostCreateStackInstancesRequestVersion": ".post_create_stack_instances_request_version",
    "PostCreateStackRequestAction": ".post_create_stack_request_action",
    "PostCreateStackRequestVersion": ".post_create_stack_request_version",
    "PostCreateStackSetRequestAction": ".post_create_stack_set_request_action",
    "PostCreateStackSetRequestVersion": ".post_create_stack_set_request_version",
    "PostDeactivateTypeRequestAction": ".post_deactivate_type_request_action",
    "PostDeactivateTypeRequestVersion": ".post_deactivate_type_request_version",
    "PostDeleteChangeSetRequestAction": ".post_delete_change_set_request_action",
    "PostDeleteChangeSetRequestVersion": ".post_delete_change_set_request_version",
    "PostDeleteStackInstancesRequestAction": ".post_delete_stack_instances_request_action",
    "PostDeleteStackInstancesRequestVersion": ".post_delete_stack_instances_request_version",
    "PostDeleteStackRequestAction": ".post_delete_stack_request_action",
    "PostDeleteStackRequestVersion": ".post_delete_stack_request_version",
    "PostDeleteStackSetRequestAction": ".post_delete_stack_set_request_action",
    "PostDeleteStackSetRequestVersion": ".post_delete_stack_set_request_version",
    "PostDeregisterTypeRequestAction": ".post_deregister_type_request_action",
    "PostDeregisterTypeRequestVersion": ".post_deregister_type_request_version",
    "PostDescribeAccountLimitsRequestAction": ".post_describe_account_limits_request_action",
    "PostDescribeAccountLimitsRequestVersion": ".post_describe_account_limits_request_version",
    "PostDescribeChangeSetHooksRequestAction": ".post_describe_change_set_hooks_request_action",
    "PostDescribeChangeSetHooksRequestVersion": ".post_describe_change_set_hooks_request_version",
    "PostDescribeChangeSetRequestAction": ".post_describe_change_set_request_action",
    "PostDescribeChangeSetRequestVersion": ".post_describe_change_set_request_version",
    "PostDescribePublisherRequestAction": ".post_describe_publisher_request_action",
    "PostDescribePublisherRequestVersion": ".post_describe_publisher_request_version",
    "PostDescribeStackDriftDetectionStatusRequestAction": ".post_describe_stack_drift_detection_status_request_action",
    "PostDescribeStackDriftDetectionStatusRequestVersion": ".post_describe_stack_drift_detection_status_request_version",
    "PostDescribeStackEventsRequestAction": ".post_describe_stack_events_request_action",
    "PostDescribeStackEventsRequestVersion": ".post_describe_stack_events_request_version",
    "PostDescribeStackInstanceRequestAction": ".post_describe_stack_instance_request_action",
    "PostDescribeStackInstanceRequestVersion": ".post_describe_stack_instance_request_version",
    "PostDescribeStackResourceDriftsRequestAction": ".post_describe_stack_resource_drifts_request_action",
    "PostDescribeStackResourceDriftsRequestVersion": ".post_describe_stack_resource_drifts_request_version",
    "PostDescribeStackResourceRequestAction": ".post_describe_stack_resource_request_action",
    "PostDescribeStackResourceRequestVersion": ".post_describe_stack_resource_request_version",
    "PostDescribeStackResourcesRequestAction": ".post_describe_stack_resources_request_action",
    "PostDescribeStackResourcesRequestVersion": ".post_describe_stack_resources_request_version",
    "PostDescribeStackSetOperationRequestAction": ".post_describe_stack_set_operation_request_action",
    "PostDescribeStackSetOperationRequestVersion": ".post_describe_stack_set_operation_request_version",
    "PostDescribeStackSetRequestAction": ".post_describe_stack_set_request_action",
    "PostDescribeStackSetRequestVersion": ".post_describe_stack_set_request_version",
    "PostDescribeStacksRequestAction": ".post_describe_stacks_request_action",
    "PostDescribeStacksRequestVersion": ".post_describe_stacks_request_version",
    "PostDescribeTypeRegistrationRequestAction": ".post_describe_type_registration_request_action",
    "PostDescribeTypeRegistrationRequestVersion": ".post_describe_type_registration_request_version",
    "PostDescribeTypeRequestAction": ".post_describe_type_request_action",
    "PostDescribeTypeRequestVersion": ".post_describe_type_request_version",
    "PostDetectStackDriftRequestAction": ".post_detect_stack_drift_request_action",
    "PostDetectStackDriftRequestVersion": ".post_detect_stack_drift_request_version",
    "PostDetectStackResourceDriftRequestAction": ".post_detect_stack_resource_drift_request_action",
    "PostDetectStackResourceDriftRequestVersion": ".post_detect_stack_resource_drift_request_version",
    "PostDetectStackSetDriftRequestAction": ".post_detect_stack_set_drift_request_action",
    "PostDetectStackSetDriftRequestVersion": ".post_detect_stack_set_drift_request_version",
    "PostEstimateTemplateCostRequestAction": ".post_estimate_template_cost_request_action",
    "PostEstimateTemplateCostRequestVersion": ".post_estimate_template_cost_request_version",
    "PostExecuteChangeSetRequestAction": ".post_execute_change_set_request_action",
    "PostExecuteChangeSetRequestVersion": ".post_execute_change_set_request_version",
    "PostGetStackPolicyRequestAction": ".post_get_stack_policy_request_action",
    "PostGetStackPolicyRequestVersion": ".post_get_stack_policy_request_version",
    "PostGetTemplateRequestAction": ".post_get_template_request_action",
    "PostGetTemplateRequestVersion": ".post_get_template_request_version",
    "PostGetTemplateSummaryRequestAction": ".post_get_template_summary_request_action",
    "PostGetTemplateSummaryRequestVersion": ".post_get_template_summary_request_version",
    "PostImportStacksToStackSetRequestAction": ".post_import_stacks_to_stack_set_request_action",
    "PostImportStacksToStackSetRequestVersion": ".post_import_stacks_to_stack_set_request_version",
    "PostListChangeSetsRequestAction": ".post_list_change_sets_request_action",
    "PostListChangeSetsRequestVersion": ".post_list_change_sets_request_version",
    "PostListExportsRequestAction": ".post_list_exports_request_action",
    "PostListExportsRequestVersion": ".post_list_exports_request_version",
    "PostListImportsRequestAction": ".post_list_imports_request_action",
    "PostListImportsRequestVersion": ".post_list_imports_request_version",
    "PostListStackInstancesRequestAction": ".post_list_stack_instances_request_action",
    "PostListStackInstancesRequestVersion": ".post_list_stack_instances_request_version",
    "PostListStackResourcesRequestAction": ".post_list_stack_resources_request_action",
    "PostListStackResourcesRequestVersion": ".post_list_stack_resources_request_version",
    "PostListStackSetOperationResultsRequestAction": ".post_list_stack_set_operation_results_request_action",
    "PostListStackSetOperationResultsRequestVersion": ".post_list_stack_set_operation_results_request_version",
    "PostListStackSetOperationsRequestAction": ".post_list_stack_set_operations_request_action",
    "PostListStackSetOperationsRequestVersion": ".post_list_stack_set_operations_request_version",
    "PostListStackSetsRequestAction": ".post_list_stack_sets_request_action",
    "PostListStackSetsRequestVersion": ".post_list_stack_sets_request_version",
    "PostListStacksRequestAction": ".post_list_stacks_request_action",
    "PostListStacksRequestVersion": ".post_list_stacks_request_version",
    "PostListTypeRegistrationsRequestAction": ".post_list_type_registrations_request_action",
    "PostListTypeRegistrationsRequestVersion": ".post_list_type_registrations_request_version",
    "PostListTypeVersionsRequestAction": ".post_list_type_versions_request_action",
    "PostListTypeVersionsRequestVersion": ".post_list_type_versions_request_version",
    "PostListTypesRequestAction": ".post_list_types_request_action",
    "PostListTypesRequestVersion": ".post_list_types_request_version",
    "PostPublishTypeRequestAction": ".post_publish_type_request_action",
    "PostPublishTypeRequestVersion": ".post_publish_type_request_version",
    "PostRecordHandlerProgressRequestAction": ".post_record_handler_progress_request_action",
    "PostRecordHandlerProgressRequestVersion": ".post_record_handler_progress_request_version",
    "PostRegisterPublisherRequestAction": ".post_register_publisher_request_action",
    "PostRegisterPublisherRequestVersion": ".post_register_publisher_request_version",
    "PostRegisterTypeRequestAction": ".post_register_type_request_action",
    "PostRegisterTypeRequestVersion": ".post_register_type_request_version",
    "PostRollbackStackRequestAction": ".post_rollback_stack_request_action",
    "PostRollbackStackRequestVersion": ".post_rollback_stack_request_version",
    "PostSetStackPolicyRequestAction": ".post_set_stack_policy_request_action",
    "PostSetStackPolicyRequestVersion": ".post_set_stack_policy_request_version",
    "PostSetTypeConfigurationRequestAction": ".post_set_type_configuration_request_action",
    "PostSetTypeConfigurationRequestVersion": ".post_set_type_configuration_request_version",
    "PostSetTypeDefaultVersionRequestAction": ".post_set_type_default_version_request_action",
    "PostSetTypeDefaultVersionRequestVersion": ".post_set_type_default_version_request_version",
    "PostSignalResourceRequestAction": ".post_signal_resource_request_action",
    "PostSignalResourceRequestVersion": ".post_signal_resource_request_version",
    "PostStopStackSetOperationRequestAction": ".post_stop_stack_set_operation_request_action",
    "PostStopStackSetOperationRequestVersion": ".post_stop_stack_set_operation_request_version",
    "PostTestTypeRequestAction": ".post_test_type_request_action",
    "PostTestTypeRequestVersion": ".post_test_type_request_version",
    "PostUpdateStackInstancesRequestAction": ".post_update_stack_instances_request_action",
    "PostUpdateStackInstancesRequestVersion": ".post_update_stack_instances_request_version",
    "PostUpdateStackRequestAction": ".post_update_stack_request_action",
    "PostUpdateStackRequestVersion": ".post_update_stack_request_version",
    "PostUpdateStackSetRequestAction": ".post_update_stack_set_request_action",
    "PostUpdateStackSetRequestVersion": ".post_update_stack_set_request_version",
    "PostUpdateTerminationProtectionRequestAction": ".post_update_termination_protection_request_action",
    "PostUpdateTerminationProtectionRequestVersion": ".post_update_termination_protection_request_version",
    "PostValidateTemplateRequestAction": ".post_validate_template_request_action",
    "PostValidateTemplateRequestVersion": ".post_validate_template_request_version",
    "PrivateTypeArn": ".private_type_arn",
    "Properties": ".properties",
    "PropertyDifference": ".property_difference",
    "PropertyDifferenceDifferenceType": ".property_difference_difference_type",
    "PropertyDifferences": ".property_differences",
    "PropertyName": ".property_name",
    "PropertyPath": ".property_path",
    "PropertyValue": ".property_value",
    "ProvisioningType": ".provisioning_type",
    "PublicVersionNumber": ".public_version_number",
    "PublishTypeInput": ".publish_type_input",
    "PublishTypeInputType": ".publish_type_input_type",
    "PublishTypeOutput": ".publish_type_output",
    "PublisherId": ".publisher_id",
    "PublisherName": ".publisher_name",
    "PublisherProfile": ".publisher_profile",
    "PublisherStatus": ".publisher_status",
    "Reason": ".reason",
    "RecordHandlerProgressInput": ".record_handler_progress_input",
    "RecordHandlerProgressInputCurrentOperationStatus": ".record_handler_progress_input_current_operation_status",
    "RecordHandlerProgressInputErrorCode": ".record_handler_progress_input_error_code",
    "RecordHandlerProgressInputOperationStatus": ".record_handler_progress_input_operation_status",
    "RecordHandlerProgressOutput": ".record_handler_progress_output",
    "Region": ".region",
    "RegionConcurrencyType": ".region_concurrency_type",
    "RegionList": ".region_list",
    "RegisterPublisherInput": ".register_publisher_input",
    "RegisterPublisherOutput": ".register_publisher_output",
    "RegisterTypeInput": ".register_type_input",
    "RegisterTypeInputLoggingConfig": ".register_type_input_logging_config",
    "RegisterTypeInputType": ".register_type_input_type",
    "RegisterTypeOutput": ".register_type_output",
    "RegistrationStatus": ".registration_status",
    "RegistrationToken": ".registration_token",
    "RegistrationTokenList": ".registration_token_list",
    "RegistryType": ".registry_type",
    "Replacement": ".replacement",
    "RequestToken": ".request_token",
    "RequiredActivatedType": ".required_activated_type",
    "RequiredActivatedTypes": ".required_activated_types",
    "RequiresRecreation": ".requires_recreation",
    "ResourceAttribute": ".resource_attribute",
    "ResourceChange": ".resource_change",
    "ResourceChangeAction": ".resource_change_action",
    "ResourceChangeDetail": ".resource_change_detail",
    "ResourceChangeDetailChangeSource": ".resource_change_detail_change_source",
    "ResourceChangeDetailEvaluation": ".resource_change_detail_evaluation",
    "ResourceChangeDetailTarget": ".resource_change_detail_target",
    "ResourceChangeDetailTargetAttribute": ".resource_change_detail_target_attribute",
    "ResourceChangeDetailTargetRequiresRecreation": ".resource_change_detail_target_requires_recreation",
    "ResourceChangeDetails": ".resource_change_details",
    "ResourceChangeModuleInfo": ".resource_change_module_info",
    "ResourceChangeReplacement": ".resource_change_replacement",
    "ResourceIdentifierProperties": ".resource_identifier_properties",
    "ResourceIdentifierPropertyKey": ".resource_identifier_property_key",
    "ResourceIdentifierPropertyValue": ".resource_identifier_property_value",
    "ResourceIdentifierSummaries": ".resource_identifier_summaries",
    "ResourceIdentifierSummary": ".resource_identifier_summary",
    "ResourceIdentifiers": ".resource_identifiers",
    "ResourceModel": ".resource_model",
    "ResourceProperties": ".resource_properties",
    "ResourceSignalStatus": ".resource_signal_status",
    "ResourceSignalUniqueId": ".resource_signal_unique_id",
    "ResourceStatus": ".resource_status",
    "ResourceStatusReason": ".resource_status_reason",
    "ResourceTargetDefinition": ".resource_target_definition",
    "ResourceTargetDefinitionAttribute": ".resource_target_definition_attribute",
    "ResourceTargetDefinitionRequiresRecreation": ".resource_target_definition_requires_recreation",
    "ResourceToImport": ".resource_to_import",
    "ResourceToSkip": ".resource_to_skip",
    "ResourceType": ".resource_type",
    "ResourceTypes": ".resource_types",
    "ResourcesToImport": ".resources_to_import",
    "ResourcesToSkip": ".resources_to_skip",
    "RetainResources": ".retain_resources",
    "RetainStacks": ".retain_stacks",
    "RetainStacksNullable": ".retain_stacks_nullable",
    "RetainStacksOnAccountRemovalNullable": ".retain_stacks_on_account_removal_nullable",
    "RoleArn": ".role_arn",
    "RollbackConfiguration": ".rollback_configuration",
    "RollbackStackInput": ".rollback_stack_input",
    "RollbackStackOutput": ".rollback_stack_output",
    "RollbackTrigger": ".rollback_trigger",
    "RollbackTriggers": ".rollback_triggers",
    "S3Bucket": ".s3bucket",
    "S3Url": ".s3url",
    "Scope": ".scope",
    "SetStackPolicyInput": ".set_stack_policy_input",
    "SetTypeConfigurationInput": ".set_type_configuration_input",
    "SetTypeConfigurationInputType": ".set_type_configuration_input_type",
    "SetTypeConfigurationOutput": ".set_type_configuration_output",
    "SetTypeDefaultVersionInput": ".set_type_default_version_input",
    "SetTypeDefaultVersionInputType": ".set_type_default_version_input_type",
    "SetTypeDefaultVersionOutput": ".set_type_default_version_output",
    "SignalResourceInput": ".signal_resource_input",
    "SignalResourceInputStatus": ".signal_resource_input_status",
    "Stack": ".stack",
    "StackDriftDetectionId": ".stack_drift_detection_id",
    "StackDriftDetectionStatus": ".stack_drift_detection_status",
    "StackDriftDetectionStatusReason": ".stack_drift_detection_status_reason",
    "StackDriftInformation": ".stack_drift_information",
    "StackDriftInformationStackDriftStatus": ".stack_drift_information_stack_drift_status",
    "StackDriftInformationSummary": ".stack_drift_information_summary",
    "StackDriftInformationSummaryStackDriftStatus": ".stack_drift_information_summary_stack_drift_status",
    "StackDriftStatus": ".stack_drift_status",
    "StackEvent": ".stack_event",
    "StackEventHookFailureMode": ".stack_event_hook_failure_mode",
    "StackEventHookInvocationPoint": ".stack_event_hook_invocation_point",
    "StackEventHookStatus": ".stack_event_hook_status",
    "StackEventResourceStatus": ".stack_event_resource_status",
    "StackEvents": ".stack_events",
    "StackId": ".stack_id",
    "StackIdList": ".stack_id_list",
    "StackIdsUrl": ".stack_ids_url",
    "StackInstance": ".stack_instance",
    "StackInstanceComprehensiveStatus": ".stack_instance_comprehensive_status",
    "StackInstanceComprehensiveStatusDetailedStatus": ".stack_instance_comprehensive_status_detailed_status",
    "StackInstanceDetailedStatus": ".stack_instance_detailed_status",
    "StackInstanceDriftStatus": ".stack_instance_drift_status",
    "StackInstanceFilter": ".stack_instance_filter",
    "StackInstanceFilterName": ".stack_instance_filter_name",
    "StackInstanceFilterValues": ".stack_instance_filter_values",
    "StackInstanceFilters": ".stack_instance_filters",
    "StackInstanceNotFoundException": ".stack_instance_not_found_exception",
    "StackInstanceStackInstanceStatus": ".stack_instance_stack_instance_status",
    "StackInstanceStackInstanceStatusDetailedStatus": ".stack_instance_stack_instance_status_detailed_status",
    "StackInstanceStatus": ".stack_instance_status",
    "StackInstanceSummaries": ".stack_instance_summaries",
    "StackInstanceSummary": ".stack_instance_summary",
    "StackInstanceSummaryDriftStatus": ".stack_instance_summary_drift_status",
    "StackInstanceSummaryStackInstanceStatus": ".stack_instance_summary_stack_instance_status",
    "StackInstanceSummaryStackInstanceStatusDetailedStatus": ".stack_instance_summary_stack_instance_status_detailed_status",
    "StackInstanceSummaryStatus": ".stack_instance_summary_status",
    "StackName": ".stack_name",
    "StackNameOrId": ".stack_name_or_id",
    "StackNotFoundException": ".stack_not_found_exception",
    "StackPolicyBody": ".stack_policy_body",
    "StackPolicyDuringUpdateBody": ".stack_policy_during_update_body",
    "StackPolicyDuringUpdateUrl": ".stack_policy_during_update_url",
    "StackPolicyUrl": ".stack_policy_url",
    "StackResource": ".stack_resource",
    "StackResourceDetail": ".stack_resource_detail",
    "StackResourceDetailDriftInformation": ".stack_resource_detail_drift_information",
    "StackResourceDetailDriftInformationStackResourceDriftStatus": ".stack_resource_detail_drift_information_stack_resource_drift_status",
    "StackResourceDetailModuleInfo": ".stack_resource_detail_module_info",
    "StackResourceDetailResourceStatus": ".stack_resource_detail_resource_status",
    "StackResourceDrift": ".stack_resource_drift",
    "StackResourceDriftInformation": ".stack_resource_drift_information",
    "StackResourceDriftInformationStackResourceDriftStatus": ".stack_resource_drift_information_stack_resource_drift_status",
    "StackResourceDriftInformationSummary": ".stack_resource_drift_information_summary",
    "StackResourceDriftInformationSummaryStackResourceDriftStatus": ".stack_resource_drift_information_summary_stack_resource_drift_status",
    "StackResourceDriftModuleInfo": ".stack_resource_drift_module_info",
    "StackResourceDriftStackResourceDriftStatus": ".stack_resource_drift_stack_resource_drift_status",
    "StackResourceDriftStatus": ".stack_resource_drift_status",
    "StackResourceDriftStatusFilters": ".stack_resource_drift_status_filters",
    "StackResourceDrifts": ".stack_resource_drifts",
    "StackResourceModuleInfo": ".stack_resource_module_info",
    "StackResourceResourceStatus": ".stack_resource_resource_status",
    "StackResourceSummaries": ".stack_resource_summaries",
    "StackResourceSummary": ".stack_resource_summary",
    "StackResourceSummaryDriftInformation": ".stack_resource_summary_drift_information",
    "StackResourceSummaryDriftInformationStackResourceDriftStatus": ".stack_resource_summary_drift_information_stack_resource_drift_status",
    "StackResourceSummaryModuleInfo": ".stack_resource_summary_module_info",
    "StackResourceSummaryResourceStatus": ".stack_resource_summary_resource_status",
    "StackResources": ".stack_resources",
    "StackRollbackConfiguration": ".stack_rollback_configuration",
    "StackSet": ".stack_set",
    "StackSetArn": ".stack_set_arn",
    "StackSetAutoDeployment": ".stack_set_auto_deployment",
    "StackSetDriftDetectionDetails": ".stack_set_drift_detection_details",
    "StackSetDriftDetectionDetailsDriftDetectionStatus": ".stack_set_drift_detection_details_drift_detection_status",
    "StackSetDriftDetectionDetailsDriftStatus": ".stack_set_drift_detection_details_drift_status",
    "StackSetDriftDetectionStatus": ".stack_set_drift_detection_status",
    "StackSetDriftStatus": ".stack_set_drift_status",
    "StackSetId": ".stack_set_id",
    "StackSetManagedExecution": ".stack_set_managed_execution",
    "StackSetName": ".stack_set_name",
    "StackSetNameOrId": ".stack_set_name_or_id",
    "StackSetNotEmptyException": ".stack_set_not_empty_exception",
    "StackSetNotFoundException": ".stack_set_not_found_exception",
    "StackSetOperation": ".stack_set_operation",
    "StackSetOperationAction": ".stack_set_operation_action",
    "StackSetOperationDeploymentTargets": ".stack_set_operation_deployment_targets",
    "StackSetOperationDeploymentTargetsAccountFilterType": ".stack_set_operation_deployment_targets_account_filter_type",
    "StackSetOperationOperationPreferences": ".stack_set_operation_operation_preferences",
    "StackSetOperationOperationPreferencesRegionConcurrencyType": ".stack_set_operation_operation_preferences_region_concurrency_type",
    "StackSetOperationPreferences": ".stack_set_operation_preferences",
    "StackSetOperationPreferencesRegionConcurrencyType": ".stack_set_operation_preferences_region_concurrency_type",
    "StackSetOperationResultStatus": ".stack_set_operation_result_status",
    "StackSetOperationResultSummaries": ".stack_set_operation_result_summaries",
    "StackSetOperationResultSummary": ".stack_set_operation_result_summary",
    "StackSetOperationResultSummaryAccountGateResult": ".stack_set_operation_result_summary_account_gate_result",
    "StackSetOperationResultSummaryAccountGateResultStatus": ".stack_set_operation_result_summary_account_gate_result_status",
    "StackSetOperationResultSummaryStatus": ".stack_set_operation_result_summary_status",
    "StackSetOperationStackSetDriftDetectionDetails": ".stack_set_operation_stack_set_drift_detection_details",
    "StackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus": ".stack_set_operation_stack_set_drift_detection_details_drift_detection_status",
    "StackSetOperationStackSetDriftDetectionDetailsDriftStatus": ".stack_set_operation_stack_set_drift_detection_details_drift_status",
    "StackSetOperationStatus": ".stack_set_operation_status",
    "StackSetOperationStatusDetails": ".stack_set_operation_status_details",
    "StackSetOperationStatusReason": ".stack_set_operation_status_reason",
    "StackSetOperationSummaries": ".stack_set_operation_summaries",
    "StackSetOperationSummary": ".stack_set_operation_summary",
    "StackSetOperationSummaryAction": ".stack_set_operation_summary_action",
    "StackSetOperationSummaryStatus": ".stack_set_operation_summary_status",
    "StackSetOperationSummaryStatusDetails": ".stack_set_operation_summary_status_details",
    "StackSetPermissionModel": ".stack_set_permission_model",
    "StackSetStackSetDriftDetectionDetails": ".stack_set_stack_set_drift_detection_details",
    "StackSetStackSetDriftDetectionDetailsDriftDetectionStatus": ".stack_set_stack_set_drift_detection_details_drift_detection_status",
    "StackSetStackSetDriftDetectionDetailsDriftStatus": ".stack_set_stack_set_drift_detection_details_drift_status",
    "StackSetStatus": ".stack_set_status",
    "StackSetSummaries": ".stack_set_summaries",
    "StackSetSummary": ".stack_set_summary",
    "StackSetSummaryAutoDeployment": ".stack_set_summary_auto_deployment",
    "StackSetSummaryDriftStatus": ".stack_set_summary_drift_status",
    "StackSetSummaryManagedExecution": ".stack_set_summary_managed_execution",
    "StackSetSummaryPermissionModel": ".stack_set_summary_permission_model",
    "StackSetSummaryStatus": ".stack_set_summary_status",
    "StackStackStatus": ".stack_stack_status",
    "StackStatus": ".stack_status",
    "StackStatusFilter": ".stack_status_filter",
    "StackStatusReason": ".stack_status_reason",
    "StackSummaries": ".stack_summaries",
    "StackSummary": ".stack_summary",
    "StackSummaryDriftInformation": ".stack_summary_drift_information",
    "StackSummaryDriftInformationStackDriftStatus": ".stack_summary_drift_information_stack_drift_status",
    "StackSummaryStackStatus": ".stack_summary_stack_status",
    "Stacks": ".stacks",
    "StageList": ".stage_list",
    "StaleRequestException": ".stale_request_exception",
    "StatusMessage": ".status_message",
    "StopStackSetOperationInput": ".stop_stack_set_operation_input",
    "StopStackSetOperationInputCallAs": ".stop_stack_set_operation_input_call_as",
    "StopStackSetOperationOutput": ".stop_stack_set_operation_output",
    "SupportedMajorVersion": ".supported_major_version",
    "SupportedMajorVersions": ".supported_major_versions",
    "Tag": ".tag",
    "TagKey": ".tag_key",
    "TagValue": ".tag_value",
    "Tags": ".tags",
    "TemplateBody": ".template_body",
    "TemplateDescription": ".template_description",
    "TemplateParameter": ".template_parameter",
    "TemplateParameters": ".template_parameters",
    "TemplateStage": ".template_stage",
    "TemplateUrl": ".template_url",
    "TestTypeInput": ".test_type_input",
    "TestTypeInputType": ".test_type_input_type",
    "TestTypeOutput": ".test_type_output",
    "ThirdPartyType": ".third_party_type",
    "ThirdPartyTypeArn": ".third_party_type_arn",
    "TimeoutMinutes": ".timeout_minutes",
    "Timestamp": ".timestamp",
    "TokenAlreadyExistsException": ".token_already_exists_exception",
    "TotalStackInstancesCount": ".total_stack_instances_count",
    "TransformName": ".transform_name",
    "TransformsList": ".transforms_list",
    "Type": ".type",
    "TypeArn": ".type_arn",
    "TypeConfiguration": ".type_configuration",
    "TypeConfigurationAlias": ".type_configuration_alias",
    "TypeConfigurationArn": ".type_configuration_arn",
    "TypeConfigurationDetails": ".type_configuration_details",
    "TypeConfigurationDetailsList": ".type_configuration_details_list",
    "TypeConfigurationIdentifier": ".type_configuration_identifier",
    "TypeConfigurationIdentifierType": ".type_configuration_identifier_type",
    "TypeConfigurationIdentifiers": ".type_configuration_identifiers",
    "TypeConfigurationNotFoundException": ".type_configuration_not_found_exception",
    "TypeFilters": ".type_filters",
    "TypeFiltersCategory": ".type_filters_category",
    "TypeHierarchy": ".type_hierarchy",
    "TypeName": ".type_name",
    "TypeNamePrefix": ".type_name_prefix",
    "TypeNotFoundException": ".type_not_found_exception",
    "TypeSchema": ".type_schema",
    "TypeSummaries": ".type_summaries",
    "TypeSummary": ".type_summary",
    "TypeSummaryPublisherIdentity": ".type_summary_publisher_identity",
    "TypeSummaryType": ".type_summary_type",
    "TypeTestsStatus": ".type_tests_status",
    "TypeTestsStatusDescription": ".type_tests_status_description",
    "TypeVersionId": ".type_version_id",
    "TypeVersionSummaries": ".type_version_summaries",
    "TypeVersionSummary": ".type_version_summary",
    "TypeVersionSummaryType": ".type_version_summary_type",
    "UnprocessedTypeConfigurations": ".unprocessed_type_configurations",
    "UpdateStackInput": ".update_stack_input",
    "UpdateStackInputRollbackConfiguration": ".update_stack_input_rollback_configuration",
    "UpdateStackInstancesInput": ".update_stack_instances_input",
    "UpdateStackInstancesInputCallAs": ".update_stack_instances_input_call_as",
    "UpdateStackInstancesInputDeploymentTargets": ".update_stack_instances_input_deployment_targets",
    "UpdateStackInstancesInputDeploymentTargetsAccountFilterType": ".update_stack_instances_input_deployment_targets_account_filter_type",
    "UpdateStackInstancesInputOperationPreferences": ".update_stack_instances_input_operation_preferences",
    "UpdateStackInstancesInputOperationPreferencesRegionConcurrencyType": ".update_stack_instances_input_operation_preferences_region_concurrency_type",
    "UpdateStackInstancesOutput": ".update_stack_instances_output",
    "UpdateStackOutput": ".update_stack_output",
    "UpdateStackSetInput": ".update_stack_set_input",
    "UpdateStackSetInputAutoDeployment": ".update_stack_set_input_auto_deployment",
    "UpdateStackSetInputCallAs": ".update_stack_set_input_call_as",
    "UpdateStackSetInputDeploymentTargets": ".update_stack_set_input_deployment_targets",
    "UpdateStackSetInputDeploymentTargetsAccountFilterType": ".update_stack_set_input_deployment_targets_account_filter_type",
    "UpdateStackSetInputManagedExecution": ".update_stack_set_input_managed_execution",
    "UpdateStackSetInputOperationPreferences": ".update_stack_set_input_operation_preferences",
    "UpdateStackSetInputOperationPreferencesRegionConcurrencyType": ".update_stack_set_input_operation_preferences_region_concurrency_type",
    "UpdateStackSetInputPermissionModel": ".update_stack_set_input_permission_model",
    "UpdateStackSetOutput": ".update_stack_set_output",
    "UpdateTerminationProtectionInput": ".update_termination_protection_input",
    "UpdateTerminationProtectionOutput": ".update_termination_protection_output",
    "Url": ".url",
    "UsePreviousTemplate": ".use_previous_template",
    "UsePreviousValue": ".use_previous_value",
    "ValidateTemplateInput": ".validate_template_input",
    "ValidateTemplateOutput": ".validate_template_output",
    "Value": ".value",
    "Version": ".version",
    "VersionBump": ".version_bump",
    "Visibility": ".visibility",
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
    "AcceptTermsAndConditions",
    "Account",
    "AccountFilterType",
    "AccountGateResult",
    "AccountGateResultStatus",
    "AccountGateStatus",
    "AccountGateStatusReason",
    "AccountLimit",
    "AccountLimitList",
    "AccountList",
    "AccountsUrl",
    "ActivateTypeInput",
    "ActivateTypeInputType",
    "ActivateTypeInputVersionBump",
    "ActivateTypeOutput",
    "AllowedValue",
    "AllowedValues",
    "AlreadyExistsException",
    "Arn",
    "AutoDeployment",
    "AutoDeploymentNullable",
    "AutoUpdate",
    "BatchDescribeTypeConfigurationsError",
    "BatchDescribeTypeConfigurationsErrors",
    "BatchDescribeTypeConfigurationsInput",
    "BatchDescribeTypeConfigurationsOutput",
    "BoxedInteger",
    "BoxedMaxResults",
    "CallAs",
    "CancelUpdateStackInput",
    "Capabilities",
    "CapabilitiesReason",
    "Capability",
    "Category",
    "CausingEntity",
    "CfnRegistryException",
    "Change",
    "ChangeAction",
    "ChangeResourceChange",
    "ChangeResourceChangeAction",
    "ChangeResourceChangeModuleInfo",
    "ChangeResourceChangeReplacement",
    "ChangeSetHook",
    "ChangeSetHookFailureMode",
    "ChangeSetHookInvocationPoint",
    "ChangeSetHookResourceTargetDetails",
    "ChangeSetHookResourceTargetDetailsResourceAction",
    "ChangeSetHookTargetDetails",
    "ChangeSetHookTargetDetailsResourceTargetDetails",
    "ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction",
    "ChangeSetHookTargetDetailsTargetType",
    "ChangeSetHooks",
    "ChangeSetHooksStatus",
    "ChangeSetId",
    "ChangeSetName",
    "ChangeSetNameOrId",
    "ChangeSetNotFoundException",
    "ChangeSetStatus",
    "ChangeSetStatusReason",
    "ChangeSetSummaries",
    "ChangeSetSummary",
    "ChangeSetSummaryExecutionStatus",
    "ChangeSetSummaryStatus",
    "ChangeSetType",
    "ChangeSource",
    "ChangeType",
    "Changes",
    "ClientRequestToken",
    "ClientToken",
    "ConfigurationSchema",
    "ConnectionArn",
    "ContinueUpdateRollbackInput",
    "ContinueUpdateRollbackOutput",
    "CreateChangeSetInput",
    "CreateChangeSetInputChangeSetType",
    "CreateChangeSetInputRollbackConfiguration",
    "CreateChangeSetOutput",
    "CreateStackInput",
    "CreateStackInputOnFailure",
    "CreateStackInputRollbackConfiguration",
    "CreateStackInstancesInput",
    "CreateStackInstancesInputCallAs",
    "CreateStackInstancesInputDeploymentTargets",
    "CreateStackInstancesInputDeploymentTargetsAccountFilterType",
    "CreateStackInstancesInputOperationPreferences",
    "CreateStackInstancesInputOperationPreferencesRegionConcurrencyType",
    "CreateStackInstancesOutput",
    "CreateStackOutput",
    "CreateStackSetInput",
    "CreateStackSetInputAutoDeployment",
    "CreateStackSetInputCallAs",
    "CreateStackSetInputManagedExecution",
    "CreateStackSetInputPermissionModel",
    "CreateStackSetOutput",
    "CreatedButModifiedException",
    "CreationTime",
    "DeactivateTypeInput",
    "DeactivateTypeInputType",
    "DeactivateTypeOutput",
    "DeleteChangeSetInput",
    "DeleteChangeSetOutput",
    "DeleteStackInput",
    "DeleteStackInstancesInput",
    "DeleteStackInstancesInputCallAs",
    "DeleteStackInstancesInputDeploymentTargets",
    "DeleteStackInstancesInputDeploymentTargetsAccountFilterType",
    "DeleteStackInstancesInputOperationPreferences",
    "DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType",
    "DeleteStackInstancesOutput",
    "DeleteStackSetInput",
    "DeleteStackSetInputCallAs",
    "DeleteStackSetOutput",
    "DeletionTime",
    "DeploymentTargets",
    "DeploymentTargetsAccountFilterType",
    "DeprecatedStatus",
    "DeregisterTypeInput",
    "DeregisterTypeInputType",
    "DeregisterTypeOutput",
    "DescribeAccountLimitsInput",
    "DescribeAccountLimitsOutput",
    "DescribeChangeSetHooksInput",
    "DescribeChangeSetHooksOutput",
    "DescribeChangeSetHooksOutputStatus",
    "DescribeChangeSetInput",
    "DescribeChangeSetOutput",
    "DescribeChangeSetOutputExecutionStatus",
    "DescribeChangeSetOutputRollbackConfiguration",
    "DescribeChangeSetOutputStatus",
    "DescribePublisherInput",
    "DescribePublisherOutput",
    "DescribePublisherOutputIdentityProvider",
    "DescribePublisherOutputPublisherStatus",
    "DescribeStackDriftDetectionStatusInput",
    "DescribeStackDriftDetectionStatusOutput",
    "DescribeStackDriftDetectionStatusOutputDetectionStatus",
    "DescribeStackDriftDetectionStatusOutputStackDriftStatus",
    "DescribeStackEventsInput",
    "DescribeStackEventsOutput",
    "DescribeStackInstanceInput",
    "DescribeStackInstanceInputCallAs",
    "DescribeStackInstanceOutput",
    "DescribeStackInstanceOutputStackInstance",
    "DescribeStackInstanceOutputStackInstanceDriftStatus",
    "DescribeStackInstanceOutputStackInstanceStackInstanceStatus",
    "DescribeStackInstanceOutputStackInstanceStackInstanceStatusDetailedStatus",
    "DescribeStackInstanceOutputStackInstanceStatus",
    "DescribeStackResourceDriftsInput",
    "DescribeStackResourceDriftsOutput",
    "DescribeStackResourceInput",
    "DescribeStackResourceOutput",
    "DescribeStackResourceOutputStackResourceDetail",
    "DescribeStackResourceOutputStackResourceDetailDriftInformation",
    "DescribeStackResourceOutputStackResourceDetailDriftInformationStackResourceDriftStatus",
    "DescribeStackResourceOutputStackResourceDetailModuleInfo",
    "DescribeStackResourceOutputStackResourceDetailResourceStatus",
    "DescribeStackResourcesInput",
    "DescribeStackResourcesOutput",
    "DescribeStackSetInput",
    "DescribeStackSetInputCallAs",
    "DescribeStackSetOperationInput",
    "DescribeStackSetOperationInputCallAs",
    "DescribeStackSetOperationOutput",
    "DescribeStackSetOperationOutputStackSetOperation",
    "DescribeStackSetOperationOutputStackSetOperationAction",
    "DescribeStackSetOperationOutputStackSetOperationDeploymentTargets",
    "DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType",
    "DescribeStackSetOperationOutputStackSetOperationOperationPreferences",
    "DescribeStackSetOperationOutputStackSetOperationOperationPreferencesRegionConcurrencyType",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetails",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus",
    "DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus",
    "DescribeStackSetOperationOutputStackSetOperationStatus",
    "DescribeStackSetOperationOutputStackSetOperationStatusDetails",
    "DescribeStackSetOutput",
    "DescribeStackSetOutputStackSet",
    "DescribeStackSetOutputStackSetAutoDeployment",
    "DescribeStackSetOutputStackSetManagedExecution",
    "DescribeStackSetOutputStackSetPermissionModel",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetails",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftDetectionStatus",
    "DescribeStackSetOutputStackSetStackSetDriftDetectionDetailsDriftStatus",
    "DescribeStackSetOutputStackSetStatus",
    "DescribeStacksInput",
    "DescribeStacksOutput",
    "DescribeTypeInput",
    "DescribeTypeInputType",
    "DescribeTypeOutput",
    "DescribeTypeOutputDeprecatedStatus",
    "DescribeTypeOutputLoggingConfig",
    "DescribeTypeOutputProvisioningType",
    "DescribeTypeOutputType",
    "DescribeTypeOutputTypeTestsStatus",
    "DescribeTypeOutputVisibility",
    "DescribeTypeRegistrationInput",
    "DescribeTypeRegistrationOutput",
    "DescribeTypeRegistrationOutputProgressStatus",
    "Description",
    "DetectStackDriftInput",
    "DetectStackDriftOutput",
    "DetectStackResourceDriftInput",
    "DetectStackResourceDriftOutput",
    "DetectStackResourceDriftOutputStackResourceDrift",
    "DetectStackResourceDriftOutputStackResourceDriftModuleInfo",
    "DetectStackResourceDriftOutputStackResourceDriftStackResourceDriftStatus",
    "DetectStackSetDriftInput",
    "DetectStackSetDriftInputCallAs",
    "DetectStackSetDriftOutput",
    "DifferenceType",
    "DisableRollback",
    "DriftedStackInstancesCount",
    "EnableTerminationProtection",
    "ErrorCode",
    "ErrorMessage",
    "EstimateTemplateCostInput",
    "EstimateTemplateCostOutput",
    "EvaluationType",
    "EventId",
    "ExecuteChangeSetInput",
    "ExecuteChangeSetOutput",
    "ExecutionRoleName",
    "ExecutionStatus",
    "Export",
    "ExportName",
    "ExportValue",
    "Exports",
    "FailedStackInstancesCount",
    "FailureToleranceCount",
    "FailureTolerancePercentage",
    "GetActivateTypeRequestAction",
    "GetActivateTypeRequestLoggingConfig",
    "GetActivateTypeRequestType",
    "GetActivateTypeRequestVersion",
    "GetActivateTypeRequestVersionBump",
    "GetBatchDescribeTypeConfigurationsRequestAction",
    "GetBatchDescribeTypeConfigurationsRequestVersion",
    "GetCancelUpdateStackRequestAction",
    "GetCancelUpdateStackRequestVersion",
    "GetContinueUpdateRollbackRequestAction",
    "GetContinueUpdateRollbackRequestVersion",
    "GetCreateChangeSetRequestAction",
    "GetCreateChangeSetRequestChangeSetType",
    "GetCreateChangeSetRequestRollbackConfiguration",
    "GetCreateChangeSetRequestVersion",
    "GetCreateStackInstancesRequestAction",
    "GetCreateStackInstancesRequestCallAs",
    "GetCreateStackInstancesRequestDeploymentTargets",
    "GetCreateStackInstancesRequestDeploymentTargetsAccountFilterType",
    "GetCreateStackInstancesRequestOperationPreferences",
    "GetCreateStackInstancesRequestOperationPreferencesRegionConcurrencyType",
    "GetCreateStackInstancesRequestVersion",
    "GetCreateStackRequestAction",
    "GetCreateStackRequestOnFailure",
    "GetCreateStackRequestRollbackConfiguration",
    "GetCreateStackRequestVersion",
    "GetCreateStackSetRequestAction",
    "GetCreateStackSetRequestAutoDeployment",
    "GetCreateStackSetRequestCallAs",
    "GetCreateStackSetRequestManagedExecution",
    "GetCreateStackSetRequestPermissionModel",
    "GetCreateStackSetRequestVersion",
    "GetDeactivateTypeRequestAction",
    "GetDeactivateTypeRequestType",
    "GetDeactivateTypeRequestVersion",
    "GetDeleteChangeSetRequestAction",
    "GetDeleteChangeSetRequestVersion",
    "GetDeleteStackInstancesRequestAction",
    "GetDeleteStackInstancesRequestCallAs",
    "GetDeleteStackInstancesRequestDeploymentTargets",
    "GetDeleteStackInstancesRequestDeploymentTargetsAccountFilterType",
    "GetDeleteStackInstancesRequestOperationPreferences",
    "GetDeleteStackInstancesRequestOperationPreferencesRegionConcurrencyType",
    "GetDeleteStackInstancesRequestVersion",
    "GetDeleteStackRequestAction",
    "GetDeleteStackRequestVersion",
    "GetDeleteStackSetRequestAction",
    "GetDeleteStackSetRequestCallAs",
    "GetDeleteStackSetRequestVersion",
    "GetDeregisterTypeRequestAction",
    "GetDeregisterTypeRequestType",
    "GetDeregisterTypeRequestVersion",
    "GetDescribeAccountLimitsRequestAction",
    "GetDescribeAccountLimitsRequestVersion",
    "GetDescribeChangeSetHooksRequestAction",
    "GetDescribeChangeSetHooksRequestVersion",
    "GetDescribeChangeSetRequestAction",
    "GetDescribeChangeSetRequestVersion",
    "GetDescribePublisherRequestAction",
    "GetDescribePublisherRequestVersion",
    "GetDescribeStackDriftDetectionStatusRequestAction",
    "GetDescribeStackDriftDetectionStatusRequestVersion",
    "GetDescribeStackEventsRequestAction",
    "GetDescribeStackEventsRequestVersion",
    "GetDescribeStackInstanceRequestAction",
    "GetDescribeStackInstanceRequestCallAs",
    "GetDescribeStackInstanceRequestVersion",
    "GetDescribeStackResourceDriftsRequestAction",
    "GetDescribeStackResourceDriftsRequestVersion",
    "GetDescribeStackResourceRequestAction",
    "GetDescribeStackResourceRequestVersion",
    "GetDescribeStackResourcesRequestAction",
    "GetDescribeStackResourcesRequestVersion",
    "GetDescribeStackSetOperationRequestAction",
    "GetDescribeStackSetOperationRequestCallAs",
    "GetDescribeStackSetOperationRequestVersion",
    "GetDescribeStackSetRequestAction",
    "GetDescribeStackSetRequestCallAs",
    "GetDescribeStackSetRequestVersion",
    "GetDescribeStacksRequestAction",
    "GetDescribeStacksRequestVersion",
    "GetDescribeTypeRegistrationRequestAction",
    "GetDescribeTypeRegistrationRequestVersion",
    "GetDescribeTypeRequestAction",
    "GetDescribeTypeRequestType",
    "GetDescribeTypeRequestVersion",
    "GetDetectStackDriftRequestAction",
    "GetDetectStackDriftRequestVersion",
    "GetDetectStackResourceDriftRequestAction",
    "GetDetectStackResourceDriftRequestVersion",
    "GetDetectStackSetDriftRequestAction",
    "GetDetectStackSetDriftRequestCallAs",
    "GetDetectStackSetDriftRequestOperationPreferences",
    "GetDetectStackSetDriftRequestOperationPreferencesRegionConcurrencyType",
    "GetDetectStackSetDriftRequestVersion",
    "GetEstimateTemplateCostRequestAction",
    "GetEstimateTemplateCostRequestVersion",
    "GetExecuteChangeSetRequestAction",
    "GetExecuteChangeSetRequestVersion",
    "GetGetStackPolicyRequestAction",
    "GetGetStackPolicyRequestVersion",
    "GetGetTemplateRequestAction",
    "GetGetTemplateRequestTemplateStage",
    "GetGetTemplateRequestVersion",
    "GetGetTemplateSummaryRequestAction",
    "GetGetTemplateSummaryRequestCallAs",
    "GetGetTemplateSummaryRequestVersion",
    "GetImportStacksToStackSetRequestAction",
    "GetImportStacksToStackSetRequestCallAs",
    "GetImportStacksToStackSetRequestOperationPreferences",
    "GetImportStacksToStackSetRequestOperationPreferencesRegionConcurrencyType",
    "GetImportStacksToStackSetRequestVersion",
    "GetListChangeSetsRequestAction",
    "GetListChangeSetsRequestVersion",
    "GetListExportsRequestAction",
    "GetListExportsRequestVersion",
    "GetListImportsRequestAction",
    "GetListImportsRequestVersion",
    "GetListStackInstancesRequestAction",
    "GetListStackInstancesRequestCallAs",
    "GetListStackInstancesRequestVersion",
    "GetListStackResourcesRequestAction",
    "GetListStackResourcesRequestVersion",
    "GetListStackSetOperationResultsRequestAction",
    "GetListStackSetOperationResultsRequestCallAs",
    "GetListStackSetOperationResultsRequestVersion",
    "GetListStackSetOperationsRequestAction",
    "GetListStackSetOperationsRequestCallAs",
    "GetListStackSetOperationsRequestVersion",
    "GetListStackSetsRequestAction",
    "GetListStackSetsRequestCallAs",
    "GetListStackSetsRequestStatus",
    "GetListStackSetsRequestVersion",
    "GetListStacksRequestAction",
    "GetListStacksRequestVersion",
    "GetListTypeRegistrationsRequestAction",
    "GetListTypeRegistrationsRequestRegistrationStatusFilter",
    "GetListTypeRegistrationsRequestType",
    "GetListTypeRegistrationsRequestVersion",
    "GetListTypeVersionsRequestAction",
    "GetListTypeVersionsRequestDeprecatedStatus",
    "GetListTypeVersionsRequestType",
    "GetListTypeVersionsRequestVersion",
    "GetListTypesRequestAction",
    "GetListTypesRequestDeprecatedStatus",
    "GetListTypesRequestFilters",
    "GetListTypesRequestFiltersCategory",
    "GetListTypesRequestProvisioningType",
    "GetListTypesRequestType",
    "GetListTypesRequestVersion",
    "GetListTypesRequestVisibility",
    "GetPublishTypeRequestAction",
    "GetPublishTypeRequestType",
    "GetPublishTypeRequestVersion",
    "GetRecordHandlerProgressRequestAction",
    "GetRecordHandlerProgressRequestCurrentOperationStatus",
    "GetRecordHandlerProgressRequestErrorCode",
    "GetRecordHandlerProgressRequestOperationStatus",
    "GetRecordHandlerProgressRequestVersion",
    "GetRegisterPublisherRequestAction",
    "GetRegisterPublisherRequestVersion",
    "GetRegisterTypeRequestAction",
    "GetRegisterTypeRequestLoggingConfig",
    "GetRegisterTypeRequestType",
    "GetRegisterTypeRequestVersion",
    "GetRollbackStackRequestAction",
    "GetRollbackStackRequestVersion",
    "GetSetStackPolicyRequestAction",
    "GetSetStackPolicyRequestVersion",
    "GetSetTypeConfigurationRequestAction",
    "GetSetTypeConfigurationRequestType",
    "GetSetTypeConfigurationRequestVersion",
    "GetSetTypeDefaultVersionRequestAction",
    "GetSetTypeDefaultVersionRequestType",
    "GetSetTypeDefaultVersionRequestVersion",
    "GetSignalResourceRequestAction",
    "GetSignalResourceRequestStatus",
    "GetSignalResourceRequestVersion",
    "GetStackPolicyInput",
    "GetStackPolicyOutput",
    "GetStopStackSetOperationRequestAction",
    "GetStopStackSetOperationRequestCallAs",
    "GetStopStackSetOperationRequestVersion",
    "GetTemplateInput",
    "GetTemplateInputTemplateStage",
    "GetTemplateOutput",
    "GetTemplateSummaryInput",
    "GetTemplateSummaryInputCallAs",
    "GetTemplateSummaryOutput",
    "GetTestTypeRequestAction",
    "GetTestTypeRequestType",
    "GetTestTypeRequestVersion",
    "GetUpdateStackInstancesRequestAction",
    "GetUpdateStackInstancesRequestCallAs",
    "GetUpdateStackInstancesRequestDeploymentTargets",
    "GetUpdateStackInstancesRequestDeploymentTargetsAccountFilterType",
    "GetUpdateStackInstancesRequestOperationPreferences",
    "GetUpdateStackInstancesRequestOperationPreferencesRegionConcurrencyType",
    "GetUpdateStackInstancesRequestVersion",
    "GetUpdateStackRequestAction",
    "GetUpdateStackRequestRollbackConfiguration",
    "GetUpdateStackRequestVersion",
    "GetUpdateStackSetRequestAction",
    "GetUpdateStackSetRequestAutoDeployment",
    "GetUpdateStackSetRequestCallAs",
    "GetUpdateStackSetRequestDeploymentTargets",
    "GetUpdateStackSetRequestDeploymentTargetsAccountFilterType",
    "GetUpdateStackSetRequestManagedExecution",
    "GetUpdateStackSetRequestOperationPreferences",
    "GetUpdateStackSetRequestOperationPreferencesRegionConcurrencyType",
    "GetUpdateStackSetRequestPermissionModel",
    "GetUpdateStackSetRequestVersion",
    "GetUpdateTerminationProtectionRequestAction",
    "GetUpdateTerminationProtectionRequestVersion",
    "GetValidateTemplateRequestAction",
    "GetValidateTemplateRequestVersion",
    "HandlerErrorCode",
    "HookFailureMode",
    "HookInvocationCount",
    "HookInvocationPoint",
    "HookStatus",
    "HookStatusReason",
    "HookTargetType",
    "HookTargetTypeName",
    "HookType",
    "HookTypeConfigurationVersionId",
    "HookTypeName",
    "HookTypeVersionId",
    "IdentityProvider",
    "ImportStacksToStackSetInput",
    "ImportStacksToStackSetInputCallAs",
    "ImportStacksToStackSetOutput",
    "Imports",
    "InProgressStackInstancesCount",
    "InSyncStackInstancesCount",
    "IncludeNestedStacks",
    "InsufficientCapabilitiesException",
    "InvalidChangeSetStatusException",
    "InvalidOperationException",
    "InvalidStateTransitionException",
    "IsActivated",
    "IsDefaultConfiguration",
    "IsDefaultVersion",
    "Key",
    "LastUpdatedTime",
    "LimitExceededException",
    "LimitName",
    "LimitValue",
    "ListChangeSetsInput",
    "ListChangeSetsOutput",
    "ListExportsInput",
    "ListExportsOutput",
    "ListImportsInput",
    "ListImportsOutput",
    "ListStackInstancesInput",
    "ListStackInstancesInputCallAs",
    "ListStackInstancesOutput",
    "ListStackResourcesInput",
    "ListStackResourcesOutput",
    "ListStackSetOperationResultsInput",
    "ListStackSetOperationResultsInputCallAs",
    "ListStackSetOperationResultsOutput",
    "ListStackSetOperationsInput",
    "ListStackSetOperationsInputCallAs",
    "ListStackSetOperationsOutput",
    "ListStackSetsInput",
    "ListStackSetsInputCallAs",
    "ListStackSetsInputStatus",
    "ListStackSetsOutput",
    "ListStacksInput",
    "ListStacksOutput",
    "ListTypeRegistrationsInput",
    "ListTypeRegistrationsInputRegistrationStatusFilter",
    "ListTypeRegistrationsInputType",
    "ListTypeRegistrationsOutput",
    "ListTypeVersionsInput",
    "ListTypeVersionsInputDeprecatedStatus",
    "ListTypeVersionsInputType",
    "ListTypeVersionsOutput",
    "ListTypesInput",
    "ListTypesInputDeprecatedStatus",
    "ListTypesInputFilters",
    "ListTypesInputFiltersCategory",
    "ListTypesInputProvisioningType",
    "ListTypesInputType",
    "ListTypesInputVisibility",
    "ListTypesOutput",
    "LogGroupName",
    "LoggingConfig",
    "LogicalIdHierarchy",
    "LogicalResourceId",
    "LogicalResourceIds",
    "MajorVersion",
    "ManagedExecution",
    "ManagedExecutionNullable",
    "MaxConcurrentCount",
    "MaxConcurrentPercentage",
    "MaxResults",
    "Metadata",
    "ModuleInfo",
    "MonitoringTimeInMinutes",
    "NameAlreadyExistsException",
    "NextToken",
    "NoEcho",
    "NotificationArNs",
    "NotificationArn",
    "OnFailure",
    "OperationIdAlreadyExistsException",
    "OperationInProgressException",
    "OperationNotFoundException",
    "OperationResultFilter",
    "OperationResultFilterName",
    "OperationResultFilterValues",
    "OperationResultFilters",
    "OperationStatus",
    "OperationStatusCheckFailedException",
    "OptionalSecureUrl",
    "OrganizationalUnitId",
    "OrganizationalUnitIdList",
    "Output",
    "OutputKey",
    "OutputValue",
    "Outputs",
    "Parameter",
    "ParameterConstraints",
    "ParameterDeclaration",
    "ParameterDeclarationParameterConstraints",
    "ParameterDeclarations",
    "ParameterKey",
    "ParameterType",
    "ParameterValue",
    "Parameters",
    "PermissionModels",
    "PhysicalResourceId",
    "PhysicalResourceIdContext",
    "PhysicalResourceIdContextKeyValuePair",
    "PostActivateTypeRequestAction",
    "PostActivateTypeRequestVersion",
    "PostBatchDescribeTypeConfigurationsRequestAction",
    "PostBatchDescribeTypeConfigurationsRequestVersion",
    "PostCancelUpdateStackRequestAction",
    "PostCancelUpdateStackRequestVersion",
    "PostContinueUpdateRollbackRequestAction",
    "PostContinueUpdateRollbackRequestVersion",
    "PostCreateChangeSetRequestAction",
    "PostCreateChangeSetRequestVersion",
    "PostCreateStackInstancesRequestAction",
    "PostCreateStackInstancesRequestVersion",
    "PostCreateStackRequestAction",
    "PostCreateStackRequestVersion",
    "PostCreateStackSetRequestAction",
    "PostCreateStackSetRequestVersion",
    "PostDeactivateTypeRequestAction",
    "PostDeactivateTypeRequestVersion",
    "PostDeleteChangeSetRequestAction",
    "PostDeleteChangeSetRequestVersion",
    "PostDeleteStackInstancesRequestAction",
    "PostDeleteStackInstancesRequestVersion",
    "PostDeleteStackRequestAction",
    "PostDeleteStackRequestVersion",
    "PostDeleteStackSetRequestAction",
    "PostDeleteStackSetRequestVersion",
    "PostDeregisterTypeRequestAction",
    "PostDeregisterTypeRequestVersion",
    "PostDescribeAccountLimitsRequestAction",
    "PostDescribeAccountLimitsRequestVersion",
    "PostDescribeChangeSetHooksRequestAction",
    "PostDescribeChangeSetHooksRequestVersion",
    "PostDescribeChangeSetRequestAction",
    "PostDescribeChangeSetRequestVersion",
    "PostDescribePublisherRequestAction",
    "PostDescribePublisherRequestVersion",
    "PostDescribeStackDriftDetectionStatusRequestAction",
    "PostDescribeStackDriftDetectionStatusRequestVersion",
    "PostDescribeStackEventsRequestAction",
    "PostDescribeStackEventsRequestVersion",
    "PostDescribeStackInstanceRequestAction",
    "PostDescribeStackInstanceRequestVersion",
    "PostDescribeStackResourceDriftsRequestAction",
    "PostDescribeStackResourceDriftsRequestVersion",
    "PostDescribeStackResourceRequestAction",
    "PostDescribeStackResourceRequestVersion",
    "PostDescribeStackResourcesRequestAction",
    "PostDescribeStackResourcesRequestVersion",
    "PostDescribeStackSetOperationRequestAction",
    "PostDescribeStackSetOperationRequestVersion",
    "PostDescribeStackSetRequestAction",
    "PostDescribeStackSetRequestVersion",
    "PostDescribeStacksRequestAction",
    "PostDescribeStacksRequestVersion",
    "PostDescribeTypeRegistrationRequestAction",
    "PostDescribeTypeRegistrationRequestVersion",
    "PostDescribeTypeRequestAction",
    "PostDescribeTypeRequestVersion",
    "PostDetectStackDriftRequestAction",
    "PostDetectStackDriftRequestVersion",
    "PostDetectStackResourceDriftRequestAction",
    "PostDetectStackResourceDriftRequestVersion",
    "PostDetectStackSetDriftRequestAction",
    "PostDetectStackSetDriftRequestVersion",
    "PostEstimateTemplateCostRequestAction",
    "PostEstimateTemplateCostRequestVersion",
    "PostExecuteChangeSetRequestAction",
    "PostExecuteChangeSetRequestVersion",
    "PostGetStackPolicyRequestAction",
    "PostGetStackPolicyRequestVersion",
    "PostGetTemplateRequestAction",
    "PostGetTemplateRequestVersion",
    "PostGetTemplateSummaryRequestAction",
    "PostGetTemplateSummaryRequestVersion",
    "PostImportStacksToStackSetRequestAction",
    "PostImportStacksToStackSetRequestVersion",
    "PostListChangeSetsRequestAction",
    "PostListChangeSetsRequestVersion",
    "PostListExportsRequestAction",
    "PostListExportsRequestVersion",
    "PostListImportsRequestAction",
    "PostListImportsRequestVersion",
    "PostListStackInstancesRequestAction",
    "PostListStackInstancesRequestVersion",
    "PostListStackResourcesRequestAction",
    "PostListStackResourcesRequestVersion",
    "PostListStackSetOperationResultsRequestAction",
    "PostListStackSetOperationResultsRequestVersion",
    "PostListStackSetOperationsRequestAction",
    "PostListStackSetOperationsRequestVersion",
    "PostListStackSetsRequestAction",
    "PostListStackSetsRequestVersion",
    "PostListStacksRequestAction",
    "PostListStacksRequestVersion",
    "PostListTypeRegistrationsRequestAction",
    "PostListTypeRegistrationsRequestVersion",
    "PostListTypeVersionsRequestAction",
    "PostListTypeVersionsRequestVersion",
    "PostListTypesRequestAction",
    "PostListTypesRequestVersion",
    "PostPublishTypeRequestAction",
    "PostPublishTypeRequestVersion",
    "PostRecordHandlerProgressRequestAction",
    "PostRecordHandlerProgressRequestVersion",
    "PostRegisterPublisherRequestAction",
    "PostRegisterPublisherRequestVersion",
    "PostRegisterTypeRequestAction",
    "PostRegisterTypeRequestVersion",
    "PostRollbackStackRequestAction",
    "PostRollbackStackRequestVersion",
    "PostSetStackPolicyRequestAction",
    "PostSetStackPolicyRequestVersion",
    "PostSetTypeConfigurationRequestAction",
    "PostSetTypeConfigurationRequestVersion",
    "PostSetTypeDefaultVersionRequestAction",
    "PostSetTypeDefaultVersionRequestVersion",
    "PostSignalResourceRequestAction",
    "PostSignalResourceRequestVersion",
    "PostStopStackSetOperationRequestAction",
    "PostStopStackSetOperationRequestVersion",
    "PostTestTypeRequestAction",
    "PostTestTypeRequestVersion",
    "PostUpdateStackInstancesRequestAction",
    "PostUpdateStackInstancesRequestVersion",
    "PostUpdateStackRequestAction",
    "PostUpdateStackRequestVersion",
    "PostUpdateStackSetRequestAction",
    "PostUpdateStackSetRequestVersion",
    "PostUpdateTerminationProtectionRequestAction",
    "PostUpdateTerminationProtectionRequestVersion",
    "PostValidateTemplateRequestAction",
    "PostValidateTemplateRequestVersion",
    "PrivateTypeArn",
    "Properties",
    "PropertyDifference",
    "PropertyDifferenceDifferenceType",
    "PropertyDifferences",
    "PropertyName",
    "PropertyPath",
    "PropertyValue",
    "ProvisioningType",
    "PublicVersionNumber",
    "PublishTypeInput",
    "PublishTypeInputType",
    "PublishTypeOutput",
    "PublisherId",
    "PublisherName",
    "PublisherProfile",
    "PublisherStatus",
    "Reason",
    "RecordHandlerProgressInput",
    "RecordHandlerProgressInputCurrentOperationStatus",
    "RecordHandlerProgressInputErrorCode",
    "RecordHandlerProgressInputOperationStatus",
    "RecordHandlerProgressOutput",
    "Region",
    "RegionConcurrencyType",
    "RegionList",
    "RegisterPublisherInput",
    "RegisterPublisherOutput",
    "RegisterTypeInput",
    "RegisterTypeInputLoggingConfig",
    "RegisterTypeInputType",
    "RegisterTypeOutput",
    "RegistrationStatus",
    "RegistrationToken",
    "RegistrationTokenList",
    "RegistryType",
    "Replacement",
    "RequestToken",
    "RequiredActivatedType",
    "RequiredActivatedTypes",
    "RequiresRecreation",
    "ResourceAttribute",
    "ResourceChange",
    "ResourceChangeAction",
    "ResourceChangeDetail",
    "ResourceChangeDetailChangeSource",
    "ResourceChangeDetailEvaluation",
    "ResourceChangeDetailTarget",
    "ResourceChangeDetailTargetAttribute",
    "ResourceChangeDetailTargetRequiresRecreation",
    "ResourceChangeDetails",
    "ResourceChangeModuleInfo",
    "ResourceChangeReplacement",
    "ResourceIdentifierProperties",
    "ResourceIdentifierPropertyKey",
    "ResourceIdentifierPropertyValue",
    "ResourceIdentifierSummaries",
    "ResourceIdentifierSummary",
    "ResourceIdentifiers",
    "ResourceModel",
    "ResourceProperties",
    "ResourceSignalStatus",
    "ResourceSignalUniqueId",
    "ResourceStatus",
    "ResourceStatusReason",
    "ResourceTargetDefinition",
    "ResourceTargetDefinitionAttribute",
    "ResourceTargetDefinitionRequiresRecreation",
    "ResourceToImport",
    "ResourceToSkip",
    "ResourceType",
    "ResourceTypes",
    "ResourcesToImport",
    "ResourcesToSkip",
    "RetainResources",
    "RetainStacks",
    "RetainStacksNullable",
    "RetainStacksOnAccountRemovalNullable",
    "RoleArn",
    "RollbackConfiguration",
    "RollbackStackInput",
    "RollbackStackOutput",
    "RollbackTrigger",
    "RollbackTriggers",
    "S3Bucket",
    "S3Url",
    "Scope",
    "SetStackPolicyInput",
    "SetTypeConfigurationInput",
    "SetTypeConfigurationInputType",
    "SetTypeConfigurationOutput",
    "SetTypeDefaultVersionInput",
    "SetTypeDefaultVersionInputType",
    "SetTypeDefaultVersionOutput",
    "SignalResourceInput",
    "SignalResourceInputStatus",
    "Stack",
    "StackDriftDetectionId",
    "StackDriftDetectionStatus",
    "StackDriftDetectionStatusReason",
    "StackDriftInformation",
    "StackDriftInformationStackDriftStatus",
    "StackDriftInformationSummary",
    "StackDriftInformationSummaryStackDriftStatus",
    "StackDriftStatus",
    "StackEvent",
    "StackEventHookFailureMode",
    "StackEventHookInvocationPoint",
    "StackEventHookStatus",
    "StackEventResourceStatus",
    "StackEvents",
    "StackId",
    "StackIdList",
    "StackIdsUrl",
    "StackInstance",
    "StackInstanceComprehensiveStatus",
    "StackInstanceComprehensiveStatusDetailedStatus",
    "StackInstanceDetailedStatus",
    "StackInstanceDriftStatus",
    "StackInstanceFilter",
    "StackInstanceFilterName",
    "StackInstanceFilterValues",
    "StackInstanceFilters",
    "StackInstanceNotFoundException",
    "StackInstanceStackInstanceStatus",
    "StackInstanceStackInstanceStatusDetailedStatus",
    "StackInstanceStatus",
    "StackInstanceSummaries",
    "StackInstanceSummary",
    "StackInstanceSummaryDriftStatus",
    "StackInstanceSummaryStackInstanceStatus",
    "StackInstanceSummaryStackInstanceStatusDetailedStatus",
    "StackInstanceSummaryStatus",
    "StackName",
    "StackNameOrId",
    "StackNotFoundException",
    "StackPolicyBody",
    "StackPolicyDuringUpdateBody",
    "StackPolicyDuringUpdateUrl",
    "StackPolicyUrl",
    "StackResource",
    "StackResourceDetail",
    "StackResourceDetailDriftInformation",
    "StackResourceDetailDriftInformationStackResourceDriftStatus",
    "StackResourceDetailModuleInfo",
    "StackResourceDetailResourceStatus",
    "StackResourceDrift",
    "StackResourceDriftInformation",
    "StackResourceDriftInformationStackResourceDriftStatus",
    "StackResourceDriftInformationSummary",
    "StackResourceDriftInformationSummaryStackResourceDriftStatus",
    "StackResourceDriftModuleInfo",
    "StackResourceDriftStackResourceDriftStatus",
    "StackResourceDriftStatus",
    "StackResourceDriftStatusFilters",
    "StackResourceDrifts",
    "StackResourceModuleInfo",
    "StackResourceResourceStatus",
    "StackResourceSummaries",
    "StackResourceSummary",
    "StackResourceSummaryDriftInformation",
    "StackResourceSummaryDriftInformationStackResourceDriftStatus",
    "StackResourceSummaryModuleInfo",
    "StackResourceSummaryResourceStatus",
    "StackResources",
    "StackRollbackConfiguration",
    "StackSet",
    "StackSetArn",
    "StackSetAutoDeployment",
    "StackSetDriftDetectionDetails",
    "StackSetDriftDetectionDetailsDriftDetectionStatus",
    "StackSetDriftDetectionDetailsDriftStatus",
    "StackSetDriftDetectionStatus",
    "StackSetDriftStatus",
    "StackSetId",
    "StackSetManagedExecution",
    "StackSetName",
    "StackSetNameOrId",
    "StackSetNotEmptyException",
    "StackSetNotFoundException",
    "StackSetOperation",
    "StackSetOperationAction",
    "StackSetOperationDeploymentTargets",
    "StackSetOperationDeploymentTargetsAccountFilterType",
    "StackSetOperationOperationPreferences",
    "StackSetOperationOperationPreferencesRegionConcurrencyType",
    "StackSetOperationPreferences",
    "StackSetOperationPreferencesRegionConcurrencyType",
    "StackSetOperationResultStatus",
    "StackSetOperationResultSummaries",
    "StackSetOperationResultSummary",
    "StackSetOperationResultSummaryAccountGateResult",
    "StackSetOperationResultSummaryAccountGateResultStatus",
    "StackSetOperationResultSummaryStatus",
    "StackSetOperationStackSetDriftDetectionDetails",
    "StackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus",
    "StackSetOperationStackSetDriftDetectionDetailsDriftStatus",
    "StackSetOperationStatus",
    "StackSetOperationStatusDetails",
    "StackSetOperationStatusReason",
    "StackSetOperationSummaries",
    "StackSetOperationSummary",
    "StackSetOperationSummaryAction",
    "StackSetOperationSummaryStatus",
    "StackSetOperationSummaryStatusDetails",
    "StackSetPermissionModel",
    "StackSetStackSetDriftDetectionDetails",
    "StackSetStackSetDriftDetectionDetailsDriftDetectionStatus",
    "StackSetStackSetDriftDetectionDetailsDriftStatus",
    "StackSetStatus",
    "StackSetSummaries",
    "StackSetSummary",
    "StackSetSummaryAutoDeployment",
    "StackSetSummaryDriftStatus",
    "StackSetSummaryManagedExecution",
    "StackSetSummaryPermissionModel",
    "StackSetSummaryStatus",
    "StackStackStatus",
    "StackStatus",
    "StackStatusFilter",
    "StackStatusReason",
    "StackSummaries",
    "StackSummary",
    "StackSummaryDriftInformation",
    "StackSummaryDriftInformationStackDriftStatus",
    "StackSummaryStackStatus",
    "Stacks",
    "StageList",
    "StaleRequestException",
    "StatusMessage",
    "StopStackSetOperationInput",
    "StopStackSetOperationInputCallAs",
    "StopStackSetOperationOutput",
    "SupportedMajorVersion",
    "SupportedMajorVersions",
    "Tag",
    "TagKey",
    "TagValue",
    "Tags",
    "TemplateBody",
    "TemplateDescription",
    "TemplateParameter",
    "TemplateParameters",
    "TemplateStage",
    "TemplateUrl",
    "TestTypeInput",
    "TestTypeInputType",
    "TestTypeOutput",
    "ThirdPartyType",
    "ThirdPartyTypeArn",
    "TimeoutMinutes",
    "Timestamp",
    "TokenAlreadyExistsException",
    "TotalStackInstancesCount",
    "TransformName",
    "TransformsList",
    "Type",
    "TypeArn",
    "TypeConfiguration",
    "TypeConfigurationAlias",
    "TypeConfigurationArn",
    "TypeConfigurationDetails",
    "TypeConfigurationDetailsList",
    "TypeConfigurationIdentifier",
    "TypeConfigurationIdentifierType",
    "TypeConfigurationIdentifiers",
    "TypeConfigurationNotFoundException",
    "TypeFilters",
    "TypeFiltersCategory",
    "TypeHierarchy",
    "TypeName",
    "TypeNamePrefix",
    "TypeNotFoundException",
    "TypeSchema",
    "TypeSummaries",
    "TypeSummary",
    "TypeSummaryPublisherIdentity",
    "TypeSummaryType",
    "TypeTestsStatus",
    "TypeTestsStatusDescription",
    "TypeVersionId",
    "TypeVersionSummaries",
    "TypeVersionSummary",
    "TypeVersionSummaryType",
    "UnprocessedTypeConfigurations",
    "UpdateStackInput",
    "UpdateStackInputRollbackConfiguration",
    "UpdateStackInstancesInput",
    "UpdateStackInstancesInputCallAs",
    "UpdateStackInstancesInputDeploymentTargets",
    "UpdateStackInstancesInputDeploymentTargetsAccountFilterType",
    "UpdateStackInstancesInputOperationPreferences",
    "UpdateStackInstancesInputOperationPreferencesRegionConcurrencyType",
    "UpdateStackInstancesOutput",
    "UpdateStackOutput",
    "UpdateStackSetInput",
    "UpdateStackSetInputAutoDeployment",
    "UpdateStackSetInputCallAs",
    "UpdateStackSetInputDeploymentTargets",
    "UpdateStackSetInputDeploymentTargetsAccountFilterType",
    "UpdateStackSetInputManagedExecution",
    "UpdateStackSetInputOperationPreferences",
    "UpdateStackSetInputOperationPreferencesRegionConcurrencyType",
    "UpdateStackSetInputPermissionModel",
    "UpdateStackSetOutput",
    "UpdateTerminationProtectionInput",
    "UpdateTerminationProtectionOutput",
    "Url",
    "UsePreviousTemplate",
    "UsePreviousValue",
    "ValidateTemplateInput",
    "ValidateTemplateOutput",
    "Value",
    "Version",
    "VersionBump",
    "Visibility",
]
