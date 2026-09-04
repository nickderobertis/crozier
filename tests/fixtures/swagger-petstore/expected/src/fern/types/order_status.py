

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderStatus(enum.StrEnum):
    """
    Order Status
    """

    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"

    def visit(
        self,
        placed: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderStatus.PLACED:
            return placed()
        if self is OrderStatus.APPROVED:
            return approved()
        if self is OrderStatus.DELIVERED:
            return delivered()
