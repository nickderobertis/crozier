

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorStatus(enum.StrEnum):
    RUNNING = "Running"
    PAUSED = "Paused"
    FAILED = "Failed"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitorStatus.RUNNING:
            return running()
        if self is MonitorStatus.PAUSED:
            return paused()
        if self is MonitorStatus.FAILED:
            return failed()
