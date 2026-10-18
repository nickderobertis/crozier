

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListRunsHttpThreadsThreadIdRunsGetRequestStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    ERROR = "error"
    SUCCESS = "success"
    TIMEOUT = "timeout"
    INTERRUPTED = "interrupted"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        timeout: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.PENDING:
            return pending()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.RUNNING:
            return running()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.ERROR:
            return error()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.SUCCESS:
            return success()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.TIMEOUT:
            return timeout()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestStatus.INTERRUPTED:
            return interrupted()
