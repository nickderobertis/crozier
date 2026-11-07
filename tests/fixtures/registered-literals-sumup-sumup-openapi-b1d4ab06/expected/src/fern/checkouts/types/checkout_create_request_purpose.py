

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CheckoutCreateRequestPurpose(enum.StrEnum):
    """
    Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.
    """

    CHECKOUT = "CHECKOUT"
    SETUP_RECURRING_PAYMENT = "SETUP_RECURRING_PAYMENT"

    def visit(
        self, checkout: typing.Callable[[], T_Result], setup_recurring_payment: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CheckoutCreateRequestPurpose.CHECKOUT:
            return checkout()
        if self is CheckoutCreateRequestPurpose.SETUP_RECURRING_PAYMENT:
            return setup_recurring_payment()
