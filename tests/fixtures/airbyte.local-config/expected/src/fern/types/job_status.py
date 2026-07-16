

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    INCOMPLETE = "incomplete"
    FAILED = "failed"
    SUCCEEDED = "succeeded"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.PENDING:
            return pending()
        if self is JobStatus.RUNNING:
            return running()
        if self is JobStatus.INCOMPLETE:
            return incomplete()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.SUCCEEDED:
            return succeeded()
        if self is JobStatus.CANCELLED:
            return cancelled()
