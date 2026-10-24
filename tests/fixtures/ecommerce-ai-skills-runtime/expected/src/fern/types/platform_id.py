

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlatformId(enum.StrEnum):
    ALIEXPRESS = "aliexpress"
    AMAZON = "amazon"
    COUPANG = "coupang"
    CROSS_PLATFORM = "cross_platform"
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
        cross_platform: typing.Callable[[], T_Result],
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
        if self is PlatformId.ALIEXPRESS:
            return aliexpress()
        if self is PlatformId.AMAZON:
            return amazon()
        if self is PlatformId.COUPANG:
            return coupang()
        if self is PlatformId.CROSS_PLATFORM:
            return cross_platform()
        if self is PlatformId.EBAY:
            return ebay()
        if self is PlatformId.FAIRE:
            return faire()
        if self is PlatformId.LAZADA:
            return lazada()
        if self is PlatformId.MERCADO_LIBRE:
            return mercado_libre()
        if self is PlatformId.OTTO:
            return otto()
        if self is PlatformId.RAKUTEN:
            return rakuten()
        if self is PlatformId.SHOPEE:
            return shopee()
        if self is PlatformId.SHOPIFY:
            return shopify()
        if self is PlatformId.TEMU:
            return temu()
        if self is PlatformId.TIKTOK_SHOP:
            return tiktok_shop()
        if self is PlatformId.WALMART:
            return walmart()
        if self is PlatformId.ZALANDO:
            return zalando()
