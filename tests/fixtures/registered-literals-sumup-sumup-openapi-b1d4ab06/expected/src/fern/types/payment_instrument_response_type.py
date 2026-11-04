

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInstrumentResponseType(enum.StrEnum):
    """
    Type of the payment instrument.
    """

    CARD = "card"

    def visit(self, card: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentInstrumentResponseType.CARD:
            return card()
