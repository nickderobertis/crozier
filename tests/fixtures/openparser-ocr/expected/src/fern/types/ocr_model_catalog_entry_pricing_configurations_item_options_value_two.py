

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo(enum.StrEnum):
    UNSET = "unset"

    def visit(self, unset: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo.UNSET:
            return unset()
