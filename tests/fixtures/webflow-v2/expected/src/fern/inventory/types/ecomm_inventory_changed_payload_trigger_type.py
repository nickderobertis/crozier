

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EcommInventoryChangedPayloadTriggerType(enum.StrEnum):
    ECOMM_INVENTORY_CHANGED = "ecomm_inventory_changed"

    def visit(self, ecomm_inventory_changed: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcommInventoryChangedPayloadTriggerType.ECOMM_INVENTORY_CHANGED:
            return ecomm_inventory_changed()
