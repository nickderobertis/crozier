

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderStatus(enum.StrEnum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        shipped: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderStatus.PENDING:
            return pending()
        if self is OrderStatus.PAID:
            return paid()
        if self is OrderStatus.SHIPPED:
            return shipped()
        if self is OrderStatus.DELIVERED:
            return delivered()
        if self is OrderStatus.CANCELLED:
            return cancelled()
