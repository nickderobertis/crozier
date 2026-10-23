

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_filters_response_filters_trust_options_item import (
    GetChainsChainIdMarketsFiltersResponseFiltersTrustOptionsItem,
)


class GetChainsChainIdMarketsFiltersResponseFiltersTrust(UniversalBaseModel):
    label: str
    default: str
    options: typing.List[GetChainsChainIdMarketsFiltersResponseFiltersTrustOptionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
