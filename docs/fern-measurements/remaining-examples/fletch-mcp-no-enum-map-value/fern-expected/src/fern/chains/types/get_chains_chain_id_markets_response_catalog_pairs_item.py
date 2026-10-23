

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_response_catalog_pairs_item_asset_currency import (
    GetChainsChainIdMarketsResponseCatalogPairsItemAssetCurrency,
)
from .get_chains_chain_id_markets_response_catalog_pairs_item_quote_currency import (
    GetChainsChainIdMarketsResponseCatalogPairsItemQuoteCurrency,
)
from .get_chains_chain_id_markets_response_catalog_pairs_item_tradability import (
    GetChainsChainIdMarketsResponseCatalogPairsItemTradability,
)
from .get_chains_chain_id_markets_response_catalog_pairs_item_tradability_by_account_type_value import (
    GetChainsChainIdMarketsResponseCatalogPairsItemTradabilityByAccountTypeValue,
)


class GetChainsChainIdMarketsResponseCatalogPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: GetChainsChainIdMarketsResponseCatalogPairsItemTradability
    tradability_by_account_type: typing.Dict[
        str, GetChainsChainIdMarketsResponseCatalogPairsItemTradabilityByAccountTypeValue
    ]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: GetChainsChainIdMarketsResponseCatalogPairsItemAssetCurrency
    quote_currency: GetChainsChainIdMarketsResponseCatalogPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
