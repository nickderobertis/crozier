

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisBetaRequestRiskFreeReturnsPortfoliosItem(UniversalBaseModel):
    portfolio_returns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="portfolioReturns")] = (
        pydantic.Field()
    )
    """
    portfolioReturns[t] is the return of the portfolio at the time t, all the portfolioReturns arrays must have the same length, equal to the length of the benchmarkReturns array
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
