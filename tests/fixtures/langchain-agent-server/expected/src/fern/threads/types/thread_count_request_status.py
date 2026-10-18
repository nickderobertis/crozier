

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadCountRequestStatus(enum.StrEnum):
    """
    Thread status to filter on.
    """

    IDLE = "idle"
    BUSY = "busy"
    INTERRUPTED = "interrupted"
    ERROR = "error"

    def visit(
        self,
        idle: typing.Callable[[], T_Result],
        busy: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThreadCountRequestStatus.IDLE:
            return idle()
        if self is ThreadCountRequestStatus.BUSY:
            return busy()
        if self is ThreadCountRequestStatus.INTERRUPTED:
            return interrupted()
        if self is ThreadCountRequestStatus.ERROR:
            return error()
