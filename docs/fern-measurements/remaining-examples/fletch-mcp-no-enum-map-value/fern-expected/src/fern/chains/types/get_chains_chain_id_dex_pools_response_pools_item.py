

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_dex_pools_response_pools_item_depth_measure import (
    GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure,
)
from .get_chains_chain_id_dex_pools_response_pools_item_kind import GetChainsChainIdDexPoolsResponsePoolsItemKind
from .get_chains_chain_id_dex_pools_response_pools_item_listing import GetChainsChainIdDexPoolsResponsePoolsItemListing
from .get_chains_chain_id_dex_pools_response_pools_item_quote_observation import (
    GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation,
)
from .get_chains_chain_id_dex_pools_response_pools_item_tier import GetChainsChainIdDexPoolsResponsePoolsItemTier
from .get_chains_chain_id_dex_pools_response_pools_item_token import GetChainsChainIdDexPoolsResponsePoolsItemToken
from .get_chains_chain_id_dex_pools_response_pools_item_trust import GetChainsChainIdDexPoolsResponsePoolsItemTrust
from .get_chains_chain_id_dex_pools_response_pools_item_venue import GetChainsChainIdDexPoolsResponsePoolsItemVenue


class GetChainsChainIdDexPoolsResponsePoolsItem(UniversalBaseModel):
    pool_id: typing_extensions.Annotated[str, FieldMetadata(alias="poolId"), pydantic.Field(alias="poolId")]
    venue: GetChainsChainIdDexPoolsResponsePoolsItemVenue
    kind: GetChainsChainIdDexPoolsResponsePoolsItemKind = pydantic.Field()
    """
    Alias of trust for the priced token. Listing membership is separate.
    """

    trust: typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemTrust] = None
    trust_detail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="trustDetail"), pydantic.Field(alias="trustDetail")
    ] = None
    token_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tokenAddress"), pydantic.Field(alias="tokenAddress")
    ] = None
    listing: typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemListing] = None
    depth_measure: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure],
        FieldMetadata(alias="depthMeasure"),
        pydantic.Field(alias="depthMeasure"),
    ] = None
    depth_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="depthSource"), pydantic.Field(alias="depthSource")
    ] = None
    quote_observation: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation],
        FieldMetadata(alias="quoteObservation"),
        pydantic.Field(
            alias="quoteObservation",
            description="Quote conversion captured with the pool snapshot. Null for older observations. A fixed USDG notional assumption has no oracle source timestamp.",
        ),
    ] = None
    """
    Quote conversion captured with the pool snapshot. Null for older observations. A fixed USDG notional assumption has no oracle source timestamp.
    """

    tier: typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemTier] = pydantic.Field(default=None)
    """
    Active pools are prioritized for background sampling; quiet pools receive a daily cycle; dormant pools receive demand-driven reads. Scheduling does not establish freshness: inspect stateCheckedAt and stateCurrent.
    """

    last_swap_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastSwapAt"), pydantic.Field(alias="lastSwapAt")
    ] = None
    pool_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="poolAddress"), pydantic.Field(alias="poolAddress")
    ] = None
    currency0: str
    currency1: str
    fee: int
    fee_dynamic: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="feeDynamic"), pydantic.Field(alias="feeDynamic")
    ] = None
    fee_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="feePct"), pydantic.Field(alias="feePct")
    ] = None
    tick_spacing: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tickSpacing"), pydantic.Field(alias="tickSpacing")
    ] = None
    hooks: typing.Optional[str] = None
    asset: typing.Optional[str] = pydantic.Field(default=None)
    """
    The listed asset's ticker; null for a community pool.
    """

    token: typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemToken] = pydantic.Field(default=None)
    """
    The unlisted side of a community pool, as its own contract describes it. Nothing here is verified.
    """

    quote: typing.Optional[str] = None
    created_block: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdBlock"), pydantic.Field(alias="createdBlock")
    ]
    sqrt_price_x96: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sqrtPriceX96"), pydantic.Field(alias="sqrtPriceX96")
    ] = None
    tick: typing.Optional[int] = None
    liquidity: typing.Optional[str] = None
    depth_usd: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="depthUsd"),
        pydantic.Field(
            alias="depthUsd",
            description="Depth in USD uses observed quote-side holdings for v3. For v4 it uses a bounded quote estimate for a 1% price move; per-pool token reserves are unavailable. Check the pool's observation time and stateCurrent flag.",
        ),
    ] = None
    """
    Depth in USD uses observed quote-side holdings for v3. For v4 it uses a bounded quote estimate for a 1% price move; per-pool token reserves are unavailable. Check the pool's observation time and stateCurrent flag.
    """

    price_in_quote: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceInQuote"), pydantic.Field(alias="priceInQuote")
    ] = None
    price_usd: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceUsd"), pydantic.Field(alias="priceUsd")
    ] = None
    swaps24h: typing.Optional[int] = None
    transactions24h: typing.Optional[int] = pydantic.Field(default=None)
    """
    Distinct transactions in the exact indexed 24-hour window.
    """

    metrics_as_of: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="metricsAsOf"),
        pydantic.Field(
            alias="metricsAsOf", description="End of the indexed 24-hour window; metrics expire after 120 seconds."
        ),
    ] = None
    """
    End of the indexed 24-hour window; metrics expire after 120 seconds.
    """

    metrics_window_start_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="metricsWindowStartAt"),
        pydantic.Field(alias="metricsWindowStartAt"),
    ] = None
    metrics_coverage_complete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="metricsCoverageComplete"),
        pydantic.Field(alias="metricsCoverageComplete"),
    ] = None
    metrics_current: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="metricsCurrent"), pydantic.Field(alias="metricsCurrent")
    ] = None
    volume0raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="volume0Raw"),
        pydantic.Field(
            alias="volume0Raw",
            description="Sum of absolute currency0 swap amounts in base units, only for a complete current window.",
        ),
    ] = None
    """
    Sum of absolute currency0 swap amounts in base units, only for a complete current window.
    """

    volume1raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="volume1Raw"),
        pydantic.Field(
            alias="volume1Raw",
            description="Sum of absolute currency1 swap amounts in base units. Separate from currency0; the legs are never added together.",
        ),
    ] = None
    """
    Sum of absolute currency1 swap amounts in base units. Separate from currency0; the legs are never added together.
    """

    volume_usd24h: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="volumeUsd24h"), pydantic.Field(alias="volumeUsd24h")
    ] = None
    volume_valuation: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="volumeValuation"),
        pydantic.Field(
            alias="volumeValuation",
            description="Historical quote method, source and missing-value reason. USDG is nominal denomination; WETH uses a bounded-age historical oracle estimate.",
        ),
    ] = None
    """
    Historical quote method, source and missing-value reason. USDG is nominal denomination; WETH uses a bounded-age historical oracle estimate.
    """

    state_checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="stateCheckedAt"), pydantic.Field(alias="stateCheckedAt")
    ] = None
    state_current: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="stateCurrent"),
        pydantic.Field(
            alias="stateCurrent",
            description="The pool state was observed within three minutes, its timestamp is not in the future, and its captured quote conversion has not expired. When false, depth, price, FDV and price changes are null; stateCheckedAt retains the actual observation time.",
        ),
    ]
    """
    The pool state was observed within three minutes, its timestamp is not in the future, and its captured quote conversion has not expired. When false, depth, price, FDV and price changes are null; stateCheckedAt retains the actual observation time.
    """

    price_published: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="pricePublished"),
        pydantic.Field(
            alias="pricePublished",
            description="Current state has a finite positive price and clears the configured depth floor.",
        ),
    ]
    """
    Current state has a finite positive price and clears the configured depth floor.
    """

    change5m_pct: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="change5mPct"),
        pydantic.Field(
            alias="change5mPct",
            description="Dollar price against the newest sample at or before five minutes ago; null when no sample is old enough.",
        ),
    ] = None
    """
    Dollar price against the newest sample at or before five minutes ago; null when no sample is old enough.
    """

    change1h_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="change1hPct"), pydantic.Field(alias="change1hPct")
    ] = None
    change6h_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="change6hPct"), pydantic.Field(alias="change6hPct")
    ] = None
    change24h_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="change24hPct"), pydantic.Field(alias="change24hPct")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
