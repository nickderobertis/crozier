

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Shift(enum.StrEnum):
    EARLY = "early"
    LATE = "late"

    def visit(self, early: typing.Callable[[], T_Result], late: typing.Callable[[], T_Result]) -> T_Result:
        if self is Shift.EARLY:
            return early()
        if self is Shift.LATE:
            return late()
