

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentScheduleInterval(enum.StrEnum):
    """
    The frequency interval of the payment.
    """

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

    def visit(self, weekly: typing.Callable[[], T_Result], monthly: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentScheduleInterval.WEEKLY:
            return weekly()
        if self is PaymentScheduleInterval.MONTHLY:
            return monthly()
