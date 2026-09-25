

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallbackStatus(enum.StrEnum):
    RUNNING = "Running"
    PAUSED = "Paused"
    FAILED = "Failed"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallbackStatus.RUNNING:
            return running()
        if self is CallbackStatus.PAUSED:
            return paused()
        if self is CallbackStatus.FAILED:
            return failed()
