

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Product(str, enum.Enum):
    """
    Indicates the Square product used to generate an inventory change.
    """

    SQUARE_POS = "SQUARE_POS"
    EXTERNAL_API = "EXTERNAL_API"
    BILLING = "BILLING"
    APPOINTMENTS = "APPOINTMENTS"
    INVOICES = "INVOICES"
    ONLINE_STORE = "ONLINE_STORE"
    PAYROLL = "PAYROLL"
    DASHBOARD = "DASHBOARD"
    ITEM_LIBRARY_IMPORT = "ITEM_LIBRARY_IMPORT"
    OTHER = "OTHER"

    def visit(
        self,
        square_pos: typing.Callable[[], T_Result],
        external_api: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        appointments: typing.Callable[[], T_Result],
        invoices: typing.Callable[[], T_Result],
        online_store: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
        dashboard: typing.Callable[[], T_Result],
        item_library_import: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Product.SQUARE_POS:
            return square_pos()
        if self is Product.EXTERNAL_API:
            return external_api()
        if self is Product.BILLING:
            return billing()
        if self is Product.APPOINTMENTS:
            return appointments()
        if self is Product.INVOICES:
            return invoices()
        if self is Product.ONLINE_STORE:
            return online_store()
        if self is Product.PAYROLL:
            return payroll()
        if self is Product.DASHBOARD:
            return dashboard()
        if self is Product.ITEM_LIBRARY_IMPORT:
            return item_library_import()
        if self is Product.OTHER:
            return other()
