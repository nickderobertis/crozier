

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60ServiceTaxable(enum.StrEnum):
    """
    Whether services/labor are taxable in this jurisdiction. 'Y' = the service is fully taxable and must be separately stated on the invoice; 'N' = the service is not taxable and must be separately stated on the invoice; 'L' = the service is not taxable, but the labor portion is taxable and both must be separately stated on the invoice.
    """

    Y = "Y"
    N = "N"
    L = "L"

    def visit(
        self, y: typing.Callable[[], T_Result], n: typing.Callable[[], T_Result], l: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is V60ServiceTaxable.Y:
            return y()
        if self is V60ServiceTaxable.N:
            return n()
        if self is V60ServiceTaxable.L:
            return l()
