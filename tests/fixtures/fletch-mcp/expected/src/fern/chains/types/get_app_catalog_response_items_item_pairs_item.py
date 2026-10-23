

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_app_catalog_response_items_item_pairs_item_asset_currency import (
    GetAppCatalogResponseItemsItemPairsItemAssetCurrency,
)
from .get_app_catalog_response_items_item_pairs_item_quote_currency import (
    GetAppCatalogResponseItemsItemPairsItemQuoteCurrency,
)
from .get_app_catalog_response_items_item_pairs_item_tradability import (
    GetAppCatalogResponseItemsItemPairsItemTradability,
)
from .get_app_catalog_response_items_item_pairs_item_tradability_by_account_type_value import (
    GetAppCatalogResponseItemsItemPairsItemTradabilityByAccountTypeValue,
)


class GetAppCatalogResponseItemsItemPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: GetAppCatalogResponseItemsItemPairsItemTradability
    tradability_by_account_type: typing.Dict[str, GetAppCatalogResponseItemsItemPairsItemTradabilityByAccountTypeValue]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: GetAppCatalogResponseItemsItemPairsItemAssetCurrency
    quote_currency: GetAppCatalogResponseItemsItemPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
