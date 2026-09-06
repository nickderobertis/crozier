

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetOrdersResponseStatus(enum.StrEnum):
    """
    The status of the Order
    """

    PENDING = "pending"
    UNFULFILLED = "unfulfilled"
    FULFILLED = "fulfilled"
    DISPUTED = "disputed"
    DISPUTE_LOST = "dispute-lost"
    REFUNDED = "refunded"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        unfulfilled: typing.Callable[[], T_Result],
        fulfilled: typing.Callable[[], T_Result],
        disputed: typing.Callable[[], T_Result],
        dispute_lost: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetOrdersResponseStatus.PENDING:
            return pending()
        if self is GetOrdersResponseStatus.UNFULFILLED:
            return unfulfilled()
        if self is GetOrdersResponseStatus.FULFILLED:
            return fulfilled()
        if self is GetOrdersResponseStatus.DISPUTED:
            return disputed()
        if self is GetOrdersResponseStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is GetOrdersResponseStatus.REFUNDED:
            return refunded()
