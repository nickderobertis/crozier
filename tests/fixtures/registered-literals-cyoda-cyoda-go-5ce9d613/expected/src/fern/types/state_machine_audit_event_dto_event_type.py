

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StateMachineAuditEventDtoEventType(enum.StrEnum):
    """
    Type of the state machine event
    """

    STARTED = "STARTED"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"
    FORCED_SUCCESS = "FORCED_SUCCESS"
    WORKFLOW_FOUND = "WORKFLOW_FOUND"
    WORKFLOW_NOT_FOUND = "WORKFLOW_NOT_FOUND"
    WORKFLOW_SKIPPED = "WORKFLOW_SKIPPED"
    TRANSITION_MADE = "TRANSITION_MADE"
    TRANSITION_NOT_FOUND = "TRANSITION_NOT_FOUND"
    TRANSITION_CRITERION_NOT_MATCHED = "TRANSITION_CRITERION_NOT_MATCHED"
    PROCESS_CRITERION_NOT_MATCHED = "PROCESS_CRITERION_NOT_MATCHED"
    PROCESSING_PAUSED = "PROCESSING_PAUSED"
    STATE_PROCESS_RESULT = "STATE_PROCESS_RESULT"

    def visit(
        self,
        started: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        forced_success: typing.Callable[[], T_Result],
        workflow_found: typing.Callable[[], T_Result],
        workflow_not_found: typing.Callable[[], T_Result],
        workflow_skipped: typing.Callable[[], T_Result],
        transition_made: typing.Callable[[], T_Result],
        transition_not_found: typing.Callable[[], T_Result],
        transition_criterion_not_matched: typing.Callable[[], T_Result],
        process_criterion_not_matched: typing.Callable[[], T_Result],
        processing_paused: typing.Callable[[], T_Result],
        state_process_result: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StateMachineAuditEventDtoEventType.STARTED:
            return started()
        if self is StateMachineAuditEventDtoEventType.FINISHED:
            return finished()
        if self is StateMachineAuditEventDtoEventType.CANCELLED:
            return cancelled()
        if self is StateMachineAuditEventDtoEventType.FORCED_SUCCESS:
            return forced_success()
        if self is StateMachineAuditEventDtoEventType.WORKFLOW_FOUND:
            return workflow_found()
        if self is StateMachineAuditEventDtoEventType.WORKFLOW_NOT_FOUND:
            return workflow_not_found()
        if self is StateMachineAuditEventDtoEventType.WORKFLOW_SKIPPED:
            return workflow_skipped()
        if self is StateMachineAuditEventDtoEventType.TRANSITION_MADE:
            return transition_made()
        if self is StateMachineAuditEventDtoEventType.TRANSITION_NOT_FOUND:
            return transition_not_found()
        if self is StateMachineAuditEventDtoEventType.TRANSITION_CRITERION_NOT_MATCHED:
            return transition_criterion_not_matched()
        if self is StateMachineAuditEventDtoEventType.PROCESS_CRITERION_NOT_MATCHED:
            return process_criterion_not_matched()
        if self is StateMachineAuditEventDtoEventType.PROCESSING_PAUSED:
            return processing_paused()
        if self is StateMachineAuditEventDtoEventType.STATE_PROCESS_RESULT:
            return state_process_result()
