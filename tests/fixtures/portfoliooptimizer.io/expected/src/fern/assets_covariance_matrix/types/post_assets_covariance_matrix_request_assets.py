

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCovarianceMatrixRequestAssets(UniversalBaseModel):
    assets: int = pydantic.Field()
    """
    The number of assets
    """

    assets_correlation_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCorrelationMatrix")
    ] = pydantic.Field()
    """
    assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    """

    assets_volatilities: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="assetsVolatilities")] = (
        pydantic.Field()
    )
    """
    assetsVolatilities[i] is the volatility of the asset i
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
