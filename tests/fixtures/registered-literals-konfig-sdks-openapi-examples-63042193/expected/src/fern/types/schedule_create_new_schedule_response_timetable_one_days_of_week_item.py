

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem(enum.StrEnum):
    """
    Day in a week, in three letters format
    """

    TUE = "TUE"
    SAT = "SAT"
    SUN = "SUN"
    MON = "MON"
    THU = "THU"
    WED = "WED"
    FRI = "FRI"

    def visit(
        self,
        tue: typing.Callable[[], T_Result],
        sat: typing.Callable[[], T_Result],
        sun: typing.Callable[[], T_Result],
        mon: typing.Callable[[], T_Result],
        thu: typing.Callable[[], T_Result],
        wed: typing.Callable[[], T_Result],
        fri: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.TUE:
            return tue()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.SAT:
            return sat()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.SUN:
            return sun()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.MON:
            return mon()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.THU:
            return thu()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.WED:
            return wed()
        if self is ScheduleCreateNewScheduleResponseTimetableOneDaysOfWeekItem.FRI:
            return fri()
