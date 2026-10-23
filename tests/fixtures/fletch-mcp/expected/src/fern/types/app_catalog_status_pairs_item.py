

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_catalog_status_pairs_item_asset_currency import AppCatalogStatusPairsItemAssetCurrency
from .app_catalog_status_pairs_item_quote_currency import AppCatalogStatusPairsItemQuoteCurrency
from .app_catalog_status_pairs_item_tradability import AppCatalogStatusPairsItemTradability
from .app_catalog_status_pairs_item_tradability_by_account_type_value import (
    AppCatalogStatusPairsItemTradabilityByAccountTypeValue,
)


class AppCatalogStatusPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: AppCatalogStatusPairsItemTradability
    tradability_by_account_type: typing.Dict[str, AppCatalogStatusPairsItemTradabilityByAccountTypeValue]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: AppCatalogStatusPairsItemAssetCurrency
    quote_currency: AppCatalogStatusPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
