

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EcommerceOrderFulfillmentStatus(enum.StrEnum):
    """
    Current fulfillment status of the order.
    """

    PENDING = "pending"
    SHIPPED = "shipped"
    PARTIAL = "partial"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"
    UNKNOWN = "unknown"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        shipped: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        returned: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcommerceOrderFulfillmentStatus.PENDING:
            return pending()
        if self is EcommerceOrderFulfillmentStatus.SHIPPED:
            return shipped()
        if self is EcommerceOrderFulfillmentStatus.PARTIAL:
            return partial()
        if self is EcommerceOrderFulfillmentStatus.DELIVERED:
            return delivered()
        if self is EcommerceOrderFulfillmentStatus.CANCELLED:
            return cancelled()
        if self is EcommerceOrderFulfillmentStatus.RETURNED:
            return returned()
        if self is EcommerceOrderFulfillmentStatus.UNKNOWN:
            return unknown()
