

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentUnit(enum.StrEnum):
    """
    Unit of measurement for employee compensation.
    """

    HOUR = "hour"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    PAYCHECK = "paycheck"

    def visit(
        self,
        hour: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
        paycheck: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentUnit.HOUR:
            return hour()
        if self is PaymentUnit.WEEK:
            return week()
        if self is PaymentUnit.MONTH:
            return month()
        if self is PaymentUnit.YEAR:
            return year()
        if self is PaymentUnit.PAYCHECK:
            return paycheck()
