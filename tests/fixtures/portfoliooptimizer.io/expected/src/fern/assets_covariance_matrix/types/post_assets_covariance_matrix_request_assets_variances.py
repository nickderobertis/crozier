

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCovarianceMatrixRequestAssetsVariances(UniversalBaseModel):
    assets: int = pydantic.Field()
    """
    The number of assets
    """

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

    assets_variances: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="assetsVariances"),
        pydantic.Field(alias="assetsVariances", description="assetsVariances[i] is the variance of the asset i"),
    ]
    """
    assetsVariances[i] is the variance of the asset i
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
