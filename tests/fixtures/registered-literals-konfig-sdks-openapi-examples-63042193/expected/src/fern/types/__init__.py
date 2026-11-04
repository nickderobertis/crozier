



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bundle_diff import BundleDiff
    from .claim_response import ClaimResponse
    from .context_create_new_context_response import ContextCreateNewContextResponse
    from .context_create_new_contextdefault_response import ContextCreateNewContextdefaultResponse
    from .context_create_restriction409response import ContextCreateRestriction409Response
    from .context_create_restriction_response import ContextCreateRestrictionResponse
    from .context_delete_restriction_response import ContextDeleteRestrictionResponse
    from .context_get_information_response import ContextGetInformationResponse
    from .context_get_informationdefault_response import ContextGetInformationdefaultResponse
    from .context_get_restrictions401response import ContextGetRestrictions401Response
    from .context_get_restrictions404response import ContextGetRestrictions404Response
    from .context_get_restrictions429response import ContextGetRestrictions429Response
    from .context_get_restrictions500response import ContextGetRestrictions500Response
    from .context_get_restrictions_response import ContextGetRestrictionsResponse
    from .context_list_environment_variables_response import ContextListEnvironmentVariablesResponse
    from .context_list_environment_variables_response_items_item import ContextListEnvironmentVariablesResponseItemsItem
    from .context_list_environment_variablesdefault_response import ContextListEnvironmentVariablesdefaultResponse
    from .context_list_owner_contexts_response import ContextListOwnerContextsResponse
    from .context_list_owner_contexts_response_items_item import ContextListOwnerContextsResponseItemsItem
    from .context_list_owner_contextsdefault_response import ContextListOwnerContextsdefaultResponse
    from .context_project_restrictions_list import ContextProjectRestrictionsList
    from .context_project_restrictions_list_items_item import ContextProjectRestrictionsListItemsItem
    from .context_project_restrictions_list_items_item_restriction_type import (
        ContextProjectRestrictionsListItemsItemRestrictionType,
    )
    from .context_remove_context_response import ContextRemoveContextResponse
    from .context_remove_contextdefault_response import ContextRemoveContextdefaultResponse
    from .context_remove_environment_variable_response import ContextRemoveEnvironmentVariableResponse
    from .context_remove_environment_variabledefault_response import ContextRemoveEnvironmentVariabledefaultResponse
    from .context_update_environment_variable_response import ContextUpdateEnvironmentVariableResponse
    from .context_update_environment_variable_response_context_id import (
        ContextUpdateEnvironmentVariableResponseContextId,
    )
    from .context_update_environment_variable_response_message import ContextUpdateEnvironmentVariableResponseMessage
    from .context_update_environment_variabledefault_response import ContextUpdateEnvironmentVariabledefaultResponse
    from .decision import Decision
    from .decision_log import DecisionLog
    from .decision_log_metadata import DecisionLogMetadata
    from .decision_log_metadata_vcs import DecisionLogMetadataVcs
    from .decision_settings import DecisionSettings
    from .insights_get_flaky_tests_response import InsightsGetFlakyTestsResponse
    from .insights_get_flaky_tests_response_flaky_tests_item import InsightsGetFlakyTestsResponseFlakyTestsItem
    from .insights_get_flaky_tests_response_flaky_tests_item_job_number import (
        InsightsGetFlakyTestsResponseFlakyTestsItemJobNumber,
    )
    from .insights_get_flaky_tests_response_flaky_tests_item_pipeline_number import (
        InsightsGetFlakyTestsResponseFlakyTestsItemPipelineNumber,
    )
    from .insights_get_flaky_tests_response_flaky_tests_item_time_wasted import (
        InsightsGetFlakyTestsResponseFlakyTestsItemTimeWasted,
    )
    from .insights_get_flaky_testsdefault_response import InsightsGetFlakyTestsdefaultResponse
    from .insights_get_job_timeseries_data_response import InsightsGetJobTimeseriesDataResponse
    from .insights_get_job_timeseries_data_response_items_item import InsightsGetJobTimeseriesDataResponseItemsItem
    from .insights_get_job_timeseries_data_response_items_item_metrics import (
        InsightsGetJobTimeseriesDataResponseItemsItemMetrics,
    )
    from .insights_get_job_timeseries_data_response_items_item_metrics_duration_metrics import (
        InsightsGetJobTimeseriesDataResponseItemsItemMetricsDurationMetrics,
    )
    from .insights_get_job_timeseries_datadefault_response import InsightsGetJobTimeseriesDatadefaultResponse
    from .insights_get_project_summary_metrics_response import InsightsGetProjectSummaryMetricsResponse
    from .insights_get_project_summary_metrics_response_project_data import (
        InsightsGetProjectSummaryMetricsResponseProjectData,
    )
    from .insights_get_project_summary_metrics_response_project_data_metrics import (
        InsightsGetProjectSummaryMetricsResponseProjectDataMetrics,
    )
    from .insights_get_project_summary_metrics_response_project_data_trends import (
        InsightsGetProjectSummaryMetricsResponseProjectDataTrends,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item_metrics import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item_trends import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_data_item import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_data_item_metrics import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemMetrics,
    )
    from .insights_get_project_summary_metrics_response_project_workflow_data_item_trends import (
        InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemTrends,
    )
    from .insights_get_project_summary_metricsdefault_response import InsightsGetProjectSummaryMetricsdefaultResponse
    from .insights_get_project_workflow_job_metrics_response import InsightsGetProjectWorkflowJobMetricsResponse
    from .insights_get_project_workflow_job_metrics_response_items_item import (
        InsightsGetProjectWorkflowJobMetricsResponseItemsItem,
    )
    from .insights_get_project_workflow_job_metrics_response_items_item_metrics import (
        InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics,
    )
    from .insights_get_project_workflow_job_metrics_response_items_item_metrics_duration_metrics import (
        InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics,
    )
    from .insights_get_project_workflow_job_metricsdefault_response import (
        InsightsGetProjectWorkflowJobMetricsdefaultResponse,
    )
    from .insights_get_project_workflow_metrics_response import InsightsGetProjectWorkflowMetricsResponse
    from .insights_get_project_workflow_metrics_response_items_item import (
        InsightsGetProjectWorkflowMetricsResponseItemsItem,
    )
    from .insights_get_project_workflow_metrics_response_items_item_metrics import (
        InsightsGetProjectWorkflowMetricsResponseItemsItemMetrics,
    )
    from .insights_get_project_workflow_metrics_response_items_item_metrics_duration_metrics import (
        InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics,
    )
    from .insights_get_project_workflow_metricsdefault_response import InsightsGetProjectWorkflowMetricsdefaultResponse
    from .insights_get_project_workflow_test_metrics_response import InsightsGetProjectWorkflowTestMetricsResponse
    from .insights_get_project_workflow_test_metrics_response_most_failed_tests_item import (
        InsightsGetProjectWorkflowTestMetricsResponseMostFailedTestsItem,
    )
    from .insights_get_project_workflow_test_metrics_response_slowest_tests_item import (
        InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem,
    )
    from .insights_get_project_workflow_test_metrics_response_test_runs_item import (
        InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem,
    )
    from .insights_get_project_workflow_test_metrics_response_test_runs_item_test_counts import (
        InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts,
    )
    from .insights_get_project_workflow_test_metricsdefault_response import (
        InsightsGetProjectWorkflowTestMetricsdefaultResponse,
    )
    from .insights_get_recent_workflow_runs_response import InsightsGetRecentWorkflowRunsResponse
    from .insights_get_recent_workflow_runs_response_items_item import InsightsGetRecentWorkflowRunsResponseItemsItem
    from .insights_get_recent_workflow_runs_response_items_item_status import (
        InsightsGetRecentWorkflowRunsResponseItemsItemStatus,
    )
    from .insights_get_recent_workflow_runsdefault_response import InsightsGetRecentWorkflowRunsdefaultResponse
    from .insights_get_summary_metrics_with_trends_response import InsightsGetSummaryMetricsWithTrendsResponse
    from .insights_get_summary_metrics_with_trends_response_org_data import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgData,
    )
    from .insights_get_summary_metrics_with_trends_response_org_data_metrics import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics,
    )
    from .insights_get_summary_metrics_with_trends_response_org_data_trends import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends,
    )
    from .insights_get_summary_metrics_with_trends_response_org_project_data_item import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem,
    )
    from .insights_get_summary_metrics_with_trends_response_org_project_data_item_metrics import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics,
    )
    from .insights_get_summary_metrics_with_trends_response_org_project_data_item_trends import (
        InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends,
    )
    from .insights_get_summary_metrics_with_trendsdefault_response import (
        InsightsGetSummaryMetricsWithTrendsdefaultResponse,
    )
    from .insights_get_workflow_summary_metrics_response import InsightsGetWorkflowSummaryMetricsResponse
    from .insights_get_workflow_summary_metrics_response_metrics import InsightsGetWorkflowSummaryMetricsResponseMetrics
    from .insights_get_workflow_summary_metrics_response_metrics_duration_metrics import (
        InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics,
    )
    from .insights_get_workflow_summary_metrics_response_trends import InsightsGetWorkflowSummaryMetricsResponseTrends
    from .insights_get_workflow_summary_metricsdefault_response import InsightsGetWorkflowSummaryMetricsdefaultResponse
    from .insights_list_project_branches_response import InsightsListProjectBranchesResponse
    from .insights_list_project_branchesdefault_response import InsightsListProjectBranchesdefaultResponse
    from .job_cancel_with_number_response import JobCancelWithNumberResponse
    from .job_cancel_with_numberdefault_response import JobCancelWithNumberdefaultResponse
    from .job_get_artifacts_response import JobGetArtifactsResponse
    from .job_get_artifacts_response_items_item import JobGetArtifactsResponseItemsItem
    from .job_get_artifactsdefault_response import JobGetArtifactsdefaultResponse
    from .job_get_details_response import JobGetDetailsResponse
    from .job_get_details_response_contexts_item import JobGetDetailsResponseContextsItem
    from .job_get_details_response_executor import JobGetDetailsResponseExecutor
    from .job_get_details_response_latest_workflow import JobGetDetailsResponseLatestWorkflow
    from .job_get_details_response_messages_item import JobGetDetailsResponseMessagesItem
    from .job_get_details_response_organization import JobGetDetailsResponseOrganization
    from .job_get_details_response_parallel_runs_item import JobGetDetailsResponseParallelRunsItem
    from .job_get_details_response_pipeline import JobGetDetailsResponsePipeline
    from .job_get_details_response_project import JobGetDetailsResponseProject
    from .job_get_details_response_status import JobGetDetailsResponseStatus
    from .job_get_detailsdefault_response import JobGetDetailsdefaultResponse
    from .job_get_test_metadata_response import JobGetTestMetadataResponse
    from .job_get_test_metadata_response_items_item import JobGetTestMetadataResponseItemsItem
    from .job_get_test_metadatadefault_response import JobGetTestMetadatadefaultResponse
    from .json_duration import JsonDuration
    from .oidc_token_management_delete_org_claims403response import OidcTokenManagementDeleteOrgClaims403Response
    from .oidc_token_management_delete_org_claims500response import OidcTokenManagementDeleteOrgClaims500Response
    from .oidc_token_management_delete_org_claims_response import OidcTokenManagementDeleteOrgClaimsResponse
    from .patch_claims_request import PatchClaimsRequest
    from .pipeline_continue_execution_response import PipelineContinueExecutionResponse
    from .pipeline_continue_executiondefault_response import PipelineContinueExecutiondefaultResponse
    from .pipeline_get_all_pipelines_response import PipelineGetAllPipelinesResponse
    from .pipeline_get_all_pipelines_response_items_item import PipelineGetAllPipelinesResponseItemsItem
    from .pipeline_get_all_pipelines_response_items_item_errors_item import (
        PipelineGetAllPipelinesResponseItemsItemErrorsItem,
    )
    from .pipeline_get_all_pipelines_response_items_item_errors_item_type import (
        PipelineGetAllPipelinesResponseItemsItemErrorsItemType,
    )
    from .pipeline_get_all_pipelines_response_items_item_state import PipelineGetAllPipelinesResponseItemsItemState
    from .pipeline_get_all_pipelines_response_items_item_trigger import PipelineGetAllPipelinesResponseItemsItemTrigger
    from .pipeline_get_all_pipelines_response_items_item_trigger_actor import (
        PipelineGetAllPipelinesResponseItemsItemTriggerActor,
    )
    from .pipeline_get_all_pipelines_response_items_item_trigger_parameters_value import (
        PipelineGetAllPipelinesResponseItemsItemTriggerParametersValue,
    )
    from .pipeline_get_all_pipelines_response_items_item_trigger_type import (
        PipelineGetAllPipelinesResponseItemsItemTriggerType,
    )
    from .pipeline_get_all_pipelines_response_items_item_vcs import PipelineGetAllPipelinesResponseItemsItemVcs
    from .pipeline_get_all_pipelines_response_items_item_vcs_commit import (
        PipelineGetAllPipelinesResponseItemsItemVcsCommit,
    )
    from .pipeline_get_all_pipelinesdefault_response import PipelineGetAllPipelinesdefaultResponse
    from .pipeline_get_by_id_response import PipelineGetByIdResponse
    from .pipeline_get_by_id_response_errors_item import PipelineGetByIdResponseErrorsItem
    from .pipeline_get_by_id_response_errors_item_type import PipelineGetByIdResponseErrorsItemType
    from .pipeline_get_by_id_response_state import PipelineGetByIdResponseState
    from .pipeline_get_by_id_response_trigger import PipelineGetByIdResponseTrigger
    from .pipeline_get_by_id_response_trigger_actor import PipelineGetByIdResponseTriggerActor
    from .pipeline_get_by_id_response_trigger_parameters_value import PipelineGetByIdResponseTriggerParametersValue
    from .pipeline_get_by_id_response_trigger_type import PipelineGetByIdResponseTriggerType
    from .pipeline_get_by_id_response_vcs import PipelineGetByIdResponseVcs
    from .pipeline_get_by_id_response_vcs_commit import PipelineGetByIdResponseVcsCommit
    from .pipeline_get_by_iddefault_response import PipelineGetByIddefaultResponse
    from .pipeline_get_by_number_response import PipelineGetByNumberResponse
    from .pipeline_get_by_number_response_errors_item import PipelineGetByNumberResponseErrorsItem
    from .pipeline_get_by_number_response_errors_item_type import PipelineGetByNumberResponseErrorsItemType
    from .pipeline_get_by_number_response_state import PipelineGetByNumberResponseState
    from .pipeline_get_by_number_response_trigger import PipelineGetByNumberResponseTrigger
    from .pipeline_get_by_number_response_trigger_actor import PipelineGetByNumberResponseTriggerActor
    from .pipeline_get_by_number_response_trigger_parameters_value import (
        PipelineGetByNumberResponseTriggerParametersValue,
    )
    from .pipeline_get_by_number_response_trigger_type import PipelineGetByNumberResponseTriggerType
    from .pipeline_get_by_number_response_vcs import PipelineGetByNumberResponseVcs
    from .pipeline_get_by_number_response_vcs_commit import PipelineGetByNumberResponseVcsCommit
    from .pipeline_get_by_numberdefault_response import PipelineGetByNumberdefaultResponse
    from .pipeline_get_configuration_by_id_response import PipelineGetConfigurationByIdResponse
    from .pipeline_get_configuration_by_iddefault_response import PipelineGetConfigurationByIddefaultResponse
    from .pipeline_list_recent_pipelines_response import PipelineListRecentPipelinesResponse
    from .pipeline_list_recent_pipelines_response_items_item import PipelineListRecentPipelinesResponseItemsItem
    from .pipeline_list_recent_pipelines_response_items_item_errors_item import (
        PipelineListRecentPipelinesResponseItemsItemErrorsItem,
    )
    from .pipeline_list_recent_pipelines_response_items_item_errors_item_type import (
        PipelineListRecentPipelinesResponseItemsItemErrorsItemType,
    )
    from .pipeline_list_recent_pipelines_response_items_item_state import (
        PipelineListRecentPipelinesResponseItemsItemState,
    )
    from .pipeline_list_recent_pipelines_response_items_item_trigger import (
        PipelineListRecentPipelinesResponseItemsItemTrigger,
    )
    from .pipeline_list_recent_pipelines_response_items_item_trigger_actor import (
        PipelineListRecentPipelinesResponseItemsItemTriggerActor,
    )
    from .pipeline_list_recent_pipelines_response_items_item_trigger_parameters_value import (
        PipelineListRecentPipelinesResponseItemsItemTriggerParametersValue,
    )
    from .pipeline_list_recent_pipelines_response_items_item_trigger_type import (
        PipelineListRecentPipelinesResponseItemsItemTriggerType,
    )
    from .pipeline_list_recent_pipelines_response_items_item_vcs import PipelineListRecentPipelinesResponseItemsItemVcs
    from .pipeline_list_recent_pipelines_response_items_item_vcs_commit import (
        PipelineListRecentPipelinesResponseItemsItemVcsCommit,
    )
    from .pipeline_list_recent_pipelinesdefault_response import PipelineListRecentPipelinesdefaultResponse
    from .pipeline_list_user_pipelines_response import PipelineListUserPipelinesResponse
    from .pipeline_list_user_pipelines_response_items_item import PipelineListUserPipelinesResponseItemsItem
    from .pipeline_list_user_pipelines_response_items_item_errors_item import (
        PipelineListUserPipelinesResponseItemsItemErrorsItem,
    )
    from .pipeline_list_user_pipelines_response_items_item_errors_item_type import (
        PipelineListUserPipelinesResponseItemsItemErrorsItemType,
    )
    from .pipeline_list_user_pipelines_response_items_item_state import PipelineListUserPipelinesResponseItemsItemState
    from .pipeline_list_user_pipelines_response_items_item_trigger import (
        PipelineListUserPipelinesResponseItemsItemTrigger,
    )
    from .pipeline_list_user_pipelines_response_items_item_trigger_actor import (
        PipelineListUserPipelinesResponseItemsItemTriggerActor,
    )
    from .pipeline_list_user_pipelines_response_items_item_trigger_parameters_value import (
        PipelineListUserPipelinesResponseItemsItemTriggerParametersValue,
    )
    from .pipeline_list_user_pipelines_response_items_item_trigger_type import (
        PipelineListUserPipelinesResponseItemsItemTriggerType,
    )
    from .pipeline_list_user_pipelines_response_items_item_vcs import PipelineListUserPipelinesResponseItemsItemVcs
    from .pipeline_list_user_pipelines_response_items_item_vcs_commit import (
        PipelineListUserPipelinesResponseItemsItemVcsCommit,
    )
    from .pipeline_list_user_pipelinesdefault_response import PipelineListUserPipelinesdefaultResponse
    from .pipeline_list_workflows_response import PipelineListWorkflowsResponse
    from .pipeline_list_workflows_response_items_item import PipelineListWorkflowsResponseItemsItem
    from .pipeline_list_workflows_response_items_item_status import PipelineListWorkflowsResponseItemsItemStatus
    from .pipeline_list_workflows_response_items_item_tag import PipelineListWorkflowsResponseItemsItemTag
    from .pipeline_list_workflowsdefault_response import PipelineListWorkflowsdefaultResponse
    from .pipeline_trigger_new_pipeline_response import PipelineTriggerNewPipelineResponse
    from .pipeline_trigger_new_pipeline_response_state import PipelineTriggerNewPipelineResponseState
    from .pipeline_trigger_new_pipelinedefault_response import PipelineTriggerNewPipelinedefaultResponse
    from .policy import Policy
    from .policy_bundle import PolicyBundle
    from .policy_management_create_policy_bundle_for_context_response import (
        PolicyManagementCreatePolicyBundleForContextResponse,
    )
    from .policy_management_evaluate_input_data401response import PolicyManagementEvaluateInputData401Response
    from .policy_management_evaluate_input_data500response import PolicyManagementEvaluateInputData500Response
    from .policy_management_evaluate_input_data_response import PolicyManagementEvaluateInputDataResponse
    from .policy_management_get_decision_audit_log_by_given_id_response import (
        PolicyManagementGetDecisionAuditLogByGivenIdResponse,
    )
    from .policy_management_get_decision_audit_logs401response import PolicyManagementGetDecisionAuditLogs401Response
    from .policy_management_get_decision_audit_logs500response import PolicyManagementGetDecisionAuditLogs500Response
    from .policy_management_get_decision_audit_logs_response import PolicyManagementGetDecisionAuditLogsResponse
    from .policy_management_get_document_response import PolicyManagementGetDocumentResponse
    from .policy_management_get_policy_bundle_for_decision_response import (
        PolicyManagementGetPolicyBundleForDecisionResponse,
    )
    from .project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse
    from .project_create_checkout_key_response_type import ProjectCreateCheckoutKeyResponseType
    from .project_create_checkout_keydefault_response import ProjectCreateCheckoutKeydefaultResponse
    from .project_create_env_var_response import ProjectCreateEnvVarResponse
    from .project_create_env_vardefault_response import ProjectCreateEnvVardefaultResponse
    from .project_create_project_default_settings403response import ProjectCreateProjectDefaultSettings403Response
    from .project_create_project_default_settings404response import ProjectCreateProjectDefaultSettings404Response
    from .project_create_project_default_settings405response import ProjectCreateProjectDefaultSettings405Response
    from .project_create_project_default_settings_response import ProjectCreateProjectDefaultSettingsResponse
    from .project_delete_checkout_key_by_fingerprint_response import ProjectDeleteCheckoutKeyByFingerprintResponse
    from .project_delete_checkout_key_by_fingerprintdefault_response import (
        ProjectDeleteCheckoutKeyByFingerprintdefaultResponse,
    )
    from .project_delete_environment_variable_response import ProjectDeleteEnvironmentVariableResponse
    from .project_delete_environment_variabledefault_response import ProjectDeleteEnvironmentVariabledefaultResponse
    from .project_get_by_slug_response import ProjectGetBySlugResponse
    from .project_get_by_slug_response_vcs_info import ProjectGetBySlugResponseVcsInfo
    from .project_get_by_slug_response_vcs_info_provider import ProjectGetBySlugResponseVcsInfoProvider
    from .project_get_by_slugdefault_response import ProjectGetBySlugdefaultResponse
    from .project_get_checkout_key_by_fingerprint_response import ProjectGetCheckoutKeyByFingerprintResponse
    from .project_get_checkout_key_by_fingerprint_response_type import ProjectGetCheckoutKeyByFingerprintResponseType
    from .project_get_checkout_key_by_fingerprintdefault_response import (
        ProjectGetCheckoutKeyByFingerprintdefaultResponse,
    )
    from .project_get_masked_env_var_response import ProjectGetMaskedEnvVarResponse
    from .project_get_masked_env_vardefault_response import ProjectGetMaskedEnvVardefaultResponse
    from .project_get_settings_response import ProjectGetSettingsResponse
    from .project_list_checkout_keys_response import ProjectListCheckoutKeysResponse
    from .project_list_checkout_keys_response_items_item import ProjectListCheckoutKeysResponseItemsItem
    from .project_list_checkout_keys_response_items_item_type import ProjectListCheckoutKeysResponseItemsItemType
    from .project_list_checkout_keysdefault_response import ProjectListCheckoutKeysdefaultResponse
    from .project_list_env_var_values_response import ProjectListEnvVarValuesResponse
    from .project_list_env_var_values_response_items_item import ProjectListEnvVarValuesResponseItemsItem
    from .project_list_env_var_valuesdefault_response import ProjectListEnvVarValuesdefaultResponse
    from .project_settings import ProjectSettings
    from .project_settings_advanced import ProjectSettingsAdvanced
    from .project_update_settings_response import ProjectUpdateSettingsResponse
    from .restriction_created import RestrictionCreated
    from .restriction_created_restriction_type import RestrictionCreatedRestrictionType
    from .restriction_deleted import RestrictionDeleted
    from .schedule_create_new_schedule_response import ScheduleCreateNewScheduleResponse
    from .schedule_create_new_schedule_response_actor import ScheduleCreateNewScheduleResponseActor
    from .schedule_create_new_schedule_response_parameters_value import ScheduleCreateNewScheduleResponseParametersValue
    from .schedule_create_new_schedule_response_timetable import ScheduleCreateNewScheduleResponseTimetable
    from .schedule_create_new_schedule_response_timetable_one import ScheduleCreateNewScheduleResponseTimetableOne
    from .schedule_create_new_schedule_response_timetable_one_days_of_week_item import (
        ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem,
    )
    from .schedule_create_new_schedule_response_timetable_one_months_item import (
        ScheduleCreateNewScheduleResponseTimetableOneMonthsItem,
    )
    from .schedule_create_new_schedule_response_timetable_zero import ScheduleCreateNewScheduleResponseTimetableZero
    from .schedule_create_new_schedule_response_timetable_zero_days_of_week_item import (
        ScheduleCreateNewScheduleResponseTimetableZeroDaysOfWeekItem,
    )
    from .schedule_create_new_schedule_response_timetable_zero_months_item import (
        ScheduleCreateNewScheduleResponseTimetableZeroMonthsItem,
    )
    from .schedule_create_new_scheduledefault_response import ScheduleCreateNewScheduledefaultResponse
    from .schedule_get_all_schedules_response import ScheduleGetAllSchedulesResponse
    from .schedule_get_all_schedules_response_items_item import ScheduleGetAllSchedulesResponseItemsItem
    from .schedule_get_all_schedules_response_items_item_actor import ScheduleGetAllSchedulesResponseItemsItemActor
    from .schedule_get_all_schedules_response_items_item_parameters_value import (
        ScheduleGetAllSchedulesResponseItemsItemParametersValue,
    )
    from .schedule_get_all_schedules_response_items_item_timetable import (
        ScheduleGetAllSchedulesResponseItemsItemTimetable,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_one import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableOne,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_one_days_of_week_item import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableOneDaysOfWeekItem,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_one_months_item import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableOneMonthsItem,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_zero import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableZero,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_zero_days_of_week_item import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableZeroDaysOfWeekItem,
    )
    from .schedule_get_all_schedules_response_items_item_timetable_zero_months_item import (
        ScheduleGetAllSchedulesResponseItemsItemTimetableZeroMonthsItem,
    )
    from .schedule_get_all_schedulesdefault_response import ScheduleGetAllSchedulesdefaultResponse
    from .schedule_get_by_id_response import ScheduleGetByIdResponse
    from .schedule_get_by_id_response_actor import ScheduleGetByIdResponseActor
    from .schedule_get_by_id_response_parameters_value import ScheduleGetByIdResponseParametersValue
    from .schedule_get_by_id_response_timetable import ScheduleGetByIdResponseTimetable
    from .schedule_get_by_id_response_timetable_one import ScheduleGetByIdResponseTimetableOne
    from .schedule_get_by_id_response_timetable_one_days_of_week_item import (
        ScheduleGetByIdResponseTimetableOneDaysOfWeekItem,
    )
    from .schedule_get_by_id_response_timetable_one_months_item import ScheduleGetByIdResponseTimetableOneMonthsItem
    from .schedule_get_by_id_response_timetable_zero import ScheduleGetByIdResponseTimetableZero
    from .schedule_get_by_id_response_timetable_zero_days_of_week_item import (
        ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem,
    )
    from .schedule_get_by_id_response_timetable_zero_months_item import ScheduleGetByIdResponseTimetableZeroMonthsItem
    from .schedule_get_by_iddefault_response import ScheduleGetByIddefaultResponse
    from .schedule_remove_by_id_response import ScheduleRemoveByIdResponse
    from .schedule_remove_by_iddefault_response import ScheduleRemoveByIddefaultResponse
    from .schedule_update_schedule_response import ScheduleUpdateScheduleResponse
    from .schedule_update_schedule_response_actor import ScheduleUpdateScheduleResponseActor
    from .schedule_update_schedule_response_parameters_value import ScheduleUpdateScheduleResponseParametersValue
    from .schedule_update_schedule_response_timetable import ScheduleUpdateScheduleResponseTimetable
    from .schedule_update_schedule_response_timetable_one import ScheduleUpdateScheduleResponseTimetableOne
    from .schedule_update_schedule_response_timetable_one_days_of_week_item import (
        ScheduleUpdateScheduleResponseTimetableOneDaysOfWeekItem,
    )
    from .schedule_update_schedule_response_timetable_one_months_item import (
        ScheduleUpdateScheduleResponseTimetableOneMonthsItem,
    )
    from .schedule_update_schedule_response_timetable_zero import ScheduleUpdateScheduleResponseTimetableZero
    from .schedule_update_schedule_response_timetable_zero_days_of_week_item import (
        ScheduleUpdateScheduleResponseTimetableZeroDaysOfWeekItem,
    )
    from .schedule_update_schedule_response_timetable_zero_months_item import (
        ScheduleUpdateScheduleResponseTimetableZeroMonthsItem,
    )
    from .schedule_update_scheduledefault_response import ScheduleUpdateScheduledefaultResponse
    from .user_get_information_response import UserGetInformationResponse
    from .user_get_informationdefault_response import UserGetInformationdefaultResponse
    from .user_get_user_information_response import UserGetUserInformationResponse
    from .user_get_user_informationdefault_response import UserGetUserInformationdefaultResponse
    from .user_list_collaborations_response import UserListCollaborationsResponse
    from .user_list_collaborations_response_item import UserListCollaborationsResponseItem
    from .user_list_collaborationsdefault_response import UserListCollaborationsdefaultResponse
    from .violation import Violation
    from .webhook_create_outbound_webhook_response import WebhookCreateOutboundWebhookResponse
    from .webhook_create_outbound_webhook_response_events_item import WebhookCreateOutboundWebhookResponseEventsItem
    from .webhook_create_outbound_webhook_response_scope import WebhookCreateOutboundWebhookResponseScope
    from .webhook_create_outbound_webhookdefault_response import WebhookCreateOutboundWebhookdefaultResponse
    from .webhook_delete_outbound_webhook_response import WebhookDeleteOutboundWebhookResponse
    from .webhook_delete_outbound_webhookdefault_response import WebhookDeleteOutboundWebhookdefaultResponse
    from .webhook_get_by_id_response import WebhookGetByIdResponse
    from .webhook_get_by_id_response_events_item import WebhookGetByIdResponseEventsItem
    from .webhook_get_by_id_response_scope import WebhookGetByIdResponseScope
    from .webhook_get_by_iddefault_response import WebhookGetByIddefaultResponse
    from .webhook_list_matching_scope_response import WebhookListMatchingScopeResponse
    from .webhook_list_matching_scope_response_items_item import WebhookListMatchingScopeResponseItemsItem
    from .webhook_list_matching_scope_response_items_item_events_item import (
        WebhookListMatchingScopeResponseItemsItemEventsItem,
    )
    from .webhook_list_matching_scope_response_items_item_scope import WebhookListMatchingScopeResponseItemsItemScope
    from .webhook_list_matching_scopedefault_response import WebhookListMatchingScopedefaultResponse
    from .webhook_update_outbound_webhook_response import WebhookUpdateOutboundWebhookResponse
    from .webhook_update_outbound_webhook_response_events_item import WebhookUpdateOutboundWebhookResponseEventsItem
    from .webhook_update_outbound_webhook_response_scope import WebhookUpdateOutboundWebhookResponseScope
    from .webhook_update_outbound_webhookdefault_response import WebhookUpdateOutboundWebhookdefaultResponse
    from .workflow_approve_job_response import WorkflowApproveJobResponse
    from .workflow_approve_jobdefault_response import WorkflowApproveJobdefaultResponse
    from .workflow_cancel_workflow_response import WorkflowCancelWorkflowResponse
    from .workflow_cancel_workflowdefault_response import WorkflowCancelWorkflowdefaultResponse
    from .workflow_get_by_id_response import WorkflowGetByIdResponse
    from .workflow_get_by_id_response_status import WorkflowGetByIdResponseStatus
    from .workflow_get_by_id_response_tag import WorkflowGetByIdResponseTag
    from .workflow_get_by_iddefault_response import WorkflowGetByIddefaultResponse
    from .workflow_get_jobs_response import WorkflowGetJobsResponse
    from .workflow_get_jobs_response_items_item import WorkflowGetJobsResponseItemsItem
    from .workflow_get_jobs_response_items_item_status import WorkflowGetJobsResponseItemsItemStatus
    from .workflow_get_jobs_response_items_item_type import WorkflowGetJobsResponseItemsItemType
    from .workflow_get_jobsdefault_response import WorkflowGetJobsdefaultResponse
    from .workflow_rerun_workflow_response import WorkflowRerunWorkflowResponse
    from .workflow_rerun_workflowdefault_response import WorkflowRerunWorkflowdefaultResponse
_dynamic_imports: typing.Dict[str, str] = {
    "BundleDiff": ".bundle_diff",
    "ClaimResponse": ".claim_response",
    "ContextCreateNewContextResponse": ".context_create_new_context_response",
    "ContextCreateNewContextdefaultResponse": ".context_create_new_contextdefault_response",
    "ContextCreateRestriction409Response": ".context_create_restriction409response",
    "ContextCreateRestrictionResponse": ".context_create_restriction_response",
    "ContextDeleteRestrictionResponse": ".context_delete_restriction_response",
    "ContextGetInformationResponse": ".context_get_information_response",
    "ContextGetInformationdefaultResponse": ".context_get_informationdefault_response",
    "ContextGetRestrictions401Response": ".context_get_restrictions401response",
    "ContextGetRestrictions404Response": ".context_get_restrictions404response",
    "ContextGetRestrictions429Response": ".context_get_restrictions429response",
    "ContextGetRestrictions500Response": ".context_get_restrictions500response",
    "ContextGetRestrictionsResponse": ".context_get_restrictions_response",
    "ContextListEnvironmentVariablesResponse": ".context_list_environment_variables_response",
    "ContextListEnvironmentVariablesResponseItemsItem": ".context_list_environment_variables_response_items_item",
    "ContextListEnvironmentVariablesdefaultResponse": ".context_list_environment_variablesdefault_response",
    "ContextListOwnerContextsResponse": ".context_list_owner_contexts_response",
    "ContextListOwnerContextsResponseItemsItem": ".context_list_owner_contexts_response_items_item",
    "ContextListOwnerContextsdefaultResponse": ".context_list_owner_contextsdefault_response",
    "ContextProjectRestrictionsList": ".context_project_restrictions_list",
    "ContextProjectRestrictionsListItemsItem": ".context_project_restrictions_list_items_item",
    "ContextProjectRestrictionsListItemsItemRestrictionType": ".context_project_restrictions_list_items_item_restriction_type",
    "ContextRemoveContextResponse": ".context_remove_context_response",
    "ContextRemoveContextdefaultResponse": ".context_remove_contextdefault_response",
    "ContextRemoveEnvironmentVariableResponse": ".context_remove_environment_variable_response",
    "ContextRemoveEnvironmentVariabledefaultResponse": ".context_remove_environment_variabledefault_response",
    "ContextUpdateEnvironmentVariableResponse": ".context_update_environment_variable_response",
    "ContextUpdateEnvironmentVariableResponseContextId": ".context_update_environment_variable_response_context_id",
    "ContextUpdateEnvironmentVariableResponseMessage": ".context_update_environment_variable_response_message",
    "ContextUpdateEnvironmentVariabledefaultResponse": ".context_update_environment_variabledefault_response",
    "Decision": ".decision",
    "DecisionLog": ".decision_log",
    "DecisionLogMetadata": ".decision_log_metadata",
    "DecisionLogMetadataVcs": ".decision_log_metadata_vcs",
    "DecisionSettings": ".decision_settings",
    "InsightsGetFlakyTestsResponse": ".insights_get_flaky_tests_response",
    "InsightsGetFlakyTestsResponseFlakyTestsItem": ".insights_get_flaky_tests_response_flaky_tests_item",
    "InsightsGetFlakyTestsResponseFlakyTestsItemJobNumber": ".insights_get_flaky_tests_response_flaky_tests_item_job_number",
    "InsightsGetFlakyTestsResponseFlakyTestsItemPipelineNumber": ".insights_get_flaky_tests_response_flaky_tests_item_pipeline_number",
    "InsightsGetFlakyTestsResponseFlakyTestsItemTimeWasted": ".insights_get_flaky_tests_response_flaky_tests_item_time_wasted",
    "InsightsGetFlakyTestsdefaultResponse": ".insights_get_flaky_testsdefault_response",
    "InsightsGetJobTimeseriesDataResponse": ".insights_get_job_timeseries_data_response",
    "InsightsGetJobTimeseriesDataResponseItemsItem": ".insights_get_job_timeseries_data_response_items_item",
    "InsightsGetJobTimeseriesDataResponseItemsItemMetrics": ".insights_get_job_timeseries_data_response_items_item_metrics",
    "InsightsGetJobTimeseriesDataResponseItemsItemMetricsDurationMetrics": ".insights_get_job_timeseries_data_response_items_item_metrics_duration_metrics",
    "InsightsGetJobTimeseriesDatadefaultResponse": ".insights_get_job_timeseries_datadefault_response",
    "InsightsGetProjectSummaryMetricsResponse": ".insights_get_project_summary_metrics_response",
    "InsightsGetProjectSummaryMetricsResponseProjectData": ".insights_get_project_summary_metrics_response_project_data",
    "InsightsGetProjectSummaryMetricsResponseProjectDataMetrics": ".insights_get_project_summary_metrics_response_project_data_metrics",
    "InsightsGetProjectSummaryMetricsResponseProjectDataTrends": ".insights_get_project_summary_metrics_response_project_data_trends",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem": ".insights_get_project_summary_metrics_response_project_workflow_branch_data_item",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics": ".insights_get_project_summary_metrics_response_project_workflow_branch_data_item_metrics",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends": ".insights_get_project_summary_metrics_response_project_workflow_branch_data_item_trends",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem": ".insights_get_project_summary_metrics_response_project_workflow_data_item",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemMetrics": ".insights_get_project_summary_metrics_response_project_workflow_data_item_metrics",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemTrends": ".insights_get_project_summary_metrics_response_project_workflow_data_item_trends",
    "InsightsGetProjectSummaryMetricsdefaultResponse": ".insights_get_project_summary_metricsdefault_response",
    "InsightsGetProjectWorkflowJobMetricsResponse": ".insights_get_project_workflow_job_metrics_response",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItem": ".insights_get_project_workflow_job_metrics_response_items_item",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics": ".insights_get_project_workflow_job_metrics_response_items_item_metrics",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics": ".insights_get_project_workflow_job_metrics_response_items_item_metrics_duration_metrics",
    "InsightsGetProjectWorkflowJobMetricsdefaultResponse": ".insights_get_project_workflow_job_metricsdefault_response",
    "InsightsGetProjectWorkflowMetricsResponse": ".insights_get_project_workflow_metrics_response",
    "InsightsGetProjectWorkflowMetricsResponseItemsItem": ".insights_get_project_workflow_metrics_response_items_item",
    "InsightsGetProjectWorkflowMetricsResponseItemsItemMetrics": ".insights_get_project_workflow_metrics_response_items_item_metrics",
    "InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics": ".insights_get_project_workflow_metrics_response_items_item_metrics_duration_metrics",
    "InsightsGetProjectWorkflowMetricsdefaultResponse": ".insights_get_project_workflow_metricsdefault_response",
    "InsightsGetProjectWorkflowTestMetricsResponse": ".insights_get_project_workflow_test_metrics_response",
    "InsightsGetProjectWorkflowTestMetricsResponseMostFailedTestsItem": ".insights_get_project_workflow_test_metrics_response_most_failed_tests_item",
    "InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem": ".insights_get_project_workflow_test_metrics_response_slowest_tests_item",
    "InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem": ".insights_get_project_workflow_test_metrics_response_test_runs_item",
    "InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts": ".insights_get_project_workflow_test_metrics_response_test_runs_item_test_counts",
    "InsightsGetProjectWorkflowTestMetricsdefaultResponse": ".insights_get_project_workflow_test_metricsdefault_response",
    "InsightsGetRecentWorkflowRunsResponse": ".insights_get_recent_workflow_runs_response",
    "InsightsGetRecentWorkflowRunsResponseItemsItem": ".insights_get_recent_workflow_runs_response_items_item",
    "InsightsGetRecentWorkflowRunsResponseItemsItemStatus": ".insights_get_recent_workflow_runs_response_items_item_status",
    "InsightsGetRecentWorkflowRunsdefaultResponse": ".insights_get_recent_workflow_runsdefault_response",
    "InsightsGetSummaryMetricsWithTrendsResponse": ".insights_get_summary_metrics_with_trends_response",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgData": ".insights_get_summary_metrics_with_trends_response_org_data",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics": ".insights_get_summary_metrics_with_trends_response_org_data_metrics",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends": ".insights_get_summary_metrics_with_trends_response_org_data_trends",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem": ".insights_get_summary_metrics_with_trends_response_org_project_data_item",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics": ".insights_get_summary_metrics_with_trends_response_org_project_data_item_metrics",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends": ".insights_get_summary_metrics_with_trends_response_org_project_data_item_trends",
    "InsightsGetSummaryMetricsWithTrendsdefaultResponse": ".insights_get_summary_metrics_with_trendsdefault_response",
    "InsightsGetWorkflowSummaryMetricsResponse": ".insights_get_workflow_summary_metrics_response",
    "InsightsGetWorkflowSummaryMetricsResponseMetrics": ".insights_get_workflow_summary_metrics_response_metrics",
    "InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics": ".insights_get_workflow_summary_metrics_response_metrics_duration_metrics",
    "InsightsGetWorkflowSummaryMetricsResponseTrends": ".insights_get_workflow_summary_metrics_response_trends",
    "InsightsGetWorkflowSummaryMetricsdefaultResponse": ".insights_get_workflow_summary_metricsdefault_response",
    "InsightsListProjectBranchesResponse": ".insights_list_project_branches_response",
    "InsightsListProjectBranchesdefaultResponse": ".insights_list_project_branchesdefault_response",
    "JobCancelWithNumberResponse": ".job_cancel_with_number_response",
    "JobCancelWithNumberdefaultResponse": ".job_cancel_with_numberdefault_response",
    "JobGetArtifactsResponse": ".job_get_artifacts_response",
    "JobGetArtifactsResponseItemsItem": ".job_get_artifacts_response_items_item",
    "JobGetArtifactsdefaultResponse": ".job_get_artifactsdefault_response",
    "JobGetDetailsResponse": ".job_get_details_response",
    "JobGetDetailsResponseContextsItem": ".job_get_details_response_contexts_item",
    "JobGetDetailsResponseExecutor": ".job_get_details_response_executor",
    "JobGetDetailsResponseLatestWorkflow": ".job_get_details_response_latest_workflow",
    "JobGetDetailsResponseMessagesItem": ".job_get_details_response_messages_item",
    "JobGetDetailsResponseOrganization": ".job_get_details_response_organization",
    "JobGetDetailsResponseParallelRunsItem": ".job_get_details_response_parallel_runs_item",
    "JobGetDetailsResponsePipeline": ".job_get_details_response_pipeline",
    "JobGetDetailsResponseProject": ".job_get_details_response_project",
    "JobGetDetailsResponseStatus": ".job_get_details_response_status",
    "JobGetDetailsdefaultResponse": ".job_get_detailsdefault_response",
    "JobGetTestMetadataResponse": ".job_get_test_metadata_response",
    "JobGetTestMetadataResponseItemsItem": ".job_get_test_metadata_response_items_item",
    "JobGetTestMetadatadefaultResponse": ".job_get_test_metadatadefault_response",
    "JsonDuration": ".json_duration",
    "OidcTokenManagementDeleteOrgClaims403Response": ".oidc_token_management_delete_org_claims403response",
    "OidcTokenManagementDeleteOrgClaims500Response": ".oidc_token_management_delete_org_claims500response",
    "OidcTokenManagementDeleteOrgClaimsResponse": ".oidc_token_management_delete_org_claims_response",
    "PatchClaimsRequest": ".patch_claims_request",
    "PipelineContinueExecutionResponse": ".pipeline_continue_execution_response",
    "PipelineContinueExecutiondefaultResponse": ".pipeline_continue_executiondefault_response",
    "PipelineGetAllPipelinesResponse": ".pipeline_get_all_pipelines_response",
    "PipelineGetAllPipelinesResponseItemsItem": ".pipeline_get_all_pipelines_response_items_item",
    "PipelineGetAllPipelinesResponseItemsItemErrorsItem": ".pipeline_get_all_pipelines_response_items_item_errors_item",
    "PipelineGetAllPipelinesResponseItemsItemErrorsItemType": ".pipeline_get_all_pipelines_response_items_item_errors_item_type",
    "PipelineGetAllPipelinesResponseItemsItemState": ".pipeline_get_all_pipelines_response_items_item_state",
    "PipelineGetAllPipelinesResponseItemsItemTrigger": ".pipeline_get_all_pipelines_response_items_item_trigger",
    "PipelineGetAllPipelinesResponseItemsItemTriggerActor": ".pipeline_get_all_pipelines_response_items_item_trigger_actor",
    "PipelineGetAllPipelinesResponseItemsItemTriggerParametersValue": ".pipeline_get_all_pipelines_response_items_item_trigger_parameters_value",
    "PipelineGetAllPipelinesResponseItemsItemTriggerType": ".pipeline_get_all_pipelines_response_items_item_trigger_type",
    "PipelineGetAllPipelinesResponseItemsItemVcs": ".pipeline_get_all_pipelines_response_items_item_vcs",
    "PipelineGetAllPipelinesResponseItemsItemVcsCommit": ".pipeline_get_all_pipelines_response_items_item_vcs_commit",
    "PipelineGetAllPipelinesdefaultResponse": ".pipeline_get_all_pipelinesdefault_response",
    "PipelineGetByIdResponse": ".pipeline_get_by_id_response",
    "PipelineGetByIdResponseErrorsItem": ".pipeline_get_by_id_response_errors_item",
    "PipelineGetByIdResponseErrorsItemType": ".pipeline_get_by_id_response_errors_item_type",
    "PipelineGetByIdResponseState": ".pipeline_get_by_id_response_state",
    "PipelineGetByIdResponseTrigger": ".pipeline_get_by_id_response_trigger",
    "PipelineGetByIdResponseTriggerActor": ".pipeline_get_by_id_response_trigger_actor",
    "PipelineGetByIdResponseTriggerParametersValue": ".pipeline_get_by_id_response_trigger_parameters_value",
    "PipelineGetByIdResponseTriggerType": ".pipeline_get_by_id_response_trigger_type",
    "PipelineGetByIdResponseVcs": ".pipeline_get_by_id_response_vcs",
    "PipelineGetByIdResponseVcsCommit": ".pipeline_get_by_id_response_vcs_commit",
    "PipelineGetByIddefaultResponse": ".pipeline_get_by_iddefault_response",
    "PipelineGetByNumberResponse": ".pipeline_get_by_number_response",
    "PipelineGetByNumberResponseErrorsItem": ".pipeline_get_by_number_response_errors_item",
    "PipelineGetByNumberResponseErrorsItemType": ".pipeline_get_by_number_response_errors_item_type",
    "PipelineGetByNumberResponseState": ".pipeline_get_by_number_response_state",
    "PipelineGetByNumberResponseTrigger": ".pipeline_get_by_number_response_trigger",
    "PipelineGetByNumberResponseTriggerActor": ".pipeline_get_by_number_response_trigger_actor",
    "PipelineGetByNumberResponseTriggerParametersValue": ".pipeline_get_by_number_response_trigger_parameters_value",
    "PipelineGetByNumberResponseTriggerType": ".pipeline_get_by_number_response_trigger_type",
    "PipelineGetByNumberResponseVcs": ".pipeline_get_by_number_response_vcs",
    "PipelineGetByNumberResponseVcsCommit": ".pipeline_get_by_number_response_vcs_commit",
    "PipelineGetByNumberdefaultResponse": ".pipeline_get_by_numberdefault_response",
    "PipelineGetConfigurationByIdResponse": ".pipeline_get_configuration_by_id_response",
    "PipelineGetConfigurationByIddefaultResponse": ".pipeline_get_configuration_by_iddefault_response",
    "PipelineListRecentPipelinesResponse": ".pipeline_list_recent_pipelines_response",
    "PipelineListRecentPipelinesResponseItemsItem": ".pipeline_list_recent_pipelines_response_items_item",
    "PipelineListRecentPipelinesResponseItemsItemErrorsItem": ".pipeline_list_recent_pipelines_response_items_item_errors_item",
    "PipelineListRecentPipelinesResponseItemsItemErrorsItemType": ".pipeline_list_recent_pipelines_response_items_item_errors_item_type",
    "PipelineListRecentPipelinesResponseItemsItemState": ".pipeline_list_recent_pipelines_response_items_item_state",
    "PipelineListRecentPipelinesResponseItemsItemTrigger": ".pipeline_list_recent_pipelines_response_items_item_trigger",
    "PipelineListRecentPipelinesResponseItemsItemTriggerActor": ".pipeline_list_recent_pipelines_response_items_item_trigger_actor",
    "PipelineListRecentPipelinesResponseItemsItemTriggerParametersValue": ".pipeline_list_recent_pipelines_response_items_item_trigger_parameters_value",
    "PipelineListRecentPipelinesResponseItemsItemTriggerType": ".pipeline_list_recent_pipelines_response_items_item_trigger_type",
    "PipelineListRecentPipelinesResponseItemsItemVcs": ".pipeline_list_recent_pipelines_response_items_item_vcs",
    "PipelineListRecentPipelinesResponseItemsItemVcsCommit": ".pipeline_list_recent_pipelines_response_items_item_vcs_commit",
    "PipelineListRecentPipelinesdefaultResponse": ".pipeline_list_recent_pipelinesdefault_response",
    "PipelineListUserPipelinesResponse": ".pipeline_list_user_pipelines_response",
    "PipelineListUserPipelinesResponseItemsItem": ".pipeline_list_user_pipelines_response_items_item",
    "PipelineListUserPipelinesResponseItemsItemErrorsItem": ".pipeline_list_user_pipelines_response_items_item_errors_item",
    "PipelineListUserPipelinesResponseItemsItemErrorsItemType": ".pipeline_list_user_pipelines_response_items_item_errors_item_type",
    "PipelineListUserPipelinesResponseItemsItemState": ".pipeline_list_user_pipelines_response_items_item_state",
    "PipelineListUserPipelinesResponseItemsItemTrigger": ".pipeline_list_user_pipelines_response_items_item_trigger",
    "PipelineListUserPipelinesResponseItemsItemTriggerActor": ".pipeline_list_user_pipelines_response_items_item_trigger_actor",
    "PipelineListUserPipelinesResponseItemsItemTriggerParametersValue": ".pipeline_list_user_pipelines_response_items_item_trigger_parameters_value",
    "PipelineListUserPipelinesResponseItemsItemTriggerType": ".pipeline_list_user_pipelines_response_items_item_trigger_type",
    "PipelineListUserPipelinesResponseItemsItemVcs": ".pipeline_list_user_pipelines_response_items_item_vcs",
    "PipelineListUserPipelinesResponseItemsItemVcsCommit": ".pipeline_list_user_pipelines_response_items_item_vcs_commit",
    "PipelineListUserPipelinesdefaultResponse": ".pipeline_list_user_pipelinesdefault_response",
    "PipelineListWorkflowsResponse": ".pipeline_list_workflows_response",
    "PipelineListWorkflowsResponseItemsItem": ".pipeline_list_workflows_response_items_item",
    "PipelineListWorkflowsResponseItemsItemStatus": ".pipeline_list_workflows_response_items_item_status",
    "PipelineListWorkflowsResponseItemsItemTag": ".pipeline_list_workflows_response_items_item_tag",
    "PipelineListWorkflowsdefaultResponse": ".pipeline_list_workflowsdefault_response",
    "PipelineTriggerNewPipelineResponse": ".pipeline_trigger_new_pipeline_response",
    "PipelineTriggerNewPipelineResponseState": ".pipeline_trigger_new_pipeline_response_state",
    "PipelineTriggerNewPipelinedefaultResponse": ".pipeline_trigger_new_pipelinedefault_response",
    "Policy": ".policy",
    "PolicyBundle": ".policy_bundle",
    "PolicyManagementCreatePolicyBundleForContextResponse": ".policy_management_create_policy_bundle_for_context_response",
    "PolicyManagementEvaluateInputData401Response": ".policy_management_evaluate_input_data401response",
    "PolicyManagementEvaluateInputData500Response": ".policy_management_evaluate_input_data500response",
    "PolicyManagementEvaluateInputDataResponse": ".policy_management_evaluate_input_data_response",
    "PolicyManagementGetDecisionAuditLogByGivenIdResponse": ".policy_management_get_decision_audit_log_by_given_id_response",
    "PolicyManagementGetDecisionAuditLogs401Response": ".policy_management_get_decision_audit_logs401response",
    "PolicyManagementGetDecisionAuditLogs500Response": ".policy_management_get_decision_audit_logs500response",
    "PolicyManagementGetDecisionAuditLogsResponse": ".policy_management_get_decision_audit_logs_response",
    "PolicyManagementGetDocumentResponse": ".policy_management_get_document_response",
    "PolicyManagementGetPolicyBundleForDecisionResponse": ".policy_management_get_policy_bundle_for_decision_response",
    "ProjectCreateCheckoutKeyResponse": ".project_create_checkout_key_response",
    "ProjectCreateCheckoutKeyResponseType": ".project_create_checkout_key_response_type",
    "ProjectCreateCheckoutKeydefaultResponse": ".project_create_checkout_keydefault_response",
    "ProjectCreateEnvVarResponse": ".project_create_env_var_response",
    "ProjectCreateEnvVardefaultResponse": ".project_create_env_vardefault_response",
    "ProjectCreateProjectDefaultSettings403Response": ".project_create_project_default_settings403response",
    "ProjectCreateProjectDefaultSettings404Response": ".project_create_project_default_settings404response",
    "ProjectCreateProjectDefaultSettings405Response": ".project_create_project_default_settings405response",
    "ProjectCreateProjectDefaultSettingsResponse": ".project_create_project_default_settings_response",
    "ProjectDeleteCheckoutKeyByFingerprintResponse": ".project_delete_checkout_key_by_fingerprint_response",
    "ProjectDeleteCheckoutKeyByFingerprintdefaultResponse": ".project_delete_checkout_key_by_fingerprintdefault_response",
    "ProjectDeleteEnvironmentVariableResponse": ".project_delete_environment_variable_response",
    "ProjectDeleteEnvironmentVariabledefaultResponse": ".project_delete_environment_variabledefault_response",
    "ProjectGetBySlugResponse": ".project_get_by_slug_response",
    "ProjectGetBySlugResponseVcsInfo": ".project_get_by_slug_response_vcs_info",
    "ProjectGetBySlugResponseVcsInfoProvider": ".project_get_by_slug_response_vcs_info_provider",
    "ProjectGetBySlugdefaultResponse": ".project_get_by_slugdefault_response",
    "ProjectGetCheckoutKeyByFingerprintResponse": ".project_get_checkout_key_by_fingerprint_response",
    "ProjectGetCheckoutKeyByFingerprintResponseType": ".project_get_checkout_key_by_fingerprint_response_type",
    "ProjectGetCheckoutKeyByFingerprintdefaultResponse": ".project_get_checkout_key_by_fingerprintdefault_response",
    "ProjectGetMaskedEnvVarResponse": ".project_get_masked_env_var_response",
    "ProjectGetMaskedEnvVardefaultResponse": ".project_get_masked_env_vardefault_response",
    "ProjectGetSettingsResponse": ".project_get_settings_response",
    "ProjectListCheckoutKeysResponse": ".project_list_checkout_keys_response",
    "ProjectListCheckoutKeysResponseItemsItem": ".project_list_checkout_keys_response_items_item",
    "ProjectListCheckoutKeysResponseItemsItemType": ".project_list_checkout_keys_response_items_item_type",
    "ProjectListCheckoutKeysdefaultResponse": ".project_list_checkout_keysdefault_response",
    "ProjectListEnvVarValuesResponse": ".project_list_env_var_values_response",
    "ProjectListEnvVarValuesResponseItemsItem": ".project_list_env_var_values_response_items_item",
    "ProjectListEnvVarValuesdefaultResponse": ".project_list_env_var_valuesdefault_response",
    "ProjectSettings": ".project_settings",
    "ProjectSettingsAdvanced": ".project_settings_advanced",
    "ProjectUpdateSettingsResponse": ".project_update_settings_response",
    "RestrictionCreated": ".restriction_created",
    "RestrictionCreatedRestrictionType": ".restriction_created_restriction_type",
    "RestrictionDeleted": ".restriction_deleted",
    "ScheduleCreateNewScheduleResponse": ".schedule_create_new_schedule_response",
    "ScheduleCreateNewScheduleResponseActor": ".schedule_create_new_schedule_response_actor",
    "ScheduleCreateNewScheduleResponseParametersValue": ".schedule_create_new_schedule_response_parameters_value",
    "ScheduleCreateNewScheduleResponseTimetable": ".schedule_create_new_schedule_response_timetable",
    "ScheduleCreateNewScheduleResponseTimetableOne": ".schedule_create_new_schedule_response_timetable_one",
    "ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem": ".schedule_create_new_schedule_response_timetable_one_days_of_week_item",
    "ScheduleCreateNewScheduleResponseTimetableOneMonthsItem": ".schedule_create_new_schedule_response_timetable_one_months_item",
    "ScheduleCreateNewScheduleResponseTimetableZero": ".schedule_create_new_schedule_response_timetable_zero",
    "ScheduleCreateNewScheduleResponseTimetableZeroDaysOfWeekItem": ".schedule_create_new_schedule_response_timetable_zero_days_of_week_item",
    "ScheduleCreateNewScheduleResponseTimetableZeroMonthsItem": ".schedule_create_new_schedule_response_timetable_zero_months_item",
    "ScheduleCreateNewScheduledefaultResponse": ".schedule_create_new_scheduledefault_response",
    "ScheduleGetAllSchedulesResponse": ".schedule_get_all_schedules_response",
    "ScheduleGetAllSchedulesResponseItemsItem": ".schedule_get_all_schedules_response_items_item",
    "ScheduleGetAllSchedulesResponseItemsItemActor": ".schedule_get_all_schedules_response_items_item_actor",
    "ScheduleGetAllSchedulesResponseItemsItemParametersValue": ".schedule_get_all_schedules_response_items_item_parameters_value",
    "ScheduleGetAllSchedulesResponseItemsItemTimetable": ".schedule_get_all_schedules_response_items_item_timetable",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOne": ".schedule_get_all_schedules_response_items_item_timetable_one",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOneDaysOfWeekItem": ".schedule_get_all_schedules_response_items_item_timetable_one_days_of_week_item",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOneMonthsItem": ".schedule_get_all_schedules_response_items_item_timetable_one_months_item",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZero": ".schedule_get_all_schedules_response_items_item_timetable_zero",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZeroDaysOfWeekItem": ".schedule_get_all_schedules_response_items_item_timetable_zero_days_of_week_item",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZeroMonthsItem": ".schedule_get_all_schedules_response_items_item_timetable_zero_months_item",
    "ScheduleGetAllSchedulesdefaultResponse": ".schedule_get_all_schedulesdefault_response",
    "ScheduleGetByIdResponse": ".schedule_get_by_id_response",
    "ScheduleGetByIdResponseActor": ".schedule_get_by_id_response_actor",
    "ScheduleGetByIdResponseParametersValue": ".schedule_get_by_id_response_parameters_value",
    "ScheduleGetByIdResponseTimetable": ".schedule_get_by_id_response_timetable",
    "ScheduleGetByIdResponseTimetableOne": ".schedule_get_by_id_response_timetable_one",
    "ScheduleGetByIdResponseTimetableOneDaysOfWeekItem": ".schedule_get_by_id_response_timetable_one_days_of_week_item",
    "ScheduleGetByIdResponseTimetableOneMonthsItem": ".schedule_get_by_id_response_timetable_one_months_item",
    "ScheduleGetByIdResponseTimetableZero": ".schedule_get_by_id_response_timetable_zero",
    "ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem": ".schedule_get_by_id_response_timetable_zero_days_of_week_item",
    "ScheduleGetByIdResponseTimetableZeroMonthsItem": ".schedule_get_by_id_response_timetable_zero_months_item",
    "ScheduleGetByIddefaultResponse": ".schedule_get_by_iddefault_response",
    "ScheduleRemoveByIdResponse": ".schedule_remove_by_id_response",
    "ScheduleRemoveByIddefaultResponse": ".schedule_remove_by_iddefault_response",
    "ScheduleUpdateScheduleResponse": ".schedule_update_schedule_response",
    "ScheduleUpdateScheduleResponseActor": ".schedule_update_schedule_response_actor",
    "ScheduleUpdateScheduleResponseParametersValue": ".schedule_update_schedule_response_parameters_value",
    "ScheduleUpdateScheduleResponseTimetable": ".schedule_update_schedule_response_timetable",
    "ScheduleUpdateScheduleResponseTimetableOne": ".schedule_update_schedule_response_timetable_one",
    "ScheduleUpdateScheduleResponseTimetableOneDaysOfWeekItem": ".schedule_update_schedule_response_timetable_one_days_of_week_item",
    "ScheduleUpdateScheduleResponseTimetableOneMonthsItem": ".schedule_update_schedule_response_timetable_one_months_item",
    "ScheduleUpdateScheduleResponseTimetableZero": ".schedule_update_schedule_response_timetable_zero",
    "ScheduleUpdateScheduleResponseTimetableZeroDaysOfWeekItem": ".schedule_update_schedule_response_timetable_zero_days_of_week_item",
    "ScheduleUpdateScheduleResponseTimetableZeroMonthsItem": ".schedule_update_schedule_response_timetable_zero_months_item",
    "ScheduleUpdateScheduledefaultResponse": ".schedule_update_scheduledefault_response",
    "UserGetInformationResponse": ".user_get_information_response",
    "UserGetInformationdefaultResponse": ".user_get_informationdefault_response",
    "UserGetUserInformationResponse": ".user_get_user_information_response",
    "UserGetUserInformationdefaultResponse": ".user_get_user_informationdefault_response",
    "UserListCollaborationsResponse": ".user_list_collaborations_response",
    "UserListCollaborationsResponseItem": ".user_list_collaborations_response_item",
    "UserListCollaborationsdefaultResponse": ".user_list_collaborationsdefault_response",
    "Violation": ".violation",
    "WebhookCreateOutboundWebhookResponse": ".webhook_create_outbound_webhook_response",
    "WebhookCreateOutboundWebhookResponseEventsItem": ".webhook_create_outbound_webhook_response_events_item",
    "WebhookCreateOutboundWebhookResponseScope": ".webhook_create_outbound_webhook_response_scope",
    "WebhookCreateOutboundWebhookdefaultResponse": ".webhook_create_outbound_webhookdefault_response",
    "WebhookDeleteOutboundWebhookResponse": ".webhook_delete_outbound_webhook_response",
    "WebhookDeleteOutboundWebhookdefaultResponse": ".webhook_delete_outbound_webhookdefault_response",
    "WebhookGetByIdResponse": ".webhook_get_by_id_response",
    "WebhookGetByIdResponseEventsItem": ".webhook_get_by_id_response_events_item",
    "WebhookGetByIdResponseScope": ".webhook_get_by_id_response_scope",
    "WebhookGetByIddefaultResponse": ".webhook_get_by_iddefault_response",
    "WebhookListMatchingScopeResponse": ".webhook_list_matching_scope_response",
    "WebhookListMatchingScopeResponseItemsItem": ".webhook_list_matching_scope_response_items_item",
    "WebhookListMatchingScopeResponseItemsItemEventsItem": ".webhook_list_matching_scope_response_items_item_events_item",
    "WebhookListMatchingScopeResponseItemsItemScope": ".webhook_list_matching_scope_response_items_item_scope",
    "WebhookListMatchingScopedefaultResponse": ".webhook_list_matching_scopedefault_response",
    "WebhookUpdateOutboundWebhookResponse": ".webhook_update_outbound_webhook_response",
    "WebhookUpdateOutboundWebhookResponseEventsItem": ".webhook_update_outbound_webhook_response_events_item",
    "WebhookUpdateOutboundWebhookResponseScope": ".webhook_update_outbound_webhook_response_scope",
    "WebhookUpdateOutboundWebhookdefaultResponse": ".webhook_update_outbound_webhookdefault_response",
    "WorkflowApproveJobResponse": ".workflow_approve_job_response",
    "WorkflowApproveJobdefaultResponse": ".workflow_approve_jobdefault_response",
    "WorkflowCancelWorkflowResponse": ".workflow_cancel_workflow_response",
    "WorkflowCancelWorkflowdefaultResponse": ".workflow_cancel_workflowdefault_response",
    "WorkflowGetByIdResponse": ".workflow_get_by_id_response",
    "WorkflowGetByIdResponseStatus": ".workflow_get_by_id_response_status",
    "WorkflowGetByIdResponseTag": ".workflow_get_by_id_response_tag",
    "WorkflowGetByIddefaultResponse": ".workflow_get_by_iddefault_response",
    "WorkflowGetJobsResponse": ".workflow_get_jobs_response",
    "WorkflowGetJobsResponseItemsItem": ".workflow_get_jobs_response_items_item",
    "WorkflowGetJobsResponseItemsItemStatus": ".workflow_get_jobs_response_items_item_status",
    "WorkflowGetJobsResponseItemsItemType": ".workflow_get_jobs_response_items_item_type",
    "WorkflowGetJobsdefaultResponse": ".workflow_get_jobsdefault_response",
    "WorkflowRerunWorkflowResponse": ".workflow_rerun_workflow_response",
    "WorkflowRerunWorkflowdefaultResponse": ".workflow_rerun_workflowdefault_response",
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
    "BundleDiff",
    "ClaimResponse",
    "ContextCreateNewContextResponse",
    "ContextCreateNewContextdefaultResponse",
    "ContextCreateRestriction409Response",
    "ContextCreateRestrictionResponse",
    "ContextDeleteRestrictionResponse",
    "ContextGetInformationResponse",
    "ContextGetInformationdefaultResponse",
    "ContextGetRestrictions401Response",
    "ContextGetRestrictions404Response",
    "ContextGetRestrictions429Response",
    "ContextGetRestrictions500Response",
    "ContextGetRestrictionsResponse",
    "ContextListEnvironmentVariablesResponse",
    "ContextListEnvironmentVariablesResponseItemsItem",
    "ContextListEnvironmentVariablesdefaultResponse",
    "ContextListOwnerContextsResponse",
    "ContextListOwnerContextsResponseItemsItem",
    "ContextListOwnerContextsdefaultResponse",
    "ContextProjectRestrictionsList",
    "ContextProjectRestrictionsListItemsItem",
    "ContextProjectRestrictionsListItemsItemRestrictionType",
    "ContextRemoveContextResponse",
    "ContextRemoveContextdefaultResponse",
    "ContextRemoveEnvironmentVariableResponse",
    "ContextRemoveEnvironmentVariabledefaultResponse",
    "ContextUpdateEnvironmentVariableResponse",
    "ContextUpdateEnvironmentVariableResponseContextId",
    "ContextUpdateEnvironmentVariableResponseMessage",
    "ContextUpdateEnvironmentVariabledefaultResponse",
    "Decision",
    "DecisionLog",
    "DecisionLogMetadata",
    "DecisionLogMetadataVcs",
    "DecisionSettings",
    "InsightsGetFlakyTestsResponse",
    "InsightsGetFlakyTestsResponseFlakyTestsItem",
    "InsightsGetFlakyTestsResponseFlakyTestsItemJobNumber",
    "InsightsGetFlakyTestsResponseFlakyTestsItemPipelineNumber",
    "InsightsGetFlakyTestsResponseFlakyTestsItemTimeWasted",
    "InsightsGetFlakyTestsdefaultResponse",
    "InsightsGetJobTimeseriesDataResponse",
    "InsightsGetJobTimeseriesDataResponseItemsItem",
    "InsightsGetJobTimeseriesDataResponseItemsItemMetrics",
    "InsightsGetJobTimeseriesDataResponseItemsItemMetricsDurationMetrics",
    "InsightsGetJobTimeseriesDatadefaultResponse",
    "InsightsGetProjectSummaryMetricsResponse",
    "InsightsGetProjectSummaryMetricsResponseProjectData",
    "InsightsGetProjectSummaryMetricsResponseProjectDataMetrics",
    "InsightsGetProjectSummaryMetricsResponseProjectDataTrends",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemMetrics",
    "InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemTrends",
    "InsightsGetProjectSummaryMetricsdefaultResponse",
    "InsightsGetProjectWorkflowJobMetricsResponse",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItem",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics",
    "InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics",
    "InsightsGetProjectWorkflowJobMetricsdefaultResponse",
    "InsightsGetProjectWorkflowMetricsResponse",
    "InsightsGetProjectWorkflowMetricsResponseItemsItem",
    "InsightsGetProjectWorkflowMetricsResponseItemsItemMetrics",
    "InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics",
    "InsightsGetProjectWorkflowMetricsdefaultResponse",
    "InsightsGetProjectWorkflowTestMetricsResponse",
    "InsightsGetProjectWorkflowTestMetricsResponseMostFailedTestsItem",
    "InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem",
    "InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem",
    "InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts",
    "InsightsGetProjectWorkflowTestMetricsdefaultResponse",
    "InsightsGetRecentWorkflowRunsResponse",
    "InsightsGetRecentWorkflowRunsResponseItemsItem",
    "InsightsGetRecentWorkflowRunsResponseItemsItemStatus",
    "InsightsGetRecentWorkflowRunsdefaultResponse",
    "InsightsGetSummaryMetricsWithTrendsResponse",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgData",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics",
    "InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends",
    "InsightsGetSummaryMetricsWithTrendsdefaultResponse",
    "InsightsGetWorkflowSummaryMetricsResponse",
    "InsightsGetWorkflowSummaryMetricsResponseMetrics",
    "InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics",
    "InsightsGetWorkflowSummaryMetricsResponseTrends",
    "InsightsGetWorkflowSummaryMetricsdefaultResponse",
    "InsightsListProjectBranchesResponse",
    "InsightsListProjectBranchesdefaultResponse",
    "JobCancelWithNumberResponse",
    "JobCancelWithNumberdefaultResponse",
    "JobGetArtifactsResponse",
    "JobGetArtifactsResponseItemsItem",
    "JobGetArtifactsdefaultResponse",
    "JobGetDetailsResponse",
    "JobGetDetailsResponseContextsItem",
    "JobGetDetailsResponseExecutor",
    "JobGetDetailsResponseLatestWorkflow",
    "JobGetDetailsResponseMessagesItem",
    "JobGetDetailsResponseOrganization",
    "JobGetDetailsResponseParallelRunsItem",
    "JobGetDetailsResponsePipeline",
    "JobGetDetailsResponseProject",
    "JobGetDetailsResponseStatus",
    "JobGetDetailsdefaultResponse",
    "JobGetTestMetadataResponse",
    "JobGetTestMetadataResponseItemsItem",
    "JobGetTestMetadatadefaultResponse",
    "JsonDuration",
    "OidcTokenManagementDeleteOrgClaims403Response",
    "OidcTokenManagementDeleteOrgClaims500Response",
    "OidcTokenManagementDeleteOrgClaimsResponse",
    "PatchClaimsRequest",
    "PipelineContinueExecutionResponse",
    "PipelineContinueExecutiondefaultResponse",
    "PipelineGetAllPipelinesResponse",
    "PipelineGetAllPipelinesResponseItemsItem",
    "PipelineGetAllPipelinesResponseItemsItemErrorsItem",
    "PipelineGetAllPipelinesResponseItemsItemErrorsItemType",
    "PipelineGetAllPipelinesResponseItemsItemState",
    "PipelineGetAllPipelinesResponseItemsItemTrigger",
    "PipelineGetAllPipelinesResponseItemsItemTriggerActor",
    "PipelineGetAllPipelinesResponseItemsItemTriggerParametersValue",
    "PipelineGetAllPipelinesResponseItemsItemTriggerType",
    "PipelineGetAllPipelinesResponseItemsItemVcs",
    "PipelineGetAllPipelinesResponseItemsItemVcsCommit",
    "PipelineGetAllPipelinesdefaultResponse",
    "PipelineGetByIdResponse",
    "PipelineGetByIdResponseErrorsItem",
    "PipelineGetByIdResponseErrorsItemType",
    "PipelineGetByIdResponseState",
    "PipelineGetByIdResponseTrigger",
    "PipelineGetByIdResponseTriggerActor",
    "PipelineGetByIdResponseTriggerParametersValue",
    "PipelineGetByIdResponseTriggerType",
    "PipelineGetByIdResponseVcs",
    "PipelineGetByIdResponseVcsCommit",
    "PipelineGetByIddefaultResponse",
    "PipelineGetByNumberResponse",
    "PipelineGetByNumberResponseErrorsItem",
    "PipelineGetByNumberResponseErrorsItemType",
    "PipelineGetByNumberResponseState",
    "PipelineGetByNumberResponseTrigger",
    "PipelineGetByNumberResponseTriggerActor",
    "PipelineGetByNumberResponseTriggerParametersValue",
    "PipelineGetByNumberResponseTriggerType",
    "PipelineGetByNumberResponseVcs",
    "PipelineGetByNumberResponseVcsCommit",
    "PipelineGetByNumberdefaultResponse",
    "PipelineGetConfigurationByIdResponse",
    "PipelineGetConfigurationByIddefaultResponse",
    "PipelineListRecentPipelinesResponse",
    "PipelineListRecentPipelinesResponseItemsItem",
    "PipelineListRecentPipelinesResponseItemsItemErrorsItem",
    "PipelineListRecentPipelinesResponseItemsItemErrorsItemType",
    "PipelineListRecentPipelinesResponseItemsItemState",
    "PipelineListRecentPipelinesResponseItemsItemTrigger",
    "PipelineListRecentPipelinesResponseItemsItemTriggerActor",
    "PipelineListRecentPipelinesResponseItemsItemTriggerParametersValue",
    "PipelineListRecentPipelinesResponseItemsItemTriggerType",
    "PipelineListRecentPipelinesResponseItemsItemVcs",
    "PipelineListRecentPipelinesResponseItemsItemVcsCommit",
    "PipelineListRecentPipelinesdefaultResponse",
    "PipelineListUserPipelinesResponse",
    "PipelineListUserPipelinesResponseItemsItem",
    "PipelineListUserPipelinesResponseItemsItemErrorsItem",
    "PipelineListUserPipelinesResponseItemsItemErrorsItemType",
    "PipelineListUserPipelinesResponseItemsItemState",
    "PipelineListUserPipelinesResponseItemsItemTrigger",
    "PipelineListUserPipelinesResponseItemsItemTriggerActor",
    "PipelineListUserPipelinesResponseItemsItemTriggerParametersValue",
    "PipelineListUserPipelinesResponseItemsItemTriggerType",
    "PipelineListUserPipelinesResponseItemsItemVcs",
    "PipelineListUserPipelinesResponseItemsItemVcsCommit",
    "PipelineListUserPipelinesdefaultResponse",
    "PipelineListWorkflowsResponse",
    "PipelineListWorkflowsResponseItemsItem",
    "PipelineListWorkflowsResponseItemsItemStatus",
    "PipelineListWorkflowsResponseItemsItemTag",
    "PipelineListWorkflowsdefaultResponse",
    "PipelineTriggerNewPipelineResponse",
    "PipelineTriggerNewPipelineResponseState",
    "PipelineTriggerNewPipelinedefaultResponse",
    "Policy",
    "PolicyBundle",
    "PolicyManagementCreatePolicyBundleForContextResponse",
    "PolicyManagementEvaluateInputData401Response",
    "PolicyManagementEvaluateInputData500Response",
    "PolicyManagementEvaluateInputDataResponse",
    "PolicyManagementGetDecisionAuditLogByGivenIdResponse",
    "PolicyManagementGetDecisionAuditLogs401Response",
    "PolicyManagementGetDecisionAuditLogs500Response",
    "PolicyManagementGetDecisionAuditLogsResponse",
    "PolicyManagementGetDocumentResponse",
    "PolicyManagementGetPolicyBundleForDecisionResponse",
    "ProjectCreateCheckoutKeyResponse",
    "ProjectCreateCheckoutKeyResponseType",
    "ProjectCreateCheckoutKeydefaultResponse",
    "ProjectCreateEnvVarResponse",
    "ProjectCreateEnvVardefaultResponse",
    "ProjectCreateProjectDefaultSettings403Response",
    "ProjectCreateProjectDefaultSettings404Response",
    "ProjectCreateProjectDefaultSettings405Response",
    "ProjectCreateProjectDefaultSettingsResponse",
    "ProjectDeleteCheckoutKeyByFingerprintResponse",
    "ProjectDeleteCheckoutKeyByFingerprintdefaultResponse",
    "ProjectDeleteEnvironmentVariableResponse",
    "ProjectDeleteEnvironmentVariabledefaultResponse",
    "ProjectGetBySlugResponse",
    "ProjectGetBySlugResponseVcsInfo",
    "ProjectGetBySlugResponseVcsInfoProvider",
    "ProjectGetBySlugdefaultResponse",
    "ProjectGetCheckoutKeyByFingerprintResponse",
    "ProjectGetCheckoutKeyByFingerprintResponseType",
    "ProjectGetCheckoutKeyByFingerprintdefaultResponse",
    "ProjectGetMaskedEnvVarResponse",
    "ProjectGetMaskedEnvVardefaultResponse",
    "ProjectGetSettingsResponse",
    "ProjectListCheckoutKeysResponse",
    "ProjectListCheckoutKeysResponseItemsItem",
    "ProjectListCheckoutKeysResponseItemsItemType",
    "ProjectListCheckoutKeysdefaultResponse",
    "ProjectListEnvVarValuesResponse",
    "ProjectListEnvVarValuesResponseItemsItem",
    "ProjectListEnvVarValuesdefaultResponse",
    "ProjectSettings",
    "ProjectSettingsAdvanced",
    "ProjectUpdateSettingsResponse",
    "RestrictionCreated",
    "RestrictionCreatedRestrictionType",
    "RestrictionDeleted",
    "ScheduleCreateNewScheduleResponse",
    "ScheduleCreateNewScheduleResponseActor",
    "ScheduleCreateNewScheduleResponseParametersValue",
    "ScheduleCreateNewScheduleResponseTimetable",
    "ScheduleCreateNewScheduleResponseTimetableOne",
    "ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem",
    "ScheduleCreateNewScheduleResponseTimetableOneMonthsItem",
    "ScheduleCreateNewScheduleResponseTimetableZero",
    "ScheduleCreateNewScheduleResponseTimetableZeroDaysOfWeekItem",
    "ScheduleCreateNewScheduleResponseTimetableZeroMonthsItem",
    "ScheduleCreateNewScheduledefaultResponse",
    "ScheduleGetAllSchedulesResponse",
    "ScheduleGetAllSchedulesResponseItemsItem",
    "ScheduleGetAllSchedulesResponseItemsItemActor",
    "ScheduleGetAllSchedulesResponseItemsItemParametersValue",
    "ScheduleGetAllSchedulesResponseItemsItemTimetable",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOne",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOneDaysOfWeekItem",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableOneMonthsItem",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZero",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZeroDaysOfWeekItem",
    "ScheduleGetAllSchedulesResponseItemsItemTimetableZeroMonthsItem",
    "ScheduleGetAllSchedulesdefaultResponse",
    "ScheduleGetByIdResponse",
    "ScheduleGetByIdResponseActor",
    "ScheduleGetByIdResponseParametersValue",
    "ScheduleGetByIdResponseTimetable",
    "ScheduleGetByIdResponseTimetableOne",
    "ScheduleGetByIdResponseTimetableOneDaysOfWeekItem",
    "ScheduleGetByIdResponseTimetableOneMonthsItem",
    "ScheduleGetByIdResponseTimetableZero",
    "ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem",
    "ScheduleGetByIdResponseTimetableZeroMonthsItem",
    "ScheduleGetByIddefaultResponse",
    "ScheduleRemoveByIdResponse",
    "ScheduleRemoveByIddefaultResponse",
    "ScheduleUpdateScheduleResponse",
    "ScheduleUpdateScheduleResponseActor",
    "ScheduleUpdateScheduleResponseParametersValue",
    "ScheduleUpdateScheduleResponseTimetable",
    "ScheduleUpdateScheduleResponseTimetableOne",
    "ScheduleUpdateScheduleResponseTimetableOneDaysOfWeekItem",
    "ScheduleUpdateScheduleResponseTimetableOneMonthsItem",
    "ScheduleUpdateScheduleResponseTimetableZero",
    "ScheduleUpdateScheduleResponseTimetableZeroDaysOfWeekItem",
    "ScheduleUpdateScheduleResponseTimetableZeroMonthsItem",
    "ScheduleUpdateScheduledefaultResponse",
    "UserGetInformationResponse",
    "UserGetInformationdefaultResponse",
    "UserGetUserInformationResponse",
    "UserGetUserInformationdefaultResponse",
    "UserListCollaborationsResponse",
    "UserListCollaborationsResponseItem",
    "UserListCollaborationsdefaultResponse",
    "Violation",
    "WebhookCreateOutboundWebhookResponse",
    "WebhookCreateOutboundWebhookResponseEventsItem",
    "WebhookCreateOutboundWebhookResponseScope",
    "WebhookCreateOutboundWebhookdefaultResponse",
    "WebhookDeleteOutboundWebhookResponse",
    "WebhookDeleteOutboundWebhookdefaultResponse",
    "WebhookGetByIdResponse",
    "WebhookGetByIdResponseEventsItem",
    "WebhookGetByIdResponseScope",
    "WebhookGetByIddefaultResponse",
    "WebhookListMatchingScopeResponse",
    "WebhookListMatchingScopeResponseItemsItem",
    "WebhookListMatchingScopeResponseItemsItemEventsItem",
    "WebhookListMatchingScopeResponseItemsItemScope",
    "WebhookListMatchingScopedefaultResponse",
    "WebhookUpdateOutboundWebhookResponse",
    "WebhookUpdateOutboundWebhookResponseEventsItem",
    "WebhookUpdateOutboundWebhookResponseScope",
    "WebhookUpdateOutboundWebhookdefaultResponse",
    "WorkflowApproveJobResponse",
    "WorkflowApproveJobdefaultResponse",
    "WorkflowCancelWorkflowResponse",
    "WorkflowCancelWorkflowdefaultResponse",
    "WorkflowGetByIdResponse",
    "WorkflowGetByIdResponseStatus",
    "WorkflowGetByIdResponseTag",
    "WorkflowGetByIddefaultResponse",
    "WorkflowGetJobsResponse",
    "WorkflowGetJobsResponseItemsItem",
    "WorkflowGetJobsResponseItemsItemStatus",
    "WorkflowGetJobsResponseItemsItemType",
    "WorkflowGetJobsdefaultResponse",
    "WorkflowRerunWorkflowResponse",
    "WorkflowRerunWorkflowdefaultResponse",
]
