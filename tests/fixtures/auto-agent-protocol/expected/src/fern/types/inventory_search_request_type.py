

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventorySearchRequestType(enum.StrEnum):
    INVENTORY_SEARCH_REQUEST = "inventory.search.request"

    def visit(self, inventory_search_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is InventorySearchRequestType.INVENTORY_SEARCH_REQUEST:
            return inventory_search_request()
