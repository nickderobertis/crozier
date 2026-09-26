

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60TaxSummaryTaxType(enum.StrEnum):
    """
    Tax kind this summary aggregates: 'SALES_TAX' or 'USE_TAX'.
    """

    SALES_TAX = "SALES_TAX"
    USE_TAX = "USE_TAX"

    def visit(self, sales_tax: typing.Callable[[], T_Result], use_tax: typing.Callable[[], T_Result]) -> T_Result:
        if self is V60TaxSummaryTaxType.SALES_TAX:
            return sales_tax()
        if self is V60TaxSummaryTaxType.USE_TAX:
            return use_tax()
