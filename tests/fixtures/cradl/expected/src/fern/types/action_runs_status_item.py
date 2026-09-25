

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionRunsStatusItem(enum.StrEnum):
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
        if self is ActionRunsStatusItem.FAILED:
            return failed()
        if self is ActionRunsStatusItem.IGNORED:
            return ignored()
        if self is ActionRunsStatusItem.RUNNING:
            return running()
        if self is ActionRunsStatusItem.SUCCEEDED:
            return succeeded()
