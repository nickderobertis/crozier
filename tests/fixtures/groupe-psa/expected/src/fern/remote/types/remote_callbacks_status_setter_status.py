

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteCallbacksStatusSetterStatus(enum.StrEnum):
    RUNNING = "Running"
    PAUSED = "Paused"

    def visit(self, running: typing.Callable[[], T_Result], paused: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteCallbacksStatusSetterStatus.RUNNING:
            return running()
        if self is RemoteCallbacksStatusSetterStatus.PAUSED:
            return paused()
