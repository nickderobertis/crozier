

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceItemType(enum.StrEnum):
    """
    Item type
    """

    INVENTORY = "inventory"
    SERVICE = "service"
    OTHER = "other"

    def visit(
        self,
        inventory: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceItemType.INVENTORY:
            return inventory()
        if self is InvoiceItemType.SERVICE:
            return service()
        if self is InvoiceItemType.OTHER:
            return other()
