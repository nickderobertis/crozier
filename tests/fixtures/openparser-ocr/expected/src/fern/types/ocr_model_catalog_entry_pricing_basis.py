

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrModelCatalogEntryPricingBasis(enum.StrEnum):
    CUSTOMER_RETAIL = "customer_retail"

    def visit(self, customer_retail: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrModelCatalogEntryPricingBasis.CUSTOMER_RETAIL:
            return customer_retail()
