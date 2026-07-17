

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxInclusionType(enum.StrEnum):
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
