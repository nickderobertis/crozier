

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    """
    Status of the job.
    """

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.CREATED:
            return created()
        if self is JobStatus.RUNNING:
            return running()
        if self is JobStatus.COMPLETED:
            return completed()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.PENDING:
            return pending()
        if self is JobStatus.CANCELLED:
            return cancelled()
        if self is JobStatus.EXPIRED:
            return expired()
