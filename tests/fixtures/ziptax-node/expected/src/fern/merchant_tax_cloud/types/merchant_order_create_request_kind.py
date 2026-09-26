

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantOrderCreateRequestKind(enum.StrEnum):
    """
    The kind of order: 'order' for a sale (default) or 'credit' for a credit order.
    """

    ORDER = "order"
    CREDIT = "credit"

    def visit(self, order: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is MerchantOrderCreateRequestKind.ORDER:
            return order()
        if self is MerchantOrderCreateRequestKind.CREDIT:
            return credit()
