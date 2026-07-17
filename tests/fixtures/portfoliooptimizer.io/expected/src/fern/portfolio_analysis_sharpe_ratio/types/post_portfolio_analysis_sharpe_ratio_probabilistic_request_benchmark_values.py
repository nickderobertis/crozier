

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues(UniversalBaseModel):
    benchmark_values: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="benchmarkValues"),
        pydantic.Field(
            alias="benchmarkValues",
            description="benchmarkValues[t] is the value of the benchmark at the time t; the benchmarkValues array must have the same length as all the portfolioValues arrays",
        ),
    ]
    """
    benchmarkValues[t] is the value of the benchmark at the time t; the benchmarkValues array must have the same length as all the portfolioValues arrays
    """

    portfolios: typing.List[PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem]
    risk_free_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="riskFreeRate"),
        pydantic.Field(alias="riskFreeRate", description="The risk free rate"),
    ]
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
