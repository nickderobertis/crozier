

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PortfolioSyncResponseStatus(enum.StrEnum):
    INITIATED = "initiated"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        initiated: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PortfolioSyncResponseStatus.INITIATED:
            return initiated()
        if self is PortfolioSyncResponseStatus.IN_PROGRESS:
            return in_progress()
        if self is PortfolioSyncResponseStatus.COMPLETED:
            return completed()
        if self is PortfolioSyncResponseStatus.FAILED:
            return failed()
