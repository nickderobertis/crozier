

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisSharpeRatioBiasAdjustedResponsePortfoliosItem(UniversalBaseModel):
    portfolio_bias_adjusted_sharpe_ratio: typing_extensions.Annotated[
        float, FieldMetadata(alias="portfolioBiasAdjustedSharpeRatio")
    ] = pydantic.Field()
    """
    The bias-adjusted Sharpe ratio of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
