

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BasicProgramOccurenceDayItem(enum.StrEnum):
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
        if self is BasicProgramOccurenceDayItem.MON:
            return mon()
        if self is BasicProgramOccurenceDayItem.TUE:
            return tue()
        if self is BasicProgramOccurenceDayItem.WED:
            return wed()
        if self is BasicProgramOccurenceDayItem.THU:
            return thu()
        if self is BasicProgramOccurenceDayItem.FRI:
            return fri()
        if self is BasicProgramOccurenceDayItem.SAT:
            return sat()
        if self is BasicProgramOccurenceDayItem.SUN:
            return sun()
