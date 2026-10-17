

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1BackupsResponseOutputBackupsItemStatus(enum.StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    REMOVED = "REMOVED"
    ARCHIVED = "ARCHIVED"
    CANCELLED = "CANCELLED"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1BackupsResponseOutputBackupsItemStatus.COMPLETED:
            return completed()
        if self is V1BackupsResponseOutputBackupsItemStatus.FAILED:
            return failed()
        if self is V1BackupsResponseOutputBackupsItemStatus.PENDING:
            return pending()
        if self is V1BackupsResponseOutputBackupsItemStatus.REMOVED:
            return removed()
        if self is V1BackupsResponseOutputBackupsItemStatus.ARCHIVED:
            return archived()
        if self is V1BackupsResponseOutputBackupsItemStatus.CANCELLED:
            return cancelled()
