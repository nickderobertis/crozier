

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WeekDayDay(enum.StrEnum):
    SU = "SU"
    MO = "MO"
    TU = "TU"
    WE = "WE"
    TH = "TH"
    FR = "FR"
    SA = "SA"

    def visit(
        self,
        su: typing.Callable[[], T_Result],
        mo: typing.Callable[[], T_Result],
        tu: typing.Callable[[], T_Result],
        we: typing.Callable[[], T_Result],
        th: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WeekDayDay.SU:
            return su()
        if self is WeekDayDay.MO:
            return mo()
        if self is WeekDayDay.TU:
            return tu()
        if self is WeekDayDay.WE:
            return we()
        if self is WeekDayDay.TH:
            return th()
        if self is WeekDayDay.FR:
            return fr()
        if self is WeekDayDay.SA:
            return sa()
