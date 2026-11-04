

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Temporal(enum.StrEnum):
    """
    An enumeration.
    """

    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    MOY = "moy"
    DOW = "dow"
    HOUR = "hour"
    HOD = "hod"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
        moy: typing.Callable[[], T_Result],
        dow: typing.Callable[[], T_Result],
        hour: typing.Callable[[], T_Result],
        hod: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Temporal.DAY:
            return day()
        if self is Temporal.MONTH:
            return month()
        if self is Temporal.YEAR:
            return year()
        if self is Temporal.MOY:
            return moy()
        if self is Temporal.DOW:
            return dow()
        if self is Temporal.HOUR:
            return hour()
        if self is Temporal.HOD:
            return hod()
