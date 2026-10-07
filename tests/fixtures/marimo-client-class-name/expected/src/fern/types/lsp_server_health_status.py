

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LspServerHealthStatus(enum.StrEnum):
    CRASHED = "crashed"
    RUNNING = "running"
    STARTING = "starting"
    STOPPED = "stopped"
    UNRESPONSIVE = "unresponsive"

    def visit(
        self,
        crashed: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        unresponsive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LspServerHealthStatus.CRASHED:
            return crashed()
        if self is LspServerHealthStatus.RUNNING:
            return running()
        if self is LspServerHealthStatus.STARTING:
            return starting()
        if self is LspServerHealthStatus.STOPPED:
            return stopped()
        if self is LspServerHealthStatus.UNRESPONSIVE:
            return unresponsive()
