

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_assets_symbol_pools_response_discovery_item import (
    GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem,
)


class GetChainsChainIdAssetsSymbolPoolsResponse(UniversalBaseModel):
    pools: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    best: typing.Optional[typing.Dict[str, typing.Any]] = None
    discovery: typing.Optional[typing.List[GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem]] = None
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
