

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectorProvider(enum.StrEnum):
    AMAZON_ADS = "amazon_ads"
    AMAZON_SPAPI = "amazon_spapi"
    SHOPIFY = "shopify"

    def visit(
        self,
        amazon_ads: typing.Callable[[], T_Result],
        amazon_spapi: typing.Callable[[], T_Result],
        shopify: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectorProvider.AMAZON_ADS:
            return amazon_ads()
        if self is ConnectorProvider.AMAZON_SPAPI:
            return amazon_spapi()
        if self is ConnectorProvider.SHOPIFY:
            return shopify()
