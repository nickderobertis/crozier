

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventoryState(enum.StrEnum):
    """
    Indicates the state of a tracked item quantity in the lifecycle of goods.
    """

    CUSTOM = "CUSTOM"
    IN_STOCK = "IN_STOCK"
    SOLD = "SOLD"
    RETURNED_BY_CUSTOMER = "RETURNED_BY_CUSTOMER"
    RESERVED_FOR_SALE = "RESERVED_FOR_SALE"
    SOLD_ONLINE = "SOLD_ONLINE"
    ORDERED_FROM_VENDOR = "ORDERED_FROM_VENDOR"
    RECEIVED_FROM_VENDOR = "RECEIVED_FROM_VENDOR"
    IN_TRANSIT_TO = "IN_TRANSIT_TO"
    NONE = "NONE"
    WASTE = "WASTE"
    UNLINKED_RETURN = "UNLINKED_RETURN"
    COMPOSED = "COMPOSED"
    DECOMPOSED = "DECOMPOSED"
    SUPPORTED_BY_NEWER_VERSION = "SUPPORTED_BY_NEWER_VERSION"

    def visit(
        self,
        custom: typing.Callable[[], T_Result],
        in_stock: typing.Callable[[], T_Result],
        sold: typing.Callable[[], T_Result],
        returned_by_customer: typing.Callable[[], T_Result],
        reserved_for_sale: typing.Callable[[], T_Result],
        sold_online: typing.Callable[[], T_Result],
        ordered_from_vendor: typing.Callable[[], T_Result],
        received_from_vendor: typing.Callable[[], T_Result],
        in_transit_to: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        waste: typing.Callable[[], T_Result],
        unlinked_return: typing.Callable[[], T_Result],
        composed: typing.Callable[[], T_Result],
        decomposed: typing.Callable[[], T_Result],
        supported_by_newer_version: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InventoryState.CUSTOM:
            return custom()
        if self is InventoryState.IN_STOCK:
            return in_stock()
        if self is InventoryState.SOLD:
            return sold()
        if self is InventoryState.RETURNED_BY_CUSTOMER:
            return returned_by_customer()
        if self is InventoryState.RESERVED_FOR_SALE:
            return reserved_for_sale()
        if self is InventoryState.SOLD_ONLINE:
            return sold_online()
        if self is InventoryState.ORDERED_FROM_VENDOR:
            return ordered_from_vendor()
        if self is InventoryState.RECEIVED_FROM_VENDOR:
            return received_from_vendor()
        if self is InventoryState.IN_TRANSIT_TO:
            return in_transit_to()
        if self is InventoryState.NONE:
            return none()
        if self is InventoryState.WASTE:
            return waste()
        if self is InventoryState.UNLINKED_RETURN:
            return unlinked_return()
        if self is InventoryState.COMPOSED:
            return composed()
        if self is InventoryState.DECOMPOSED:
            return decomposed()
        if self is InventoryState.SUPPORTED_BY_NEWER_VERSION:
            return supported_by_newer_version()
