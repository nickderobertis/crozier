

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAllWorkflowsRequestStatus(enum.StrEnum):
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
        if self is ListAllWorkflowsRequestStatus.ACTIVE:
            return active()
        if self is ListAllWorkflowsRequestStatus.PAUSED:
            return paused()
        if self is ListAllWorkflowsRequestStatus.COMPLETED:
            return completed()
        if self is ListAllWorkflowsRequestStatus.CANCELLED:
            return cancelled()
