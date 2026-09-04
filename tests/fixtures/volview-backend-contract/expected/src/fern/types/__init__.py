



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .annotations_file import AnnotationsFile
    from .annotations_file_labels import AnnotationsFileLabels
    from .annotations_file_labels_polygons_value import AnnotationsFileLabelsPolygonsValue
    from .annotations_file_labels_rectangles_value import AnnotationsFileLabelsRectanglesValue
    from .annotations_file_labels_rulers_value import AnnotationsFileLabelsRulersValue
    from .annotations_file_space import AnnotationsFileSpace
    from .annotations_file_tools import AnnotationsFileTools
    from .annotations_file_tools_polygons_item import AnnotationsFileToolsPolygonsItem
    from .annotations_file_tools_polygons_item_frame_of_reference import (
        AnnotationsFileToolsPolygonsItemFrameOfReference,
    )
    from .annotations_file_tools_rectangles_item import AnnotationsFileToolsRectanglesItem
    from .annotations_file_tools_rectangles_item_frame_of_reference import (
        AnnotationsFileToolsRectanglesItemFrameOfReference,
    )
    from .annotations_file_tools_rulers_item import AnnotationsFileToolsRulersItem
    from .annotations_file_tools_rulers_item_frame_of_reference import AnnotationsFileToolsRulersItemFrameOfReference
    from .input_value import InputValue
    from .job_history_detail import JobHistoryDetail
    from .job_history_page import JobHistoryPage
    from .job_history_summary import JobHistorySummary
    from .job_history_summary_created_by import JobHistorySummaryCreatedBy
    from .job_history_summary_output_summary import JobHistorySummaryOutputSummary
    from .job_history_summary_result_state import JobHistorySummaryResultState
    from .job_history_summary_state import JobHistorySummaryState
    from .job_ref import JobRef
    from .job_results import JobResults
    from .job_results_error import JobResultsError, JobResultsError_ResultsNotReady, JobResultsError_ResultsUnavailable
    from .job_results_error_results_not_ready import JobResultsErrorResultsNotReady
    from .job_results_error_results_not_ready_result_state import JobResultsErrorResultsNotReadyResultState
    from .job_results_error_results_not_ready_state import JobResultsErrorResultsNotReadyState
    from .job_results_error_results_unavailable import JobResultsErrorResultsUnavailable
    from .job_results_error_results_unavailable_result_state import JobResultsErrorResultsUnavailableResultState
    from .job_results_error_results_unavailable_state import JobResultsErrorResultsUnavailableState
    from .job_results_result_state import JobResultsResultState
    from .neutral_job_status import (
        NeutralJobStatus,
        NeutralJobStatus_Cancelled,
        NeutralJobStatus_Error,
        NeutralJobStatus_Pending,
        NeutralJobStatus_Running,
        NeutralJobStatus_Success,
    )
    from .neutral_job_status_cancelled import NeutralJobStatusCancelled
    from .neutral_job_status_cancelled_result_state import NeutralJobStatusCancelledResultState
    from .neutral_job_status_error import NeutralJobStatusError
    from .neutral_job_status_error_result_state import NeutralJobStatusErrorResultState
    from .neutral_job_status_pending import NeutralJobStatusPending
    from .neutral_job_status_pending_result_state import NeutralJobStatusPendingResultState
    from .neutral_job_status_running import NeutralJobStatusRunning
    from .neutral_job_status_running_result_state import NeutralJobStatusRunningResultState
    from .neutral_job_status_success import NeutralJobStatusSuccess
    from .neutral_job_status_success_result_state import NeutralJobStatusSuccessResultState
    from .result_intent import ResultIntent
    from .result_intent_id import ResultIntentId
    from .result_intent_zero import (
        ResultIntentZero,
        ResultIntentZero_AddAnnotations,
        ResultIntentZero_AddBaseImage,
        ResultIntentZero_AddLayer,
        ResultIntentZero_AddSegmentGroup,
    )
    from .result_intent_zero_add_annotations import ResultIntentZeroAddAnnotations
    from .result_intent_zero_add_annotations_source import ResultIntentZeroAddAnnotationsSource
    from .result_intent_zero_add_base_image import ResultIntentZeroAddBaseImage
    from .result_intent_zero_add_layer import ResultIntentZeroAddLayer
    from .result_intent_zero_add_segment_group import ResultIntentZeroAddSegmentGroup
    from .result_intent_zero_add_segment_group_segments_item import ResultIntentZeroAddSegmentGroupSegmentsItem
    from .result_intent_zero_add_segment_group_source import ResultIntentZeroAddSegmentGroupSource
    from .stage_input_descriptor import (
        StageInputDescriptor,
        StageInputDescriptor_Annotations,
        StageInputDescriptor_Labelmap,
    )
    from .stage_input_descriptor_annotations import StageInputDescriptorAnnotations
    from .stage_input_descriptor_annotations_reference_image import StageInputDescriptorAnnotationsReferenceImage
    from .stage_input_descriptor_annotations_reference_image_type import (
        StageInputDescriptorAnnotationsReferenceImageType,
    )
    from .stage_input_descriptor_labelmap import StageInputDescriptorLabelmap
    from .stage_input_descriptor_labelmap_reference_image import StageInputDescriptorLabelmapReferenceImage
    from .stage_input_descriptor_labelmap_reference_image_type import StageInputDescriptorLabelmapReferenceImageType
    from .stage_response import StageResponse
    from .task_spec import TaskSpec
    from .task_spec_outputs_item import TaskSpecOutputsItem
    from .task_spec_parameters_item import (
        TaskSpecParametersItem,
        TaskSpecParametersItem_Bool,
        TaskSpecParametersItem_Bounds,
        TaskSpecParametersItem_Enum,
        TaskSpecParametersItem_Float,
        TaskSpecParametersItem_Int,
        TaskSpecParametersItem_SourceRef,
        TaskSpecParametersItem_String,
    )
    from .task_spec_parameters_item_bool import TaskSpecParametersItemBool
    from .task_spec_parameters_item_bounds import TaskSpecParametersItemBounds
    from .task_spec_parameters_item_enum import TaskSpecParametersItemEnum
    from .task_spec_parameters_item_enum_default import TaskSpecParametersItemEnumDefault
    from .task_spec_parameters_item_enum_options_item import TaskSpecParametersItemEnumOptionsItem
    from .task_spec_parameters_item_float import TaskSpecParametersItemFloat
    from .task_spec_parameters_item_int import TaskSpecParametersItemInt
    from .task_spec_parameters_item_source_ref import TaskSpecParametersItemSourceRef
    from .task_spec_parameters_item_string import TaskSpecParametersItemString
    from .task_summary import TaskSummary
_dynamic_imports: typing.Dict[str, str] = {
    "AnnotationsFile": ".annotations_file",
    "AnnotationsFileLabels": ".annotations_file_labels",
    "AnnotationsFileLabelsPolygonsValue": ".annotations_file_labels_polygons_value",
    "AnnotationsFileLabelsRectanglesValue": ".annotations_file_labels_rectangles_value",
    "AnnotationsFileLabelsRulersValue": ".annotations_file_labels_rulers_value",
    "AnnotationsFileSpace": ".annotations_file_space",
    "AnnotationsFileTools": ".annotations_file_tools",
    "AnnotationsFileToolsPolygonsItem": ".annotations_file_tools_polygons_item",
    "AnnotationsFileToolsPolygonsItemFrameOfReference": ".annotations_file_tools_polygons_item_frame_of_reference",
    "AnnotationsFileToolsRectanglesItem": ".annotations_file_tools_rectangles_item",
    "AnnotationsFileToolsRectanglesItemFrameOfReference": ".annotations_file_tools_rectangles_item_frame_of_reference",
    "AnnotationsFileToolsRulersItem": ".annotations_file_tools_rulers_item",
    "AnnotationsFileToolsRulersItemFrameOfReference": ".annotations_file_tools_rulers_item_frame_of_reference",
    "InputValue": ".input_value",
    "JobHistoryDetail": ".job_history_detail",
    "JobHistoryPage": ".job_history_page",
    "JobHistorySummary": ".job_history_summary",
    "JobHistorySummaryCreatedBy": ".job_history_summary_created_by",
    "JobHistorySummaryOutputSummary": ".job_history_summary_output_summary",
    "JobHistorySummaryResultState": ".job_history_summary_result_state",
    "JobHistorySummaryState": ".job_history_summary_state",
    "JobRef": ".job_ref",
    "JobResults": ".job_results",
    "JobResultsError": ".job_results_error",
    "JobResultsErrorResultsNotReady": ".job_results_error_results_not_ready",
    "JobResultsErrorResultsNotReadyResultState": ".job_results_error_results_not_ready_result_state",
    "JobResultsErrorResultsNotReadyState": ".job_results_error_results_not_ready_state",
    "JobResultsErrorResultsUnavailable": ".job_results_error_results_unavailable",
    "JobResultsErrorResultsUnavailableResultState": ".job_results_error_results_unavailable_result_state",
    "JobResultsErrorResultsUnavailableState": ".job_results_error_results_unavailable_state",
    "JobResultsError_ResultsNotReady": ".job_results_error",
    "JobResultsError_ResultsUnavailable": ".job_results_error",
    "JobResultsResultState": ".job_results_result_state",
    "NeutralJobStatus": ".neutral_job_status",
    "NeutralJobStatusCancelled": ".neutral_job_status_cancelled",
    "NeutralJobStatusCancelledResultState": ".neutral_job_status_cancelled_result_state",
    "NeutralJobStatusError": ".neutral_job_status_error",
    "NeutralJobStatusErrorResultState": ".neutral_job_status_error_result_state",
    "NeutralJobStatusPending": ".neutral_job_status_pending",
    "NeutralJobStatusPendingResultState": ".neutral_job_status_pending_result_state",
    "NeutralJobStatusRunning": ".neutral_job_status_running",
    "NeutralJobStatusRunningResultState": ".neutral_job_status_running_result_state",
    "NeutralJobStatusSuccess": ".neutral_job_status_success",
    "NeutralJobStatusSuccessResultState": ".neutral_job_status_success_result_state",
    "NeutralJobStatus_Cancelled": ".neutral_job_status",
    "NeutralJobStatus_Error": ".neutral_job_status",
    "NeutralJobStatus_Pending": ".neutral_job_status",
    "NeutralJobStatus_Running": ".neutral_job_status",
    "NeutralJobStatus_Success": ".neutral_job_status",
    "ResultIntent": ".result_intent",
    "ResultIntentId": ".result_intent_id",
    "ResultIntentZero": ".result_intent_zero",
    "ResultIntentZeroAddAnnotations": ".result_intent_zero_add_annotations",
    "ResultIntentZeroAddAnnotationsSource": ".result_intent_zero_add_annotations_source",
    "ResultIntentZeroAddBaseImage": ".result_intent_zero_add_base_image",
    "ResultIntentZeroAddLayer": ".result_intent_zero_add_layer",
    "ResultIntentZeroAddSegmentGroup": ".result_intent_zero_add_segment_group",
    "ResultIntentZeroAddSegmentGroupSegmentsItem": ".result_intent_zero_add_segment_group_segments_item",
    "ResultIntentZeroAddSegmentGroupSource": ".result_intent_zero_add_segment_group_source",
    "ResultIntentZero_AddAnnotations": ".result_intent_zero",
    "ResultIntentZero_AddBaseImage": ".result_intent_zero",
    "ResultIntentZero_AddLayer": ".result_intent_zero",
    "ResultIntentZero_AddSegmentGroup": ".result_intent_zero",
    "StageInputDescriptor": ".stage_input_descriptor",
    "StageInputDescriptorAnnotations": ".stage_input_descriptor_annotations",
    "StageInputDescriptorAnnotationsReferenceImage": ".stage_input_descriptor_annotations_reference_image",
    "StageInputDescriptorAnnotationsReferenceImageType": ".stage_input_descriptor_annotations_reference_image_type",
    "StageInputDescriptorLabelmap": ".stage_input_descriptor_labelmap",
    "StageInputDescriptorLabelmapReferenceImage": ".stage_input_descriptor_labelmap_reference_image",
    "StageInputDescriptorLabelmapReferenceImageType": ".stage_input_descriptor_labelmap_reference_image_type",
    "StageInputDescriptor_Annotations": ".stage_input_descriptor",
    "StageInputDescriptor_Labelmap": ".stage_input_descriptor",
    "StageResponse": ".stage_response",
    "TaskSpec": ".task_spec",
    "TaskSpecOutputsItem": ".task_spec_outputs_item",
    "TaskSpecParametersItem": ".task_spec_parameters_item",
    "TaskSpecParametersItemBool": ".task_spec_parameters_item_bool",
    "TaskSpecParametersItemBounds": ".task_spec_parameters_item_bounds",
    "TaskSpecParametersItemEnum": ".task_spec_parameters_item_enum",
    "TaskSpecParametersItemEnumDefault": ".task_spec_parameters_item_enum_default",
    "TaskSpecParametersItemEnumOptionsItem": ".task_spec_parameters_item_enum_options_item",
    "TaskSpecParametersItemFloat": ".task_spec_parameters_item_float",
    "TaskSpecParametersItemInt": ".task_spec_parameters_item_int",
    "TaskSpecParametersItemSourceRef": ".task_spec_parameters_item_source_ref",
    "TaskSpecParametersItemString": ".task_spec_parameters_item_string",
    "TaskSpecParametersItem_Bool": ".task_spec_parameters_item",
    "TaskSpecParametersItem_Bounds": ".task_spec_parameters_item",
    "TaskSpecParametersItem_Enum": ".task_spec_parameters_item",
    "TaskSpecParametersItem_Float": ".task_spec_parameters_item",
    "TaskSpecParametersItem_Int": ".task_spec_parameters_item",
    "TaskSpecParametersItem_SourceRef": ".task_spec_parameters_item",
    "TaskSpecParametersItem_String": ".task_spec_parameters_item",
    "TaskSummary": ".task_summary",
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
    "AnnotationsFile",
    "AnnotationsFileLabels",
    "AnnotationsFileLabelsPolygonsValue",
    "AnnotationsFileLabelsRectanglesValue",
    "AnnotationsFileLabelsRulersValue",
    "AnnotationsFileSpace",
    "AnnotationsFileTools",
    "AnnotationsFileToolsPolygonsItem",
    "AnnotationsFileToolsPolygonsItemFrameOfReference",
    "AnnotationsFileToolsRectanglesItem",
    "AnnotationsFileToolsRectanglesItemFrameOfReference",
    "AnnotationsFileToolsRulersItem",
    "AnnotationsFileToolsRulersItemFrameOfReference",
    "InputValue",
    "JobHistoryDetail",
    "JobHistoryPage",
    "JobHistorySummary",
    "JobHistorySummaryCreatedBy",
    "JobHistorySummaryOutputSummary",
    "JobHistorySummaryResultState",
    "JobHistorySummaryState",
    "JobRef",
    "JobResults",
    "JobResultsError",
    "JobResultsErrorResultsNotReady",
    "JobResultsErrorResultsNotReadyResultState",
    "JobResultsErrorResultsNotReadyState",
    "JobResultsErrorResultsUnavailable",
    "JobResultsErrorResultsUnavailableResultState",
    "JobResultsErrorResultsUnavailableState",
    "JobResultsError_ResultsNotReady",
    "JobResultsError_ResultsUnavailable",
    "JobResultsResultState",
    "NeutralJobStatus",
    "NeutralJobStatusCancelled",
    "NeutralJobStatusCancelledResultState",
    "NeutralJobStatusError",
    "NeutralJobStatusErrorResultState",
    "NeutralJobStatusPending",
    "NeutralJobStatusPendingResultState",
    "NeutralJobStatusRunning",
    "NeutralJobStatusRunningResultState",
    "NeutralJobStatusSuccess",
    "NeutralJobStatusSuccessResultState",
    "NeutralJobStatus_Cancelled",
    "NeutralJobStatus_Error",
    "NeutralJobStatus_Pending",
    "NeutralJobStatus_Running",
    "NeutralJobStatus_Success",
    "ResultIntent",
    "ResultIntentId",
    "ResultIntentZero",
    "ResultIntentZeroAddAnnotations",
    "ResultIntentZeroAddAnnotationsSource",
    "ResultIntentZeroAddBaseImage",
    "ResultIntentZeroAddLayer",
    "ResultIntentZeroAddSegmentGroup",
    "ResultIntentZeroAddSegmentGroupSegmentsItem",
    "ResultIntentZeroAddSegmentGroupSource",
    "ResultIntentZero_AddAnnotations",
    "ResultIntentZero_AddBaseImage",
    "ResultIntentZero_AddLayer",
    "ResultIntentZero_AddSegmentGroup",
    "StageInputDescriptor",
    "StageInputDescriptorAnnotations",
    "StageInputDescriptorAnnotationsReferenceImage",
    "StageInputDescriptorAnnotationsReferenceImageType",
    "StageInputDescriptorLabelmap",
    "StageInputDescriptorLabelmapReferenceImage",
    "StageInputDescriptorLabelmapReferenceImageType",
    "StageInputDescriptor_Annotations",
    "StageInputDescriptor_Labelmap",
    "StageResponse",
    "TaskSpec",
    "TaskSpecOutputsItem",
    "TaskSpecParametersItem",
    "TaskSpecParametersItemBool",
    "TaskSpecParametersItemBounds",
    "TaskSpecParametersItemEnum",
    "TaskSpecParametersItemEnumDefault",
    "TaskSpecParametersItemEnumOptionsItem",
    "TaskSpecParametersItemFloat",
    "TaskSpecParametersItemInt",
    "TaskSpecParametersItemSourceRef",
    "TaskSpecParametersItemString",
    "TaskSpecParametersItem_Bool",
    "TaskSpecParametersItem_Bounds",
    "TaskSpecParametersItem_Enum",
    "TaskSpecParametersItem_Float",
    "TaskSpecParametersItem_Int",
    "TaskSpecParametersItem_SourceRef",
    "TaskSpecParametersItem_String",
    "TaskSummary",
]
