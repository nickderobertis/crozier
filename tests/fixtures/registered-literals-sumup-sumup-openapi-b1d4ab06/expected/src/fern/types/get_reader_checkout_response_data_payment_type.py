

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetReaderCheckoutResponseDataPaymentType(enum.StrEnum):
    """
    Type of the payment. Required for some countries
    """

    CARD = "card"
    PIX = "pix"

    def visit(self, card: typing.Callable[[], T_Result], pix: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetReaderCheckoutResponseDataPaymentType.CARD:
            return card()
        if self is GetReaderCheckoutResponseDataPaymentType.PIX:
            return pix()
