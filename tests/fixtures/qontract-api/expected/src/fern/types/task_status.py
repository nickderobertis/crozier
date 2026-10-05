

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskStatus(enum.StrEnum):
    """
    Status for background tasks.

    Used across all async API endpoints to indicate task execution state.
    """

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskStatus.PENDING:
            return pending()
        if self is TaskStatus.SUCCESS:
            return success()
        if self is TaskStatus.FAILED:
            return failed()
        if self is TaskStatus.SKIPPED:
            return skipped()
