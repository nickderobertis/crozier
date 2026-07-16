

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatioPortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatio(
    UniversalBaseModel
):
    benchmark_sharpe_ratio: typing_extensions.Annotated[float, FieldMetadata(alias="benchmarkSharpeRatio")] = (
        pydantic.Field()
    )
    """
    The Sharpe ratio of the benchmark, in the same sampling frequency as the sampling frequency of the portfolio values
    """

    confidence_level: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="confidenceLevel")] = (
        pydantic.Field(default=None)
    )
    """
    The confidence level of the minimum track record length, in percentage
    """

    portfolios: typing.List[
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatioPortfoliosItem
    ]
    risk_free_rate: typing_extensions.Annotated[float, FieldMetadata(alias="riskFreeRate")] = pydantic.Field()
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
