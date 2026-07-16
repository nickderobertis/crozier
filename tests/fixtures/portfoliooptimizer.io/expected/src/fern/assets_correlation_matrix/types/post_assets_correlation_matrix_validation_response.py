

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_correlation_matrix_validation_response_message import (
    PostAssetsCorrelationMatrixValidationResponseMessage,
)


class PostAssetsCorrelationMatrixValidationResponse(UniversalBaseModel):
    message: PostAssetsCorrelationMatrixValidationResponseMessage = pydantic.Field()
    """
    Indicates whether the matrix is a valid correlation matrix
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
