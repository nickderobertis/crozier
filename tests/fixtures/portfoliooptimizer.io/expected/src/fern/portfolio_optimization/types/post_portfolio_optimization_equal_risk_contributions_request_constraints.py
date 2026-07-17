

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioOptimizationEqualRiskContributionsRequestConstraints(UniversalBaseModel):
    maximum_assets_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[float]],
        FieldMetadata(alias="maximumAssetsWeights"),
        pydantic.Field(
            alias="maximumAssetsWeights",
            description="maximumAssetsWeights[i] is the maximum weight of the asset i in the portfolio, in percentage",
        ),
    ] = None
    """
    maximumAssetsWeights[i] is the maximum weight of the asset i in the portfolio, in percentage
    """

    minimum_assets_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[float]],
        FieldMetadata(alias="minimumAssetsWeights"),
        pydantic.Field(
            alias="minimumAssetsWeights",
            description="minimumAssetsWeights[i] is the minimum weight of the asset i in the portfolio, in percentage",
        ),
    ] = None
    """
    minimumAssetsWeights[i] is the minimum weight of the asset i in the portfolio, in percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
