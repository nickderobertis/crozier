

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeTriggerEntryOccurenceDayItem(enum.StrEnum):
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
        if self is TimeTriggerEntryOccurenceDayItem.MON:
            return mon()
        if self is TimeTriggerEntryOccurenceDayItem.TUE:
            return tue()
        if self is TimeTriggerEntryOccurenceDayItem.WED:
            return wed()
        if self is TimeTriggerEntryOccurenceDayItem.THU:
            return thu()
        if self is TimeTriggerEntryOccurenceDayItem.FRI:
            return fri()
        if self is TimeTriggerEntryOccurenceDayItem.SAT:
            return sat()
        if self is TimeTriggerEntryOccurenceDayItem.SUN:
            return sun()
