

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_asset_currency import (
    GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemAssetCurrency,
)
from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_quote_currency import (
    GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemQuoteCurrency,
)
from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability import (
    GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradability,
)
from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability_by_account_type_value import (
    GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradabilityByAccountTypeValue,
)


class GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradability
    tradability_by_account_type: typing.Dict[
        str, GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradabilityByAccountTypeValue
    ]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemAssetCurrency
    quote_currency: GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
