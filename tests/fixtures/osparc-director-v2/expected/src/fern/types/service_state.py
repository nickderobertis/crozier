

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceState(enum.StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    PULLING = "pulling"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    COMPLETE = "complete"
    IDLE = "idle"

    def visit(
        self,
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        pulling: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        idle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceState.FAILED:
            return failed()
        if self is ServiceState.PENDING:
            return pending()
        if self is ServiceState.PULLING:
            return pulling()
        if self is ServiceState.STARTING:
            return starting()
        if self is ServiceState.RUNNING:
            return running()
        if self is ServiceState.STOPPING:
            return stopping()
        if self is ServiceState.COMPLETE:
            return complete()
        if self is ServiceState.IDLE:
            return idle()
