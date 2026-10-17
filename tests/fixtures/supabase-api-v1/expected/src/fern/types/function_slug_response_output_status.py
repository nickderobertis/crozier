

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionSlugResponseOutputStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    REMOVED = "REMOVED"
    THROTTLED = "THROTTLED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        throttled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionSlugResponseOutputStatus.ACTIVE:
            return active()
        if self is FunctionSlugResponseOutputStatus.REMOVED:
            return removed()
        if self is FunctionSlugResponseOutputStatus.THROTTLED:
            return throttled()
