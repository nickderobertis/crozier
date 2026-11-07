

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileStatus(enum.StrEnum):
    ACTIVE = "active"
    TRASHED = "trashed"
    SPAM = "spam"
    DELETION_PENDING = "deletion_pending"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        trashed: typing.Callable[[], T_Result],
        spam: typing.Callable[[], T_Result],
        deletion_pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileStatus.ACTIVE:
            return active()
        if self is FileStatus.TRASHED:
            return trashed()
        if self is FileStatus.SPAM:
            return spam()
        if self is FileStatus.DELETION_PENDING:
            return deletion_pending()
