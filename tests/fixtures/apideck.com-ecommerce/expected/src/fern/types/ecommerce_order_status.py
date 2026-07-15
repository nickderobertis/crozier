

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcommerceOrderStatus(str, enum.Enum):
    """
    Current status of the order.
    """

    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    ARCHIVED = "archived"
    UNKNOWN = "unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcommerceOrderStatus.ACTIVE:
            return active()
        if self is EcommerceOrderStatus.COMPLETED:
            return completed()
        if self is EcommerceOrderStatus.CANCELLED:
            return cancelled()
        if self is EcommerceOrderStatus.ARCHIVED:
            return archived()
        if self is EcommerceOrderStatus.UNKNOWN:
            return unknown()
