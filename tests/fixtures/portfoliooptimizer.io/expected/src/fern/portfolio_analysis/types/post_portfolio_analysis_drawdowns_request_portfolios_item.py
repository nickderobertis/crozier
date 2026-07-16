

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisDrawdownsRequestPortfoliosItem(UniversalBaseModel):
    portfolio_values: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="portfolioValues")] = (
        pydantic.Field()
    )
    """
    portfolioValues[t] is the value of the portfolio at the time t
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
