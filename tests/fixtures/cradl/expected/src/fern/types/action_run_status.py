

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionRunStatus(enum.StrEnum):
    FAILED = "failed"
    IGNORED = "ignored"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def visit(
        self,
        failed: typing.Callable[[], T_Result],
        ignored: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionRunStatus.FAILED:
            return failed()
        if self is ActionRunStatus.IGNORED:
            return ignored()
        if self is ActionRunStatus.RUNNING:
            return running()
        if self is ActionRunStatus.SUCCEEDED:
            return succeeded()
