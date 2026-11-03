

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingDaysItem(enum.StrEnum):
    """ """

    WEEKDAY = "WEEKDAY"
    WEEKEND = "WEEKEND"

    def visit(self, weekday: typing.Callable[[], T_Result], weekend: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrossingDaysItem.WEEKDAY:
            return weekday()
        if self is CrossingDaysItem.WEEKEND:
            return weekend()
