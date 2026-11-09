

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookType(enum.StrEnum):
    """
    The webhook types that can be fired by this test endpoint.
    """

    AUTH = "AUTH"
    HOLDINGS = "HOLDINGS"
    INVESTMENTS_TRANSACTIONS = "INVESTMENTS_TRANSACTIONS"
    ITEM = "ITEM"
    LIABILITIES = "LIABILITIES"
    TRANSACTIONS = "TRANSACTIONS"

    def visit(
        self,
        auth: typing.Callable[[], T_Result],
        holdings: typing.Callable[[], T_Result],
        investments_transactions: typing.Callable[[], T_Result],
        item: typing.Callable[[], T_Result],
        liabilities: typing.Callable[[], T_Result],
        transactions: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookType.AUTH:
            return auth()
        if self is WebhookType.HOLDINGS:
            return holdings()
        if self is WebhookType.INVESTMENTS_TRANSACTIONS:
            return investments_transactions()
        if self is WebhookType.ITEM:
            return item()
        if self is WebhookType.LIABILITIES:
            return liabilities()
        if self is WebhookType.TRANSACTIONS:
            return transactions()
