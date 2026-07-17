

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationStatus(enum.StrEnum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    QUEUED = "QUEUED"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetOperationStatus.RUNNING:
            return running()
        if self is StackSetOperationStatus.SUCCEEDED:
            return succeeded()
        if self is StackSetOperationStatus.FAILED:
            return failed()
        if self is StackSetOperationStatus.STOPPING:
            return stopping()
        if self is StackSetOperationStatus.STOPPED:
            return stopped()
        if self is StackSetOperationStatus.QUEUED:
            return queued()
