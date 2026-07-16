

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCorrelationMatrixInformativenessResponse(UniversalBaseModel):
    assets_correlation_matrix_informativeness: typing_extensions.Annotated[
        float, FieldMetadata(alias="assetsCorrelationMatrixInformativeness")
    ] = pydantic.Field()
    """
    The informativeness of the asset correlation matrix
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
