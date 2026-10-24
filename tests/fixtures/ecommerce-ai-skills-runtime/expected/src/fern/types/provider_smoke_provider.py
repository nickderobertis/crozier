

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderSmokeProvider(enum.StrEnum):
    OPENAI = "openai"
    AMAZON_SPAPI = "amazon_spapi"
    SHOPIFY = "shopify"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        amazon_spapi: typing.Callable[[], T_Result],
        shopify: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderSmokeProvider.OPENAI:
            return openai()
        if self is ProviderSmokeProvider.AMAZON_SPAPI:
            return amazon_spapi()
        if self is ProviderSmokeProvider.SHOPIFY:
            return shopify()
