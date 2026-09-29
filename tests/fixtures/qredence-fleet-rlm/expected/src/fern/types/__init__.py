



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .artifact_response import ArtifactResponse
    from .artifact_response_kind import ArtifactResponseKind
    from .attachment_response import AttachmentResponse
    from .cancellation_response import CancellationResponse
    from .cancellation_response_state import CancellationResponseState
    from .data_artifact_ui_message_part import DataArtifactUiMessagePart
    from .data_attachment_ui_message_part import DataAttachmentUiMessagePart
    from .data_child_progress_ui_message_part import DataChildProgressUiMessagePart
    from .data_rlm_code_ui_message_part import DataRlmCodeUiMessagePart
    from .data_rlm_output_ui_message_part import DataRlmOutputUiMessagePart
    from .data_skill_ui_message_part import DataSkillUiMessagePart
    from .data_status_ui_message_part import DataStatusUiMessagePart
    from .data_step_ui_message_part import DataStepUiMessagePart
    from .data_structured_result_ui_message_part import DataStructuredResultUiMessagePart
    from .data_usage_ui_message_part import DataUsageUiMessagePart
    from .data_warning_ui_message_part import DataWarningUiMessagePart
    from .dynamic_tool_ui_message_part import DynamicToolUiMessagePart
    from .error_response import ErrorResponse
    from .fleet_ui_message_chunk import (
        FleetUiMessageChunk,
        FleetUiMessageChunk_Abort,
        FleetUiMessageChunk_DataArtifact,
        FleetUiMessageChunk_DataAttachment,
        FleetUiMessageChunk_DataChildProgress,
        FleetUiMessageChunk_DataRlmCode,
        FleetUiMessageChunk_DataRlmOutput,
        FleetUiMessageChunk_DataSkill,
        FleetUiMessageChunk_DataStatus,
        FleetUiMessageChunk_DataStructuredResult,
        FleetUiMessageChunk_DataUsage,
        FleetUiMessageChunk_DataWarning,
        FleetUiMessageChunk_Error,
        FleetUiMessageChunk_Finish,
        FleetUiMessageChunk_FinishStep,
        FleetUiMessageChunk_ReasoningDelta,
        FleetUiMessageChunk_ReasoningEnd,
        FleetUiMessageChunk_ReasoningStart,
        FleetUiMessageChunk_Start,
        FleetUiMessageChunk_StartStep,
        FleetUiMessageChunk_TextDelta,
        FleetUiMessageChunk_TextEnd,
        FleetUiMessageChunk_TextStart,
        FleetUiMessageChunk_ToolInputAvailable,
        FleetUiMessageChunk_ToolOutputAvailable,
        FleetUiMessageChunk_ToolOutputError,
    )
    from .fleet_ui_message_chunk_abort import FleetUiMessageChunkAbort
    from .fleet_ui_message_chunk_data_artifact import FleetUiMessageChunkDataArtifact
    from .fleet_ui_message_chunk_data_artifact_data import FleetUiMessageChunkDataArtifactData
    from .fleet_ui_message_chunk_data_attachment import FleetUiMessageChunkDataAttachment
    from .fleet_ui_message_chunk_data_attachment_data import FleetUiMessageChunkDataAttachmentData
    from .fleet_ui_message_chunk_data_child_progress import FleetUiMessageChunkDataChildProgress
    from .fleet_ui_message_chunk_data_child_progress_data import FleetUiMessageChunkDataChildProgressData
    from .fleet_ui_message_chunk_data_child_progress_data_cleanup_state import (
        FleetUiMessageChunkDataChildProgressDataCleanupState,
    )
    from .fleet_ui_message_chunk_data_child_progress_data_state import FleetUiMessageChunkDataChildProgressDataState
    from .fleet_ui_message_chunk_data_rlm_code import FleetUiMessageChunkDataRlmCode
    from .fleet_ui_message_chunk_data_rlm_code_data import FleetUiMessageChunkDataRlmCodeData
    from .fleet_ui_message_chunk_data_rlm_output import FleetUiMessageChunkDataRlmOutput
    from .fleet_ui_message_chunk_data_rlm_output_data import FleetUiMessageChunkDataRlmOutputData
    from .fleet_ui_message_chunk_data_skill import FleetUiMessageChunkDataSkill
    from .fleet_ui_message_chunk_data_skill_data import FleetUiMessageChunkDataSkillData
    from .fleet_ui_message_chunk_data_skill_data_phase import FleetUiMessageChunkDataSkillDataPhase
    from .fleet_ui_message_chunk_data_status import FleetUiMessageChunkDataStatus
    from .fleet_ui_message_chunk_data_status_data import FleetUiMessageChunkDataStatusData
    from .fleet_ui_message_chunk_data_structured_result import FleetUiMessageChunkDataStructuredResult
    from .fleet_ui_message_chunk_data_structured_result_data import FleetUiMessageChunkDataStructuredResultData
    from .fleet_ui_message_chunk_data_usage import FleetUiMessageChunkDataUsage
    from .fleet_ui_message_chunk_data_usage_data import FleetUiMessageChunkDataUsageData
    from .fleet_ui_message_chunk_data_warning import FleetUiMessageChunkDataWarning
    from .fleet_ui_message_chunk_data_warning_data import FleetUiMessageChunkDataWarningData
    from .fleet_ui_message_chunk_error import FleetUiMessageChunkError
    from .fleet_ui_message_chunk_finish import FleetUiMessageChunkFinish
    from .fleet_ui_message_chunk_finish_finish_reason import FleetUiMessageChunkFinishFinishReason
    from .fleet_ui_message_chunk_finish_step import FleetUiMessageChunkFinishStep
    from .fleet_ui_message_chunk_reasoning_delta import FleetUiMessageChunkReasoningDelta
    from .fleet_ui_message_chunk_reasoning_end import FleetUiMessageChunkReasoningEnd
    from .fleet_ui_message_chunk_reasoning_start import FleetUiMessageChunkReasoningStart
    from .fleet_ui_message_chunk_start import FleetUiMessageChunkStart
    from .fleet_ui_message_chunk_start_step import FleetUiMessageChunkStartStep
    from .fleet_ui_message_chunk_text_delta import FleetUiMessageChunkTextDelta
    from .fleet_ui_message_chunk_text_end import FleetUiMessageChunkTextEnd
    from .fleet_ui_message_chunk_text_start import FleetUiMessageChunkTextStart
    from .fleet_ui_message_chunk_tool_input_available import FleetUiMessageChunkToolInputAvailable
    from .fleet_ui_message_chunk_tool_output_available import FleetUiMessageChunkToolOutputAvailable
    from .fleet_ui_message_chunk_tool_output_error import FleetUiMessageChunkToolOutputError
    from .health_liveness_response import HealthLivenessResponse
    from .health_liveness_response_status import HealthLivenessResponseStatus
    from .health_readiness_response import HealthReadinessResponse
    from .health_readiness_response_database import HealthReadinessResponseDatabase
    from .health_readiness_response_status import HealthReadinessResponseStatus
    from .json_value import JsonValue
    from .reasoning_ui_message_part import ReasoningUiMessagePart
    from .session_detail_response import SessionDetailResponse
    from .session_detail_response_status import SessionDetailResponseStatus
    from .session_list_response import SessionListResponse
    from .session_summary_response import SessionSummaryResponse
    from .session_summary_response_status import SessionSummaryResponseStatus
    from .session_task_response import SessionTaskResponse
    from .session_turn_page_response import SessionTurnPageResponse
    from .settings_field_response import SettingsFieldResponse
    from .settings_field_response_editor import SettingsFieldResponseEditor
    from .settings_field_response_origin import SettingsFieldResponseOrigin
    from .settings_policy_patch_request import SettingsPolicyPatchRequest
    from .settings_policy_patch_request_default_profile import SettingsPolicyPatchRequestDefaultProfile
    from .settings_policy_patch_request_default_profile_updates import SettingsPolicyPatchRequestDefaultProfileUpdates
    from .settings_policy_patch_request_path import SettingsPolicyPatchRequestPath
    from .settings_policy_patch_request_profile import SettingsPolicyPatchRequestProfile
    from .settings_policy_response import SettingsPolicyResponse
    from .settings_policy_update import SettingsPolicyUpdate
    from .settings_policy_update_one import SettingsPolicyUpdateOne
    from .settings_policy_update_value import SettingsPolicyUpdateValue
    from .settings_scope_response import SettingsScopeResponse
    from .skill_card_response import SkillCardResponse
    from .skill_card_response_scope import SkillCardResponseScope
    from .skill_card_response_trust import SkillCardResponseTrust
    from .skill_selection_request import SkillSelectionRequest
    from .step_start_ui_message_part import StepStartUiMessagePart
    from .text_ui_message_part import TextUiMessagePart
    from .trace_feedback_response import TraceFeedbackResponse
    from .trace_feedback_response_name import TraceFeedbackResponseName
    from .ui_message_response import UiMessageResponse
    from .ui_message_response_parts_item import (
        UiMessageResponsePartsItem,
        UiMessageResponsePartsItem_DataArtifact,
        UiMessageResponsePartsItem_DataAttachment,
        UiMessageResponsePartsItem_DataChildProgress,
        UiMessageResponsePartsItem_DataRlmCode,
        UiMessageResponsePartsItem_DataRlmOutput,
        UiMessageResponsePartsItem_DataSkill,
        UiMessageResponsePartsItem_DataStatus,
        UiMessageResponsePartsItem_DataStep,
        UiMessageResponsePartsItem_DataStructuredResult,
        UiMessageResponsePartsItem_DataUsage,
        UiMessageResponsePartsItem_DataWarning,
        UiMessageResponsePartsItem_DynamicTool,
        UiMessageResponsePartsItem_Reasoning,
        UiMessageResponsePartsItem_StepStart,
        UiMessageResponsePartsItem_Text,
    )
    from .ui_message_response_role import UiMessageResponseRole
    from .volume_tree_response import VolumeTreeResponse
    from .workspace_file_delete_response import WorkspaceFileDeleteResponse
    from .workspace_file_entry_response import WorkspaceFileEntryResponse
    from .workspace_file_entry_response_kind import WorkspaceFileEntryResponseKind
    from .workspace_file_list_response import WorkspaceFileListResponse
    from .workspace_file_read_response import WorkspaceFileReadResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ArtifactResponse": ".artifact_response",
    "ArtifactResponseKind": ".artifact_response_kind",
    "AttachmentResponse": ".attachment_response",
    "CancellationResponse": ".cancellation_response",
    "CancellationResponseState": ".cancellation_response_state",
    "DataArtifactUiMessagePart": ".data_artifact_ui_message_part",
    "DataAttachmentUiMessagePart": ".data_attachment_ui_message_part",
    "DataChildProgressUiMessagePart": ".data_child_progress_ui_message_part",
    "DataRlmCodeUiMessagePart": ".data_rlm_code_ui_message_part",
    "DataRlmOutputUiMessagePart": ".data_rlm_output_ui_message_part",
    "DataSkillUiMessagePart": ".data_skill_ui_message_part",
    "DataStatusUiMessagePart": ".data_status_ui_message_part",
    "DataStepUiMessagePart": ".data_step_ui_message_part",
    "DataStructuredResultUiMessagePart": ".data_structured_result_ui_message_part",
    "DataUsageUiMessagePart": ".data_usage_ui_message_part",
    "DataWarningUiMessagePart": ".data_warning_ui_message_part",
    "DynamicToolUiMessagePart": ".dynamic_tool_ui_message_part",
    "ErrorResponse": ".error_response",
    "FleetUiMessageChunk": ".fleet_ui_message_chunk",
    "FleetUiMessageChunkAbort": ".fleet_ui_message_chunk_abort",
    "FleetUiMessageChunkDataArtifact": ".fleet_ui_message_chunk_data_artifact",
    "FleetUiMessageChunkDataArtifactData": ".fleet_ui_message_chunk_data_artifact_data",
    "FleetUiMessageChunkDataAttachment": ".fleet_ui_message_chunk_data_attachment",
    "FleetUiMessageChunkDataAttachmentData": ".fleet_ui_message_chunk_data_attachment_data",
    "FleetUiMessageChunkDataChildProgress": ".fleet_ui_message_chunk_data_child_progress",
    "FleetUiMessageChunkDataChildProgressData": ".fleet_ui_message_chunk_data_child_progress_data",
    "FleetUiMessageChunkDataChildProgressDataCleanupState": ".fleet_ui_message_chunk_data_child_progress_data_cleanup_state",
    "FleetUiMessageChunkDataChildProgressDataState": ".fleet_ui_message_chunk_data_child_progress_data_state",
    "FleetUiMessageChunkDataRlmCode": ".fleet_ui_message_chunk_data_rlm_code",
    "FleetUiMessageChunkDataRlmCodeData": ".fleet_ui_message_chunk_data_rlm_code_data",
    "FleetUiMessageChunkDataRlmOutput": ".fleet_ui_message_chunk_data_rlm_output",
    "FleetUiMessageChunkDataRlmOutputData": ".fleet_ui_message_chunk_data_rlm_output_data",
    "FleetUiMessageChunkDataSkill": ".fleet_ui_message_chunk_data_skill",
    "FleetUiMessageChunkDataSkillData": ".fleet_ui_message_chunk_data_skill_data",
    "FleetUiMessageChunkDataSkillDataPhase": ".fleet_ui_message_chunk_data_skill_data_phase",
    "FleetUiMessageChunkDataStatus": ".fleet_ui_message_chunk_data_status",
    "FleetUiMessageChunkDataStatusData": ".fleet_ui_message_chunk_data_status_data",
    "FleetUiMessageChunkDataStructuredResult": ".fleet_ui_message_chunk_data_structured_result",
    "FleetUiMessageChunkDataStructuredResultData": ".fleet_ui_message_chunk_data_structured_result_data",
    "FleetUiMessageChunkDataUsage": ".fleet_ui_message_chunk_data_usage",
    "FleetUiMessageChunkDataUsageData": ".fleet_ui_message_chunk_data_usage_data",
    "FleetUiMessageChunkDataWarning": ".fleet_ui_message_chunk_data_warning",
    "FleetUiMessageChunkDataWarningData": ".fleet_ui_message_chunk_data_warning_data",
    "FleetUiMessageChunkError": ".fleet_ui_message_chunk_error",
    "FleetUiMessageChunkFinish": ".fleet_ui_message_chunk_finish",
    "FleetUiMessageChunkFinishFinishReason": ".fleet_ui_message_chunk_finish_finish_reason",
    "FleetUiMessageChunkFinishStep": ".fleet_ui_message_chunk_finish_step",
    "FleetUiMessageChunkReasoningDelta": ".fleet_ui_message_chunk_reasoning_delta",
    "FleetUiMessageChunkReasoningEnd": ".fleet_ui_message_chunk_reasoning_end",
    "FleetUiMessageChunkReasoningStart": ".fleet_ui_message_chunk_reasoning_start",
    "FleetUiMessageChunkStart": ".fleet_ui_message_chunk_start",
    "FleetUiMessageChunkStartStep": ".fleet_ui_message_chunk_start_step",
    "FleetUiMessageChunkTextDelta": ".fleet_ui_message_chunk_text_delta",
    "FleetUiMessageChunkTextEnd": ".fleet_ui_message_chunk_text_end",
    "FleetUiMessageChunkTextStart": ".fleet_ui_message_chunk_text_start",
    "FleetUiMessageChunkToolInputAvailable": ".fleet_ui_message_chunk_tool_input_available",
    "FleetUiMessageChunkToolOutputAvailable": ".fleet_ui_message_chunk_tool_output_available",
    "FleetUiMessageChunkToolOutputError": ".fleet_ui_message_chunk_tool_output_error",
    "FleetUiMessageChunk_Abort": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataArtifact": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataAttachment": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataChildProgress": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataRlmCode": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataRlmOutput": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataSkill": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataStatus": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataStructuredResult": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataUsage": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_DataWarning": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_Error": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_Finish": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_FinishStep": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ReasoningDelta": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ReasoningEnd": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ReasoningStart": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_Start": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_StartStep": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_TextDelta": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_TextEnd": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_TextStart": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ToolInputAvailable": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ToolOutputAvailable": ".fleet_ui_message_chunk",
    "FleetUiMessageChunk_ToolOutputError": ".fleet_ui_message_chunk",
    "HealthLivenessResponse": ".health_liveness_response",
    "HealthLivenessResponseStatus": ".health_liveness_response_status",
    "HealthReadinessResponse": ".health_readiness_response",
    "HealthReadinessResponseDatabase": ".health_readiness_response_database",
    "HealthReadinessResponseStatus": ".health_readiness_response_status",
    "JsonValue": ".json_value",
    "ReasoningUiMessagePart": ".reasoning_ui_message_part",
    "SessionDetailResponse": ".session_detail_response",
    "SessionDetailResponseStatus": ".session_detail_response_status",
    "SessionListResponse": ".session_list_response",
    "SessionSummaryResponse": ".session_summary_response",
    "SessionSummaryResponseStatus": ".session_summary_response_status",
    "SessionTaskResponse": ".session_task_response",
    "SessionTurnPageResponse": ".session_turn_page_response",
    "SettingsFieldResponse": ".settings_field_response",
    "SettingsFieldResponseEditor": ".settings_field_response_editor",
    "SettingsFieldResponseOrigin": ".settings_field_response_origin",
    "SettingsPolicyPatchRequest": ".settings_policy_patch_request",
    "SettingsPolicyPatchRequestDefaultProfile": ".settings_policy_patch_request_default_profile",
    "SettingsPolicyPatchRequestDefaultProfileUpdates": ".settings_policy_patch_request_default_profile_updates",
    "SettingsPolicyPatchRequestPath": ".settings_policy_patch_request_path",
    "SettingsPolicyPatchRequestProfile": ".settings_policy_patch_request_profile",
    "SettingsPolicyResponse": ".settings_policy_response",
    "SettingsPolicyUpdate": ".settings_policy_update",
    "SettingsPolicyUpdateOne": ".settings_policy_update_one",
    "SettingsPolicyUpdateValue": ".settings_policy_update_value",
    "SettingsScopeResponse": ".settings_scope_response",
    "SkillCardResponse": ".skill_card_response",
    "SkillCardResponseScope": ".skill_card_response_scope",
    "SkillCardResponseTrust": ".skill_card_response_trust",
    "SkillSelectionRequest": ".skill_selection_request",
    "StepStartUiMessagePart": ".step_start_ui_message_part",
    "TextUiMessagePart": ".text_ui_message_part",
    "TraceFeedbackResponse": ".trace_feedback_response",
    "TraceFeedbackResponseName": ".trace_feedback_response_name",
    "UiMessageResponse": ".ui_message_response",
    "UiMessageResponsePartsItem": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataArtifact": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataAttachment": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataChildProgress": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataRlmCode": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataRlmOutput": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataSkill": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataStatus": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataStep": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataStructuredResult": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataUsage": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DataWarning": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_DynamicTool": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_Reasoning": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_StepStart": ".ui_message_response_parts_item",
    "UiMessageResponsePartsItem_Text": ".ui_message_response_parts_item",
    "UiMessageResponseRole": ".ui_message_response_role",
    "VolumeTreeResponse": ".volume_tree_response",
    "WorkspaceFileDeleteResponse": ".workspace_file_delete_response",
    "WorkspaceFileEntryResponse": ".workspace_file_entry_response",
    "WorkspaceFileEntryResponseKind": ".workspace_file_entry_response_kind",
    "WorkspaceFileListResponse": ".workspace_file_list_response",
    "WorkspaceFileReadResponse": ".workspace_file_read_response",
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
    "ArtifactResponse",
    "ArtifactResponseKind",
    "AttachmentResponse",
    "CancellationResponse",
    "CancellationResponseState",
    "DataArtifactUiMessagePart",
    "DataAttachmentUiMessagePart",
    "DataChildProgressUiMessagePart",
    "DataRlmCodeUiMessagePart",
    "DataRlmOutputUiMessagePart",
    "DataSkillUiMessagePart",
    "DataStatusUiMessagePart",
    "DataStepUiMessagePart",
    "DataStructuredResultUiMessagePart",
    "DataUsageUiMessagePart",
    "DataWarningUiMessagePart",
    "DynamicToolUiMessagePart",
    "ErrorResponse",
    "FleetUiMessageChunk",
    "FleetUiMessageChunkAbort",
    "FleetUiMessageChunkDataArtifact",
    "FleetUiMessageChunkDataArtifactData",
    "FleetUiMessageChunkDataAttachment",
    "FleetUiMessageChunkDataAttachmentData",
    "FleetUiMessageChunkDataChildProgress",
    "FleetUiMessageChunkDataChildProgressData",
    "FleetUiMessageChunkDataChildProgressDataCleanupState",
    "FleetUiMessageChunkDataChildProgressDataState",
    "FleetUiMessageChunkDataRlmCode",
    "FleetUiMessageChunkDataRlmCodeData",
    "FleetUiMessageChunkDataRlmOutput",
    "FleetUiMessageChunkDataRlmOutputData",
    "FleetUiMessageChunkDataSkill",
    "FleetUiMessageChunkDataSkillData",
    "FleetUiMessageChunkDataSkillDataPhase",
    "FleetUiMessageChunkDataStatus",
    "FleetUiMessageChunkDataStatusData",
    "FleetUiMessageChunkDataStructuredResult",
    "FleetUiMessageChunkDataStructuredResultData",
    "FleetUiMessageChunkDataUsage",
    "FleetUiMessageChunkDataUsageData",
    "FleetUiMessageChunkDataWarning",
    "FleetUiMessageChunkDataWarningData",
    "FleetUiMessageChunkError",
    "FleetUiMessageChunkFinish",
    "FleetUiMessageChunkFinishFinishReason",
    "FleetUiMessageChunkFinishStep",
    "FleetUiMessageChunkReasoningDelta",
    "FleetUiMessageChunkReasoningEnd",
    "FleetUiMessageChunkReasoningStart",
    "FleetUiMessageChunkStart",
    "FleetUiMessageChunkStartStep",
    "FleetUiMessageChunkTextDelta",
    "FleetUiMessageChunkTextEnd",
    "FleetUiMessageChunkTextStart",
    "FleetUiMessageChunkToolInputAvailable",
    "FleetUiMessageChunkToolOutputAvailable",
    "FleetUiMessageChunkToolOutputError",
    "FleetUiMessageChunk_Abort",
    "FleetUiMessageChunk_DataArtifact",
    "FleetUiMessageChunk_DataAttachment",
    "FleetUiMessageChunk_DataChildProgress",
    "FleetUiMessageChunk_DataRlmCode",
    "FleetUiMessageChunk_DataRlmOutput",
    "FleetUiMessageChunk_DataSkill",
    "FleetUiMessageChunk_DataStatus",
    "FleetUiMessageChunk_DataStructuredResult",
    "FleetUiMessageChunk_DataUsage",
    "FleetUiMessageChunk_DataWarning",
    "FleetUiMessageChunk_Error",
    "FleetUiMessageChunk_Finish",
    "FleetUiMessageChunk_FinishStep",
    "FleetUiMessageChunk_ReasoningDelta",
    "FleetUiMessageChunk_ReasoningEnd",
    "FleetUiMessageChunk_ReasoningStart",
    "FleetUiMessageChunk_Start",
    "FleetUiMessageChunk_StartStep",
    "FleetUiMessageChunk_TextDelta",
    "FleetUiMessageChunk_TextEnd",
    "FleetUiMessageChunk_TextStart",
    "FleetUiMessageChunk_ToolInputAvailable",
    "FleetUiMessageChunk_ToolOutputAvailable",
    "FleetUiMessageChunk_ToolOutputError",
    "HealthLivenessResponse",
    "HealthLivenessResponseStatus",
    "HealthReadinessResponse",
    "HealthReadinessResponseDatabase",
    "HealthReadinessResponseStatus",
    "JsonValue",
    "ReasoningUiMessagePart",
    "SessionDetailResponse",
    "SessionDetailResponseStatus",
    "SessionListResponse",
    "SessionSummaryResponse",
    "SessionSummaryResponseStatus",
    "SessionTaskResponse",
    "SessionTurnPageResponse",
    "SettingsFieldResponse",
    "SettingsFieldResponseEditor",
    "SettingsFieldResponseOrigin",
    "SettingsPolicyPatchRequest",
    "SettingsPolicyPatchRequestDefaultProfile",
    "SettingsPolicyPatchRequestDefaultProfileUpdates",
    "SettingsPolicyPatchRequestPath",
    "SettingsPolicyPatchRequestProfile",
    "SettingsPolicyResponse",
    "SettingsPolicyUpdate",
    "SettingsPolicyUpdateOne",
    "SettingsPolicyUpdateValue",
    "SettingsScopeResponse",
    "SkillCardResponse",
    "SkillCardResponseScope",
    "SkillCardResponseTrust",
    "SkillSelectionRequest",
    "StepStartUiMessagePart",
    "TextUiMessagePart",
    "TraceFeedbackResponse",
    "TraceFeedbackResponseName",
    "UiMessageResponse",
    "UiMessageResponsePartsItem",
    "UiMessageResponsePartsItem_DataArtifact",
    "UiMessageResponsePartsItem_DataAttachment",
    "UiMessageResponsePartsItem_DataChildProgress",
    "UiMessageResponsePartsItem_DataRlmCode",
    "UiMessageResponsePartsItem_DataRlmOutput",
    "UiMessageResponsePartsItem_DataSkill",
    "UiMessageResponsePartsItem_DataStatus",
    "UiMessageResponsePartsItem_DataStep",
    "UiMessageResponsePartsItem_DataStructuredResult",
    "UiMessageResponsePartsItem_DataUsage",
    "UiMessageResponsePartsItem_DataWarning",
    "UiMessageResponsePartsItem_DynamicTool",
    "UiMessageResponsePartsItem_Reasoning",
    "UiMessageResponsePartsItem_StepStart",
    "UiMessageResponsePartsItem_Text",
    "UiMessageResponseRole",
    "VolumeTreeResponse",
    "WorkspaceFileDeleteResponse",
    "WorkspaceFileEntryResponse",
    "WorkspaceFileEntryResponseKind",
    "WorkspaceFileListResponse",
    "WorkspaceFileReadResponse",
]
