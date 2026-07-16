

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_tracking_error_response_portfolios_item import (
    PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem,
)


class PostPortfolioAnalysisTrackingErrorResponse(UniversalBaseModel):
    portfolios: typing.List[PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
