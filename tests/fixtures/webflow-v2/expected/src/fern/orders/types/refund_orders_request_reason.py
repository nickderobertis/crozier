

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RefundOrdersRequestReason(enum.StrEnum):
    """
    The reason for the refund
    """

    DUPLICATE = "duplicate"
    FRAUDULENT = "fraudulent"
    REQUESTED = "requested"

    def visit(
        self,
        duplicate: typing.Callable[[], T_Result],
        fraudulent: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RefundOrdersRequestReason.DUPLICATE:
            return duplicate()
        if self is RefundOrdersRequestReason.FRAUDULENT:
            return fraudulent()
        if self is RefundOrdersRequestReason.REQUESTED:
            return requested()
