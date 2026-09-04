

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobHistorySummaryState(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobHistorySummaryState.PENDING:
            return pending()
        if self is JobHistorySummaryState.RUNNING:
            return running()
        if self is JobHistorySummaryState.SUCCESS:
            return success()
        if self is JobHistorySummaryState.ERROR:
            return error()
        if self is JobHistorySummaryState.CANCELLED:
            return cancelled()
