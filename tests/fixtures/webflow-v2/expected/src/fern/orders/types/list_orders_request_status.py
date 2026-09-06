

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListOrdersRequestStatus(enum.StrEnum):
    PENDING = "pending"
    REFUNDED = "refunded"
    DISPUTE_LOST = "dispute-lost"
    FULFILLED = "fulfilled"
    DISPUTED = "disputed"
    UNFULFILLED = "unfulfilled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        dispute_lost: typing.Callable[[], T_Result],
        fulfilled: typing.Callable[[], T_Result],
        disputed: typing.Callable[[], T_Result],
        unfulfilled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListOrdersRequestStatus.PENDING:
            return pending()
        if self is ListOrdersRequestStatus.REFUNDED:
            return refunded()
        if self is ListOrdersRequestStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is ListOrdersRequestStatus.FULFILLED:
            return fulfilled()
        if self is ListOrdersRequestStatus.DISPUTED:
            return disputed()
        if self is ListOrdersRequestStatus.UNFULFILLED:
            return unfulfilled()
