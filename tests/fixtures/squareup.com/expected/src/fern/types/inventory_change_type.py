

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InventoryChangeType(str, enum.Enum):
    """
    Indicates how the inventory change was applied to a tracked product quantity.
    """

    PHYSICAL_COUNT = "PHYSICAL_COUNT"
    ADJUSTMENT = "ADJUSTMENT"
    TRANSFER = "TRANSFER"

    def visit(
        self,
        physical_count: typing.Callable[[], T_Result],
        adjustment: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InventoryChangeType.PHYSICAL_COUNT:
            return physical_count()
        if self is InventoryChangeType.ADJUSTMENT:
            return adjustment()
        if self is InventoryChangeType.TRANSFER:
            return transfer()
