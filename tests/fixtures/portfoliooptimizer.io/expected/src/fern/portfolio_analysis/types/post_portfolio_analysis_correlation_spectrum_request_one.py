

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_correlation_spectrum_request_one_assets_item import (
    PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem,
)
from .post_portfolio_analysis_correlation_spectrum_request_one_portfolios_item import (
    PostPortfolioAnalysisCorrelationSpectrumRequestOnePortfoliosItem,
)


class PostPortfolioAnalysisCorrelationSpectrumRequestOne(UniversalBaseModel):
    assets: typing.List[PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem]
    portfolios: typing.List[PostPortfolioAnalysisCorrelationSpectrumRequestOnePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
