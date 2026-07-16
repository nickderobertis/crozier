

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_mean_variance_minimum_variance_frontier_response_portfolios_item import (
    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponsePortfoliosItem,
)


class PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse(UniversalBaseModel):
    portfolios: typing.List[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponsePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
