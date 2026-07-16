

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_diversification_ratio_request_one_assets_item import (
    PostPortfolioAnalysisDiversificationRatioRequestOneAssetsItem,
)
from .post_portfolio_analysis_diversification_ratio_request_one_portfolios_item import (
    PostPortfolioAnalysisDiversificationRatioRequestOnePortfoliosItem,
)


class PostPortfolioAnalysisDiversificationRatioRequestOne(UniversalBaseModel):
    assets: typing.List[PostPortfolioAnalysisDiversificationRatioRequestOneAssetsItem]
    portfolios: typing.List[PostPortfolioAnalysisDiversificationRatioRequestOnePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
