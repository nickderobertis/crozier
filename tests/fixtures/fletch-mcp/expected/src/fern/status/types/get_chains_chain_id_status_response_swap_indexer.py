

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_status_response_swap_indexer_coverage_scope import (
    GetChainsChainIdStatusResponseSwapIndexerCoverageScope,
)
from .get_chains_chain_id_status_response_swap_indexer_mode import GetChainsChainIdStatusResponseSwapIndexerMode
from .get_chains_chain_id_status_response_swap_indexer_tiers_item import (
    GetChainsChainIdStatusResponseSwapIndexerTiersItem,
)
from .get_chains_chain_id_status_response_swap_indexer_tiers_scope import (
    GetChainsChainIdStatusResponseSwapIndexerTiersScope,
)
from .get_chains_chain_id_status_response_swap_indexer_valuation_methods_item import (
    GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem,
)


class GetChainsChainIdStatusResponseSwapIndexer(UniversalBaseModel):
    """
    Live swap tail and separate backwards backfill. Coverage is measured independently of daemon health. USDG uses a disclosed nominal dollar assumption; supported WETH windows use explicitly estimated historical oracle samples. Inspect valuation methods and valued-pool coverage.
    """

    mode: GetChainsChainIdStatusResponseSwapIndexerMode
    checked_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="checkedAt"), pydantic.Field(alias="checkedAt")
    ]
    newest_counted_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newestCountedBlock"), pydantic.Field(alias="newestCountedBlock")
    ] = None
    newest_counted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="newestCountedAt"), pydantic.Field(alias="newestCountedAt")
    ] = None
    head_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headBlock"), pydantic.Field(alias="headBlock")
    ] = None
    head_read_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="headReadAt"), pydantic.Field(alias="headReadAt")
    ] = None
    lag_blocks: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lagBlocks"), pydantic.Field(alias="lagBlocks")
    ] = None
    lag_seconds: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lagSeconds"),
        pydantic.Field(
            alias="lagSeconds",
            description="Wall-clock age of the newest indexed block, independent of assumed block cadence.",
        ),
    ] = None
    """
    Wall-clock age of the newest indexed block, independent of assumed block cadence.
    """

    window_start_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="windowStartAt"), pydantic.Field(alias="windowStartAt")
    ] = None
    window_end_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="windowEndAt"), pydantic.Field(alias="windowEndAt")
    ] = None
    current: bool = pydantic.Field()
    """
    The indexed boundary is at most 120 seconds old; individual pools also require complete coverage.
    """

    historical_usd_available: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="historicalUsdAvailable"),
        pydantic.Field(
            alias="historicalUsdAvailable",
            description="True when complete current indexed pools include historical quote valuations; does not claim all pools are covered.",
        ),
    ]
    """
    True when complete current indexed pools include historical quote valuations; does not claim all pools are covered.
    """

    coverage_scope: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdStatusResponseSwapIndexerCoverageScope],
        FieldMetadata(alias="coverageScope"),
        pydantic.Field(alias="coverageScope"),
    ] = None
    tiers_scope: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdStatusResponseSwapIndexerTiersScope],
        FieldMetadata(alias="tiersScope"),
        pydantic.Field(alias="tiersScope"),
    ] = None
    priority_pool_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="priorityPoolCount"), pydantic.Field(alias="priorityPoolCount")
    ] = None
    priority_complete24h_pools: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="priorityComplete24hPools"),
        pydantic.Field(alias="priorityComplete24hPools"),
    ] = None
    priority_valued24h_pools: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="priorityValued24hPools"),
        pydantic.Field(alias="priorityValued24hPools"),
    ] = None
    valuation_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem]],
        FieldMetadata(alias="valuationMethods"),
        pydantic.Field(alias="valuationMethods"),
    ] = None
    tiers: typing.List[GetChainsChainIdStatusResponseSwapIndexerTiersItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
