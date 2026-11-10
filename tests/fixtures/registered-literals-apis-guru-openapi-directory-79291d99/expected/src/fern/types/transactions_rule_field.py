

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionsRuleField(enum.StrEnum):
    """
    Transaction field for which the rule is defined.
    """

    TRANSACTION_ID = "TRANSACTION_ID"
    NAME = "NAME"

    def visit(self, transaction_id: typing.Callable[[], T_Result], name: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionsRuleField.TRANSACTION_ID:
            return transaction_id()
        if self is TransactionsRuleField.NAME:
            return name()
