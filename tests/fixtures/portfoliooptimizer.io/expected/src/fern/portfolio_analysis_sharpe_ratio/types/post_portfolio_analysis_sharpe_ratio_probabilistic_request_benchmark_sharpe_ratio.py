

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatioPortfoliosItem,
)


class PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatio(UniversalBaseModel):
    benchmark_sharpe_ratio: typing_extensions.Annotated[float, FieldMetadata(alias="benchmarkSharpeRatio")] = (
        pydantic.Field()
    )
    """
    The Sharpe ratio of the benchmark, in the same sampling frequency as the sampling frequency of the portfolio values
    """

    portfolios: typing.List[PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatioPortfoliosItem]
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
