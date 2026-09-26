

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60ShippingTaxable(enum.StrEnum):
    """
    Whether freight/shipping is taxable in this jurisdiction. 'Y' = taxable, 'N' = not taxable.
    """

    Y = "Y"
    N = "N"

    def visit(self, y: typing.Callable[[], T_Result], n: typing.Callable[[], T_Result]) -> T_Result:
        if self is V60ShippingTaxable.Y:
            return y()
        if self is V60ShippingTaxable.N:
            return n()
