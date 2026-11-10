

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInitiationPaymentCreateStatus(enum.StrEnum):
    """
    For a payment returned by this endpoint, there is only one possible value:

    `PAYMENT_STATUS_INPUT_NEEDED`: The initial phase of the payment
    """

    PAYMENT_STATUS_INPUT_NEEDED = "PAYMENT_STATUS_INPUT_NEEDED"

    def visit(self, payment_status_input_needed: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentInitiationPaymentCreateStatus.PAYMENT_STATUS_INPUT_NEEDED:
            return payment_status_input_needed()
