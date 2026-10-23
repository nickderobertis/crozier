

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_response_items_item_alternatives_item import (
    GetChainsChainIdMarketsResponseItemsItemAlternativesItem,
)
from .get_chains_chain_id_markets_response_items_item_burned_raw import (
    GetChainsChainIdMarketsResponseItemsItemBurnedRaw,
)
from .get_chains_chain_id_markets_response_items_item_decimals import GetChainsChainIdMarketsResponseItemsItemDecimals
from .get_chains_chain_id_markets_response_items_item_holders import GetChainsChainIdMarketsResponseItemsItemHolders
from .get_chains_chain_id_markets_response_items_item_market_cap_usd import (
    GetChainsChainIdMarketsResponseItemsItemMarketCapUsd,
)
from .get_chains_chain_id_markets_response_items_item_price_usd import GetChainsChainIdMarketsResponseItemsItemPriceUsd
from .get_chains_chain_id_markets_response_items_item_robinhood_app import (
    GetChainsChainIdMarketsResponseItemsItemRobinhoodApp,
)
from .get_chains_chain_id_markets_response_items_item_selection import GetChainsChainIdMarketsResponseItemsItemSelection
from .get_chains_chain_id_markets_response_items_item_stock_pairings_item import (
    GetChainsChainIdMarketsResponseItemsItemStockPairingsItem,
)
from .get_chains_chain_id_markets_response_items_item_swaps24h import GetChainsChainIdMarketsResponseItemsItemSwaps24H
from .get_chains_chain_id_markets_response_items_item_total_supply_raw import (
    GetChainsChainIdMarketsResponseItemsItemTotalSupplyRaw,
)
from .get_chains_chain_id_markets_response_items_item_transactions24h import (
    GetChainsChainIdMarketsResponseItemsItemTransactions24H,
)
from .get_chains_chain_id_markets_response_items_item_trust import GetChainsChainIdMarketsResponseItemsItemTrust
from .get_chains_chain_id_markets_response_items_item_v3quote_holdings_usd import (
    GetChainsChainIdMarketsResponseItemsItemV3QuoteHoldingsUsd,
)
from .get_chains_chain_id_markets_response_items_item_v4one_percent_depth_usd import (
    GetChainsChainIdMarketsResponseItemsItemV4OnePercentDepthUsd,
)
from .get_chains_chain_id_markets_response_items_item_volume_scope import (
    GetChainsChainIdMarketsResponseItemsItemVolumeScope,
)
from .get_chains_chain_id_markets_response_items_item_volume_usd24h import (
    GetChainsChainIdMarketsResponseItemsItemVolumeUsd24H,
)


class GetChainsChainIdMarketsResponseItemsItem(UniversalBaseModel):
    robinhood_app: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdMarketsResponseItemsItemRobinhoodApp],
        FieldMetadata(alias="robinhoodApp"),
        pydantic.Field(alias="robinhoodApp"),
    ] = None
    stock_pairings: typing_extensions.Annotated[
        typing.Optional[typing.List[GetChainsChainIdMarketsResponseItemsItemStockPairingsItem]],
        FieldMetadata(alias="stockPairings"),
        pydantic.Field(alias="stockPairings"),
    ] = None
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    address: str
    asset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assetId"), pydantic.Field(alias="assetId")
    ] = None
    symbol: typing.Optional[str] = None
    name: typing.Optional[str] = None
    trust: GetChainsChainIdMarketsResponseItemsItemTrust
    selection: GetChainsChainIdMarketsResponseItemsItemSelection = pydantic.Field()
    """
    Recorded bounded universe comparison; expires after fifteen minutes. A stale selection withholds dominantAddress while retaining its explanation and observation time.
    """

    dominant_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dominantAddress"), pydantic.Field(alias="dominantAddress")
    ] = None
    selection_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="selectionReason"), pydantic.Field(alias="selectionReason")
    ]
    close_call: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="closeCall"), pydantic.Field(alias="closeCall")
    ] = None
    alternatives: typing.List[GetChainsChainIdMarketsResponseItemsItemAlternativesItem]
    best_pool_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bestPoolId"), pydantic.Field(alias="bestPoolId")
    ] = None
    pool_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="poolCount"), pydantic.Field(alias="poolCount")
    ] = None
    decimals: typing.Optional[GetChainsChainIdMarketsResponseItemsItemDecimals] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdMarketsResponseItemsItemTotalSupplyRaw],
        FieldMetadata(alias="totalSupplyRaw"),
        pydantic.Field(alias="totalSupplyRaw"),
    ] = None
    burned_raw: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdMarketsResponseItemsItemBurnedRaw],
        FieldMetadata(alias="burnedRaw"),
        pydantic.Field(alias="burnedRaw"),
    ] = None
    metadata_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metadataReason"), pydantic.Field(alias="metadataReason")
    ] = None
    volume_scope: typing_extensions.Annotated[
        GetChainsChainIdMarketsResponseItemsItemVolumeScope,
        FieldMetadata(alias="volumeScope"),
        pydantic.Field(alias="volumeScope"),
    ]
    price_usd: typing_extensions.Annotated[
        GetChainsChainIdMarketsResponseItemsItemPriceUsd,
        FieldMetadata(alias="priceUsd"),
        pydantic.Field(alias="priceUsd"),
    ]
    market_cap_usd: typing_extensions.Annotated[
        GetChainsChainIdMarketsResponseItemsItemMarketCapUsd,
        FieldMetadata(alias="marketCapUsd"),
        pydantic.Field(alias="marketCapUsd"),
    ]
    volume_usd24h: typing_extensions.Annotated[
        GetChainsChainIdMarketsResponseItemsItemVolumeUsd24H,
        FieldMetadata(alias="volumeUsd24h"),
        pydantic.Field(alias="volumeUsd24h"),
    ]
    swaps24h: typing.Optional[GetChainsChainIdMarketsResponseItemsItemSwaps24H] = None
    transactions24h: typing.Optional[GetChainsChainIdMarketsResponseItemsItemTransactions24H] = None
    holders: GetChainsChainIdMarketsResponseItemsItemHolders
    v3quote_holdings_usd: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdMarketsResponseItemsItemV3QuoteHoldingsUsd],
        FieldMetadata(alias="v3QuoteHoldingsUsd"),
        pydantic.Field(alias="v3QuoteHoldingsUsd"),
    ] = None
    v4one_percent_depth_usd: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdMarketsResponseItemsItemV4OnePercentDepthUsd],
        FieldMetadata(alias="v4OnePercentDepthUsd"),
        pydantic.Field(alias="v4OnePercentDepthUsd"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetChainsChainIdMarketsResponseItemsItem)
