

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExcludeStrategy(str, enum.Enum):
    """
    Indicates which products matched by a CatalogPricingRule
    will be excluded if the pricing rule uses an exclude set.
    """

    LEAST_EXPENSIVE = "LEAST_EXPENSIVE"
    MOST_EXPENSIVE = "MOST_EXPENSIVE"

    def visit(
        self, least_expensive: typing.Callable[[], T_Result], most_expensive: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ExcludeStrategy.LEAST_EXPENSIVE:
            return least_expensive()
        if self is ExcludeStrategy.MOST_EXPENSIVE:
            return most_expensive()
