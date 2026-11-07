

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInteractionKind(enum.StrEnum):
    PAYMENT = "payment"

    def visit(self, payment: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentInteractionKind.PAYMENT:
            return payment()
