

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Pitch(enum.StrEnum):
    LOW = "low"
    HIGH = "high"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is Pitch.LOW:
            return low()
        if self is Pitch.HIGH:
            return high()
