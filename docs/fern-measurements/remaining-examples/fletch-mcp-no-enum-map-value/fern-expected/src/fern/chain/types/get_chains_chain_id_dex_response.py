

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_dex_response_discovery_item import GetChainsChainIdDexResponseDiscoveryItem
from .get_chains_chain_id_dex_response_venues_item import GetChainsChainIdDexResponseVenuesItem


class GetChainsChainIdDexResponse(UniversalBaseModel):
    venues: typing.Optional[typing.List[GetChainsChainIdDexResponseVenuesItem]] = None
    discovery: typing.Optional[typing.List[GetChainsChainIdDexResponseDiscoveryItem]] = None
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
