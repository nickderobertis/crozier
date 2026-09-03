

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessStatusStatus(enum.StrEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessStatusStatus.ACTIVE:
            return active()
        if self is ProcessStatusStatus.COMPLETED:
            return completed()
        if self is ProcessStatusStatus.FAILED:
            return failed()
        if self is ProcessStatusStatus.CANCELLED:
            return cancelled()
