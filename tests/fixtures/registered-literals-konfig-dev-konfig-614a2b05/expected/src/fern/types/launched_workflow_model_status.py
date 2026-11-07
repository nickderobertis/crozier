

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchedWorkflowModelStatus(enum.StrEnum):
    """
    The current status of the launched workflow.
    """

    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LaunchedWorkflowModelStatus.ACTIVE:
            return active()
        if self is LaunchedWorkflowModelStatus.PAUSED:
            return paused()
        if self is LaunchedWorkflowModelStatus.CANCELLED:
            return cancelled()
        if self is LaunchedWorkflowModelStatus.COMPLETED:
            return completed()
