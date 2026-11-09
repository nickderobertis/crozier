

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessStatus(enum.StrEnum):
    STARTING = "starting"
    RUNNING = "running"
    DRAINING = "draining"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"

    def visit(
        self,
        starting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        draining: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessStatus.STARTING:
            return starting()
        if self is ProcessStatus.RUNNING:
            return running()
        if self is ProcessStatus.DRAINING:
            return draining()
        if self is ProcessStatus.STOPPING:
            return stopping()
        if self is ProcessStatus.STOPPED:
            return stopped()
        if self is ProcessStatus.FAILED:
            return failed()
