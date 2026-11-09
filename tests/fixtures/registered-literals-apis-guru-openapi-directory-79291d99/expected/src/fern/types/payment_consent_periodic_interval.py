

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentConsentPeriodicInterval(enum.StrEnum):
    """
    Payment consent periodic interval.
    """

    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentConsentPeriodicInterval.DAY:
            return day()
        if self is PaymentConsentPeriodicInterval.WEEK:
            return week()
        if self is PaymentConsentPeriodicInterval.MONTH:
            return month()
        if self is PaymentConsentPeriodicInterval.YEAR:
            return year()
