

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BreakdownSortOrder(enum.StrEnum):
    """
    Required. The sort order is applied to the values of the breakdown column.
    """

    SORT_ORDER_UNSPECIFIED = "SORT_ORDER_UNSPECIFIED"
    SORT_ORDER_NONE = "SORT_ORDER_NONE"
    SORT_ORDER_ASCENDING = "SORT_ORDER_ASCENDING"
    SORT_ORDER_DESCENDING = "SORT_ORDER_DESCENDING"

    def visit(
        self,
        sort_order_unspecified: typing.Callable[[], T_Result],
        sort_order_none: typing.Callable[[], T_Result],
        sort_order_ascending: typing.Callable[[], T_Result],
        sort_order_descending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BreakdownSortOrder.SORT_ORDER_UNSPECIFIED:
            return sort_order_unspecified()
        if self is BreakdownSortOrder.SORT_ORDER_NONE:
            return sort_order_none()
        if self is BreakdownSortOrder.SORT_ORDER_ASCENDING:
            return sort_order_ascending()
        if self is BreakdownSortOrder.SORT_ORDER_DESCENDING:
            return sort_order_descending()
