

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoMessageCategory(enum.StrEnum):
    """
    Identifies the category of the message for a specific use case. Possible values:

    * **payment**
    * **nonPayment**
    """

    PAYMENT = "payment"
    NON_PAYMENT = "nonPayment"

    def visit(self, payment: typing.Callable[[], T_Result], non_payment: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationInfoMessageCategory.PAYMENT:
            return payment()
        if self is AuthenticationInfoMessageCategory.NON_PAYMENT:
            return non_payment()
