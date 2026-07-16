

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisReturnsAverageResponsePortfoliosItem(UniversalBaseModel):
    portfolio_average_return: typing_extensions.Annotated[float, FieldMetadata(alias="portfolioAverageReturn")] = (
        pydantic.Field()
    )
    """
    The arithmetic average return of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
