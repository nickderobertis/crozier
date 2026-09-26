

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventoryFacetsResponseType(enum.StrEnum):
    INVENTORY_FACETS_RESPONSE = "inventory.facets.response"

    def visit(self, inventory_facets_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is InventoryFacetsResponseType.INVENTORY_FACETS_RESPONSE:
            return inventory_facets_response()
