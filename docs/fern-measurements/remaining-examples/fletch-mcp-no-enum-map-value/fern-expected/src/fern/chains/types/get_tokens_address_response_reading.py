

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata
from .get_tokens_address_response_reading_alternatives_item import GetTokensAddressResponseReadingAlternativesItem
from .get_tokens_address_response_reading_burned_raw import GetTokensAddressResponseReadingBurnedRaw
from .get_tokens_address_response_reading_decimals import GetTokensAddressResponseReadingDecimals
from .get_tokens_address_response_reading_holders import GetTokensAddressResponseReadingHolders
from .get_tokens_address_response_reading_market_cap_usd import GetTokensAddressResponseReadingMarketCapUsd
from .get_tokens_address_response_reading_price_usd import GetTokensAddressResponseReadingPriceUsd
from .get_tokens_address_response_reading_robinhood_app import GetTokensAddressResponseReadingRobinhoodApp
from .get_tokens_address_response_reading_selection import GetTokensAddressResponseReadingSelection
from .get_tokens_address_response_reading_stock_pairings_item import GetTokensAddressResponseReadingStockPairingsItem
from .get_tokens_address_response_reading_swaps24h import GetTokensAddressResponseReadingSwaps24H
from .get_tokens_address_response_reading_total_supply_raw import GetTokensAddressResponseReadingTotalSupplyRaw
from .get_tokens_address_response_reading_transactions24h import GetTokensAddressResponseReadingTransactions24H
from .get_tokens_address_response_reading_trust import GetTokensAddressResponseReadingTrust
from .get_tokens_address_response_reading_v3quote_holdings_usd import GetTokensAddressResponseReadingV3QuoteHoldingsUsd
from .get_tokens_address_response_reading_v4one_percent_depth_usd import (
    GetTokensAddressResponseReadingV4OnePercentDepthUsd,
)
from .get_tokens_address_response_reading_volume_scope import GetTokensAddressResponseReadingVolumeScope
from .get_tokens_address_response_reading_volume_usd24h import GetTokensAddressResponseReadingVolumeUsd24H


class GetTokensAddressResponseReading(UniversalBaseModel):
    robinhood_app: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseReadingRobinhoodApp],
        FieldMetadata(alias="robinhoodApp"),
        pydantic.Field(alias="robinhoodApp"),
    ] = None
    stock_pairings: typing_extensions.Annotated[
        typing.Optional[typing.List[GetTokensAddressResponseReadingStockPairingsItem]],
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
    trust: GetTokensAddressResponseReadingTrust
    selection: GetTokensAddressResponseReadingSelection = pydantic.Field()
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
    alternatives: typing.List[GetTokensAddressResponseReadingAlternativesItem]
    best_pool_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bestPoolId"), pydantic.Field(alias="bestPoolId")
    ] = None
    pool_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="poolCount"), pydantic.Field(alias="poolCount")
    ] = None
    decimals: typing.Optional[GetTokensAddressResponseReadingDecimals] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseReadingTotalSupplyRaw],
        FieldMetadata(alias="totalSupplyRaw"),
        pydantic.Field(alias="totalSupplyRaw"),
    ] = None
    burned_raw: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseReadingBurnedRaw],
        FieldMetadata(alias="burnedRaw"),
        pydantic.Field(alias="burnedRaw"),
    ] = None
    metadata_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metadataReason"), pydantic.Field(alias="metadataReason")
    ] = None
    volume_scope: typing_extensions.Annotated[
        GetTokensAddressResponseReadingVolumeScope,
        FieldMetadata(alias="volumeScope"),
        pydantic.Field(alias="volumeScope"),
    ]
    price_usd: typing_extensions.Annotated[
        GetTokensAddressResponseReadingPriceUsd, FieldMetadata(alias="priceUsd"), pydantic.Field(alias="priceUsd")
    ]
    market_cap_usd: typing_extensions.Annotated[
        GetTokensAddressResponseReadingMarketCapUsd,
        FieldMetadata(alias="marketCapUsd"),
        pydantic.Field(alias="marketCapUsd"),
    ]
    volume_usd24h: typing_extensions.Annotated[
        GetTokensAddressResponseReadingVolumeUsd24H,
        FieldMetadata(alias="volumeUsd24h"),
        pydantic.Field(alias="volumeUsd24h"),
    ]
    swaps24h: typing.Optional[GetTokensAddressResponseReadingSwaps24H] = None
    transactions24h: typing.Optional[GetTokensAddressResponseReadingTransactions24H] = None
    holders: GetTokensAddressResponseReadingHolders
    v3quote_holdings_usd: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseReadingV3QuoteHoldingsUsd],
        FieldMetadata(alias="v3QuoteHoldingsUsd"),
        pydantic.Field(alias="v3QuoteHoldingsUsd"),
    ] = None
    v4one_percent_depth_usd: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseReadingV4OnePercentDepthUsd],
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


update_forward_refs(GetTokensAddressResponseReading)
