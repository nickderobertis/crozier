

import typing

from .post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix import (
    PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix,
)
from .post_portfolio_analysis_diversification_ratio_request_one import (
    PostPortfolioAnalysisDiversificationRatioRequestOne,
)

PostPortfolioAnalysisDiversificationRatioRequest = typing.Union[
    PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix,
    PostPortfolioAnalysisDiversificationRatioRequestOne,
]
