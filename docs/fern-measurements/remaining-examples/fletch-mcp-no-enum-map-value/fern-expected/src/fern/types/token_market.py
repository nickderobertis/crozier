

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .token_market_alternatives_item import TokenMarketAlternativesItem
from .token_market_burned_raw import TokenMarketBurnedRaw
from .token_market_decimals import TokenMarketDecimals
from .token_market_holders import TokenMarketHolders
from .token_market_market_cap_usd import TokenMarketMarketCapUsd
from .token_market_price_usd import TokenMarketPriceUsd
from .token_market_robinhood_app import TokenMarketRobinhoodApp
from .token_market_selection import TokenMarketSelection
from .token_market_stock_pairings_item import TokenMarketStockPairingsItem
from .token_market_swaps24h import TokenMarketSwaps24H
from .token_market_total_supply_raw import TokenMarketTotalSupplyRaw
from .token_market_transactions24h import TokenMarketTransactions24H
from .token_market_trust import TokenMarketTrust
from .token_market_v3quote_holdings_usd import TokenMarketV3QuoteHoldingsUsd
from .token_market_v4one_percent_depth_usd import TokenMarketV4OnePercentDepthUsd
from .token_market_volume_scope import TokenMarketVolumeScope
from .token_market_volume_usd24h import TokenMarketVolumeUsd24H


class TokenMarket(UniversalBaseModel):
    robinhood_app: typing_extensions.Annotated[
        typing.Optional[TokenMarketRobinhoodApp],
        FieldMetadata(alias="robinhoodApp"),
        pydantic.Field(alias="robinhoodApp"),
    ] = None
    stock_pairings: typing_extensions.Annotated[
        typing.Optional[typing.List[TokenMarketStockPairingsItem]],
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
    trust: TokenMarketTrust
    selection: TokenMarketSelection = pydantic.Field()
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
    alternatives: typing.List[TokenMarketAlternativesItem]
    best_pool_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bestPoolId"), pydantic.Field(alias="bestPoolId")
    ] = None
    pool_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="poolCount"), pydantic.Field(alias="poolCount")
    ] = None
    decimals: typing.Optional[TokenMarketDecimals] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[TokenMarketTotalSupplyRaw],
        FieldMetadata(alias="totalSupplyRaw"),
        pydantic.Field(alias="totalSupplyRaw"),
    ] = None
    burned_raw: typing_extensions.Annotated[
        typing.Optional[TokenMarketBurnedRaw], FieldMetadata(alias="burnedRaw"), pydantic.Field(alias="burnedRaw")
    ] = None
    metadata_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metadataReason"), pydantic.Field(alias="metadataReason")
    ] = None
    volume_scope: typing_extensions.Annotated[
        TokenMarketVolumeScope, FieldMetadata(alias="volumeScope"), pydantic.Field(alias="volumeScope")
    ]
    price_usd: typing_extensions.Annotated[
        TokenMarketPriceUsd, FieldMetadata(alias="priceUsd"), pydantic.Field(alias="priceUsd")
    ]
    market_cap_usd: typing_extensions.Annotated[
        TokenMarketMarketCapUsd, FieldMetadata(alias="marketCapUsd"), pydantic.Field(alias="marketCapUsd")
    ]
    volume_usd24h: typing_extensions.Annotated[
        TokenMarketVolumeUsd24H, FieldMetadata(alias="volumeUsd24h"), pydantic.Field(alias="volumeUsd24h")
    ]
    swaps24h: typing.Optional[TokenMarketSwaps24H] = None
    transactions24h: typing.Optional[TokenMarketTransactions24H] = None
    holders: TokenMarketHolders
    v3quote_holdings_usd: typing_extensions.Annotated[
        typing.Optional[TokenMarketV3QuoteHoldingsUsd],
        FieldMetadata(alias="v3QuoteHoldingsUsd"),
        pydantic.Field(alias="v3QuoteHoldingsUsd"),
    ] = None
    v4one_percent_depth_usd: typing_extensions.Annotated[
        typing.Optional[TokenMarketV4OnePercentDepthUsd],
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


update_forward_refs(TokenMarket)
