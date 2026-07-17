

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1OrderHistoryEntryAction(enum.StrEnum):
    """ """

    ORDER_PLACED = "ORDER_PLACED"
    DECLINED = "DECLINED"
    PAYMENT_RECEIVED = "PAYMENT_RECEIVED"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    REFUNDED = "REFUNDED"
    EXPIRED = "EXPIRED"

    def visit(
        self,
        order_placed: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        payment_received: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OrderHistoryEntryAction.ORDER_PLACED:
            return order_placed()
        if self is V1OrderHistoryEntryAction.DECLINED:
            return declined()
        if self is V1OrderHistoryEntryAction.PAYMENT_RECEIVED:
            return payment_received()
        if self is V1OrderHistoryEntryAction.CANCELED:
            return canceled()
        if self is V1OrderHistoryEntryAction.COMPLETED:
            return completed()
        if self is V1OrderHistoryEntryAction.REFUNDED:
            return refunded()
        if self is V1OrderHistoryEntryAction.EXPIRED:
            return expired()
