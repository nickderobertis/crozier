

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCloudOrderResponseKind(enum.StrEnum):
    """
    The kind of order: 'order' for a sale or 'credit' for a credit order.
    """

    ORDER = "order"
    CREDIT = "credit"

    def visit(self, order: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxCloudOrderResponseKind.ORDER:
            return order()
        if self is TaxCloudOrderResponseKind.CREDIT:
            return credit()
