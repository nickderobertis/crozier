

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCovarianceMatrixExponentiallyWeightedResponse(UniversalBaseModel):
    assets_covariance_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCovarianceMatrix")
    ] = pydantic.Field()
    """
    assetsCovarianceMatrix[i][j] is the sample covariance between the asset i returns and the asset j returns
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
