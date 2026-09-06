

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EcommNewOrderPayloadPayloadStatus(enum.StrEnum):
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
        if self is EcommNewOrderPayloadPayloadStatus.PENDING:
            return pending()
        if self is EcommNewOrderPayloadPayloadStatus.UNFULFILLED:
            return unfulfilled()
        if self is EcommNewOrderPayloadPayloadStatus.FULFILLED:
            return fulfilled()
        if self is EcommNewOrderPayloadPayloadStatus.DISPUTED:
            return disputed()
        if self is EcommNewOrderPayloadPayloadStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is EcommNewOrderPayloadPayloadStatus.REFUNDED:
            return refunded()
