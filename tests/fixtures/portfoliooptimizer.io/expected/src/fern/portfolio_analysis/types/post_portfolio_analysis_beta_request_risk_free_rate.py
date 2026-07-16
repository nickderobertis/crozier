

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_beta_request_risk_free_rate_portfolios_item import (
    PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem,
)


class PostPortfolioAnalysisBetaRequestRiskFreeRate(UniversalBaseModel):
    benchmark_returns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="benchmarkReturns")] = (
        pydantic.Field()
    )
    """
    benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays
    """

    portfolios: typing.List[PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem]
    risk_free_rate: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="riskFreeRate")] = (
        pydantic.Field(default=None)
    )
    """
    The risk free rate, assumed to be constant for any time t
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
