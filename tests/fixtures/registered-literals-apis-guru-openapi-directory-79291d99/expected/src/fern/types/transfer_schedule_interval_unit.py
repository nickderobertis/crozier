

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferScheduleIntervalUnit(enum.StrEnum):
    """
    The unit of the recurring interval.
    """

    WEEK = "week"
    MONTH = "month"

    def visit(self, week: typing.Callable[[], T_Result], month: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferScheduleIntervalUnit.WEEK:
            return week()
        if self is TransferScheduleIntervalUnit.MONTH:
            return month()
