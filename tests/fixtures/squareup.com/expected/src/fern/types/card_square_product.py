

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardSquareProduct(str, enum.Enum):
    """ """

    UNKNOWN_SQUARE_PRODUCT = "UNKNOWN_SQUARE_PRODUCT"
    CONNECT_API = "CONNECT_API"
    DASHBOARD = "DASHBOARD"
    REGISTER_CLIENT = "REGISTER_CLIENT"
    BUYER_DASHBOARD = "BUYER_DASHBOARD"
    WEB = "WEB"
    INVOICES = "INVOICES"
    GIFT_CARD = "GIFT_CARD"
    VIRTUAL_TERMINAL = "VIRTUAL_TERMINAL"
    READER_SDK = "READER_SDK"

    def visit(
        self,
        unknown_square_product: typing.Callable[[], T_Result],
        connect_api: typing.Callable[[], T_Result],
        dashboard: typing.Callable[[], T_Result],
        register_client: typing.Callable[[], T_Result],
        buyer_dashboard: typing.Callable[[], T_Result],
        web: typing.Callable[[], T_Result],
        invoices: typing.Callable[[], T_Result],
        gift_card: typing.Callable[[], T_Result],
        virtual_terminal: typing.Callable[[], T_Result],
        reader_sdk: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardSquareProduct.UNKNOWN_SQUARE_PRODUCT:
            return unknown_square_product()
        if self is CardSquareProduct.CONNECT_API:
            return connect_api()
        if self is CardSquareProduct.DASHBOARD:
            return dashboard()
        if self is CardSquareProduct.REGISTER_CLIENT:
            return register_client()
        if self is CardSquareProduct.BUYER_DASHBOARD:
            return buyer_dashboard()
        if self is CardSquareProduct.WEB:
            return web()
        if self is CardSquareProduct.INVOICES:
            return invoices()
        if self is CardSquareProduct.GIFT_CARD:
            return gift_card()
        if self is CardSquareProduct.VIRTUAL_TERMINAL:
            return virtual_terminal()
        if self is CardSquareProduct.READER_SDK:
            return reader_sdk()
