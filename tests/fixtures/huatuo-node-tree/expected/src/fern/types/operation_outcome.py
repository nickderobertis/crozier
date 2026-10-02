

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperationOutcome(enum.StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    STOPPED = "stopped"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperationOutcome.COMPLETED:
            return completed()
        if self is OperationOutcome.FAILED:
            return failed()
        if self is OperationOutcome.STOPPED:
            return stopped()
