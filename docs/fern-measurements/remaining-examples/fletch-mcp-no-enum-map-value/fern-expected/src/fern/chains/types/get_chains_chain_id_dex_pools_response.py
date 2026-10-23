

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_dex_pools_response_discovery_item import GetChainsChainIdDexPoolsResponseDiscoveryItem
from .get_chains_chain_id_dex_pools_response_pools_item import GetChainsChainIdDexPoolsResponsePoolsItem


class GetChainsChainIdDexPoolsResponse(UniversalBaseModel):
    pools: typing.List[GetChainsChainIdDexPoolsResponsePoolsItem]
    total: int
    limit: int
    offset: int
    kind: typing.Optional[str] = None
    tier: typing.Optional[str] = None
    sort: typing.Optional[str] = None
    venue: typing.Optional[str] = None
    q: typing.Optional[str] = None
    discovery: typing.List[GetChainsChainIdDexPoolsResponseDiscoveryItem]
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
