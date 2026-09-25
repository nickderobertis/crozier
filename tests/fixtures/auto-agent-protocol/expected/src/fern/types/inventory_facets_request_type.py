

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventoryFacetsRequestType(enum.StrEnum):
    INVENTORY_FACETS_REQUEST = "inventory.facets.request"

    def visit(self, inventory_facets_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is InventoryFacetsRequestType.INVENTORY_FACETS_REQUEST:
            return inventory_facets_request()
