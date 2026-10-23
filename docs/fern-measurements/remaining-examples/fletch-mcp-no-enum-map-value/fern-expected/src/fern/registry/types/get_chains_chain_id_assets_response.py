

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_assets_response_assets_item import GetChainsChainIdAssetsResponseAssetsItem


class GetChainsChainIdAssetsResponse(UniversalBaseModel):
    assets: typing.Optional[typing.List[GetChainsChainIdAssetsResponseAssetsItem]] = None
    fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The extra blocks a caller may request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
