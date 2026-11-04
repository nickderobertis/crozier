

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateReaderCheckoutRequestCardType(enum.StrEnum):
    """
    The card type of the card used for the transaction.
    Is is required only for some countries (e.g: Brazil).
    """

    CREDIT = "credit"
    DEBIT = "debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateReaderCheckoutRequestCardType.CREDIT:
            return credit()
        if self is CreateReaderCheckoutRequestCardType.DEBIT:
            return debit()
