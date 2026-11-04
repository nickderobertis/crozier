

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleUpdateScheduleRequestTimetableMonthsItem(enum.StrEnum):
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
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.MAR:
            return mar()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.NOV:
            return nov()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.DEC:
            return dec()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.JUN:
            return jun()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.MAY:
            return may()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.OCT:
            return oct()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.FEB:
            return feb()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.APR:
            return apr()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.SEP:
            return sep()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.AUG:
            return aug()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.JAN:
            return jan()
        if self is ScheduleUpdateScheduleRequestTimetableMonthsItem.JUL:
            return jul()
