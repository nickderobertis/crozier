

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix(UniversalBaseModel):
    assets: int
    assets_correlation_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCorrelationMatrix")
    ] = pydantic.Field()
    """
    assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    """

    shrinkage_factor: typing_extensions.Annotated[float, FieldMetadata(alias="shrinkageFactor")]
    target_correlation_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="targetCorrelationMatrix")
    ] = pydantic.Field()
    """
    targetCorrelationMatrix[i][j] is the target correlation between the asset i and the asset j
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
