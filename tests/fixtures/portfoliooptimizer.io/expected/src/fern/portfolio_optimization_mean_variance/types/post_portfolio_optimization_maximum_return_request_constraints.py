

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioOptimizationMaximumReturnRequestConstraints(UniversalBaseModel):
    assets_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[int]]], FieldMetadata(alias="assetsGroups")
    ] = None
    assets_groups_matrix: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[float]]], FieldMetadata(alias="assetsGroupsMatrix")
    ] = pydantic.Field(default=None)
    """
    assetsGroupsMatrix[k][i] is the weight of the asset i in the group of assets k; exclusive with assetsGroups
    """

    maximum_assets_groups_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="maximumAssetsGroupsWeights")
    ] = pydantic.Field(default=None)
    """
    maximumAssetsGroupsWeights[k] is the maximum weight of the assets group k in the portfolio, in percentage between 0 and 1 if assetsGroups is provided
    """

    maximum_assets_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="maximumAssetsWeights")
    ] = pydantic.Field(default=None)
    """
    maximumAssetsWeights[i] is the maximum weight of the asset i in the portfolio, in percentage
    """

    maximum_portfolio_exposure: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maximumPortfolioExposure")
    ] = pydantic.Field(default=None)
    """
    The maximum portfolio exposure; must be higher than or equal to minimumPortfolioExposure
    """

    minimum_assets_weights: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="minimumAssetsWeights")
    ] = pydantic.Field(default=None)
    """
    minimumAssetsWeights[i] is the minimum weight of the asset i in the portfolio, in percentage
    """

    minimum_portfolio_exposure: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minimumPortfolioExposure")
    ] = pydantic.Field(default=None)
    """
    The minimum portfolio exposure; must be lower than or equal to maximumPortfolioExposure
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
