

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisSharpeRatioProbabilisticResponsePortfoliosItem(UniversalBaseModel):
    portfolio_probabilistic_sharpe_ratio: typing_extensions.Annotated[
        float, FieldMetadata(alias="portfolioProbabilisticSharpeRatio")
    ] = pydantic.Field()
    """
    The probabilistic Sharpe ratio of the portfolio, in percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
