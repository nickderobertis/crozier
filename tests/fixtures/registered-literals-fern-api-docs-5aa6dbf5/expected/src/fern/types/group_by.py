

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupBy(enum.StrEnum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GroupBy.DAY:
            return day()
        if self is GroupBy.WEEK:
            return week()
        if self is GroupBy.MONTH:
            return month()
