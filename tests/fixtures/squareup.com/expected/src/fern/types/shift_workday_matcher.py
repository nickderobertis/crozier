

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShiftWorkdayMatcher(enum.StrEnum):
    """
    Defines the logic used to apply a workday filter.
    """

    START_AT = "START_AT"
    END_AT = "END_AT"
    INTERSECTION = "INTERSECTION"

    def visit(
        self,
        start_at: typing.Callable[[], T_Result],
        end_at: typing.Callable[[], T_Result],
        intersection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShiftWorkdayMatcher.START_AT:
            return start_at()
        if self is ShiftWorkdayMatcher.END_AT:
            return end_at()
        if self is ShiftWorkdayMatcher.INTERSECTION:
            return intersection()
