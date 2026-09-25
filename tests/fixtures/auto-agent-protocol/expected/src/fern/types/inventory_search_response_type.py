

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventorySearchResponseType(enum.StrEnum):
    INVENTORY_SEARCH_RESPONSE = "inventory.search.response"

    def visit(self, inventory_search_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is InventorySearchResponseType.INVENTORY_SEARCH_RESPONSE:
            return inventory_search_response()
