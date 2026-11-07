

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowStopReasonDtoType(enum.StrEnum):
    COMPLETED_NO_AUTO_TRANSITIONS = "COMPLETED_NO_AUTO_TRANSITIONS"
    COMPLETED_ALL_CRITERIA_REJECTED = "COMPLETED_ALL_CRITERIA_REJECTED"
    PAUSED_FOR_PROCESSING = "PAUSED_FOR_PROCESSING"
    CANCELED = "CANCELED"
    NO_WORKFLOW_FOUND = "NO_WORKFLOW_FOUND"
    WORKFLOW_SKIPPED = "WORKFLOW_SKIPPED"
    FORCE_SUCCESS = "FORCE_SUCCESS"
    INCOMPLETE_TRANSACTION = "INCOMPLETE_TRANSACTION"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        completed_no_auto_transitions: typing.Callable[[], T_Result],
        completed_all_criteria_rejected: typing.Callable[[], T_Result],
        paused_for_processing: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        no_workflow_found: typing.Callable[[], T_Result],
        workflow_skipped: typing.Callable[[], T_Result],
        force_success: typing.Callable[[], T_Result],
        incomplete_transaction: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowStopReasonDtoType.COMPLETED_NO_AUTO_TRANSITIONS:
            return completed_no_auto_transitions()
        if self is WorkflowStopReasonDtoType.COMPLETED_ALL_CRITERIA_REJECTED:
            return completed_all_criteria_rejected()
        if self is WorkflowStopReasonDtoType.PAUSED_FOR_PROCESSING:
            return paused_for_processing()
        if self is WorkflowStopReasonDtoType.CANCELED:
            return canceled()
        if self is WorkflowStopReasonDtoType.NO_WORKFLOW_FOUND:
            return no_workflow_found()
        if self is WorkflowStopReasonDtoType.WORKFLOW_SKIPPED:
            return workflow_skipped()
        if self is WorkflowStopReasonDtoType.FORCE_SUCCESS:
            return force_success()
        if self is WorkflowStopReasonDtoType.INCOMPLETE_TRANSACTION:
            return incomplete_transaction()
        if self is WorkflowStopReasonDtoType.UNKNOWN:
            return unknown()
