



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .application_response import ApplicationResponse
    from .artefact_build_environment_review_decision import ArtefactBuildEnvironmentReviewDecision
    from .artefact_build_environment_review_response import ArtefactBuildEnvironmentReviewResponse
    from .artefact_build_minimal_response import ArtefactBuildMinimalResponse
    from .artefact_build_response import ArtefactBuildResponse
    from .artefact_history_item_response import ArtefactHistoryItemResponse
    from .artefact_history_response import ArtefactHistoryResponse
    from .artefact_matching_rule_base import ArtefactMatchingRuleBase
    from .artefact_matching_rule_in_response import ArtefactMatchingRuleInResponse
    from .artefact_matching_rule_response import ArtefactMatchingRuleResponse
    from .artefact_response import ArtefactResponse
    from .artefact_search_response import ArtefactSearchResponse
    from .artefact_status import ArtefactStatus
    from .artefact_version_response import ArtefactVersionResponse
    from .c3test_result import C3TestResult
    from .c3test_result_status import C3TestResultStatus
    from .charm_stage import CharmStage
    from .deb_stage import DebStage
    from .environment_reported_issue_request import EnvironmentReportedIssueRequest
    from .environment_reported_issue_response import EnvironmentReportedIssueResponse
    from .environment_response import EnvironmentResponse
    from .environment_review_patch import EnvironmentReviewPatch
    from .environments_response import EnvironmentsResponse
    from .execution_metadata import ExecutionMetadata
    from .execution_metadata_get_response import ExecutionMetadataGetResponse
    from .expected_environment_input import ExpectedEnvironmentInput
    from .family_name import FamilyName
    from .http_validation_error import HttpValidationError
    from .image_stage import ImageStage
    from .issue_attachment_request import IssueAttachmentRequest
    from .issue_response import IssueResponse
    from .issue_source import IssueSource
    from .issue_status import IssueStatus
    from .issues_get_response import IssuesGetResponse
    from .minimal_issue_response import MinimalIssueResponse
    from .minimal_issue_test_result_attachment_response import MinimalIssueTestResultAttachmentResponse
    from .minimal_issue_test_result_attachment_rule_response import MinimalIssueTestResultAttachmentRuleResponse
    from .notification_response import NotificationResponse
    from .notification_type import NotificationType
    from .notifications_response import NotificationsResponse
    from .pending_rerun import PendingRerun
    from .permission import Permission
    from .previous_test_result import PreviousTestResult
    from .rerun_detail import RerunDetail
    from .rerun_details_response import RerunDetailsResponse
    from .rerun_priority_summary import RerunPrioritySummary
    from .reviewer_response import ReviewerResponse
    from .snap_stage import SnapStage
    from .solution_stage import SolutionStage
    from .stage_name import StageName
    from .start_charm_test_execution_request import StartCharmTestExecutionRequest
    from .start_deb_test_execution_request import StartDebTestExecutionRequest
    from .start_deb_test_execution_request_execution_stage import StartDebTestExecutionRequestExecutionStage
    from .start_deb_test_execution_request_execution_stage_one import StartDebTestExecutionRequestExecutionStageOne
    from .start_image_test_execution_request import StartImageTestExecutionRequest
    from .start_snap_test_execution_request import StartSnapTestExecutionRequest
    from .start_solution_test_execution_request import StartSolutionTestExecutionRequest
    from .status_update_request import StatusUpdateRequest
    from .team_minimal import TeamMinimal
    from .team_minimal_response import TeamMinimalResponse
    from .team_response import TeamResponse
    from .test_case_info import TestCaseInfo
    from .test_cases_response import TestCasesResponse
    from .test_event_response import TestEventResponse
    from .test_execution_relevant_link_create import TestExecutionRelevantLinkCreate
    from .test_execution_relevant_link_response import TestExecutionRelevantLinkResponse
    from .test_execution_rerun_filters import TestExecutionRerunFilters
    from .test_execution_rerun_filters_assignee_ids import TestExecutionRerunFiltersAssigneeIds
    from .test_execution_rerun_filters_assignee_ids_one import TestExecutionRerunFiltersAssigneeIdsOne
    from .test_execution_rerun_filters_reviewer_ids import TestExecutionRerunFiltersReviewerIds
    from .test_execution_rerun_filters_reviewer_ids_one import TestExecutionRerunFiltersReviewerIdsOne
    from .test_execution_response import TestExecutionResponse
    from .test_execution_response_with_context import TestExecutionResponseWithContext
    from .test_execution_search_response import TestExecutionSearchResponse
    from .test_execution_status import TestExecutionStatus
    from .test_plans_response import TestPlansResponse
    from .test_reported_issue_request import TestReportedIssueRequest
    from .test_reported_issue_response import TestReportedIssueResponse
    from .test_result_request import TestResultRequest
    from .test_result_response import TestResultResponse
    from .test_result_response_with_context import TestResultResponseWithContext
    from .test_result_search_filters import TestResultSearchFilters
    from .test_result_search_filters_assignee_ids import TestResultSearchFiltersAssigneeIds
    from .test_result_search_filters_assignee_ids_one import TestResultSearchFiltersAssigneeIdsOne
    from .test_result_search_filters_issues import TestResultSearchFiltersIssues
    from .test_result_search_filters_issues_one import TestResultSearchFiltersIssuesOne
    from .test_result_search_filters_reviewer_ids import TestResultSearchFiltersReviewerIds
    from .test_result_search_filters_reviewer_ids_one import TestResultSearchFiltersReviewerIdsOne
    from .test_result_search_response_with_context import TestResultSearchResponseWithContext
    from .test_result_status import TestResultStatus
    from .user_minimal_response import UserMinimalResponse
    from .user_response import UserResponse
    from .users_response import UsersResponse
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "ApplicationResponse": ".application_response",
    "ArtefactBuildEnvironmentReviewDecision": ".artefact_build_environment_review_decision",
    "ArtefactBuildEnvironmentReviewResponse": ".artefact_build_environment_review_response",
    "ArtefactBuildMinimalResponse": ".artefact_build_minimal_response",
    "ArtefactBuildResponse": ".artefact_build_response",
    "ArtefactHistoryItemResponse": ".artefact_history_item_response",
    "ArtefactHistoryResponse": ".artefact_history_response",
    "ArtefactMatchingRuleBase": ".artefact_matching_rule_base",
    "ArtefactMatchingRuleInResponse": ".artefact_matching_rule_in_response",
    "ArtefactMatchingRuleResponse": ".artefact_matching_rule_response",
    "ArtefactResponse": ".artefact_response",
    "ArtefactSearchResponse": ".artefact_search_response",
    "ArtefactStatus": ".artefact_status",
    "ArtefactVersionResponse": ".artefact_version_response",
    "C3TestResult": ".c3test_result",
    "C3TestResultStatus": ".c3test_result_status",
    "CharmStage": ".charm_stage",
    "DebStage": ".deb_stage",
    "EnvironmentReportedIssueRequest": ".environment_reported_issue_request",
    "EnvironmentReportedIssueResponse": ".environment_reported_issue_response",
    "EnvironmentResponse": ".environment_response",
    "EnvironmentReviewPatch": ".environment_review_patch",
    "EnvironmentsResponse": ".environments_response",
    "ExecutionMetadata": ".execution_metadata",
    "ExecutionMetadataGetResponse": ".execution_metadata_get_response",
    "ExpectedEnvironmentInput": ".expected_environment_input",
    "FamilyName": ".family_name",
    "HttpValidationError": ".http_validation_error",
    "ImageStage": ".image_stage",
    "IssueAttachmentRequest": ".issue_attachment_request",
    "IssueResponse": ".issue_response",
    "IssueSource": ".issue_source",
    "IssueStatus": ".issue_status",
    "IssuesGetResponse": ".issues_get_response",
    "MinimalIssueResponse": ".minimal_issue_response",
    "MinimalIssueTestResultAttachmentResponse": ".minimal_issue_test_result_attachment_response",
    "MinimalIssueTestResultAttachmentRuleResponse": ".minimal_issue_test_result_attachment_rule_response",
    "NotificationResponse": ".notification_response",
    "NotificationType": ".notification_type",
    "NotificationsResponse": ".notifications_response",
    "PendingRerun": ".pending_rerun",
    "Permission": ".permission",
    "PreviousTestResult": ".previous_test_result",
    "RerunDetail": ".rerun_detail",
    "RerunDetailsResponse": ".rerun_details_response",
    "RerunPrioritySummary": ".rerun_priority_summary",
    "ReviewerResponse": ".reviewer_response",
    "SnapStage": ".snap_stage",
    "SolutionStage": ".solution_stage",
    "StageName": ".stage_name",
    "StartCharmTestExecutionRequest": ".start_charm_test_execution_request",
    "StartDebTestExecutionRequest": ".start_deb_test_execution_request",
    "StartDebTestExecutionRequestExecutionStage": ".start_deb_test_execution_request_execution_stage",
    "StartDebTestExecutionRequestExecutionStageOne": ".start_deb_test_execution_request_execution_stage_one",
    "StartImageTestExecutionRequest": ".start_image_test_execution_request",
    "StartSnapTestExecutionRequest": ".start_snap_test_execution_request",
    "StartSolutionTestExecutionRequest": ".start_solution_test_execution_request",
    "StatusUpdateRequest": ".status_update_request",
    "TeamMinimal": ".team_minimal",
    "TeamMinimalResponse": ".team_minimal_response",
    "TeamResponse": ".team_response",
    "TestCaseInfo": ".test_case_info",
    "TestCasesResponse": ".test_cases_response",
    "TestEventResponse": ".test_event_response",
    "TestExecutionRelevantLinkCreate": ".test_execution_relevant_link_create",
    "TestExecutionRelevantLinkResponse": ".test_execution_relevant_link_response",
    "TestExecutionRerunFilters": ".test_execution_rerun_filters",
    "TestExecutionRerunFiltersAssigneeIds": ".test_execution_rerun_filters_assignee_ids",
    "TestExecutionRerunFiltersAssigneeIdsOne": ".test_execution_rerun_filters_assignee_ids_one",
    "TestExecutionRerunFiltersReviewerIds": ".test_execution_rerun_filters_reviewer_ids",
    "TestExecutionRerunFiltersReviewerIdsOne": ".test_execution_rerun_filters_reviewer_ids_one",
    "TestExecutionResponse": ".test_execution_response",
    "TestExecutionResponseWithContext": ".test_execution_response_with_context",
    "TestExecutionSearchResponse": ".test_execution_search_response",
    "TestExecutionStatus": ".test_execution_status",
    "TestPlansResponse": ".test_plans_response",
    "TestReportedIssueRequest": ".test_reported_issue_request",
    "TestReportedIssueResponse": ".test_reported_issue_response",
    "TestResultRequest": ".test_result_request",
    "TestResultResponse": ".test_result_response",
    "TestResultResponseWithContext": ".test_result_response_with_context",
    "TestResultSearchFilters": ".test_result_search_filters",
    "TestResultSearchFiltersAssigneeIds": ".test_result_search_filters_assignee_ids",
    "TestResultSearchFiltersAssigneeIdsOne": ".test_result_search_filters_assignee_ids_one",
    "TestResultSearchFiltersIssues": ".test_result_search_filters_issues",
    "TestResultSearchFiltersIssuesOne": ".test_result_search_filters_issues_one",
    "TestResultSearchFiltersReviewerIds": ".test_result_search_filters_reviewer_ids",
    "TestResultSearchFiltersReviewerIdsOne": ".test_result_search_filters_reviewer_ids_one",
    "TestResultSearchResponseWithContext": ".test_result_search_response_with_context",
    "TestResultStatus": ".test_result_status",
    "UserMinimalResponse": ".user_minimal_response",
    "UserResponse": ".user_response",
    "UsersResponse": ".users_response",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "ApplicationResponse",
    "ArtefactBuildEnvironmentReviewDecision",
    "ArtefactBuildEnvironmentReviewResponse",
    "ArtefactBuildMinimalResponse",
    "ArtefactBuildResponse",
    "ArtefactHistoryItemResponse",
    "ArtefactHistoryResponse",
    "ArtefactMatchingRuleBase",
    "ArtefactMatchingRuleInResponse",
    "ArtefactMatchingRuleResponse",
    "ArtefactResponse",
    "ArtefactSearchResponse",
    "ArtefactStatus",
    "ArtefactVersionResponse",
    "C3TestResult",
    "C3TestResultStatus",
    "CharmStage",
    "DebStage",
    "EnvironmentReportedIssueRequest",
    "EnvironmentReportedIssueResponse",
    "EnvironmentResponse",
    "EnvironmentReviewPatch",
    "EnvironmentsResponse",
    "ExecutionMetadata",
    "ExecutionMetadataGetResponse",
    "ExpectedEnvironmentInput",
    "FamilyName",
    "HttpValidationError",
    "ImageStage",
    "IssueAttachmentRequest",
    "IssueResponse",
    "IssueSource",
    "IssueStatus",
    "IssuesGetResponse",
    "MinimalIssueResponse",
    "MinimalIssueTestResultAttachmentResponse",
    "MinimalIssueTestResultAttachmentRuleResponse",
    "NotificationResponse",
    "NotificationType",
    "NotificationsResponse",
    "PendingRerun",
    "Permission",
    "PreviousTestResult",
    "RerunDetail",
    "RerunDetailsResponse",
    "RerunPrioritySummary",
    "ReviewerResponse",
    "SnapStage",
    "SolutionStage",
    "StageName",
    "StartCharmTestExecutionRequest",
    "StartDebTestExecutionRequest",
    "StartDebTestExecutionRequestExecutionStage",
    "StartDebTestExecutionRequestExecutionStageOne",
    "StartImageTestExecutionRequest",
    "StartSnapTestExecutionRequest",
    "StartSolutionTestExecutionRequest",
    "StatusUpdateRequest",
    "TeamMinimal",
    "TeamMinimalResponse",
    "TeamResponse",
    "TestCaseInfo",
    "TestCasesResponse",
    "TestEventResponse",
    "TestExecutionRelevantLinkCreate",
    "TestExecutionRelevantLinkResponse",
    "TestExecutionRerunFilters",
    "TestExecutionRerunFiltersAssigneeIds",
    "TestExecutionRerunFiltersAssigneeIdsOne",
    "TestExecutionRerunFiltersReviewerIds",
    "TestExecutionRerunFiltersReviewerIdsOne",
    "TestExecutionResponse",
    "TestExecutionResponseWithContext",
    "TestExecutionSearchResponse",
    "TestExecutionStatus",
    "TestPlansResponse",
    "TestReportedIssueRequest",
    "TestReportedIssueResponse",
    "TestResultRequest",
    "TestResultResponse",
    "TestResultResponseWithContext",
    "TestResultSearchFilters",
    "TestResultSearchFiltersAssigneeIds",
    "TestResultSearchFiltersAssigneeIdsOne",
    "TestResultSearchFiltersIssues",
    "TestResultSearchFiltersIssuesOne",
    "TestResultSearchFiltersReviewerIds",
    "TestResultSearchFiltersReviewerIdsOne",
    "TestResultSearchResponseWithContext",
    "TestResultStatus",
    "UserMinimalResponse",
    "UserResponse",
    "UsersResponse",
    "ValidationError",
    "ValidationErrorLocItem",
]
