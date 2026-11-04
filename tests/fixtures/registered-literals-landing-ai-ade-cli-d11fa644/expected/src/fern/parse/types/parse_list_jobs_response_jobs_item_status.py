

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParseListJobsResponseJobsItemStatus(enum.StrEnum):
    """
    The job's current status: ``pending``, ``processing``, ``completed``, or ``failed``.
    """

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParseListJobsResponseJobsItemStatus.PENDING:
            return pending()
        if self is ParseListJobsResponseJobsItemStatus.PROCESSING:
            return processing()
        if self is ParseListJobsResponseJobsItemStatus.COMPLETED:
            return completed()
        if self is ParseListJobsResponseJobsItemStatus.FAILED:
            return failed()
