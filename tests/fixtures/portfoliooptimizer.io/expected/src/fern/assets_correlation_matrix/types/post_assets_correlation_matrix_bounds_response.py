

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCorrelationMatrixBoundsResponse(UniversalBaseModel):
    assets_correlation_matrix_lower_bounds: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCorrelationMatrixLowerBounds")
    ] = pydantic.Field()
    """
    assetsCorrelationMatrixLowerBounds[i][j] is the lower bound of the correlation between the asset i and the asset j
    """

    assets_correlation_matrix_upper_bounds: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCorrelationMatrixUpperBounds")
    ] = pydantic.Field()
    """
    assetsCorrelationMatrixUpperBounds[i][j] is the upper bound of the correlation between the asset i and the asset j
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
