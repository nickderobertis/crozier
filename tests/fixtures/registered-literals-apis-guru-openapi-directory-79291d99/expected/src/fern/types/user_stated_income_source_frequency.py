

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatedIncomeSourceFrequency(enum.StrEnum):
    """
    The pay frequency of a specified income source
    """

    UNKNOWN = "UNKNOWN"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        biweekly: typing.Callable[[], T_Result],
        semi_monthly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserStatedIncomeSourceFrequency.UNKNOWN:
            return unknown()
        if self is UserStatedIncomeSourceFrequency.WEEKLY:
            return weekly()
        if self is UserStatedIncomeSourceFrequency.BIWEEKLY:
            return biweekly()
        if self is UserStatedIncomeSourceFrequency.SEMI_MONTHLY:
            return semi_monthly()
        if self is UserStatedIncomeSourceFrequency.MONTHLY:
            return monthly()
