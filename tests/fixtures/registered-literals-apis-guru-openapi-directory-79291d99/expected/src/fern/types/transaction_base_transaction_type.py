

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionBaseTransactionType(enum.StrEnum):
    """
    Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.

    `digital:` transactions that took place online.

    `place:` transactions that were made at a physical location.

    `special:` transactions that relate to banks, e.g. fees or deposits.

    `unresolved:` transactions that do not fit into the other three types.
    """

    DIGITAL = "digital"
    PLACE = "place"
    SPECIAL = "special"
    UNRESOLVED = "unresolved"

    def visit(
        self,
        digital: typing.Callable[[], T_Result],
        place: typing.Callable[[], T_Result],
        special: typing.Callable[[], T_Result],
        unresolved: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionBaseTransactionType.DIGITAL:
            return digital()
        if self is TransactionBaseTransactionType.PLACE:
            return place()
        if self is TransactionBaseTransactionType.SPECIAL:
            return special()
        if self is TransactionBaseTransactionType.UNRESOLVED:
            return unresolved()
