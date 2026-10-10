

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsoBand(enum.StrEnum):
    LOW = "low"
    HIGH = "high"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsoBand.LOW:
            return low()
        if self is IsoBand.HIGH:
            return high()
