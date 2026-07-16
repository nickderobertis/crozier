

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_correlation_spectrum_response_portfolios_item import (
    PostPortfolioAnalysisCorrelationSpectrumResponsePortfoliosItem,
)


class PostPortfolioAnalysisCorrelationSpectrumResponse(UniversalBaseModel):
    portfolios: typing.List[PostPortfolioAnalysisCorrelationSpectrumResponsePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
