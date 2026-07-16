

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchCatalogItemsRequestStockLevel(enum.StrEnum):
    """
    Defines supported stock levels of the item inventory.
    """

    OUT = "OUT"
    LOW = "LOW"

    def visit(self, out: typing.Callable[[], T_Result], low: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchCatalogItemsRequestStockLevel.OUT:
            return out()
        if self is SearchCatalogItemsRequestStockLevel.LOW:
            return low()
