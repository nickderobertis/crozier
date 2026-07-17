

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix_target_equicorrelation_matrix import (
    PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix,
)


class PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix(UniversalBaseModel):
    assets: int
    assets_correlation_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]],
        FieldMetadata(alias="assetsCorrelationMatrix"),
        pydantic.Field(
            alias="assetsCorrelationMatrix",
            description="assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j",
        ),
    ]
    """
    assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    """

    shrinkage_factor: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="shrinkageFactor"),
        pydantic.Field(alias="shrinkageFactor", description="The shrinkage factor"),
    ]
    """
    The shrinkage factor
    """

    target_equicorrelation_matrix: typing_extensions.Annotated[
        PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix,
        FieldMetadata(alias="targetEquicorrelationMatrix"),
        pydantic.Field(alias="targetEquicorrelationMatrix", description="The shrinkage target correlation matrix"),
    ]
    """
    The shrinkage target correlation matrix
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
