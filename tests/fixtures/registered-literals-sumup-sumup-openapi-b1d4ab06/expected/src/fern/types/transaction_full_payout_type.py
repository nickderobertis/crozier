

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionFullPayoutType(enum.StrEnum):
    """
    Payout type for the transaction.
    """

    BANK_ACCOUNT = "BANK_ACCOUNT"
    PREPAID_CARD = "PREPAID_CARD"

    def visit(
        self, bank_account: typing.Callable[[], T_Result], prepaid_card: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransactionFullPayoutType.BANK_ACCOUNT:
            return bank_account()
        if self is TransactionFullPayoutType.PREPAID_CARD:
            return prepaid_card()
