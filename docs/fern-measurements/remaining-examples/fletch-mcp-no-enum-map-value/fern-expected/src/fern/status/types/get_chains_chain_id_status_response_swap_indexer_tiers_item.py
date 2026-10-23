

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_status_response_swap_indexer_tiers_item_tier import (
    GetChainsChainIdStatusResponseSwapIndexerTiersItemTier,
)


class GetChainsChainIdStatusResponseSwapIndexerTiersItem(UniversalBaseModel):
    tier: GetChainsChainIdStatusResponseSwapIndexerTiersItemTier
    total_pools: typing_extensions.Annotated[int, FieldMetadata(alias="totalPools"), pydantic.Field(alias="totalPools")]
    enrolled_pools: typing_extensions.Annotated[
        int, FieldMetadata(alias="enrolledPools"), pydantic.Field(alias="enrolledPools")
    ]
    complete24h_pools: typing_extensions.Annotated[
        int, FieldMetadata(alias="complete24hPools"), pydantic.Field(alias="complete24hPools")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
