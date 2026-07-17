

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_alpha_request_risk_free_returns_portfolios_item import (
    PostPortfolioAnalysisAlphaRequestRiskFreeReturnsPortfoliosItem,
)


class PostPortfolioAnalysisAlphaRequestRiskFreeReturns(UniversalBaseModel):
    benchmark_returns: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="benchmarkReturns"),
        pydantic.Field(
            alias="benchmarkReturns",
            description="benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays",
        ),
    ]
    """
    benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays
    """

    portfolios: typing.List[PostPortfolioAnalysisAlphaRequestRiskFreeReturnsPortfoliosItem]
    risk_free_returns: typing_extensions.Annotated[
        typing.Optional[typing.List[float]],
        FieldMetadata(alias="riskFreeReturns"),
        pydantic.Field(
            alias="riskFreeReturns",
            description="riskFreeReturns[t] is the risk free return at the time t; the riskFreeReturns array must have the same length as all the portfolioReturns arrays",
        ),
    ] = None
    """
    riskFreeReturns[t] is the risk free return at the time t; the riskFreeReturns array must have the same length as all the portfolioReturns arrays
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
