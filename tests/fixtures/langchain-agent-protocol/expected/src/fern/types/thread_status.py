

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadStatus(enum.StrEnum):
    """
    The status of the thread. One of 'idle', 'busy', 'interrupted', 'error'.
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
        if self is ThreadStatus.IDLE:
            return idle()
        if self is ThreadStatus.BUSY:
            return busy()
        if self is ThreadStatus.INTERRUPTED:
            return interrupted()
        if self is ThreadStatus.ERROR:
            return error()
