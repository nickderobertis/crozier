

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelativeFormQueryTimeUnit(enum.StrEnum):
    DAYS = "DAYS"
    QUARTERS = "QUARTERS"
    YEARS = "YEARS"

    def visit(
        self,
        days: typing.Callable[[], T_Result],
        quarters: typing.Callable[[], T_Result],
        years: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelativeFormQueryTimeUnit.DAYS:
            return days()
        if self is RelativeFormQueryTimeUnit.QUARTERS:
            return quarters()
        if self is RelativeFormQueryTimeUnit.YEARS:
            return years()
