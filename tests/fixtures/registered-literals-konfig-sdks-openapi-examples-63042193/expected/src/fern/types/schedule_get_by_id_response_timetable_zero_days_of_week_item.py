

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem(enum.StrEnum):
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
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.TUE:
            return tue()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.SAT:
            return sat()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.SUN:
            return sun()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.MON:
            return mon()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.THU:
            return thu()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.WED:
            return wed()
        if self is ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem.FRI:
            return fri()
