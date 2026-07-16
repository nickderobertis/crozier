

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaxInclusionType(str, enum.Enum):
    """
    Whether to the tax amount should be additional to or included in the CatalogItem price.
    """

    ADDITIVE = "ADDITIVE"
    INCLUSIVE = "INCLUSIVE"

    def visit(self, additive: typing.Callable[[], T_Result], inclusive: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxInclusionType.ADDITIVE:
            return additive()
        if self is TaxInclusionType.INCLUSIVE:
            return inclusive()
