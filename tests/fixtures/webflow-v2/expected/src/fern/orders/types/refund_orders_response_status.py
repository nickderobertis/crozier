

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RefundOrdersResponseStatus(enum.StrEnum):
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
        if self is RefundOrdersResponseStatus.PENDING:
            return pending()
        if self is RefundOrdersResponseStatus.UNFULFILLED:
            return unfulfilled()
        if self is RefundOrdersResponseStatus.FULFILLED:
            return fulfilled()
        if self is RefundOrdersResponseStatus.DISPUTED:
            return disputed()
        if self is RefundOrdersResponseStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is RefundOrdersResponseStatus.REFUNDED:
            return refunded()
