

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketplaceProviderSmokeRequestProvider(enum.StrEnum):
    AMAZON_SPAPI = "amazon_spapi"
    SHOPIFY = "shopify"

    def visit(self, amazon_spapi: typing.Callable[[], T_Result], shopify: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarketplaceProviderSmokeRequestProvider.AMAZON_SPAPI:
            return amazon_spapi()
        if self is MarketplaceProviderSmokeRequestProvider.SHOPIFY:
            return shopify()
