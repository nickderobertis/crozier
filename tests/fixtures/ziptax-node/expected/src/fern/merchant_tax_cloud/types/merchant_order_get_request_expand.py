

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantOrderGetRequestExpand(enum.StrEnum):
    """
    Set to 'refunds' to include the order's refunds in the response. Forwarded to TaxCloud as a query parameter.
    """

    REFUNDS = "refunds"

    def visit(self, refunds: typing.Callable[[], T_Result]) -> T_Result:
        if self is MerchantOrderGetRequestExpand.REFUNDS:
            return refunds()
