

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_volatility_request_assets_assets_item import PostAssetsVolatilityRequestAssetsAssetsItem


class PostAssetsVolatilityRequestAssets(UniversalBaseModel):
    assets: typing.List[PostAssetsVolatilityRequestAssetsAssetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
