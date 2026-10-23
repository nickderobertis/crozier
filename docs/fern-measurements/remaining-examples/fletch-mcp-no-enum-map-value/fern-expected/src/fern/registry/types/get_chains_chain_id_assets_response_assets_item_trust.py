

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_assets_response_assets_item_trust_level import (
    GetChainsChainIdAssetsResponseAssetsItemTrustLevel,
)


class GetChainsChainIdAssetsResponseAssetsItemTrust(UniversalBaseModel):
    """
    Derived from the row: whether bytecode was found and the contract agrees with the listing.
    """

    level: typing.Optional[GetChainsChainIdAssetsResponseAssetsItemTrustLevel] = None
    label: typing.Optional[str] = None
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
