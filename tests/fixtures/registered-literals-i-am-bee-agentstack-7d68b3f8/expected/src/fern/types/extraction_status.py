

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionStatus(enum.StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionStatus.PENDING:
            return pending()
        if self is ExtractionStatus.IN_PROGRESS:
            return in_progress()
        if self is ExtractionStatus.COMPLETED:
            return completed()
        if self is ExtractionStatus.FAILED:
            return failed()
        if self is ExtractionStatus.CANCELLED:
            return cancelled()
