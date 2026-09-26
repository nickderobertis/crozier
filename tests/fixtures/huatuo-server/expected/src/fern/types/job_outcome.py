

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobOutcome(enum.StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    STOPPED = "stopped"
    UNKNOWN = "unknown"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobOutcome.COMPLETED:
            return completed()
        if self is JobOutcome.FAILED:
            return failed()
        if self is JobOutcome.STOPPED:
            return stopped()
        if self is JobOutcome.UNKNOWN:
            return unknown()
