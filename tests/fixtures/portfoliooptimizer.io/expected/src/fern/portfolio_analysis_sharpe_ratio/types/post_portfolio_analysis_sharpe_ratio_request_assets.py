

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_sharpe_ratio_request_assets_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioRequestAssets(UniversalBaseModel):
    assets: int = pydantic.Field()
    """
    The number of assets
    """

    assets_covariance_matrix: typing_extensions.Annotated[
        typing.List[typing.List[float]],
        FieldMetadata(alias="assetsCovarianceMatrix"),
        pydantic.Field(
            alias="assetsCovarianceMatrix",
            description="assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j",
        ),
    ]
    """
    assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    """

    assets_returns: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="assetsReturns"),
        pydantic.Field(alias="assetsReturns", description="assetsReturns[i] is the arithmetic return of asset i"),
    ]
    """
    assetsReturns[i] is the arithmetic return of asset i
    """

    portfolios: typing.List[PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem]
    risk_free_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="riskFreeRate"),
        pydantic.Field(alias="riskFreeRate", description="The risk free rate"),
    ]
    """
    The risk free rate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
