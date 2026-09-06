

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EcommOrderChangedPayloadPayloadStatus(enum.StrEnum):
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
        if self is EcommOrderChangedPayloadPayloadStatus.PENDING:
            return pending()
        if self is EcommOrderChangedPayloadPayloadStatus.UNFULFILLED:
            return unfulfilled()
        if self is EcommOrderChangedPayloadPayloadStatus.FULFILLED:
            return fulfilled()
        if self is EcommOrderChangedPayloadPayloadStatus.DISPUTED:
            return disputed()
        if self is EcommOrderChangedPayloadPayloadStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is EcommOrderChangedPayloadPayloadStatus.REFUNDED:
            return refunded()
