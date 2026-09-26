

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantOrderCreateFromCartRequestKind(enum.StrEnum):
    """
    The kind of order to create: 'order' for a sale (default) or 'credit' for a credit order.
    """

    ORDER = "order"
    CREDIT = "credit"

    def visit(self, order: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is MerchantOrderCreateFromCartRequestKind.ORDER:
            return order()
        if self is MerchantOrderCreateFromCartRequestKind.CREDIT:
            return credit()
