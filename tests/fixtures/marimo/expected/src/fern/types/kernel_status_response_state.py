

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KernelStatusResponseState(enum.StrEnum):
    IDLE = "idle"
    RUNNING = "running"
    STOPPED = "stopped"

    def visit(
        self,
        idle: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KernelStatusResponseState.IDLE:
            return idle()
        if self is KernelStatusResponseState.RUNNING:
            return running()
        if self is KernelStatusResponseState.STOPPED:
            return stopped()
