

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleUpdateScheduleResponseTimetableOneMonthsItem(enum.StrEnum):
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
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.MAR:
            return mar()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.NOV:
            return nov()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.DEC:
            return dec()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.JUN:
            return jun()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.MAY:
            return may()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.OCT:
            return oct()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.FEB:
            return feb()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.APR:
            return apr()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.SEP:
            return sep()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.AUG:
            return aug()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.JAN:
            return jan()
        if self is ScheduleUpdateScheduleResponseTimetableOneMonthsItem.JUL:
            return jul()
