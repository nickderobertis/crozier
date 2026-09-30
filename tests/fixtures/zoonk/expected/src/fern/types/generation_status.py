

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerationStatus.PENDING:
            return pending()
        if self is GenerationStatus.RUNNING:
            return running()
        if self is GenerationStatus.COMPLETED:
            return completed()
        if self is GenerationStatus.FAILED:
            return failed()
        if self is GenerationStatus.CANCELLED:
            return cancelled()
