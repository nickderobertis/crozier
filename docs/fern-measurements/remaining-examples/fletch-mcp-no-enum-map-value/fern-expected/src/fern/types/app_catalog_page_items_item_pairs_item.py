

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_catalog_page_items_item_pairs_item_asset_currency import AppCatalogPageItemsItemPairsItemAssetCurrency
from .app_catalog_page_items_item_pairs_item_quote_currency import AppCatalogPageItemsItemPairsItemQuoteCurrency
from .app_catalog_page_items_item_pairs_item_tradability import AppCatalogPageItemsItemPairsItemTradability
from .app_catalog_page_items_item_pairs_item_tradability_by_account_type_value import (
    AppCatalogPageItemsItemPairsItemTradabilityByAccountTypeValue,
)


class AppCatalogPageItemsItemPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: AppCatalogPageItemsItemPairsItemTradability
    tradability_by_account_type: typing.Dict[str, AppCatalogPageItemsItemPairsItemTradabilityByAccountTypeValue]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: AppCatalogPageItemsItemPairsItemAssetCurrency
    quote_currency: AppCatalogPageItemsItemPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
