

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventorySearchRequestSortField(enum.StrEnum):
    """
    Field to sort by. Sorting by 'price' uses the FTC-final 'price' field (which dealers MUST keep accurate); 'updated_at' sorts by listing freshness.
    """

    PRICE = "price"
    LIST_PRICE = "list_price"
    OFFERED_PRICE = "offered_price"
    MSRP = "msrp"
    MILEAGE = "mileage"
    YEAR = "year"
    MAKE = "make"
    MODEL = "model"
    STOCK = "stock"
    UPDATED_AT = "updated_at"

    def visit(
        self,
        price: typing.Callable[[], T_Result],
        list_price: typing.Callable[[], T_Result],
        offered_price: typing.Callable[[], T_Result],
        msrp: typing.Callable[[], T_Result],
        mileage: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
        make: typing.Callable[[], T_Result],
        model: typing.Callable[[], T_Result],
        stock: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InventorySearchRequestSortField.PRICE:
            return price()
        if self is InventorySearchRequestSortField.LIST_PRICE:
            return list_price()
        if self is InventorySearchRequestSortField.OFFERED_PRICE:
            return offered_price()
        if self is InventorySearchRequestSortField.MSRP:
            return msrp()
        if self is InventorySearchRequestSortField.MILEAGE:
            return mileage()
        if self is InventorySearchRequestSortField.YEAR:
            return year()
        if self is InventorySearchRequestSortField.MAKE:
            return make()
        if self is InventorySearchRequestSortField.MODEL:
            return model()
        if self is InventorySearchRequestSortField.STOCK:
            return stock()
        if self is InventorySearchRequestSortField.UPDATED_AT:
            return updated_at()
