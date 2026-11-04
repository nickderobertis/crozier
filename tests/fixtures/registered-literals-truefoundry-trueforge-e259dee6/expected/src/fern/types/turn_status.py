

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TurnStatus(enum.StrEnum):
    RUNNING = "running"
    PAUSED = "paused"
    DONE = "done"
    CANCELLED = "cancelled"
    ERROR = "error"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TurnStatus.RUNNING:
            return running()
        if self is TurnStatus.PAUSED:
            return paused()
        if self is TurnStatus.DONE:
            return done()
        if self is TurnStatus.CANCELLED:
            return cancelled()
        if self is TurnStatus.ERROR:
            return error()
