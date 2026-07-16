

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_covariance_matrix_request_zero_assets_item import PostAssetsCovarianceMatrixRequestZeroAssetsItem


class PostAssetsCovarianceMatrixRequestZero(UniversalBaseModel):
    assets: typing.List[PostAssetsCovarianceMatrixRequestZeroAssetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
