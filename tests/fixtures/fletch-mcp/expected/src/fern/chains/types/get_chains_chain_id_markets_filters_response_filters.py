

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_filters_response_filters_activity import (
    GetChainsChainIdMarketsFiltersResponseFiltersActivity,
)
from .get_chains_chain_id_markets_filters_response_filters_data import GetChainsChainIdMarketsFiltersResponseFiltersData
from .get_chains_chain_id_markets_filters_response_filters_depth import (
    GetChainsChainIdMarketsFiltersResponseFiltersDepth,
)
from .get_chains_chain_id_markets_filters_response_filters_identity import (
    GetChainsChainIdMarketsFiltersResponseFiltersIdentity,
)
from .get_chains_chain_id_markets_filters_response_filters_kind import GetChainsChainIdMarketsFiltersResponseFiltersKind
from .get_chains_chain_id_markets_filters_response_filters_sort import GetChainsChainIdMarketsFiltersResponseFiltersSort
from .get_chains_chain_id_markets_filters_response_filters_trust import (
    GetChainsChainIdMarketsFiltersResponseFiltersTrust,
)


class GetChainsChainIdMarketsFiltersResponseFilters(UniversalBaseModel):
    kind: GetChainsChainIdMarketsFiltersResponseFiltersKind
    trust: GetChainsChainIdMarketsFiltersResponseFiltersTrust
    sort: GetChainsChainIdMarketsFiltersResponseFiltersSort
    activity: GetChainsChainIdMarketsFiltersResponseFiltersActivity
    data: GetChainsChainIdMarketsFiltersResponseFiltersData
    depth: GetChainsChainIdMarketsFiltersResponseFiltersDepth
    identity: GetChainsChainIdMarketsFiltersResponseFiltersIdentity

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
