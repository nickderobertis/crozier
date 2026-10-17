

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadSearchRequestStatus(enum.StrEnum):
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
        if self is ThreadSearchRequestStatus.IDLE:
            return idle()
        if self is ThreadSearchRequestStatus.BUSY:
            return busy()
        if self is ThreadSearchRequestStatus.INTERRUPTED:
            return interrupted()
        if self is ThreadSearchRequestStatus.ERROR:
            return error()
