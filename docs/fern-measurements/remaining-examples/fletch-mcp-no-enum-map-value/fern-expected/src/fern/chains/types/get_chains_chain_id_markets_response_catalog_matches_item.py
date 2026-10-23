

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_markets_response_catalog_matches_item_status import (
    GetChainsChainIdMarketsResponseCatalogMatchesItemStatus,
)


class GetChainsChainIdMarketsResponseCatalogMatchesItem(UniversalBaseModel):
    symbol: str
    name: str
    status: GetChainsChainIdMarketsResponseCatalogMatchesItemStatus
    addresses: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
