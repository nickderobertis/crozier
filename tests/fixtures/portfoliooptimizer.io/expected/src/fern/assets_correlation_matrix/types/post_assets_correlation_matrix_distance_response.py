

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCorrelationMatrixDistanceResponse(UniversalBaseModel):
    assets_correlation_matrix_distance: typing_extensions.Annotated[
        float, FieldMetadata(alias="assetsCorrelationMatrixDistance")
    ] = pydantic.Field()
    """
    The computed distance between the two correlation matrices
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
