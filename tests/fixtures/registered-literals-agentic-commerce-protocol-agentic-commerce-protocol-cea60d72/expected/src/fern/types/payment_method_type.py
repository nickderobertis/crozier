

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentMethodType(enum.StrEnum):
    CARD = "card"

    def visit(self, card: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentMethodType.CARD:
            return card()
