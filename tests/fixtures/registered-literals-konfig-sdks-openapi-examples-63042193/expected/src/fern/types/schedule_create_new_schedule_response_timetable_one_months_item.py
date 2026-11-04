

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleCreateNewScheduleResponseTimetableOneMonthsItem(enum.StrEnum):
    """
    Month, in three letters format.
    """

    MAR = "MAR"
    NOV = "NOV"
    DEC = "DEC"
    JUN = "JUN"
    MAY = "MAY"
    OCT = "OCT"
    FEB = "FEB"
    APR = "APR"
    SEP = "SEP"
    AUG = "AUG"
    JAN = "JAN"
    JUL = "JUL"

    def visit(
        self,
        mar: typing.Callable[[], T_Result],
        nov: typing.Callable[[], T_Result],
        dec: typing.Callable[[], T_Result],
        jun: typing.Callable[[], T_Result],
        may: typing.Callable[[], T_Result],
        oct: typing.Callable[[], T_Result],
        feb: typing.Callable[[], T_Result],
        apr: typing.Callable[[], T_Result],
        sep: typing.Callable[[], T_Result],
        aug: typing.Callable[[], T_Result],
        jan: typing.Callable[[], T_Result],
        jul: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.MAR:
            return mar()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.NOV:
            return nov()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.DEC:
            return dec()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.JUN:
            return jun()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.MAY:
            return may()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.OCT:
            return oct()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.FEB:
            return feb()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.APR:
            return apr()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.SEP:
            return sep()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.AUG:
            return aug()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.JAN:
            return jan()
        if self is ScheduleCreateNewScheduleResponseTimetableOneMonthsItem.JUL:
            return jul()
