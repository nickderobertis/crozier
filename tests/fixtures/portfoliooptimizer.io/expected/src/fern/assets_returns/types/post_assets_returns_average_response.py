

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_returns_average_response_assets_item import PostAssetsReturnsAverageResponseAssetsItem


class PostAssetsReturnsAverageResponse(UniversalBaseModel):
    assets: typing.List[PostAssetsReturnsAverageResponseAssetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
