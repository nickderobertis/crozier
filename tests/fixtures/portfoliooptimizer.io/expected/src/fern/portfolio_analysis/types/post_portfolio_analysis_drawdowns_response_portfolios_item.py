

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_drawdowns_response_portfolios_item_portfolio_worst_drawdowns_item import (
    PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem,
)


class PostPortfolioAnalysisDrawdownsResponsePortfoliosItem(UniversalBaseModel):
    portfolio_drawdowns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="portfolioDrawdowns")] = (
        pydantic.Field()
    )
    """
    portfolioDrawdowns[t] is the value of the drawdown function at the time t
    """

    portfolio_worst_drawdowns: typing_extensions.Annotated[
        typing.List[PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem],
        FieldMetadata(alias="portfolioWorstDrawdowns"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
