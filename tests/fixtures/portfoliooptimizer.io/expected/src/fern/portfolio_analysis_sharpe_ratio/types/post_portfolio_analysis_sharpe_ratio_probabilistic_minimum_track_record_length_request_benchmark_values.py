

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues(UniversalBaseModel):
    benchmark_values: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="benchmarkValues")
    ] = pydantic.Field(default=None)
    """
    benchmarkValues[t] is the value of the benchmark at the time t; the benchmarkValues array must have the same length as all the portfolioValues arrays
    """

    confidence_level: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="confidenceLevel")] = (
        pydantic.Field(default=None)
    )
    """
    The confidence level of the minimum track record length, in percentage
    """

    portfolios: typing.List[
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem
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
