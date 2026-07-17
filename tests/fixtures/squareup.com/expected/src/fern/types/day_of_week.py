

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DayOfWeek(enum.StrEnum):
    """
    Indicates the specific day  of the week.
    """

    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"

    def visit(
        self,
        sun: typing.Callable[[], T_Result],
        mon: typing.Callable[[], T_Result],
        tue: typing.Callable[[], T_Result],
        wed: typing.Callable[[], T_Result],
        thu: typing.Callable[[], T_Result],
        fri: typing.Callable[[], T_Result],
        sat: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DayOfWeek.SUN:
            return sun()
        if self is DayOfWeek.MON:
            return mon()
        if self is DayOfWeek.TUE:
            return tue()
        if self is DayOfWeek.WED:
            return wed()
        if self is DayOfWeek.THU:
            return thu()
        if self is DayOfWeek.FRI:
            return fri()
        if self is DayOfWeek.SAT:
            return sat()
