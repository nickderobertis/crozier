

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AsyncSearchStatusDtoSearchJobStatus(enum.StrEnum):
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
        if self is AsyncSearchStatusDtoSearchJobStatus.RUNNING:
            return running()
        if self is AsyncSearchStatusDtoSearchJobStatus.FAILED:
            return failed()
        if self is AsyncSearchStatusDtoSearchJobStatus.CANCELLED:
            return cancelled()
        if self is AsyncSearchStatusDtoSearchJobStatus.SUCCESSFUL:
            return successful()
        if self is AsyncSearchStatusDtoSearchJobStatus.NOT_FOUND:
            return not_found()
