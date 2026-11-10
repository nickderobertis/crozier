

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentConsentPeriodicAlignment(enum.StrEnum):
    """
    Where the payment consent period should start.

    `CALENDAR`: line up with a calendar.

    `CONSENT`: on the date of consent creation.
    """

    CALENDAR = "CALENDAR"
    CONSENT = "CONSENT"

    def visit(self, calendar: typing.Callable[[], T_Result], consent: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentConsentPeriodicAlignment.CALENDAR:
            return calendar()
        if self is PaymentConsentPeriodicAlignment.CONSENT:
            return consent()
