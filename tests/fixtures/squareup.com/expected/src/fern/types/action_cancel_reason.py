

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActionCancelReason(str, enum.Enum):
    """ """

    BUYER_CANCELED = "BUYER_CANCELED"
    SELLER_CANCELED = "SELLER_CANCELED"
    TIMED_OUT = "TIMED_OUT"

    def visit(
        self,
        buyer_canceled: typing.Callable[[], T_Result],
        seller_canceled: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionCancelReason.BUYER_CANCELED:
            return buyer_canceled()
        if self is ActionCancelReason.SELLER_CANCELED:
            return seller_canceled()
        if self is ActionCancelReason.TIMED_OUT:
            return timed_out()
