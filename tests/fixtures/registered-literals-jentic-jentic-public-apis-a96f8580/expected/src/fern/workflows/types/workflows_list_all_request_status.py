

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowsListAllRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowsListAllRequestStatus.ACTIVE:
            return active()
        if self is WorkflowsListAllRequestStatus.PAUSED:
            return paused()
        if self is WorkflowsListAllRequestStatus.COMPLETED:
            return completed()
        if self is WorkflowsListAllRequestStatus.CANCELLED:
            return cancelled()
