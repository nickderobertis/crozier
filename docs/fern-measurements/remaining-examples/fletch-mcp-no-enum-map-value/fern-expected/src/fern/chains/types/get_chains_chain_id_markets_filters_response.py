

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_filters_response_filters import GetChainsChainIdMarketsFiltersResponseFilters
from .get_chains_chain_id_markets_filters_response_min_volume_usd import (
    GetChainsChainIdMarketsFiltersResponseMinVolumeUsd,
)
from .get_chains_chain_id_markets_filters_response_presets_item import GetChainsChainIdMarketsFiltersResponsePresetsItem


class GetChainsChainIdMarketsFiltersResponse(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    version: int
    scope: str
    combination: str
    ordering: str
    filters: GetChainsChainIdMarketsFiltersResponseFilters
    min_volume_usd: typing_extensions.Annotated[
        GetChainsChainIdMarketsFiltersResponseMinVolumeUsd,
        FieldMetadata(alias="minVolumeUsd"),
        pydantic.Field(alias="minVolumeUsd"),
    ]
    presets: typing.List[GetChainsChainIdMarketsFiltersResponsePresetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
