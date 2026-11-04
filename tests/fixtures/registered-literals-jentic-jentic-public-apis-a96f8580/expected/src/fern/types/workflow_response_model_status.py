

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowResponseModelStatus(enum.StrEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    PAUSED = "paused"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowResponseModelStatus.ACTIVE:
            return active()
        if self is WorkflowResponseModelStatus.COMPLETED:
            return completed()
        if self is WorkflowResponseModelStatus.CANCELLED:
            return cancelled()
        if self is WorkflowResponseModelStatus.PAUSED:
            return paused()
