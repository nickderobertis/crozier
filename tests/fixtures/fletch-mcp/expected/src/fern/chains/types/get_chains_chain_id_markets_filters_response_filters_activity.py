

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_filters_response_filters_activity_options_item import (
    GetChainsChainIdMarketsFiltersResponseFiltersActivityOptionsItem,
)


class GetChainsChainIdMarketsFiltersResponseFiltersActivity(UniversalBaseModel):
    label: str
    default: str
    options: typing.List[GetChainsChainIdMarketsFiltersResponseFiltersActivityOptionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
