

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix_portfolios_item import (
    PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem,
)


class PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix(UniversalBaseModel):
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

    portfolios: typing.List[PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
