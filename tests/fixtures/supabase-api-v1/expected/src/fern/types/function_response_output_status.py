

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionResponseOutputStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    REMOVED = "REMOVED"
    THROTTLED = "THROTTLED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        throttled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionResponseOutputStatus.ACTIVE:
            return active()
        if self is FunctionResponseOutputStatus.REMOVED:
            return removed()
        if self is FunctionResponseOutputStatus.THROTTLED:
            return throttled()
