

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CatalogPricingType(str, enum.Enum):
    """
    Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale.
    """

    FIXED_PRICING = "FIXED_PRICING"
    VARIABLE_PRICING = "VARIABLE_PRICING"

    def visit(
        self, fixed_pricing: typing.Callable[[], T_Result], variable_pricing: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CatalogPricingType.FIXED_PRICING:
            return fixed_pricing()
        if self is CatalogPricingType.VARIABLE_PRICING:
            return variable_pricing()
