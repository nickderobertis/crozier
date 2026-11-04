

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchedWorkflowModelApprovalsState(enum.StrEnum):
    """
    The state of the approvals.
    """

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    NOT_APPLICABLE = "not_applicable"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        not_applicable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LaunchedWorkflowModelApprovalsState.NOT_STARTED:
            return not_started()
        if self is LaunchedWorkflowModelApprovalsState.IN_PROGRESS:
            return in_progress()
        if self is LaunchedWorkflowModelApprovalsState.COMPLETED:
            return completed()
        if self is LaunchedWorkflowModelApprovalsState.NOT_APPLICABLE:
            return not_applicable()
