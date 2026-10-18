

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BulkUpdateFunctionBodyItemStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    REMOVED = "REMOVED"
    THROTTLED = "THROTTLED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        throttled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkUpdateFunctionBodyItemStatus.ACTIVE:
            return active()
        if self is BulkUpdateFunctionBodyItemStatus.REMOVED:
            return removed()
        if self is BulkUpdateFunctionBodyItemStatus.THROTTLED:
            return throttled()
