

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    """
    The status of the run. One of 'pending', 'error', 'success', 'timeout', 'interrupted'.
    """

    PENDING = "pending"
    ERROR = "error"
    SUCCESS = "success"
    TIMEOUT = "timeout"
    INTERRUPTED = "interrupted"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        timeout: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.PENDING:
            return pending()
        if self is RunStatus.ERROR:
            return error()
        if self is RunStatus.SUCCESS:
            return success()
        if self is RunStatus.TIMEOUT:
            return timeout()
        if self is RunStatus.INTERRUPTED:
            return interrupted()
