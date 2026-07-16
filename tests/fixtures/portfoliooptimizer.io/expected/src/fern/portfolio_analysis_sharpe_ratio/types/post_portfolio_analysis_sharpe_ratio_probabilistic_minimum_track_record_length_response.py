

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse(UniversalBaseModel):
    portfolios: typing.List[PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
