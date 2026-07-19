

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    """
    Status of the run.
    """

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.CREATED:
            return created()
        if self is RunStatus.RUNNING:
            return running()
        if self is RunStatus.COMPLETED:
            return completed()
        if self is RunStatus.FAILED:
            return failed()
        if self is RunStatus.CANCELLED:
            return cancelled()
