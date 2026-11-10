

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionsRuleType(enum.StrEnum):
    """
    Transaction rule's match type. For TRANSACTION_ID field, EXACT_MATCH is available.
    Matches are case sensitive.
    """

    EXACT_MATCH = "EXACT_MATCH"
    SUBSTRING_MATCH = "SUBSTRING_MATCH"

    def visit(
        self, exact_match: typing.Callable[[], T_Result], substring_match: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransactionsRuleType.EXACT_MATCH:
            return exact_match()
        if self is TransactionsRuleType.SUBSTRING_MATCH:
            return substring_match()
