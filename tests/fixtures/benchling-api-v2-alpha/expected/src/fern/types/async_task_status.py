

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AsyncTaskStatus(enum.StrEnum):
    """
    The current state of the task.
    """

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AsyncTaskStatus.RUNNING:
            return running()
        if self is AsyncTaskStatus.SUCCEEDED:
            return succeeded()
        if self is AsyncTaskStatus.FAILED:
            return failed()
