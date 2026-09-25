

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProgramOccurenceDayItem(enum.StrEnum):
    MON = "Mon"
    TUE = "Tue"
    WED = "Wed"
    THU = "Thu"
    FRI = "Fri"
    SAT = "Sat"
    SUN = "Sun"

    def visit(
        self,
        mon: typing.Callable[[], T_Result],
        tue: typing.Callable[[], T_Result],
        wed: typing.Callable[[], T_Result],
        thu: typing.Callable[[], T_Result],
        fri: typing.Callable[[], T_Result],
        sat: typing.Callable[[], T_Result],
        sun: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProgramOccurenceDayItem.MON:
            return mon()
        if self is ProgramOccurenceDayItem.TUE:
            return tue()
        if self is ProgramOccurenceDayItem.WED:
            return wed()
        if self is ProgramOccurenceDayItem.THU:
            return thu()
        if self is ProgramOccurenceDayItem.FRI:
            return fri()
        if self is ProgramOccurenceDayItem.SAT:
            return sat()
        if self is ProgramOccurenceDayItem.SUN:
            return sun()
