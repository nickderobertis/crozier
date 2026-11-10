

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferIntentCreateMode(enum.StrEnum):
    """
    The direction of the flow of transfer funds.

    `PAYMENT`: Transfers funds from an end user's account to your business account.

    `DISBURSEMENT`: Transfers funds from your business account to an end user's account.
    """

    PAYMENT = "PAYMENT"
    DISBURSEMENT = "DISBURSEMENT"

    def visit(self, payment: typing.Callable[[], T_Result], disbursement: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferIntentCreateMode.PAYMENT:
            return payment()
        if self is TransferIntentCreateMode.DISBURSEMENT:
            return disbursement()
