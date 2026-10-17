

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1RestorePointResponseStatus(enum.StrEnum):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    REMOVED = "REMOVED"
    FAILED = "FAILED"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1RestorePointResponseStatus.AVAILABLE:
            return available()
        if self is V1RestorePointResponseStatus.PENDING:
            return pending()
        if self is V1RestorePointResponseStatus.REMOVED:
            return removed()
        if self is V1RestorePointResponseStatus.FAILED:
            return failed()
