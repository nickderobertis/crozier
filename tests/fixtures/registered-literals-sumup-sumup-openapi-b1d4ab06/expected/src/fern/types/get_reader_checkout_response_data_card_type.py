

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetReaderCheckoutResponseDataCardType(enum.StrEnum):
    """
    Type of the card. Required for some countries
    """

    CREDIT = "credit"
    DEBIT = "debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetReaderCheckoutResponseDataCardType.CREDIT:
            return credit()
        if self is GetReaderCheckoutResponseDataCardType.DEBIT:
            return debit()
