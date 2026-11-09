

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CancelAsyncSearchDtoCurrentSearchJobStatus(enum.StrEnum):
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    SUCCESSFUL = "SUCCESSFUL"
    NOT_FOUND = "NOT_FOUND"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        successful: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CancelAsyncSearchDtoCurrentSearchJobStatus.RUNNING:
            return running()
        if self is CancelAsyncSearchDtoCurrentSearchJobStatus.FAILED:
            return failed()
        if self is CancelAsyncSearchDtoCurrentSearchJobStatus.CANCELLED:
            return cancelled()
        if self is CancelAsyncSearchDtoCurrentSearchJobStatus.SUCCESSFUL:
            return successful()
        if self is CancelAsyncSearchDtoCurrentSearchJobStatus.NOT_FOUND:
            return not_found()
