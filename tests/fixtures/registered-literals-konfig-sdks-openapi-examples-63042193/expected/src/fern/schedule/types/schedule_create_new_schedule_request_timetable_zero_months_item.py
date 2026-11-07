

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem(enum.StrEnum):
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
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.MAR:
            return mar()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.NOV:
            return nov()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.DEC:
            return dec()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.JUN:
            return jun()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.MAY:
            return may()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.OCT:
            return oct()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.FEB:
            return feb()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.APR:
            return apr()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.SEP:
            return sep()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.AUG:
            return aug()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.JAN:
            return jan()
        if self is ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem.JUL:
            return jul()
