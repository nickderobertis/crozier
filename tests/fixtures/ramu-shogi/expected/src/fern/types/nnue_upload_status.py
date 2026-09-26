

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NnueUploadStatus(enum.StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    DELETED = "deleted"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NnueUploadStatus.PENDING:
            return pending()
        if self is NnueUploadStatus.COMPLETED:
            return completed()
        if self is NnueUploadStatus.FAILED:
            return failed()
        if self is NnueUploadStatus.DELETED:
            return deleted()
