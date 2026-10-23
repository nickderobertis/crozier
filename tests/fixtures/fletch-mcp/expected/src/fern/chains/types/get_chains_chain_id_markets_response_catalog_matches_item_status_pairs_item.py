

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_asset_currency import (
    GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemAssetCurrency,
)
from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_quote_currency import (
    GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemQuoteCurrency,
)
from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability import (
    GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradability,
)
from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability_by_account_type_value import (
    GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradabilityByAccountTypeValue,
)


class GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradability
    tradability_by_account_type: typing.Dict[
        str, GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradabilityByAccountTypeValue
    ]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemAssetCurrency
    quote_currency: GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
