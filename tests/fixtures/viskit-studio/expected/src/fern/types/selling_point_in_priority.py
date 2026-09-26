

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SellingPointInPriority(enum.StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SellingPointInPriority.HIGH:
            return high()
        if self is SellingPointInPriority.MEDIUM:
            return medium()
        if self is SellingPointInPriority.LOW:
            return low()
