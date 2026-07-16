

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_prices_adjusted_response_assets_item import PostAssetsPricesAdjustedResponseAssetsItem


class PostAssetsPricesAdjustedResponse(UniversalBaseModel):
    assets: typing.List[PostAssetsPricesAdjustedResponseAssetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
