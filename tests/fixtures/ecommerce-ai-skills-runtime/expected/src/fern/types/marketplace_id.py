

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketplaceId(enum.StrEnum):
    ALIEXPRESS = "aliexpress"
    AMAZON = "amazon"
    COUPANG = "coupang"
    EBAY = "ebay"
    FAIRE = "faire"
    LAZADA = "lazada"
    MERCADO_LIBRE = "mercado_libre"
    OTTO = "otto"
    RAKUTEN = "rakuten"
    SHOPEE = "shopee"
    SHOPIFY = "shopify"
    TEMU = "temu"
    TIKTOK_SHOP = "tiktok_shop"
    WALMART = "walmart"
    ZALANDO = "zalando"

    def visit(
        self,
        aliexpress: typing.Callable[[], T_Result],
        amazon: typing.Callable[[], T_Result],
        coupang: typing.Callable[[], T_Result],
        ebay: typing.Callable[[], T_Result],
        faire: typing.Callable[[], T_Result],
        lazada: typing.Callable[[], T_Result],
        mercado_libre: typing.Callable[[], T_Result],
        otto: typing.Callable[[], T_Result],
        rakuten: typing.Callable[[], T_Result],
        shopee: typing.Callable[[], T_Result],
        shopify: typing.Callable[[], T_Result],
        temu: typing.Callable[[], T_Result],
        tiktok_shop: typing.Callable[[], T_Result],
        walmart: typing.Callable[[], T_Result],
        zalando: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarketplaceId.ALIEXPRESS:
            return aliexpress()
        if self is MarketplaceId.AMAZON:
            return amazon()
        if self is MarketplaceId.COUPANG:
            return coupang()
        if self is MarketplaceId.EBAY:
            return ebay()
        if self is MarketplaceId.FAIRE:
            return faire()
        if self is MarketplaceId.LAZADA:
            return lazada()
        if self is MarketplaceId.MERCADO_LIBRE:
            return mercado_libre()
        if self is MarketplaceId.OTTO:
            return otto()
        if self is MarketplaceId.RAKUTEN:
            return rakuten()
        if self is MarketplaceId.SHOPEE:
            return shopee()
        if self is MarketplaceId.SHOPIFY:
            return shopify()
        if self is MarketplaceId.TEMU:
            return temu()
        if self is MarketplaceId.TIKTOK_SHOP:
            return tiktok_shop()
        if self is MarketplaceId.WALMART:
            return walmart()
        if self is MarketplaceId.ZALANDO:
            return zalando()
