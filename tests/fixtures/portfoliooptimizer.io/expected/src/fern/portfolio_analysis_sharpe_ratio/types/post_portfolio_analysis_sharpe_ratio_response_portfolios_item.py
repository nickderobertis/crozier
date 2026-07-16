

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisSharpeRatioResponsePortfoliosItem(UniversalBaseModel):
    portfolio_sharpe_ratio: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="portfolioSharpeRatio"),
        pydantic.Field(alias="portfolioSharpeRatio", description="The Sharpe ratio of the portfolio"),
    ]
    """
    The Sharpe ratio of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
