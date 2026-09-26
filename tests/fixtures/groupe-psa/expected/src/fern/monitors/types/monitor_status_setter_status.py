

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorStatusSetterStatus(enum.StrEnum):
    RUNNING = "Running"
    PAUSED = "Paused"

    def visit(self, running: typing.Callable[[], T_Result], paused: typing.Callable[[], T_Result]) -> T_Result:
        if self is MonitorStatusSetterStatus.RUNNING:
            return running()
        if self is MonitorStatusSetterStatus.PAUSED:
            return paused()
