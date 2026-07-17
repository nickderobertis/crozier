

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventoryAlertType(enum.StrEnum):
    """
    Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is low.
    """

    NONE = "NONE"
    LOW_QUANTITY = "LOW_QUANTITY"

    def visit(self, none: typing.Callable[[], T_Result], low_quantity: typing.Callable[[], T_Result]) -> T_Result:
        if self is InventoryAlertType.NONE:
            return none()
        if self is InventoryAlertType.LOW_QUANTITY:
            return low_quantity()
